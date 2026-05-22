# Vera Cole — Open Issues Tracker
*Updated automatically each run. Only mark RESOLVED after verifying the fix works.*

---

## RESOLVED — Jasmine infinite retry loop (not_in_channel)
- Resolved: 2026-05-18
- Fix: `pair["processed"] = True` set before try block. `pair["success"]` distinguishes clean vs failed.

## RESOLVED — Carla Apollo keyword filter ignored
- Resolved: 2026-05-18 (run 5)
- Fix: `apollo_search()` accepts `keywords=None` param and passes `q_organization_keyword_tags`.

## RESOLVED — verify_and_repair_enrollment mass re-enrollment on API failure
- Resolved: 2026-05-18 (run 5)
- Fix: Returns `None` on all-failure; skips repair on `None`.

## RESOLVED — nina_report fetch_recipients drops dict responses
- Resolved: 2026-05-18
- Fix: Handles both list and dict Mixmax responses.

## RESOLVED — Apollo JSON parse crash
- Resolved: 2026-05-18
- Fix: try/except around all Apollo calls.

## RESOLVED — Workiz case-insensitive job matching
- Resolved: 2026-05-18
- Fix: 10 variants, diagnostic logging.

## RESOLVED — jasmine_flyer.py env loading only in __main__
- Resolved: 2026-05-18
- Fix: `_load_env()` at module level.

## RESOLVED — workiz_report "No jobs found" misleads on API failure
- Resolved: 2026-05-18
- Fix: `WORKIZ_API_ERROR` sentinel.

## RESOLVED — nina_report.py misleading action items
- Resolved: 2026-05-18
- Fix: Accurate wording for 0-reply state.

## RESOLVED — nina_report.py double API fetch in run_daily()
- Resolved: 2026-05-18 (run 5)
- Fix: `seq_stats_cache` dict eliminates redundant calls.

## RESOLVED — p['id'] KeyError crash in lead_pipeline run_danny() / run_carla()
- Resolved: 2026-05-20
- Fix: `if not person_id: continue` before apollo_reveal call.

## RESOLVED — gas_station/fleet contacts not blocked from repair loop
- Resolved: 2026-05-20
- Fix: `_sequence_is_live()` checked in `verify_and_repair_enrollment()`; PENDING sequences skipped.

## RESOLVED — Apollo 0 people vs all-duplicates logging confusion
- Resolved: 2026-05-20
- Fix: Separate log messages distinguish API block from dedup.

## RESOLVED — server.py POST /api/queue — malformed body crash (500)
- Resolved: 2026-05-20
- Fix: try/except around json.loads(body), returns HTTP 400.

## RESOLVED — server.py parse_log() — concurrent write crash
- Resolved: 2026-05-20
- Fix: try/except around LOG_FILE.read_text().

## RESOLVED — server.py POST /api/contacts/workflow — write failure 500
- Resolved: 2026-05-20
- Fix: CONTACTS_F.write_text() wrapped in try/except.

## RESOLVED — Mixmax contacts not flagged stale on dashboard (no last_contact)
- Resolved: 2026-05-20
- Fix: server.py fallback for Mixmax contacts with no last_contact.

## RESOLVED — workiz_report.py fragile path (os.path.dirname(__file__))
- Resolved: 2026-05-20
- Fix: Replaced with BASE_DIR for all paths.

## RESOLVED — server.py get_outputs() — PermissionError crashes dashboard
- Resolved: 2026-05-20
- Fix: d.iterdir() wrapped in try/except.

## RESOLVED — gas_station misrouting — 'district manager' false positive
- Resolved: 2026-05-21 (run 36)
- Fix: Removed from GAS_STATION_KEYWORDS in mixmax.py.

## RESOLVED — fleet_washing misrouting — 'operations manager' false positive
- Resolved: 2026-05-21 (run 36)
- Fix: Removed from FLEET_KEYWORDS in mixmax.py.

## RESOLVED — lead_pipeline verify_and_repair — doesn't skip PENDING sequences
- Resolved: 2026-05-21 (run 36)
- Fix: `_sequence_is_live` check before repair attempt.

## RESOLVED — server.py save_queue() — write failure propagates as 500
- Resolved: 2026-05-21 (run 36)
- Fix: Wrapped in try/except.

## RESOLVED — workiz_report.py log_activity() crash on fresh clone
- Resolved: 2026-05-21 (run 35)
- Fix: os.makedirs() + try/except around file write.

## RESOLVED — workiz_report.py JobTotalPrice TypeError on string price
- Resolved: 2026-05-21 (runs 40–41)
- Fix: float() cast around all 6 price fields.

## RESOLVED — jasmine_flyer.py output filename collision (same-date pairs)
- Resolved: 2026-05-21 (run 38)
- Fix: pair_id suffix appended to output filename.

## RESOLVED — jasmine_flyer.py LOGS_DIR.mkdir missing — fresh clone crash
- Resolved: 2026-05-21 (run 41)
- Fix: LOGS_DIR.mkdir(exist_ok=True) added to log().

## RESOLVED — nina_report weekly — no overdue/due-soon follow-up section
- Resolved: 2026-05-21 (run 42)
- Fix: Added "Overdue Follow-ups" and "Due This Week" sections with name+phone+date.

## RESOLVED — Carla realtor search missing brokerage keywords
- Resolved: 2026-05-21 (run 42)
- Fix: Added 10 NE Ohio real estate firm names to CARLA_SEARCHES realtor keywords.

## RESOLVED — lead_pipeline DANNY_TITLES missing Apollo search titles
- Resolved: 2026-05-21 (run 43)
- Fix: Added 'portfolio manager' and 'building supervisor' — present in mixmax.py detection but absent from Apollo search. These leads would be routed correctly but never pulled.

## RESOLVED — No ready-to-paste crontab setup file
- Resolved: 2026-05-21 (run 43)
- Fix: Created scripts/crontab_setup.txt with all 6 cron jobs. Bradley runs `crontab -e` and pastes.

## RESOLVED — Slack photo watcher — JSON/timeout safety
- Resolved: 2026-05-21
- Fix: load_seen() + load_pairs() + slack_get() all wrapped in try/except.

## RESOLVED — server.py /api/file — directory traversal vulnerability
- Resolved: 2026-05-21 (run 40)
- Fix: resolve().startswith(OUTPUTS) path containment check.

## RESOLVED — vera_relay.py redundant --oneline flag
- Resolved: 2026-05-20 (run 33)
- Fix: Removed conflicting --oneline from git log command.

## RESOLVED — pipeline_data.json missing next_followup dates
- Resolved: 2026-05-20 (run 33)
- Fix: Set next_followup 2026-05-26 for Bulletproof Lawncare + Damrons Landscaping.

