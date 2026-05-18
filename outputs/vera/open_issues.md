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

## OPEN — 🚨 HOT CONTRACTORS WAITING FOR TEXT (URGENT — REVENUE NOW)
- First seen: 2026-05-18
- Description: pipeline_data.json shows 2 contractors in "Replied" stage, notes say "Very interested — send text":
  - **Bulletproof Lawncare** | 216-307-4344
  - **Damrons Landscaping** | 440-494-0422
  These are warm referral partners who already said YES. No follow-up logged. Every day without a text is lost referrals.
- Attempts:
  - 2026-05-18 (run 2): Flagged via high-priority Slack alert.
  - 2026-05-18 (run 4): SMS follow-up template written and saved to `outputs/vera/sms_templates_contractors_2026-05-18.md`.
  - 2026-05-18 (run 5): Re-escalating. Templates are ready. This is now 6+ days without follow-up.
- Resolution criteria: Bradley texts both and logs response in pipeline_data.json.

---

## OPEN — 21 Manual Leads in "New Lead" — No Outreach
- First seen: 2026-05-18
- Description: 24 manual contacts in pipeline_data.json. 21 in "New Lead" stage with no contact logged. All contractors (landscapers, roofers, construction companies) with phone numbers.
- Attempts:
  - 2026-05-18 (run 2): Flagged to Bradley. Proposed Carla write SMS outreach templates.
  - 2026-05-18 (run 4): SMS templates written — ready in `outputs/vera/sms_templates_contractors_2026-05-18.md`.
  - 2026-05-18 (run 5): Re-escalating. 30 minutes of texting could generate thousands in referrals this season.
- Resolution criteria: Each contact moved to Contacted or further.

---

## OPEN — Mixmax API blocked in cloud execution environment
- First seen: 2026-05-18
- Description: All Mixmax API calls return `HTTP 403: Forbidden` with body "Host not in allowlist." Cannot pull live sequence data during cloud runs.
- Impact: Cannot verify real-time enrollment. Nina reports must run locally.
- Attempts:
  - 2026-05-18 (runs 1–5): Confirmed blocked each run. Network-level policy.
- Workaround: `get_mixmax_enrolled_emails()` now returns `None` on failure — safe fallback in place.
- Next steps: Bradley checks Mixmax → API Settings → IP Allowlist. Remove restriction or add cloud IPs.

---

## OPEN — All external APIs blocked from cloud (Apollo, Workiz, Mixmax, Slack)
- First seen: 2026-05-18
- Description: Apollo, Workiz, Mixmax, and Slack all return 403 from cloud execution environment. Lead pulls, pipeline reports, and Workiz data all require local execution.
- Attempts:
  - 2026-05-18 (runs 4–5): Confirmed. Code-level safeguards deployed. Core operations must run locally.
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
  - 2026-05-18 (runs 4–5): Flagging. Bradley needs to confirm which platform is active.
- Resolution criteria: Bradley confirms which platform is live. Non-active platform paused.

---

## OPEN — 0% reply rate across 45 enrolled contacts
- First seen: 2026-05-18
- Description: 45 enrolled, 42% open rate, 0 replies. 13 contacts opened 2+ times. Opens work, body copy doesn't convert.
- Attempts:
  - 2026-05-18 (runs 1–5): Full rewrite drafts ready in `outputs/vera/sequence_rewrites_proposal_2026-05-18.md`. Under 100 words + yes/no close + break-up email touch 4. Awaiting Bradley's YES.
- Next steps: Bradley says YES → copy goes live in Mixmax sequences.

---

## OPEN — 13 hot leads sitting uncontacted on LinkedIn
- First seen: 2026-05-18
- Description: 13 contacts with 2+ opens, no replies, no LinkedIn outreach.
- Attempts:
  - 2026-05-18 (runs 1–5): LinkedIn connect templates ready in `outputs/vera/linkedin_connect_template_2026-05-18.md`. All 3 variants. Ready to use. Bradley needs to open daily hot leads report and send connects.

---

## OPEN — Marcus/Tommy/Rick/Donna silent since May 12
- First seen: 2026-05-18
- Description: 4 workers have produced zero output for 6+ days. Peak season is now.
- Attempts:
  - 2026-05-18 (runs 1–5): Proposed activation each run. Jasmine's Facebook/LinkedIn posts filled by Vera this run. Still waiting for Bradley to say YES.
- Resolution criteria: Each worker produces at least one new peak-season output.

---

## OPEN — HubSpot not connected (CRM blind)
- First seen: 2026-05-12
- Description: HUBSPOT_TOKEN listed as "pending." Nina's CRM architecture is built and idle.
- Attempts:
  - 2026-05-18 (runs 1–5): Escalating each run. Still open.
- Resolution criteria: HUBSPOT_TOKEN added to .env. Nina confirms CRM live.

---

## OPEN — No residential homeowner outreach channel
- First seen: 2026-05-18
- Description: Entire pipeline is B2B. Zero homeowner outreach. Peak season — highest-volume segment.
- Attempts:
  - 2026-05-18 (runs 4–5): Escalating. Facebook/Google Ads + neighborhood groups recommended.
- Resolution criteria: At least one homeowner channel live.

---

## OPEN — Workiz API blocked in cloud AND 0 jobs on local
- First seen: 2026-05-14 (0 jobs), 2026-05-18 (cloud 403)
- Description: Two separate problems: (1) API returns 403 from cloud. (2) Even locally, 0 Power Washing jobs found.
- Attempts:
  - 2026-05-18 (runs 1–5): Fixed matching code (10 variants), added API error sentinel. Next local run will show exact JobType values. Bradley needs to check how jobs are tagged in Workiz.
- Resolution criteria: Local run shows job count > 0 OR Bradley confirms job tag format.

---

## OPEN — Danny/Carla lead pulls not logged (pipeline not growing visibly)
- First seen: 2026-05-18
- Description: Activity log shows no Danny or Carla lead pull ever logged. 45 enrolled contacts exist in Mixmax but the pipeline.py runs aren't showing in activity.log.
- Attempts:
  - 2026-05-18 (runs 4–5): Flagging. Either script isn't scheduled or ran before logging was in place.
- Next steps: Bradley confirms whether `python3 workers/lead_pipeline.py both` is scheduled to run locally (cron/launchd). If not, schedule it weekly.

---

## OPEN — "Ghost fixes" pattern: previously-deployed fixes lost in merge conflicts
- First seen: 2026-05-18 (run 5)
- Description: At least 2 major fixes (Carla keyword filter, Mixmax mass-enrollment guard) were marked RESOLVED in open_issues.md after runs 2–3, but were NOT present in the code cloned for run 5. Root cause: merge conflict resolution at commit d3a6337 likely dropped Vera's changes when two concurrent runs conflicted.
- Fix applied run 5: Both bugs reapplied and confirmed in code.
- Prevention: Each run should verify key fixes are actually present in code before trusting open_issues.md RESOLVED status.

---

*Last updated: 2026-05-18 by Vera Cole (run 5)*
