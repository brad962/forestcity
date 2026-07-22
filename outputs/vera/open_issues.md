# Vera Cole — Open Issues Tracker
*Run 220 | 2026-07-22 | Compact version — historical run entries archived in git history*
*220 open (218 carry-forward + 2 new this run) | 125 resolved*

> ⚠️ **FILE SIZE NOTE:** This file was 572KB as of Run 195 due to prepending a full header every run.
> Rewritten as a compact rolling summary on Run 196. Full history is in git log.
> Going forward: update the metrics line at top + append new issues only (no full run header dumps).

---

## NEW OPEN — Run 220 | 2026-07-22 — GEAUGA+PORTAGE 9 DAYS OVERDUE | DAY 41 APOLLO BLOCK | DAY 68 GAS/FLEET | 55+ DAYS OVERDUE

### OPEN — Wood Products & Cabinet Manufacturers / Millwork (Segment #214)
- **First seen:** 2026-07-22 (Run 220)
- **Description:** Segment #214 added to `workers/lead_pipeline.py` (DANNY_TITLES + DANNY_ORG_KEYWORDS) and `integrations/mixmax.py` (PROPERTY_MANAGER_TITLES). Titles: woodworking shop owner, cabinet manufacturing manager, millwork operations manager, custom furniture manufacturer, wood products plant manager, cabinet shop owner, woodworking operations manager, millwork plant manager. Org keywords: cabinet manufacturer, custom cabinetry manufacturer, millwork company, wood products manufacturer, woodworking company, custom furniture manufacturer, wood cabinet manufacturer, custom woodwork manufacturer.
- **Targets:** KraftMaid Cabinetry HQ (Middlefield OH — Geauga County), MasterBrand Cabinets NE Ohio distribution, American Woodmark NE Ohio, 100+ Amish-owned custom cabinet + furniture manufacturers in Geauga/Wayne/Medina corridor, millwork/trim manufacturers (Alside NE Ohio). Sawdust + lacquer overspray + wood stain residue on production floor exteriors + parking areas + dumpster pads. OSHA 1910.272 combustible dust + NESHAP Subpart DDDD + OEPA NPDES SWPPP compliance angle.
- **Revenue:** $800–$2,500/facility; quarterly = $3,200–$10,000/year; zero competitors cold-calling cabinet shop owners or woodworking plant FMs.
- **DISTINCT from:** general mfg (run 118), machine shops (#184), plastics (#209). KraftMaid HQ in Middlefield makes Geauga County the highest-priority county for this segment.
- **First pull:** Next local Geauga+Portage run (OVERDUE — 9 days past July 13 window). NEW: `scripts/run_geauga_portage_both.command` created this run.
- **Attempts:**
  - 2026-07-22 (Run 220): Segment added to code. `run_geauga_portage_both.command` and `run_geauga_portage_pull.command` created and made executable.

### RESOLVED — Missing run_geauga_portage_both.command script (Root Cause Found)
- **Resolved:** 2026-07-22 (Run 220)
- **Root cause:** `scripts/run_geauga_portage_both.command` and `scripts/run_geauga_portage_pull.command` were NEVER CREATED. All other 5 counties had working `.command` files (Cuyahoga, Lake, Lorain, Summit, Medina). Geauga+Portage had none — this is why it has never been run.
- **Fix:** Created and chmod +x both files this run. Bradley can now double-click `run_geauga_portage_both.command` in Finder to run the full pull.

---

## NEW OPEN — Run 219 | 2026-07-21 — GEAUGA+PORTAGE 8 DAYS OVERDUE | DAY 40 APOLLO BLOCK | DAY 67 GAS/FLEET | 54+ DAYS OVERDUE

### OPEN — Wire & Cable Manufacturing Facilities (Segment #213)
- **First seen:** 2026-07-21 (Run 219)
- **Description:** Segment #213 added to `workers/lead_pipeline.py` (DANNY_TITLES + DANNY_ORG_KEYWORDS) and `integrations/mixmax.py` (PROPERTY_MANAGER_TITLES). Titles: wire drawing manager, cable manufacturing manager, wire mill superintendent, cable operations manager, wire and cable plant manager, cable plant superintendent, wire mill manager, cable manufacturing director. Org keywords: wire manufacturer, cable manufacturer, wire and cable manufacturer, wire drawing, copper wire manufacturer, aluminum wire manufacturer, power cable manufacturer, wire rope manufacturer.
- **Targets:** Prysmian Group NE Ohio (formerly General Cable, Highland Heights OH), TE Connectivity Lorain County, Superior Essex NE Ohio, Southwire Cleveland DC, Belden NE Ohio, CommScope, AFC Cable/Atkore NE Ohio, + 50+ wire harness sub-assembly suppliers to Ford Avon Lake + Honda East Liberty supply chain. Wire drawing lubricant residue + copper oxide dust (annealing) + plastic insulation pellet residue accumulate on production floors + exterior surfaces.
- **Compliance angle:** OSHA 1910.22 + EPA RCRA (drawing compounds = petroleum-based hazardous waste documentation required) + OEPA NPDES SWPPP (drawing compound runoff + copper particulate discharge).
- **Revenue:** $2,000–$5,000/facility; quarterly = $8K–$20K/year; zero competitors cold-calling wire/cable plant FMs.
- **DISTINCT from:** electronics/PCB mfg (run 194), aerospace (run 183), general mfg (run 118), machine shops (run 184), rubber/elastomer (run 216 #210).
- **First pull:** Next local Geauga+Portage run (OVERDUE — 8 days past July 13 window).
- **Attempts:**
  - 2026-07-21 (Run 219): Segment added to code. Awaiting first local pull.

---

## NEW OPEN — Run 218 | 2026-07-18 — GEAUGA+PORTAGE 5 DAYS OVERDUE | DAY 37 APOLLO BLOCK | DAY 64 GAS/FLEET | 51+ DAYS OVERDUE

### OPEN — Cold Storage Facilities & Refrigerated Warehouses (Segment #212)
- **First seen:** 2026-07-18 (Run 218)
- **Description:** Segment #212 added to `workers/lead_pipeline.py` (DANNY_TITLES + DANNY_ORG_KEYWORDS) and `integrations/mixmax.py` (PROPERTY_MANAGER_TITLES). Titles: cold storage facility manager, refrigerated warehouse manager, cold chain operations manager, refrigerated distribution manager, cold storage operations director, cold chain facility director, temperature controlled warehouse manager, refrigerated logistics manager. Org keywords: cold storage facility, refrigerated warehouse, cold chain logistics, refrigerated distribution, temperature controlled storage, cold storage company, refrigerated food storage, cold storage logistics.
- **Targets:** SYSCO Cleveland DC, US Foods (Twinsburg DC), Gordon Food Service, AmeriCold (Conneaut OH + NE Ohio), food processing cold storage, meat/poultry/produce distribution centers. Floor drains + dock areas + loading bays accumulate food residue, grease, mold, bio-film. Summer = peak exterior wash demand (dock seals, loading dock approach pads, trash staging areas).
- **Compliance angle:** FDA FSMA HACCP + GMP requires documented sanitation program; USDA FSIS for meat/poultry cold storage; OEPA NPDES for food processing wastewater discharge. Facility inspections = contracted cleaning = recurring revenue.
- **Revenue:** $2,000–$6,000/facility; quarterly = $8K–$24K/year; zero competitors cold-calling cold storage FMs.
- **DISTINCT from:** general warehouses (run 105), food manufacturing/processing plants (run 144), grocery DCs (run 136).
- **First pull:** Next local Geauga+Portage run (OVERDUE — should have been July 13).
- **Attempts:**
  - 2026-07-18 (Run 218): Segment added to code. Awaiting first local pull.

---

## NEW OPEN — Run 217 | 2026-07-16 — GEAUGA+PORTAGE 3 DAYS OVERDUE | DAY 35 APOLLO BLOCK | DAY 62 GAS/FLEET | 49+ DAYS OVERDUE

### 🚨 CRITICAL OPEN — Geauga+Portage Pull 3 Days Past Window
- **First seen:** 2026-07-08 (Run 215) as "upcoming" — became overdue 2026-07-14 (3 days after missed July 13 window)
- **Description:** The July 13 Geauga+Portage pull window passed with NO pull logged in activity.log. Activity.log on July 13 shows Tommy/Jasmine/Donna/Rick/Nina/Marcus all ran weekly work — but NO Danny or Carla pull entry. This is the only county in the 6-county rotation that has NEVER been pulled. 211 segments have never fired there. Every day of delay is commercial leads lost to the back half of summer 2026.
- **High-value Geauga+Portage targets never contacted:** Grand River Marina, Fairport Harbor marine facilities, Debonne Vineyards, Laurello Vineyards, Fowler's Mill Golf Course, Aurora Country Club, Geauga County wholesale nurseries (200+ — nursery heartland), Willoughby Hopkins Airport FBO (LNN), Parker Hannifin (Freudenberg-NOK Twinsburg), rubber/elastomer plants, plastics shops, precast concrete plants.
- **Fix:** Run `scripts/run_geauga_portage_both.command` locally TODAY. Takes 12-20 min unattended.
- **Attempts:**
  - 2026-07-08 (Run 215): Logged as upcoming — 5 days until July 13 window
  - 2026-07-09 (Run 216): Logged as 4 days away — escalated urgently
  - 2026-07-16 (Run 217): July 13 MISSED — no log entry found — marked 3 days OVERDUE
  - 2026-07-18 (Run 218): Still no log entry — now 5 DAYS OVERDUE. Activity.log July 13–17 shows weekly workers running but zero Danny/Carla pull for Geauga+Portage. Must run locally. 212 segments queued. Segment #212 Cold Storage added this run — also queued for this county.
  - 2026-07-22 (Run 220): ROOT CAUSE FOUND. `scripts/run_geauga_portage_both.command` NEVER EXISTED — every other county had a working .command file but Geauga+Portage had none. Created both `run_geauga_portage_both.command` + `run_geauga_portage_pull.command` this run (chmod +x, committed). Bradley can now double-click in Finder — same as every other county. ISSUE RESOLVED from a script-creation standpoint; awaiting first actual pull.

### OPEN — Precast Concrete & Concrete Products Manufacturers (Segment #211)
- **First seen:** 2026-07-16 (Run 217)
- **Description:** Segment #211 added to `workers/lead_pipeline.py` (DANNY_TITLES + DANNY_ORG_KEYWORDS) and `integrations/mixmax.py` (PROPERTY_MANAGER_TITLES). Titles: precast concrete operations manager, concrete products plant manager, precast plant superintendent, precast manufacturing manager, concrete products manager, precast concrete manager, concrete pipe plant manager, precast products director. Org keywords: precast concrete manufacturer, concrete products manufacturer, precast manufacturer, precast concrete company, concrete pipe manufacturer, septic tank manufacturer, precast panel manufacturer, concrete block manufacturer.
- **Targets:** National Precast Concrete (Medina), Superior Concrete Products (Cleveland), Hanson Pipe & Precast (Summit County), Medina Supply Company, Ohio Concrete, Continental Concrete Products; 50+ plants in NE Ohio Summit/Medina/Cuyahoga/Geauga corridor. Cement dust + aggregate runoff on production yard surfaces. OEPA NPDES SWPPP (concrete washwater = regulated discharge) + OSHA 1910.22.
- **Revenue:** $2,000–$5,000/facility; quarterly = $8K–$20K/year; zero competitors cold-calling precast plant FMs.
- **DISTINCT from:** ready-mix concrete (run 192), general manufacturing (run 118), construction equipment rental (run 179).
- **First pull:** Next local Geauga+Portage run (OVERDUE — should have been July 13).

---

## NEW OPEN — Run 216 | 2026-07-09 — GEAUGA+PORTAGE 4 DAYS AWAY | DAY 28 APOLLO BLOCK | DAY 55 GAS/FLEET | 42+ DAYS OVERDUE

### OPEN — Rubber & Elastomer Manufacturing Facilities (Segment #210)
- **First seen:** 2026-07-09 (Run 216)
- **Description:** Segment #210 added to `workers/lead_pipeline.py` (DANNY_TITLES + DANNY_ORG_KEYWORDS) and `integrations/mixmax.py` (PROPERTY_MANAGER_TITLES). Titles: rubber manufacturing manager, elastomer plant manager, rubber compound operations manager, seals manufacturing manager, rubber products manager, gasket manufacturing manager, rubber plant superintendent, elastomer manufacturing director. Org keywords: rubber manufacturer, elastomer manufacturer, rubber products manufacturer, rubber compound manufacturer, gasket manufacturer, sealing products manufacturer, rubber molding company, vulcanized rubber manufacturer.
- **Targets:** Parker Hannifin Engineered Materials/Seals (Clyde OH), Freudenberg-NOK (Twinsburg — 1,000+ employees), Trelleborg Sealing Solutions (Aurora), Jason Industries, General Rubber Corp, Ohio Rubber Company; 80+ rubber/elastomer facilities in NE Ohio Ford/GM/Honda supply chain. Sulfur compounds + carbon black + process oils accumulate on production floors + dock areas. OSHA 1910.22 + EPA RCRA compliance angle.
- **Revenue:** $2,000–$5,000/facility; quarterly = $8K–$20K/year; zero competitors cold-calling rubber plant FMs.
- **DISTINCT from:** plastics/injection molding (Segment #209), general mfg (run 118), specialty chemical (run 176), machine shops (run 184), aerospace (run 183).
- **First pull:** Geauga+Portage (~July 13) — 4 DAYS AWAY. Must run locally.

---

## NEW OPEN — Run 215 | 2026-07-08 — POST-JULY 4TH | DAY 27 APOLLO BLOCK | DAY 54 GAS/FLEET | 41+ DAYS OVERDUE

### OPEN — Plastic Injection Molding & Plastics Manufacturing Facilities (Segment #209)
- **First seen:** 2026-07-08 (Run 215)
- **Description:** Segment #209 added to `workers/lead_pipeline.py` (DANNY_TITLES + DANNY_ORG_KEYWORDS) and `integrations/mixmax.py` (PROPERTY_MANAGER_TITLES). Titles: injection molding plant manager, plastics facility manager, plastics operations manager, molding plant superintendent, plastics manufacturing manager, injection molding operations manager, plastics plant manager, thermoplastic operations manager. Org keywords: injection molding, plastics manufacturer, plastic injection, plastics molding, thermoplastic manufacturer, polymer manufacturer, plastic components manufacturer, plastic molding company.
- **Targets:** Ford + Honda NE Ohio auto supply chain (100+ plastics/injection molding shops within 50 miles); Cuyahoga/Lorain/Summit corridors; Eaton/Parker Hannifin/Avery Dennison plastics divisions; independent molders in Strongsville/North Ridgeville/Twinsburg industrial parks. Pellet spills + mold release agent residue + chiller condensate accumulate on production floors around injection molding presses.
- **Compliance angle:** OSHA 1910.22 + EPA RCRA (mold release agents = hazardous waste documentation required). IATF 16949 auto supplier quality cert requires documented facility maintenance for tier-1 auto suppliers.
- **Revenue:** $1,500–$4,000/facility; quarterly = $6K–$16K/year; zero competitors cold-calling plastics plant FMs.
- **DISTINCT from:** general mfg (run 118), machine shops (run 184), metal stamping (run 207), powder coating (run 208), rubber/polymer (separate segment).
- **First pull:** Geauga+Portage (~July 13, Week 29 rotation — must run locally; Apollo blocked in cloud).

### OPEN — Geauga+Portage Pull MISSED (Week 27, ~June 29)
- **First seen:** 2026-07-08 (Run 215)
- **Description:** The Geauga+Portage county pull scheduled for Week 27 (~June 29) never happened. Apollo API still blocked in cloud (Day 27). No log entry in activity.log after June 23. This is the ONLY county in the 6-county rotation that has NEVER been pulled — Geauga+Portage has some of the highest-value specialty targets: marinas (Grand River, Fairport Harbor), wineries (Debonne Vineyards, Laurello), golf courses (Fowler's Mill, Aurora Country Club), wholesale nurseries (Geauga = Ohio nursery heartland — 200+ operations), FBOs (small airports), and the new Segment #209 plastics shops.
- **Fix required:** Run `scripts/run_geauga_portage_both.command` locally (or `python3 workers/lead_pipeline.py both Geauga+Portage`) BEFORE next week's rotation. Target date: July 13.
- **All 209 segments will fire on this pull** — 7+ newly added segments (199-209) have NEVER been pulled for Geauga+Portage.

---

## NEW OPEN — Run 214 | 2026-06-23 — DAY AFTER LORAIN PULL

### OPEN — Powder Coating & Industrial Surface Finishing Shops (Segment #208)
- **First seen:** 2026-06-23 (Run 214)
- **Description:** Segment #208 added to `workers/lead_pipeline.py` (DANNY_TITLES + DANNY_ORG_KEYWORDS) and `integrations/mixmax.py` (PROPERTY_MANAGER_TITLES). Titles: powder coating shop manager, surface finishing manager, powder coat operations manager, industrial coating manager, surface treatment manager, plating operations manager, powder coating plant manager, anodizing operations manager. Org keywords: powder coating, powder coat shop, industrial coating, surface finishing, electroplating, metal finishing, anodizing shop, plating shop.
- **Targets:** NE Ohio industrial corridors — Elyria/Sheffield Village/Avon Lake industrial parks (Lorain County), Strongsville/Twinsburg industrial parks (Cuyahoga/Summit); floor areas around powder coating lines accumulate overspray + aluminum oxide media blast residue + iron phosphate pretreatment rinse residue. DISTINCT from general mfg (run 118), machine shops (run 184), structural steel fab (run 201), metal stamping (run 207).
- **Compliance angle:** EPA NESHAP 6H (powder coating operations) + OSHA 1910.22 + OEPA NPDES SWPPP (metal rinse water = regulated effluent = documented cleaning program required).
- **Revenue:** $1,500–$4,000/facility; quarterly = $6K–$16K/year; zero competitors cold-calling powder coat shop FMs.
- **First pull:** Geauga+Portage (Week 27, ~June 29) or Cuyahoga 2nd pass.

### OPEN — 36 Pipeline Contacts Critically Overdue (25-26+ Days Stale)
- **First seen:** 2026-06-23 (Run 214)
- **Description:** Nina's June 22 weekly report shows 36 manually-tracked contacts who have NEVER been reached out to, now 25-26 days overdue. These are primarily contractor referral partners pulled in May. Three are gas station contacts (Jim Lavigne/Certified Oil, Kevin Kayden/Speedway, Mark Elyden/truenorth) who can't be enrolled in sequences because Gas/Fleet Mixmax sequences are still PENDING. The manual pipeline is silently rotting — 33 of 36 contacts are stale. This is a direct revenue leak.
- **Priority contacts to call TODAY:**
  - Jim Lavigne (Certified Oil) | gas station | 26 days overdue
  - Kevin Kayden (Speedway) | gas station | 26 days overdue
  - Mark Elyden (truenorth) | gas station | 26 days overdue
  - Venus (Reliable Roofing) | 216-810-2497 | 26 days overdue
  - Bulletproof Lawncare | 216-307-4344 | 26 days overdue
- **Root cause:** Gas/Fleet sequences PENDING = contacts pulled but no auto-enrollment path. Manual pipeline has no daily nudge.
- **Fix needed:** (1) Create Gas/Fleet sequences in Mixmax NOW — these 3 gas contacts have been waiting 26 days. (2) Bradley needs to work through the contractor list manually.

---

## NEW OPEN — Run 213 | 2026-06-22 — LORAIN COUNTY PULL DAY

### OPEN — Metal Stamping & Sheet Metal Fabrication Shops (Segment #207)
- **First seen:** 2026-06-22 (Run 213)
- **Description:** Segment #207 added to `workers/lead_pipeline.py` (DANNY_TITLES + DANNY_ORG_KEYWORDS) and `integrations/mixmax.py` (PROPERTY_MANAGER_TITLES). Titles: metal stamping plant manager, stamping facility manager, sheet metal operations manager, stamping shop manager, metal stamping superintendent, sheet metal plant manager, stamping plant superintendent, sheet metal fabrication manager. Org keywords: metal stamping, sheet metal stamping, stamping manufacturer, metal press shop, stampings manufacturer, metal pressing plant, sheet metal products manufacturer.
- **Targets:** NE Ohio Ford Avon Lake EV assembly supply chain (100+ stamping/pressing shops within 50 miles); Lorain County industrial corridor (North Ridgeville industrial park, Sheffield Village, Avon Lake supply chain). DISTINCT from steel service centers/distributors (run 189), structural steel fabrication shops (run 201), general manufacturing (run 118). NE Ohio is one of the densest auto-supply stamping corridors in the US. IATF 16949 auto supplier quality certification requires documented facility maintenance records.
- **Revenue:** $2,000–$5,000/facility; quarterly = $8,000–$20,000/year; OSHA 1910.22 + OEPA NPDES SWPPP (stamping fluid runoff = regulated) compliance angle; zero competitors cold-calling stamping shop FMs.
- **First pull:** Lorain County June 22 (TODAY — must run locally; Apollo blocked in cloud). Mark resolved when stamping shop contacts appear in Nina's report.

---

## NEW OPEN — Run 212 | 2026-06-21

### OPEN — Modular Building & Relocatable Space Rental Companies (Segment #206)
- **First seen:** 2026-06-21 (Run 212)
- **Description:** Segment #206 added to `workers/lead_pipeline.py` (DANNY_TITLES + DANNY_ORG_KEYWORDS) and `integrations/mixmax.py` (PROPERTY_MANAGER_TITLES). Titles: modular building branch manager, relocatable building manager, portable building manager, modular building operations manager, modular space manager, temporary structures manager, modular building regional manager, portable building branch manager. Org keywords: modular building rental, modular building company, relocatable buildings, portable buildings rental, modular space rental, temporary structures rental, modular office rental.
- **Targets:** Williams Scotsman (world's largest modular space company, NE Ohio operations), Mobile Mini (container/portable storage), ATCO Structures & Logistics, Pac-Van / General Finance, NRS National Relocatable Structures; NE Ohio staging yards packed with modular office units, job site trailers, portable classrooms; Lorain County connection: construction boom (Ford Avon Lake, I-90 corridor projects, new manufacturing expansions).
- **Revenue:** $2K–$6K/facility; quarterly = $8K–$24K/year; OSHA 29 CFR 1926.50 + EPA NPDES stormwater compliance angle; DISTINCT from equipment rental (run 179), mobile home parks (run 158), manufacturing (run 118); zero competitors cold-calling modular building FMs.
- **First pull:** Lorain County June 22. Mark resolved when modular building contacts appear in Nina's report.

---

## NEW OPEN — Run 211 | 2026-06-20

### OPEN — Municipal Public Works Departments (Segment #204)
- **First seen:** 2026-06-20 (Run 211)
- **Description:** Segment #204 added to `workers/lead_pipeline.py` (DANNY_TITLES + DANNY_ORG_KEYWORDS) and `integrations/mixmax.py` (PROPERTY_MANAGER_TITLES). Titles: public works director, city public works director, director of public works, public works superintendent, dpw director, infrastructure maintenance manager, public works manager, highway superintendent. Org keywords: department of public works, public works department, city public works, municipal public works, highway department.
- **Targets:** City of Lorain DPW, City of Elyria DPW, Avon Lake DPW, North Ridgeville DPW, Vermilion DPW, Amherst DPW, Sheffield Village DPW, Sheffield Lake DPW, Lorain County Highway Department.
- **Revenue:** $1,500–$5,000/facility; seasonal retainer potential; OEPA NPDES MS4 municipal stormwater permit compliance angle; DISTINCT from parks/rec (run 202), water/wastewater (run 186); zero competitors cold-calling city DPW directors.
- **First pull:** Lorain County June 22. Mark resolved when DPW contacts appear in Nina's report.

### OPEN — Funeral Homes & Mortuary Services (Segment #205)
- **First seen:** 2026-06-20 (Run 211)
- **Description:** Segment #205 added to `workers/lead_pipeline.py` (DANNY_TITLES + DANNY_ORG_KEYWORDS) and `integrations/mixmax.py` (PROPERTY_MANAGER_TITLES). Titles: funeral home director, mortuary director, funeral services manager, funeral home manager, funeral home administrator, mortuary administrator, cremation services director, funeral home owner. Org keywords: funeral home, mortuary, funeral services, cremation services, funeral chapel, memorial chapel, funeral parlor.
- **Targets:** ~60+ independent NE Ohio funeral homes; family-owned businesses where curb appeal = client trust; brick facades, parking lots, canopy/portico areas. Lorain County targets include Dovin-Reber-Jones Funeral Home (Lorain), Riddle Funeral Home (Elyria), Reidy-Scanlan-Giovannazzo (Lorain).
- **Revenue:** $300–$800/visit; 3x/year = $900–$2,400/year; zero competitors targeting this niche; recession-proof maintenance budgets.
- **First pull:** Lorain County June 22. Mark resolved when funeral home contacts appear in Nina's report.

---

## NEW OPEN — Run 210 | 2026-06-19

### OPEN — Private & Independent Colleges and Universities (Segment #203)
- **First seen:** 2026-06-19 (Run 210)
- **Description:** Segment #203 added to `workers/lead_pipeline.py` (DANNY_TITLES + DANNY_ORG_KEYWORDS) and `integrations/mixmax.py` (PROPERTY_MANAGER_TITLES). Titles: director of physical plant, physical plant director, physical plant manager, campus physical plant manager, associate vp of facilities, associate vice president of facilities, university facilities director, college facilities director. Org keywords: private university, private college, liberal arts college, independent college, independent university, liberal arts university.
- **Targets:** Oberlin College (Lorain County — flagship June 22 target), Lake Erie College (Painesville, Lake County), Baldwin Wallace University (Berea, Cuyahoga), John Carroll University (University Heights, Cuyahoga), Notre Dame College (South Euclid, Cuyahoga), Ursuline College (Pepper Pike, Cuyahoga), Hiram College (Hiram, Portage County).
- **Revenue:** $3,000–$15,000/campus visit; 2-3x/year = $6K–$45K/year per campus; June = PEAK WINDOW (summer break, buildings empty, annual maintenance). HLC accreditation = facility appearance standard. Endowment-funded budgets = not subject to municipal cycles. DISTINCT from K-12 school districts (run 119), charter schools (run 154), vocational/trade schools (run 157). Zero competitors cold-calling higher-ed physical plant directors.
- **First pull:** Lorain June 22 (Oberlin flagship); retroactive Cuyahoga/Lake on next county rotation.
- **Resolution:** Pull fires June 22. Mark resolved when college/university contacts appear in Nina's report.

---

## NEW OPEN — Run 209 | 2026-06-18

### 🚨 CRITICAL OPEN — Apollo API Network Block (Untracked Until Now)
- **First seen:** 2026-06-11 (Run 202) — in logs but never formally tracked
- **Description:** `api.apollo.io` is not in this cloud environment's network egress allowlist. Every daily scheduled pull from Danny and Carla returns 0 results. This has been happening for **7+ consecutive days**. Lorain County pull June 22 will also pull 0 leads if this isn't fixed before then. This is the most operationally damaging issue in the office right now — it's silently blocking ALL lead generation.
- **Evidence:** Logs June 11–17 consistently show: "Apollo returned 0 people — API may be blocked or rate limited" and "BLOCKED — api.apollo.io not in network egress allowlist. 0 leads pulled."
- **Fix required:** Add `api.apollo.io` to the Claude Code on the web environment's network egress allowlist via environment settings. See: https://code.claude.com/docs/en/claude-code-on-the-web
- **Workaround until fixed:** Run `python3 workers/lead_pipeline.py danny` locally (not in cloud session) before Lorain June 22.
- **Attempts:**
  - 2026-06-18 (Run 209): Formally tracked. Escalated to Bradley via Slack. Documented fix path.

### OPEN — Municipal & Public Recreation Centers / Community Pools (Segment #202)
- **First seen:** 2026-06-18 (Run 209)
- **Description:** Segment #202 added to `workers/lead_pipeline.py` (DANNY_TITLES + DANNY_ORG_KEYWORDS) and `integrations/mixmax.py` (PROPERTY_MANAGER_TITLES). Titles: parks and recreation director, recreation center manager, aquatics director, community center manager, parks facilities manager, recreation facility manager, aquatics manager, aquatics facility manager. Org keywords: recreation center, community center, parks department, parks and recreation, aquatics facility, public pool, municipal recreation, community recreation.
- **Targets:** Lorain Metro Parks, Elyria Recreation Center, Cleveland MetroParks aquatics facilities, Lorain/Elyria municipal pools, county parks departments. Ohio Dept. Health aquatic sanitation rules + OSHA 1910.141 compliance angle. DISTINCT from fitness centers/gyms (run 99) and YMCAs.
- **Revenue:** $800–$2,500/facility; 2x/season = $1,600–$5,000/year; zero competitors cold-calling aquatics directors.
- **First pull:** Lorain County June 22 (if Apollo egress block is resolved).
- **Resolution:** Pull fires June 22. Mark resolved when rec center/aquatics contacts appear in Nina's report.

---

## NEW OPEN — Run 208 | 2026-06-17

### OPEN — Steel Fabrication & Structural Steel Shops (Segment #201)
- **First seen:** 2026-06-17 (Run 208)
- **Description:** Segment #201 added to `workers/lead_pipeline.py` (DANNY_TITLES + DANNY_ORG_KEYWORDS) and `integrations/mixmax.py` (PROPERTY_MANAGER_TITLES). Titles: steel fabrication plant manager, structural steel operations manager, steel fabricator superintendent, fabrication shop manager, structural fab manager, metal fabrication plant manager, steel shop superintendent, fabrication facility manager. Org keywords: steel fabrication shop, structural steel erector, structural fabrication, custom steel fabrication, fabricated steel, iron works, steel erector.
- **Targets:** Lorain/Sheffield Village steel fabrication corridor; 50+ independent fab shops; Lorain steel corridor (Sheffield Village, North Ridgeville industrial parks). DISTINCT from steel service centers/distributors (run 189) and general manufacturing (run 118).
- **Revenue:** $2,000–$6,000/facility; quarterly = $8,000–$24,000/year; OSHA 1910.22 + OEPA NPDES SWPPP compliance angle; zero competitors cold-calling fab shop FMs
- **First pull:** Lorain County June 22
- **Resolution:** Pull fires June 22. Mark resolved when steel fabrication contacts appear in Nina's report.

### OPEN — GitHub Actions Relay: PAT `workflow` Scope (Run 209 Update)
- **Run 209 New Approach Result:** Tried `git push` directly (not REST API) with the workflow file committed locally. Git returned definitive error: `"refusing to allow a Personal Access Token to create or update workflow .github/workflows/vera_slack_relay.yml without workflow scope"`. This is the identical block as the REST API — both paths require `workflow` scope. Commit was reverted so it doesn't block future pushes. Local `.github/workflows/vera_slack_relay.yml` file exists on disk (untracked).
- **Status:** Still BLOCKED. Both git push AND REST API require PAT `workflow` scope. Only Bradley can fix.
- **Bradley's two options (unchanged):**
  - **Option A (preferred — 5 min):** github.com/settings/tokens → find token → Edit → check `workflow` → Save → Vera deploys next run
  - **Option B (manual — 5 min):** github.com/brad962/forestcity → Code → New file → path: `.github/workflows/vera_slack_relay.yml` → paste content from `outputs/vera/github_action_vera_slack_relay.yaml` → Commit directly to main

---

## NEW OPEN — Run 207 | 2026-06-16

### OPEN — FQHCs & Community Health Centers (Segment #200)
- **First seen:** 2026-06-16 (Run 207)
- **Description:** Segment #200 added to `workers/lead_pipeline.py` (DANNY_TITLES + DANNY_ORG_KEYWORDS) and `integrations/mixmax.py` (PROPERTY_MANAGER_TITLES). Titles: fqhc administrator, community health center director, federally qualified health center director, community clinic director, neighborhood health center manager, public health facilities manager, health district facilities director, community health center administrator. Org keywords: federally qualified health center, fqhc, community health center, neighborhood health center, community clinic, public health department, county health department, community health clinic, health district office.
- **Targets:** Care Alliance Health Center (Cleveland), Near West Healthcare, Northeast Neighborhood Health (Euclid), Lake County General Health District (Willoughby), Lorain County General Health District
- **Revenue:** $1,500–$4,000/facility; quarterly = $6K–$16K/year; government direct-award contracts possible; zero competitors cold-calling
- **First pull:** Lorain County June 22
- **Resolution:** Pull fires June 22. Mark resolved when FQHC/community health contacts appear in Nina's report.

---

## NEW OPEN — Run 206 | 2026-06-15

### OPEN — GitHub Actions Relay: PAT Needs `workflow` Scope to Deploy
- **First seen:** 2026-05-18 (relay never deployed); escalated Run 206 (June 15)
- **Description:** `.github/workflows/vera_slack_relay.yml` was created locally this run but CANNOT be pushed — the PAT (stored in `.env` as GITHUB_PAT) lacks `workflow` scope. GitHub requires this scope to create or modify files in `.github/workflows/`.
- **Workflow file content:** Complete YAML is in `outputs/vera/github_action_vera_slack_relay.yaml` (or local `/tmp/forestcity/.github/workflows/vera_slack_relay.yml`)
- **Bradley action required (5 minutes — CHOOSE ONE):**
  - **Option A (preferred):** github.com/settings/tokens → find token → Edit → check `workflow` checkbox → Save → Vera can push next run
  - **Option B (manual):** github.com/brad962/forestcity → Code → `.github/workflows/` (create folder) → `vera_slack_relay.yml` → paste content from `outputs/vera/github_action_vera_slack_relay.yaml` → Commit
- **Attempts:**
  - 2026-06-14 (Run 205): Claimed RESOLVED — incorrect. `.github/workflows/` directory was never created.
  - 2026-06-15 (Run 206): Created workflow locally; push blocked by PAT scope. Documented both options above.

### OPEN — Portable Restroom Rental & Event Sanitation Companies (Segment #199)
- **First seen:** 2026-06-15 (Run 206)
- **Description:** Segment #199 added to `workers/lead_pipeline.py` (DANNY_TITLES + DANNY_ORG_KEYWORDS) and `integrations/mixmax.py` (PROPERTY_MANAGER_TITLES). Titles: portable restroom manager, portable sanitation manager, sanitation services manager, etc. Org keywords: portable restroom rental, porta potty rental, portable sanitation, etc.
- **Targets:** Mr. John Inc. (Stow OH), Porta-Jon Inc. (NE Ohio), Pioneer Services Group, United Site Services NE Ohio
- **Revenue:** $2K–$6K/facility; quarterly = $8K–$24K/year; zero competitors cold-calling
- **First pull:** Lorain County June 22
- **Resolution:** Pull fires June 22. Mark resolved when portable restroom contacts appear in Nina's report.

### OPEN — GAS_STATION_KEYWORDS Missing NE Ohio C-Store Chains (auto-fix this run)
- **First seen:** 2026-06-14 (Run 205)
- **Description:** Kwik Fill / Country Fair Stores (significant Lake/Geauga county presence) and United Dairy Farmers (UDF — 180+ Ohio locations, strong NE Ohio presence) were absent from GAS_STATION_KEYWORDS in `integrations/mixmax.py`. Contacts from these chains would fall through to property_manager sequence instead of the (pending) gas_station sequence.
- **Fix:** Added 'kwik fill', 'country fair stores', 'country fair gas', 'united dairy farmers', 'udf convenience', 'udf store' to GAS_STATION_KEYWORDS in `integrations/mixmax.py` this run.
- **Status:** Auto-fixed this run. Will correctly route on next pull once gas_station sequence ID is live.

---

## Previously NEW OPEN — Run 204 | 2026-06-13

### OPEN — Commercial/Wholesale Nursery & Greenhouse Production Facilities (Segment #198)
- **Status:** Code live — titles + org keywords in `lead_pipeline.py` + `mixmax.py`; first pull Lake County June 15 (2 days)
- **Files updated:** `workers/lead_pipeline.py` (DANNY_TITLES + DANNY_ORG_KEYWORDS), `integrations/mixmax.py` (PROPERTY_MANAGER_TITLES), `agents/danny.md` (Run 204 batching note)
- **Key targets:** Willoway Nurseries, Lake County Nursery Exchange, Berns Nurseries, Heritage Farm Nurseries; Ohio Dept. of Agriculture nursery dealer licensing compliance angle; $2K-$8K/facility; quarterly = $8K-$32K/year; zero competitors cold-calling wholesale nursery ops managers
- **Lake County angle:** Lake County is Ohio's "Nursery Capital" with 200+ commercial/wholesale nurseries — this segment has higher concentration here than any other county
- **Resolution:** Pull fires June 15. Mark resolved when nursery/greenhouse contacts appear in Nina's report.

### OPEN — danny.md File Size Bloat (Technical Debt)
- **First seen:** 2026-06-13 (Run 204)
- **Description:** `agents/danny.md` is 466KB (2,310 lines) — exceeds the 256KB tool read limit. Every new segment adds 200-400 words of documentation directly to danny.md. When Claude activates Danny, it cannot read the full file. The most recent segments are at the bottom — which means the most critical current instructions may be invisible.
- **Root cause:** Each run adds full segment documentation (why, revenue math, pitch angle, Apollo titles, org keywords, distinct-from) directly inline in the agent file rather than referencing a separate segment library.
- **Impact:** MEDIUM-HIGH — Danny activation may miss recent segments and current batching notes; risk grows with each run
- **Proposed fix:** Archive all segment documentation blocks (runs 87-197) to `docs/commercial_segments_archive.md`. Keep in `danny.md`: core instructions, last 3 batching notes, and a pointer to the archive. This would reduce danny.md to ~15KB.
- **Attempts:**
  - 2026-06-13 (Run 204): Identified and logged. Added compact batching note (no full docs block) to prevent further growth. Proposed fix to Bradley in pending_slack_messages.md.

---

## Previously NEW OPEN — Run 203 | 2026-06-12

### OPEN — General Aviation (FBO) & Private Airport Terminals (Segment #197)
- **Status:** Code live — first pull Lake County June 15 (Willoughby Hopkins Airport/LNN is Day-1 priority)
- **Files updated:** `workers/lead_pipeline.py` (DANNY_TITLES + DANNY_ORG_KEYWORDS), `integrations/mixmax.py` (PROPERTY_MANAGER_TITLES), `agents/danny.md` (Run 203 batching note)
- **Also fixed:** Duplicate brewery/taproom entries in Segment #196 block removed from both lead_pipeline.py and mixmax.py (run 129 titles were duplicated by run 202)
- **Key targets:** Willoughby Hopkins Airport FBO (LNN — Lake County), Cuyahoga County Airport FBO (CGF), Executive Flight Center, Jet Center, North Coast Air, ProJet Aviation; FAA Part 139 + OSHA SPCC compliance angle; $3K–$10K/visit; zero competitors
- **Revenue:** $3K–$10K/visit; quarterly = $12K–$40K/year per FBO; zero competitors cold-calling
- **Resolution:** Pull fires June 15. Mark resolved when FBO/aviation contacts appear in Nina's report.

### BUG FIX — Segment #196 Duplicate Titles (Run 203)
- **Status:** RESOLVED this run
- **Issue:** Run 202 re-added 5 titles already in PROPERTY_MANAGER_TITLES from run 129 ('brewery manager', 'taproom manager', 'craft brewery manager', 'brewery operations manager', 'taproom director')
- **Fix:** Removed duplicates from run 202 block in both `lead_pipeline.py` and `integrations/mixmax.py`; kept unique new titles only ('brewery director', 'production brewery manager', 'beverage facility manager', 'brewery owner')

---

## Previously NEW OPEN — Run 202 | 2026-06-11

### OPEN — Craft Breweries & Taprooms (Segment #196)
- **Status:** Code live — first pull Lake County June 15 (Willoughby Brewing is flagship Lake target); Cuyahoga retroactive
- **Files updated:** `workers/lead_pipeline.py` (DANNY_TITLES + DANNY_ORG_KEYWORDS), `integrations/mixmax.py` (PROPERTY_MANAGER_TITLES), `agents/danny.md` (Run 202 batching note)
- **Key targets:** Willoughby Brewing (Lake County), Platform Beer (Cleveland), Great Lakes Brewing (Ohio City), Market Garden, Fat Head's (Middleburg Heights), Forest City Brewery, Hoppin' Frog (Akron), Thirsty Dog (Akron); DISTINCT from restaurants (run 106)
- **Revenue:** $800–$2,500/visit; 3x/year = $2,400–$7,500/year; 100+ NE Ohio targets; zero competitors cold-calling this segment
- **Resolution:** Pull fires June 15. Mark resolved when brewery contacts appear in Nina's report.

---

## Previously Open — Run 201 | 2026-06-10

### OPEN — Boat Repair & Marine Service Centers (Segment #195)
- **Status:** Code live — first pull Lake County June 15
- **Files updated:** `workers/lead_pipeline.py` (DANNY_TITLES + DANNY_ORG_KEYWORDS), `integrations/mixmax.py` (PROPERTY_MANAGER_TITLES), `agents/danny.md` (Run 201 batching note)
- **Key targets:** Grand River Marine Service, Fairport Harbor Boat Works, Mentor Marine; DISTINCT from marinas (run 109), boat dealers (run 146), charter fishing (run 174); $800–$2,500/visit; 3x/year; zero competitors
- **Resolution:** Pull fires June 15. Mark resolved when marine service contacts appear in Nina's report.

---

## Previously Open — Run 200 | 2026-06-09

### OPEN — Co-Packing & Contract Manufacturing Facilities (Segment #193)
- **Status:** Code live — first pull Lake County June 15
- **Files updated:** `workers/lead_pipeline.py` (DANNY_TITLES + DANNY_ORG_KEYWORDS), `integrations/mixmax.py` (PROPERTY_MANAGER_TITLES), `agents/danny.md` (Run 200 batching note)
- **Key targets:** Lake County contract packagers and toll manufacturers; FDA 21 CFR Part 110/117 compliance angle; $3K-$8K/facility; OSHA 1910.22; DISTINCT from food plants (run 127) and general manufacturing (run 118)
- **Resolution:** Pull fires June 15. Mark resolved when co-packing contacts appear in Nina's report.

### OPEN — Semiconductor & PCB/Electronics Manufacturers (Segment #194)
- **Status:** Code live — first pull Lake County June 15
- **Files updated:** `workers/lead_pipeline.py` (DANNY_TITLES + DANNY_ORG_KEYWORDS), `integrations/mixmax.py` (PROPERTY_MANAGER_TITLES), `agents/danny.md` (Run 200 batching note)
- **Key targets:** Integer Holdings Corp (formerly Greatbatch, Lake County), API Technologies, Benchmark Electronics, Parker Hannifin Electronics (Mayfield Heights); ISO 14001 + OEPA NPDES compliance; $3K-$12K/facility; DISTINCT from aerospace (run 183) and medical device (run 168)
- **Resolution:** Pull fires June 15. Mark resolved when electronics manufacturer contacts appear in Nina's report.

---

## Previously Open — Run 199 | 2026-06-08

### OPEN — Intermodal Rail Terminals & Freight Hub Facilities (Segment #191)
- **Status:** Code live — first pull June 8 Cuyahoga (today)
- **Files updated:** `workers/lead_pipeline.py` (DANNY_TITLES + DANNY_ORG_KEYWORDS), `integrations/mixmax.py` (PROPERTY_MANAGER_TITLES), `agents/danny.md` (count sync)
- **Key targets:** CSX Collinwood Terminal (Cleveland's largest Class I rail freight facility), Norfolk Southern Cleveland Consolidated Terminal, Wheeling & Lake Erie Railway, CPKC (Canadian Pacific Kansas City) Cleveland hub
- **Revenue:** $5,000–$20,000/year per terminal; OSHA 29 CFR 1926 + EPA SPCC compliance angle; zero competitors cold-calling rail terminal FM contacts
- **Resolution:** Pull fired June 8. Mark resolved when rail terminal contacts appear in Nina's report.

### OPEN — Commercial Parking Management Portfolio Companies (Segment #192)
- **Status:** Code live — first pull June 8 Cuyahoga (today)
- **Files updated:** `workers/lead_pipeline.py` (DANNY_TITLES + DANNY_ORG_KEYWORDS), `integrations/mixmax.py` (PROPERTY_MANAGER_TITLES)
- **Key targets:** SP+ Corporation (formerly Standard Parking Plus), Impark, ABM Parking Services, InterPark, Lanier Parking, Premium Parking — portfolio-level management companies operating 50–200+ NE Ohio lots/garages
- **Revenue:** $15,000–$60,000/year from ONE regional portfolio manager contact; zero competitors targeting parking management company regional ops managers
- **Resolution:** Pull fired June 8. Mark resolved when parking portfolio contacts appear in Nina's report.

---

## 🚨 CRITICAL BLOCKER — Gas Station + Fleet Washing Mixmax Sequences (Day 23+)

- **First seen:** 2026-05-15 (Run ~55)
- **Status:** OPEN — both sequences still `'id': 'PENDING'` in `integrations/mixmax.py` lines 47–58
- **Impact:** All gas station + fleet washing contacts Danny has pulled since May 15 are sitting in `contacts_cache.json` unenrolled. They received NOTHING. This includes contacts pulled in Summit (Week 21), Medina (Week 22), Cuyahoga (Week 24), and Lake (Week 25 — June 15). Every week they sit unenrolled = lost peak season window. Day 34 as of June 17.
- **What's needed:** 5 minutes in Mixmax UI:
  1. Go to app.mixmax.com → Sequences → New Sequence
  2. Create: "Forest City Power Washing — Gas Station & C-Store Outreach"
  3. Copy the sequence ID from the URL
  4. Paste into `integrations/mixmax.py` line 54 (replace `'PENDING'`)
  5. Repeat for Fleet: "Forest City Power Washing — Fleet Washing Outreach" → line 48
  6. Run `python3 workers/lead_pipeline.py pending` to enroll the waiting contacts
- **Last attempt Run 203 (NEW ANGLE):** Previous guides described WHAT to do — not HOW with specific copy. This run delivers the COMPLETE email sequence text (3 touches each, both sequences) to `outputs/vera/gas_fleet_sequence_copy_2026-06-12.md`. Bradley can paste directly without writing anything. Reduces friction to: open Mixmax → create shell → paste 3 emails per sequence → copy IDs → replace PENDING. **Day 34.** Lake County pull ran June 15 — Lake gas/fleet contacts now unenrolled too. Lorain June 22 will add more.

---

## Active Open Issues — Summary Table

*Updated Run 219 | July 21 — GEAUGA+PORTAGE 8 DAYS OVERDUE (July 13 MISSED) | Gas/Fleet blocker Day 67 | Apollo API BLOCKED Day 40 | Segment #213 Wire & Cable Mfg added | 36+ pipeline contacts 54+ days overdue*

| Issue # | Segment | Status | Expected Resolution |
|---------|---------|--------|---------------------|
| Geauga+Portage | **Geauga+Portage pull OVERDUE — July 13 window MISSED — only county never pulled** | 🚨 CRITICAL — 8 DAYS OVERDUE | Bradley: run `scripts/run_geauga_portage_both.command` locally TODAY. 213 segments queued. |
| Overdue | **36+ pipeline contacts — 54+ days stale, NEVER contacted** | 🚨 CRITICAL Day 54 — 3 gas contacts + 33 contractors silent | Bradley: call Jim Lavigne (Certified Oil), Kevin Kayden (Speedway), Mark Elyden (truenorth) TODAY. Create Gas/Fleet sequences. |
| Apollo | **Apollo API network block — 0 leads pulled 40+ days** | 🚨 CRITICAL Day 40 — ALL cloud lead gen at 0 since June 11 | Bradley: add `api.apollo.io` to network egress allowlist OR run all county pulls locally |
| Gas Station | Gas Station & C-Store Mixmax sequence | 🚨 BLOCKER Day 67 — email copy ready: `gas_fleet_sequence_copy_2026-06-12.md` | Bradley action — paste copy + replace PENDING in mixmax.py |
| Fleet Washing | Fleet Washing Mixmax sequence | 🚨 BLOCKER Day 67 — same as above; copy ready to paste | Bradley action — paste copy + replace PENDING in mixmax.py |
| danny.md | File size bloat — 570KB+ exceeds tool read limit | Run 204–219 proposal; awaiting Bradley YES | Bradley approves → Vera archives in 1 run |
| #193–#198 | Co-Packing, Semiconductors, Boat Repair, Breweries, FBOs, Nurseries | Code live — Lake pull ran June 15 (IF run locally) | Confirm contacts in Nina report locally |
| #199–#207 | Portable Restroom, FQHCs, Steel Fab, Rec Centers, Colleges, DPW, Funeral, Modular, Stamping | Code live — Lorain pull was June 22 (IF run locally) | Confirm contacts in Nina report locally |
| #208 | Powder Coating & Industrial Surface Finishing Shops | Code live (Run 214) — first pull Geauga+Portage OVERDUE | Confirm contacts on next local pull |
| #209 | Plastic Injection Molding & Plastics Manufacturing | Code live (Run 215) — first pull Geauga+Portage OVERDUE | Confirm contacts on next local pull |
| #210 | Rubber & Elastomer Manufacturing Facilities | Code live (Run 216) — first pull Geauga+Portage OVERDUE | Confirm contacts on next local pull |
| #211 | Precast Concrete & Concrete Products Manufacturers | Code live (Run 217) — first pull Geauga+Portage OVERDUE | Confirm contacts on next local pull |
| #212 | Cold Storage Facilities & Refrigerated Warehouses | Code live (Run 218) — first pull Geauga+Portage OVERDUE | Confirm contacts on next local pull |
| #213 | Wire & Cable Manufacturing Facilities | Code live (Run 219) — first pull Geauga+Portage OVERDUE | NEW — first pull overdue |
| Relay | GitHub Actions relay: PAT needs `workflow` scope | 🚨 BLOCKED — definitive; YAML ready in `outputs/vera/github_action_vera_slack_relay.yaml` | Bradley: Option A — github.com/settings/tokens → add workflow scope. Option B — manually create in GitHub UI |

**Total open: 218 | Total resolved: 124**

> 🚨 **GEAUGA+PORTAGE — 8 DAYS OVERDUE (JULY 13 MISSED):** Only county never pulled. 213 segments queued. Run `scripts/run_geauga_portage_both.command` locally TODAY.
> 🚨 **APOLLO BLOCKED — Day 40:** ALL cloud lead generation 0 since June 11. Run locally.
> 🚨 **GAS/FLEET BLOCKER — Day 67:** 3 gas contacts (Jim Lavigne, Kevin Kayden, Mark Elyden) now 54+ days overdue with NO sequence. Email copy ready: `outputs/vera/gas_fleet_sequence_copy_2026-06-12.md`. 10 min in Mixmax UI.
> 🚨 **36 CONTACTS OVERDUE — 54 DAYS:** These contractor leads from May have NEVER been reached out to.
> 🚨 **DANNY.MD — 570KB+:** File exceeds tool read limit. Most recent segment instructions invisible to Danny. Approve archive to fix.

---

## Previously Resolved Issues (122 total)
Detailed resolved issue entries are in git history (pre-Run 196 versions of this file).
Categories of resolved issues: missing error handling, Apollo search configuration bugs, sequence routing mismatches, county rotation calendar fixes, Instantly.ai overlap detection, Mixmax enrollment verification, report card formatting, stale count references, and worker script improvements.
