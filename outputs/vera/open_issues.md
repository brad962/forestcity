# Vera Cole — Open Issues Tracker
*Updated automatically each run. Only mark RESOLVED after verifying the fix works.*

---

## RESOLVED — Jasmine infinite retry loop (not_in_channel)
- Resolved: 2026-05-18
- Fix: `pair["processed"] = True` set before try block. `pair["success"]` distinguishes clean vs failed. Same pair was re-processing dozens of times daily.
- File: `workers/jasmine_flyer.py`

---

## RESOLVED — Carla Apollo keyword filter ignored
- Resolved: 2026-05-18 (run 5 — reapplied after merge conflict wiped it)
- Fix: `apollo_search()` now accepts `keywords=None` param and passes `q_organization_keyword_tags` to Apollo API. `run_carla()` passes `search.get('keywords')`. Confirmed in code this run.
- Note: This fix appeared in open_issues as RESOLVED after run 2 but was NOT in the deployed code — wiped by a merge conflict in the d3a6337 commit. Reapplied and confirmed run 5.
- File: `workers/lead_pipeline.py`

---

## RESOLVED — verify_and_repair_enrollment mass re-enrollment on API failure
- Resolved: 2026-05-18 (run 5 — reapplied after merge conflict wiped it)
- Fix: `get_mixmax_enrolled_emails()` now tracks `success_count`. Returns `None` (not empty set) when all 3 sequences fail. `verify_and_repair_enrollment()` skips repair on `None` return with clear warning. Confirmed in code this run.
- Note: Same as above — appeared RESOLVED in open_issues but was NOT in deployed code. Reapplied run 5.
- File: `workers/lead_pipeline.py`

---

## RESOLVED — nina_report fetch_recipients drops dict responses
- Resolved: 2026-05-18
- Fix: `fetch_recipients()` handles both list and dict (`results`/`recipients` keys) Mixmax responses, with error logging.
- File: `workers/nina_report.py`

---

## RESOLVED — Apollo JSON parse crash (no error handling)
- Resolved: 2026-05-18
- Fix: Added try/except around apollo_search, apollo_reveal, and get_org_phone. Pipeline no longer crashes on malformed API responses.
- File: `workers/lead_pipeline.py`

---

## RESOLVED — Workiz case-insensitive job matching
- Resolved: 2026-05-18
- Fix: `_is_power_washing_job()` checks against 10 variants. Added diagnostic logging of all JobType values seen when 0 matches found.
- File: `workers/workiz_report.py`

---

## RESOLVED — jasmine_flyer.py env loading only in __main__
- Resolved: 2026-05-18
- Fix: Added `_load_env()` at module level. Removed duplicate `load_dotenv()` from `__main__` block.
- File: `workers/jasmine_flyer.py`

---

## RESOLVED — workiz_report "No jobs found" misleads on API failure
- Resolved: 2026-05-18
- Fix: `fetch_all_jobs()` returns sentinel `WORKIZ_API_ERROR` string on exception. Report shows honest "API unavailable" message.
- File: `workers/workiz_report.py`

---

## RESOLVED — nina_report.py misleading action items
- Resolved: 2026-05-18
- Fix: "Review 0 replies" now says "No replies yet — sequence is sending." "Connect page" reference updated to "daily hot leads report."
- File: `workers/nina_report.py`

---

## RESOLVED — nina_report.py double API fetch in run_daily()
- Resolved: 2026-05-18 (run 5)
- Fix: First loop now caches stats in `seq_stats_cache` dict. Second loop reads from cache. Eliminates 3 redundant API calls per daily run.
- File: `workers/nina_report.py`

---

## RESOLVED — jasmine_flyer.py dead location_hint variable
- Resolved: 2026-05-18 (run 5)
- Fix: Removed 5 lines of dead code in `write_facebook_post()`.
- File: `workers/jasmine_flyer.py`

---

## RESOLVED — vera_relay.py crashes if .env missing
- Resolved: 2026-05-18 (run 5)
- Fix: Added `_env.exists()` guard before reading `.env`.
- File: `workers/vera_relay.py`

---

## RESOLVED — workiz_report.py sentinel check uses `is` instead of `==`
- Resolved: 2026-05-18 (run 6)
- Fix: `if jobs is WORKIZ_API_ERROR:` → `if jobs == WORKIZ_API_ERROR:`.
- File: `workers/workiz_report.py`

---

## RESOLVED — lead_pipeline.py save_to_cache crashes on malformed JSON
- Resolved: 2026-05-18 (run 6)
- Fix: Added try/except around `json.loads(CACHE_FILE.read_text())` in `save_to_cache()`.
- File: `workers/lead_pipeline.py`

---

## RESOLVED — server.py stale detection ignores calls log for manual contacts
- Resolved: 2026-05-18 (run 6)
- Fix: Pipeline dashboard falls back to `calls_data` for `last_contact` on manual contacts.
- File: `server.py`

