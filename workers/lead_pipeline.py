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

BASE_DIR    = Path(__file__).parent.parent.resolve()
OUTPUTS     = BASE_DIR / 'outputs'
LOG_FILE    = BASE_DIR / 'logs' / 'activity.log'
CACHE_FILE  = BASE_DIR / 'contacts_cache.json'
PIPELINE_F  = BASE_DIR / 'pipeline_data.json'

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
    'asset manager', 'portfolio manager', 'leasing manager',
    'facilities director', 'building superintendent', 'building supervisor',
    'apartment manager', 'condo manager', 'property supervisor',
    'residential manager', 'property director',
    # Multi-site decision-makers at larger management firms
    'regional manager', 'operations director', 'general manager',
    # Multifamily-specific titles (added 2026-05-21 — large apt complex segment)
    'multifamily manager', 'multifamily director', 'multifamily asset manager',
    'multifamily regional manager', 'apartment complex manager',
    # CAI-certified HOA titles and plural facilities form (added 2026-05-21 run 45)
    'community association manager', 'hoa director', 'facilities manager',
    # Standalone CAM variant — added 2026-05-22 to match mixmax.py routing
    'association manager',
    # Full spelling — 'condo manager' substring does NOT match 'condominium manager' (added 2026-05-22)
    'condominium manager',
    # Decision-makers at small HOA/PM firms who list owner/founder titles, not PM titles (added 2026-05-22 run 52)
    'managing partner', 'principal',
    # Commercial/retail property segment — office buildings, shopping centers (added 2026-05-22 run 56)
    'leasing director',    # large multifamily/office leasing director — distinct from leasing manager
    'center manager',      # shopping center manager — common title at retail property groups
    # Additional PM title variants covering residential communities + commercial buildings (added 2026-05-23)
    'site manager',              # residential community site manager
    'community director',        # HOA community director (distinct from community manager)
    'building operations manager', # commercial PM ops title at office/industrial properties
    'property administrator',    # administrative PM role — often signs vendor contracts
    # Large national PM firms (Greystar, Lincoln Property, etc.) use this ops title (added 2026-05-25)
    'property operations manager',
    # CAI board-level HOA director — decision-maker at HOA firms (added 2026-05-25)
    'community association director',
    # Self-storage segment — district/facility managers oversee multiple properties (added 2026-05-25 run 87)
    'self storage manager', 'storage facility manager', 'self-storage manager',
    # Senior & assisted living — top decision-maker titles missing from search (added 2026-05-26 run 94)
    # 'facility manager' already above; 'executive director' + 'facility administrator' are the primary titles at
    # senior living, memory care, and skilled nursing facilities — without these Apollo returns nothing
    # NOTE: narrowed 'administrator' → 'facility administrator' (run 99) — 'administrator' is too broad a
    # substring; would match IT Administrator, Database Administrator, etc. in Apollo results
    'executive director', 'facility administrator', 'director of care', 'senior living director',
    # Word-order variants — 'facilities director' does NOT substring-match 'director of facilities' (added 2026-05-26 run 95)
    'director of facilities',         # reverse word order of 'facilities director'; different substring
    'campus manager',                  # university/corporate campus FM; large paved areas + buildings = high-value accounts
    'facilities operations manager',   # ops-level FM at large commercial/industrial properties
    # 'operations director' already above, but 'director of operations' is a distinct word-order variant (added 2026-05-26 run 97)
    'director of operations',
    # Hotels/motels — GMs run the property like a facility manager; large parking lots + pool decks + building facades (added 2026-05-26 run 98)
    'hotel general manager', 'hotel manager', 'hospitality manager',
    # Fitness centers & health clubs — district/regional FMs at chains (Planet Fitness, LA Fitness, Anytime) (added 2026-05-26 run 99)
    # NE Ohio has 50+ chain fitness centers; large parking lots + building exteriors; GMs sign vendor contracts
    'fitness center manager', 'health club manager', 'gym manager', 'fitness director',
    # Universities/private schools — campus facilities; campus manager already above; director of campus ops variant (added 2026-05-26 run 99)
    'campus facilities manager', 'director of campus operations',
    # Banks & credit unions — branch FMs + district managers oversee 3-10+ branches; parking lots + drive-throughs + building exteriors (added 2026-05-26 run 100)
    # NE Ohio: Huntington, KeyBank, Fifth Third, PNC, Chase + local credit unions = hundreds of branches; appearance standard = brand requirement; one district deal = multi-site revenue
    'bank branch manager', 'branch facilities manager', 'district branch manager', 'credit union manager', 'branch operations manager',
    # Medical office & healthcare facilities — NE Ohio health systems run dozens of outpatient campuses (added 2026-05-26 run 101)
    # Large paved lots + brick facades + ADA ramps; patient-facing appearance = FM priority; FMs sign vendor contracts
    'medical facility manager', 'healthcare facility manager', 'medical office manager', 'clinic manager',
    'outpatient facilities manager', 'medical building manager',
    # Corporate/tech parks — campus FMs oversee multiple buildings + shared parking; professional exterior standard (added 2026-05-26 run 101)
    # 'campus manager' already in list above; adding specific variants for corporate/tech park context
    'corporate facilities manager', 'campus operations manager', 'office park manager',
    # Grocery/supermarket chains — district FM-level contacts sign vendor contracts across multiple stores (added 2026-05-27 run 104)
    # 'facilities manager' + 'district manager' already in list; adding grocery-specific variants Apollo surfaces
    'grocery district manager', 'supermarket facilities manager',
    # Distribution centers & logistics — NE Ohio is a major freight hub (Amazon, UPS, FedEx, XPO, Sysco, GFS);
    # loading dock areas accumulate oil, grease, fuel, food residue = recurring high-priority cleaning;
    # OSHA compliance angle: loading docks must be clean for forklift safety + food safety audits;
    # district/regional FMs sign multi-site contracts; large facilities = $2K-$6K/visit; 4x/year = $8K-$24K/facility (added 2026-05-27 run 105)
    'distribution center manager', 'fulfillment center manager', 'warehouse manager',
    'logistics facility manager', 'dock manager', 'transportation facility manager',
    'warehouse operations manager', 'regional distribution manager',
    # Car dealerships — fixed ops and service directors manage vehicle service bays + large paved lots;
    # 'general manager' already in list; adding dealership-specific titles not matched by existing entries (added 2026-05-27 run 107)
    'fixed operations director',    # dealership-specific: oversees service + parts; parking lot + service bay concrete = recurring wash
    'automotive service director',  # variant; signs vendor contracts for lot maintenance
    'dealer principal',             # owner/operator of single-rooftop dealership; lot + showroom exterior standard
    # Restaurants & QSR chains — McDonald's, Burger King, Wendy's, Taco Bell, Panera, Chipotle, Applebee's, Bob Evans in NE Ohio;
    # drive-through canopies accumulate grease, mildew, exhaust; parking lots have heavy traffic stains + dumpster pad grime;
    # district managers sign vendor contracts for 5-20 locations; $400-$1,200/location visit; quarterly = $1.6K-$4.8K/location;
    # 10-location district deal = $16K-$48K/year; first pull Medina June 1 (added 2026-05-27 run 106)
    'restaurant district manager', 'food service district manager', 'franchise operations manager',
    'restaurant facilities manager', 'qsr district manager', 'franchise district manager',
    # Event venues & banquet halls — NE Ohio spring/summer wedding season peaks May-June; Landerhaven, Emerald Event Center,
    # Hilton Cleveland ballrooms, Sheraton Suites, standalone wedding barns; large parking lots + building exteriors +
    # outdoor patios + ceremony areas must look pristine (event photos are permanent); venue directors sign vendor contracts;
    # 2-4 visits/year (pre-wedding season + post-summer cleanup); $1,500-$5,000/visit; $3K-$8K/year per venue (added 2026-05-27 run 108)
    'venue manager', 'event venue manager', 'banquet manager', 'event center manager',
    'venue director', 'venue operations manager', 'catering director', 'conference center manager',
    # Auto body & collision shops — large concrete aprons + building exteriors accumulate oil, paint overspray, chemical residue;
    # OSHA/EPA compliance angle; Maaco, CARSTAR, Caliber Collision, Crash Champions have district managers signing vendor contracts;
    # $800-$2,500/shop; district manager oversees 5-15 locations = $4K-$37K/year deal; zero current competitors (added 2026-05-27 run 108)
    'auto body shop manager', 'collision center manager', 'body shop manager',
    'collision shop manager', 'district collision manager', 'body shop district manager',
    # HOA board-level decision-makers — boards vote on vendor contracts + annual budgets in May-June;
    # DIFFERENT from HOA managers (management company employees) — these ELECTED VOLUNTEERS sign the checks;
    # self-managed HOAs have NO management company; board president is the only decision-maker;
    # Apollo surfaces these at HOA/condo association orgs (added 2026-05-27 run 109)
    'hoa president', 'hoa board president', 'community association president',
    'hoa treasurer', 'hoa board treasurer',
    'condo board president', 'condominium board president',
    # Marinas & waterfront properties — Lake Erie shoreline (Vermilion, Lorain, Sandusky Bay, Mentor Headlands, Lakewood);
    # concrete boat ramps, dock areas, storage buildings, parking lots = pressure washing need all season;
    # May-June = peak pre-season marina prep; marina managers sign vendor contracts;
    # $1,500-$6,000/visit; 2-3x/year = $3K-$18K/year per marina; zero competitors targeting this (added 2026-05-27 run 109)
    'marina manager', 'marina director', 'harbor master', 'waterfront facilities manager',
    'marina operations manager', 'dock master',
    # Churches & religious facilities — 500+ large NE Ohio parishes + evangelical megachurch campuses;
    # large parking lots + brick facades + outdoor areas; church administrator or facilities director signs vendor contracts;
    # $1,000-$3,000/visit; 2-3x/year = $2K-$9K/year per campus (added 2026-05-27 run 110)
    'church facilities manager', 'parish administrator', 'religious facilities manager',
    'church administrator', 'facilities coordinator', 'director of facilities management',
    # Childcare & early education — licensing inspections create recurring urgency; director signs vendor contracts;
    # NE Ohio has 1,000+ licensed centers; parking + entrance + playground = recurring need; $300-$800/visit; 2x/year (added 2026-05-27 run 110)
    'childcare center director', 'daycare director', 'early childhood director',
    'childcare director', 'preschool director', 'early learning director',
]

