# Vera Cole — Open Issues Tracker
*Updated automatically each run. Only mark RESOLVED after verifying the fix works.*
*Run 57 | 2026-05-23 | Auto-fixes shipped: 5 | New deliverables: 2 | Proposals: 0*

---

## RESOLVED SUMMARY (58 total — details in git history)

Key resolved issues by category:
- **Pipeline routing:** PM-before-realtor check order, gas_station/fleet false positives removed, all 5 PM title variants added (multifamily, CAI, condo, association manager)
- **Run 55 new RESOLVED:** duplicate 'leasing manager' in PROPERTY_MANAGER_TITLES; Danny + Carla sentinel file reliability (write + read); pending-mode for gas station enrollment without Apollo pull; Carla staleness sentinel (read side)
- **Run 56 new RESOLVED:** irrigation/sprinkler routing gap (CONTRACTOR_TITLES); commercial/retail segment title gap (leasing director, center manager added to PROPERTY_MANAGER_TITLES + DANNY_TITLES); nina_report replied contacts missing Phone column; check_replies.py phone lookup missing; Danny county override CLI flag missing
- **Enrollment safety:** mass re-enrollment guard, PENDING sequence skip, contacts_cache commit gap
- **Script stability:** report_card.py PIL crash, jasmine_flyer PIL + requests guards, workiz_report float cast, nina_report dict response handling, vera_relay write guard
- **Dashboard/server:** path traversal fix, concurrent write guard, queue parse safety
- **Content gaps:** county rotation calendar, crontab setup, LinkedIn June posts, nina weekly hot leads section with phone numbers, vera_relay Danny staleness detector
- **Routing accuracy:** detect_lead_type order swapped (PM before realtor), condominium manager substring bug

---

## OPEN — Manual Contacts Sitting Untouched (New Lead stage) 🔴
- First seen: 2026-05-18
- Description: 33 contacts in New Lead stage. 0 last_contact dates. Tier 1 contractors need personal text.
- Tier 1: Anthony/Land Pro (440-320-2779), Dontez/GTP (440-396-0814), Chris/Twin Improvements (216-773-0757), Venus/Reliable Roofing (216-810-2497), Logan/Pagels (216-956-5263)
- Run 54: Touch 3 fired May 22. Weekend checklist written.
- Run 57 (2026-05-23 Sat): Day 2 of 72-hour reply window. Sunday May 24 action card written with Tier 1 texts as Priority 2 task. Fresh angle: Sunday texts + Monday May 26 blitz follow-up texts (`outputs/tommy/may26_monday_morning_followup_texts.md` NEW). Resolution window = by May 26.
- Resolution criteria: Bradley texts Tier 1 list. Confirmed when pipeline_data.json shows "Contacted" stage for these 5.

---

## OPEN — Mixmax API blocked in cloud execution environment
- First seen: 2026-05-18
- Workaround: All pipeline scripts return safe fallbacks on 403. nina_report shows explicit API warning. `check_replies.py` (new Run 52) is a fast local alternative to full nina_report.
- Run 54: check_replies.py now also posts Slack notification when hot leads exist (not just replies) — Bradley gets daily open-count update during the reply window even with 0 replies. Infrastructure constraint — not fixable from cloud.
- Resolution criteria: Bradley adds cloud IP to Mixmax API allowlist (Mixmax → Settings → API → IP Allowlist).

---

## OPEN — All external APIs blocked from cloud (Apollo, Workiz, Mixmax)
- First seen: 2026-05-18
- Workaround: scripts/crontab_setup.txt ready to paste into crontab -e. scripts/danny_launchd_plist.xml as Mac alternative. scripts/danny_cron_check.sh for diagnostics. check_replies.py added to crontab (8:45am weekdays).
- Run 54: Danny cron down since May 12 (10 days). Next auto-run would be June 1 (Monday after Memorial Day) since Week 21 = May 25 = Memorial Day holiday. Round 2 enrollment June 4 = 13 days away. May 26 manual run is critical path item. 
- Fresh angle: Added to `weekend_lead_gen_checklist_2026-05-22.md` as Monday May 26 Priority #5 with exact command. It's now on a checklist Bradley will actually open.
- Resolution criteria: crontab -l shows Danny cron entry AND logs/cron.log confirms pull by May 26.

