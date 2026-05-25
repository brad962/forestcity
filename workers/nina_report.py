#!/usr/bin/env python3
"""
Nina Kowalski — Pipeline Report
Runs daily. Pulls Mixmax data, generates hot leads report and weekly pipeline summary.
Usage: python3 workers/nina_report.py [daily|weekly]
"""

import json
import os
import sys
import urllib.request
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from utils.report_card import send_report_card

BASE_DIR  = Path(__file__).parent.parent.resolve()
OUTPUTS   = BASE_DIR / 'outputs' / 'nina'
LOG_FILE  = BASE_DIR / 'logs' / 'activity.log'


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


GITHUB_BASE = 'https://github.com/brad962/forestcity/blob/main'


def notify_slack(message):
    try:
        payload = json.dumps({'text': message}).encode()
        req = urllib.request.Request(SLACK_WEBHOOK, data=payload, headers={'Content-Type': 'application/json'})
        urllib.request.urlopen(req, timeout=5)
    except Exception:
        pass


def git_push(commit_msg):
    import subprocess
    try:
        subprocess.run(['git', '-C', str(BASE_DIR), 'add', 'outputs/nina/', 'logs/'], capture_output=True)
        subprocess.run(['git', '-C', str(BASE_DIR), 'commit', '-m', commit_msg], capture_output=True)
        subprocess.run(['git', '-C', str(BASE_DIR), 'push', 'origin', 'main'], capture_output=True, timeout=15)
    except Exception:
        pass
_DISPLAY_NAMES = {
    'property_manager': 'Property Managers',
    'realtor':          'Realtors',
    'contractor':       'Contractors',
    'gas_station':      'Gas Stations',
    'fleet_washing':    'Fleet Washing',
}
_WORKER_MAP = {
    'property_manager': 'Danny',
    'realtor':          'Carla',
    'contractor':       'Carla',
    'gas_station':      'Danny',
    'fleet_washing':    'Danny',
}
_FALLBACK_SEQUENCES = {
    '6a048cfc110bc620ca0f1aee': {'name': 'Property Managers', 'worker': 'Danny'},
    '6a048cfba81429e5dfe55010': {'name': 'Realtors',          'worker': 'Carla'},
    '6a048cfd624a5989a68ba16c': {'name': 'Contractors',       'worker': 'Carla'},
}


def _build_sequences():
    """Build sequence map from mixmax.py — single source of truth for active IDs."""
    try:
        from integrations.mixmax import SEQUENCES as MX_SEQS
        mapping = {}
        for seq_type, meta in MX_SEQS.items():
            sid = meta.get('id', '')
            if sid and sid != 'PENDING':
                mapping[sid] = {
                    'name':   _DISPLAY_NAMES.get(seq_type, seq_type.replace('_', ' ').title()),
                    'worker': _WORKER_MAP.get(seq_type, 'Danny'),
                }
        return mapping if mapping else _FALLBACK_SEQUENCES
    except Exception:
        return _FALLBACK_SEQUENCES


SEQUENCES = _build_sequences()


def log(task, output_file, status='Done'):
    ts = datetime.now().strftime('%Y-%m-%d %H:%M')
    line = f'[{ts}] Nina | {task} | {output_file} | {status}\n'
    LOG_FILE.parent.mkdir(exist_ok=True)
    with open(LOG_FILE, 'a') as f:
        f.write(line)


def fetch_recipients(seq_id):
    url = f'https://api.mixmax.com/v1/sequences/{seq_id}/recipients?apiToken={MIXMAX_TOKEN}&limit=200'
    try:
        with urllib.request.urlopen(url, timeout=10) as resp:
            data = json.loads(resp.read())
        if isinstance(data, list):
            return data
        # Mixmax may return {"results": [...]} or {"recipients": [...]}
        return data.get('results', data.get('recipients', []))
    except Exception as e:
        print(f'  fetch_recipients error for {seq_id}: {e}')
        return []


