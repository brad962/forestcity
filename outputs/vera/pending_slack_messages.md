🔧 *Vera — Auto-Upgrade (Run 83)*
>Changed: agents/danny.md — removed hardcoded "TODAY IS MEMORIAL DAY MAY 25. TOMORROW (MAY 26) = LAUNCH DAY. 6 days left" from urgency note
>Why: Language was wrong the moment May 26 arrived — replaced with date-agnostic "SUMMIT COUNTY — DEADLINE: MAY 31" that remains accurate all week
>File: agents/danny.md
---
🔧 *Vera — Auto-Upgrade (Run 83)*
>Changed: workers/check_replies.py — updated docstring; removed "72-hour post-Touch 3 reply window" reference (window closed May 25)
>Why: Script is now the permanent daily pipeline health tool, not a temporary window monitor; docstring reflected old context
>File: workers/check_replies.py
---
🔧 *Vera — Auto-Upgrade (Run 83)*
>Changed: agents/donna.md — added launch_day_evening_debrief_[date].md to output format catalog
>Why: New deliverable written this run fills the gap between the morning launch brief and Day 3 ad monitoring
>File: agents/donna.md
---
📄 *Vera — Deliverable (Run 83)*
>File: outputs/donna/launch_day_evening_debrief_2026-05-26.md
>What: 5-minute end-of-Day-1 check for 5pm Tuesday May 26
>Content: 7 steps — did ads go live?, Summit pull done?, any leads?, GBP Post 1 published?, gas station emails sent?, contractor texts done?, Instantly.ai paused?; "what success looks like on Day 1" table; clear Day 1 vs. Day 3 distinction (Google Ads shows 0 data on Day 1 — that's normal)
>Action: At 5pm Tuesday, open this file and run through it. Takes 5 minutes.
---
📄 *Vera — Deliverable (Run 83)*
>File: outputs/vera/launch_week_daily_checklist_2026-05-26.md
>What: May 26–31 daily 10-minute micro-checklist
>Content: Each day (Tue–Sun) has 5–7 specific tasks with linked files; covers GBP posts (1/day), check_replies.py, ad monitoring, contractor follow-ups, gas station Wave 2 Thursday, Summit deadline Sunday, neighbor canvass on every job; "week success" table with targets (3–10 FB leads, 2–5 jobs booked, 5 GBP posts published, Summit pull done)
>Action: Open every morning. 10 minutes keeps the entire launch week on track.
---
💡 *Vera — Upgrade Proposal (Run 83)*
>Idea: Workiz + Facebook Lead Gen intake automation
>Why: facebook_lead_response_sop says to manually log leads in Workiz after calling. If Bradley is on a job at 9am and a lead comes in at 9:05am, the 5-min callback window passes AND no Workiz entry gets made. Proposal: set up Workiz's built-in online booking form or a simple Zapier zap (Facebook Lead Gen → Workiz new job). Zero manual entry = no lead falls through on a busy job day.
>Impact: Every ad lead is captured in Workiz the moment it comes in, even if Bradley is mid-job. Zero revenue visibility gaps.
>Reply YES to approve and I'll write the Zapier setup guide + Workiz booking form config.
---
💡 *Vera — Upgrade Proposal (Run 83)*
>Idea: Post-launch review request for first ad-generated jobs
>Why: First customers from Facebook ads are new — they don't know Bradley. A post-job review request is especially important for this segment (builds Google/Yelp social proof that lowers CPL over time). Tommy's review_request_sequence_2026-05-18.md has templates. Proposal: use the booking_confirmation_text_2026-05-25.md completion checklist to trigger the review request text immediately when a job is marked Done in Workiz.
>Impact: Every ad-generated job = 1 new Google review; 10 jobs = 10 reviews; raises GBP star rating → better local search ranking → organic leads on top of paid leads.
>Reply YES to approve and I'll write the ad-generated job review request protocol.
---
✅ *Vera — Scan Complete 2026-05-25 (Run 83 | Launch Eve — 12 hours out)*
>4 auto-upgrades shipped | 2 proposals | 0 open issues resolved
>Key auto-fixes: danny.md stale date language removed; check_replies.py docstring updated for ongoing use; donna.md catalog updated; 0% reply rate issue reframed as Round 2 June 4
>Key deliverables: launch_day_evening_debrief_2026-05-26.md (5pm Tuesday check) + launch_week_daily_checklist_2026-05-26.md (10 min/day May 26-31)
>STATUS: System is launch-ready. All 83 runs of prep are staged. Tomorrow is the day.
>TONIGHT priority: Pause Instantly.ai now → 9 days recovery starts tonight. 3 minutes: app.instantly.ai → a1c08c3d + 626cd15d → ⋮ → Pause → add INSTANTLY_PAUSED=true to .env
>TOMORROW MORNING: READ outputs/donna/may26_final_launch_brief_2026-05-25.md FIRST. Then launch_week_daily_checklist at 5pm. This is it.
---
🔧 *Vera — Auto-Upgrade (Run 84)*
>Changed: `integrations/mixmax.py` — added GetGo/Giant Eagle Fuel, BP, Shell, Pilot Flying J, Exxon, Mobil, Valero, Citgo, Kwik Trip to GAS_STATION_KEYWORDS
>Why: Major NE Ohio gas station chains were missing; GetGo is one of NE Ohio's largest c-store chains and wasn't in the routing list
>File: integrations/mixmax.py
---
🔧 *Vera — Auto-Upgrade (Run 84)*
>Changed: `workers/lead_pipeline.py` + `integrations/mixmax.py` — added 'property operations manager' to DANNY_TITLES and PROPERTY_MANAGER_TITLES
>Why: National PM firms like Greystar and Lincoln Property use this title; contacts there were falling through to the default instead of the PM sequence
>File: workers/lead_pipeline.py + integrations/mixmax.py
---
🔧 *Vera — Auto-Upgrade (Run 84)*
>Changed: `agents/tommy.md` — updated website_copy_service_pages_voc_refresh catalog entry to note current file is DONE (2026-05-25); marks open issue as resolved
>File: agents/tommy.md
---
🔧 *Vera — Auto-Upgrade (Run 84)*
>Changed: `agents/donna.md` — added launch_eve_prep_checklist format entry to output catalog
>File: agents/donna.md
---
📄 *Vera — Deliverable (Run 84): website_copy_service_pages_voc_refresh_2026-05-25.md*
>File: `outputs/tommy/website_copy_service_pages_voc_refresh_2026-05-25.md`
>What: Drop-in replacement for all 5 Google Ads landing pages using Marcus's exact NE Ohio VOC phrases
>Key H1s: "Your Siding Is Green and Slimy. We Fix That." / "Your Roof Looks Black from the Street. That's Not Age — It's Alive." / "Every NE Ohio Driveway Has Road Salt Stains. Here's How to Get Rid of Them."
>Trust blocks use real customer language: "I've been meaning to do it for three years. Wish I'd done it sooner." / "Saved us from replacing the deck."
>Action: 15-min swap in web builder — do it Day 3–7 after ads go live. Roof Soft Wash page first.
>RESOLVES open issue from Run 81.
---
📄 *Vera — Deliverable (Run 84): launch_eve_prep_checklist_2026-05-25.md*
>File: `outputs/donna/launch_eve_prep_checklist_2026-05-25.md`
>What: 10-minute "before bed" checklist for tonight — so tomorrow morning has zero friction
>7 items: verify FB Ads billing active, verify Google Ads access, draft gas station emails, check contractor texts sent, Instantly.ai pause, swap FB hooks to draft, set alarms (7:30am + 5pm)
>Also: full staged asset table (all tomorrow's tasks with time estimates) + what can wait this week
>Read it NOW — it's for tonight.
---
✅ *Vera — Scan Complete 2026-05-25 (Run 84 | Final prep before Launch Day)*
>4 auto-upgrades | 2 deliverables | 1 RESOLVED (Website Service Pages VOC — open 4 runs) | 20 open issues
>Gas station routing expanded (GetGo/BP/Shell/Pilot now covered). PM title net extended (property operations manager). Service pages VOC-refreshed (all 5 done). Launch eve checklist ready.
>TONIGHT: Open `outputs/donna/launch_eve_prep_checklist_2026-05-25.md` — 10 min before bed
>7:30am TOMORROW: `outputs/donna/may26_final_launch_brief_2026-05-25.md` — 90-min launch
