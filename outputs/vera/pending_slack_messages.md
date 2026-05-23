🔧 *Vera — Auto-Upgrade*
>Changed: integrations/mixmax.py CONTRACTOR_TITLES — added 'irrigation', 'sprinkler'
>Why: Irrigation/sprinkler companies are in CARLA_SEARCHES keywords but were missing from routing detection — contacts with these titles were silently defaulting to wrong sequence
>File: integrations/mixmax.py
---
🔧 *Vera — Auto-Upgrade*
>Changed: integrations/mixmax.py PROPERTY_MANAGER_TITLES — added 'leasing director', 'center manager'
>Why: Commercial/retail segment gap — office building leasing directors and shopping center managers were not being routed to PM sequence; significant commercial PM segment now covered
>File: integrations/mixmax.py
---
🔧 *Vera — Auto-Upgrade*
>Changed: workers/lead_pipeline.py DANNY_TITLES + DANNY_ORG_KEYWORDS — added 'leasing director', 'center manager' to titles; added 'shopping center management', 'office building management', 'retail property management', 'commercial building management' to org keywords
>Why: Commercial/retail property segment (shopping centers, office buildings) was entirely missing from Apollo search parameters
>File: workers/lead_pipeline.py
---
🔧 *Vera — Auto-Upgrade*
>Changed: workers/lead_pipeline.py — added `--county` override CLI flag: `python3 workers/lead_pipeline.py danny Summit` forces Summit County pull regardless of week rotation
>Why: CRITICAL — Summit County window closes this Sunday (May 25). May 26 = Week 22 = Medina. Without this override, Summit is gone until July 6. Now Bradley can force any county any time.
>File: workers/lead_pipeline.py
---
🔧 *Vera — Auto-Upgrade*
>Changed: workers/nina_report.py — injected phone into replied_contacts in both daily and weekly reports; added Phone column to REPLIED table
>Why: When a contact replies, Bradley needs the phone number immediately to call back — it was missing from the replied table (only hot_leads had phone)
>File: workers/nina_report.py
---
🔧 *Vera — Auto-Upgrade*
>Changed: workers/check_replies.py — added _load_phone_map(); phone now shown in terminal output and Slack notification for replied contacts
>Why: Same issue as nina_report — when a reply comes in, the Slack alert should show the phone number so Bradley can call within the 1-hour reply window
>File: workers/check_replies.py
---
🔧 *Vera — Auto-Upgrade*
>Changed: agents/danny.md — updated Summit County urgency note with explicit deadline: "Window closes May 25 (Sunday). May 26 = Medina County rotation. Summit not available again until July 6."
>Why: Previous note said "Run NOW (May 22+)" without explaining that May 26 is already too late for Summit County — deadline is now crystal clear
>File: agents/danny.md
---
📄 *Vera — New Deliverable*
>File: outputs/donna/june_week2_sprint_2026-05-22.md
>What: June 9–13 day-by-day sprint — Monday Geauga+Portage pull + round 2 open-rate check, Tuesday contractor follow-up wave 2, Wednesday GBP + Google Guaranteed status, Thursday round 2 DMs, Friday weekly report + week 3 prep. Full metric targets table.
>Why: June Week 1 sprint existed but Week 2 was undocumented — this closes the gap and keeps momentum through the June Booking Blitz
---
📄 *Vera — New Deliverable*
>File: outputs/tommy/hot_lead_bridge_email_may26_2026-05-22.md
>What: Personal Gmail bridge email templates (3 versions: direct, problem-first, mobile-short) for top 5 hot leads on May 26 — sent from Bradley's real inbox after the Mixmax sequence ends
>Why: If the 72-hour window closes May 25 with 0 replies, the best move Monday is a personal email that bypasses spam filters and looks nothing like the automated sequence. Includes timing guide, personalization notes by lead type, and "no reply by Wed → phone" protocol.
---
🚨 *Vera — SUMMIT COUNTY DEADLINE (closes Sunday May 25)*

The automated cron hasn't run since May 12. Summit County = Week 21 (this week). After Sunday night, the rotation shifts to Medina County (Week 22 = May 26+) and **Summit won't run again until July 6 (Week 27).**

That's 6 weeks of Summit pipeline gap during peak summer.

Run this NOW (works any time this weekend):
`python3 workers/lead_pipeline.py danny Summit`

Or force any county at any time (new flag added this run):
`python3 workers/lead_pipeline.py danny Medina` (for May 26+)

