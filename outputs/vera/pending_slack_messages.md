🔧 *Vera — Auto-Upgrade*
>Changed: Removed hardcoded Apollo API key from danny.md and carla.md — key was committed in plaintext to git
>Why: Any repo viewer could read the key; moved to `load from .env as APOLLO_KEY` reference
>Files: `agents/danny.md`, `agents/carla.md`

---

🔧 *Vera — Auto-Upgrade*
>Changed: Added `git_push()` to workiz_report.py — Workiz reports were saved locally but never committed to the repo
>Why: When the cron ran locally, the report file existed on disk but was invisible in GitHub and to other workers
>File: `workers/workiz_report.py`

---

🔧 *Vera — Auto-Upgrade*
>Changed: nina_report.py weekly report now sends `IN PROGRESS` status to Slack when Mixmax API is blocked
>Why: Was sending `DONE` with all-zero metrics when API blocked — looked like an empty pipeline instead of an API issue
>File: `workers/nina_report.py`

---

🔧 *Vera — Auto-Upgrade*
>Changed: Marked "No phone cold call script" as RESOLVED in open_issues.md — script was written in run 27 but issue was never closed
>Why: open_issues.md showed it OPEN even though `hot_lead_phone_script_2026-05-22.md` was already complete
>File: `outputs/vera/open_issues.md`

---

📋 *Vera — New Deliverable*
>File: `outputs/tommy/quote_followup_sequence_2026-05-20.md`
>What: 3-touch post-estimate follow-up (text at 24h, email at day 4, final text at day 7)
>Gap filled: After sending a quote, there was no follow-up. Data says a single 24h text closes 20–25% more quotes. This sequence also covers the contractor referral follow-up script.
>Use it: Next time you send a quote — set a reminder for 24h and send Touch 1.

---

💡 *Vera — Upgrade Proposal*
>Idea: June Residential Push — launch all pre-built assets as a coordinated 4-week campaign starting June 2
>Why: Facebook ads, Google Ads, service pages, past customer texts, review requests are ALL written and ready. The only missing piece was this plan.
>Revenue math: $4,800–$8,400 net in June at $45/day ad spend. Breakeven at ~5 jobs.
>Plan: `outputs/donna/june_residential_push_2026-05-20.md`
>Critical first step: Service pages in your website platform (Wix/Squarespace/WordPress) before launching ads. Roof Soft Wash page first — highest-value, highest search intent.
>Reply YES to approve and I'll schedule the week-by-week task reminders.

---

🚨 *Vera — TONIGHT CHECKLIST (May 20 — Touch 3 fires TOMORROW)*
>3 things to do tonight (55 minutes total):
>1. Check Mixmax Reply-To (10 min) → `outputs/vera/mixmax_reply_to_check_2026-05-20.md` — if this is wrong, Touch 3 replies go to a dead inbox
>2. Send 13 LinkedIn connects (30 min) → `outputs/tommy/hot_lead_linkedin_dm_playbook_2026-05-19.md`
>3. Text 5 Tier 1 contractors (15 min): Land Pro 440-320-2779 | GTP 440-396-0814 | Twin Improvements 216-773-0757 | Reliable Roofing 216-810-2497 | Pagels 216-956-5263
>THURSDAY MORNING: Read `outputs/vera/touch3_morning_brief_2026-05-22.md` first thing
>PHONE SCRIPT READY: `outputs/tommy/hot_lead_phone_script_2026-05-22.md`

---

⏰ *Vera — Action Needed: Run Danny's Pipeline TODAY (Summit County — 10 days overdue)*
>Command: `python3 workers/lead_pipeline.py danny` from `/Users/bradleyneal/forestcity`
>Expected: 15–20 new Summit County PMs (Akron/Fairlawn/Stow) auto-enrolled in Mixmax.
>Also set up cron per CLAUDE.md so it runs automatically every Monday.

---

⏰ *Vera — Action Needed: Create Gas Station + Fleet Sequences in Mixmax (June 2 target)*
>18 gas station contacts waiting. 15 minutes in Mixmax UI = they all auto-enroll.
>Gas station copy: `outputs/danny/sequence_gas_stations_2026-05-19.md`
>Fleet copy: `outputs/danny/sequence_fleet_washing_2026-05-18.md`
>Paste IDs into `integrations/mixmax.py` lines 48 and 54. Next pipeline run auto-enrolls everyone.

---

✅ *Vera — Scan Complete 2026-05-20 (Run 29)*
>4 auto-upgrades shipped | 2 new deliverables (June Residential Push brief, Quote Follow-Up Sequence) | 1 issue marked RESOLVED
>78 RESOLVED | 13 OPEN
>TODAY: Tonight's checklist + run Danny pipeline locally
>THURSDAY: Read touch3_morning_brief first thing
