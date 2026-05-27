#!/usr/bin/env python3
"""
contact_done.py — Quick pipeline contact updater.
After texting or calling someone, run this to update their stage + set next follow-up.

Usage:
  python3 scripts/contact_done.py              # lists today's due contacts, update each
  python3 scripts/contact_done.py <company>    # jump straight to a specific company
  python3 scripts/contact_done.py --all        # show all active contacts
"""

import json
import sys
from datetime import datetime, date, timedelta
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.resolve()
PIPELINE_F = BASE_DIR / 'pipeline_data.json'

STAGES = [
    'New Lead', 'Contacted', 'Replied', 'Estimate Sent',
    'Estimate Accepted', 'Closed Won', 'Closed Lost'
]

FOLLOW_UP_SHORTCUTS = {
    '1': (date.today() + timedelta(days=1)).isoformat(),
    '2': (date.today() + timedelta(days=2)).isoformat(),
    '3': (date.today() + timedelta(days=3)).isoformat(),
    '5': (date.today() + timedelta(days=5)).isoformat(),
    '7': (date.today() + timedelta(days=7)).isoformat(),
    '14': (date.today() + timedelta(days=14)).isoformat(),
    '30': (date.today() + timedelta(days=30)).isoformat(),
}


def load_pipeline():
    if not PIPELINE_F.exists():
        print('pipeline_data.json not found.')
        sys.exit(1)
    try:
        return json.loads(PIPELINE_F.read_text())
    except Exception as e:
        print(f'Error reading pipeline_data.json: {e}')
        sys.exit(1)


def save_pipeline(data):
    PIPELINE_F.write_text(json.dumps(data, indent=2))
    print('  ✅ pipeline_data.json updated.')


def display_contact(c, idx=None):
    name = f'{c.get("first_name","")} {c.get("last_name","")}'.strip() or c.get('company', '?')
    prefix = f'[{idx}] ' if idx is not None else ''
    print(f'  {prefix}{name} | {c.get("company","")}')
    print(f'       Stage: {c.get("stage","?")}  |  Phone: {c.get("phone","—")}')
    print(f'       Last contact: {c.get("last_contact","never")}  |  Next followup: {c.get("next_followup","not set")}')


def update_contact(c):
    """Interactive update for a single contact. Returns True if changed."""
    name = f'{c.get("first_name","")} {c.get("last_name","")}'.strip() or c.get('company', '?')
    print(f'\n── Updating: {name} ({c.get("company","")}) ──')
    display_contact(c)

    # Stage update
    print(f'\n  Stages: ' + ' | '.join(f'{i+1}={s}' for i, s in enumerate(STAGES)))
    current_stage_idx = STAGES.index(c.get('stage', 'New Lead')) if c.get('stage') in STAGES else 0
    stage_input = input(f'  New stage? (Enter=keep "{STAGES[current_stage_idx]}", or 1-{len(STAGES)}): ').strip()
    if stage_input.isdigit() and 1 <= int(stage_input) <= len(STAGES):
        c['stage'] = STAGES[int(stage_input) - 1]
        print(f'  Stage → {c["stage"]}')

    # Last contact date
    today_str = date.today().isoformat()
    lc_input = input(f'  Set last_contact to today ({today_str})? (Y/n): ').strip().lower()
    if lc_input != 'n':
        c['last_contact'] = today_str

    # Next followup
    print(f'  Next followup shortcuts: 1=tomorrow, 2=+2d, 3=+3d, 5=+5d, 7=+1wk, 14=+2wk, 30=+30d, or type YYYY-MM-DD, or "none"')
    nf_input = input(f'  Next followup? (current: {c.get("next_followup","not set")}): ').strip()
    if nf_input == 'none':
        c.pop('next_followup', None)
        print('  next_followup cleared.')
    elif nf_input in FOLLOW_UP_SHORTCUTS:
        c['next_followup'] = FOLLOW_UP_SHORTCUTS[nf_input]
        print(f'  next_followup → {c["next_followup"]}')
    elif nf_input and len(nf_input) == 10:
        c['next_followup'] = nf_input
        print(f'  next_followup → {c["next_followup"]}')
    elif nf_input == '':
        pass  # keep existing

    # Notes
    note = input('  Add a note? (Enter to skip): ').strip()
    if note:
        existing_notes = c.get('notes', '')
        c['notes'] = f'[{today_str}] {note}' + (f'\n{existing_notes}' if existing_notes else '')
        print('  Note saved.')

    return True


def main():
    data = load_pipeline()
    contacts = data.get('manual_contacts', [])
    today_str = date.today().isoformat()
    _inactive = {'Closed Won', 'Closed Lost'}

    # Determine which contacts to show
    search_term = None
    show_all = False
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == '--all':
            show_all = True
        else:
            search_term = arg.lower()

    if search_term:
        targets = [
            c for c in contacts
            if search_term in (c.get('company', '') + ' ' + c.get('first_name', '') + ' ' + c.get('last_name', '')).lower()
            and c.get('stage') not in _inactive
        ]
        if not targets:
            print(f'No active contact matching "{search_term}" found.')
            return
    elif show_all:
        targets = [c for c in contacts if c.get('stage') not in _inactive]
    else:
        # Default: due today + overdue
        overdue = [c for c in contacts if c.get('next_followup') and c['next_followup'] < today_str and c.get('stage') not in _inactive]
        due_today = [c for c in contacts if c.get('next_followup') == today_str and c.get('stage') not in _inactive]
        targets = overdue + due_today
        if not targets:
            print(f'No contacts due today ({today_str}). Run with --all to see everyone.')
            print('Or search: python3 scripts/contact_done.py <company name>')
            return

    print(f'\n=== Contact Done — {today_str} ===')
    print(f'  {len(targets)} contacts to update:\n')
    for i, c in enumerate(targets):
        display_contact(c, idx=i + 1)

    if len(targets) > 1:
        pick = input(f'\nUpdate which? (1-{len(targets)}, "all", or Enter to skip): ').strip().lower()
        if pick == '' or pick == 'skip':
            print('Exiting without changes.')
            return
        elif pick == 'all':
            to_update = targets
        elif pick.isdigit() and 1 <= int(pick) <= len(targets):
            to_update = [targets[int(pick) - 1]]
        else:
            print('Invalid selection. Exiting.')
            return
    else:
        confirm = input(f'\nUpdate {targets[0].get("company","this contact")}? (Y/n): ').strip().lower()
        to_update = [] if confirm == 'n' else targets

    changed = False
    for c in to_update:
        if update_contact(c):
            changed = True

    if changed:
        save_pipeline(data)
        print(f'\n✅ Done. Run `python3 workers/nina_report.py daily` to see updated pipeline report.')
    else:
        print('\nNo changes made.')


if __name__ == '__main__':
    main()
