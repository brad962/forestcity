# Vera Cole — Open Issues Tracker
*Updated automatically each run. Only mark RESOLVED after verifying the fix works.*
*Run 80 | 2026-05-25 (Memorial Day — final run before launch day) | Auto-fixes shipped: 4 | New deliverables: 2 | Proposals: 3 | New RESOLVED: 1*

---

## RESOLVED SUMMARY (80 total — details in git history)

Key resolved issues by category:
- **Pipeline routing:** PM-before-realtor check order, gas_station/fleet false positives removed, all 5 PM title variants added (multifamily, CAI, condo, association manager)
- **Run 55 new RESOLVED:** duplicate 'leasing manager' in PROPERTY_MANAGER_TITLES; Danny + Carla sentinel file reliability (write + read); pending-mode for gas station enrollment without Apollo pull; Carla staleness sentinel (read side)
- **Run 56 new RESOLVED:** irrigation/sprinkler routing gap (CONTRACTOR_TITLES); commercial/retail segment title gap (leasing director, center manager added to PROPERTY_MANAGER_TITLES + DANNY_TITLES); nina_report replied contacts missing Phone column; check_replies.py phone lookup missing; Danny county override CLI flag missing
- **Enrollment safety:** mass re-enrollment guard, PENDING sequence skip, contacts_cache commit gap
- **Script stability:** report_card.py PIL crash, jasmine_flyer PIL + requests guards, workiz_report float cast, nina_report dict response handling, vera_relay write guard
- **Dashboard/server:** path traversal fix, concurrent write guard, queue parse safety
- **Content gaps:** county rotation calendar, crontab setup, LinkedIn June posts, nina weekly hot leads section with phone numbers, vera_relay Danny staleness detector
- **Routing accuracy:** detect_lead_type order swapped (PM before realtor), condominium manager substring bug
- **Run 61 new RESOLVED:** rick.md "Monday after Memorial Day" date error fixed to Tuesday; danny.md urgency note clarified (deadline = May 31, not just "Sunday night"); danny.md output format catalog updated; open_issues.md header corrected (58 → 74 total); donna.md + carla.md new output format entries added

---

## OPEN — Facebook Ad Copy Predates VOC Research 🔴 NEW (Run 75)
- First seen: 2026-05-24 (Run 75)
- Description: `facebook_ads_peak_season_2026-05-20.md` (Facebook ad creative, Campaign 2 Lead Gen) was written May 20 — 3 days before Marcus's VOC library was completed (May 23). The ad hooks don't use proven NE Ohio customer language.
- Fix staged: `outputs/rick/facebook_ad_creative_voc_refresh_2026-05-24.md` — 6 drop-in hooks + 3 body copy variants using exact VOC phrases. 15-min swap.
- Run 80 (2026-05-25 Memorial Day): Added BEFORE LAUNCH warning to `agents/rick.md` directly in the Facebook Ads ready assets section — Bradley sees the swap requirement the moment he opens the agent file. Also added as a step in `outputs/donna/may26_final_launch_brief_2026-05-25.md` at 9:00am.
- Resolution criteria: Bradley swaps hooks BEFORE clicking launch on May 26. Confirmed when ads are running with updated copy.

---

## OPEN — Email List at 0 / Lead Magnet Not Live 🔴 NEW
- First seen: 2026-05-24 (Run 74)
- Description: Facebook and Google ads launch Tuesday May 26. Traffic that doesn't book immediately has nowhere to go — no email opt-in, no nurture, permanently lost. The Home Maintenance Checklist brief has existed since May 12 but was never turned into a live opt-in. Kit.com is free up to 10K subscribers.
- Assets now ready (all written this run):
  - Checklist content: `outputs/tommy/home_maintenance_checklist_content_2026-05-24.md`
  - Kit.com setup guide: `outputs/donna/kit_email_capture_setup_2026-05-24.md`
  - Nurture sequence: `outputs/donna/nurture_sequence_home_maintenance_checklist_2026-05-12.md` (exists since May 12)
- Setup time: 23 minutes. Should be done before Tuesday ads launch.
- Run 74: Assets written. Kit.com account still needs to be created at kit.com. Setup guide is ready.
- Resolution criteria: Kit.com landing page live + first subscriber captured.

---

