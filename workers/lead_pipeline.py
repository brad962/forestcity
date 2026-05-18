#!/usr/bin/env python3
"""
Lead Pipeline — Danny & Carla
Runs weekly. Pulls fresh leads from Apollo, deduplicates, enrolls in Mixmax.
Usage: python3 workers/lead_pipeline.py [danny|carla|both]
"""

import json
import os
import subprocess
import sys
import time
import urllib.request
from datetime import datetime
from pathlib import Path

BASE_DIR   = Path(__file__).parent.parent.resolve()
OUTPUTS    = BASE_DIR / 'outputs'
LOG_FILE   = BASE_DIR / 'logs' / 'activity.log'
CACHE_FILE = BASE_DIR / 'contacts_cache.json'

sys.path.insert(0, str(BASE_DIR))
from utils.report_card import send_report_card


def _load_env():
    env_file = BASE_DIR / '.env'
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                k, v = line.split('=', 1)
                os.environ.setdefault(k.strip(), v.strip())


_load_env()

APOLLO_KEY    = os.environ.get('APOLLO_KEY', '')
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


def git_push(worker, commit_msg):
    try:
        subprocess.run(['git', '-C', str(BASE_DIR), 'add', f'outputs/{worker}/', 'logs/'], capture_output=True)
        subprocess.run(['git', '-C', str(BASE_DIR), 'commit', '-m', commit_msg], capture_output=True)
        subprocess.run(['git', '-C', str(BASE_DIR), 'push', 'origin', 'main'], capture_output=True, timeout=15)
    except Exception:
        pass

# Rotating county batches — Danny cycles through these weekly
DANNY_SEARCHES = [
    {'counties': ['Cuyahoga County, Ohio', 'Cleveland, Ohio'],          'label': 'Cuyahoga'},
    {'counties': ['Lake County, Ohio', 'Mentor, Ohio'],                  'label': 'Lake'},
    {'counties': ['Lorain County, Ohio', 'Elyria, Ohio'],               'label': 'Lorain'},
    {'counties': ['Summit County, Ohio', 'Akron, Ohio'],                 'label': 'Summit'},
    {'counties': ['Medina County, Ohio', 'Medina, Ohio'],               'label': 'Medina'},
    {'counties': ['Geauga County, Ohio', 'Portage County, Ohio'],       'label': 'Geauga+Portage'},
]

DANNY_TITLES = [
    'property manager', 'facility manager', 'community manager',
    'hoa manager', 'building manager', 'property management director',
    'asset manager', 'leasing manager',
    'facilities director', 'building superintendent',
    'apartment manager', 'condo manager', 'property supervisor',
    'residential manager', 'property director',
]

CARLA_SEARCHES = [
    {'type': 'contractors', 'titles': ['owner', 'president', 'founder'],
     'keywords': ['siding', 'exterior contractor', 'roofing', 'gutters', 'painting',
                  'landscaping', 'lawn care', 'window washing', 'chimney', 'concrete'],
     'label': 'Contractors'},
    {'type': 'realtors', 'titles': ['realtor', 'real estate agent', 'listing agent',
                                     'real estate broker', 'buyers agent'],
     'keywords': [],
     'label': 'Realtors'},
]

# Rotating county batches for Carla — mirrors Danny's county rotation
CARLA_COUNTY_ROTATION = [
    ['Cuyahoga County, Ohio', 'Cleveland, Ohio'],
    ['Lake County, Ohio', 'Mentor, Ohio', 'Willoughby, Ohio'],
    ['Lorain County, Ohio', 'Elyria, Ohio', 'Avon, Ohio'],
    ['Summit County, Ohio', 'Akron, Ohio'],
    ['Medina County, Ohio', 'Medina, Ohio', 'Brunswick, Ohio'],
    ['Geauga County, Ohio', 'Portage County, Ohio'],
]


