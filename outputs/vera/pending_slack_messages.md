🔧 *Vera — Auto-Upgrade*
>Changed: rick.md output catalog — added `google_guaranteed_setup_[date].md` + `facebook_lead_gen_launch_checklist_[date].md`
>Why: Both files exist in outputs/rick/ since runs 55 and 68 but were invisible to any agent reading rick.md; catalog gap closed
>File: agents/rick.md
---
🔧 *Vera — Auto-Upgrade*
>Changed: jasmine.md output catalog — added `instagram_stories_scripts_[date].md` format entry
>Why: Instagram Stories is the highest-engagement format for before/after content; Stories channel was never formally opened despite being mentioned in the capture protocol; format now documented so Jasmine can produce it on request
>File: agents/jasmine.md
---
🔧 *Vera — Auto-Upgrade*
>Changed: donna.md output catalog — added `monday_memorial_day_final_check_[date].md` format entry
>Why: File was created Run 68 but not added to Donna's catalog; now documented as a named deliverable type
>File: agents/donna.md
---
📄 *Vera — New Deliverable: Facebook Lead Response SOP*
>File: `outputs/rick/facebook_lead_response_sop_2026-05-24.md`
>What: Step-by-step SOP for the exact moment a Facebook Lead Gen form comes in — notification setup, 5-min call target, live call script, voicemail script, text follow-up, Day 2 follow-up, Workiz logging, pricing reference, objection handling
>Why: Ads launch TUESDAY. Without this, you'll miss the 5-minute response window. First company to call wins 40%+ of leads. READ THIS BEFORE LAUNCHING ADS.
---
📄 *Vera — New Deliverable: June GBP Content Calendar*
>File: `outputs/vera/june_gbp_content_calendar_2026-05-24.md`
>What: 5 GBP posts for all of June (publish every Monday June 2–30), each with hook, body, image guidance, CTA, and SEO keywords
>Why: Weekly GBP posts = higher ranking for "power washing Cleveland" searches in peak season. 2 minutes per post. Zero cost. June = highest search volume of the year.
---
📄 *Vera — New Deliverable: Instagram Stories Scripts*
>File: `outputs/jasmine/instagram_stories_scripts_2026-05-24.md`
>What: 5 peak-season Story scripts — before/after reveal, roof reveal (question sticker for algorithm boost), neighbor hook, customer reaction, Friday urgency. Each is 15–30 sec, shot on phone, no editing required.
>Why: Stories reach more followers than feed posts. Before/after Stories drive more DMs than any other format. Zero production cost — just shoot on-site.
---
🚨 *Vera — CRITICAL: Reply Window Closes TOMORROW*
>Monday May 25 (Memorial Day) = reply window close. Run `python3 workers/check_replies.py` at 10am.
>Protocol: `outputs/donna/monday_memorial_day_final_check_2026-05-24.md` (10 min)
>0 replies = that's fine — Round 2 is fully staged for June 4 with VOC-rewritten copy
>All Round 2 assets ready: PM sequence rewrite ✅ | Contractor sequence rewrite ✅ | Enrollment readiness checklist ✅
---
🚨 *Vera — CRITICAL: Instantly.ai Still Running (11 days until Round 2)*
>app.instantly.ai → Campaigns → ⋮ → Pause: a1c08c3d AND 626cd15d
>3 minutes. Every day not paused = less deliverability recovery before June 4 enrollment.
>After pausing: add INSTANTLY_PAUSED=true to your .env — turns off the runtime warning in enroll_batch()
---
💡 *Vera — Upgrade Proposal*
>Idea: Build the actual "Northeast Ohio Home Maintenance Checklist" content — not just the brief
>Why: Donna's brief (`outputs/donna/lead_magnet_home_maintenance_checklist_2026-05-12.md`) has been in the repo since May 12. The actual checklist content — month-by-month exterior maintenance guide that homeowners would give an email address for — was never written. This is a PDF-ready lead magnet waiting to happen.
>Impact: Email list growth channel. Every homeowner who downloads it gets a 3-email nurture sequence → estimate request. Zero ad spend leads. Kit.com handles delivery free up to 10k subscribers.
>Reply YES to approve and Tommy + Donna build the content + delivery sequence.
---
💡 *Vera — Upgrade Proposal*
>Idea: Set up Facebook Messenger auto-reply for keyword triggers
>Why: When people DM Forest City on Facebook after seeing an organic post or ad, they often wait hours for a reply. Meta Business Suite has built-in auto-reply for keywords like "quote," "price," "cost," "how much" — no code required, takes 10 minutes to configure.
>Impact: Every Facebook DM gets an immediate response even at 10pm. Keeps the conversation warm until Bradley can follow up personally. No missed leads from late-night DMs.
>Reply YES and Jasmine writes the 5 auto-reply message versions.
---
✅ *Vera — Scan Complete 2026-05-24 (Run 69)*
>3 auto-upgrades shipped | 3 new deliverables | 2 proposals | 0 new issues | 18 open (all need Bradley action)
>TODAY priority: (1) Text Anthony 440-320-2779 + Venus 216-810-2497 — 5 min (2) Pause Instantly.ai — 3 min (3) GBP post June Week 1 — 2 min
>MONDAY priority: Run check_replies.py at 10am — `outputs/donna/monday_memorial_day_final_check_2026-05-24.md`
>TUESDAY priority: READ facebook_lead_response_sop BEFORE launching ads → then `tuesday_may26_launch_card_2026-05-23.md`