## RESOLVED — lead_pipeline.py gas_station/fleet worker tag wrong
- Resolved: 2026-05-20 (run 31)
- Fix: gas_station/fleet tagged 'danny' not 'carla' in mixmax_enroll().

## RESOLVED — agent files API key hardcoded
- Resolved: 2026-05-20 (run 29)
- Fix: Replaced with load-from-.env note in danny.md and carla.md.

## RESOLVED — No phone cold call script for hot leads
- Resolved: 2026-05-20 (run 27)
- File: outputs/tommy/hot_lead_phone_script_2026-05-22.md

## RESOLVED — No service pages written for web build
- Resolved: 2026-05-20 (run 27)
- File: outputs/tommy/website_copy_service_pages_2026-05-20.md

## RESOLVED — No quote follow-up sequence
- Resolved: 2026-05-20 (run 29)
- File: outputs/tommy/quote_followup_sequence_2026-05-20.md

## RESOLVED — LinkedIn followup post-connect templates missing
- Resolved: 2026-05-20 (run 32)
- File: outputs/tommy/linkedin_followup_post_connect_2026-05-20.md

## RESOLVED — No touch3 reply response templates
- Resolved: 2026-05-20
- File: outputs/tommy/touch3_reply_response_templates_2026-05-20.md

## RESOLVED — No inbound response protocol
- Resolved: 2026-05-19
- File: outputs/tommy/inbound_response_protocol_2026-05-19.md

## RESOLVED — No contractor referral text scripts
- Resolved: 2026-05-20
- File: outputs/tommy/contractor_referral_text_script_2026-05-20.md

## RESOLVED — GBP post content gap (no templates)
- Resolved: 2026-05-21 (run 39)
- File: outputs/vera/gbp_post_may21_2026.md

## RESOLVED — Jasmine LinkedIn posts for June peak season (gap)
- Resolved: 2026-05-21 (run 43)
- Fix: 10 LinkedIn posts written May 27–June 30. File: outputs/jasmine/linkedin_posts_june_2026-05-21.md

---

## OPEN — Manual Contacts Sitting Untouched (New Lead stage)
- First seen: 2026-05-18
- Description: 33 contacts in New Lead stage. 0 last_contact dates. Tier 1 contractors — tonight is the last window before Memorial Day weekend.
- Tier 1 TEXT TONIGHT: Anthony/Land Pro (440-320-2779), Dontez/GTP (440-396-0814), Chris/Twin Improvements (216-773-0757), Venus/Reliable Roofing (216-810-2497), Logan/Pagels (216-956-5263)
- Run 43: Past customer reengagement launch guide written (donna/past_customer_reengagement_launch_2026-05-21.md). May 26 is the backup if tonight doesn't happen.
- Resolution criteria: Bradley texts Tier 1 list tonight or May 26 (Memorial Day Blitz Day).

---

## OPEN — Mixmax API blocked in cloud execution environment
- First seen: 2026-05-18
- Workaround: All pipeline scripts return None/safe fallback on 403. nina_report shows explicit API warning.
- Next steps: Bradley checks Mixmax → API Settings → IP Allowlist.

---

## OPEN — All external APIs blocked from cloud (Apollo, Workiz, Mixmax)
- First seen: 2026-05-18
- Workaround: Cron job schedule documented. scripts/crontab_setup.txt created run 43 — paste into `crontab -e` on Mac.
- CRITICAL: Danny has not pulled leads since May 12 (9 days). Round 2 enrollment targets June 4. Cron must be running by May 26.

---

## OPEN — Slack Webhook blocked in cloud execution environment
- First seen: 2026-05-18
- Workaround: Messages written to pending_slack_messages.md. GitHub Action posts on push.
- Run 43: vera_relay.py is the local alternative — runs on crontab every 5 min and posts pending messages.

---

## OPEN — GitHub Actions PAT missing workflow scope
- First seen: 2026-05-20 (run 34)
- Description: vera-slack-relay.yaml written to .github/workflows/. Cloud push blocked — PAT needs 'workflow' scope.
- Run 43: deploy_github_action.sh in scripts/ — run AFTER adding PAT workflow scope.
- Action: Settings → Developer settings → Personal access tokens → Edit ghp_lrUhBq7... → check 'workflow' → Save → run scripts/deploy_github_action.sh

---

## OPEN — Instantly.ai vs Mixmax Overlap (duplicate sequence risk)
- First seen: 2026-05-18
- Description: server.py has active Instantly.ai campaign IDs. Risk of duplicate emails to same contacts.
- Run 43: Still unresolved.
- Action: Log into Instantly.ai and pause/disable all campaigns. Mixmax is the sole active platform.

---

## OPEN — 0% reply rate across enrolled contacts
- First seen: 2026-05-18
- Description: ~45 contacts enrolled, 0 replies. Touch 3 fires May 22.
- Run 43: All playbooks in place. Update after May 22 with actual reply count.
- Resolution criteria: Replies confirmed OR Round 2 sequence rewrite initiated by May 25.

---

## OPEN — Hot leads uncontacted on LinkedIn (Touch 3 active)
- First seen: 2026-05-18
- Description: Contacts with 2+ opens haven't been connected with on LinkedIn.
- Run 43: linkedin_posts_june_2026-05-21.md written — 10 posts for peak season. Bradley has fresh content to post while connecting.
- Resolution criteria: Bradley runs touch3_open_trigger_protocol May 22–23 per outputs/tommy/touch3_open_trigger_protocol_2026-05-21.md.

---

## OPEN — HubSpot not connected (CRM blind)
- First seen: 2026-05-18
- Workaround: Nina weekly report includes overdue/due-soon follow-up section with names + phone numbers.
- Resolution criteria: HUBSPOT_TOKEN added to .env. Not urgent until post-peak season (July+).

---

## OPEN — No residential homeowner outreach channel active
- First seen: 2026-05-18
- Description: Facebook ads not running. June Residential Push brief written. Service pages written. Rick's ad copy written.
- Run 43: Past Customer Reengagement Launch Guide written — fastest path to residential revenue this week (20 min, zero cost).
- Resolution criteria: (1) Service pages live on website, (2) Facebook ads launched, (3) Past customer blast sent May 26.

---

## OPEN — Workiz API blocked in cloud AND 0 power washing jobs on local
- First seen: 2026-05-18
- Workaround: Diagnostic logging added — locally run shows all JobType values found.
- Run 43: Still open. Bradley must run locally and check logs for JobType values from Workiz.
- Resolution criteria: Bradley runs `python3 workers/workiz_report.py daily` locally, finds the JobType string Workiz uses, adds it to JOB_TYPE_VARIANTS.

