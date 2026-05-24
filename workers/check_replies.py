#!/usr/bin/env python3
"""
check_replies.py — Fast Mixmax reply checker.
Scans all 3 live sequences for new replies. Prints results + posts to Slack if any found.
Run any time: python3 workers/check_replies.py
Designed for daily use during the 72-hour post-Touch 3 reply window.
"""

import json
import os
import sys
import urllib.request
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.resolve()
LOG_FILE  = BASE_DIR / 'logs' / 'activity.log'

sys.path.insert(0, str(BASE_DIR))


def _load_env():
    env_file = BASE_DIR / '.env'
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                k, v = line.split('=', 1)
                os.environ.setdefault(k.strip(), v.strip())


_load_env()

MIXMAX_TOKEN  = os.environ.get('MIXMAX_TOKEN', '')
SLACK_WEBHOOK = os.environ.get('SLACK_WEBHOOK_OFFICE', '')

_DISPLAY_NAMES = {
    'property_manager': 'Property Managers',
    'realtor': 'Realtors',
    'contractor': 'Contractors',
    'gas_station': 'Gas Stations',
    'fleet_washing': 'Fleet Washing',
}


def _load_sequences():
    """Import live sequences from mixmax.py — auto-includes gas/fleet when they go live."""
    try:
        from integrations.mixmax import SEQUENCES as MX_SEQS, _sequence_is_live
        return {
            meta['id']: _DISPLAY_NAMES.get(seq_type, seq_type.replace('_', ' ').title())
            for seq_type, meta in MX_SEQS.items()
            if _sequence_is_live(seq_type)
        }
    except Exception:
        return {
            '6a048cfc110bc620ca0f1aee': 'Property Managers',
            '6a048cfba81429e5dfe55010': 'Realtors',
            '6a048cfd624a5989a68ba16c': 'Contractors',
        }


SEQUENCES = _load_sequences()


def _load_phone_map() -> dict:
    """Build email → phone from contacts cache + pipeline_data (manual contacts)."""
    result = {}
    for src_file, contacts_key in [
        (BASE_DIR / 'contacts_cache.json', 'contacts'),
        (BASE_DIR / 'pipeline_data.json', 'manual_contacts'),
    ]:
        if not src_file.exists():
            continue
        try:
            data = json.loads(src_file.read_text())
            for c in data.get(contacts_key, []):
                email = c.get('email', '').lower()
                phone = c.get('phone', '')
                if email and phone and email not in result:
                    result[email] = phone
        except Exception:
            pass
    return result


def _load_company_map() -> dict:
    """Build email → company_name from contacts cache + pipeline_data (manual contacts)."""
    result = {}
    for src_file, contacts_key in [
        (BASE_DIR / 'contacts_cache.json', 'contacts'),
        (BASE_DIR / 'pipeline_data.json', 'manual_contacts'),
    ]:
        if not src_file.exists():
            continue
        try:
            data = json.loads(src_file.read_text())
            for c in data.get(contacts_key, []):
                email = c.get('email', '').lower()
                company = c.get('company_name', '') or c.get('company', '')
                if email and company and email not in result:
                    result[email] = company
        except Exception:
            pass
    return result



def fetch_recipients(seq_id: str) -> list:
    url = f'https://api.mixmax.com/v1/sequences/{seq_id}/recipients?apiToken={MIXMAX_TOKEN}&limit=200'
    try:
        with urllib.request.urlopen(url, timeout=10) as resp:
            data = json.loads(resp.read())
        if isinstance(data, list):
            return data
        return data.get('results', data.get('recipients', []))
    except Exception as e:
        print(f'  ⚠️  {seq_id[:8]}... — {e}')
        return []


def post_slack(msg: str):
    if not SLACK_WEBHOOK:
        return
    try:
        payload = json.dumps({'text': msg}).encode()
        req = urllib.request.Request(
            SLACK_WEBHOOK, payload, {'Content-Type': 'application/json'}
        )
        urllib.request.urlopen(req, timeout=8)
    except Exception:
        pass


def log(msg: str):
    ts = datetime.now().strftime('%Y-%m-%d %H:%M')
    LOG_FILE.parent.mkdir(exist_ok=True)
    with open(LOG_FILE, 'a') as f:
        f.write(f'[{ts}] Nina | check_replies — {msg}\n')


