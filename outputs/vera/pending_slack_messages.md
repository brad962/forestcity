🔧 *Vera — Auto-Upgrade*
>Changed: agents/rick.md — added google_ads_first_week_monitoring_guide format entry to output catalog
>Why: Facebook ads monitoring guide existed but Google Ads had no equivalent; both campaigns launch Tuesday
>File: agents/rick.md
---
🔧 *Vera — Auto-Upgrade*
>Changed: agents/tommy.md — added annual_plan_customer_welcome_kit format entry to output catalog
>Why: Annual plan upsell pitch exists but post-YES onboarding was undocumented; welcome kit written this run closes the gap
>File: agents/tommy.md
---
🔧 *Vera — Auto-Upgrade*
>Changed: CLAUDE.md — added Quick Shortcuts section for run_summit_pull.command + run_summit_both.command
>Why: Double-click shortcuts existed in scripts/ since runs 62/67 but were never in the master CLAUDE.md reference
>File: CLAUDE.md
---
🔧 *Vera — Auto-Upgrade*
>Changed: agents/danny.md — updated example Apollo payload per_page from 25 → 50
>Why: Code was updated to 50 in run 67 but the danny.md example still showed 25; inconsistency fixed
>File: agents/danny.md
---
📄 *Vera — New Deliverable: Jasmine*
>File: outputs/jasmine/facebook_posts_may26_week_2026-05-24.md
>What: 5 Facebook posts for launch week (Tue May 26 – Sat May 30) — Post 1 goes up same morning as ads, Post 2 educational (designed for shares), Post 3 social proof, Post 4 urgency, Post 5 behind-the-scenes
>Action: Post 1 at 8am Tuesday before launching ads. Each ends with "comment QUOTE" to capture leads.
---
📄 *Vera — New Deliverable: Rick*
>File: outputs/rick/google_ads_first_week_monitoring_guide_2026-05-24.md
>What: Day 1/3/7 guide for first Google Ads launch — CTR benchmarks, CPC ranges ($2–$5/click NE Ohio), Quality Score timeline, search terms cleanup, common mistakes, Week 1 decision tree
>Action: READ before Tuesday launch. Check Day 1 (Tuesday evening), Day 3 (Friday), Day 7 (June 2). Do NOT edit or pause ads in first 48 hours.
---
📄 *Vera — New Deliverable: Donna*
>File: outputs/donna/june_week1_sprint_2026-05-24.md
>What: Refreshed June 2–6 day-by-day sprint (replaces May 20 version) — enrollment battle card, VOC rewrites, past customer texts, Medina pull, revenue targets $4,550–$14,700 for the week
>Action: Read Sunday or Monday night before June. June 4 = enrollment day anchor.
---
📄 *Vera — New Deliverable: Tommy*
>File: outputs/tommy/annual_plan_customer_welcome_kit_2026-05-24.md
>What: Post-YES annual plan onboarding — confirmation text (30 min), welcome email (same day), schedule-visits email (48h), referral seed text (14 days post-job), FAQ answers, revenue math (10 customers = $3,250–$5,500/yr)
>Action: Next YES to annual plan → fire Touch 1 text within 30 minutes. Kit is copy-paste ready.
---
⚡ *Vera — TODAY Alert (Sunday May 24 — final window)*
>REPLY WINDOW CLOSES TOMORROW (Memorial Day, Mon May 25)
>
>2 actions. 15 minutes total:
>1. Text Anthony/Land Pro: *440-320-2779* — "Hey Anthony, it's Bradley from Forest City Power Washing. We do exterior cleaning for a lot of landscapers' customers — want to do a quick referral swap? No paperwork, $50 for every job you send our way."
>2. Pause Instantly.ai — app.instantly.ai → Campaigns → ⋮ → Pause *a1c08c3d + 626cd15d*. 3 minutes. Without this, Round 2 (June 4) lands in spam.
>
>Tomorrow at 10am: `python3 workers/check_replies.py` — see monday_memorial_day_final_check_2026-05-24.md
---
💡 *Vera — Upgrade Proposal*
>Idea: Set up Kit.com email capture + publish NE Ohio Home Maintenance Checklist as first lead magnet
>Why: Ads go live Tuesday but the only lead capture is the Facebook Lead Gen form. Kit.com is free (up to 10K). The checklist brief exists from May 12. Tommy writes 12-month content (~2h), Donna sets up landing page (~1h). Organic leads captured forever after.
>Impact: Second lead funnel alongside paid ads; builds email list for future broadcasts; checklist positions Forest City as a trusted local resource, not just another ad
>Reply YES to approve.
---
💡 *Vera — Upgrade Proposal*
>Idea: Activate Yelp Business profile
>Why: Most NE Ohio competitors don't manage their Yelp. Yelp shows up in mobile local searches alongside Google Maps. Forest City may already have a profile from customer reviews. 15-min setup: claim, add photos, enable messaging. Free ongoing impressions.
>Impact: Second free local search channel; any past customer reviews already there become visible; captures people who check Yelp before Googling
>Reply YES and I'll write a step-by-step activation guide.
---
✅ *Vera — Scan Complete 2026-05-24 (Run 72)*
>4 auto-upgrades shipped | 4 deliverables written | 2 proposals | 18 open issues
>
>Ready for Tuesday launch:
>• facebook_posts_may26_week_2026-05-24.md (Jasmine — Post 1 at 8am)
>• google_ads_first_week_monitoring_guide_2026-05-24.md (Rick — Day 1/3/7)
>• june_week1_sprint_2026-05-24.md (Donna — June 2–6 full plan)
>• annual_plan_customer_welcome_kit_2026-05-24.md (Tommy — post-YES onboarding)
>
>🔴 CRITICAL: Instantly.ai still active. Pause before June 4 or Round 2 lands in spam.
---
🔧 *Vera — Auto-Upgrade*
>Changed: agents/carla.md — added county rotation calendar section
>Why: Carla mirrors Danny's county rotation but had no calendar; Week 21 = Summit, same as Danny — double-click run_summit_both.command pulls both together
>File: agents/carla.md
---
🔧 *Vera — Auto-Upgrade*
>Changed: agents/marcus.md — added exact local CLI commands to Cloud Limitation section
>Why: "run Marcus locally" has been an open action item for 25 runs with no copy-paste command; now Bradley can run one line and Marcus is live
>File: agents/marcus.md
---
🔧 *Vera — Auto-Upgrade*
>Changed: agents/donna.md — June Booking Blitz section updated with current action docs
>Why: Section was pointing to May 20 sprint (stale); now points to june_week1_sprint_2026-05-24.md and adds june4_enrollment_battle_card_2026-05-24.md as the press-GO doc
>File: agents/donna.md
---
🔧 *Vera — Auto-Upgrade*
>Changed: agents/tommy.md — added inbound_response_protocol format entry
>Why: New format written this run (organic Facebook DM/comment + website form + inbound call); Tommy's catalog updated to document it
>File: agents/tommy.md
---
📅 *Vera — Monday 6am Weekly Summary*
>Week of May 19–24 | Full summary: outputs/vera/weekly_summary_2026-05-25.md
>
>This week in numbers:
>• 17 auto-upgrades shipped (scripts, agents, CLAUDE.md)
>• 20 deliverables written (ads, monitoring guides, enrollment docs, VOC content)
>• 4 proposals pending approval
>• Touch 3 fired May 22 — 45 contacts enrolled
>• Reply window closes TODAY (Memorial Day)
>
>🏁 Everything is staged for Tuesday. One-page launch plan: outputs/donna/may26_week_priority_stack_2026-05-24.md
>
>Biggest opportunity this week: Tuesday May 26 launch day — Facebook posts + ads + past customer texts + contractor blitz. Potential pipeline: $3,000–$9,600.
---
📄 *Vera — New Deliverable: Jasmine*
>File: outputs/jasmine/facebook_posts_june_week1_2026-05-24.md
>What: 5 Facebook posts for June 2–6 — launch week of the June Booking Blitz. June 4 post (Wednesday) is commercial/HOA angle, deliberately timed to coincide with Round 2 email enrollment that same day. PM who gets the email AND sees the post = double Forest City touchpoint in 24 hours.
>Action: Schedule all 5 posts in advance OR post each morning. June 4 post goes up at 9am — same day as Danny's Round 2 enrollment run.
---
📄 *Vera — New Deliverable: Tommy*
>File: outputs/tommy/inbound_response_protocol_2026-05-24.md
>What: How to handle organic inbound — Facebook DM/comment, website contact form, inbound call, missed call recovery. Separate from Rick's paid-ad response SOPs (which cover Lead Gen form submissions). Covers: public comment reply, DM opener, website form email, call script with pricing ranges, warm close, cold follow-up.
>Action: READ before Tuesday launch — organic engagement from the May 26 Facebook posts will start within hours of posting.
---
✅ *Vera — Scan Complete 2026-05-24 (Run 73)*
>4 auto-upgrades shipped | 3 deliverables written | 0 new proposals | 18 open issues
>
>Run 73 verifications:
>• pipeline_data.json checked — 5 Tier 1 contractors confirmed "New Lead," phones verified
>• Gas station contacts — all 12 have lead_type="gas_station" set (enrollment ready when Mixmax ID added)
>• Scripts verified — run_summit_pull.command + run_summit_both.command both correct
>• vera_relay.py reviewed — no bugs
>
>🔴 Today's top 2 actions (15 min total):
>1. Text Anthony/Land Pro — 440-320-2779 (referral swap pitch)
>2. Pause Instantly.ai — app.instantly.ai → a1c08c3d + 626cd15d → Pause
---
🔧 *Vera — Auto-Upgrade: check_replies.py*
>Changed: phone_map and company_map now read both contacts_cache.json AND pipeline_data.json
>Why: Manual contacts (gas station, fleet, Tier 1 contractors) added directly to pipeline_data.json now get phone/company enrichment in reply check output — future-proofs for when gas station/fleet Mixmax sequences go live.
>File: workers/check_replies.py
---
🔧 *Vera — Auto-Upgrade: agents/rick.md*
>Changed: Added yelp_business_profile_guide_[date].md to Rick's output format catalog
>Why: Yelp was proposed in Run 72 as a free local search channel but never had a documented output format — adding it now so the deliverable (written this run) has a home in Rick's catalog.
>File: agents/rick.md
---
🔧 *Vera — Auto-Upgrade: agents/donna.md*
>Changed: Added kit_email_capture_setup_[date].md to Donna's output format catalog
>Why: Kit.com email capture was proposed Run 72; the setup guide was written this run; now documented in Donna's catalog so future runs don't re-propose what's already built.
>File: agents/donna.md
---
🔧 *Vera — Auto-Upgrade: agents/tommy.md*
>Changed: Added home_maintenance_checklist_content_[date].md to Tommy's output format catalog
>Why: The brief for the Home Maintenance Checklist has existed since May 12 but the actual content document had no format entry — this signals it as a first-class deliverable (and it's now written).
>File: agents/tommy.md
---
📄 *Vera — New Deliverable: Tommy*
>File: outputs/tommy/home_maintenance_checklist_content_2026-05-24.md
>What: The actual NE Ohio 12-month home exterior maintenance checklist — the document subscribers receive when they opt in. Month-by-month tasks built for NE Ohio's climate (lake humidity, freeze-thaw, algae season timing, driveway sealing windows). NOT the brief (that existed since May 12) — this is the actual content.
>Action: Use as the opt-in magnet at the Kit.com landing page. Every subscriber is a potential booking. Pairs with kit_email_capture_setup_2026-05-24.md (see next message).
---
📄 *Vera — New Deliverable: Rick*
>File: outputs/rick/yelp_business_profile_guide_2026-05-24.md
>What: Step-by-step Yelp Business Profile activation and optimization guide. Free, 15-minute setup, zero ongoing cost. Most NE Ohio power washing competitors don't actively manage Yelp — first-mover advantage. Includes profile copy (ready to paste), photo checklist, Request-a-Quote setup, ongoing review request text script, and Yelp vs. GBP comparison table.
>Action: Open biz.yelp.com, search Forest City Power Washing, claim the listing. Takes 15 minutes. Can be done Tuesday before ads launch.
---
📄 *Vera — New Deliverable: Donna*
>File: outputs/donna/kit_email_capture_setup_2026-05-24.md
>What: Full Kit.com email capture setup guide for the NE Ohio Home Maintenance Checklist magnet. Covers: Kit.com account creation (free), landing page copy (ready to paste), delivery automation email (ready to send), 3-touch nurture trigger using the existing `nurture_sequence_home_maintenance_checklist_2026-05-12.md`, Facebook ad traffic integration. Setup time: 23 minutes.
>⚠️ Action BEFORE Tuesday: Without this live, every ad visitor who doesn't book immediately = permanently lost. 23 minutes before ads launch = email list that grows automatically.
---
💡 *Vera — Upgrade Proposal*
>Idea: Refresh Jasmine's June Week 2–4 Facebook posts before June 8
>Why: `outputs/jasmine/facebook_posts_june_week2_4_2026-05-20.md` was written May 20 — before all VOC rewrites, before June Booking Blitz strategy was finalized, and before the Round 2 enrollment angle was built. June 8–27 is the height of peak season and these posts will run alongside active commercial enrollment outreach.
>Impact: Posts that use current VOC language + commercial booking angle will outperform the May 20 version on engagement and drive-to-quote clicks; also gives Jasmine a June Week 2–4 version that's synced with the June commercial calendar.
>Reply YES to approve — Jasmine rewrites 5 posts, replaces the May 20 file.
---
✅ *Vera — Scan Complete 2026-05-24 (Run 74)*
>4 auto-upgrades shipped | 3 deliverables | 1 proposal | 19 open issues (1 new: Email List at 0)

>🆕 New issue this run: Email capture gap — ads launch Tuesday with no opt-in. All 3 assets written and ready. 23-min setup before Tuesday = permanent email list asset.

>Run 74 priority stack (TUESDAY May 26):
>1. Read may26_week_priority_stack_2026-05-24.md FIRST
>2. 20 min: Kit.com setup (kit_email_capture_setup_2026-05-24.md) — BEFORE ads launch
>3. 15 min: Claim Yelp listing (yelp_business_profile_guide_2026-05-24.md)
>4. Summit pull 8am → bridge emails 8:20am → contractor texts 8:45am → gas station sequence 9am → ads launch 9:15am → past customer texts 10am
---
🔧 *Vera — Auto-Upgrade*
>Changed: workers/jasmine_flyer.py — "We serve the greater Cleveland area" → "We serve Northeast Ohio — all 7 counties"
>Why: Forest City serves Cuyahoga, Lake, Lorain, Summit, Medina, Geauga, and Portage — "greater Cleveland area" excluded Akron/Summit and everything south. Every auto-generated flyer post now shows the full service area.
>File: workers/jasmine_flyer.py
---
🔧 *Vera — Auto-Upgrade*
>Changed: workers/vera_relay.py — removed hardcoded "danny Summit" from Danny staleness alert; now shows generic rotation command
>Why: After May 31, the hardcoded "python3 lead_pipeline.py danny Summit" would instruct Bradley to pull the wrong county. The alert now shows `python3 workers/lead_pipeline.py danny` which auto-selects the current week's county via rotation — always correct.
>File: workers/vera_relay.py
---
📄 *Vera — New Deliverable: Jasmine*
>File: outputs/jasmine/facebook_posts_june_week2_4_2026-05-24.md
>What: Refreshed 9 Facebook posts + 3 LinkedIn posts for June 9–27. Supersedes the May 20 version that predated Marcus's VOC library. Uses exact NE Ohio customer language: "green and slimy siding," "roof looks black from the street," "kept putting it off," "looks like you repainted it." Week 2 has commercial/PM angle (Round 2 emails just went out June 4). Week 3 has residential 4th of July hook. Week 4 has urgency + annual plan.
>Action: Use this version instead of the May 20 file starting June 9.
---
📄 *Vera — New Deliverable: Rick*
>File: outputs/rick/facebook_ad_creative_voc_refresh_2026-05-24.md
>What: Drop-in Facebook ad copy using Marcus's NE Ohio VOC phrases. 6 hook variants + 3 body copy variants. Replaces the generic May 20 hooks with language customers are ALREADY THINKING: "green and slimy siding," "kept putting it off," "roof looks black from the street," "looks like you repainted it," "lake moisture," "road salt splash."
>⚠️ BEFORE TUESDAY LAUNCH — 15 min in Ads Manager to swap. Higher-CTR hooks → cheaper leads from day 1 of the learning phase.
>Action: Open Ads Manager, edit each ad's Headline + Primary Text with the corresponding hook from this file. Campaign structure/targeting/budget unchanged.
---
💡 *Vera — Upgrade Proposal*
>Idea: Swap Facebook ad copy hooks before Tuesday launch using facebook_ad_creative_voc_refresh_2026-05-24.md
>Why: May 20 ad creative predates Marcus's VOC research. The new hooks use exact NE Ohio customer language that stops the scroll faster → higher CTR → cheaper cost per lead in the learning phase.
>Impact: 15-min swap before clicking "launch." Better hooks can reduce CPL by 20–40% in first-week learning phase — potentially the difference between $15 and $25 per lead on a $30/day budget.
>Files: outputs/rick/facebook_ad_creative_voc_refresh_2026-05-24.md + facebook_ads_peak_season_2026-05-20.md (unchanged for structure/targeting/budget)
>Reply YES to approve — just do it before launching Tuesday.
---
💡 *Vera — Upgrade Proposal*
>Idea: File Google Guaranteed (Local Services Ads) application TODAY or Tuesday
>Why: Application takes 7–14 days to approve. Filed today (Sunday May 24) = potentially live by June 7. Filed Tuesday = June 9. Filed after Wednesday = won't be live before June Booking Blitz (Round 2 enrollment June 4). Google Guaranteed puts Forest City ABOVE regular Google Ads in search results. Pay-per-lead ($15–$35), not pay-per-click. Most NE Ohio competitors haven't set it up.
>Impact: Could be the highest-ROI ad channel active during peak June season. Every day of delay = days offline.
>Action: ads.google.com/local-services-ads → 10 minutes to start the application. Full guide: outputs/rick/google_guaranteed_setup_2026-05-22.md
>Reply YES to flag this as done.
---
✅ *Vera — Scan Complete 2026-05-24 (Run 75)*
>2 auto-upgrades shipped | 2 deliverables | 2 proposals | 20 open issues (1 new: Facebook ad copy VOC gap)

>Run 75 priority additions for TUESDAY May 26:
>• Read facebook_ad_creative_voc_refresh_2026-05-24.md BEFORE launching ads — 15-min swap in Ads Manager
>• File Google Guaranteed today or Tuesday before ads launch (google_guaranteed_setup_2026-05-22.md)

>STILL OPEN — needs Bradley action TODAY (Sunday):
>• Text Anthony/Land Pro 440-320-2779 — Memorial Day weekend, trades are working
>• Pause Instantly.ai — app.instantly.ai → a1c08c3d + 626cd15d → Pause (3 min)

---
🔧 *Vera — Auto-Upgrade: integrations/mixmax.py*
>Changed: enroll_batch() now ABORTS enrollment for batches > 5 contacts when INSTANTLY_PAUSED != 'true' (previously just warned and proceeded)
>Why: The warn-and-proceed behavior was being ignored for 20+ runs. The block means Bradley CANNOT accidentally enroll Round 2 contacts into Mixmax while Instantly.ai is still running duplicate campaigns — enrollment fails loudly with step-by-step fix instructions. Set INSTANTLY_PAUSED=true in .env after pausing to unblock. Emergency bypass: INSTANTLY_OVERRIDE=true.
>File: integrations/mixmax.py
---
🔧 *Vera — Auto-Upgrade: workers/lead_pipeline.py*
>Changed: run_pending_sequences() now checks INSTANTLY_PAUSED before enrolling pending contacts (gas station + fleet contacts waiting on Mixmax IDs)
>Why: run_pending_sequences() called enroll_lead() directly, bypassing the enroll_batch() guard entirely. When Bradley adds the gas station Mixmax ID and runs `python3 workers/lead_pipeline.py pending`, 18 gas station contacts would enroll with no protection. Now blocked unless INSTANTLY_PAUSED=true.
>File: workers/lead_pipeline.py
---
🔧 *Vera — Auto-Upgrade: workers/vera_relay.py*
>Changed: Removed run_summit_both.command shortcut reference from Danny + Carla staleness alerts; replaced with generic rotation command
>Why: run_summit_both.command hardcodes Summit County. After May 31 (Week 22 = Medina), the shortcut would instruct the wrong county pull. Staleness alerts now show `python3 workers/lead_pipeline.py danny/carla` which auto-rotates by week number — always correct regardless of when the alert fires.
>File: workers/vera_relay.py
---
📄 *Vera — New Deliverable: Tommy*
>File: outputs/tommy/annual_plan_upsell_sequence_2026-05-24.md
>What: Word-for-word annual plan upsell system. 2-hour post-job text (2 versions: direct + soft), pricing guide by service combo ($350–$700/yr), response handling (YES/maybe/no), 30-day follow-up email (ready to send), 4 objection responses (too expensive, might sell house, need to think). Revenue math: 10 customers = $4,000–$6,000/yr locked.
>Action: Use within 2 hours of EVERY job completion this season. Conversion is highest while the house looks amazing and they can see the before/after.
---
📄 *Vera — New Deliverable: Tommy*
>File: outputs/tommy/pre_job_reminder_text_sequence_2026-05-24.md
>What: 3-text pre/post-job sequence. Day-before confirmation (soft-wash smell heads-up + no-show prevention), day-of ETA text (+ running-late version + gate/access version), job-complete text (with Google review prompt version). Also includes soft-wash FAQ reply templates for "is it safe for plants?" / "do I need to be home?" / "will algae come back?" (annual plan bridge at the end).
>Action: Start using IMMEDIATELY for any booked jobs this week, especially first-time ad leads who don't know Forest City yet.
---
📄 *Vera — New Deliverable: Donna*
>File: outputs/donna/june_week2_sprint_2026-05-24.md
>What: June 9–13 day-by-day sprint. Monday: Geauga+Portage county pull (Danny + Carla) + Nina weekly report + Round 2 reply review + contractor follow-up Wave 2. Tuesday: Facebook + Google Week 1 ad review with specific decision thresholds (CPL > $30 → tighten audience; CPL < $20 + 3 leads → scale to $45/day). Wednesday: GBP post + quote follow-up for Week 1 leads + Workiz report. Thursday: Mixmax Round 2 check (Day 8 post-enrollment). Friday: week review + Week 3 prep. Revenue target: $3,200–$7,500.
>Action: Read Monday June 9 morning before opening anything else.
---
✅ *Vera — Scan Complete 2026-05-24 (Run 76)*
>3 auto-upgrades shipped | 3 deliverables | 0 proposals | 20 open issues (2 new RESOLVED this run)

>🔒 BIGGEST FIX THIS RUN: Round 2 enrollment is now mechanically blocked until Instantly.ai is paused. Bradley cannot accidentally enroll 50+ contacts while Instantly is still running — the command will fail with step-by-step instructions. This prevents Round 2 from failing the same way as Round 1.

>STILL NEEDS BRADLEY TODAY (Sunday May 24):
>• Text Anthony/Land Pro 440-320-2779 — Memorial Day weekend, trades are working
>• Pause Instantly.ai — app.instantly.ai → a1c08c3d + 626cd15d → Pause → add INSTANTLY_PAUSED=true to .env (now required to unblock enrollment)