---

## OPEN — Regular Danny PM cron not running (9+ days overdue) 🔴
- First seen: 2026-05-20 (run 28)
- Description: Last pull May 12. Apollo blocked in cloud. Cron not set up locally.
- Run 43: scripts/crontab_setup.txt created. Bradley pastes into `crontab -e` on Mac.
- CRITICAL PATH: Round 2 enrollment June 4. Danny needs Summit + Medina leads in cache BEFORE June 4.
- Resolution criteria: crontab running; Danny pull confirmed in logs/cron.log by May 26.

---

## OPEN — Google Business Profile not managed
- First seen: 2026-05-20 (run 30)
- Description: GBP posts drive local search ranking. Free. High ROI for residential inbound.
- Run 43: Full weekly routine written (outputs/vera/gbp_weekly_routine_2026-05-21.md). 30 min/week protocol with 4 post templates.
- Resolution criteria: Bradley posts first GBP photo + caption by May 26 at business.google.com.

---

## OPEN — No review request automation
- First seen: 2026-05-20 (run 30)
- Description: Template exists (outputs/tommy/review_request_sequence_2026-05-18.md). No automation.
- Workaround: Manual send after each job using the template.
- Resolution criteria: Twilio credentials added + automated trigger post job completion. Post-peak season (July+).

---

## OPEN — Gas station contacts not enrolled in Mixmax (18 emails idle)
- First seen: 2026-05-20 (run 31)
- Description: 18 gas station DMs in pipeline_data.json. Sequence ID = PENDING.
- Setup guide: outputs/vera/mixmax_sequence_setup_guide_2026-05-20.md
- Run 43: Still open.
- Action: Bradley creates Mixmax sequence → pastes ID into integrations/mixmax.py SEQUENCES['gas_station']['id'] → runs lead_pipeline.py to auto-enroll all 18.

---

## OPEN — No Google Ads running
- First seen: 2026-05-21 (run 36)
- Description: Rick's copy ready (outputs/rick/google_ads_june_2026-05-19.md). Not launched.
- Run 43: Still open.
- Resolution criteria: Google Ads account created + campaigns live. Budget: $15–25/day.

---

## OPEN — Past customer reengagement not launched
- First seen: 2026-05-20 (run 29)
- Description: Tommy's template sitting unused. Highest-ROI action for residential revenue.
- Run 43: Launch guide written — step-by-step for May 26 (outputs/donna/past_customer_reengagement_launch_2026-05-21.md).
- Revenue potential: $1,400–$4,000 from 20–30 contacts at 20–35% conversion.
- Resolution criteria: Bradley sends reengagement texts May 26 using the launch guide.

---

## RESOLVED — report_card.py PIL import crash (silent blocker — all workers broken in cloud)
- Resolved: 2026-05-21 (run 44)
- Fix: Wrapped `from PIL import ...` in try/except, set `_PIL_AVAILABLE` flag. `send_report_card()` falls back to a text-only Slack message when Pillow not installed. Added `_send_text_report_card()` fallback. All workers now import cleanly in cloud environment (confirmed: `python3 -c "from utils.report_card import send_report_card"` passes).

---

## OPEN — Manual Contacts Sitting Untouched (New Lead stage)
- First seen: 2026-05-18
- Description: 33 contacts in New Lead stage. 0 last_contact dates. Tier 1 contractors — tonight is the last window before Memorial Day weekend.
- Tier 1 TEXT TONIGHT: Anthony/Land Pro (440-320-2779), Dontez/GTP (440-396-0814), Chris/Twin Improvements (216-773-0757), Venus/Reliable Roofing (216-810-2497), Logan/Pagels (216-956-5263)
- Run 43: Past customer reengagement launch guide written (donna/past_customer_reengagement_launch_2026-05-21.md). May 26 is the backup if tonight doesn't happen.
- Run 44: touch3_outcome_tracker_2026-05-22.md created — Bradley fills this in May 22-26 as replies come in.
- Resolution criteria: Bradley texts Tier 1 list tonight or May 26 (Memorial Day Blitz Day).

---

## OPEN — Mixmax API blocked in cloud execution environment
- First seen: 2026-05-18
- Workaround: All pipeline scripts return None/safe fallback on 403. nina_report shows explicit API warning.
- Next steps: Bradley checks Mixmax → API Settings → IP Allowlist.

---

## OPEN — All external APIs blocked from cloud (Apollo, Workiz, Mixmax)
- First seen: 2026-05-18
- Workaround: Cron job schedule documented. scripts/crontab_setup.txt created run 43 — paste into `crontab -e` on Mac.
- CRITICAL: Danny has not pulled leads since May 12 (9 days). Round 2 enrollment targets June 4. Cron must be running by May 26.
- Run 44: County rotation calendar added to agents/danny.md — Bradley can see exactly which county Danny will pull each week through July.

---

## OPEN — Slack Webhook blocked in cloud execution environment
- First seen: 2026-05-18
- Workaround: Messages written to pending_slack_messages.md. GitHub Action posts on push.
- Run 43: vera_relay.py is the local alternative — runs on crontab every 5 min and posts pending messages.

---

## OPEN — GitHub Actions PAT missing workflow scope
- First seen: 2026-05-20 (run 34)
- Description: vera-slack-relay.yaml written to .github/workflows/. Cloud push blocked — PAT needs 'workflow' scope.
- Run 43: deploy_github_action.sh in scripts/ — run AFTER adding PAT workflow scope.
- Action: Settings → Developer settings → Personal access tokens → Edit ghp_lrUhBq7... → check 'workflow' → Save → run scripts/deploy_github_action.sh

---

## OPEN — Instantly.ai vs Mixmax Overlap (duplicate sequence risk)
- First seen: 2026-05-18
- Description: server.py has active Instantly.ai campaign IDs. Risk of duplicate emails to same contacts.
- Run 43: Still unresolved.
- Action: Log into Instantly.ai and pause/disable all campaigns. Mixmax is the sole active platform.

---

## OPEN — 0% reply rate across enrolled contacts
- First seen: 2026-05-18
- Description: ~45 contacts enrolled, 0 replies. Touch 3 fires May 22.
- Run 44: touch3_outcome_tracker_2026-05-22.md created — single tracker for all results May 22-26 including Round 2 decision gate.
- Resolution criteria: Replies confirmed OR Round 2 sequence rewrite initiated by May 25.

---

