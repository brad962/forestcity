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
