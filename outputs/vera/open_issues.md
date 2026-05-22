# Vera Cole — Open Issues Tracker
*Updated automatically each run. Only mark RESOLVED after verifying the fix works.*
*Run 52 | 2026-05-22 | Auto-fixes shipped: 4 | New deliverables: 2 | Proposals: 2*

---

## RESOLVED SUMMARY (55 total — details in git history)

Key resolved issues by category:
- **Pipeline routing:** PM-before-realtor check order, gas_station/fleet false positives removed, all 5 PM title variants added (multifamily, CAI, condo, association manager)
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
- Run 52: Touch 3 fired May 22. 72-hour window tracked in `outputs/vera/reply_window_tracker_2026-05-22.md`. Tier 1 contractor texts scripted + ready to send TONIGHT. May 26 is blitz day.
- Resolution criteria: Bradley texts Tier 1 list. Confirmed when pipeline_data.json shows "Contacted" stage for these 5.

---

## OPEN — Mixmax API blocked in cloud execution environment
- First seen: 2026-05-18
- Workaround: All pipeline scripts return safe fallbacks on 403. nina_report shows explicit API warning. `check_replies.py` (new Run 52) is a fast local alternative to full nina_report.
- Run 52: Infrastructure constraint — not fixable from cloud. New check_replies.py worker built so Bradley can run a 30-second reply check any time locally.
- Resolution criteria: Bradley adds cloud IP to Mixmax API allowlist (Mixmax → Settings → API → IP Allowlist).

---

## OPEN — All external APIs blocked from cloud (Apollo, Workiz, Mixmax)
- First seen: 2026-05-18
- Workaround: scripts/crontab_setup.txt ready to paste into crontab -e. scripts/danny_launchd_plist.xml as Mac alternative. scripts/danny_cron_check.sh for diagnostics. check_replies.py added to crontab (8:45am weekdays).
- Run 52: Danny cron has been down since May 12 (10 days). Round 2 enrollment June 4 = 13 days away. This is the most time-sensitive action item in the office. Manual run command: `python3 workers/lead_pipeline.py both`
- Resolution criteria: crontab -l shows Danny cron entry AND logs/cron.log confirms pull by May 26.

---

## OPEN — Slack Webhook blocked in cloud execution environment
- First seen: 2026-05-18
- Workaround: Messages written to pending_slack_messages.md. GitHub Action fires on every Vera push and posts content to Slack. vera_relay.py on local cron provides 5-min delivery.
- Run 52: Relay working. Permanent constraint, not a fixable bug. check_replies.py also posts to Slack on local run.

---

## OPEN — GitHub Actions PAT missing workflow scope
- First seen: 2026-05-20 (run 34)
- Description: vera-slack-relay.yaml and github_action_vera_slack_relay.yaml exist in outputs/vera/ but can't be pushed to .github/workflows/ — PAT needs 'workflow' scope.
- Run 52: Still blocked. Guide written: outputs/vera/pat_scope_upgrade_guide_2026-05-22.md. 3-step fix takes 2 minutes.
- Action: Settings → Developer settings → Personal access tokens → Edit ghp_lrUhBq7... → check 'workflow' → Save

---

## OPEN — Instantly.ai vs Mixmax Overlap (0% reply rate root cause) 🔴
- First seen: 2026-05-18
- Description: Two active Instantly.ai campaigns (a1c08c3d = PM Cuyahoga, 626cd15d = Contractor Referral) run against the same contacts as Mixmax sequences → duplicate emails → spam filtering → 0 replies.
- Run 52: Touch 3 fired May 22. Pause guide: outputs/vera/instantly_pause_guide_2026-05-22.md — 3-minute fix. MUST pause TONIGHT before Reply-To check runs tomorrow. CRITICAL: Must pause before Round 2 enrollment (June 4) or the same problem repeats.
- Resolution criteria: Both campaigns paused in Instantly.ai → confirmed by Bradley.

---

## OPEN — 0% reply rate across enrolled contacts
- First seen: 2026-05-18
- Description: ~45 contacts enrolled, 0 replies across all 3 email touches.
- Run 52: Touch 3 fired TODAY (May 22). 72-hour reply window tracked in reply_window_tracker_2026-05-22.md. New `check_replies.py` makes it easy to monitor daily. Decision gate May 25. Round 2 rewrite ready. Three levers: (1) Pause Instantly.ai TONIGHT, (2) verify Reply-To in Mixmax, (3) rewrite Email 1 for Round 2.
- Resolution criteria: At least 1 confirmed reply before May 25 OR Round 2 rewrite + enrollment launched by June 4.

---