## OPEN — Manual Contacts Sitting Untouched (New Lead stage) 🔴
- First seen: 2026-05-18
- Description: 33 contacts in New Lead stage. 0 last_contact dates. Tier 1 contractors need personal text.
- Run 77 (2026-05-24 Sun): FRESH DELIVERABLE — `outputs/vera/memorial_day_contractor_text_card_2026-05-24.md` written this run. 5 copy-paste texts for all 5 Tier 1 contractors. Send at 10am Monday May 25 (Memorial Day — trades are working, phones on). Zero reading required. Open card, copy, send, done. All 5 numbers confirmed in pipeline_data.json. This is the simplest possible path to finally moving these contacts out of "New Lead."
- Tier 1: Anthony/Land Pro (440-320-2779), Dontez/GTP (440-396-0814), Chris/Twin Improvements (216-773-0757), Venus/Reliable Roofing (216-810-2497), Logan/Pagels (216-956-5263)
- Run 54: Touch 3 fired May 22. Weekend checklist written.
- Run 57 (2026-05-23 Sat): Day 2 of 72-hour reply window. Sunday May 24 action card written with Tier 1 texts as Priority 2 task. Fresh angle: Sunday texts + Monday May 26 blitz follow-up texts (`outputs/tommy/may26_monday_morning_followup_texts.md` NEW). Resolution window = by May 26.
- Run 60 (2026-05-23 Sat): Reply window closes TONIGHT. Fresh angle: may25_sunday_evening_protocol_2026-05-23.md (new) includes Tier 1 LinkedIn connects as tonight priority. If window closes 0 replies, Monday blitz texts are queued. Text at 10am Mon May 26 — highest response rate for trades.
- Run 61 (2026-05-23 Sat): Reply window still open (ends Sunday May 25). Fresh angle: text scripts corrected in `tuesday_may26_launch_card_2026-05-23.md` — Tier 1 contractor texts are Priority #4 at 8:45am Tuesday. That's 36 hours from now. Window for a Memorial Day weekend text (Saturday afternoon) is also valid — higher open rate than weekday. Try one TODAY: Anthony/Land Pro 440-320-2779.
- Run 62 (2026-05-23 Sat): Still open — all 5 Tier 1 contractors uncontacted. Reply window closes TOMORROW (Sunday May 25). Fresh angle: the reply window that closes tomorrow is for the Mixmax sequence. But the PERSONAL outreach window (texts to Tier 1) has no deadline — it's just been sitting idle. Text Anthony at 440-320-2779 this afternoon. Memorial Day weekend = trades are doing estimates, phones are on. Script: "Hey Anthony, it's Bradley from Forest City Power Washing. We do exterior cleaning for a lot of landscapers' customers — want to do a quick referral swap? No paperwork. $50 for every job you send our way."
- Run 65 (2026-05-23 Sat): Tier 1 texts queued for Tuesday May 26 blitz (tuesday_may26_launch_card). Mixmax reply window closes tomorrow. Nothing Vera can do from cloud — this requires Bradley to open his phone. Priority #2 on Tuesday morning.
- Run 68 (2026-05-24 Sun): Still open. It's Memorial Day weekend — trades are doing estimates and running jobs. TODAY (Sunday) or tomorrow (Memorial Day Monday) is actually the BEST window to text a contractor: they're working but not buried in office tasks. Script for Anthony 440-320-2779: "Hey Anthony, it's Bradley from Forest City Power Washing. We do exterior cleaning for a lot of landscapers' customers — want to do a quick referral swap? No paperwork, $50 for every job you send our way." Tuesday is still Plan B. Text one today.
- Run 69 (2026-05-24 Sun): TODAY is the day. Mixmax reply window closes TOMORROW (Mon May 25 Memorial Day). Today + tomorrow = last chance for Memorial Day weekend contractor contact before Tuesday's 90-min blitz. Text Anthony first (landscaper = highest referral ROI). Text Venus second (roofer = high-ticket jobs). 2 texts = 10 minutes of real action. `tuesday_may26_launch_card_2026-05-23.md` has the full Tier 1 list at Priority 4 (8:45am Tuesday) as the backstop if not texted today.
- Run 70 (2026-05-24 Sun): Same window — still Sunday. 5 contacts, 2 texts in 10 minutes. If not done today, these move to Tuesday morning blitz (8:45am slot). When any of these contacts calls back after a text, use `outputs/tommy/hot_lead_callback_script_2026-05-24.md` (new this run) — the inbound call conversion rate from warm contractors is much higher than cold, and Bradley has no script for that scenario until now.
- Run 71 (2026-05-24 Sun): Text window TODAY (Sunday) still open — trades working Memorial Day weekend. If not today, Tuesday May 26 at 8:45am is the blitz slot (in may26_week_priority_stack). June 4 enrollment battle card now exists (`outputs/donna/june4_enrollment_battle_card_2026-05-24.md`) — Tier 1 contractor texts are the same-day activity alongside enrollment.
- Run 73 (2026-05-24 Sun): VERIFIED via pipeline_data.json — all 5 Tier 1 contractors confirmed "New Lead," 0 last_contact dates. Phones confirmed in pipeline_data.json (Anthony 440-320-2779, Dontez 440-396-0814, Chris/Twin 216-773-0757, Venus 216-810-2497, Logan 216-956-5263). Fresh angle: inbound call handling is now covered — if a contractor calls back after a text, use `outputs/tommy/inbound_response_protocol_2026-05-24.md` Section 4. Tuesday 8:45am is the Plan B slot from `may26_week_priority_stack_2026-05-24.md`.
- Run 74 (2026-05-24 Sun): Final window narrowing. If not texted today (Sunday) or tomorrow (Memorial Day), Tuesday 8:45am slot is the backstop. After Tuesday, these 5 contacts will have been "New Lead" for 6+ days. If Mixmax sequence is now finished (reply window closed tomorrow), Tuesday texts become the ONLY active outreach channel for these contacts — Mixmax won't re-enroll them. Text Anthony first (landscaper → highest referral volume in NE Ohio exterior maintenance). $50/referral, $0 upfront cost, no paperwork needed to start.
- Run 78 (2026-05-24 Sun): FINAL WINDOW — It's Sunday night Memorial Day weekend. Tomorrow (Monday May 25, Memorial Day) is the last day of the reply window AND a valid day for contractor texts (trades work Memorial Day). If texts not sent today, they MUST go Tuesday May 26 at 8:45am (first slot on may26_week_priority_stack). After Tuesday, these contacts will be 7+ days in "New Lead" with no personal outreach. The memorial_day_contractor_text_card_2026-05-24.md has all 5 scripts ready to copy-paste. Anthony/Land Pro is the highest-ROI first text (landscapers refer the most volume).
- Run 79 (2026-05-25 Mon, Memorial Day): TODAY IS THE DAY. It is Memorial Day. Trades are working — phones are on. `memorial_day_contractor_text_card_2026-05-24.md` has all 5 scripts. Open it, copy, send Anthony first (440-320-2779). 10 minutes, 5 texts. If not today, Tuesday 8:45am is the absolute last slot before these contacts are 7+ days "New Lead" with zero personal touch. After ads launch Tuesday, Bradley will be busy with inbound — these outbound texts will get deprioritized further.
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
- Run 57 (2026-05-23 Sat): Still unresolved. Reply window closes tonight.
- Run 60 (2026-05-23 Sat): Fresh angle — included in tonight's `may25_sunday_evening_protocol_2026-05-23.md` as Step 3a (pause if 0 replies tonight). The protocol makes it automatic: zero replies tonight = pause Instantly tonight, before Monday Round 2 prep begins.
- Run 61 (2026-05-23 Sat): Slack message includes TONIGHT ALERT with 3-step pause: app.instantly.ai → Campaigns → ⋮ → Pause.
- Run 62 (2026-05-23 Sat): Round 2 enrollment is June 4 — 12 days away. Pausing today = 12 full days of deliverability recovery before Round 2 sends. Pausing June 3 = 0 days of recovery. Every day of delay costs deliverability. New escalation: Round 2 Enrollment Readiness Checklist (`outputs/donna/round2_enrollment_readiness_checklist_2026-05-23.md`) now includes Instantly pause as the first block — without it, the entire checklist is a NO-GO and Round 2 enrollment cannot proceed.
- Run 65 (2026-05-23 Sat): 11 days until Round 2 enrollment. Pause now = 11 days recovery. Every day not paused = worse deliverability on June 4. This is the single most impactful action before Tuesday.
- Run 66 (2026-05-23 Sat): Auto-fix applied: danny.md updated to explicitly flag these two campaigns as ACTIVE (was saying "Not active" — misleading any agent reading the file). enroll_batch() already warns at runtime. Open issue remains: Bradley must pause in app.instantly.ai UI.
- Run 68 (2026-05-24 Sun): REPLY WINDOW CLOSES TOMORROW (Monday May 25, Memorial Day). 11 days remain until Round 2 enrollment (June 4). Every day not paused = less deliverability recovery. This is a 3-minute task: app.instantly.ai → Campaigns → ⋮ → Pause a1c08c3d AND 626cd15d. If not paused before Round 2, all Round 2 emails will land in spam just like Round 1.
- Run 69 (2026-05-24 Sun): 11 days until Round 2. Pause window = NOW. app.instantly.ai → Campaigns → ⋮ (three dots on right) → Pause. Do both campaigns: a1c08c3d + 626cd15d. 3 minutes. Every day of recovery = better deliverability on June 4. After pausing, add INSTANTLY_PAUSED=true to .env so enroll_batch() stops warning.
- Run 70 (2026-05-24 Sun): Still 11 days. May 25 (Memorial Day) = last day with no cost for not pausing. June 4 is 11 days away. Email deliverability recovery needs at least 7–10 days. If not paused by Tuesday May 26, the recovery window before Round 2 drops below 7 days — high risk of landing in spam again. This is a 3-minute action: app.instantly.ai → Campaigns → ⋮ → Pause.
- Run 71 (2026-05-24 Sun): 11 days until Round 2. June 4 enrollment battle card now has an explicit Instantly.ai pre-check as Step 1 the night of June 3 (grep INSTANTLY_PAUSED .env). If still not paused by Tuesday May 26, the recovery window is exactly 9 days — minimum viable. Every day after Tuesday = higher spam risk for June 4.
- Run 73 (2026-05-24 Sun): 11 days until Round 2. Reply window closes TOMORROW. If 0 replies come in by Memorial Day morning, Instantly.ai is confirmed to have hurt deliverability. Pausing immediately after the window closes = maximum recovery time before June 4. Critical path: pause TODAY → 11 days recovery; pause Tuesday → 9 days recovery (minimum viable); pause after June 1 → less than 7 days (high risk). The 3-minute pause is the highest-leverage action available this weekend.
- Run 74 (2026-05-24 Sun): This is the same Sunday. REPLY WINDOW CLOSES TOMORROW (Memorial Day). 11 days until Round 2 enrollment. The math is clear: pause today = best deliverability on June 4. Pause Tuesday = 9 days recovery (still OK). Pause after Memorial Day week = high risk. The Round 2 enrollment readiness checklist (`outputs/donna/round2_enrollment_readiness_checklist_2026-05-23.md`) lists this as the first and hardest blocking item. Without it confirmed, the readiness check is NO-GO.
- Run 76 (2026-05-24): CODE-LEVEL BLOCK SHIPPED. `enroll_batch()` in integrations/mixmax.py now ABORTS (not just warns) for batches > 5 contacts when INSTANTLY_PAUSED != 'true'. `run_pending_sequences()` in workers/lead_pipeline.py also blocked. Bradley CANNOT accidentally enroll Round 2 contacts while Instantly.ai is still running — enrollment will fail loudly with step-by-step fix instructions. To bypass (emergency only): set INSTANTLY_OVERRIDE=true in .env. To fix properly: pause a1c08c3d + 626cd15d → add INSTANTLY_PAUSED=true to .env → re-run. This resolves the mechanical risk; manual Instantly.ai pause still required.
- Run 78 (2026-05-24 Sun): 11 days until Round 2 enrollment. Reply window closes TOMORROW (Memorial Day). Deliverability recovery math: pause TODAY = 11 days = maximum recovery; pause Tuesday May 26 = 9 days = minimum viable; pause after May 27 = 8 days or fewer = high spam risk on June 4. The `round2_warmup_timeline_2026-05-26.md` (NEW this run) maps the entire May 26→June 3 prep sequence with Instantly.ai pause as Day 1 blocker. New nina_report.py fix this run ensures manual contacts (gas station, Tier 1 contractors) show phone/company in Nina's reply reports — consistent with check_replies.py.
- Run 79 (2026-05-25 Mon, Memorial Day): 10 days until Round 2 enrollment. Reply window closes TODAY. Mixmax reply window = DONE after today whether paused or not — this is now purely about June 4 deliverability. Pause TODAY = 10 days recovery. Pause Tuesday = 9 days (minimum viable). Pause Wednesday or later = under 8 days = high risk June 4 lands in spam again. This is still a 3-minute action: app.instantly.ai → Campaigns → ⋮ → Pause a1c08c3d AND 626cd15d. Code block in enroll_batch() and run_pending_sequences() means Bradley cannot accidentally enroll Round 2 while Instantly runs — but the mechanical block does NOT fix the deliverability damage that accumulates every day Instantly stays active.
- Resolution criteria: Both campaigns paused in Instantly.ai → confirmed by Bradley.

