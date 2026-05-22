# Memorial Day Week Full Playbook — May 26–30, 2026
*Donna Park | Growth & Launch Strategist*
*Written: 2026-05-22 | Covers the 5 days after Memorial Day weekend*

---

## Context Going In
- Touch 3 fired May 22. 72-hour reply window closed May 25.
- Round 2 decision gate: May 25 evening (see `outputs/donna/may25_round2_decision_gate_2026-05-22.md`)
- Danny cron has been down since May 12 — Summit County pull is overdue
- 18 gas station contacts sitting unenrolled (sequence ID pending)
- Ads written and ready — not launched
- Past customer blast not sent
- Google Business Profile: no posts in weeks

---

## Monday May 26 — BLITZ DAY
*Estimated time: 2.5–3 hours total*

**See `outputs/donna/may26_blitz_action_card.md` for full detail.**

Quick order:
1. ✅ Check Mixmax for Touch 3 replies (5 min)
2. ✅ Text Tier 1 contractors — Anthony/Land Pro, Dontez/GTP, Chris/Twin, Venus/Reliable, Logan/Pagels (20 min)
   → Scripts: `outputs/tommy/contractor_referral_text_script_2026-05-20.md`
3. ✅ Follow up contacted contractors — Bulletproof, Damrons, CLE Lawn (10 min)
   → Scripts: `outputs/tommy/contractor_followup_texts_may26_2026-05-21.md`
4. ✅ Run Danny Summit County pull manually: `python3 workers/lead_pipeline.py danny` (automated — 5 min to start)
5. ✅ Create Mixmax gas station sequence → paste ID into `integrations/mixmax.py` → run pipeline (30 min)
   → Guide: `outputs/vera/mixmax_sequence_setup_guide_2026-05-20.md`
6. ✅ Past customer text blast — 20–30 contacts from Workiz history (45 min)
   → Guide: `outputs/donna/past_customer_reengagement_launch_2026-05-21.md`
7. ✅ Google Business Profile post — photo + caption (10 min at business.google.com)
   → Templates: `outputs/vera/gbp_post_may21_2026.md`
8. ✅ Set up Google Ads — paste copy from `outputs/rick/google_ads_june_2026-05-19.md` (45 min)

**End-of-day goal:** Tier 1 texts sent, Danny running, past customer blast done, GBP posted.

---

## Tuesday May 27 — FOLLOW-UP + ADS LAUNCH
*Estimated time: 1.5–2 hours total*

### Morning (8–9am)
- Check replies from Tier 1 contractor texts (May 26)
  - YES → send onboarding text (script in `outputs/carla/referral_partner_onboarding_[date].md`)
  - Not yet → no action, let it breathe 48h
- Check Mixmax for any new Touch 3 replies that came in after May 25 (they still count)
- Reply to any PM sequence replies using `outputs/tommy/touch3_reply_response_templates_2026-05-20.md`

### Late Morning (9am–noon)
- **Launch Facebook Ads** (if not done Monday)
  - Full setup: `outputs/rick/facebook_ads_peak_season_2026-05-20.md`
  - Budget: $30/day to start. Awareness + Lead Gen campaigns first.
  - Audiences: homeowners 35–65, NE Ohio counties, home improvement interests
- Check past customer blast responses (from May 26)
  - Use bridge email script to any who reply: `outputs/tommy/hot_lead_bridge_email_2026-05-19.md`

### LinkedIn Actions (30 min)
- Connect with any contacts from Touch 3 who opened 2+ times but haven't replied
- Use connection note from `outputs/tommy/linkedin_followup_post_connect_2026-05-20.md` (Version A)
- Post one Jasmine LinkedIn post: see `outputs/jasmine/linkedin_posts_june_2026-05-21.md` (Post 1 of 10)

---

## Wednesday May 28 — PHONE DAY + DANNY STATUS CHECK
*Estimated time: 1–2 hours total*

### Morning — Phone Calls
Call the top 3–5 contacts by open count (from Mixmax) who have NOT replied after 3 emails.
- Call script: `outputs/tommy/hot_lead_phone_script_2026-05-22.md`
- Leave a 30-second voicemail if no answer
- Best call window: 10–11am or 2–3pm (property managers at desk)

### Check Danny's Summit County Pull
- `cat logs/cron.log | tail -30` — verify Danny ran on May 26
- If it didn't run, run manually NOW: `python3 workers/lead_pipeline.py danny`
- Target: 15–25 new Summit County property managers in cache before June 2

