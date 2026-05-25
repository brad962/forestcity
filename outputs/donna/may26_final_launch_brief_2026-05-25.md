# May 26 — Final Launch Brief
### Memorial Day +1 | Tuesday Morning Blitz | Forest City Power Washing
*Donna Park | 2026-05-25 — Read this FIRST on Tuesday morning*

---

## THE SITUATION RIGHT NOW

It is Memorial Day night. Tomorrow is the most important single day of peak season so far.

- Facebook + Google ads are loaded and ready. **They need to go live.**
- Summit County pull is 13 days overdue. **Deadline May 31 — 5 days from tomorrow.**
- 18 gas station district managers have been waiting 5 weeks for an email. **Send tomorrow.**
- 5 Tier 1 contractors have never received a personal text. **Send tomorrow.**
- Instantly.ai overlap is killing reply rates. **Pause before Round 2 enrollment.**

Do these 6 things tomorrow morning in order. Total time: ~90 minutes.

---

## TUESDAY MAY 26 — ORDER OF OPERATIONS

### 8:00am — Summit County Pull (20 min)
**This is non-negotiable. May 31 is the hard deadline.**

Double-click: `scripts/run_summit_both.command` (pulls Danny + Carla simultaneously, no typing)

OR manually:
```bash
python3 workers/lead_pipeline.py danny Summit
python3 workers/lead_pipeline.py carla Summit
```

Watch the terminal. You'll see leads printing in real-time. When it finishes, you have fresh Summit County property managers and referral partners in the pipeline ready for June 4 enrollment.

---

### 8:30am — Check Replies + Hot Leads (5 min)
```bash
python3 workers/check_replies.py
```

The 72-hour Touch 3 reply window closed yesterday (Memorial Day). This check tells you if anyone replied over the weekend. Slack gets the summary automatically.

**If there are replies:** Use `outputs/tommy/touch3_reply_response_templates_2026-05-20.md` — respond within 1 hour.
**If 0 replies:** Pivot to Round 2 June 4 enrollment. Everything is staged and ready.

---

### 8:45am — Pause Instantly.ai (5 min)
Go to app.instantly.ai → Campaigns → Find these two:
- Campaign a1c08c3d (PM Cuyahoga)
- Campaign 626cd15d (Contractor Referral)

Click the three dots (⋮) next to each → Pause.

Then open your `.env` file and add: `INSTANTLY_PAUSED=true`

**Why this matters:** These campaigns are sending to the same contacts as Mixmax. Double emails = spam filter = 0% reply rate. This is the root cause of the 0-reply problem. Pause it before Round 2 enrollment or Round 2 fails the same way.

Full guide: `outputs/vera/instantly_pause_guide_2026-05-22.md`

---

### 9:00am — Facebook Ads Launch (20 min)
**BEFORE YOU CLICK LAUNCH — swap the hooks. Takes 10 minutes.**

Read: `outputs/rick/facebook_ad_creative_voc_refresh_2026-05-24.md`

The May 20 ad copy was written before Marcus built the VOC library. The refresh file has 6 drop-in hooks using the exact phrases NE Ohio customers use. Better hooks = lower cost per lead = faster payback.

Then go to business.facebook.com → Ads Manager → Campaign 2 (Lead Gen) → Edit ad → paste new hook → Publish.

Budget to start: **$30/day** (Campaign 2 Lead Gen only). Don't launch all 3 campaigns at once — let Lead Gen prove itself first.

Read first: `outputs/rick/facebook_ads_first_week_monitoring_guide_2026-05-23.md` — Day 1 checklist is in there.

---

### 9:30am — Gas Station Email Blast (20 min)
18 district managers have been waiting 5 weeks. They're worth more per contact than anyone else in the pipeline.

Full guide: `outputs/danny/gas_station_manual_email_blast_2026-05-25.md`

**Tier 1 Wave 1 (7 emails — send individually, 90 sec each):**
- Jim Lavigne — jlavigne@certifiedoil.com
- Kevin Kayden — kkayden@speedway.com
- Stephan Saumid — ssaumid332@speedway.com
- Mark Elyden — melyden@truenorth.org
- John Borchert — jborchert@truenorth.org
- Amer Odat — aodat@openpantry.com
- Nicholas Goad — nicholas.goad@7-11.com

Copy the template from the blast guide. Fill in [First Name] and [Company]. Send. Repeat.

**Time: ~15 minutes for all 7.**

---

