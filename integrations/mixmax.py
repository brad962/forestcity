#!/usr/bin/env python3
"""
Mixmax integration for Forest City Power Washing.
Enrolls Apollo leads into the correct Mixmax sequence based on lead type.
"""

import json
import os
import urllib.request
import urllib.error
from pathlib import Path

# Load .env so MIXMAX_TOKEN can be overridden without touching this file
def _load_env():
    env_file = Path(__file__).parent.parent / '.env'
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                k, v = line.split('=', 1)
                os.environ.setdefault(k.strip(), v.strip())

_load_env()

MIXMAX_TOKEN = os.environ.get('MIXMAX_TOKEN', '')
BASE_URL = 'https://api.mixmax.com/v1'

# Sequence IDs (created 2026-05-12)
SEQUENCES = {
    'property_manager': {
        'id': '6a048cfc110bc620ca0f1aee',
        'name': 'Forest City Power Washing – NE Ohio Property Managers',
        'variables': ['firstName', 'company', 'propertyCount', 'Phone'],
    },
    'realtor': {
        'id': '6a048cfba81429e5dfe55010',
        'name': 'Forest City Power Washing – Pre‑Listing Referral Partnership',
        'variables': ['firstName', 'company', 'listingArea', 'recentListingAddress', 'Phone'],
    },
    'contractor': {
        'id': '6a048cfd624a5989a68ba16c',
        'name': 'Forest City Power Washing – $50 Referral Partner Sequence',
        'variables': ['recipientFirstName', 'recipientCompany', 'Phone'],
    },
    # PENDING — create in Mixmax UI then paste ID here
    # Name: Forest City Power Washing — Fleet Washing Outreach
    'fleet_washing': {
        'id': 'PENDING',
        'name': 'Forest City Power Washing — Fleet Washing Outreach',
        'variables': ['firstName', 'company', 'fleetType', 'Phone'],
    },
    # PENDING — create in Mixmax UI then paste ID here
    # Name: Forest City Power Washing — Gas Station & C-Store Outreach
    'gas_station': {
        'id': 'PENDING',
        'name': 'Forest City Power Washing — Gas Station & C-Store Outreach',
        'variables': ['firstName', 'company', 'Phone'],
    },
}

# Keywords for lead type detection
PROPERTY_MANAGER_TITLES = [
    'property manager', 'facility manager', 'community manager',
    'hoa manager', 'building manager', 'property management',
    'asset manager', 'portfolio manager', 'leasing manager',
    'apartment manager', 'condo manager', 'property supervisor',
    'building supervisor', 'residential manager', 'facilities director',
    'building superintendent', 'property director',
    # Multi-site decision-makers at larger management firms (added 2026-05-20)
    'regional manager', 'operations director', 'general manager',
]

REALTOR_TITLES = [
    'realtor', 'real estate agent', 'listing agent', 'buyers agent',
    'real estate', 'broker', 'realty',
]

CONTRACTOR_TITLES = [
    'contractor', 'siding', 'painter', 'painting', 'roofer', 'roofing',
    'gutter', 'landscap', 'remodel', 'construction', 'handyman',
    'window clean', 'concrete', 'deck build', 'deck contractor',
    'fence contractor', 'fence install', 'exterior clean', 'pressure wash',
    'driveway seal', 'power wash', 'janitorial', 'property maintenance',
    # Home-services referral partners added 2026-05-19 (Carla's new search categories)
    'chimney', 'hvac', 'heating', 'cooling', 'air condition', 'pool service',
    'pool clean', 'pest control', 'exterminator', 'junk removal', 'home clean',
    'maid', 'moving company', 'mover',
    # Deck and driveway trades — customer often books power washing same visit (added 2026-05-20)
    'deck builder', 'deck contractor', 'asphalt seal', 'driveway seal', 'concrete seal',
]


