# Vera Cole — Open Issues Tracker
*Updated automatically each run. Only mark RESOLVED after verifying the fix works.*
*Run 51 | 2026-05-22 | Consolidated from duplicate-heavy prior version.*

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
- Run 51: Touch 3 fired today (May 22). May 26 is the definitive blitz day — Tier 1 texts go out then if not already sent. Use contractor_referral_text_script_2026-05-20.md.
- Resolution criteria: Bradley texts Tier 1 list. Confirmed when pipeline_data.json shows "Contacted" stage for these 5.

---

## OPEN — Mixmax API blocked in cloud execution environment
- First seen: 2026-05-18
- Workaround: All pipeline scripts return safe fallbacks on 403. nina_report shows explicit API warning.
- Run 51: Infrastructure constraint — can't fix from cloud. Will always require local run for live data.
- Resolution criteria: Bradley adds cloud IP to Mixmax API allowlist (Mixmax → Settings → API → IP Allowlist).

---

## OPEN — All external APIs blocked from cloud (Apollo, Workiz, Mixmax)
- First seen: 2026-05-18
- Workaround: scripts/crontab_setup.txt ready to paste into crontab -e. scripts/danny_launchd_plist.xml as Mac alternative. scripts/danny_cron_check.sh for diagnostics.
- Run 51: Danny cron has been down since May 12 (10 days). Round 2 enrollment June 4 is 13 days away. This is the most time-sensitive action item in the office.
- Resolution criteria: crontab -l shows Danny cron entry AND logs/cron.log confirms pull by May 26.

---

## OPEN — Slack Webhook blocked in cloud execution environment
- First seen: 2026-05-18
- Workaround: Messages written to pending_slack_messages.md. GitHub Action fires on every Vera push and posts content to Slack. vera_relay.py on local cron provides 5-min delivery.
- Run 51: Relay working. This is a permanent constraint, not a fixable bug.

---

## OPEN — GitHub Actions PAT missing workflow scope
- First seen: 2026-05-20 (run 34)
- Description: vera-slack-relay.yaml and github_action_vera_slack_relay.yaml exist in outputs/vera/ but can't be pushed to .github/workflows/ — PAT needs 'workflow' scope to create/update workflow files.
- Run 51: Still blocked at GitHub API level. Guide written: outputs/vera/pat_scope_upgrade_guide_2026-05-22.md.
- Action: Settings → Developer settings → Personal access tokens → Edit ghp_lrUhBq7... → check 'workflow' → Save → run scripts/deploy_github_action.sh
- Fresh approach tried: Confirmed blocked via both git push and API PUT (404). Only PAT scope change unblocks this.

---

## OPEN — Instantly.ai vs Mixmax Overlap (0% reply rate root cause) 🔴
- First seen: 2026-05-18
- Description: Two active Instantly.ai campaigns (a1c08c3d = PM Cuyahoga, 626cd15d = Contractor Referral) run against the same contacts as Mixmax sequences → contacts getting duplicate emails → spam filtering → 0 replies.
- Run 51: Touch 3 fired today. If reply rate stays at 0%, Instantly overlap is the most probable cause. Pause guide is written: outputs/vera/instantly_pause_guide_2026-05-22.md — 3-minute fix.
- CRITICAL: Must pause before Round 2 enrollment (June 4) or the same problem repeats.
- Resolution criteria: Both campaigns paused in Instantly.ai → confirmed by Bradley. Then Round 2 tests clean.

---

## OPEN — 0% reply rate across enrolled contacts
- First seen: 2026-05-18
- Description: ~45 contacts enrolled, 0 replies across all 3 email touches.
- Run 51: Touch 3 fired TODAY (May 22). 72-hour reply window open until May 25. Round 2 decision gate: outputs/donna/may25_round2_decision_gate_2026-05-22.md. If 0 replies by tonight: start phone calls per outputs/tommy/may23_morning_call_protocol_2026-05-22.md tomorrow 9am.
- Three levers in priority order: (1) Pause Instantly.ai, (2) check Reply-To address in Mixmax, (3) rewrite sequence copy for Round 2.
- Resolution criteria: At least 1 confirmed reply before May 25 OR Round 2 rewrite + enrollment launched by June 4.

---

## OPEN — Hot leads not contacted on LinkedIn (Touch 3 day)
- First seen: 2026-05-18
- Description: ~13 contacts with 2+ opens haven't received personal LinkedIn connects.
- Run 51: Touch 3 fired today — window to connect is NOW (context: "just sent you an email"). Every hour past the send reduces conversion rate. Protocol: outputs/tommy/touch3_open_trigger_protocol_2026-05-21.md.
- Resolution criteria: Bradley connects on LinkedIn with top 5+ contacts TODAY.

---

## OPEN — HubSpot not connected (CRM blind)
- First seen: 2026-05-18
- Workaround: Nina weekly report has overdue/due-soon sections. pipeline_data.json is the manual CRM.
- Run 51: Not urgent. Post-peak season priority (July+).
- Resolution criteria: HUBSPOT_TOKEN added to .env. Estimate setup guide needed from Donna.

---

## OPEN — No residential homeowner outreach channel active
- First seen: 2026-05-18
- Description: Facebook ads not running. June Residential Push brief written. Service pages written. Rick's ad copy written.
- Run 51: May 26 launch window. Ads launch checklist: outputs/vera/may26_ads_launch_checklist_2026-05-22.md (new this run). Past customer blast: outputs/donna/past_customer_reengagement_launch_2026-05-21.md.
- Resolution criteria: (1) Facebook ads live by May 27, (2) past customer blast sent May 26. Service pages can follow.

