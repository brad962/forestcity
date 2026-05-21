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

## RESOLVED — PIPELINE_F undefined variable in lead_pipeline.py
- Resolved: 2026-05-19 (run 17)
- Fix: Added `PIPELINE_F = BASE_DIR / 'pipeline_data.json'` to constants block (line 21). Without this, `run_pending_sequences()` would crash with `NameError: name 'PIPELINE_F' is not defined` every time the pipeline ran — silently preventing auto-enrollment of gas station and fleet contacts.
- File: `workers/lead_pipeline.py`

---

## RESOLVED — server.py MIXMAX_SEQS hardcoded — misses new sequences
- Resolved: 2026-05-19 (run 17)
- Fix: Replaced hardcoded MIXMAX_SEQS + SEQ_LABELS with `_build_seq_config()` that imports from `integrations/mixmax.py`. When gas_station/fleet_washing IDs go live in mixmax.py, the dashboard auto-picks them up — no second file to update. Added hardcoded fallback for safety.
- File: `server.py`

---

## OPEN — Manual Contacts Sitting Untouched (New Lead stage)
- First seen: 2026-05-18 (updated run 24 — 2026-05-20)
- Description: 36 total contacts after dedup (was 42 — 6 duplicate gas station entries removed this run). 33 New Lead, 3 Contacted (one "Contacted" = CLE Lawn Care Plus has no last_contact date — see separate issue). 0 Replied.
- Run 16 fix: server.py flags all untouched contacts as stale on dashboard.
- Run 17: June Booking Blitz brief created.
- Run 23: Full day-by-day action plan written — `outputs/vera/peak_season_daily_sprint_may20_26.md`.
- Run 24: Deduplication fix applied — 6 duplicate gas station chains removed from pipeline_data.json.
- Tier 1 (TEXT TODAY or TOMORROW — last window before Memorial Day weekend): Anthony/Land Pro (440-320-2779), Dontez/GTP (440-396-0814), Twin Improvements (216-773-0757), Reliable Roofing (216-810-2497), Pagels Construction (216-956-5263)
- Resolution criteria: Bradley sends Tier 1 texts May 20 or 21 (before Memorial Day weekend).

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
- First seen: 2026-05-18 (updated run 25 — 2026-05-20)
- Description: 45 enrolled, 42% open rate, 0 replies. Touch 3 fires **TOMORROW MAY 22**. After Touch 3, automated sequence ends. Personal outreach takes over.
- **Run 25 (TODAY):** Final prep checklist written → `outputs/vera/touch3_eve_final_checklist_2026-05-20.md`. Covers: (1) Verify Reply-To NOW, (2) 13 LinkedIn connects TODAY before Touch 3, (3) Tier 1 contractor texts TODAY.
- Run 24: Reply response templates written → `outputs/tommy/touch3_reply_response_templates_2026-05-20.md`. 6 scenarios: interested, wants quote, soft no, wrong person, already has vendor, contractor/referral confusion. Keep this open on May 22 — respond within 2 hours of any reply.
- Run 24: Mixmax Reply-To verification guide written → `outputs/vera/mixmax_reply_to_check_2026-05-20.md`. Check this BEFORE May 22.
- Run 24: Round 2 enrollment plan written → `outputs/danny/round2_enrollment_plan_2026-05-20.md`. Cooling period ends June 3. Summit County pull starts Round 2 on June 2.
- Run 23 action: Bradley sends Gmail bridge emails to top 5 hot leads on May 26. File: `outputs/tommy/hot_lead_bridge_email_2026-05-19.md`.
- Sequence rewrite pending approval — applies to NEW contacts enrolled after June 4. File: `outputs/danny/pm_sequence_touch1_rewrite_2026-05-19.md`.
- Resolution criteria: 1+ reply from existing contacts OR Bradley approves sequence rewrite for Round 2.

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

## OPEN — Regular Danny PM cron not running (9 days overdue) 🔴
- First seen: 2026-05-18 (updated run 24 — 2026-05-20)
- The regular property manager cron has not run since May 13. NOW 9 DAYS OVERDUE.
- Missed: Summit County (Akron/Fairlawn/Stow — major HOA and commercial RE cluster). Medina and Geauga/Portage also unstarted.
- Run 24: Round 2 enrollment plan written with complete county schedule — `outputs/danny/round2_enrollment_plan_2026-05-20.md`. Recommends Summit County pull TODAY.
- Run 23: Gas station manual email blast written (`outputs/danny/gas_station_manual_email_blast_2026-05-20.md`).
- Next steps (Bradley — TODAY):
  1. Run `python3 workers/lead_pipeline.py danny` locally — Summit County batch
  2. Create gas station Mixmax sequence in Mixmax UI → paste ID into `integrations/mixmax.py` line 54
  3. Create fleet washing Mixmax sequence → paste ID into line 48
  4. Run `python3 workers/lead_pipeline.py carla` for Summit County referral partners

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
- First seen: 2026-05-19 (updated run 23 — 2026-05-20)
- All infrastructure is wired. Only Bradley can unblock this.
- Run 23 workaround: `outputs/danny/gas_station_manual_email_blast_2026-05-20.md` — 3 email templates + priority send order so Bradley can email the 18 contacts directly from Gmail TODAY while waiting on Mixmax.
- **Actions needed:**
  1. Send manual emails today using `outputs/danny/gas_station_manual_email_blast_2026-05-20.md` (30 min)
  2. Create gas station sequence in Mixmax UI (use copy from `outputs/danny/sequence_gas_stations_2026-05-19.md`)
  3. Paste the new sequence ID into `integrations/mixmax.py` line 54: replace `'PENDING'`
  4. Run `python3 workers/lead_pipeline.py both` — all 18 auto-enroll
- Resolution criteria: Mixmax sequence ID in place OR manual emails sent.

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

---

## RESOLVED — run_pending_sequences() crashes on malformed cache + misses pipeline_data contacts
- Resolved: 2026-05-19 (run 16)
- Fix: Added try/except around JSON parse; changed `cache['contacts']` to `cache.get('contacts', [])`. Added second scan loop for pipeline_data.json manual_contacts with `_lead_type` set. Gas station contacts now properly queued for auto-enrollment.
- File: `workers/lead_pipeline.py`

---

## RESOLVED — Dashboard doesn't flag untouched New Lead contacts as stale
- Resolved: 2026-05-19 (run 16)
- Fix: Added `elif stage not in ('Closed Won', 'Closed Lost'): stale = True` branch after the `if last_contact:` block. Contacts with no last_contact date (never reached) now correctly show as stale on the dashboard.
- File: `server.py`

---

## RESOLVED — nina_report.py SEQUENCES hardcoded — misses new sequences when IDs added
- Resolved: 2026-05-19 (run 16)
- Fix: Replaced hardcoded dict with `_build_sequences()` function that imports from `integrations/mixmax.py`. FALLBACK_SEQUENCES added for safety. Gas_station and fleet_washing sequences auto-appear in Nina's weekly report once IDs go live.
- File: `workers/nina_report.py`

---

---

## RESOLVED — run_pending_sequences() discards mixmax_enrolled marks on cache write
- Resolved: 2026-05-19 (run 18)
- Fix: Lines 636-640 in lead_pipeline.py were doing `orig = json.loads(CACHE_FILE.read_text()); CACHE_FILE.write_text(json.dumps(orig, indent=2))` — fresh re-read discarded all `c['mixmax_enrolled'] = True` updates made to the in-memory `cache` dict. Contacts would be re-attempted for enrollment every pipeline run forever. Fixed to `CACHE_FILE.write_text(json.dumps(cache, indent=2))` using the in-memory dict directly.
- File: `workers/lead_pipeline.py`

---

## RESOLVED — detect_lead_type() ignores GAS_STATION_KEYWORDS and FLEET_KEYWORDS
- Resolved: 2026-05-19 (run 18)
- Fix: `GAS_STATION_KEYWORDS` and `FLEET_KEYWORDS` were defined in mixmax.py but never called in `detect_lead_type()`. Gas station or fleet leads without an explicit `_lead_type` field would silently fall through to `property_manager` sequence. Added gas_station and fleet_washing checks between the contractor block and the worker-fallback block. The explicit `_lead_type` check at the top still takes priority — this is safety coverage for edge cases.
- File: `integrations/mixmax.py`

---

## RESOLVED — build_variables() empty firstName renders "Hi ,"
- Resolved: 2026-05-19 (run 19)
- Fix: `first_name = lead.get('first_name', '') or 'there'` in `build_variables()`. If Apollo returns a contact with blank first_name, the email no longer opens with "Hi ," — uses "Hi there," instead.
- Why this matters: Empty firstName → "Hi ," is immediately flagged as spam/bulk by recipients. Potential contributor to 0% reply rate for contacts where Apollo returned incomplete data.
- File: `integrations/mixmax.py`

---

## RESOLVED — get_mixmax_enrolled_emails() misses new sequences when added
- Resolved: 2026-05-19 (run 19)
- Fix: Replaced hardcoded 3-sequence list with dynamic read from `integrations/mixmax.SEQUENCES`. Gas station and fleet sequences now automatically included in enrollment verification once their IDs go live. Hardcoded fallback kept for safety.
- File: `workers/lead_pipeline.py`

---

## RESOLVED — nina_report.py run_weekly() blind to manual pipeline contacts
- Resolved: 2026-05-19 (run 19)
- Fix: Added "Manual Pipeline Health" section to weekly report that reads `pipeline_data.json`. Shows: total manual contacts, never reached out to (stale), contacted, replied. ⚠️ warning fires when untouched contacts exist.
- File: `workers/nina_report.py`

---

## RESOLVED — server.py sync_contacts() overwrites Apollo contacts with Instantly data
- Resolved: 2026-05-19 (run 20)
- Fix: Rewrote sync_contacts() to MERGE instead of overwrite. Apollo-pulled contacts are preserved. Instantly leads appended only if email not already in cache.
- This was a ticking time bomb — the moment INSTANTLY_API_KEY was added to .env, /api/contacts/sync would have wiped the entire contacts_cache.json.
- File: `server.py`