### 9:55am — Tier 1 Contractor Texts (10 min)
5 contractors, 5 copy-paste texts. These referral partners have the highest per-referral volume in the pipeline.

Scripts: `outputs/vera/memorial_day_contractor_text_card_2026-05-24.md`

| Name | Company | Phone | Text first? |
|------|---------|-------|-------------|
| Anthony | Land Pro Landscaping | 440-320-2779 | YES — highest referral volume |
| Dontez | GTP | 440-396-0814 | 2nd |
| Chris | Twin Improvements | 216-773-0757 | 3rd |
| Venus | Reliable Roofing | 216-810-2497 | 4th |
| Logan | Pagels | 216-956-5263 | 5th |

If anyone texts back, use `outputs/tommy/hot_lead_callback_script_2026-05-24.md`.

---

### 10:10am — Create Gas Station Mixmax Sequence (15 min, optional)
If you have 15 minutes after the above, create the Mixmax sequence so the 18 contacts can be auto-enrolled.

Step-by-step guide: `outputs/danny/gas_station_mixmax_sequence_creation_2026-05-23.md`

Once you paste the sequence ID into `integrations/mixmax.py`, run:
```bash
python3 workers/lead_pipeline.py pending
```
This auto-enrolls all 18 gas station contacts AND any fleet washing contacts. The gas station Instantly bypass is now in the code — no need for INSTANTLY_PAUSED=true for these contacts.

---

## WEEK PRIORITIES (May 26–30)

| Day | Priority | Time |
|-----|----------|------|
| Tue May 26 | Summit pull + Ads launch + Gas station emails | 90 min AM |
| Wed May 27 | Check ad metrics (Day 1 — don't change anything yet) | 10 min |
| Thu May 28 | Gas station Wave 2 emails (11 contacts) | 15 min |
| Thu May 28 | Google Ads launch (if not done Tuesday) | 20 min |
| Fri May 29 | Check replies again + Nina weekly report | 15 min |
| Fri May 29 | GBP photo upload (any job photo from the week) | 5 min |

---

## ROUND 2 ENROLLMENT (JUNE 4)

Everything is staged. You just need to not miss the steps above.

**Night of June 3 — Pre-check:**
Read `outputs/donna/round2_enrollment_readiness_checklist_2026-05-23.md`
All 5 items must be green before enrolling.

**June 4 morning — Press GO:**
Read `outputs/donna/june4_enrollment_battle_card_2026-05-24.md`
Has copy-paste commands for Summit + Medina + pending sequence enrollment.

---

## REVENUE MATH (TOMORROW'S ACTIONS)

| Action | Effort | Revenue Potential |
|--------|--------|-------------------|
| Summit County pull | 20 min | 50 fresh PM leads → ~10% reply rate = 5 leads → 1–2 booked = $600–$1,200 |
| Facebook ads launch | 20 min | $30/day → 2–3 leads/day → 1 job/week = $400–$600/week recurring |
| Gas station emails | 20 min | 1 account = 5–15 locations × $300/visit × 2/yr = $3,000–$9,000/yr |
| Contractor texts | 10 min | 1 referral per month × $450/job = $5,400/yr per partner |
| **Total tomorrow AM** | **~90 min** | **$10,000–$15,000 in new pipeline value** |

---

## FILES REFERENCED

| Purpose | File |
|---------|------|
| Summit pull shortcut | `scripts/run_summit_both.command` |
| Facebook VOC hook swap | `outputs/rick/facebook_ad_creative_voc_refresh_2026-05-24.md` |
| Facebook first-week monitoring | `outputs/rick/facebook_ads_first_week_monitoring_guide_2026-05-23.md` |
| Gas station email blast guide | `outputs/danny/gas_station_manual_email_blast_2026-05-25.md` |
| Gas station Mixmax creation | `outputs/danny/gas_station_mixmax_sequence_creation_2026-05-23.md` |
| Contractor text scripts | `outputs/vera/memorial_day_contractor_text_card_2026-05-24.md` |
| Instantly.ai pause guide | `outputs/vera/instantly_pause_guide_2026-05-22.md` |
| Touch 3 reply templates | `outputs/tommy/touch3_reply_response_templates_2026-05-20.md` |
| Round 2 readiness checklist | `outputs/donna/round2_enrollment_readiness_checklist_2026-05-23.md` |
| June 4 battle card | `outputs/donna/june4_enrollment_battle_card_2026-05-24.md` |

---

*Donna Park | Forest City AI Office | 2026-05-25*