---
🔧 *Vera — Auto-Upgrade (Run 70)*
>Changed: agents/rick.md — "Monday after Memorial Day" → "Tuesday after Memorial Day" in the Ready Assets section header
>Why: The sub-items on the next two lines correctly said Tuesday, but the header on line 52 still said Monday — survived 9 previous runs because all prior fixes targeted the urgency preamble, not this section
>File: agents/rick.md

---
🔧 *Vera — Auto-Upgrade (Run 70)*
>Changed: agents/carla.md — added realtor_summer_voc_sequence_[date].md to output format catalog
>Why: Summer listing season is live in NE Ohio; realtor segment hasn't had fresh outreach since May 12 (6+ weeks); VOC-rewritten sequence now queued for June 4 enrollment alongside Round 2 PM batch
>File: agents/carla.md

---
🔧 *Vera — Auto-Upgrade (Run 70)*
>Changed: agents/tommy.md — added hot_lead_callback_script_[date].md to output format catalog; agents/donna.md — added may26_week_priority_stack_[date].md; agents/danny.md — added gas_station_manual_email_blast_[date].md (file existed in outputs/danny/ since May 20, catalog entry missing until now)
>Why: Three formats in active use with no catalog entry — documentation gap closes this run
>Files: agents/tommy.md, agents/donna.md, agents/danny.md

---
📋 *Vera — New Deliverable (Run 70)*
>File: outputs/carla/realtor_summer_voc_sequence_2026-05-24.md
>What: 3-touch realtor referral sequence rewritten for summer listing season using Marcus's NE Ohio VOC library. Hooks: "before the lockbox goes up," "black roof stains," "noticeable difference in photos." 3 trade-specific Touch 1 variants (large brokerages, social agents, buyer's agents transitioning to listings). Response handling for YES / not now / commercial/HOA inquiry. Send June 4 alongside Round 2 PM enrollment.
>Revenue math: 10 realtor partners × 4 referrals/summer × $450/job = $18,000 incremental from zero ad spend

---
📋 *Vera — New Deliverable (Run 70)*
>File: outputs/tommy/hot_lead_callback_script_2026-05-24.md
>What: Word-for-word script for when a PM/realtor/contractor who opened your email 2–3 times calls back organically. Opening (15 seconds), 3 discovery questions, how to quote a range on the phone, how to close, how to handle "send me something in writing," post-call actions within 30 minutes.
>Why: This is the highest-conversion moment in the pipeline (warm inbound = they already decided to explore). Bradley has had no script for this until now.