def analyze_recipients(recipients, seq_name):
    total   = len(recipients)
    active  = sum(1 for r in recipients if r.get('state') == 'active')
    opens   = sum(1 for r in recipients if (r.get('analytics') or {}).get('events', {}).get('opens', 0) > 0)
    clicks  = sum(1 for r in recipients if (r.get('analytics') or {}).get('events', {}).get('clicks', 0) > 0)
    replied = []

    for r in recipients:
        total_replies = sum(s.get('replied', 0) for s in r.get('stages', []))
        if total_replies > 0:
            replied.append({
                'name':    r.get('to', {}).get('name', ''),
                'email':   r.get('to', {}).get('email', ''),
                'stage':   r.get('lastStageSentOrdinal', 1),
                'opens':   (r.get('analytics') or {}).get('events', {}).get('opens', 0),
            })

    hot_leads = []
    for r in recipients:
        r_opens = (r.get('analytics') or {}).get('events', {}).get('opens', 0)
        r_replies = sum(s.get('replied', 0) for s in r.get('stages', []))
        if r_opens >= 2 or r_replies > 0:
            hot_leads.append({
                'name':    r.get('to', {}).get('name', ''),
                'email':   r.get('to', {}).get('email', ''),
                'opens':   r_opens,
                'replied': r_replies > 0,
                'stage':   r.get('lastStageSentOrdinal', 1),
                'linkedin': '',
            })

    return {
        'sequence': seq_name,
        'total': total, 'active': active,
        'opens': opens, 'clicks': clicks,
        'replied_contacts': replied,
        'hot_leads': hot_leads,
        'open_rate': f'{round(opens/total*100)}%' if total else '0%',
        'reply_rate': f'{round(len(replied)/total*100)}%' if total else '0%',
    }


def _load_linkedin_map():
    """Build email → linkedin_url map from contacts cache (best-effort)."""
    cache_file = BASE_DIR / 'contacts_cache.json'
    if not cache_file.exists():
        return {}
    try:
        data = json.loads(cache_file.read_text())
        return {
            c['email'].lower(): c.get('linkedin_url', '')
            for c in data.get('contacts', [])
            if c.get('email') and c.get('linkedin_url')
        }
    except Exception:
        return {}


def _load_phone_map():
    """Build email → phone from contacts cache + pipeline_data (manual contacts).
    Matches check_replies.py — ensures Tier 1 contractors, gas station, and fleet
    contacts show phone numbers in Nina's reports if they reply.
    """
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


def _load_company_map():
    """Build email → company_name from contacts cache + pipeline_data (manual contacts).
    Matches check_replies.py — ensures manual contacts show company in Nina's reports.
    """
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