# Org-level keywords passed to Apollo q_organization_keyword_tags.
# Catches companies where the decision-maker's title isn't explicitly "property manager"
# but the company clearly operates in that space (e.g. "owner" at an HOA management firm).
DANNY_ORG_KEYWORDS = [
    'property management', 'association management', 'hoa management',
    'community management', 'apartment management', 'condo management',
    'real estate management', 'facilities management',
    # Commercial RE segment — office/retail/warehouse buildings with facility managers
    'commercial real estate', 'commercial property management',
    # Multifamily segment — apartment complexes, large multi-unit residential (added 2026-05-21)
    'multifamily', 'multi-family', 'multifamily housing', 'apartment complex',
    'residential portfolio',
    # Condo/HOA association management (added 2026-05-22)
    'condominium management', 'condo association', 'condominium association',
    # Commercial/retail property segment (added 2026-05-22 run 56)
    'shopping center management', 'office building management',
    'retail property management', 'commercial building management',
    # Self-storage facilities — large concrete pads + metal building facades = recurring soft-wash accounts (added 2026-05-25 run 87)
    'self storage', 'self-storage', 'storage facility', 'storage units',
    # Car dealerships — large paved lots + building exteriors; facility managers + GMs are decision-makers (added 2026-05-26 run 88)
    'car dealership', 'auto dealership', 'automotive dealer', 'auto group', 'car dealer',
    # Parking + industrial segments — high square footage of concrete/asphalt; recurring pressure washing demand (added 2026-05-25 run 89)
    'parking management', 'parking facility', 'parking garage', 'industrial park', 'business park',
    # Senior & assisted living — brick facades with algae, concrete walkways, ADA compliance = quarterly soft-wash need (added 2026-05-26 run 93)
    'senior living', 'assisted living', 'memory care', 'skilled nursing', 'retirement community',
    'independent living', 'continuing care', 'senior housing', 'assisted care',
    # Hotels/motels — large parking lots, pool decks, pool surrounds, exterior facades, covered walkways (added 2026-05-26 run 98)
    # NE Ohio has ~200 hotels in 7 counties; one contract = $3K–$8K/year; GMs sign vendor contracts
    # 'lodging management' + 'hotel group' + 'motel chain' added run 102 — catches hotel companies not tagged as 'hotel management' in Apollo
    'hotel management', 'hospitality management', 'hotel chain', 'extended stay', 'motel management',
    'lodging management', 'lodging facilities', 'hotel group', 'motel chain', 'resort management',
    # Fitness centers & health clubs — Planet Fitness, LA Fitness, Anytime, snap fitness; large lots + building exteriors (added 2026-05-26 run 99)
    # NE Ohio has 50+ chain gyms; district managers oversee 3-8 locations; one deal = multi-site recurring revenue
    'fitness center', 'health club', 'fitness club', 'gym management', 'athletic club',
    # Universities & private schools — large campuses, parking structures, athletic facilities (added 2026-05-26 run 99)
    # Private schools (St. Ignatius, Padua, Walsh Jesuit) + universities (JCU, BW, Ursuline) sign vendor contracts directly
    'private school', 'independent school', 'university facilities', 'college campus',
    # Banks & credit unions — NE Ohio has 300+ bank branches (Huntington, KeyBank, Fifth Third, PNC, Chase) + 50+ credit unions (added 2026-05-26 run 100)
    # Each branch: parking lot + drive-through canopy + building exterior + ATM pad; appearance is brand standard not optional
    # District managers oversee 3-10+ branches; one deal = multi-site recurring; $500-$1,500/branch quarterly = $6K-$24K/year per district manager
    'bank branch', 'credit union', 'banking facilities', 'bank facilities management',
    # Medical office parks & outpatient facilities — NE Ohio health systems (Cleveland Clinic, UH, MetroHealth, Summa) have dozens of
    # outpatient campuses along Routes 82/303/91/422; large paved lots, brick facades, ADA ramps, covered drop-off areas;
    # appearance standard = patient trust signal; facility managers sign vendor contracts; $800–$2,500/visit; quarterly = $3K–$10K/year (added 2026-05-26 run 101)
    'medical office', 'medical plaza', 'medical park', 'outpatient facility', 'healthcare facility', 'medical building',
    'outpatient center', 'medical campus', 'physician office', 'specialty clinic',
    # Corporate & technology parks — Chagrin Highlands, Bishop Trautman Business Park, Tiedeman, Great Northern;
    # multiple buildings per park, shared parking lots, professional exterior standard = vendor contract;
    # campus facilities manager oversees all buildings; $1,500–$5,000/visit for full campus (added 2026-05-26 run 101)
    'corporate campus', 'corporate park', 'technology park', 'office complex', 'office campus',
    'tech park', 'business campus', 'innovation campus',
    # Grocery & supermarket chains — Giant Eagle (200+ regional stores), Heinen's (23 NE Ohio), Marc's (64),
    # Aldi, Kroger, Meijer; large parking lots with heavy cart traffic = oil stains, gum, tire marks;
    # drive-through pharmacy canopies; building exteriors; district FMs sign vendor contracts across 5-15 locations;
    # $600–$2,000/store visit; 10-store district deal = $6K–$20K/year (added 2026-05-27 run 104)
    'grocery store', 'supermarket chain', 'grocery chain', 'food retail', 'grocery management',
    'supermarket management',
    # Distribution centers & logistics facilities — NE Ohio is a primary freight hub for the Midwest;
    # Amazon (multiple fulfillment/distribution centers near CLE/Akron), UPS Worldport feeder hubs,
    # FedEx Ground stations, XPO Logistics, Saia, Old Dominion, Sysco/Gordon Food Service distribution;
    # loading dock concrete + building exteriors accumulate oil, fuel, food residue = recurring soft-wash/pressure-wash;
    # OSHA compliance: forklift safety + food safety audits require clean dock areas;
    # $2K-$6K/visit for large facility; 4 visits/year = $8K-$24K/facility; district FMs oversee multiple sites (added 2026-05-27 run 105)
    'distribution center', 'fulfillment center', 'warehouse operations', 'logistics center',
    'shipping facility', 'freight terminal', 'loading dock facility', 'transportation hub',
    'food distribution', 'beverage distribution', 'wholesale distribution',
    # Restaurants & QSR chains — heavy NE Ohio saturation of McDonald's, Burger King, Wendy's, Taco Bell,
    # Panera, Chipotle, Applebee's, Bob Evans, Cracker Barrel; drive-through canopies, parking lots, dumpster pads;
    # franchisees and district managers sign multi-location vendor contracts;
    # $400-$1,200/location; quarterly = $1.6K-$4.8K/location; 10-location district deal = $16K-$48K/year (added 2026-05-27 run 106)
    'restaurant chain', 'fast food franchise', 'food service management', 'restaurant franchise',
    'quick service restaurant', 'restaurant management', 'qsr management', 'casual dining',
    # Event venues & banquet halls — NE Ohio wedding season peaks May-June; Landerhaven, Emerald, Hilton Cleveland,
    # Sheraton Suites, wedding barns; large parking lots + outdoor patios + building exteriors = curb appeal is non-negotiable;
    # venue directors sign vendor contracts; one contract = $3K-$8K/year (added 2026-05-27 run 108)
    'event venue', 'banquet hall', 'wedding venue', 'event center', 'conference center',
    'banquet facility', 'event facility', 'wedding reception',
    # Auto body & collision shops — large concrete aprons accumulate oil, paint overspray, chemical residue;
    # Maaco, CARSTAR, Caliber Collision, Crash Champions district managers sign vendor contracts (added 2026-05-27 run 108)
    'auto body shop', 'body shop', 'collision center', 'collision repair', 'auto body',
    'auto collision', 'vehicle collision',
    # Marinas & waterfront properties — Lake Erie shoreline (Vermilion, Lorain, Sandusky Bay, Mentor Headlands);
    # NE Ohio has dozens of marinas and yacht clubs; pre-season prep (May-June) = concrete ramps, dock areas, storage lots;
    # marina manager signs vendor contracts; $1,500-$6,000/visit; 2-3x/year; zero competitors; LOCAL LAKE ERIE ADVANTAGE (added 2026-05-27 run 109)
    'marina management', 'marine services', 'boat storage', 'yacht club', 'sailing club',
    'waterfront property', 'marina facility', 'boat launch',
    # Churches & religious facilities — NE Ohio has 500+ large churches (Catholic diocesan campuses, evangelical megachurches,
    # East Side Christian, Westside, Crossroads NE Ohio campuses); large parking lots, brick facades, educational wings,
    # outdoor ceremony/picnic areas; facilities director or church administrator signs vendor contracts;
    # one contract = multiple campus buildings; $1,000-$3,000/visit; 2-3x/year = $2K-$9K/year per campus (added 2026-05-27 run 110)
    'church campus', 'religious organization', 'faith community', 'church facilities', 'parish management',
    'diocese facilities', 'religious campus', 'church property',
    # Childcare & early education facilities — May-June = summer program prep; licensing inspections require clean exteriors;
    # NE Ohio has 1,000+ licensed daycare and preschool centers; director signs vendor contracts directly;
    # parking lot + entrance walkways + playground area = recurring cleaning need; $300-$800/visit; 2x/year (added 2026-05-27 run 110)
    'childcare center', 'daycare center', 'early childhood education', 'child care management',
    'preschool facility', 'early learning center',
]

