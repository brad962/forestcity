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

## RESOLVED — detect_lead_type ignores _lead_type field — Carla realtor leads misrouted
- Resolved: 2026-05-19 (run 12)
- Fix: Added `explicit = lead.get('_lead_type', '')` check at top of `detect_lead_type()`. Returns immediately if value is a valid SEQUENCES key. Also fixed `mixmax_enroll()` to explicitly set `lead['_lead_type'] = lead_type`. Verified: 5-test suite all pass.
- Files: `integrations/mixmax.py`, `workers/lead_pipeline.py`

---

## RESOLVED — server.py manual contact name shows blank (no first_name/last_name)
- Resolved: 2026-05-19 (run 12)
- Fix: Added `if not name: name = mc.get('company', '')` fallback after name construction. Bulletproof Lawncare and Damrons Landscaping now display their company name in the pipeline dashboard.
- File: `server.py`

---

## RESOLVED — Carla searches miss HVAC, pool service, pest control referral partners
- Resolved: 2026-05-19 (run 12)
- Fix: Added "Home Services" search type to `CARLA_SEARCHES` with 9 new keywords (hvac, heating cooling, air conditioning, pool service, pool cleaning, pest control, home cleaning, junk removal, moving company). Updated `agents/carla.md` with 4 new partner types.
- Files: `workers/lead_pipeline.py`, `agents/carla.md`

---

## RESOLVED — 🚨 HOT CONTRACTORS WAITING FOR TEXT
- Resolved: 2026-05-19 (run 15)
- Fix: Bradley texted both contacts on 2026-05-19. pipeline_data.json confirms:
  - Bulletproof Lawncare → stage: "Contacted", last_contact: "2026-05-19", notes: "Texted referral partnership follow-up — awaiting reply"
  - Damrons Landscaping → stage: "Contacted", last_contact: "2026-05-19", notes: "Texted referral partnership follow-up — awaiting reply"
- Next: Watch for replies. If they reply → move to "Replied" stage, schedule estimate call.

---

## OPEN — 38 Manual Contacts Sitting Untouched (New Lead stage)
- First seen: 2026-05-18 (updated run 15)
- Description: 42 total manual contacts. 38 in "New Lead" stage with no outreach logged. 2 "Contacted" (Bulletproof + Damrons — texted today). Pipeline has expanded significantly: 18 gas station companies added today by Danny.
- Priority text list ready: `outputs/vera/priority_outreach_list_2026-05-19.md`
  - Tier 1 (text today): CLE Lawn Care Plus (warm reactivation), Land Pro Management, GTP Landscaping, Twin Improvements, Reliable Roofing, Pagels Construction
  - Tier 2 (text this week): 10 landscapers
  - Tier 3 (next week): 6 construction contractors
- Resolution criteria: Bradley works through Tier 1 by Thursday May 22.

---

## OPEN — Mixmax API blocked in cloud execution environment
- First seen: 2026-05-18
- Workaround: All pipeline scripts return None/safe fallback on 403. nina_report shows explicit API warning.
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
- Run 12 angle: Bridge email from Gmail (not Mixmax) to top 3 is the fastest win this week. Sequence rewrite still needs approval.
- Next steps: Bradley sends bridge email (`outputs/tommy/hot_lead_bridge_email_2026-05-19.md`) to 3 hot leads OR approves sequence rewrite.

---

## OPEN — 13 hot leads sitting uncontacted on LinkedIn
- First seen: 2026-05-18
- Description: 13 contacts with 2+ opens, no replies, no LinkedIn outreach.
- Memorial Day week is peak window — PMs making summer vendor decisions now.
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
- Run 11: Nextdoor templates written. Memorial Day social posts ready.
- Resolution criteria: Bradley posts 1 Facebook post OR creates Nextdoor account.

---

## OPEN — Workiz API blocked in cloud AND 0 power washing jobs on local
- First seen: 2026-05-14
- All code fixes confirmed present. Diagnostic logging active.
- Next step: Bradley checks Workiz for actual JobType field name.

---

## OPEN — Regular Danny PM cron not running (gas stations pulled manually)
- First seen: 2026-05-18 (updated run 15)
- Danny manually pulled gas station leads today (23 contacts, 18 emails). But the regular property manager cron (`lead_pipeline.py both`) has not run since May 13. The weekly PM pull is 6 days overdue.
- Gas station contacts added to pipeline_data.json ✓ but NOT enrolled in Mixmax — no sequence exists yet for this commercial segment.
- Next steps: 
  1. Bradley runs `python3 workers/lead_pipeline.py both` locally to resume PM pipeline
  2. Create gas station Mixmax sequence (see proposal in Slack)