def run_daily():
    print('\n📊 Nina — Daily Hot Leads Report')
    OUTPUTS.mkdir(exist_ok=True)
    date_str = datetime.now().strftime('%Y-%m-%d')
    all_hot  = []
    all_replied = []
    linkedin_map = _load_linkedin_map()
    phone_map    = _load_phone_map()

    company_map  = _load_company_map()
    seq_stats_cache = {}
    api_responses_received = 0
    for seq_id, meta in SEQUENCES.items():
        recipients = fetch_recipients(seq_id)
        if recipients:
            api_responses_received += 1
        stats = analyze_recipients(recipients, meta['name'])
        seq_stats_cache[seq_id] = stats
        all_hot.extend([(meta['name'], l) for l in stats['hot_leads']])
        all_replied.extend([(meta['name'], r) for r in stats['replied_contacts']])
        print(f'  {meta["name"]}: {stats["total"]} enrolled | {stats["open_rate"]} opens | {stats["reply_rate"]} replies')

    # Inject LinkedIn URLs, phone numbers, and company names from contacts cache
    for _, lead in all_hot:
        lead['linkedin'] = linkedin_map.get(lead['email'].lower(), '')
        lead['phone']    = phone_map.get(lead['email'].lower(), '')
        lead['company']  = company_map.get(lead['email'].lower(), '')
    # Inject phone + company into replied contacts — both needed for immediate follow-up
    for _, r in all_replied:
        r['phone']   = phone_map.get(r['email'].lower(), '')
        r['company'] = company_map.get(r['email'].lower(), '')

    api_blocked = (api_responses_received == 0)

    lines = [
        f'# Daily Hot Leads Report',
        f'### {datetime.now().strftime("%A, %B %d %Y")}',
        f'*Nina Kowalski | RevOps Manager*',
        '',
    ]

    if api_blocked:
        lines += [
            '> ⚠️ **Mixmax API unavailable** — all sequences returned 0 recipients.',
            '> This happens when running in the cloud environment (Mixmax is network-blocked).',
            '> Run `python3 workers/nina_report.py daily` locally for accurate data.',
            '',
        ]

    # Warn when API is live but reply rate is 0 — Instantly.ai overlap is the #1 suspect
    total_enrolled_check = sum(s['total'] for s in seq_stats_cache.values())
    if not api_blocked and not all_replied and total_enrolled_check > 10:
        lines += [
            '> ⚠️ **0% reply rate** — Primary suspect: Instantly.ai overlap.',
            '> Two Instantly.ai campaigns (a1c08c3d + 626cd15d) may be hitting the same contacts.',
            '> Duplicate emails trigger spam filters. Pause guide: `outputs/vera/instantly_pause_guide_2026-05-22.md`',
            '',
        ]

    if all_replied:
        lines += [
            '## 🔥 REPLIED — Action Required',
            '*These contacts responded. Follow up today.*',
            '',
            '| Name | Company | Email | Phone | Sequence | Stage |',
            '|------|---------|-------|-------|----------|-------|',
        ]
        for seq_name, r in all_replied:
            ph = r.get('phone', '') or '—'
            co = r.get('company', '') or '—'
            lines.append(f'| {r["name"]} | {co} | {r["email"]} | {ph} | {seq_name} | {r["stage"]} |')
        lines.append('')

    if all_hot:
        lines += [
            '## ⚡ HOT LEADS — High Engagement',
            '*2+ opens or clicked a link. Connect on LinkedIn now.*',
            '',
            '| Name | Company | Email | Phone | Sequence | Opens | Replied | LinkedIn |',
            '|------|---------|-------|-------|----------|-------|---------|---------|',
        ]
        for seq_name, l in all_hot:
            replied_str = '✅ Yes' if l['replied'] else 'No'
            li = f'[Connect]({l["linkedin"]})' if l.get('linkedin') else '—'
            ph = l.get('phone', '') or '—'
            co = l.get('company', '') or '—'
            lines.append(f'| {l["name"]} | {co} | {l["email"]} | {ph} | {seq_name} | {l["opens"]} | {replied_str} | {li} |')
        lines.append('')
    else:
        lines += ['## No hot leads yet', '*Check back once emails start sending.*', '']

    lines += [
        '---',
        f'*Generated automatically by Nina | {datetime.now().strftime("%Y-%m-%d %H:%M")}*',
    ]

    out_file = f'hot_leads_{date_str}.md'
    (OUTPUTS / out_file).write_text('\n'.join(lines))
    log(f'Daily hot leads report — {len(all_replied)} replied, {len(all_hot)} hot', out_file)
    print(f'  → {len(all_replied)} replied, {len(all_hot)} hot leads. Saved to {out_file}')
    git_push(f'Nina: daily hot leads {date_str}')
    status = 'ACTION NEEDED' if all_replied else ('DONE' if not all_hot else 'ACTION NEEDED')
    summary = []
    if all_replied:
        summary.append(f'{len(all_replied)} contacts replied — follow up TODAY')
    if all_hot:
        summary.append(f'{len(all_hot)} hot leads (2+ opens) — connect on LinkedIn')
    for seq_id, meta in SEQUENCES.items():
        stats = seq_stats_cache[seq_id]
        summary.append(f'{meta["name"]}: {stats["total"]} enrolled, {stats["open_rate"]} opens')
    send_report_card(
        worker_name='nina',
        title='Daily Hot Leads Report',
        metrics=[
            ('Replied', len(all_replied)),
            ('Hot Leads', len(all_hot)),
        ],
        summary_lines=summary or ['No hot leads yet — check back tomorrow'],
        status=status,
    )
    return all_hot, all_replied