CARLA_SEARCHES = [
    {'type': 'contractors', 'titles': ['owner', 'president', 'founder'],
     'keywords': ['siding', 'exterior contractor', 'roofing', 'gutters', 'painting',
                  'landscaping', 'lawn care', 'window washing', 'window cleaning',
                  'chimney', 'concrete', 'deck builder', 'deck contractor',
                  'asphalt sealing', 'driveway sealing',
                  'irrigation', 'sprinkler system', 'lawn irrigation',
                  'tree service', 'tree care', 'arborist',
                  'home inspection', 'home inspector',  # at buyer/seller moment; sees dirty houses every job
                  'solar installation', 'solar energy',  # on roofs constantly; homeowner in invest-in-home mode
                  'plumbing', 'plumber',                 # in homes 2-4x/year; trusted advisor; sees every exterior surface
                  'electrician', 'electrical contractor',  # same reasoning; high referral value (added 2026-05-26)
                  # Snow removal companies — completely idle in May-June; actively seeking summer revenue;
                  # service the same driveways, parking lots, and commercial lots Forest City washes;
                  # high referral value because they're the trusted off-season contractor relationship (added 2026-05-27 run 107)
                  'snow removal', 'snow plowing', 'snow plow', 'ice management',
                  'winter maintenance', 'snow and ice', 'snow clearing'],
     'label': 'Contractors'},
    # Home-services companies that visit properties weekly — high-value referral sources
    {'type': 'contractors', 'titles': ['owner', 'president', 'founder', 'operator'],
     'keywords': ['hvac', 'heating cooling', 'air conditioning', 'pool service',
                  'pool cleaning', 'pest control', 'home cleaning', 'junk removal',
                  'moving company'],
     'label': 'Home Services'},
    {'type': 'realtors', 'titles': ['realtor', 'real estate agent', 'listing agent',
                                     'real estate broker', 'buyers agent'],
     'keywords': ['real estate', 'realty', 'brokerage', 'keller williams', 'coldwell banker',
                  'century 21', 're/max', 'howard hanna', 'exp realty', 'compass'],
     'label': 'Realtors'},
    # HOA management companies — owner/president manages 5–50+ HOAs; one deal = many recurring jobs
    # Different from Danny's individual PM targets — Carla builds a referral relationship with the COMPANY
    {'type': 'contractors', 'titles': ['owner', 'president', 'founder', 'principal', 'managing director'],
     'keywords': ['association management', 'hoa management', 'community management',
                  'property association', 'homeowners association management',
                  'condominium management', 'condo association', 'community association'],
     'label': 'HOA Management Companies'},
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
CARLA_COUNTY_LABELS = ['Cuyahoga', 'Lake', 'Lorain', 'Summit', 'Medina', 'Geauga+Portage']


def log(worker, task, output_file, status='Done'):
    ts = datetime.now().strftime('%Y-%m-%d %H:%M')
    line = f'[{ts}] {worker.capitalize()} | {task} | {output_file} | {status}\n'
    LOG_FILE.parent.mkdir(exist_ok=True)
    with open(LOG_FILE, 'a') as f:
        f.write(line)
    print(f'  → Logged: {line.strip()}')


def apollo_search(titles, locations, per_page=25, keywords=None):
    body = {
        'person_titles': titles,
        'person_locations': locations,
        'per_page': per_page,
    }
    if keywords:
        body['q_organization_keyword_tags'] = keywords
    payload = json.dumps(body)
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
            err = data['error']
            if 'rate' in str(err).lower() or '429' in str(err):
                print(f'  Apollo search rate-limited (429) — will retry next run: {err}')
            else:
                print(f'  Apollo search error: {err}')
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
    try:
        cache = json.loads(CACHE_FILE.read_text())
    except (json.JSONDecodeError, Exception):
        print('  ⚠️ contacts_cache.json malformed — treating as empty (no duplicates skipped).')
        return set()
    return {c.get('email', '').lower() for c in cache.get('contacts', []) if c.get('email')}


def save_to_cache(new_contacts):
    """Append new contacts to the cache file."""
    if not new_contacts:
        return
    if CACHE_FILE.exists():
        try:
            cache = json.loads(CACHE_FILE.read_text())
        except (json.JSONDecodeError, Exception):
            print('  ⚠️ contacts_cache.json was malformed — starting fresh.')
            cache = {'contacts': []}
    else:
        cache = {'contacts': []}
    cache['contacts'].extend(new_contacts)
    cache['updated'] = time.time()
    CACHE_FILE.write_text(json.dumps(cache, indent=2))


def mixmax_enroll(lead, lead_type):
    """Enroll a single lead in the correct Mixmax sequence."""
    sys.path.insert(0, str(BASE_DIR))
    from integrations.mixmax import enroll_lead
    lead['_worker'] = 'carla' if lead_type in ('contractor', 'realtor') else 'danny'
    lead['_lead_type'] = lead_type  # Ensure detect_lead_type honors pipeline intent
    return enroll_lead(lead)


def _write_danny_sentinel():
    """Write today's date to a sentinel file so vera_relay can detect Danny staleness without log-parsing."""
    try:
        sentinel = BASE_DIR / 'outputs' / 'vera' / '.danny_last_pull_date'
        sentinel.parent.mkdir(exist_ok=True)
        sentinel.write_text(datetime.now().strftime('%Y-%m-%d'))
    except Exception:
        pass


def _write_carla_sentinel():
    """Write today's date to a sentinel file so vera_relay can detect Carla staleness without log-parsing."""
    try:
        sentinel = BASE_DIR / 'outputs' / 'vera' / '.carla_last_pull_date'
        sentinel.parent.mkdir(exist_ok=True)
        sentinel.write_text(datetime.now().strftime('%Y-%m-%d'))
    except Exception:
        pass


def run_danny(county_override=None):
    print('\n🔵 Danny — Property Manager Lead Pull')
    existing = load_existing_emails()

    # Rotate county based on week number; --county override forces a specific batch
    if county_override:
        # Flexible match: substring of label (case-insensitive) — handles "Summit", "Geauga", "Cuyahoga"
        search = next(
            (s for s in DANNY_SEARCHES if county_override.lower() in s['label'].lower()),
            None
        )
        if search:
            print(f'  County batch: {search["label"]} [MANUAL OVERRIDE]')
        else:
            valid = ', '.join(s['label'] for s in DANNY_SEARCHES)
            print(f'  ⚠️ County "{county_override}" not found. Valid values: {valid}')
            print(f'  Falling back to rotation.')
            search = None
    else:
        search = None

    if search is None:
        week_num = datetime.now().isocalendar()[1]
        search = DANNY_SEARCHES[week_num % len(DANNY_SEARCHES)]
        print(f'  County batch: {search["label"]} (week {week_num} rotation)')

    people = apollo_search(DANNY_TITLES, search['counties'], per_page=50, keywords=DANNY_ORG_KEYWORDS)
    print(f'  Found {len(people)} people from Apollo')

    new_leads = []
    for p in people:
        first   = p.get('first_name', '')
        last    = p.get('last_name_obfuscated', '').replace('*', '')
        org     = p.get('organization', {})
        org_name = org.get('name', '')

        # Reveal to get email + linkedin
        person_id = p.get('id', '')
        if not person_id:
            continue  # Malformed Apollo response — skip rather than KeyError crash
        revealed = apollo_reveal(person_id, first, last, org_name)
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
            '_lead_type':   'property_manager',
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
        # Sentinel: vera_relay uses this to detect Danny staleness more reliably than log-parsing
        _write_danny_sentinel()
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
        if not people:
            reason = f'Apollo returned 0 people — API may be blocked or rate limited ({search["label"]})'
        else:
            reason = f'all {len(people)} leads from Apollo were duplicates ({search["label"]})'
            # Cron IS running but found no new leads — still update sentinel so vera_relay doesn't false-alarm
            _write_danny_sentinel()
        log('danny', f'Apollo pull — {reason}', 'none', 'Done')
        send_report_card(
            worker_name='danny',
            title='Lead Pull — No New Leads',
            metrics=[
                ('New Leads', 0),
                ('Enrolled', 0),
            ],
            summary_lines=[reason],
            status='DONE',
        )

    return new_leads


def run_carla(county_override=None):
    print('\n🟣 Carla — Referral Partner Lead Pull')
    existing = load_existing_emails()

    week_num = datetime.now().isocalendar()[1]
    if county_override:
        idx = next(
            (i for i, label in enumerate(CARLA_COUNTY_LABELS) if county_override.lower() in label.lower()),
            None
        )
        if idx is not None:
            locations = CARLA_COUNTY_ROTATION[idx]
            county_label = CARLA_COUNTY_LABELS[idx]
            print(f'  County batch: {county_label} [MANUAL OVERRIDE]')
        else:
            valid = ', '.join(CARLA_COUNTY_LABELS)
            print(f'  ⚠️ County "{county_override}" not found. Valid values: {valid}')
            print(f'  Falling back to rotation.')
            county_idx = week_num % len(CARLA_COUNTY_ROTATION)
            locations = CARLA_COUNTY_ROTATION[county_idx]
            county_label = CARLA_COUNTY_LABELS[county_idx]
            print(f'  County batch: {county_label} (week {week_num} rotation)')
    else:
        county_idx = week_num % len(CARLA_COUNTY_ROTATION)
        locations = CARLA_COUNTY_ROTATION[county_idx]
        county_label = CARLA_COUNTY_LABELS[county_idx]
        print(f'  County batch: {county_label} (week {week_num} rotation)')

    all_new = []
    all_people_count = 0
    for search in CARLA_SEARCHES:
        people = apollo_search(search['titles'], locations, per_page=20, keywords=search.get('keywords'))
        all_people_count += len(people)
        print(f'  {search["label"]}: Found {len(people)} people')

        for p in people:
            first    = p.get('first_name', '')
            last     = p.get('last_name_obfuscated', '').replace('*', '')
            org      = p.get('organization', {})
            org_name = org.get('name', '')

            person_id = p.get('id', '')
            if not person_id:
                continue  # Malformed Apollo response — skip rather than KeyError crash
            revealed = apollo_reveal(person_id, first, last, org_name)
            email    = revealed.get('email', '')
            if not email or email.lower() in existing:
                continue

            org_id = revealed.get('organization_id', '') or p.get('organization', {}).get('id', '')
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
        out_file = f'leads_referral_partners_{county_label.lower().replace("+", "_")}_{date_str}.md'
        out_path = OUTPUTS / 'carla' / out_file
        out_path.parent.mkdir(exist_ok=True)

        lines = [
            f'# Referral Partner Leads — {county_label}',
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
        log('carla', f'Apollo pull — {len(all_new)} new referral partners in {county_label}, {enrolled} enrolled in Mixmax', out_file)
        _write_carla_sentinel()
        git_push('carla', f'Carla: lead pull {county_label} {date_str}')
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
    else:
        if all_people_count == 0:
            reason = 'Apollo returned 0 people — API may be blocked or rate limited'
        else:
            reason = f'all {all_people_count} leads from Apollo were duplicates'
            _write_carla_sentinel()  # Cron is alive even if no new leads
        log('carla', f'Apollo pull — {reason}', 'none', 'Done')
        send_report_card(
            worker_name='carla',
            title='Lead Pull — No New Leads',
            metrics=[('New Leads', 0), ('Enrolled', 0)],
            summary_lines=[reason],
            status='DONE',
        )

    return all_new


def get_mixmax_enrolled_emails():
    """Pull the set of emails currently confirmed in all live Mixmax sequences.
    Returns None if ALL sequences fail to respond — caller should skip repair
    to avoid mass re-enrollment when the API is temporarily unavailable.
    Reads sequence IDs dynamically from integrations/mixmax.py so gas_station
    and fleet sequences are checked automatically once their IDs go live.
    """
    try:
        from integrations.mixmax import SEQUENCES, _sequence_is_live
        seq_ids = [meta['id'] for seq_type, meta in SEQUENCES.items() if _sequence_is_live(seq_type)]
    except Exception:
        seq_ids = []
    # Fallback to hardcoded IDs in case import fails
    if not seq_ids:
        seq_ids = [
            '6a048cfc110bc620ca0f1aee',  # Property Managers
            '6a048cfba81429e5dfe55010',  # Realtors
            '6a048cfd624a5989a68ba16c',  # Contractors
        ]
    enrolled = set()
    success_count = 0
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
            success_count += 1
        except Exception:
            pass
    if success_count == 0:
        return None  # All calls failed — prevent mass re-enrollment
    return enrolled


def verify_and_repair_enrollment():
    """
    After every pipeline run: cross-check the contacts cache against live
    Mixmax data and re-enroll anyone who slipped through the cracks.
    Runs automatically at the end of every lead pull.
    """
    print('\n🔍 Verifying Mixmax enrollment...')
    # Warn if Instantly.ai is still running — re-enrolling contacts while Instantly is active
    # can create duplicate sends for contacts that originally failed enrollment (first Mixmax email
    # + active Instantly email = duplicate → spam risk for those contacts).
    if os.environ.get('INSTANTLY_PAUSED', '').lower() != 'true':
        if os.environ.get('INSTANTLY_OVERRIDE', '').lower() != 'true':
            print('  ⚠️  INSTANTLY.AI NOT PAUSED — repair enrollment will proceed but re-enrolled contacts')
            print('     may receive duplicate emails if Instantly campaigns a1c08c3d/626cd15d are still active.')
            print('     Pause at app.instantly.ai → set INSTANTLY_PAUSED=true in .env to suppress this warning.')

    if not CACHE_FILE.exists():
        print('  No cache file — skipping.')
        return

    confirmed = get_mixmax_enrolled_emails()
    if confirmed is None:
        print('  ⚠️ Mixmax API unavailable — skipping repair to prevent mass re-enrollment.')
        log('pipeline', 'Enrollment verification skipped — Mixmax API unavailable (all sequences 403/timeout)', 'contacts_cache.json')
        return
    print(f'  Confirmed in Mixmax: {len(confirmed)}')

    try:
        cache = json.loads(CACHE_FILE.read_text())
    except (json.JSONDecodeError, Exception):
        print('  ⚠️ contacts_cache.json malformed — skipping repair.')
        return
    contacts = cache.get('contacts', [])

    # Find contacts with an email that aren't in Mixmax yet
    # Skip contacts whose sequence is PENDING — they can't be enrolled yet
    try:
        from integrations.mixmax import _sequence_is_live as _sil
        missing = [
            c for c in contacts
            if c.get('email')
            and c['email'].lower() not in confirmed
            and _sil(c.get('_lead_type', ''))
        ]
        pending_skip = [
            c for c in contacts
            if c.get('email')
            and c['email'].lower() not in confirmed
            and not _sil(c.get('_lead_type', ''))
        ]
        if pending_skip:
            print(f'  Skipping {len(pending_skip)} contacts with PENDING sequences (gas_station/fleet_washing)')
    except Exception:
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


def run_pending_sequences():
    """
    Enroll contacts that have a live sequence but haven't been enrolled yet.
    Checks both contacts_cache.json and pipeline_data.json (manual contacts with _lead_type).
    Runs automatically — as soon as a PENDING sequence ID is added to
    integrations/mixmax.py, these contacts go into the sequence on the next run.
    """
    from integrations.mixmax import enroll_lead, _sequence_is_live

    # Lead types that were NEVER enrolled in Instantly.ai (campaigns a1c08c3d + 626cd15d were
    # PM Cuyahoga + Contractor Referral only). These types have zero duplicate-email risk.
    INSTANTLY_SAFE_TYPES = {'gas_station', 'fleet_washing'}

    pending = []
    cache = {}  # initialized here so the persist block below never hits NameError

    # Source 1: contacts_cache.json (Apollo-pulled leads)
    if CACHE_FILE.exists():
        try:
            cache = json.loads(CACHE_FILE.read_text())
        except (json.JSONDecodeError, Exception):
            print('  ⚠️ contacts_cache.json malformed — skipping cache pending enrollment.')
            cache = {}
        for c in cache.get('contacts', []):
            if (not c.get('mixmax_enrolled')
                    and c.get('email')
                    and c.get('_lead_type')
                    and _sequence_is_live(c.get('_lead_type', ''))):
                pending.append(('cache', c))

    # Source 2: pipeline_data.json manual contacts with _lead_type (or lead_type) set and email present
    pipeline_dirty = False
    pipeline_data = {}
    if PIPELINE_F.exists():
        try:
            pipeline_data = json.loads(PIPELINE_F.read_text())
        except (json.JSONDecodeError, Exception):
            print('  ⚠️ pipeline_data.json malformed — skipping pipeline pending enrollment.')
        for mc in pipeline_data.get('manual_contacts', []):
            # Check both _lead_type (Apollo-imported) and lead_type (manually imported) fields
            lt_field = mc.get('_lead_type') or mc.get('lead_type', '')
            if (not mc.get('mixmax_enrolled')
                    and mc.get('email')
                    and lt_field
                    and _sequence_is_live(lt_field)):
                pending.append(('pipeline', mc))

    if not pending:
        return

    # Check if ALL pending contacts are Instantly-safe types (never in Instantly.ai campaigns)
    all_instantly_safe = all(
        (c.get('_lead_type') or c.get('lead_type', '')) in INSTANTLY_SAFE_TYPES
        for _, c in pending
    )

    # Block enrollment for contact types that overlap with Instantly.ai campaigns,
    # unless Instantly is confirmed paused or the override is set.
    if not all_instantly_safe:
        if os.environ.get('INSTANTLY_PAUSED', '').lower() != 'true':
            if os.environ.get('INSTANTLY_OVERRIDE', '').lower() != 'true':
                print('🚫 PENDING ENROLLMENT BLOCKED — INSTANTLY.AI NOT CONFIRMED PAUSED')
                print('   Add INSTANTLY_PAUSED=true to .env after pausing campaigns a1c08c3d + 626cd15d.')
                print('   Guide: outputs/vera/instantly_pause_guide_2026-05-22.md')
                return
            else:
                print('⚠️  INSTANTLY.AI NOT PAUSED — bypassing block (INSTANTLY_OVERRIDE=true)')
    else:
        print('ℹ️  All pending contacts are gas_station/fleet_washing — never in Instantly.ai. Bypassing Instantly check.')

    print(f'\n⏳ Enrolling {len(pending)} pending contacts now that sequences are live...')
    enrolled = 0
    for source, c in pending:
        # Resolve lead type — honor both _lead_type (Apollo) and lead_type (manual imports)
        resolved_lead_type = c.get('_lead_type') or c.get('lead_type', '')
        # Build a normalized lead dict for mixmax.enroll_lead
        lead = {
            'first_name':   c.get('first_name', ''),
            'last_name':    c.get('last_name', ''),
            'email':        c.get('email', ''),
            'title':        c.get('title', ''),
            'company_name': c.get('company_name') or c.get('company', ''),
            'phone':        c.get('phone', ''),
            '_lead_type':   resolved_lead_type,
            '_worker':      c.get('_worker', 'danny'),
        }
        result = enroll_lead(lead)
        if result.get('status') == 'enrolled':
            c['mixmax_enrolled'] = True
            c['mixmax_sequence'] = result.get('sequence', '')
            enrolled += 1
            print(f'  ✅ {c.get("first_name","")} {c.get("last_name","")} ({c.get("company","")})'
                  f' → {result["sequence"]}')
            if source == 'pipeline':
                pipeline_dirty = True
        else:
            print(f'  ⚠️  {c.get("email")} — {result.get("reason", result.get("errors",""))}')
        time.sleep(0.3)

    # Persist changes — write the in-memory cache (which has mixmax_enrolled=True updates)
    # NOT a fresh re-read, which would silently discard the enrollment marks
    if CACHE_FILE.exists() and cache.get('contacts'):
        try:
            CACHE_FILE.write_text(json.dumps(cache, indent=2))
        except Exception:
            pass
    if pipeline_dirty and pipeline_data:
        PIPELINE_F.write_text(json.dumps(pipeline_data, indent=2))

    log('pipeline', f'Pending sequence enrollment — {enrolled}/{len(pending)} enrolled', 'contacts_cache.json+pipeline_data.json')

    if enrolled:
        send_report_card(
            worker_name='danny',
            title='Pending Contacts Enrolled',
            metrics=[('Enrolled', enrolled), ('Total Pending', len(pending))],
            summary_lines=[f'{enrolled} contacts moved from pending into live Mixmax sequences'],
            status='DONE',
        )


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'both'
    # Optional county override for Danny: python3 workers/lead_pipeline.py danny Summit
    # Optional county override for Carla: python3 workers/lead_pipeline.py carla Summit
    # Forces a specific county batch regardless of the week rotation.
    # Valid labels: Cuyahoga, Lake, Lorain, Summit, Medina, Geauga+Portage
    county_override = sys.argv[2] if len(sys.argv) > 2 and mode in ('danny', 'carla') else None

    print(f'\n=== Forest City Lead Pipeline — {datetime.now().strftime("%Y-%m-%d %H:%M")} ===')

    if mode in ('danny', 'both'):
        run_danny(county_override=county_override if mode == 'danny' else None)
    if mode in ('carla', 'both'):
        run_carla(county_override=county_override if mode == 'carla' else None)

    # 'pending' mode: enroll contacts waiting on sequences that just went live,
    # without triggering a fresh Apollo pull. Use this once gas_station/fleet
    # sequence IDs are added to integrations/mixmax.py.
    # Example: python3 workers/lead_pipeline.py pending
    run_pending_sequences()

    # Always verify enrollment after pulling leads — catches any silent failures
    if mode != 'pending':
        verify_and_repair_enrollment()

    # Commit pipeline_data.json and contacts_cache.json if changed
    # (enrollment marks from run_pending_sequences + verify_and_repair_enrollment)
    try:
        subprocess.run(['git', '-C', str(BASE_DIR), 'add', 'pipeline_data.json', 'contacts_cache.json'], capture_output=True)
        subprocess.run(['git', '-C', str(BASE_DIR), 'commit', '-m',
                        f'Pipeline: update pipeline_data.json enrollment marks {datetime.now().strftime("%Y-%m-%d")}'],
                       capture_output=True)
        subprocess.run(['git', '-C', str(BASE_DIR), 'push', 'origin', 'main'],
                       capture_output=True, timeout=15)
    except Exception:
        pass

    print('\n✅ Lead pipeline complete.')