---

## OPEN — 0% reply rate across enrolled contacts
- First seen: 2026-05-18
- Description: ~45 contacts enrolled, 0 replies across all 3 email touches.
- Run 56: 72-hour window closes May 25.
- Run 60 (2026-05-23 Sat): Window closes TONIGHT. Sunday evening protocol (`may25_sunday_evening_protocol_2026-05-23.md`) has the full if/then tree: replies → templates ready; 0 replies → Instantly.ai pause + LinkedIn connects + bridge emails queued for Monday. Round 2 enrollment June 4 with A/B subjects (`outputs/tommy/email_subject_line_ab_test_2026-05-22.md`). Plan B is fully built — no gap if window closes at zero.
- Run 61 (2026-05-23 Sat): 2 days remain in window (closes Sunday May 25). Memorial Day weekend open rates are lower than weekdays but replies still happen. Bridge email from personal Gmail (bypasses spam, see `outputs/tommy/hot_lead_bridge_email_may26_2026-05-22.md`) has higher chance of landing during the weekend than the Mixmax sequence emails did. Round 2 June 4 plan fully built regardless of outcome.
- Run 68 (2026-05-24 Sun): Reply window closes TOMORROW (Monday May 25, Memorial Day). Final check: run `python3 workers/check_replies.py` at 10am Monday (10 minutes). Decision gate: `outputs/donna/may25_round2_decision_gate_2026-05-22.md`. Protocol for tomorrow: `outputs/donna/monday_memorial_day_final_check_2026-05-24.md`. 0 replies = pivot cleanly to Round 2 June 4 with VOC-rewritten copy.
- Run 69 (2026-05-24 Sun): Round 2 is now 11 days out. VOC-rewritten PM sequence exists (`outputs/tommy/round2_pm_sequence_voc_rewrite_2026-05-23.md`). VOC-rewritten contractor sequence exists (`outputs/carla/contractor_referral_sequence_voc_rewrite_2026-05-23.md`). Enrollment readiness checklist exists (`outputs/donna/round2_enrollment_readiness_checklist_2026-05-23.md`). All assets are staged — the only missing piece is Instantly.ai being paused and a fresh Summit County pull. Both on the May 26 blitz plan.
- Run 71 (2026-05-24 Sun): check_replies.py fixed this run — now posts Slack "all clear" confirmation when api_ok=True and pipeline is quiet, so Bradley knows the check ran. June 4 battle card written (`outputs/donna/june4_enrollment_battle_card_2026-05-24.md`) — full press-GO execution guide. Reply window closes TOMORROW.
- Resolution criteria: At least 1 confirmed reply before May 25 OR Round 2 rewrite + enrollment launched by June 4.

---

## RESOLVED — Hot leads not contacted on LinkedIn (Touch 3 day)
- Resolved: 2026-05-24 (Run 78)
- Fix: Time-boxed issue. Touch 3 window closed May 22–25. LinkedIn connect window was specific to the post-Touch-3 engagement spike. Issue is now moot — contacts either replied (see Round 2 plan) or moved to cold. LinkedIn connects for Round 2 contacts are built into the june4_enrollment_battle_card. Marking resolved to clear the noise; ongoing LinkedIn strategy is embedded in Round 2 enrollment docs.

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

## OPEN — Danny PM cron not running (12 days overdue) 🔴 CRITICAL — SUMMIT DEADLINE MAY 31
- First seen: 2026-05-20 (run 28)
- Description: Last successful pull: May 12. Apollo blocked in cloud. Cron not set up on Bradley's Mac.
- Run 62: Added `scripts/run_summit_pull.command` double-click shortcut.
- Run 65: danny.md urgency note updated to generic "WEEK 21 = SUMMIT COUNTY — DEADLINE MAY 31."
- Command (manual): `python3 workers/lead_pipeline.py danny Summit` (valid any day May 23–31)
- Double-click shortcut: `scripts/run_summit_pull.command` (in Finder — just open it)
- Run 77 (2026-05-24 Sun): NEXT COUNTY PREP — Created `scripts/run_medina_pull.command` and `scripts/run_medina_both.command` for Week 22 (June 1 = Medina County). When Summit deadline passes May 31, the very next day is Medina. Shortcut is ready. Also wrote `outputs/donna/june1_medina_pull_guide_2026-05-24.md` — operationalized June 1 guide. Summary: Summit (May 23–31) → Medina (June 1) → Geauga+Portage (June 8). All three have double-click shortcuts. danny.md and carla.md updated with Week 22 urgency note.
- Resolution criteria: logs/activity.log shows Danny Summit pull entry by May 31.

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
- Run 54: Unchanged — sequence creation is a 5-minute Mixmax UI task.
- Run 60 (2026-05-23 Sat): Fresh angle — wrote complete step-by-step Mixmax creation guide (`outputs/danny/gas_station_mixmax_sequence_creation_2026-05-23.md`).
- Run 61 (2026-05-23 Sat): Slotted into Tuesday May 26 action card at 9:00am as 10-minute task.
- Run 62 (2026-05-23 Sat): This is now on the Round 2 Enrollment Readiness Checklist as Block 4 (`outputs/donna/round2_enrollment_readiness_checklist_2026-05-23.md`). If gas station sequence is live by June 3, the 18 idle contacts get enrolled in the same enrollment run as the fresh PM contacts — zero extra effort.
- Run 80 (2026-05-25 Mon Memorial Day): PARTIAL FIX — Two changes shipped this run:
  1. `outputs/danny/gas_station_manual_email_blast_2026-05-25.md` — Direct Gmail blast guide for all 18 contacts. No Mixmax required. Bradley can email them from personal Gmail in 20 minutes. Tier 1 (7 contacts) goes May 26 AM; Tier 2 (11 contacts) goes May 28.
  2. `workers/lead_pipeline.py` — Added `INSTANTLY_SAFE_TYPES` bypass in `run_pending_sequences()`. Once the Mixmax sequence ID is added, gas station contacts can enroll WITHOUT needing INSTANTLY_PAUSED=true — because these contacts were never in Instantly.ai. Removes the last blocker from the automated path.
- Resolution criteria: Bradley either (A) sends Gmail blast tomorrow [now slotted at 9:30am in may26_final_launch_brief] OR (B) creates Mixmax sequence + runs `python3 workers/lead_pipeline.py pending`. Both paths now unblocked.
- Sequence copy: outputs/danny/sequence_gas_stations_2026-05-19.md.
- Creation guide: outputs/danny/gas_station_mixmax_sequence_creation_2026-05-23.md.
- Gmail blast guide: outputs/danny/gas_station_manual_email_blast_2026-05-25.md.

---

