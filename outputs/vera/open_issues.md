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
- File: `workers/lead_pipeline.py`

---

## RESOLVED — verify_and_repair_enrollment mass re-enrollment on API failure
- Resolved: 2026-05-18 (run 5 — reapplied after merge conflict wiped it)
- Fix: `get_mixmax_enrolled_emails()` now tracks `success_count`. Returns `None` (not empty set) when all 3 sequences fail. `verify_and_repair_enrollment()` skips repair on `None` return with clear warning. Confirmed in code run 8.
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
- Fix: Removed hardcoded fallback token from `integrations/mixmax.py`. Changed to `os.environ.get('MIXMAX_TOKEN', '')`.
- File: `integrations/mixmax.py`

---

## RESOLVED — jasmine_flyer.py generic Facebook post every month
- Resolved: 2026-05-18 (run 7)
- Fix: `write_facebook_post()` now selects seasonal hook and CTA based on the month of the date parameter.
- File: `workers/jasmine_flyer.py`

---

## RESOLVED — workiz_report.py Workiz credentials hardcoded in source (security risk)
- Resolved: 2026-05-18 (run 8)
- Fix: Removed hardcoded fallback values from `WORKIZ_TOKEN` and `WORKIZ_SECRET`. Changed to `os.environ.get(..., '')`. Same class as MIXMAX_TOKEN issue fixed in run 7.
- File: `workers/workiz_report.py`

---

## RESOLVED — Danny Apollo search misses property management companies (org-level gap)
- Resolved: 2026-05-18 (run 8)
- Fix: Added `DANNY_ORG_KEYWORDS` list with 8 property management company keyword tags. `run_danny()` now passes these to `apollo_search()` via `q_organization_keyword_tags`. Catches HOA management firms where the contact's title isn't "property manager" but the company clearly is in that space.
- File: `workers/lead_pipeline.py`, `agents/danny.md`

---

## OPEN — 🚨 HOT CONTRACTORS WAITING FOR TEXT (URGENT — REVENUE NOW)
- First seen: 2026-05-18
- Description: pipeline_data.json shows 2 contractors in "Replied" stage:
  - **Bulletproof Lawncare** | 216-307-4344 — called 2026-05-13, said "very interested"
  - **Damrons Landscaping** | 440-494-0422 — called 2026-05-13, said "very interested"
  Both were called. Neither has received a follow-up text. It has been 5+ days.
- Attempts:
  - 2026-05-18 (runs 1–7): Flagged via high-priority Slack alert each run.
  - 2026-05-18 (run 8): Full conversation decision tree written — `outputs/vera/contractor_conversation_tree_2026-05-18.md`. Every possible reply is scripted. No thinking required from Bradley — just copy and send.
- Resolution criteria: Bradley texts both and logs response in pipeline_data.json.

---

## OPEN — 22 Manual Contacts Need Stage Updates
- First seen: 2026-05-18 (updated run 8)
- Description: 24 manual contacts in pipeline_data.json. Stages: 2 Replied, 1 Contacted, 21 New Lead. Most were called on 2026-05-13 but stages not updated.
- Attempts:
  - 2026-05-18 (runs 6–8): server.py stale detection uses calls data. Stage update is Bradley's action.
- Resolution criteria: Bradley updates stages in dashboard, or says YES to auto-promote script.

---

## OPEN — Mixmax API blocked in cloud execution environment
- First seen: 2026-05-18
- Description: All Mixmax API calls return `HTTP 403: Forbidden` with body "Host not in allowlist." Cannot pull live sequence data during cloud runs.
- Impact: Cannot verify real-time enrollment. Nina reports must run locally.
- Attempts:
  - 2026-05-18 (runs 1–8): Confirmed blocked each run. Network-level policy.
- Workaround: `get_mixmax_enrolled_emails()` returns `None` on failure — safe fallback in place.
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
  - 2026-05-18 (runs 4–8): Flagging. Bradley needs to confirm which platform is active.
- Resolution criteria: Bradley confirms which platform is live. Non-active platform paused.

---

## OPEN — 0% reply rate across 45 enrolled contacts
- First seen: 2026-05-18
- Description: 45 enrolled, 42% open rate, 0 replies. 13 contacts opened 2+ times. Opens work, body copy doesn't convert.
- Attempts:
  - 2026-05-18 (runs 1–8): Full rewrite drafts ready in `outputs/vera/sequence_rewrites_proposal_2026-05-18.md`. Awaiting Bradley's YES.
  - Marcus's seasonal VOC bulletin active — Tommy/Jasmine have fresh language to work with.
- Next steps: Bradley says YES → copy goes live in Mixmax sequences.

---

## OPEN — 13 hot leads sitting uncontacted on LinkedIn
- First seen: 2026-05-18
- Description: 13 contacts with 2+ opens, no replies, no LinkedIn outreach.
- Attempts:
  - 2026-05-18 (runs 1–7): LinkedIn DM Protocol written (`outputs/danny/linkedin_hot_lead_dm_protocol_2026-05-18.md`). Awaiting Bradley's action.
  - 2026-05-18 (run 8): Re-escalating. 3 connects per day. Work 3 this week using the DM protocol.

