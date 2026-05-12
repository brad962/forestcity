#!/usr/bin/env python3
"""
Nina Kowalski — Pipeline Report
Runs daily. Pulls Mixmax data, generates hot leads report and weekly pipeline summary.
Usage: python3 workers/nina_report.py [daily|weekly]
"""

import json
import urllib.request
import sys
from datetime import datetime
from pathlib import Path

BASE_DIR  = Path(__file__).parent.parent.resolve()
OUTPUTS   = BASE_DIR / 'outputs' / 'nina'
LOG_FILE  = BASE_DIR / 'logs' / 'activity.log'

MIXMAX_TOKEN = '3646d2be-c1be-44b7-b3ef-e7ea047cad83'
SEQUENCES = {
    '6a037da614a5158fcfc165fc': {'name': 'Property Managers', 'worker': 'Danny'},
    '6a0382b96c6ce077a2544212': {'name': 'Realtors',          'worker': 'Carla'},
    '6a038613e22797c40fc5d457': {'name': 'Contractors',       'worker': 'Carla'},
}


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
            return data if isinstance(data, list) else []
    except Exception:
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


def run_daily():
    print('\n📊 Nina — Daily Hot Leads Report')
    OUTPUTS.mkdir(exist_ok=True)
    date_str = datetime.now().strftime('%Y-%m-%d')
    all_hot  = []
    all_replied = []

    for seq_id, meta in SEQUENCES.items():
        recipients = fetch_recipients(seq_id)
        stats = analyze_recipients(recipients, meta['name'])
        all_hot.extend([(meta['name'], l) for l in stats['hot_leads']])
        all_replied.extend([(meta['name'], r) for r in stats['replied_contacts']])
        print(f'  {meta["name"]}: {stats["total"]} enrolled | {stats["open_rate"]} opens | {stats["reply_rate"]} replies')

    lines = [
        f'# Daily Hot Leads Report',
        f'### {datetime.now().strftime("%A, %B %d %Y")}',
        f'*Nina Kowalski | RevOps Manager*',
        '',
    ]

    if all_replied:
        lines += [
            '## 🔥 REPLIED — Action Required',
            '*These contacts responded. Follow up today.*',
            '',
            '| Name | Email | Sequence | Stage |',
            '|------|-------|----------|-------|',
        ]
        for seq_name, r in all_replied:
            lines.append(f'| {r["name"]} | {r["email"]} | {seq_name} | {r["stage"]} |')
        lines.append('')

    if all_hot:
        lines += [
            '## ⚡ HOT LEADS — High Engagement',
            '*2+ opens or clicked a link. Connect on LinkedIn now.*',
            '',
            '| Name | Email | Sequence | Opens | Replied |',
            '|------|-------|----------|-------|---------|',
        ]
        for seq_name, l in all_hot:
            replied_str = '✅ Yes' if l['replied'] else 'No'
            lines.append(f'| {l["name"]} | {l["email"]} | {seq_name} | {l["opens"]} | {replied_str} |')
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
    return all_hot, all_replied


def run_weekly():
    print('\n📈 Nina — Weekly Pipeline Report')
    OUTPUTS.mkdir(exist_ok=True)
    date_str = datetime.now().strftime('%Y-%m-%d')
    all_stats = []

    for seq_id, meta in SEQUENCES.items():
        recipients = fetch_recipients(seq_id)
        stats = analyze_recipients(recipients, meta['name'])
        all_stats.append(stats)
        print(f'  {meta["name"]}: {stats["total"]} | opens={stats["open_rate"]} | replies={stats["reply_rate"]}')

    total_enrolled = sum(s['total'] for s in all_stats)
    total_opens    = sum(s['opens'] for s in all_stats)
    total_replied  = sum(len(s['replied_contacts']) for s in all_stats)
    total_hot      = sum(len(s['hot_leads']) for s in all_stats)

    lines = [
        f'# Weekly Pipeline Report',
        f'### Week of {datetime.now().strftime("%B %d, %Y")}',
        f'*Nina Kowalski | RevOps Manager*',
        '',
        '## Summary',
        '',
        f'| Metric | Value |',
        f'|--------|-------|',
        f'| Total enrolled across sequences | {total_enrolled} |',
        f'| Contacts with opens | {total_opens} |',
        f'| Contacts who replied | {total_replied} |',
        f'| Hot leads (2+ opens) | {total_hot} |',
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

    lines += ['', '## Contacts Who Replied', '']
    for s in all_stats:
        if s['replied_contacts']:
            lines.append(f'### {s["sequence"]}')
            lines += ['| Name | Email | Stage | Opens |', '|------|-------|-------|-------|']
            for r in s['replied_contacts']:
                lines.append(f'| {r["name"]} | {r["email"]} | {r["stage"]} | {r["opens"]} |')
            lines.append('')

    if not any(s['replied_contacts'] for s in all_stats):
        lines += ['*No replies yet. Emails are scheduled — check back next week.*', '']

    lines += [
        '## Action Items for Bradley',
        '',
        f'- [ ] Review {total_replied} replies and respond personally',
        f'- [ ] Connect on LinkedIn with {total_hot} hot leads via the Connect page',
        f'- [ ] Check Danny\'s new leads this week and confirm enrollment',
        '',
        '---',
        f'*Generated automatically by Nina | {datetime.now().strftime("%Y-%m-%d %H:%M")}*',
    ]

    out_file = f'weekly_report_{date_str}.md'
    (OUTPUTS / out_file).write_text('\n'.join(lines))
    log(f'Weekly pipeline report — {total_enrolled} enrolled, {total_replied} replied, {total_hot} hot leads', out_file)
    print(f'  → Report saved to {out_file}')


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'daily'
    print(f'\n=== Nina Report — {datetime.now().strftime("%Y-%m-%d %H:%M")} ===')
    if mode == 'weekly':
        run_weekly()
    else:
        run_daily()
    print('\n✅ Done.')