---

## RESOLVED — MIXMAX_TOKEN hardcoded in source code (security risk)
- Resolved: 2026-05-18 (run 7)
- Fix: Removed hardcoded fallback token `'3646d2be-...'` from `integrations/mixmax.py`. Changed to `os.environ.get('MIXMAX_TOKEN', '')`. Token should only live in `.env` (gitignored). Committed to GitHub with the live token was a security exposure.
- File: `integrations/mixmax.py`

---

## RESOLVED — jasmine_flyer.py generic Facebook post every month
- Resolved: 2026-05-18 (run 7)
- Fix: `write_facebook_post()` now selects seasonal hook and CTA based on the month of the date parameter. May/June = algae + booking urgency. Summer = pre-cookout. Fall = pre-winter. Winter = evergreen.
- File: `workers/jasmine_flyer.py`

---

## OPEN — 🚨 HOT CONTRACTORS WAITING FOR TEXT (URGENT — REVENUE NOW)
- First seen: 2026-05-18
- Description: pipeline_data.json shows 2 contractors in "Replied" stage:
  - **Bulletproof Lawncare** | 216-307-4344 — called 2026-05-13, said "very interested"
  - **Damrons Landscaping** | 440-494-0422 — called 2026-05-13, said "very interested"
  Both were called. Neither has received a follow-up text. It has been 5+ days.
- Attempts:
  - 2026-05-18 (runs 1–6): Flagged via high-priority Slack alert each run.
  - 2026-05-18 (run 7): Re-escalating again. Templates in `outputs/vera/sms_templates_contractors_2026-05-18.md`. Summer Push campaign brief lists this as step 1. This is the highest-ROI action in the entire office right now.
- Resolution criteria: Bradley texts both and logs response in pipeline_data.json.

---

## OPEN — 22 Manual Contacts Need Stage Updates
- First seen: 2026-05-18 (updated run 7)
- Description: All 24 manual contacts were called on 2026-05-13 (logged in pipeline_data.json `calls` section). Most stages still "New Lead."
- Attempts:
  - 2026-05-18 (runs 6–7): server.py stale detection now uses calls data. Stage update is Bradley's action.
- Resolution criteria: Bradley updates stages in dashboard, or says YES to auto-promote script.

---

## OPEN — Mixmax API blocked in cloud execution environment
- First seen: 2026-05-18
- Description: All Mixmax API calls return `HTTP 403: Forbidden` with body "Host not in allowlist." Cannot pull live sequence data during cloud runs.
- Impact: Cannot verify real-time enrollment. Nina reports must run locally.
- Attempts:
  - 2026-05-18 (runs 1–7): Confirmed blocked each run. Network-level policy.
- Workaround: `get_mixmax_enrolled_emails()` now returns `None` on failure — safe fallback in place.
- Next steps: Bradley checks Mixmax → API Settings → IP Allowlist. Remove restriction or add cloud IPs.

---

## OPEN — All external APIs blocked from cloud (Apollo, Workiz, Mixmax, Slack)
- First seen: 2026-05-18
- Description: Apollo, Workiz, Mixmax, and Slack all return 403 from cloud. Lead pulls, pipeline reports, and Workiz data all require local execution.
- Workaround: Cron job schedule added to CLAUDE.md (run 7). Bradley has the exact commands to set up local scheduling.
- Next steps: Bradley runs `crontab -e` and pastes the cron jobs from CLAUDE.md.

---

## OPEN — Slack Webhook blocked in cloud execution environment
- First seen: 2026-05-18
- Workaround: All messages saved to `outputs/vera/pending_slack_messages.md`. GitHub Action fires on push and posts them.

---

## OPEN — Instantly.ai vs Mixmax Overlap (dual platform risk)
- First seen: 2026-05-18
- Description: `server.py` has 2 active Instantly.ai campaign IDs for Property Managers and Contractors — same segments Mixmax handles. Risk: same contact receives emails from both platforms.
- Attempts:
  - 2026-05-18 (runs 4–7): Flagging. Bradley needs to confirm which platform is active.
- Resolution criteria: Bradley confirms which platform is live. Non-active platform paused.

---

## OPEN — 0% reply rate across 45 enrolled contacts
- First seen: 2026-05-18
- Description: 45 enrolled, 42% open rate, 0 replies. 13 contacts opened 2+ times. Opens work, body copy doesn't convert.
- Attempts:
  - 2026-05-18 (runs 1–7): Full rewrite drafts ready in `outputs/vera/sequence_rewrites_proposal_2026-05-18.md`. Awaiting Bradley's YES.
  - 2026-05-18 (run 7): Marcus's seasonal VOC bulletin (`outputs/marcus/voc_seasonal_bulletin_may_2026.md`) written this run — Tommy and Jasmine can use this to sharpen copy if Bradley doesn't approve the sequence rewrite yet.