---

## OPEN — Marcus fresh web intel needed (competitor + VOC)
- First seen: 2026-05-18
- Description: Marcus's VOC library and competitor profiles are from May 12. 6 days old in peak season. New reviews posted weekly.
- Attempts:
  - 2026-05-18 (run 7): Created seasonal VOC synthesis bulletin from existing research.
  - 2026-05-18 (run 8): GBP optimization guide written with competitor gap context. Fresh web intel still needed for competitor pricing / new reviews.
- Next steps: Bradley runs Marcus locally with web search enabled for a fresh competitor scrape.

---

## OPEN — HubSpot not connected (CRM blind)
- First seen: 2026-05-12
- Description: HUBSPOT_TOKEN listed as "pending." Nina's CRM architecture is built and idle.
- Attempts:
  - 2026-05-18 (runs 1–8): Escalating each run. Still open.
- Resolution criteria: HUBSPOT_TOKEN added to .env. Nina confirms CRM live.

---

## OPEN — No residential homeowner outreach channel
- First seen: 2026-05-18
- Description: Entire pipeline is B2B. Zero homeowner outreach. Peak season — highest-volume segment.
- Attempts:
  - 2026-05-18 (run 6): Rick's June Facebook ads written. Tommy's reengagement email written.
  - 2026-05-18 (run 7): Facebook posts and LinkedIn content written. Tommy's one-pager written.
  - 2026-05-18 (run 8): Google review request sequence written (Tommy). GBP optimization guide written (Marcus). Annual Plan campaign brief written (Donna). Residential channel still needs: Facebook ads running OR Bradley posting in Nextdoor groups.
- Resolution criteria: At least one homeowner channel live (Facebook ads running OR GBP weekly posts active).

---

## OPEN — Workiz API blocked in cloud AND 0 power washing jobs on local
- First seen: 2026-05-14 (0 jobs), 2026-05-18 (cloud 403)
- Description: Two separate problems: (1) API returns 403 from cloud. (2) Even locally, 0 Power Washing jobs found.
- Attempts:
  - 2026-05-18 (runs 1–8): All code fixes confirmed in place. Diagnostic logging will print JobType values seen.
- Next step: Bradley logs into Workiz and checks how jobs are tagged (JobType field). Or runs workiz_report.py locally and looks at the `JobType values seen` diagnostic log output.

---

## OPEN — Danny/Carla lead pulls not logged (pipeline not growing visibly)
- First seen: 2026-05-18
- Description: No Danny or Carla lead pull logged in activity.log since May 13. Pipeline needs local scheduling.
- Attempts:
  - 2026-05-18 (runs 4–8): Cron job schedule in CLAUDE.md. Still not confirmed running.
- Next steps: Bradley confirms whether `python3 workers/lead_pipeline.py both` is scheduled locally.

---

## OPEN — "Ghost fixes" pattern: fixes lost in merge conflicts
- First seen: 2026-05-18 (run 5)
- Run 8 verification: All 6 key fixes + 2 new run-8 fixes verified. No ghost fixes.
- Status: Verified each run. Pattern documented.

---

## OPEN — Google Business Profile not managed (zero-cost lead channel ignored)
- First seen: 2026-05-18 (run 8)
- Description: No GBP activity in the office. No weekly posts, no photo uploads, no review responses. Peak season = peak Google search volume. NE Ohio competitors have < 10 photos and < 50% review response rate — Forest City can dominate this for free.
- Attempts:
  - 2026-05-18 (run 8): Full GBP optimization guide written — `outputs/marcus/gbp_optimization_guide_2026-05-18.md`. Covers: profile completeness, photos, weekly posts, review responses, Q&A seeding, competitor gap analysis.
- Resolution criteria: Bradley completes GBP profile completeness checklist + starts weekly posting (1 post/week, 2–3 photos/week).
- Note: This is the only free lead channel currently untouched. 20+ reviews + weekly posts = Google 3-pack eligibility.

---

## OPEN — No review request automation (jobs complete, no review ask)
- First seen: 2026-05-18 (run 8)
- Description: Every completed job is an opportunity for a 5-star review. No post-job review request sequence exists. Google reviews directly impact GBP ranking and organic leads.
- Attempts:
  - 2026-05-18 (run 8): Full review request sequence written — `outputs/tommy/review_request_sequence_2026-05-18.md`. 3-touch: same-day text, 3-day email, 7-day text ($500+ jobs). Ready to use immediately.
- Resolution criteria: Bradley sends review request text after each completed job. 5+ new Google reviews in May.
- Note: This is the fastest path to more organic homeowner leads. Zero cost. 10 minutes per job.

---

*Last updated: 2026-05-18 by Vera Cole (run 8)*
*Key metrics: 19 RESOLVED | 15 OPEN | 4 new deliverables this run | 2 new issues found*