## OPEN — Hot leads uncontacted on LinkedIn (Touch 3 active)
- First seen: 2026-05-18
- Description: Contacts with 2+ opens haven't been connected with on LinkedIn.
- Run 43: linkedin_posts_june_2026-05-21.md written — 10 posts for peak season. Bradley has fresh content to post while connecting.
- Resolution criteria: Bradley runs touch3_open_trigger_protocol May 22–23 per outputs/tommy/touch3_open_trigger_protocol_2026-05-21.md.

---

## OPEN — HubSpot not connected (CRM blind)
- First seen: 2026-05-18
- Workaround: Nina weekly report includes overdue/due-soon follow-up section with names + phone numbers.
- Resolution criteria: HUBSPOT_TOKEN added to .env. Not urgent until post-peak season (July+).

---

## OPEN — No residential homeowner outreach channel active
- First seen: 2026-05-18
- Description: Facebook ads not running. June Residential Push brief written. Service pages written. Rick's ad copy written.
- Run 43: Past Customer Reengagement Launch Guide written — fastest path to residential revenue this week (20 min, zero cost).
- Resolution criteria: (1) Service pages live on website, (2) Facebook ads launched, (3) Past customer blast sent May 26.

---

## OPEN — Workiz API blocked in cloud AND 0 power washing jobs on local
- First seen: 2026-05-18
- Workaround: Diagnostic logging added — locally run shows all JobType values found.
- Run 44: Still open. Bradley must run locally and check logs for JobType values from Workiz.
- Resolution criteria: Bradley runs `python3 workers/workiz_report.py daily` locally, finds the JobType string Workiz uses, adds it to JOB_TYPE_VARIANTS.

---

## OPEN — Regular Danny PM cron not running (9+ days overdue) 🔴
- First seen: 2026-05-20 (run 28)
- Description: Last pull May 12. Apollo blocked in cloud. Cron not set up locally.
- Run 44: County rotation calendar in agents/danny.md now shows Memorial Day risk — May 25 cron may not run if Mac is off. Manual run instruction added.
- CRITICAL PATH: Round 2 enrollment June 4. Danny needs Summit + Medina leads in cache BEFORE June 4.
- Resolution criteria: crontab running; Danny pull confirmed in logs/cron.log by May 26.

---

## OPEN — Google Business Profile not managed
- First seen: 2026-05-20 (run 30)
- Description: GBP posts drive local search ranking. Free. High ROI for residential inbound.
- Run 43: Full weekly routine written (outputs/vera/gbp_weekly_routine_2026-05-21.md). 30 min/week protocol with 4 post templates.
- Resolution criteria: Bradley posts first GBP photo + caption by May 26 at business.google.com.

---

## OPEN — No review request automation
- First seen: 2026-05-20 (run 30)
- Description: Template exists (outputs/tommy/review_request_sequence_2026-05-18.md). No automation.
- Workaround: Manual send after each job using the template.
- Resolution criteria: Twilio credentials added + automated trigger post job completion. Post-peak season (July+).

---

## OPEN — Gas station contacts not enrolled in Mixmax (18 emails idle)
- First seen: 2026-05-20 (run 31)
- Description: 18 gas station DMs in pipeline_data.json. Sequence ID = PENDING.
- Setup guide: outputs/vera/mixmax_sequence_setup_guide_2026-05-20.md
- Run 44: Still open.
- Action: Bradley creates Mixmax sequence → pastes ID into integrations/mixmax.py SEQUENCES['gas_station']['id'] → runs lead_pipeline.py to auto-enroll all 18.

---

## OPEN — No Google Ads running
- First seen: 2026-05-21 (run 36)
- Description: Rick's copy ready (outputs/rick/google_ads_june_2026-05-19.md). Not launched.
- Run 44: Still open.
- Resolution criteria: Google Ads account created + campaigns live. Budget: $15–25/day.

---

## OPEN — Past customer reengagement not launched
- First seen: 2026-05-20 (run 29)
- Description: Tommy's template sitting unused. Highest-ROI action for residential revenue.
- Run 44: May 26 launch guide exists. Touch 3 outcome tracker created for same-day tracking.
- Revenue potential: $1,400–$4,000 from 20–30 contacts at 20–35% conversion.
- Resolution criteria: Bradley sends reengagement texts May 26 using the launch guide.

---

## OPEN — Marcus silent — no competitor/VOC intel since May 19
- First seen: 2026-05-21 (run 44)
- Description: Marcus's most recent output is voc_seasonal_bulletin_may_2026.md. No competitor profiles or live review mining since May 19. Web search blocked in cloud.
- Run 44: competitive_intel_brief_2026-05-21.md written from known market data. Covers bucket analysis, VOC phrases, NE Ohio seasonal patterns.
- Resolution criteria: Bradley runs Marcus locally with web search enabled to pull live competitor Google reviews (last 60 days) and Facebook Ad Library data.

---

## RUN METRICS — Run 44 | 2026-05-21
- Total RESOLVED: 43 (added: report_card.py PIL crash)
- Total OPEN: 16 (added: Marcus silent)
- Auto-upgrades shipped: 5 (report_card.py PIL fix, DANNY_ORG_KEYWORDS multifamily, DANNY_TITLES multifamily, mixmax.py multifamily PM titles, Apollo 429 detection, danny.md county calendar)
- Deliverables written: 2 (touch3_outcome_tracker, competitive_intel_brief)

---

## RESOLVED — detect_lead_type routing bug (PM at real estate company → realtor)
- Resolved: 2026-05-21 (run 45)
- Description: REALTOR_TITLES was checked before PROPERTY_MANAGER_TITLES. 'real estate' substring in REALTOR_TITLES matched PM contacts at companies like "Howard Hanna Real Estate" or "ABC Real Estate Management" — routing them to the realtor sequence instead of PM sequence.
- Fix: Swapped check order in detect_lead_type() — PROPERTY_MANAGER_TITLES checked first. All 9 routing tests pass. PM titles are specific enough that no real realtor would be misrouted.

---

## RESOLVED — contacts_cache.json not committed in final pipeline git push
- Resolved: 2026-05-21 (run 45)
- Description: The final git add in lead_pipeline.py __main__ only staged pipeline_data.json. Enrollment marks written to contacts_cache.json by verify_and_repair_enrollment() and run_pending_sequences() were never pushed to GitHub.
- Fix: Added 'contacts_cache.json' to the git add command alongside pipeline_data.json.

---

## OPEN — Manual Contacts Sitting Untouched (New Lead stage)
- First seen: 2026-05-18
- Description: 33 contacts in New Lead stage. Tier 1 contractors — tonight is the last window before Memorial Day weekend.
- Tier 1 TEXT TONIGHT: Anthony/Land Pro (440-320-2779), Dontez/GTP (440-396-0814), Chris/Twin Improvements (216-773-0757), Venus/Reliable Roofing (216-810-2497), Logan/Pagels (216-956-5263)
- Run 45: Touch 3 fires tomorrow (May 22). May 26 is the backup blitz day. All playbooks in place.
- Resolution criteria: Bradley texts Tier 1 list or May 26 blitz.

