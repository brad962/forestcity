🔧 *Vera — Auto-Upgrade*
>Changed: `integrations/mixmax.py` — removed `'district manager'` from `GAS_STATION_KEYWORDS`
>Why: Too generic — any contact with "District Manager" title at an unrecognized company was being misrouted to the gas station sequence. Company name keywords (speedway, circle k, etc.) are sufficient to identify gas station accounts.
>File: `integrations/mixmax.py`
---
🔧 *Vera — Auto-Upgrade*
>Changed: `workers/lead_pipeline.py` `verify_and_repair_enrollment()` — now skips contacts with PENDING sequences (gas_station, fleet_washing) gracefully
>Why: Previously, every pipeline run attempted to re-enroll these contacts, failed, and marked them `mixmax_enrolled=False` — creating noise. Now logs "Skipping N contacts with PENDING sequences" and moves on.
>File: `workers/lead_pipeline.py`
---
🔧 *Vera — Auto-Upgrade*
>Changed: `server.py` `save_queue()` — wrapped `QUEUE_F.write_text()` in try/except
>Why: Full disk or locked file would throw unhandled exception propagating as 500 to the dashboard. 4-line fix, consistent with all other write operations in server.py.
>File: `server.py`
---
📋 *Vera — New Deliverable*
>File: `outputs/tommy/touch3_open_trigger_protocol_2026-05-21.md`
>What: Real-time protocol for the 48 hours starting when Touch 3 fires tomorrow. Covers: check Mixmax 3x/day, LinkedIn connect within 2 hours of each open, Memorial Day voicemail + SMS scripts, decision tree for every scenario, all 7 key files in one reference table.
>Gap filled: The morning brief, phone script, and evening debrief covered "scheduled" touch points. This covers the REAL-TIME trigger — what happens in the 2-hour window after each open.
---
📋 *Vera — New Deliverable*
>File: `scripts/deploy_github_action.sh`
>What: ONE command to deploy the Vera Slack relay GitHub Action from your Mac: `bash /Users/bradleyneal/forestcity/scripts/deploy_github_action.sh`
>Gap filled: The workflow file has existed since run 34. The 3-step instructions have been in open_issues.md for 2 runs. This new script removes ALL manual steps — just run it.
>Still needs (before running the script, ~4 min total):
>1. Add workflow scope to PAT: github.com → Settings → Developer settings → PATs → Edit ghp_lrUhBq7... → check 'workflow' → Save
>2. Add repo secret: github.com/brad962/forestcity → Settings → Secrets → SLACK_WEBHOOK_OFFICE = webhook URL from .env
---
🚨 *Vera — TODAY May 21 — LAST WINDOW Before Touch 3 + Holiday Weekend*
>Touch 3 fires TOMORROW. Contractor texts close at end of business today — people won't check over Memorial Day.
>
>Tonight (55 min) — outputs/vera/touch3_eve_final_checklist_2026-05-20.md:
>1. Verify Mixmax Reply-To — 10 min
>2. LinkedIn connects to 13 hot leads — 30 min
>3. Text 5 Tier 1 contractors — 15 min:
>   Anthony/Land Pro: 440-320-2779 (script A)
>   Dontez/GTP: 440-396-0814 (script A)
>   Twin Improvements: 216-773-0757 (script B)
>   Reliable Roofing: 216-810-2497 (script C)
>   Pagels Construction: 216-956-5263 (script C)
>Scripts: outputs/tommy/contractor_referral_text_script_2026-05-20.md
---
📅 *Vera — Tomorrow (May 22) Full Playbook — 5 Resources Cover Every Scenario*
>8am: outputs/vera/touch3_morning_brief_2026-05-22.md — first check
>Each open (real-time): outputs/tommy/touch3_open_trigger_protocol_2026-05-21.md (NEW)
>If replies: outputs/tommy/touch3_reply_response_templates_2026-05-20.md
>If no replies by noon: outputs/tommy/hot_lead_phone_script_2026-05-22.md
>6pm: outputs/vera/touch3_evening_debrief_2026-05-22.md
---
✅ *Vera — Scan Complete 2026-05-21 (Run 36)*
>3 auto-upgrades shipped | 2 new deliverables | 0 new open issues
>
>Key actions for Bradley TODAY (last window before Memorial Day weekend):
>TONIGHT: Touch 3 eve checklist — 55 min (Reply-To check, LinkedIn connects, Tier 1 texts)
>TONIGHT: Read outputs/tommy/touch3_open_trigger_protocol_2026-05-21.md for tomorrow
>TODAY (5 min): Add workflow scope to PAT + add Slack secret then run scripts/deploy_github_action.sh
>TODAY (5 min): Post 1 photo to Google Business Profile
>
>99 RESOLVED | 13 OPEN | Touch 3 fires in less than 12 hours
