🔧 *Vera — Auto-Upgrade (Run 47)*
>Changed: workers/jasmine_flyer.py — guarded `import requests` at module level with try/except + `_REQUESTS_AVAILABLE` flag. `push_to_github()` and `post_to_slack()` now raise clear RuntimeError when requests not installed instead of crashing with NoneType.
>Why: Same class of bug as the PIL crash (fixed run 46) — unguarded hard import breaks the module in any environment without requests installed.
>File: workers/jasmine_flyer.py

---

📋 *Vera — New Deliverable (Run 47)*
>File: outputs/donna/may26_blitz_action_card.md
>What: Single-screen May 26 morning action card — 8 priorities in order with time estimates, all scripts linked, phone-sized quick reference. May 26 is the highest-action day of the week.
>Top 3 items: Touch 3 reply check → 3 contractor follow-ups → 5 Tier 1 new lead texts.

---

📋 *Vera — New Deliverable (Run 47)*
>File: outputs/vera/email_deliverability_checklist_2026-05-22.md
>What: Fresh angle on the 0% reply rate. Step-by-step deliverability audit: Mixmax stats check, sequence sending verify, mail-tester.com spam score, SPF/DKIM check, Instantly.ai overlap investigation. Decision tree maps each finding to an action.
>Why: 0 replies after 3 touches to 45 contacts is a deliverability signal, not just a message problem. Most likely culprit: Instantly.ai running in parallel and triggering spam flags.

---

📋 *Vera — New Deliverable (Run 47)*
>File: scripts/danny_launchd_plist.xml
>What: macOS launchd plist alternative to cron for Danny's weekly pipeline run. More reliable on macOS — queues missed runs if Mac was asleep, unlike cron which simply skips.
>Install: `cp scripts/danny_launchd_plist.xml ~/Library/LaunchAgents/com.forestcity.danny.plist && launchctl load ~/Library/LaunchAgents/com.forestcity.danny.plist`
>Why: Cron has been down 10+ days. launchd is the right tool for scheduled tasks on Mac.

---

🚨 *Vera — TODAY May 22 — 3 Priority Actions Right Now*

Touch 3 fired this morning. The 72-hour reply window closes May 24.

1️⃣ *Check Mixmax → Property Manager sequence for replies NOW* (5 min)
   → Any replies? Use `outputs/tommy/touch3_reply_response_templates_2026-05-20.md`
   → 0 opens on ALL 45 contacts? Run deliverability check: `outputs/vera/email_deliverability_checklist_2026-05-22.md`

2️⃣ *LinkedIn connects — top 5 most-opened contacts* (5 min)
   → Protocol: `outputs/tommy/touch3_open_trigger_protocol_2026-05-21.md`

3️⃣ *Check and pause Instantly.ai campaigns* (2 min)
   → This may be the reason for 0 replies — duplicate emails triggering spam flags
   → Mixmax is your sole platform. Instantly should be off.

---

💡 *Vera — Upgrade Proposal (Run 47)*
>Idea: Switch Danny's weekly cron from crontab to macOS launchd (scripts/danny_launchd_plist.xml already written)
>Why: cron on macOS silently skips when the Mac is asleep. launchd queues the job and fires it when the machine wakes. The 10-day gap in Danny's pipeline would not have happened with launchd.
>Impact: Reliable weekly lead pulls even on holiday weekends. No more manual intervention.
>Reply YES to approve and I'll write the install instructions as a one-liner.

---

💡 *Vera — Upgrade Proposal (Run 47)*
>Idea: Add a Mixmax open notification → personal Gmail bridge email automation. When a contact opens 3+ times with no reply, Mixmax can trigger a personal email from Bradley's Gmail (not the sequence) the same day.
>Why: Hot leads who open 3+ times are interested but not replying to automated emails. A personal Gmail email from Bradley breaks the automation pattern and typically gets a reply.
>Impact: Converts 1–3 of the most engaged contacts in the current sequence into actual conversations. Zero cost, 15 minutes to set up in Mixmax.
>Reply YES to approve and I'll write the Mixmax trigger setup guide.

---

✅ *Vera — Scan Complete 2026-05-22 (Run 47)*
>1 auto-upgrade shipped | 2 proposals | 15 open issues (1 resolved — jasmine_flyer requests guard)
>Key fix: jasmine_flyer.py requests import guard (same class as PIL crash run 46)
>Key deliverable: email_deliverability_checklist_2026-05-22.md — fresh angle on 0% reply rate
>Top action for Bradley: Run deliverability checklist NOW and pause Instantly.ai before Touch 3 window closes May 24