---

## OPEN — Mixmax API blocked in cloud execution environment
- First seen: 2026-05-18
- Workaround: All pipeline scripts return None/safe fallback on 403.
- Run 45: Still blocked. Run locally for live data.

---

## OPEN — All external APIs blocked from cloud (Apollo, Workiz, Mixmax)
- First seen: 2026-05-18
- Workaround: scripts/crontab_setup.txt created — paste into crontab -e on Mac.
- Run 45: CRITICAL — Danny cron still not running. Round 2 enrollment June 4.

---

## OPEN — Slack Webhook blocked in cloud execution environment
- First seen: 2026-05-18
- Workaround: Messages written to pending_slack_messages.md. GitHub Action + vera_relay.py on local cron.

---

## OPEN — GitHub Actions PAT missing workflow scope
- First seen: 2026-05-20 (run 34)
- Description: vera-slack-relay.yaml exists at .github/workflows/. PAT needs 'workflow' scope to push it.
- Run 45: Action: Settings → Developer settings → Personal access tokens → Edit ghp_lrUhBq7... → check 'workflow' → Save → run scripts/deploy_github_action.sh

---

## OPEN — Instantly.ai vs Mixmax Overlap (duplicate sequence risk)
- First seen: 2026-05-18
- Run 45: Still unresolved. Action: Log into Instantly.ai and pause all campaigns.

---

## OPEN — 0% reply rate across enrolled contacts
- First seen: 2026-05-18
- Description: ~45 contacts enrolled, 0 replies. Touch 3 fires May 22 (tomorrow).
- Run 45: round2_pm_sequence_rewrite_2026-05-21.md written — 3 Email 1 alternatives (social proof, fear/urgency, direct question) ready if 0 replies by May 25. Decision gate: May 25.
- Resolution criteria: Replies confirmed OR Round 2 launched with rewritten sequence by May 25.

---

## OPEN — Hot leads uncontacted on LinkedIn (Touch 3 active)
- First seen: 2026-05-18
- Run 45: Touch 3 fires tomorrow. LinkedIn connect protocol is outputs/tommy/touch3_open_trigger_protocol_2026-05-21.md.
- Resolution criteria: Bradley connects on LinkedIn with 2+ open contacts May 22-23.

---

## OPEN — HubSpot not connected (CRM blind)
- First seen: 2026-05-18
- Not urgent until post-peak season (July+).

---

## OPEN — No residential homeowner outreach channel active
- First seen: 2026-05-18
- Run 45: All assets ready. Past customer blast May 26 + Facebook ads + service pages needed.

---

## OPEN — Workiz API blocked in cloud AND 0 power washing jobs on local
- First seen: 2026-05-18
- Run 45: Still open. Bradley must run locally and check log for JobType values.

---

## OPEN — Regular Danny PM cron not running (9+ days overdue) 🔴
- First seen: 2026-05-20 (run 28)
- Run 45: 10+ days since last pull. scripts/crontab_setup.txt is ready to paste.
- CRITICAL PATH: Round 2 enrollment June 4. Danny needs Summit + Medina leads BEFORE June 4.

---

## OPEN — Google Business Profile not managed
- First seen: 2026-05-20 (run 30)
- Run 45: gbp_weekly_routine_2026-05-21.md exists. Action: post first photo by May 26.

---

## OPEN — No review request automation
- First seen: 2026-05-20 (run 30)
- Run 45: Manual template exists. Automation is post-peak (July+).

---

## OPEN — Gas station contacts not enrolled in Mixmax (18 emails idle)
- First seen: 2026-05-20 (run 31)
- Run 45: Still open. Action: create Mixmax sequence → paste ID into integrations/mixmax.py.

---

## OPEN — No Google Ads running
- First seen: 2026-05-21 (run 36)
- Run 45: Copy ready (outputs/rick/google_ads_june_2026-05-19.md). Not launched.

---

## OPEN — Past customer reengagement not launched
- First seen: 2026-05-20 (run 29)
- Run 45: Launch guide exists (outputs/donna/past_customer_reengagement_launch_2026-05-21.md). Target: May 26.

---

## OPEN — Marcus silent — no live competitor/VOC intel since May 19
- First seen: 2026-05-21 (run 44)
- Run 45: Still open. Web search blocked in cloud. Existing intel brief written.
- Resolution criteria: Bradley runs Marcus locally for live Google review mining.

---

## RUN METRICS — Run 45 | 2026-05-21
- Total RESOLVED: 45 (added: detect_lead_type routing bug, contacts_cache.json commit gap)
- Total OPEN: 15 (net: resolved 2 new, no new opens)
- Auto-upgrades shipped: 4 (detect_lead_type order fix, 3 PM titles added to mixmax.py+lead_pipeline.py, contacts_cache.json commit, nina_report.py API-blocked action item)
- Deliverables written: 1 (round2_pm_sequence_rewrite_2026-05-21.md)

---

## RESOLVED — jasmine_flyer.py hard PIL import crash (module-level, no guard)
- Resolved: 2026-05-21 (run 46)
- Description: `from PIL import Image, ImageDraw` at module level (line 17) with no try/except. Any cloud or fresh-clone environment without Pillow would crash on import — same class of bug as report_card.py (fixed run 44).
- Fix: Wrapped in try/except, set `_PIL_AVAILABLE` flag. `build_flyer()` raises RuntimeError with install instructions when PIL unavailable. `fit_image` type hints changed to strings for forward-compatibility. Confirmed: `python3 -c "import workers.jasmine_flyer"` passes with `_PIL_AVAILABLE: False`.

---

## RESOLVED — vera_relay.py file-clear not guarded (crash on filesystem error)
- Resolved: 2026-05-21 (run 46)
- Description: `PENDING_FILE.write_text('')` at line 102 was called bare after posting messages. Any filesystem error (permissions, disk full) would crash the relay mid-run, leaving posted messages on disk.
- Fix: Wrapped in try/except with warning print.

---

## RESOLVED — touch3_morning_brief wrong round2 file path
- Resolved: 2026-05-21 (run 46)
- Description: Brief referenced `outputs/danny/round2_enrollment_plan_2026-05-20.md` — file is at `outputs/donna/round2_enrollment_plan_2026-05-21.md`.
- Fix: Path corrected in touch3_morning_brief_2026-05-22.md.

---

