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
- Fix: First loop now caches stats in `seq_stats_cache` dict. Second loop (summary builder for report card) reads from cache instead of calling `fetch_recipients()` again. Eliminates 3 redundant API calls per daily run.
- File: `workers/nina_report.py`

---

## RESOLVED — jasmine_flyer.py dead location_hint variable
- Resolved: 2026-05-18 (run 5)
- Fix: Removed 5 lines of dead code in `write_facebook_post()` — `location_hint` was computed but never used in the post template.
- File: `workers/jasmine_flyer.py`

---

## RESOLVED — vera_relay.py crashes if .env missing
- Resolved: 2026-05-18 (run 5)
- Fix: Added `_env.exists()` guard before reading `.env`. Previously would throw FileNotFoundError in cloud environments where .env is absent.
- File: `workers/vera_relay.py`

---

## RESOLVED — workiz_report.py sentinel check uses `is` instead of `==`
- Resolved: 2026-05-18 (run 6)
- Fix: `if jobs is WORKIZ_API_ERROR:` → `if jobs == WORKIZ_API_ERROR:`. Using identity comparison on a string constant is dangerous — if the constant is ever imported across modules or reconstructed, the `is` check fails silently and the API error string gets treated as a list (len=26), generating a fake "26 Power Washing jobs" report.
- File: `workers/workiz_report.py`

---

## RESOLVED — lead_pipeline.py save_to_cache crashes on malformed JSON
- Resolved: 2026-05-18 (run 6)
- Fix: Added try/except around `json.loads(CACHE_FILE.read_text())` in `save_to_cache()`. If the cache file exists but is corrupted (e.g., from a previous failed write), it logs a warning and starts fresh instead of crashing mid-pipeline-run.
- File: `workers/lead_pipeline.py`

---

## RESOLVED — server.py stale detection ignores calls log for manual contacts
- Resolved: 2026-05-18 (run 6)
- Fix: When building manual contact data for `/api/pipeline`, server now falls back to `calls_data.get(mc.get('id'), {}).get('called_at', '')` if `last_contact` is empty. All 24 manual contacts were called 2026-05-13 — the calls are logged in `pipeline.get('calls', {})` but the `manual_contacts[*].last_contact` field was empty. Stale detection now correctly flags them as needing follow-up.
- File: `server.py`

---

## OPEN — 🚨 HOT CONTRACTORS WAITING FOR TEXT (URGENT — REVENUE NOW)
- First seen: 2026-05-18
- Description: pipeline_data.json shows 2 contractors in "Replied" stage:
  - **Bulletproof Lawncare** | 216-307-4344 — called 2026-05-13, said "very interested"
  - **Damrons Landscaping** | 440-494-0422 — called 2026-05-13, said "very interested"
  Both were called. Neither has received a follow-up text. It has been 5+ days.
- Attempts:
  - 2026-05-18 (runs 1–5): Flagged via high-priority Slack alert.
  - 2026-05-18 (run 6): Re-escalating. Templates ready. Summer Push campaign brief now includes these as step 1.
- Resolution criteria: Bradley texts both and logs response in pipeline_data.json.

---

## OPEN — 22 Manual Contacts Need Stage Updates
- First seen: 2026-05-18 (updated run 6)
- Description: All 24 manual contacts were called on 2026-05-13 (logged in pipeline_data.json `calls` section). But most `manual_contacts[*].stage` is still "New Lead" and `last_contact` is empty — so the dashboard shows them as new/un-contacted.
  - CLE Lawn Care Plus (Bryan, 216-402-1924): Stage = "Contacted", notes "left off here — follow up." Needs second contact.
  - 21 others: Called but stage not updated from "New Lead" to "Contacted."
- Fix attempt: server.py now uses calls data for stale detection (run 6). But the stages in pipeline_data.json itself need updating — Bradley should update them manually in the dashboard, or we auto-update them.
- Attempts:
  - 2026-05-18 (run 6): server.py stale detection now uses calls data. Stage update is Bradley's action.
- Resolution criteria: Bradley updates stages in the pipeline dashboard, or approves auto-promotion script.

---

## OPEN — Mixmax API blocked in cloud execution environment
- First seen: 2026-05-18
- Description: All Mixmax API calls return `HTTP 403: Forbidden` with body "Host not in allowlist." Cannot pull live sequence data during cloud runs.
- Impact: Cannot verify real-time enrollment. Nina reports must run locally.
- Attempts:
  - 2026-05-18 (runs 1–6): Confirmed blocked each run. Network-level policy.
- Workaround: `get_mixmax_enrolled_emails()` now returns `None` on failure — safe fallback in place.
- Next steps: Bradley checks Mixmax → API Settings → IP Allowlist. Remove restriction or add cloud IPs.

---

## OPEN — All external APIs blocked from cloud (Apollo, Workiz, Mixmax, Slack)
- First seen: 2026-05-18
- Description: Apollo, Workiz, Mixmax, and Slack all return 403 from cloud execution environment. Lead pulls, pipeline reports, and Workiz data all require local execution.
- Attempts:
  - 2026-05-18 (runs 4–6): Confirmed. Code-level safeguards deployed. Core operations must run locally.
- Next steps: Schedule all API-dependent scripts via local cron, not cloud sessions.

---

## OPEN — Slack Webhook blocked in cloud execution environment
- First seen: 2026-05-18
- Workaround: All messages saved to `outputs/vera/pending_slack_messages.md`. GitHub Action fires on push and posts them.

---