## OPEN — Hot leads not contacted on LinkedIn (Touch 3 day)
- First seen: 2026-05-18
- Description: ~13 contacts with 2+ opens haven't received personal LinkedIn connects.
- Run 52: Touch 3 fired today — connect NOW while "just sent you an email" context is live. Protocol: outputs/tommy/touch3_open_trigger_protocol_2026-05-21.md. Delay = lower conversion.
- Resolution criteria: Bradley connects on LinkedIn with top 5+ contacts TODAY.

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
- Run 52: May 26 launch window approaching. Checklist: outputs/vera/may26_ads_launch_checklist_2026-05-22.md. Past customer blast: outputs/donna/past_customer_reengagement_launch_2026-05-21.md. Every day past May 26 is peak-season revenue going to competitors.
- Resolution criteria: (1) Facebook ads live by May 27, (2) past customer blast sent May 26.

---

## OPEN — Workiz API blocked in cloud + 0 power washing jobs showing
- First seen: 2026-05-18
- Workaround: API error sentinel prevents misleading $0 reports. JOB_TYPE_VARIANTS expanded to 22 variants (run 51). Diagnostic logging shows JobType values on local run.
- Run 52: Expanded JOB_TYPE_VARIANTS covers all common naming conventions. If 0 jobs still appear locally, the issue is a non-standard JobType value in Workiz — Bradley needs to check what name was entered for the job type.
- Resolution criteria: Bradley runs `python3 workers/workiz_report.py daily` locally and sees jobs in the report.

---

## OPEN — Danny PM cron not running (10 days overdue) 🔴 CRITICAL
- First seen: 2026-05-20 (run 28)
- Description: Last successful pull: May 12. Apollo blocked in cloud. Cron not set up on Bradley's Mac.
- Run 52: 10 days since last pull. Round 2 enrollment June 4 = 13 days away. Summit County + Medina leads MUST be in cache before June 4. Vera relay now also alerts if Carla pull goes stale 10+ days (added run 52).
- Fresh angle: Manual run is the fastest path. One command, takes 5 minutes, unlocks the whole Round 2 pipeline: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both`
- Resolution criteria: logs/cron.log shows Danny pull entry by May 26.

---

## OPEN — Google Business Profile not managed
- First seen: 2026-05-20 (run 30)
- Description: GBP posts drive local SEO ranking for "power washing [city]" searches. Free channel.
- Run 52: gbp_weekly_routine_2026-05-21.md is the complete protocol (4 post templates, 30 min/week). gbp_post_may21_2026.md has ready-to-post May content.
- Resolution criteria: Bradley posts first GBP photo by May 26 at business.google.com/dashboard.

---

## OPEN — No review request automation
- First seen: 2026-05-20 (run 30)
- Workaround: Manual template at outputs/tommy/review_request_sequence_2026-05-18.md.
- Run 52: Post-peak season priority (July+). Twilio credentials needed for automation.

---

## OPEN — Gas station contacts not enrolled in Mixmax (18 emails idle)
- First seen: 2026-05-20 (run 31)
- Description: 18 gas station district manager contacts pulled May 19. Sequence ID = PENDING.
- Run 52: Sequence copy at outputs/danny/sequence_gas_stations_2026-05-19.md. Setup guide at outputs/vera/mixmax_sequence_setup_guide_2026-05-20.md. These 18 contacts auto-enroll the moment Bradley creates the sequence and pastes the ID into integrations/mixmax.py line 54.

---

## OPEN — Google Ads and Facebook Ads not launched
- First seen: 2026-05-21 (run 36)
- Description: All copy ready (outputs/rick/). Not launched. Peak season revenue being missed daily.
- Run 52: Launch target May 26. Checklist: outputs/vera/may26_ads_launch_checklist_2026-05-22.md. Google Guaranteed setup guide: outputs/rick/google_guaranteed_setup_2026-05-22.md. Every day of delay in peak season costs estimated $100–200 in lost leads.
- Resolution criteria: At least one campaign live by May 27. Confirmed by Bradley in Slack.

---

## OPEN — Past customer reengagement not launched
- First seen: 2026-05-20 (run 29)
- Description: Tommy's text templates ready. Fastest path to residential revenue — zero ad spend.
- Run 52: Launch guide: outputs/donna/past_customer_reengagement_launch_2026-05-21.md. Execute May 26 morning. Revenue potential: $1,400–$4,000 from 20–30 contacts.
- Resolution criteria: Bradley sends texts May 26.

---

## OPEN — Marcus running cloud-only (no live web search)
- First seen: 2026-05-21 (run 44)
- Description: Marcus's competitor profiling requires live web search. Blocked in cloud.
- Run 52: Marcus has competitive_intel_brief_2026-05-21.md and peak_season_intel_update_2026-05-22.md — useful but not real-time. Fresh competitor Google reviews (last 60 days) still missing.
- Resolution criteria: Bradley runs Marcus locally: `claude` CLI → "Marcus, profile top 5 Cleveland power washing competitors."

---

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
