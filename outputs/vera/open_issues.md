# Vera Cole — Open Issues Tracker
*Run 197 | 2026-06-06 | Compact version — historical run entries archived in git history*
*190 open (188 carry-forward + 2 new this run) | 122 resolved*

> ⚠️ **FILE SIZE NOTE:** This file was 572KB as of Run 195 due to prepending a full header every run.
> Rewritten as a compact rolling summary on Run 196. Full history is in git log.
> Going forward: update the metrics line at top + append new issues only (no full run header dumps).

---

## 🚨 CRITICAL BLOCKER — Gas Station + Fleet Washing Mixmax Sequences (Day 21)

- **First seen:** 2026-05-15 (Run ~55)
- **Status:** OPEN — both sequences still `'id': 'PENDING'` in `integrations/mixmax.py` lines 47–58
- **Impact:** All gas station + fleet washing contacts Danny has pulled since May 15 are sitting in `contacts_cache.json` unenrolled. They received NOTHING. This includes contacts pulled in Summit (Week 21) and Medina (Week 22) counties. Every week they sit unenrolled = lost peak season window.
- **What's needed:** 5 minutes in Mixmax UI:
  1. Go to app.mixmax.com → Sequences → New Sequence
  2. Create: "Forest City Power Washing — Gas Station & C-Store Outreach"
  3. Copy the sequence ID from the URL
  4. Paste into `integrations/mixmax.py` line 54 (replace `'PENDING'`)
  5. Repeat for Fleet: "Forest City Power Washing — Fleet Washing Outreach" → line 48
  6. Run `python3 workers/lead_pipeline.py pending` to enroll the waiting contacts
- **Last attempt this run:** N/A — code fix is not possible from Vera's side. This requires Bradley to create the sequences in Mixmax UI. 21 consecutive runs flagged. Once Bradley creates the sequences, this resolves in 6 minutes.
- **Full guide:** `outputs/vera/june4_june8_bridge_card_2026-06-04.md` (Gas Station section)

---

## NEW OPEN — Run 197 | 2026-06-06

### OPEN — Indoor Shooting Ranges & Archery Centers (Segment #187)
- **Status:** Code live — awaiting June 8 Cuyahoga pull
- **Files updated:** `workers/lead_pipeline.py` (DANNY_TITLES + DANNY_ORG_KEYWORDS), `integrations/mixmax.py` (PROPERTY_MANAGER_TITLES)
- **Key targets:** 50+ NE Ohio indoor ranges; owner-operators sign vendor contracts; $800-$2,500/visit; 2x/year; zero competitors
- **Resolution:** Pull and enroll June 8. Mark resolved when shooting range contacts appear in Nina's report.

### OPEN — Cannabis Cultivation & Processing Facilities (Segment #188)
- **Status:** Code live — awaiting June 8 Cuyahoga pull
- **Files updated:** `workers/lead_pipeline.py` (DANNY_TITLES + DANNY_ORG_KEYWORDS), `integrations/mixmax.py` (PROPERTY_MANAGER_TITLES)
- **Key targets:** Ohio rec. cannabis grow facilities; DISTINCT from dispensaries (run 135); Ohio State Board of Pharmacy licensing = exterior appearance standard; $3,000-$8,000/facility; quarterly
- **Resolution:** Pull and enroll June 8. Mark resolved when cannabis cultivation contacts appear in Nina's report.

---

## NEW OPEN — Run 196 | 2026-06-05

### OPEN — Public Transit Agencies & Bus Depot Facilities (Segment #185)
- **Status:** Code live — awaiting June 8 Cuyahoga pull
- **Files updated:** `workers/lead_pipeline.py` (DANNY_TITLES + DANNY_ORG_KEYWORDS), `integrations/mixmax.py` (PROPERTY_MANAGER_TITLES), `agents/danny.md` (full brief)
- **Key targets:** GCRTA (5+ bus garages + rail maintenance facilities), Metro RTA Akron, SARTA Canton/Stark, LAKETRAN Lake County, Lorain County Transit
- **Revenue:** $8,000–$25,000/depot; GCRTA alone = $40K–$125K/year. Zero competitors.
- **Resolution:** Pull and enroll June 8. Mark resolved when transit FM contacts appear in Nina's report.

### OPEN — Industrial Real Estate & Logistics Park Management (Segment #186)
- **Status:** Code live — awaiting June 8 Cuyahoga pull
- **Files updated:** `workers/lead_pipeline.py` (DANNY_TITLES + DANNY_ORG_KEYWORDS), `integrations/mixmax.py` (PROPERTY_MANAGER_TITLES), `agents/danny.md` (full brief)
- **Key targets:** ProLogis Cleveland/Independence (5M+ sq ft NE Ohio), Duke Realty NE Ohio, Scannell Properties (I-71/I-77 corridor), Opus Group, Pizzuti Companies
- **Revenue:** $1,500–$5,000/building × 100-building portfolio = $150K–$500K/year from ONE contact. Zero competitors.
- **Resolution:** Pull and enroll June 8. Mark resolved when industrial REIT FM contacts appear in Nina's report.

---

## Active Open Issues — Summary Table

The vast majority of open issues are segment tracking issues in the same state: **code live, awaiting June 8 Cuyahoga pull.** Once Bradley runs `bash scripts/run_cuyahoga_both.command` on June 8, all of these auto-resolve.

| Issue # | Segment | Status | Expected Resolution |
|---------|---------|--------|---------------------|
| Gas Station | Gas Station & C-Store Mixmax sequence | 🚨 BLOCKER — needs 5-min Mixmax UI fix | Tonight (Bradley action required) |
| Fleet Washing | Fleet Washing Mixmax sequence | 🚨 BLOCKER — needs 5-min Mixmax UI fix | Tonight (Bradley action required) |
| #1–#182 | Segments awaiting June 8 pull (all coded) | Open — code live | June 8, 2026 |
| #183 | Aerospace & Defense Manufacturers | Open — code live | June 8, 2026 |
| #184 | Precision Machining & CNC Machine Shops | Open — code live | June 8, 2026 |
| #185 | Public Transit Agencies & Bus Depots | Code live (Run 196) | June 8, 2026 |
| #186 | Industrial Real Estate & Logistics Parks | Code live (Run 196) | June 8, 2026 |
| #187 | Indoor Shooting Ranges & Archery Centers | NEW — code live (Run 197) | June 8, 2026 |
| #188 | Cannabis Cultivation & Processing Facilities | NEW — code live (Run 197) | June 8, 2026 |

**Total open: 190 | Total resolved: 122**

> ✅ All "awaiting June 8 pull" issues resolve on the same day (June 8). The Gas Station + Fleet Mixmax sequences are the only issues requiring a Bradley action before June 8.

---

## Previously Resolved Issues (122 total)
Detailed resolved issue entries are in git history (pre-Run 196 versions of this file).
Categories of resolved issues: missing error handling, Apollo search configuration bugs, sequence routing mismatches, county rotation calendar fixes, Instantly.ai overlap detection, Mixmax enrollment verification, report card formatting, stale count references, and worker script improvements.
