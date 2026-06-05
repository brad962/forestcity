# June 5 → June 8 Pre-Flight Card
*Vera Cole | Run 196 | 3 days to the biggest pull of the season*

---

## The Situation

June 8 is Monday. It is the largest Apollo pull of the 2026 season — 186+ commercial segments, Cuyahoga County, Danny + Carla running simultaneously. Every segment from hospitals to aerospace to transit agencies to industrial REITs fires on this one day. Cuyahoga is the densest commercial market in NE Ohio. The pull takes 12–20 minutes unattended.

**Everything else this week is secondary. June 8 is the mission.**

---

## TONIGHT (Friday June 5) — 15 minutes

### 1. Fix Gas Station + Fleet Mixmax Sequences (5 minutes, DAY 21 BLOCKER)
This is the only thing that can derail June 8 enrollment.

**Do it now:**
1. Open app.mixmax.com → Sequences → + New Sequence
2. Name it exactly: **"Forest City Power Washing — Gas Station & C-Store Outreach"**
3. Copy the sequence ID from the URL bar (looks like: `6a048c...`)
4. Open `integrations/mixmax.py` → Line 54 → Replace `'PENDING'` with the ID
5. Repeat: Name **"Forest City Power Washing — Fleet Washing Outreach"** → Line 48
6. Save → commit → done

> After June 8 pull, run: `python3 workers/lead_pipeline.py pending` to enroll any gas/fleet contacts that accumulated since May 15.

### 2. Verify Instantly.ai is Paused (2 minutes)
Confirm campaigns `a1c08c3d` and `626cd15d` are paused. If they're still running against the same contacts that Danny enrolled in Mixmax, spam filters will kill open rates.

### 3. Set Your June 8 Alarm (30 seconds)
Set alarm: **Monday June 8 — 7:30am**
Label: "CUYAHOGA PULL — 186 segments — biggest day of year"

---

## SATURDAY June 7 — 20 minutes

### Morning (5 minutes)
- Check ads: Facebook CTR, Google impressions. Log in `outputs/rick/launch_week_lead_log_*.md`. No changes — just observe.
- Check for any Mixmax replies that came in late week. Run `python3 workers/check_replies.py` locally.

### Evening Pre-Flight (15 minutes) — Run the night-before checklist
1. ✅ Open `scripts/run_cuyahoga_both.command` in Finder — confirm it opens without error
2. ✅ Confirm internet is working (Apollo API requires stable connection)
3. ✅ Confirm `.env` file has valid `APOLLO_KEY` and `MIXMAX_TOKEN`
4. ✅ Confirm `integrations/mixmax.py` shows NO `'PENDING'` sequence IDs
5. ✅ Read `outputs/donna/june8_cuyahoga_megapull_exec_guide_2026-06-03.md` (10 minutes) — know what to expect
6. ✅ Set 7:30am alarm (second check)

---

## SUNDAY June 8 — 7:30am

### Step-by-Step Execution (90 minutes, mostly unattended)

**7:30am — Open Terminal or Finder**
```bash
# Option A: Double-click in Finder
# Navigate to: forestcity/scripts/
# Double-click: run_cuyahoga_both.command

# Option B: Terminal
bash /Users/bradleyneal/forestcity/scripts/run_cuyahoga_both.command
```

**7:32am — Walk away**
The pull runs unattended. Danny searches 186+ segments across Cuyahoga County. Carla runs her referral partner pull simultaneously. Expected runtime: 12–20 minutes.

**7:50am (or when terminal shows "✅ Lead pipeline complete") — Verify**
- Check terminal for any red errors
- Check `logs/activity.log` — look for Danny and Carla entries from today
- Check `contacts_cache.json` — should show new contacts added

**8:00am — Enroll pending contacts**
```bash
python3 workers/lead_pipeline.py pending
```
This catches any gas station + fleet contacts (if you fixed the sequences Friday night) and any contacts from previous weeks that weren't enrolled.

**8:05am — Run Nina's weekly report**
```bash
python3 workers/nina_report.py weekly
```
Reports to Slack automatically.

**8:10am — Log into Mixmax**
- Verify new contacts appear in the Property Manager sequence
- Confirm enrollment is running (not paused)

---

## What June 8 Pulls (186+ Segments)

Key first-time Cuyahoga segments that will get contacts for the first time:
- **Hospitals & Health Systems** — Cleveland Clinic Main Campus, UH Rainbow, MetroHealth, Summa
- **Museums & Cultural Institutions** — Cleveland Museum of Art, Rock Hall, Great Lakes Science Center, Maltz
- **Sports Venues** — Rocket Mortgage FieldHouse, Progressive Field, FirstEnergy Stadium
- **Aerospace & Defense** — Parker Hannifin (50+ NE Ohio facilities), TransDigm Group
- **Precision Machining** — 500+ NE Ohio machine shops, ISO 9001 compliance angle
- **Public Transit** — GCRTA bus depots, transit center facilities
- **Industrial REITs** — ProLogis, Duke Realty, Scannell (50-200 buildings per FM contact)
- **Universities** — Case Western, Cleveland State, John Carroll, Baldwin Wallace
- **Government** — Cuyahoga County buildings, Cleveland City Hall, federal facilities
- **All 170+ other segments** that already have org keywords live

**Revenue at stake if this pull doesn't happen:** 186 segments × ~5 contacts each × $3,500 avg deal = $3.2M in pipeline opportunity that misses the peak season window.

---

## After June 8

| Date | Action | Time |
|------|--------|------|
| June 8 afternoon | Check Nina's report for new hot leads | 10 min |
| June 9-10 | Watch for early opens (Touch 1 sends Day 0) | Passive |
| June 11-13 | First opens expected — check hot leads daily | 5 min/day |
| June 15 | Lake County pull (Danny + Carla) | 90 min unattended |
| June 22 | Lorain County pull (Danny + Carla) | 90 min unattended |

---

*Vera Cole | Chief Innovation Officer | Forest City AI Office | 2026-06-05*