---

## OPEN — Workiz API blocked in cloud + 0 power washing jobs showing
- First seen: 2026-05-18
- Workaround: API error sentinel prevents misleading $0 reports. Diagnostic logging shows JobType values on local run.
- Run 51 new fix: Added 12 more JobType variants to JOB_TYPE_VARIANTS (roof washing, deck cleaning, concrete cleaning, commercial washing, etc.) — covers more Workiz naming conventions. If 0 jobs persist after this, JobType mismatch is still the cause.
- Resolution criteria: Bradley runs `python3 workers/workiz_report.py daily` locally and sees jobs in the report.

---

## OPEN — Danny PM cron not running (10 days overdue) 🔴 CRITICAL
- First seen: 2026-05-20 (run 28)
- Description: Last successful pull: May 12. Apollo blocked in cloud. Cron not set up on Bradley's Mac.
- Run 51: 10 days since last pull. Round 2 enrollment June 4 = 13 days away. Summit County + Medina leads MUST be in cache before June 4 or Round 2 enrolls zero new contacts.
- All tools ready: scripts/crontab_setup.txt (paste into crontab -e), scripts/danny_launchd_plist.xml (Mac alternative), scripts/danny_cron_check.sh (diagnostic).
- Fresh angle: If crontab setup is too complex, Bradley can run one manual pull right now: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py danny`
- Resolution criteria: logs/cron.log shows Danny pull entry by May 26.

---

## OPEN — Google Business Profile not managed
- First seen: 2026-05-20 (run 30)
- Description: GBP is a free, high-ROI local SEO channel. Posts drive ranking for "power washing [city]" searches.
- Run 51: gbp_weekly_routine_2026-05-21.md is the complete protocol (4 post templates, 30 min/week). gbp_post_may21_2026.md has ready-to-post May content.
- Resolution criteria: Bradley posts first GBP photo by May 26 at business.google.com/dashboard.

---

## OPEN — No review request automation
- First seen: 2026-05-20 (run 30)
- Workaround: Manual template at outputs/tommy/review_request_sequence_2026-05-18.md. Use after each completed job.
- Run 51: Post-peak season priority (July+). Twilio credentials needed.

---

## OPEN — Gas station contacts not enrolled in Mixmax (18 emails idle)
- First seen: 2026-05-20 (run 31)
- Description: 18 gas station district manager contacts pulled May 19. Sequence ID = PENDING — can't enroll until Bradley creates the sequence in Mixmax.
- Run 51: Sequence copy is at outputs/danny/sequence_gas_stations_2026-05-19.md. Setup guide at outputs/vera/mixmax_sequence_setup_guide_2026-05-20.md.
- Action: Create sequence in Mixmax UI → paste ID into integrations/mixmax.py line 54 → run lead_pipeline.py → all 18 auto-enroll.

---

## OPEN — Google Ads and Facebook Ads not launched
- First seen: 2026-05-21 (run 36) + 2026-05-22 (run 48)
- Description: All copy ready (outputs/rick/). Not launched. Peak season revenue being missed daily.
- Run 51: New simplified launch checklist: outputs/vera/may26_ads_launch_checklist_2026-05-22.md. Google Guaranteed setup guide: outputs/rick/google_guaranteed_setup_2026-05-22.md.
- Launch target: May 26. Every day of delay in peak season is revenue going to competitors.
- Resolution criteria: At least one campaign live by May 27. Confirmed by Bradley in Slack.

---

## OPEN — Past customer reengagement not launched
- First seen: 2026-05-20 (run 29)
- Description: Tommy's text templates sitting unused. Fastest path to residential revenue — zero ad spend.
- Run 51: Launch guide at outputs/donna/past_customer_reengagement_launch_2026-05-21.md. 20-minute execution on May 26 morning.
- Revenue potential: $1,400–$4,000 from 20–30 past customers at 20–35% conversion.
- Resolution criteria: Bradley sends texts May 26.

---

## OPEN — Marcus running cloud-only (no live web search)
- First seen: 2026-05-21 (run 44)
- Description: Marcus's competitor profiling and VOC mining requires live web search (Google Maps, Yelp). Web search is blocked in the cloud execution environment.
- Run 51: Marcus has produced competitive_intel_brief_2026-05-21.md and peak_season_intel_update_2026-05-22.md from known market data — not silent, just limited. Fresh competitor Google reviews (last 60 days) still missing.
- Resolution criteria: Bradley runs Marcus locally with web search enabled: `claude` CLI, then "Marcus, profile the top 5 power washing competitors in Cleveland — pull their latest Google Maps reviews."

---

## RUN METRICS — Run 51 | 2026-05-22
- Total RESOLVED: 55
- Total OPEN: 17 (0 new closed, 0 new opened)
- Auto-upgrades shipped: 3 (workiz_report.py JobType variants, tommy.md format entries, donna.md format entries)
- Deliverables written: 2 (may23_morning_call_protocol, may26_ads_launch_checklist)
- Highest priority action: Call top 5 hot leads tomorrow 9am (may23_morning_call_protocol) + Pause Instantly.ai tonight (3 min)
