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
    # HOA board-level decision-makers — boards vote on vendor budgets in May-June;
    # DIFFERENT from HOA managers; self-managed HOAs have no management company — board president IS the decision-maker;
    # Apollo surfaces at HOA/condo association orgs; adds 'hoa member' substring risk — using specific compound phrases (added 2026-05-27 run 109)
    'hoa president', 'hoa board president', 'community association president',
    'hoa treasurer', 'hoa board treasurer',
    'condo board president', 'condominium board president',
    # Marinas & waterfront — Lake Erie shoreline; pre-season May-June = peak prep window;
    # marina managers sign vendor contracts for concrete ramps, dock areas, storage lots (added 2026-05-27 run 109)
    'marina manager', 'marina director', 'harbor master', 'waterfront facilities manager',
    'marina operations manager', 'dock master',
    # Churches & religious facilities — large NE Ohio Catholic parishes + evangelical campuses;
    # church administrator or facilities director signs vendor contracts; large parking lots + brick facades + outdoor event areas;
    # 500+ large NE Ohio churches; $1,000-$3,000/visit; 2-3x/year (added 2026-05-27 run 110)
    'church facilities manager', 'parish administrator', 'religious facilities manager',
    'church administrator', 'facilities coordinator', 'director of facilities management',
    # Childcare & early education — licensing inspections create recurring urgency; director signs vendor contracts directly;
    # NE Ohio has 1,000+ licensed centers; parking + entrance + playground = recurring pressure washing need (added 2026-05-27 run 110)
    'childcare center director', 'daycare director', 'early childhood director',
    'childcare director', 'preschool director', 'early learning director',
    # Golf courses & country clubs — NE Ohio has 100+ courses; peak May-June season; superintendent + GM sign vendor contracts;
    # clubhouse exterior + cart area + parking lot = recurring quarterly wash; zero competitors (added 2026-05-27 run 112)
    'golf course superintendent', 'golf club manager', 'club general manager',
    'golf course director', 'director of golf', 'golf operations manager',
    # Cemeteries & memorial parks — large paved driveways + monument areas; spring = peak visitor season (added 2026-05-27 run 112)
    'cemetery superintendent', 'cemetery director', 'cemetery manager', 'memorial park director',
    # Funeral homes — 100+ NE Ohio locations; appearance is non-negotiable on the most emotional day for families;
    # funeral directors/owners sign vendor contracts; low competition; $2K-$6K/year per location (added 2026-05-27 run 113)
    'funeral director', 'funeral home director', 'mortuary manager', 'funeral home manager',
    'mortuary director', 'funeral services director',
    # Urgent care centers — FastMed, Concentra, GoHealth, CareNow, Summa Now, MetroHealth Urgent Care;
    # state licensing inspections check patient-facing exterior appearance; high foot traffic = clean entry mandatory;
    # regional FMs sign multi-clinic vendor contracts; $3,200-$8,000/year per clinic (added 2026-05-27 run 114)
    'urgent care director', 'urgent care center manager', 'clinic director',
    'ambulatory care director', 'walk-in clinic manager', 'urgent care manager',
    # Veterinary clinics & animal hospitals — Banfield, VCA, BluePearl, National Veterinary Associates;
    # 300+ NE Ohio locations; licensing inspections = exterior appearance standard;
    # district FMs sign multi-clinic contracts; $800-$2,000/clinic; 20-clinic chain = $16K-$40K/year (added 2026-05-28 run 115)
    'veterinary practice manager', 'animal hospital manager', 'veterinary clinic manager',
    'vet clinic manager', 'animal hospital director', 'veterinary district manager',
    # Towing companies & auto salvage — large paved yards + building exteriors + loading areas;
    # oil, hydraulic fluid, road grime = heavy accumulation; NE Ohio has 50+ operators (Jeff's Towing, Allied, AAA contracted lots);
    # owner-operators manage multiple tow yards + impound lots; zero competitors targeting this segment;
    # $800-$2,500/visit; 4x/year = $3,200-$10,000/year per operator (added 2026-05-28 run 117)
    'tow yard manager', 'towing company owner', 'auto salvage manager', 'impound lot manager',
    'towing operations manager', 'salvage yard manager', 'auto salvage director',
    # Manufacturing & industrial facilities — NE Ohio manufacturing hub (Ford Avon Lake, Lincoln Electric, Eaton, Parker Hannifin);
    # loading docks + building exteriors + parking lots; OSHA compliance = recurring contract;
    # plant FMs + maintenance managers sign vendor contracts; $3,000-$15,000/year per facility (added 2026-05-28 run 118)
    'plant manager', 'plant superintendent', 'manufacturing plant manager', 'plant facilities manager',
    'industrial facility manager', 'maintenance manager', 'plant maintenance manager',
    'ehs manager', 'environmental health safety manager', 'manufacturing facility manager',
    # Car wash facilities — Mr. Clean Car Wash (12+ NE Ohio), Mister Car Wash, independent operators;
    # building exteriors, vacuum areas, equipment bays; OSHA stormwater compliance;
    # district managers sign multi-location contracts; ironic pitch = memorable; $1,500-$4,000/year (added 2026-05-28 run 118)
    'car wash manager', 'car wash district manager', 'car wash owner', 'car wash operator',
    'carwash manager', 'express wash manager', 'tunnel wash manager', 'car wash general manager',
    # Public K-12 school districts — summer = buildings empty; facilities teams do annual maintenance;
    # buildings and grounds directors sign vendor contracts for all district buildings (added 2026-05-28 run 119)
    'director of buildings and grounds', 'buildings and grounds director',
    'school maintenance director', 'school district facilities manager',
    # Car rental companies — large paved lots at airport + suburban locations;
    # district managers sign multi-site vendor contracts (added 2026-05-28 run 119)
    'car rental district manager', 'rental car location manager', 'car rental operations manager',
    'branch rental manager',
    # Tire & auto service chains — Discount Tire, Jiffy Lube, Firestone, Midas, Valvoline, Monro in NE Ohio;
    # district managers sign multi-location vendor contracts (added 2026-05-28 run 120)
    # 'automotive service center director' added run 122 — was in DANNY_TITLES but missing here (routing sync gap)
    'tire center manager', 'auto service center manager', 'tire store manager', 'service center manager',
    'quick lube manager', 'auto lube manager', 'tire district manager', 'automotive service center director',
    # Movie theaters / cineplexes — AMC, Regal, Cinemark, Atlas Cinemas NE Ohio; GMs sign vendor contracts (added 2026-05-28 run 120)
    # 'cinema general manager' added run 122 — was in DANNY_TITLES but missing here (routing sync gap)
    'theater general manager', 'cinema manager', 'movie theater manager', 'multiplex manager',
    'theater operations manager', 'cinema general manager',
    # Public library systems — Cuyahoga County PL, Akron-Summit County PL; government FMs (added 2026-05-28 run 120)
    'library director', 'public library director', 'library facilities manager', 'library system director',
    'branch library manager', 'library operations manager',
    # Bowling alleys & entertainment centers — Brunswick Zone, Dave & Buster's, AMF in NE Ohio;
    # large parking lots + building exteriors; GMs sign vendor contracts (added 2026-05-28 run 120)
    # 'bowling center director' added run 122 — was in DANNY_TITLES but missing here (routing sync gap)
    'bowling alley manager', 'bowling center manager', 'entertainment center manager',
    'family entertainment center manager', 'bowling center director', 'recreation center manager',
    # Dental Service Organizations (DSOs) — Aspen Dental, Heartland Dental, Dental Care Alliance in NE Ohio;
    # district managers oversee 10-20 clinics and sign multi-location vendor contracts;
    # ORC dental licensing = exterior appearance standard; routing to Property Manager sequence (added 2026-05-28 run 123)
    'dso district manager', 'dental district manager', 'dental group practice director',
    'practice area director', 'regional dental director', 'dental operations director',
    'dental regional manager', 'group practice administrator',
    # Municipal & Government Facilities — city halls, county buildings, township offices, transit depots;
    # RTA (GCRTA), Port of Cleveland, Cleveland Metroparks; large parking lots + public plazas;
    # government FMs sign direct-award vendor contracts; routing to Property Manager sequence (added 2026-05-28 run 124)
    'city facilities manager', 'municipal facility manager', 'government facility manager',
    'township facilities manager', 'public works facilities manager', 'county facilities director',
    'transit facility manager', 'city maintenance director', 'municipal buildings manager',
    'government buildings manager', 'public facilities manager', 'parks district manager',
    'parks and recreation director', 'parks facilities manager',
    # Hospital & Health System Main Campuses — main hospital buildings (not outpatient offices above);
    # Cleveland Clinic Main, UH Rainbow/Ahuja/Geauga, MetroHealth, Summa Health Akron City, Mercy Health;
    # hospital facility directors manage parking structures, entrance plazas, loading docks;
    # routing to Property Manager sequence (facility management / compliance angle) (added 2026-05-28 run 124)
    'hospital facilities director', 'hospital plant operations manager', 'health system facilities director',
    'hospital maintenance director', 'hospital facility manager', 'acute care facilities manager',
    'hospital engineering director', 'clinical facilities manager', 'hospital plant manager',
    'vice president of facilities', 'vp facilities',
    # Pet Boarding & Kennel Facilities — PetSmart PetsHotel, Bark Avenue, Hounds Town, Camp Bow Wow;
    # Ohio pet boarding license = exterior cleanliness standard; 300+ NE Ohio facilities;
    # routing to Property Manager sequence (facility/compliance angle) (added 2026-05-28 run 125)
    'pet boarding manager', 'kennel manager', 'dog boarding director', 'pet resort manager',
    'doggy daycare manager', 'animal boarding manager', 'pet care director', 'kennel director',
    # Dialysis Centers — DaVita (50+ NE Ohio), Fresenius Medical Care (40+ NE Ohio), US Renal Care;
    # CMS certification = exterior cleanliness standard; district FMs sign multi-location contracts;
    # routing to Property Manager sequence (compliance + facility management angle) (added 2026-05-28 run 125)
    'dialysis center manager', 'dialysis clinic manager', 'renal care director',
    'dialysis facility manager', 'outpatient dialysis manager', 'dialysis district manager',
    'dialysis regional manager', 'kidney care director',
    # Sports Complexes & Youth Athletic Facilities — heavy weekend traffic = staining;
    # Sportsplex at Mentor, Great Lakes Athletic Complex, youth baseball/softball/soccer/hockey complexes;
    # GM or owner signs vendor contracts; routing to Property Manager sequence (added 2026-05-28 run 125)
    'sports complex manager', 'athletic complex director', 'sports facility manager',
    'recreation complex manager', 'sports complex director', 'athletic facility director',
    'youth sports director', 'sports facility director',
    # Physical Therapy Clinic Chains — NovaCare, ATI Physical Therapy, Select PT, Athletico in NE Ohio;
    # district managers sign multi-clinic vendor contracts; state PT licensing = exterior appearance standard;
    # routing to Property Manager sequence (compliance + facility management angle) (added 2026-05-28 run 126)
    'physical therapy district manager', 'physical therapy clinic manager', 'outpatient pt manager',
    'rehabilitation clinic manager', 'physical therapy center director', 'therapy district manager',
    'outpatient physical therapy manager', 'rehab clinic director', 'pt clinic manager',
    # Pharmacy & Drug Store Chains — CVS, Walgreens, Rite Aid, Giant Eagle Pharmacy, Discount Drug Mart;
    # district FM contacts sign vendor contracts for 5-15 store territories;
    # drive-through canopies + parking lots + building exteriors; routing to Property Manager sequence (added 2026-05-28 run 126)
    'pharmacy district manager', 'drug store district manager', 'pharmacy facilities manager',
    'retail pharmacy manager', 'pharmacy store manager', 'pharmacy operations manager',
    'drug store manager', 'pharmacy regional manager',
    # Concert Venues & Outdoor Amphitheaters — Blossom Music Center (Live Nation, Cuyahoga Falls),
    # Jacobs Pavilion at Nautica (Cleveland waterfront), Hard Rock Rocksino Northfield Park;
    # massive parking lots + plaza concourses + loading dock areas;
    # Live Nation / AEG regional FM directors sign seasonal vendor contracts;
    # spring pre-season + fall post-season = 2 visits/year; zero competitors cold-calling; routing to PM sequence (added 2026-05-29 run 127)
    'amphitheater manager', 'performing arts center manager', 'concert venue manager',
    'outdoor venue manager', 'music venue manager', 'live entertainment venue manager',
    # Food Processing Plants & Cold Storage — FDA/USDA GMP exterior cleanliness regulations;
    # Shiloh Foods (Medina County), J.M. Smucker (Orville OH), Bob Evans Foods, Cloverleaf Cold Storage;
    # loading docks + building exteriors + refrigerated bay areas = recurring quarterly pressure wash;
    # FDA 21 CFR Part 110/117 compliance angle drives urgency; routing to Property Manager sequence (added 2026-05-29 run 127)
    'food plant manager', 'food processing facility manager', 'food manufacturing manager',
    'cold storage manager', 'food production manager', 'food operations manager',
    'food facility manager', 'food plant superintendent',
    # Airport & Aviation Facilities — CLE Hopkins, CAK, Lorain County Airport;
    # FAA certification appearance standards; one airport contract = $10K-$30K/year;
    # zero competitors targeting airport FM contacts; routing to Property Manager sequence (added 2026-05-29 run 128)
    'airport facilities manager', 'airport operations manager', 'aviation facilities director',
    'airport maintenance director', 'airport facilities director', 'terminal facilities manager',
    'airport grounds manager', 'airfield maintenance manager',
    # Parking Garages & Structures — downtown Cleveland/Akron, hospital garages, HOA parking;
    # org keywords already in DANNY_ORG_KEYWORDS; adding title routing so contacts are correctly
    # mapped to Property Manager sequence on Mixmax import (added 2026-05-29 run 128)
    'parking manager', 'parking operations manager', 'parking district manager',
    'parking structure manager', 'garage manager', 'parking lot manager',
    'parking facility manager',
    # Convention Centers & Exhibition Halls — Cleveland Convention Center, I-X Center, Akron Civic Complex,
    # John S. Knight Center; massive event plaza + loading areas; routing to Property Manager sequence (added 2026-05-29 run 128)
    'convention center manager', 'convention center director', 'exhibition hall manager',
    'trade show facility manager', 'events center manager', 'convention facilities manager',
    'expo center manager', 'conference facility director',
    # Craft Breweries & Taprooms — Great Lakes Brewing, Platform Beer, Masthead, Thirsty Dog, Goldhorn,
    # Terrestrial, Collision Bend, Forest City Brewery, Crooked River, Brew Kettle, Trail Brew Works;
    # outdoor patios + parking + building facades; spring patio opening = natural pitch window;
    # seasonal events = appearance is marketing; taproom GM or owner signs vendor contracts directly;
    # routing to Property Manager sequence (FM/vendor contract angle); zero competitors cold-calling (added 2026-05-29 run 129)
    'taproom manager', 'brewery manager', 'craft brewery manager', 'tap room manager',
    'brewery operations manager', 'taproom director', 'brewery general manager',
    # Standalone generic decision-maker titles for routing of manually-imported leads.
    # 'district manager' is now SAFE to include because detect_lead_type() checks GAS_STATION_KEYWORDS
    # against company name FIRST (before PROPERTY_MANAGER_TITLES), so "District Manager" at Circle K
    # routes to gas_station, while "District Manager" at CVS routes to property_manager. (fixed run 136)
    'district manager',     # CVS, Walgreens, Discount Tire, Jiffy Lube, QSR franchises, DSO chains, etc.
    'area manager',         # Enterprise Rent-A-Car, Planet Fitness, Anytime Fitness, Aspen Dental chains
    'regional director',    # DaVita dialysis, NovaCare PT, Concentra, Heartland Dental, hotel brand regional FMs
    'branch manager',       # bank branches (Huntington, KeyBank, Fifth Third, PNC) — branch-level vendor contact
    # Museums & Cultural Institutions — Cleveland Museum of Art, Cleveland Museum of Natural History,
    # Cleveland Metroparks Zoo, Rock & Roll Hall of Fame, Great Lakes Science Center, Maltz Museum,
    # Stan Hywet Hall, Severance Hall, Cleveland Play House; zero competitors targeting this segment;
    # appearance is non-negotiable for donor events + public trust; routing to Property Manager sequence (added 2026-05-29 run 130)
    'museum facilities manager', 'museum director', 'cultural center director', 'museum manager',
    'zoo facilities manager', 'zoo director', 'aquarium manager', 'botanical garden manager',
    'cultural institution manager', 'arts center director', 'science center manager',
    'natural history museum manager', 'art museum facilities manager', 'historic estate manager',
    # YMCA & Community Centers — YMCA of Greater Cleveland (12+ branches), Akron Area YMCA (7 branches),
    # Summit/Medina/Lake County YMCAs; state health dept. licensing = exterior cleanliness standard;
    # branch directors + facilities managers sign vendor contracts; routing to Property Manager sequence
    # (facility management / compliance angle); zero competitors targeting YMCA FMs (added 2026-05-29 run 131)
    'ymca director', 'ymca branch director', 'ymca facilities manager', 'ymca operations manager',
    'ywca director', 'community center director',
    # Car Auctions & Vehicle Wholesale — Manheim Cleveland (Cox Automotive), ADESA/KAR Auction (Portage County),
    # NovaStar Auto Auction, NADB, independent wholesale auction houses;
    # enormous paved outdoor lots + reconditioning bays + building facades; OSHA stormwater compliance;
    # FM signs quarterly vendor contracts; routing to Property Manager sequence (added 2026-05-29 run 133)
    'auto auction manager', 'vehicle auction manager', 'auction facility manager',
    'auto auction operations manager', 'vehicle wholesale manager', 'auction site manager',
    # Coin Laundries & Laundromats — ironic pitch; owner-operators sign vendor contracts directly;
    # routing to Property Manager sequence (FM/facility vendor angle) (added 2026-05-29 run 135)
    'laundromat owner', 'coin laundry manager', 'laundry facility manager', 'laundromat manager',
    'coin laundry owner', 'self-service laundry manager', 'laundry district manager',
    # Blood/Plasma Donation Centers — BioLife, CSL Plasma, Grifols, Vitalant;
    # FDA licensing = exterior cleanliness standard; district FMs sign multi-center contracts;
    # routing to Property Manager sequence (compliance + FM angle) (added 2026-05-29 run 135)
    'plasma center manager', 'donation center manager', 'blood center manager',
    'plasma donation manager', 'blood bank manager', 'donor center manager',
    # Cannabis Dispensaries — Ohio rec. cannabis legal Nov 2023; state ODM licensing = appearance standard;
    # dispensary owners/GMs sign vendor contracts; routing to Property Manager sequence (added 2026-05-29 run 135)
    'dispensary manager', 'cannabis dispensary manager', 'dispensary director',
    'dispensary general manager', 'cannabis operations manager', 'dispensary owner',
    # Professional Sports Venues — Rocket Mortgage FieldHouse, Progressive Field, FirstEnergy Stadium;
    # facility directors manage large maintenance budgets; routing to Property Manager sequence (added 2026-05-29 run 135)
    'sports venue facilities manager', 'stadium facilities manager', 'arena facilities manager',
    'venue operations director', 'sports facility operations manager', 'stadium operations manager',
    'arena operations manager', 'ballpark facilities manager',
    # Dollar Stores & General Merchandise Discount Chains — Dollar General (100+ NE Ohio), Family Dollar,
    # Dollar Tree, Five Below, Big Lots; enormous NE Ohio store density; district FMs sign multi-site vendor
    # contracts; large paved lots + building exteriors + dumpster pads; $300-$700/location quarterly;
    # 30-location district deal = $36K-$84K/year; zero competitors cold-calling dollar store DMs (added 2026-05-29 run 136)
    'dollar store district manager', 'dollar store manager', 'general merchandise manager',
    'general merchandise district manager', 'family dollar manager', 'dollar general manager',
    'discount store manager', 'dollar store operations manager', 'value retail manager',
    'five below manager', 'big lots manager', 'discount retail manager',
    # Auto Parts Stores — O'Reilly Auto Parts (50+ NE Ohio), AutoZone (60+ NE Ohio), Advance Auto Parts,
    # NAPA Auto Parts (Genuine Parts Co.), Pep Boys; oily parking lots + building exteriors + dumpster areas;
    # district managers sign multi-site vendor contracts; $400-$800/location; 25-location district = $20K-$50K/year;
    # zero competitors cold-calling auto parts district managers in NE Ohio (added 2026-05-29 run 136)
    'auto parts district manager', 'auto parts store manager', 'auto parts regional manager',
    'automotive parts manager', 'parts store district manager', 'parts store manager',
    'auto parts operations manager', 'auto parts facilities manager',
    # Hardware & Home Improvement Centers — Home Depot (20+ NE Ohio), Lowe's (15+ NE Ohio), Menards,
    # Ace Hardware (50+ NE Ohio dealer-owned), True Value, Do It Best; enormous garden center plazas +
    # massive parking lots + building exteriors + lumber yard areas + outdoor display pads;
    # district FMs manage 10-20 stores and sign vendor contracts; $1,500-$5,000/location;
    # one Home Depot district = $30K-$100K/year; premium accounts (added 2026-05-29 run 136)
    'home improvement district manager', 'hardware store manager', 'home center manager',
    'home improvement store manager', 'hardware district manager', 'building materials manager',
    'home improvement operations manager', 'hardware store district manager',
    # Community Swimming Pools & Aquatic Centers — NE Ohio municipal pools (Lyndhurst, North Olmsted,
    # Brunswick Swim Center, Westlake Rec Center, Rocky River Recreation Center, Shaker Heights Natatorium,
    # Solon Rec Center, Twinsburg Family Aquatic Center, Strongsville Rec Center pool, Brecksville pool);
    # NE Ohio park districts operate dozens of seasonal outdoor pools + year-round aquatic centers;
    # pool deck concrete + surrounding walkways + parking lots + building exteriors = recurring cleaning need;
    # summer = peak operational season = natural pitch window for pre-season exterior cleaning;
    # aquatic center directors sign vendor contracts; $1,000-$3,000/location; 10-pool system = $10K-$30K/year;
    # DISTINCT from YMCA pools (already targeted) — these are standalone municipal recreation facilities (added 2026-05-29 run 136)
    'aquatic center director', 'pool facility manager', 'swimming pool manager',
    'community pool director', 'aquatic facility manager', 'recreational aquatic manager',
    'natatorium manager', 'aquatic center manager', 'public pool manager',
    # Wireless & Telecom Retail Chains — AT&T, Verizon, T-Mobile, Boost, Cricket;
    # hundreds of NE Ohio strip-mall storefronts; district managers sign vendor contracts;
    # routing to Property Manager sequence (facility vendor contract angle) (added 2026-05-29 run 137)
    'wireless retail district manager', 'telecom retail manager', 'wireless store manager',
    'cell phone store manager', 'mobile retail manager', 'wireless district manager',
    'telecom district manager', 'wireless retail manager',
    # Uniform & Workwear Services — Cintas, Aramark, UniFirst, G&K Services, ALSCO;
    # large processing facilities + fleet vehicles; food-service/healthcare compliance angle;
    # routing to Property Manager sequence (facility management angle) (added 2026-05-29 run 137)
    'uniform services manager', 'laundry services manager', 'uniform district manager',
    'linen services manager', 'textile services manager', 'workwear services manager',
    'uniform operations manager', 'garment services manager',
    # Warehouse Club & Membership Retail — Costco, Sam's Club, BJ's Wholesale Club;
    # enormous parking lots + gas station concourses + building exteriors not caught by 'grocery chain';
    # routing to Property Manager sequence (multi-site facility management angle) (added 2026-05-29 run 138)
    'warehouse club manager', 'warehouse club general manager', 'wholesale club manager',
    'wholesale club district manager', 'warehouse club facilities manager', 'membership store manager',
    'warehouse store manager', 'membership warehouse manager', 'wholesale store manager',
    # Optical/Vision Centers (added 2026-05-30 run 139)
    'optometry district manager', 'vision center manager', 'optical center manager',
    'eyecare district manager', 'eye care center manager', 'optical district manager',
    'optometric practice manager', 'vision care manager',
    # Medical/Clinical Labs (added 2026-05-30 run 139)
    'laboratory district manager', 'lab district manager', 'clinical lab manager',
    'patient service center manager', 'laboratory facilities manager', 'lab operations manager',
    'laboratory operations manager', 'clinical laboratory manager',
    # Tax Preparation Offices (added 2026-05-30 run 139)
    'tax district manager', 'tax preparation manager', 'tax office manager',
    'tax center manager', 'tax services district manager', 'tax franchise manager',
    'tax preparation district manager',
    # Coffee & Drive-Through Beverage Chains (added 2026-05-30 run 140)
    'coffee district manager', 'coffee shop manager', 'coffee chain manager',
    'drive through manager', 'drive-through manager', 'quick service beverage manager',
    'coffee store manager',
    # Pet Supply Retail Chains — PetSmart, Petco, Pet Supplies Plus; grooming salon chemical spill compliance;
    # routing to Property Manager sequence (facility vendor contract angle) (added 2026-05-30 run 141)
    'pet supply district manager', 'pet store district manager', 'pet retail district manager',
    'pet supply store manager', 'pet retail manager', 'pet specialty district manager',
    # Hair & Nail Salon Chains — Great Clips, Sport Clips, Supercuts, Fantastic Sams, Floyd's Barbershop;
    # state cosmetology licensing + chemical spill compliance = exterior cleaning compliance need;
    # routing to Property Manager sequence (facility management / vendor contract angle) (added 2026-05-30 run 141)
    'salon district manager', 'hair salon district manager', 'salon regional manager',
    'barbershop district manager', 'beauty salon district manager', 'salon franchise manager',
    'nail salon district manager', 'spa district manager',
    # Coworking Spaces & Flex Offices (added 2026-05-30 run 142)
    'coworking space manager', 'flex office manager', 'coworking manager',
    'shared workspace manager', 'business center manager', 'executive suite manager',
    'shared office director', 'coworking director', 'flexible workspace manager',
    # Truck Stops & Travel Centers (added 2026-05-30 run 143)
    'truck stop manager', 'travel center manager', 'travel plaza manager',
    'truck stop general manager', 'travel center operations manager', 'fuel stop manager',
    'travel center area manager',
    # Ambulatory Surgery Centers (added 2026-05-30 run 143)
    'ambulatory surgery center manager', 'surgery center administrator', 'surgical center director',
    'outpatient surgery manager', 'asc administrator', 'surgery center operations manager',
    'surgical center operations manager', 'outpatient surgical administrator',
    # Boutique Fitness Studios (added 2026-05-30 run 143)
    'fitness studio manager', 'boutique fitness manager', 'fitness franchise owner',
    'studio director', 'fitness studio director', 'group fitness studio manager',
    # Commercial Truck & Heavy Equipment Dealers (added 2026-05-30 run 143)
    'commercial truck dealer manager', 'heavy equipment dealer manager', 'truck dealer general manager',
    'equipment dealer manager', 'commercial vehicle dealer manager', 'heavy equipment sales manager',
    'equipment dealer operations manager',
    # Wineries & Distilleries (added 2026-05-30 run 144)
    'winery manager', 'vineyard manager', 'winery general manager', 'distillery manager',
    'distillery general manager', 'tasting room manager',
    # Motorcycle & Powersport Dealers (added 2026-05-30 run 144)
    'motorcycle dealer manager', 'powersport dealer manager', 'motorcycle dealership manager',
    'motorcycle dealer general manager', 'powersports manager', 'motorcycle store manager',
    'motorsport dealer manager',
    # RV & Camper Dealers (added 2026-05-30 run 144)
    'rv dealer manager', 'rv dealership manager', 'rv dealer general manager', 'camper dealer manager',
    'recreational vehicle dealer manager', 'rv store manager', 'motorhome dealer manager',
    # Garden Centers & Nurseries (added 2026-05-30 run 145)
    'garden center manager', 'nursery manager', 'garden center district manager',
    'plant nursery manager', 'nursery district manager', 'garden supply manager',
    'greenhouse manager',
    # Marine/Boat Dealers (added 2026-05-30 run 146)
    'marine dealer manager', 'boat dealer manager', 'marina boat dealer manager',
    'yacht dealer manager', 'marine sales manager', 'boat dealership manager',
    'marine general manager', 'powerboat dealer manager', 'marine dealer general manager',
    # Ice Cream & Frozen Dessert Chains (added 2026-05-30 run 146)
    'ice cream franchise manager', 'frozen dessert manager', 'ice cream district manager',
    'ice cream store manager', 'frozen yogurt manager', 'dessert franchise owner',
    'ice cream general manager', 'soft serve manager',
    # Party/Event Rental Companies (added 2026-05-30 run 147)
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
    # Off-Price Apparel & Home Goods Retail — TJ Maxx, Marshalls, HomeGoods, Burlington, Ross;
    # routing to Property Manager sequence (multi-site FM/district vendor contract angle) (added 2026-05-30 run 149)
    'off-price retail district manager', 'discount apparel district manager', 'off price store manager',
    'value retail district manager', 'home goods district manager', 'off-price district manager',
    'discount fashion manager',
    # Truck Rental Companies — U-Haul, Penske, Ryder, Budget Truck;
    # routing to Property Manager sequence (facility management / lot maintenance angle) (added 2026-05-30 run 149)
    'truck rental district manager', 'moving truck rental manager', 'truck rental location manager',
    'rental truck fleet manager', 'moving truck manager', 'truck rental operations manager',
    # Lumber Yards & Building Supply Distributors — 84 Lumber, ABC Supply, Builders FirstSource;
    # routing to Property Manager sequence (facility / vendor contract angle) (added 2026-05-31 run 150)
    'lumber yard manager', 'building supply manager', 'lumber yard branch manager',
    'building materials branch manager', 'roofing supply manager', 'building supply branch manager',
    # Behavioral Health & Mental Health Clinics — Signature Health, Recovery Resources, Frontline Service;
    # routing to Property Manager sequence (facility / compliance angle) (added 2026-05-31 run 150)
    'behavioral health director', 'mental health clinic director', 'behavioral health clinic manager',
    'mental health facility manager', 'behavioral health regional director', 'substance abuse clinic manager',
    'addiction treatment center director', 'outpatient behavioral health manager',
    # Motorsports Venues & Racing Facilities — routing to Property Manager sequence (facility management angle)
    # Summit Motorsports Park, Mid-Ohio Sports Car Course, Autobahn Indoor Speedway; (added 2026-05-31 run 151)
    'speedway operations manager', 'motorsports venue manager', 'racetrack facilities manager',
    'motorsports park manager', 'racing venue director', 'karting facility manager',
    'indoor karting manager', 'speedway manager', 'raceway manager',
    # Print & Business Services Chains — routing to Property Manager sequence (franchise facility angle)
    # FedEx Office, UPS Store franchise owners, AlphaGraphics, Minuteman Press; (added 2026-05-31 run 151)
    'print center manager', 'print shop district manager', 'printing services manager',
    'fedex office manager', 'ups store franchise owner', 'business services manager',
    'shipping center manager', 'copy center manager',
    # Chiropractic Chains & Spinal Care Groups — The Joint Chiropractic, ChiroOne franchise owners;
    # Ohio chiropractic licensing = exterior appearance standard; routing to Property Manager sequence (added 2026-05-31 run 152)
    'chiropractic district manager', 'chiropractor practice manager', 'chiropractic clinic manager',
    'chiropractic regional manager', 'chiropractic franchise owner', 'spine center manager',
    'chiropractic practice director', 'spinal care manager',
    # Escape Rooms & Interactive Entertainment — Breakout Games, Scene 75, room2escape;
    # franchise owners sign vendor contracts; routing to Property Manager sequence (added 2026-05-31 run 152)
    'escape room manager', 'escape room franchise owner', 'escape room owner', 'escape room operator',
    'interactive entertainment manager', 'escape room general manager', 'escape room director',
    'immersive experience manager', 'entertainment venue franchise owner',
    # Charter Schools & Charter Management Organizations — Ohio charter authorizer compliance = exterior appearance standard;
    # CMO facilities directors sign multi-campus vendor contracts; routing to Property Manager sequence (added 2026-05-31 run 154)
    'charter school director', 'charter management director', 'charter school principal',
    'charter academy director', 'charter operations director', 'director of school operations',
    'charter principal', 'cmo facilities director',
    # Outdoor RV & Boat Storage Facilities — spring commissioning = peak pitch window (right now);
    # large paved/gravel surfaces accumulate winter salt + algae; owner-operators sign vendor contracts;
    # routing to Property Manager sequence (facility vendor contract angle) (added 2026-05-31 run 154)
    'rv storage manager', 'outdoor storage facility manager',
    'boat storage manager', 'marine dry storage manager', 'vehicle storage manager',
    # Ice Rinks & Indoor Ice Arenas — Palace Ice Arenas (Solon/Twinsburg), Mentor Ice Arena, OBM Arena;
    # summer = maintenance window (ice out = full exterior access); DISTINCT Apollo tags from sports complex;
    # routing to Property Manager sequence (facility management / summer maintenance window angle) (added 2026-05-31 run 155)
    'ice rink manager', 'ice arena manager', 'ice arena director', 'skating center director',
    'ice facility manager', 'ice sports manager', 'skating rink manager', 'hockey arena manager',
    # Sporting Goods Chains (added 2026-05-31 run 156)
    'sporting goods district manager', 'sporting goods store manager', 'sporting goods manager',
    'sporting goods regional manager', 'sports retail district manager', 'sports store manager',
    'athletic retail manager', 'sporting goods operations manager',
    # Tractor Supply Co. & Farm/Rural Supply Chains (added 2026-05-31 run 156)
    'tractor supply district manager', 'tractor supply store manager', 'farm supply district manager',
    'farm supply store manager', 'rural supply manager', 'farm store manager',
    'agricultural retail manager', 'farm supply operations manager',
    # Used Car Superstores & Independent Used Car Lots — routing to Property Manager sequence
    # (vendor contract / facility lot maintenance angle); CarMax, DriveTime, independent lots (added 2026-05-31 run 157)
    'used car lot manager', 'used car dealership manager', 'pre-owned vehicle manager',
    'used auto dealer manager', 'independent car dealer owner', 'used car district manager',
    'pre-owned sales manager', 'used car operations manager',
    # Outdoor Power Equipment Dealers — routing to Property Manager sequence
    # (facility lot / outdoor display yard maintenance angle); STIHL, Husqvarna, Cub Cadet dealers (added 2026-05-31 run 157)
    'power equipment dealer manager', 'outdoor power equipment manager', 'small engine dealer manager',
    'equipment dealer owner', 'power equipment store manager', 'lawn equipment dealer manager',
    'outdoor equipment manager',
    # Vocational & Trade Schools / CTE Centers — routing to Property Manager sequence
    # (facility maintenance / compliance angle); EHOVE, Auburn, CVCC, Portage Lakes (added 2026-05-31 run 157)
    'career technical director', 'vocational school director', 'trade school director',
    'cte director', 'career center principal', 'career technical center manager',
    'vocational education director', 'cte facilities manager',
    # Animal Shelters & Humane Societies — routing to Property Manager sequence
    # (facility/compliance angle); Cleveland APL, Summit APL, Geauga Humane, Lake APL (added 2026-05-31 run 158)
    'animal shelter director', 'animal shelter manager', 'humane society director',
    'animal control director', 'shelter operations manager', 'animal services director',
    'animal welfare director', 'adoption center manager', 'animal shelter executive director',
    # Campgrounds & RV Parks — routing to Property Manager sequence
    # (facility maintenance / seasonal prep angle); spring opening = peak pitch window (added 2026-05-31 run 158)
    'campground manager', 'campground director', 'rv park manager', 'camping resort manager',
    'campground owner', 'camp operations manager', 'campground general manager',
    'rv resort manager', 'camping facility manager', 'outdoor recreation manager',
    # Mobile Home Parks & Manufactured Housing Communities — routing to Property Manager sequence
    # (facility maintenance / vendor contract angle); 200+ NE Ohio communities (added 2026-05-31 run 158)
    'mobile home park manager', 'manufactured housing community manager', 'mobile home park director',
    'manufactured housing manager', 'community park manager', 'manufactured community director',
    'mobile home community manager', 'mobile home park operations manager',
    # Senior Adult Day Programs & Adult Day Care Centers — Ohio Dept of Aging licensing = exterior appearance standard;
    # routing to Property Manager sequence (facility/compliance angle); 60+ NE Ohio programs (added 2026-05-31 run 159)
    'adult day program director', 'adult day care director', 'senior day program manager',
    'adult day services director', 'adult day center manager', 'senior day services manager',
    'adult day health director', 'adult day program manager',
    # Diagnostic Imaging & Radiology Centers — Ohio DOH radiology licensing = exterior appearance standard;
    # routing to Property Manager sequence (facility/compliance angle); HealthSpan, UH Radiology, Summa (added 2026-05-31 run 159)
    'radiology center manager', 'imaging center manager', 'diagnostic imaging manager',
    'radiology practice manager', 'mri center manager', 'imaging director', 'radiology director',
    'diagnostic center manager',
    # Swim Schools & Aquatic Learn-to-Swim Programs — Ohio DOH pool licensing = exterior appearance standard;
    # PEAK SEASON RIGHT NOW; routing to Property Manager sequence (facility/compliance angle) (added 2026-05-31 run 159)
    'swim school director', 'swim school manager', 'swim academy director', 'swim school owner',
    'swim school franchise owner', 'aquatic learning director', 'learn to swim director',
    'swim program manager',
    # Massage Therapy & Wellness Chains — Massage Envy, Elements Massage, Hand & Stone, LaVida;
    # franchise owners sign vendor contracts independently; routing to property_manager sequence (added 2026-05-31 run 160)
    'massage therapy manager', 'massage center manager', 'wellness studio manager',
    'massage franchise owner', 'wellness center manager', 'spa franchise manager',
    'massage clinic manager', 'therapeutic massage manager',
    # Non-Profit & Social Service Organizations — Salvation Army, Catholic Charities, United Way, food banks;
    # executive directors sign vendor contracts; routing to property_manager sequence (added 2026-05-31 run 160)
    'nonprofit executive director', 'social services director', 'nonprofit facilities director',
    'nonprofit operations manager', 'thrift store district manager', 'food bank operations director',
    'community services manager', 'social service agency director',
    # Auto Glass Repair & Windshield Replacement Chains — Safelite, Glass America (Cleveland HQ);
    # district managers sign multi-location vendor contracts; routing to property_manager sequence (added 2026-05-31 run 161)
    'auto glass manager', 'auto glass district manager', 'windshield repair manager',
    'glass repair center manager', 'auto glass franchise owner', 'auto glass operations manager',
    'windshield replacement manager', 'auto glass general manager',
    # Furniture & Home Furnishings Retail Chains — Ashley, Value City, Bob's Discount Furniture;
    # district managers sign multi-location vendor contracts; routing to property_manager sequence (added 2026-05-31 run 161)
    'furniture store manager', 'furniture district manager', 'furniture retail manager',
    'home furnishings store manager', 'furniture store general manager',
    'furniture district operations manager', 'home furnishings district manager', 'furniture showroom manager',
    # Salon Suites & Booth Rental Studios — Sola Salon Studios, MY SALON Suite, Phenix Salon Suites;
    # franchise owners sign vendor contracts independently; routing to property_manager sequence (added 2026-05-31 run 161)
    'salon suite manager', 'salon suites director', 'salon suite franchise owner',
    'booth rental manager', 'salon suite operations manager', 'salon suite property manager',
    'salon suite general manager',
    # Tutoring Centers & Learning Centers — Kumon (50+ NE Ohio), Sylvan, Mathnasium, Huntington Learning;
    # franchise owners sign independently; routing to property_manager sequence (added 2026-06-01 run 162)
    'tutoring center director', 'learning center director', 'tutoring center manager',
    'learning center manager', 'tutoring franchise owner', 'kumon center director',
    'academic learning center manager', 'after school program director',
    # Med Spas & Aesthetic Clinics — European Wax Center (20+ NE Ohio), LaserAway, National Laser Institute;
    # franchise owners sign independently; routing to property_manager sequence (added 2026-06-01 run 162)
    'med spa manager', 'medical spa director', 'medical spa manager', 'aesthetic clinic manager',
    'medspa manager', 'medical aesthetics manager', 'cosmetic clinic manager',
    'european wax center manager', 'laser clinic manager', 'aesthetics director',
    # Dry Cleaning & Laundry Service Chains — Fox Cleaners (30+ NE Ohio), Martinizing, One Hour Cleaners;
    # DISTINCT from coin laundries (run 135); franchise owners + multi-location operators sign contracts;
    # routing to property_manager sequence (added 2026-06-01 run 162)
    'dry cleaning manager', 'dry cleaner manager', 'dry cleaning chain manager',
    'laundry service manager', 'dry cleaning franchise owner', 'laundry chain manager',
    'dry cleaning district manager', 'garment care manager',
    # Home Care Agencies & In-Home Health Services — Visiting Angels, Home Instead, Comfort Keepers;
    # routing to property_manager sequence (facility/vendor contract angle) (added 2026-06-01 run 163)
    'home care director', 'home health director', 'home care regional director',
    'home health regional director', 'home care agency director', 'in-home care director',
    'home care manager', 'home health manager', 'home care district manager',
    'visiting angels franchise owner', 'home instead franchise owner',
    # Pawn Shops & Cash Advance / Payday Loan Chains — Cashland/EZCorp, Advance America, ACE Cash Express;
    # routing to property_manager sequence (facility vendor contract angle) (added 2026-06-01 run 163)
    'pawn shop manager', 'pawn shop district manager', 'pawn shop owner', 'cash advance manager',
    'payday loan manager', 'check cashing manager', 'cashland manager', 'pawn store manager',
    'pawn shop operations manager', 'financial retail district manager',
    # Hearing Aid Centers & Audiology Clinics — HearingLife, Miracle-Ear, Beltone, Connect Hearing;
    # routing to property_manager sequence (facility vendor contract angle) (added 2026-06-01 run 163)
    'hearing center director', 'hearing aid center manager', 'audiology clinic manager',
    'hearing health director', 'hearing center district manager', 'audiologist practice manager',
    'hearing clinic manager', 'audiology district manager', 'hearing center operations manager',
    # Staffing & Temporary Employment Agencies — Robert Half, Manpower, Kelly Services, Adecco, Aerotek;
    # routing to property_manager sequence (facility vendor contract angle) (added 2026-06-01 run 164)
    'staffing branch manager', 'staffing district manager', 'workforce solutions manager',
    'employment agency manager', 'temp agency manager', 'staffing operations manager',
    'staffing agency director', 'workforce director',
    # Big Box Electronics Retail — Best Buy (10+ NE Ohio), Micro Center (Westgate Cleveland);
    # routing to property_manager sequence (facility vendor contract angle) (added 2026-06-01 run 164)
    'electronics retail district manager', 'electronics store district manager', 'best buy manager',
    'consumer electronics manager', 'electronics retail manager', 'big box electronics manager',
    'electronics district manager', 'consumer electronics district manager',
    # Rent-to-Own / Consumer Lease Chains — Rent-A-Center (25+ NE Ohio), Aaron's Holdings (15+ NE Ohio);
    # routing to property_manager sequence (facility vendor contract angle) (added 2026-06-01 run 164)
    'rent to own manager', 'rent-to-own manager', 'rent to own district manager',
    'consumer lease manager', 'furniture rental manager', 'appliance rental manager',
    'aarons store manager', 'rentacenter manager', 'rent to own district director',
    # Insurance Agency Offices — State Farm, Allstate, Erie Insurance, Nationwide, Farmers, AAA;
    # 500+ NE Ohio franchise agency offices; agency owners sign vendor contracts directly;
    # routing to property_manager sequence (client-facing exterior / vendor contract angle);
    # (added 2026-06-01 run 165)
    'insurance agency owner', 'insurance agency manager', 'insurance district manager',
    'insurance office manager', 'independent insurance agent', 'insurance franchise owner',
    'state farm agent', 'allstate agent', 'erie insurance agent', 'insurance agency director',
    # Orthopedic & Sports Medicine Clinics — OrthoNEOA, Cleveland Orthopedic & Spine, UH Orthopaedics;
    # DISTINCT from PT chains (run 126), urgent care (run 114), diagnostic imaging (run 159);
    # practice managers sign vendor contracts; routing to property_manager sequence (added 2026-06-01 run 166)
    'orthopedic practice manager', 'sports medicine manager', 'orthopedic clinic manager',
    'orthopedic surgery center manager', 'sports medicine director', 'orthopedic center manager',
    'sports medicine clinic manager', 'orthopedic group manager',
    # Financial Advisory & Wealth Management Offices — Edward Jones, Raymond James, Ameriprise;
    # DISTINCT from insurance agencies (run 165), bank branches (run 100);
    # individual advisors sign vendor contracts independently (no corporate FM);
    # routing to property_manager sequence (client-facing exterior / trust angle) (added 2026-06-01 run 166)
    'financial advisor owner', 'wealth management director', 'financial planning manager',
    'investment advisor manager', 'financial services office manager', 'wealth advisor owner',
    'financial district manager', 'investment office manager',
    # Waste Hauling & Dumpster Rental Companies — routing to property_manager sequence
    # (vendor contract / facility compliance angle) (added 2026-06-01 run 167)
    'waste hauler manager', 'waste management district manager', 'dumpster rental manager',
    'waste collection district manager', 'solid waste manager', 'waste operations manager',
    'commercial waste manager', 'residential waste manager',
    # Dermatology & Skin Care Medical Groups — routing to property_manager sequence
    # (facility management / compliance angle) (added 2026-06-01 run 167)
    'dermatology practice manager', 'dermatology clinic manager', 'dermatology group administrator',
    'skin care clinic manager', 'dermatology office manager', 'dermatology district manager',
    'dermatology center director', 'dermatology regional manager',
    # Hospice & Palliative Care Facilities — routing to property_manager sequence
    # (facility management / compliance angle) (added 2026-06-01 run 167)
    'hospice administrator', 'hospice director', 'hospice facility manager', 'palliative care director',
    'hospice operations director', 'hospice regional director', 'inpatient hospice manager',
    'hospice center director',
    # Community Colleges & Technical Institutes — routing to property_manager sequence
    # (campus facilities / vendor contract angle) (added 2026-06-01 run 168)
    'community college facilities director', 'community college facilities manager',
    'college campus facilities director', 'higher education facilities director',
    'campus facilities director', 'community college maintenance director',
    'college grounds director', 'technical college facilities manager',
    # Medical Equipment & Device Manufacturers — routing to property_manager sequence
    # (FDA GMP / facility compliance angle) (added 2026-06-01 run 168)
    'medical device operations manager', 'medical equipment operations manager',
    'medical device facility manager', 'medical manufacturing manager',
    'medical equipment plant manager', 'medical device plant operations manager',
    'biomedical equipment manager', 'medical device manufacturing director',
    # Pain Management & Spine Clinics — routing to property_manager sequence
    # (Ohio Medical Board licensing / facility compliance angle) (added 2026-06-01 run 168)
    'pain management clinic manager', 'pain management practice manager',
    'pain clinic director', 'pain management director',
    'pain center manager', 'interventional pain manager',
    'pain management administrator', 'pain medicine practice manager',
    # Skilled Nursing Facilities & Long-Term Care Centers — routing to property_manager sequence
    # (CMS Five-Star Rating compliance / ODH facility licensing angle) (added 2026-06-01 run 169)
    'skilled nursing facility administrator', 'nursing home administrator',
    'long-term care administrator', 'director of nursing home operations',
    'snf administrator', 'nursing facility director',
    'post-acute care director', 'skilled nursing regional director',
    # Orthodontic Practices & Pediatric Dental Groups — routing to property_manager sequence
    # (Ohio State Dental Board / AAO accreditation compliance angle) (added 2026-06-01 run 169)
    'orthodontic practice manager', 'orthodontist office manager',
    'orthodontic district manager', 'pediatric dental practice manager',
    'orthodontic group director', 'orthodontic operations director',
    'pediatric dental district manager', 'orthodontic regional manager',
    # County Fairgrounds & Agricultural Exhibition Facilities — routing to property_manager sequence
    # (Ohio Dept of Agriculture / county fair board licensing / seasonal maintenance angle) (added 2026-06-01 run 170)
    'fairgrounds manager', 'county fair director', 'exhibition grounds manager',
    'fairgrounds facilities manager', 'county fairgrounds director', 'fair operations manager',
    'agricultural fair manager', 'fair facility director', 'fair superintendent',
    # Title Companies & Real Estate Closing Offices — routing to property_manager sequence
    # (client-facing exterior / professional trust signal angle) (added 2026-06-01 run 170)
    'title company manager', 'title office manager', 'title branch manager',
    'settlement agent manager', 'closing attorney office manager', 'title company branch manager',
    'real estate closing manager', 'title services manager', 'title operations manager',
    # Fire Stations & Fire Departments — routing to property_manager sequence
    # (ISO 2 rating / facility maintenance compliance angle) (added 2026-06-01 run 171)
    'fire station manager', 'fire department director', 'fire chief', 'fire rescue director',
    'fire station director', 'fire district manager', 'fire station facilities manager',
    'fire department facilities coordinator',
    # Home Builders & Residential Real Estate Developers — routing to property_manager sequence
    # (first impression / model home curb appeal / June peak selling season angle) (added 2026-06-01 run 171)
    'home builder manager', 'residential construction manager', 'new home sales manager',
    'community sales manager', 'home development manager', 'residential developer manager',
    'new home community manager', 'model home manager',
    # Propane & Fuel Oil Delivery Companies — routing to property_manager sequence
    # (OSHA SPCC / EPA compliance / fuel staining = regulatory liability angle) (added 2026-06-01 run 171)
    'propane district manager', 'fuel oil manager', 'propane operations manager',
    'fuel delivery manager', 'propane service manager', 'heating oil manager',
    'energy delivery manager', 'fuel distribution manager',
    # Dance Studios & Performing Arts Schools (added 2026-06-01 run 172)
    'dance studio owner', 'dance studio manager', 'dance studio director', 'performing arts director',
    'dance academy director', 'dance school director', 'dance studio franchise owner',
    'performing arts school manager',
    # Martial Arts Academies & Combat Sports Studios (added 2026-06-01 run 172)
    'martial arts school owner', 'karate school owner', 'martial arts academy director',
    'dojo owner', 'martial arts instructor', 'karate instructor', 'taekwondo instructor',
    'bjj gym owner', 'jiu-jitsu academy owner', 'krav maga instructor',
    # Wedding Venues & Special Occasion Facilities — fills title routing gap; 'wedding venue' org keyword
    # already in list (run 108) but wedding coordinator/venue coordinator titles were absent from DANNY_TITLES;
    # routing to property_manager sequence (facility vendor contract / appearance angle) (added 2026-06-02 run 173)
    'wedding coordinator', 'venue coordinator', 'wedding venue coordinator', 'bridal venue manager',
    'wedding venue owner', 'wedding estate manager', 'bridal hall manager', 'event coordinator',
    # Outdoor Recreation & Adventure Parks — mini-golf, go-karts, batting cages, axe throwing venues;
    # owners/operators sign vendor contracts; routing to property_manager sequence (added 2026-06-02 run 173)
    'mini golf manager', 'miniature golf manager', 'go-kart park manager', 'go kart park owner',
    'batting cage manager', 'axe throwing venue manager', 'outdoor recreation park owner',
    'family fun park manager', 'outdoor entertainment park manager',
    # Charter Fishing & Lake Erie Boat Tour Operators — owner-operators route to property_manager sequence
    # (vendor contract / facility maintenance angle); peak walleye season June-August (added 2026-06-02 run 174)
    'charter boat captain', 'fishing charter owner', 'charter fishing owner', 'boat charter owner',
    'lake charter captain', 'charter boat operator', 'fishing guide owner', 'charter captain',
    # VFW Posts & American Legion Halls — post commanders route to property_manager sequence
    # (facility management / vendor contract angle); 150+ NE Ohio posts (added 2026-06-02 run 174)
    'vfw post commander', 'american legion commander', 'post commander', 'veterans post director',
    'veterans facility manager', 'post adjutant', 'vfw commander', 'legion post adjutant',
    # Law Firms & Legal Office Buildings — administrators route to property_manager sequence
    # (professional appearance / facility vendor contract angle); downtown + suburban NE Ohio offices (added 2026-06-02 run 174)
    'law firm administrator', 'legal office manager', 'law office manager', 'legal administrator',
    'law firm facilities manager', 'legal facilities director', 'office services manager',
    'law firm operations manager',
    # Independent Dental Practices — solo/small-group offices (DISTINCT from DSO chains run 123);
    # Ohio State Dental Board licensing = exterior appearance standard; routing to property_manager sequence (added 2026-06-02 run 175)
    'dental office manager', 'dental practice manager', 'dental administrator',
    'dental office administrator', 'dental practice director', 'general dentistry manager',
    'dental clinic administrator', 'dental office director',
    # Accounting & CPA Firms — post-tax-season window; client-facing professional exterior;
    # routing to property_manager sequence (professional trust / vendor contract angle) (added 2026-06-02 run 175)
    'cpa firm manager', 'accounting firm administrator', 'accounting practice manager',
    'cpa office administrator', 'accounting firm director', 'public accounting manager',
    'cpa managing partner', 'audit firm manager',
    # Flooring & Tile Showrooms — delivery truck staining; exterior appearance for customer-facing retail;
    # routing to property_manager sequence (facility vendor contract angle) (added 2026-06-02 run 175)
    'flooring showroom manager', 'flooring store manager', 'flooring district manager',
    'tile showroom manager', 'carpet store manager', 'flooring operations manager',
    'flooring franchise owner', 'flooring store director',
    # Summer Day Camps & Youth Day Programs — Ohio DJFS child care licensing = exterior appearance standard;
    # routing to property_manager sequence (facility/compliance angle) (added 2026-06-02 run 176)
    'day camp director', 'summer camp director', 'youth program director', 'youth day camp director',
    'summer youth director', 'camp director', 'day camp manager', 'youth summer program manager',
    # B2B Wholesale Supply Houses (Plumbing, HVAC, Electrical) — routing to property_manager sequence
    # (facility vendor contract angle); branch managers sign vendor contracts (added 2026-06-02 run 178)
    'plumbing supply branch manager', 'hvac supply branch manager', 'electrical supply branch manager',
    'plumbing wholesale manager', 'hvac wholesale manager', 'mechanical supply manager',
    'industrial supply branch manager', 'supply house manager', 'wholesale distribution manager',
    # School Bus Companies & Charter Motor Coach Operators — routing to property_manager sequence
    # (facility vendor contract / depot maintenance angle) (added 2026-06-02 run 178)
    'school bus company manager', 'student transportation manager', 'bus fleet manager',
    'charter bus manager', 'motor coach manager', 'school bus operations manager',
    'bus transportation manager', 'student transport director',
    # USPS & Postal Service Facilities — routing to property_manager sequence
    # (federal facility maintenance / compliance angle) (added 2026-06-02 run 179)
    'postmaster', 'postal facility manager', 'usps facility manager', 'postal station manager',
    'mail processing facility manager', 'postal district manager', 'postal operations supervisor',
    'postal service manager', 'post office manager', 'usps operations manager',
    # Construction & Industrial Equipment Rental Companies — routing to property_manager sequence
    # (OSHA SPCC stormwater compliance / facility vendor contract angle) (added 2026-06-02 run 179)
    'equipment rental branch manager', 'equipment rental manager', 'rental equipment manager',
    'rental yard manager', 'equipment rental operations manager', 'rental branch general manager',
    'construction equipment rental manager', 'heavy equipment rental manager',
    # Public Housing Authorities & Affordable Housing — CMHA, AMHA, Lake/Lorain/Medina CMHAs;
    # HUD-funded direct-award vendor contracts; routing to property_manager sequence (added 2026-06-02 run 180)
    'housing authority maintenance director', 'housing authority facilities manager', 'public housing director',
    'housing development manager', 'housing authority property manager', 'affordable housing director',
    'public housing facilities manager', 'housing authority operations manager',
    # TV & Radio Broadcasting Stations — WEWS, WJW Fox 8, WKYC, iHeartMedia, Cumulus Media Cleveland;
    # brand image = on-camera exterior = non-negotiable appearance; routing to property_manager sequence (added 2026-06-02 run 180)
    'broadcast facility manager', 'station operations manager', 'television station manager',
    'broadcast operations director', 'radio station manager', 'media facility director',
    'broadcast engineering manager', 'television facility manager',
    # Pharmaceutical Manufacturing & Research Facilities — STERIS Corporation (Mentor OH), Ferro Corporation;
    # FDA 21 CFR Part 211 compliance; routing to property_manager sequence (added 2026-06-02 run 180)
    'pharmaceutical plant manager', 'pharma facility manager', 'pharmaceutical operations manager',
    'drug manufacturing manager', 'pharmaceutical plant superintendent', 'biotech facility manager',
    'pharmaceutical manufacturing manager', 'pharmaceutical plant operations manager',
    # Scrap Metal Dealers & Metal Recycling Facilities — routing to property_manager sequence (added 2026-06-02 run 181)
    'scrap yard manager', 'metal recycling manager', 'scrap metal operations manager',
    'recycling facility manager', 'scrap operations director', 'yard operations manager',
    'metal recycling director', 'scrap metal yard manager',
    # Data Centers & Colocation Facilities — routing to property_manager sequence (added 2026-06-02 run 181)
    'data center manager', 'data center operations manager', 'colocation facility manager',
    'data center facilities manager', 'colo facility manager', 'infrastructure manager',
    'data center general manager', 'colocation operations manager',
    # Gymnastics Centers & Tumbling Academies — routing to property_manager sequence (added 2026-06-02 run 182)
    'gymnastics center director', 'gymnastics gym owner', 'tumbling academy director',
    'gymnastics academy director', 'cheerleading gym owner', 'cheer gym director',
    'gymnastics studio manager', 'cheer academy owner',
    # Beverage Distribution Centers & Soft Drink Bottlers — routing to property_manager sequence (added 2026-06-02 run 182)
    'beverage distribution manager', 'beverage district manager', 'soft drink distribution manager',
    'beverage depot manager', 'bottling operations manager', 'beverage route manager',
    'beer distributor manager', 'beverage operations director',
    # Electric Utility Substations & Power Distribution Facilities — routing to property_manager sequence
    # (EPA SPCC/NPDES compliance / facility vendor contract angle) (added 2026-06-02 run 183)
    'electric utility facilities manager', 'utility site manager', 'substation facility manager',
    'power utility facility manager', 'electric utility operations manager', 'utility facilities director',
    'power distribution facility manager', 'electric cooperative facilities manager',
    # Private EMS & Ambulance Service Depots — routing to property_manager sequence
    # (OSHA bloodborne pathogens / EPA hazmat compliance angle) (added 2026-06-02 run 183)
    'ems operations manager', 'ambulance service manager', 'emergency medical services director',
    'ems director', 'ambulance operations director', 'medical transport manager',
    'ems district manager', 'emergency services manager',
    # Industrial Gas & Welding Supply — routing to property_manager sequence
    # (DOT hazmat / EPA Tier I compliance angle) (added 2026-06-02 run 184)
    'industrial gas manager', 'welding supply manager', 'gas distribution manager',
    'cylinder plant manager', 'compressed gas manager', 'welding supply branch manager',
    'industrial gas branch manager', 'gas depot manager',
    # Commercial Printing Plants — routing to property_manager sequence
    # (EPA VOC permit / OSHA 29 CFR 1910.22 compliance angle) (added 2026-06-02 run 184)
    'printing plant manager', 'commercial printing manager', 'print plant operations manager',
    'publishing facility manager', 'offset printing manager', 'print manufacturing manager',
    'commercial print manager', 'printing plant superintendent',
    # Aquatic Management Companies — company-level FMs who manage 10-50 pools for HOAs/apartments/municipalities;
    # DISTINCT from facility-level pool managers (run 136 — aquatic center director, pool facility manager);
    # route to property_manager sequence (facility vendor contract angle) (added 2026-06-03 run 185)
    'aquatics operations manager', 'pool management director', 'aquatics services manager',
    'pool operations manager', 'aquatic operations director', 'pool services director',
    'aquatics program director', 'aquatic services manager',
    # Crane & Rigging Companies — segment #167 (added 2026-06-03 run 186)
    'crane yard manager', 'rigging manager', 'crane operations manager', 'lift superintendent',
    'crane company manager', 'rigging contractor manager', 'crane service director',
    'lifting services manager',
    # Municipal Water & Wastewater Treatment — segment #168 (added 2026-06-03 run 186)
    'water plant superintendent', 'wastewater treatment manager', 'utilities facilities manager',
    'water treatment plant manager', 'sewer district operations manager', 'public utilities director',
    'water utilities manager', 'wastewater plant superintendent',
    # Ice Rinks & Hockey Facilities — segment #169; new titles added run 187 (deduped against run 155 block)
    'arena manager', 'rink operations manager', 'ice complex manager',
    # Bowling Centers & Family Entertainment Centers — segment #170; new titles added run 187 (deduped against run 120 block)
    'entertainment venue manager', 'bowling operations manager',
    'fec manager', 'entertainment complex manager',
    # EV Charging Network Operators — segment #171; ChargePoint (100+ NE Ohio), EVgo, Blink, BP Pulse, Electrify America;
    # concrete charging pads = rubber streaks, brake dust, coolant leaks; canopy structures = bird droppings + grime;
    # regional network ops managers sign vendor contracts for all stations in a territory;
    # $500-$1,500/location; 20-station regional deal = $10K-$30K/year; zero competitors cold-calling these FMs;
    # NE Ohio EV infrastructure growing fast (I-90/I-77 corridors); first pull June 8 Cuyahoga (added 2026-06-03 run 188)
    'ev charging station manager', 'electric vehicle charging manager', 'ev network operations manager',
    'charging infrastructure manager', 'ev facility manager', 'charging station operations director',
    'ev charging operations manager', 'ev infrastructure director',
    # Steel Service Centers & Metal Distributors — segment #172; Olympic Steel (Bedford Heights HQ),
    # Metals USA (Independence OH), Reliance Steel, Chapel Steel, Service Center Corp;
    # OSHA 1910.22 + EPA NPDES SWPPP compliance; $2,000–$8,000/visit; first pull June 8 Cuyahoga (added 2026-06-03 run 189)
    'steel service center manager', 'metal service center manager', 'metals distribution manager',
    'steel distribution manager', 'steel processing manager', 'metals operations director',
    'service center branch manager', 'metals facility manager',
    # Fraternal & Social Organizations — segment #173; Elks, Moose, Eagles, Knights of Columbus;
    # DISTINCT from VFW/Legion (run 174); 400+ NE Ohio locations; zero competitors; first pull June 8 Cuyahoga (added 2026-06-03 run 189)
    'lodge manager', 'lodge administrator', 'fraternal lodge manager', 'elks lodge manager',
    'moose lodge manager', 'social club manager', 'hall manager', 'fraternal organization manager',
    # Residential Group Homes & DODD-Licensed Care Facilities — segment #174; Ohio DODD Medicaid waiver
    # residential programs: group homes (5-8 residents), ICF/DD, supported living, community living;
    # DISTINCT from skilled nursing (run 169), senior assisted living (run 94), home care agencies (run 163);
    # DODD Rule 5123:2-3 + CMS CoP exterior cleanliness compliance; routing to property_manager sequence
    # (facility compliance / vendor contract angle); first pull June 8 Cuyahoga (added 2026-06-03 run 190)
    'group home administrator', 'group home director', 'residential group home manager',
    'dodd home manager', 'icf administrator', 'supported living manager',
    'residential care manager', 'community living manager',
    # Restaurant Equipment & Commercial Kitchen Supply Companies — segment #175 (added 2026-06-03 run 191)
    'restaurant equipment manager', 'commercial kitchen supply manager', 'food service equipment manager',
    'restaurant supply manager', 'kitchen equipment district manager', 'food equipment operations manager',
    'restaurant supply district manager', 'commercial food equipment manager',
    # Specialty Chemical Manufacturers & Polymer Plants — segment #176 (added 2026-06-03 run 191)
    'chemical plant manager', 'chemical operations manager', 'specialty chemical manager',
    'polymer plant manager', 'chemical facility manager', 'chemical manufacturing manager',
    'chemical plant superintendent', 'polymer operations manager',
    # Federal Government & VA Healthcare Facilities — segment #177; DISTINCT from municipal government (run 124
    # which covers city/county/township); these are FEDERAL-tier FMs at VA medical centers, IRS service
    # centers, NASA Glenn, federal courthouses, National Guard armories, GSA-managed buildings;
    # routing to property_manager sequence (regulatory compliance / facility management angle) (added 2026-06-03 run 192)
    'federal building manager', 'va facility manager', 'veterans affairs facility manager',
    'federal facilities manager', 'federal property manager', 'national guard facilities manager',
    'army reserve facilities manager', 'federal facility manager',
    # Ready-Mix Concrete & Asphalt Production Facilities — segment #178; DISTINCT from manufacturing (run 118);
    # concrete dust + asphalt residue + aggregate runoff; OSHA 1910.22 + OEPA NPDES SWPPP compliance;
    # Shelly Company (Medina HQ), Aggregate Industries, CEMEX, Martin Marietta NE Ohio;
    # routing to property_manager sequence (OSHA/OEPA compliance angle) (added 2026-06-03 run 192)
    'ready mix concrete manager', 'concrete plant manager', 'concrete plant superintendent',
    'asphalt plant manager', 'hot mix asphalt manager', 'concrete production manager',
    'asphalt plant superintendent', 'quarry plant manager', 'aggregate plant manager',
    'batch plant manager', 'concrete operations manager', 'asphalt operations manager',
    # County Correctional Facilities & Detention Centers — segment #179; DISTINCT from municipal (run 124)
    # and federal government (run 177); county sheriff-operated jails + juvenile detention centers;
    # ACA accreditation + OEPA NPDES SWPPP = exterior appearance standard; zero competitors;
    # routing to property_manager sequence (government compliance / facility management angle) (added 2026-06-03 run 193)
    'jail administrator', 'detention facility manager', 'corrections facilities director',
    'county jail administrator', 'county jail manager', 'detention center director',
    'sheriff facilities manager', 'correctional facility manager', 'corrections facility director',
    'juvenile detention director', 'detention operations manager', 'county corrections manager',
    # Inpatient Rehabilitation Hospitals & Long-Term Acute Care (LTAC) Facilities — segment #180
    # DISTINCT from skilled nursing (run 169), outpatient PT (run 126), hospital main campuses (run 124);
    # CMS CoP Section 482 + JCAHO accreditation = exterior appearance standard;
    # routing to property_manager sequence (regulatory compliance / facility management angle) (added 2026-06-03 run 193)
    'rehabilitation hospital administrator', 'rehabilitation hospital director',
    'ltac administrator', 'inpatient rehabilitation director', 'long-term acute care director',
    'rehab hospital manager', 'ltac facility manager', 'inpatient rehab director',
    'ltac hospital administrator', 'rehab hospital administrator', 'acute rehabilitation director',
    # K-12 Private & Parochial Schools — segment #181; DISTINCT from public school districts (run 119)
    # and churches/parishes (run 110); private school facilities directors manage vendor contracts
    # independently; routing to property_manager sequence (facility management angle) (added 2026-06-03 run 194)
    'private school facilities director', 'private school building manager',
    'independent school facilities manager', 'diocesan facilities manager',
    'catholic school facilities manager', 'prep school facilities director',
    'independent school superintendent', 'parochial school administrator',
    'private school operations manager',
    # County Fairgrounds & Agricultural Exhibit Facilities — segment #182; DISTINCT from sports venues
    # (run 127), convention centers (run 128), event venues (run 108); county agricultural society FMs
    # sign direct-award contracts; routing to property_manager sequence (added 2026-06-03 run 194)
    'fairgrounds manager', 'county fair director', 'fairgrounds director',
    'fairgrounds facilities manager', 'agricultural fair manager', 'county fair manager',
    'fairgrounds operations manager', 'fairgrounds superintendent', 'fair operations director',
    # Aerospace & Defense Manufacturers — segment #183; Parker Hannifin, TransDigm, Ducommun;
    # AS9100D + ITAR compliance = documented facility maintenance requirement;
    # routing to property_manager sequence (facility management / compliance angle) (added 2026-06-04 run 195)
    'aerospace facilities manager', 'defense plant manager', 'aerospace plant manager',
    'aerospace operations manager', 'aerospace manufacturing manager',
    'defense facilities manager', 'aerospace plant superintendent', 'defense manufacturing manager',
    # Precision Machining & CNC Machine Shops — segment #184; DISTINCT ORG TAGS from general manufacturing (run 118);
    # ISO 9001 / AS9100 compliance; 500+ NE Ohio machine shops; direct vendor contracts with shop owners/managers;
    # routing to property_manager sequence (facility vendor contract angle) (added 2026-06-04 run 195)
    'machine shop manager', 'precision machining manager', 'cnc operations manager',
    'precision manufacturing manager', 'machine shop superintendent',
    'cnc shop manager', 'precision machining superintendent', 'machine shop owner',
    # Public Transit Agencies & Bus Depot Facilities — segment #185; routing to property_manager sequence
    # GCRTA, Metro RTA, SARTA, LAKETRAN; FTA ADA compliance angle; (added 2026-06-05 run 196)
    'transit operations director', 'bus depot operations manager', 'transit system facilities manager',
    'transit depot manager', 'transit agency facilities manager', 'bus garage manager',
    'public transit facilities director', 'transit maintenance facilities manager',
    # Industrial Real Estate & Logistics Park Management — segment #186; routing to property_manager sequence
    # ProLogis, Duke Realty, Scannell; DISTINCT from Carla's commercial RE brokers (run 176); (added 2026-06-05 run 196)
    'industrial property manager', 'logistics real estate manager', 'warehouse property manager',
    'industrial park manager', 'logistics park manager', 'industrial campus manager',
    'industrial portfolio manager', 'warehouse campus manager',
    # Indoor Shooting Ranges & Archery Centers — segment #187; routing to property_manager sequence
    # (facility vendor contract / seasonal prep angle) (added 2026-06-06 run 197)
    'shooting range manager', 'gun range manager', 'indoor range manager',
    'archery center director', 'shooting sports manager', 'firearms range manager',
    'gun range owner', 'archery range owner',
    # Cannabis Cultivation & Processing Facilities — segment #188; routing to property_manager sequence
    # (Ohio State Board of Pharmacy licensing / facility compliance angle); DISTINCT from dispensaries (run 135)
    # (added 2026-06-06 run 197)
    'cannabis cultivation manager', 'grow facility manager', 'cultivation director',
    'cannabis operations manager', 'cannabis plant manager', 'marijuana operations manager',
    'grow operations manager', 'cannabis facility manager',
    # Multi-Site Fitness Chain District Operations — segment #189; routing to property_manager sequence
    # (multi-site vendor contract / facility management angle); DISTINCT from individual gym managers
    # (gym manager/fitness director run 99) and boutique studio owners (fitness franchise owner run 143);
    # district-level fitness chain FMs sign one contract covering all locations in their territory
    # (added 2026-06-07 run 198)
    'health club district manager', 'gym district manager', 'fitness chain operations manager',
    'multi-club manager', 'fitness operations director', 'fitness area manager',
    'health club operations director', 'gym operations manager',
    # Cold Storage & Refrigerated Warehouse Networks — segment #190; routing to property_manager sequence
    # (USDA AMS cold storage licensing / EPA SPCC-NPDES compliance / facility management angle);
    # DISTINCT from food manufacturers with cold storage (run 127 cold storage manager already in list);
    # standalone cold storage REIT/network FMs — Lineage Logistics, Americold, US Cold Storage
    # (added 2026-06-07 run 198)
    'cold storage facility manager', 'cold storage operations manager', 'refrigerated warehouse manager',
    'temperature controlled facility manager', 'cold chain facility manager',
    'cold storage district manager', 'refrigerated storage manager', 'cold storage regional manager',
    # Intermodal Rail Terminals & Freight Hub Facilities — segment #191; routing to property_manager sequence
    # (OSHA 29 CFR 1926 + EPA SPCC stormwater compliance angle); CSX Collinwood Terminal, NS Cleveland,
    # Wheeling & Lake Erie Railway; first pull June 8 Cuyahoga (added 2026-06-08 run 199)
    'rail terminal manager', 'intermodal terminal manager', 'freight terminal manager',
    'rail yard manager', 'intermodal facility manager', 'freight hub manager',
    'rail operations manager', 'terminal operations director', 'rail terminal superintendent',
    # Commercial Parking Management Portfolio Companies — segment #192; routing to property_manager sequence
    # (facility management / multi-site vendor contract angle); SP+, Impark, ABM Parking, Lanier Parking;
    # DISTINCT from individual parking structure managers (run 128); first pull June 8 Cuyahoga (added 2026-06-08 run 199)
    'parking management regional manager', 'parking portfolio manager', 'parking network manager',
    'parking operations regional manager', 'parking management director', 'parking services director',
    'valet parking manager', 'parking management operations director', 'parking company regional director',
    # Co-Packing & Contract Manufacturing Facilities — segment #193; routing to property_manager sequence
    # (FDA 21 CFR + OSHA compliance angle); DISTINCT from food plants (run 127) + general mfg (run 118)
    # first pull Lake County June 15 (added 2026-06-09 run 200)
    'co-packing operations manager', 'contract manufacturing manager', 'packaging plant manager',
    'co-manufacturing director', 'contract packaging manager', 'co-pack facility manager',
    'toll manufacturing manager', 'packaging operations manager',
    # Semiconductor & PCB/Electronics Manufacturers — segment #194; routing to property_manager sequence
    # (ISO 14001 + OEPA NPDES compliance angle); DISTINCT from aerospace (run 183) + medical device (run 168)
    # Parker Hannifin Electronics (Mayfield Heights), API Technologies, Greatbatch (Lake County)
    # first pull Lake County June 15 (added 2026-06-09 run 200)
    'semiconductor plant manager', 'pcb manufacturing manager', 'circuit board plant manager',
    'electronics plant manager', 'printed circuit board manager', 'electronics manufacturing manager',
    'semiconductor facility manager', 'electronics operations manager',
    # Boat Repair & Marine Service Centers — segment #195; routing to property_manager sequence
    # (facility maintenance / vendor contract angle); DISTINCT from marinas (run 109), boat dealers (run 146),
    # charter fishing (run 174); repair yards + equipment bays = algae + oil staining;
    # first pull Lake County June 15 (added 2026-06-10 run 201)
    'marine service manager', 'boat yard manager', 'marine repair manager', 'boat repair manager',
    'marine service director', 'boat yard superintendent', 'marine maintenance supervisor',
    'marine operations director',
    # Craft Breweries & Taprooms — segment #196; routing to property_manager sequence
    # (facility maintenance / vendor contract angle); DISTINCT from restaurants (run 106);
    # Willoughby Brewing = flagship Lake County target; first pull Lake County June 15 (added 2026-06-11 run 202)
    # NOTE: 'brewery manager', 'taproom manager', 'craft brewery manager', 'brewery operations manager',
    # 'taproom director', 'brewery general manager' already in list (run 129 block) — adding NEW-ONLY titles
    'brewery director', 'production brewery manager',
    'beverage facility manager', 'brewery owner',
    # General Aviation (FBO) & Private Airport Terminals — segment #197; routing to property_manager sequence
    # (FAA Part 139 + OSHA SPCC compliance / facility management angle); DISTINCT from commercial airports
    # (run 128 — CLE Hopkins, CAK Akron-Canton); FBOs at Cuyahoga County Airport (CGF), Willoughby Hopkins
    # Airport (LNN — Lake County June 15 flagship target), Akron Executive Airport (AKR), Lorain County
    # Airport (LOR); ramp concrete + hangar floors + terminal exteriors = oil/fuel/exhaust staining;
    # $3K–$10K/visit; zero competitors cold-calling FBO managers; first pull Lake County June 15
    # (added 2026-06-12 run 203)
    'fbo manager', 'fixed base operator manager', 'general aviation manager',
    'private aviation manager', 'aviation terminal manager', 'ramp operations manager',
    'executive aviation manager', 'aircraft hangar manager',
    # Commercial/Wholesale Nursery & Greenhouse Production Facilities — segment #198;
    # routing to property_manager sequence (facility vendor contract / compliance angle)
    # Lake County June 15 first pull (added 2026-06-13 run 204)
    'nursery operations manager', 'greenhouse production manager', 'wholesale nursery manager',
    'commercial nursery manager', 'growing operations director', 'plant production manager',
    'nursery facility manager', 'greenhouse operations manager',
    # Portable Restroom Rental & Event Sanitation Companies — segment #199; routing to property_manager sequence
    # (EPA NPDES stormwater compliance / facility vendor contract angle); DISTINCT from waste haulers (run 167);
    # staging yards + service yards = concrete chemical residue; Mr. John, Porta-Jon, United Site Services;
    # first pull Lorain June 22 (added 2026-06-15 run 206)
    'portable restroom manager', 'portable sanitation manager', 'sanitation services manager',
    'porta potty manager', 'portable toilet manager', 'field sanitation manager',
    'restroom trailer manager', 'portable restroom regional manager', 'sanitation fleet manager',
    # FQHCs & Community Health Centers — segment #200; routing to property_manager sequence
    # (HRSA + OSHA + ODH licensing compliance angle); DISTINCT from hospital campuses (run 124),
    # urgent care (run 114), behavioral health (run 150), outpatient medical (run 101);
    # first pull Lorain June 22 (added 2026-06-16 run 207)
    'fqhc administrator', 'community health center director', 'federally qualified health center director',
    'community clinic director', 'neighborhood health center manager', 'public health facilities manager',
    'health district facilities director', 'community health center administrator',
    # Steel Fabrication & Structural Steel Shops — segment #201; routing to property_manager sequence
    # (OSHA 1910.22 / OEPA NPDES compliance angle); DISTINCT from steel service centers (run 189)
    # and general manufacturing (run 118); first pull Lorain June 22 (added 2026-06-17 run 208)
    'steel fabrication plant manager', 'structural steel operations manager', 'steel fabricator superintendent',
    'fabrication shop manager', 'structural fab manager', 'metal fabrication plant manager',
    'steel shop superintendent', 'fabrication facility manager',
    # Municipal & Public Recreation Centers / Community Pools — segment #202; routing to property_manager sequence;
    # Ohio Dept. Health aquatic sanitation + OSHA 1910.141 compliance angle; first pull Lorain June 22
    # (added 2026-06-18 run 209)
    'parks and recreation director', 'recreation center manager', 'aquatics director',
    'community center manager', 'parks facilities manager', 'recreation facility manager',
    'aquatics manager', 'aquatics facility manager',
    # Private & Independent Colleges and Universities — Segment #203; routing to property_manager sequence
    # (HLC accreditation facility appearance standards / endowment-funded FM budget angle);
    # DISTINCT from K-12 school districts (run 119) and vocational/trade schools (run 157);
    # Oberlin College (Lorain), Lake Erie College (Lake), Baldwin Wallace/John Carroll/Notre Dame (Cuyahoga);
    # 'director of physical plant' = quintessential higher-ed FM title; first pull Lorain June 22
    # (added 2026-06-19 run 210)
    'director of physical plant', 'physical plant director', 'physical plant manager',
    'campus physical plant manager', 'associate vp of facilities', 'associate vice president of facilities',
    'university facilities director', 'college facilities director',
    # Municipal Public Works Departments — Segment #204; all DPW contacts route to property_manager
    # sequence (compliance pitch; MS4 stormwater + OEPA NPDES angle); (added 2026-06-20 run 211)
    'public works director', 'city public works director', 'director of public works',
    'public works superintendent', 'dpw director', 'infrastructure maintenance manager',
    'public works manager', 'highway superintendent',
    # Funeral Homes & Mortuary Services — Segment #205; curb appeal pitch matches property_manager
    # sequence tone perfectly (appearance = client trust); (added 2026-06-20 run 211)
    'funeral home director', 'mortuary director', 'funeral services manager',
    'funeral home manager', 'funeral home administrator', 'mortuary administrator',
    'cremation services director', 'funeral home owner',
    # Modular Building & Relocatable Space Rental Companies — Segment #206; routing to property_manager
    # sequence (facility management / vendor contract angle); (added 2026-06-21 run 212)
    'modular building branch manager', 'relocatable building manager', 'portable building manager',
    'modular building operations manager', 'modular space manager', 'temporary structures manager',
    'modular building regional manager', 'portable building branch manager',
    # Metal Stamping & Sheet Metal Fabrication Shops — Segment #207; routing to property_manager
    # sequence (OSHA 1910.22 / OEPA NPDES / IATF 16949 compliance angle);
    # DISTINCT from steel service centers (run 189), steel fab (run 201), general mfg (run 118);
    # Ford Avon Lake EV supply chain = 100+ stamping shops in Lorain County corridor;
    # first pull Lorain June 22 (added 2026-06-22 run 213)
    'metal stamping plant manager', 'stamping facility manager', 'sheet metal operations manager',
    'stamping shop manager', 'metal stamping superintendent', 'sheet metal plant manager',
    'stamping plant superintendent', 'sheet metal fabrication manager',
    # Powder Coating & Industrial Surface Finishing Shops — Segment #208; routing to property_manager
    # sequence (EPA NESHAP 6H / OEPA NPDES / OSHA 1910.22 compliance angle);
    # DISTINCT from general mfg (run 118), machine shops (run 184), steel fab (run 201), stamping (run 207);
    # NE Ohio corridors: Elyria/Sheffield Village/Avon Lake/Strongsville industrial parks;
    # first pull Geauga+Portage / Cuyahoga 2nd pass (added 2026-06-23 run 214)
    'powder coating shop manager', 'surface finishing manager', 'powder coat operations manager',
    'industrial coating manager', 'surface treatment manager', 'plating operations manager',
    'powder coating plant manager', 'anodizing operations manager',
    # Plastic Injection Molding & Plastics Manufacturing — Segment #209 routing sync; all new plastics/injection
    # molding contacts correctly route to property_manager Mixmax sequence on enrollment;
    # DISTINCT from general mfg, machine shops, metal stamping, powder coating (added 2026-07-08 run 215)
    'injection molding plant manager', 'plastics facility manager', 'plastics operations manager',
    'molding plant superintendent', 'plastics manufacturing manager', 'injection molding operations manager',
    'plastics plant manager', 'thermoplastic operations manager',
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
    # Snow removal & ice management — completely idle May–Sept; same driveways/parking lots Forest City washes;
    # pitch: "You're their winter vendor — be their summer referral, we'll return the favor in September";
    # routing fix: without these keywords, snow removal contacts fall through to property_manager default (added 2026-05-28 run 117)
    'snow removal', 'snow plowing', 'ice management', 'winter services', 'snow plow',
    'salting service', 'de-icing', 'snow contractor',
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
    # Additional NE Ohio / Northeast regional C-store chains (added 2026-06-14 run 205)
    # Kwik Fill / Country Fair: significant Western NY + NE Ohio chain; Lake & Geauga county presence
    'kwik fill', 'country fair stores', 'country fair gas',
    # United Dairy Farmers (UDF): Ohio-native C-store + dairy chain; 180+ OH locations; strong NE Ohio presence
    'united dairy farmers', 'udf convenience', 'udf store',
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

    # Check gas station by COMPANY NAME first — before any title-based routing.
    # This prevents 'district manager' (now in PROPERTY_MANAGER_TITLES) from incorrectly routing
    # a gas station DM to the PM sequence. Gas station detection is company-based (brand names,
    # industry terms) so checking company alone is more precise than checking combined.
    for kw in GAS_STATION_KEYWORDS:
        if kw in company:
            return 'gas_station'

    # Check PM titles next — more specific than realtor keywords.
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
            results = data
        else:
            results = data.get('results', data.get('recipients', []))
        if len(results) == 200:
            import sys
            print(
                f'⚠️  WARNING: {sequence_type} sequence returned exactly 200 recipients — '
                'Mixmax API limit reached. Additional contacts are not shown in this report. '
                'Enrollment counts and hot-lead detection may be incomplete.',
                file=sys.stderr
            )
        return results
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