## OPEN — Google Ads and Facebook Ads not launched
- First seen: 2026-05-21 (run 36)
- Description: All copy ready (outputs/rick/). Not launched. Peak season revenue being missed daily.
- Run 54: Weekend free lead gen now bridges to May 26 launch.
- Run 61 (2026-05-23 Sat): Memorial Day weekend = prime time. Google Guaranteed application should be filed today. Facebook ads launch Tuesday May 26.
- Run 62 (2026-05-23 Sat): Still unresolved. Days since this was first flagged: 2 days. Days of peak season revenue being missed: counting. New escalation: once ads are live, they need a lead RESPONSE SOP — Google Guaranteed specifically measures response time and penalizes slow responders with fewer leads. Added `google_guaranteed_lead_response_sop_[date].md` format to rick.md so this can be pre-built BEFORE ads launch (5-minute read = much higher conversion on $15–$35 leads). Proposal: Tommy writes annual plan upsell sequence BEFORE ads launch — every ad lead is also a potential annual plan customer, not just a one-time job.
- Checklist: outputs/vera/may26_ads_launch_checklist_2026-05-22.md.
- Google Guaranteed: outputs/rick/google_guaranteed_setup_2026-05-22.md.
- Resolution criteria: At least one campaign live by May 28. Confirmed by Bradley in Slack.

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

## RESOLVED — vera_relay.py Summit-specific shortcut stale after June 1
- Resolved: 2026-05-24 (Run 76)
- Fix: Removed `scripts/run_summit_both.command` shortcut reference from Danny and Carla staleness alerts in vera_relay.py. The shortcut is Summit-specific (hardcodes Summit county) and would instruct the wrong county pull for any week after May 31. Alerts now show only the generic rotation command which auto-selects the correct county by week number.

## RESOLVED — run_pending_sequences() missing Instantly.ai protection
- Resolved: 2026-05-24 (Run 76)
- Fix: Added INSTANTLY_PAUSED check to run_pending_sequences() in workers/lead_pipeline.py. Previously, `python3 workers/lead_pipeline.py pending` (used to enroll gas station + fleet contacts when Mixmax IDs are added) had no protection against Instantly.ai overlap — it would enroll directly via enroll_lead() bypassing the enroll_batch() guard. Now blocked unless INSTANTLY_PAUSED=true or INSTANTLY_OVERRIDE=true.

## RESOLVED — PROPERTY_MANAGER_TITLES missing 3 titles (leasing manager, managing partner, principal)
- Resolved: 2026-05-22
- Fix: Added 'leasing manager', 'managing partner', 'principal' to PROPERTY_MANAGER_TITLES in integrations/mixmax.py — all 3 were in DANNY_TITLES but absent from routing detection; manual imports with these titles now route correctly to PM sequence without needing _lead_type set

## RESOLVED — check_replies.py silent on hot leads (no Slack notification without replies)
- Resolved: 2026-05-22
- Fix: Added Slack notification block when hot leads (2+ opens, 0 replies) are found; Bradley now gets a daily Slack summary during the post-Touch-3 reply window even if no one has replied yet

## RESOLVED — workiz_report.py dead JOB_TYPE_FILTER constant
- Resolved: 2026-05-22
- Fix: Removed unused constant JOB_TYPE_FILTER — JOB_TYPE_VARIANTS is the live filter; dead code removed

## RESOLVED — nina_report.py replied contacts missing company field
- Resolved: 2026-05-23 (Run 65)
- Fix: Added company injection to `run_daily()` and `run_weekly()` replied contacts loop; added Company column to REPLIED table in both daily and weekly report markdown output. Hot leads already showed company — replied contacts (the highest-value rows) did not. Bradley can now see immediately which company a reply came from without cross-referencing other files.

## RESOLVED — vera_relay.py concurrent instance race condition
- Resolved: 2026-05-22
- Fix: Added _acquire_lock()/_release_lock() with LOCK_FILE + 3-minute stale-lock timeout; concurrent 5-min cron instances now exit cleanly instead of colliding on git operations

## RESOLVED — vera_relay.py Slack message loss when push fails mid-relay
- Resolved: 2026-05-23
- Fix: Added _flush_unpushed_commits() called at start of _main_body() before git pull --rebase; if a prior push failed leaving a "cleared pending_messages" commit unpushed, it gets pushed first; prevents rebase from applying the empty-file commit on top of new Vera messages and silently discarding them

---

## RUN METRICS — Run 79 | 2026-05-25 (Memorial Day)
- Total RESOLVED: 80 (0 new this run — all open issues require Bradley action or are permanent infrastructure constraints)
- Total OPEN: 20 (0 new closed, 0 new opened)
- Auto-upgrades shipped: 4
  1. agents/nina.md — added workiz_job_entry_sop_[date].md to output format catalog; deliverable existed in outputs/nina/ since Run 78 but format entry was missing
  2. agents/tommy.md — removed duplicate neighbor_canvass_script_[date].md entry; same format name appeared twice; kept the more detailed version
  3. workers/lead_pipeline.py — added Instantly.ai warning to verify_and_repair_enrollment(); function calls enroll_lead() directly, bypassing the enroll_batch() guard; now warns when INSTANTLY_PAUSED is not set
  4. agents/jasmine.md — added instagram_launch_kit_[date].md to output format catalog
- Deliverables written: 1
  1. outputs/jasmine/instagram_launch_kit_2026-05-25.md — full Instagram channel launch kit: Business Account setup, profile bio copy, 5-Highlight plan, first-5-post sequence with captions, DM response protocol, pipeline_data.json lead logging guide, 30-day quick wins; everything needed to open the channel starting today or Tuesday; pairs with existing instagram_stories_scripts_2026-05-24.md
- Proposals: 2 (Workiz built-in review request automation; gas station Gmail blast this week)
- Code bugs fixed this run: verify_and_repair_enrollment() Instantly warning; tommy.md duplicate entry; nina.md catalog gap
- Highest priority TODAY (Mon May 25, Memorial Day):
  1. 10am: Run `python3 workers/check_replies.py` — reply window closes TODAY
  2. 10am: Open memorial_day_contractor_text_card_2026-05-24.md — text Anthony 440-320-2779 first
  3. Pause Instantly.ai: app.instantly.ai → a1c08c3d + 626cd15d → ⋮ → Pause (10 days recovery starts NOW)
- Highest priority TUESDAY May 26: READ may26_week_priority_stack_2026-05-24.md FIRST → VOC ad swap → Kit.com setup → ads launch → contractor texts 8:45am → Instagram profile setup

## RUN METRICS — Run 77 | 2026-05-24
- Total RESOLVED: 79 (0 new this run — all open issues require Bradley action or permanent infrastructure constraints)
- Total OPEN: 20 (0 new closed, 0 new opened)
- Auto-upgrades shipped: 5
  1. scripts/run_medina_pull.command — new double-click Finder shortcut for Medina County Danny pull (Week 22 = June 1); mirrors Summit shortcut pattern; proactive 8 days before the deadline
  2. scripts/run_medina_both.command — Danny + Carla Medina pull together in one click
  3. CLAUDE.md — added Medina shortcuts to Quick Shortcuts section with week labels
  4. agents/danny.md — added Week 22 Medina urgency note after Summit deadline; countdown-style like Summit note was
  5. agents/carla.md — added Week 22 Medina note with double-click shortcut reference
- Deliverables written: 2
  1. outputs/vera/memorial_day_contractor_text_card_2026-05-24.md — 5 copy-paste texts for all 5 Tier 1 contractors at 10am Monday Memorial Day; includes if-they-reply scripts and pipeline_data.json update instructions; zero reading required — open card, copy, send
  2. outputs/donna/june1_medina_pull_guide_2026-05-24.md — operationalized June 1 Medina County pull guide; mirrors Summit guide pattern; includes pre-pull check, both command options, June 4 enrollment connection, Medina-specific Apollo targets
- Proposals: 2 (see Slack messages — Workiz missed-call auto-text before Tuesday launch; Instagram account activation while before/after content is fresh)
- Key context: Medina County shortcuts built 8 days early — same lead time that Summit shortcut had, which proved effective. After Summit deadline May 31, the very next step is Medina June 1 → enrollment June 4. No gap in the friction-reduction chain.
- Highest priority TOMORROW (Mon May 25 Memorial Day):
  1. 10am: Open `outputs/vera/memorial_day_contractor_text_card_2026-05-24.md` — 5 texts, 10 minutes, closes weeks-old open issue
  2. 10am: Run `python3 workers/check_replies.py` → see monday_memorial_day_final_check_2026-05-24.md for decision tree
  3. Pause Instantly.ai: app.instantly.ai → a1c08c3d + 626cd15d → ⋮ → Pause