---

## OPEN — Google Business Profile not managed (zero-cost lead channel ignored)
- First seen: 2026-05-18 (run 8)
- Memorial Day execution checklist: upload 1 photo to GBP by Wednesday May 21.
- Resolution: Bradley posts 1 photo to GBP.

---

## OPEN — No review request automation
- First seen: 2026-05-18 (run 8)
- 3-touch sequence written: `outputs/tommy/review_request_sequence_2026-05-18.md`.
- Resolution: Bradley sends review request text after each completed job.

---

## RESOLVED — Ghost fixes pattern: fixes lost in merge conflicts
- Resolved: 2026-05-19 (run 15)
- Run 12 verification: all 29 prior fixes confirmed present.
- Run 13 verification: all 32 prior+new fixes confirmed present.
- Run 15 verification: all fixes confirmed present. No regressions detected.
- Git discipline established: individual file additions (not `git add -A`), descriptive commit messages.

---

## RESOLVED — server.py /api/mixmax/recipients drops dict API response
- Resolved: 2026-05-19 (run 15)
- Fix: Line 193 now normalizes both list and dict responses: `data if isinstance(data, list) else data.get('results', data.get('recipients', []))`. Matches pattern already used in nina_report.py and lead_pipeline.py.
- File: `server.py`

---

## OPEN — Gas station contacts not enrolled in Mixmax (18 emails sitting idle)
- First seen: 2026-05-19 (run 15)
- Description: Danny pulled 23 gas station/c-store contacts today. 18 have verified emails. All added to pipeline_data.json with notes "email sequence pending." BUT no Mixmax sequence exists for this commercial segment yet. The contractor sequence is not the right fit — these are multi-location commercial operators, not referral partners.
- What's ready: Sequence copy written (`outputs/danny/sequence_gas_stations_2026-05-19.md`). Individual contact details in `outputs/danny/leads_gas_stations_2026-05-19.md`.
- Next steps: Bradley creates new Mixmax sequence "Forest City — Gas Station & C-Store Outreach" → paste sequence ID into mixmax.py SEQUENCES dict → Vera adds enrollment logic to lead_pipeline.py in next run.
- Resolution criteria: Sequence ID in SEQUENCES dict + contacts enrolled.

---

## RESOLVED — CONTRACTOR_TITLES missing home-services keywords
- Resolved: 2026-05-19 (run 13)
- Fix: Added chimney, hvac, heating, cooling, air condition, pool service, pool clean, pest control, exterminator, junk removal, home clean, maid, moving company to CONTRACTOR_TITLES. Carla's new search categories now route to contractor sequence correctly.
- File: `integrations/mixmax.py`

---

## RESOLVED — run_carla() zero-lead run produces no log/report-card
- Resolved: 2026-05-19 (run 13)
- Fix: Added `else` block matching Danny's zero-lead fallback. Logs `all leads were duplicates` and sends report_card so the run is visible in Slack.
- File: `workers/lead_pipeline.py`

---

## RESOLVED — DANNY_ORG_KEYWORDS missing commercial real estate segment
- Resolved: 2026-05-19 (run 13)
- Fix: Added 'commercial real estate' and 'commercial property management' to DANNY_ORG_KEYWORDS. Office/retail/warehouse buildings with facility managers were invisible to Apollo org-level filtering.
- File: `workers/lead_pipeline.py`

---

## RESOLVED — run_carla() missing org phone fallback
- Resolved: 2026-05-19 (run 14)
- Fix: `org_id = revealed.get('organization_id', '') or p.get('organization', {}).get('id', '')` — matches Danny's existing fallback. Carla was silently missing org phones when reveal didn't return organization_id.
- File: `workers/lead_pipeline.py`

---

## RESOLVED — workiz_report.py post_to_slack shows $0/$0 on API block
- Resolved: 2026-05-19 (run 14)
- Fix: Added early-return branch in `post_to_slack()` when `not jobs and 'unavailable' in summary`. Shows clear "⚠️ Workiz API unavailable" card with IN PROGRESS status instead of misleading $0 total / $0 outstanding metrics.
- File: `workers/workiz_report.py`

---

*Last updated: 2026-05-19 by Vera Cole (run 15)*
*Key metrics: 37 RESOLVED | 12 OPEN | 2 auto-upgrades this run | 1 new deliverable (priority_outreach_list)*
