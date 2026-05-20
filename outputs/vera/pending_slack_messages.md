🔧 *Vera — Auto-Upgrade*
>Changed: `server.py` /api/pipeline GET — normalize Mixmax dict response to list
>Why: If Mixmax returns `{"results": [...]}` format, all pipeline contacts were silently dropped from the dashboard with no error. Same pattern already fixed in nina_report.py and every other Mixmax endpoint — this one was missed.
>File: `server.py`
---
🔧 *Vera — Auto-Upgrade*
>Changed: `workers/vera_relay.py` messages[:10] → messages[:50]
>Why: If pending_slack_messages.md had >10 messages, messages 11+ were permanently dropped when the file was cleared. Vera generates 10-15 messages per run — the old cap was always at risk of dropping the last few.
>File: `workers/vera_relay.py`
---
🔧 *Vera — Auto-Upgrade*
>Changed: `agents/rick.md` Facebook Ads status — "Pending" → references the completed file
>Why: The Facebook ads campaign was written in run 23 (`outputs/rick/facebook_ads_peak_season_2026-05-20.md`) but rick.md still said "Pending." Any future activation of Rick would show no ads ready.
>File: `agents/rick.md`
---
🚨 *Vera — URGENT: Touch 3 fires TOMORROW (May 22)*
>45 enrolled | 42% opens | 0 replies. Sequence ends tomorrow. Personal outreach starts.
>
>TODAY — 3 actions (55 min total):
>1. Check Mixmax Reply-To address (10 min) → `outputs/vera/mixmax_reply_to_check_2026-05-20.md`
>2. LinkedIn connects to 13 hot leads (30 min) → `outputs/danny/linkedin_hot_lead_dm_protocol_2026-05-18.md`
>3. Text 5 Tier 1 contractors (15 min) → 440-320-2779, 440-396-0814, 216-773-0757, 216-810-2497, 216-956-5263
>
>TOMORROW — watch inbox from 8am. Reply templates ready: `outputs/tommy/touch3_reply_response_templates_2026-05-20.md`
>Full checklist: `outputs/vera/touch3_eve_final_checklist_2026-05-20.md`
---
📱 *Vera — Deliverable: Memorial Day Week Social Posts*
>Jasmine wrote 5 Facebook posts + 1 LinkedIn for May 21-25. This was the content gap — the week leading into Memorial Day had no posts written.
>Wednesday: algae education | Thursday: before/after | Friday: holiday kickoff | Saturday: social proof | Sunday: Memorial Day respect post
>LinkedIn post Thursday targets property managers directly (good timing — commercial decisions happening now).
>File: `outputs/jasmine/facebook_posts_memorial_day_week_2026-05-20.md`
---
📋 *Vera — Weekly Open Issues Escalation*
>
>🔴 Danny PM cron — 9 DAYS OVERDUE: Pipeline hasn't run since May 13. Today is week 22 (Medina County). Run: `python3 workers/lead_pipeline.py both` locally.
>
>🔴 Gas station emails — 18 idle: Manual email templates at `outputs/danny/gas_station_manual_email_blast_2026-05-20.md`. Or create Mixmax sequence (10 min) → paste ID into `integrations/mixmax.py` line 54.
>
>🟡 Fleet washing: Copy ready at `outputs/danny/sequence_fleet_washing_2026-05-18.md`. ID goes in `integrations/mixmax.py` line 48.
>
>🟡 Round 2 starts June 2: Plan at `outputs/danny/round2_enrollment_plan_2026-05-20.md`. Sequence rewrite ready: `outputs/danny/pm_sequence_touch1_rewrite_2026-05-19.md`
>
>🟡 Facebook Ads: Everything written. `outputs/rick/facebook_ads_peak_season_2026-05-20.md`. Budget: $30/day.
---
✅ *Vera — Scan Complete 2026-05-20 (Run 25)*
>3 auto-upgrades shipped | 0 new proposals | 15 open issues
>Key this run: Touch 3 fires tomorrow — checklist written, LinkedIn connects should go out TODAY. Server.py pipeline dict normalization bug fixed (was silently dropping Mixmax contacts from dashboard on dict API response). Memorial Day week posts written (5-day content gap filled). vera_relay message drop bug fixed.