### Google Ads Check (if launched May 26–27)
- Log into Google Ads — check impressions and clicks (first 24–48h data)
- If CPC > $5 or CTR < 2%, check keyword match types and ad copy
- Reference: `outputs/rick/google_ads_june_2026-05-19.md`

### Past Customer Follow-ups
- Any past customers who texted back but haven't booked — send quote follow-up
- Script: `outputs/tommy/quote_followup_sequence_2026-05-20.md` (Day 1 version)

---

## Thursday May 29 — MEDINA COUNTY PREP + CONTENT
*Estimated time: 45 min total*

### Danny — Medina County is next (Week 22, June 1 cron)
- Verify crontab is set and will fire June 1: `crontab -l`
- If launchd is configured instead: `launchctl list | grep forestcity`
- If neither is set up: install from `scripts/crontab_setup.txt` or `scripts/danny_launchd_plist.xml`
- Medina County targets: Medina, Brunswick, Wadsworth — medium-density market, less competitive than Cuyahoga

### Jasmine Content Batch
- Schedule Facebook posts for May 27–30 week (use `outputs/jasmine/facebook_posts_may26_week_2026-05-20.md`)
- 3–4 posts this week minimum. Before/after + educational + local angle.
- Post LinkedIn update #2 from `outputs/jasmine/linkedin_posts_june_2026-05-21.md`

### GBP Second Post
- If GBP post from May 26 got good views — post a second one
- Use template from `outputs/vera/gbp_weekly_routine_2026-05-21.md` (Week 2 template)

---

## Friday May 30 — WEEKLY REVIEW + JUNE PREP
*Estimated time: 30–45 min total*

### Run Nina Weekly Report (locally)
```
python3 workers/nina_report.py weekly
```
Review: enrolled count, open rate, reply count, hot leads list with names.

### Decision Points — Check Each
| Question | If YES | If NO |
|----------|--------|-------|
| Reply rate ≥ 5% (2+ replies from 45 enrolled)? | Keep sequence, start Round 2 enrollment | Rewrite Email 1 for Round 2 (see `outputs/tommy/round2_pm_sequence_rewrite_2026-05-21.md`) |
| Danny Summit County pull confirmed in logs? | Proceed with Medina June 1 | Run manually today |
| Gas station sequence created + enrolled? | ✓ Done | Create Mixmax sequence next |
| Facebook ads live? | Check spend vs clicks | Launch by June 1 (peak June window) |
| Past customer replies converting? | Quote them this week | Try follow-up text Sunday |

### Build the June Week 1 Checklist
Review `outputs/donna/june_week1_sprint_2026-05-20.md` — this is your roadmap for June 2–6.
- Confirm Round 2 enrollment date: June 4
- Confirm Medina County pull: June 1
- Confirm Google Guaranteed badge application submitted (takes 1–3 days to approve)
  → Guide: `outputs/rick/google_guaranteed_setup_2026-05-22.md`

---

## 5-Day Outcome Tracker

| Day | Key Actions | Done? | Notes |
|-----|------------|-------|-------|
| Mon May 26 | Tier 1 texts, Danny pull, past customer blast, GBP post | | |
| Tue May 27 | FB ads launch, LinkedIn connects, reply follow-ups | | |
| Wed May 28 | Phone calls to hot leads, ads check, Danny status | | |
| Thu May 29 | Medina prep, content batch, GBP post #2 | | |
| Fri May 30 | Nina weekly report, all decision checks, June prep | | |

---

## June 1 Entry Criteria
By end of May 30, you want:
- [x] At least 2 contractor text replies (YES or referral)
- [x] Danny Summit County pull confirmed in logs
- [x] Facebook or Google ads live with first data
- [x] Past customer blast sent to 20+ contacts
- [x] Round 2 decision made (rewrite or keep sequence)
- [x] GBP has at least 1 fresh post
- [x] Gas station sequence created or scheduled

If 5+ of 7 are checked, June Booking Blitz starts in a strong position.
If fewer than 5, prioritize the ones most likely to generate revenue this week.

---

*See June Booking Blitz brief: `outputs/donna/campaign_brief_june_booking_blitz_2026-05-19.md`*
*See June Week 1 Sprint (June 2–6): `outputs/donna/june_week1_sprint_2026-05-20.md`*
*See Round 2 Decision Gate: `outputs/donna/may25_round2_decision_gate_2026-05-22.md`*