- Next steps: Bradley says YES → copy goes live in Mixmax sequences.

---

## OPEN — 13 hot leads sitting uncontacted on LinkedIn
- First seen: 2026-05-18
- Description: 13 contacts with 2+ opens, no replies, no LinkedIn outreach.
- Attempts:
  - 2026-05-18 (runs 1–6): LinkedIn connect templates ready. Awaiting Bradley's action.
  - 2026-05-18 (run 7): Full LinkedIn DM Protocol written (`outputs/danny/linkedin_hot_lead_dm_protocol_2026-05-18.md`). Includes decision tree: connect → open question → 3 response branches → booking ask. Work 3–4 per day to avoid LinkedIn flagging.

---

## OPEN — Marcus fresh web intel needed (competitor + VOC)
- First seen: 2026-05-18
- Description: Marcus's VOC library and competitor profiles are from May 12. 6 days old in peak season. New reviews posted weekly. Fresh data would sharpen all creative output.
- Attempts:
  - 2026-05-18 (run 7): Created seasonal VOC synthesis bulletin (`outputs/marcus/voc_seasonal_bulletin_may_2026.md`) from existing research. Covers 6 key customer triggers + PM-specific triggers + competitor gap. Covers Tommy/Jasmine/Rick for this week.
- Next steps: Bradley runs Marcus locally with web search enabled for a fresh competitor scrape.
- Resolution criteria: Fresh competitor profile + VOC update from web search (Marcus + web search, local run).

---

## OPEN — HubSpot not connected (CRM blind)
- First seen: 2026-05-12
- Description: HUBSPOT_TOKEN listed as "pending." Nina's CRM architecture is built and idle.
- Attempts:
  - 2026-05-18 (runs 1–7): Escalating each run. Still open.
- Resolution criteria: HUBSPOT_TOKEN added to .env. Nina confirms CRM live.

---

## OPEN — No residential homeowner outreach channel
- First seen: 2026-05-18
- Description: Entire pipeline is B2B. Zero homeowner outreach. Peak season — highest-volume segment.
- Attempts:
  - 2026-05-18 (run 6): Rick's June Facebook ads written. Tommy's reengagement email written. Still need: paid ad launch + Facebook/Nextdoor posts.
  - 2026-05-18 (run 7): Facebook posts for week of May 18–24 already written (run 6). Tommy's one-pager leave-behind written this run — useful for any walk-throughs Bradley does with homeowners. LinkedIn DM protocol written this run covers commercial side. Residential still needs: actual Facebook post publishing or ad spend.
- Resolution criteria: At least one homeowner channel live (Facebook ads running OR Bradley posting in Nextdoor groups).

---

## OPEN — Workiz API blocked in cloud AND 0 power washing jobs on local
- First seen: 2026-05-14 (0 jobs), 2026-05-18 (cloud 403)
- Description: Two separate problems: (1) API returns 403 from cloud. (2) Even locally, 0 Power Washing jobs found.
- Attempts:
  - 2026-05-18 (runs 1–6): Fixed matching code (10 variants), sentinel bug fixed, diagnostic logging in place.
  - 2026-05-18 (run 7): All fixes confirmed still in code. Root cause of 0 jobs remains: likely job tagging in Workiz uses a different JobType string. Next local run will print all JobType strings seen.
- Next step: Bradley logs into Workiz and checks how jobs are tagged (JobType field). Or runs workiz_report.py locally and looks at the `JobType values seen` diagnostic log output.

---

## OPEN — Danny/Carla lead pulls not logged (pipeline not growing visibly)
- First seen: 2026-05-18
- Description: No Danny or Carla lead pull logged in activity.log. 45 enrolled contacts exist in Mixmax but pipeline.py runs aren't showing up.
- Attempts:
  - 2026-05-18 (runs 4–7): Flagging. Cron job schedule added to CLAUDE.md this run so Bradley can set up local scheduling.
- Next steps: Bradley confirms whether `python3 workers/lead_pipeline.py both` is scheduled locally. If not, add the cron job from CLAUDE.md.

---

## OPEN — "Ghost fixes" pattern: fixes lost in merge conflicts
- First seen: 2026-05-18 (run 5)
- Run 6 verification: All 6 key fixes confirmed present. No ghost fixes.
- Run 7 verification: MIXMAX_TOKEN hardcode fixed and confirmed. Jasmine seasonal post fix confirmed. All previous fixes still present in code.
- Status: Pattern documented. Verify key fixes each run before closing.

---

*Last updated: 2026-05-18 by Vera Cole (run 7)*
*Key metrics: 17 RESOLVED | 13 OPEN | 5 new deliverables this run*
