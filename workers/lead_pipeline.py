#!/usr/bin/env python3
"""
Lead Pipeline — Danny & Carla
Runs weekly. Pulls fresh leads from Apollo, deduplicates, enrolls in Mixmax.
Usage: python3 workers/lead_pipeline.py [danny|carla|both]
"""

import json
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

BASE_DIR   = Path(__file__).parent.parent.resolve()
OUTPUTS    = BASE_DIR / 'outputs'
LOG_FILE   = BASE_DIR / 'logs' / 'activity.log'
CACHE_FILE = BASE_DIR / 'contacts_cache.json'

APOLLO_KEY   = 'aKRZyBffyV7ScWVCuTXBjA'
MIXMAX_TOKEN = '3646d2be-c1be-44b7-b3ef-e7ea047cad83'

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
]

CARLA_SEARCHES = [
    {'type': 'contractors', 'titles': ['owner', 'president', 'founder'],
     'keywords': ['siding', 'exterior contractor', 'roofing', 'gutters', 'painting'],
     'label': 'Contractors'},
    {'type': 'realtors', 'titles': ['realtor', 'real estate agent', 'listing agent'],
     'keywords': [],
     'label': 'Realtors'},
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
    result = subprocess.run(
        ['curl', '-s', '-X', 'POST',
         'https://api.apollo.io/api/v1/mixed_people/api_search',
         '-H', 'Content-Type: application/json',
         '-H', f'X-Api-Key: {APOLLO_KEY}',
         '-d', payload],
        capture_output=True, text=True, timeout=15
    )
    data = json.loads(result.stdout)
    return data.get('people', [])


def apollo_reveal(person_id, first_name, last_name, org_name):
    payload = json.dumps({
        'id': person_id,
        'first_name': first_name,
        'last_name': last_name,
        'organization_name': org_name,
        'reveal_personal_emails': False,
    })
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


def get_org_phone(org_id):
    result = subprocess.run(
        ['curl', '-s',
         f'https://api.apollo.io/api/v1/organizations/{org_id}',
         '-H', f'X-Api-Key: {APOLLO_KEY}'],
        capture_output=True, text=True, timeout=10
    )
    data = json.loads(result.stdout)
    return data.get('organization', {}).get('phone', '')


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
    else:
        log('danny', f'Apollo pull — {search["label"]} — no new leads found (all duplicates)', 'none', 'Done')

    return new_leads


def run_carla():
    print('\n🟣 Carla — Referral Partner Lead Pull')
    existing = load_existing_emails()

    all_new = []
    for search in CARLA_SEARCHES:
        locations = ['Cleveland, Ohio', 'Northeast Ohio', 'Cuyahoga County, Ohio']
        people    = apollo_search(search['titles'], locations, per_page=15)
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

    return all_new


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'both'
    print(f'\n=== Forest City Lead Pipeline — {datetime.now().strftime("%Y-%m-%d %H:%M")} ===')

    if mode in ('danny', 'both'):
        run_danny()
    if mode in ('carla', 'both'):
        run_carla()

    print('\n✅ Lead pipeline complete.')
