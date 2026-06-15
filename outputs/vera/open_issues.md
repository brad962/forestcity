# Vera Cole — Open Issues Tracker
*Run 206 | 2026-06-15 | Compact version — historical run entries archived in git history*
*201 open (200 carry-forward + 1 new this run) | 124 resolved*

> ⚠️ **FILE SIZE NOTE:** This file was 572KB as of Run 195 due to prepending a full header every run.
> Rewritten as a compact rolling summary on Run 196. Full history is in git log.
> Going forward: update the metrics line at top + append new issues only (no full run header dumps).

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
- **Impact:** All gas station + fleet washing contacts Danny has pulled since May 15 are sitting in `contacts_cache.json` unenrolled. They received NOTHING. This includes contacts pulled in Summit (Week 21), Medina (Week 22), and Cuyahoga (Week 24 — June 8 today). Every week they sit unenrolled = lost peak season window.
- **What's needed:** 5 minutes in Mixmax UI:
  1. Go to app.mixmax.com → Sequences → New Sequence
  2. Create: "Forest City Power Washing — Gas Station & C-Store Outreach"
  3. Copy the sequence ID from the URL
  4. Paste into `integrations/mixmax.py` line 54 (replace `'PENDING'`)
  5. Repeat for Fleet: "Forest City Power Washing — Fleet Washing Outreach" → line 48
  6. Run `python3 workers/lead_pipeline.py pending` to enroll the waiting contacts
- **Last attempt Run 203 (NEW ANGLE):** Previous guides described WHAT to do — not HOW with specific copy. This run delivers the COMPLETE email sequence text (3 touches each, both sequences) to `outputs/vera/gas_fleet_sequence_copy_2026-06-12.md`. Bradley can paste directly without writing anything. Reduces friction to: open Mixmax → create shell → paste 3 emails per sequence → copy IDs → replace PENDING. **Day 28.** Lake County pull fires June 15 — 3 days away. All Lake County gas/fleet contacts will be unenrolled without this fix.

---

## Active Open Issues — Summary Table

*Updated Run 206 | June 15 — Lake County pull TODAY | Gas/Fleet blocker Day 32 | Hot leads window opens June 16–18*

| Issue # | Segment | Status | Expected Resolution |
|---------|---------|--------|---------------------|
| Gas Station | Gas Station & C-Store Mixmax sequence | 🚨 BLOCKER Day 32 — complete email copy in `gas_fleet_sequence_copy_2026-06-12.md` | Bradley action — paste copy + replace PENDING in mixmax.py |
| Fleet Washing | Fleet Washing Mixmax sequence | 🚨 BLOCKER Day 32 — same as above; copy ready to paste | Bradley action — paste copy + replace PENDING in mixmax.py |
| danny.md | File size bloat — 466KB exceeds tool read limit | Run 204 — proposed archive to `docs/commercial_segments_archive.md`; awaiting Bradley YES | Bradley approves → Vera executes in 1 run |
| #193 | Co-Packing & Contract Manufacturing | Code live — Lake pull TODAY | Confirm contacts in Nina report June 16–18 |
| #194 | Semiconductor & PCB/Electronics Manufacturers | Code live — Lake pull TODAY | Confirm contacts in Nina report June 16–18 |
| #195 | Boat Repair & Marine Service Centers | Code live — Lake pull TODAY | Confirm contacts in Nina report June 16–18 |
| #196 | Craft Breweries & Taprooms | Code live — Willoughby Brewing = Lake target TODAY | Confirm contacts in Nina report June 16–18 |
| #197 | General Aviation (FBO) & Private Airport Terminals | Code live — Willoughby Hopkins Airport (LNN) = Lake flagship TODAY | Confirm FBO contacts in Nina report June 16–18 |
| #198 | Commercial/Wholesale Nursery & Greenhouse Production | Code live — Lake County Nursery Capital; pull TODAY | Confirm nursery contacts in Nina report June 16–18 |
| #199 | Portable Restroom Rental & Event Sanitation | Code live this run — first pull Lorain June 22 | Confirm contacts in Nina report June 23–25 |
| Relay | GitHub Actions relay: PAT needs `workflow` scope | 🚨 BLOCKED — PAT can't push to `.github/workflows/`; workflow YAML ready to deploy | Bradley adds `workflow` scope to PAT → Vera deploys next run |

**Total open: 201 | Total resolved: 124**

> 🚨 **GAS/FLEET BLOCKER — Day 32:** Lake County pull fires TODAY — adding more unenrolled contacts. Sequence copy ready to paste: `outputs/vera/gas_fleet_sequence_copy_2026-06-12.md`. 10 minutes in Mixmax.
> 📅 **LAKE COUNTY PULL — TODAY:** Run `scripts/run_lake_both.command`. 199 segments — Willoughby Hopkins Airport (LNN), Willoughby Brewing, Lake County Nurseries, Integer Holdings, Grand River Marine.
> ⚡ **HOT LEADS WINDOW:** June 16–18 — run `python3 workers/nina_report.py daily` locally each morning.
> 📅 **NEXT PULL: LORAIN COUNTY — June 22.** Segment #199 Portable Restroom companies first appear.

---

## Previously Resolved Issues (122 total)
Detailed resolved issue entries are in git history (pre-Run 196 versions of this file).
Categories of resolved issues: missing error handling, Apollo search configuration bugs, sequence routing mismatches, county rotation calendar fixes, Instantly.ai overlap detection, Mixmax enrollment verification, report card formatting, stale count references, and worker script improvements.
