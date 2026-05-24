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
