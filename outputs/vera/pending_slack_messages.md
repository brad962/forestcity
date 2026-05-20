🔧 *Vera — Auto-Upgrade*
>Changed: server.py — Mixmax contacts now correctly flagged stale on dashboard when never contacted (no last_contact)
>Why: Manual contacts had this logic; Mixmax contacts didn't — 45 enrolled contacts looked like they didn't need attention when they did.
>File: server.py
---
🔧 *Vera — Auto-Upgrade*
>Changed: workiz_report.py save_report() + log_activity() paths — replaced os.path.dirname(__file__) with BASE_DIR (already defined at module level)
>Why: Eliminates path resolution risk when script is called from a non-standard working directory.
>File: workers/workiz_report.py
---
🔧 *Vera — Auto-Upgrade*
>Changed: agents/donna.md, agents/carla.md, agents/tommy.md — added missing output format entries for 6 file types created in runs 22-31
>Why: Agent output format sections should document all file types they generate. 6 types (daily_sprint, outreach_blitz_brief, june_week1_sprint, june_residential_push, referral_partner_onboarding, linkedin_followup_post_connect) were missing.
>Files: agents/donna.md, agents/carla.md, agents/tommy.md
---
📄 *Vera — New Deliverable*
>File: outputs/tommy/linkedin_followup_post_connect_2026-05-20.md
>The gap the DM playbook didn't cover: what to say AFTER a connect is accepted.
>3 versions: A (direct/PM) | B (warm/HOA) | C (referral/realtor angle)
>Includes response playbook for all reply scenarios + timing guide for May 22
>Send within 24h of any acceptance — the accept window is the warmest moment in the sequence.
---
🚨 *Vera — TONIGHT (Bradley — 55 min)*
>Touch 3 fires TOMORROW May 22. Do these tonight:
>1. Check Mixmax Reply-To (10 min) → mixmax_reply_to_check_2026-05-20.md
>2. Send 13 LinkedIn connects to hot leads (30 min) → hot_lead_linkedin_dm_playbook_2026-05-19.md
>3. Text 5 Tier 1 contractors (15 min):
>Anthony/Land Pro 440-320-2779 | Dontez/GTP 440-396-0814 | Twin Improvements 216-773-0757 | Reliable Roofing 216-810-2497 | Pagels Construction 216-956-5263
>If contractor says YES: outputs/carla/referral_partner_onboarding_2026-05-20.md
---
📋 *Vera — Thursday Morning (Bradley)*
>READ FIRST THING MAY 22: outputs/vera/touch3_morning_brief_2026-05-22.md
>Covers: Did Touch 3 send? → 3 reply scenarios with exact scripts → LinkedIn follow-up to accepted connections → If 0 replies by noon, phone calls using hot_lead_phone_script_2026-05-22.md
>All resources linked. Do not start Thursday without reading it.
---
🔴 *Vera — Danny Cron Still Overdue (10+ Days)*
>Summit County (Akron/Fairlawn/Stow) unworked. This is Week 21.
>Run TODAY locally: python3 workers/lead_pipeline.py danny (from /Users/bradleyneal/forestcity)
>~15-20 Summit County property managers waiting to be pulled.
>Full June pipeline schedule: outputs/donna/june_week1_sprint_2026-05-20.md
---
✅ *Vera — Scan Complete 2026-05-20 (Run 32)*
>4 auto-upgrades shipped | 0 proposals | 88 RESOLVED | 9 OPEN
>Code fixes: server.py Mixmax stale detection, workiz_report.py BASE_DIR paths
>Doc fixes: 6 missing output format entries across 3 agent files
>New deliverable: LinkedIn post-connect messages (3 versions + response playbook for all scenarios)
>TONIGHT: Reply-To check + 13 LinkedIn connects + 5 contractor texts
>TOMORROW AM: Read touch3_morning_brief_2026-05-22.md first thing
