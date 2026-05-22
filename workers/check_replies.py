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

            if total_replies > 0:
                replied.append({'name': name, 'email': email, 'opens': opens})
                all_replies.append({'name': name, 'email': email, 'seq': seq_name})
            elif opens >= 2:
                hot.append({'name': name, 'email': email, 'opens': opens})
                all_hot.append({'name': name, 'email': email, 'seq': seq_name, 'opens': opens})

        status = '🔥 REPLIED' if replied else ('⚡ Hot' if hot else '—')
        print(f'  {seq_name}: {len(recipients)} enrolled | {len(replied)} replied | {len(hot)} hot | {status}')
        for r in replied:
            print(f'    ✅ REPLY: {r["name"]} ({r["email"]}) — {r["opens"]} opens')
        for h in hot:
            print(f'    ⚡ HOT:   {h["name"]} ({h["email"]}) — {h["opens"]} opens, no reply yet')

    print('=' * 50)

    if not api_ok:
        print('\n⚠️  Mixmax API unavailable — run this locally, not from the cloud.')
        log('check failed — Mixmax API unavailable')
        return

    # Summary
    if all_replies:
        print(f'\n🔥 {len(all_replies)} REPL{"Y" if len(all_replies) == 1 else "IES"} — respond NOW')
        for r in all_replies:
            print(f'   → {r["name"]} | {r["email"]} | {r["seq"]}')

        reply_lines = '\n'.join(f'>• {r["name"]} — {r["email"]} ({r["seq"]})' for r in all_replies)
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
                f'>• {h["name"]} — {h["opens"]} opens | {h["seq"]}'
                for h in all_hot[:10]
            )
            post_slack(
                f'⚡ *Mixmax — {len(all_hot)} Hot Lead{"s" if len(all_hot) != 1 else ""} (0 replies yet)*\n'
                f'{hot_lines}\n'
                f'>Connect on LinkedIn + call these contacts TODAY.'
            )
        log(f'0 replies | {len(all_hot)} hot leads')

    print('\nDone. Run again tomorrow morning.')


if __name__ == '__main__':
    main()
