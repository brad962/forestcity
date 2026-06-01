# June 1 Launch Day Card — Monday Morning
**Today: Monday, June 1, 2026 | Medina County Pull Day + June 4 Countdown**

> This is the day. Medina County pull fires today. June 4 enrollment is 3 days out.
> Read this first. Everything else waits.

---

## 🔴 BLOCK 1 — Medina County Pull (8:00am, 6 min unattended)

**What:** Run Danny + Carla combined Medina County pull
**How:** Double-click `scripts/run_medina_both.command` in Finder (no terminal needed)
**Time:** 6 minutes — starts immediately, runs in background

Manual alternative:
```bash
python3 workers/lead_pipeline.py both medina
```

**What it pulls:**
- Danny: Property managers, HOA managers, facility managers in Medina/Brunswick/Wadsworth corridor
- Carla: Siding, painting, landscaping, gutter, HVAC referral partners in Medina County
- All 123+ commercial segments fire for Medina County targets

**Why today matters:** Week 23 manual override. After today, the auto-rotation moves to Geauga+Portage. Fresh Medina leads need 3 days to cache before June 4 enrollment. Run before 5pm to guarantee they're in the system for Thursday.

**Note on Summit County:** If the May 31 Summit pull ran — great. If not, Summit contacts won't be in the June 4 enrollment batch (rotation moves to Cuyahoga June 8). Check `logs/activity.log` for "Danny | Summit" to confirm.

---

## 🟡 BLOCK 2 — Ads Check Day 6 (8:30am, 10 min read-only)

Ads launched May 26. Today is Day 6. This is NOT the Day 7 review — just a quick read.

**Check these only:**
1. Facebook Ads Manager → Campaigns → Is spend happening? (should be ~$180 total by now)
2. Any Facebook Lead Gen form submissions? (check Leads Center)
3. Google Ads → Campaigns → Impressions > 0? CTR > 1%?
4. Any calls from Google Ads? (check Call Details report)

**If 0 leads total so far:** Normal at Day 6. Learning phase. Do NOT touch anything. Full Day 7 review tomorrow.
**If 1-3 leads:** Log them in `outputs/rick/launch_week_lead_log_2026-05-26.md`. Respond within 5 min.
**Reference:** `outputs/rick/facebook_ads_first_week_monitoring_guide_2026-05-23.md`

---

## 🟡 BLOCK 3 — Bridge Emails + June 4 Prep (9:00am, 20 min)

**If you haven't sent bridge emails to hot leads yet:**
- Read `outputs/tommy/hot_lead_bridge_email_2026-05-20.md`
- Send to any contacts with 2+ Mixmax opens and 0 reply
- Personal Gmail → NOT automated → feels like a real follow-up

**June 4 enrollment prep — 3 days out:**
Check: Is Instantly.ai paused? (app.instantly.ai → Campaigns → status should show Paused)
Check: Is new Round 2 email copy in Mixmax? (read `outputs/donna/round2_enrollment_plan_2026-05-21.md` if not set up yet)
Check: Is `INSTANTLY_PAUSED=true` in your `.env` file?

**If Instantly NOT paused:** Stop and pause it now. Guide: `outputs/vera/instantly_pause_guide_2026-05-22.md`
**If copy NOT updated:** Do this today. Sequence rewrite: `outputs/tommy/round2_pm_sequence_voc_rewrite_2026-05-22.md`

---

## 🟢 BLOCK 4 — Gas Station Sequence (9:30am, 10 min if Mixmax sequence created)

12 gas station district manager contacts are sitting idle in pipeline_data.json.
They've had `next_followup = 2026-05-27` for days. June 4 is the last window to enroll them before they age out.

**Path A — Mixmax sequence (best):**
1. Create sequence in Mixmax UI (guide: `outputs/danny/gas_station_mixmax_sequence_creation_2026-05-23.md`)
2. Paste ID into `integrations/mixmax.py` line ~54
3. Run: `python3 workers/lead_pipeline.py pending`

**Path B — Manual Gmail blast (backup):**
- Guide: `outputs/danny/gas_station_manual_email_blast_2026-05-25.md`
- 20 min, no code needed

---

## 🟢 BLOCK 5 — GBP Post (10:00am, 2 min)

June GBP content calendar is ready at `outputs/vera/june_gbp_content_calendar_2026-05-24.md`.
Go to `business.google.com` → Post update → Use June Week 1 post (first entry in the calendar).

Free local SEO signal. 2 minutes. Do it before you forget.

---

## 📅 June 1–4 Countdown Table

| Day | Priority Action | File |
|-----|-----------------|------|
| **Mon Jun 1 (TODAY)** | Medina County pull + Instantly pause confirm + Bridge emails | This card |
| **Tue Jun 2** | Check Medina pull results in contacts_cache.json. Respond to any ad leads. | `outputs/nina/hot_leads_[date].md` |
| **Wed Jun 3 (Eve)** | June 3 night-before enrollment checklist: verify Instantly paused + new copy in Mixmax + all flags clear | `outputs/donna/june3_tuesday_evening_checklist_2026-05-26.md` |
| **Thu Jun 4 (ENROLLMENT DAY)** | Run Round 2 enrollment: Danny + Carla leads + pending gas station contacts | `outputs/donna/june4_enrollment_battle_card_2026-05-24.md` |

---

## ✅ Success Criteria for June 1

- [ ] Medina pull ran (check `logs/activity.log` for "Danny | Medina" entry)
- [ ] Ads spend is happening (not stuck at $0)
- [ ] Instantly.ai confirmed paused (app.instantly.ai shows Paused on both campaigns)
- [ ] Round 2 email copy is in Mixmax (new sequence text matches the VOC rewrite)
- [ ] GBP post published (business.google.com — at least 1 post this week)
- [ ] Gas station path selected (Mixmax sequence or Gmail blast — pick one, commit)

---

*Written by Vera Cole — June 1, 2026 (Run 165)*
*Pairs with: june4_enrollment_battle_card_2026-05-24.md | june3_tuesday_evening_checklist_2026-05-26.md*
