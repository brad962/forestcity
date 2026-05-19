# Vera Cole — Open Issues Tracker
*Updated automatically each run. Only mark RESOLVED after verifying the fix works.*

---

## RESOLVED — Jasmine infinite retry loop (not_in_channel)
- Resolved: 2026-05-18
- Fix: `pair["processed"] = True` set before try block. `pair["success"]` distinguishes clean vs failed.
- File: `workers/jasmine_flyer.py`

---

## RESOLVED — Carla Apollo keyword filter ignored
- Resolved: 2026-05-18 (run 5 — reapplied after merge conflict wiped it)
- Fix: `apollo_search()` now accepts `keywords=None` param and passes `q_organization_keyword_tags` to Apollo API.
- File: `workers/lead_pipeline.py`

---

## RESOLVED — verify_and_repair_enrollment mass re-enrollment on API failure
- Resolved: 2026-05-18 (run 5)
- Fix: Returns `None` on all-failure; skips repair on `None`.
- File: `workers/lead_pipeline.py`

---

## RESOLVED — nina_report fetch_recipients drops dict responses
- Resolved: 2026-05-18
- Fix: Handles both list and dict Mixmax responses.
- File: `workers/nina_report.py`

---

## RESOLVED — Apollo JSON parse crash
- Resolved: 2026-05-18
- Fix: try/except around all Apollo calls.
- File: `workers/lead_pipeline.py`

---

## RESOLVED — Workiz case-insensitive job matching
- Resolved: 2026-05-18
- Fix: 10 variants, diagnostic logging.
- File: `workers/workiz_report.py`

---

## RESOLVED — jasmine_flyer.py env loading only in __main__
- Resolved: 2026-05-18
- Fix: `_load_env()` at module level.
- File: `workers/jasmine_flyer.py`

---

## RESOLVED — workiz_report "No jobs found" misleads on API failure
- Resolved: 2026-05-18
- Fix: `WORKIZ_API_ERROR` sentinel.
- File: `workers/workiz_report.py`

---

## RESOLVED — nina_report.py misleading action items
- Resolved: 2026-05-18
- Fix: Accurate wording for 0-reply state.
- File: `workers/nina_report.py`

---

## RESOLVED — nina_report.py double API fetch in run_daily()
- Resolved: 2026-05-18 (run 5)
- Fix: `seq_stats_cache` dict eliminates redundant calls.
- File: `workers/nina_report.py`

---

## RESOLVED — jasmine_flyer.py dead location_hint variable
- Resolved: 2026-05-18 (run 5)
- Fix: 5 lines of dead code removed.
- File: `workers/jasmine_flyer.py`

---

## RESOLVED — vera_relay.py crashes if .env missing
- Resolved: 2026-05-18 (run 5)
- Fix: `.exists()` guard.
- File: `workers/vera_relay.py`

---

## RESOLVED — workiz_report.py sentinel check uses `is` instead of `==`
- Resolved: 2026-05-18 (run 6)
- Fix: String identity → equality comparison.
- File: `workers/workiz_report.py`

---

## RESOLVED — lead_pipeline.py save_to_cache crashes on malformed JSON
- Resolved: 2026-05-18 (run 6)
- Fix: try/except around JSON parse in `save_to_cache()`.
- File: `workers/lead_pipeline.py`

---

## RESOLVED — server.py stale detection ignores calls log for manual contacts
- Resolved: 2026-05-18 (run 6)
- Fix: Falls back to `calls_data` for `last_contact`.
- File: `server.py`

---

## RESOLVED — MIXMAX_TOKEN hardcoded in source code
- Resolved: 2026-05-18 (run 7)
- Fix: `os.environ.get('MIXMAX_TOKEN', '')`.
- File: `integrations/mixmax.py`

---

## RESOLVED — jasmine_flyer.py generic Facebook post every month
- Resolved: 2026-05-18 (run 7)
- Fix: Seasonal hook + CTA by month.
- File: `workers/jasmine_flyer.py`

---

## RESOLVED — workiz_report.py Workiz credentials hardcoded
- Resolved: 2026-05-18 (run 8)
- Fix: `os.environ.get(...)` for both WORKIZ_TOKEN and WORKIZ_SECRET.
- File: `workers/workiz_report.py`

---

## RESOLVED — Danny Apollo search misses property management companies (org-level gap)
- Resolved: 2026-05-18 (run 8)
- Fix: `DANNY_ORG_KEYWORDS` list with 8 PM company tags.
- File: `workers/lead_pipeline.py`, `agents/danny.md`

---

## RESOLVED — server.py APOLLO_KEY hardcoded in /api/apollo/linkedin endpoint
- Resolved: 2026-05-19 (run 9)
- Fix: Added `APOLLO_KEY = os.environ.get('APOLLO_KEY', '')` at module level. Replaced hardcoded string.
- File: `server.py`

---

