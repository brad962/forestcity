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
- First seen: 2026-05-18 (updated run 24 — 2026-05-20)
- Description: 45 enrolled, 42% open rate, 0 replies. Touch 3 fires **MAY 22** (Friday). After Touch 3, automated sequence is complete. Personal outreach takes over.
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
- Updated: 2026-05-20 (run 22) — TOUCH 3 FIRES IN ~36 HOURS
- Run 22: Post-sequence recovery protocol written — `outputs/tommy/post_sequence_recovery_protocol_2026-05-20.md`. Bradley knows exactly what to do AFTER Touch 3 fires: LinkedIn connects (same day), personal Gmail email to top 5 (May 26), contractor text blast (May 26). Protocol covers all 3 contact tiers and a tracking method.
- Run 22 angle: The sequence ending is not a failure — it's a hand-off moment. Hot leads with 2+ opens are WARM. Personal follow-up converts warm leads at 3–5x the rate of automated email.
- Run 21: Touch 1 & Touch 2 rewrite written → `outputs/danny/pm_sequence_touch1_rewrite_2026-05-19.md`. Applies to round 2 only.
- Run 20 angle: LinkedIn DM playbook ready for 13 hot leads.
- Run 18 diagnostic: 5 hypotheses in `outputs/vera/reply_rate_diagnostic_2026-05-19.md`
- IMMEDIATE action today (May 20): (1) Check Mixmax Reply-To — 10 min. (2) LinkedIn connects to 13 hot leads — 30 min. (3) Schedule Gmail drafts for Monday May 26.
- Resolution criteria: 1+ reply received from any channel (LinkedIn, Gmail, or Touch 3 response).

---

## OPEN — 40 Manual Contacts Sitting Untouched (New Lead stage) — NO PROGRESS
- Updated: 2026-05-20 (run 22) — TODAY IS THE LAST DAY. AFTER TODAY CONTRACTORS GO INTO WEEKEND MODE.
- Run 22: May 26 outreach blitz brief written — `outputs/donna/may26_outreach_blitz_brief_2026-05-20.md`. The Day After Memorial Day is the BEST response day of peak season. Plan covers 70 minutes of outreach, all assets mapped.
- TODAY May 20 — text 5 Tier 1: Anthony/Land Pro (440-320-2779), Dontez/GTP (440-396-0814), Twin Improvements, Reliable Roofing, Pagels Construction
- THURSDAY May 21 — text next 10 from priority list if possible (Fri going into weekend won't land)
- MAY 26 (Tuesday after Memorial Day) — second blast per `outputs/donna/may26_outreach_blitz_brief_2026-05-20.md`
- Templates: `outputs/vera/sms_templates_contractors_2026-05-18.md`
- Priority list: `outputs/vera/priority_outreach_list_2026-05-19.md`

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

## OPEN — Regular Danny PM cron not running (8 days overdue)
- Updated: 2026-05-20 (run 22) — 8 DAYS OVERDUE. MISSED SUMMIT COUNTY WEEK.
- Run 22 fix: lead_pipeline.py `run_pending_sequences()` `cache` undefined bug fixed (defensive init).
- Pipeline not run since May 13. Week 20 = Lorain (done). Week 21 = Summit. Week 22 = Medina.
- Running today would pull Week 21 Summit County batch (~15-25 PMs), auto-enroll in Mixmax.
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

## OPEN — CLE Lawn Care Plus marked "Contacted" but no last_contact date
- First seen: 2026-05-20 (run 24)
- Description: CLE Lawn Care Plus (216-402-1924) has stage="Contacted" but last_contact is empty string. The server.py stale detection correctly identifies this as stale (falls through to the "never contacted" branch), but the stage mismatch is a data quality issue — either the contact was never actually reached (stage should be "New Lead") or it was contacted but the date wasn't recorded.
- Resolution: Bradley either (a) updates last_contact to the actual contact date in the dashboard, or (b) changes stage back to "New Lead" if they haven't actually been reached.
- File: `pipeline_data.json`

---

*Last updated: 2026-05-20 by Vera Cole (run 24)*
*Key metrics: 61 RESOLVED | 15 OPEN | 2 auto-upgrades (dedup, data quality flag) | 4 deliverables (touch3 reply templates, round2 plan, mixmax check guide, June content calendar)*
