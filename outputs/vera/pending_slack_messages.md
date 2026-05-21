🔧 *Vera — Auto-Upgrade*
>Changed: Removed 'operations manager' from FLEET_KEYWORDS in mixmax.py — replaced with specific alternatives (fleet operations manager, transportation director, vehicle fleet)
>Why: Same false-positive class as 'district manager' fixed run 36 — any non-fleet contact titled "Operations Manager" was misrouted to the fleet washing sequence.
>File: integrations/mixmax.py

---

🔧 *Vera — Auto-Upgrade*
>Changed: Added path containment check to server.py /api/file endpoint
>Why: Unsanitized fname query param allowed ../../../server.py traversal — server would serve its own source file containing API key variable names.
>File: server.py

---

🔧 *Vera — Auto-Upgrade*
>Changed: workiz_report.py JobTotalPrice + JobAmountDue wrapped in float() cast
>Why: Workiz API may return price fields as strings; sum() crashes with TypeError on mixed int/string types.
>File: workers/workiz_report.py

---

🚨 *Vera — TONIGHT ACTION REQUIRED (May 21)*
>Touch 3 fires TOMORROW morning (May 22). This is the last evening to prep.
>
>4 things to do TONIGHT (35 minutes total):
>1. Verify Mixmax Reply-To → outputs/vera/mixmax_reply_to_check_2026-05-20.md (10 min)
>2. Enable open notifications → outputs/vera/mixmax_open_notifications_setup_2026-05-21.md (5 min)
>3. Text 5 Tier 1 contractors using scripts → outputs/tommy/contractor_referral_text_script_2026-05-20.md (15 min)
>4. Run Summit County pipeline (LAST CHANCE tonight): cd ~/forestcity && python3 workers/lead_pipeline.py danny
>
>Full checklist: outputs/vera/touch3_last_night_checklist_2026-05-21.md

---

📅 *Vera — June Pipeline Schedule*
>New reference doc: outputs/donna/june_apollo_pull_schedule_2026-05-21.md
>Full week-by-week Apollo pull schedule: May 21 through July 4.
>KEY: Summit County pulls TONIGHT (week 21). After midnight = Medina. Next Summit without intervention: June 30.
>June 2 target for gas station + fleet Mixmax sequences. 100-140 new PM leads possible if every Monday runs.

---

📋 *Vera — Tomorrow May 22 Playbook (all 7 resources ready)*
>SETUP (5 min): outputs/vera/mixmax_open_notifications_setup_2026-05-21.md
>8 AM: outputs/vera/touch3_morning_brief_2026-05-22.md
>REAL-TIME: outputs/tommy/touch3_open_trigger_protocol_2026-05-21.md
>IF REPLIES: touch3_reply_response_templates + quote_to_close_kit
>NO REPLIES BY NOON: outputs/tommy/hot_lead_phone_script_2026-05-22.md
>6 PM: outputs/vera/touch3_evening_debrief_2026-05-22.md
>MAY 23-26: outputs/tommy/memorial_day_monitoring_2026-05-21.md

---

✅ *Vera — Scan Complete 2026-05-21 (Run 40)*
>3 auto-upgrades shipped | 0 proposals | 17 open issues
>Code fixes: FLEET_KEYWORDS false-positive, server.py path traversal, Workiz price float cast
>New files: June Apollo Pull Schedule, Touch 3 Last Night Checklist
>Touch 3 fires TOMORROW. All 7 resources locked and loaded.
