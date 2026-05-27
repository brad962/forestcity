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
    # Multifamily segment — apartment complexes (added 2026-05-21)
    'multifamily manager', 'multifamily director', 'multifamily asset manager',
    'multifamily regional', 'apartment complex manager',
    # CAI-certified HOA titles and plural facilities form (added 2026-05-21 run 45)
    'community association manager', 'hoa director', 'facilities manager',
    # Standalone CAM variant — some professionals list just "association manager" (added 2026-05-22)
    'association manager',
    # Full spelling — 'condo manager' substring does NOT match 'condominium manager' (added 2026-05-22)
    'condominium manager',
    # In Danny search titles but was missing from routing — PM firms where director-level title is used
    'property management director',
    # managing partner / principal — small HOA/PM firm owners who list owner-level titles (added 2026-05-22)
    'managing partner',
    'principal',
    # Commercial/retail segment — leasing director and center manager are common at office/retail properties (added 2026-05-22)
    'leasing director',
    'center manager',
    # Additional PM title variants covering residential communities + commercial buildings (added 2026-05-23)
    'site manager',              # residential community site manager (common at large apartment/condo complexes)
    'community director',        # HOA community director (distinct from community manager)
    'building operations manager', # commercial PM ops title at office/industrial properties
    'property administrator',    # administrative PM role — often signs vendor contracts
    # Large national PM firms (Greystar, Lincoln Property, etc.) use this ops title (added 2026-05-25)
    'property operations manager',
    # CAI board-level HOA director — decision-maker at HOA management companies, distinct from 'community director' (added 2026-05-25)
    'community association director',
    # Self-storage segment — district managers oversee 3-5 facilities; one deal = multiple buildings (added 2026-05-25 run 87)
    'self storage manager', 'storage facility manager', 'self-storage manager',
    # Senior & assisted living — primary decision-maker titles; mirrors DANNY_TITLES (added 2026-05-26 run 94)
    # 'facility manager' already above; 'executive director' + 'facility administrator' are the titles Apollo surfaces
    # NOTE: 'administrator' was narrowed to 'facility administrator' (run 99) — 'administrator' alone matched
    # IT Administrator, Database Administrator, School Administrator etc. on manual imports (substring = 'administrator')
    'executive director', 'facility administrator', 'director of care', 'senior living director',
    # Word-order variants for correct routing on import (added 2026-05-26 run 95)
    'director of facilities', 'campus manager', 'facilities operations manager',
    # 'operations director' already above; 'director of operations' is a distinct non-matching word order (added 2026-05-26 run 97)
    'director of operations',
    # Hotels/motels — GMs are the vendor decision-makers; large parking lots + pool decks + facades (added 2026-05-26 run 98)
    'hotel general manager', 'hotel manager', 'hospitality manager',
    # Fitness centers & health clubs — large parking lots + building exteriors; chains have district/regional FMs (added 2026-05-26 run 99)
    'fitness center manager', 'health club manager', 'gym manager', 'fitness director',
    # Universities & private schools — facilities directors already in list; org routing catches campus FM contacts (added 2026-05-26 run 99)
    'campus facilities manager', 'director of campus operations',
    # Banks & credit unions — branch FMs + district managers sign vendor contracts for appearance-critical properties (added 2026-05-26 run 100)
    # NE Ohio Huntington/KeyBank/Fifth Third/PNC/Chase branches + local credit unions; parking + drive-through + exterior = recurring revenue
    'bank branch manager', 'branch facilities manager', 'district branch manager', 'credit union manager', 'branch operations manager',
    # Medical office & outpatient facilities — NE Ohio health system campuses (Cleveland Clinic, UH, MetroHealth outpatient sites) (added 2026-05-26 run 101)
    # Appearance = patient trust signal; FMs sign vendor contracts; large paved lots + brick facades + ADA ramps
    'medical facility manager', 'healthcare facility manager', 'medical office manager', 'clinic manager',
    'outpatient facilities manager', 'medical building manager',
    # Corporate/tech park FMs — campus operations managers oversee multiple buildings + shared parking (added 2026-05-26 run 101)
    'corporate facilities manager', 'campus operations manager', 'office park manager',
    # Grocery/supermarket chains — Giant Eagle, Heinen's, Marc's, Kroger, Aldi/Meijer in NE Ohio;
    # district FMs sign vendor contracts; high-traffic parking + drive-through pharmacy canopies + building exteriors (added 2026-05-27 run 104)
    'grocery district manager', 'supermarket facilities manager',
    # Distribution centers & logistics — NE Ohio freight hub (Amazon, UPS, FedEx, XPO, Sysco);
    # loading dock areas + building exteriors; OSHA compliance angle; district FMs sign multi-site contracts (added 2026-05-27 run 105)
    'distribution center manager', 'fulfillment center manager', 'warehouse manager',
    'logistics facility manager', 'dock manager', 'transportation facility manager',
    'warehouse operations manager', 'regional distribution manager',
    # Car dealerships — fixed ops directors and service directors manage lot maintenance + bay concrete;
    # 'general manager' already in list; adding dealership-specific decision-maker titles (added 2026-05-27 run 107)
    'fixed operations director', 'automotive service director', 'dealer principal',
    # Restaurants & QSR chains — drive-through canopies, parking lots, dumpster pads; district managers sign
    # multi-location vendor contracts for 5-20 locations; $16K-$48K/year per district deal (added 2026-05-27 run 106)
    'restaurant district manager', 'food service district manager', 'franchise operations manager',
    'restaurant facilities manager', 'qsr district manager', 'franchise district manager',
    # Event venues & banquet halls — appearance critical for event photos; venue directors sign vendor contracts (added 2026-05-27 run 108)
    'venue manager', 'event venue manager', 'banquet manager', 'event center manager',
    'venue director', 'venue operations manager', 'catering director', 'conference center manager',
    # Auto body & collision shops — OSHA/EPA compliance angle; district managers sign multi-location contracts (added 2026-05-27 run 108)
    'auto body shop manager', 'collision center manager', 'body shop manager',
    'collision shop manager', 'district collision manager', 'body shop district manager',
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
    # Deck and driveway trades — 'deck build' already matches 'deck builder' via substring;
    # 'driveway seal' already above; removed duplicates (added 2026-05-20, cleaned 2026-05-23)
    'asphalt seal', 'concrete seal',
    # Irrigation/sprinkler companies — in customers' yards constantly, high referral value (added 2026-05-22)
    'irrigation', 'sprinkler',
    # Tree service / arborists — visit properties constantly, see dirty roofs/siding; natural referral partner
    # NOTE: also in FLEET_KEYWORDS, but CONTRACTOR_TITLES is checked first — correct routing for Carla
    'tree service', 'tree care', 'arborist',
    # Home inspectors — trusted advisor at buyer/seller moment; sees dirty siding/roofs at every inspection (added 2026-05-24)
    'home inspector', 'property inspector', 'home inspection',
    # Solar installers — on roofs constantly, see algae/moss; homeowner is already in "invest in home" mode (added 2026-05-24)
    'solar installer', 'solar panel', 'solar installation',
    # Plumbers and electricians — in homes 2-4x/year, trusted advisor relationship, see dirty exteriors on every call (added 2026-05-26 run 88)
    'plumber', 'plumbing', 'electrician', 'electrical contractor',
]