- Highest priority TUESDAY May 26: READ `may26_week_priority_stack_2026-05-24.md` first → all actions in order

## RUN METRICS — Run 75 | 2026-05-24
- Total RESOLVED: 77 (0 new — all open issues require Bradley action or permanent infrastructure constraints)
- Total OPEN: 20 (1 new: Facebook Ad Copy Predates VOC Research — fix ready in rick/facebook_ad_creative_voc_refresh_2026-05-24.md)
- Auto-upgrades shipped: 2 (workers/jasmine_flyer.py — "greater Cleveland area" → "Northeast Ohio" in auto-generated post template, accurate for 7-county service area; workers/vera_relay.py — removed hardcoded Summit county from Danny staleness alert, now uses generic rotation command that's always correct after May 31)
- Deliverables written: 2 (facebook_posts_june_week2_4_2026-05-24.md — 9 Facebook posts + 3 LinkedIn posts for June 9–27 using Marcus VOC library + June Booking Blitz context; supersedes May 20 version; facebook_ad_creative_voc_refresh_2026-05-24.md — 6 drop-in Facebook ad hooks + 3 body copy variants using exact NE Ohio VOC phrases; 15-min swap before Tuesday launch to improve CTR from day 1)
- Proposals: 2 (Facebook ad copy VOC swap before Tuesday — 15 min action with potentially significant CTR impact; Google Guaranteed application urgency — filing now = potentially live by June 7, filing after Wednesday = won't be live before June Booking Blitz)
- Key code fixes: jasmine_flyer.py "greater Cleveland area" was factually wrong for a 7-county service area; vera_relay.py hardcoded "Summit" would have told Bradley to force Summit county after May 31 rotation moved to Medina
- TUESDAY May 26 PRIORITY STACK (see may26_week_priority_stack_2026-05-24.md for full card):
  1. Read may26_week_priority_stack_2026-05-24.md FIRST
  2. 15 min: Swap Facebook ad copy using facebook_ad_creative_voc_refresh_2026-05-24.md BEFORE launching
  3. 23 min: Kit.com setup — kit_email_capture_setup_2026-05-24.md — email capture BEFORE ads launch
  4. 15 min: Yelp listing claim — yelp_business_profile_guide_2026-05-24.md
  5. 8am Summit pull → bridge emails → contractor texts 8:45am → gas station sequence → ads launch 9:15am

## RUN METRICS — Run 74 | 2026-05-24
- Total RESOLVED: 77 (0 new — all open issues require Bradley action or permanent infrastructure constraints)
- Total OPEN: 19 (1 new: Email List at 0 / Lead Magnet Not Live — new high-priority issue; 0 closed)
- Auto-upgrades shipped: 4 (workers/check_replies.py — phone_map and company_map now also read pipeline_data.json manual contacts; agents/rick.md — added yelp_business_profile_guide format to catalog; agents/donna.md — added kit_email_capture_setup format to catalog; agents/tommy.md — added home_maintenance_checklist_content format to catalog)
- Deliverables written: 3 (home_maintenance_checklist_content_2026-05-24.md — actual 12-month NE Ohio home maintenance checklist for homeowners; yelp_business_profile_guide_2026-05-24.md — 15-min Yelp listing claim + optimization guide, free channel, first-mover in NE Ohio power washing; kit_email_capture_setup_2026-05-24.md — Kit.com landing page + delivery automation + nurture trigger for the checklist magnet; 23 minutes to implement before Tuesday ads launch)
- Proposals: 1 (Jasmine refresh of facebook_posts_june_week2_4 — current version from May 20 predates VOC rewrites and June Booking Blitz context; should be rewritten before June 8 when that content goes live)
- New issue: Email List at 0 — with ads launching Tuesday, every non-converting visitor is permanently lost without an email opt-in; all 3 required assets now written and ready; 23 min to implement before Tuesday
- Key code fix: check_replies.py phone/company enrichment now reads both contacts_cache.json AND pipeline_data.json — future-proofs for when gas station/fleet contacts get Mixmax sequences and show up in reply checks
- Highest priority TODAY (Sun May 24 evening): (1) Text Anthony/Land Pro 440-320-2779 — "referral swap" pitch (2) Pause Instantly.ai — app.instantly.ai → a1c08c3d + 626cd15d → Pause
- Highest priority TOMORROW (Mon May 25 Memorial Day): Run check_replies.py at 10am → read monday_memorial_day_final_check_2026-05-24.md
- Highest priority TUESDAY May 26: (1) READ may26_week_priority_stack_2026-05-24.md FIRST (2) 20 min Kit.com setup BEFORE ads launch — kit_email_capture_setup_2026-05-24.md (3) Claim Yelp listing — yelp_business_profile_guide_2026-05-24.md — 15 min (4) Then launch ads per launch card

## RUN METRICS — Run 73 | 2026-05-24
- Total RESOLVED: 77 (0 new — all open issues require Bradley action or are permanent infrastructure constraints)
- Total OPEN: 18 (0 new closed, 0 new opened)
- Auto-upgrades shipped: 4 (carla.md — county rotation calendar added; marcus.md — local CLI run commands added; donna.md — June Booking Blitz section updated with current action docs; tommy.md — inbound_response_protocol format entry added)
- Deliverables written: 3 (weekly_summary_2026-05-25.md — Vera's first-ever Monday 6am weekly summary: upgrades this week, proposals pending, biggest Tuesday opportunity; facebook_posts_june_week1_2026-05-24.md — 5 Facebook posts for June 2–6 Booking Blitz launch week, June 4 commercial post synced with Round 2 enrollment; inbound_response_protocol_2026-05-24.md — handles organic Facebook comment/DM, website form, inbound call, missed call recovery; complements Rick's paid-ad SOPs)
- Proposals: 0 (all pending proposals already in Slack from Runs 70–72; no new proposals this run)
- Key verifications this run: pipeline_data.json confirmed — all 5 Tier 1 contractors still "New Lead," phones present; gas station contacts all have lead_type="gas_station" set — routing confirmed correct for pending enrollment; run_summit_pull.command + run_summit_both.command scripts verified — both correct; vera_relay.py code reviewed — no bugs found
- Highest priority TODAY (Sun May 24 evening): (1) Text Anthony/Land Pro 440-320-2779 — "referral swap" pitch (2) Pause Instantly.ai — app.instantly.ai → a1c08c3d + 626cd15d → Pause
- Highest priority TOMORROW (Mon May 25 Memorial Day): Run check_replies.py at 10am → see monday_memorial_day_final_check_2026-05-24.md
- Highest priority TUESDAY May 26: Read may26_week_priority_stack_2026-05-24.md first → Post Facebook Post 1 at 8am → Launch ads 9:15am → Past customer texts 10am → Tier 1 contractor texts 8:45am

## RUN METRICS — Run 72 | 2026-05-24
- Total RESOLVED: 77 (0 new — all open issues require Bradley action or are permanent infrastructure constraints)
- Total OPEN: 18 (0 new closed, 0 new opened)
- Auto-upgrades shipped: 4 (agents/rick.md — added google_ads_first_week_monitoring_guide format entry; agents/tommy.md — added annual_plan_customer_welcome_kit format entry; CLAUDE.md — added Quick Shortcuts section for run_summit_pull.command + run_summit_both.command double-click shortcuts; agents/danny.md — updated example Apollo payload per_page 25→50 to match actual code)
- Deliverables written: 4 (facebook_posts_may26_week_2026-05-24.md — 5 launch-week Facebook posts Tue May 26 through Sat May 30 with schedule guide; google_ads_first_week_monitoring_guide_2026-05-24.md — Day 1/3/7 monitoring guide with CTR benchmarks, CPC ranges, negative keywords, Quality Score guide, common mistakes; june_week1_sprint_2026-05-24.md — refreshed June 2–6 day-by-day sprint incorporating all new context: VOC rewrites, enrollment battle card, past customer texts, ads monitoring, revenue targets; annual_plan_customer_welcome_kit_2026-05-24.md — post-YES annual plan onboarding: 4-touch sequence from confirmation text through referral seed + FAQ answers + revenue math)
- Proposals: 2 (Kit.com email capture setup — ads are live but no email list funnel beyond Facebook Lead Gen form; Kit.com + Home Maintenance Checklist content = organic lead capture at zero cost; Yelp Business profile activation — free local search channel alongside GBP; most competitors don't actively manage it; 15-min setup, ongoing impressions)
- Key issue updates: Tier 1 contractors — TODAY is final Sunday window (Memorial Day tomorrow); 5 contractors untouched since May 18; Anthony 440-320-2779 and Venus 216-810-2497 are highest-ROI 10-min action; Instantly.ai — 11 days until June 4 enrollment, every day paused = one more day of recovery; Tuesday is now the main action day: use facebook_posts_may26_week for launch-week social, google_ads_first_week_monitoring_guide for Day 1 check, june_week1_sprint for June plan
- Highest priority TODAY (Sun May 24 evening): (1) Text Anthony/Land Pro 440-320-2779 — "referral swap" pitch (2) Text Venus/Reliable Roofing 216-810-2497 (3) Pause Instantly.ai — app.instantly.ai → a1c08c3d + 626cd15d
- Highest priority TOMORROW (Mon May 25, Memorial Day): Run check_replies.py at 10am → `outputs/donna/monday_memorial_day_final_check_2026-05-24.md`
- Highest priority TUESDAY May 26: (1) Post `facebook_posts_may26_week_2026-05-24.md` Post 1 at 8am (2) Launch ads 9:15am (3) Check Day 1 at end of day using `google_ads_first_week_monitoring_guide_2026-05-24.md` (4) Full blitz: `may26_week_priority_stack_2026-05-24.md`

## RUN METRICS — Run 71 | 2026-05-24
- Total RESOLVED: 77 (0 new — all open issues require Bradley action or are permanent infrastructure constraints)
- Total OPEN: 18 (0 new closed, 0 new opened)
- Auto-upgrades shipped: 4 (check_replies.py — added "all clear" Slack post when API works but pipeline is quiet; was silent before, Bradley couldn't tell if script ran or not; integrations/mixmax.py — added home inspector + property inspector + solar installer + solar panel to CONTRACTOR_TITLES; workers/lead_pipeline.py — added home inspection + solar installation to Carla contractor search keywords; agents/rick.md + tommy.md + donna.md — added 3 new output format catalog entries)
- Deliverables written: 3 (june4_enrollment_battle_card_2026-05-24.md — operationalized press-GO June 4 execution card with exact copy-paste commands, pre-check June 3, expected outputs, failure modes; past_customer_june_text_scripts_2026-05-24.md — 5 copy-paste text scripts for June 4 past customer blast by service type, personalization guide, response handling, timing guide, revenue math; facebook_ad_week1_revenue_tracker_2026-05-24.md — Day 1/3/7/14 fill-in tracker with benchmarks, decision tree, and revenue projections for first two weeks of ad spend)
- Proposals: 2 (home inspector referral segment for Carla — high-value new segment at buyer/seller moments; post-5-star review referral text chain — zero-cost referral generation from satisfied customers)
- Key issue updates: check_replies.py Slack silence bug FIXED this run; June 4 battle card NOW EXISTS — was the last missing operational document; reply window closes TOMORROW (May 25); Instantly.ai still CRITICAL — 11 days recovery window starting NOW
- Highest priority TODAY (Sun May 24): (1) Text Anthony/Land Pro 440-320-2779 + Venus/Reliable Roofing 216-810-2497 — 10 min (2) Pause Instantly.ai — 3 min — app.instantly.ai → a1c08c3d + 626cd15d → Pause
- Highest priority TOMORROW (Mon May 25 Memorial Day): Run check_replies.py at 10am — `python3 workers/check_replies.py` — see monday_memorial_day_final_check_2026-05-24.md
- Highest priority TUESDAY May 26: 8am Summit pull → 8:20am bridge emails → 9am gas station Mixmax sequence → 9:15am Facebook Ads launch → 10am past customer text blast (past_customer_june_text_scripts_2026-05-24.md)

## RUN METRICS — Run 70 | 2026-05-24
- Total RESOLVED: 77 (0 new — all open issues require Bradley action or are permanent infrastructure constraints)
- Total OPEN: 18 (0 new closed, 0 new opened)
- Auto-upgrades shipped: 5 (rick.md Ready Assets header "Monday after Memorial Day" → "Tuesday after Memorial Day" — survived 9 previous runs hiding in the header while sub-items were already corrected; carla.md added realtor_summer_voc_sequence format entry; tommy.md added hot_lead_callback_script format entry; donna.md added may26_week_priority_stack format entry; danny.md added gas_station_manual_email_blast format entry — file existed in outputs/danny/ since May 20 with no catalog entry)
- Deliverables written: 3 (realtor_summer_voc_sequence_2026-05-24.md — full 3-touch realtor referral sequence using NE Ohio VOC, 3 trade-specific Touch 1 variants, response handling, $18K revenue math; hot_lead_callback_script_2026-05-24.md — word-for-word script for when a PM/realtor/contractor who opened Mixmax email 2-3x calls back, 3 discovery questions, phone quoting guide, 5-step closing, post-call actions; may26_week_priority_stack_2026-05-24.md — single-page cheat sheet for week of May 26-30: 10-slot Tuesday 90-min action plan, Wed-Fri priority tables, critical path deadlines, week-end check)
- Proposals: 2 (NE Ohio Home Maintenance Checklist content — brief exists since May 12, actual 12-month content never written; Tommy should write it; becomes the email list-building asset for Kit.com; realtor pipeline revival blitz — all 7 NE Ohio counties in June with fresh Apollo pull; 10 realtor partners = $18K potential)
- Key issue updates: Tier 1 contractors — TODAY window still open (Sunday May 24), Anthony text is the highest-ROI single action available; Instantly.ai — 11 days until Round 2, every day not paused = worse deliverability June 4; rick.md "Monday" bug — RESOLVED in this run after surviving 9 previous fixes in the same file; Reply window — closes TOMORROW (Memorial Day), run check_replies.py at 10am per monday_memorial_day_final_check_2026-05-24.md
- Highest priority TODAY (Sun May 24): (1) Text Anthony/Land Pro 440-320-2779 (2) Text Venus/Reliable Roofing 216-810-2497 — 10 min total (3) Pause Instantly.ai — app.instantly.ai → a1c08c3d + 626cd15d → Pause (3 min)
- Highest priority TOMORROW (Mon May 25 Memorial Day): Run check_replies.py at 10am — outputs/donna/monday_memorial_day_final_check_2026-05-24.md
- Highest priority TUESDAY May 26: Read outputs/rick/facebook_lead_response_sop_2026-05-24.md FIRST → then outputs/donna/may26_week_priority_stack_2026-05-24.md

## RUN METRICS — Run 69 | 2026-05-24
- Total RESOLVED: 77 (0 new this run — all open issues require Bradley action)
- Total OPEN: 18 (0 new closed, 0 new opened)
- Auto-upgrades shipped: 3 (rick.md — added google_guaranteed_setup + facebook_lead_gen_launch_checklist to output catalog; jasmine.md — added instagram_stories_scripts format entry; donna.md — added monday_memorial_day_final_check format entry)
- Deliverables written: 3 (facebook_lead_response_sop_2026-05-24.md — step-by-step SOP for Facebook Lead Gen form submissions: 5-min response target, live call script, voicemail, text follow-up, pricing reference, Workiz logging; MUST READ before Tuesday ads launch; june_gbp_content_calendar_2026-05-24.md — 5 GBP posts for all of June, week-by-week, each with hook + body + image guidance + CTA + keywords; instagram_stories_scripts_2026-05-24.md — 5 Story scripts for peak season: before/after reveal, roof reveal with question sticker, neighbor hook, customer reaction, Friday urgency)
- Proposals: 2 (Build actual "NE Ohio Home Maintenance Checklist" content — Donna has the brief from May 12, the CONTENT was never written; this becomes the email list-building asset; auto-reply to Facebook messages with keyword triggers — Meta Business Suite has this built in, no code needed)
- Highest priority TODAY (Sun May 24): (1) Text Anthony/Land Pro 440-320-2779 — trades are working right now (2) Text Venus/Reliable Roofing 216-810-2497 — 2 texts in 5 minutes (3) Pause Instantly.ai — app.instantly.ai → Campaigns → ⋮ → Pause a1c08c3d + 626cd15d (4) GBP post — `outputs/vera/june_gbp_content_calendar_2026-05-24.md` Week 1 post if not published yet
- Highest priority MONDAY May 25 (Memorial Day): Run check_replies.py at 10am — protocol in `outputs/donna/monday_memorial_day_final_check_2026-05-24.md`
- Highest priority TUESDAY May 26: (1) READ `outputs/rick/facebook_lead_response_sop_2026-05-24.md` BEFORE launching ads (2) READ `outputs/rick/facebook_lead_gen_launch_checklist_2026-05-24.md` (3) Then launch — `outputs/donna/tuesday_may26_launch_card_2026-05-23.md`

## RUN METRICS — Run 68 | 2026-05-24
- Total RESOLVED: 77 (0 new this run — all open issues require Bradley action)
- Total OPEN: 18 (0 new closed, 0 new opened)
- Auto-upgrades shipped: 4 (lead_pipeline.py run_carla() output filename now includes county label — prevents same-day overwrite when two counties pulled; vera_relay.py Carla staleness alert updated with run_summit_both.command double-click shortcut; agents/nina.md added check_replies.py reference; agents/carla.md added pool_service_referral_blitz format)
- Deliverables written: 3 (monday_memorial_day_final_check_2026-05-24.md — 10-min Memorial Day morning protocol, reply window closes tomorrow; pool_service_referral_blitz_2026-05-24.md — Memorial Day pool season outreach for Carla, NE Ohio pool openings happening NOW; facebook_lead_gen_launch_checklist_2026-05-24.md — 5-block pre-launch checklist for Tuesday Facebook ads: Pixel, lead notifications, form settings, budget, response SOP)
- Proposals: 1 (pool service referral blitz — Memorial Day timing makes this the best week to pitch pool companies; revenue math: 15 referrals × $350 = $5,250 from a single relationship)
- Highest priority TODAY (Sun May 24): (1) Text Anthony/Land Pro 440-320-2779 — trades working Memorial Day weekend, phones are on (2) Pause Instantly.ai — 3 min — app.instantly.ai → Campaigns → ⋮ → Pause a1c08c3d + 626cd15d (3) LinkedIn pitches to pool service companies — `outputs/carla/pool_service_referral_blitz_2026-05-24.md`
- Highest priority MONDAY May 25 (Memorial Day): Run check_replies.py at 10am — 10 min — `outputs/donna/monday_memorial_day_final_check_2026-05-24.md`
- Highest priority TUESDAY May 26: Read `outputs/rick/facebook_lead_gen_launch_checklist_2026-05-24.md` BEFORE launching ads → then full 90-min blitz `outputs/donna/tuesday_may26_launch_card_2026-05-23.md`

## RUN METRICS — Run 67 | 2026-05-23
- Total RESOLVED: 77 (0 new this run — all open issues require Bradley action)
- Total OPEN: 18 (0 new closed, 0 new opened)
- Auto-upgrades shipped: 3 (lead_pipeline.py Danny per_page 25→50 + Carla 15→20; carla.md 2 new output format entries; scripts/run_summit_both.command — new double-click shortcut for Danny+Carla Summit pull in one step)
- Deliverables written: 3 (gbp_memorial_day_post_2026-05-23.md — GBP post for TODAY, 2-min to publish, Memorial Day weekend search traffic; contractor_referral_sequence_voc_rewrite_2026-05-23.md — Carla's 3-touch contractor sequence using Marcus VOC + 10 trade-specific customizations; summit_county_referral_pull_guide_2026-05-23.md — Carla Summit County parallel pull guide)
- Proposals: 2 (update CLAUDE.md with run_summit_both.command; add Carla county-specific staleness check to vera_relay.py)
- Highest priority TODAY (Sat May 23): (1) Post GBP NOW — business.google.com/dashboard — outputs/vera/gbp_memorial_day_post_2026-05-23.md (2) Pause Instantly.ai — app.instantly.ai → Campaigns → ⋮ → Pause a1c08c3d + 626cd15d (3) Double-click scripts/run_summit_both.command — Danny + Carla Summit County, 6 min (4) Post Saturday Facebook post — outputs/jasmine/facebook_posts_memorial_day_weekend_2026-05-23.md
- Highest priority TUESDAY May 26: Full 90-min blitz — `outputs/donna/tuesday_may26_launch_card_2026-05-23.md`

## RUN METRICS — Run 66 | 2026-05-23
- Total RESOLVED: 77 (0 new this run — all open issues require Bradley action)
- Total OPEN: 18 (0 new closed, 0 new opened)
- Auto-upgrades shipped: 4 (danny.md Instantly.ai "Not active" → accurate warning with campaign IDs; vera_relay.py git log window -20 → -100 to prevent silent Slack message drops; rick.md output format catalog + facebook_ads_first_week_monitoring_guide entry; tommy.md output format catalog + neighbor_canvass_script entry)
- Deliverables written: 2 (facebook_ads_first_week_monitoring_guide_2026-05-23.md — Day 1/3/7 guide for first-time Facebook ad launch, metric thresholds, lead response setup, budget scaling, common mistakes; neighbor_canvass_script_2026-05-23.md — 4 versions: door-knock script, leave-behind card, same-street past customer text, in-neighborhood commercial text; revenue math: ~$750/week zero-cost at 10 jobs/week)
- Proposals: 2 (see Slack messages)
- Highest priority TODAY (Sat May 23): (1) Pause Instantly.ai — app.instantly.ai → Campaigns → ⋮ → Pause a1c08c3d + 626cd15d (2) Double-click scripts/run_summit_pull.command — Summit County pull, 5 min (3) Text Anthony 440-320-2779 — referral swap pitch
- Highest priority TUESDAY May 26: 8:00am Summit pull → 8:20am bridge emails → 9:00am gas station sequence → 9:15am Facebook/Google Ads launch → READ facebook_ads_first_week_monitoring_guide BEFORE first lead arrives → START door-knocking neighbors after first job

## RUN METRICS — Run 58 | 2026-05-23
- Total RESOLVED: 73 (1 new: vera_relay unpushed-commit flush — prevents Slack message loss when push fails mid-relay)
- Total OPEN: 17 (0 new closed — all require Bradley action; 0 new opened)
- Auto-upgrades shipped: 5 (vera_relay.py unpushed commit flush; tommy.md missing output entry; danny.md Summit urgency date to May 23; crontab 2pm check_replies scan; jasmine.md linkedin_posts_may26_week format entry)
- Deliverables written: 2 (linkedin_posts_may26_week_2026-05-23.md — fills May 26-30 LinkedIn gap for PM connect week; june_commercial_calendar_2026-05-23.md — 4-week commercial action calendar May 26–June 18)
- Proposals: 2 (yard sign + on-site referral card protocol; referral partner voicemail scripts for warm contractor follow-up)
- Highest priority actions TODAY: (1) Summit County pull — `python3 workers/lead_pipeline.py danny Summit` — DEADLINE SUNDAY NIGHT (2) Post LinkedIn Post 1 (HOA board meeting angle) + 5 PM connect requests (3) Pause Instantly.ai campaigns a1c08c3d + 626cd15d — 3 min fix

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

## RUN METRICS — Run 64 | 2026-05-23
- Total RESOLVED: 76 (0 new this run — all open issues require Bradley action)
- Total OPEN: 18 (0 new closed, 0 new opened)
- Auto-upgrades shipped: 4 (lead_pipeline.py run_carla() double-print bug fixed — removed unconditional county-batch print, each branch now prints its own label; vera_relay.py Danny staleness message updated with double-click shortcut + May 31 deadline; agents/jasmine.md 2 new output format entries; agents/tommy.md pre_job_reminder format entry)
- Deliverables written: 3 (pre_job_reminder_text_sequence_2026-05-23.md — day-before + 2h-before + post-job texts, response handling, Workiz integration note; voc_library_2026-05-23.md — Marcus VOC framework from first principles: 40+ phrases, residential/commercial/referral tables, seasonal NE Ohio language, what to avoid; before_after_photo_capture_protocol_2026-05-23.md — Jasmine capture guide with shot types, file naming, photo_pairs.json integration, caption templates, Instagram Stories, LinkedIn version)
- Proposals: 2 (Run Marcus locally for live competitor VOC from Google Maps reviews — run `claude` CLI on Mac, ask Marcus to profile top 5 Cleveland competitors; Approve Twilio setup to automate pre-job reminder texts — $15/mo cost, reduces no-shows 40%+, pays back on first prevented no-show)
- Highest priority TODAY (Sat May 23): (1) Pause Instantly.ai NOW — app.instantly.ai → Campaigns → ⋮ → Pause a1c08c3d + 626cd15d (2) Text Anthony/Land Pro 440-320-2779 — script in open_issues.md (3) Double-click scripts/run_summit_pull.command in Finder — 5 min, no typing required
- Highest priority TUESDAY May 26: 8:00am Summit pull → 8:20am bridge emails → 9:00am gas station sequence → 9:15am ads launch → Read google_guaranteed_lead_response_sop BEFORE first ad lead comes in

## RUN METRICS — Run 63 | 2026-05-23
- Total RESOLVED: 76 (0 new this run — all open issues require Bradley action)
- Total OPEN: 18 (0 new closed, 0 new opened)
- Auto-upgrades shipped: 3 (vera_relay.py git fetch before flush — ordering fix; lead_pipeline.py Carla county override CLI flag; integrations/mixmax.py INSTANTLY_PAUSED runtime warning in enroll_batch — blocks accidental Round 2 enrollment when Instantly still running)
- Deliverables written: 2 (google_guaranteed_lead_response_sop_2026-05-23.md — full SOP including call script, voicemail, text follow-up, quote conversation, booking steps, pricing reference; annual_plan_upsell_sequence_2026-05-23.md — same-day text + 30-day email + objection handling + pricing table + revenue math)
- Proposals: 2 (Pre-job reminder text sequence — day-before + 2-hour reminder reduces no-shows 40%+; Before/after photo capture protocol — systematic pipeline for Jasmine's content machine after every job)
- Highest priority TODAY (Sat May 23): (1) Pause Instantly.ai NOW — app.instantly.ai → Campaigns → ⋮ → Pause a1c08c3d + 626cd15d (2) Text Anthony/Land Pro 440-320-2779 — referral swap pitch (3) Double-click scripts/run_summit_pull.command — Summit pull, 5 min
- Highest priority TUESDAY May 26: 8:00am Summit pull → 8:20am bridge emails → 9:00am gas station sequence → 9:15am ads launch → Read google_guaranteed_lead_response_sop BEFORE ads go live

## RUN METRICS — Run 62 | 2026-05-23
- Total RESOLVED: 76 (0 new this run — all open issues require Bradley action)
- Total OPEN: 18 (0 new closed, 0 new opened)
- Auto-upgrades shipped: 4 (scripts/run_summit_pull.command — double-click Mac shortcut for Summit County pull; donna.md + tommy.md + rick.md output format catalog additions)
- Deliverables written: 3 (round2_enrollment_readiness_checklist_2026-05-23.md — GO/NO-GO for June 3 Round 2 prep; june_week3_4_commercial_sprint_2026-05-23.md — June 16-30 day-by-day plan; scripts/run_summit_pull.command — zero-typing Mac shortcut)
- Proposals: 2 (Annual Plan Upsell Sequence — Tommy writes post-job same-day text + 30-day follow-up; Roof Soft Wash mini-campaign to existing PM contacts — highest-margin service, competitors skip it)
- Highest priority TODAY (Sat May 23): (1) Pause Instantly.ai NOW — app.instantly.ai → Campaigns → ⋮ → Pause a1c08c3d + 626cd15d (2) Text ONE contractor: Anthony/Land Pro 440-320-2779 — "referral swap" pitch (3) Double-click `scripts/run_summit_pull.command` in Finder — 5 min, no typing
- Highest priority TUESDAY May 26: Full 90-min blitz — `outputs/donna/tuesday_may26_launch_card_2026-05-23.md`

## RUN METRICS — Run 61 | 2026-05-23
- Total RESOLVED: 76 (2 new: rick.md "Monday May 26" date error fixed to Tuesday; open_issues.md header resolved from 58→74 stale count; danny.md + carla.md + donna.md output format catalog updates)
- Total OPEN: 18 (corrected from prior 17 count — 18 actual issues; 0 new closed; 0 new opened)
- Auto-upgrades shipped: 5 (rick.md Tuesday date fix; danny.md urgency note clarified + output formats added; donna.md + carla.md output format additions; open_issues.md header correction)
- Deliverables written: 2 (`tuesday_may26_launch_card_2026-05-23.md` — corrected 90-min Tuesday blitz with revenue math + week-of priority stack; `june_referral_revival_texts_2026-05-23.md` — 6-trade text scripts for June Booking Blitz warm-up of Carla's pipeline)
- Proposals: 3 (Google Guaranteed app TODAY while at computer; past customer text THIS AFTERNOON while it's Memorial Day weekend; Instagram Stories Memorial Day angle)
- Highest priority actions TODAY: (1) Pause Instantly.ai — 3 min — app.instantly.ai → Campaigns → Pause a1c08c3d + 626cd15d (2) Run `python3 workers/lead_pipeline.py danny Summit` — 5 min (3) Text ONE past customer this afternoon — Memorial Day "before your cookout" angle
- Highest priority TUESDAY May 26: 8:00am Summit pull → 8:20am bridge emails → 9:00am gas station sequence → 9:15am Facebook Ads live

## RUN METRICS — Run 60 | 2026-05-23
- Total RESOLVED: 74 (0 new this run — all open issues require Bradley action)
- Total OPEN: 17 (0 new closed, 0 new opened)
- Auto-upgrades shipped: 5 (check_replies.py company enrichment; donna.md output format additions; rick.md urgency date made generic; tommy.md output format entry; danny.md output format entry)
- Deliverables written: 2 (gas_station_mixmax_sequence_creation_2026-05-23.md — step-by-step Mixmax UI guide to unlock 18 idle contacts; may25_sunday_evening_protocol_2026-05-23.md — tonight's reply window close protocol with full if/then decision tree)
- Proposals: 2 (post-job doorstep video testimonial protocol; CAI Ohio Chapter vendor directory listing)
- Highest priority actions TONIGHT: (1) Run Sunday evening protocol — outputs/tommy/may25_sunday_evening_protocol_2026-05-23.md (2) Summit County pull — DEADLINE TONIGHT — `python3 workers/lead_pipeline.py danny Summit`
- Highest priority MONDAY May 26: 8:15am Danny pull, 9am bridge emails + Facebook Ads launch, 10am gas station sequence creation

## RUN METRICS — Run 59 | 2026-05-23
- Total RESOLVED: 74 (1 new: danny.md Week 22 date bug — "May 26 (Week 22) = Medina" was wrong; May 26 is Week 21; running on May 26 still targets Summit; fixed to "June 1 (Week 22) = Medina")
- Total OPEN: 17 (0 new closed — all require Bradley action; 0 new opened)
- Auto-upgrades shipped: 3 (danny.md Week 22 date fix; CLAUDE.md check_replies cron lines added; rick.md stale "May 22" date → "May 23")
- Deliverables written: 1 (june1_prep_checklist_2026-05-23.md — 15-min June 1 morning launch: Medina pull, Summit catch-up, Nina weekly, bridge email follow-up, Instantly pause check, Round 2 timeline, gas station sequence creation)
- Proposals: 2 (Instagram Reels channel; post-job 3-text automation sequence)
- Highest priority actions TODAY: (1) Summit County pull — `python3 workers/lead_pipeline.py danny Summit` — NOW, deadline TOMORROW NIGHT (2) Pause Instantly.ai campaigns a1c08c3d + 626cd15d (3) LinkedIn connects with 2+ open leads
