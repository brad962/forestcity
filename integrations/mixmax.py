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
    'home improvement operations manager', 'garden center manager', 'hardware store district manager',
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
    'beverage district manager', 'coffee store manager',
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
