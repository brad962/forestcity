🔧 *Vera — Auto-Upgrade*
>Changed: workers/check_replies.py — added company enrichment to hot leads output
>Why: Hot leads Slack notification showed name + opens + phone but no company. Bradley couldn't tell a PM from a contractor at a glance. Now shows company next to name in both terminal and Slack output.
>File: workers/check_replies.py
---
🔧 *Vera — Auto-Upgrade*
>Changed: agents/donna.md — added june1_prep_checklist and june_commercial_calendar to output format list
>Why: Both files were created (Runs 58-59) but not catalogued in donna.md — output format list was out of sync.
>File: agents/donna.md
---
🔧 *Vera — Auto-Upgrade*
>Changed: agents/rick.md — made urgency date generic instead of a hard-coded daily date
>Why: "May 23" was going stale every day, requiring manual updates. Changed to "late May 2026" so the urgency message stays accurate without daily edits.
>File: agents/rick.md
---
🔧 *Vera — Auto-Upgrade*
>Changed: agents/tommy.md — added may25_sunday_evening_protocol to output format list
>Why: New deliverable created this run; catalogued in tommy.md for future reference.
>File: agents/tommy.md
---
🔧 *Vera — Auto-Upgrade*
>Changed: agents/danny.md — added gas_station_mixmax_sequence_creation to output format list
>Why: New deliverable created this run; catalogued in danny.md for future reference.
>File: agents/danny.md
---
📄 *Vera — New Deliverable*
>File: outputs/danny/gas_station_mixmax_sequence_creation_2026-05-23.md
>What: Step-by-step Mixmax UI walkthrough to create the Gas Station sequence — includes exact subject lines, email bodies, send timing, and where to copy the sequence ID. After creating: paste ID into integrations/mixmax.py → run `python3 workers/lead_pipeline.py pending` → 18 contacts auto-enroll. Total time: 5 minutes.
>Why now: 18 district manager contacts have been sitting unenrolled since May 19 (4 days idle). Each DM manages 5-15 locations. One account = recurring multi-site revenue.
---
📄 *Vera — New Deliverable*
>File: outputs/tommy/may25_sunday_evening_protocol_2026-05-23.md
>What: Sunday evening (tonight) window-close protocol — exactly what to do at 8pm: run check_replies, handle any replies, if 0 replies: pause Instantly.ai (3 min), send LinkedIn connects to hot leads, queue bridge emails for Monday 9am, set alarm for Monday morning 90-min blitz schedule.
>Why now: The 72-hour reply window closes TONIGHT. This is the pivot moment. Clear action plan prevents wasted time and captured opportunities.
---
🚨 *Vera — REPLY WINDOW CLOSES TONIGHT (Sunday May 25)*
>Touch 3 fired Thursday May 22. The 72-hour window ends tonight.
>If 0 replies by tonight → the sequence is spent. Monday pivot is ready.
>TONIGHT'S 15-min protocol: outputs/tommy/may25_sunday_evening_protocol_2026-05-23.md
>Step 1: `python3 workers/check_replies.py` — see exact reply count
>Step 2: If 0 replies → pause Instantly.ai (a1c08c3d + 626cd15d) — 3 min, 2 clicks each
>Step 3: LinkedIn connects with top 5 hot leads — seen Monday morning
>Step 4: Queue bridge emails for Monday 9am
---
💡 *Vera — Upgrade Proposal*
>Idea: Post-job doorstep video testimonial protocol
>Why: Bradley visits every job site. Right after finishing — when the house looks incredible and the homeowner is delighted — is the single best moment to capture a video testimonial. A 15-second phone video ("I was nervous but look at this") becomes a Facebook Reel, an Instagram post, a Google review prompt, and a social proof ad. The moment costs zero dollars and is the most powerful content format for local services.
>Impact: 1 video/week = 4-5 reels/month. Authentic before/after content that runs as ads performs 3-5x better than static images. Revenue from social proof compounds over the summer.
>Execution: Tommy writes the ask script (3 sentences Bradley says at the door). Jasmine writes 3 caption variations for each video. Launch next job.
>Reply YES to approve and Tommy + Jasmine produce the protocol this week.
---
💡 *Vera — Upgrade Proposal*
>Idea: CAI Ohio Chapter vendor directory listing
>Why: The Community Associations Institute (CAI) is the professional association for HOA and property managers — exactly Danny's audience. The Ohio chapter maintains a vendor directory that PMs actively reference when vetting service providers. A listing costs $150-300/year and puts Forest City in front of decision-makers who are ALREADY looking for vendors like us.
>Impact: Inbound leads from PMs searching the vendor directory. Adds third-party credibility to Danny's cold emails ("we're a CAI-listed vendor"). Compounds over time as the listing generates reviews.
>Action needed: Bradley joins as a vendor member at caionline.org → Ohio chapter → vendor directory listing.
>Reply YES to approve and Vera will write the listing copy.
---
✅ *Vera — Scan Complete 2026-05-23 (Run 60)*
>5 auto-upgrades shipped | 2 deliverables | 2 proposals | 17 open issues (all require Bradley action)
>New this run: check_replies.py company enrichment; gas station creation guide (5 min to unlock 18 contacts); Sunday evening reply window close protocol
>TONIGHT: Reply window closes. Run the protocol: outputs/tommy/may25_sunday_evening_protocol_2026-05-23.md
>MONDAY May 26: Bridge emails 9am → Danny Summit pull 8:15am → Facebook Ads launch 9am → gas station sequence creation 10am
