# Vera Cole — Open Issues Tracker
*Run 200 | 2026-06-09 | Compact version — historical run entries archived in git history*
*194 open (192 carry-forward + 2 new this run) | 122 resolved*

> ⚠️ **FILE SIZE NOTE:** This file was 572KB as of Run 195 due to prepending a full header every run.
> Rewritten as a compact rolling summary on Run 196. Full history is in git log.
> Going forward: update the metrics line at top + append new issues only (no full run header dumps).

---

## NEW OPEN — Run 200 | 2026-06-09

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
- **Last attempt this run:** N/A — code fix is not possible from Vera's side. This requires Bradley to create the sequences in Mixmax UI. 23+ consecutive runs flagged. Once Bradley creates the sequences, this resolves in 6 minutes.

---

## Active Open Issues — Summary Table

Today is June 9. The June 8 Cuyahoga mega-pull should have fired yesterday. Verify contacts are appearing in contacts_cache.json and enrolled in Mixmax. Run Nina's hot leads report to confirm.

| Issue # | Segment | Status | Expected Resolution |
|---------|---------|--------|---------------------|
| Gas Station | Gas Station & C-Store Mixmax sequence | 🚨 BLOCKER Day 25+ — needs 5-min Mixmax UI fix BEFORE June 15 Lake pull | Bradley action required TONIGHT (June 14 at latest) |
| Fleet Washing | Fleet Washing Mixmax sequence | 🚨 BLOCKER Day 25+ — same as above | Bradley action required TONIGHT (June 14 at latest) |
| #1–#192 | Segments — June 8 Cuyahoga pull | **VERIFY: run `check_replies.py` + read `contacts_cache.json`** | Confirm contacts enrolled, first opens June 9-11 |
| #193 | Co-Packing & Contract Manufacturing | NEW (Run 200) — code live — pull fires Lake June 15 | Confirm contacts in Nina report June 16-18 |
| #194 | Semiconductor & PCB/Electronics Manufacturers | NEW (Run 200) — code live — pull fires Lake June 15 | Confirm contacts in Nina report June 16-18 |

**Total open: 194 | Total resolved: 122**

> ⚠️ June 8 Cuyahoga pull should have fired. KEY ACTION TODAY: verify enrollment by running `check_replies.py`. First opens from June 8 batch expected today (June 9) through June 11. Hot leads (2+ opens) = call within 24 hours.
> Gas Station + Fleet sequences remain the only issues requiring a Bradley action (Mixmax UI, 5 minutes). Must fix before Lake County June 15 pull.

---

## Previously Resolved Issues (122 total)
Detailed resolved issue entries are in git history (pre-Run 196 versions of this file).
Categories of resolved issues: missing error handling, Apollo search configuration bugs, sequence routing mismatches, county rotation calendar fixes, Instantly.ai overlap detection, Mixmax enrollment verification, report card formatting, stale count references, and worker script improvements.