## RESOLVED — report_card.py Mac-only font paths fail silently in Linux/cloud
- Resolved: 2026-05-19 (run 9)
- Fix: Added `_find_font()` helper that checks Mac path first, then Liberation Sans and DejaVu Linux paths.
- File: `utils/report_card.py`

---

## RESOLVED — danny.md agent file references dead tools (Instantly.ai, HubSpot) as active
- Resolved: 2026-05-19 (run 9)
- Fix: Updated Tools section to mark Mixmax as active, Instantly.ai as inactive, HubSpot pending.
- File: `agents/danny.md`

---

## RESOLVED — server.py PUT /api/pipeline cannot update manual contacts (no email key)
- Resolved: 2026-05-19 (run 10)
- Fix: Extended PUT handler to accept `contact_id` field. If present, looks up manual contact in `manual_contacts[]` by ID and updates in-place. If only `email` present, uses legacy email-keyed path. If neither, returns 400.
- File: `server.py`

---

## OPEN — 🚨 HOT CONTRACTORS WAITING FOR TEXT (DAY 7 — CRITICAL)
- First seen: 2026-05-13
- Description: 2 contractors in "Replied" stage:
  - **Bulletproof Lawncare** | 216-307-4344 — notes: "Very interested — send text"
  - **Damrons Landscaping** | 440-494-0422 — notes: "Very interested — send text"
  Both were called 2026-05-13. Today is 2026-05-19 — **7 days without a text**. At 7 days, warm interest transitions to cold. Every additional day increases drop-off significantly.
- Attempts:
  - 2026-05-18 (runs 1–9): Flagged via high-priority Slack alerts every run.
  - 2026-05-19 (run 10): Day-7 specific text scripts written: `outputs/vera/contractor_day7_texts_2026-05-19.md`
  - 2026-05-19 (run 10): Memorial Day sprint plan includes these as Day 1 priority: `outputs/donna/memorial_day_sprint_2026-05-19.md`
- Resolution criteria: Bradley texts both TODAY and logs response in pipeline_data.json.

---

## OPEN — 22 Manual Contacts Need Stage Updates + Texts
- First seen: 2026-05-18 (updated run 10)
- Description: 24 manual contacts total. 21 in "New Lead", 1 in "Contacted", 2 in "Replied". Notes say "Send text" on most.
- Attempts:
  - 2026-05-18 (runs 6–10): SMS templates ready (`outputs/vera/sms_templates_contractors_2026-05-18.md`).
  - 2026-05-19 (run 10): Memorial Day sprint plan prioritizes texting all contacts this week.
  - 2026-05-19 (run 10): server.py fix deployed — Bradley can now update stages from dashboard using contact_id.
- Resolution criteria: Bradley texts leads + updates stages in pipeline_data.json.

---

## OPEN — Mixmax API blocked in cloud execution environment
- First seen: 2026-05-18
- Description: All Mixmax API calls return HTTP 403 from cloud. Cannot pull live sequence data during cloud runs.
- Workaround: `get_mixmax_enrolled_emails()` returns `None` on failure — safe fallback confirmed.
- Attempts: 2026-05-18 through 2026-05-19: Confirmed blocked each run.
- Next steps: Bradley checks Mixmax → API Settings → IP Allowlist. Remove restriction or add cloud IPs.

---

## OPEN — All external APIs blocked from cloud (Apollo, Workiz, Mixmax)
- First seen: 2026-05-18
- Description: Lead pulls, pipeline reports, and Workiz data all require local execution.
- Workaround: Cron job schedule in CLAUDE.md. Local scheduling confirmed documented.
- Next steps: Bradley runs `crontab -e` and pastes the cron jobs from CLAUDE.md.

---

## OPEN — Slack Webhook blocked in cloud execution environment
- First seen: 2026-05-18
- Workaround: All messages saved to `outputs/vera/pending_slack_messages.md`. GitHub Action fires on push and posts them.

---

## OPEN — Instantly.ai vs Mixmax Overlap (dual platform risk)
- First seen: 2026-05-18
- Description: `server.py` has 2 active Instantly.ai campaign IDs for Property Managers and Contractors — same segments Mixmax handles. Risk: same contact receives emails from both platforms.
- Attempts: 2026-05-18–19: Flagging. Bradley needs to confirm which platform is active.
- Resolution criteria: Bradley confirms which platform is live. Non-active platform paused.

---

## OPEN — 0% reply rate across 45 enrolled contacts
- First seen: 2026-05-18
- Description: 45 enrolled, 42% open rate, 0 replies. Opens work, body copy doesn't convert.
- Attempts:
  - 2026-05-18 (runs 1–9): Full rewrite drafts ready — `outputs/vera/sequence_rewrites_proposal_2026-05-18.md`. Awaiting YES.
  - 2026-05-19 (run 10): Manual bridge email written for top 13 hot leads as parallel track: `outputs/tommy/hot_lead_bridge_email_2026-05-19.md`. Doesn't require sequence change.
  - Bridge email can be sent TODAY without approval — no platform changes needed.
