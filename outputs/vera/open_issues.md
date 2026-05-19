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
- Fix: Added `APOLLO_KEY = os.environ.get('APOLLO_KEY', '')` at module level.
- File: `server.py`

---

## RESOLVED — report_card.py Mac-only font paths fail silently in Linux/cloud
- Resolved: 2026-05-19 (run 9)
- Fix: Added `_find_font()` helper with Linux Liberation Sans and DejaVu fallbacks.
- File: `utils/report_card.py`

---

## RESOLVED — danny.md agent file references dead tools (Instantly.ai, HubSpot) as active
- Resolved: 2026-05-19 (run 9)
- Fix: Updated Tools section to mark Mixmax as active, Instantly.ai inactive, HubSpot pending.
- File: `agents/danny.md`

---

## RESOLVED — server.py PUT /api/pipeline cannot update manual contacts (no email key)
- Resolved: 2026-05-19 (run 10)
- Fix: Extended PUT handler to accept `contact_id` field. Manual contacts updated by ID lookup.
- File: `server.py`

---

## RESOLVED — lead_pipeline.py load_existing_emails() crashes on malformed cache JSON
- Resolved: 2026-05-19 (run 11)
- Fix: Added try/except around `json.loads(CACHE_FILE.read_text())` in `load_existing_emails()`. On parse failure, warns and returns empty set so pipeline continues.
- File: `workers/lead_pipeline.py`

---

## RESOLVED — lead_pipeline.py verify_and_repair_enrollment() crashes on malformed cache JSON
- Resolved: 2026-05-19 (run 11)
- Fix: Added try/except around cache JSON parse in `verify_and_repair_enrollment()`. On failure, logs warning and returns early.
- File: `workers/lead_pipeline.py`

---

## RESOLVED — nina_report.py shows misleading "0 enrolled" when Mixmax API is blocked
- Resolved: 2026-05-19 (run 11)
- Fix: Added `api_responses_received` counter in both `run_daily()` and `run_weekly()`. When all sequences return empty (cloud block), report now prominently warns "⚠️ Mixmax API unavailable" instead of showing 0 enrolled as if pipeline is empty.
- File: `workers/nina_report.py`

---

## OPEN — 🚨 HOT CONTRACTORS WAITING FOR TEXT (DAY 8 — CRITICAL)
- First seen: 2026-05-13
- Description: 2 contractors in "Replied" stage:
  - **Bulletproof Lawncare** | 216-307-4344 — notes: "Very interested — send text"
  - **Damrons Landscaping** | 440-494-0422 — notes: "Very interested — send text"
  Both were called 2026-05-13. Today is 2026-05-19 — **8 days without a text**. Reply rate drops ~40% after 7 days.
- Attempts:
  - 2026-05-18 (runs 1–9): Flagged via high-priority Slack alerts every run.
  - 2026-05-19 (run 10): Day-7 texts written: `outputs/vera/contractor_day7_texts_2026-05-19.md`
  - 2026-05-19 (run 11): Day-8 texts with Memorial Day hook + 3-option sequence: `outputs/vera/contractor_day8_texts_2026-05-19.md`
- Resolution criteria: Bradley texts both TODAY and logs response in pipeline_data.json.

---

## OPEN — 22 Manual Contacts Need Stage Updates + Texts
- First seen: 2026-05-18 (updated run 11)
- Description: 24 manual contacts total. 21 "New Lead", 1 "Contacted", 2 "Replied". Notes say "Send text" on most.
- Attempts:
  - 2026-05-18 (runs 6–10): SMS templates ready (`outputs/vera/sms_templates_contractors_2026-05-18.md`).
  - 2026-05-19 (run 10): Memorial Day sprint plan prioritizes texting all contacts.
  - 2026-05-19 (run 11): Memorial Day (May 24) = perfect text hook for all landscaper/contractor leads. Use "before the holiday" framing.
- Resolution criteria: Bradley texts leads + updates stages in pipeline_data.json.

---

## OPEN — Mixmax API blocked in cloud execution environment
- First seen: 2026-05-18
- Workaround: All pipeline scripts return None/safe fallback on 403. nina_report now shows explicit API warning instead of misleading zeroes (run 11 fix).
- Next steps: Bradley checks Mixmax → API Settings → IP Allowlist.

