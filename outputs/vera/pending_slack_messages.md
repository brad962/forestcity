🔧 *Vera — Auto-Upgrade*
>Changed: integrations/mixmax.py PROPERTY_MANAGER_TITLES — added 'leasing manager', 'managing partner', 'principal'
>Why: All 3 were in DANNY_TITLES and Apollo search but absent from routing — manual imports now route to PM sequence correctly
>File: integrations/mixmax.py
---
🔧 *Vera — Auto-Upgrade*
>Changed: workers/check_replies.py — added Slack notification when hot leads exist (not just replies)
>Why: During the 72-hour post-Touch-3 window, Bradley needs to know how many opens happened even if 0 replies — gets daily Slack summary with names + open counts
>File: workers/check_replies.py
---
🔧 *Vera — Auto-Upgrade*
>Changed: workers/workiz_report.py — removed dead JOB_TYPE_FILTER constant
>Why: Was defined but never used; JOB_TYPE_VARIANTS is the live filter; dead code removed
>File: workers/workiz_report.py
---
🔧 *Vera — Auto-Upgrade*
>Changed: workers/vera_relay.py — added lock file protection (_acquire_lock/_release_lock, 3-min stale timeout)
>Why: Cron fires every 5 min; if git took >5 min two instances would collide on push; lock file prevents this
>File: workers/vera_relay.py
---
🔧 *Vera — Auto-Upgrade*
>Changed: integrations/mixmax.py enroll_lead() — added Instantly.ai overlap warning in docstring
>Why: Code-level persistent reminder before any Round 2 enrollment: pause campaigns a1c08c3d + 626cd15d first
>File: integrations/mixmax.py
---
📄 *Vera — New Deliverable*
>File: outputs/tommy/hoa_spring_meeting_email_2026-05-22.md
>What: 3 email variants for Round 2 PM sequence using HOA board meeting season angle
>Why: May–June is when NE Ohio HOA boards meet to evaluate vendors. "Before your board meeting" is timely + specific — competitors don't use it. Variants: board meeting, resident complaints, vendor evaluation. Send June 4 at 10:30am.
---
📄 *Vera — New Deliverable*
>File: outputs/donna/weekend_lead_gen_checklist_2026-05-22.md
>What: Memorial Day weekend (May 23–25) free lead gen checklist — runs parallel to reply window monitoring
>Why: Homeowners are on Facebook and Nextdoor all weekend. 90 minutes: 3 FB group posts, GBP photo, 5 past customer texts, Nextdoor setup. Zero ad spend. Bridges to the May 26 paid blitz.
---
🚨 *Vera — TONIGHT Priority (May 22)*
>1. Pause Instantly.ai campaigns a1c08c3d + 626cd15d — 3 min: outputs/vera/instantly_pause_guide_2026-05-22.md
>2. LinkedIn connects with 2+ open contacts — context is live TONIGHT while "just sent you an email" is fresh
>3. Run check_replies.py locally if possible to get live open count

🗓️ *Vera — Weekend Plan (May 23–25)*
>Checklist: outputs/donna/weekend_lead_gen_checklist_2026-05-22.md
>Sat morning (30 min): 3 Facebook homeowner group posts + GBP photo upload
>Sun morning (30 min): 5 past customer texts + Nextdoor setup
>Mon May 26: Danny pull + ads launch + contractor texts + check_replies.py at 9am
---
💡 *Vera — Upgrade Proposal*
>Idea: Shift Round 2 PM enrollment from June 4 to June 9 if Danny cron hasn't run by May 26
>Why: Next auto-run is June 1; if it fails, June 4 enrollment uses 3-week-old leads. June 9 gives buffer.
>Impact: Higher quality Round 2 contacts (Summit + Medina fresh); Wednesday June 9 = stronger send day
>Reply YES to approve schedule shift — only applies if manual Danny pull doesn't happen by May 26.
---
✅ *Vera — Scan Complete 2026-05-22 (Run 54)*
>4 auto-upgrades shipped | 2 deliverables | 1 proposal | 59 RESOLVED | 17 OPEN
>Touch 3 reply window LIVE — 72 hours through Sunday May 25
>Key items: Instantly.ai pause TONIGHT, weekend free lead gen, May 26 blitz day