def log(worker, task, output_file, status='Done'):
    ts = datetime.now().strftime('%Y-%m-%d %H:%M')
    line = f'[{ts}] {worker.capitalize()} | {task} | {output_file} | {status}\n'
    LOG_FILE.parent.mkdir(exist_ok=True)
    with open(LOG_FILE, 'a') as f:
        f.write(line)
    print(f'  → Logged: {line.strip()}')


def apollo_search(titles, locations, per_page=25):
    payload = json.dumps({
        'person_titles': titles,
        'person_locations': locations,
        'per_page': per_page,
    })
    try:
        result = subprocess.run(
            ['curl', '-s', '-X', 'POST',
             'https://api.apollo.io/api/v1/mixed_people/api_search',
             '-H', 'Content-Type: application/json',
             '-H', f'X-Api-Key: {APOLLO_KEY}',
             '-d', payload],
            capture_output=True, text=True, timeout=15
        )
        data = json.loads(result.stdout)
        if 'error' in data:
            print(f'  Apollo search error: {data["error"]}')
            return []
        return data.get('people', [])
    except json.JSONDecodeError as e:
        print(f'  Apollo search JSON parse error: {e} | Response: {result.stdout[:200]}')
        return []
    except Exception as e:
        print(f'  Apollo search failed: {e}')
        return []


def apollo_reveal(person_id, first_name, last_name, org_name):
    payload = json.dumps({
        'id': person_id,
        'first_name': first_name,
        'last_name': last_name,
        'organization_name': org_name,
        'reveal_personal_emails': False,
    })
    try:
        result = subprocess.run(
            ['curl', '-s', '-X', 'POST',
             'https://api.apollo.io/api/v1/people/match',
             '-H', 'Content-Type: application/json',
             '-H', f'X-Api-Key: {APOLLO_KEY}',
             '-d', payload],
            capture_output=True, text=True, timeout=10
        )
        data = json.loads(result.stdout)
        return data.get('person', {})
    except json.JSONDecodeError as e:
        print(f'  Apollo reveal JSON parse error: {e}')
        return {}
    except Exception as e:
        print(f'  Apollo reveal failed: {e}')
        return {}


def get_org_phone(org_id):
    try:
        result = subprocess.run(
            ['curl', '-s',
             f'https://api.apollo.io/api/v1/organizations/{org_id}',
             '-H', f'X-Api-Key: {APOLLO_KEY}'],
            capture_output=True, text=True, timeout=10
        )
        data = json.loads(result.stdout)
        return data.get('organization', {}).get('phone', '')
    except Exception:
        return ''


def load_existing_emails():
    """Load all emails already in the contacts cache to avoid duplicates."""
    if not CACHE_FILE.exists():
        return set()
    cache = json.loads(CACHE_FILE.read_text())
    return {c.get('email', '').lower() for c in cache.get('contacts', []) if c.get('email')}


def save_to_cache(new_contacts):
    """Append new contacts to the cache file."""
    if not new_contacts:
        return
    cache = json.loads(CACHE_FILE.read_text()) if CACHE_FILE.exists() else {'contacts': []}
    cache['contacts'].extend(new_contacts)
    cache['updated'] = time.time()
    CACHE_FILE.write_text(json.dumps(cache, indent=2))


def mixmax_enroll(lead, lead_type):
    """Enroll a single lead in the correct Mixmax sequence."""
    sys.path.insert(0, str(BASE_DIR))
    from integrations.mixmax import enroll_lead
    lead['_worker'] = 'danny' if lead_type == 'property_manager' else 'carla'
    return enroll_lead(lead)