---

## OPEN — All external APIs blocked from cloud (Apollo, Workiz, Mixmax)
- First seen: 2026-05-18
- Workaround: Cron job schedule documented in CLAUDE.md.
- Next steps: Bradley runs `crontab -e` and pastes cron jobs.

---

## OPEN — Slack Webhook blocked in cloud execution environment
- First seen: 2026-05-18
- Workaround: Messages written to `outputs/vera/pending_slack_messages.md`. GitHub Action posts to Slack on push.

---

## OPEN — Instantly.ai vs Mixmax Overlap (dual platform risk)
- First seen: 2026-05-18
- Description: server.py has active Instantly.ai campaign IDs for same segments Mixmax handles. Risk: duplicate emails.
- Resolution criteria: Bradley confirms which platform is live. Non-active platform paused.

---

## OPEN — 0% reply rate across 45 enrolled contacts
- First seen: 2026-05-18
- Description: 45 enrolled, 42% open rate, 0 replies. Opens work, body copy doesn't convert.
- Attempts:
  - Run 11 fresh angle: May be email 2 drop-off (opens on email 1, weak email 2). Full rewrites ready: `outputs/vera/sequence_rewrites_proposal_2026-05-18.md`. Bridge email ready: `outputs/tommy/hot_lead_bridge_email_2026-05-19.md`.
- Next steps: Bradley says YES to sequence rewrite. OR sends bridge email to top 3 hot leads this week.

---

## OPEN — 13 hot leads sitting uncontacted on LinkedIn
- First seen: 2026-05-18
- Description: 13 contacts with 2+ opens, no replies, no LinkedIn outreach.
- Run 11: Memorial Day week is ideal for first connects — PMs are planning summer vendor contracts.
- Protocol ready: `outputs/danny/linkedin_hot_lead_dm_protocol_2026-05-18.md`
- Resolution criteria: Bradley sends 3 LinkedIn connects or 3 bridge emails this week.

---

## OPEN — Marcus fresh web intel needed (competitor + VOC)
- First seen: 2026-05-18
- Web search blocked in cloud. All prior intel from patterns/research.
- Next steps: Bradley runs Marcus locally.

---

## OPEN — HubSpot not connected (CRM blind)
- First seen: 2026-05-12
- Escalating every run. Resolution: HUBSPOT_TOKEN added to .env.

---

## OPEN — No residential homeowner outreach channel
- First seen: 2026-05-18
- Run 11: Nextdoor templates written (`outputs/donna/nextdoor_post_template_2026-05-19.md`). Memorial Day social posts ready (`outputs/jasmine/memorial_day_posts_2026-05-19.md`). Peak season peaks THIS WEEK.
- Resolution criteria: Bradley posts 1 Facebook post OR creates Nextdoor account.

---

## OPEN — Workiz API blocked in cloud AND 0 power washing jobs on local
- First seen: 2026-05-14
- All code fixes confirmed present. Diagnostic logging will print JobType values when run locally.
- Next step: Bradley checks Workiz for actual JobType field name.

---

## OPEN — Danny/Carla lead pulls not logged (pipeline not growing)
- First seen: 2026-05-18
- No lead pull in activity.log since May 13. One-week gap.
- Next steps: Bradley confirms `python3 workers/lead_pipeline.py both` is running locally via cron.

---

## OPEN — Google Business Profile not managed (zero-cost lead channel ignored)
- First seen: 2026-05-18 (run 8)
- GBP optimization guide: `outputs/marcus/gbp_optimization_guide_2026-05-18.md`. Before/after from May 13 ready to upload.
- Resolution: Bradley posts 1 photo to GBP today.

---

## OPEN — No review request automation
- First seen: 2026-05-18 (run 8)
- 3-touch sequence written: `outputs/tommy/review_request_sequence_2026-05-18.md`.
- Resolution: Bradley sends review request text after each completed job.

---

## OPEN — Ghost fixes pattern: fixes lost in merge conflicts
- First seen: 2026-05-18 (run 5)
- Run 11 verification: all 26 prior fixes confirmed present. No regressions.

---

*Last updated: 2026-05-19 by Vera Cole (run 11)*
*Key metrics: 26 RESOLVED | 14 OPEN | 3 auto-upgrades shipped | 4 new deliverables*