---
📋 *Vera — New Deliverable (Run 70)*
>File: outputs/donna/may26_week_priority_stack_2026-05-24.md
>What: Single-page cheat sheet for the week of May 26–30. Tuesday: 10-action 90-min launch window in order (Summit pull → bridge emails → contractor texts → gas station sequence → Facebook lead SOP → ads launch). Wed–Fri: daily priority tables with time estimates. Critical path deadline table (what slips = what fails). Week-end 6-question check.
>Read this Tuesday morning before anything else.

---
🚨 *Vera — CRITICAL: Reply Window Closes TOMORROW*
>Mixmax reply window (post-Touch 3) closes Monday May 25 (Memorial Day).
>Action: Run `python3 workers/check_replies.py` at 10am Monday.
>Protocol: outputs/donna/monday_memorial_day_final_check_2026-05-24.md
>0 replies → confirmed pivot to Round 2 June 4 with VOC-rewritten copy. Pause Instantly.ai immediately.
>Any reply → respond within 1 hour. Use outputs/tommy/hot_lead_callback_script_2026-05-24.md if they call back.

---
🚨 *Vera — CRITICAL: Instantly.ai Still Active (11 Days to Round 2)*
>Both campaigns still running: a1c08c3d (PM Cuyahoga) + 626cd15d (Contractor Referral)
>Round 2 enrollment = June 4. Deliverability recovery needs 7–10 days. Deadline to pause = May 26.
>3-minute fix: app.instantly.ai → Campaigns → ⋮ → Pause both.
>After pausing: add INSTANTLY_PAUSED=true to .env — stops the runtime warning in enroll_batch().
>If not paused before June 4, Round 2 will land in spam exactly like Round 1.

---
💡 *Vera — Upgrade Proposal (Run 70)*
>Idea: Have Tommy write the actual NE Ohio Home Maintenance Checklist content
>Why: Donna wrote the brief (lead_magnet_home_maintenance_checklist_2026-05-12.md) on May 12, but the 12-month exterior maintenance calendar content was never written. This is the highest-priority lead magnet for Kit.com email list building — every homeowner in NE Ohio is a target.
>Impact: Email list = retargeting audience for ads + recurring revenue pipeline. Content takes 2 hours to write. Landing page setup takes 30 minutes on Kit.com (free).
>Reply YES to approve and Tommy will write the full checklist.

---
💡 *Vera — Upgrade Proposal (Run 70)*
>Idea: Realtor pipeline revival — all 7 NE Ohio counties in June
>Why: Carla's last realtor pull was May 12 (6+ weeks ago). Summer listing season is live NOW. Realtors listing homes in June/July are the highest-ROI referral partners for the next 90 days. realtor_summer_voc_sequence_2026-05-24.md is ready to deploy.
>Impact: 10 active realtor partners = 40 referral jobs/summer = $18,000 at $450/avg job. Zero ad spend.
>Reply YES to approve and Carla will run a fresh realtor pull in all 7 counties on June 1.

---
✅ *Vera — Scan Complete 2026-05-24 (Run 70)*
>5 auto-upgrades shipped | 3 deliverables | 2 proposals | 18 open issues (0 new)
>Confirmed working this run: check_replies.py company map ✅ | vera_relay.py Carla staleness check ✅ | lead_pipeline.py county-labeled filenames ✅
>Bug found and fixed: rick.md "Monday after Memorial Day" survived 9 prior runs in the header — now corrected
>New scripts verified: All 18 open issues require Bradley action (external systems or physical actions)
>TODAY priority: Text Anthony/Land Pro (440-320-2779) + Text Venus/Reliable Roofing (216-810-2497) + Pause Instantly.ai = 15 minutes of real action
>MONDAY priority: check_replies.py at 10am per monday_memorial_day_final_check_2026-05-24.md
>TUESDAY priority: Read outputs/donna/may26_week_priority_stack_2026-05-24.md before touching anything