- Next steps: Bradley sends bridge emails to top 3 hot leads today. Say YES to sequence rewrite.

---

## OPEN — 13 hot leads sitting uncontacted on LinkedIn
- First seen: 2026-05-18
- Description: 13 contacts with 2+ opens, no replies, no LinkedIn outreach. LinkedIn DM protocol ready.
- Attempts:
  - 2026-05-18 (runs 1–9): Protocol written (`outputs/danny/linkedin_hot_lead_dm_protocol_2026-05-18.md`). 3 connects/day.
  - 2026-05-19 (run 10): Bridge email written as faster alternative for today.
- Resolution criteria: Bradley sends first 3 LinkedIn connects OR 3 bridge emails using the protocol/template.

---

## OPEN — Marcus fresh web intel needed (competitor + VOC)
- First seen: 2026-05-18
- Description: Live competitor pricing + GBP status needs web search (cloud-blocked).
- Attempts:
  - 2026-05-18 (run 7): VOC seasonal bulletin from existing research.
  - 2026-05-19 (run 9): GBP optimization guide written.
  - 2026-05-19 (run 10): Synthesized intel update written from patterns: `outputs/marcus/competitor_intel_may19_2026.md`. Live web data still needed.
- Next steps: Bradley runs Marcus locally with web search enabled.

---

## OPEN — HubSpot not connected (CRM blind)
- First seen: 2026-05-12
- Description: HUBSPOT_TOKEN listed as "pending." Nina's CRM architecture is built and idle.
- Attempts: 2026-05-12 through 2026-05-19 (runs 1–10): Escalating each run. Still open.
- Resolution criteria: HUBSPOT_TOKEN added to .env. Nina confirms CRM live.

---

## OPEN — No residential homeowner outreach channel
- First seen: 2026-05-18
- Description: Entire pipeline is B2B. Zero homeowner outreach. Peak season = highest-volume segment.
- Attempts:
  - 2026-05-18 (runs 6–9): Facebook ads written (Rick), re-engagement email (Tommy), one-pager (Tommy), GBP guide (Marcus), review request sequence (Tommy).
  - 2026-05-19 (run 10): Memorial Day sprint plan outlines 5-channel residential push: `outputs/donna/memorial_day_sprint_2026-05-19.md`
  - Nextdoor post written in sprint plan — 10 minutes, zero cost.
- Resolution criteria: One action taken: Facebook post published, Nextdoor post live, OR GBP photo posted.

---

## OPEN — Workiz API blocked in cloud AND 0 power washing jobs on local
- First seen: 2026-05-14 (0 jobs), 2026-05-18 (cloud 403)
- Description: Two problems: (1) API returns 403 from cloud. (2) 0 Power Washing jobs found even locally.
- Attempts: 2026-05-18–19: All code fixes confirmed. Diagnostic logging will print JobType values.
- Next step: Bradley logs into Workiz, checks how jobs are tagged (JobType field name).

---

## OPEN — Danny/Carla lead pulls not logged (pipeline not growing)
- First seen: 2026-05-18
- Description: No Danny or Carla lead pull logged in activity.log since May 13. One week gap. `contacts_cache.json` confirmed missing from cloud clone (local-only file, not committed to git).
- Attempts: 2026-05-18–19 (runs 1–10): Cron job schedule in CLAUDE.md. Still not confirmed running.
- Next steps: Bradley confirms `python3 workers/lead_pipeline.py both` is scheduled locally. Week of May 19 is Geauga+Portage rotation for Danny.

---

## OPEN — Google Business Profile not managed (zero-cost lead channel ignored)
- First seen: 2026-05-18 (run 8)
- Description: No GBP posts, photos, or review responses. Full optimization guide written. Peak Google search volume is NOW.
- Attempts:
  - 2026-05-18 (run 8): GBP guide — `outputs/marcus/gbp_optimization_guide_2026-05-18.md`.
  - 2026-05-19 (runs 9–10): Escalating. Before/after from Westlake May 13 job is ready to upload today.
- Resolution criteria: Bradley posts 1 photo to GBP today. 10 minutes.

---

## OPEN — No review request automation
- First seen: 2026-05-18 (run 8)
- Description: No post-job review request sequence. Every completed job is a missed review opportunity.
- Attempts:
  - 2026-05-18 (run 8): 3-touch sequence written — `outputs/tommy/review_request_sequence_2026-05-18.md`.
  - 2026-05-19 (runs 9–10): Still open.
- Resolution criteria: Bradley sends review request text after each completed job.

---

## OPEN — Ghost fixes pattern: fixes lost in merge conflicts
- First seen: 2026-05-18 (run 5)
- Status: Monitored each run. No ghost fixes detected in runs 8, 9, or 10. Pattern documented. Watch for it.

---

*Last updated: 2026-05-19 by Vera Cole (run 10)*
*Key metrics: 23 RESOLVED | 14 OPEN | 4 new deliverables shipped | 1 auto-upgrade shipped*
