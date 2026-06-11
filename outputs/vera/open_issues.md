# Vera Cole — Open Issues Tracker
*Run 202 | 2026-06-11 | Compact version — historical run entries archived in git history*
*196 open (195 carry-forward + 1 new this run) | 122 resolved*

> ⚠️ **FILE SIZE NOTE:** This file was 572KB as of Run 195 due to prepending a full header every run.
> Rewritten as a compact rolling summary on Run 196. Full history is in git log.
> Going forward: update the metrics line at top + append new issues only (no full run header dumps).

---

## NEW OPEN — Run 202 | 2026-06-11

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
- **Last attempt Run 202:** N/A — code fix is not possible from Vera's side. This requires Bradley to create the sequences in Mixmax UI. **Day 27+ consecutive runs flagged.** Lake County pull fires June 15 — 4 days away. All gas/fleet contacts from Summit, Medina, Cuyahoga + upcoming Lake County will be unenrolled unless Bradley creates these sequences. **FINAL WINDOW: June 11–14 night.**

---

## Active Open Issues — Summary Table

*Updated Run 202 | June 11 — FIRST HOT LEADS DAY from June 8 Cuyahoga batch*

| Issue # | Segment | Status | Expected Resolution |
|---------|---------|--------|---------------------|
| Gas Station | Gas Station & C-Store Mixmax sequence | 🚨 BLOCKER Day 27+ — create in Mixmax UI TONIGHT (June 11–14) | Bradley action — 10 min in Mixmax UI |
| Fleet Washing | Fleet Washing Mixmax sequence | 🚨 BLOCKER Day 27+ — same as above | Bradley action — 10 min in Mixmax UI |
| #1–#195 | Segments — June 8 Cuyahoga mega-pull | TODAY: run `python3 workers/nina_report.py daily` — first hot leads expected (2+ opens) | First hot leads June 11–13 |
| #193 | Co-Packing & Contract Manufacturing | Code live — pull fires Lake June 15 | Confirm contacts in Nina report June 16-18 |
| #194 | Semiconductor & PCB/Electronics Manufacturers | Code live — pull fires Lake June 15 | Confirm contacts in Nina report June 16-18 |
| #195 | Boat Repair & Marine Service Centers | Code live — pull fires Lake June 15 | Confirm contacts in Nina report June 16-18 |
| #196 | Craft Breweries & Taprooms | NEW (Run 202) — code live — pull fires Lake June 15 (Willoughby Brewing) | Confirm contacts in Nina report June 16-18 |

**Total open: 196 | Total resolved: 122**

> ⚠️ **TODAY IS FIRST HOT LEADS DAY.** Run `python3 workers/nina_report.py daily` NOW. Hot leads (2+ opens) from June 8 Cuyahoga batch expected June 11–13. Connect on LinkedIn within 2 hours of seeing any open.
> Gas Station + Fleet sequences: **must fix before Lake pull June 15 — 4 days away.** Guide: `outputs/vera/lake_county_june15_preflight_2026-06-09.md`

---

## Previously Resolved Issues (122 total)
Detailed resolved issue entries are in git history (pre-Run 196 versions of this file).
Categories of resolved issues: missing error handling, Apollo search configuration bugs, sequence routing mismatches, county rotation calendar fixes, Instantly.ai overlap detection, Mixmax enrollment verification, report card formatting, stale count references, and worker script improvements.
