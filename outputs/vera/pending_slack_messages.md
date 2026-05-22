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
