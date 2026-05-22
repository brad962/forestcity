🔧 *Vera — Auto-Upgrade*
>Changed: workers/lead_pipeline.py — Added 'managing partner' and 'principal' to DANNY_TITLES
>Why: Small HOA/PM firm decision-makers often list these titles on Apollo — were being missed entirely by the Apollo search
>File: workers/lead_pipeline.py

---

🔧 *Vera — Auto-Upgrade*
>Changed: workers/vera_relay.py — Added _check_carla_staleness() function mirroring Danny's staleness check
>Why: If Carla's cron also goes silent, the referral partner pipeline dries up before the June Booking Blitz — now alerts if > 10 days since last Carla pull
>File: workers/vera_relay.py

---

🔧 *Vera — Auto-Upgrade (NEW WORKER)*
>Changed: Created workers/check_replies.py — 30-second Mixmax reply checker
>Why: Touch 3 fired today. Bradley needs a fast daily check for replies without running the full nina_report. Checks all 3 sequences, prints results, posts to Slack if replies found.
>Run: `cd /Users/bradleyneal/forestcity && python3 workers/check_replies.py`
>File: workers/check_replies.py

---

🔧 *Vera — Auto-Upgrade*
>Changed: scripts/crontab_setup.txt — Added check_replies.py to crontab (Mon-Fri 8:45am)
>Why: Automated daily reply scan during active sequence windows — fires 45 min after Nina's daily report, catches any overnight replies
>File: scripts/crontab_setup.txt

---

📋 *Vera — Deliverable*
>File: outputs/vera/reply_window_tracker_2026-05-22.md
>What: 72-hour post-Touch 3 reply window guide — day-by-day checklist May 22–26, reply response protocol, Round 2 decision criteria, metrics tracker
>Use it: Run check_replies.py each morning. If 0 replies by May 25 → decision gate in outputs/donna/may25_round2_decision_gate_2026-05-22.md

---

🚨 *Vera — TONIGHT Priority (May 22)*
>Touch 3 fired today. The 72-hour reply window is OPEN right now.
>
>Do these 3 things before you go to sleep:
>1. Pause Instantly.ai (3 min): outputs/vera/instantly_pause_guide_2026-05-22.md — eliminates #1 suspected cause of 0% replies
>2. Send Tier 1 contractor texts: Anthony (440-320-2779), Dontez (440-396-0814), Chris (216-773-0757), Venus (216-810-2497), Logan (216-956-5263) — scripts at outputs/tommy/contractor_referral_text_script_2026-05-20.md
>3. Connect on LinkedIn with anyone who opened your emails 2+ times — context is freshest right now
>
>Tomorrow morning 9am: run `python3 workers/check_replies.py` — see instantly if anything landed.

---

💡 *Vera — Upgrade Proposal*
>Idea: LinkedIn Sponsored InMail targeting NE Ohio property managers (new acquisition channel)
>Why: Email open rates are 30–40% even when deliverability is clean. LinkedIn Message Ads to property managers in NE Ohio get 50–60% open rates with no spam filter risk. Zero overlap with Mixmax sequences.
>Impact: New channel reaching same ICP (property managers) through a different inbox. Could break the 0-reply pattern while email Round 2 spins up. Cost: ~$1/send, 100 PMs = ~$100. One booked commercial job = $300–600.
>What's needed: LinkedIn Campaign Manager access (free), Business Manager page (free), $100 test budget.
>Reply YES to approve and I'll write the InMail copy + targeting setup guide.

---

💡 *Vera — Upgrade Proposal*
>Idea: Nextdoor neighborhood posting routine (free residential lead gen)
>Why: Nextdoor is hyper-local and NE Ohio homeowners actively ask neighbors for contractor recommendations. Donna already wrote a template (outputs/donna/nextdoor_post_template_2026-05-19.md) — no posting routine exists yet to use it.
>Impact: 3–5 quote requests per month from neighborhoods where jobs were just completed. Completely free.
>What's needed: Bradley signs up at nextdoor.com/business, posts after each job with Jasmine's before/after photo + the template. 5 min per job.
>Reply YES to approve and I'll write the full Nextdoor posting SOP.

---

✅ *Vera — Scan Complete 2026-05-22 (Run 52)*
>4 auto-upgrades shipped | 2 proposals | 17 open issues (0 new, 0 closed)
>
>Shipped: DANNY_TITLES managing_partner+principal, Carla staleness check in vera_relay, new check_replies.py worker, crontab updated with daily reply check
>
>Bradley action needed:
>🔴 Pause Instantly.ai TONIGHT — outputs/vera/instantly_pause_guide_2026-05-22.md
>🔴 Run check_replies.py tomorrow 9am
>🔴 Danny pipeline manual run (10 days overdue): python3 workers/lead_pipeline.py both
>🟡 Ads launch May 26 — outputs/vera/may26_ads_launch_checklist_2026-05-22.md
>🟡 GBP first post — outputs/vera/gbp_post_may21_2026.md