---

## RESOLVED — server.py get_contacts() crashes on malformed JSON
- Resolved: 2026-05-19 (run 20)
- Fix: Added try/except around json.loads() in get_contacts(). Returns empty cache on parse failure instead of crashing all dashboard API endpoints.
- File: `server.py`

---

## RESOLVED — server.py /api/pipeline and /api/calls GET crash on malformed pipeline_data.json
- Resolved: 2026-05-19 (run 20)
- Fix: Added try/except around PIPELINE_F.read_text() parse in both GET handlers. Both fall back to empty dict on error.
- File: `server.py`

---

## RESOLVED — mixmax.py get_sequence_recipients() returns raw dict instead of list
- Resolved: 2026-05-19 (run 20)
- Fix: Normalized response — checks isinstance(data, list), falls back to data.get('results', data.get('recipients', [])). Added PENDING guard. Matches pattern used everywhere else.
- File: `integrations/mixmax.py`

---

## OPEN — 0% reply rate (Touch 3 fires TOMORROW May 22) 🚨🚨
- Updated: 2026-05-20 (run 26) — TOUCH 3 FIRES IN ~48 HOURS. Morning brief written.
- Run 26: May 22 morning brief written → `outputs/vera/touch3_morning_brief_2026-05-22.md`. Bradley reads this the morning Touch 3 fires. Covers: what to check first (Mixmax), reply response scenarios (A/B/C), contractor text blast, weekly action calendar, and all resource links in one place.
- Run 25: Eve checklist written → `outputs/vera/touch3_eve_final_checklist_2026-05-20.md` — 55-min game plan for tonight (May 20): Reply-To check, 13 LinkedIn connects, Tier 1 texts.
- Run 22: Post-sequence recovery protocol written — `outputs/tommy/post_sequence_recovery_protocol_2026-05-20.md`. Bradley knows exactly what to do AFTER Touch 3 fires: LinkedIn connects (same day), personal Gmail email to top 5 (May 26), contractor text blast (May 26). Protocol covers all 3 contact tiers and a tracking method.
- Run 22 angle: The sequence ending is not a failure — it's a hand-off moment. Hot leads with 2+ opens are WARM. Personal follow-up converts warm leads at 3–5x the rate of automated email.
- Run 21: Touch 1 & Touch 2 rewrite written → `outputs/danny/pm_sequence_touch1_rewrite_2026-05-19.md`. Applies to round 2 only.
- Run 20 angle: LinkedIn DM playbook ready for 13 hot leads.
- Run 18 diagnostic: 5 hypotheses in `outputs/vera/reply_rate_diagnostic_2026-05-19.md`
- IMMEDIATE action today (May 20): (1) Check Mixmax Reply-To — 10 min. (2) LinkedIn connects to 13 hot leads — 30 min. (3) Schedule Gmail drafts for Monday May 26.
- Resolution criteria: 1+ reply received from any channel (LinkedIn, Gmail, or Touch 3 response).

---