GAS_STATION_KEYWORDS = [
    'gas station', 'convenience store', 'c-store', 'fuel station',
    'petroleum', 'speedway', 'circle k', 'sheetz', 'certifiedoil',
    'truenorth', 'open pantry', 'sunoco', 'marathon', "love's",
    'ferrellgas', '7-eleven', 'bellstore', 'campbell oil',
    # NOTE: 'district manager' removed — too generic; non-gas-station DMs would mismatch.
    # Company name keywords (speedway, circle k, etc.) are sufficient for routing.
]

FLEET_KEYWORDS = [
    'fleet', 'tree service', 'tree care', 'arborist', 'trucking',
    'logistics', 'delivery', 'landscaping fleet', 'hvac fleet',
    'fleet manager', 'fleet supervisor', 'transportation manager',
    'equipment manager',
    # NOTE: 'operations manager' removed — too generic; nearly every company has one.
    # Specific fleet/transport titles are sufficient for routing.
    'fleet operations manager', 'transportation director', 'vehicle fleet',
]


def detect_lead_type(lead: dict) -> str:
    """Detect lead type from title/company. Returns sequence key from SEQUENCES."""
    # Honor explicit intent from pipeline
    explicit = lead.get('_lead_type', '')
    if explicit in SEQUENCES:
        return explicit

    title = (lead.get('title') or lead.get('personalization') or '').lower()
    company = (lead.get('company_name') or lead.get('organization') or '').lower()
    combined = f"{title} {company}"

    for kw in REALTOR_TITLES:
        if kw in combined:
            return 'realtor'
    for kw in PROPERTY_MANAGER_TITLES:
        if kw in combined:
            return 'property_manager'
    for kw in CONTRACTOR_TITLES:
        if kw in combined:
            return 'contractor'
    for kw in GAS_STATION_KEYWORDS:
        if kw in combined:
            return 'gas_station'
    for kw in FLEET_KEYWORDS:
        if kw in combined:
            return 'fleet_washing'

    # Default to property manager for Danny's campaign, contractor for Carla's
    worker = lead.get('_worker', '')
    if worker == 'danny':
        return 'property_manager'
    if worker == 'carla':
        return 'contractor'
    return 'property_manager'


def _sequence_is_live(lead_type: str) -> bool:
    """Returns True only if the sequence has a real Mixmax ID (not PENDING)."""
    seq = SEQUENCES.get(lead_type, {})
    return bool(seq.get('id')) and seq['id'] != 'PENDING'


def build_variables(lead: dict, lead_type: str) -> dict:
    """Build the variable map for a given lead and sequence type."""
    first_name = lead.get('first_name', '') or 'there'  # prevents "Hi ," if Apollo returns blank
    last_name = lead.get('last_name', '')
    company = lead.get('company_name') or lead.get('organization') or ''
    phone = lead.get('phone', '')
    city = lead.get('city', 'Northeast Ohio')

    # Phone fallback — some contacts don't have a direct number
    phone_display = phone if phone else 'N/A'

    if lead_type == 'property_manager':
        return {
            'firstName': first_name,
            'company': company,
            'propertyCount': 'your properties',
            'Phone': phone_display,
        }
    elif lead_type == 'realtor':
        return {
            'firstName': first_name,
            'company': company,
            'listingArea': city or 'Northeast Ohio',
            'recentListingAddress': '',
            'Phone': phone_display,
        }
    elif lead_type == 'contractor':
        return {
            'recipientFirstName': first_name,
            'recipientCompany': company,
            'Phone': phone_display,
        }
    elif lead_type == 'fleet_washing':
        return {
            'firstName': first_name,
            'company': company,
            'fleetType': lead.get('fleet_type', 'vehicles'),
            'Phone': phone_display,
        }
    elif lead_type == 'gas_station':
        return {
            'firstName': first_name,
            'company': company,
            'Phone': phone_display,
        }
    return {}