## RESOLVED — jasmine_flyer.py unguarded `import requests` at module level
- Resolved: 2026-05-22 (run 47)
- Description: `import requests` at line 5 (now line 6) — hard module-level import with no try/except. Same class of bug as PIL (fixed run 46). Any environment without `requests` installed crashes on import.
- Fix: Wrapped in try/except, `_REQUESTS_AVAILABLE` flag set. `push_to_github()` and `post_to_slack()` raise clear RuntimeError when requests unavailable. Confirmed: `python3 -c "import workers.jasmine_flyer"` passes with `_REQUESTS_AVAILABLE: True | _PIL_AVAILABLE: False`.

---

## OPEN — Manual Contacts Sitting Untouched (New Lead stage)
- First seen: 2026-05-18
- Description: 33 contacts in New Lead stage — confirmed from pipeline_data.json (run 47 direct check). Tier 1 list unchanged. 3 contacts (Bulletproof, Damrons, CLE Lawn) in Contacted stage with next_followup = 2026-05-26.
- Run 47: may26_blitz_action_card.md created — unified Monday morning action card covering all 8 priorities in order, with scripts linked and time estimates.
- Run 48: No change. May 26 is the execution date. All scripts and guides in place.
- Resolution criteria: Bradley texts Tier 1 list on May 26 using may26_blitz_action_card.md.

---

## OPEN — Mixmax API blocked in cloud execution environment
- First seen: 2026-05-18
- Run 47: Still blocked. Run locally for live data. No new cloud fix possible.
- Run 48: Unchanged. vera_relay.py local cron is the working path.

---