---

## OPEN — Slack Webhook blocked in cloud execution environment
- First seen: 2026-05-18
- Workaround: Messages written to pending_slack_messages.md. GitHub Action fires on every Vera push and posts content to Slack. vera_relay.py on local cron provides 5-min delivery.
- Run 54: Relay working. vera_relay.py now has lock file protection (added this run) to prevent concurrent instances from colliding on git operations. Permanent constraint, not a fixable bug.

---

## OPEN — GitHub Actions PAT missing workflow scope
- First seen: 2026-05-20 (run 34)
- Description: vera-slack-relay.yaml and github_action_vera_slack_relay.yaml exist in outputs/vera/ but can't be pushed to .github/workflows/ — PAT needs 'workflow' scope.
- Run 55: Still blocked. No change this run. Local vera_relay.py with lock file is stable. PAT scope upgrade remains a 2-minute fix.
- Action: Settings → Developer settings → Personal access tokens → Edit ghp_lrUhBq7... → check 'workflow' → Save

---

## OPEN — Instantly.ai vs Mixmax Overlap (0% reply rate root cause) 🔴
- First seen: 2026-05-18
- Description: Two active Instantly.ai campaigns (a1c08c3d = PM Cuyahoga, 626cd15d = Contractor Referral) run against the same contacts as Mixmax sequences → duplicate emails → spam filtering → 0 replies.
- Run 55: nina_report.py daily run now shows explicit 0-reply/Instantly overlap warning.
- Run 57 (2026-05-23 Sat): Still unresolved. This is day 2 of 72-hour window. If 0 replies by May 25, Instantly.ai overlap is likely root cause. MUST pause before Round 2 enrollment June 4. Pause guide: `outputs/vera/instantly_pause_guide_2026-05-22.md`. This is a 3-minute fix — needs Bradley to open Instantly.ai dashboard.
- Resolution criteria: Both campaigns paused in Instantly.ai → confirmed by Bradley.

---

## OPEN — 0% reply rate across enrolled contacts
- First seen: 2026-05-18
- Description: ~45 contacts enrolled, 0 replies across all 3 email touches.
- Run 56: 72-hour window closes May 25. After May 25, the sequence is spent. If 0 replies by May 26: (1) send personal Gmail bridge emails to top 5 hot leads — `outputs/tommy/hot_lead_bridge_email_may26_2026-05-22.md` (NEW), (2) pause Instantly.ai before Round 2 enrollment, (3) A/B test subjects in Round 2 — `outputs/tommy/email_subject_line_ab_test_2026-05-22.md`.
- Resolution criteria: At least 1 confirmed reply before May 25 OR Round 2 rewrite + enrollment launched by June 4.

---

## OPEN — Hot leads not contacted on LinkedIn (Touch 3 day)
- First seen: 2026-05-18
- Description: ~13 contacts with 2+ opens haven't received personal LinkedIn connects.
- Run 55: Touch 3 window live. LinkedIn context strongest TONIGHT (May 22 evening). Evening debrief (outputs/vera/touch3_evening_debrief_2026-05-22.md) has the LinkedIn connect protocol as Priority 2 for tonight. Weekend connects still effective — LinkedIn DMs are seen Monday.
- Resolution criteria: Bradley connects on LinkedIn with top 5+ contacts TONIGHT or Saturday May 23.

---

## OPEN — HubSpot not connected (CRM blind)
- First seen: 2026-05-18
- Workaround: Nina weekly report has overdue/due-soon sections. pipeline_data.json is the manual CRM.
- Run 52: Not urgent. Post-peak season priority (July+).
- Resolution criteria: HUBSPOT_TOKEN added to .env.

---

