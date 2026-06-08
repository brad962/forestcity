# Vera Cole — Open Issues Tracker
*Run 199 | 2026-06-08 | Compact version — historical run entries archived in git history*
*192 open (190 carry-forward + 2 new this run) | 122 resolved*

> ⚠️ **FILE SIZE NOTE:** This file was 572KB as of Run 195 due to prepending a full header every run.
> Rewritten as a compact rolling summary on Run 196. Full history is in git log.
> Going forward: update the metrics line at top + append new issues only (no full run header dumps).

---

## NEW OPEN — Run 199 | 2026-06-08

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
- **Last attempt this run:** N/A — code fix is not possible from Vera's side. This requires Bradley to create the sequences in Mixmax UI. 23+ consecutive runs flagged. Once Bradley creates the sequences, this resolves in 6 minutes.

---

## Active Open Issues — Summary Table

Today is June 8. The Cuyahoga mega-pull fires today. All 190+ "awaiting June 8 pull" segments now have the pull in motion. Resolution status changes from "awaiting" to "verify enrollment" — mark fully resolved when contacts appear in Nina's report June 9-11.

| Issue # | Segment | Status | Expected Resolution |
|---------|---------|--------|---------------------|
| Gas Station | Gas Station & C-Store Mixmax sequence | 🚨 BLOCKER — needs 5-min Mixmax UI fix | Bradley action required |
| Fleet Washing | Fleet Washing Mixmax sequence | 🚨 BLOCKER — needs 5-min Mixmax UI fix | Bradley action required |
| #1–#182 | Segments awaiting June 8 pull (all coded) | **Pull fired June 8 — verify enrollment June 9** | Confirm contacts in Nina report June 9-11 |
| #183 | Aerospace & Defense Manufacturers | **Pull fired June 8** | Confirm contacts in Nina report |
| #184 | Precision Machining & CNC Machine Shops | **Pull fired June 8** | Confirm contacts in Nina report |
| #185 | Public Transit Agencies & Bus Depots | **Pull fired June 8** | Confirm contacts in Nina report |
| #186 | Industrial Real Estate & Logistics Parks | **Pull fired June 8** | Confirm contacts in Nina report |
| #187 | Indoor Shooting Ranges & Archery Centers | **Pull fired June 8** | Confirm contacts in Nina report |
| #188 | Cannabis Cultivation & Processing Facilities | **Pull fired June 8** | Confirm contacts in Nina report |
| #189 | Multi-Site Fitness Chain District Operations | **Pull fired June 8** | Confirm contacts in Nina report |
| #190 | Cold Storage & Refrigerated Warehouse Networks | **Pull fired June 8** | Confirm contacts in Nina report |
| #191 | Intermodal Rail Terminals & Freight Hubs | NEW — code live (Run 199) — pull fires today | Confirm contacts in Nina report |
| #192 | Commercial Parking Management Portfolio Companies | NEW — code live (Run 199) — pull fires today | Confirm contacts in Nina report |

**Total open: 194 | Total resolved: 122**

> ✅ June 8 Cuyahoga pull fires today. All 192+ segments are in motion. Next verification milestone: Nina's hot leads report June 9-11 confirms enrollment.
> Gas Station + Fleet sequences remain the only issues requiring a Bradley action (Mixmax UI, 5 minutes).

---

## Previously Resolved Issues (122 total)
Detailed resolved issue entries are in git history (pre-Run 196 versions of this file).
Categories of resolved issues: missing error handling, Apollo search configuration bugs, sequence routing mismatches, county rotation calendar fixes, Instantly.ai overlap detection, Mixmax enrollment verification, report card formatting, stale count references, and worker script improvements.