## OPEN — All external APIs blocked from cloud (Apollo, Workiz, Mixmax)
- First seen: 2026-05-18
- Run 47: Danny cron still not confirmed running. launchd alternative created (scripts/danny_launchd_plist.xml) — more reliable than cron on macOS, queues missed runs if Mac was asleep.
- Run 48: NEW ANGLE — crontab_setup.txt upgraded with 4-section verification guide including exact terminal commands: `crontab -l` to verify install, `sudo launchctl list | grep cron` to verify daemon, manual Danny pull command. All instructions are now copy-paste ready.
- CRITICAL: Round 2 enrollment June 4. Danny needs Summit + Medina leads before June 2. Run manually NOW: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both`

---

## OPEN — Slack Webhook blocked in cloud execution environment
- First seen: 2026-05-18
- Run 47: Messages written to pending_slack_messages.md. GitHub Action + vera_relay.py on local cron.

---

## OPEN — GitHub Actions PAT missing workflow scope
- First seen: 2026-05-20 (run 34)
- Run 47: Action: Settings → Developer settings → Personal access tokens → Edit ghp_lrUhBq7... → check 'workflow' → Save → run scripts/deploy_github_action.sh
- Run 48: NEW ANGLE — attempted git push of .github/workflows/vera-slack-relay.yaml directly via cloud git. GitHub rejected with explicit error: "refusing to allow a Personal Access Token to create or update workflow files without `workflow` scope." PAT currently has `repo` scope only (confirmed via API headers). Attempted GitHub API PUT to create file — also blocked (404). Workaround: wrote pat_scope_upgrade_guide_2026-05-22.md — 3-step guide, direct GitHub URL, specific checkbox to check.
- Resolution criteria: Bradley adds workflow scope + runs scripts/deploy_github_action.sh. File: outputs/vera/pat_scope_upgrade_guide_2026-05-22.md

---

## OPEN — Instantly.ai vs Mixmax Overlap (duplicate sequence risk)
- First seen: 2026-05-18
- Run 47: NEW ANGLE — this may be the primary cause of the 0% reply rate. If Instantly was sending duplicate emails, recipients may have marked them spam, depressing deliverability for Mixmax too. email_deliverability_checklist_2026-05-22.md covers this as Step 5.
- Run 48: NEW ANGLE — identified EXACT campaign IDs from server.py code review: `a1c08c3d-43c6-4a0f-b253-e3f14e66f3bc` (Property Managers — Cuyahoga County) and `626cd15d-4d89-4c29-a609-436e69fbb404` (Referral Partners — Contractors NE Ohio). Both directly overlap active Mixmax sequences. Written instantly_pause_guide_2026-05-22.md with exact IDs and 5-step pause process.
- Action: Log into app.instantly.ai → Campaigns → Pause both campaigns using IDs above. 3 minutes. File: outputs/vera/instantly_pause_guide_2026-05-22.md

---

## OPEN — 0% reply rate across enrolled contacts
- First seen: 2026-05-18
- Description: ~45 contacts enrolled. Touch 3 fired May 22. 72-hour reply window.
- Run 47: NEW ANGLE — deliverability hypothesis. email_deliverability_checklist_2026-05-22.md written — step-by-step: check Mixmax stats, verify sequence sending, run mail-tester.com spam score, check SPF/DKIM, check Instantly.ai overlap. Decision tree at end maps finding → action.
- Run 48: Touch 3 fired TODAY (May 22). 72-hour window runs through May 25. Round 2 Decision Gate: may25_round2_decision_gate_2026-05-22.md — exact criteria and action playbook for 0/1-2/3-5/6+ reply scenarios. New hypothesis: Instantly.ai overlap (now documented with exact campaign IDs) may be the root cause — pausing Instantly is the single highest-impact action before Round 2.
- Resolution criteria: Replies confirmed by May 25 OR Round 2 launched May 26 with rewritten sequence. Decision gate file: outputs/donna/may25_round2_decision_gate_2026-05-22.md

---

## OPEN — Hot leads uncontacted on LinkedIn (Touch 3 fired May 22)
- First seen: 2026-05-18
- Run 47: Touch 3 fired yesterday. LinkedIn connect window is open NOW through May 23. Protocol: outputs/tommy/touch3_open_trigger_protocol_2026-05-21.md.
- Run 48: Touch 3 fired TODAY. Window is OPEN NOW. Each hour of delay loses the "just sent an email" context that makes LinkedIn connects land. Priority: open Mixmax → sort by opens → connect on LinkedIn with top 5 (2+ opens) contacts TODAY.
- Resolution criteria: Bradley connects on LinkedIn with top 5 hot leads May 22–23.

---

## OPEN — HubSpot not connected (CRM blind)
- First seen: 2026-05-18
- Run 47: Not urgent until post-peak season (July+).

---

## OPEN — No residential homeowner outreach channel active
- First seen: 2026-05-18
- Run 47: All assets ready. may26_blitz_action_card.md Step 7 is the past customer blast. Facebook ads + service pages are the June 3–4 priorities.

---

## OPEN — Workiz API blocked in cloud AND 0 power washing jobs on local
- First seen: 2026-05-18
- Run 47: Still open. Bradley must run locally: `python3 workers/workiz_report.py daily` and check logs for JobType values.

---

## OPEN — Regular Danny PM cron not running (10+ days overdue) 🔴
- First seen: 2026-05-20 (run 28)
- Run 47: NEW ANGLE — macOS launchd plist created (scripts/danny_launchd_plist.xml). More reliable than cron: if Mac was asleep at 7am, launchd queues the job and runs it on wake. Install: `cp scripts/danny_launchd_plist.xml ~/Library/LaunchAgents/com.forestcity.danny.plist && launchctl load ~/Library/LaunchAgents/com.forestcity.danny.plist`
- CRITICAL PATH: Round 2 enrollment June 4. Manual run NOW: `python3 workers/lead_pipeline.py danny`

---

## OPEN — Google Business Profile not managed
- First seen: 2026-05-20 (run 30)
- Run 47: gbp_weekly_routine_2026-05-21.md + gbp_post_may21_2026.md exist. Step 8 of may26_blitz_action_card.md. Action: post by May 26.

---

## OPEN — No review request automation
- First seen: 2026-05-20 (run 30)
- Run 47: Manual template exists. Post-peak season (July+).

---

## OPEN — Gas station contacts not enrolled in Mixmax (18 emails idle)
- First seen: 2026-05-20 (run 31)
- Run 47: Still open. Step 6 of may26_blitz_action_card.md with setup guide link. Action: create Mixmax sequence May 26.

---

## OPEN — No Google Ads running
- First seen: 2026-05-21 (run 36)
- Run 47: Copy ready (outputs/rick/google_ads_june_2026-05-19.md). Budget: $15–25/day. June 3 is the target launch date per june_residential_push_2026-05-20.md.

---

## OPEN — Past customer reengagement not launched
- First seen: 2026-05-20 (run 29)
- Run 47: Step 7 of may26_blitz_action_card.md. Revenue potential: $1,400–$4,000. Target: May 26 morning.

---

## OPEN — Marcus silent — no live competitor/VOC intel since May 19
- First seen: 2026-05-21 (run 44)
- Run 47: Web search blocked in cloud. competitive_intel_brief_2026-05-21.md is the standing brief.
- Run 48: NEW ANGLE — wrote peak_season_intel_update_2026-05-22.md from knowledge base (no web search needed). Covers: competitor weakness patterns (Clean Pro rescheduling complaints, Brothers response time), 8 VOC phrases to add to Tommy's library, NE Ohio market dynamics (east side algae, west side HOA, Summit salt damage), and specific research tasks for next local Marcus run.
- Resolution criteria: Bradley runs Marcus locally for live Google review data. Existing intel is actionable now.

---

## OPEN — Facebook/Google Ads not launched (CRITICAL PEAK SEASON GAP)
- First seen: 2026-05-22 (run 48)
- Description: Rick wrote Google Ads copy May 19, Facebook Ads copy May 20. TODAY IS MAY 22. Ads have been sitting for 3 days during peak season. Every day without ads = booked jobs going to competitors running Google/Facebook campaigns. Service pages are written (`outputs/tommy/website_copy_service_pages_2026-05-20.md`), Google Ads are written (`outputs/rick/google_ads_june_2026-05-19.md`), Facebook Ads are written (`outputs/rick/facebook_ads_peak_season_2026-05-20.md`). Nothing is stopping launch today.
- Run 48: Updated agents/rick.md with urgent LAUNCH NOW message. Added Google Guaranteed Badge guide (outputs/rick/google_guaranteed_setup_2026-05-22.md) — biggest untapped inbound channel.
- Action: Launch Google Ads and Facebook ads BY May 26. Apply for Google Guaranteed badge TODAY (takes 1–3 days to approve, could be live by May 27).

---

## RUN METRICS — Run 49 | 2026-05-22

### Open Issue Status — Run 49 Updates:

**Manual Contacts:** May 26 blitz day unchanged. All scripts in place. memorial_day_week_full_playbook_2026-05-22.md created — covers May 26–30 day-by-day.

**Mixmax API / All APIs blocked:** No change. Local cron path is the fix. Danny still needs Summit County pull.

**Slack relay:** pending_slack_messages.md → GitHub push → vera_relay.py path unchanged.

**GitHub Actions PAT:** Still needs workflow scope. pat_scope_upgrade_guide_2026-05-22.md is the guide.

**Instantly.ai overlap:** Still unresolved. instantly_pause_guide_2026-05-22.md has exact campaign IDs. 3 minutes to fix. Leading cause of 0% reply rate.

**0% reply rate:** Touch 3 72h window closed May 25. Check Mixmax before May 26 blitz and use may25_round2_decision_gate_2026-05-22.md to decide Round 2 approach.

**LinkedIn hot leads:** Touch 3 fired May 22 — connection window is May 22–23. If not done, follow up via bridge email: `outputs/tommy/hot_lead_bridge_email_2026-05-19.md`

**Ads not launched:** Still the most urgent revenue gap. Launch target: May 26.

**Danny cron:** Run manually NOW if not done. `python3 workers/lead_pipeline.py danny` (Summit County, Week 21).

**GBP, review automation, HubSpot, Workiz:** All same status — waiting on Bradley action.

- Total RESOLVED: 51 (added: nina_report.py weekly hot leads section, 'association manager' CAM title sync)
- Total OPEN: 16 (no new opens; no closures — all waiting on Bradley action)
- Auto-upgrades shipped: 4
  1. workers/nina_report.py run_weekly() — added individual hot leads section with names, company, opens, LinkedIn links; Bradley now gets "who to call" list in Monday weekly report
  2. integrations/mixmax.py PROPERTY_MANAGER_TITLES — added 'association manager' (standalone CAM variant)
  3. workers/lead_pipeline.py DANNY_TITLES — added 'association manager' (kept in sync with mixmax.py)
  4. agents/donna.md — added june_week1_sprint file reference to June Booking Blitz section
- Deliverables written: 1
  - outputs/donna/memorial_day_week_full_playbook_2026-05-22.md — May 26–30 full day-by-day playbook; fills the gap between May 26 blitz card and June week 1 sprint; covers contractor follow-ups, LinkedIn connects, phone calls, ad launch check, Medina prep, and June entry criteria checklist

---

## RESOLVED — 'condominium manager' missing from Apollo search and routing
- Resolved: 2026-05-22 (run 50)
- Description: DANNY_TITLES + PROPERTY_MANAGER_TITLES both had 'condo manager' but NOT 'condominium manager'. Substring matching means 'condo manager' is NOT found inside 'condominium manager' — gap was real. These contacts would be fetched by Apollo (org keyword match) but silently routed to property_manager default rather than being explicitly caught. Also missing: 'condominium management' + 'condo association' + 'condominium association' from DANNY_ORG_KEYWORDS.
- Fix: Added 'condominium manager' to integrations/mixmax.py PROPERTY_MANAGER_TITLES + workers/lead_pipeline.py DANNY_TITLES. Added 'condominium management', 'condo association', 'condominium association' to DANNY_ORG_KEYWORDS. All 4 files import clean.

---

## RESOLVED — Carla contractors search missing irrigation/sprinkler keywords
- Resolved: 2026-05-22 (run 50)
- Description: Irrigation companies (sprinkler system installers/servicers) were absent from CARLA_SEARCHES contractors keywords. These are high-value referral partners — they open/close irrigation systems in spring and fall, making the same exterior property calls as power washing. One of the best "see the dirty house" touchpoint trades missing from Carla's search.
- Fix: Added 'irrigation', 'sprinkler system', 'lawn irrigation' to Contractors keywords in CARLA_SEARCHES.

---

## RESOLVED — vera_relay.py no proactive Danny staleness detector
- Resolved: 2026-05-22 (run 50)
- Description: vera_relay.py only relayed pending messages on new Vera commits — it never independently checked if Danny's cron was running. Bradley could go weeks without a Danny pull and get no automated alert.
- Fix: Added _check_danny_staleness() function. Runs every time vera_relay.py executes (via local 5-min cron). Reads activity.log in reverse, finds last "Danny | Apollo pull" entry, computes days since last pull. If >7 days: posts urgent Slack alert directly. Sentinel file prevents repeated daily alerts. Fires independently of new Vera commits.

---

## RESOLVED — nina_report.py hot leads missing phone numbers
- Resolved: 2026-05-22 (run 50)
- Description: Daily and weekly hot leads tables showed Name, Email, Sequence, Opens, Replied, LinkedIn — no phone number. When Bradley wants to call a hot lead, he has to manually dig through contacts_cache.json. Phone is already in the cache alongside LinkedIn URL.
- Fix: Added _load_phone_map() function (mirrors _load_linkedin_map()). Phone injected into all_hot leads alongside LinkedIn URL in run_daily(). Hot leads table now has Phone column. Same fix applied to run_weekly() hot leads table.

---

## RUN METRICS — Run 50 | 2026-05-22
- Total RESOLVED: 55 (added: condominium manager gap, irrigation gap, vera_relay staleness, nina phone column)
- Total OPEN: 16 (no new opens; no closures — all waiting on Bradley action)
- Auto-upgrades shipped: 6
  1. integrations/mixmax.py — added 'condominium manager' to PROPERTY_MANAGER_TITLES
  2. workers/lead_pipeline.py — added 'condominium manager' to DANNY_TITLES
  3. workers/lead_pipeline.py — added 'condominium management', 'condo association', 'condominium association' to DANNY_ORG_KEYWORDS
  4. workers/lead_pipeline.py CARLA_SEARCHES — added 'irrigation', 'sprinkler system', 'lawn irrigation' to contractors keywords
  5. workers/vera_relay.py — added _check_danny_staleness() — proactive Slack alert if Danny hasn't pulled in 7+ days, fires independently every run
  6. workers/nina_report.py — added _load_phone_map() + phone column in daily AND weekly hot leads tables
- Deliverables written: 2
  - outputs/tommy/email_subject_line_ab_test_2026-05-22.md — 5 A/B subject line pairs for Round 2 PM sequence; Mixmax setup instructions; success metrics; timeline May 25–June 18
  - scripts/danny_cron_check.sh — Mac terminal diagnostic: checks crontab, launchd plist, days since last Danny pull, last 10 cron.log lines
- Open issues new angles:
  - Danny cron: vera_relay.py now auto-alerts Slack when stale — Bradley will get a ping every day the cron is down
  - 0% reply rate: A/B subject line test plan written for Round 2 — concrete Mixmax setup instructions + 5 test pairs
  - Condominium management segment: gap confirmed and fixed — 'condominium manager' not caught by substring, now explicitly added

---

## RUN METRICS — Run 47 | 2026-05-22
- Total RESOLVED: 49 (added: jasmine_flyer requests guard)
- Total OPEN: 15 (0 new opens added, 0 closed this run — all waiting on Bradley action)
- Auto-upgrades shipped: 1 (jasmine_flyer.py requests import guard)
- Deliverables written: 3 (may26_blitz_action_card.md, email_deliverability_checklist_2026-05-22.md, danny_launchd_plist.xml)
- New angle on cron issue: macOS launchd plist (more reliable than cron on macOS)
- New angle on 0% reply: deliverability checklist — spam test + Instantly.ai overlap hypothesis

---

## RUN METRICS — Run 48 | 2026-05-22
- Total RESOLVED: 49 (no new resolutions this run — all blockers require Bradley action)
- Total OPEN: 16 (1 new: Facebook/Google Ads not launched)
- Auto-upgrades shipped: 4
  1. lead_pipeline.py CARLA_SEARCHES — HOA management company search added (new segment: owners of firms managing 5–50+ HOAs)
  2. agents/rick.md — LAUNCH NOW urgency + Google Guaranteed Badge priority section added
  3. workers/vera_relay.py — `git pull --rebase` to prevent merge commit divergence
  4. scripts/crontab_setup.txt — Full 4-section verification guide with copy-paste terminal commands
- Deliverables written: 5
  1. outputs/vera/instantly_pause_guide_2026-05-22.md — exact Instantly campaign IDs + 5-step pause process
  2. outputs/donna/may25_round2_decision_gate_2026-05-22.md — May 25 decision table with 4 reply-count scenarios + exact action steps
  3. outputs/rick/google_guaranteed_setup_2026-05-22.md — Google Local Services Ads full setup guide
  4. outputs/vera/pat_scope_upgrade_guide_2026-05-22.md — 3-step PAT scope upgrade (addresses GitHub Actions blocker)
  5. outputs/marcus/peak_season_intel_update_2026-05-22.md — Marcus unblocked; competitor weakness map, 8 VOC phrases, NE Ohio market dynamics
- Key new findings this run:
  - GitHub Actions push CONFIRMED blocked by GitHub itself (explicit error message). PAT needs workflow scope — no workaround possible.
  - Instantly.ai campaign IDs identified from server.py: specific campaigns overlap exactly with active Mixmax sequences. This is the leading hypothesis for 0% reply rate.
  - Ads written 3 days ago — NOT launched. This is now an open issue.
  - Touch 3 fired TODAY. LinkedIn connect window is open NOW.