## OPEN — No residential homeowner outreach channel active
- First seen: 2026-05-18
- Description: Facebook ads not running. June Residential Push brief written. All ad copy ready.
- Run 54: Weekend lead gen checklist written (outputs/donna/weekend_lead_gen_checklist_2026-05-22.md) — Facebook groups + past customer texts this weekend = zero ad spend leads before May 26. May 26 launch target still holds for paid ads.
- Resolution criteria: (1) Facebook group posts + past customer texts this weekend, (2) Facebook paid ads live by May 27.

---

## OPEN — Workiz API blocked in cloud + 0 power washing jobs showing
- First seen: 2026-05-18
- Workaround: API error sentinel prevents misleading $0 reports. JOB_TYPE_VARIANTS expanded to 22 variants (run 51). Diagnostic logging shows JobType values on local run.
- Run 54: Cleaned up dead constant `JOB_TYPE_FILTER` from workiz_report.py (was defined but never used). JOB_TYPE_VARIANTS is the correct filter and remains unchanged.
- Resolution criteria: Bradley runs `python3 workers/workiz_report.py daily` locally and sees jobs in the report.

---

## OPEN — Danny PM cron not running (11 days overdue) 🔴 CRITICAL — SUMMIT DEADLINE TONIGHT
- First seen: 2026-05-20 (run 28)
- Description: Last successful pull: May 12. Apollo blocked in cloud. Cron not set up on Bradley's Mac.
- Run 56: Added `--county Summit` override CLI flag. Updated danny.md with May 25 deadline.
- Run 57 (2026-05-23 Sat): **TODAY IS SATURDAY MAY 23. Summit County deadline = SUNDAY NIGHT MAY 25.** 11 days since last pull. Sunday action card includes Summit pull as Priority 6 (TONIGHT). Fresh angle: this is the last possible window before 6-week gap. Command is simple: 5 minutes.
- Command to force Summit (run TODAY or TOMORROW): `python3 workers/lead_pipeline.py danny Summit`
- Resolution criteria: logs/cron.log or activity.log shows Danny summit pull entry by May 26.

---

## OPEN — Google Business Profile not managed
- First seen: 2026-05-20 (run 30)
- Description: GBP posts drive local SEO ranking for "power washing [city]" searches. Free channel.
- Run 54: GBP photo upload added to weekend_lead_gen_checklist as Saturday May 23 Task 2. Protocol: outputs/vera/gbp_weekly_routine_2026-05-21.md. Ready content: outputs/vera/gbp_post_may21_2026.md.
- Resolution criteria: Bradley posts first GBP photo this weekend at business.google.com/dashboard.

---

## OPEN — No review request automation
- First seen: 2026-05-20 (run 30)
- Workaround: Manual template at outputs/tommy/review_request_sequence_2026-05-18.md.
- Run 52: Post-peak season priority (July+). Twilio credentials needed for automation.

---

## OPEN — Gas station contacts not enrolled in Mixmax (18 emails idle)
- First seen: 2026-05-20 (run 31)
- Description: 18 gas station district manager contacts pulled May 19. Sequence ID = PENDING.
- Run 54: Unchanged — sequence creation is a 5-minute Mixmax UI task. These are commercial multi-location accounts (district managers manage 5–15 locations). Post-Memorial Day blitz week is the right time to launch — commercial managers are back in the office June 2.
- Sequence copy: outputs/danny/sequence_gas_stations_2026-05-19.md. Setup guide: outputs/vera/mixmax_sequence_setup_guide_2026-05-20.md.

---

## OPEN — Google Ads and Facebook Ads not launched
- First seen: 2026-05-21 (run 36)
- Description: All copy ready (outputs/rick/). Not launched. Peak season revenue being missed daily.
- Run 54: Weekend free lead gen now bridges to May 26 launch. If Bradley does Facebook group posts this weekend (5 min, free), he generates SOME residential leads immediately while setting up paid ads Monday. May 26 is still the target for paid campaigns.
- Checklist: outputs/vera/may26_ads_launch_checklist_2026-05-22.md. Google Guaranteed: outputs/rick/google_guaranteed_setup_2026-05-22.md.
- Resolution criteria: At least one campaign live by May 27. Confirmed by Bradley in Slack.

---

