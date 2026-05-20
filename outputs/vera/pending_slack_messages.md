🔧 *Vera — Auto-Upgrade*
>Changed: `lead_pipeline.py` run_pending_sequences() — checks both `_lead_type` AND `lead_type` fields (and fixes lead dict construction). 6 contractor manual contacts (Blue Line, Kardiac, Don't Move Improve, Woolworth, Everguard, Camlin) were being silently skipped for Mixmax enrollment because their field was `lead_type` not `_lead_type`. Once pipeline runs locally, all 6 auto-enroll in contractor sequence.
>Why: Silent enrollment gap — 6 contacts with valid emails and a live sequence were never going to be touched.
>File: `workers/lead_pipeline.py`
---
🔧 *Vera — Auto-Upgrade*
>Changed: `pipeline_data.json` — set `next_followup: 2026-05-26` for Bulletproof Lawncare and Damrons Landscaping. Both were marked Contacted on May 19 with no follow-up date.
>Why: Dashboard showed "awaiting reply" with no reminder. May 26 is the target blitz day — now dashboard will surface them correctly.
>File: `pipeline_data.json`
---
🔧 *Vera — Auto-Upgrade*
>Changed: Added `regional manager`, `operations director`, `general manager` to DANNY_TITLES and PROPERTY_MANAGER_TITLES. These are common titles at multi-site property management companies — the exact accounts that book recurring commercial washes.
>Why: Apollo was missing high-value decision-makers at larger management firms. One regional manager = 5–20 properties.
>Files: `workers/lead_pipeline.py`, `integrations/mixmax.py`
---
🔧 *Vera — Auto-Upgrade*
>Changed: `agents/jasmine.md` — added 4 missing output format variants. `agents/nina.md` — added hot_leads and workiz report formats. `workers/vera_relay.py` — removed redundant --oneline flag from git log.
>Why: Agent files undocumented for 10+ deliverables written over 2 weeks. Relay flag cleanup.
>Files: `agents/jasmine.md`, `agents/nina.md`, `workers/vera_relay.py`
---
📋 *Vera — New Deliverable*
>File: `outputs/tommy/contractor_referral_text_script_2026-05-20.md`
>What: Personalized text scripts for all 5 Tier 1 contractors. 3 trade-specific versions: Script A (landscapers), Script B (siding), Script C (roofing). Each is pre-written copy/paste ready. Includes YES/NO/no-reply handling, timing notes, and dashboard tracking instructions.
>Action: Copy and send tonight or tomorrow May 21. Goal = all 5 texts out before Memorial Day weekend.
---
🚨 *Vera — TONIGHT ACTION ALERT (May 20)*
>Touch 3 fires in ~36 hours. Three things to do TONIGHT (55 min total):
>1️⃣ *Check Mixmax Reply-To* (10 min) — `outputs/vera/mixmax_reply_to_check_2026-05-20.md`
>2️⃣ *Send 13 LinkedIn connects* to hot leads (30 min) — `outputs/tommy/hot_lead_linkedin_dm_playbook_2026-05-19.md`
>3️⃣ *Text 5 Tier 1 contractors* (15 min) — `outputs/tommy/contractor_referral_text_script_2026-05-20.md`
>Full checklist: `outputs/vera/touch3_eve_final_checklist_2026-05-20.md`
---
📅 *Vera — Thursday May 22 Morning Brief*
>Touch 3 fires Thursday morning. Read this first thing: `outputs/vera/touch3_morning_brief_2026-05-22.md`
>Covers: check Mixmax for replies, 3 reply scenarios (A/B/C), phone script for hot leads, contractor text blast.
>Phone script (if email gets 0 replies): `outputs/tommy/hot_lead_phone_script_2026-05-22.md`
>Quote-to-close kit (if anyone asks for pricing): `outputs/tommy/quote_to_close_kit_2026-05-20.md`
---
💡 *Vera — Upgrade Proposal*
>Idea: Set up Twilio SMS to send post-job review requests automatically when a Workiz job is marked "Done."
>Why: Review requests sent within 30 min of job completion get 4x the response rate vs. manual follow-up. Each new 5-star review generates an estimated 1–3 additional inbound leads/month.
>Impact: Hands-off review generation — every completed job triggers a text. No extra work for Bradley.
>Requires: Twilio account (~$20/mo), 3 credentials added to .env, Workiz webhook configured. I'll build the whole thing once approved.
>Reply YES to approve.
---
✅ *Vera — Scan Complete 2026-05-20 (run 33)*
>5 auto-upgrades shipped | 1 new deliverable (contractor referral text scripts) | 1 proposal (Twilio review automation) | 8 open issues
>
>*Key fixes this run:* run_pending_sequences() bug fixed (6 contractor contacts with emails now correctly route to contractor sequence). Regional Manager + Operations Director + General Manager added to Apollo search (more multi-site PM decision-makers next pull).
>
>🔴 *Tonight (May 20):* Reply-To check + 13 LinkedIn connects + Tier 1 contractor texts
>🔴 *Thursday May 22:* Read morning brief, respond to Touch 3 replies within 2 hours
>🟡 *Run locally today:* `python3 workers/lead_pipeline.py both` — Summit County + auto-enrolls 6 contractors