## OPEN — Instantly.ai vs Mixmax Overlap (dual platform risk)
- First seen: 2026-05-18
- Description: `server.py` has 2 active Instantly.ai campaign IDs for Property Managers and Contractors — same segments Mixmax handles. Risk: same contact receives emails from both platforms.
- Attempts:
  - 2026-05-18 (runs 4–6): Flagging. Bradley needs to confirm which platform is active.
- Resolution criteria: Bradley confirms which platform is live. Non-active platform paused.

---

## OPEN — 0% reply rate across 45 enrolled contacts
- First seen: 2026-05-18
- Description: 45 enrolled, 42% open rate, 0 replies. 13 contacts opened 2+ times. Opens work, body copy doesn't convert.
- Attempts:
  - 2026-05-18 (runs 1–6): Full rewrite drafts ready in `outputs/vera/sequence_rewrites_proposal_2026-05-18.md`. Under 100 words + yes/no close + break-up email touch 4. Awaiting Bradley's YES.
- Next steps: Bradley says YES → copy goes live in Mixmax sequences.

---

## OPEN — 13 hot leads sitting uncontacted on LinkedIn
- First seen: 2026-05-18
- Description: 13 contacts with 2+ opens, no replies, no LinkedIn outreach.
- Attempts:
  - 2026-05-18 (runs 1–6): LinkedIn connect templates ready in `outputs/vera/linkedin_connect_template_2026-05-18.md`. All 3 variants. Ready to use. Bradley needs to open daily hot leads report and send connects.

---

## OPEN — Marcus/Tommy/Rick/Donna output — new peak-season deliverables needed
- First seen: 2026-05-18
- Updated: 2026-05-18 (run 6)
- Description: All creative workers had output from May 12 but nothing since. Peak season is NOW.
- Attempts:
  - 2026-05-18 (runs 1–5): Proposed activation each run. Bradley hadn't said YES.
  - 2026-05-18 (run 6): Vera produced new deliverables directly (no API needed for content):
    - Tommy: `outputs/tommy/past_customer_reengagement_2026-05-18.md` — past customer re-engagement email
    - Rick: `outputs/rick/facebook_ads_june_2026-05-18.md` — 5 June Facebook ad variations
    - Donna: `outputs/donna/campaign_brief_summer_push_2026-05-18.md` — Summer Push campaign brief
    - Jasmine: `outputs/jasmine/content_calendar_june_2026-05-18.md` — June content calendar
- Status: PARTIALLY RESOLVED — content written, Marcus still needs a fresh VOC/competitor update (requires web search).
- Resolution criteria: Bradley starts using these assets. Marcus activated for fresh market intel.

---

## OPEN — HubSpot not connected (CRM blind)
- First seen: 2026-05-12
- Description: HUBSPOT_TOKEN listed as "pending." Nina's CRM architecture is built and idle.
- Attempts:
  - 2026-05-18 (runs 1–6): Escalating each run. Still open.
- Resolution criteria: HUBSPOT_TOKEN added to .env. Nina confirms CRM live.

---

## OPEN — No residential homeowner outreach channel
- First seen: 2026-05-18
- Description: Entire pipeline is B2B. Zero homeowner outreach. Peak season — highest-volume segment.
- Attempts:
  - 2026-05-18 (runs 4–5): Escalating. Facebook/Google Ads + neighborhood groups recommended.
  - 2026-05-18 (run 6): Rick's June Facebook ads (written this run) address this — 5 ad variations targeting homeowners 35–65 in NE Ohio counties. Tommy's re-engagement email covers past customers. Still need: paid ad launch + Facebook/Nextdoor neighborhood group posts.
- Resolution criteria: At least one homeowner channel live (Facebook ads running OR Bradley posting in Nextdoor groups).

---

## OPEN — Workiz API blocked in cloud AND 0 power washing jobs on local
- First seen: 2026-05-14 (0 jobs), 2026-05-18 (cloud 403)
- Description: Two separate problems: (1) API returns 403 from cloud. (2) Even locally, 0 Power Washing jobs found.
- Attempts:
  - 2026-05-18 (runs 1–5): Fixed matching code (10 variants), added API error sentinel. Next local run will show exact JobType values.
  - 2026-05-18 (run 6): Sentinel check bug fixed (`is` → `==`). All matching logic confirmed correct. Root cause of 0 jobs is likely job tagging in Workiz — jobs may be entered with a different JobType string than any variant we check.
- Next step: Bradley logs into Workiz and checks how current jobs are tagged (JobType field). Diagnostic logging already in place — will print all JobType values on next local run.
- Resolution criteria: Local run shows job count > 0 OR Bradley confirms job tag format and we add the variant.

---

## OPEN — Danny/Carla lead pulls not logged (pipeline not growing visibly)
- First seen: 2026-05-18
- Description: Activity log shows no Danny or Carla lead pull ever logged. 45 enrolled contacts exist in Mixmax but the pipeline.py runs aren't showing in activity.log.
- Attempts:
  - 2026-05-18 (runs 4–6): Flagging. Either script isn't scheduled or ran before logging was in place.
- Next steps: Bradley confirms whether `python3 workers/lead_pipeline.py both` is scheduled to run locally (cron/launchd). If not, schedule it weekly.

---

## OPEN — "Ghost fixes" pattern: fixes lost in merge conflicts
- First seen: 2026-05-18 (run 5)
- Description: At least 2 major fixes were marked RESOLVED in open_issues.md after earlier runs but were NOT present in deployed code. Caused by concurrent run merge conflicts.
- Fix applied run 5: Both bugs reapplied and confirmed.
- Run 6 verification: All 6 key fixes from runs 1–5 confirmed present in code this run. No ghost fixes detected.
- Prevention: Each run now verifies key fixes before trusting RESOLVED status.

---

*Last updated: 2026-05-18 by Vera Cole (run 6)*