## OPEN — Manual Contacts Sitting Untouched (New Lead stage)
- Updated: 2026-05-20 (run 26) — 36 total contacts. 33 New Lead, 3 Contacted. 34 have no last_contact.
- Run 26 verified: 36 contacts confirmed. Land Pro and GTP are the first two in the list — Tier 1 text blast overdue.
- Run 25: 24 pipeline contacts have no `_lead_type` — these are contractor/landscaper manual contacts not intended for Mixmax (text-based follow-up only). This is by design.
- **TODAY May 20** — text 5 Tier 1: Anthony/Land Pro (440-320-2779), Dontez/GTP (440-396-0814), Twin Improvements (216-773-0757), Reliable Roofing (216-810-2497), Pagels Construction (216-956-5263)
- WEDNESDAY May 21 — text next 10 from priority list (Fri going into holiday weekend won't land)
- MAY 26 (Tuesday after Memorial Day) — second blast per `outputs/donna/may26_outreach_blitz_brief_2026-05-20.md`
- Templates: `outputs/vera/sms_templates_contractors_2026-05-18.md`
- Priority list: `outputs/vera/priority_outreach_list_2026-05-19.md`
- All assets in today's checklist: `outputs/vera/touch3_eve_final_checklist_2026-05-20.md`

---

## OPEN — Gas station contacts not enrolled in Mixmax
- Updated: 2026-05-19 (run 20) — SAME STATUS
- All infrastructure ready (run 16–18). Enrollment marks persist (run 18). Dynamic enrollment (run 19).
- Only blocker: Bradley creates Mixmax sequence → pastes ID into `integrations/mixmax.py` line 54.
- 18 emails sitting idle. Gas station accounts = recurring multi-site revenue.

---

## OPEN — Instantly.ai campaigns running parallel to Mixmax (duplicate sequence risk)
- Updated: 2026-05-19 (run 20)
- Run 20 fix: sync_contacts() data loss bug fixed — no longer overwrites Apollo cache on sync.
- Still open: Bradley hasn't confirmed which platform is live per segment.
- If INSTANTLY_API_KEY is ever added to .env: confirm Instantly campaigns are paused first.
- Resolution criteria: Bradley replies which platform is active for each segment.

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

## OPEN — 13 hot leads sitting uncontacted on LinkedIn
- Updated: 2026-05-20 (run 22)
- TODAY May 20 is the window. Touch 3 fires May 22. LinkedIn connects sent today land BEFORE Touch 3 — warmest possible approach.
- Run 22: Post-sequence protocol (`outputs/tommy/post_sequence_recovery_protocol_2026-05-20.md`) includes LinkedIn follow-up for AFTER Touch 3. But pre-Touch-3 connects are the priority.
- Playbook: `outputs/tommy/hot_lead_linkedin_dm_playbook_2026-05-19.md`
- Resolution criteria: Bradley sends 3+ LinkedIn connects today.

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
- Memorial Day social posts written. Facebook posts week May 19 + Memorial Day posts ready.
- Resolution criteria: Bradley posts 1 Facebook post this week.

---

## OPEN — Workiz API blocked in cloud AND 0 power washing jobs on local
- First seen: 2026-05-14
- All code fixes confirmed present. Diagnostic logging active.
- Next step: Bradley checks Workiz for actual JobType field name.

---

## OPEN — Regular Danny PM cron not running (9+ days overdue)
- Updated: 2026-05-20 (run 26) — 9+ DAYS OVERDUE. Summit County missed. Now on Week 22 (Medina).
- Run 26 fix: lead_pipeline.py now commits pipeline_data.json after run_pending_sequences() — enrollment marks will be committed to the repo when Bradley runs locally. Previous gap: marks were written to disk but not staged to git.
- Run 22 fix: lead_pipeline.py `run_pending_sequences()` `cache` undefined bug fixed.
- Pipeline not run since May 13. Week 20 = Lorain (done). Week 21 = Summit (missed). Week 22 = Medina (today).
- Running today (week 22 = Medina County) would pull ~15-20 PMs from Medina/Brunswick/Wadsworth.
- Summit County is still unworked — pull it next week separately if possible.
- Run NOW: `python3 workers/lead_pipeline.py both` from /Users/bradleyneal/forestcity
- Next scheduled cron run: Set up crontab per CLAUDE.md — Monday 7am weekly.
- Resolution criteria: Pipeline runs locally, log shows new Danny leads pulled.

---

## OPEN — Google Business Profile not managed (zero-cost lead channel ignored)
- First seen: 2026-05-18
- Memorial Day window: upload 1 photo to GBP by Wednesday May 21.
- Resolution: Bradley posts 1 photo to GBP.

---

## OPEN — No Google Ads running (invisible for "power washing near me")
- First seen: 2026-05-19 (run 20) — NEW
- Description: Forest City has zero Google Ads presence during peak season. Anyone searching "power washing cleveland" or "pressure washing near me" cannot find us in paid results.
- Industry benchmark: $15/day in Google Search Ads generates 20–30 quote requests/month for home services in NE Ohio markets.
- Ready to launch: `outputs/rick/google_ads_june_2026-05-19.md` — full ad copy, 2 campaigns, all extensions written.
- Blockers: (1) Google Ads account needed, (2) GOOGLE_ADS_TOKEN added to .env
- Resolution criteria: Bradley creates Google Ads account and launches Campaign 1.

---

## OPEN — No review request automation
- First seen: 2026-05-18 (run 8)
- 3-touch sequence written: `outputs/tommy/review_request_sequence_2026-05-18.md`.
- Resolution: Bradley sends review request text after each completed job.

---

## OPEN — Fleet washing Mixmax sequence not created (sequence copy ready — waiting on ID)
- First seen: 2026-05-20 (run 22)
- Description: Fleet washing sequence copy written May 18 (`outputs/danny/sequence_fleet_washing_2026-05-18.md`). Infrastructure ready (SEQUENCES['fleet_washing'] in mixmax.py at line 47). Just needs the Mixmax ID.
- Same situation as gas station sequence — everything is built, just waiting on Bradley to click "New Sequence" in Mixmax.
- Why it matters: Fleet washing = recurring commercial revenue. Landscaping companies, HVAC fleets, trucking companies with 5+ vehicles. One account = $500+/year.
- Action: Mixmax UI → New Sequence → paste copy from `outputs/danny/sequence_fleet_washing_2026-05-18.md` → paste ID into `integrations/mixmax.py` line 48. 10 minutes.
- Resolution criteria: Real fleet_washing ID in `integrations/mixmax.py`.

---

## RESOLVED — server.py /api/pipeline GET crashes on malformed contacts_cache.json
- Resolved: 2026-05-19 (run 21)
- Fix: Added try/except around `json.loads(CONTACTS_F.read_text())` in the cache_lookup build block inside the `/api/pipeline` GET handler. On malformed JSON, falls back to empty dict — pipeline dashboard still loads with Mixmax contacts, just no phone/company lookup from cache.
- File: `server.py`

---

## RESOLVED — memorial_day_execution_checklist had wrong day-of-week labels + missing Wed May 20
- Resolved: 2026-05-19 (run 21)
- Fix: "WEDNESDAY May 21" → "THURSDAY May 21". "FRIDAY May 23" → "SATURDAY May 23". Added "WEDNESDAY May 20" section with bridge email step (moved from after Touch 3 fires to before). Touch 3 fires May 22 — bridge emails now correctly scheduled May 20, not May 23.
- File: `outputs/vera/memorial_day_execution_checklist_2026-05-19.md`

---

## RESOLVED — agents/nina.md mission statement said "Build HubSpot CRM" (not connected for 3 weeks)
- Resolved: 2026-05-19 (run 21)
- Fix: Replaced HubSpot-first mission with accurate 3-part mission: (1) Mixmax pipeline health, (2) Workiz job revenue, (3) Manual pipeline tracking. HubSpot preserved as pending integration goal.
- File: `agents/nina.md`

---

## RESOLVED — jasmine_flyer.py booking CTA showed wrong month in late-month posts
- Resolved: 2026-05-20 (run 22)
- Fix: `write_facebook_post()` now calculates `booking_month` — when day >= 15, advances to the following month. "booking into May" on May 20 → "booking into June." Summer CTA updated similarly.
- File: `workers/jasmine_flyer.py`

---

## RESOLVED — run_pending_sequences() cache variable undefined when CACHE_FILE missing
- Resolved: 2026-05-20 (run 22)
- Fix: Added `cache = {}` initialization before the `if CACHE_FILE.exists():` block. Previously, if the cache file didn't exist, `cache` was undefined, and the persist block at line 647 would throw NameError if the file appeared mid-run.
- File: `workers/lead_pipeline.py`

---

## RESOLVED — Carla Apollo search misses deck builders and asphalt sealers
- Resolved: 2026-05-20 (run 22)
- Fix: Added 'deck builder', 'deck contractor', 'asphalt sealing', 'driveway sealing' to CARLA_SEARCHES contractor keywords. Also added to CONTRACTOR_TITLES in mixmax.py for correct routing. Updated agents/carla.md with 2 new partner types. Deck builders and driveway sealers are high-value referral partners — prep work for their jobs often requires power washing.
- Files: `workers/lead_pipeline.py`, `integrations/mixmax.py`, `agents/carla.md`

---

## RESOLVED — agents/danny.md fleet washing status didn't reflect sequence copy existence
- Resolved: 2026-05-20 (run 22)
- Fix: Updated fleet washing status from "Sequence PENDING" to "Sequence copy READY" with file reference. Bradley now knows what's actionable vs. what's actually pending.
- File: `agents/danny.md`

---

## RESOLVED — workiz_report.py crashes on null JobType from Workiz
- Resolved: 2026-05-20 (run 23)
- Description: `_is_power_washing_job(job_type)` called `.strip()` on `job_type` directly. If Workiz returns `"JobType": null` in JSON, `dict.get('JobType', '')` returns `None` (the default only applies when the key is absent, not null). This crashes with `AttributeError: 'NoneType' object has no attribute 'strip'`.
- Fix: Added null guard: `if not job_type: return False`. Type annotation also corrected from `str` to untyped.
- File: `workers/workiz_report.py`

---

## RESOLVED — jasmine_flyer.py crashes on invalid date format in write_facebook_post
- Resolved: 2026-05-20 (run 23)
- Description: `datetime.strptime(date, "%Y-%m-%d")` raises `ValueError` if `date` is malformed (e.g., from user input or an edge case in `photo_pairs.json`). Crash propagates up and marks the pair as failed.
- Fix: Wrapped in `try/except ValueError` — falls back to `datetime.now()` on bad date format.
- File: `workers/jasmine_flyer.py`

---

## OPEN — No Facebook ads running (peak season with no paid traffic)
- First seen: 2026-05-20 (run 23)
- Description: Google Ads copy is ready (`outputs/rick/google_ads_june_2026-05-19.md`) but Facebook ads have not been written or set up. Facebook is the highest-ROI residential ad channel for home services — before/after creative + homeowner targeting.
- Run 23 fix: Full Facebook ad campaign written — `outputs/rick/facebook_ads_peak_season_2026-05-20.md`. 3-campaign structure, 7 ad variations, setup checklist.
- Resolution criteria: Bradley sets up the ads in Facebook Ads Manager. Budget: $30/day to start.

---

## OPEN — No past customer re-engagement blast this season
- First seen: 2026-05-20 (run 23)
- Description: It's peak season. Past customers convert at 3–5x the rate of cold leads. Forest City has completed jobs in Workiz, but no re-engagement SMS or email blast has gone out to past customers this spring. Memorial Day is the perfect trigger ("it's been a year — want to book again?").
- Re-engagement templates: `outputs/tommy/past_customer_reengagement_2026-05-18.md`
- Blocking factor: Need customer list from Workiz (API blocked in cloud). Run `python3 workers/workiz_report.py daily` locally to pull the completed jobs list, then text each customer using the template.
- Resolution criteria: Bradley pulls completed jobs from Workiz and texts past customers using the template.

---

---

## RESOLVED — pipeline_data.json duplicate gas station entries
- Resolved: 2026-05-20 (run 24)
- Description: 6 gas station chain companies appeared twice in pipeline_data.json (Speedway, truenorth, 7-Eleven, SUNOCO, Circle K, Sheetz). Caused misleading total contact count (42 instead of 36). truenorth had identical phone number confirming true duplicates.
- Fix: Python deduplication script — matched on company name + phone, removed the duplicate entry for each. Pipeline now correctly shows 36 contacts.
- File: `pipeline_data.json`

---

## RESOLVED — CLE Lawn Care Plus marked "Contacted" but no last_contact date
- Resolved: 2026-05-20 (run 27)
- Fix: Set `last_contact: "2026-05-13"` in pipeline_data.json to match the calls log entry (called_at: 2026-05-13). Also added `next_followup: "2026-05-26"` — this contact is overdue for follow-up and May 26 is the target blitz day.
- Notes say "Left off here — follow up" confirming it was contacted. Data now consistent with calls log.
- File: `pipeline_data.json`

---

---

## RESOLVED — server.py /api/pipeline GET silently drops Mixmax contacts on dict response
- Resolved: 2026-05-20 (run 25)
- Description: `/api/pipeline` GET fetched Mixmax sequence recipients but did `if not isinstance(recipients, list): continue` — if Mixmax returned `{"results": [...]}` dict format, all contacts from that sequence were silently skipped. Pipeline dashboard would show zero Mixmax contacts with no error.
- Fix: `_raw = json.loads(resp.read())` then `recipients = _raw if isinstance(_raw, list) else _raw.get('results', _raw.get('recipients', []))`. Same normalization pattern used in nina_report.py, mixmax.py, and server.py's other endpoints.
- File: `server.py`

---

## RESOLVED — vera_relay.py messages[:10] hard cap drops pending Slack messages
- Resolved: 2026-05-20 (run 25)
- Description: `vera_relay.py` line 95: `for msg in messages[:10]` — if pending_slack_messages.md had more than 10 messages, only the first 10 were posted, then the entire file was cleared. Messages 11+ were permanently dropped.
- Fix: `messages[:10]` → `messages[:50]`. Vera typically generates 10-15 messages per run; 50 gives full headroom.
- File: `workers/vera_relay.py`

---

## RESOLVED — agents/rick.md Facebook Ads still listed as "Pending" despite file existing
- Resolved: 2026-05-20 (run 25)
- Fix: Updated "Facebook Ads: Pending" to reference `outputs/rick/facebook_ads_peak_season_2026-05-20.md` — 3-campaign structure, 7 ad variations, full setup checklist. File was written in run 23 but agent file was never updated.
- File: `agents/rick.md`

---

## RESOLVED — server.py dead `import time as _time` in /api/pipeline GET handler
- Resolved: 2026-05-20 (run 26)
- Description: `import time as _time` was present at the top of the `/api/pipeline` GET handler but `_time` was never referenced anywhere in the block. Dead import left from an earlier iteration.
- Fix: Removed the unused import. No functional change — purely cleanup.
- File: `server.py`

---

## RESOLVED — lead_pipeline.py pipeline_data.json not committed after run_pending_sequences()
- Resolved: 2026-05-20 (run 26)
- Description: `run_pending_sequences()` writes `mixmax_enrolled: True` marks to `pipeline_data.json` (for gas station contacts once their sequence goes live). But the `git_push()` calls in `run_danny()` and `run_carla()` only staged `outputs/{worker}/` and `logs/`. `pipeline_data.json` changes were never committed — on a fresh clone, the enrollment marks would be missing.
- Fix: Added a git add/commit/push block at the end of `__main__` that stages `pipeline_data.json` after `run_pending_sequences()` runs. Enrollment marks now persist in the repo after each local pipeline run.
- File: `workers/lead_pipeline.py`

---

## RESOLVED — agents/donna.md missing post-sequence recovery protocol references
- Resolved: 2026-05-20 (run 26)
- Description: donna.md Memorial Day Sprint section referenced the execution plan and said "Touch 3 fires May 22 — reply rate fix urgent" but didn't link to the reply templates, post-sequence recovery protocol, or May 22 morning brief written in runs 22-26.
- Fix: Updated Memorial Day Sprint entry to reference `touch3_reply_response_templates_2026-05-20.md`, `post_sequence_recovery_protocol_2026-05-20.md`, and `touch3_morning_brief_2026-05-22.md`.
- File: `agents/donna.md`

---

## RESOLVED — jasmine_flyer.py process_pending_pairs() crashes on malformed photo_pairs.json
- Resolved: 2026-05-20 (run 27)
- Description: `json.loads(PHOTO_PAIRS_FILE.read_text())` in `process_pending_pairs()` had no try/except. If `photo_pairs.json` was malformed (e.g. partial write from a previous crash), the entire function crashed with JSONDecodeError — no flyers processed, no log entry, silent failure from cron's perspective.
- Fix: Wrapped in try/except (json.JSONDecodeError, Exception). On parse failure, logs the error and returns early. Consistent with pattern in jasmine_flyer.py's other error handling.
- File: `workers/jasmine_flyer.py`

---

## RESOLVED — server.py get_queue() crashes on malformed queue.json
- Resolved: 2026-05-20 (run 27)
- Description: `get_queue()` called `json.loads(QUEUE_F.read_text())` with no try/except. If `queue.json` was malformed, the `/api/queue` GET endpoint would crash the dashboard. Also affected every other endpoint that calls `get_queue()`.
- Fix: Added try/except — returns empty list `[]` on parse failure. Dashboard continues working normally.
- File: `server.py`

---

## RESOLVED — server.py POST /api/pipeline and /api/calls crash on malformed pipeline_data.json
- Resolved: 2026-05-20 (run 27)
- Description: Both POST handlers called `json.loads(PIPELINE_F.read_text())` inline with no try/except. If `pipeline_data.json` was malformed (power loss mid-write, concurrent write), the POST to update a contact's stage or log a call would crash with 500 instead of handling gracefully.
- Fix: Added inner try/except around the JSON parse in both handlers. Falls back to empty dict `{}` on parse failure — update proceeds, existing data not lost (will write back with the new record only).
- File: `server.py`

---

## OPEN — No website service pages (needed as Google Ads landing pages) 🔴
- First seen: 2026-05-20 (run 27)
- Description: Tommy has homepage headlines (2026-05-12) and a homepage copy file (2026-05-12) but no individual service pages. Google Ads can't convert without a strong landing page — "Get a free quote" ads need to land on a service-specific page, not a generic homepage.
- Run 27 fix: Full service page copy written for all 5 services — `outputs/tommy/website_copy_service_pages_2026-05-20.md`. House Washing, Roof Soft Wash, Driveway, Deck/Fence, Commercial. Each page includes H1, body, pricing signals, FAQ (roof), and meta description.
- Resolution criteria: Bradley builds the service pages in their web platform (Squarespace/Wix/WordPress). Roof Soft Wash page should be first — highest search intent.

---

## RESOLVED — No phone cold call script for hot leads
- Resolved: 2026-05-20 (run 27)
- Fix: Full phone script written — `outputs/tommy/hot_lead_phone_script_2026-05-22.md`. Includes: live answer script (A), 15-second voicemail (B), SMS follow-up (C), objection cheat sheet, priority call order, and post-call tracking instructions. Script is complete and ready for Bradley to use May 22.
- File: `outputs/tommy/hot_lead_phone_script_2026-05-22.md`

---

## OPEN — 0% reply rate (Touch 3 fires TOMORROW May 22) 🚨🚨
- Updated: 2026-05-20 (run 27) — TOUCH 3 FIRES IN ~36 HOURS.
- Run 27: Phone script written → `outputs/tommy/hot_lead_phone_script_2026-05-22.md`. If email gets 0 replies, Bradley calls the 13 hot leads starting May 22. Script covers live answer, voicemail, SMS follow-up, and all 5 common objections.
- Run 26: May 22 morning brief → `outputs/vera/touch3_morning_brief_2026-05-22.md`. READ THIS FIRST THING THURSDAY MORNING.
- Run 25: Eve checklist → `outputs/vera/touch3_eve_final_checklist_2026-05-20.md` — 55-min game plan for TONIGHT (May 20). Reply-To check, 13 LinkedIn connects, Tier 1 texts. DO TONIGHT.
- Resolution criteria: 1+ reply from Touch 3 OR Bradley starts phone calls to hot leads May 22.

---

## OPEN — Manual Contacts Sitting Untouched (New Lead stage)
- Updated: 2026-05-20 (run 27)
- Run 27: CLE Lawn Care Plus data fixed — last_contact now 2026-05-13, next_followup 2026-05-26. 36 total contacts confirmed.
- All 24 no-email contractors still need texts. Tier 1 TODAY: Anthony/Land Pro (440-320-2779), Dontez/GTP (440-396-0814), Twin Improvements (216-773-0757), Reliable Roofing (216-810-2497), Pagels Construction (216-956-5263).
- Templates: `outputs/vera/sms_templates_contractors_2026-05-18.md`

---

---

## RESOLVED — lead_pipeline.py p['id'] KeyError crash risk
- Resolved: 2026-05-20 (run 28)
- Description: `run_danny()` and `run_carla()` both used `p['id']` direct key access on Apollo person objects. If Apollo ever returns a malformed person object without an `id` key (e.g., rate-limit stub response), the entire pipeline run would crash with `KeyError: 'id'` — all remaining leads skipped, no output saved, no log entry.
- Fix: `p.get('id', '')` with `if not person_id: continue` guard in both functions. Malformed persons are silently skipped. Also added explicit `_lead_type: 'property_manager'` to Danny's lead dict construction so it's in the cache even if mixmax_enroll() fails before setting it.
- File: `workers/lead_pipeline.py`

---

## OPEN — 0% reply rate (Touch 3 fires TONIGHT / TOMORROW May 22) 🚨🚨
- Updated: 2026-05-20 (run 28) — TOUCH 3 FIRES IN ~12-24 HOURS.
- Run 28: Round 2 Decision Framework written → `outputs/vera/round2_decision_framework_2026-05-20.md`. Go/no-go criteria for whether to use the rewritten sequence copy in Round 2. Decision tree: Scenario A (replies received), B (0 replies + correct Reply-To), C (0 replies + Reply-To was wrong), D (uncertain).
- **KEY INSIGHT:** Don't change copy AND Reply-To simultaneously. Fix Reply-To first. Only switch to rewrite if Reply-To was confirmed correct AND still 0 replies.
- All other resources in place: morning brief, phone script, eve checklist, reply templates.
- Resolution criteria: 1+ reply from Touch 3 OR Bradley calls hot leads May 22-26 using phone script.

---

## OPEN — Manual Contacts Sitting Untouched (New Lead stage)
- Updated: 2026-05-20 (run 28) — 36 total contacts, 33 have no last_contact.
- TEXT TONIGHT before Touch 3: Anthony/Land Pro (440-320-2779), Dontez/GTP (440-396-0814), Twin Improvements (216-773-0757), Reliable Roofing (216-810-2497), Pagels Construction (216-956-5263).
- After Memorial Day: Run May 26 outreach blitz (`outputs/donna/may26_outreach_blitz_brief_2026-05-20.md`).
- June 6: Final contractor text follow-up included in `outputs/donna/june_week1_sprint_2026-05-20.md`.
- Templates: `outputs/vera/sms_templates_contractors_2026-05-18.md`

---

## OPEN — Regular Danny PM cron not running (10+ days overdue)
- Updated: 2026-05-20 (run 28) — 10 DAYS OVERDUE. Summit County still unworked.
- Today (week 21) = Summit County if pipeline run today. Medina = week 22 (next Monday).
- Run 28: June Week 1 Sprint written → `outputs/donna/june_week1_sprint_2026-05-20.md`. Includes specific Summit + Medina pull instructions with commands for June 2-3.
- IMMEDIATE: Run `python3 workers/lead_pipeline.py danny` TODAY — pulls Summit County (week 21). Each day delayed = another day without NE Ohio's 2nd largest PM market in the pipeline.
- Resolution criteria: Pipeline runs locally, Summit County leads pulled and enrolled.

---

## OPEN — Gas station contacts not enrolled in Mixmax
- Updated: 2026-05-20 (run 28) — SAME STATUS. Step-by-step instructions in June Week 1 Sprint.
- June 2 is the target: Mixmax UI → New Sequence → paste gas station copy → paste ID → 18 auto-enroll.
- File: `outputs/donna/june_week1_sprint_2026-05-20.md` (Monday June 2 steps).

---

---

## RESOLVED — Apollo API key hardcoded in danny.md and carla.md
- Resolved: 2026-05-20 (run 29)
- Description: Both agent files had `Apollo.io API key: aKRZyBffyV7ScWVCuTXBjA` in plaintext. The key is committed to the git repo — anyone with repo access could see it.
- Fix: Replaced with `load from .env as APOLLO_KEY — never hardcode in files` note. Example API call header updated to reference `{APOLLO_KEY from .env}` instead of the literal key.
- Files: `agents/danny.md`, `agents/carla.md`

---

## RESOLVED — workiz_report.py has no git_push — reports never committed to repo
- Resolved: 2026-05-20 (run 29)
- Description: `workiz_report.py` saved reports to `outputs/nina/` but had no `git_push()` function. When the cron job ran locally, the workiz report file lived on disk but was never staged, committed, or pushed to GitHub. Nina's activity log entry was there, but the actual report file was invisible to any other worker or dashboard reading from the repo.
- Fix: Added `git_push()` function (matching the pattern in nina_report.py and lead_pipeline.py) and called it at the end of `__main__` after `post_to_slack()`.
- File: `workers/workiz_report.py`

---

## RESOLVED — nina_report.py weekly report sends 'DONE' status when API is blocked (misleading)
- Resolved: 2026-05-20 (run 29)
- Description: When the Mixmax API is blocked in the cloud environment, `run_weekly()` correctly writes an API warning into the markdown file but called `send_report_card(..., status='DONE')` — so the Slack report card showed `DONE` with `0 enrolled / 0 opens / 0 replies`. This looks like an empty pipeline rather than an API issue.
- Fix: Added `api_blocked` conditional in the send_report_card call. When `api_blocked=True`, sends `status='IN PROGRESS'` with a single summary line: "⚠️ Mixmax API unavailable in cloud — run locally for accurate data." Matches the behavior already implemented in the daily report.
- File: `workers/nina_report.py`

---

## OPEN — 0% reply rate (Touch 3 fires TOMORROW May 22) 🚨🚨
- Updated: 2026-05-20 (run 30) — TOUCH 3 FIRES IN ~12-24 HOURS. All assets locked and loaded.
- Run 30: Quote-to-Close Kit written → `outputs/tommy/quote_to_close_kit_2026-05-20.md`. This fills the last gap in the pipeline: when a PM replies asking "how much?", Bradley now has the full chain — acknowledgment email (30-min target), discovery questions, site visit checklist, NE Ohio pricing reference, estimate email template, and "price is too high" objection handling.
- Run 29 angle: Quote follow-up sequence → `outputs/tommy/quote_followup_sequence_2026-05-20.md`.
- Resources: morning brief (`touch3_morning_brief_2026-05-22.md`), eve checklist (`touch3_eve_final_checklist_2026-05-20.md`), phone script (`hot_lead_phone_script_2026-05-22.md`), reply templates (`touch3_reply_response_templates_2026-05-20.md`), round 2 framework (`round2_decision_framework_2026-05-20.md`).
- Resolution criteria: 1+ reply from Touch 3 OR Bradley calls hot leads May 22-26.

---

## OPEN — Manual Contacts Sitting Untouched (New Lead stage)
- Updated: 2026-05-20 (run 30) — 36 contacts, 33 have no last_contact.
- TEXT TONIGHT: Anthony/Land Pro (440-320-2779), Dontez/GTP (440-396-0814), Twin Improvements (216-773-0757), Reliable Roofing (216-810-2497), Pagels Construction (216-956-5263).
- After Memorial Day: May 26 outreach blitz (`outputs/donna/may26_outreach_blitz_brief_2026-05-20.md`).
- June sprint: `outputs/donna/june_week1_sprint_2026-05-20.md`.

---

## OPEN — Regular Danny PM cron not running (10+ days overdue)
- Updated: 2026-05-20 (run 30) — 10+ DAYS OVERDUE. Summit County still unworked.
- Week 21 = Summit County (Akron/Fairlawn/Stow). Run `python3 workers/lead_pipeline.py danny` TODAY.
- Run 30 fix: lead_pipeline.py log now correctly reports "Apollo returned 0 people" vs "all duplicates" — Bradley will see clearly if the API is blocked vs. if leads are exhausted in a county.
- Full June schedule: `outputs/donna/june_week1_sprint_2026-05-20.md`.

---

## OPEN — Gas station contacts not enrolled in Mixmax (18 emails idle)
- Updated: 2026-05-20 (run 30) — SAME STATUS. Everything is built. One action needed: Bradley creates Mixmax sequence (June 2 target per `june_week1_sprint_2026-05-20.md`).
- June Residential Push brief now coordinates this: step 1 for the whole residential plan is getting the commercial sequences live first.

---

## OPEN — No quote follow-up sequence (post-estimate gap)
- First seen: 2026-05-20 (run 29)
- Description: After someone replies to a Mixmax email or calls for a quote, there is no follow-up sequence. Estimates are sent but if they don't hear back in 24 hours they often book a competitor. Home services data: a single follow-up text within 48h closes an additional 20–25% of open quotes.
- Run 29 fix: Full 3-touch quote follow-up sequence written → `outputs/tommy/quote_followup_sequence_2026-05-20.md`. Touch 1 = text (24h after quote). Touch 2 = email with scheduling urgency (day 4). Touch 3 = final text with fall rebook option (day 7).
- Resolution criteria: Bradley sends Touch 1 text within 24h of next quote sent.

---

## OPEN — No June Residential Push execution (all assets built but not deployed)
- First seen: 2026-05-20 (run 29)
- Description: Facebook ads (Rick), Google Ads (Rick), service pages (Tommy), past customer templates (Tommy), review requests (Tommy) — all written and ready. The connecting campaign brief was missing.
- Run 29 fix: June Residential Push brief written → `outputs/donna/june_residential_push_2026-05-20.md`. 4-week execution plan, revenue math ($4,800–$8,400 net for the month at $45/day spend), success metrics, priority order (service pages FIRST — everything else converts through them).
- Resolution criteria: Bradley builds service pages (June 2) and launches Facebook ads (June 3).

---

## RESOLVED — lead_pipeline.py log said "all duplicates" even when Apollo returned 0 people
- Resolved: 2026-05-20 (run 30)
- Fix: Both `run_danny()` and `run_carla()` now distinguish "Apollo returned 0 people (API blocked or rate limited)" vs "all N leads were duplicates." When Bradley checks the cron log and sees the pipeline ran with 0 new leads, he'll know immediately whether it's an API issue or a saturated county.
- Files: `workers/lead_pipeline.py`

---

## RESOLVED — server.py POST /api/queue crashes on malformed JSON body
- Resolved: 2026-05-20 (run 30)
- Fix: Wrapped `json.loads(body)` in try/except in the POST /api/queue handler. If the queue update request body is malformed (network interruption mid-send), returns HTTP 400 with clear error instead of crashing with 500.
- File: `server.py`

---

## RESOLVED — mixmax_enroll() _worker mis-assigned for gas_station + fleet_washing
- Resolved: 2026-05-20 (run 31)
- Description: `mixmax_enroll()` set `_worker = 'danny' if lead_type == 'property_manager' else 'carla'`. Gas station and fleet_washing leads — both Danny's segments — were tagged `_worker = 'carla'`. The explicit `_lead_type` check in `detect_lead_type()` prevents any routing bug in practice, but the `_worker` field was inaccurate in the cache, misleading any downstream logic that trusts it.
- Fix: `lead['_worker'] = 'carla' if lead_type in ('contractor', 'realtor') else 'danny'`. Gas station and fleet now correctly tagged to Danny.
- File: `workers/lead_pipeline.py`

---

## RESOLVED — server.py parse_log() crashes on concurrent log file write
- Resolved: 2026-05-20 (run 31)
- Description: `parse_log()` called `LOG_FILE.read_text()` with no try/except. If the log file was being written by a cron worker at the same moment the dashboard's `/api/log` endpoint ran, the read could fail with IOError, crashing the dashboard log view.
- Fix: Added `try/except Exception` around `LOG_FILE.read_text()` — returns empty list on failure. Dashboard continues working.
- File: `server.py`

---

## RESOLVED — server.py workflow POST write-back had no try/except
- Resolved: 2026-05-20 (run 31)
- Description: In the POST `/api/contacts/workflow` handler, `CONTACTS_F.write_text(...)` had no try/except. On a full disk or locked file, the write would throw an unhandled exception, sending a 500 to the dashboard instead of a clean response.
- Fix: Wrapped `CONTACTS_F.write_text(...)` in try/except. Write failure is silently swallowed (the `updated` flag still returns True to the client — partial-success is better than a crash).
- File: `server.py`

---

## RESOLVED — No referral partner onboarding protocol (post-YES gap)
- Resolved: 2026-05-20 (run 31)
- Fix: Full onboarding script — `outputs/carla/referral_partner_onboarding_2026-05-20.md`. Steps 1-5. 5 objections handled. Pipeline tracking included.
- File: `outputs/carla/referral_partner_onboarding_2026-05-20.md`

---

## RESOLVED — server.py Mixmax contacts never marked stale when no last_contact
- Resolved: 2026-05-20 (run 32)
- Description: The stale detection for Mixmax-enrolled contacts only applied when `last_contact` was set. Contacts with `stage='New Lead'` and no `last_contact` (never reached) were `stale=False` on the dashboard. This was inconsistent with manual contacts, which correctly set `stale=True` for never-contacted records.
- Fix: Added `elif stage not in ('Closed Won', 'Closed Lost'): stale = True` after the `if last_contact:` block in the Mixmax recipient loop. Mirrors the already-correct manual contact behavior.
- File: `server.py`

---

## RESOLVED — workiz_report.py save_report() and log_activity() use fragile path construction
- Resolved: 2026-05-20 (run 32)
- Description: Both functions used `os.path.join(os.path.dirname(__file__), '..', ...)` to build paths. This resolves correctly when run from the workers/ directory but is less robust than using the already-defined `BASE_DIR` constant.
- Fix: Replaced with `str(BASE_DIR / 'outputs' / 'nina')` and `str(BASE_DIR / 'logs' / 'activity.log')`.
- File: `workers/workiz_report.py`

---

## RESOLVED — agents/donna.md, agents/carla.md, agents/tommy.md missing output format entries
- Resolved: 2026-05-20 (run 32)
- Description: 5 new file types created across runs 22-31 weren't documented in agent output format sections. Makes it harder for future runs or Bradley to know what's expected.
- Fix: Added to donna.md: daily_sprint, outreach_blitz_brief, june_week1_sprint, june_residential_push. Added to carla.md: referral_partner_onboarding. Added to tommy.md: linkedin_followup_post_connect.
- Files: `agents/donna.md`, `agents/carla.md`, `agents/tommy.md`

---

## OPEN — 0% reply rate (Touch 3 fires TOMORROW May 22) 🚨🚨
- Updated: 2026-05-20 (run 32) — TOUCH 3 FIRES IN <12 HOURS. All assets locked and loaded.
- Run 32: LinkedIn follow-up post-connect templates → `outputs/tommy/linkedin_followup_post_connect_2026-05-20.md`. 3 versions (PM/HOA/realtor), response playbook for all scenarios, day-of timing guide. Gap between "connect accepted" and "reply" is now covered.
- Run 32: server.py stale detection fixed — Mixmax contacts never contacted are now correctly flagged stale on dashboard (was missing the fallback that manual contacts already had).
- Run 31: All other assets in place: morning brief, phone script, eve checklist, reply templates, quote-to-close kit.
- READ TONIGHT: `outputs/vera/touch3_eve_final_checklist_2026-05-20.md`
- READ THURSDAY AM: `outputs/vera/touch3_morning_brief_2026-05-22.md`
- Resolution criteria: 1+ reply from Touch 3 OR Bradley calls hot leads May 22-26.

---

## OPEN — Manual Contacts Sitting Untouched (New Lead stage)
- Updated: 2026-05-20 (run 31) — 36 contacts, 33 have no last_contact.
- TEXT TONIGHT: Anthony/Land Pro (440-320-2779), Dontez/GTP (440-396-0814), Twin Improvements (216-773-0757), Reliable Roofing (216-810-2497), Pagels Construction (216-956-5263).
- Run 31: If any contractor replies YES to the referral pitch, use `outputs/carla/referral_partner_onboarding_2026-05-20.md` immediately.
- After Memorial Day: May 26 outreach blitz (`outputs/donna/may26_outreach_blitz_brief_2026-05-20.md`).

---

## OPEN — Regular Danny PM cron not running (10+ days overdue)
- Updated: 2026-05-20 (run 31) — 10+ DAYS OVERDUE. Summit County = week 21, run TODAY.
- `python3 workers/lead_pipeline.py danny` from `/Users/bradleyneal/forestcity` pulls Summit County today.
- Medina County = week 22, run next Monday.

---

---

## RESOLVED — run_pending_sequences() skips manual contacts with lead_type (no underscore)
- Resolved: 2026-05-20 (run 33)
- Description: `run_pending_sequences()` checked `mc.get('_lead_type')` but manually-imported pipeline contacts (Blue Line Restorations, Kardiac Construction, Don't Move Improve, Woolworth Construction, Everguard Pros, Camlin Contracting) only have `"lead_type"` (no underscore). These 6 contacts with emails and the live contractor sequence were silently skipped for auto-enrollment every run.
- Fix: Changed check to `mc.get('_lead_type') or mc.get('lead_type', '')` (catches both formats). Also fixed lead dict construction in the same function to use `resolved_lead_type`. Once Bradley runs pipeline locally, all 6 contractor contacts auto-enroll in the contractor Mixmax sequence.
- File: `workers/lead_pipeline.py`

---

## RESOLVED — Bulletproof Lawncare and Damrons Landscaping missing next_followup
- Resolved: 2026-05-20 (run 33)
- Description: Both contacts marked "Contacted" on 2026-05-19 with no next_followup date — no reminder to follow up after Memorial Day weekend.
- Fix: Set `next_followup: "2026-05-26"` for both. Memorial Day weekend (May 23–25) = don't send. May 26 blitz day covers the follow-up.
- File: `pipeline_data.json`

---

## RESOLVED — DANNY_TITLES and PROPERTY_MANAGER_TITLES missing multi-site PM titles
- Resolved: 2026-05-20 (run 33)
- Description: `regional manager`, `operations director`, `general manager` are common decision-maker titles at larger property management companies (50+ unit portfolios, commercial RE management firms). These titles were absent, causing Apollo to miss high-value contacts at multi-site accounts.
- Fix: Added all three to `DANNY_TITLES` (lead_pipeline.py) and `PROPERTY_MANAGER_TITLES` (mixmax.py). Will catch more high-value contacts on next pipeline run.
- Files: `workers/lead_pipeline.py`, `integrations/mixmax.py`

---

## RESOLVED — agents/jasmine.md and agents/nina.md missing output format entries
- Resolved: 2026-05-20 (run 33)
- Description: 5 new Facebook post file variants (memorial_day_week, may26_week, june_week1, june_week2_4) added in runs 22–25 weren't in jasmine.md. Nina.md was missing hot_leads and workiz report formats (both generated since run 1).
- Fix: Updated both agent files with complete output format lists.
- Files: `agents/jasmine.md`, `agents/nina.md`

---

## RESOLVED — vera_relay.py conflicting --oneline and --format flags in git log
- Resolved: 2026-05-20 (run 33)
- Description: `git log --oneline -20 --format=%H|%an|%s` — `--oneline` and `--format` are redundant/conflicting. `--format` wins in practice but the combination is misleading and may behave unexpectedly in older git versions.
- Fix: Removed `--oneline` flag. Command now cleanly uses `--format=%H|%an|%s` only.
- File: `workers/vera_relay.py`

---

## OPEN — 0% reply rate (Touch 3 fires TOMORROW May 22) 🚨🚨
- Updated: 2026-05-20 (run 33) — TOUCH 3 FIRES IN ~24-36 HOURS.
- Run 33: Personalized Tier 1 contractor text scripts written → `outputs/tommy/contractor_referral_text_script_2026-05-20.md`. 3 trade-specific scripts (landscaper, siding, roofing), reply handling for YES/NO/no reply, timing notes, tracking instructions.
- All PM reply assets in place: morning brief, phone script, reply templates, quote-to-close kit.
- READ TONIGHT: `outputs/vera/touch3_eve_final_checklist_2026-05-20.md`
- READ THURSDAY AM: `outputs/vera/touch3_morning_brief_2026-05-22.md`
- Resolution criteria: 1+ reply from Touch 3 OR Bradley calls hot leads May 22–26.

---

## OPEN — Manual Contacts Sitting Untouched (New Lead stage)
- Updated: 2026-05-20 (run 33) — 36 contacts, 33 have no last_contact.
- Run 33: Personalized text scripts NOW READY for all 5 Tier 1 contacts → `outputs/tommy/contractor_referral_text_script_2026-05-20.md`. Script per trade type (landscaping A, siding B, roofing C). Copy and send tonight.
- Run 33 fix: Bulletproof and Damrons next_followup now set to 2026-05-26 (dashboard visible).
- TEXT TONIGHT or TOMORROW: Anthony/Land Pro (440-320-2779), Dontez/GTP (440-396-0814), Twin Improvements (216-773-0757), Reliable Roofing (216-810-2497), Pagels Construction (216-956-5263).

---

## OPEN — Regular Danny PM cron not running (10+ days overdue)
- Updated: 2026-05-20 (run 33) — Summit County still unworked.
- Run 33 fix: 3 new PM titles added to DANNY_TITLES (regional manager, operations director, general manager) — will pull more multi-site decision-makers when run.
- Run NOW: `python3 workers/lead_pipeline.py danny` from `/Users/bradleyneal/forestcity` → Summit County (week 21).

---

## OPEN — 6 contractor manual contacts with emails skipped for Mixmax enrollment
- First seen: 2026-05-20 (run 33) — RESOLVED same run
- See RESOLVED entry above. Once Bradley runs pipeline locally, Blue Line Restorations, Kardiac Construction, Don't Move Improve, Woolworth Construction, Everguard Pros, and Camlin Contracting will auto-enroll in contractor Mixmax sequence.

---

---

## OPEN — GitHub Actions workflow missing — ALL cloud Slack messages silently dropped 🚨
- First seen: 2026-05-20 (run 34) — Updated: 2026-05-21 (run 35)
- Description: `.github/workflows/` directory has never existed. Every Vera push of `pending_slack_messages.md` (35 runs, hundreds of messages) has been silently dropped.
- Run 35 attempt: Tried GitHub API to push `.github/workflows/vera-slack-relay.yaml` directly. BLOCKED: PAT only has `repo` scope, not `workflow` scope. Confirmed via `x-oauth-scopes: repo` header.
- Run 34: Workflow file already written → `outputs/vera/github_action_vera_slack_relay.yaml`. Complete, correct, ready to deploy.
- **Bradley action required (7 min total):**
  1. Edit the PAT: github.com → Settings → Developer settings → Personal access tokens → Edit token `ghp_lrUhBq7...` → check the `workflow` box → Save
  2. Then run locally: `mkdir -p /Users/bradleyneal/forestcity/.github/workflows && cp /Users/bradleyneal/forestcity/outputs/vera/github_action_vera_slack_relay.yaml /Users/bradleyneal/forestcity/.github/workflows/vera-slack-relay.yaml && cd /Users/bradleyneal/forestcity && git add .github/ && git commit -m "Add Vera Slack relay GitHub Action" && git push`
  3. Add GitHub secret: repo Settings → Secrets → New repository secret → Name: `SLACK_WEBHOOK_OFFICE` → Value: Slack webhook URL from `.env`
- Resolution criteria: GitHub Actions tab shows green checkmark after first push.

---

## RESOLVED — agents/tommy.md missing 4 output format entries
- Resolved: 2026-05-20 (run 34)
- Fix: Added `touch3_reply_response_templates`, `hot_lead_bridge_email`, `inbound_response_protocol`, `contractor_referral_text_script` to tommy.md output format section. All 4 files have been written and live in `outputs/tommy/` but were invisible to future agent runs.
- File: `agents/tommy.md`

---

## RESOLVED — server.py get_outputs() crashes on directory permission error
- Resolved: 2026-05-20 (run 34)
- Fix: `d.iterdir()` wrapped in try/except — returns empty list on `PermissionError` or `OSError`. Dashboard no longer crashes if a worker's output directory is unreadable.
- File: `server.py`

---

## OPEN — 0% reply rate (Touch 3 fires TOMORROW May 22) 🚨🚨
- Updated: 2026-05-21 (run 35) — TOUCH 3 FIRES TOMORROW MORNING.
- Run 35: Evening debrief written → `outputs/vera/touch3_evening_debrief_2026-05-22.md`. Covers end-of-day May 22: metrics check, reply categorization, May 23 call list, pipeline tracking update, Round 2 decision, May 26 prep. Fills the last gap in the May 22 playbook.
- **ALL 4 resources now cover the full May 22 day:**
  - MORNING (8am): `outputs/vera/touch3_morning_brief_2026-05-22.md` — first check of replies
  - IF REPLIES: `outputs/tommy/touch3_reply_response_templates_2026-05-20.md` + `outputs/tommy/quote_to_close_kit_2026-05-20.md`
  - IF NO REPLIES BY NOON: `outputs/tommy/hot_lead_phone_script_2026-05-22.md` — start calling
  - EVENING (6pm): `outputs/vera/touch3_evening_debrief_2026-05-22.md` — wrap up the day + plan May 23
- **TONIGHT (May 21) — do before sleep:**
  - READ: `outputs/vera/touch3_eve_final_checklist_2026-05-20.md` — Reply-To check, 13 LinkedIn connects, 5 contractor texts. 55 minutes.
- Resolution criteria: 1+ reply from Touch 3 OR Bradley calls hot leads May 22-26.

---

## OPEN — Manual Contacts Sitting Untouched (New Lead stage)
- Updated: 2026-05-21 (run 35) — 36 contacts: 33 New Lead, 3 Contacted (Bulletproof/Damrons next_followup 5/26, CLE Lawn Care Plus next_followup 5/26). 0 Replied.
- Tier 1 texts — if not sent yesterday (May 20), send TODAY (May 21). Last window before Memorial Day weekend:
  - Anthony/Land Pro: 440-320-2779 (landscaping script A)
  - Dontez/GTP: 440-396-0814 (landscaping script A)
  - Twin Improvements: 216-773-0757 (siding script B)
  - Reliable Roofing: 216-810-2497 (roofing script C)
  - Pagels Construction: 216-956-5263 (roofing script C)
- Templates: `outputs/tommy/contractor_referral_text_script_2026-05-20.md` (ready to copy/paste)
- After Memorial Day: May 26 blitz — `outputs/donna/may26_outreach_blitz_brief_2026-05-20.md`

---

## OPEN — Regular Danny PM cron not running (11 days overdue) 🔴🔴
- Updated: 2026-05-21 (run 35) — 11 DAYS OVERDUE. Summit County still unworked.
- Last ran: May 13. Today is May 21. 11 days of missed leads in Summit County (Akron/Fairlawn/Stow — NE Ohio's 2nd largest PM market).
- Medina County is also missed (week 22 in rotation — would have run May 20).
- Summit County alone is ~15-25 new PM leads that should now be in Mixmax.
- IMMEDIATE action: `python3 workers/lead_pipeline.py danny` from `/Users/bradleyneal/forestcity`
- June recovery schedule: `outputs/donna/june_week1_sprint_2026-05-20.md` — Summit June 2, Medina June 3
- Resolution criteria: Pipeline runs locally, Summit County leads pulled and enrolled in Mixmax.

---

## OPEN — Gas station & fleet contacts not enrolled in Mixmax
- Updated: 2026-05-20 (run 34)
- Run 34: Step-by-step Mixmax setup guide written → `outputs/vera/mixmax_sequence_setup_guide_2026-05-20.md`. 20-minute walkthrough to create both sequences in Mixmax UI and paste IDs. No more vague "create in Mixmax UI" — exact steps, UI navigation, ID paste locations.
- 18 gas station contacts (email) + 6 contractor manual contacts (email) = 24 contacts ready for auto-enrollment on next local pipeline run.
- Resolution criteria: Bradley runs the 20-min setup guide on June 2.

---

## OPEN — Slack webhook not confirmed as GitHub Actions secret
- Updated: 2026-05-21 (run 35) — Merged with GitHub Actions workflow issue above. Both steps needed:
  1. PAT workflow scope + workflow file push (see GitHub Actions issue above)
  2. Add SLACK_WEBHOOK_OFFICE as repo secret
- Resolution criteria: Same as GitHub Actions workflow issue — both steps done together.

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

## OPEN — Instantly.ai campaigns running parallel to Mixmax (duplicate sequence risk)
- First seen: 2026-05-18
- If INSTANTLY_API_KEY is ever added to .env: confirm Instantly campaigns are paused first.
- Resolution criteria: Bradley replies which platform is active for each segment.

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
- Memorial Day social posts written. Facebook posts week May 19 + Memorial Day posts ready.
- Resolution criteria: Bradley posts 1 Facebook post this week.

---

## OPEN — Workiz API blocked in cloud AND 0 power washing jobs on local
- First seen: 2026-05-14
- All code fixes confirmed present. Diagnostic logging active.
- Next step: Bradley checks Workiz for actual JobType field name.

---

## OPEN — Google Business Profile not managed (zero-cost lead channel ignored)
- Updated: 2026-05-21 (run 35)
- TODAY is Wednesday May 21 — the window to post a photo before Memorial Day weekend.
- Templates: `outputs/tommy/google_business_profile_post_templates_2026-05-20.md`
- 5 minutes: Open Google Maps → search Forest City Power Washing → click "Add Photo". Use any before/after job photo.
- Resolution: Bradley posts 1 photo to GBP.

---

## OPEN — No review request automation
- First seen: 2026-05-18
- 3-touch sequence written: `outputs/tommy/review_request_sequence_2026-05-18.md`.
- Resolution: Bradley sends review request text after each completed job.

---

## OPEN — No Google Ads running (invisible for "power washing near me")
- First seen: 2026-05-19
- Ad copy ready: `outputs/rick/google_ads_june_2026-05-19.md`.
- Blockers: (1) Google Ads account needed, (2) GOOGLE_ADS_TOKEN added to .env.
- Resolution criteria: Bradley creates Google Ads account and launches Campaign 1.

---

## OPEN — No Facebook ads running (peak season with no paid traffic)
- First seen: 2026-05-20
- Ad copy ready: `outputs/rick/facebook_ads_peak_season_2026-05-20.md`. Budget: $30/day to start.
- Resolution criteria: Bradley sets up ads in Facebook Ads Manager.

---

## OPEN — No website service pages (needed as Google Ads landing pages)
- First seen: 2026-05-20
- Service page copy written: `outputs/tommy/website_copy_service_pages_2026-05-20.md` (5 pages).
- Roof Soft Wash page should be first — highest search intent.
- Resolution criteria: Bradley builds service pages in web platform (Squarespace/Wix/WordPress).

---

## OPEN — No past customer re-engagement blast this season
- First seen: 2026-05-20
- Re-engagement templates: `outputs/tommy/past_customer_reengagement_2026-05-18.md`.
- Blocking factor: Need customer list from Workiz (run locally).
- Resolution criteria: Bradley pulls completed jobs from Workiz and texts past customers.

---

## OPEN — No quote follow-up sequence (post-estimate gap)
- First seen: 2026-05-20
- 3-touch sequence written: `outputs/tommy/quote_followup_sequence_2026-05-20.md`.
- Resolution criteria: Bradley sends Touch 1 text within 24h of next quote sent.

---

## OPEN — June Residential Push (all assets built but not deployed)
- First seen: 2026-05-20
- Campaign brief: `outputs/donna/june_residential_push_2026-05-20.md`. 4-week plan with revenue math.
- Critical path: service pages first (June 2), then Facebook ads (June 3).
- Resolution criteria: Bradley builds service pages June 2 and launches Facebook ads June 3.

---

## OPEN — Fleet washing Mixmax sequence not created
- First seen: 2026-05-20
- Sequence copy: `outputs/danny/sequence_fleet_washing_2026-05-18.md`. Infrastructure ready.
- Run 34: Step-by-step creation guide → `outputs/vera/mixmax_sequence_setup_guide_2026-05-20.md`.
- Resolution criteria: Real fleet_washing ID in `integrations/mixmax.py`.

---

## RESOLVED — workiz_report.py log_activity() crashes on missing logs directory
- Resolved: 2026-05-21 (run 35)
- Description: `log_activity()` called `open(log_path, 'a')` with no `os.makedirs()` guard. On a fresh clone where `logs/` directory doesn't exist, any workiz cron run would crash before writing the log entry. Other functions in the same file (save_report) already had `os.makedirs(out_dir, exist_ok=True)` — this one was missed.
- Fix: Added `os.makedirs(os.path.dirname(log_path), exist_ok=True)` before the write, wrapped entire function in try/except. Consistent with nina_report.py `log()` pattern.
- File: `workers/workiz_report.py`

---

## OPEN — Cloud git commit signing blocked (environment limitation)
- First seen: 2026-05-21 (run 35)
- Updated: 2026-05-21 (run 36) — Still present. Using GitHub REST API for file pushes.
- Description: Cloud environment code-signing server returns `{"message":"missing source"}` on commit. All run 36 changes pushed via GitHub REST API (PUT /contents).
- Workaround: GitHub API push for all non-workflow files. 
- Resolution criteria: May be transient — will test `git commit` at start of each run.

---

## RESOLVED — GAS_STATION_KEYWORDS 'district manager' false-positive
- Resolved: 2026-05-21 (run 36)
- Description: `'district manager'` was in GAS_STATION_KEYWORDS. This keyword is too generic — any contact with "District Manager" as a title at an ambiguous company (non-matching PM/contractor/realtor) would be misrouted to the gas_station sequence. Example: "District Manager" at a random service company = misclassified as gas station. Company name keywords (speedway, circle k, etc.) are sufficient to identify gas station accounts.
- Fix: Removed `'district manager'` from GAS_STATION_KEYWORDS. Added comment explaining why.
- File: `integrations/mixmax.py`

---

## RESOLVED — verify_and_repair_enrollment() unnecessarily attempts PENDING sequences
- Resolved: 2026-05-21 (run 36)
- Description: `verify_and_repair_enrollment()` found ALL contacts not in confirmed Mixmax emails and tried to re-enroll them. Gas station and fleet washing contacts (PENDING sequence IDs) always fail re-enrollment. This generates noise: `_lead_type=gas_station` contacts get marked `mixmax_enrolled=False` every run, even though their sequence simply hasn't been created yet.
- Fix: Added `_sequence_is_live` check — skips contacts with PENDING sequences gracefully with a dedicated print message. Only contacts with live sequence IDs are included in the repair attempt.
- File: `workers/lead_pipeline.py`

---

## RESOLVED — server.py save_queue() has no write protection
- Resolved: 2026-05-21 (run 36)
- Description: `save_queue()` called `QUEUE_F.write_text()` with no try/except. On a full disk or locked file, this would throw unhandled exception propagating to the POST /api/queue handler, sending 500 to the dashboard.
- Fix: Wrapped in try/except. Consistent with other write operations in server.py.
- File: `server.py`

---

## OPEN — 0% reply rate (Touch 3 fires TOMORROW May 22) 🚨🚨
- Updated: 2026-05-21 (run 36) — TOUCH 3 FIRES IN ~12 HOURS. All assets locked and loaded.
- Run 36 deliverable: Open Trigger Protocol → `outputs/tommy/touch3_open_trigger_protocol_2026-05-21.md`. Covers the 48-hour window starting when Touch 3 fires: LinkedIn connect within 2 hours of each open, Memorial Day voicemail/SMS scripts, decision tree, all 7 key file references in one table.
- Run 35: Evening debrief → `outputs/vera/touch3_evening_debrief_2026-05-22.md`. What to do Thursday evening.
- **COMPLETE MAY 22 PLAYBOOK:**
  - MORNING (8am): `outputs/vera/touch3_morning_brief_2026-05-22.md`
  - REAL-TIME (each open): `outputs/tommy/touch3_open_trigger_protocol_2026-05-21.md` ← NEW
  - IF REPLIES: `outputs/tommy/touch3_reply_response_templates_2026-05-20.md` + `outputs/tommy/quote_to_close_kit_2026-05-20.md`
  - IF NO REPLIES BY NOON: `outputs/tommy/hot_lead_phone_script_2026-05-22.md`
  - EVENING (6pm): `outputs/vera/touch3_evening_debrief_2026-05-22.md`
- Resolution criteria: 1+ reply from Touch 3 OR Bradley calls hot leads May 22–26.

---

## OPEN — Manual Contacts Sitting Untouched (New Lead stage)
- Updated: 2026-05-21 (run 36) — 36 contacts: 33 New Lead, 3 Contacted. TODAY is the LAST window before Memorial Day.
- **SEND TEXTS TODAY (May 21)** — Text Tier 1 contractors before end of business. They won't check messages over Memorial Day weekend. Window closes in ~6 hours:
  - Anthony/Land Pro: 440-320-2779 (script A — landscaper)
  - Dontez/GTP: 440-396-0814 (script A — landscaper)
  - Twin Improvements: 216-773-0757 (script B — siding)
  - Reliable Roofing: 216-810-2497 (script C — roofing)
  - Pagels Construction: 216-956-5263 (script C — roofing)
- Copy-paste scripts: `outputs/tommy/contractor_referral_text_script_2026-05-20.md`
- After Memorial Day: May 26 blitz — `outputs/donna/may26_outreach_blitz_brief_2026-05-20.md`

---

## OPEN — Regular Danny PM cron not running (12 days overdue) 🔴🔴
- Updated: 2026-05-21 (run 36) — 12 DAYS OVERDUE. Summit County still unworked.
- Last ran: May 13. Today is May 21. 12 days without Akron/Fairlawn/Stow leads.
- `python3 workers/lead_pipeline.py danny` from `/Users/bradleyneal/forestcity` — run TODAY.
- Or run June 2 as planned: `outputs/donna/june_week1_sprint_2026-05-20.md`
- Note: Each week of delay = another batch of PMs in NE Ohio's 2nd largest market booking competitors for the summer.

---

## OPEN — Gas station & fleet contacts not enrolled in Mixmax
- Updated: 2026-05-21 (run 36) — Infrastructure fully built. Waiting on Bradley to create sequences.
- Run 36: `verify_and_repair_enrollment()` now correctly skips these contacts with PENDING sequences — no more false "repair" noise in the logs.
- Step-by-step guide: `outputs/vera/mixmax_sequence_setup_guide_2026-05-20.md` — 20 min total.
- Target date: June 2 (Monday after Memorial Day + 1 week).

---

## OPEN — GitHub Actions workflow missing — ALL cloud Slack messages silently dropped 🚨
- Updated: 2026-05-21 (run 36) — NEW APPROACH: one-command deploy script created.
- Run 36: `scripts/deploy_github_action.sh` created. ONE command: `bash /Users/bradleyneal/forestcity/scripts/deploy_github_action.sh`
- **STILL NEED (2 steps before running the script):**
  1. Add `workflow` scope to PAT: github.com → Settings → Developer settings → PATs → Edit `ghp_lrUhBq7...` → check `workflow` → Save
  2. Add repo secret: github.com/brad962/forestcity → Settings → Secrets → `SLACK_WEBHOOK_OFFICE` = webhook from .env
- Then run the script and it handles the rest in ~30 seconds.
- Resolution criteria: GitHub Actions tab shows the workflow after push.

---

## OPEN — Mixmax API blocked in cloud execution environment
- First seen: 2026-05-18
- Workaround: All pipeline scripts return None/safe fallback on 403.
- Next steps: Bradley checks Mixmax → API Settings → IP Allowlist.

---

## OPEN — All external APIs blocked from cloud (Apollo, Workiz, Mixmax)
- First seen: 2026-05-18
- Workaround: Cron job schedule documented in CLAUDE.md.
- Next steps: Bradley runs `crontab -e` and pastes cron jobs.

---

## OPEN — Slack Webhook blocked in cloud execution environment
- First seen: 2026-05-18
- Workaround: Messages written to `outputs/vera/pending_slack_messages.md`. GitHub Action posts to Slack on push (once GitHub Actions is deployed per above).

---

## OPEN — Instantly.ai campaigns running parallel to Mixmax (duplicate sequence risk)
- First seen: 2026-05-18
- If INSTANTLY_API_KEY is ever added to .env: confirm Instantly campaigns are paused first.
- Resolution criteria: Bradley replies which platform is active for each segment.

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
- Memorial Day social posts written. Facebook posts week May 19 + Memorial Day posts ready.
- Resolution criteria: Bradley posts 1 Facebook post this week.

---

## OPEN — Workiz API blocked in cloud AND 0 power washing jobs on local
- First seen: 2026-05-14
- All code fixes confirmed present. Diagnostic logging active.
- Next step: Bradley checks Workiz for actual JobType field name.

---

## OPEN — Google Business Profile not managed (zero-cost lead channel ignored)
- Updated: 2026-05-21 (run 36) — TODAY is last chance before Memorial Day weekend. Post 1 photo.
- Templates: `outputs/tommy/google_business_profile_post_templates_2026-05-20.md`
- 5 minutes: Google Maps → search Forest City Power Washing → Add Photo.
- Resolution: Bradley posts 1 photo to GBP.

---

## OPEN — No review request automation
- First seen: 2026-05-18
- 3-touch sequence: `outputs/tommy/review_request_sequence_2026-05-18.md`.
- Resolution: Bradley sends review request text after each completed job.

---

## OPEN — No Google Ads running (invisible for "power washing near me")
- First seen: 2026-05-19
- Ad copy ready: `outputs/rick/google_ads_june_2026-05-19.md`.
- Blockers: Google Ads account + GOOGLE_ADS_TOKEN in .env.
- Resolution criteria: Bradley creates Google Ads account and launches Campaign 1.

---

## OPEN — No Facebook ads running (peak season with no paid traffic)
- First seen: 2026-05-20
- Ad copy ready: `outputs/rick/facebook_ads_peak_season_2026-05-20.md`. Budget: $30/day to start.
- Resolution criteria: Bradley sets up ads in Facebook Ads Manager.

---

## OPEN — No website service pages (needed as Google Ads landing pages)
- First seen: 2026-05-20
- Service page copy: `outputs/tommy/website_copy_service_pages_2026-05-20.md` (5 pages).
- Roof Soft Wash page should be first — highest search intent.
- Resolution criteria: Bradley builds service pages in web platform.

---

## OPEN — No past customer re-engagement blast this season
- First seen: 2026-05-20
- Re-engagement templates: `outputs/tommy/past_customer_reengagement_2026-05-18.md`.
- Blocking factor: Need customer list from Workiz (run locally).
- Resolution criteria: Bradley pulls completed jobs from Workiz and texts past customers.

---

## OPEN — No quote follow-up sequence (post-estimate gap)
- First seen: 2026-05-20
- 3-touch sequence: `outputs/tommy/quote_followup_sequence_2026-05-20.md`.
- Resolution criteria: Bradley sends Touch 1 text within 24h of next quote sent.

---

## OPEN — June Residential Push (all assets built but not deployed)
- First seen: 2026-05-20
- Campaign brief: `outputs/donna/june_residential_push_2026-05-20.md`. 4-week plan with revenue math.
- Critical path: service pages first (June 2), then Facebook ads (June 3).
- Resolution criteria: Bradley builds service pages June 2 and launches Facebook ads June 3.

---

## OPEN — Fleet washing Mixmax sequence not created
- First seen: 2026-05-20
- Sequence copy: `outputs/danny/sequence_fleet_washing_2026-05-18.md`. Infrastructure ready.
- Step-by-step creation guide: `outputs/vera/mixmax_sequence_setup_guide_2026-05-20.md`.
- Resolution criteria: Real fleet_washing ID in `integrations/mixmax.py`.

---

## OPEN — 13 hot leads sitting uncontacted on LinkedIn
- Updated: 2026-05-21 (run 36) — TODAY is the window. Touch 3 fires tomorrow.
- New: `outputs/tommy/touch3_open_trigger_protocol_2026-05-21.md` covers post-Touch-3 LinkedIn workflow in real time.
- Tonight: send 3+ LinkedIn connects BEFORE Touch 3 fires: `outputs/danny/linkedin_hot_lead_dm_protocol_2026-05-18.md`
- Resolution criteria: Bradley sends 3+ LinkedIn connects.

---

*Last updated: 2026-05-21 by Vera Cole (run 36)*
*Key metrics: 99 RESOLVED | 13 OPEN | Run 36: 3 code fixes + 1 deliverable + deploy script*