def run_weekly():
    print('\n📈 Nina — Weekly Pipeline Report')
    OUTPUTS.mkdir(exist_ok=True)
    date_str = datetime.now().strftime('%Y-%m-%d')
    all_stats = []
    linkedin_map = _load_linkedin_map()
    phone_map    = _load_phone_map()
    company_map  = _load_company_map()
    api_responses_received = 0
    for seq_id, meta in SEQUENCES.items():
        recipients = fetch_recipients(seq_id)
        if recipients:
            api_responses_received += 1
        stats = analyze_recipients(recipients, meta['name'])
        for lead in stats['hot_leads']:
            lead['linkedin'] = linkedin_map.get(lead['email'].lower(), '')
            lead['phone']    = phone_map.get(lead['email'].lower(), '')
            lead['company']  = company_map.get(lead['email'].lower(), '')
        all_stats.append(stats)
        print(f'  {meta["name"]}: {stats["total"]} | opens={stats["open_rate"]} | replies={stats["reply_rate"]}')

    total_enrolled = sum(s['total'] for s in all_stats)
    total_opens    = sum(s['opens'] for s in all_stats)
    total_replied  = sum(len(s['replied_contacts']) for s in all_stats)
    total_hot      = sum(len(s['hot_leads']) for s in all_stats)
    api_blocked    = (api_responses_received == 0)

    api_warning = [
        '> ⚠️ **Mixmax API unavailable** — all sequences returned 0 recipients.',
        '> Run locally for accurate data: `python3 workers/nina_report.py weekly`',
        '',
    ] if api_blocked else []

    lines = [
        f'# Weekly Pipeline Report',
        f'### Week of {datetime.now().strftime("%B %d, %Y")}',
        f'*Nina Kowalski | RevOps Manager*',
        '',
    ] + api_warning + [
        '## Summary',
        '',
        f'| Metric | Value |',
        f'|--------|-------|',
        f'| Total enrolled across sequences | {total_enrolled} |',
        f'| Contacts with opens | {total_opens} |',
        f'| Contacts who replied | {total_replied} |',
        f'| Hot leads (2+ opens or replied) | {total_hot} |',
        f'| Overall open rate | {round(total_opens/total_enrolled*100) if total_enrolled else 0}% |',
        f'| Overall reply rate | {round(total_replied/total_enrolled*100) if total_enrolled else 0}% |',
        '',
        '## By Sequence',
        '',
        '| Sequence | Enrolled | Active | Opens | Replied | Open Rate | Reply Rate |',
        '|----------|----------|--------|-------|---------|-----------|------------|',
    ]
    for s in all_stats:
        lines.append(f'| {s["sequence"]} | {s["total"]} | {s["active"]} | {s["opens"]} | {len(s["replied_contacts"])} | {s["open_rate"]} | {s["reply_rate"]} |')

    # Inject phone + company into replied contacts for weekly report
    for s in all_stats:
        for r in s['replied_contacts']:
            r['phone']   = phone_map.get(r['email'].lower(), '')
            r['company'] = company_map.get(r['email'].lower(), '')

    lines += ['', '## Contacts Who Replied', '']
    for s in all_stats:
        if s['replied_contacts']:
            lines.append(f'### {s["sequence"]}')
            lines += ['| Name | Company | Email | Phone | Stage | Opens |', '|------|---------|-------|-------|-------|-------|']
            for r in s['replied_contacts']:
                ph = r.get('phone', '') or '—'
                co = r.get('company', '') or '—'
                lines.append(f'| {r["name"]} | {co} | {r["email"]} | {ph} | {r["stage"]} | {r["opens"]} |')
            lines.append('')

    if not any(s['replied_contacts'] for s in all_stats):
        lines += ['*No replies yet. Emails are scheduled — check back next week.*', '']

    # --- Hot Leads (2+ opens, no reply yet) ---
    all_hot_unreplied = [
        (s['sequence'], l)
        for s in all_stats
        for l in s['hot_leads']
        if not l.get('replied')
    ]
    if all_hot_unreplied:
        lines += [
            '## ⚡ Hot Leads — No Reply Yet',
            '*2+ opens with no reply. Connect on LinkedIn or call them this week.*',
            '',
            '| Name | Company | Email | Phone | Sequence | Opens | Stage | LinkedIn |',
            '|------|---------|-------|-------|----------|-------|-------|---------|',
        ]
        for seq_name, l in all_hot_unreplied:
            li = f'[Connect]({l["linkedin"]})' if l.get('linkedin') else '—'
            ph = l.get('phone', '') or '—'
            co = l.get('company', '') or '—'
            lines.append(f'| {l["name"]} | {co} | {l["email"]} | {ph} | {seq_name} | {l["opens"]} | {l.get("stage", 1)} | {li} |')
        lines.append('')
    elif not api_blocked:
        lines += ['## Hot Leads', '*No contacts with 2+ opens yet — check back next week.*', '']

    # --- Manual Pipeline Health (pipeline_data.json) ---
    manual_health_lines = []
    try:
        pipeline_f = BASE_DIR / 'pipeline_data.json'
        if pipeline_f.exists():
            pd_data = json.loads(pipeline_f.read_text())
            manual = pd_data.get('manual_contacts', [])
            untouched = [c for c in manual if not c.get('last_contact') and c.get('stage') not in ('Closed Won', 'Closed Lost')]
            contacted = [c for c in manual if c.get('stage') == 'Contacted']
            replied_m = [c for c in manual if c.get('stage') == 'Replied']
            manual_health_lines = [
                '## Manual Pipeline Health (Non-Mixmax Contacts)',
                '',
                f'| Metric | Count |',
                f'|--------|-------|',
                f'| Total manual contacts | {len(manual)} |',
                f'| Never reached out to (stale) | {len(untouched)} |',
                f'| Contacted | {len(contacted)} |',
                f'| Replied | {len(replied_m)} |',
                '',
            ]
            if untouched:
                manual_health_lines.append(f'⚠️ **{len(untouched)} contacts have never been reached out to.** Work through the priority list this week.')
                for c in untouched[:10]:
                    name = f'{c.get("first_name","")} {c.get("last_name","")}'.strip() or c.get('company', '?')
                    manual_health_lines.append(f'  - {name} ({c.get("company","")}) | {c.get("lead_type","?")} | {c.get("phone","")}')
                if len(untouched) > 10:
                    manual_health_lines.append(f'  - ...and {len(untouched) - 10} more')
                manual_health_lines.append('')

            # Follow-up due in next 7 days
            from datetime import timedelta
            today_str = datetime.now().strftime('%Y-%m-%d')
            week_end = (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')
            due_soon = [c for c in manual if c.get('next_followup') and today_str <= c['next_followup'] <= week_end]
            overdue = [c for c in manual if c.get('next_followup') and c['next_followup'] < today_str]

            # Also flag "Contacted" stage contacts with last_contact > 7 days ago and no next_followup set
            from datetime import date as _date
            stale_contacted = []
            for c in manual:
                if c.get('stage') == 'Contacted' and c.get('last_contact') and not c.get('next_followup'):
                    try:
                        last_dt = _date.fromisoformat(c['last_contact'])
                        days_ago = (_date.fromisoformat(today_str) - last_dt).days
                        if days_ago >= 7:
                            stale_contacted.append((c, days_ago))
                    except Exception:
                        pass

            if overdue:
                manual_health_lines.append(f'🔴 **OVERDUE follow-ups ({len(overdue)}) — reach out now:**')
                for c in overdue:
                    name = f'{c.get("first_name","")} {c.get("last_name","")}'.strip() or c.get('company', '?')
                    manual_health_lines.append(f'  - {name} ({c.get("company","")}) | was due {c["next_followup"]} | {c.get("phone","")}')
                manual_health_lines.append('')
            if stale_contacted:
                manual_health_lines.append(f'🟡 **"Contacted" stage — no follow-up date set, going stale ({len(stale_contacted)}):**')
                for c, days_ago in stale_contacted:
                    name = f'{c.get("first_name","")} {c.get("last_name","")}'.strip() or c.get('company', '?')
                    manual_health_lines.append(f'  - {name} ({c.get("company","")}) | contacted {days_ago} days ago | {c.get("phone","")} — add next_followup date')
                manual_health_lines.append('')
            if due_soon:
                manual_health_lines.append(f'📅 **Follow-ups due this week ({len(due_soon)}):**')
                for c in due_soon:
                    name = f'{c.get("first_name","")} {c.get("last_name","")}'.strip() or c.get('company', '?')
                    manual_health_lines.append(f'  - {name} ({c.get("company","")}) | due {c["next_followup"]} | {c.get("phone","")}')
                manual_health_lines.append('')
    except Exception:
        pass

    reply_item = (
        f'- [ ] Review {total_replied} {"reply" if total_replied == 1 else "replies"} and respond personally'
        if total_replied > 0
        else '- [ ] No replies yet — sequence is sending, check open rates'
    )
    lines += manual_health_lines + [
        '## Action Items for Bradley',
        '',
        reply_item,
        ('- [ ] Run `python3 workers/nina_report.py daily` locally to see hot leads, then connect on LinkedIn'
         if api_blocked
         else f'- [ ] Connect on LinkedIn with {total_hot} hot leads (links in the daily hot leads report)'),
        f'- [ ] Check Danny\'s new leads this week and confirm enrollment',
        '',
        '---',
        f'*Generated automatically by Nina | {datetime.now().strftime("%Y-%m-%d %H:%M")}*',
    ]

    out_file = f'weekly_report_{date_str}.md'
    (OUTPUTS / out_file).write_text('\n'.join(lines))
    log(f'Weekly pipeline report — {total_enrolled} enrolled, {total_replied} replied, {total_hot} hot leads', out_file)
    print(f'  → Report saved to {out_file}')
    git_push(f'Nina: weekly pipeline report {date_str}')
    open_rate_pct = round(total_opens / total_enrolled * 100) if total_enrolled else 0
    reply_rate_pct = round(total_replied / total_enrolled * 100) if total_enrolled else 0
    seq_lines = [f'{s["sequence"]}: {s["total"]} enrolled | {s["open_rate"]} opens | {s["reply_rate"]} replies' for s in all_stats]
    if api_blocked:
        report_status = 'IN PROGRESS'
        report_summary = ['⚠️ Mixmax API unavailable in cloud — run locally for accurate data.']
    elif total_replied > 0:
        report_status = 'ACTION NEEDED'
        report_summary = seq_lines + [f'Overall open rate: {open_rate_pct}%', f'Overall reply rate: {reply_rate_pct}%']
    else:
        report_status = 'DONE'
        report_summary = seq_lines + [f'Overall open rate: {open_rate_pct}%', f'Overall reply rate: {reply_rate_pct}%']
    send_report_card(
        worker_name='nina',
        title='Weekly Pipeline Report',
        metrics=[
            ('Enrolled', total_enrolled),
            ('Opens', total_opens),
            ('Hot Leads', total_hot),
            ('Replies', total_replied),
        ],
        summary_lines=report_summary,
        status=report_status,
    )


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'daily'
    print(f'\n=== Nina Report — {datetime.now().strftime("%Y-%m-%d %H:%M")} ===')
    if mode == 'weekly':
        run_weekly()
    else:
        run_daily()
    print('\n✅ Done.')
