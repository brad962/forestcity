# June 3 TONIGHT — 30-Minute Last-Chance Card
*Written by Vera | Run 193 | 2026-06-03*
*June 4 is TOMORROW. Three things. Thirty minutes. Don't skip any of them.*

---

## WHY TONIGHT MATTERS

Tomorrow (June 4) is Round 2 enrollment day — the biggest outreach push of the season.

**What's at stake:**
- 40+ Summit County contacts + Medina County contacts going into Mixmax sequences
- Property Manager sequence Round 2 (new VOC copy) firing to the full pipeline
- If Instantly.ai is still running → duplicate sends → spam filters → 0% reply rate on everything
- June 8 Cuyahoga mega-pull is 5 days away — 180+ segments, 90 minutes, biggest pull of the year

**You need 30 minutes tonight.** That's it.

---

## THE THREE ACTIONS (DO IN THIS ORDER)

### ✅ Action 1 — Pause Instantly.ai (3 minutes)
*This is the most critical thing. Do it first.*

1. Go to → **app.instantly.ai**
2. Click **Campaigns** in left nav
3. Find campaign **a1c08c3d** (PM Cuyahoga) → click ⋮ → **Pause**
4. Find campaign **626cd15d** (Contractor Referral) → click ⋮ → **Pause**
5. Open your `.env` file → add this line: `INSTANTLY_PAUSED=true`

**Verify:** Both campaigns show "Paused" status before closing the tab.

> If you already did this before tonight: confirm both are still paused, then move on.

Full guide: `outputs/vera/instantly_pause_guide_2026-05-22.md`

---

### ✅ Action 2 — Confirm or Stage Medina Pull (5 minutes)

The Medina County pull was due June 1. Check if it ran:

**Did it run already?**
```bash
grep "Medina" logs/activity.log | tail -5
```
If you see a `Danny | Apollo pull | Medina` line from the last 3 days → ✅ you're good, move on.

**If it did NOT run:**
Medina pull fires as part of the June 4 battle card tomorrow. No action needed tonight.
Just confirm the command file is ready to double-click tomorrow morning:
- `scripts/run_medina_both.command` → right-click → Open → confirm it launches Terminal

**Target:** 50-80 Medina County property managers + contractors into pipeline.

---

### ✅ Action 3 — Read the Battle Card + Set Your Alarm (5 minutes)

1. Open: `outputs/donna/june4_enrollment_battle_card_2026-05-24.md`
2. Read the full battle card (7 min read) — it tells you exactly what to run and in what order tomorrow
3. Set your alarm: **7:30am** — the Summit + Medina pulls take 6-10 min unattended and should finish before 8am

That's it. You're set for tomorrow.

---

## JUNE 4 MORNING SEQUENCE (preview)

| Time | Action | Command/Tool | Time |
|------|--------|--------------|------|
| 7:30am | Double-click `run_summit_both.command` | Pull + enroll Summit | 8 min unattended |
| 7:40am | Double-click `run_medina_both.command` | Pull + enroll Medina | 8 min unattended |
| 8:00am | Check Nina's hot leads report | `python3 workers/nina_report.py daily` | 2 min |
| 8:15am | Review new enrollments in Mixmax | app.mixmax.com → sequences | 5 min |
| 9:00am | Ads Week 1 final check | Facebook Ads Manager + Google Ads | 15 min |

Full June 4 guide: `outputs/donna/june4_enrollment_final_brief_2026-06-03.md`

---

## WHAT YOU DON'T NEED TO DO TONIGHT

- ❌ No Apollo pull tonight (automated in tomorrow's .command scripts)
- ❌ No Mixmax sequence editing (already loaded with VOC copy from May 23)
- ❌ No gas station sequence creation (can wait — those 12 contacts will be enrolled after June 8)
- ❌ No ad changes (Week 1 is a no-touch zone — check tomorrow morning only)

---

## CRITICAL REMINDER: JUNE 8 IS 5 DAYS AWAY

The Cuyahoga County mega-pull fires June 8. **Block 90 minutes on your calendar right now.**

- 180+ commercial segments fire for the first time
- Hospitals (Cleveland Clinic, UH, MetroHealth), museums, county jails, federal facilities, concrete plants, LTAC hospitals, and 170+ other segments
- This is the largest single-day commercial lead pull of 2026

Prep guide: `outputs/donna/june8_cuyahoga_megapull_exec_guide_2026-06-03.md`

---

*You have 30 minutes. Action 1 first. Go.*
