# May 27 — Day 2 Morning Card
### Wednesday | 8:00–8:10am | 10 minutes total
*Vera Cole | Generated 2026-05-26*

---

## DO THESE IN ORDER. DO NOT SKIP.

---

### STEP 1 — Check Yesterday's Ad Leads (3 min)

Open `pipeline_data.json`. For any lead logged since yesterday (May 26):
- ✅ Stage is "Contacted" (you responded within 1 hour)
- ✅ `next_followup` is set to today (2026-05-27) or tomorrow
- ✅ `first_response_time` is under 60 minutes (if not tracked, note it now)

**If 0 leads logged from ads on Day 1:** Normal. Facebook learning phase, Google impressions building. Do NOT edit ads. Check again tomorrow.

**If you got a lead and haven't responded:** Stop and respond NOW before doing anything else.

Reference files:
- `outputs/rick/ad_lead_notification_setup_2026-05-25.md` — notification setup (do this if not done)
- `outputs/nina/ad_lead_tracker_2026-05-25.md` — how to log to pipeline_data.json
- `outputs/donna/zero_leads_day1_contingency_2026-05-25.md` — if Day 1 = 0 leads, read this

---

### STEP 2 — Summit County Pull (4 min, unattended after click)

**5 DAYS LEFT. May 31 is the hard wall.**

Double-click `scripts/run_summit_pull.command` in Finder right now.
- The script runs unattended. You can do Step 3 while it runs.
- Takes ~6 minutes. You'll see output in Terminal.
- If Terminal doesn't open: `python3 workers/lead_pipeline.py danny Summit` in Terminal.

**Why this matters:** Fresh Summit County leads are the fuel for June 4 Round 2 enrollment. If you don't pull by May 31, Summit County gets skipped entirely — next rotation is June 29 (too late). Medina is June 1 (right after), so Summit first.

---

### STEP 3 — Gas Station Wave 1 (while Summit pull runs) (3 min)

Open `outputs/danny/gas_station_manual_email_blast_2026-05-25.md`
Send Wave 1 (Tier 1 — 7 contacts). Copy-paste template. Fill in first name. Send from Gmail.

**If already sent yesterday (May 26):** ✅ Skip.

Wave 1 contacts: Jim, Kevin, Stephan, Mark, John, Amer, Nicholas — all in the file.

Wave 2 (11 contacts) goes Thursday May 28.

---

### STEP 4 — Ads Manager Glance (30 seconds, READ ONLY)

Ads Manager → look at:
- Facebook: spend, impressions, CTR (is anything showing?)
- Google: impressions, clicks, conversions

**DO NOT EDIT ANYTHING.** Day 2 is inside the learning phase. Any change resets the algorithm.

If numbers look bad: Read `outputs/donna/zero_leads_day1_contingency_2026-05-25.md` — Day 1-2 benchmarks explain what "normal" looks like.

---

### STEP 5 — GBP Post (under 2 min)

Go to business.google.com → Post → Photo + caption.
Use `outputs/jasmine/june_gbp_content_calendar_2026-05-24.md` for this week's post.
One post per day during launch week = sustained local SEO signal.

---

## WEDNESDAY PRIORITY STACK (rest of day)

| Priority | Task | Time | File |
|----------|------|------|------|
| 🔴 #1 | Pause Instantly.ai | 3 min | app.instantly.ai → a1c08c3d + 626cd15d → ⋮ → Pause |
| 🔴 #2 | Contractor texts (8 overdue) | 17 min | `outputs/vera/launch_day_contractor_outreach_stack_2026-05-26.md` |
| 🟡 #3 | Day 3 check card reminder | Read now | `outputs/vera/day3_ads_check_card_2026-05-26.md` — Thursday May 28 |
| 🟡 #4 | Facebook VOC hook swap | 15 min | `outputs/rick/facebook_ad_creative_voc_refresh_2026-05-24.md` |

---

## WEDNESDAY SUCCESS METRICS

By end of May 27:
- [ ] Summit pull ran (check Terminal output — "X new leads found")
- [ ] Gas station Wave 1 sent (or confirmed sent yesterday)
- [ ] At least 1 GBP post published
- [ ] Ads manager checked (read-only)
- [ ] Any Day 1 ad leads logged in pipeline_data.json + followed up

---

## WHAT COMES NEXT

- **Thursday May 28:** Day 3 ads check (`outputs/vera/day3_ads_check_card_2026-05-26.md`) — first allowed tweak window
- **Thursday May 28:** Gas station Wave 2 (11 contacts)
- **Sunday May 31:** Summit pull DEADLINE (absolute last day)
- **Monday June 1:** Medina County pull (double-click `scripts/run_medina_pull.command`)
- **Tuesday June 3:** Run Round 2 readiness checklist (`outputs/donna/round2_enrollment_readiness_checklist_2026-05-23.md`)
- **Wednesday June 4:** Round 2 enrollment + Carla activation + past customer texts

---
*Use this card every Wednesday morning during launch week. Filed under: `outputs/vera/`*
