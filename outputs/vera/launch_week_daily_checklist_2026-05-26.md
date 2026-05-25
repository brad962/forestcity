# Launch Week Daily Micro-Checklist — May 26–31, 2026
*10 minutes per day. This is what keeps the launch from losing momentum.*
*Written by Vera Cole, Chief Innovation Officer*

---

## Tuesday May 26 — LAUNCH DAY
**Full guide:** `outputs/donna/may26_final_launch_brief_2026-05-25.md` (read this first)
**End-of-day check:** `outputs/donna/launch_day_evening_debrief_2026-05-26.md`

Morning (90 min):
- [ ] Run Summit County pull: `python3 workers/lead_pipeline.py danny Summit`
- [ ] Check replies: `python3 workers/check_replies.py`
- [ ] Pause Instantly.ai: app.instantly.ai → a1c08c3d + 626cd15d → ⋮ → Pause → add `INSTANTLY_PAUSED=true` to .env
- [ ] Swap Facebook ad hooks (15 min): `outputs/rick/facebook_ad_creative_voc_refresh_2026-05-24.md`
- [ ] Set up Google Ads conversion tracking (20 min): `outputs/rick/google_ads_conversion_tracking_setup_2026-05-25.md`
- [ ] Launch Facebook ads → Launch Google ads
- [ ] GBP Post 1 (2 min): `outputs/vera/launch_week_gbp_posts_2026-05-25.md` → Post 1
- [ ] Gas station emails Wave 1 (7 contacts, 20 min): `outputs/danny/gas_station_manual_email_blast_2026-05-25.md`
- [ ] Contractor texts — Anthony first (440-320-2779): `outputs/vera/memorial_day_contractor_text_card_2026-05-24.md`

---

## Wednesday May 27
- [ ] **Google Ads first look** — any impressions yet? See `google_ads_first_week_monitoring_guide_2026-05-24.md` Day 1 section
- [ ] **Facebook first look** — any leads? Check Ads Manager. Respond within 5 min if yes.
- [ ] **GBP Post 2** (2 min) — copy Post 2 from `outputs/vera/launch_week_gbp_posts_2026-05-25.md`
- [ ] **check_replies.py** — `python3 workers/check_replies.py` (10 sec)
- [ ] **Contractor follow-up** — did any contractors text back? Respond immediately.
- [ ] **Gas station emails** — check for any replies; respond within 24h

---

## Thursday May 28
- [ ] **Gas station emails Wave 2** (11 contacts, 15 min) — `outputs/danny/gas_station_manual_email_blast_2026-05-25.md`
- [ ] **GBP Post 3** (2 min) — copy Post 3 from `outputs/vera/launch_week_gbp_posts_2026-05-25.md`
- [ ] **Facebook ads** — any leads? If CPL > $30, check hook copy. `facebook_ad_week1_revenue_tracker_2026-05-24.md` → fill in Day 3 column
- [ ] **check_replies.py** — `python3 workers/check_replies.py`
- [ ] **Past customer texts** (10 min, 5 contacts) — if not done yet: `outputs/tommy/past_customer_june_text_scripts_2026-05-24.md`

---

## Friday May 29
- [ ] **GBP Post 4** (2 min) — copy Post 4 from `outputs/vera/launch_week_gbp_posts_2026-05-25.md`
- [ ] **check_replies.py** — `python3 workers/check_replies.py`
- [ ] **Any jobs booked this week?** — If yes: enter in Workiz (`outputs/nina/workiz_job_entry_sop_2026-05-26.md`), send booking confirmation text (`outputs/tommy/booking_confirmation_text_2026-05-25.md`)
- [ ] **Summit County catch-up** — if pull didn't happen Tuesday, run it TODAY (deadline Sunday): `python3 workers/lead_pipeline.py danny Summit`
- [ ] **Neighbor canvass reminder** — if doing a job this week, bring door-knock scripts: `outputs/tommy/neighbor_canvass_script_2026-05-26.md`

---

## Saturday May 30
- [ ] **GBP Post 5 — Summit County** (2 min) — copy Post 5 from `outputs/vera/launch_week_gbp_posts_2026-05-25.md`
- [ ] **Facebook weekend post** (2 min) — Post 5 from `outputs/jasmine/facebook_posts_may26_week_2026-05-24.md` (behind-the-scenes)
- [ ] **Any jobs running today?** — Capture before/after photos for Jasmine. Protocol: `outputs/jasmine/before_after_photo_capture_protocol_2026-05-23.md`
- [ ] **Summit pull deadline reminder** — if still not done, MUST run today: `python3 workers/lead_pipeline.py danny Summit`

---

## Sunday May 31 — SUMMIT DEADLINE
- [ ] **FINAL DEADLINE: Summit County pull** — `python3 workers/lead_pipeline.py danny Summit`
  If not done by end of day: open `outputs/carla/summit_county_referral_pull_guide_2026-05-23.md` to confirm completion path
- [ ] **check_replies.py** — any weekend replies?
- [ ] **Facebook engagement** — reply to any comments on this week's posts (5-star signal for algorithm)
- [ ] **Instagram** (if activated) — post Story from a job this week; `outputs/jasmine/instagram_stories_scripts_2026-05-24.md`
- [ ] **Preview next week** — Monday June 1 = Medina County pull. Double-click: `scripts/run_medina_both.command`

---

## Rolling Priorities All Week

**Every day an inbound lead comes in:**
1. Call within 5 minutes: `outputs/rick/facebook_lead_response_sop_2026-05-24.md`
2. Get the YES: pricing guide is in the SOP
3. Send booking confirmation: `outputs/tommy/booking_confirmation_text_2026-05-25.md`
4. Log in Workiz: `outputs/nina/workiz_job_entry_sop_2026-05-26.md`

**Every job completed this week:**
1. Ask for Google review (text template in `outputs/tommy/review_request_sequence_2026-05-18.md`)
2. Capture before/after photos
3. Send annual plan pitch within 2 hours: `outputs/tommy/annual_plan_upsell_sequence_2026-05-24.md`
4. Door-knock the 3 neighbors closest to the job site: `outputs/tommy/neighbor_canvass_script_2026-05-26.md`

---

## Week Summary — What Success Looks Like by Sunday May 31

| Metric | Target |
|--------|--------|
| Facebook ad leads | 3–10 |
| Google ad leads | 0–3 (ads often take until Day 3-5 to generate leads) |
| Jobs booked | 2–5 |
| Summit County pull | Done ✅ |
| GBP posts published | 5 |
| Instantly.ai paused | ✅ (9 days recovery before June 4) |
| Past customer texts sent | 5–10 |
| Gas station emails sent | 18 (Waves 1+2) |
| Tier 1 contractor texts | 5 |

---

*Next week (June 1–7): Medina County pull → check_replies → gas station sequence → Round 2 enrollment prep.*
*Guide: `outputs/donna/june_week1_sprint_2026-05-24.md`*

*Generated: 2026-05-25 | Vera Cole, Chief Innovation Officer*