def run_danny():
    print('\n🔵 Danny — Property Manager Lead Pull')
    existing = load_existing_emails()

    # Rotate county based on week number
    week_num = datetime.now().isocalendar()[1]
    search = DANNY_SEARCHES[week_num % len(DANNY_SEARCHES)]
    print(f'  County batch: {search["label"]}')

    people = apollo_search(DANNY_TITLES, search['counties'], per_page=25)
    print(f'  Found {len(people)} people from Apollo')

    new_leads = []
    for p in people:
        first   = p.get('first_name', '')
        last    = p.get('last_name_obfuscated', '').replace('*', '')
        org     = p.get('organization', {})
        org_name = org.get('name', '')

        # Reveal to get email + linkedin
        revealed = apollo_reveal(p['id'], first, last, org_name)
        email = revealed.get('email', '')
        if not email or email.lower() in existing:
            continue

        org_id = revealed.get('organization_id', '') or p.get('organization', {}).get('id', '')
        phone  = get_org_phone(org_id) if org_id else ''

        lead = {
            'first_name':   revealed.get('first_name', first),
            'last_name':    revealed.get('last_name', ''),
            'email':        email,
            'title':        revealed.get('title', p.get('title', '')),
            'company_name': org_name,
            'phone':        phone,
            'city':         revealed.get('city', ''),
            'state':        revealed.get('state', 'OH'),
            'linkedin_url': revealed.get('linkedin_url', ''),
            '_worker':      'danny',
            '_source':      f'Apollo — {search["label"]} — {datetime.now().strftime("%Y-%m-%d")}',
        }
        new_leads.append(lead)
        existing.add(email.lower())
        print(f'    + {lead["first_name"]} {lead["last_name"]} | {org_name} | {email}')
        time.sleep(0.3)  # rate limit

    print(f'  New unique leads: {len(new_leads)}')

    if new_leads:
        # Enroll in Mixmax
        enrolled = 0
        for lead in new_leads:
            result = mixmax_enroll(lead, 'property_manager')
            if result.get('status') == 'enrolled':
                lead['mixmax_enrolled'] = True
                lead['mixmax_sequence'] = result.get('sequence', '')
                enrolled += 1

        # Save to cache
        save_to_cache(new_leads)

        # Save output file
        date_str   = datetime.now().strftime('%Y-%m-%d')
        out_file   = f'leads_{search["label"].lower().replace("+","_")}_property_managers_{date_str}.md'
        out_path   = OUTPUTS / 'danny' / out_file
        out_path.parent.mkdir(exist_ok=True)

        lines = [
            f'# Property Manager Leads — {search["label"]}',
            f'### Apollo Pull | {datetime.now().strftime("%Y-%m-%d %H:%M")}',
            f'*Danny Malone | Outbound Sales Rep*',
            '',
            f'**Pulled:** {len(new_leads)} new leads',
            f'**Enrolled in Mixmax:** {enrolled}',
            '',
            '| Name | Title | Company | Email | Phone | LinkedIn |',
            '|------|-------|---------|-------|-------|---------|',
        ]
        for l in new_leads:
            li = l.get('linkedin_url', '') or '—'
            lines.append(f'| {l["first_name"]} {l["last_name"]} | {l["title"]} | {l["company_name"]} | {l["email"]} | {l.get("phone","—")} | {li} |')

        out_path.write_text('\n'.join(lines))
        log('danny', f'Apollo pull — {len(new_leads)} new property managers in {search["label"]}, {enrolled} enrolled in Mixmax', out_file)
        git_push('danny', f'Danny: lead pull {search["label"]} {date_str}')
        send_report_card(
            worker_name='danny',
            title='Lead Pull Complete',
            metrics=[
                ('New Leads', len(new_leads)),
                ('Enrolled', enrolled),
            ],
            summary_lines=[
                f'{len(new_leads)} property managers pulled — {search["label"]} county',
                f'{enrolled} enrolled in Mixmax sequence',
                f'View: {GITHUB_BASE}/outputs/danny/{out_file}',
            ],
            status='DONE',
        )
    else:
        log('danny', f'Apollo pull — {search["label"]} — no new leads found (all duplicates)', 'none', 'Done')
        send_report_card(
            worker_name='danny',
            title='Lead Pull — No New Leads',
            metrics=[
                ('New Leads', 0),
                ('Enrolled', 0),
            ],
            summary_lines=[f'No new leads in {search["label"]} this week — all duplicates.'],
            status='DONE',
        )

    return new_leads