---
💡 *Vera — Upgrade Proposal*
>Idea: File the Google Guaranteed (Local Services Ads) application THIS WEEKEND, not Monday May 26
>Why: Application approval takes 7–14 days. If filed today (May 22-23), it could be live by June 5 — right when the June Booking Blitz starts. If filed May 26, the earliest it's live is June 9-12 (Week 2). Filing this weekend gains a full week of Google Guaranteed leads at peak season.
>Impact: Google Guaranteed appears above all regular ads. Pay-per-lead (~$15-35/lead). 40-60% close rate. Most NE Ohio power washing competitors haven't set it up.
>Action: 10-15 min to apply. Guide: `outputs/rick/google_guaranteed_setup_2026-05-22.md`. Reply YES and I'll add a reminder trigger for you.
---
✅ *Vera — Scan Complete 2026-05-22 (Run 56)*
>7 auto-upgrades shipped | 2 deliverables | 1 proposal | 67 RESOLVED | 17 OPEN
>Key fixes: irrigation/sprinkler routing, commercial PM segment (leasing director, center manager, shopping centers), replied contacts now show phone number, Danny county override CLI flag
>🚨 Summit County window CLOSES SUNDAY: `python3 workers/lead_pipeline.py danny Summit`
>May 26 playbook: bridge emails to top 5 hot leads + ads launch + Medina County pull
---
🔧 *Vera — Auto-Upgrade (Run 57)*
>Changed: integrations/mixmax.py CONTRACTOR_TITLES — removed 2 duplicate keywords ('deck contractor' + 'driveway seal' appeared twice each); added 'tree service', 'tree care', 'arborist' as new routing keywords
>Why: Duplicates were harmless but sloppy. Tree service/arborists are high-value referral partners (visit properties constantly, see dirty roofs) and were missing entirely — they were routing to fleet_washing sequence instead of contractor
>File: integrations/mixmax.py
---
🔧 *Vera — Auto-Upgrade (Run 57)*
>Changed: integrations/mixmax.py PROPERTY_MANAGER_TITLES + workers/lead_pipeline.py DANNY_TITLES — added 4 new PM title variants: 'site manager', 'community director', 'building operations manager', 'property administrator'
>Why: Residential community site managers, HOA community directors, commercial building ops managers, and PM administrators were all missing — they sign vendor contracts but weren't being detected
>File: integrations/mixmax.py, workers/lead_pipeline.py
---
🔧 *Vera — Auto-Upgrade (Run 57)*
>Changed: workers/lead_pipeline.py CARLA_SEARCHES — added 'tree service', 'tree care', 'arborist' to contractor search keywords
>Why: Arborists + tree services visit properties every season and see dirty roofs/siding constantly — natural referral partners, completely missing from Apollo search
>File: workers/lead_pipeline.py
---
🔧 *Vera — Auto-Upgrade (Run 57)*
>Changed: workers/check_replies.py — added phone number to hot leads Slack notification format
>Why: When check_replies.py posts hot leads to Slack, the phone was missing from the message — Bradley had to look it up separately. Now shows: Name — X opens | Sequence | 📞 phone
>File: workers/check_replies.py
---
🔧 *Vera — Auto-Upgrade (Run 57)*
>Changed: agents/donna.md — added 3 missing output format entries (weekend_lead_gen_checklist, june_week2_sprint, sunday_may24_action_card)
>Why: Files existed in outputs/donna/ but weren't documented in donna.md output format list — makes it harder for Donna to know what she's produced
>File: agents/donna.md
---
📋 *Vera — Deliverable (Run 57)*
>File: outputs/vera/sunday_may24_action_card.md
>What: Single-screen Sunday May 24 action card — 6 priorities with scripts, timing, and tracking table
>Key items: check Mixmax replies first, 5 past customer texts, Nextdoor post, GBP photo, LinkedIn connects, SUMMIT COUNTY PULL TONIGHT
---
📋 *Vera — Deliverable (Run 57)*
>File: outputs/tommy/may26_monday_morning_followup_texts.md
>What: Personal text scripts for Monday May 26 — one-at-a-time texts to top 5-8 hot leads after 72-hour reply window closes
>Includes: 3 PM versions, 2 contractor versions, 1 realtor version, timing guide, response scripts, DO NOT rules
---
🚨 *Vera — SUMMIT COUNTY DEADLINE: TONIGHT*
>Summit County window = Week 21 = closes SUNDAY NIGHT MAY 25.
>May 26 = Week 22 = Medina County. No way back to Summit until July 6.
>ONE COMMAND — runs in 5 minutes:
>`python3 workers/lead_pipeline.py danny Summit`
>This is 11 days of missed leads. Run it tonight.
---
🚨 *Vera — REPLY WINDOW: Day 2 of 3*
>Touch 3 fired Thursday May 22. Window closes Monday May 25.
>TODAY: Run check_replies.py to see if anyone opened over the weekend.
>If 0 replies by May 25 → Monday May 26 pivot: bridge emails + personal texts (file: outputs/tommy/may26_monday_morning_followup_texts.md)
>Instantly.ai campaigns a1c08c3d + 626cd15d still need to be PAUSED before Round 2. 3-minute fix.
---
✅ *Vera — Scan Complete 2026-05-23 (Run 57)*
>5 auto-upgrades shipped | 2 deliverables | 0 new proposals | 17 open issues (0 closed this run)
>Key actions needed TODAY: (1) Danny Summit pull TONIGHT (2) Pause Instantly.ai (3) LinkedIn connects with hot leads