def enroll_lead(lead: dict) -> dict:
    """
    Enroll a single lead in the correct Mixmax sequence.
    Returns a result dict with status, sequence_name, and any errors.
    """
    email = lead.get('email', '').strip()
    if not email:
        return {'status': 'skipped', 'reason': 'no email'}

    lead_type = detect_lead_type(lead)

    # Skip sequences that haven't been created in Mixmax yet
    if not _sequence_is_live(lead_type):
        return {'status': 'skipped', 'reason': f'{lead_type} sequence not yet live — add Mixmax ID to integrations/mixmax.py'}

    sequence = SEQUENCES[lead_type]
    variables = build_variables(lead, lead_type)

    payload = json.dumps({
        'recipients': [{
            'email': email,
            'variables': variables,
        }]
    }).encode()

    url = f"{BASE_URL}/sequences/{sequence['id']}/recipients?apiToken={MIXMAX_TOKEN}"

    try:
        req = urllib.request.Request(
            url,
            data=payload,
            headers={'Content-Type': 'application/json'},
            method='POST'
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())

        recipients = data.get('recipients', [])
        if not recipients:
            return {
                'status': 'error',
                'email': email,
                'lead_type': lead_type,
                'sequence': sequence['name'],
                'errors': ['Empty recipients response — contact rejected by Mixmax'],
            }
        r = recipients[0]
        if r.get('status') == 'error':
            return {
                'status': 'error',
                'email': email,
                'lead_type': lead_type,
                'sequence': sequence['name'],
                'errors': r.get('errors', []),
            }
        return {
            'status': 'enrolled',
            'email': email,
            'lead_type': lead_type,
            'sequence': sequence['name'],
        }

    except urllib.error.HTTPError as e:
        body = e.read().decode()
        return {'status': 'error', 'email': email, 'errors': [f'HTTP {e.code}: {body[:200]}']}
    except Exception as e:
        return {'status': 'error', 'email': email, 'errors': [str(e)]}


def enroll_batch(leads: list, skip_existing: bool = True) -> dict:
    """
    Enroll a list of leads. Tracks results by status.
    Returns summary dict.
    """
    results = {'enrolled': [], 'skipped': [], 'errors': []}

    for lead in leads:
        # Skip leads already enrolled (check workflow flag in lead dict)
        if skip_existing and lead.get('mixmax_enrolled'):
            results['skipped'].append(lead.get('email', ''))
            continue

        result = enroll_lead(lead)

        if result['status'] == 'enrolled':
            results['enrolled'].append(result)
            lead['mixmax_enrolled'] = True
            lead['mixmax_sequence'] = result['sequence']
            lead['mixmax_lead_type'] = result['lead_type']
        elif result['status'] == 'skipped':
            results['skipped'].append(result)
        else:
            results['errors'].append(result)

    return results


def get_sequence_recipients(sequence_type: str) -> list:
    """Pull current recipients from a sequence. Returns a list (normalizes dict responses)."""
    if sequence_type not in SEQUENCES:
        return []
    seq_id = SEQUENCES[sequence_type]['id']
    if seq_id == 'PENDING':
        return []
    url = f"{BASE_URL}/sequences/{seq_id}/recipients?apiToken={MIXMAX_TOKEN}&limit=200"
    try:
        with urllib.request.urlopen(url, timeout=10) as resp:
            data = json.loads(resp.read())
        if isinstance(data, list):
            return data
        return data.get('results', data.get('recipients', []))
    except Exception:
        return []


def get_all_sequences() -> list:
    """Pull all sequences from the account."""
    url = f"{BASE_URL}/sequences?apiToken={MIXMAX_TOKEN}"
    try:
        with urllib.request.urlopen(url, timeout=10) as resp:
            data = json.loads(resp.read())
            return data.get('results', [])
    except Exception:
        return []


if __name__ == '__main__':
    # Test: enroll one lead
    test_lead = {
        'first_name': 'Test',
        'last_name': 'Delete',
        'email': 'test_delete@mailinator.com',
        'company_name': 'Test Property Management',
        'title': 'Property Manager',
        'phone': '216-555-0000',
        '_worker': 'danny',
    }
    result = enroll_lead(test_lead)
    print(json.dumps(result, indent=2))
