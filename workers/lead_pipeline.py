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
    # Golf courses & country clubs — NE Ohio has 100+ courses (Quail Hollow, StoneWater, Firestone CC, Gleneagles,
    # Fowler's Mill, Sleepy Hollow, Fox Creek, Windmill Lakes); May-June = peak play season + member events + tournaments;
    # clubhouse exterior + cart staging area + parking lot = recurring pressure wash need; superintendent manages grounds
    # + signs vendor contracts; club GM can override for larger contracts; $2K-$8K/year per course; zero competitors (added 2026-05-27 run 112)
    'golf course superintendent', 'golf club manager', 'club general manager',
    'golf course director', 'director of golf', 'golf operations manager',
    # Cemeteries & memorial parks — large paved driveways, monument areas, pavilions, funeral home offices;
    # NE Ohio: Forest Hills Memorial Park, Sunset Memorial Park, Knollwood, Lake View Cemetery (landmark);
    # facilities directors manage long-term vendor relationships; spring = peak visitor season; $1K-$3K/year (added 2026-05-27 run 112)
    'cemetery superintendent', 'cemetery director', 'cemetery manager', 'memorial park director',
    # Funeral homes — 100+ NE Ohio locations (Davis-Becker, Brown-Forward, McGorray-Hanna, Busch Funeral Homes);
    # large paved parking lots (family gathering day = maximum visibility for a grieving family);
    # brick/stone building facades + covered porticos + chapel exterior + carport areas;
    # appearance directly reflects respect and professionalism — cannot look neglected on the most emotional day of a family's life;
    # funeral home director or owner signs vendor contracts; low competition = no cold-calling from competitors;
    # $1,000-$3,000/visit; spring + fall = 2x/year = $2K-$6K/year per location (added 2026-05-27 run 113)
    'funeral director', 'funeral home director', 'mortuary manager', 'funeral home manager',
    'mortuary director', 'funeral services director',
    # Urgent care centers — FastMed Urgent Care, Concentra (multiple NE Ohio locations), GoHealth,
    # CareNow (HCA), Summa Now, MetroHealth Urgent Care, Cleveland Clinic Express Care, UH Urgent Care;
    # state licensing inspectors check exterior cleanliness and patient-facing appearance (ORC licensing standards);
    # high patient volume = maximum foot traffic across parking lot + entrance walkways + building exterior;
    # regional FMs or district medical directors sign vendor contracts across multiple clinic locations;
    # $800-$2,000/visit (parking + entrance + facade). Quarterly = $3,200-$8,000/year per clinic;
    # 10-clinic regional deal = $32K-$80K/year; summer = peak volume (sports injuries, heat illness, vacations) (added 2026-05-27 run 114)
    'urgent care director', 'urgent care center manager', 'clinic director',
    'ambulatory care director', 'walk-in clinic manager', 'urgent care manager',
    # Veterinary clinics & animal hospitals — NE Ohio has 300+ vet clinics/animal hospitals;
    # Banfield (PetSmart-affiliated), VCA Animal Hospitals, BluePearl Specialty + Emergency,
    # National Veterinary Associates, Petco VetCo operate corporate chains with district FMs;
    # state licensing inspections require clean patient-facing exteriors + entry walkways + parking;
    # high foot traffic = recurring pressure washing need for entrance surfaces + lot striping areas;
    # practice manager or district FM signs vendor contracts across multiple clinic locations;
    # $400-$1,000/visit; 2x/year per clinic = $800-$2,000; 20-clinic chain deal = $16K-$40K/year (added 2026-05-28 run 115)
    'veterinary practice manager', 'animal hospital manager', 'veterinary clinic manager',
    'vet clinic manager', 'animal hospital director', 'veterinary district manager',
    # Towing companies & auto salvage — large paved yards + impound lots accumulate heavy oil/fluid staining;
    # NE Ohio: Jeff's Towing, Allied Towing, AAA impound lots, Belden's, regional salvage chains;
    # owner-operators sign contracts directly; zero competitors; $800-$2,500/visit; 4x/year (added 2026-05-28 run 117)
    'tow yard manager', 'towing company owner', 'auto salvage manager', 'impound lot manager',
    'towing operations manager', 'salvage yard manager', 'auto salvage director',
    # Manufacturing & industrial facilities — NE Ohio = major Midwest manufacturing hub;
    # Ford Avon Lake plant, Lincoln Electric, Eaton, Parker Hannifin, Republic Steel, North Star BlueScope;
    # hundreds of mid-size suppliers in Lorain/Lake/Cuyahoga/Summit corridors;
    # loading docks, building exteriors, parking lots = recurring pressure wash; OSHA compliance angle;
    # plant FMs sign vendor contracts; $800-$4,000/visit; quarterly = $3,000-$15,000/year per facility (added 2026-05-28 run 118)
    'plant manager', 'plant superintendent', 'manufacturing plant manager', 'plant facilities manager',
    'industrial facility manager', 'maintenance manager', 'plant maintenance manager',
    'ehs manager', 'environmental health safety manager', 'manufacturing facility manager',
    # Car wash facilities — NE Ohio has Mr. Clean Car Wash (12+ locations), Mister Car Wash, independent coin-ops;
    # car wash GMs/owners understand clean surfaces; building exteriors, vacuum areas, equipment bays;
    # ironic pitch: "We wash your building while you wash cars"; OSHA water runoff compliance angle;
    # district managers sign multi-location contracts; $1,500-$4,000/year per facility (added 2026-05-28 run 118)
    'car wash manager', 'car wash district manager', 'car wash owner', 'car wash operator',
    'carwash manager', 'express wash manager', 'tunnel wash manager', 'car wash general manager',
    # Public K-12 school districts — buildings and grounds directors oversee all district facilities;
    # summer (June-August) = buildings empty = peak annual exterior maintenance window;
    # Cleveland Metro, Lakewood, Parma, Solon, Strongsville, Shaker Heights, Cuyahoga Falls, Akron Public;
    # one district deal = 10-30 school buildings; $2K-$8K/building; one district = $20K-$160K/year;
    # 'director of facilities' already in list; adding school-specific titles Apollo surfaces at school orgs (added 2026-05-28 run 119)
    'director of buildings and grounds', 'buildings and grounds director',
    'school maintenance director', 'school district facilities manager',
    # Car rental companies — Enterprise, Hertz, Avis, Budget, National, Alamo at Hopkins Airport + NE Ohio suburban lots;
    # large paved parking lots with vehicle oil/exhaust staining; building exteriors;
    # district managers oversee 3-8 locations and sign multi-site vendor contracts;
    # $1,500-$4,000/location; district deal = $12K-$32K/year (added 2026-05-28 run 119)
    'car rental district manager', 'rental car location manager', 'car rental operations manager',
    'branch rental manager',
    # Tire & auto service chains — Discount Tire (100+ NE Ohio locations), Jiffy Lube, Firestone Complete Auto Care,
    # Midas, Valvoline Instant Oil Change, Monro Muffler, Goodyear service centers;
    # high-traffic paved lots + building exteriors + dumpster pads accumulate oil staining;
    # district managers sign multi-location vendor contracts; ironic pitch: "we clean around your cars";
    # $400-$800/location; quarterly = $1.6K-$3.2K/location; 20-location district deal = $32K-$64K/year (added 2026-05-28 run 120)
    'tire center manager', 'auto service center manager', 'tire store manager', 'service center manager',
    'quick lube manager', 'auto lube manager', 'tire district manager', 'automotive service center director',
    # Movie theaters / cineplexes — AMC Ridge Park, Regal Great Lakes Mall, Cinemark Valley View,
    # Atlas Cinemas (NE Ohio regional chain with 8 locations); large paved parking lots;
    # GMs sign vendor contracts; high foot traffic = stained entry concrete, drive lanes, dumpster areas;
    # spring cleaning before summer blockbuster season = natural pitch window; $1,500-$4,000/year (added 2026-05-28 run 120)
    'theater general manager', 'cinema manager', 'movie theater manager', 'multiplex manager',
    'theater operations manager', 'cinema general manager',
    # Public library systems — Cuyahoga County Public Library (28 branches, 2nd busiest system in USA),
    # Akron-Summit County PL, Lake County PL, Medina County PL, Portage County District Library;
    # government facility managers sign vendor contracts; high foot traffic = stained entry walkways + parking lots;
    # public appearance = community trust signal; $500-$1,500/branch; system deal = $10K-$40K/year (added 2026-05-28 run 120)
    'library director', 'public library director', 'library facilities manager', 'library system director',
    'branch library manager', 'library operations manager',
    # Bowling alleys & entertainment centers — Brunswick Zone (Stow, Strongsville, Twinsburg), AMF Bowling,
    # Dave & Buster's (Westlake), Main Event, Lucky Strike, Great Lakes Bowling;
    # large parking lots + building exteriors + entrance areas; GMs sign vendor contracts;
    # $800-$2,000/visit; 2-4x/year; zero competitors targeting this segment (added 2026-05-28 run 120)
    'bowling alley manager', 'bowling center manager', 'entertainment center manager',
    'family entertainment center manager', 'bowling center director', 'recreation center manager',
    # Dental Service Organizations (DSOs) & group dental practices — NE Ohio: Aspen Dental (20+ locations),
    # Heartland Dental (largest US DSO, owns many NE Ohio group practices), Dental Care Alliance,
    # Great Lakes Dental Partners, Midwest Dental, Pacific Dental Services, Western Dental;
    # DSO district managers oversee 10-20 clinics; ORC dental licensing = exterior appearance standard;
    # parking lots + patient-facing entrance areas + building exteriors;
    # $600-$1,500/clinic visit; 10-clinic district deal = $6K-$15K/year per district manager;
    # DSO targets ONLY — individual solo-dentist offices are too small for cold outreach (added 2026-05-28 run 123)
    'dso district manager', 'dental district manager', 'dental group practice director',
    'practice area director', 'regional dental director', 'dental operations director',
    'dental regional manager', 'group practice administrator',
    # Municipal & Government Facilities — city halls, county admin buildings, township public works,
    # RTA/transit depots, port authority, Cleveland Metroparks, county justice centers;
    # government FMs control large paved surfaces (vehicle lots, entrance plazas, public walkways);
    # appearance is a public-trust signal; small contracts (<$25K) often direct-awarded without public bid;
    # NE Ohio: City of Cleveland (multiple municipal buildings), Cuyahoga County Admin Building,
    # GCRTA bus depots (Hayden Garage, Triskett Garage, Warrensville Garage), Port of Cleveland,
    # Cleveland Metroparks facilities, multiple suburb city halls (Strongsville, Parma, Lakewood) (added 2026-05-28 run 124)
    'city facilities manager', 'municipal facility manager', 'government facility manager',
    'township facilities manager', 'public works facilities manager', 'county facilities director',
    'transit facility manager', 'city maintenance director', 'municipal buildings manager',
    'government buildings manager', 'public facilities manager', 'parks district manager',
    'parks and recreation director', 'parks facilities manager',
    # Hospital & Health System Main Campuses — main hospital buildings (NOT outpatient offices, already in list above);
    # Cleveland Clinic Main Campus (Euclid Ave), UH Rainbow/Ahuja/Geauga, MetroHealth Medical Center,
    # Summa Health Akron City Hospital, Mercy Health facilities, Southwest General (Middleburg Heights),
    # Hillcrest Hospital, Marymount Hospital, South Pointe Hospital, Huron Hospital;
    # hospital facility directors manage enormous building footprints with large parking structures,
    # building exteriors, entrance plazas, loading dock areas, medical waste staging areas;
    # facility engineering and plant operations are distinct from outpatient FM contacts;
    # $2,000-$8,000/building (exterior + entrance + loading dock). Annual or bi-annual contracts;
    # health system portfolio = $30K-$200K/year for full-service plant operations FM (added 2026-05-28 run 124)
    'hospital facilities director', 'hospital plant operations manager', 'health system facilities director',
    'hospital maintenance director', 'hospital facility manager', 'acute care facilities manager',
    'hospital engineering director', 'clinical facilities manager', 'hospital plant manager',
    'vice president of facilities', 'vp facilities',
    # Pet Boarding & Kennel Facilities — NE Ohio has hundreds of boarding facilities;
    # PetSmart PetsHotel (10+ NE Ohio locations), Bark Avenue, Hounds Town, Camp Bow Wow,
    # independent kennels and doggy daycares across Cuyahoga/Summit/Lake/Lorain counties;
    # outdoor dog runs + building exteriors + parking lots accumulate biological residue, mud, waste;
    # Ohio pet boarding license = exterior cleanliness standard (facility inspection required);
    # high foot traffic from pet owners dropping off/picking up = stained walkways + entrance areas;
    # facility manager or owner signs vendor contracts; $400-$1,200/visit; 2-3x/year;
    # 10 facilities = $8K-$24K/year; zero competitors targeting this segment (added 2026-05-28 run 125)
    'pet boarding manager', 'kennel manager', 'dog boarding director', 'pet resort manager',
    'doggy daycare manager', 'animal boarding manager', 'pet care director', 'kennel director',
    # Dialysis Centers — DaVita (50+ NE Ohio locations), Fresenius Medical Care (40+ NE Ohio),
    # US Renal Care, NephroMed, Rotech Healthcare outpatient dialysis centers;
    # patients visit 3x/week = extremely high foot traffic on parking lots + entrance walkways;
    # CMS/Medicare certification standards require clean patient-facing exterior appearance;
    # district FMs oversee 10-20 centers and sign multi-location vendor contracts;
    # $500-$1,200/center; quarterly = $2K-$4.8K/year per center;
    # 15-center district FM deal = $30K-$72K/year; zero current competitors in this segment (added 2026-05-28 run 125)
    'dialysis center manager', 'dialysis clinic manager', 'renal care director',
    'dialysis facility manager', 'outpatient dialysis manager', 'dialysis district manager',
    'dialysis regional manager', 'kidney care director',
    # Sports Complexes & Youth Athletic Facilities — NE Ohio has dozens of multi-sport facilities;
    # Sportsplex at Mentor, Great Lakes Athletic Complex, Cleveland Sport & Social Club,
    # youth baseball/softball complexes (dozens in Cuyahoga/Summit/Lake/Lorain), indoor soccer facilities,
    # youth hockey rinks (OHF-affiliated rinks throughout NE Ohio), gymnastics academies,
    # martial arts academies with large studio/parking footprints;
    # heavy weekend foot traffic from parents + kids = staining on parking lots + entrance walkways;
    # large paved parking areas + building exteriors + walkways = recurring pressure wash need;
    # GM or owner signs vendor contracts; $800-$2,500/visit; 2-3x/year per facility;
    # zero competitors targeting this segment (added 2026-05-28 run 125)
    'sports complex manager', 'athletic complex director', 'sports facility manager',
    'recreation complex manager', 'sports complex director', 'athletic facility director',
    'youth sports director', 'sports facility director',
    # Physical Therapy Clinic Chains — NovaCare (80+ NE Ohio), ATI Physical Therapy (100+ NE Ohio),
    # Select Physical Therapy, Athletico PT, Results Physiotherapy;
    # high foot traffic (3x/week rehab visits) = stained entry walkways + parking lots;
    # state PT licensing inspections include patient-facing exterior appearance;
    # district managers oversee 10-20 clinics and sign multi-location vendor contracts;
    # $400-$1,200/clinic; quarterly = $1.6K-$4.8K/year per clinic;
    # 20-clinic district deal = $32K-$96K/year; zero competitors targeting this segment (added 2026-05-28 run 126)
    'physical therapy district manager', 'physical therapy clinic manager', 'outpatient pt manager',
    'rehabilitation clinic manager', 'physical therapy center director', 'therapy district manager',
    'outpatient physical therapy manager', 'rehab clinic director', 'pt clinic manager',
    # Pharmacy & Drug Store Chains — CVS (50+ NE Ohio), Walgreens (60+ NE Ohio), Rite Aid (HQ Wooster OH),
    # Giant Eagle Pharmacy, Discount Drug Mart (NE Ohio regional, 70+ locations);
    # drive-through canopies accumulate grime + mold; large parking lots; building exteriors visible from road;
    # district loss prevention / FM managers sign vendor contracts for 5-15 store territories;
    # $400-$1,000/location; quarterly = $1.6K-$4K/location; 15-store district = $24K-$60K/year;
    # Discount Drug Mart (headquartered in Medina — strong local angle!) (added 2026-05-28 run 126)
    'pharmacy district manager', 'drug store district manager', 'pharmacy facilities manager',
    'retail pharmacy manager', 'pharmacy store manager', 'pharmacy operations manager',
    'drug store manager', 'pharmacy regional manager',
    # Concert Venues & Outdoor Amphitheaters — Blossom Music Center (Live Nation, Cuyahoga Falls,
    # capacity 19,000+), Jacobs Pavilion at Nautica (Cleveland waterfront, capacity 5,000),
    # Hard Rock Rocksino Northfield Park outdoor stage, Akron Civic Theatre, Playhouse Square loading areas;
    # massive paved parking lots + concrete plaza concourses + loading dock areas + entrance walkways;
    # Live Nation / AEG regional facilities managers sign seasonal vendor contracts for all venues in territory;
    # spring pre-season clean (before May concerts) + post-summer cleanup = 2 visits/year at $3K-$10K/venue;
    # zero competitors cold-calling Live Nation / AEG FM contacts; (added 2026-05-29 run 127)
    'amphitheater manager', 'performing arts center manager', 'concert venue manager',
    'outdoor venue manager', 'music venue manager', 'live entertainment venue manager',
    # Food Processing Plants & Cold Storage — distinct from manufacturing/industrial above;
    # FDA/USDA Good Manufacturing Practice (GMP) regulations require licensed food production facilities
    # to maintain clean exterior loading docks and facility perimeters (21 CFR Part 110/117);
    # NE Ohio targets: Shiloh Foods (Lodi, Medina County — large bakery operation), J.M. Smucker
    # (Orville OH — Wayne/Medina corridor), Bob Evans Foods processing centers, Cloverleaf Cold Storage
    # (NE Ohio distribution hubs), Nestle USA (Solon OH), TreeHouse Foods, LiDestri Food & Drink;
    # loading dock concrete + refrigerated bay exteriors + building facades = recurring quarterly wash;
    # FDA compliance angle opens doors other cleaning vendors don't use; $2,000-$6,000/visit;
    # quarterly = $8,000-$24,000/facility; zero competitors using this compliance framing (added 2026-05-29 run 127)
    'food plant manager', 'food processing facility manager', 'food manufacturing manager',
    'cold storage manager', 'food production manager', 'food operations manager',
    'food facility manager', 'food plant superintendent',
    # Airport & Aviation Facilities — Cleveland Hopkins International (CLE, 11M passengers/year),
    # Akron-Canton Airport (CAK), Lorain County Airport; airport terminals + parking structures +
    # rental car lots + ground transport staging areas; FAA certification = appearance standards;
    # airport facilities managers sign vendor contracts for terminal exteriors + landside pavement;
    # one CLE contract = $10K-$30K/year; zero competitors have approached airport FM contacts;
    # Medina/June 1 pull for regional airports; Cuyahoga/June 8 for CLE Hopkins (added 2026-05-29 run 128)
    'airport facilities manager', 'airport operations manager', 'aviation facilities director',
    'airport maintenance director', 'airport facilities director', 'terminal facilities manager',
    'airport grounds manager', 'airfield maintenance manager',
    # Parking Garages & Structures — downtown Cleveland (Tower City, Gateway, hospital garages),
    # Akron urban core, suburban HOA parking structures, airport parking;
    # DANNY_ORG_KEYWORDS already has 'parking management', 'parking facility', 'parking garage'
    # but title list was missing parking-specific decision-maker titles;
    # district managers sign multi-structure contracts; $1,500-$4,000/clean; 4×/year;
    # multi-structure contract = $12K-$32K/year (added 2026-05-29 run 128)
    'parking manager', 'parking operations manager', 'parking district manager',
    'parking structure manager', 'garage manager', 'parking lot manager',
    'parking facility manager',
    # Convention Centers & Exhibition Halls — Cleveland Convention Center (I-X Center, downtown GCCC),
    # Akron Civic Complex, John S. Knight Center, Kalahari Resorts (Sandusky — adjacent to NE Ohio),
    # Richfield Event Center; massive paved plaza concourses + loading dock areas + building exteriors;
    # event appearance is non-negotiable (all photos shared publicly); convention managers sign
    # seasonal vendor contracts; pre-season clean before fall conference calendar (Aug-Sep timing);
    # one Cleveland Convention Center contract = $8K-$25K/year; zero competitors targeting this segment (added 2026-05-29 run 128)
    'convention center manager', 'convention center director', 'exhibition hall manager',
    'trade show facility manager', 'events center manager', 'convention facilities manager',
    'expo center manager', 'conference facility director',
    # Craft Breweries & Taprooms — NE Ohio is a major craft beer market (100+ breweries);
    # Great Lakes Brewing Co (Cleveland — OG NE Ohio craft), Platform Beer Co (Cleveland), Masthead Brewing,
    # Thirsty Dog Brewing (Akron), Goldhorn Brewery, Terrestrial Brewing, Collision Bend Brewing,
    # Forest City Brewery (Cleveland), Crooked River Brewing, Trail Brew Works, Brew Kettle;
    # outdoor beer gardens + patios + large parking lots + building facades;
    # spring pre-season clean BEFORE patio season opens (May–June) = natural pitch window;
    # seasonal events (tapping parties, summer outdoor concerts, festivals) = appearance is marketing;
    # taproom managers or owners sign vendor contracts directly; zero power washing competitors cold-calling;
    # $800-$2,500/visit; 2-3x/year (spring open + fall close + event prep); $1.6K-$7.5K/year per taproom;
    # NE Ohio craft beer belt: Cleveland → Akron → Lake Erie corridor = dense target density (added 2026-05-29 run 129)
    'taproom manager', 'brewery manager', 'craft brewery manager', 'tap room manager',
    'brewery operations manager', 'taproom director', 'brewery general manager',
    # Standalone generic decision-maker titles — NOT added to PROPERTY_MANAGER_TITLES (routing) because
    # 'district manager' was previously in GAS_STATION_KEYWORDS and caused routing conflicts on manual imports.
    # These ARE safe for Apollo search because DANNY_ORG_KEYWORDS constrains results to target companies only
    # (Apollo won't return "District Manager" at a software company if its org keyword isn't in our list).
    # Danny's pipeline sets _lead_type='property_manager' explicitly so routing is handled correctly upstream.
    # Without these entries, Apollo MISSES contacts who simply list generic corporate titles:
    #   "District Manager" at CVS/Walgreens/Discount Drug Mart
    #   "Area Manager" at Enterprise Rent-A-Car/Planet Fitness/Anytime Fitness/Aspen Dental
    #   "Regional Director" at DaVita/NovaCare/Concentra/Heartland Dental
    #   "Branch Manager" at Huntington/KeyBank/Fifth Third/PNC (branch-level can initiate vendor relationships)
    # (added 2026-05-29 run 130)
    'district manager',     # CVS, Walgreens, Jiffy Lube, Discount Tire, QSR franchises, DSO chains
    'area manager',         # Enterprise Rent-A-Car, Planet Fitness, Anytime Fitness, Aspen Dental chains
    'regional director',    # DaVita dialysis, NovaCare PT, Concentra, Heartland Dental, hotel brands
    'branch manager',       # bank branches (Huntington, KeyBank, Fifth Third, PNC) — branch-level vendor contact
    # Museums & Cultural Institutions — Cleveland Museum of Art (University Circle), Cleveland Museum of Natural History,
    # Cleveland Metroparks Zoo (largest NE Ohio — 3M visitors/year), Rock & Roll Hall of Fame (lakefront),
    # Great Lakes Science Center (lakefront), Maltz Museum of Jewish Heritage (Beachwood),
    # Crawford Auto-Aviation Museum, Severance Hall (Cleveland Orchestra), Cleveland Play House, Playhouse Square,
    # Akron Art Museum, Stan Hywet Hall & Gardens (Akron — historic estate, 70 acres, large event venue);
    # Cultural institutions have ZERO power washing vendor relationships — no competitor targets this segment.
    # Large paved plazas + building facades + parking structures + loading dock areas = recurring cleaning need.
    # Museum facilities directors manage large campus footprints; appearance is critical for donor events,
    # corporate rentals, school field trips, and public trust. Facilities budgets are robust (funded by endowments,
    # admission, and corporate sponsors). Annual or bi-annual exterior cleaning contracts.
    # One contract with Cleveland Museum of Art = $4K-$12K/year. Cleveland Metroparks Zoo = $8K-$25K/year.
    # June 8 Cuyahoga pull fires first — all major NE Ohio museums are in Cuyahoga County University Circle corridor
    # or lakefront (CMA, CMNH, Great Lakes Science Center, Rock Hall), or Beachwood (Maltz), or Akron (CFA) (added 2026-05-29 run 130)
    'museum facilities manager', 'museum director', 'cultural center director', 'museum manager',
    'zoo facilities manager', 'zoo director', 'aquarium manager', 'botanical garden manager',
    'cultural institution manager', 'arts center director', 'science center manager',
    'natural history museum manager', 'art museum facilities manager', 'historic estate manager',
    # YMCA & Community Centers — YMCA of Greater Cleveland (12+ branches across Cuyahoga County),
    # Akron Area YMCA (7 branches), Summit County YMCA, Medina County Family YMCA, Lake County YMCA;
    # large parking lots + outdoor pools + building exteriors + sports court areas;
    # licensed facilities (state health dept. inspections) create recurring exterior cleanliness requirement;
    # branch directors and facilities managers sign vendor contracts; $800-$2,500/visit; 2-3x/year;
    # YMCA of Greater Cleveland portfolio contract = $15K-$30K/year across all branches;
    # zero power washing competitors targeting YMCA facilities managers in NE Ohio;
    # first pull June 8 Cuyahoga (all Greater Cleveland YMCA branches) (added 2026-05-29 run 131)
    'ymca director', 'ymca branch director', 'ymca facilities manager', 'ymca operations manager',
    'ywca director', 'community center director',
    # Car Auctions & Vehicle Wholesale — Manheim Cleveland (Cox Automotive, one of the largest wholesale
    # auto auctions in NE Ohio), ADESA/KAR Auction (Portage County), NovaStar Auto Auction,
    # National Auto Dealers Exchange (NADB), independent wholesale auction houses;
    # enormous paved outdoor lots with hundreds of vehicles; building exteriors, reconditioning bays,
    # administrative facades; heavy vehicle traffic = oil drip accumulation + fluid staining + tire marks;
    # OSHA stormwater compliance for auction lot runoff — clean lots reduce EPA/OEPA violation risk;
    # auction FMs run quarterly cleaning cycles (pre-auction season prep); FM signs vendor contracts;
    # zero competitors targeting auction facility managers; Manheim Cleveland alone: $2K-$8K/visit;
    # 4x/year = $8K-$32K/year; first pull June 8 Cuyahoga (Manheim Cleveland — Cuyahoga County) (added 2026-05-29 run 133)
    'auto auction manager', 'vehicle auction manager', 'auction facility manager',
    'auto auction operations manager', 'vehicle wholesale manager', 'auction site manager',
    # Coin Laundries & Laundromats — NE Ohio has hundreds of independent and franchise coin laundries;
    # CoinMach, Alliance Laundry Systems, Laundrylux-franchised operators; large paved parking areas;
    # chemical water runoff from laundry detergent residue = OEPA stormwater compliance consideration;
    # concrete exterior is chronically stained from chemical splash + heavy foot traffic;
    # owner-operators or route/district managers sign vendor contracts directly;
    # ironic pitch: "We clean the building where people do their cleaning."
    # $400-$1,200/visit; 2-3x/year = $800-$3,600 per location; 20-location route deal = $16K-$72K/year;
    # zero competitors cold-calling laundromat owners in NE Ohio; first pull June 8 Cuyahoga (added 2026-05-29 run 135)
    'laundromat owner', 'coin laundry manager', 'laundry facility manager', 'laundromat manager',
    'coin laundry owner', 'self-service laundry manager', 'laundry district manager',
    # Blood/Plasma Donation Centers — BioLife Plasma Services (multiple NE Ohio locations),
    # CSL Plasma (Cleveland/Akron area), Grifols (Cleveland), Vitalant, American Red Cross donation centers;
    # FDA-licensed blood establishments = exterior cleanliness + facility appearance required by regulation;
    # donors visit 2x/week = highest foot traffic frequency of any healthcare-adjacent facility;
    # entrance walkways + parking lots + building exteriors = recurring high-priority pressure wash need;
    # district managers sign multi-center vendor contracts; 10-center deal = $20K-$60K/year;
    # zero competitors cold-calling plasma/blood center FMs in NE Ohio; first pull June 8 Cuyahoga (added 2026-05-29 run 135)
    'plasma center manager', 'donation center manager', 'blood center manager',
    'plasma donation manager', 'blood bank manager', 'donor center manager',
    # Cannabis Dispensaries — Ohio legalized recreational cannabis Nov 2023 (Issue 2);
    # hundreds of new dispensaries opening across NE Ohio (Cleveland, Akron, Lakewood, Strongsville,
    # Mentor, Solon, Massillon corridor); state ODM/OEPA licensing includes exterior facility appearance standards;
    # high foot traffic from daily customers = stained entry walkways + parking lots;
    # dispensary owners/district managers sign vendor contracts; appearance is brand trust signal in regulated market;
    # zero current competitors targeting cannabis dispensary owners for power washing in NE Ohio;
    # $400-$1,200/visit; 2-3x/year = $800-$3,600 per location; first pull June 8 Cuyahoga (added 2026-05-29 run 135)
    'dispensary manager', 'cannabis dispensary manager', 'dispensary director',
    'dispensary general manager', 'cannabis operations manager', 'dispensary owner',
    # Professional Sports Venues — Rocket Mortgage FieldHouse (Cleveland Cavaliers, Monsters, 19,432 seats),
    # Progressive Field (Cleveland Guardians, 34,830 seats), FirstEnergy Stadium (Cleveland Browns, 67,895 seats),
    # Canal Park (Akron RubberDucks, minor league affiliate);
    # enormous paved parking lots (thousands of spaces) + concrete concourse plazas + loading dock areas +
    # building exteriors; events drive 20K-70K fans = maximum visible staining on all surfaces;
    # facility directors manage multi-million-dollar venue maintenance budgets;
    # one FieldHouse or Progressive Field contract = $15K-$50K/year; zero competitors targeting sports FM contacts;
    # peak season timing: baseball (April-Sept), basketball (Oct-June) = year-round cleaning need;
    # first pull June 8 Cuyahoga (all three major venues in Cuyahoga County) (added 2026-05-29 run 135)
    'sports venue facilities manager', 'stadium facilities manager', 'arena facilities manager',
    'venue operations director', 'sports facility operations manager', 'stadium operations manager',
    'arena operations manager', 'ballpark facilities manager',
    # Dollar Stores & General Merchandise Discount Chains — Dollar General (100+ NE Ohio), Family Dollar,
    # Dollar Tree, Five Below, Big Lots; enormous NE Ohio store density (DG alone has 100+ in 7-county area);
    # district FMs sign multi-site vendor contracts for 15-40 stores per district territory;
    # high-traffic paved lots + building exteriors + dumpster pads accumulate staining + gum + seasonal grime;
    # $300-$700/location; quarterly = $1.2K-$2.8K/location; 30-location district = $36K-$84K/year;
    # zero competitors cold-calling dollar store district managers in NE Ohio; first pull June 8 Cuyahoga (added 2026-05-29 run 136)
    'dollar store district manager', 'dollar store manager', 'general merchandise manager',
    'general merchandise district manager', 'family dollar manager', 'dollar general manager',
    'discount store manager', 'dollar store operations manager', 'value retail manager',
    'five below manager', 'big lots manager', 'discount retail manager',
    # Auto Parts Stores — O'Reilly Auto Parts (50+ NE Ohio), AutoZone (60+ NE Ohio), Advance Auto Parts,
    # NAPA Auto Parts (Genuine Parts Company, largest auto parts network in US), Pep Boys, Parts Authority;
    # parking lots + aprons around service bays accumulate motor oil, hydraulic fluid, grease staining;
    # OSHA compliance angle: oil-stained parking lots = slip hazard = citation risk;
    # district managers sign multi-site vendor contracts for 20-30 locations;
    # $400-$800/location; quarterly = $1.6K-$3.2K/location; 25-location district = $20K-$50K/year;
    # zero competitors cold-calling auto parts district managers in NE Ohio; first pull June 8 Cuyahoga (added 2026-05-29 run 136)
    'auto parts district manager', 'auto parts store manager', 'auto parts regional manager',
    'automotive parts manager', 'parts store district manager', 'parts store manager',
    'auto parts operations manager', 'auto parts facilities manager',
    # Hardware & Home Improvement Centers — Home Depot (20+ NE Ohio), Lowe's (15+ NE Ohio), Menards (4 NE Ohio),
    # Ace Hardware (50+ NE Ohio dealer-owned locations), True Value Hardware, Do It Best;
    # enormous paved garden center plazas + massive parking lots (10+ acres at big-box locations) +
    # building exteriors + covered lumber yard areas + outdoor display pads;
    # seasonal grime (mulch dust, potting soil, fertilizer residue, oil stains) accumulates heavily;
    # district FMs manage 10-20 stores and sign vendor contracts for exterior maintenance;
    # $1,500-$5,000/location; one Home Depot district = $30K-$100K/year; zero competitors;
    # first pull June 8 Cuyahoga (all major big-box home improvement retailers in Cuyahoga County) (added 2026-05-29 run 136)
    'home improvement district manager', 'hardware store manager', 'home center manager',
    'home improvement store manager', 'hardware district manager', 'building materials manager',
    'home improvement operations manager', 'hardware store district manager',
    # Community Swimming Pools & Aquatic Centers — NE Ohio park districts and recreation departments operate
    # dozens of seasonal outdoor pools + year-round indoor aquatic centers;
    # targets: Lyndhurst Community Pool, North Olmsted Aquatic Center, Brunswick Swim Center,
    # Westlake Recreation Center, Rocky River Recreation Center, Shaker Heights Natatorium,
    # Solon Recreation Center aquatics, Twinsburg Family Aquatic Center, Strongsville Rec Center,
    # Brecksville Community Pool, Cuyahoga Falls Natatorium, Summit County MetroParks rec centers;
    # pool deck concrete + surrounding walkways + entry areas + parking lots = recurring cleaning need;
    # summer = peak operation season = natural pre-season pitch window (April-May exterior cleaning);
    # aquatic center directors sign vendor contracts; $1,000-$3,000/location; 10-pool system = $10K-$30K/year;
    # DISTINCT from YMCA aquatics (already targeted) — these are standalone municipal recreation facilities;
    # first pull June 8 Cuyahoga (Cuyahoga County park district runs largest NE Ohio aquatic system) (added 2026-05-29 run 136)
    'aquatic center director', 'pool facility manager', 'swimming pool manager',
    'community pool director', 'aquatic facility manager', 'recreational aquatic manager',
    'natatorium manager', 'aquatic center manager', 'public pool manager',
    # Wireless & Telecom Retail Chains — AT&T (200+ NE Ohio), Verizon (200+ NE Ohio), T-Mobile (150+ NE Ohio),
    # Boost Mobile, Cricket Wireless, Metro by T-Mobile; strip-mall storefront parking lots + building exteriors;
    # district managers sign vendor contracts for 10-20 store territories;
    # $300-$600/location; quarterly = $1.2K-$2.4K/location; 15-location district = $18K-$36K/year;
    # zero competitors cold-calling telecom retail district managers in NE Ohio; first pull June 8 Cuyahoga (added 2026-05-29 run 137)
    'wireless retail district manager', 'telecom retail manager', 'wireless store manager',
    'cell phone store manager', 'mobile retail manager', 'wireless district manager',
    'telecom district manager', 'wireless retail manager',
    # Uniform & Workwear Services — Cintas Corporation (NE Ohio HQ: Cincinnati but major Euclid/Solon/Twinsburg
    # processing facilities), Aramark Uniform Services, UniFirst Corporation, G&K Services (Cintas subsidiary),
    # Superior Uniform Group, ALSCO (American Linen); large processing/distribution facilities with
    # loading dock areas + building exteriors + employee parking lots; fleet vehicles also need regular washing;
    # ironic pitch: "We clean the building of the company that cleans everyone else's workwear";
    # FDA food-service + healthcare partner client standards = stringent facility cleanliness requirement;
    # district service managers sign vendor contracts; $2K-$8K/facility; multi-facility district deals;
    # zero competitors cold-calling uniform services facility managers; first pull June 8 Cuyahoga (added 2026-05-29 run 137)
    'uniform services manager', 'laundry services manager', 'uniform district manager',
    'linen services manager', 'textile services manager', 'workwear services manager',
    'uniform operations manager', 'garment services manager',
    # Warehouse Club & Membership Retail — Costco (3+ NE Ohio: Westlake, Macedonia, Avon/Sheffield),
    # Sam's Club (4+ NE Ohio: Mayfield Heights, Avon, Brunswick, Stow), BJ's Wholesale Club (2 NE Ohio);
    # ENORMOUS parking lots (8–15 acres per location) NOT caught by 'grocery chain' in Apollo — Costco/Sam's
    # are tagged 'wholesale retail' or 'membership warehouse' in Apollo, not 'grocery store';
    # gas station concourses + massive building exteriors + cart return areas;
    # district/regional FM contacts sign vendor contracts (Costco regional FM covers 3–5 locations);
    # Revenue: $3,000–$8,000/location (parking + building + gas concourse). 4x/year = $12K–$32K/location;
    # Costco regional district (3 NE Ohio locations) = $36K–$96K/year; zero competitors targeting;
    # first pull June 8 Cuyahoga (Costco Westlake + Sam's Club Mayfield Heights in Cuyahoga County) (added 2026-05-29 run 138)
    'warehouse club manager', 'warehouse club general manager', 'wholesale club manager',
    'wholesale club district manager', 'warehouse club facilities manager', 'membership store manager',
    'warehouse store manager', 'membership warehouse manager', 'wholesale store manager',
    # Optical/Vision Centers — LensCrafters (30+ NE Ohio), MyEyeDr (10+ NE Ohio), Visionworks,
    # Pearle Vision (Luxottica), America's Best, For Eyes, National Vision; strip-mall storefronts
    # with 300-600+ patients/week; parking lots + building exteriors must meet corporate brand standards;
    # district managers oversee 10-20 locations and sign vendor contracts; state optometry licensing
    # = facility appearance standard; $300-$700/location; 15-location district = $18K-$42K/year;
    # zero competitors cold-calling optical retail district managers in NE Ohio; first pull June 8 Cuyahoga (added 2026-05-30 run 139)
    'optometry district manager', 'vision center manager', 'optical center manager',
    'eyecare district manager', 'eye care center manager', 'optical district manager',
    'optometric practice manager', 'vision care manager',
    # Medical/Clinical Labs — Quest Diagnostics (50+ NE Ohio patient service centers), LabCorp (40+ NE Ohio),
    # ARUP Laboratories, BioReference Laboratories, Cleveland Clinic outpatient labs, UH diagnostic labs;
    # patients visit for blood draws + specimen collection = very high recurring foot traffic;
    # CLIA (Clinical Laboratory Improvement Amendments) federal certification = facility appearance standard;
    # district managers sign vendor contracts for multi-center coverage;
    # $300-$700/center; quarterly = $1.2K-$2.8K/center; 20-center district = $24K-$56K/year;
    # zero competitors cold-calling lab district managers; first pull June 8 Cuyahoga (added 2026-05-30 run 139)
    'laboratory district manager', 'lab district manager', 'clinical lab manager',
    'patient service center manager', 'laboratory facilities manager', 'lab operations manager',
    'laboratory operations manager', 'clinical laboratory manager',
    # Tax Preparation Offices — H&R Block (100+ NE Ohio locations), Jackson Hewitt Tax Service (60+ NE Ohio),
    # Liberty Tax Service (40+ NE Ohio); strip-mall storefronts that are open Jan-April but physically
    # present year-round; May-September = peak facility maintenance window (post-season exterior cleaning);
    # district managers sign vendor contracts for 10-20 location territories;
    # pitch angle: "Tax season is over — let us clean up the mess 4 months of client traffic left behind";
    # $300-$600/location; 10-location district = $12K-$24K/year; zero competitors targeting this segment;
    # first pull June 8 Cuyahoga (added 2026-05-30 run 139)
    'tax district manager', 'tax preparation manager', 'tax office manager',
    'tax center manager', 'tax services district manager', 'tax franchise manager',
    'tax preparation district manager',
    # Coffee & Drive-Through Beverage Chains — Starbucks (60+ NE Ohio), Dunkin' (80+ NE Ohio),
    # Panera Bread (has drive-through at most NE Ohio locations), Dutch Bros (growing in OH),
    # Caribou Coffee, Tim Hortons (50+ NE Ohio — strong Cleveland presence); drive-through canopies
    # accumulate exhaust, mildew, grime on the underside; parking lots + building exteriors;
    # high volume (hundreds of cars/day) = heavy staining at entry lanes and drive-through queue areas;
    # district managers sign vendor contracts for 5-15 store territories;
    # $400-$900/location; quarterly = $1.6K-$3.6K/location; 15-location district = $24K-$54K/year;
    # DISTINCT from restaurant QSR segment — coffee chain DMs have separate org tags in Apollo;
    # zero competitors cold-calling coffee chain district managers in NE Ohio; first pull June 8 Cuyahoga (added 2026-05-30 run 140)
    'coffee district manager', 'coffee shop manager', 'coffee chain manager',
    'drive through manager', 'drive-through manager', 'quick service beverage manager',
    'coffee store manager',
    # Pet Supply Retail Chains — PetSmart (20+ NE Ohio), Petco (15+ NE Ohio), Pet Supplies Plus (30+ NE Ohio);
    # DISTINCT from pet boarding/kennel segment — these are large-format retail stores with grooming salons;
    # grooming salon areas have water + dog shampoo runoff that stains concrete entries and curbside aprons constantly;
    # large suburban parking lots accumulate pet waste staining + heavy cart traffic;
    # state cosmetology/grooming licensing = facility appearance standard;
    # district managers sign vendor contracts for 5-15 store territories;
    # $400-$800/location; quarterly = $1.6K-$3.2K/location; 15-store district = $24K-$48K/year;
    # Pet Supplies Plus is headquartered in Livonia MI but has 30+ NE Ohio franchise stores;
    # zero competitors targeting pet supply retail district managers in NE Ohio; first pull June 8 Cuyahoga (added 2026-05-30 run 141)
    'pet supply district manager', 'pet store district manager', 'pet retail district manager',
    'pet supply store manager', 'pet retail manager', 'pet specialty district manager',
    # Hair & Nail Salon Chains — Great Clips (80+ NE Ohio — one of the largest Great Clips markets in USA),
    # Sport Clips (30+ NE Ohio), Supercuts (40+ NE Ohio), Cost Cutters, Fantastic Sam's, Floyd's Barbershop,
    # Nail salon chains (Regal Nails @ Walmart, Nail Superstore); VERY high NE Ohio strip-mall density;
    # high foot traffic = heavy staining on entry walkways + parking lot aprons around entry doors;
    # chemical product spills (hair color, bleach, acetone nail products) stain concrete and asphalt regularly;
    # state cosmetology/barbering licensing inspections include exterior appearance of entryway;
    # district managers sign vendor contracts for 10-20 location territories;
    # $200-$500/location; quarterly = $800-$2K/location; 15-salon district = $12K-$30K/year;
    # zero power washing competitors cold-calling salon chain district managers in NE Ohio (added 2026-05-30 run 141)
    'salon district manager', 'hair salon district manager', 'salon regional manager',
    'barbershop district manager', 'beauty salon district manager', 'salon franchise manager',
    'nail salon district manager', 'spa district manager',
    # Coworking Spaces & Flex Offices — IWG/Regus (5+ NE Ohio), WeWork (Cleveland downtown),
    # Industrious, Serendipity Labs; large commercial buildings with shared entry lobbies,
    # parking structures, exterior building facades; FM/building operator signs vendor contracts;
    # premium tenants expect premium appearance; IWG NE Ohio portfolio = $15K-$40K/year;
    # zero competitors cold-calling coworking facility operators in NE Ohio (added 2026-05-30 run 142)
    'coworking space manager', 'flex office manager', 'coworking manager',
    'shared workspace manager', 'business center manager', 'executive suite manager',
    'shared office director', 'coworking director', 'flexible workspace manager',
    # Truck Stops & Travel Centers — Pilot Flying J (5+ NE Ohio: Streetsboro, Hubbard, Austinburg, Medina, Lodi),
    # Love's Travel Stops (3+ NE Ohio), TA/Petro Stopping Centers (4+ NE Ohio), 7-Eleven/Speedway truck plazas;
    # NE Ohio sits at the intersection of I-71, I-76, I-77, I-80, and I-90 — high-density truck corridor;
    # diesel fuel islands + truck parking lots + building exteriors + dumpster pads = constant heavy staining;
    # OEPA SPCC (Spill Prevention Control + Countermeasure) compliance angle — fuel storage = exterior stormwater management;
    # area managers sign vendor contracts for regional portfolios (3-10 locations per deal);
    # $2K-$6K/visit; quarterly = $8K-$24K/facility; one Pilot portfolio deal = $40K-$120K/year;
    # zero NE Ohio power washing competitors cold-calling truck stop area managers (added 2026-05-30 run 143)
    'truck stop manager', 'travel center manager', 'travel plaza manager',
    'truck stop general manager', 'travel center operations manager', 'fuel stop manager',
    'travel center area manager',
    # Ambulatory Surgery Centers (ASCs) — Cleveland Clinic Surgery Centers (Westlake, Solon, Brecksville, Mentor, Avon),
    # UH Surgical Centers (multiple Cuyahoga/Lake/Lorain), Summa Health Surgery Centers (Akron/Barberton),
    # SurgiCenter of Cleveland, MetroHealth Ambulatory Surgery, NOMS Healthcare surgical suites,
    # Ohio Surgical Center, Akron General Ambulatory Surgery; freestanding outpatient surgical facilities —
    # COMPLETELY DISTINCT from urgent care (different licensing, different patient demographic, different appearance standards);
    # Ohio Board of Registration (OBR) state license + CMS certification = non-negotiable exterior appearance standards;
    # surgeons and patients judge the ENTIRE facility's cleanliness as a proxy for surgical sterility standards;
    # one Cleveland Clinic surgery center portfolio deal = $15K-$40K/year; zero competitors using OBR/CMS angle;
    # first pull June 8 Cuyahoga (Cleveland Clinic + UH + MetroHealth ASC campuses) (added 2026-05-30 run 143)
    'ambulatory surgery center manager', 'surgery center administrator', 'surgical center director',
    'outpatient surgery manager', 'asc administrator', 'surgery center operations manager',
    'surgical center operations manager', 'outpatient surgical administrator',
    # Boutique Fitness Studios — Orangetheory Fitness (30+ NE Ohio), F45 Training (15+ NE Ohio),
    # Pure Barre (8+ NE Ohio), Club Pilates (12+ NE Ohio), CycleBar, 9Round, barre3, Anytime Fitness,
    # Snap Fitness, OrangeTheory; COMPLETELY DISTINCT from big-box fitness (Planet Fitness/LA Fitness)
    # already in DANNY_ORG_KEYWORDS under 'fitness center'/'health club';
    # boutique studios have SEPARATE Apollo org tags: 'boutique fitness', 'fitness franchise', etc.;
    # 200+ boutique fitness studios in NE Ohio; franchise owners sign vendor contracts directly (no corporate procurement);
    # heavy member traffic in/out daily = strip-mall entry concrete + parking lot aprons heavily stained;
    # $200-$500/visit; quarterly = $800-$2K/studio; 10-studio franchise territory = $8K-$20K/year;
    # zero competitors cold-calling boutique fitness franchise owners in NE Ohio (added 2026-05-30 run 143)
    'fitness studio manager', 'boutique fitness manager', 'fitness franchise owner',
    'studio director', 'fitness studio director', 'group fitness studio manager',
    # Commercial Truck & Heavy Equipment Dealers — Kenworth of Ohio (Cleveland/Akron),
    # Freightliner Great Lakes Trucks, Mack Trucks of Ohio, Peterbilt (multiple NE Ohio dealers),
    # International Trucks, Volvo Trucks; ALSO: Thompson Lift Truck (Toyota/Cat forklifts in Cleveland),
    # Ohio CAT (Caterpillar — Cuyahoga + Summit + Medina + Geauga), Bobcat of Cleveland,
    # John Deere construction equipment dealers, Komatsu dealer network;
    # COMPLETELY DISTINCT from passenger car/auto dealers (already in DANNY_ORG_KEYWORDS);
    # service bays where trucks sit overnight have oil, hydraulic fluid, diesel exhaust accumulation at 10× the rate of passenger cars;
    # outdoor equipment staging lots are among the dirtiest commercial surfaces in NE Ohio;
    # OEPA/EPA SPCC compliance for hydraulic fluid and diesel storage;
    # dealership GMs or service directors sign vendor contracts; $3K-$10K/visit; quarterly = $12K-$40K/year;
    # zero NE Ohio power washing competitors targeting commercial truck or heavy equipment dealers (added 2026-05-30 run 143)
    'commercial truck dealer manager', 'heavy equipment dealer manager', 'truck dealer general manager',
    'equipment dealer manager', 'commercial vehicle dealer manager', 'heavy equipment sales manager',
    'equipment dealer operations manager',
    # Wineries & Distilleries — Ferrante Winery (Geneva-on-the-Lake), Cuyahoga Valley Winery (Brecksville),
    # Debonne Vineyards (Madison), Erie Shore Vineyard (North Kingsville), Tom's Foolery Distillery (Burton),
    # Cleveland Whiskey (Cleveland), BottleHouse Brewing & Mead Winery (Cleveland Heights/Lakewood);
    # outdoor patios + parking lots + building facades + barrel aging areas;
    # spring patio opening (April-May) = PRIME pitch window — they're cleaning and prepping for season;
    # seasonal events + wedding rentals = appearance is marketing; owner or GM signs vendor contracts directly;
    # COMPLETELY DISTINCT from craft breweries (separate Apollo org tags: 'winery', 'vineyard', 'distillery');
    # $600-$2,000/visit; 2-3x/year = $1,200-$6,000 per winery; zero competitors cold-calling winery GMs (added 2026-05-30 run 144)
    'winery manager', 'vineyard manager', 'winery general manager', 'distillery manager',
    'distillery general manager', 'tasting room manager',
    # Motorcycle & Powersport Dealers — Harley-Davidson of Cleveland (N. Olmsted/Avon Lake), H-D Lake Erie,
    # Mike's Famous Harley-Davidson (Mentor/Akron), Northeast Ohio Powersports (Euclid),
    # Honda Powersports, Kawasaki dealers, Yamaha dealers, Polaris dealers, Can-Am/Sea-Doo dealers;
    # showroom floors + service bays where motorcycles/ATVs sit = oil, grease, hydraulic fluid on concrete;
    # outdoor display lots with bikes = tire marks + weathering stains on aprons;
    # COMPLETELY DISTINCT from car dealers (separate Apollo tags: 'motorcycle dealer', 'powersport dealer');
    # OSHA stormwater compliance for oil runoff from service areas;
    # dealership GMs sign vendor contracts; $800-$2,500/visit; 4x/year = $3,200-$10,000/year;
    # zero NE Ohio power washing competitors targeting motorcycle/powersport dealer GMs (added 2026-05-30 run 144)
    'motorcycle dealer manager', 'powersport dealer manager', 'motorcycle dealership manager',
    'motorcycle dealer general manager', 'powersports manager', 'motorcycle store manager',
    'motorsport dealer manager',
    # RV & Camper Dealers — RV World of Ohio (Hudson/Cuyahoga Falls), Camping World (Streetsboro + Avon),
    # Campers Inn RV (Sandusky area), Holiday Motorhomes, Giant Recreation World, national chains;
    # ENORMOUS paved lots with 50-500 RVs/trailers on display = massive square footage of stained asphalt;
    # service bay areas with black water/gray water hoses, diesel exhaust, generator oil staining;
    # building exteriors + showroom entry areas + service drive aprons;
    # spring (April-May) = inventory prep season before camping season opener;
    # one large dealer lot visit = $2,500-$8,000; 2-3x/year = $5,000-$24,000/year per dealer;
    # COMPLETELY DISTINCT from car dealers (separate Apollo org tags: 'rv dealer', 'camper dealer');
    # zero NE Ohio power washing competitors targeting RV dealership GMs (added 2026-05-30 run 144)
    'rv dealer manager', 'rv dealership manager', 'rv dealer general manager', 'camper dealer manager',
    'recreational vehicle dealer manager', 'rv store manager', 'motorhome dealer manager',
    # Garden Centers & Nurseries — Petitti Garden Centers (12+ NE Ohio — dominant local chain),
    # Sunrize Garden Center, Rittgers' Greenhouse & Garden Center (Medina), Cornell's Garden Center,
    # Rolling Ridge Nursery (Medina), Planter's Choice Nursery (Stow), independent retail nurseries;
    # DISTINCT from landscaping contractors (Carla route) — these are RETAIL garden centers with large display yards;
    # paved display areas accumulate mulch dust, potting soil, fertilizer residue, and cart-traffic staining daily;
    # entry concrete + parking lots + display yard aprons = high-visibility, high-stain surfaces;
    # Ohio Department of Agriculture nursery licensing = exterior facility appearance standard;
    # spring (April-June) = PEAK PITCH WINDOW — they're at peak revenue and see the worst staining;
    # GM or district manager signs vendor contracts; $600-$2,000/location visit; 2-3x/year;
    # Petitti Garden Centers 12 locations × 3 visits = $21,600–$72,000/year (one deal = full season coverage);
    # zero NE Ohio power washing competitors cold-calling garden center operators (added 2026-05-30 run 145)
    'garden center manager', 'nursery manager', 'garden center district manager',
    'plant nursery manager', 'nursery district manager', 'garden supply manager',
    'greenhouse manager',
    # Marine/Boat Dealers — NE Ohio sits on Lake Erie: largest freshwater boating market in the Midwest;
    # Skipper Buds (Mentor/Lorain), West End Boat Sales, ComMar Sales/Bayliner (Sandusky), Inland Seas Yachts (Vermilion),
    # Erie Marine, Superior Outdoors, Twin Post Marina dealers, national chains (MarineMax);
    # large paved outdoor inventory lots with 50-300 boats on display + service bay areas;
    # fiberglass hull repairs + engine service bays accumulate oil, bilge fluid, antifouling residue;
    # concrete lot staining from boat trailers + hydraulic fluids = constant pressure wash need;
    # COMPLETELY DISTINCT from marina management (already in list) — these are retail DEALERS, not marinas;
    # spring (April-June) = peak prep season; boat-buying season opens = appearance is a marketing asset;
    # one large dealer visit = $1,500-$5,000; 2-3x/year = $3,000-$15,000; zero competitors targeting boat dealers;
    # first pull: June 15 Lake County (Skipper Buds Mentor + Lorain + Inland Seas Yachts Vermilion) (added 2026-05-30 run 146)
    'marine dealer manager', 'boat dealer manager', 'marina boat dealer manager',
    'yacht dealer manager', 'marine sales manager', 'boat dealership manager',
    'marine general manager', 'powerboat dealer manager', 'marine dealer general manager',
    # Ice Cream & Frozen Dessert Chains — NE Ohio is peak season NOW (late May/June/July);
    # Dairy Queen (40+ NE Ohio franchise locations), Handel's Homemade Ice Cream (NE Ohio regional chain — dozens of locations,
    # headquartered in Youngstown OH, beloved across all 6 counties), Bruster's Real Ice Cream (NE Ohio franchise),
    # Cold Stone Creamery, Rita's Italian Ice (growing NE Ohio presence), Baskin-Robbins, Dairy Queen franchises;
    # walk-up concrete + paved parking lots stained with dairy, sugar syrup, and foot traffic daily;
    # outdoor seating patio areas + drive-through lanes accumulate heavy grime from peak traffic;
    # peak season (May-August) = worst staining AND when owners most motivated to look good;
    # franchise owners or district managers sign vendor contracts; $300-$800/visit; 2x/year spring+fall cleanup;
    # DISTINCT from QSR/restaurant chains in Apollo org tags — ice cream/frozen dessert has separate tags;
    # zero competitors cold-calling ice cream chain district managers in NE Ohio; first pull June 8 Cuyahoga (added 2026-05-30 run 146)
    'ice cream franchise manager', 'frozen dessert manager', 'ice cream district manager',
    'ice cream store manager', 'frozen yogurt manager', 'dessert franchise owner',
    'ice cream general manager', 'soft serve manager',
    # Party/Event Rental Companies — A-1 Party Rental (Solon), Taylor Rental Centers (Avon/Brunswick/N. Olmsted/Medina),
    # Fun Planners, Abbey Rents, Classic Party Rentals; large outdoor storage yards (tents/tables/chairs) + fleet vehicles
    # returning from winter storage = heavy grime accumulation; OSHA stormwater compliance on storage yard runoff;
    # spring = dirty equipment season; peak season May-September = wedding/graduation/corporate events;
    # owner-operators or managers sign vendor contracts directly without procurement committees;
    # zero NE Ohio power washing competitors targeting party rental yards; $800-$3,000/visit; 2-3x/year;
    # first pull June 8 Cuyahoga (added 2026-05-30 run 147)
    'event rental manager', 'party rental manager', 'party supply manager', 'event equipment manager',
    'tent rental manager', 'special event manager', 'party rental owner', 'event rental owner',
    # Trampoline Parks & Indoor Adventure Centers (added 2026-05-30 run 148)
    'trampoline park manager', 'indoor adventure park manager', 'trampoline park franchise owner',
    'adventure park director', 'trampoline park general manager', 'indoor play center manager',
    'bounce park manager',
    # Moving & Relocation Companies (added 2026-05-30 run 148)
    'moving company manager', 'moving company operations manager', 'relocation services manager',
    'moving and storage manager', 'van lines agent manager', 'relocation manager',
    'moving company general manager',
    # Off-Price Apparel & Home Goods Retail — TJ Maxx (15+ NE Ohio), Marshalls (10+), HomeGoods (10+),
    # Burlington Coat Factory (6+), Ross Dress for Less (3+); DISTINCT from dollar stores (different Apollo org tags);
    # large strip-mall parking lots + building exteriors; district managers sign vendor contracts for 10-20 stores;
    # NE Ohio has 35+ TJ Maxx/Marshalls/HomeGoods alone; appearance-sensitive shoppers = brand standard is HIGH;
    # $500-$1,500/location; 2-3x/year; 15-location district deal = $15K-$67K/year; zero competitors (added 2026-05-30 run 149)
    'off-price retail district manager', 'discount apparel district manager', 'off price store manager',
    'value retail district manager', 'home goods district manager', 'off-price district manager',
    'discount fashion manager',
    # Truck Rental Companies — U-Haul (25+ NE Ohio), Penske Truck Rental (15+), Ryder System (10+), Budget Truck Rental;
    # DISTINCT from passenger car rental (different Apollo org keywords; truck lots are filthier — exhaust + oil + road grime);
    # large paved lots with moving trucks accumulate road salt + diesel exhaust; district managers sign multi-location contracts;
    # $800-$2,500/lot visit; quarterly = $3,200-$10,000/year per location; zero competitors cold-calling truck rental DMs (added 2026-05-30 run 149)
    'truck rental district manager', 'moving truck rental manager', 'truck rental location manager',
    'rental truck fleet manager', 'moving truck manager', 'truck rental operations manager',
    # Lumber Yards & Building Supply Distributors — 84 Lumber (15+ NE Ohio stores), ABC Supply Co. (largest roofing
    # distributor in US, multiple NE Ohio branches), Builders FirstSource, Heritage Building Products;
    # DISTINCT from Home Depot/Lowe's (retail consumer-facing hardware) — these are WHOLESALE contractor-only supply yards;
    # open outdoor storage yards: lumber in concrete bays, roofing shingles on pallets, masonry on concrete pads;
    # forklift oil + concrete dust + wood tannin staining accumulates rapidly in material yards;
    # branch managers + operations managers sign vendor contracts for yard and dock maintenance;
    # $2,000-$6,000/visit; quarterly = $8,000-$24,000/year per large branch; zero competitors cold-calling
    # building supply branch managers in NE Ohio; contractor customer base sees clean yard = professional operation (added 2026-05-31 run 150)
    'lumber yard manager', 'building supply manager', 'lumber yard branch manager',
    'building materials branch manager', 'roofing supply manager', 'building supply branch manager',
    # Behavioral Health & Mental Health Clinics — Signature Health (80+ NE Ohio clinics), Recovery Resources,
    # Frontline Service, LCADA Way, Emerge Behavioral Wellness (Akron), Crossroads Health, Harbor Light,
    # University Hospitals Behavioral Health, Cleveland Clinic Behavioral Resources;
    # DISTINCT from urgent care + physical therapy + ambulatory surgery centers (all already in list);
    # Ohio ODMH/OMHAS facility licensing inspections check patient-facing exterior appearance;
    # stigma-reduction brand campaigns make appearance a clinical credibility signal (not just curb appeal);
    # district managers / regional directors sign multi-clinic vendor contracts for 5-15 locations;
    # $800-$2,500/clinic visit; 10-clinic district deal = $8,000-$25,000/year; zero competitors targeting
    # behavioral health facility managers in NE Ohio (added 2026-05-31 run 150)
    'behavioral health director', 'mental health clinic director', 'behavioral health clinic manager',
    'mental health facility manager', 'behavioral health regional director', 'substance abuse clinic manager',
    'addiction treatment center director', 'outpatient behavioral health manager',
    # Motorsports Venues & Racing Facilities — Summit Motorsports Park (Norwalk — largest drag strip in OH:
    # Funny Car Cavalcade, Night of Fire), Mid-Ohio Sports Car Course (Lexington — road racing, IndyCar),
    # Medina County Speedway (Medina — dirt oval), Mahoning Valley Speedway (Youngstown area),
    # indoor karting: Autobahn Indoor Speedway (Brecksville), K1 Speed, Kart World;
    # enormous paved parking lots + grandstand concourse concrete + pit lane aprons + building exteriors;
    # tire rubber accumulation + oil/fuel residue from racing operations = constant high-intensity staining;
    # spring (April-June) = racing season opener = peak pitch window for pre-season cleaning contracts;
    # facility managers / venue directors sign vendor contracts; zero competitors targeting motorsport venues;
    # $2,000-$8,000/visit; 2-3x/year = $4,000-$24,000/year per venue (added 2026-05-31 run 151)
    'speedway operations manager', 'motorsports venue manager', 'racetrack facilities manager',
    'motorsports park manager', 'racing venue director', 'karting facility manager',
    'indoor karting manager', 'speedway manager', 'raceway manager',
    # Print & Business Services Chains — FedEx Office (25+ NE Ohio), UPS Store (50+ NE Ohio franchise owners),
    # AlphaGraphics (15+ NE Ohio), Minuteman Press (20+ NE Ohio), Sir Speedy, The UPS Store;
    # strip-mall entry concrete stained by box dust, packing tape residue, heavy foot traffic;
    # state franchise brand standards = exterior appearance maintained to corporate spec;
    # UPS Store franchise owners are INDEPENDENT BUSINESS OWNERS who sign their own vendor contracts (1-3 stores each);
    # FedEx Office district managers oversee 5-10 locations in NE Ohio territory;
    # $200-$600/location; quarterly = $800-$2,400/location; 10-location territory = $8K-$24K/year;
    # DISTINCT Apollo org tags from restaurant/retail — tagged 'printing services', 'shipping services' (added 2026-05-31 run 151)
    'print center manager', 'print shop district manager', 'printing services manager',
    'fedex office manager', 'ups store franchise owner', 'business services manager',
    'shipping center manager', 'copy center manager',
    # Chiropractic Chains & Spinal Care Groups — The Joint Chiropractic (15+ NE Ohio franchise locations),
    # ChiroOne Wellness Centers, Ohio State Chiropractic Board member practices, Spine & Rehab Group;
    # DISTINCT from physical therapy (different Ohio licensing body: Ohio State Chiropractic Board);
    # franchise owners sign vendor contracts directly for individual locations without corporate procurement;
    # strip-mall storefronts with high patient foot traffic = persistent oil stain + salt residue on entry concrete;
    # Ohio chiropractic board licensing inspections include patient-facing exterior appearance standard;
    # $300–$700/visit; 2×/year spring + fall cleanup; 10-location territory = $6K–$14K/year;
    # zero NE Ohio power washing competitors cold-calling chiropractic franchise owners (added 2026-05-31 run 152)
    'chiropractic district manager', 'chiropractor practice manager', 'chiropractic clinic manager',
    'chiropractic regional manager', 'chiropractic franchise owner', 'spine center manager',
    'chiropractic practice director', 'spinal care manager',
    # Escape Rooms & Interactive Entertainment Venues — NE Ohio: Breakout Games (franchise locations in
    # Strongsville + Independence), room2escape (Parma), Paranormal Escape (Cleveland), Cleveland Escape,
    # Scene 75 Entertainment Center (Berea — NE Ohio's largest indoor entertainment venue: 100,000+ sq ft),
    # Puzzled Escape Games, Escapades Ohio, Nickle City Fun Center (Euclid);
    # DISTINCT from trampoline parks (already in list) + bowling alleys (already in list);
    # parking lots + building exteriors + entrance canopies stained from high evening/weekend traffic;
    # summer peak = families + birthday parties + corporate team-building events = HIGH visibility pressure;
    # franchise owners sign vendor contracts directly (1-3 locations each = fast close, no procurement committee);
    # $400–$1,000/location visit; 2–3×/year = $800–$3,000/year per location; zero competitors cold-calling;
    # first pull: June 8 Cuyahoga (Scene 75 Berea, Breakout Games Strongsville + Independence) (added 2026-05-31 run 152)
    'escape room manager', 'escape room franchise owner', 'escape room owner', 'escape room operator',
    'interactive entertainment manager', 'escape room general manager', 'escape room director',
    'immersive experience manager', 'entertainment venue franchise owner',
    # Charter Schools & Charter Management Organizations — DISTINCT from public school districts ('school district' tag above)
    # and private/independent schools ('private school' tag above); 'charter school' is a separate Apollo org tag;
    # NE Ohio: Breakthrough Schools (12 Cleveland campuses), Constellation Schools (7+ campuses), Citizens Academy,
    # MC2 STEM High School, Intergenerational School, Hope Academy (35+ OH statewide), Ohio Department of Education
    # authorizer compliance = facility appearance review; CMO facilities directors sign multi-campus vendor contracts;
    # summer (June-August) = buildings empty = peak exterior maintenance window (same as public schools);
    # $800-$3,000/building; 2x/year; 10-campus CMO deal = $16K-$60K/year; zero competitors targeting this segment (added 2026-05-31 run 154)
    'charter school director', 'charter management director', 'charter school principal',
    'charter academy director', 'charter operations director', 'director of school operations',
    'charter principal', 'cmo facilities director',
    # Outdoor RV & Boat Storage Facilities — DISTINCT from marinas (wet slips/docking, already in list) and self-storage
    # (indoor climate-controlled units); standalone outdoor yards storing boats, RVs, travel trailers, farm equipment;
    # NE Ohio: Lake Road Storage (Mentor-on-the-Lake), Northcoast Boat & RV Storage, Lakeshore Storage, Bass Lake Marina
    # dry storage, multiple independent operators along Lake Erie corridor (Lake/Lorain/Erie county border);
    # spring commissioning season = RIGHT NOW; customers picking up boats/RVs want a clean, presentable facility;
    # enormous concrete/gravel pads accumulate 6 months of winter salt, bird droppings, algae from pooling;
    # owner-operators sign vendor contracts directly; $1,500-$5,000/visit; 2x/year (spring + fall close) = $3K-$10K/year;
    # 200-500 storage space facility = large paved surface area = high per-visit revenue; zero competitors (added 2026-05-31 run 154)
    'rv storage manager', 'outdoor storage facility manager',
    'boat storage manager', 'marine dry storage manager', 'vehicle storage manager',
    # Ice Rinks & Indoor Ice Arenas — Palace Ice Arenas (Solon/Twinsburg multi-location operator),
    # Mentor Ice Arena (City of Mentor recreation facility), OBM Arena (Parma area — youth hockey),
    # Brooklyn Ice Center, Westlake Rec Center ice rink, Kent State University ice rink,
    # various YMCA ice facilities and youth hockey association arenas (Summit/Cuyahoga/Lake counties);
    # DISTINCT from sports complexes/youth sports complexes already in list — Apollo indexes dedicated
    # ice skating facilities under 'ice rink'/'ice arena'/'hockey rink' org tags (not 'sports complex');
    # SUMMER = maintenance window: no ice = full exterior access; buildings haven't been cleaned since
    # last fall; facility director is planning summer maintenance RIGHT NOW in May-June;
    # 2x/year (spring post-season + early fall pre-season) = $2K-$8K per location;
    # multi-location operator deal (Palace Ice Arenas: 2-3 NE Ohio rinks) = $6K-$24K/year;
    # zero NE Ohio power washing competitors cold-calling ice arena facility managers (added 2026-05-31 run 155)
    'ice rink manager', 'ice arena manager', 'ice arena director', 'skating center director',
    'ice facility manager', 'ice sports manager', 'skating rink manager', 'hockey arena manager',
    # Sporting Goods Chains — Dick's Sporting Goods (10+ NE Ohio: Strongsville, Macedonia, Mentor, Twinsburg,
    # North Olmsted, Avon, Berea, Akron, Cuyahoga Falls + more), Academy Sports & Outdoors (3 NE Ohio),
    # Play It Again Sports (franchise-owned, 8+ NE Ohio); DISTINCT from sports facilities/YMCA (already in list);
    # large paved parking lots (Dick's anchors major shopping centers: Great Northern, SouthPark, Belden Village);
    # building exteriors + seasonal outdoor display areas + dumpster pad areas;
    # district managers sign vendor contracts for 5-15 store territories;
    # $600-$2,000/location; quarterly = $2.4K-$8K/location; 10-location district = $24K-$80K/year;
    # zero competitors cold-calling sporting goods retail district managers in NE Ohio (added 2026-05-31 run 156)
    'sporting goods district manager', 'sporting goods store manager', 'sporting goods manager',
    'sporting goods regional manager', 'sports retail district manager', 'sports store manager',
    'athletic retail manager', 'sporting goods operations manager',
    # Tractor Supply Co. & Farm/Rural Supply Chains — Tractor Supply Co. (20+ NE Ohio), Rural King (4 NE Ohio),
    # Southern States, Agway; DISTINCT from all existing segments — genuine rural-suburban NE Ohio segment
    # concentrated in Medina/Lorain/Summit/Geauga counties along the rural-suburban interface;
    # large outdoor display yards + garden/supply lots + equipment staging areas + building exteriors;
    # spring/summer = display lots packed with grills, lawn equipment, chick brooders, fencing = staining season;
    # district managers sign vendor contracts for 3-8 store territories;
    # $800-$2,500/location; 5-location district = $4K-$12.5K/year;
    # zero NE Ohio power washing competitors targeting farm supply store district managers (added 2026-05-31 run 156)
    'tractor supply district manager', 'tractor supply store manager', 'farm supply district manager',
    'farm supply store manager', 'rural supply manager', 'farm store manager',
    'agricultural retail manager', 'farm supply operations manager',
    # Used Car Superstores & Independent Used Car Lots — CarMax (Willoughby Hills, Mayfield Heights),
    # DriveTime (multiple NE Ohio locations), AutoNation pre-owned centers, hundreds of independent dealers;
    # DISTINCT from franchise car dealers (different Apollo org tags: 'used car dealer' vs 'car dealer franchise');
    # large open-air display lots: 50-400 vehicles, heavy rubber + oil + exhaust accumulation year-round;
    # buy here pay here lots (high-volume, lower-income areas) — curb appeal = walk-in traffic = revenue;
    # spring = inventory refresh season; owner-operators and district managers sign vendor contracts directly;
    # $1,000-$3,000/visit; 2x/year = $2,000-$6,000/location; CarMax multi-location deal = $20K+/year;
    # zero competitors cold-calling used car lot operators in NE Ohio (added 2026-05-31 run 157)
    'used car lot manager', 'used car dealership manager', 'pre-owned vehicle manager',
    'used auto dealer manager', 'independent car dealer owner', 'used car district manager',
    'pre-owned sales manager', 'used car operations manager',
    # Outdoor Power Equipment Dealers — STIHL dealers (50+ NE Ohio independent shops), Husqvarna dealers,
    # Cub Cadet dealers, BJ's Rental & Equipment, Northern Tool + Equipment (3 NE Ohio);
    # DISTINCT from farm equipment dealers (commercial/construction scale, added Run 143) and car dealers;
    # large outdoor display yards with riding mowers, zero-turns, snow blowers, generators on display;
    # spring = PEAK DISPLAY SEASON = RIGHT NOW — lots packed, max visual impact;
    # owner-operators sign vendor contracts directly; one large dealership = 2-3 visits/year;
    # $400-$1,500/visit; zero NE Ohio power washing competitors targeting outdoor power equipment dealers (added 2026-05-31 run 157)
    'power equipment dealer manager', 'outdoor power equipment manager', 'small engine dealer manager',
    'equipment dealer owner', 'power equipment store manager', 'lawn equipment dealer manager',
    'outdoor equipment manager',
    # Vocational & Trade Schools / Career Technical Education Centers — Ohio Technical College (Cleveland),
    # Lincoln Tech (Ohio), EHOVE Career Center (Erie/Huron/Ottawa counties), Portage Lakes Career Center,
    # Mahoning County Career & Technical Center, Stark County Career Center, Auburn Career Center (Geauga),
    # Tri-C Workforce Development, Cuyahoga Valley Career Center (CVCC), Lake County Educational Service Center;
    # DISTINCT from public K-12 school districts (Run 119), private schools (Run 99), charter schools (Run 154);
    # automotive/welding/HVAC/culinary labs = heavy oil, metal dust, chemical accumulation on exterior surfaces;
    # State CTE program compliance inspections check facility appearance; directors sign vendor contracts;
    # summer = buildings less occupied = ideal exterior wash window; $800-$2,500/visit; 2x/year;
    # zero NE Ohio power washing competitors targeting CTE/vocational center directors (added 2026-05-31 run 157)
    'career technical director', 'vocational school director', 'trade school director',
    'cte director', 'career center principal', 'career technical center manager',
    'vocational education director', 'cte facilities manager',
    # Animal Shelters & Humane Societies — Cleveland APL (2 main campuses + 3 satellite adoption centers),
    # Summit County Animal Control & Adoption, Geauga County Humane Society, Lake County APL,
    # Lorain County APL, Portage County Animal Protective League, Mahoning County Humane Society;
    # 50+ NE Ohio animal shelters and humane societies; Ohio ORC 955.16 shelter licensing + state USDA APHIS
    # registered facilities require maintained exterior appearance; outdoor dog runs + concrete kennels +
    # building exteriors + parking lots accumulate biological residue, mud, waste at extreme rates;
    # directors/executive directors sign vendor contracts directly (no procurement committee at non-profits);
    # DISTINCT from pet boarding/kennel (commercial boarders) and vet clinics (different Apollo org tags);
    # zero NE Ohio power washing competitors targeting humane society directors; $500-$1,500/visit; 2-3x/year (added 2026-05-31 run 158)
    'animal shelter director', 'animal shelter manager', 'humane society director',
    'animal control director', 'shelter operations manager', 'animal services director',
    'animal welfare director', 'adoption center manager', 'animal shelter executive director',
    # Campgrounds & RV Parks — Ohio State Parks with full-hookup campgrounds (Punderson (Newbury),
    # West Branch (Ravenna), Findley (Wellington — Lorain County), Nelson Ledges, Buck Creek State Park);
    # KOA Campgrounds (Sandusky KOA, Streetsboro/Cleveland SE KOA, Lake Erie Western Basin KOA);
    # Yogi Bear's Jellystone Park (Timberlane Campground, Streetsboro); Cherry Hill Village (Canton);
    # DISTINCT from RV dealers (sell RVs) and RV storage facilities (store RVs) — these are OVERNIGHT facilities;
    # DISTINCT Apollo org tags: 'campground', 'rv park', 'camping resort' return zero overlap with above;
    # large paved RV pad areas, concrete dump station pads, bathhouse building exteriors, recreation halls;
    # spring opening = RIGHT NOW — facilities coming out of winter need to be cleaned before Memorial Day;
    # campground managers sign vendor contracts; $800-$3,000/visit; 2x/year (spring + fall);
    # NE Ohio has 30+ state park campgrounds + 15+ KOA/franchise locations; zero competitors (added 2026-05-31 run 158)
    'campground manager', 'campground director', 'rv park manager', 'camping resort manager',
    'campground owner', 'camp operations manager', 'campground general manager',
    'rv resort manager', 'camping facility manager', 'outdoor recreation manager',
    # Mobile Home Parks & Manufactured Housing Communities — NE Ohio has 200+ communities;
    # large concentrations in Medina (Medina MH Village, Windmill Lake MH Community), Lorain (Avon Lake MH Park,
    # Lakeview Estates), Summit (Portage Lakes MH Park, Green Meadows), Cuyahoga (North Olmsted Estates),
    # Geauga/Lake (rural community clusters); national operators: Sun Communities (largest US MH REIT),
    # Equity LifeStyle Properties (ELS), UDR — these own dozens of NE Ohio communities under one FM team;
    # DISTINCT from 'apartment management'/'multifamily' (different Apollo org tags); Apollo indexes
    # mobile home/manufactured housing under 'mobile home park', 'manufactured housing community' tags;
    # large paved internal streets + community centers + laundry buildings + entrance/check-in areas;
    # community managers sign vendor contracts; $1,000-$3,000/visit; 2x/year;
    # Sun Communities NE Ohio portfolio deal = $15K-$40K/year; zero competitors targeting MH park FMs (added 2026-05-31 run 158)
    'mobile home park manager', 'manufactured housing community manager', 'mobile home park director',
    'manufactured housing manager', 'community park manager', 'manufactured community director',
    'mobile home community manager', 'mobile home park operations manager',
    # Senior Adult Day Programs & Adult Day Care Centers — Ohio Department of Aging licensed;
    # DISTINCT from residential senior living (independent/assisted living already in list);
    # non-residential daytime programs for seniors; accessible parking + entrance ramps + walkways;
    # medical transport van drop-off areas accumulate diesel + grime; state licensing inspection = appearance standard;
    # 60+ NE Ohio adult day programs; $400-$1,200/visit; 2-3x/year; zero competitors (added 2026-05-31 run 159)
    'adult day program director', 'adult day care director', 'senior day program manager',
    'adult day services director', 'adult day center manager', 'senior day services manager',
    'adult day health director', 'adult day program manager',
    # Diagnostic Imaging & Radiology Centers — DISTINCT from urgent care, hospitals, and medical office parks;
    # stand-alone imaging centers accessed via separate Apollo org tags ('diagnostic imaging', 'radiology center');
    # Ohio Dept of Health radiology licensing = exterior cleanliness standard; large accessible surface parking;
    # HealthSpan Radiology (NE Ohio's largest independent network — 15+ locations), Cleveland Clinic Imaging,
    # UH Radiology, Summa Radiology, Mid-Ohio Radiology; district managers sign multi-site vendor contracts;
    # $600-$1,800/visit; 2x/year; zero competitors cold-calling imaging center managers in NE Ohio (added 2026-05-31 run 159)
    'radiology center manager', 'imaging center manager', 'diagnostic imaging manager',
    'radiology practice manager', 'mri center manager', 'imaging director', 'radiology director',
    'diagnostic center manager',
    # Swim Schools & Aquatic Learn-to-Swim Programs — Ohio Dept of Health pool licensing = exterior cleanliness standard;
    # DISTINCT from YMCA (already in list), aquatic centers (already in list), and community pools (already in list);
    # stand-alone franchise swim schools with separate Apollo org tags: 'swim school', 'swim academy';
    # Goldfish Swim School (3+ NE Ohio franchise locations — Strongsville, North Olmsted, Mentor area),
    # British Swim School (2+ NE Ohio franchise locations), SwimKids of Ohio, Aqua-Tots NE Ohio;
    # PEAK SEASON RIGHT NOW — summer = highest enrollment period; parents touring facilities;
    # franchise owners sign vendor contracts directly; pool decks + parking lots + building exteriors;
    # $500-$1,500/location; 2x/year; zero competitors cold-calling swim school franchise owners (added 2026-05-31 run 159)
    'swim school director', 'swim school manager', 'swim academy director', 'swim school owner',
    'swim school franchise owner', 'aquatic learning director', 'learn to swim director',
    'swim program manager',
    # Massage Therapy & Wellness Chains — Massage Envy (30+ NE Ohio franchise locations),
    # Elements Massage (8+ NE Ohio), Hand & Stone Massage & Facial Spa (4+ NE Ohio), LaVida Massage;
    # DISTINCT from hair/nail salon chains (different Apollo org tags: 'massage therapy' vs 'hair salon'/'nail salon');
    # Ohio State Massage Therapy Board licensing = exterior appearance standard;
    # high repeat client foot traffic (weekly or bi-weekly appointments) = persistent oil stain + grime on entry concrete;
    # franchise owners sign vendor contracts independently (1-3 locations each = fast close, no procurement committee);
    # $300-$800/location; 2x/year = $600-$1,600; 10-franchise territory = $6K-$16K/year;
    # zero competitors cold-calling massage therapy franchise owners in NE Ohio; first pull June 8 Cuyahoga (added 2026-05-31 run 160)
    'massage therapy manager', 'massage center manager', 'wellness studio manager',
    'massage franchise owner', 'wellness center manager', 'spa franchise manager',
    'massage clinic manager', 'therapeutic massage manager',
    # Non-Profit & Social Service Organizations — Salvation Army NE Ohio (6+ chapter facilities + thrift stores),
    # Catholic Charities Diocese of Cleveland (20+ program offices), United Way of Greater Cleveland,
    # Volunteers of America of Greater Ohio, Second Harvest Food Bank of NE Ohio, Habitat for Humanity ReStores
    # (5+ NE Ohio locations), Lutheran Metropolitan Ministry, Jewish Family Service Association of Cleveland;
    # DISTINCT from all existing segments — these are non-profit/social service orgs with DISTINCT Apollo org tags
    # ('nonprofit organization', 'social services', 'food bank', 'thrift store');
    # donor perception is the fundraising platform — clean, maintained facilities signal organizational credibility;
    # large building footprints (thrift store warehouses, food bank distribution facilities, service center complexes);
    # executive directors sign vendor contracts; most have no active power washing vendor relationship;
    # $500-$2,000/facility; 2x/year; multi-location chapter deal = $10K-$25K/year;
    # zero competitors cold-calling nonprofit operations directors for power washing in NE Ohio; first pull June 8 Cuyahoga (added 2026-05-31 run 160)
    'nonprofit executive director', 'social services director', 'nonprofit facilities director',
    'nonprofit operations manager', 'thrift store district manager', 'food bank operations director',
    'community services manager', 'social service agency director',
    # Auto Glass Repair & Windshield Replacement Chains — Safelite AutoGlass (15+ NE Ohio service centers),
    # Glass America (Cleveland-based national chain, 50+ NE Ohio locations — HQ on Carnegie Ave);
    # drive-in service bays + large concrete aprons + building exteriors + vehicle staging areas;
    # Ohio Dept of Commerce glass contractor licensing = exterior appearance standard;
    # district managers sign multi-location vendor contracts; owner-operators at independent shops sign directly;
    # $600-$1,500/location; 2-3x/year; Glass America regional deal = $30K-$75K/year;
    # zero competitors cold-calling auto glass district managers in NE Ohio; first pull June 8 Cuyahoga (added 2026-05-31 run 161)
    'auto glass manager', 'auto glass district manager', 'windshield repair manager',
    'glass repair center manager', 'auto glass franchise owner', 'auto glass operations manager',
    'windshield replacement manager', 'auto glass general manager',
    # Furniture & Home Furnishings Retail Chains — Ashley Furniture HomeStore (5+ NE Ohio: Solon, Mentor, Strongsville),
    # Value City Furniture (10+ NE Ohio: Mayfield, Berea, Stow, Parma, Mentor, etc.),
    # Bob's Discount Furniture (Mayfield, Westgate, Akron area — 3+ NE Ohio), Big Sandy Superstore (NE Ohio expanding),
    # Nationwide Furniture (Cleveland area); large showrooms + enormous parking lots;
    # district managers sign multi-location vendor contracts; $1,500-$4,500/location; 2x/year;
    # Ashley Furniture 5-location district deal = $15K-$45K/year; zero competitors cold-calling furniture DMs (added 2026-05-31 run 161)
    'furniture store manager', 'furniture district manager', 'furniture retail manager',
    'home furnishings store manager', 'furniture store general manager',
    'furniture district operations manager', 'home furnishings district manager', 'furniture showroom manager',
    # Salon Suites & Booth Rental Studios — Sola Salon Studios (10+ NE Ohio: Independence, Beachwood, Mentor, Westlake, etc.
    # — fastest-growing salon suite franchise in US), MY SALON Suite (4+ NE Ohio), Phenix Salon Suites (Strongsville/Avon),
    # Salon Lofts (5+ NE Ohio); each building houses 30-60 individual booth renters with heavy daily foot traffic;
    # large parking lots + strip-mall building exteriors + entry concrete; franchise owners sign vendor contracts independently;
    # GENUINELY DISTINCT from hair/nail salon chains (Run 141, 'hair salon chain' Apollo tag) — salon suites are
    # commercial real estate operators, not service businesses; Apollo tags 'salon suite', 'salon suites' = zero overlap;
    # $800-$2,500/building; 2-3x/year; 4-location Sola franchise = $6K-$20K/year; zero competitors (added 2026-05-31 run 161)
    'salon suite manager', 'salon suites director', 'salon suite franchise owner',
    'booth rental manager', 'salon suite operations manager', 'salon suite property manager',
    'salon suite general manager',
    # Tutoring Centers & Learning Centers — Kumon (50+ NE Ohio franchise locations), Sylvan Learning (8+ NE Ohio),
    # Mathnasium (10+ NE Ohio), Huntington Learning Center (12+ NE Ohio), Oxford Learning;
    # DISTINCT from private schools (run 99), charter schools (run 154), vocational schools (run 157) — distinct Apollo org tags;
    # Ohio DOE tutoring program regulations; franchise owners sign vendor contracts independently — fast close;
    # strip-mall storefronts: parking lot + entry concrete + building exterior; high daily foot traffic (parents + students);
    # $200-$500/location; 2x/year; Kumon area developer (20+ centers, one contact) = $8K-$20K/year; zero competitors (added 2026-06-01 run 162)
    'tutoring center director', 'learning center director', 'tutoring center manager',
    'learning center manager', 'tutoring franchise owner', 'kumon center director',
    'academic learning center manager', 'after school program director',
    # Med Spas & Aesthetic Clinics — European Wax Center (20+ NE Ohio franchise locations),
    # LaserAway (entering NE Ohio), National Laser Institute (Cleveland area), Clearwave Health;
    # Ohio Medical Board + Ohio State Cosmetology Board licensing = exterior appearance standard;
    # DISTINCT from massage therapy chains (run 160), hair salon chains (run 141), boutique fitness (run 143);
    # Apollo tags 'medical spa', 'med spa', 'aesthetic clinic', 'medspa' return zero overlap with existing segments;
    # franchise owners sign vendor contracts independently — fast close; strip-mall storefronts;
    # $400-$1,200/location; 2x/year; European Wax Center 15-location NE Ohio territory = $12K-$36K/year; zero competitors (added 2026-06-01 run 162)
    'med spa manager', 'medical spa director', 'medical spa manager', 'aesthetic clinic manager',
    'medspa manager', 'medical aesthetics manager', 'cosmetic clinic manager',
    'european wax center manager', 'laser clinic manager', 'aesthetics director',
    # Dry Cleaning & Laundry Service Chains — Fox Cleaners (Cleveland-based chain, 30+ NE Ohio locations),
    # Martinizing Dry Cleaning (franchise), One Hour Cleaners, Dry Clean USA, Sketchley Cleaners;
    # DISTINCT from coin laundries/laundromats (run 135 — self-service, 'coin laundry' Apollo tag);
    # Apollo tags 'dry cleaning', 'dry cleaner', 'laundry service' return zero overlap with existing segments;
    # Ohio EPA perchloroethylene dry-cleaning solvent regulations → exterior appearance compliance standard;
    # customer-facing storefronts = curb appeal is brand image; Fox Cleaners 30-location NE Ohio deal = $12K-$36K/year;
    # franchise owners / multi-location operators sign vendor contracts; $200-$600/location; 2x/year; zero competitors (added 2026-06-01 run 162)
    'dry cleaning manager', 'dry cleaner manager', 'dry cleaning chain manager',
    'laundry service manager', 'dry cleaning franchise owner', 'laundry chain manager',
    'dry cleaning district manager', 'garment care manager',
    # Home Care Agencies & In-Home Health Services — Visiting Angels (15+ NE Ohio offices),
    # Home Instead (12+ NE Ohio offices), Comfort Keepers, Bayada Home Health, Kindred at Home;
    # Ohio ODJFS home health agency licensing = exterior appearance standard;
    # DISTINCT from senior living facilities (run 96), behavioral health clinics (run 150);
    # office buildings + parking lots; regional directors sign vendor contracts; 100+ NE Ohio offices;
    # $600-$1,800/office; annual contracts; first pull June 8 Cuyahoga (added 2026-06-01 run 163)
    'home care director', 'home health director', 'home care regional director',
    'home health regional director', 'home care agency director', 'in-home care director',
    'home care manager', 'home health manager', 'home care district manager',
    'visiting angels franchise owner', 'home instead franchise owner',
    # Pawn Shops & Cash Advance / Payday Loan Chains — Cashland/EZCorp (20+ NE Ohio),
    # Advance America (15+ NE Ohio), ACE Cash Express, Check Into Cash, Dollar Loan Center;
    # DISTINCT from banks/credit unions (run 100), dollar stores (run 136);
    # high-traffic strip mall storefronts; district managers sign multi-location vendor contracts;
    # heavy foot traffic = dirty facades + parking + dumpster areas; $300-$600/location;
    # 60+ NE Ohio locations; 10-location district = $12K-$24K/year; zero competitors (added 2026-06-01 run 163)
    'pawn shop manager', 'pawn shop district manager', 'pawn shop owner', 'cash advance manager',
    'payday loan manager', 'check cashing manager', 'cashland manager', 'pawn store manager',
    'pawn shop operations manager', 'financial retail district manager',
    # Hearing Aid Centers & Audiology Clinics — HearingLife (50+ NE Ohio), Miracle-Ear (30+ NE Ohio),
    # Beltone, NovaCare Hearing, Connect Hearing, Amplifon;
    # Ohio Audiology & Speech-Language Pathology Board licensing = exterior appearance standard;
    # DISTINCT from optical/vision centers (run 139), medical offices (run 101);
    # district managers sign multi-location vendor contracts for 5-15 locations per district;
    # 100+ NE Ohio hearing center locations; $400-$1,200/location;
    # HearingLife NE Ohio district deal = $12K-$36K/year; zero competitors (added 2026-06-01 run 163)
    'hearing center director', 'hearing aid center manager', 'audiology clinic manager',
    'hearing health director', 'hearing center district manager', 'audiologist practice manager',
    'hearing clinic manager', 'audiology district manager', 'hearing center operations manager',
    # Staffing & Temporary Employment Agencies — Robert Half (multiple NE Ohio offices), Manpower (10+ NE Ohio),
    # Kelly Services (NE Ohio HQ Troy MI but large Cleveland branch), Adecco (8+ NE Ohio), Randstad (8+ NE Ohio),
    # Aerotek/Allegis Group (Allegis HQ Hanover MD; Aerotek Cleveland office = major industrial/tech placement hub),
    # Integrity Staffing Solutions (Amazon-partnered, Cleveland-area warehousing staff);
    # COMPLETELY DISTINCT from manufacturing/industrial (run 118 — factory buildings/loading docks),
    # distribution centers (run 105), and corporate parks (run 101 — DANNY_ORG_KEYWORDS 'corporate park');
    # staffing agencies are OFFICE buildings in suburban business parks and strip mall storefronts —
    # Apollo tags them under 'staffing agency', 'temporary staffing', 'employment agency', 'workforce solutions';
    # branch managers and district directors sign vendor contracts for exterior maintenance;
    # 50+ staffing agency branches across NE Ohio 7-county area; parking lots + building exteriors;
    # May-June = peak staffing season (summer industrial hiring surge, Amazon surge prep) = agencies are VISIBLE;
    # $400-$1,200/office visit; 2x/year = $800-$2,400/office; 10-office district deal = $8K-$24K/year;
    # zero competitors cold-calling staffing agency branch managers in NE Ohio; first pull June 8 Cuyahoga (added 2026-06-01 run 164)
    'staffing branch manager', 'staffing district manager', 'workforce solutions manager',
    'employment agency manager', 'temp agency manager', 'staffing operations manager',
    'staffing agency director', 'workforce director',
    # Big Box Electronics Retail — Best Buy (10+ large-format NE Ohio stores: Strongsville, Macedonia, Mentor,
    # North Olmsted, Berea, Avon, Akron/Montrose, Cuyahoga Falls, Twinsburg, Mayfield Heights);
    # Micro Center (Westgate Cleveland — flagship single-location but enormous store; largest private tech retailer in US);
    # COMPLETELY DISTINCT from wireless/telecom retail (run 137 — small strip-mall kiosks),
    # auto parts stores (run 136), and hardware/home improvement (run 136);
    # Best Buy stores anchor major NE Ohio shopping centers (SouthPark, Great Northern, Belden Village side);
    # ENORMOUS parking lots (5-10 acres) + building exteriors + seasonal outdoor display areas;
    # heavy foot traffic (electronics buyers bring kids) = constantly stained entry concrete + cart aprons;
    # Best Buy district managers oversee 5-8 stores and sign vendor contracts for exterior maintenance;
    # $800-$2,500/location (large parking lot + building exterior + display pad); 2x/year;
    # 10-store district = $16K-$50K/year; zero competitors cold-calling Best Buy district managers;
    # Micro Center = single large-format store = owner/GM contact; first pull June 8 Cuyahoga (added 2026-06-01 run 164)
    'electronics retail district manager', 'electronics store district manager', 'best buy manager',
    'consumer electronics manager', 'electronics retail manager', 'big box electronics manager',
    'electronics district manager', 'consumer electronics district manager',
    # Rent-to-Own / Consumer Lease Chains — Rent-A-Center (25+ NE Ohio locations), Aaron's Holdings/Aarons (15+ NE Ohio),
    # FlexShopper (online but NE Ohio storefronts), Rainbow Rent (local NE Ohio chain);
    # COMPLETELY DISTINCT from pawn shops (run 163 — buy/sell model) and dollar stores (run 136 — outright purchase);
    # rent-to-own stores have VERY HIGH daily foot traffic (weekly payment collection days = 2-3x traffic spike);
    # Apollo tags 'rent to own', 'rent-to-own', 'consumer lease', 'furniture rental', 'appliance rental',
    # 'aarons', 'rent-a-center', 'rentacenter' — zero overlap with existing DANNY_ORG_KEYWORDS;
    # heavy foot traffic + vehicle traffic in/out = chronically stained entry concrete + parking lot aprons;
    # state consumer rental licensing = licensed retail facility exterior appearance standard;
    # district managers oversee 5-12 locations and sign multi-location vendor contracts;
    # $300-$700/location (parking lot + entry concrete + building exterior); 2x/year = $600-$1,400/location;
    # 10-location district deal = $6K-$14K/year; zero competitors cold-calling rent-to-own district managers;
    # NE Ohio has highest rent-to-own density in OH due to working-class suburban demographic base;
    # first pull June 8 Cuyahoga (Rent-A-Center + Aaron's Cuyahoga County district) (added 2026-06-01 run 164)
    'rent to own manager', 'rent-to-own manager', 'rent to own district manager',
    'consumer lease manager', 'furniture rental manager', 'appliance rental manager',
    'aarons store manager', 'rentacenter manager', 'rent to own district director',
    # Insurance Agency Offices — State Farm (80+ NE Ohio agency offices), Allstate (60+ NE Ohio),
    # Erie Insurance (50+ NE Ohio), Nationwide (40+ NE Ohio), Farmers (30+ NE Ohio), AAA Insurance;
    # COMPLETELY DISTINCT from banks/credit unions (run 100 — financial institution buildings) and
    # corporate parks (run 101 — office complexes); insurance agencies are INDIVIDUALLY-OWNED
    # franchise storefronts — strip mall + standalone offices where the AGENT owner is the vendor
    # decision-maker, not a corporate FM; client-facing exterior = trust standard (people visit with
    # major life decisions — home, car, life insurance); state DOI licensing = appearance standard;
    # Apollo org tags: 'insurance agency', 'independent insurance', 'state farm', 'allstate',
    # 'erie insurance', 'nationwide insurance', 'farmers insurance' — zero overlap with any existing
    # DANNY_ORG_KEYWORDS; NE Ohio has 500+ active insurance agency offices across 7 counties;
    # agency owners sign vendor contracts directly as independent franchise operators;
    # $200-$600/visit; 2x/year = $400-$1,200/office; one regional district FM = 15+ offices =
    # $6K-$18K/year; zero competitors cold-calling insurance agency owners about exterior cleaning;
    # first pull June 8 Cuyahoga (State Farm/Allstate/Erie offices in Strongsville, Parma, Westlake,
    # Solon, Beachwood, Mentor corridor) (added 2026-06-01 run 165)
    'insurance agency owner', 'insurance agency manager', 'insurance district manager',
    'insurance office manager', 'independent insurance agent', 'insurance franchise owner',
    'state farm agent', 'allstate agent', 'erie insurance agent', 'insurance agency director',
    # Orthopedic & Sports Medicine Clinics — OrthoNEOA (25+ NE Ohio locations, Ohio's largest ortho group),
    # Cleveland Orthopedic & Spine, UH Orthopaedics outpatient offices, Premier Orthopedics,
    # Ohio Orthopedic Associates, Beacon Orthopaedics; DISTINCT from PT chains (run 126 — rehabilitation
    # post-op recovery), urgent care (run 114 — walk-in), diagnostic imaging (run 159 — radiology);
    # pre/post-op surgical patients + large family-member waiting groups = heavy parking lot demand;
    # Ohio Medical Board + Joint Commission accreditation = exterior appearance standard;
    # practice managers sign vendor contracts for entire clinic group; $600-$1,800/visit; 2x/year;
    # OrthoNEOA multi-location deal = $18K-$54K/year; zero competitors cold-calling ortho PMs (added 2026-06-01 run 166)
    'orthopedic practice manager', 'sports medicine manager', 'orthopedic clinic manager',
    'orthopedic surgery center manager', 'sports medicine director', 'orthopedic center manager',
    'sports medicine clinic manager', 'orthopedic group manager',
    # Financial Advisory & Wealth Management Offices — Edward Jones (60+ NE Ohio branch offices),
    # Raymond James (30+ NE Ohio), Ameriprise Financial (40+ NE Ohio), Northwestern Mutual (20+ NE Ohio),
    # Merrill Lynch/BofA advisory offices; DISTINCT from insurance agencies (run 165 — insurance product
    # sales, different Apollo org tags) and bank branches (run 100 — depository institution buildings);
    # clients visit for retirement planning + estate discussions = highest-stakes visits = pristine
    # client-facing appearance is non-negotiable; individual advisors own/lease office space and sign
    # vendor contracts independently (no corporate FM); Ohio Div. of Securities licensing = appearance standard;
    # $200-$600/visit; 2x/year; Edward Jones 5-office territory = $2K-$6K/year; zero competitors (added 2026-06-01 run 166)
    'financial advisor owner', 'wealth management director', 'financial planning manager',
    'investment advisor manager', 'financial services office manager', 'wealth advisor owner',
    'financial district manager', 'investment office manager',
    # Waste Hauling & Dumpster Rental Companies — Republic Services (NE Ohio's largest hauler: Strongsville district
    # HQ), Rumpke Waste Services (NE Ohio regional), Kimble Companies (Navarre OH HQ — largest independent waste
    # hauler in Ohio; 15+ NE Ohio transfer stations + service yards), GFL Environmental/Advanced Disposal (NE Ohio
    # districts), Waste Management Inc. (WM) NE Ohio district offices;
    # COMPLETELY DISTINCT from all existing segments — waste hauling companies have ENORMOUS fenced staging yards
    # where 200-500 commercial dumpsters sit on concrete pads accumulating leachate, rot, hydraulic fluid, road grime;
    # haul yard aprons + vehicle maintenance bays + dispatch office building exteriors = extreme staining;
    # OEPA NPDES stormwater permit + EPA SPCC plan require yard owners to prevent runoff from contaminated surfaces —
    # pressure washing the yard is a COMPLIANCE REQUIREMENT, not just aesthetics; district managers oversee 3-10
    # service yards and sign vendor contracts; $2,000-$8,000/yard visit; 4x/year = $8K-$32K/yard;
    # one Republic Services NE Ohio district = $40K-$160K/year; zero power washing competitors targeting this segment
    # (added 2026-06-01 run 167)
    'waste hauler manager', 'waste management district manager', 'dumpster rental manager',
    'waste collection district manager', 'solid waste manager', 'residential waste manager',
    'commercial waste manager', 'waste operations manager',
    # Dermatology & Skin Care Medical Groups — SkinCure Oncology (Cleveland HQ, 15+ NE Ohio outpatient
    # dermatology/Mohs surgery sites — one of the fastest-growing US dermatology chains), Cleveland Dermatology
    # Associates, Mahler Dermatology, Bahl & Bahl Dermatology (Brecksville/Westlake), Advanced Dermatology &
    # Cosmetic Surgery (national chain, 3 NE Ohio locations), Dermatology Associates of Cleveland,
    # U.S. Dermatology Partners NE Ohio, NorthShore Dermatology;
    # COMPLETELY DISTINCT from run 166 (orthopedic), run 114 (urgent care), run 101 (general medical offices),
    # run 162 (med spas/aesthetic clinics — cosmetic, not clinical); Apollo org tags 'dermatology clinic',
    # 'dermatology practice', 'skin care clinic' return ZERO overlap with any existing DANNY_ORG_KEYWORDS;
    # Ohio State Medical Board + Joint Commission accreditation (clinical Mohs/surgery practices) = exterior
    # appearance standard; high patient volume (dermatology is 3rd highest-volume medical specialty — patients
    # visit 2-4x/year); practice managers sign vendor contracts; $600-$1,800/clinic; 2x/year;
    # SkinCure Oncology 10-clinic NE Ohio group deal = $12K-$36K/year; zero competitors; first pull June 8 Cuyahoga
    # (added 2026-06-01 run 167)
    'dermatology practice manager', 'dermatology clinic manager', 'dermatology group administrator',
    'skin care clinic manager', 'dermatology office manager', 'dermatology district manager',
    'dermatology center director', 'dermatology regional manager',
    # Hospice & Palliative Care Facilities — Hospice of the Western Reserve (Westlake OH HQ, largest
    # non-profit hospice in NE Ohio; 5 inpatient residential facilities: Cleveland/Akron/Sandusky/Warren/Youngstown
    # regions; served 5,000+ patients in 2024), Amedisys Hospice (multiple NE Ohio office locations),
    # VITAS Healthcare (NE Ohio district office), Ohio's Hospice (merged system with NE Ohio coverage),
    # CrossCountry Hospice, Constellation Hospice, Midwest Hospice Care;
    # COMPLETELY DISTINCT from run 163 (home care agencies — non-medical personal care visits to patients' homes),
    # run 96 (senior/assisted living — residential facilities), run 150 (behavioral health clinics);
    # Apollo org tags 'hospice care', 'palliative care', 'inpatient hospice' return ZERO overlap with any
    # existing DANNY_ORG_KEYWORDS or existing medical segments;
    # Ohio DOH hospice program licensing + CMS Conditions of Participation = exterior cleanliness standard;
    # families arriving for final visits need a pristine, dignified facility exterior — appearance is a
    # mission-critical quality signal at the most emotionally charged moment of a family's life;
    # administrators (licensed hospice administrator = Ohio requirement) sign vendor contracts;
    # inpatient residential facilities: large parking lots + garden areas + building exteriors;
    # $800-$2,500/facility; 2x/year; Hospice of Western Reserve 5-facility NE Ohio portfolio = $8K-$25K/year;
    # zero NE Ohio power washing competitors targeting hospice facility administrators (added 2026-06-01 run 167)
    'hospice administrator', 'hospice director', 'hospice facility manager', 'palliative care director',
    'hospice operations director', 'hospice regional director', 'inpatient hospice manager',
    'hospice center director',
    # Community Colleges & Technical Institutes — Cuyahoga Community College (Unified/Western/Eastern/Metro
    # campuses), Lakeland Community College (Kirtland), Lorain County CC (Elyria), Stark State College (Canton),
    # Sinclair CC NE Ohio, Ohio State ATI; DISTINCT from K-12 vocational/CTE centers (run 157 — 'career technical',
    # 'vocational school' Apollo tags) and main universities (not yet targeted);
    # summer = academic maintenance window (buildings empty June-August = peak exterior cleaning access);
    # campus facilities director signs contracts for MULTIPLE buildings in a single deal;
    # large paved parking lots (hundreds of spaces) + building exteriors + covered walkways + amphitheater plazas;
    # $8K-$25K per campus; multi-campus system deal = $40K-$80K/year; zero competitors targeting college FM contacts;
    # first pull June 8 Cuyahoga (Tri-C Metro + Western + Eastern campuses all in Cuyahoga County) (added 2026-06-01 run 168)
    'community college facilities director', 'community college facilities manager',
    'college campus facilities director', 'higher education facilities director',
    'campus facilities director', 'community college maintenance director',
    'college grounds director', 'technical college facilities manager',
    # Medical Equipment & Device Manufacturers — Invacare Corporation (Elyria HQ — home medical equipment),
    # Steris Corporation (Mentor HQ — global sterilization + infection prevention), Nordson Corporation (Westlake HQ),
    # Swagelok Company (Solon — fluid system components), Materion Corporation (Mayfield Heights — medical alloys),
    # Natus Medical (Middleburg Heights), Mentice AB US office; LARGEST NE OHIO EMPLOYER SEGMENT NOT YET TARGETED;
    # DISTINCT from distribution centers (run 105 — logistics/fulfillment), medical offices (run 101 — patient-facing),
    # manufacturing (run 118 — general industrial, different Apollo org tags);
    # FDA GMP 21 CFR Part 820 Quality System Regulation = exterior facility cleanliness standard for all
    # FDA-registered device manufacturers; ISO 13485 certification audits check facility exterior appearance;
    # loading docks + manufacturing building exteriors + parking + shipping/receiving bays;
    # $3K-$12K/facility; 4x/year = $12K-$48K/year per large facility; Invacare + Steris alone = $50K+/year potential;
    # zero competitors targeting medical device plant operations managers in NE Ohio (added 2026-06-01 run 168)
    'medical device operations manager', 'medical equipment operations manager',
    'medical device facility manager', 'medical manufacturing manager',
    'medical equipment plant manager', 'medical device plant operations manager',
    'biomedical equipment manager', 'medical device manufacturing director',
    # Pain Management & Spine Clinics — Cleveland Clinic Pain Management (multiple NE Ohio sites),
    # University Hospitals Pain Clinic, Summa Health Pain Management, National Spine & Pain Centers NE Ohio,
    # OhioHealth Pain Centers, Greater Cleveland Urology (Pain division), Interventional Pain Solutions;
    # COMPLETELY DISTINCT from orthopedic (run 166 — surgical, 'orthopedic clinic' Apollo tag),
    # chiropractic (run 152 — non-MD, 'chiropractic' Apollo tag), PT chains (run 126 — 'physical therapy' Apollo tag),
    # urgent care (run 114 — acute episodic), behavioral health (run 150 — mental health focus);
    # pain management = MD/DO interventional procedures (injections, nerve blocks, ablation);
    # Ohio Medical Board + DEA registration = stringent facility licensing; inspection checks exterior appearance;
    # CHRONIC patients visit weekly or bi-weekly = highest visit frequency of any specialty clinic segment;
    # heavy recurring foot traffic = parking lot + entry concrete heavily stained; state licensing urgency angle;
    # $800-$2,500/clinic; 2x/year = $1,600-$5,000; 10-clinic network = $16K-$50K/year; zero competitors;
    # first pull June 8 Cuyahoga (Cleveland Clinic Pain Mgmt Beachwood + UH Pain Clinic Westlake) (added 2026-06-01 run 168)
    'pain management clinic manager', 'pain management practice manager',
    'pain clinic director', 'pain management director',
    'pain center manager', 'interventional pain manager',
    'pain management administrator', 'pain medicine practice manager',
    # Skilled Nursing Facilities & Long-Term Care Centers — ProMedica Senior Care (15+ NE Ohio SNF facilities),
    # Genesis Healthcare NE Ohio, Consulate Health Care, HCR ManorCare Heritage Park, Altercare of Ohio;
    # DISTINCT from senior/assisted living (run 96 — 'assisted living', 'memory care' Apollo tags),
    # hospice (run 167 — 'hospice care' Apollo tag), adult day care (run 159 — 'adult day' Apollo tag);
    # CMS Five-Star Quality Rating System: exterior appearance affects star rating = affects Medicare/Medicaid census =
    # affects revenue; state ODH nursing home licensing = exterior inspection checks;
    # administrator signs vendor contracts for entire facility; one ProMedica SNF regional ops contact = 15 facilities;
    # $4K-$12K/facility per year; ProMedica NE Ohio portfolio = $60K-$180K/year; zero competitors cold-calling SNFs;
    # first pull June 8 Cuyahoga (ProMedica Senior Care Parma/Strongsville/Westlake SNFs) (added 2026-06-01 run 169)
    'skilled nursing facility administrator', 'nursing home administrator',
    'long-term care administrator', 'director of nursing home operations',
    'snf administrator', 'nursing facility director',
    'post-acute care director', 'skilled nursing regional director',
    # Orthodontic Practices & Pediatric Dental Groups — Smile Doctors NE Ohio (acquired/affiliated multiple practices),
    # Ortho Studios Ohio franchise, OrthoSynetics-managed practices, Orthodontic Associates of Ohio,
    # Kids First Dental (multi-location), Great Lakes Pediatric Dental, Pediatric Dentistry at Beachwood;
    # DISTINCT from general DSO chains (run 123 — 'dental group', 'dental service organization' Apollo tags);
    # orthodontic patients visit every 4-6 weeks for adjustments = HIGHEST dental visit frequency = maximum staining;
    # pediatric patients arrive WITH parents = 2 vehicles per appointment = elevated parking lot demand;
    # Ohio State Dental Board + AAO accreditation = exterior appearance standard; practice managers sign contracts;
    # 10-location Smile Doctors/Ortho Studios territory deal = $6K-$15K/year; zero competitors;
    # first pull June 8 Cuyahoga (Smile Doctors Beachwood + Ortho Studios Strongsville) (added 2026-06-01 run 169)
    'orthodontic practice manager', 'orthodontist office manager',
    'orthodontic district manager', 'pediatric dental practice manager',
    'orthodontic group director', 'orthodontic operations director',
    'pediatric dental district manager', 'orthodontic regional manager',
    # County Fairgrounds & Agricultural Exhibition Facilities — Cuyahoga County Fair (Berea),
    # Summit County Fair (Tallmadge), Medina County Fair (Medina), Lake County Fair (Painesville Twp),
    # Lorain County Fair (Wellington), Geauga County Fair (Burton — Ohio's oldest), Portage County Fair (Ravenna);
    # 7 county fairgrounds in the 7-county service area = perfect geographic alignment;
    # Ohio Dept of Agriculture / county fair board licensing = facility appearance inspection standard;
    # June/July pre-fair pressure washing of concrete livestock pavilions + midway areas + parking lots;
    # facilities directors/superintendents sign vendor contracts; $3,000-$8,000/visit; 2x/year (spring prep + post-fair);
    # DISTINCT from convention centers (run 128 — I-X Center, Cleveland Convention Center) which are year-round;
    # county fairgrounds are seasonal agricultural venues with distinct Apollo org tags;
    # zero competitors cold-calling county fair facilities directors (added 2026-06-01 run 170)
    'fairgrounds manager', 'county fair director', 'exhibition grounds manager',
    'fairgrounds facilities manager', 'county fairgrounds director', 'fair operations manager',
    'agricultural fair manager', 'fair facility director', 'fair superintendent',
    # Title Companies & Real Estate Closing Offices — Stewart Title (Cleveland HQ), Chicago Title Insurance,
    # First American Title, Fidelity National Title, Ohio Title Agency, Buckeye Title Agency,
    # Western Reserve Title, HomePoint Title, WFG National Title, Old Republic Title, plus 100+ independent
    # closing attorney offices across Cuyahoga/Lake/Lorain/Summit/Medina/Geauga/Portage;
    # client-facing offices where NE Ohio homebuyers close the largest transaction of their lives;
    # curb appeal = direct trust signal; June = peak real estate closing season = peak pitch window;
    # DISTINCT from realtors (Carla's referral territory) and financial advisors (run 166);
    # 200+ NE Ohio title company offices across 7 counties; office managers sign vendor contracts;
    # $600-$1,500/office; 2x/year; multi-office territory deal = $12K-$30K/year;
    # zero competitors cold-calling title company office managers (added 2026-06-01 run 170)
    'title company manager', 'title office manager', 'title branch manager',
    'settlement agent manager', 'closing attorney office manager', 'title company branch manager',
    'real estate closing manager', 'title services manager', 'title operations manager',
    # Fire Stations & Fire Departments — 150+ municipal fire stations across 7-county NE Ohio service area
    # (Cleveland, Parma, Lakewood, Strongsville, Mentor, Lorain, Elyria, Akron, Medina, Brunswick townships);
    # apparatus bay concrete aprons + exterior building facades + equipment training pads + parking lots =
    # recurring pressure wash need; summer (June-August) = annual exterior maintenance window for municipalities;
    # ISO 2 Public Protection Classification: station condition/maintenance affects community fire insurance ratings;
    # fire chief or city FM signs vendor contracts; small contracts routinely direct-awarded <$25K without competitive bid;
    # DISTINCT from municipal/government segment (run 124 — city halls + admin buildings) — fire stations have
    # dedicated fire district budgets, separate from city general facilities, and are Apollo-tagged under 'fire department';
    # $800-$2,500/station; 2x/year; one township FD (5 stations) = $8K-$25K/year; zero competitors (added 2026-06-01 run 171)
    'fire station manager', 'fire department director', 'fire chief', 'fire rescue director',
    'fire station director', 'fire district manager', 'fire station facilities manager',
    'fire department facilities coordinator',
    # Home Builders & Residential Real Estate Developers — M/I Homes NE Ohio, Pulte/Del Webb (Cuyahoga/Summit),
    # K. Hovnanian Homes (Greater Cleveland), Maronda Homes NE Ohio, Fischer Homes, Integrity Homes NE Ohio,
    # DiVosta, Epcon Communities, Smith Homes, Independence Landing; model homes pressure-washed before EVERY
    # showing/open house; community entrance monuments, welcome sign structures, model home sidewalks + facades;
    # sales center exteriors = buyer's first impression when signing the largest check of their life;
    # June = PEAK NE Ohio new home showing season — construction debris on walks + staining from equipment;
    # DISTINCT from realtors (existing homes, Carla's territory) and title companies (run 170 — closing offices);
    # Apollo org tags 'home builder', 'residential developer', 'new home construction' return zero overlap with existing;
    # $300-$800/model home wash; $500-$1,500/community entrance; one active development = $1,200-$4,000/year;
    # zero competitors cold-calling home builder construction/sales managers for pressure washing (added 2026-06-01 run 171)
    'home builder manager', 'residential construction manager', 'new home sales manager',
    'community sales manager', 'home development manager', 'residential developer manager',
    'new home community manager', 'model home manager',
    # Propane & Fuel Oil Delivery Companies — AmeriGas (largest US propane supplier, multiple NE Ohio service centers),
    # Ferrellgas (NE Ohio operations), Suburban Propane NE Ohio, Energy One/National Fuel Gas (Akron HQ),
    # Ohio Valley Gas, Superior Plus Energy, Westmore Fuel, local independent heating oil dealers;
    # fuel storage yards: large concrete pads with persistent oil/fuel staining + propane cylinder staging areas +
    # vehicle maintenance bays; OSHA SPCC (Spill Prevention Control & Countermeasure) + EPA Tier II hazmat compliance;
    # oil/fuel staining = EPA violation risk + slip hazard = recurring regulatory pressure to stay clean;
    # DISTINCT from gas stations (retail consumer-facing) — these are WHOLESALE/commercial delivery operations;
    # Apollo tags 'propane delivery', 'fuel oil delivery', 'heating oil' return zero overlap with gas station keywords;
    # $800-$2,500/facility; 2x/year; AmeriGas district (3-5 NE Ohio service centers) = $5K-$25K/year;
    # zero competitors cold-calling propane/fuel oil operations managers for power washing (added 2026-06-01 run 171)
    'propane district manager', 'fuel oil manager', 'propane operations manager',
    'fuel delivery manager', 'propane service manager', 'heating oil manager',
    'energy delivery manager', 'fuel distribution manager',
    # Dance Studios & Performing Arts Schools — Arthur Murray Dance Studios (10+ NE Ohio franchise locations),
    # Fred Astaire Dance Studios (Akron/Strongsville/Beachwood area), Center Stage Dance, NovaDance Academy,
    # Ballet Western Reserve, Broadway Dance School, regional competition studio chains;
    # spring recital season May-June = peak parent/student visibility RIGHT NOW — 100-400 students per studio;
    # entry walkways, lobby exteriors, parking lots = recurring scuff marks, algae, gum, staining;
    # studio owners or franchise operators sign vendor contracts directly (no procurement layer);
    # DISTINCT from fitness centers (gym/workout focus), martial arts (below), sports complexes (run 125);
    # Apollo tags 'dance studio', 'performing arts school', 'dance academy' = zero overlap with existing org keywords;
    # $400-$1,200/studio; 2x/year; Arthur Murray 5-location NE Ohio franchise = $4K-$12K/year;
    # zero competitors cold-calling dance studio owners for power washing (added 2026-06-01 run 172)
    'dance studio owner', 'dance studio manager', 'dance studio director', 'performing arts director',
    'dance academy director', 'dance school director', 'dance studio franchise owner',
    'performing arts school manager',
    # Martial Arts Academies & Combat Sports Studios — ATA Martial Arts (national franchise, 8+ NE Ohio),
    # Tiger Rock Martial Arts, Century Martial Arts, World Tang Soo Do Association (multiple NE Ohio dojos),
    # Carlson Gracie BJJ (Westlake), Gracie Barra (multiple NE Ohio), Krav Maga (Strongsville, Mentor);
    # DISTINCT from sports complexes (run 125 — 'sports complex' org tag; martial arts mentioned but not specifically pulled);
    # summer kids' karate camps = RIGHT NOW (June-August) = peak traffic + maximum entry/lot staining;
    # studio owners (sole proprietors) or franchise operators sign vendor contracts directly = fastest close;
    # Apollo tags 'martial arts', 'karate', 'taekwondo', 'jiu-jitsu', 'bjj gym' = zero overlap with existing;
    # $400-$1,200/studio; 2x/year; ATA 3-location NE Ohio district franchise = $2.4K-$7.2K/year;
    # zero competitors cold-calling martial arts school owners for power washing (added 2026-06-01 run 172)
    'martial arts school owner', 'karate school owner', 'martial arts academy director',
    'dojo owner', 'martial arts instructor', 'karate instructor', 'taekwondo instructor',
    'bjj gym owner', 'jiu-jitsu academy owner', 'krav maga instructor',
    # Wedding Venues & Special Occasion Facilities — 'wedding venue' in DANNY_ORG_KEYWORDS (run 108) catches
    # general venues, but 'wedding coordinator'/'venue coordinator' titles were never in DANNY_TITLES;
    # Apollo returns coordinator-level contacts at dedicated wedding venues but their title didn't match;
    # June = peak booking month — couples visiting venues for July/Aug/Sept weddings RIGHT NOW;
    # NE Ohio targets: Barn at Mapleside Farms (Brunswick), Willow Tree Ranch (Chardon), Posh on Park (Akron),
    # Spencer's Restaurant & Inn (Aurora), Gervasi Vineyard (Canton area), Hale Farm & Village (Bath);
    # outdoor ceremony areas + parking + cobblestone paths + building facades = critical for wedding photos;
    # $2,000–$5,000/visit; 2x/year; 25-venue NE Ohio territory = $100K–$250K/year potential;
    # zero competitors targeting wedding venue coordinators for power washing (added 2026-06-02 run 173)
    'wedding coordinator', 'venue coordinator', 'wedding venue coordinator', 'bridal venue manager',
    'wedding venue owner', 'wedding estate manager', 'bridal hall manager', 'event coordinator',
    # Outdoor Recreation & Adventure Parks — mini-golf, go-karts, batting cages, axe throwing venues;
    # June = school's out = PEAK family activity season RIGHT NOW;
    # NE Ohio: All-American Fun Park (Chardon), Berea Golf Dome, Zone Sports (multiple), Adventure Zone Avon;
    # large paved lots + walkways + building facades + equipment areas accumulate staining in peak traffic;
    # owners / franchise operators sign vendor contracts directly = fastest close, no procurement layer;
    # DISTINCT from trampoline parks/indoor adventure centers (run 148 — indoor); these are OUTDOOR facilities;
    # 'outdoor recreation manager' already in DANNY_TITLES (run 158, campground) — adding venue-specific titles;
    # Apollo 'mini golf', 'go-kart', 'batting cage', 'axe throwing' tags = zero overlap with existing segments;
    # $600–$1,800/visit; 2x/year; zero competitors cold-calling outdoor rec park managers (added 2026-06-02 run 173)
    'mini golf manager', 'miniature golf manager', 'go-kart park manager', 'go kart park owner',
    'batting cage manager', 'axe throwing venue manager', 'outdoor recreation park owner',
    'family fun park manager', 'outdoor entertainment park manager',
    # Charter Fishing & Lake Erie Boat Tour Operators — 50+ independent charter operators along Lake Erie shoreline
    # (Lorain, Huron, Mentor Headlands, Westlake, Vermilion, Sandusky Bay corridor);
    # June-August = PEAK walleye + perch charter season RIGHT NOW — dock areas, concrete launch ramps,
    # parking lots, bait station pads; owner-operators sign vendor contracts directly = fastest close;
    # DISTINCT from marinas (run 109 — marina management companies); these are INDEPENDENT charter captains;
    # Apollo tags 'charter fishing', 'fishing charter', 'lake erie charter' = zero overlap with existing;
    # $400-$1,200/dock area; 2x/year; 15-charter NE Ohio territory = $12K-$36K/year;
    # pitch: "Season is heating up — let us pressure wash your dock and launch pad before July 4th weekend." (added 2026-06-02 run 174)
    'charter boat captain', 'fishing charter owner', 'charter fishing owner', 'boat charter owner',
    'lake charter captain', 'charter boat operator', 'fishing guide owner', 'charter captain',
    # VFW Posts & American Legion Halls — 90+ VFW posts + 60+ American Legion posts = 150+ NE Ohio facilities;
    # Memorial Day just passed = facilities heavily used for events + annual ceremonies;
    # large parking lots + brick/concrete building exteriors + banquet hall wings;
    # post commanders sign vendor contracts directly; small-purchase authority under $5K = direct award;
    # government/veteran-preference angle: "We support veteran-owned and served venues with priority scheduling";
    # DISTINCT from government/municipal facilities (run 124 — city halls, county admin buildings);
    # Apollo tags 'vfw post', 'american legion', 'veterans of foreign wars' = zero overlap with existing;
    # $600-$1,500/post; 2x/year; NE Ohio full territory = $90K-$225K/year potential;
    # zero competitors cold-calling VFW/Legion post commanders for power washing (added 2026-06-02 run 174)
    'vfw post commander', 'american legion commander', 'post commander', 'veterans post director',
    'veterans facility manager', 'post adjutant', 'vfw commander', 'legion post adjutant',
    # Law Firms & Legal Office Buildings — Jones Day (Cleveland HQ), Benesch Friedlander, Thompson Hine,
    # Hahn Loeser & Parks, Roetzel & Andress (Akron HQ), Squire Patton Boggs, McCarthy Lebit, Reminger;
    # downtown Cleveland office buildings + suburban satellite offices (Beachwood, Westlake, Independence);
    # client reception areas = professional trust signal; building facades + parking + entrance plazas;
    # law firm administrator or office manager signs vendor contracts; no procurement layer at mid-size firms;
    # DISTINCT from financial advisors (run 166 — small individual office) and corporate campuses (run 101 — tech parks);
    # Apollo tags 'law firm', 'legal services', 'attorneys at law' = zero overlap with existing segments;
    # $1,500-$5,000/building; 2x/year; 10-building downtown firm = $30K-$100K/year;
    # zero competitors cold-calling law firm facilities managers for power washing (added 2026-06-02 run 174)
    'law firm administrator', 'legal office manager', 'law office manager', 'legal administrator',
    'law firm facilities manager', 'legal facilities director', 'office services manager',
    'law firm operations manager',
    # Independent Dental Practices — solo/small-group dentist offices (DISTINCT from DSO chains, run 123);
    # 1,000+ independent NE Ohio dental practices; Ohio State Dental Board licensing = exterior appearance standard;
    # July-Aug = traditionally slower patient volume = dentist-owner available to discuss vendors;
    # dental office manager or dentist-owner signs vendor contracts directly; no procurement layer at independent practices;
    # Apollo tags 'dental office', 'dental practice', 'family dentistry' catch independents NOT in DSO orgs;
    # $600-$1,500/visit; 2x/year; 20-practice territory = $24K-$60K/year (added 2026-06-02 run 175)
    'dental office manager', 'dental practice manager', 'dental administrator',
    'dental office administrator', 'dental practice director', 'general dentistry manager',
    'dental clinic administrator', 'dental office director',
    # Accounting & CPA Firms — 500+ NE Ohio CPA practices; HW&Co, Maloney+Novotny, SS&G Financial,
    # Bober Markey Fedorovich, Corrigan Krause, Rea & Associates (regional NE Ohio CPA firms);
    # post-tax-season June-July = partners/administrators available to evaluate vendors;
    # client-facing professional offices = exterior appearance as important as law firms (run 145);
    # DISTINCT from financial advisors (run 166 — investment/wealth) and banks (run 100 — branch FM);
    # Apollo tags 'cpa firm', 'accounting firm', 'public accounting' return zero overlap with existing segments;
    # $800-$2,500/building; 2x/year; 10-office regional CPA firm = $16K-$50K/year (added 2026-06-02 run 175)
    'cpa firm manager', 'accounting firm administrator', 'accounting practice manager',
    'cpa office administrator', 'accounting firm director', 'public accounting manager',
    'cpa managing partner', 'audit firm manager',
    # Flooring & Tile Showrooms & Retailers — Floor & Decor (Independence, Mentor, North Canton NE Ohio),
    # Classic Hardwood Floors Cleveland, City Tile Cleveland, Color Tile & Carpet, Shaw Floors dealers, Mohawk dealers;
    # large parking lots + building exteriors + delivery truck staging areas accumulate staining from material deliveries;
    # ironic pitch: "We clean outside so customers can focus on your beautiful floors inside";
    # DISTINCT from home improvement/hardware (run 136 — Home Depot/Lowe's) and lumber yards (run 150);
    # Apollo tags 'flooring', 'tile store', 'floor store' return zero overlap with existing segments;
    # $600-$2,000/visit; 2x/year; Floor & Decor district deal (3-5 NE Ohio stores) = $3.6K-$20K/year (added 2026-06-02 run 175)
    'flooring showroom manager', 'flooring store manager', 'flooring district manager',
    'tile showroom manager', 'carpet store manager', 'flooring operations manager',
    'flooring franchise owner', 'flooring store director',
    # Summer Day Camps & Youth Day Programs — schools out first week of June in NE Ohio;
    # day camps opening RIGHT NOW; DISTINCT from YMCA (run 131 — fitness, 'ymca' Apollo tag),
    # campgrounds (run 158 — overnight, 'campground'/'rv park' tags), sports complexes (run 125 — athletic);
    # Ohio DJFS child care licensing = exterior appearance inspection standard;
    # director or owner signs vendor contracts directly; facilities: paved parking lots + building
    # exteriors + outdoor activity area concrete; Boys & Girls Club NE Ohio (20+ Cuyahoga County locations);
    # Camp Ho Mita Koda (Painesville), Camp Cheerful (Strongsville), Kelleys Island Day Camp;
    # $400-$1,200/facility; 2x/year (spring pre-opening + fall close); first pull June 8 Cuyahoga (added 2026-06-02 run 176)
    'day camp director', 'summer camp director', 'youth program director', 'youth day camp director',
    'summer youth director', 'camp director', 'day camp manager', 'youth summer program manager',
    # B2B Wholesale Supply Houses (Plumbing, HVAC, Electrical) — branch managers sign vendor contracts;
    # large loading docks + parts lots + vehicle staging areas; constant truck traffic = oil/diesel staining;
    # DISTINCT from distribution centers (run 105), manufacturing (run 118), hardware stores (run 136);
    # Ferguson Enterprises (Strongsville/Euclid/Brooklyn Heights/Akron), Hajoca Corp (Cleveland/Akron),
    # Winsupply (multi-location franchise NE Ohio), Graybar Electric (Independence/Akron),
    # Rexel USA (Valley View/Mentor), McNaughton-McKay Electric (Twinsburg/Elyria);
    # $600–$2,000/visit; 4x/year; Ferguson 4-branch territory = $9.6K–$32K/year; zero competitors;
    # first pull June 8 Cuyahoga (added 2026-06-02 run 178)
    'plumbing supply branch manager', 'hvac supply branch manager', 'electrical supply branch manager',
    'plumbing wholesale manager', 'hvac wholesale manager', 'mechanical supply manager',
    'industrial supply branch manager', 'supply house manager', 'wholesale distribution manager',
    # School Bus Companies & Charter Motor Coach Operators — large bus depot lots accumulate diesel exhaust
    # + hydraulic fluid + road salt + tire marks; DISTINCT from school districts (run 119 — facilities/
    # buildings directors) and public transit (run 124 — GCRTA municipal transit authority);
    # private contract carriers sign independent vendor contracts per depot or region;
    # First Student / National Express US (10+ NE Ohio school district contracts),
    # Durham School Services, Transdev North America, GO Transportation (Ohio charter bus);
    # $800–$3,000/bus depot visit; 4x/year; 3-depot territory = $9.6K–$36K/year; first pull June 8 Cuyahoga (added 2026-06-02 run 178)
    'school bus company manager', 'student transportation manager', 'bus fleet manager',
    'charter bus manager', 'motor coach manager', 'school bus operations manager',
    'bus transportation manager', 'student transport director',
    # USPS & Postal Service Facilities — NE Ohio Cleveland P&DC (9850 E 30th St) + Akron P&DC +
    # 100+ delivery unit offices; USPS FAC (Federal Acquisition Circular) contractor standards;
    # large loading docks + concrete mail-staging aprons + parking lots + vehicle bays accumulate
    # diesel exhaust + road grime + road salt every day; postmasters and facility managers sign
    # vendor contracts independently; COMPLETELY DISTINCT from municipal government (run 124 — city halls)
    # and distribution centers (run 105 — private logistics); $500–$2,000/facility; 2x/year (added 2026-06-02 run 179)
    'postmaster', 'postal facility manager', 'usps facility manager', 'postal station manager',
    'mail processing facility manager', 'postal district manager', 'postal operations supervisor',
    'postal service manager', 'post office manager', 'usps operations manager',
    # Construction & Industrial Equipment Rental Companies — United Rentals (10+ NE Ohio branches),
    # Sunbelt Rentals (7+ NE Ohio branches), H&E Equipment Services, BlueLine Rental,
    # HERC Rentals, RSC Equipment Rental, Nesco Resource, Ahern Rentals;
    # COMPLETELY DISTINCT from construction equipment DEALERS (run 143 — showrooms with new equipment);
    # rental branch lots have heavy equipment sitting outdoors 24/7 — excavators, boom lifts, skid steers,
    # concrete saws; hydraulic fluid + diesel + mud = extreme surface staining beyond any other segment;
    # OSHA SPCC stormwater compliance for hydraulic fluid and diesel storage is a regulatory angle;
    # branch managers sign vendor contracts independently (no corporate procurement);
    # $2,000–$6,000/branch; 4x/year = $8K–$24K/year per branch; zero competitors targeting this (added 2026-06-02 run 179)
    'equipment rental branch manager', 'equipment rental manager', 'rental equipment manager',
    'rental yard manager', 'equipment rental operations manager', 'rental branch general manager',
    'construction equipment rental manager', 'heavy equipment rental manager',
    # Public Housing Authorities & Affordable Housing Management — CMHA (Cuyahoga Metropolitan Housing Authority,
    # 5,600+ units), AMHA (Akron Metropolitan Housing Authority, 3,200+ units), Lake County CMHA,
    # Lorain Metropolitan Housing Authority, Medina County Housing Authority;
    # COMPLETELY DISTINCT from private property managers (those are for-profit PM firms);
    # government HUD-funded authorities operate direct-award vendor contracts without competitive bidding <$25K;
    # large paved parking lots + walkways + building facades + common area concrete across hundreds of properties;
    # maintenance directors sign vendor contracts; $800–$2,500/site; annual county-wide contract = $20K–$80K/year;
    # zero competitors cold-calling public housing maintenance directors in NE Ohio (added 2026-06-02 run 180)
    'housing authority maintenance director', 'housing authority facilities manager', 'public housing director',
    'housing development manager', 'housing authority property manager', 'affordable housing director',
    'public housing facilities manager', 'housing authority operations manager',
    # TV & Radio Broadcasting Stations & Media Facilities — WEWS Cleveland (ABC affiliate, Scripps Media),
    # WJW Fox 8 (iHeartMedia), WKYC (NBC affiliate, Tegna), WUAB (My Network TV, Nexstar),
    # iHeartMedia Cleveland (WTAM 1100, WMMS 100.7, WKRK 92.3, WENZ 107.9), Cumulus Media Cleveland;
    # transmitter buildings + satellite dish farms + parking areas + building facades;
    # COMPLETELY DISTINCT from corporate office parks — broadcasting facilities have unique outdoor structures;
    # station FMs or engineering directors sign vendor contracts; $1,500–$4,000/site; 2x/year;
    # brand image = on-camera outdoor shots for news promos = non-negotiable appearance standard;
    # zero competitors cold-calling broadcast facility managers in NE Ohio (added 2026-06-02 run 180)
    'broadcast facility manager', 'station operations manager', 'television station manager',
    'broadcast operations director', 'radio station manager', 'media facility director',
    'broadcast engineering manager', 'television facility manager',
    # Pharmaceutical Manufacturing & Research Facilities — STERIS Corporation (Mentor OH — Fortune 500,
    # largest sterile processing company globally), Ferro Corporation (Cleveland — specialty materials/pharma),
    # OhioHealth pharmaceutical research (Columbus but with NE Ohio outpatient research sites),
    # Summa Health / UH clinical research facilities, Noven Pharmaceuticals;
    # COMPLETELY DISTINCT from general manufacturing (run 118) and medical device (run 168);
    # FDA 21 CFR Part 211 (current Good Manufacturing Practice for finished pharmaceuticals) mandates
    # facility appearance and contamination control — exterior cleaning is a compliance line item;
    # plant FMs + EHS managers sign vendor contracts; $3,000–$12,000/visit; 4x/year;
    # STERIS Mentor campus alone is a $15K–$40K/year account; zero competitors targeting pharma FMs;
    # first pull June 8 Cuyahoga (STERIS Mentor corridor + Ferro Corporation HQ) (added 2026-06-02 run 180)
    'pharmaceutical plant manager', 'pharma facility manager', 'pharmaceutical operations manager',
    'drug manufacturing manager', 'pharmaceutical plant superintendent', 'biotech facility manager',
    'pharmaceutical manufacturing manager', 'pharmaceutical plant operations manager',
    # Scrap Metal Dealers & Metal Recycling Facilities — NE Ohio is a major scrap metals hub
    # (steel industry legacy); OmniSource/Steel Technologies (Cleveland), Sims Metal Management
    # (multiple NE Ohio yards), Metal Management (Cleveland), TriState Metals (Youngstown),
    # Reserve Iron & Metal (Cleveland), General Iron, Cohen Brothers Recycling (Cincinnati/NE Ohio);
    # large paved yards + truck staging areas + scale pads + loading bays accumulate extreme concrete
    # staining from metal dust, rust runoff, hydraulic fluid, diesel exhaust, and coolants;
    # EPA stormwater permit NPDES for metals runoff = power washing of concrete is a compliance
    # line item on every facility's stormwater pollution prevention plan (SWPPP);
    # COMPLETELY DISTINCT from towing/auto salvage ('salvage yard'/'junkyard' Apollo tags — run 113)
    # and manufacturing ('metal fabrication'/'steel manufacturer' Apollo tags — run 118);
    # scrap metal org tags ('scrap metal', 'metal recycling', 'ferrous metals') return zero overlap;
    # yard managers or operations directors sign vendor contracts directly; $2,000–$6,000/yard visit;
    # 4x/year; multi-yard regional operator contract = $32K–$96K/year; zero competitors targeting
    # scrap yard managers for power washing in NE Ohio (added 2026-06-02 run 181)
    'scrap yard manager', 'metal recycling manager', 'scrap metal operations manager',
    'recycling facility manager', 'scrap operations director', 'yard operations manager',
    'metal recycling director', 'scrap metal yard manager',
    # Data Centers & Colocation Facilities — Expedient Technology (Independence OH — largest NE Ohio
    # colocation provider), Zayo Group (Cleveland Points of Presence), Iron Mountain (Beachwood OH —
    # data center + records storage), OnX Enterprise Solutions (Cleveland HQ), Sungard Availability
    # Services, Cleveland Clinic enterprise data center (Beachwood), University Hospitals IT campus;
    # building exteriors + parking + loading dock areas require regular cleaning;
    # COMPLETELY DISTINCT from corporate park FMs (run 101 — general office park management) and
    # IT/tech companies (general corporate); 'data center'/'colocation facility' Apollo org tags
    # return zero overlap with any existing DANNY_ORG_KEYWORDS;
    # security-certified local vendors get exclusive long-term service contracts (no competitive bid
    # once security clearance is established); facility operations managers sign vendor contracts;
    # $2,000–$5,000/visit; 2x/year; data center campus = $8K–$20K/year anchor account;
    # zero power washing competitors cold-calling data center FMs in NE Ohio (added 2026-06-02 run 181)
    'data center manager', 'data center operations manager', 'colocation facility manager',
    'data center facilities manager', 'colo facility manager', 'infrastructure manager',
    'data center general manager', 'colocation operations manager',
    # Gymnastics Centers & Tumbling Academies — summer camps RIGHT NOW (June = peak enrollment);
    # Ohio DOH gymnastics facility registration = exterior appearance is a licensing inspection criterion;
    # COMPLETELY DISTINCT from dance studios (run 172 — ballet/jazz/performing arts Apollo tags),
    # sports complexes (run 125 — multi-sport team sports), trampoline parks (run 148 — foam pit/indoor);
    # 100+ NE Ohio gymnastics centers; USA Gymnastics affiliated gyms + ATA Cheerleading affiliates;
    # owner-operators sign vendor contracts directly with zero corporate procurement = fastest-close accounts;
    # June = end-of-year showcase season + summer camp enrollment = maximum parent/student traffic = peak staining;
    # parking lots + entrance walkways + lobby areas get maximum concrete traffic this exact month;
    # $400–$1,200/visit; 2x/year; All American Gymnastics (Mentor), Champion's Edge (Beachwood),
    # Gymnastics Zone (Avon/North Olmsted), World Class Gymnastics (Akron), Extreme Gymnastics (Cleveland),
    # Ohio Twisters Gymnastics (Strongsville), Power Gymnastics Academy; zero competitors (added 2026-06-02 run 182)
    'gymnastics center director', 'gymnastics gym owner', 'tumbling academy director',
    'gymnastics academy director', 'cheerleading gym owner', 'cheer gym director',
    'gymnastics studio manager', 'cheer academy owner',
    # Beverage Distribution Centers & Soft Drink Bottlers — Coca-Cola Consolidated (Strongsville HQ),
    # Pepsi Beverages Company (Bedford Heights distribution depot), 7UP/Dr. Pepper (Cleveland distribution),
    # Great Lakes Distributing (craft beer/beverage distributor Mentor), Southern Glazer's Wine & Spirits
    # (Twinsburg regional distribution center), Anheuser-Busch NE Ohio wholesaler depots;
    # loading dock concrete accumulates extreme staining: sugar spills (sticky residue), CO2 condensation,
    # yeast/hop residue from beer leakage, syrup drips from fountain syrup deliveries, and diesel exhaust
    # from constant refrigerated truck staging — worst concrete staining type outside scrap yards;
    # FDA FSMA (Food Safety Modernization Act) requires food loading dock areas be maintained to prevent
    # contamination = power washing of loading concrete is a regulatory line item, not discretionary;
    # COMPLETELY DISTINCT from general distribution centers (run 105 — 'fulfillment center'/'distribution center'
    # Apollo tags) and food processing plants (run 127 — production plants, not distribution depots);
    # Apollo org tags 'beverage distribution'/'soft drink distributor'/'beer distributor' return zero overlap
    # with run 105 'fulfillment center'/'logistics facility' tags (different Apollo taxonomy);
    # branch/depot managers sign vendor contracts directly; $800–$3,000/loading dock area;
    # Coca-Cola Strongsville 4-dock facility = $4,000–$8,000/year; Pepsi Bedford Heights depot = anchor account;
    # zero power washing competitors cold-calling beverage distribution depot managers in NE Ohio (added 2026-06-02 run 182)
    'beverage distribution manager', 'beverage district manager', 'soft drink distribution manager',
    'beverage depot manager', 'bottling operations manager', 'beverage route manager',
    'beer distributor manager', 'beverage operations director',
    # Electric Utility Substations & Power Distribution Facilities — FirstEnergy Corp (HQ Akron OH),
    # AEP Ohio, The Illuminating Company (Cleveland), Ohio Edison (Akron/Summit); 200+ NE Ohio substations
    # each with large concrete equipment pads, control buildings, fenced perimeter surfaces;
    # EPA SPCC Plan (40 CFR Part 112) + NPDES stormwater permit = facility concrete cleaning is a
    # regulatory compliance line item, not discretionary; one regional FM = multi-site contract across
    # dozens of substations; COMPLETELY DISTINCT from manufacturing (run 118 — factory loading docks),
    # government (run 124 — city/county buildings), pharma (run 180), data centers (run 181);
    # utility FM contacts are completely un-targeted by any NE Ohio power washing competitor;
    # $2K–$6K/facility; quarterly = $8K–$24K/facility/year; FirstEnergy territory = $200K+ potential;
    # zero competitors; first pull June 8 Cuyahoga (added 2026-06-02 run 183)
    'electric utility facilities manager', 'utility site manager', 'substation facility manager',
    'power utility facility manager', 'electric utility operations manager', 'utility facilities director',
    'power distribution facility manager', 'electric cooperative facilities manager',
    # Private EMS & Ambulance Service Depots — American Medical Response (AMR — Cuyahoga County EMS
    # contract), Rural Metro Medical Services (Lorain/Lake County), STAT Medical Transport, Medix Ambulance;
    # private EMS vehicle bays accumulate blood, IV solution, biological material, chemical decontaminant
    # residue, diesel exhaust — among the worst concrete staining scenarios outside industrial facilities;
    # OSHA 29 CFR 1910.1030 bloodborne pathogens standard + EPA hazmat disposal compliance =
    # exterior surface cleaning of ambulance bays is a regulatory requirement, not optional;
    # COMPLETELY DISTINCT from hospital campuses (run 124), urgent care (run 114), ambulatory surgery (run 143);
    # EMS operations managers sign vendor contracts; zero competitors cold-calling EMS depot managers;
    # $800–$2,500/depot visit; 4x/year; AMR multi-depot NE Ohio territory = $12.8K–$40K/year;
    # first pull June 8 Cuyahoga (added 2026-06-02 run 183)
    'ems operations manager', 'ambulance service manager', 'emergency medical services director',
    'ems director', 'ambulance operations director', 'medical transport manager',
    'ems district manager', 'emergency services manager',
    # Industrial Gas Suppliers & Welding Supply Companies — Airgas (NE Ohio division — multiple
    # cylinder filling plants + distribution depots), Air Products (Cleveland/Akron operations),
    # Matheson Gas Products (NE Ohio distribution center), Praxair Distribution / Linde Gas (NE Ohio),
    # Valley National Gases (Pittsburgh/NE Ohio), Roberts Oxygen (NE Ohio), Alexander Chemical;
    # Welding supply: Lincoln Electric (Euclid OH HQ — Fortune 500, largest US welding equipment mfr),
    # Miller Electric distributor locations, ESAB Ohio distributor (Strongsville), Red-D-Arc (Cleveland);
    # Concrete staining profile: liquid nitrogen/oxygen spill residue (extreme cryogenic + residue),
    # acetylene/propane cylinder corrosion rust runoff, hydraulic fluid from delivery truck staging areas,
    # diesel exhaust from cylinder delivery fleet — among worst industrial concrete environments;
    # DOT hazardous materials transportation regulations (49 CFR) + EPA Tier I/II EPCRA hazardous chemicals
    # storage = facility exterior cleanliness is tracked in compliance records, not discretionary;
    # COMPLETELY DISTINCT from manufacturing (run 118 — factory production, different Apollo org tags),
    # distribution centers (run 105 — fulfillment/logistics, different Apollo org tags),
    # scrap metal (run 181 — metals recycling), pharma (run 180 — pharmaceutical GMP compliance);
    # Apollo org tags 'welding supply'/'industrial gas'/'compressed gas'/'gas distributor' return ZERO
    # overlap with any existing DANNY_ORG_KEYWORDS; branch/depot managers sign vendor contracts;
    # $1,500–$5,000/facility; quarterly = $6K–$20K/year; Lincoln Electric Euclid campus alone is an
    # $8K–$20K/year anchor account; zero NE Ohio competitors targeting industrial gas depot FMs;
    # first pull June 8 Cuyahoga (added 2026-06-02 run 184)
    'industrial gas manager', 'welding supply manager', 'gas distribution manager',
    'cylinder plant manager', 'compressed gas manager', 'welding supply branch manager',
    'industrial gas branch manager', 'gas depot manager',
    # Commercial Printing Plants & Publishing Facilities — COMPLETELY DISTINCT from retail print shops
    # (run 151 — FedEx Office, UPS Store, Minuteman Press; Apollo tags 'printing services'/'business
    # services center' — strip-mall retail, not industrial); these are large-format commercial offset
    # printing plants with industrial-scale loading docks and massive paved concrete areas;
    # NE Ohio targets: Lake Shore Printing (Willoughby — one of largest NE Ohio commercial printers),
    # West Shore Printing & Publishing (Berea), Ohio Business Media (Chagrin Falls — magazine publishing),
    # Dispatch Printing NE Ohio operations, Hometown Newspapers (Sun News/suburban chains — Berea HQ),
    # Great Lakes Educational Book (Mentor — educational publisher + print ops), Commercial Printing
    # Company of Cleveland; Lincoln/National (specialty commercial printing, NE Ohio operations);
    # Concrete staining profile: offset printing ink overspray on loading dock concrete (metallic + black
    # ink = permanent if untreated), petroleum-based solvent wash residue from press cleaning cycles,
    # paper dust + moisture accumulation = thick gray compacted staining, diesel exhaust from delivery
    # truck staging areas — some of the most visually severe concrete staining in any industrial segment;
    # EPA VOC (Volatile Organic Compound) permit requirements for printing facilities (40 CFR Part 63
    # MACT for printing/publishing) = plant exterior maintenance is documented in compliance records;
    # OSHA 29 CFR 1910.22 general industry housekeeping standards apply to exterior walkways + loading;
    # Apollo org tags 'commercial printing'/'offset printing'/'printing plant'/'print manufacturer' return
    # ZERO overlap with run 151 'printing services'/'business services center' (retail print shops);
    # plant operations managers or facility managers sign vendor contracts; $2,000–$6,000/facility;
    # 2x/year (spring + fall maintenance windows); $4K–$12K/year per plant; zero competitors targeting
    # industrial printing plant FMs in NE Ohio; first pull June 8 Cuyahoga (added 2026-06-02 run 184)
    'printing plant manager', 'commercial printing manager', 'print plant operations manager',
    'publishing facility manager', 'offset printing manager', 'print manufacturing manager',
    'commercial print manager', 'printing plant superintendent',
    # Aquatic Management Companies & Pool Operations Services — DISTINCT from community swimming pools
    # (run 136 — facility-level: aquatic center director, pool facility manager, natatorium manager).
    # These are COMPANIES that manage 10-50 pools FOR others: HOAs, apartment complexes, municipalities, schools.
    # United Aquatics (NE Ohio's largest pool operator), Aquatic Management Services, Pool Management Group,
    # American Pool (NE Ohio franchise territory), Great Lakes Aquatic Management, Belfor Aquatics.
    # One company = potential 10-50 soft-wash jobs from a single outreach. PEAK TIMING: June = pool startup
    # week; companies are on-site commissioning every managed pool — and the pool deck concrete, bath house
    # exterior, and perimeter parking are all in plain sight. $800–$2,000/pool; 20-pool company =
    # $16K–$40K revenue from ONE contact. Zero competitors cold-calling aquatic management companies.
    # First pull June 8 Cuyahoga. (added 2026-06-03 run 185)
    'aquatics operations manager', 'pool management director', 'aquatics services manager',
    'pool operations manager', 'aquatic operations director', 'pool services director',
    'aquatics program director', 'aquatic services manager',
    # Crane & Rigging Service Companies — Cleveland Crane & Engineering, Barnhart Crane & Rigging,
    # Maxim Crane Works (Cleveland), American Erectors, Laurel Crane & Service, LaborMax Crane (Strongsville);
    # large outdoor equipment staging yards with concrete pads; hydraulic oil drip + lubricant residue +
    # rust streaks = heavy industrial concrete staining; OSHA 29 CFR 1926.1400 crane regs require clean
    # maintenance areas; COMPLETELY DISTINCT from construction equipment rental (run 154 — United Rentals)
    # and manufacturing (run 118); crane yard manager signs vendor contracts directly; $1,500–$4,000/visit;
    # quarterly; multi-crane territory = $6K–$16K/year; zero competitors cold-calling crane yards;
    # first pull June 8 Cuyahoga (NE Ohio industrial corridor — heavy construction activity) (added 2026-06-03 run 186)
    'crane yard manager', 'rigging manager', 'crane operations manager', 'lift superintendent',
    'crane company manager', 'rigging contractor manager', 'crane service director',
    'lifting services manager',
    # Municipal Water & Wastewater Treatment Facilities — NEORSD (Northeast Ohio Regional Sewer District,
    # 7 treatment plants), Akron Metropolitan Sewer District, Lorain/Elyria/Medina city water departments,
    # Geauga-Trumbull Solid Waste District, Northeast Ohio Water Authority (NEOWA);
    # large concrete infrastructure: settling basins, pump station exteriors, chemical storage pads,
    # loading docks for chemical deliveries; spring moisture = peak biofilm/algae on treatment structures;
    # OEPA NPDES SWPPP permit = exterior cleaning is a documented compliance budget line item;
    # COMPLETELY DISTINCT from municipal facilities (run 124 — city halls/admin) and electric utilities (run 162);
    # Apollo org tags 'water treatment', 'wastewater treatment', 'sewer district' have zero overlap with existing;
    # $2,000–$6,000/facility visit; quarterly; NEORSD 7-plant territory = $56K–$168K/year potential;
    # zero competitors cold-calling water plant superintendents in NE Ohio; first pull June 8 Cuyahoga (added 2026-06-03 run 186)
    'water plant superintendent', 'wastewater treatment manager', 'utilities facilities manager',
    'water treatment plant manager', 'sewer district operations manager', 'public utilities director',
    'water utilities manager', 'wastewater plant superintendent',
    # Ice Rinks & Hockey Facilities — Brooklyn Ice Arena, Mentor Ice Arena, Strongsville Surburban Arena,
    # OhioHealth Ice Burg (Westlake), Sheffield Lake Ice Arena, Kent State Ice Arena;
    # NE Ohio = one of the densest hockey markets in the US (Ohio Hockey Assoc. + USAH Ohio district);
    # Zamboni bay + concrete rink surround + building exterior + parking lot; spring/summer = ideal pitch
    # window (rink schedules lighten, exterior maintenance season opens); hydraulic fluid + ice melt
    # chemical residue = concrete staining unique to this segment; $1,000–$3,000/visit; 2x/year;
    # new unique titles only — deduped against run 155 block (added 2026-06-03 run 187, deduped run 188)
    'arena manager', 'rink operations manager', 'ice complex manager',
    # Bowling Centers & FECs — new unique titles only; deduped against run 120 block (run 188)
    'entertainment venue manager', 'bowling operations manager',
    'fec manager', 'entertainment complex manager',
    # EV Charging Network Operators — segment #171; ChargePoint, EVgo, Blink, BP Pulse, Electrify America;
    # concrete charging pads + canopy structures; regional ops managers sign vendor contracts;
    # $10K-$30K/year per territory deal; zero competitors; first pull June 8 Cuyahoga (added 2026-06-03 run 188)
    'ev charging station manager', 'electric vehicle charging manager', 'ev network operations manager',
    'charging infrastructure manager', 'ev facility manager', 'charging station operations director',
    'ev charging operations manager', 'ev infrastructure director',
    # Steel Service Centers & Metal Distributors — segment #172; Olympic Steel (Bedford Heights HQ),
    # Metals USA (Independence OH), Service Center Corp, Worthington Industries NE Ohio ops, Reliance Steel,
    # Chapel Steel, Samuel Service Centers; 50+ facilities in the Cuyahoga/Lake/Lorain corridor;
    # NE Ohio = heart of US steel service center industry (Cleveland-area warehoused more flat-rolled steel
    # than any metro outside Pittsburgh); processing bays + loading docks coated in cutting fluid, metal
    # chips, rust staining, lubricating oil, and mill scale dust; OSHA 29 CFR 1910.22 (floor/aisle
    # cleanliness) + EPA NPDES SWPPP stormwater permit = regulatory urgency for exterior cleaning;
    # COMPLETELY DISTINCT from scrap metal dealers (run 181 — ferrous recycling Apollo tags) and
    # manufacturing plants (run 118 — 'metal fabrication'/'steel manufacturer' production tags);
    # $2,000–$8,000/visit; quarterly = $8,000–$32,000/year per facility; zero competitors targeting
    # steel service center FMs in NE Ohio; first pull June 8 Cuyahoga (Bedford Heights/Independence corridor)
    # (added 2026-06-03 run 189)
    'steel service center manager', 'metal service center manager', 'metals distribution manager',
    'steel distribution manager', 'steel processing manager', 'metals operations director',
    'service center branch manager', 'metals facility manager',
    # Fraternal & Social Organizations — segment #173; Elks Lodge (80+ NE Ohio chapters), Moose Lodge (70+),
    # Fraternal Order of Eagles (100+), Knights of Columbus (150+ NE Ohio councils), Boy Scouts council
    # service centers; COMPLETELY DISTINCT from VFW/American Legion (run 174 — veterans service orgs);
    # meeting halls + parking lots + building exteriors; lodge manager or hall administrator signs vendor
    # contracts directly with zero procurement layer; these organizations host weddings, graduation parties,
    # and community banquets — appearance is a direct reflection of the community they serve;
    # pitch: "Your lodge is a community institution — it should look like one";
    # $500–$1,500/visit; 1-2x/year; 400+ NE Ohio locations; zero power washing competitors;
    # first pull June 8 Cuyahoga (added 2026-06-03 run 189)
    'lodge manager', 'lodge administrator', 'fraternal lodge manager', 'elks lodge manager',
    'moose lodge manager', 'social club manager', 'hall manager', 'fraternal organization manager',
    # Residential Group Homes & DODD-Licensed Care Facilities — segment #174;
    # Ohio DODD Medicaid waiver residential programs: group homes (5-8 residents), ICF/DD facilities,
    # supported living homes, community living facilities; DISTINCT from skilled nursing (run 169),
    # senior assisted living (run 94), home care agencies (run 163);
    # DODD Rule 5123:2-3 + CMS CoP exterior cleanliness standard = compliance driver;
    # administrators sign vendor contracts directly — no property management layer;
    # 2,000+ licensed facilities in Cuyahoga County alone; managed by Elara Caring, LADD Inc,
    # Buckeye Community Health Plan providers, Residential Opportunities Inc (ROI), OAKS of NE Ohio;
    # $400–$900/visit; 2x/year; 1 management company with 20 homes = $16K–$36K/year;
    # zero competitors cold-calling group home administrators; first pull June 8 Cuyahoga (added 2026-06-03 run 190)
    'group home administrator', 'group home director', 'residential group home manager',
    'dodd home manager', 'icf administrator', 'supported living manager',
    'residential care manager', 'community living manager',
    # Restaurant Equipment & Commercial Kitchen Supply Companies — segment #175
    # Eastern Restaurant Supply (Cleveland), American Restaurant Equipment (Akron), Wasserstrom NE Ohio
    # warehouse, WebstaurantStore distribution hub, Sysco NE Ohio division;
    # DISTINCT from restaurants/QSR (run 106), food processing plants (run 127), distribution centers (run 105);
    # NASDA food equipment dealer licensing + FDA FSMA compliance = exterior appearance standard;
    # $2,000–$5,000/facility; 2–3×/year; zero competitors; first pull June 8 Cuyahoga (added 2026-06-03 run 191)
    'restaurant equipment manager', 'commercial kitchen supply manager', 'food service equipment manager',
    'restaurant supply manager', 'kitchen equipment district manager', 'food equipment operations manager',
    'restaurant supply district manager', 'commercial food equipment manager',
    # Specialty Chemical Manufacturers & Polymer Plants — segment #176
    # Lubrizol Corporation (Wickliffe OH HQ), RPM International (Medina OH HQ), Vibrantz Technologies/Ferro
    # (Mayfield Heights), Materion Corporation (Mayfield Heights), Omnova Solutions (Beachwood), BASF Cleveland;
    # DISTINCT from manufacturing (run 118), pharma (run 180), industrial gas (run 184);
    # EPA 40 CFR Part 68 RMP + OSHA PSM 29 CFR 1910.119 + OEPA NPDES SWPPP = exterior compliance-documented;
    # $3,000–$10,000/facility; quarterly; zero competitors; first pull June 8 Cuyahoga (added 2026-06-03 run 191)
    'chemical plant manager', 'chemical operations manager', 'specialty chemical manager',
    'polymer plant manager', 'chemical facility manager', 'chemical manufacturing manager',
    'chemical plant superintendent', 'polymer operations manager',
    # Federal Government & VA Healthcare Facilities — segment #177
    # VA Northeast Ohio Healthcare System (Wade Park Cleveland + Brecksville + 18 CBOCs), IRS Brookpark Service
    # Center, NASA Glenn Research Center (Brookpark), Federal Reserve Bank of Cleveland, US District Court
    # Northern Ohio; National Guard Armories (18+ Cuyahoga area), Army Reserve Centers, GSA-managed federal
    # buildings; DISTINCT from municipal/government (run 124 — city/county/township facilities);
    # these are FEDERAL-tier FMs with UFC 3-301 + Clean Water Act Section 438 stormwater compliance;
    # $3,000–$15,000/facility; zero competitors cold-calling VA FMs; first pull June 8 Cuyahoga (added 2026-06-03 run 192)
    'federal building manager', 'va facility manager', 'veterans affairs facility manager',
    'federal facilities manager', 'federal property manager', 'national guard facilities manager',
    'army reserve facilities manager', 'federal facility manager',
    # Ready-Mix Concrete & Asphalt Production Facilities — segment #178
    # Shelly Company (Medina County HQ — NE Ohio's largest paving/aggregate company), Aggregate Industries NE Ohio,
    # CEMEX NE Ohio division, Martin Marietta (Lorain County quarries), Hanson Aggregates (Lake/Portage County);
    # concrete dust + asphalt residue + aggregate runoff = documented OSHA 1910.22 + OEPA NPDES SWPPP staining;
    # DISTINCT from manufacturing (run 118 — general industrial), specialty chemical (run 176);
    # 80+ NE Ohio plants; $2,000–$6,000/plant; quarterly; zero competitors; first pull June 8 Cuyahoga (added 2026-06-03 run 192)
    'ready mix concrete manager', 'concrete plant manager', 'concrete plant superintendent',
    'asphalt plant manager', 'hot mix asphalt manager', 'concrete production manager',
    'asphalt plant superintendent', 'quarry plant manager', 'aggregate plant manager',
    'batch plant manager', 'concrete operations manager', 'asphalt operations manager',
    # County Correctional Facilities & Detention Centers — segment #179
    # Cuyahoga County Jail (downtown Cleveland + Euclid Ave campus), Summit County Jail (Akron),
    # Lake County Adult Correctional Facility, Medina County Jail, Lorain County Jail,
    # Geauga County Jail, Portage County Adult Correctional Facility + juvenile detention centers;
    # exterior building surfaces + sally port aprons + vehicle staging areas + perimeter concrete;
    # ACA (American Correctional Association) accreditation + OEPA NPDES SWPPP compliance = exterior standard;
    # Ohio Revised Code Sec. 341.01 — county sheriff responsible for maintaining jail in clean condition;
    # government direct-award contracts; $3,000–$10,000/facility; annual recurring; zero competitors;
    # DISTINCT from municipal facilities (run 124 — city halls/transit) + federal gov (run 177 — VA/NASA);
    # first pull June 8 Cuyahoga (added 2026-06-03 run 193)
    'jail administrator', 'detention facility manager', 'corrections facilities director',
    'county jail administrator', 'county jail manager', 'detention center director',
    'sheriff facilities manager', 'correctional facility manager', 'corrections facility director',
    'juvenile detention director', 'detention operations manager', 'county corrections manager',
    # Inpatient Rehabilitation Hospitals & Long-Term Acute Care (LTAC) Facilities — segment #180
    # Select Medical / Regency Hospital (Cleveland + Akron), Kindred Hospitals NE Ohio,
    # Promise Hospitals, Encompass Health Rehabilitation Hospitals (Concord Township + Sheffield Village);
    # DISTINCT from skilled nursing/LTC (run 169 — nursing homes), outpatient PT (run 126 — NovaCare/ATI),
    # hospital main campuses (run 124), acute care (run 143 — ASCs);
    # CMS CoP Section 482 + JCAHO hospital accreditation = exterior appearance standard;
    # 30+ NE Ohio LTAC/IRF facilities; $3,000–$8,000/facility; 2x/year; zero competitors;
    # first pull June 8 Cuyahoga (added 2026-06-03 run 193)
    'rehabilitation hospital administrator', 'rehabilitation hospital director',
    'ltac administrator', 'inpatient rehabilitation director', 'long-term acute care director',
    'rehab hospital manager', 'ltac facility manager', 'inpatient rehab director',
    'ltac hospital administrator', 'rehab hospital administrator', 'acute rehabilitation director',
    # K-12 Private & Parochial Schools — segment #181
    # Gilmour Academy (Gates Mills), St. Ignatius HS, Magnificat HS, Walsh Jesuit, Archbishop Hoban,
    # Western Reserve Academy (Hudson), Laurel School (Shaker Heights), University School (Hunting Valley);
    # Diocese of Cleveland Catholic school system (140+ schools in 8-county area);
    # DISTINCT from public K-12 districts (run 119 — buildings & grounds directors in public school districts)
    # and from churches/parishes (run 110 — parish administrators at church facilities);
    # private school buildings & grounds directors manage vendor contracts independently;
    # summer (June-August) = empty campus = PEAK annual exterior maintenance window;
    # multiple buildings per campus (St. Ignatius: 5 buildings; Western Reserve Academy: 30+ campus buildings);
    # $1,500–$5,000/building; one campus deal = $8K–$25K/year; zero competitors targeting private school FM contacts;
    # Apollo org tags 'private school', 'independent school', 'catholic school' DISTINCT from 'school district';
    # first pull June 8 Cuyahoga (added 2026-06-03 run 194)
    'private school facilities director', 'private school building manager',
    'independent school facilities manager', 'diocesan facilities manager',
    'catholic school facilities manager', 'prep school facilities director',
    'independent school superintendent', 'parochial school administrator',
    'private school operations manager',
    # County Fairgrounds & Agricultural Exhibit Facilities — segment #182
    # Cuyahoga County Fairgrounds (I-X Center grounds / Berea), Summit County Fairgrounds (Tallmadge),
    # Medina County Fairgrounds (Medina), Lorain County Fairgrounds (Wellington),
    # Lake County Fairgrounds (Painesville), Geauga County Fairgrounds (Burton — Geauga County Fair
    # is one of Ohio's largest), Portage County Fairgrounds (Ravenna);
    # MASSIVE paved midway lots + grandstand concourses + exhibit hall exteriors + livestock barn aprons;
    # June = fair prep season — county fairs run July-September = pressure washing contracts awarded NOW;
    # government direct-award contracts (county agricultural society = quasi-governmental entity);
    # DISTINCT from sports venues (run 127), convention centers (run 128), event venues (run 108);
    # $3,000–$12,000/fairground; annual pre-fair prep contract; zero competitors targeting fairgrounds FMs;
    # first pull June 8 Cuyahoga (added 2026-06-03 run 194)
    'fairgrounds manager', 'county fair director', 'fairgrounds director',
    'fairgrounds facilities manager', 'agricultural fair manager', 'county fair manager',
    'fairgrounds operations manager', 'fairgrounds superintendent', 'fair operations director',
    # Aerospace & Defense Component Manufacturers — segment #183; DISTINCT from general manufacturing (run 118);
    # Parker Hannifin (Mayfield Heights HQ — Fortune 500, 50+ NE Ohio facilities), TransDigm Group (Cleveland HQ — NYSE:TDG),
    # Moog Inc. (NE Ohio supply chain), Ducommun Incorporated; AS9100D quality management + ITAR compliance =
    # documented facility maintenance requirement; building exteriors + loading docks + employee parking structures;
    # zero competitors cold-calling aerospace FM contacts; $5,000–$25,000/facility; quarterly (added 2026-06-04 run 195)
    'aerospace facilities manager', 'defense plant manager', 'aerospace plant manager',
    'aerospace operations manager', 'aerospace manufacturing manager',
    'defense facilities manager', 'aerospace plant superintendent', 'defense manufacturing manager',
    # Precision Machining & CNC Machine Shops — segment #184; DISTINCT ORG KEYWORDS from general manufacturing (run 118);
    # 'precision machining', 'cnc machining' Apollo tags return ZERO overlap with 'manufacturing plant' tags;
    # NE Ohio has 500+ precision machine shops in Lorain/Lake/Cuyahoga/Summit corridors;
    # ISO 9001 + AS9100 supply chain compliance; machining coolant + metal chips = heavy exterior staining;
    # shop owners sign vendor contracts directly; $1,500–$5,000/shop; quarterly; zero competitors (added 2026-06-04 run 195)
    'machine shop manager', 'precision machining manager', 'cnc operations manager',
    'precision manufacturing manager', 'machine shop superintendent',
    'cnc shop manager', 'precision machining superintendent', 'machine shop owner',
    # Public Transit Agencies & Bus Depot Facilities — segment #185
    # GCRTA (Greater Cleveland RTA), Metro RTA (Akron), SARTA (Canton/Stark), LAKETRAN (Lake County),
    # Lorain County Transit, Medina County transit; bus garage concrete floors + transit center plazas +
    # maintenance yards = recurring cleaning need; FTA ADA compliance + ODOT transit standards;
    # DISTINCT from municipal government (run 124) — transit-specific Apollo org keywords not covered by
    # 'city facilities manager'; DISTINCT from school bus companies (run 178) — public transit, not school transport;
    # $8,000–$25,000/depot facility; GCRTA alone has 5+ facilities = $40K–$125K/year; zero competitors;
    # first pull June 8 Cuyahoga (added 2026-06-05 run 196)
    'transit operations director', 'bus depot operations manager', 'transit system facilities manager',
    'transit depot manager', 'transit agency facilities manager', 'bus garage manager',
    'public transit facilities director', 'transit maintenance facilities manager',
    # Industrial Real Estate & Logistics Park Management — segment #186
    # ProLogis Cleveland/Independence (Fortune 500, 5M+ sq ft NE Ohio), Duke Realty NE Ohio, Scannell Properties,
    # Opus Group, Pizzuti Companies, NRP Group; own/manage 50–200 industrial buildings per company =
    # ONE FM contact = 50–200 potential cleaning jobs at $1,500–$5,000 each;
    # DISTINCT from Carla's commercial RE brokers (transactional sales, run 176) — these are property
    # maintenance managers, not listing agents; DISTINCT Apollo org keywords = additive leads, zero overlap
    # with residential/office property management ('commercial property management' existing tag); building
    # exteriors + loading dock facades + massive paved lots = quarterly recurring contract;
    # $1,500–$5,000/building × 100-building portfolio = $150K–$500K/year from ONE REIT relationship;
    # zero competitors targeting industrial REIT FMs; first pull June 8 Cuyahoga (added 2026-06-05 run 196)
    'industrial property manager', 'logistics real estate manager', 'warehouse property manager',
    'industrial park manager', 'logistics park manager', 'industrial campus manager',
    'industrial portfolio manager', 'warehouse campus manager',
    # Indoor Shooting Ranges & Archery Centers — segment #187; 50+ NE Ohio ranges;
    # large parking lots + building exteriors + range surroundings; owner/operators sign vendor contracts;
    # NRA-affiliated compliance standard; spring pre-season = peak pitch window (ranges get dirty over winter);
    # $800-$2,500/visit; 2x/year = $1,600-$5,000/year per range; zero competitors cold-calling;
    # first pull June 8 Cuyahoga (added 2026-06-06 run 197)
    'shooting range manager', 'gun range manager', 'indoor range manager',
    'archery center director', 'shooting sports manager', 'firearms range manager',
    'gun range owner', 'archery range owner',
    # Cannabis Cultivation & Processing Facilities — segment #188; Ohio rec. cannabis legal Nov 2023;
    # grow licenses now active; DISTINCT from dispensaries (run 135) — these are production facilities;
    # industrial-scale exterior maintenance: large secured perimeters + equipment areas + loading zones;
    # Ohio State Board of Pharmacy licensing = exterior appearance standard;
    # $3,000-$8,000/facility; quarterly recurring; zero competitors cold-calling cannabis grow FMs;
    # first pull June 8 Cuyahoga (added 2026-06-06 run 197)
    'cannabis cultivation manager', 'grow facility manager', 'cultivation director',
    'cannabis operations manager', 'cannabis plant manager', 'marijuana operations manager',
    'grow operations manager', 'cannabis facility manager',
    # Multi-Site Fitness Chain District Operations — segment #189; Planet Fitness franchise groups
    # (3-8+ NE Ohio locations per franchisee), Anytime Fitness franchise networks (40+ NE Ohio),
    # Gold's Gym regional operators, LA Fitness regional FMs, Crunch Fitness franchise groups;
    # DISTINCT from individual gym managers (run 99 — gym manager/fitness director already in list)
    # and boutique studio owners (run 143 — fitness franchise owner/studio director already in list);
    # multi-site district FMs sign one vendor contract covering all locations in their territory;
    # large paved parking lots + building exteriors + concrete entry aprons across every location;
    # $800-$2,000/location; 8-location district = $6,400-$16,000/year; zero competitors cold-calling
    # fitness chain district managers; first pull June 8 Cuyahoga (added 2026-06-07 run 198)
    'health club district manager', 'gym district manager', 'fitness chain operations manager',
    'multi-club manager', 'fitness operations director', 'fitness area manager',
    'health club operations director', 'gym operations manager',
    # Cold Storage & Refrigerated Warehouse Networks — segment #190; Lineage Logistics (multiple
    # Cleveland-area facilities — world's largest cold storage REIT), Americold Cleveland,
    # US Cold Storage NE Ohio, NewCold, Burris Logistics, Performance Food Group cold warehouses;
    # DISTINCT from food manufacturers with cold storage (run 127 — org tag 'food processing plant'/'food manufacturer');
    # DISTINCT from general warehouses (run 105 — 'warehouse manager' already in list but targets
    # distribution/fulfillment; cold storage companies have distinct Apollo org tags);
    # loading dock concrete + refrigerated bay exteriors + truck court areas = heavy staining
    # from brake fluid, hydraulic fluid, diesel, and constant heavy vehicle traffic;
    # USDA AMS cold storage facility licensing + EPA SPCC/NPDES compliance = exterior cleanliness standard;
    # $2,000-$6,000/facility visit; quarterly = $8,000-$24,000/year; NE Ohio = major cold chain hub;
    # zero competitors cold-calling cold storage network FMs; first pull June 8 Cuyahoga (added 2026-06-07 run 198)
    'cold storage facility manager', 'cold storage operations manager', 'refrigerated warehouse manager',
    'temperature controlled facility manager', 'cold chain facility manager',
    'cold storage district manager', 'refrigerated storage manager', 'cold storage regional manager',
    # Intermodal Rail Terminals & Freight Hub Facilities — segment #191; CSX Collinwood Terminal (Cleveland's
    # largest Class I rail freight facility), Norfolk Southern Cleveland Consolidated Terminal,
    # Wheeling & Lake Erie Railway, CPKC (Canadian Pacific Kansas City) Cleveland hub;
    # OSHA 29 CFR 1926 + EPA SPCC stormwater compliance = documented exterior maintenance requirement;
    # locomotive service pits + freight cargo building facades + massive paved truck court areas = heavy staining;
    # terminal facility managers sign vendor contracts; $5,000–$20,000/year per terminal;
    # zero competitors cold-calling rail terminal FM contacts in NE Ohio; first pull June 8 Cuyahoga (added 2026-06-08 run 199)
    'rail terminal manager', 'intermodal terminal manager', 'freight terminal manager',
    'rail yard manager', 'intermodal facility manager', 'freight hub manager',
    'rail operations manager', 'terminal operations director', 'rail terminal superintendent',
    # Commercial Parking Management Portfolio Companies — segment #192; SP+ Corporation (formerly Standard
    # Parking Plus), Impark, ABM Parking Services, InterPark, Lanier Parking, Premium Parking;
    # DISTINCT from individual parking structure managers (run 128 — single-facility titles);
    # these are PORTFOLIO-LEVEL management companies operating 50-200+ NE Ohio lots/garages;
    # one regional operations manager contact = vendor deal across entire NE Ohio portfolio;
    # $500-$2,000/location × 30-lot portfolio = $15,000-$60,000/year from ONE contact;
    # zero competitors cold-calling parking management company regional ops managers; first pull June 8 Cuyahoga (added 2026-06-08 run 199)
    'parking management regional manager', 'parking portfolio manager', 'parking network manager',
    'parking operations regional manager', 'parking management director', 'parking services director',
    'valet parking manager', 'parking management operations director', 'parking company regional director',
    # Co-Packing & Contract Manufacturing Facilities — segment #193; DISTINCT from general manufacturing
    # (run 118 — captive plant FMs) and food processing (run 127 — branded food plants);
    # these are THIRD-PARTY contract packagers and toll manufacturers who package/produce for brands;
    # FDA 21 CFR Part 110/117 (food co-packing) + OSHA 1910.22 compliance angle;
    # NE Ohio contract manufacturing sector: Invacare (Elyria), Nidec Motor Corp, Ferro Corp co-pack division;
    # 100+ NE Ohio contract packagers; loading dock areas + building exteriors = recurring pressure wash;
    # plant managers/operations directors sign vendor contracts directly; $3K-$8K/facility;
    # zero competitors cold-calling co-packing facility FMs in NE Ohio; first pull Lake June 15 (added 2026-06-09 run 200)
    'co-packing operations manager', 'contract manufacturing manager', 'packaging plant manager',
    'co-manufacturing director', 'contract packaging manager', 'co-pack facility manager',
    'toll manufacturing manager', 'packaging operations manager',
    # Semiconductor & PCB/Electronics Circuit Board Manufacturers — segment #194;
    # DISTINCT from aerospace/defense (run 183) and medical device (run 168);
    # NE Ohio electronics manufacturing: Parker Hannifin Electronics (Mayfield Heights),
    # API Technologies (Cleveland), Benchmark Electronics, Greatbatch (Lake County),
    # Vishay Intertechnology (Cleveland), Keithley Instruments (Solon);
    # ISO 14001 + OEPA NPDES permit = documented exterior maintenance requirement;
    # cleanrooms require clean exterior perimeters — audit-ready appearance standard;
    # $3K-$12K/facility; zero competitors cold-calling NE Ohio electronics plant FMs; first pull Lake June 15 (added 2026-06-09 run 200)
    'semiconductor plant manager', 'pcb manufacturing manager', 'circuit board plant manager',
    'electronics plant manager', 'printed circuit board manager', 'electronics manufacturing manager',
    'semiconductor facility manager', 'electronics operations manager',
    # Boat Repair & Marine Service Centers — segment #195; routing to property_manager sequence
    # (facility maintenance / vendor contract angle); Lake Erie corridor peak window = June–August;
    # repair yards + equipment bays + covered boat storage areas = algae + oil staining;
    # DISTINCT from marinas (run 109 — slip docking/seasonal storage), boat dealers (run 146 — retail sales),
    # charter fishing (run 174 — excursion operators);
    # NE Ohio targets: Grand River Marine Service, Fairport Harbor Boat Works, Mentor Marine, Chagrin Falls Marine;
    # $800–$2,500/visit; 3x/year = $2,400–$7,500/year; zero competitors cold-calling marine repair FMs;
    # first pull Lake County June 15 (added 2026-06-10 run 201)
    'marine service manager', 'boat yard manager', 'marine repair manager', 'boat repair manager',
    'marine service director', 'boat yard superintendent', 'marine maintenance supervisor',
    'marine operations director',
    # Craft Breweries & Taprooms — segment #196 (added 2026-06-11 run 202)
    # NE Ohio has 100+ craft breweries: Platform Beer (Cleveland), Great Lakes Brewing (Ohio City), Market Garden Brewery,
    # Fat Head's Brewery (Middleburg Heights), Willoughby Brewing (Lake County — fires June 15), Hoppin' Frog (Akron),
    # Thirsty Dog Brewing (Akron), Elliot Brewing (Willoughby), Forest City Brewery (yes, same name — Cleveland),
    # Cornerstone Brewing, Birdfish Brewing (Chesterland), Chagrin Valley Brewing, Buckeye Brewing;
    # outdoor seating areas + loading dock concrete + parking lots + patio/deck surfaces accumulate grime during
    # peak outdoor season (May–Sept = maximum visibility); brewery/taproom manager signs vendor contracts;
    # $800–$2,500/visit; 3x/year = $2,400–$7,500/year; zero competitors cold-calling this segment;
    # DISTINCT from restaurants (run 106 — org tags: 'restaurant', 'dining', 'food service');
    # first pull: Cuyahoga retroactive + Lake County June 15 (Willoughby Brewing is a flagship Lake County target)
    'brewery manager', 'taproom manager', 'brewery operations manager', 'brewery director',
    'taproom director', 'craft brewery manager', 'production brewery manager',
    'beverage facility manager', 'brewery owner',
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
    # Golf courses & country clubs — 100+ NE Ohio courses; large paved lots + cart staging + clubhouse exterior;
    # May-June = peak season (member events, tournaments, corporate outings); zero competitors targeting this segment (added 2026-05-27 run 112)
    'golf course', 'country club', 'golf club', 'golf course management', 'private club',
    # Cemeteries & memorial parks — large paved driveways + pavilion areas; spring = peak visitor season (added 2026-05-27 run 112)
    'cemetery management', 'memorial park management', 'cemetery services',
    # Funeral homes — 100+ NE Ohio locations; parking lots, chapel facades, covered porticos;
    # families see the property on their most emotional day — appearance is non-negotiable;
    # funeral directors/owners sign vendor contracts; low competition; $2K-$6K/year per location (added 2026-05-27 run 113)
    'funeral home', 'funeral services', 'mortuary services', 'funeral parlor', 'memorial services',
    'cremation services', 'funeral home management',
    # Urgent care centers — FastMed, Concentra, GoHealth, CareNow, Summa Now, MetroHealth Urgent Care;
    # ORC licensing = exterior cleanliness standards; summer = peak volume; high foot traffic on entry surfaces;
    # regional FMs sign multi-clinic contracts; $3,200-$8,000/year per clinic; first pull Medina June 1 (added 2026-05-27 run 114)
    'urgent care center', 'urgent care clinic', 'walk-in clinic', 'immediate care center',
    'urgent care facility', 'ambulatory care center',
    # Veterinary clinics & animal hospitals — Banfield (PetSmart-affiliated), VCA Animal Hospitals,
    # BluePearl Specialty + Emergency (Westlake, Northfield), National Veterinary Associates, Petco VetCo;
    # licensing inspections = clean exterior requirement; high-traffic parking + entry walkways = recurring need;
    # corporate chains sign multi-clinic vendor contracts across NE Ohio (added 2026-05-28 run 115)
    'veterinary clinic', 'animal hospital', 'veterinary practice', 'vet clinic',
    'animal care center', 'veterinary hospital', 'pet hospital',
    # Towing companies & auto salvage — large paved yards + impound lots + loading bays;
    # heavy oil, hydraulic fluid, road salt accumulation; NE Ohio has 50+ operators: Jeff's Towing, Allied,
    # AAA-contracted impound lots, Belden's, regional salvage chains; owner-operators sign vendor contracts directly;
    # zero competitors targeting this segment; $800-$2,500/visit; 4x/year = $3,200-$10,000/year per operator (added 2026-05-28 run 117)
    'towing company', 'auto salvage', 'salvage yard', 'impound lot', 'tow yard',
    'junkyard', 'vehicle salvage', 'towing service',
    # Manufacturing & industrial facilities — NE Ohio is a major Midwest manufacturing hub;
    # Ford Avon Lake, Lincoln Electric (Euclid), Eaton (Beachwood HQ), Parker Hannifin (Mayfield Heights),
    # Republic Steel (Canton), North Star BlueScope (Delta), hundreds of Tier 1/2 auto suppliers;
    # loading docks accumulate oil, grease, chemical residue; OSHA compliance = recurring urgency;
    # plant FMs sign vendor contracts for exterior cleaning; $800-$4,000/visit; 4x/year (added 2026-05-28 run 118)
    'manufacturing plant', 'industrial facility', 'production facility', 'metal fabrication',
    'steel manufacturing', 'auto parts manufacturer', 'industrial manufacturing',
    'assembly plant', 'manufacturing operations', 'plant operations',
    # Car wash facilities — Mr. Clean Car Wash (12+ NE Ohio locations), Mister Car Wash, independent coin-ops;
    # building exteriors, vacuum bays, equipment areas need periodic pressure washing;
    # ironic pitch: "We wash your building while you wash cars"; OSHA stormwater/runoff compliance;
    # district managers sign multi-location contracts; $1,500-$4,000/year per location (added 2026-05-28 run 118)
    'car wash', 'auto wash', 'carwash', 'vehicle wash', 'express car wash',
    'tunnel car wash', 'coin car wash', 'car wash franchise',
    # Public K-12 school districts — Cleveland Metro, Lakewood, Parma, Shaker Heights, Solon, Strongsville,
    # Brecksville-Broadview Heights, North Royalton, Cuyahoga Falls, Akron Public, Hudson City Schools;
    # summer (June-August) = buildings empty; facilities teams do annual exterior maintenance in this window;
    # 'private school' + 'independent school' already above — these keywords catch PUBLIC district orgs in Apollo (added 2026-05-28 run 119)
    'school district', 'city schools', 'public school district', 'local school district',
    'board of education', 'k-12 education',
    # Car rental companies — Enterprise Rent-A-Car, Hertz, Avis, Budget, National, Alamo at Hopkins Airport + suburban NE Ohio;
    # large paved lots with vehicle oil/exhaust staining; building exteriors; district managers sign
    # multi-location vendor contracts; $1,500-$4,000/location; district deal = $12K-$32K/year (added 2026-05-28 run 119)
    'car rental', 'vehicle rental', 'rental car', 'auto rental',
    # Tire & auto service chains — Discount Tire, Jiffy Lube, Firestone, Midas, Valvoline, Monro;
    # oil-stained paved lots + building exteriors; district managers sign multi-site contracts (added 2026-05-28 run 120)
    'tire center', 'auto service center', 'tire store', 'quick lube', 'auto lube',
    'tire franchise', 'automotive service franchise', 'muffler shop',
    # Movie theaters & cineplexes — large paved lots, marquee exteriors, entry concrete (added 2026-05-28 run 120)
    'movie theater', 'cinema', 'multiplex', 'film theater', 'theater management',
    # Public library systems — government facility managers, high foot traffic entry surfaces (added 2026-05-28 run 120)
    'public library', 'library system', 'county library', 'library district',
    # Bowling alleys & entertainment centers — large parking lots, building exteriors (added 2026-05-28 run 120)
    'bowling alley', 'bowling center', 'family entertainment center', 'entertainment center',
    'bowling lanes',
    # Dental Service Organizations (DSOs) & multi-location group dental practices — NE Ohio: Aspen Dental (20+),
    # Heartland Dental, Great Lakes Dental Partners, Midwest Dental, Dental Care Alliance;
    # DSO district managers oversee 10-20 clinics; ORC dental licensing = exterior appearance standard;
    # patient-facing parking + building entrance = appearance non-negotiable; district deal = $6K-$15K/year;
    # DSO targets ONLY — solo-dentist offices are too small; Apollo org keyword catches DSO orgs specifically (added 2026-05-28 run 123)
    'dental service organization', 'dso', 'dental group', 'dental practice management',
    'dental management company', 'group dental practice', 'dental services group',
    # Municipal & Government Facilities — city halls, county admin buildings, township offices,
    # RTA transit depots (GCRTA Hayden/Triskett/Warrensville garages), Port of Cleveland,
    # Cleveland Metroparks maintenance facilities, suburb city halls, county justice centers;
    # large parking lots, entrance plazas, public walkways = high-visibility appearance standard;
    # government FM contacts sign vendor contracts on small direct-award contracts; NE Ohio has
    # 100+ municipal entities with active facilities maintenance budgets (added 2026-05-28 run 124)
    'city facilities', 'municipal facilities', 'government facilities', 'public works department',
    'county administration', 'township administration', 'transit authority', 'port authority',
    'parks district', 'metropolitan park', 'government building management', 'municipal building',
    'city public works', 'county public works', 'civic center', 'city administration',
    # Hospital & Health System Main Campuses — main acute-care hospital buildings (separate from
    # outpatient medical offices already in DANNY_ORG_KEYWORDS above);
    # Cleveland Clinic Main Campus, UH Rainbow Babies, UH Ahuja, UH Geauga, MetroHealth Medical Center,
    # Summa Health Akron City Hospital, Mercy Health West, Southwest General, Hillcrest Hospital,
    # Marymount Hospital, South Pointe Hospital, Parma Community General Hospital;
    # hospital facility directors manage large building footprints: parking structures, entrance plazas,
    # loading docks, exterior facades — all requiring periodic pressure washing (added 2026-05-28 run 124)
    'hospital campus', 'regional hospital', 'acute care hospital', 'health system campus',
    'community hospital', 'teaching hospital', 'hospital network', 'medical center campus',
    'hospital facilities management', 'health system facilities', 'hospital plant operations',
    # Pet Boarding & Kennel Facilities — PetSmart PetsHotel, Bark Avenue, Hounds Town, Camp Bow Wow,
    # independent kennels across Cuyahoga/Summit/Lake/Lorain; outdoor runs + parking lots + building exteriors
    # accumulate biological residue; Ohio pet boarding license = exterior cleanliness standard;
    # zero competitors targeting this segment (added 2026-05-28 run 125)
    'pet boarding', 'dog kennel', 'pet hotel', 'doggy daycare', 'pet resort',
    'boarding kennel', 'animal boarding', 'dog boarding', 'cat boarding', 'pet care center',
    # Dialysis Centers — DaVita (50+ NE Ohio), Fresenius Medical Care (40+ NE Ohio), US Renal Care;
    # patients visit 3x/week = highest foot traffic density of any outpatient facility;
    # CMS certification requires clean patient-facing exterior; district FMs sign multi-location contracts (added 2026-05-28 run 125)
    'dialysis center', 'renal care', 'kidney care', 'dialysis clinic', 'dialysis facility',
    'dialysis services', 'outpatient dialysis', 'renal dialysis',
    # Sports Complexes & Youth Athletic Facilities — Sportsplex at Mentor, Great Lakes Athletic Complex,
    # youth baseball/softball complexes, indoor soccer facilities, youth hockey rinks, gymnastics academies;
    # heavy weekend traffic from parents + kids = staining on parking lots + entrance walkways;
    # GM or owner signs vendor contracts; zero competitors targeting this segment (added 2026-05-28 run 125)
    'sports complex', 'athletic complex', 'sports facility', 'recreation complex',
    'youth sports complex', 'indoor sports facility', 'multi-sport complex', 'athletic facility',
    'youth athletics', 'sports training facility',
    # Physical Therapy Clinic Chains — NovaCare (80+ NE Ohio), ATI Physical Therapy (100+ NE Ohio),
    # Select Physical Therapy, Athletico PT; district FMs sign multi-clinic contracts;
    # state PT licensing inspections include patient-facing exterior appearance; high foot traffic;
    # 20-clinic district deal = $32K-$96K/year; zero competitors (added 2026-05-28 run 126)
    'physical therapy', 'physical therapy clinic', 'outpatient physical therapy',
    'rehabilitation clinic', 'sports medicine clinic', 'therapy clinic', 'pt clinic',
    'physical rehabilitation', 'outpatient rehab',
    # Pharmacy & Drug Store Chains — CVS (50+ NE Ohio), Walgreens (60+ NE Ohio), Rite Aid,
    # Giant Eagle Pharmacy, Discount Drug Mart (Medina HQ — 70+ NE Ohio locations);
    # drive-through canopies + large parking lots + building exteriors;
    # district FM contacts sign vendor contracts for 5-15 store territories (added 2026-05-28 run 126)
    'pharmacy chain', 'drug store chain', 'retail pharmacy', 'pharmacy management',
    'discount drug mart', 'drug mart',
    # Concert Venues & Outdoor Amphitheaters — Blossom Music Center (Live Nation, Cuyahoga Falls),
    # Jacobs Pavilion at Nautica (Cleveland waterfront, Live Nation), Hard Rock Rocksino Northfield Park,
    # Akron Civic Theatre, Playhouse Square outdoor/loading areas;
    # massive paved parking lots + concrete concourses + loading dock areas + entrance walkways;
    # Live Nation / AEG regional FM directors sign seasonal vendor contracts; zero competitors (added 2026-05-29 run 127)
    'outdoor amphitheater', 'concert venue', 'performing arts center', 'amphitheater',
    'music venue', 'concert hall', 'outdoor music venue', 'live entertainment venue',
    # Food Processing Plants & Cold Storage — FDA/USDA GMP exterior cleanliness is a regulatory requirement;
    # Shiloh Foods (Lodi/Medina County), J.M. Smucker (Orville OH), Bob Evans Foods NE Ohio centers,
    # Cloverleaf Cold Storage, Nestle USA (Solon), TreeHouse Foods, LiDestri Food & Drink;
    # loading docks + building exteriors + refrigerated bay areas = recurring quarterly pressure wash;
    # FDA 21 CFR Part 110/117 compliance angle opens doors other cleaning vendors don't use (added 2026-05-29 run 127)
    'food processing plant', 'food manufacturing facility', 'food production facility',
    'cold storage facility', 'food plant management', 'food processing operations',
    'food production plant', 'cold storage warehouse',
    # Airport & Aviation Facilities — Cleveland Hopkins, Akron-Canton, Lorain County Airport;
    # terminal building exteriors + parking structures + landside pavement + rental car lots (added 2026-05-29 run 128)
    'airport authority', 'airport facilities', 'aviation facilities', 'airport operations',
    'airport management', 'airport ground services', 'aviation ground operations',
    # Parking Garages & Structures — downtown Cleveland, hospital parking structures,
    # suburban shopping center garages; large concrete multi-story structures need periodic pressure washing (added 2026-05-29 run 128)
    'parking structure', 'parking garage management', 'parking operations management',
    # Convention Centers & Exhibition Halls — Cleveland Convention Center, I-X Center, Akron Civic Complex,
    # John S. Knight Center, Kalahari Resorts; massive event plaza + loading areas + building exteriors (added 2026-05-29 run 128)
    'convention center', 'exhibition hall', 'convention facility', 'expo center',
    'trade show facility', 'events facility management', 'convention management',
    # Craft Breweries & Taprooms — Great Lakes Brewing, Platform Beer, Masthead, Thirsty Dog, Goldhorn,
    # Terrestrial, Collision Bend, Forest City Brewery, Crooked River, Brew Kettle, Trail Brew Works;
    # outdoor patios + parking + building facades; spring patio opening = natural pitch window;
    # seasonal events = appearance is marketing; taproom GM or owner signs vendor contracts directly;
    # zero power washing competitors cold-calling brewery managers in NE Ohio (added 2026-05-29 run 129)
    'craft brewery', 'taproom', 'brewing company', 'microbrewery', 'craft beer',
    'brewpub', 'ale house', 'tap house', 'beer garden',
    # Museums & Cultural Institutions — Cleveland Museum of Art, Cleveland Museum of Natural History,
    # Cleveland Metroparks Zoo, Rock & Roll Hall of Fame, Great Lakes Science Center, Maltz Museum,
    # Crawford Auto-Aviation Museum, Severance Hall, Cleveland Play House, Akron Art Museum,
    # Stan Hywet Hall & Gardens (Akron); large paved plazas + facades + parking structures;
    # zero competitors targeting cultural institution FMs; appearance is non-negotiable for donor events;
    # first pull June 8 Cuyahoga (all major museums in University Circle + lakefront) (added 2026-05-29 run 130)
    'museum', 'art museum', 'natural history museum', 'science museum', 'science center',
    'zoo management', 'aquarium', 'botanical garden', 'cultural center', 'cultural institution',
    'museum facilities', 'historic estate', 'historic site management', 'heritage site',
    'performing arts organization', 'symphony orchestra', 'theater company', 'playhouse',
    # YMCA & Community Centers — YMCA of Greater Cleveland (12+ branches), Akron Area YMCA (7 branches),
    # Summit/Medina/Lake County YMCAs; large paved lots + outdoor pools + building exteriors;
    # state health dept. licensing inspections = exterior cleanliness standard;
    # zero competitors targeting YMCA facilities managers; first pull June 8 Cuyahoga (added 2026-05-29 run 131)
    'ymca', 'ywca', 'young mens christian association', 'community recreation center',
    # Car Auctions & Vehicle Wholesale — Manheim Cleveland (Cox Automotive), ADESA/KAR Auction (Portage County),
    # NovaStar Auto Auction, National Auto Dealers Exchange, independent wholesale auction houses;
    # enormous paved outdoor lots + reconditioning bays + building facades; OSHA stormwater compliance;
    # auction FMs run quarterly vendor contracts; zero competitors targeting this segment (added 2026-05-29 run 133)
    'auto auction', 'vehicle auction', 'car auction', 'wholesale auto auction',
    'vehicle wholesale', 'auto wholesale', 'car wholesale', 'wholesale vehicle',
    # Coin Laundries & Laundromats — NE Ohio has hundreds of independent coin laundries;
    # CoinMach route management, Alliance Laundry Systems franchisees, independent operators;
    # OEPA stormwater compliance angle (detergent runoff from parking areas) opens conversations;
    # owner-operators sign vendor contracts directly; zero competitors cold-calling this segment (added 2026-05-29 run 135)
    'coin laundry', 'laundromat', 'self-service laundry', 'laundry facility',
    'coin operated laundry', 'laundry management',
    # Blood/Plasma Donation Centers — BioLife Plasma Services, CSL Plasma, Grifols, Vitalant;
    # FDA-licensed blood establishments require clean patient-facing exterior;
    # district FMs sign multi-center vendor contracts (added 2026-05-29 run 135)
    'plasma donation center', 'blood donation center', 'plasma center', 'blood bank',
    'donor center', 'blood collection center',
    # Cannabis Dispensaries — Ohio rec. cannabis legal Nov 2023; new dispensaries opening monthly;
    # state ODM licensing = exterior appearance standard; high foot traffic = recurring cleaning need;
    # zero competitors targeting cannabis FM contacts in NE Ohio (added 2026-05-29 run 135)
    'cannabis dispensary', 'marijuana dispensary', 'cannabis retailer', 'cannabis store',
    'medical marijuana dispensary', 'recreational cannabis', 'cannabis management',
    # Professional Sports Venues — Rocket Mortgage FieldHouse (Cavs/Monsters), Progressive Field (Guardians),
    # FirstEnergy Stadium (Browns), Canal Park (Akron RubberDucks);
    # enormous paved concourses + parking lots + loading docks; year-round events = recurring cleaning;
    # facility directors manage large maintenance budgets; zero competitors (added 2026-05-29 run 135)
    'sports venue', 'professional sports venue', 'sports arena management', 'stadium management',
    'arena management', 'sports facility management', 'ballpark management', 'venue facilities',
    # Dollar Stores & General Merchandise Discount Chains — Dollar General, Family Dollar, Dollar Tree,
    # Five Below, Big Lots; 100+ NE Ohio locations per major chain; district FMs sign vendor contracts;
    # high-traffic lots + building exteriors; zero competitors cold-calling this segment (added 2026-05-29 run 136)
    'dollar store', 'dollar general', 'family dollar', 'dollar tree', 'five below',
    'general merchandise retail', 'discount retail store', 'big lots', 'discount store chain',
    'value retail', 'tuesday morning',
    # Auto Parts Stores — O'Reilly, AutoZone, Advance Auto Parts, NAPA, Pep Boys;
    # oily parking lots + building exteriors + dumpster areas; OSHA slip-hazard compliance;
    # district managers sign multi-site vendor contracts (added 2026-05-29 run 136)
    'auto parts store', 'auto parts chain', 'automotive parts retailer', 'oreilly auto parts',
    'autozone', 'advance auto parts', 'napa auto parts', 'pep boys', 'parts authority',
    'auto parts management',
    # Hardware & Home Improvement Centers — Home Depot, Lowe's, Menards, Ace Hardware, True Value;
    # enormous garden center plazas + massive parking lots + covered lumber yards;
    # district FMs sign vendor contracts; premium high-value accounts (added 2026-05-29 run 136)
    'home improvement store', 'hardware store chain', 'home center', 'home depot',
    'lowes', "lowe's", 'menards', 'ace hardware', 'true value hardware', 'do it best',
    'building supply store', 'home improvement retail', 'hardware chain',
    # Community Swimming Pools & Aquatic Centers — NE Ohio park district and municipal recreation pools;
    # seasonal outdoor + year-round indoor; pool deck + walkways + parking lots + building exteriors;
    # summer pre-season pitch window (April-May); distinct from YMCA aquatics already targeted (added 2026-05-29 run 136)
    'aquatic center', 'community pool', 'municipal pool', 'swimming pool facility',
    'natatorium', 'public swimming pool', 'recreation aquatic center', 'community aquatics',
    'indoor aquatic center', 'outdoor pool management', 'municipal aquatics',
    # Wireless & Telecom Retail Chains — AT&T, Verizon, T-Mobile, Boost Mobile, Cricket;
    # hundreds of NE Ohio strip-mall storefronts; district managers sign vendor contracts (added 2026-05-29 run 137)
    'wireless retail', 'telecom retail', 'wireless store', 'cell phone retail',
    'mobile retail', 'phone carrier retail', 'wireless carrier store',
    # Uniform & Workwear Services — Cintas, Aramark, UniFirst, G&K Services, ALSCO;
    # large processing/distribution facilities + fleet vehicles; food-service + healthcare client compliance;
    # ironic pitch: "We clean the building of the company that cleans everyone else's workwear" (added 2026-05-29 run 137)
    'uniform services', 'linen services', 'workwear services', 'textile services',
    'uniform laundry', 'industrial laundry', 'garment services', 'cintas',
    'aramark uniform', 'unifirst', 'uniform rental',
    # Warehouse Club & Membership Retail — Apollo does NOT tag Costco/Sam's Club as 'grocery store';
    # they're indexed under 'wholesale retail', 'membership warehouse', 'warehouse club' etc.;
    # Costco (Westlake/Macedonia/Sheffield), Sam's Club (Mayfield Heights/Avon/Brunswick/Stow),
    # BJ's Wholesale Club (2 NE Ohio); enormous 8–15 acre lots + gas station concourses + building exteriors;
    # real segment gap: only caught by 'supermarket chain' (unreliable) — specific keywords fill the gap (added 2026-05-29 run 138)
    'warehouse club', 'membership warehouse', 'wholesale club', 'wholesale retail',
    'membership retail', 'warehouse retail', 'costco', "sam's club", "bj's wholesale",
    'membership store', 'warehouse store',
    # Optical/Vision Centers — LensCrafters, MyEyeDr, Visionworks, Pearle Vision, America's Best, For Eyes, National Vision;
    # strip-mall storefronts; district managers sign vendor contracts; first pull June 8 Cuyahoga (added 2026-05-30 run 139)
    'optical center', 'vision center', 'eyecare center', 'eye care center', 'optometry practice',
    'optical retail', 'vision retail', 'lenscrafters', 'pearle vision', 'visionworks',
    'myeyedr', "america's best eyecare", 'for eyes optical', 'national vision',
    # Medical/Clinical Labs — Quest Diagnostics, LabCorp, Cleveland Clinic outpatient labs, UH diagnostic labs;
    # CLIA federal certification = facility appearance standard; first pull June 8 Cuyahoga (added 2026-05-30 run 139)
    'clinical laboratory', 'medical laboratory', 'diagnostic laboratory', 'patient service center',
    'blood draw center', 'lab testing center', 'quest diagnostics', 'labcorp',
    'laboratory services', 'diagnostic testing center',
    # Tax Preparation Offices — H&R Block, Jackson Hewitt, Liberty Tax; May-September = peak maintenance window;
    # pitch: "Tax season is over — let us clean up"; first pull June 8 Cuyahoga (added 2026-05-30 run 139)
    'tax preparation', 'tax services', 'tax office', 'tax franchise', "h&r block",
    'jackson hewitt', 'liberty tax', 'tax center', 'tax preparation services', 'income tax services',
    # Coffee & Drive-Through Beverage Chains — Starbucks, Dunkin', Panera, Tim Hortons, Dutch Bros, Caribou;
    # drive-through canopies + parking lots + building exteriors; distinct Apollo org tags from QSR;
    # first pull June 8 Cuyahoga (added 2026-05-30 run 140)
    'coffee chain', 'coffee shop chain', 'coffee franchise', 'quick service beverage',
    'drive through beverage', 'starbucks', "dunkin'", 'tim hortons', 'dutch bros',
    'caribou coffee', 'panera bread',
    # Pet Supply Retail Chains — PetSmart, Petco, Pet Supplies Plus; grooming salon runoff stains concrete;
    # DISTINCT from pet boarding/kennel org keywords; first pull June 8 Cuyahoga (added 2026-05-30 run 141)
    'pet supply store', 'pet specialty retail', 'petsmart', 'petco', 'pet supplies plus',
    'pet supply retail', 'pet supplies',
    # Hair & Nail Salon Chains — Great Clips, Sport Clips, Supercuts, Floyd's, Fantastic Sams;
    # chemical spill compliance + high foot traffic; first pull June 8 Cuyahoga (added 2026-05-30 run 141)
    'hair salon chain', 'barbershop chain', 'beauty salon chain', 'salon franchise',
    'great clips', 'sport clips', 'supercuts', 'hair salon management',
    # Coworking Spaces & Flex Offices — IWG/Regus, WeWork, Industrious;
    # large commercial building entry lobbies + parking; premium tenant appearance standard (added 2026-05-30 run 142)
    'coworking space', 'flex office', 'shared workspace', 'coworking', 'executive suite',
    'flexible office', 'serviced office', 'shared office', 'regus', 'iwg', 'wework',
    'industrious office', 'flexible workspace',
    # Truck Stops & Travel Centers — Pilot Flying J, Love's, TA/Petro, Speedway/7-Eleven truck plazas;
    # NE Ohio I-71/I-76/I-77/I-80/I-90 corridor; diesel canopies + truck lots + OEPA SPCC compliance;
    # area managers sign vendor contracts for 3-10 location regional portfolios; first pull June 8 Cuyahoga (added 2026-05-30 run 143)
    'truck stop', 'travel center', 'travel plaza', 'truckstop', 'pilot flying j',
    "love's travel stops", 'ta travel centers', 'petro stopping center',
    'truck fuel stop', 'highway travel center', 'truck plaza',
    # Ambulatory Surgery Centers — Cleveland Clinic Surgery Centers, UH Surgical Centers, Summa Surgery Centers;
    # OBR state license + CMS certification = exterior appearance standard; first pull June 8 Cuyahoga (added 2026-05-30 run 143)
    'ambulatory surgery center', 'outpatient surgery center', 'surgical center',
    'asc management', 'surgery center management', 'outpatient surgical',
    'ambulatory surgical facility', 'outpatient surgical center',
    # Boutique Fitness Studios — Orangetheory, F45, Pure Barre, Club Pilates, CycleBar, Snap Fitness, Anytime Fitness;
    # DISTINCT from Planet Fitness/LA Fitness (already in 'fitness center'/'health club' above);
    # franchise owners sign contracts directly; 200+ NE Ohio studios; first pull June 8 Cuyahoga (added 2026-05-30 run 143)
    'boutique fitness', 'fitness studio', 'orangetheory fitness', 'f45 training',
    'pure barre', 'club pilates', 'cyclebar', 'anytime fitness', 'snap fitness',
    'studio fitness', 'franchise fitness studio', 'group fitness studio',
    # Commercial Truck & Heavy Equipment Dealers — Kenworth, Freightliner, Mack, Peterbilt dealers;
    # Ohio CAT, Thompson Lift Truck, Bobcat dealer, John Deere construction equipment;
    # DISTINCT from passenger car/auto dealers (already in 'car dealership'/'auto dealership' above);
    # service bays + equipment staging lots = heavy diesel/oil staining; first pull June 8 Cuyahoga (added 2026-05-30 run 143)
    'commercial truck dealer', 'heavy equipment dealer', 'truck dealership',
    'equipment dealership', 'kenworth trucks', 'freightliner dealer',
    'mack trucks dealer', 'peterbilt dealer', 'caterpillar dealer',
    'bobcat dealer', 'john deere dealer', 'forklift dealer', 'heavy equipment sales',
    'commercial vehicle dealer', 'equipment dealer network',
    # Wineries & Distilleries — DISTINCT Apollo org tags from 'craft brewery'/'taproom' already above;
    # Ferrante, Debonne, Erie Shore, Cuyahoga Valley Winery + Cleveland Whiskey/Tom's Foolery Distillery;
    # spring patio opening = prime pitch window; outdoor event space = appearance is marketing (added 2026-05-30 run 144)
    'winery', 'vineyard', 'winery management', 'wine production', 'craft distillery',
    'distillery', 'bourbon distillery', 'whiskey distillery', 'spirits production', 'tasting room',
    # Motorcycle & Powersport Dealers — DISTINCT from 'car dealership'/'auto dealership' already above;
    # Harley-Davidson dealers, Honda Powersports, Kawasaki, Yamaha, Polaris, Can-Am, Sea-Doo dealers;
    # service bays + display lots = heavy grease + oil staining; zero competitors (added 2026-05-30 run 144)
    'motorcycle dealer', 'powersport dealer', 'motorcycle dealership', 'powersports dealer',
    'harley davidson dealer', 'kawasaki dealer', 'yamaha dealer', 'honda powersports',
    'motorcycle sales', 'powersport sales',
    # RV & Camper Dealers — DISTINCT from 'car rental'/'car dealership' already above;
    # RV World of Ohio, Camping World, Campers Inn RV, Holiday Motorhomes;
    # enormous paved lots + service bays; spring = peak prep season (added 2026-05-30 run 144)
    'rv dealer', 'rv dealership', 'recreational vehicle dealer', 'camper dealer',
    'motorhome dealer', 'rv sales', 'camping world', 'rv world', 'campers inn',
    'rv rental', 'travel trailer dealer',
    # Garden Centers & Nurseries — Petitti Garden Centers (12+ NE Ohio), Sunrize Garden Center,
    # Rittgers' Greenhouse (Medina), Cornell's Garden Center, Rolling Ridge Nursery;
    # DISTINCT Apollo org tags from landscaping contractors (Carla segment) — retail garden centers;
    # Ohio Dept. of Agriculture nursery licensing = exterior appearance standard;
    # spring patio/display prep = PEAK PITCH WINDOW right now (added 2026-05-30 run 145)
    'garden center', 'plant nursery', 'nursery center', 'garden supply',
    'petitti garden', 'greenhouse nursery', 'landscape nursery', 'garden retail',
    # Marine/Boat Dealers — NE Ohio Lake Erie boating market; Skipper Buds, West End Boat Sales,
    # ComMar Sales (Sandusky), Inland Seas Yachts (Vermilion), Erie Marine, MarineMax;
    # COMPLETELY DISTINCT from marina management (already in 'marina management'/'marine services' above);
    # Apollo tags boat dealers separately under 'boat dealer', 'marine dealer', 'yacht dealer' org tags;
    # first pull: June 15 Lake County (marina corridor — Mentor/Lorain/Vermilion axis) (added 2026-05-30 run 146)
    'boat dealer', 'marine dealer', 'boat dealership', 'yacht dealer', 'marine sales',
    'boat sales', 'powerboat dealer', 'sailboat dealer', 'marine dealership',
    'boat retailer', 'marine retailer', 'skipper buds', 'marine boat dealer',
    # Ice Cream & Frozen Dessert Chains — peak season = NOW; Dairy Queen (40+ NE Ohio), Handel's Ice Cream
    # (Youngstown-based NE Ohio regional chain), Bruster's, Cold Stone Creamery, Rita's Italian Ice;
    # DISTINCT from QSR/restaurant org tags — Apollo tags ice cream chains under separate keywords;
    # walk-up concrete + parking + drive-through lanes stained from peak summer traffic;
    # first pull June 8 Cuyahoga (added 2026-05-30 run 146)
    'ice cream franchise', 'frozen dessert', 'ice cream chain', 'dairy queen',
    "handel's ice cream", 'frozen yogurt franchise', 'soft serve chain',
    'ice cream management', 'dessert franchise', "bruster's ice cream",
    'cold stone creamery', "rita's italian ice", 'frozen custard',
    # Party/Event Rental Companies — A-1 Party Rental (Solon), Taylor Rental Centers (4 NE Ohio locations),
    # Fun Planners, Abbey Rents, Classic Party Rentals; large outdoor storage yards (tents/tables/chairs/linens);
    # DISTINCT from event venues (already targeted) — these are EQUIPMENT SUPPLIERS with storage yard + fleet vehicles;
    # wedding/graduation/corporate event season = May-September = dirtiest equipment + most motivated to spend;
    # OSHA stormwater compliance on storage yard runoff; zero NE Ohio competitors targeting party rental operators;
    # first pull June 8 Cuyahoga (added 2026-05-30 run 147)
    'party rental', 'event rental', 'tent rental', 'party supply', 'event equipment rental',
    'special event rental', 'party supply store', 'wedding rental', 'event equipment',
    # Trampoline Parks & Indoor Adventure Centers — Sky Zone (Beachwood/Mentor/N. Olmsted/Strongsville),
    # Urban Air Adventure Park (Strongsville/Mentor/Stow), Altitude Trampoline, Scene75 Entertainment Center (Berea);
    # DISTINCT from 'family entertainment center'/'bowling center' already above;
    # summer peak season = NOW; large building exteriors + massive parking lots; franchise owners sign directly;
    # zero NE Ohio competitors cold-calling trampoline park franchise owners; first pull June 8 Cuyahoga (added 2026-05-30 run 148)
    'trampoline park', 'sky zone', 'urban air', 'altitude trampoline', 'indoor adventure park',
    'bounce park', 'indoor play center', 'trampoline franchise', 'adventure zone', 'jump zone',
    # Moving & Relocation Companies — Two Men and a Truck (5+ NE Ohio franchises), Gentle Giant Moving,
    # O'Brien's Moving & Storage, Johnson Moving & Storage (Atlas Van Lines agent), Bekins/Mayflower agents;
    # PEAK MOVING SEASON = NOW (May-September); large warehouse/terminal + truck lots accumulate road salt + mud;
    # DISTINCT from fleet washing (Carla targets fleet trucks; Danny targets the FACILITY exterior + parking lot);
    # facility managers sign vendor contracts for building washing, not truck washing;
    # zero NE Ohio competitors cold-calling moving company facility contacts; first pull June 8 Cuyahoga (added 2026-05-30 run 148)
    'moving and storage', 'relocation services', 'two men and a truck', 'van lines',
    'moving services', 'relocation company', 'commercial movers', 'residential movers',
    'moving franchise', 'storage and moving',
    # Off-Price Apparel & Home Goods Retail — TJ Maxx, Marshalls, HomeGoods, Burlington, Ross;
    # DISTINCT from dollar stores + grocery chains (different Apollo org tags for off-price retail segment);
    # high store density in NE Ohio strip malls; district FMs sign multi-site vendor contracts (added 2026-05-30 run 149)
    'tj maxx', 'tjmaxx', 'marshalls', 'homegoods', 'burlington coat factory', 'ross dress for less',
    'off-price retail', 'off price retail', 'discount apparel', 'value retailer',
    # Truck Rental Companies — U-Haul, Penske Truck Rental, Ryder System, Budget Truck Rental;
    # DISTINCT from passenger car rental (uhaul/penske = moving/cargo trucks, not rental cars);
    # large paved lots with trucks + diesel exhaust + road salt; zero competitors cold-calling (added 2026-05-30 run 149)
    'u-haul', 'uhaul', 'penske truck', 'ryder truck', 'budget truck rental',
    'moving truck rental', 'truck rental company',
    # Lumber Yards & Building Supply Distributors — 84 Lumber, ABC Supply Co., Builders FirstSource,
    # Heritage Building Products, ProBuild; DISTINCT from Home Depot/Lowe's (retail) — wholesale contractor-supply;
    # open material yards accumulate forklift oil + concrete dust + wood tannin staining rapidly;
    # first pull June 8 Cuyahoga (84 Lumber Strongsville/Independence/Solon, ABC Supply multiple branches) (added 2026-05-31 run 150)
    'lumber yard', 'building supply distributor', 'roofing supply distributor', 'building materials distributor',
    '84 lumber', 'abc supply', 'builders firstsource', 'probuild', 'roofing supply',
    'building materials supply',
    # Behavioral Health & Mental Health Clinics — Signature Health, Recovery Resources, Frontline Service,
    # LCADA Way, Emerge Behavioral Wellness, Crossroads Health, Harbor Light, UH Behavioral Health, Cleveland Clinic Behavioral;
    # DISTINCT from urgent care + physical therapy + ambulatory surgery centers (all already above);
    # Ohio ODMH/OMHAS licensing + stigma-reduction branding = exterior appearance is a clinical credibility signal;
    # first pull June 8 Cuyahoga (Signature Health has 30+ NE Ohio outpatient sites) (added 2026-05-31 run 150)
    'behavioral health center', 'mental health clinic', 'behavioral health clinic', 'substance abuse treatment',
    'addiction treatment center', 'mental health services', 'outpatient behavioral health',
    'psychiatric clinic', 'counseling center', 'behavioral health management',
    # Motorsports Venues & Racing Facilities — Summit Motorsports Park, Mid-Ohio Sports Car Course,
    # Medina County Speedway, Autobahn Indoor Speedway (Brecksville), K1 Speed, Kart World;
    # DISTINCT from sports complexes/athletic facilities (youth sports, indoor soccer) — different Apollo tags;
    # paved track aprons + parking lots + grandstand concourses = heavy rubber/oil/fuel staining;
    # first pull: June 8 Cuyahoga (Autobahn Indoor Speedway, Brecksville); June 22 Lorain/June 29 Summit
    # for regional speedways (Summit Motorsports Park is Huron County — first pull with county override) (added 2026-05-31 run 151)
    'motorsports park', 'speedway management', 'racetrack facilities', 'motorsports venue',
    'racing facility', 'karting center', 'indoor karting', 'motorsports complex',
    # Print & Business Services Chains — FedEx Office, UPS Store (50+ NE Ohio franchise owners),
    # AlphaGraphics, Minuteman Press, Sir Speedy, Allegra Marketing Print Mail;
    # DISTINCT from distribution centers (shipping facilities) — strip-mall storefronts, not warehouses;
    # Apollo tags: 'printing services', 'shipping services', 'business services center';
    # franchise owners sign vendor contracts directly for 1-3 store territories;
    # first pull: June 8 Cuyahoga (all major FedEx Office + UPS Store locations in Cuyahoga County) (added 2026-05-31 run 151)
    'printing services', 'business services center', 'print shop', 'shipping center',
    'copy center', 'ups store franchise', 'business print services', 'print and ship',
    # Chiropractic Chains & Spinal Care Groups — DISTINCT from physical therapy/urgent care already above;
    # The Joint Chiropractic franchise + ChiroOne + independent multi-location practices;
    # Ohio State Chiropractic Board licensing = exterior appearance standard;
    # first pull June 8 Cuyahoga (The Joint Chiropractic has 3+ Cuyahoga County locations) (added 2026-05-31 run 152)
    'chiropractic clinic', 'chiropractic center', 'chiropractor group',
    'the joint chiropractic', 'chiroone', 'chiropractic franchise',
    'spinal care center', 'spine clinic', 'chiropractic management',
    # Escape Rooms & Interactive Entertainment Venues — Breakout Games (franchise), room2escape, Paranormal Escape,
    # Scene 75 Entertainment Center (Berea — 100K+ sq ft indoor venue), Cleveland Escape, Puzzled Escape Games;
    # DISTINCT from trampoline parks ('trampoline park' tag above) + bowling ('bowling' tag above);
    # peak evening/weekend traffic + corporate team-building events = heavy staining + high appearance stakes;
    # first pull June 8 Cuyahoga (Scene 75 Berea, Breakout Games Strongsville + Independence) (added 2026-05-31 run 152)
    'escape room', 'escape game', 'escape experience', 'room escape',
    'breakout games', 'interactive entertainment venue', 'immersive experience venue',
    'escape room franchise', 'puzzle room', 'entertainment escape',
    # Charter Schools & Charter Management Organizations — 'charter school' is a DISTINCT Apollo org tag
    # from 'private school' + 'school district' already in list; NE Ohio has 100+ charter campuses;
    # CMO: charter management organization signs multi-campus vendor contracts;
    # Ohio charter authorizer facility compliance inspections = exterior appearance = procurement driver;
    # first pull: June 8 Cuyahoga (Cleveland has highest charter school density in Ohio — 50+ campuses) (added 2026-05-31 run 154)
    'charter school', 'charter academy', 'charter management organization', 'charter management',
    # Outdoor RV & Boat Storage Facilities — DISTINCT from 'marina management'/'boat storage' (marina/wet-slip tag above)
    # and 'self storage'/'self-storage' (indoor climate-controlled units); standalone outdoor yards for boats/RVs/travel trailers;
    # NE Ohio Lake Erie corridor (Lake/Lorain/Erie county lines) has dense concentration of these facilities;
    # spring commissioning = peak pitch window RIGHT NOW; large concrete/gravel pads = high-revenue per visit;
    # first pull: June 8 Cuyahoga; June 15 Lake (marina corridor); June 22 Lorain (Avon/Avon Lake shoreline) (added 2026-05-31 run 154)
    'rv storage', 'outdoor rv storage', 'boat and rv storage', 'marine dry storage',
    'outdoor vehicle storage', 'outdoor storage facility', 'rv resort storage',
    # Ice Rinks & Indoor Ice Arenas — DISTINCT from 'sports complex'/'youth sports complex' already above;
    # Apollo indexes dedicated ice skating and hockey facilities under 'ice rink'/'ice arena'/'hockey rink'
    # org keywords which return zero overlap with 'sports complex' tag searches;
    # NE Ohio: Palace Ice Arenas (Solon + Twinsburg), Mentor Ice Arena, OBM Arena (Parma),
    # Brooklyn Ice Center, Westlake Rec Center ice rink, Kent State University ice rink,
    # multiple independent and municipally-operated ice rinks in Summit/Cuyahoga/Lake counties;
    # summer (June-August) = ice out or minimal usage = PEAK MAINTENANCE WINDOW; facility GM/director
    # is planning exterior cleaning right now; zero NE Ohio competitors targeting this segment;
    # first pull: June 8 Cuyahoga; June 15 Lake County; June 29 Summit County (2nd pass) (added 2026-05-31 run 155)
    'ice rink', 'ice arena', 'ice skating rink', 'hockey rink', 'skating facility',
    'ice sports complex', 'ice skating center', 'hockey arena',
    # Sporting Goods Chains — Dick's Sporting Goods, Academy Sports, Play It Again Sports, DICK'S;
    # DISTINCT from 'sports complex'/'athletic complex'/'ymca' already above — retail stores, not facilities;
    # Apollo org tags: 'sporting goods', 'sporting goods store', 'sports retail', 'sporting goods retail';
    # first pull: June 8 Cuyahoga (Dick's anchors Great Northern, SouthPark, Macedonia + Belden Village, Macedonia) (added 2026-05-31 run 156)
    'sporting goods', 'sporting goods store', 'sporting goods retail', 'sports retail',
    "dick's sporting goods", 'academy sports', 'play it again sports', 'sporting goods chain',
    'athletic retail', 'sports equipment retail',
    # Tractor Supply Co. & Farm/Rural Supply Chains — DISTINCT from ALL existing segments;
    # NE Ohio rural-suburban interface: Medina (Wadsworth/Medina city), Lorain (Grafton/Oberlin), Summit (Tallmadge),
    # Geauga (Chardon), Portage (Ravenna) — 20+ Tractor Supply locations; 4 Rural King in NE Ohio;
    # Apollo org tags: 'tractor supply', 'farm supply', 'rural supply', 'farm and ranch supply';
    # first pull: June 8 Cuyahoga (Tractor Supply Strongsville, Brook Park/Berea area); June 15 Medina-area pass (added 2026-05-31 run 156)
    'tractor supply', 'farm supply store', 'rural supply store', 'farm and ranch supply',
    'rural king', 'farm supply chain', 'agway', 'agricultural supply retail',
    # Used Car Superstores & Independent Used Car Lots — DISTINCT from franchise car dealers
    # ('car dealer' ≠ 'used car dealer' in Apollo org tag space);
    # CarMax (Willoughby Hills, Mayfield Heights), DriveTime, AutoNation Pre-Owned, independent lots;
    # Apollo org tags: 'used car dealer', 'used car lot', 'pre-owned vehicles', 'pre-owned car dealer';
    # first pull: June 8 Cuyahoga (CarMax Willoughby Hills is the highest-volume NE Ohio used car site) (added 2026-05-31 run 157)
    'used car dealer', 'used car lot', 'pre-owned vehicles', 'used car dealership',
    'carmax', 'drivetime', 'used car sales', 'independent auto dealer',
    'buy here pay here', 'used auto sales',
    # Outdoor Power Equipment Dealers — STIHL dealer network (50+ NE Ohio shops), Husqvarna dealers,
    # Cub Cadet dealers, Northern Tool + Equipment (3 NE Ohio locations);
    # Apollo org tags: 'power equipment dealer', 'outdoor power equipment', 'small engine dealer';
    # first pull: June 8 Cuyahoga; June 22 Lorain (Avon corridor has strong lawn equipment dealer density) (added 2026-05-31 run 157)
    'power equipment dealer', 'outdoor power equipment', 'stihl dealer', 'husqvarna dealer',
    'cub cadet dealer', 'lawn equipment dealer', 'small engine dealer', 'outdoor equipment dealer',
    # Vocational & Trade Schools / Career Technical Education Centers — EHOVE, Auburn Career Center,
    # CVCC (Cuyahoga Valley Career Center), Portage Lakes Career Center, Mahoning County CTC;
    # Apollo org tags: 'vocational school', 'trade school', 'career technical center';
    # DISTINCT from 'school district' (K-12), 'private school', 'charter school' (all separate Apollo org tags);
    # summer = buildings less occupied = ideal exterior wash window = decision window NOW;
    # first pull: June 8 Cuyahoga (CVCC, Ohio Technical College, Tri-C Workforce) (added 2026-05-31 run 157)
    'vocational school', 'trade school', 'career technical center', 'cte school',
    'career center', 'technical education center', 'career technical education',
    'vocational education center',
    # Animal Shelters & Humane Societies — Cleveland APL, Summit County APL, Geauga Humane Society,
    # Lake County APL, Lorain County APL, Portage County APL, Mahoning County Humane Society;
    # Ohio ORC 955.16 shelter licensing = exterior cleanliness standard; outdoor kennels + concrete runs
    # + building exteriors accumulate biological residue at extreme rates;
    # DISTINCT from 'pet boarding'/'dog kennel'/'pet hotel' (commercial boarders) and 'veterinary clinic'
    # (medical care) — animal shelters are non-profit/government with separate Apollo org tags;
    # zero competitors targeting humane society directors for power washing in NE Ohio;
    # first pull: June 8 Cuyahoga (Cleveland APL Tremont campus + satellite adoption centers) (added 2026-05-31 run 158)
    'animal shelter', 'humane society', 'animal protection league', 'animal control services',
    'spca', 'animal rescue', 'dog rescue', 'animal adoption center', 'pet adoption center',
    'animal welfare organization', 'animal control facility',
    # Campgrounds & RV Parks — Ohio State Parks (Punderson, West Branch, Findley, Nelson Ledges,
    # Buck Creek), KOA Campgrounds (Sandusky, Streetsboro/Cleveland SE, Lake Erie Basin),
    # Yogi Bear's Jellystone Park, Cherry Hill Village (Canton area), private camping resorts;
    # spring opening = RIGHT NOW; concrete dump station pads + bathhouse exteriors + rec halls;
    # DISTINCT from 'rv dealer' (retail), 'rv storage' (outdoor storage), 'marina management' (wet slips);
    # Apollo org tags: 'campground', 'rv park', 'camping resort' return zero overlap with those segments;
    # zero NE Ohio power washing competitors targeting campground managers; first pull June 8 Cuyahoga (added 2026-05-31 run 158)
    'campground', 'rv park', 'camping resort', 'campground management', 'rv campground',
    'camping facility', 'state park campground', 'koa campground', 'jellystone park',
    'campground resort', 'camping park', 'outdoor recreation park',
    # Mobile Home Parks & Manufactured Housing Communities — 200+ NE Ohio communities;
    # Sun Communities (largest US MH REIT), Equity LifeStyle Properties (ELS), UDR —
    # national operators with multi-community NE Ohio portfolios;
    # DISTINCT from 'apartment management'/'multifamily' (different Apollo org tags);
    # large internal streets + community centers + laundry buildings + entrance areas;
    # community managers sign vendor contracts; zero competitors targeting MH park FMs in NE Ohio;
    # first pull: June 8 Cuyahoga (North Olmsted Estates, Valley Mobile Home Park) (added 2026-05-31 run 158)
    'mobile home park', 'manufactured housing community', 'manufactured home park',
    'mobile home community', 'manufactured housing', 'mobile home management',
    'manufactured community', 'mobile home village', 'mobile home estates',
    # Senior Adult Day Programs & Adult Day Care Centers — Ohio Dept of Aging licensed;
    # DISTINCT from 'senior living'/'assisted living' (residential — already in list);
    # Apollo org tags: 'adult day program', 'adult day services', 'adult day care' return zero overlap;
    # 60+ NE Ohio programs serving medically fragile seniors; wheelchair ramp concrete + entrance areas + van drop-off pads;
    # first pull June 8 Cuyahoga (Family Connections Adult Day Program, ParkView, ElderCare Alliance) (added 2026-05-31 run 159)
    'adult day program', 'adult day services', 'adult day care', 'adult day health',
    'senior day program', 'adult daycare', 'senior day services', 'day program for seniors',
    # Diagnostic Imaging & Radiology Centers — DISTINCT from 'medical office', 'urgent care', 'hospital';
    # Apollo org tags: 'diagnostic imaging', 'radiology center' return zero overlap with those segments;
    # stand-alone imaging centers with dedicated large accessible parking lots;
    # first pull June 8 Cuyahoga (HealthSpan Radiology — Beachwood/Mayfield Hts/Westlake, UH Radiology) (added 2026-05-31 run 159)
    'diagnostic imaging', 'radiology center', 'imaging center', 'mri center',
    'radiology clinic', 'imaging clinic', 'x-ray center', 'medical imaging center',
    # Swim Schools & Aquatic Learn-to-Swim Programs — DISTINCT from 'ymca', 'aquatic center', 'community pool';
    # Apollo org tags: 'swim school', 'swim academy', 'aquatic learning' return zero overlap;
    # franchise-owned; summer = peak season; first pull June 8 Cuyahoga
    # (Goldfish Swim School Strongsville/North Olmsted, British Swim School NE Ohio locations) (added 2026-05-31 run 159)
    'swim school', 'swim academy', 'swimming school', 'learn to swim', 'aquatic learning',
    'swimming lessons', 'swim studio', 'children swim school',
    # Massage Therapy & Wellness Chains — DISTINCT from 'hair salon chain'/'salon franchise' already above;
    # Apollo org tags: 'massage therapy', 'massage center', 'massage franchise' return zero overlap with salon tags;
    # Massage Envy (30+ NE Ohio), Elements Massage (8+ NE Ohio), Hand & Stone, LaVida;
    # first pull June 8 Cuyahoga (Massage Envy Strongsville/Mentor/Westlake + Elements Massage Beachwood/Solon) (added 2026-05-31 run 160)
    'massage therapy', 'massage center', 'massage franchise', 'wellness studio',
    'massage clinic', 'therapeutic massage', 'massage chain', 'massage envy',
    # Non-Profit & Social Service Organizations — Salvation Army NE Ohio, Catholic Charities Diocese of Cleveland,
    # United Way of Greater Cleveland, Volunteers of America, Second Harvest Food Bank, Habitat for Humanity ReStore,
    # Lutheran Metropolitan Ministry, Jewish Family Service Association;
    # DISTINCT Apollo org tags: 'nonprofit organization', 'social services', 'food bank', 'thrift store'
    # return zero overlap with ANY existing DANNY_ORG_KEYWORDS above;
    # large facility footprints (thrift store warehouses, food bank complexes, service center buildings);
    # donor-trust appearance standard = genuine external cleaning urgency; first pull June 8 Cuyahoga (added 2026-05-31 run 160)
    'nonprofit organization', 'social services organization', 'charitable organization',
    'community service organization', 'food bank', 'thrift store', 'salvation army',
    'human services organization', 'community outreach organization',
    # Auto Glass Repair & Windshield Replacement Chains — DISTINCT from car dealerships, auto body shops, car wash;
    # Apollo tags 'auto glass', 'auto glass repair', 'windshield replacement' return zero overlap with existing segments;
    # Glass America (Cleveland HQ), Safelite AutoGlass, Auto Glass Now, O'Brien Auto Glass;
    # first pull June 8 Cuyahoga (Glass America Carnegie Ave HQ + Safelite Strongsville/Parma/Mentor) (added 2026-05-31 run 161)
    'auto glass', 'auto glass repair', 'windshield replacement', 'glass repair center',
    'auto glass service', 'windshield repair', 'auto glass shop', 'glass america',
    # Furniture & Home Furnishings Retail Chains — DISTINCT from hardware/home improvement (run 136) + warehouse clubs;
    # Apollo tags 'furniture store', 'furniture retail', 'home furnishings' return zero overlap with existing segments;
    # Ashley Furniture, Value City Furniture, Bob's Discount Furniture, Big Sandy Superstore, Nationwide Furniture;
    # first pull June 8 Cuyahoga (Ashley Solon/Mentor, Value City Mayfield/Parma/Berea) (added 2026-05-31 run 161)
    'furniture store', 'furniture retail', 'home furnishings store', 'furniture showroom',
    'home furnishings', 'furniture outlet', 'furniture gallery', 'home furniture store',
    # Salon Suites & Booth Rental Studios — DISTINCT from hair/nail salon chains (run 141, 'hair salon chain' Apollo tag);
    # Apollo tags 'salon suite', 'salon suites', 'booth rental salon' return zero overlap with any existing segment;
    # Sola Salon Studios, MY SALON Suite, Phenix Salon Suites, Salon Lofts;
    # first pull June 8 Cuyahoga (Sola Salon Studios Independence/Beachwood/Westlake) (added 2026-05-31 run 161)
    'salon suite', 'salon suites', 'booth rental salon', 'salon studios',
    'sola salon', 'phenix salon', 'my salon suite', 'salon lofts',
    # Tutoring Centers & Learning Centers — Kumon, Sylvan Learning, Mathnasium, Huntington Learning Center;
    # DISTINCT from private schools, charter schools, vocational schools (different Apollo org tags);
    # Apollo tags 'tutoring center', 'learning center', 'academic tutoring' return zero overlap with existing segments;
    # first pull June 8 Cuyahoga (Kumon Beachwood/Pepper Pike/Westlake, Sylvan Strongsville/Solon) (added 2026-06-01 run 162)
    'tutoring center', 'learning center', 'academic tutoring', 'after school tutoring',
    'kumon center', 'mathnasium', 'sylvan learning', 'huntington learning',
    # Med Spas & Aesthetic Clinics — European Wax Center, LaserAway, National Laser Institute, Clearwave Health;
    # DISTINCT from massage therapy chains (run 160), hair salons (run 141), boutique fitness (run 143);
    # Apollo tags 'medical spa', 'med spa', 'aesthetic clinic' return zero overlap with existing segments;
    # first pull June 8 Cuyahoga (European Wax Center Beachwood/Westlake/Strongsville locations) (added 2026-06-01 run 162)
    'medical spa', 'med spa', 'medspa', 'aesthetic clinic', 'aesthetics clinic',
    'laser clinic', 'cosmetic clinic', 'european wax center', 'laser aesthetics',
    # Dry Cleaning & Laundry Service Chains — Fox Cleaners (30+ NE Ohio), Martinizing, One Hour Cleaners;
    # DISTINCT from coin laundries/laundromats (run 135 — 'coin laundry' tag, self-service, zero overlap);
    # Apollo tags 'dry cleaning', 'dry cleaner', 'laundry service' are unused in existing DANNY_ORG_KEYWORDS;
    # first pull June 8 Cuyahoga (Fox Cleaners corporate HQ contact, Martinizing franchise owners) (added 2026-06-01 run 162)
    'dry cleaning', 'dry cleaner', 'dry cleaning chain', 'laundry service',
    'garment care', 'dry cleaning franchise', 'martinizing', 'fox cleaners',
    # Home Care Agencies — Visiting Angels, Home Instead, Comfort Keepers, Bayada, Kindred at Home;
    # ODJFS licensing; DISTINCT from senior living (run 96 — 'assisted living', 'senior living' tags);
    # Apollo tags 'home care agency', 'in-home care' return zero overlap with existing segments;
    # first pull June 8 Cuyahoga (added 2026-06-01 run 163)
    'home care agency', 'in-home care', 'home health care', 'visiting angels', 'home instead',
    'comfort keepers', 'senior home care', 'elder care services', 'home health agency',
    # Pawn Shops & Cash Advance Chains — Cashland (EZCorp), Advance America, ACE Cash Express;
    # DISTINCT from banks (run 100), dollar stores (run 136) — different Apollo industry tags;
    # Apollo tags 'pawn shop', 'cash advance', 'payday loan' return zero overlap with existing segments;
    # first pull June 8 Cuyahoga (Cashland NE Ohio, Advance America Parma/Strongsville/Mentor) (added 2026-06-01 run 163)
    'pawn shop', 'cash advance', 'payday loan', 'check cashing', 'cashland', 'ezcorp',
    'advance america', 'ace cash express',
    # Hearing Aid Centers & Audiology Clinics — HearingLife, Miracle-Ear, Beltone, Connect Hearing;
    # DISTINCT from optical centers (run 139 — 'optometry', 'vision center' tags), medical offices (run 101);
    # Apollo tags 'hearing aid center', 'audiology clinic', 'hearing center' return zero overlap;
    # first pull June 8 Cuyahoga (HearingLife Beachwood/Parma/Strongsville, Miracle-Ear NE Ohio) (added 2026-06-01 run 163)
    'hearing aid center', 'audiology clinic', 'hearing center', 'hearing health',
    'hearinglife', 'miracle-ear', 'beltone', 'hearing care',
    # Staffing & Temporary Employment Agencies — Robert Half, Manpower, Kelly Services, Adecco, Randstad,
    # Aerotek/Allegis Group (large Cleveland industrial/tech staffing hub), Integrity Staffing Solutions;
    # DISTINCT from manufacturing/industrial (run 118), distribution centers (run 105), corporate parks (run 101);
    # staffing agency branch offices have parking lots + building exteriors needing periodic maintenance;
    # 50+ staffing branches across NE Ohio 7-county area; May-June = peak industrial hiring surge (added 2026-06-01 run 164)
    'staffing agency', 'temporary staffing', 'employment agency', 'temp agency',
    'workforce solutions', 'staffing solutions', 'temp staffing', 'staffing firm',
    'robert half', 'manpower', 'kelly services', 'adecco', 'randstad', 'aerotek',
    # Big Box Electronics Retail — Best Buy (10+ large-format NE Ohio stores), Micro Center (Westgate Cleveland);
    # DISTINCT from wireless/telecom retail (run 137 — kiosks), hardware/home improvement (run 136);
    # enormous parking lots (5-10 acres) + building exteriors + seasonal outdoor display areas;
    # district managers sign vendor contracts for 5-8 store territories; first pull June 8 Cuyahoga (added 2026-06-01 run 164)
    'electronics retail', 'consumer electronics retail', 'electronics store', 'best buy',
    'micro center', 'big box electronics', 'electronics chain', 'consumer electronics store',
    # Rent-to-Own / Consumer Lease Chains — Rent-A-Center (25+ NE Ohio), Aaron's Holdings (15+ NE Ohio);
    # DISTINCT from pawn shops (run 163 — buy/sell model), dollar stores (run 136 — outright purchase);
    # high daily foot traffic (weekly payment collection days = traffic spike); strip-mall storefronts;
    # district managers sign multi-location vendor contracts; first pull June 8 Cuyahoga (added 2026-06-01 run 164)
    'rent to own', 'rent-to-own', 'consumer lease', 'furniture rental store',
    'appliance rental store', 'aarons', 'rent-a-center', 'rentacenter', 'consumer rental',
    'rent to own chain', 'lease to own',
    # Insurance Agency Offices — State Farm, Allstate, Erie Insurance, Nationwide, Farmers, AAA;
    # DISTINCT from banks (run 100), corporate parks (run 101) — completely different Apollo org tags;
    # 500+ independent franchise agency offices across NE Ohio 7 counties; client-facing storefronts;
    # agency owners sign vendor contracts independently; first pull June 8 Cuyahoga (added 2026-06-01 run 165)
    'insurance agency', 'independent insurance', 'insurance office', 'state farm',
    'allstate insurance', 'erie insurance', 'nationwide insurance', 'farmers insurance',
    'insurance franchise',
    # Orthopedic & Sports Medicine Clinics — DISTINCT from 'medical office', 'outpatient facility',
    # 'diagnostic imaging', 'urgent care'; Apollo org tags 'orthopedic clinic', 'sports medicine'
    # return zero overlap with any existing DANNY_ORG_KEYWORDS;
    # first pull June 8 Cuyahoga (OrthoNEOA Beachwood/Strongsville offices, UH Ortho Westlake) (added 2026-06-01 run 166)
    'orthopedic clinic', 'orthopedic surgery', 'sports medicine', 'orthopedic group',
    'orthopaedic clinic', 'orthopedic associates', 'orthopedic center', 'sports medicine clinic',
    # Financial Advisory & Wealth Management Offices — DISTINCT from 'insurance agency', 'bank branch';
    # Apollo tags 'financial advisory', 'wealth management', 'edward jones', 'ameriprise',
    # 'raymond james' return zero overlap with any existing DANNY_ORG_KEYWORDS;
    # first pull June 8 Cuyahoga (Edward Jones offices, Ameriprise advisors in Cuyahoga County) (added 2026-06-01 run 166)
    'financial advisory', 'wealth management', 'financial planning office', 'investment advisory',
    'edward jones', 'raymond james', 'ameriprise', 'northwestern mutual financial',
    'financial services office',
    # Waste Hauling & Dumpster Rental Companies — Republic Services, Rumpke, Kimble Companies, GFL/Advanced
    # Disposal, Waste Management Inc.; OEPA NPDES stormwater compliance = pressure washing the staging yard is a
    # regulatory requirement; Apollo org tags 'waste management company', 'waste hauling', 'dumpster rental',
    # 'solid waste management' return ZERO overlap with any existing DANNY_ORG_KEYWORDS;
    # first pull June 8 Cuyahoga (Republic Services Strongsville district HQ + Kimble NE Ohio facilities)
    # (added 2026-06-01 run 167)
    'waste management company', 'waste hauling', 'dumpster rental', 'trash hauling',
    'solid waste management', 'garbage collection', 'refuse collection', 'recycling company',
    'waste collection service', 'rubbish removal', 'republic services', 'rumpke',
    'kimble companies', 'waste management inc',
    # Dermatology & Skin Care Medical Groups — SkinCure Oncology, Cleveland Dermatology Associates,
    # Mahler Dermatology, Bahl & Bahl, Advanced Dermatology & Cosmetic Surgery, US Dermatology Partners;
    # DISTINCT from run 101 (general medical offices), run 162 (med spas — cosmetic non-clinical),
    # run 166 (orthopedic), run 114 (urgent care); Apollo org tags 'dermatology clinic', 'dermatology practice',
    # 'skin care clinic', 'skin care center' return ZERO overlap with existing segments;
    # first pull June 8 Cuyahoga (SkinCure Oncology Beachwood/Strongsville, Cleveland Derm Associates Westlake)
    # (added 2026-06-01 run 167)
    'dermatology clinic', 'dermatology practice', 'dermatology group', 'skin care clinic',
    'skin care center', 'dermatology associates', 'medical dermatology', 'clinical dermatology',
    'dermatology center', 'skincure oncology', 'dermatology management',
    # Hospice & Palliative Care Facilities — Hospice of the Western Reserve (Westlake HQ, 5 NE Ohio inpatient
    # facilities), Amedisys Hospice, VITAS Healthcare, Ohio's Hospice, CrossCountry Hospice;
    # DISTINCT from run 163 (home care agencies), run 96 (senior living), run 150 (behavioral health);
    # Ohio DOH hospice licensing + CMS CoP = exterior appearance standard; appearance = mission-critical dignity
    # signal for families at the most emotional moment; Apollo org tags 'hospice care', 'palliative care',
    # 'inpatient hospice' return ZERO overlap with any existing segments;
    # first pull June 8 Cuyahoga (Hospice of Western Reserve Cleveland residential facility + Amedisys NE Ohio)
    # (added 2026-06-01 run 167)
    'hospice care', 'palliative care', 'inpatient hospice', 'hospice facility',
    'hospice center', 'hospice services', 'end of life care', 'comfort care',
    'hospice of the western reserve', 'amedisys hospice', 'vitas healthcare',
    # Community Colleges & Technical Institutes — Cuyahoga Community College (Unified/Western/Eastern/Metro),
    # Lakeland Community College, Lorain County CC, Stark State College, Sinclair CC NE Ohio, Ohio State ATI;
    # DISTINCT from K-12 vocational schools (run 157 — 'career technical', 'vocational school' Apollo tags),
    # main universities (not yet targeted); summer = academic maintenance window = peak exterior cleaning window;
    # campus facilities director signs contracts covering multiple buildings in a single deal;
    # first pull June 8 Cuyahoga (Tri-C Metro/Western/Eastern all in Cuyahoga County) (added 2026-06-01 run 168)
    'community college', 'community college campus', 'technical college',
    'junior college', 'college district', 'two year college',
    'community college facilities', 'community college district',
    # Medical Equipment & Device Manufacturers — Invacare Corporation (Elyria HQ), Steris Corporation (Mentor HQ),
    # Nordson Corporation (Westlake HQ), Swagelok Company (Solon), Materion Corporation (Mayfield Heights),
    # Natus Medical (Middleburg Heights); DISTINCT from medical offices (run 101 — patient-facing outpatient),
    # distribution centers (run 105 — logistics), general manufacturing (run 118 — non-FDA regulated);
    # FDA GMP 21 CFR Part 820 Quality System Regulation + ISO 13485 certification = exterior cleanliness standard;
    # first pull June 8 Cuyahoga (Steris Corporation Mentor/global HQ + Nordson Westlake HQ) (added 2026-06-01 run 168)
    'medical device manufacturer', 'medical device company', 'medical equipment manufacturer',
    'medical equipment company', 'biomedical company', 'medical technology company',
    'surgical instrument manufacturer', 'medical instrument manufacturer', 'medical device',
    # Pain Management & Spine Clinics — Cleveland Clinic Pain Management, UH Pain Clinic, Summa Health Pain
    # Management, National Spine & Pain Centers NE Ohio; DISTINCT from orthopedic (run 166 — 'orthopedic clinic'),
    # chiropractic (run 152 — 'chiropractic'), PT (run 126 — 'physical therapy'), urgent care (run 114);
    # MD/DO interventional procedures; Ohio Medical Board + DEA registration = facility licensing;
    # chronic patients visit weekly = highest foot traffic of any specialty clinic type;
    # first pull June 8 Cuyahoga (CC Pain Mgmt Beachwood + National Spine NE Ohio) (added 2026-06-01 run 168)
    'pain management clinic', 'pain management center', 'pain clinic',
    'interventional pain', 'chronic pain management', 'pain treatment center',
    'pain medicine clinic', 'spine and pain', 'pain management practice',
    # Skilled Nursing Facilities & Long-Term Care Centers — DISTINCT from senior/assisted living (run 96),
    # hospice (run 167), adult day care (run 159); Apollo org tags return ZERO overlap with existing segments;
    # CMS Five-Star Quality Rating System compliance = exterior appearance directly tied to Medicare/Medicaid revenue;
    # first pull June 8 Cuyahoga (ProMedica Senior Care Cuyahoga County SNF facilities) (added 2026-06-01 run 169)
    'skilled nursing facility', 'nursing home', 'long-term care facility',
    'rehabilitative care', 'post-acute care', 'sub-acute rehabilitation',
    'skilled nursing care', 'long term care',
    # Orthodontic Practices & Pediatric Dental Groups — DISTINCT from general DSO dentistry (run 123);
    # Apollo org tags 'orthodontic practice', 'orthodontics', 'pediatric dentistry' return ZERO overlap with
    # 'dental group', 'dental service organization' from run 123; monthly adjustment visits = max staining rate;
    # first pull June 8 Cuyahoga (Smile Doctors NE Ohio + Ortho Studios Strongsville) (added 2026-06-01 run 169)
    'orthodontic practice', 'orthodontics', 'pediatric dentistry',
    'pediatric dental', 'orthodontic group', 'orthodontic center',
    'braces center', 'pediatric dental group',
    # County Fairgrounds & Agricultural Exhibition Facilities — 7 NE Ohio county fairgrounds;
    # June/July pre-fair = perfect pitch window; ODA/county fair board inspection = appearance standard;
    # DISTINCT from convention centers (run 128 — I-X Center, convention halls) which are year-round commercial venues;
    # Apollo org tags 'county fairgrounds', 'county fair', 'agricultural fair' return zero overlap with existing keywords
    # (added 2026-06-01 run 170)
    'county fairgrounds', 'county fair', 'agricultural fair', 'fairgrounds',
    'exhibition grounds', 'fair grounds', 'agricultural exhibition',
    # Title Companies & Real Estate Closing Offices — Stewart Title, Chicago Title, First American,
    # Fidelity National Title, Ohio Title Agency, Buckeye Title, WFG National Title;
    # DISTINCT from realtors (realtor sequence) and financial advisors (run 166);
    # 'title insurance', 'title company', 'real estate closing' return zero overlap with existing DANNY_ORG_KEYWORDS;
    # June = peak real estate closing season = peak pitch window RIGHT NOW (added 2026-06-01 run 170)
    'title company', 'title insurance', 'title agency', 'real estate closing',
    'settlement services', 'closing services', 'title search', 'property title',
    # Fire Stations & Fire Departments — dedicated Apollo org tag; DISTINCT from 'municipal facilities' (run 124);
    # fire departments have separate district budgets and are tagged by Apollo under 'fire department'/'fire district';
    # NE Ohio: Cleveland Fire (26 stations), Parma Fire (6), Lakewood Fire (5), 100+ township/suburban fire depts;
    # one department FM = contract covering all stations in that department (added 2026-06-01 run 171)
    'fire department', 'fire station', 'fire district', 'fire rescue', 'fire protection district',
    'municipal fire department', 'volunteer fire department',
    # Home Builders & Residential Real Estate Developers — DISTINCT from existing real estate management keywords;
    # 'home builder', 'residential developer', 'new home construction' catch builder orgs Apollo tags distinctly from
    # 'property management' / 'real estate management' (which catch existing-property PMs, not new construction);
    # June = peak NE Ohio new construction showing season (added 2026-06-01 run 171)
    'home builder', 'residential developer', 'new home construction', 'home development',
    'housing development', 'real estate development', 'new home community', 'home construction',
    # Propane & Fuel Oil Delivery Companies — DISTINCT from gas stations (retail/consumer facing);
    # Apollo tags 'propane delivery', 'fuel oil delivery', 'heating oil' catch wholesale delivery operations;
    # AmeriGas, Ferrellgas, Suburban Propane, National Fuel Gas, independent NE Ohio heating oil dealers (added 2026-06-01 run 171)
    'propane delivery', 'fuel oil delivery', 'heating oil delivery', 'propane company',
    'fuel oil company', 'propane distribution', 'heating fuel delivery', 'propane service',
    # Dance Studios & Performing Arts Schools — Apollo 'dance studio' / 'performing arts school' tags
    # catch Arthur Murray, Fred Astaire, competition studios, dance conservatories distinctly from fitness chains
    # (which are caught by 'fitness center'/'health club') (added 2026-06-01 run 172)
    'dance studio', 'performing arts school', 'dance academy', 'dance school',
    'performing arts studio', 'arthur murray', 'fred astaire dance', 'dance conservatory',
    # Martial Arts Academies — Apollo 'martial arts'/'karate'/'taekwondo' tags catch dojos/academies distinctly
    # from sports complexes ('sports complex' tag — run 125). ATA, Tiger Rock, Carlson Gracie, Gracie Barra (added 2026-06-01 run 172)
    'martial arts', 'karate school', 'karate academy', 'taekwondo', 'jiu-jitsu',
    'bjj gym', 'martial arts academy', 'combat sports', 'krav maga',
    # Wedding Venues & Special Occasion Facilities — 'wedding venue' (run 108) catches general wedding-hosting
    # venues; these tags catch DEDICATED bridal/wedding estates that exist solely for weddings;
    # DISTINCT from 'banquet hall', 'event venue', 'event center' (already in list — run 108);
    # Barn at Mapleside, Willow Tree Ranch, wedding barns/chapels throughout NE Ohio counties;
    # first pull June 8 Cuyahoga (metro venues); June 22 Lorain (Avon/Westlake area barns) (added 2026-06-02 run 173)
    'bridal venue', 'wedding estate', 'wedding barn', 'wedding chapel',
    'wedding garden', 'bridal hall', 'wedding manor', 'outdoor wedding venue',
    # Outdoor Recreation & Adventure Parks — mini-golf, go-karts, batting cages, axe throwing;
    # 'outdoor recreation park' (run 158, campground section) is already in list but targets state parks;
    # these specific tags catch stand-alone family entertainment venues distinctly from parks/campgrounds;
    # All-American Fun Park (Chardon), Berea Golf Dome, Zone Sports locations, axe throwing venues opening in NE Ohio;
    # June = school's out = peak; first pull June 8 Cuyahoga (metro venues) (added 2026-06-02 run 173)
    'mini golf', 'miniature golf', 'go-kart', 'go kart track', 'batting cage',
    'axe throwing', 'outdoor family entertainment', 'family fun park', 'outdoor adventure park',
    # Charter Fishing & Lake Erie Boat Tour Operators — Apollo org tags catch independent charter operations
    # distinctly from marinas ('marina management', 'marine services', 'boat storage' — run 109);
    # walleye season June-August = peak pitch window RIGHT NOW; NE Ohio Lake Erie shoreline advantage (added 2026-06-02 run 174)
    'charter fishing', 'fishing charter', 'lake erie charter', 'charter boat',
    'boat charter', 'fishing guide', 'lake fishing charter', 'walleye charter',
    # VFW Posts & American Legion Halls — Apollo org tags catch veterans posts distinctly from
    # government/municipal facilities ('government building', 'city facilities', 'municipal' — run 124);
    # Memorial Day aftermath = facilities in active use; 150+ NE Ohio posts (added 2026-06-02 run 174)
    'vfw post', 'american legion', 'veterans of foreign wars', 'veterans organization',
    'american legion post', 'vfw hall', 'veterans hall', 'veterans post',
    # Law Firms & Legal Office Buildings — Apollo org tags catch law firms distinctly from financial advisors
    # ('wealth management', 'financial advisory' — run 166) and corporate campuses ('corporate campus', 'tech park' — run 101);
    # downtown Cleveland + Beachwood/Independence/Westlake suburban law office corridor (added 2026-06-02 run 174)
    'law firm', 'legal services', 'attorneys at law', 'legal office',
    'law office', 'law group', 'legal group', 'attorneys office',
    # Independent Dental Practices — Apollo 'dental office'/'dental practice'/'family dentistry' catch
    # solo/small-group practices DISTINCTLY from DSO chains ('dental service organization'/'dso' — run 123);
    # 1,000+ NE Ohio independent practices; dentist-owner or office manager signs vendor contracts directly (added 2026-06-02 run 175)
    'dental office', 'dental practice', 'family dentistry', 'general dentistry',
    'dental associates', 'dental clinic', 'dentistry center', 'oral health center',
    # Accounting & CPA Firms — Apollo 'cpa firm'/'accounting firm'/'public accounting' tags catch practices
    # DISTINCTLY from financial advisors ('wealth management', 'financial advisory' — run 166);
    # HW&Co, Maloney+Novotny, SS&G, Bober Markey, Corrigan Krause, Rea & Associates in NE Ohio;
    # post-tax-season June-July window = partners available for vendor conversations (added 2026-06-02 run 175)
    'cpa firm', 'accounting firm', 'certified public accountant', 'public accounting',
    'cpa office', 'cpa group', 'audit firm', 'bookkeeping firm',
    # Flooring & Tile Showrooms — Apollo 'flooring'/'tile store'/'floor store' catch specialty flooring retailers
    # DISTINCTLY from home improvement stores ('home improvement', 'hardware store' — run 136);
    # Floor & Decor (Independence/Mentor/N. Canton), Classic Hardwood, City Tile, Shaw/Mohawk dealers in NE Ohio;
    # delivery trucks stage in lots = oil/diesel staining + tire marks = recurring cleaning need (added 2026-06-02 run 175)
    'flooring store', 'flooring showroom', 'tile store', 'carpet store',
    'flooring center', 'flooring supply', 'floor covering', 'hardwood floor store',
    # Summer Day Camps & Youth Day Programs — DISTINCT from campgrounds (overnight stays — run 158 —
    # 'campground'/'rv park' tags), YMCA (run 131 — 'ymca' tag), sports complexes (run 125 — 'sports complex' tag);
    # Apollo org tags 'day camp'/'summer camp'/'youth camp' catch standalone day camp operators;
    # first pull June 8 Cuyahoga (Boys & Girls Club Cuyahoga County, summer youth programs) (added 2026-06-02 run 176)
    'day camp', 'summer camp', 'youth camp', 'summer youth program',
    'boys and girls club', 'youth day program', 'summer day camp',
    # Childcare Centers & Early Learning Facilities — ORG KEYWORD FIX + SEGMENT #150 (added 2026-06-02 run 177)
    # BUG FIX: DANNY_TITLES has had childcare director titles since run 110 (childcare center director,
    # daycare director, early childhood director, childcare director, preschool director, early learning director)
    # BUT Pass 1 Apollo search requires BOTH a matching DANNY_TITLE AND a matching DANNY_ORG_KEYWORD.
    # Without childcare org keywords, Apollo returned ZERO childcare contacts despite those titles being present.
    # This run adds the missing org keyword side of the query, closing a silent zero-return gap since run 110.
    # Pass 2 (_BROAD_TITLES = owner/president/general manager) × these org keywords also catches franchise
    # owners and general managers at KinderCare, Goddard School, Learning Tree, etc.
    # DISTINCT from summer day camps (run 176 — 'day camp'/'summer camp' — seasonal outdoor), YMCA (run 131 —
    # 'ymca' — community recreation), swim schools (run 159 — 'swim school' — aquatic instruction),
    # sports complexes (run 125 — 'sports complex' — year-round athletic facilities).
    # ODJFS Rule 5101:2-12 childcare facility licensing = exterior cleanliness is part of licensing inspection;
    # parents make enrollment decisions on first visit = exterior condition is the #1 trust signal RIGHT NOW
    # (June = end of school year = peak enrollment month for fall 2026 childcare placement);
    # NE Ohio: KinderCare Learning Centers (50+ Cuyahoga/Summit/Lake locations), Bright Horizons (10+ corporate-
    # sponsored centers — Cleveland Clinic, University Hospitals, major employers), Goddard School (20+ NE Ohio
    # franchises), Learning Tree Early Education Centers (15+ regional chain, NE Ohio HQ), La Petite Academy /
    # LearningCare Group (Medina/Lorain corridor), 1,000+ independent ODJFS-licensed daycare centers.
    # Revenue: $300-$800/visit; 2x/year (spring pre-licensing + fall post-summer); 20-center territory = $12K-$32K/year.
    # First pull: June 8 Cuyahoga.
    'childcare center', 'daycare center', 'child care center', 'early childhood education',
    'preschool center', 'early learning center', 'kindercare', 'bright horizons',
    'goddard school', 'learning tree childcare', 'childcare franchise',
    # B2B Wholesale Supply Houses (Plumbing, HVAC, Electrical) — Ferguson, Hajoca, Winsupply, Graybar, Rexel;
    # DISTINCT from manufacturing (run 118 — 'manufacturing plant'), distribution centers (run 105 — food/retail
    # logistics hubs), hardware stores (run 136 — 'home improvement'/'hardware store' retail);
    # Apollo org tags catch B2B-only trade supply houses that general retail/distribution tags miss entirely;
    # NE Ohio has 30+ Ferguson/Hajoca/Winsupply/Rexel/Graybar branches across 7 counties;
    # HVAC wholesalers: Johnstone Supply, Carrier Enterprise, Lennox Parts Plus (dealer-owned) (added 2026-06-02 run 178)
    'plumbing supply', 'hvac supply', 'electrical supply', 'mechanical supply',
    'plumbing wholesale', 'hvac wholesale', 'electrical wholesale', 'industrial supply house',
    'plumbing distributor', 'hvac distributor', 'electrical distributor', 'ferguson enterprises',
    'winsupply', 'graybar electric', 'rexel electrical', 'johnstone supply',
    # School Bus Companies & Charter Motor Coach Operators — DISTINCT from school districts
    # ('school district', 'board of education' — run 119 — the real estate / facilities side) and
    # public transit ('transit facility', 'gcrta' — run 124 — public authority); these are PRIVATE
    # contract bus operators with their own maintenance depots and vendor budgets (added 2026-06-02 run 178)
    'school bus company', 'student transportation', 'school bus fleet', 'charter bus company',
    'motor coach company', 'bus transportation company', 'charter coach company',
    'first student', 'durham school services', 'national express bus',
    # USPS & Postal Service Facilities — DISTINCT from municipal government ('city hall', 'county building'
    # run 124) and private logistics/distribution centers ('distribution center', 'fulfillment center' run 105);
    # Apollo tags 'usps', 'postal service', 'post office', 'mail processing' return ZERO overlap with
    # existing DANNY_ORG_KEYWORDS; NE Ohio has Cleveland P&DC + Akron P&DC + 100+ delivery offices;
    # postmasters sign vendor contracts via GSA schedules; no competitors cold-calling postal FMs (added 2026-06-02 run 179)
    'usps', 'postal service', 'post office', 'united states postal service',
    'mail processing', 'postal distribution', 'postal facility', 'usps processing',
    # Construction & Industrial Equipment Rental — DISTINCT from construction equipment dealers
    # ('commercial truck dealer', 'heavy equipment dealer' run 143 — those are SALES showrooms);
    # Apollo tags 'equipment rental', 'construction equipment rental', 'tool rental' return
    # ZERO overlap with existing DANNY_ORG_KEYWORDS; named NE Ohio operator keywords are unique; (added 2026-06-02 run 179)
    'equipment rental', 'construction equipment rental', 'tool rental', 'aerial equipment rental',
    'united rentals', 'sunbelt rentals', 'herc rentals', 'blueline rental', 'h&e equipment',
    'nesco rentals', 'ahern rentals', 'industrial equipment rental',
    # Public Housing Authorities — HUD-funded government authorities; DISTINCT from private PM firms
    # ('property management' already in list) and general government facilities ('city facilities', run 124);
    # Apollo tags 'housing authority', 'metropolitan housing' return ZERO overlap (added 2026-06-02 run 180)
    'housing authority', 'metropolitan housing', 'public housing', 'affordable housing',
    'hud housing', 'housing development corporation', 'community development housing', 'section 8 housing',
    # TV & Radio Broadcasting — DISTINCT from 'media' (too broad), 'entertainment' (covered by venues/concerts);
    # Apollo tags 'television station', 'radio station', 'broadcasting company' are unique org-level tags;
    # iHeartMedia + Cumulus + Scripps + Tegna + Nexstar are the major parent companies (added 2026-06-02 run 180)
    'broadcasting company', 'television station', 'radio station', 'broadcast media',
    'tv station', 'iheartmedia', 'cumulus media', 'television broadcasting',
    # Pharmaceutical Manufacturing — DISTINCT from 'manufacturing' (run 118 — general industrial),
    # 'medical device' (run 168 — device/equipment), 'food processing' (run 127 — food/beverage);
    # Apollo tags 'pharmaceutical', 'biotechnology' are clean, high-precision org-level matches;
    # STERIS (Mentor OH), Ferro Corporation (Cleveland HQ) are anchor companies (added 2026-06-02 run 180)
    'pharmaceutical', 'pharmaceuticals', 'drug manufacturing', 'biotech', 'biotechnology',
    'pharmaceutical manufacturing', 'pharma company', 'pharmaceutical plant',
    # Scrap Metal Dealers & Metal Recycling Facilities — DISTINCT from 'salvage yard'/'junkyard'
    # (towing/auto salvage — run 113) and 'metal fabrication'/'steel manufacturer' (manufacturing — run 118);
    # NE Ohio scrap metals hub: OmniSource, Sims Metal Management, Metal Management, TriState Metals;
    # EPA NPDES stormwater permit = SWPPP requires concrete cleaning → compliance pitch angle;
    # Apollo tags 'scrap metal'/'metal recycling'/'ferrous metals' return ZERO overlap with existing tags (added 2026-06-02 run 181)
    'scrap metal', 'metal recycling', 'scrap dealer', 'metal salvage', 'ferrous metals',
    'scrap yard', 'metal scrap yard', 'non-ferrous recycling',
    # Data Centers & Colocation Facilities — DISTINCT from 'corporate campus'/'tech park' (run 101),
    # general IT companies, and telecommunications ('telecom retail' — run 137);
    # Expedient Technology (Independence OH), Zayo Group Cleveland PoP, Iron Mountain Beachwood,
    # OnX Enterprise Solutions; security-certified local vendors get exclusive long-term contracts;
    # Apollo tags 'data center'/'colocation facility' return ZERO overlap with any existing tags (added 2026-06-02 run 181)
    'data center', 'colocation facility', 'server hosting', 'managed hosting',
    'colocation services', 'data center operations', 'internet exchange point',
    # Gymnastics Centers & Tumbling Academies — DISTINCT from 'sports complex' (run 125 — team sports),
    # 'dance studio'/'performing arts' (run 172 — ballet/jazz/recital), 'trampoline park' (run 148 — foam pits);
    # 'gymnastics center'/'tumbling academy'/'gymnastics gym' Apollo org tags return zero overlap with all existing;
    # Ohio DOH gymnastics facility registration catches ALL affiliated USA Gymnastics + ATA Cheer gyms; (added 2026-06-02 run 182)
    'gymnastics center', 'tumbling academy', 'gymnastics gym', 'cheer gym',
    'cheerleading academy', 'gymnastics training', 'gymnastics club', 'tumbling gym',
    # Beverage Distribution Centers & Soft Drink Bottlers — DISTINCT from general distribution centers
    # (run 105 — 'fulfillment center'/'distribution center'/'logistics facility' Apollo tags — general logistics
    # companies like Amazon/UPS/FedEx/XPO, NOT beverage-specific depots) and food processing plants
    # (run 127 — 'food manufacturing'/'food processing' Apollo tags — production facilities, not distribution);
    # Coca-Cola Strongsville, Pepsi Bedford Heights, Great Lakes Distributing Mentor, Southern Glazer's Twinsburg;
    # FDA FSMA food safety = loading dock cleanliness is regulatory = budget line item, not discretionary; (added 2026-06-02 run 182)
    'beverage distribution', 'soft drink distributor', 'beer distributor', 'wine distributor',
    'beverage depot', 'bottling plant', 'beverage warehouse', 'soda distribution',
    # Electric Utility Substations & Power Distribution Facilities — DISTINCT from 'industrial manufacturing'
    # (run 118 — factory/plant ops), 'government facilities' (run 124 — municipal/county), 'pharmaceutical'
    # (run 180), 'data center' (run 181); Apollo org tags 'electric utility'/'power utility'/'electric
    # cooperative' return zero overlap with all existing tags; FirstEnergy Corp tagged 'electric utility';
    # AEP Ohio tagged 'power utility'; first pull June 8 Cuyahoga (added 2026-06-02 run 183)
    'electric utility', 'power utility', 'electric cooperative', 'firstenergy',
    'aep ohio', 'ohio edison', 'illuminating company', 'utility substation',
    # Private EMS & Ambulance Service Depots — DISTINCT from 'hospital campus' (run 124), 'urgent care'
    # (run 114), 'ambulatory surgery center' (run 143); Apollo tags 'ambulance service'/'emergency medical
    # services' return zero overlap with all existing medical/facility tags; American Medical Response,
    # Rural Metro Medical, STAT Medical Transport; first pull June 8 Cuyahoga (added 2026-06-02 run 183)
    'ambulance service', 'ems service', 'emergency medical services', 'private ems',
    'medical transport', 'ambulance company', 'medical response team', 'emergency ambulance',
    # Industrial Gas Suppliers & Welding Supply Companies — DISTINCT from manufacturing (run 118),
    # distribution centers (run 105), scrap metal (run 181); Apollo tags 'welding supply'/
    # 'industrial gas'/'compressed gas'/'gas distributor' return ZERO overlap with existing tags;
    # Airgas NE Ohio, Air Products, Matheson Gas, Praxair/Linde, Valley National Gases, Lincoln Electric;
    # DOT hazmat + EPA Tier I/II EPCRA compliance = facility exterior cleaning is compliance-tracked;
    # first pull June 8 Cuyahoga (added 2026-06-02 run 184)
    'welding supply', 'industrial gas', 'compressed gas', 'gas distributor',
    'gas supplier', 'airgas', 'praxair', 'cylinder gas', 'welding equipment supplier',
    # Commercial Printing Plants & Publishing Facilities — DISTINCT from retail print shops (run 151
    # 'printing services'/'business services center' — FedEx Office/UPS Store/strip-mall printers);
    # industrial offset printing plants have massive concrete loading docks + ink residue staining;
    # Lake Shore Printing (Willoughby), Ohio Business Media, Hometown Newspapers (Berea HQ),
    # Great Lakes Educational Book (Mentor); EPA VOC permit + OSHA 29 CFR 1910.22 compliance;
    # Apollo tags 'commercial printing'/'offset printing'/'printing plant' = zero overlap with run 151;
    # first pull June 8 Cuyahoga (added 2026-06-02 run 184)
    'commercial printing', 'offset printing', 'printing plant', 'print manufacturer',
    'magazine publishing', 'newspaper printing', 'commercial print facility',
    # Aquatic Management Companies — companies that manage 10-50 outdoor/indoor pools for HOAs,
    # apartments, municipalities, schools; DISTINCT from pool facilities themselves (run 136);
    # June = pool startup season = peak pitch window; first pull June 8 Cuyahoga (added 2026-06-03 run 185)
    'pool management company', 'aquatics management', 'pool management services',
    'aquatic management', 'swimming pool management', 'pool operations services',
    # Crane & Rigging Service Companies — distinct from construction equipment rental (run 154 — United Rentals/Sunbelt/HERC);
    # these companies OWN and OPERATE cranes from fixed staging yards; Apollo tags crane operators separately
    # from equipment rental companies; (added 2026-06-03 run 186)
    'crane rental', 'crane service', 'rigging company', 'crane company', 'rigging contractor',
    'lifting services', 'industrial rigging',
    # Municipal Water & Wastewater Treatment Facilities — COMPLETELY DISTINCT from 'municipal facilities' (run 124);
    # 'water treatment', 'wastewater treatment', 'sewer district' return zero overlap with any existing tags;
    # NEORSD, Akron Metro Sewer, city water/sewer utility tags; (added 2026-06-03 run 186)
    'water treatment', 'wastewater treatment', 'sewer district', 'municipal water', 'sanitary district',
    'water utility', 'water reclamation',
    # Ice Rinks & Hockey Facilities — DISTINCT from sports venues/arenas (run 130 — NBA/NHL/AHL venues);
    # Apollo tags 'ice rink'/'ice arena'/'hockey arena' return operators of standalone rinks only;
    # zero overlap with existing sports/entertainment tags; first pull June 8 Cuyahoga (added 2026-06-03 run 187)
    'ice rink', 'ice arena', 'hockey arena', 'skating rink', 'ice complex',
    'ice facility', 'indoor ice rink',
    # Bowling Centers & Family Entertainment Centers — DISTINCT from event venues (run 108) and sports venues (run 130);
    # Apollo 'bowling center'/'family entertainment' tags return stand-alone bowling + FEC operators only;
    # zero overlap with existing entertainment/venue tags; first pull June 8 Cuyahoga (added 2026-06-03 run 187)
    'bowling center', 'bowling alley', 'bowling lanes', 'family entertainment center',
    'entertainment complex', 'bowling management', 'entertainment venue management',
    # EV Charging Network Operators — segment #171; ChargePoint (100+ NE Ohio), EVgo, Blink, BP Pulse, Electrify America;
    # concrete pads = tire rubber, brake dust, coolant leaks; canopy structures = grime;
    # regional network ops managers sign vendor contracts; $10K-$30K/year per territory deal;
    # zero competitors cold-calling EV network FMs; first pull June 8 Cuyahoga (added 2026-06-03 run 188)
    'ev charging', 'electric vehicle charging', 'charging station network', 'ev network',
    'chargepoint', 'evgo', 'blink charging', 'electrify america', 'bp pulse', 'ev infrastructure',
    # Steel Service Centers & Metal Distributors — segment #172; DISTINCT from scrap metal (run 181)
    # and manufacturing (run 118); Apollo 'steel service center'/'metal service center' tags are a
    # separate taxonomy that returns zero overlap with 'metal fabrication'/'scrap metal' org tags;
    # NE Ohio steel service center corridor runs Bedford Heights → Independence → Garfield Heights (added 2026-06-03 run 189)
    'steel service center', 'metal service center', 'steel distributor', 'steel distribution',
    'metal processing', 'steel processing',
    # Fraternal & Social Organizations — segment #173; DISTINCT from VFW/American Legion (run 174);
    # Apollo 'elks lodge'/'moose lodge'/'knights of columbus' tags return zero overlap with any
    # existing veteran, community, or nonprofit tags in the keyword list (added 2026-06-03 run 189)
    'elks lodge', 'moose lodge', 'eagles club', 'knights of columbus',
    'fraternal organization', 'lodge hall', 'social fraternal club',
    # Residential Group Homes & DODD-Licensed Care Facilities — segment #174;
    # Ohio DODD Rule 5123:2-3 org tags; 'group home' and 'supported living' return zero overlap
    # with skilled nursing, assisted living, or home care agency tags (added 2026-06-03 run 190)
    'group home', 'residential group home', 'supported living',
    'intermediate care facility', 'community living facility',
    'dodd certified', 'developmental disabilities home', 'icf dd',
    # Restaurant Equipment & Commercial Kitchen Supply Companies — segment #175
    # Eastern Restaurant Supply (Cleveland), American Restaurant Equipment (Akron), Wasserstrom NE Ohio warehouse;
    # DISTINCT from 'restaurant chain'/'food service management' (run 106) and 'food processing plant' (run 127);
    # Apollo tags 'restaurant equipment', 'commercial kitchen supply', 'food service equipment' return zero overlap;
    # first pull June 8 Cuyahoga (added 2026-06-03 run 191)
    'restaurant equipment', 'commercial kitchen supply', 'food service equipment',
    'restaurant supply company', 'kitchen equipment supplier', 'commercial kitchen equipment',
    'food equipment distributor', 'restaurant supply distributor',
    # Specialty Chemical Manufacturers & Polymer Plants — segment #176
    # Lubrizol Corporation (Wickliffe OH HQ), RPM International (Medina OH HQ), Vibrantz Technologies/Ferro
    # (Mayfield Heights), Materion Corporation (Mayfield Heights), Omnova Solutions (Beachwood), BASF Cleveland;
    # DISTINCT from 'manufacturing plant' (run 118), 'pharmaceutical' (run 180), 'industrial gas' (run 184);
    # Apollo tags 'specialty chemical', 'polymer manufacturer', 'chemical manufacturing' return zero overlap;
    # EPA 40 CFR Part 68 RMP + OSHA PSM 29 CFR 1910.119 = compliance-documented exterior cleaning contracts;
    # first pull June 8 Cuyahoga (Lubrizol Wickliffe, Materion Mayfield Heights) (added 2026-06-03 run 191)
    'specialty chemical', 'polymer manufacturer', 'chemical manufacturing company',
    'specialty chemicals', 'polymer plant', 'chemical plant', 'specialty chemical company',
    'lubrizol', 'rpm international', 'vibrantz technologies', 'materion corporation',
    # Federal Government & VA Healthcare Facilities — segment #177
    # Apollo tags 'veterans affairs', 'va healthcare', 'va medical center' return zero overlap with
    # 'municipal facilities' (run 124 — city/county/township); federal government is a DISTINCT Apollo cluster;
    # 'national guard', 'army reserve center', 'gsa facilities' are federally-unique org tags;
    # first pull June 8 Cuyahoga (VA Northeast Ohio, NASA Glenn, IRS Brookpark) (added 2026-06-03 run 192)
    'veterans affairs', 'va healthcare', 'va medical center', 'department of veterans affairs',
    'federal facilities', 'gsa facilities', 'national guard', 'army reserve center',
    # Ready-Mix Concrete & Asphalt Production Facilities — segment #178
    # Apollo tags 'ready mix concrete', 'hot mix asphalt', 'concrete plant', 'batch plant' return
    # zero overlap with 'manufacturing plant' (run 118) or 'specialty chemical' (run 176);
    # shelly company/aggregate industries/cemex are NE Ohio-specific anchor companies (added 2026-06-03 run 192)
    'ready mix concrete', 'concrete plant', 'ready mixed concrete',
    'hot mix asphalt', 'asphalt plant', 'concrete batching',
    'shelly company', 'aggregate industries', 'cemex ohio',
    # County Correctional Facilities & Detention Centers — segment #179
    # Apollo tags 'county jail', 'detention center', 'correctional facility' return ZERO overlap with
    # 'municipal facilities' (run 124 — city halls, transit depots) or 'federal facilities' (run 177 — VA/NASA);
    # 'county detention' + 'juvenile detention' are county-sheriff-operated facilities with distinct Apollo tags;
    # Cuyahoga County Sheriff + Summit County Sheriff + Lake/Medina/Lorain/Geauga county sheriffs (added 2026-06-03 run 193)
    'county jail', 'detention center', 'correctional facility', 'county detention',
    'juvenile detention', 'county correctional', 'correctional center', 'sheriff facility',
    # Inpatient Rehabilitation Hospitals & Long-Term Acute Care — segment #180
    # Apollo tags 'rehabilitation hospital', 'long-term acute care', 'ltac hospital' return ZERO overlap
    # with 'skilled nursing facility' (run 169), 'physical therapy' (run 126), or hospital main campuses (run 124);
    # Encompass Health, Select Medical, Kindred, Promise are NE Ohio-specific anchor companies (added 2026-06-03 run 193)
    'rehabilitation hospital', 'inpatient rehabilitation', 'long-term acute care',
    'ltac hospital', 'rehab hospital', 'transitional care hospital',
    'encompass health', 'select medical', 'kindred hospital',
    # K-12 Private & Parochial Schools — segment #181
    # Apollo indexes private/parochial schools under separate org tags from public 'school district' orgs;
    # 'independent school', 'private school', 'catholic school' tags return ZERO overlap with
    # public school district org tags (run 119); Diocese of Cleveland + private academies NE Ohio;
    # first pull June 8 Cuyahoga (added 2026-06-03 run 194)
    'private school', 'independent school', 'catholic school', 'parochial school',
    'diocesan school', 'preparatory school', 'independent day school',
    'private academy', 'catholic academy',
    # County Fairgrounds & Agricultural Exhibit Facilities — segment #182
    # Apollo indexes county fairgrounds under 'county fair', 'agricultural society', 'fairgrounds' org tags;
    # return ZERO overlap with sports venues (run 127), convention centers (run 128), event venues (run 108);
    # Cuyahoga/Summit/Medina/Lorain/Lake/Geauga/Portage county agricultural societies;
    # first pull June 8 Cuyahoga (added 2026-06-03 run 194)
    'county fairgrounds', 'county fair', 'agricultural fairgrounds', 'fairgrounds',
    'county agricultural society', 'agricultural society', 'fair association',
    'county fair association', 'agricultural exhibit',
    # Aerospace & Defense Component Manufacturers — segment #183
    # Apollo tags 'aerospace manufacturing', 'defense contractor', 'aviation components' return ZERO overlap
    # with 'manufacturing plant' (run 118) or 'specialty chemical' (run 176); Parker Hannifin 50+ NE Ohio
    # facilities + TransDigm Cleveland HQ; AS9100D + ITAR = compliance-driven vendor contracts;
    # first pull June 8 Cuyahoga (added 2026-06-04 run 195)
    'aerospace manufacturing', 'aerospace components', 'defense manufacturing',
    'aviation components', 'defense contractor', 'aerospace systems',
    'aerospace supplier', 'aerospace engineering',
    # Precision Machining & CNC Machine Shops — segment #184
    # Apollo tags 'precision machining', 'cnc machining', 'machine shop' return ZERO overlap with
    # 'manufacturing plant' (run 118); NE Ohio has 500+ machine shops; ISO 9001 compliance angle;
    # machining coolant + metal chip accumulation = heavy building exterior cleaning need; additive leads
    # (added 2026-06-04 run 195)
    'precision machining', 'precision manufacturing', 'cnc machining',
    'machine shop', 'precision parts', 'cnc manufacturing',
    'precision components', 'machining services',
    # Public Transit Agencies & Bus Depot Facilities — segment #185
    # GCRTA, Metro RTA, SARTA, LAKETRAN org keywords; DISTINCT from city/municipal org tags (run 124);
    # Apollo returns transit authority contacts under these org keywords that 'city' tags miss;
    # bus garages + transit centers + maintenance yards = recurring cleaning need (added 2026-06-05 run 196)
    'transit authority', 'public transit', 'metropolitan transit', 'bus rapid transit',
    'regional transit', 'transit agency', 'transit commission',
    # Industrial Real Estate & Logistics Park Management — segment #186
    # ProLogis/Duke Realty/Scannell/Opus NE Ohio org keywords; DISTINCT from 'commercial property management' (existing)
    # and 'commercial real estate' (existing); industrial-specific tags return REIT/logistics park FMs
    # that general PM tags miss; additive Apollo leads, zero overlap with residential/office PM (added 2026-06-05 run 196)
    'industrial real estate', 'logistics real estate', 'industrial park', 'warehouse real estate',
    'industrial reit', 'industrial property management', 'logistics campus',
    # Indoor Shooting Ranges & Archery Centers — segment #187 org keywords (added 2026-06-06 run 197)
    # Apollo returns shooting range owner/manager contacts under these org tags; additive, zero overlap
    'shooting range', 'gun range', 'indoor range', 'archery center',
    'shooting sports', 'firearms range', 'indoor shooting',
    # Cannabis Cultivation & Processing Facilities — segment #188 org keywords (added 2026-06-06 run 197)
    # DISTINCT from 'cannabis dispensary' (run 135); these are production/grow facility tags in Apollo
    'cannabis cultivation', 'marijuana cultivation', 'cannabis grow', 'cannabis processor',
    'marijuana processor', 'cannabis producer', 'cannabis grower',
    # Multi-Site Fitness Chain District Operations — segment #189 org keywords (added 2026-06-07 run 198)
    # DISTINCT from 'fitness center'/'health club'/'gym management' (run 99 — individual gym location tags)
    # and 'boutique fitness'/'fitness studio' (run 143 — studio owner tags);
    # these org tags catch multi-location FITNESS CHAIN OPERATORS in Apollo (franchise groups, chain operators)
    # vs. individual gym locations; Planet Fitness franchise groups, Anytime Fitness networks, etc.
    'fitness management company', 'health club chain', 'fitness network',
    'gym chain', 'fitness portfolio', 'fitness group',
    # Cold Storage & Refrigerated Warehouse Networks — segment #190 org keywords (added 2026-06-07 run 198)
    # DISTINCT from 'cold storage warehouse'/'food plant management' (run 127 — food manufacturer context);
    # DISTINCT from 'warehouse'/'distribution center' (run 105 — general logistics/fulfillment);
    # these org tags catch STANDALONE COLD STORAGE OPERATORS in Apollo (Lineage, Americold, US Cold Storage)
    # vs. food manufacturers that happen to have cold storage (already captured under food processing tags)
    'cold storage logistics', 'refrigerated logistics', 'temperature controlled warehouse',
    'cold chain warehouse', 'refrigerated distribution', 'cold warehouse',
    # Intermodal Rail Terminals & Freight Hub Facilities — segment #191 org keywords (added 2026-06-08 run 199)
    # DISTINCT from 'freight terminal'/'distribution center' (run 105 — road-based logistics);
    # these org tags catch RAIL TERMINAL OPERATORS in Apollo vs. general logistics companies
    'intermodal terminal', 'rail terminal', 'freight rail', 'railroad terminal',
    'intermodal facility', 'rail yard', 'rail hub', 'freight hub',
    # Commercial Parking Management Portfolio Companies — segment #192 org keywords (added 2026-06-08 run 199)
    # DISTINCT from 'parking garage management'/'parking structure' (run 128 — individual facility tags);
    # these org tags catch PARKING MANAGEMENT COMPANIES (SP+, Impark, ABM Parking, Lanier) in Apollo
    'parking management company', 'parking services company', 'commercial parking management',
    'valet parking management', 'parking portfolio management', 'parking management services',
    # Co-Packing & Contract Manufacturing Facilities — segment #193 org keywords (added 2026-06-09 run 200)
    # DISTINCT from 'food processing'/'food manufacturer' (run 127 branded food plants);
    # DISTINCT from 'manufacturing plant'/'industrial facility' (run 118 captive manufacturers);
    # these org tags catch THIRD-PARTY CONTRACT MANUFACTURERS in Apollo
    'contract manufacturing', 'co-packing', 'co-manufacturing', 'toll manufacturing',
    'contract packaging', 'co-pack', 'packaging services', 'outsourced manufacturing',
    # Semiconductor & PCB/Electronics Manufacturers — segment #194 org keywords (added 2026-06-09 run 200)
    # DISTINCT from 'aerospace'/'defense manufacturer' (run 183) and 'medical device' (run 168);
    # these org tags catch ELECTRONICS/PCB MANUFACTURERS in Apollo (Parker Hannifin Electronics, API Technologies)
    'semiconductor manufacturer', 'circuit board manufacturer', 'pcb manufacturer',
    'electronics manufacturer', 'printed circuit board', 'electronics assembly',
    # Boat Repair & Marine Service Centers — segment #195 org keywords (added 2026-06-10 run 201)
    # DISTINCT from 'marina'/'boat storage' (run 109 slip/storage ops), 'boat dealer' (run 146 retail),
    # 'charter fishing' (run 174 excursion ops); these org tags catch MARINE REPAIR / SERVICE YARDS in Apollo
    'marine service center', 'boat repair', 'marine repair', 'boat yard',
    'marine maintenance', 'hull repair', 'boat service center', 'watercraft repair',
    # Craft Breweries & Taprooms — segment #196 org keywords (added 2026-06-11 run 202)
    # DISTINCT from restaurants (run 106 — 'restaurant', 'dining', 'food service', 'qsr');
    # these org tags catch CRAFT BREWERIES specifically in Apollo — 100+ in NE Ohio 7 counties
    'craft brewery', 'craft beer', 'taproom', 'microbrewery', 'craft brewing',
    'brewpub', 'production brewery', 'regional brewery', 'brewing company',
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
    # Commercial cleaning & janitorial companies — PERFECT complementary referral partner:
    # they clean the INSIDE of every building we pressure wash the outside of; zero service overlap;
    # natural pitch: "I refer you on the inside jobs; you refer me on the outside"; both benefit;
    # they're inside every commercial building, office park, medical clinic, and retail strip;
    # they see dirty building facades, stained parking lots, and grimy entrances on EVERY visit;
    # Jan-Pro Franchising (NE Ohio franchise network), ServiceMaster Clean, Coverall Cleaning,
    # Anago Cleaning Systems, ABM Industries (large national), Jani-King; all have NE Ohio operators;
    # owner/franchise operator decides referral relationships independently; added 2026-06-01 run 171
    {'type': 'contractors', 'titles': ['owner', 'president', 'founder', 'operator', 'franchise owner'],
     'keywords': ['commercial cleaning', 'janitorial service', 'building cleaning',
                  'commercial janitorial', 'office cleaning', 'facility cleaning',
                  'jan-pro', 'servicemaster clean', 'coverall cleaning', 'anago',
                  'abm industries', 'jani-king', 'commercial cleaning franchise'],
     'label': 'Commercial Cleaning Companies'},
    # Commercial Real Estate Brokers — CBRE Cleveland, Colliers International NE Ohio, JLL Cleveland,
    # NAI Daus (regional NE Ohio), Hanna Commercial Real Estate; DISTINCT from residential realtors
    # (Carla already targets those via 'Realtors' search type — different Apollo org tags);
    # commercial brokers walk and photograph properties before listing → they see dirty facades, stained
    # lots, grimy loading docks on EVERY site visit; they have deep relationships with property owners
    # and facility managers, often recommending vendors BEFORE an FM is even hired;
    # pitch: "We can make your listings look 100% better in marketing photos in 3 hours — and if any
    # of your building owners ever need exterior cleaning, we'd appreciate the referral";
    # one CBRE broker with 15 active commercial listings = 15 potential FM introductions;
    # DISTINCT Apollo org tags: 'commercial real estate brokerage', 'commercial property broker' ≠
    # 'real estate brokerage'/'realty' (residential Carla targets); added 2026-06-02 run 176
    {'type': 'contractors', 'titles': ['commercial broker', 'commercial real estate broker',
                                       'commercial leasing agent', 'commercial real estate agent',
                                       'commercial property advisor'],
     'keywords': ['commercial real estate brokerage', 'commercial property brokerage',
                  'commercial real estate', 'commercial broker', 'cbre', 'jll', 'colliers',
                  'nai daus', 'hanna commercial', 'commercial property management brokerage'],
     'label': 'Commercial RE Brokers'},
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

    # Batch DANNY_TITLES + DANNY_ORG_KEYWORDS to prevent Apollo silently capping large arrays.
    # Pass 1 (title batches): 200+ titles searched in groups of 50, each paired with ALL org keywords.
    #   Catches contacts whose title is in our list, regardless of which org keywords Apollo processes.
    # Pass 2 (org keyword batches): broad generic decision-maker titles × 50-keyword batches.
    #   Catches contacts at target companies whose titles are generic (e.g. "Owner" at YMCA,
    #   "President" at Manheim Cleveland, "Manager" at Cleveland Museum of Art) and may not match
    #   specific segment titles above even though their company IS in our org keyword list.
    # All results deduplicated by Apollo person_id.
    _TITLE_BATCH = 50
    _ORG_BATCH = 50
    _seen_ids = set()
    people = []

    # Pass 1: title batches with full org keyword list
    _t_batches = [DANNY_TITLES[i:i + _TITLE_BATCH] for i in range(0, len(DANNY_TITLES), _TITLE_BATCH)]
    for _bi, _batch in enumerate(_t_batches):
        _batch_results = apollo_search(_batch, search['counties'], per_page=25, keywords=DANNY_ORG_KEYWORDS)
        for _p in _batch_results:
            _pid = _p.get('id', '')
            if _pid and _pid not in _seen_ids:
                _seen_ids.add(_pid)
                people.append(_p)
        if _bi < len(_t_batches) - 1:
            time.sleep(1)

    # Pass 2: org keyword batches with broad generic decision-maker titles
    _BROAD_TITLES = [
        'general manager', 'district manager', 'area manager', 'regional director',
        'branch manager', 'executive director', 'owner', 'president',
    ]
    _ok_batches = [DANNY_ORG_KEYWORDS[i:i + _ORG_BATCH] for i in range(0, len(DANNY_ORG_KEYWORDS), _ORG_BATCH)]
    for _oki, _ok_batch in enumerate(_ok_batches):
        _batch_results = apollo_search(_BROAD_TITLES, search['counties'], per_page=25, keywords=_ok_batch)
        for _p in _batch_results:
            _pid = _p.get('id', '')
            if _pid and _pid not in _seen_ids:
                _seen_ids.add(_pid)
                people.append(_p)
        if _oki < len(_ok_batches) - 1:
            time.sleep(1)

    print(f'  Found {len(people)} people from Apollo ({len(_t_batches)} title batches + {len(_ok_batches)} org-keyword batches, deduplicated)')

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