## OPEN — Past customer reengagement not launched
- First seen: 2026-05-20 (run 29)
- Description: Tommy's text templates ready. Fastest path to residential revenue — zero ad spend.
- Run 54: Weekend checklist (outputs/donna/weekend_lead_gen_checklist_2026-05-22.md) includes 5 personal past customer texts this weekend — lower volume, higher conversion than mass blast. Full blast May 26 per the launch guide.
- Launch guide: outputs/donna/past_customer_reengagement_launch_2026-05-21.md. Revenue potential: $1,400–$4,000.
- Resolution criteria: Bradley sends texts May 26 (full blast) or this weekend (5-contact personal version).

---

## OPEN — Marcus running cloud-only (no live web search)
- First seen: 2026-05-21 (run 44)
- Description: Marcus's competitor profiling requires live web search. Blocked in cloud.
- Run 54: The HOA spring meeting email angles (outputs/tommy/hoa_spring_meeting_email_2026-05-22.md) use VOC that Marcus would normally source from reviews. Written from first principles — good enough for Round 2. Real-time competitor data still missing.
- Resolution criteria: Bradley runs Marcus locally: `claude` CLI → "Marcus, profile top 5 Cleveland power washing competitors."

---

## RESOLVED — PROPERTY_MANAGER_TITLES missing 3 titles (leasing manager, managing partner, principal)
- Resolved: 2026-05-22
- Fix: Added 'leasing manager', 'managing partner', 'principal' to PROPERTY_MANAGER_TITLES in integrations/mixmax.py — all 3 were in DANNY_TITLES but absent from routing detection; manual imports with these titles now route correctly to PM sequence without needing _lead_type set

## RESOLVED — check_replies.py silent on hot leads (no Slack notification without replies)
- Resolved: 2026-05-22
- Fix: Added Slack notification block when hot leads (2+ opens, 0 replies) are found; Bradley now gets a daily Slack summary during the post-Touch-3 reply window even if no one has replied yet

## RESOLVED — workiz_report.py dead JOB_TYPE_FILTER constant
- Resolved: 2026-05-22
- Fix: Removed unused constant JOB_TYPE_FILTER — JOB_TYPE_VARIANTS is the live filter; dead code removed

## RESOLVED — vera_relay.py concurrent instance race condition
- Resolved: 2026-05-22
- Fix: Added _acquire_lock()/_release_lock() with LOCK_FILE + 3-minute stale-lock timeout; concurrent 5-min cron instances now exit cleanly instead of colliding on git operations

---

## RUN METRICS — Run 57 | 2026-05-23
- Total RESOLVED: 72 (5 new: CONTRACTOR_TITLES duplicates removed, tree service/arborist added to routing + Carla search, PM title variants site manager/community director/building ops mgr/property administrator added, check_replies.py hot leads Slack shows phone)
- Total OPEN: 17 (0 new closed — all require Bradley action; 0 new opened)
- Auto-upgrades shipped: 5 (mixmax.py CONTRACTOR_TITLES cleanup+tree service; lead_pipeline.py tree service in Carla search; lead_pipeline.py + mixmax.py 4 new PM titles; check_replies.py hot leads phone in Slack; donna.md output format entries)
- Deliverables written: 2 (sunday_may24_action_card.md, may26_monday_morning_followup_texts.md)
- Proposals: 0
- Highest priority action (TONIGHT): (1) Run `python3 workers/lead_pipeline.py danny Summit` — SUMMIT DEADLINE IS TONIGHT (2) Pause Instantly.ai campaigns a1c08c3d + 626cd15d — 3 min (3) LinkedIn connects with 2+ open leads NOW — Friday evening seen Monday morning