def main():
    print(f'\n🔎 Mixmax Reply Check — {datetime.now().strftime("%Y-%m-%d %H:%M")}')
    print('=' * 50)

    all_replies   = []
    all_hot       = []
    api_ok        = False
    phone_map     = _load_phone_map()
    company_map   = _load_company_map()

    for seq_id, seq_name in SEQUENCES.items():
        recipients = fetch_recipients(seq_id)
        if not recipients:
            print(f'  {seq_name}: no data (API blocked or empty)')
            continue

        api_ok = True
        replied  = []
        hot      = []

        for r in recipients:
            total_replies = sum(s.get('replied', 0) for s in r.get('stages', []))
            opens = (r.get('analytics') or {}).get('events', {}).get('opens', 0)
            name  = r.get('to', {}).get('name', '?')
            email = r.get('to', {}).get('email', '')
            phone   = phone_map.get(email.lower(), '')
            company = company_map.get(email.lower(), '')

            if total_replies > 0:
                replied.append({'name': name, 'email': email, 'opens': opens, 'phone': phone, 'company': company})
                all_replies.append({'name': name, 'email': email, 'seq': seq_name, 'phone': phone, 'company': company})
            elif opens >= 2:
                hot.append({'name': name, 'email': email, 'opens': opens, 'phone': phone, 'company': company})
                all_hot.append({'name': name, 'email': email, 'seq': seq_name, 'opens': opens, 'phone': phone, 'company': company})

        status = '🔥 REPLIED' if replied else ('⚡ Hot' if hot else '—')
        print(f'  {seq_name}: {len(recipients)} enrolled | {len(replied)} replied | {len(hot)} hot | {status}')
        for r in replied:
            ph_str = f' | 📞 {r["phone"]}' if r.get('phone') else ''
            co_str = f' | {r["company"]}' if r.get('company') else ''
            print(f'    ✅ REPLY: {r["name"]}{co_str} ({r["email"]}){ph_str} — {r["opens"]} opens')
        for h in hot:
            ph_str = f' | 📞 {h["phone"]}' if h.get('phone') else ''
            co_str = f' | {h["company"]}' if h.get('company') else ''
            print(f'    ⚡ HOT:   {h["name"]}{co_str} ({h["email"]}){ph_str} — {h["opens"]} opens, no reply yet')

    print('=' * 50)

    if not api_ok:
        print('\n⚠️  Mixmax API unavailable — run this locally, not from the cloud.')
        log('check failed — Mixmax API unavailable')
        return

    # Summary
    if all_replies:
        print(f'\n🔥 {len(all_replies)} REPL{"Y" if len(all_replies) == 1 else "IES"} — respond NOW')
        for r in all_replies:
            ph_str = f' | 📞 {r["phone"]}' if r.get('phone') else ''
            print(f'   → {r["name"]} | {r["email"]}{ph_str} | {r["seq"]}')

        reply_lines = '\n'.join(
            f'>• {r["name"]} | {r.get("company", "") or "—"} — {r["email"]} | 📞 {r["phone"] or "—"} ({r["seq"]})'
            for r in all_replies
        )
        post_slack(
            f'🔥 *Mixmax — New {"Reply" if len(all_replies) == 1 else "Replies"} ({len(all_replies)})*\n'
            f'{reply_lines}\n'
            f'>Respond within 1 hour for best conversion.'
        )
        log(f'{len(all_replies)} replies found — Slack notified')
    else:
        print(f'\n⏳ No replies yet. {len(all_hot)} hot lead(s) with 2+ opens.')
        if all_hot:
            for h in all_hot:
                print(f'   ⚡ {h["name"]} | {h["email"]} | {h["opens"]} opens | {h["seq"]}')
            # Post hot leads to Slack so Bradley can act on LinkedIn connects + calls
            hot_lines = '\n'.join(
                f'>• {h["name"]} | {h.get("company", "") or "—"} — {h["opens"]} opens | {h["seq"]} | 📞 {h["phone"] or "—"}'
                for h in all_hot[:10]
            )
            post_slack(
                f'⚡ *Mixmax — {len(all_hot)} Hot Lead{"s" if len(all_hot) != 1 else ""} (0 replies yet)*\n'
                f'{hot_lines}\n'
                f'>Connect on LinkedIn + call these contacts TODAY.'
            )
        else:
            # API alive but completely quiet — post confirmation so Bradley knows the check ran clean
            post_slack(
                f'✅ *Mixmax — Check Complete ({datetime.now().strftime("%I:%M %p")})*\n'
                f'>No replies or hot leads yet. Pipeline is quiet.\n'
                f'>Run check_replies.py again at 2pm or tomorrow morning.'
            )
        log(f'0 replies | {len(all_hot)} hot leads')

    print('\nDone. Run again tomorrow morning.')


if __name__ == '__main__':
    main()
