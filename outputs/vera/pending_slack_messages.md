🔧 *Vera — Auto-Upgrade*
>Changed: workers/vera_relay.py — added _flush_unpushed_commits() before git pull --rebase
>Why: If a push failed mid-relay, next run would rebase a "cleared messages" commit on top of new Vera pushes, silently dropping all Slack messages. Now flushes unpushed commits first.
>File: workers/vera_relay.py
---
🔧 *Vera — Auto-Upgrade*
>Changed: agents/tommy.md — added may26_monday_morning_followup_texts_[date].md to output format list
>Why: File was created in Run 57 but not documented in tommy.md output format.
>File: agents/tommy.md
---
🔧 *Vera — Auto-Upgrade*
>Changed: agents/danny.md — updated Summit County urgency note to TODAY (May 23 = 2 days left)
>Why: Urgency note date was stale; refreshed to reflect Saturday May 23 and Sunday May 25 deadline.
>File: agents/danny.md
---
🔧 *Vera — Auto-Upgrade*
>Changed: scripts/crontab_setup.txt — added 2pm check_replies.py scan Mon-Fri
>Why: Reply window is active. Some contacts open emails in the morning and reply mid-afternoon. Double-scan adds 30 seconds of compute for same-day reply detection.
>File: scripts/crontab_setup.txt
---
🔧 *Vera — Auto-Upgrade*
>Changed: agents/jasmine.md — added linkedin_posts_may26_week_[date].md to output format
>Why: LinkedIn posts for May 26-30 were missing from the output format catalog.
>File: agents/jasmine.md
---
📄 *Vera — New Deliverable*
>File: outputs/jasmine/linkedin_posts_may26_week_2026-05-23.md
>What: 3 LinkedIn posts for May 26 (Mon), May 28 (Wed), May 30 (Fri) targeting PMs + contractors
>Post 1: HOA board meeting season + budget allocation angle
>Post 2: Before/after commercial ROI hook (warm-up for hot leads who opened email)
>Post 3: Contractor referral partnership pitch
>Each post includes a DM reuse guide — Bradley can paste the post link in LinkedIn DMs as a conversation opener with PM connects.
---
📄 *Vera — New Deliverable*
>File: outputs/donna/june_commercial_calendar_2026-05-23.md
>What: 4-week commercial action calendar, May 26 through June 18
>Covers: Summit/Medina pulls (May 26), Round 2 enrollment gate (June 4), ads launch, LinkedIn wave schedule, contractor follow-up waves, revenue math ($10,600-$16,000 potential)
>Every task has an owner, time, and linked resource file. This is the master view for the next 4 weeks.
---
🚨 *Vera — SUMMIT COUNTY DEADLINE: SUNDAY NIGHT MAY 25*
>TODAY is Saturday May 23. 2 days left. After May 25, Summit rotation doesn't return until July 6 (6-week gap during peak season).
>Command (run from /Users/bradleyneal/forestcity): python3 workers/lead_pipeline.py danny Summit
>5-minute task. Round 2 enrollment (June 4) depends on having Summit leads in the pool.
---
💡 *Vera — Upgrade Proposal*
>Idea: Yard sign + on-site 3-QR-code referral card
>Why: Bradley visits homes for every job. Neighbors watch. A yard sign ("Just cleaned by Forest City") + a wallet card with 3 QR codes (Google Review / Facebook Follow / Refer a Neighbor text) costs ~$15 to print and captures word-of-mouth at the highest-leverage moment — right after the job looks amazing.
>Impact: Neighbor referrals from direct sightlines. No digital system needed. Tommy writes the card copy, print at FedEx Office.
>Reply YES to approve and Tommy will write the yard sign + referral card copy this week.
---
💡 *Vera — Upgrade Proposal*
>Idea: Referral partner voicemail scripts for Carla's warm contractor contacts
>Why: ~40 contractor/realtor contacts opened Carla's emails but haven't replied. At this stage, one 30-second voicemail outperforms a 4th email. Tommy would write 3 voicemail variants (contractor / realtor / HVAC) + a follow-up text template.
>Impact: Referral network activation before June Booking Blitz. One active referral partner = 2-4 jobs/month minimum.
>Reply YES to approve and Tommy will write the scripts.
---
✅ *Vera — Scan Complete 2026-05-23*
>5 auto-upgrades shipped | 2 deliverables | 2 proposals | 17 open issues (all require Bradley action)
>New RESOLVED this run: vera_relay unpushed-commit flush (prevents silent Slack message loss)
>Top priority TODAY: (1) Summit County pull — python3 workers/lead_pipeline.py danny Summit (2) LinkedIn Post 1 + 5 PM connects (3) Pause Instantly.ai a1c08c3d + 626cd15d — 3 min
>Master calendar for May 26-June 18: outputs/donna/june_commercial_calendar_2026-05-23.md
