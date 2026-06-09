# Lake County June 15 Pre-Flight Card
*Vera Cole | Run 200 | 2026-06-09*

---

## Why This Pull Matters

Lake County is the **marina/waterfront corridor** — Mentor Headlands, Fairport Harbor, Grand River, Willoughby, Willoughby Hills, Eastlake, Euclid. It's a distinct commercial ecosystem from Cuyahoga with segments that either didn't exist or weren't at peak density in the June 8 pull:

- **Marina & waterfront operators** — pre-season prep window closes by July 4
- **Lake Erie charter fishing operators** — peak walleye season NOW (June–August)
- **Greatbatch Medical / electronics manufacturers** — Lake County industrial corridor
- **Mentor retail/commercial corridor** — Mentor-on-the-Lake strip malls, Great Lakes Mall facilities

**New this pull:** Segment #193 (Co-Packing & Contract Manufacturing) and #194 (Semiconductor & PCB Manufacturers) fire for the first time in Lake County. Greatbatch (now Integer Holdings Corp) has significant Lake County presence.

**Revenue at stake:** 200–400 net new Lake County contacts expected across 194+ segments.

---

## Pre-Flight Checklist (Night of June 14 — Sunday)

| # | Action | Time | Status |
|---|--------|------|--------|
| ① | Gas Station/Fleet Mixmax sequences — still PENDING? Create NOW (5 min in Mixmax UI) | 5 min | ⚠️ BLOCKER |
| ② | Confirm Instantly.ai is still paused (no overlap with Mixmax sequences) | 2 min | |
| ③ | Confirm `run_lake_both.command` is in `scripts/` folder (double-click ready) | 1 min | |
| ④ | Set 7:30am alarm for Monday June 15 | 1 min | |
| ⑤ | Read `outputs/vera/june8_post_pull_action_card_2026-06-08.md` — are any June 8 hot leads still unreplied? | 5 min | |

---

## June 15 Execution Guide (7:30am Monday)

### Step 1 — Run the pull (7:30am)
```bash
# Option A — Double-click in Finder:
scripts/run_lake_both.command

# Option B — Terminal:
cd /Users/bradleyneal/forestcity
python3 workers/lead_pipeline.py both Lake
```
**Expected runtime:** 8–14 minutes. Let it run unattended.

### Step 2 — While it runs, check June 8 replies (7:32am–7:45am)
```bash
python3 workers/check_replies.py
```
Any PM/prospect who opened Touch 1 (sent June 8–9) 2+ times and hasn't replied → **call or DM today**.
June 11–15 is the peak reply window for June 8 enrollments (Touch 1 opens Day 0–3, replies Day 2–5).

### Step 3 — Review pull output (7:45am)
```bash
cat outputs/danny/lead_pull_2026-06-15.md | head -50
```
Confirm contacts were pulled. If Apollo returns 0 → run again with single county: `python3 workers/lead_pipeline.py danny Lake`

### Step 4 — Enroll any pending contacts (7:50am)
```bash
python3 workers/lead_pipeline.py pending
```
Enrolls all contacts in contacts_cache.json who haven't been enrolled yet — including any gas_station/fleet contacts IF Bradley created the sequences.

---

## Lake County — High-Priority Segment Targets

| Segment | Key NE Ohio Targets | Expected Revenue |
|---------|---------------------|-----------------|
| Marinas & Waterfront (run 109) | Mentor Harbor Yachting Club, Fairport Harbor Marina, Grand River Marina, Eastlake Marina, Bratenahl Yacht Club | $1,500–$4,500/visit; 2x/year |
| Charter Fishing Operators (run 174) | Lake County charter fleet (15–20 boats); peak walleye season NOW | $800–$2,000/boat dock area |
| Car Dealerships (run 88) | Mentor AutoPlex (Rte 20 auto row), Euclid/Wickliffe dealerships | $2,000–$5,000/lot; quarterly |
| Senior Living (run 93) | Mentor Ridge, Wickliffe Country Place, Willoughby Hills senior campuses | $1,500–$4,000/visit |
| Manufacturing/Industrial (run 118) | Greatbatch/Integer Holdings (Clarence Center), API Technologies, Keithley Instruments | $3,000–$12,000/facility |
| **NEW: Co-Packing #193** | Lake County contract packagers and toll manufacturers | $3,000–$8,000/facility |
| **NEW: Electronics #194** | Integer Holdings Corp (formerly Greatbatch), Lake County PCB manufacturers | $3,000–$12,000/facility |
| Golf Courses (run 112) | Mentor CC, Quail Hollow, Fowler's Mill, Kirtland CC | $1,500–$4,000/visit |
| Hotels (run 98) | Mentor/Willoughby Hilton Garden, Courtyard, Hampton Inn corridor | $2,000–$5,500/year |

---

## Revenue Math

| Metric | Estimate |
|--------|---------|
| New contacts pulled | 200–400 |
| Enrolled in Mixmax sequences | ~150–300 (depending on PENDING status) |
| Expected Touch 1 open rate (NE Ohio PM sequence) | 35–45% |
| Hot leads (2+ opens, no reply) by June 18–20 | 8–20 |
| Conversion to estimate request (5–10%) | 1–3 |
| Average job value | $1,200–$3,500 |
| **Expected booked revenue from Lake pull** | **$1,200–$10,500** |

---

## Critical: Gas Station / Fleet Sequences

⚠️ **Day 25+ BLOCKER.** If Bradley hasn't created these sequences yet, DO IT TONIGHT (June 14) before the Lake pull.

1. Go to app.mixmax.com → Sequences → New Sequence
2. **Gas Station sequence:** Name it `Forest City Power Washing — Gas Station & C-Store Outreach`
3. Copy the sequence ID from the URL (looks like `6a048cfc...`)
4. Paste into `integrations/mixmax.py` line 54 (replace `'PENDING'`)
5. **Fleet sequence:** Name it `Forest City Power Washing — Fleet Washing Outreach`
6. Paste into `integrations/mixmax.py` line 48 (replace `'PENDING'`)
7. Run `python3 workers/lead_pipeline.py pending` to enroll all waiting gas_station + fleet contacts from the last 25 days

**Total time:** 10 minutes. **Revenue impact:** Dozens of unenrolled gas station + fleet contacts are currently sitting idle.

---

## Post-Pull Calendar (June 15–22)

| Date | Action | Owner |
|------|--------|-------|
| June 15 (Mon) | Lake pull + check replies + enroll pending | Bradley + cron |
| June 16 (Tue) | Check first Lake opens via `check_replies.py` | cron 8:45am + 2pm |
| June 17 (Wed) | June 8 Touch 2 fires for Cuyahoga batch (Day 9 of sequence) | Mixmax auto |
| June 18 (Thu) | First hot leads from Lake pull expected (Touch 1 opens Day 3) | Nina |
| June 19 (Fri) | June 8 batch: any replies not yet responded to → call | Bradley |
| June 22 (Sun) | Lorain County pull prep — `run_lorain_both.command` Monday June 22 | Bradley |

---

## Files to Review Before June 15

- `outputs/vera/june8_post_pull_action_card_2026-06-08.md` — June 8 Cuyahoga hot leads verification
- `outputs/donna/june9_14_bridge_sprint_2026-06-08.md` — June 9–14 day-by-day priorities
- `integrations/mixmax.py` — verify gas_station/fleet sequences are live before pull

---

*Generated by Vera Cole | Run 200 | 2026-06-09*