GAS_STATION_KEYWORDS = [
    'gas station', 'convenience store', 'c-store', 'fuel station',
    'petroleum', 'speedway', 'circle k', 'sheetz', 'certifiedoil',
    'truenorth', 'open pantry', 'sunoco', 'marathon', "love's",
    'ferrellgas', '7-eleven', 'bellstore', 'campbell oil',
    # NE Ohio gas station chains with significant local presence (added 2026-05-25)
    'getgo', 'giant eagle fuel', 'bp station', 'shell station',
    'pilot flying j', 'pilot travel', 'kwik trip', 'citgo',
    'exxon', 'mobil', 'valero', 'fuel center',
    # NOTE: 'district manager' removed — too generic; non-gas-station DMs would mismatch.
    # Company name keywords are sufficient for routing.
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

    # Check PM titles first — they are more specific than realtor keywords.
    # 'real estate' in REALTOR_TITLES is a substring that would falsely match
    # any PM title-holder working at "XYZ Real Estate Management".
    for kw in PROPERTY_MANAGER_TITLES:
        if kw in combined:
            return 'property_manager'
    for kw in REALTOR_TITLES:
        if kw in combined:
            return 'realtor'
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

    ⚠️ INSTANTLY.AI OVERLAP: If any Instantly.ai campaigns are running against these
    same contacts, duplicate emails will trigger spam filters and kill reply rates.
    Before enrolling a Round 2 batch, confirm Instantly.ai campaigns a1c08c3d and
    626cd15d are PAUSED. Guide: outputs/vera/instantly_pause_guide_2026-05-22.md
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

    ⚠️ INSTANTLY.AI PAUSE REQUIRED: Set INSTANTLY_PAUSED=true in .env after pausing
    campaigns a1c08c3d + 626cd15d. Without this, duplicate emails → spam filters → 0 replies.
    """
    # Block enrollment if Instantly.ai pause not confirmed — prevents duplicate emails → spam → 0% reply rate
    if len(leads) > 5 and os.environ.get('INSTANTLY_PAUSED', '').lower() != 'true':
        if os.environ.get('INSTANTLY_OVERRIDE', '').lower() != 'true':
            print('🚫 ENROLLMENT BLOCKED — INSTANTLY.AI NOT CONFIRMED PAUSED')
            print('   Same contacts in both Instantly.ai + Mixmax = duplicate emails = spam = 0% reply rate.')
            print()
            print('   STEP 1: Go to app.instantly.ai → Campaigns')
            print('   STEP 2: Find a1c08c3d (PM Cuyahoga) + 626cd15d (Contractor Referral) → ⋮ → Pause')
            print('   STEP 3: Add  INSTANTLY_PAUSED=true  to your .env file')
            print()
            print('   Then re-run. Guide: outputs/vera/instantly_pause_guide_2026-05-22.md')
            print('   To bypass (not recommended): set  INSTANTLY_OVERRIDE=true  in .env')
            return {'enrolled': [], 'skipped': [], 'errors': [
                'Enrollment blocked — INSTANTLY_PAUSED not confirmed. '
                'Pause campaigns a1c08c3d + 626cd15d at app.instantly.ai, '
                'then add INSTANTLY_PAUSED=true to .env and re-run.'
            ]}
        else:
            print('⚠️  INSTANTLY.AI NOT PAUSED — bypassing block (INSTANTLY_OVERRIDE=true)')
            print()

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
