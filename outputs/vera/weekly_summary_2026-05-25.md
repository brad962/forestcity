# Vera Cole — Weekly Summary
### Monday, May 25, 2026 (Memorial Day)
*Week of May 19–24 | Runs 52–73*

---

## Upgrades Shipped This Week (17 auto-upgrades)

### Scripts & Workers
- **check_replies.py** — Added company enrichment, hot-lead Slack notification, "all clear" Slack post when API alive but pipeline quiet; Bradley can now tell if the script ran even on a 0-result day
- **workers/lead_pipeline.py** — Danny per_page 25→50 (doubles leads per pull); Carla per_page 15→20; Carla county override CLI flag; run_carla() double-print bug fixed; run_carla() output filename includes county label (prevents same-day overwrite); home inspection + solar installation added to search keywords
- **workers/vera_relay.py** — Lock file added (prevents concurrent instance collision); unpushed-commit flush added (prevents Slack message loss on push failure); git log window -20→-100; git fetch moved before flush; Danny + Carla staleness alerts updated with double-click shortcuts
- **workers/nina_report.py** — Replied contacts now get company injection in daily + weekly reports; Company column added to REPLIED table
- **integrations/mixmax.py** — 8 new PROPERTY_MANAGER_TITLES (site manager, community director, building operations manager, property administrator, condominium manager, leasing director, center manager, managing partner, principal); home inspector + solar installer + solar panel titles added to CONTRACTOR_TITLES; INSTANTLY_PAUSED runtime warning in enroll_batch()
- **scripts/** — run_summit_pull.command (double-click Danny Summit pull); run_summit_both.command (double-click Danny + Carla Summit pull)

### Agent Files
- **danny.md** — Week 21 = Summit County deadline clarified; Instantly.ai campaigns flagged as ACTIVE (was "Not active"); per_page example updated 25→50; gas_station_manual_email_blast format added
- **carla.md** — County rotation calendar added; 5 new output format entries; pool_service_referral_blitz added
- **rick.md** — "Monday after Memorial Day" date fixed to Tuesday; Google Ads + Facebook monitoring guide format entries added
- **tommy.md** — 6 new output format entries (hot_lead_callback_script, past_customer_june_text_scripts, annual_plan_customer_welcome_kit, inbound_response_protocol, etc.)
- **donna.md** — June Booking Blitz section updated with current action docs; 4 new format entries
- **jasmine.md** — instagram_stories_scripts, before_after_photo_capture_protocol, facebook_posts_memorial_day_weekend format entries added
- **nina.md** — check_replies.py reference added
- **CLAUDE.md** — Quick Shortcuts section added (run_summit_pull.command + run_summit_both.command)
- **marcus.md** — Local run commands added

---

## Deliverables Written This Week (20 files)

| File | Owner | What It Does |
|------|-------|-------------|
| facebook_posts_may26_week_2026-05-24.md | Jasmine | 5 launch-week posts Tue–Sat, Post 1 at 8am before ads |
| facebook_posts_memorial_day_weekend_2026-05-23.md | Jasmine | Sat/Sun/Mon holiday posts |
| instagram_stories_scripts_2026-05-24.md | Jasmine | 5 story scripts for peak season |
| linkedin_posts_may26_week_2026-05-23.md | Jasmine | PM-targeted May 26–30 LinkedIn posts |
| google_ads_first_week_monitoring_guide_2026-05-24.md | Rick | Day 1/3/7 Google Ads launch guide |
| facebook_ads_first_week_monitoring_guide_2026-05-23.md | Rick | Day 1/3/7 Facebook Ads guide |
| facebook_lead_response_sop_2026-05-24.md | Rick | Facebook Lead Gen form response SOP |
| facebook_lead_gen_launch_checklist_2026-05-24.md | Rick | Pre-launch checklist (Pixel, budget, notifications) |
| facebook_ad_week1_revenue_tracker_2026-05-24.md | Rick | Fill-in revenue tracker with benchmarks |
| google_guaranteed_setup_2026-05-22.md | Rick | Google Guaranteed application guide |
| june4_enrollment_battle_card_2026-05-24.md | Donna | Press-GO June 4 enrollment execution card |
| may26_week_priority_stack_2026-05-24.md | Donna | Single-page Tue–Fri priority cheat sheet |
| tuesday_may26_launch_card_2026-05-23.md | Donna | 90-min Tuesday launch plan with revenue math |
| round2_enrollment_readiness_checklist_2026-05-23.md | Donna | GO/NO-GO checklist for June 3 prep night |
| june_week1_sprint_2026-05-24.md | Donna | Refreshed June 2–6 day-by-day sprint |
| round2_pm_sequence_voc_rewrite_2026-05-23.md | Tommy | Round 2 PM emails using NE Ohio VOC language |
| hot_lead_callback_script_2026-05-24.md | Tommy | Word-for-word callback script for warm inbound callers |
| annual_plan_customer_welcome_kit_2026-05-24.md | Tommy | Post-YES annual plan onboarding (4-touch sequence) |
| past_customer_june_text_scripts_2026-05-24.md | Tommy | June 4 past customer text blast scripts |
| voc_library_2026-05-23.md | Marcus | 40+ NE Ohio exterior cleaning customer phrases |

---

## Proposals Pending Bradley's Approval (4 open)

1. **Kit.com email capture + NE Ohio Home Maintenance Checklist** — Free list-building alongside ads; Tommy writes 12-month checklist (~2h), Donna sets up landing page (~1h). Organic lead capture forever after.
2. **Yelp Business profile activation** — Free local search channel; 15-min setup; most NE Ohio competitors don't manage theirs.
3. **Google Guaranteed application** — Highest-ROI channel (pay-per-lead, not pay-per-click, Google trust badge at top of search). Guide ready at `outputs/rick/google_guaranteed_setup_2026-05-22.md`. File TODAY — takes 7–14 days to approve.
4. **Twilio pre-job reminder texts** — $15/mo, automates day-before + 2-hour reminders, reduces no-shows 40%+.

---

## Biggest Opportunity This Week

**Tuesday May 26 is worth an estimated $3,000–$9,600 in pipeline.**

Everything is staged. Tuesday is a press-GO moment:
1. **8am** — Post `facebook_posts_may26_week_2026-05-24.md` Post 1 on Facebook
2. **9:15am** — Launch Google Ads + Facebook Ads (assets in `outputs/rick/`)
3. **10am** — Send past customer text blast (`outputs/tommy/past_customer_june_text_scripts_2026-05-24.md`)
4. **Any time** — Text Anthony/Land Pro 440-320-2779 (Tier 1 contractor, still "New Lead")
5. **Pause Instantly.ai** — app.instantly.ai → a1c08c3d + 626cd15d → Pause (3 min, critical for June 4 email deliverability)

Use `outputs/donna/may26_week_priority_stack_2026-05-24.md` as the one-page master checklist for the week.

---

## Open Issues (18 — all require Bradley action)

| Issue | Days Open | Status |
|-------|-----------|--------|
| Tier 1 contractors untexted | 6 | Text today or Tuesday |
| Instantly.ai not paused | 6 | CRITICAL — pause before June 4 |
| 0% reply rate | 6 | Window closes today |
| Danny cron down (12+ days) | 12 | Double-click run_summit_pull.command |
| Facebook + Google Ads not launched | 4 | Launch Tuesday 9:15am |
| Gas station sequence PENDING | 5 | Create in Mixmax UI → 10 min |
| GBP not managed | 4 | Post `june_gbp_content_calendar_2026-05-24.md` Week 1 post |
| Past customer reengagement | 4 | Send June 4 text blast |

*Full list in `outputs/vera/open_issues.md`.*

---

*Generated automatically by Vera | 2026-05-25 06:00*