def run_carla():
    print('\n🟣 Carla — Referral Partner Lead Pull')
    existing = load_existing_emails()

    week_num  = datetime.now().isocalendar()[1]
    locations = CARLA_COUNTY_ROTATION[week_num % len(CARLA_COUNTY_ROTATION)]
    print(f'  County batch: {locations[0]}')

    all_new = []
    for search in CARLA_SEARCHES:
        people = apollo_search(search['titles'], locations, per_page=15)
        print(f'  {search["label"]}: Found {len(people)} people')

        for p in people:
            first    = p.get('first_name', '')
            last     = p.get('last_name_obfuscated', '').replace('*', '')
            org      = p.get('organization', {})
            org_name = org.get('name', '')

            revealed = apollo_reveal(p['id'], first, last, org_name)
            email    = revealed.get('email', '')
            if not email or email.lower() in existing:
                continue

            org_id = revealed.get('organization_id', '')
            phone  = get_org_phone(org_id) if org_id else ''

            lead_type = 'realtor' if search['type'] == 'realtors' else 'contractor'
            lead = {
                'first_name':   revealed.get('first_name', first),
                'last_name':    revealed.get('last_name', ''),
                'email':        email,
                'title':        revealed.get('title', p.get('title', '')),
                'company_name': org_name,
                'phone':        phone,
                'city':         revealed.get('city', ''),
                'linkedin_url': revealed.get('linkedin_url', ''),
                '_worker':      'carla',
                '_lead_type':   lead_type,
                '_source':      f'Apollo — {search["label"]} — {datetime.now().strftime("%Y-%m-%d")}',
            }
            all_new.append(lead)
            existing.add(email.lower())
            print(f'    + {lead["first_name"]} {lead["last_name"]} | {org_name} | {email}')
            time.sleep(0.3)

    print(f'  Total new referral partners: {len(all_new)}')

    if all_new:
        enrolled = 0
        for lead in all_new:
            lt = lead.get('_lead_type', 'contractor')
            result = mixmax_enroll(lead, lt)
            if result.get('status') == 'enrolled':
                lead['mixmax_enrolled'] = True
                lead['mixmax_sequence'] = result.get('sequence', '')
                enrolled += 1

        save_to_cache(all_new)

        date_str = datetime.now().strftime('%Y-%m-%d')
        out_file = f'leads_referral_partners_{date_str}.md'
        out_path = OUTPUTS / 'carla' / out_file
        out_path.parent.mkdir(exist_ok=True)

        lines = [
            f'# Referral Partner Leads',
            f'### Apollo Pull | {datetime.now().strftime("%Y-%m-%d %H:%M")}',
            f'*Carla Reyes | Referral Partner Manager*',
            '',
            f'**Pulled:** {len(all_new)} new leads',
            f'**Enrolled in Mixmax:** {enrolled}',
            '',
            '| Name | Title | Company | Email | Phone | Type |',
            '|------|-------|---------|-------|-------|------|',
        ]
        for l in all_new:
            lines.append(f'| {l["first_name"]} {l["last_name"]} | {l["title"]} | {l["company_name"]} | {l["email"]} | {l.get("phone","—")} | {l.get("_lead_type","—")} |')

        out_path.write_text('\n'.join(lines))
        log('carla', f'Apollo pull — {len(all_new)} new referral partners, {enrolled} enrolled in Mixmax', out_file)
        git_push('carla', f'Carla: lead pull {date_str}')
        send_report_card(
            worker_name='carla',
            title='Lead Pull Complete',
            metrics=[
                ('New Leads', len(all_new)),
                ('Enrolled', enrolled),
            ],
            summary_lines=[
                f'{len(all_new)} referral partners pulled',
                f'{enrolled} enrolled in Mixmax sequences',
                f'View: {GITHUB_BASE}/outputs/carla/{out_file}',
            ],
            status='DONE',
        )

    return all_new