## RUN METRICS — Run 56 | 2026-05-22
- Total RESOLVED: 67 (5 new this run: irrigation/sprinkler routing gap, commercial segment title gap, nina_report replied phone, check_replies phone, danny county override)
- Total OPEN: 17 (0 new closed — all require Bradley action)
- Auto-upgrades shipped: 7 (mixmax.py irrigation+sprinkler+leasing director+center manager; lead_pipeline.py commercial titles+org keywords+county override CLI; nina_report.py replied phone column; check_replies.py phone lookup; danny.md Summit County deadline)
- Deliverables written: 2 (june_week2_sprint_2026-05-22.md, hot_lead_bridge_email_may26_2026-05-22.md)
- Proposals: 1 (Google Guaranteed app — file this weekend, not Monday; takes 7-14 days, could be live before June Booking Blitz)
- Highest priority action: (1) RUN DANNY SUMMIT COUNTY PULL BEFORE SUNDAY NIGHT — `python3 workers/lead_pipeline.py danny Summit` (2) Pause Instantly.ai — a1c08c3d + 626cd15d (3) LinkedIn connects tonight (4) May 26: bridge emails to top 5 hot leads + ads launch

## RUN METRICS — Run 55 | 2026-05-22
- Total RESOLVED: 62 (3 new this run: duplicate leasing_manager removed, Danny+Carla sentinel file write/read, pending mode in lead_pipeline.py)
- Total OPEN: 17 (0 new closed, 0 new opened)
- Auto-upgrades shipped: 6 (mixmax.py duplicate leasing_manager, lead_pipeline.py sentinel+pending mode, vera_relay.py sentinel reads for Danny+Carla, nina_report.py Instantly.ai overlap warning, agents/danny.md pending mode docs)
- Deliverables written: 2 (door_hanger_neighbor_farm_2026-05-22.md, rei_investor_outreach_2026-05-22.md)
- Proposals: 2 (door hanger neighbor farm, REI investor sub-segment for Carla)
- Highest priority action: (1) Pause Instantly.ai TONIGHT — 3 min, (2) LinkedIn connects TONIGHT while Touch 3 context is live, (3) May 23 morning: phone calls using may23_morning_call_protocol, (4) May 26: Danny pull + ads launch

## RUN METRICS — Run 54 | 2026-05-22
- Total RESOLVED: 59 (4 new this run)
- Total OPEN: 17 (0 new closed, 0 new opened)
- Auto-upgrades shipped: 4 (mixmax.py PROPERTY_MANAGER_TITLES 3 titles, check_replies.py hot-lead Slack notification, workiz_report.py dead constant cleanup, vera_relay.py lock file)
- Deliverables written: 2 (hoa_spring_meeting_email_2026-05-22.md, weekend_lead_gen_checklist_2026-05-22.md)
- Highest priority action: (1) Pause Instantly.ai TONIGHT, (2) Weekend checklist: FB group posts + past customer texts + GBP photo, (3) Monday May 26: Danny pull + ads launch + contractor texts

## RUN METRICS — Run 53 | 2026-05-22
- Total RESOLVED: 55 (unchanged — all require Bradley action)
- Total OPEN: 17 (0 new closed, 0 new opened)
- Auto-upgrades shipped: 5 (check_replies.py dynamic sequence sync, mixmax.py property_management_director routing fix, nina_report.py Company column in hot leads tables, lead_pipeline.py window cleaning keyword, danny.md date update)
- Deliverables written: 1 (free_lead_harvest_protocol_2026-05-22.md — free residential lead gen while ads aren't live)
- Highest priority action: (1) Pause Instantly.ai TONIGHT — 3 min, (2) Post in 3 Facebook homeowner groups TODAY, (3) Run check_replies.py tomorrow 9am, (4) Danny manual pull `python3 workers/lead_pipeline.py both`

## RUN METRICS — Run 52 | 2026-05-22
- Total RESOLVED: 55 (unchanged — all require Bradley action)
- Total OPEN: 17 (0 new closed, 0 new opened)
- Auto-upgrades shipped: 4 (lead_pipeline DANNY_TITLES managing_partner+principal, vera_relay Carla staleness check, new check_replies.py worker, crontab check_replies entry)
- Deliverables written: 2 (reply_window_tracker_2026-05-22.md, this open_issues update)
- Highest priority action: (1) Pause Instantly.ai TONIGHT — 3 min, (2) Run check_replies.py tomorrow 9am, (3) Danny manual pull `python3 workers/lead_pipeline.py both`