def get_mixmax_enrolled_emails():
    """Pull the set of emails currently confirmed in all 3 Mixmax sequences."""
    seq_ids = [
        '6a048cfc110bc620ca0f1aee',  # Property Managers
        '6a048cfba81429e5dfe55010',  # Realtors
        '6a048cfd624a5989a68ba16c',  # Contractors
    ]
    enrolled = set()
    for seq_id in seq_ids:
        url = f'https://api.mixmax.com/v1/sequences/{seq_id}/recipients?apiToken={MIXMAX_TOKEN}&limit=200'
        try:
            with urllib.request.urlopen(url, timeout=10) as resp:
                data = json.loads(resp.read())
            recs = data if isinstance(data, list) else data.get('results', [])
            for r in recs:
                email = (r.get('to') or {}).get('email', '') or r.get('email', '')
                if email:
                    enrolled.add(email.lower())
        except Exception:
            pass
    return enrolled


def verify_and_repair_enrollment():
    """
    After every pipeline run: cross-check the contacts cache against live
    Mixmax data and re-enroll anyone who slipped through the cracks.
    Runs automatically at the end of every lead pull.
    """
    print('\n🔍 Verifying Mixmax enrollment...')

    if not CACHE_FILE.exists():
        print('  No cache file — skipping.')
        return

    confirmed = get_mixmax_enrolled_emails()
    print(f'  Confirmed in Mixmax: {len(confirmed)}')

    cache = json.loads(CACHE_FILE.read_text())
    contacts = cache.get('contacts', [])

    # Find contacts with an email that aren't in Mixmax yet
    missing = [
        c for c in contacts
        if c.get('email') and c['email'].lower() not in confirmed
    ]
    print(f'  Missing from Mixmax: {len(missing)}')

    if not missing:
        print('  ✅ All contacts confirmed in Mixmax.')
        log('pipeline', 'Enrollment verification — all contacts confirmed', 'contacts_cache.json')
        return

    # Re-enroll missing contacts
    sys.path.insert(0, str(BASE_DIR))
    from integrations.mixmax import enroll_lead

    repaired = 0
    failed = 0
    for c in missing:
        result = enroll_lead(c)
        if result.get('status') == 'enrolled':
            c['mixmax_enrolled'] = True
            c['mixmax_sequence'] = result.get('sequence', '')
            repaired += 1
            print(f'  ↻ Re-enrolled: {c["first_name"]} {c["last_name"]} ({c["email"]})')
        else:
            failed += 1
            c['mixmax_enrolled'] = False  # mark accurately in cache
        time.sleep(0.3)

    # Save corrected cache
    CACHE_FILE.write_text(json.dumps(cache, indent=2))

    summary = f'Enrollment repair — {repaired} re-enrolled, {failed} failed (no email or rejected)'
    log('pipeline', summary, 'contacts_cache.json')
    print(f'\n  ✅ {repaired} re-enrolled | {failed} could not be enrolled')

    if repaired > 0:
        notify_slack(
            f'🔧 *Pipeline — Enrollment Repair*\n'
            f'>{repaired} contacts re-enrolled in Mixmax after verification check.\n'
            f'>{failed} contacts could not be enrolled (no email or rejected by Mixmax).'
        )


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'both'
    print(f'\n=== Forest City Lead Pipeline — {datetime.now().strftime("%Y-%m-%d %H:%M")} ===')

    if mode in ('danny', 'both'):
        run_danny()
    if mode in ('carla', 'both'):
        run_carla()

    # Always verify enrollment after pulling leads — catches any silent failures
    verify_and_repair_enrollment()

    print('\n✅ Lead pipeline complete.')
