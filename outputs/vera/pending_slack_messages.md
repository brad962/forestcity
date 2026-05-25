🔧 *Vera — Auto-Upgrade (Run 86)*
>Changed: agents/danny.md — removed "5 days left as of May 26" from Summit urgency note
>Why: Today is May 25; "as of May 26" was wrong and ages out in 24 hours; urgency note now shows deadline only (May 31) without a stale day count
>File: agents/danny.md

---

🔧 *Vera — Auto-Upgrade (Run 86)*
>Changed: integrations/mixmax.py — added 'community association director' to PROPERTY_MANAGER_TITLES
>Why: CAI board-level HOA director title was missing from routing; distinct from 'community director' and 'community association manager'; these decision-makers sign vendor contracts
>File: integrations/mixmax.py

---

🔧 *Vera — Auto-Upgrade (Run 86)*
>Changed: workers/lead_pipeline.py — added 'community association director' to DANNY_TITLES
>Why: Keeps Apollo search titles and Mixmax routing in sync; contacts with this title now pull AND route correctly
>File: workers/lead_pipeline.py

---

🚨 *Vera — NEW ISSUE: Contacted Contractors Stale (Run 86)*
>Bryan/CLE Lawn Care Plus was contacted May 13 — 12 days ago, 0 follow-up. At 12 days, a warm lead goes cold.
>Bulletproof Lawncare + Damrons Landscaping contacted May 19 — 6 days, also no 2nd touch.
>
>Scripts ready: `outputs/vera/contacted_contractor_followup_card_2026-05-25.md`
>
>Bryan 216-402-1924 — text TODAY:
>"Hey Bryan, it's Bradley from Forest City Power Washing — I reached out a couple weeks back about a referral swap. We're launching ads this week so we'll be picking up more jobs in your area. Still interested in the $50/referral deal? No forms, no hassle."
>
>Bulletproof 216-307-4344 + Damrons 440-494-0422 — same urgency, scripts in the card.
>3 texts, 3 minutes, potential recurring referral revenue.

---

📄 *Vera — Deliverable (Run 86)*
>File: `outputs/vera/may27_day2_post_launch_sprint_2026-05-25.md`
>What: Wednesday May 27 morning action card — fills the 24h gap between Day 1 debrief (Tue 5pm) and Day 3 check (Thu)
>Content: Lead log check → Ads Manager glance (spend only — DO NOT EDIT on Day 2) → GBP Post 2 → gas station Wave 2 emails → contractor texts follow-up → first-lead response protocol → neighbor canvass if jobs scheduled
>Key warning inside: Editing ad campaigns before Day 7 resets the learning phase. Zero edits on Day 2.
>Action: Open Wednesday morning May 27. 15 minutes.

---

📄 *Vera — Deliverable (Run 86)*
>File: `outputs/vera/contacted_contractor_followup_card_2026-05-25.md`
>What: 2nd-touch scripts for 3 stale "Contacted" contacts — discovered via pipeline_data.json audit
>Contacts: Bryan/CLE Lawn Care Plus (12 days, 216-402-1924), Bulletproof Lawncare (6 days, 216-307-4344), Damrons Landscaping (6 days, 440-494-0422)
>Content: Copy-paste text for each, if-they-reply handling, pipeline_data.json update instructions
>Action: Open card, copy Bryan script first, send. 3 texts in 3 minutes.

---

✅ *Vera — Scan Complete 2026-05-25 (Run 86 | Memorial Day — launch eve)*
>3 auto-upgrades shipped | 2 deliverables | 1 new issue | 0 issues resolved | 21 open total
>Key fix: danny.md stale date count removed. mixmax.py + lead_pipeline.py — community association director title added to routing and search.
>Key deliverables: Contacted contractor 2nd-touch card (Bryan 12 days urgent) + May 27 Day 2 post-launch sprint card (fills Day 1→Day 3 gap).
>HIGHEST PRIORITY TODAY: (1) Text Bryan 216-402-1924 — 12 days is too long. Script in contacted_contractor_followup_card. (2) Text Anthony 440-320-2779 — referral pitch. (3) Pause Instantly.ai — app.instantly.ai → a1c08c3d + 626cd15d → Pause → add INSTANTLY_PAUSED=true to .env.
>TOMORROW (LAUNCH DAY): READ `may26_final_launch_brief_2026-05-25.md` first. Run Google Ads pre-launch checklist before enabling. Post Day 2 card is ready for Wednesday.
---
🔧 *Vera — Auto-Upgrade (Run 87)*
>Changed: pipeline_data.json — added `next_followup=2026-05-25` for 5 Tier 1 contractors (Land Pro Management, GTP Landscaping, Twin Improvements, Reliable Roofing, Pagels Quality Construction)
>Why: All 5 were in "New Lead" stage with empty next_followup; now flags as overdue in Nina's weekly report so they don't get lost in launch day chaos
>File: pipeline_data.json
---
🔧 *Vera — Auto-Upgrade (Run 87)*
>Changed: `integrations/mixmax.py` + `workers/lead_pipeline.py` — added self-storage manager titles to PROPERTY_MANAGER_TITLES and DANNY_TITLES; added 'self storage', 'self-storage', 'storage facility', 'storage units' to DANNY_ORG_KEYWORDS
>Why: New commercial segment — district managers at Extra Space, Life Storage, CubeSmart etc. oversee 3–5 NE Ohio facilities each; blue ocean (no local competitors targeting this); auto-captured in next Apollo run
>File: integrations/mixmax.py + workers/lead_pipeline.py
---
🔧 *Vera — Auto-Upgrade (Run 87)*
>Changed: `agents/danny.md` — documented Self-Storage as a new secondary segment with targeting context, Apollo search tip, revenue math ($72K–$128K/year from 10 accounts), and link to full brief
>File: agents/danny.md
---
🔧 *Vera — Auto-Upgrade (Run 87)*
>Changed: `agents/tommy.md` — added CURRENT version tag to neighbor_canvass_script entry: `neighbor_canvass_script_2026-05-26.md` supersedes May 23 version
>Why: Two versions existed; catalog now shows which is current — matches established pattern for other versioned deliverables
>File: agents/tommy.md
---
📄 *Vera — New Deliverable (Run 87)*
>File: `outputs/donna/self_storage_commercial_segment_brief_2026-05-25.md`
>What: Full commercial segment brief for self-storage facilities — Extra Space, Life Storage, CubeSmart, StorageMart, Public Storage in NE Ohio; district managers oversee 3–5 facilities; soft-wash-only (metal buildings); revenue math $72K–$128K/year at scale; Apollo search parameters, pitch angle, PM sequence routing. Apollo keywords already live in code.
>Action: No new steps needed — self-storage auto-included in next Apollo run (Week 22 Medina, June 1). Review leads after pull for storage company names.
---
📄 *Vera — New Deliverable (Run 87)*
>File: `outputs/vera/launch_day_contractor_followups_2026-05-25.md`
>What: Tomorrow morning (May 26 launch day) — Bryan, Bulletproof, Damrons all have follow-ups due. This 1-page card says DO THESE FIRST before touching Ads Manager. 3 copy-paste texts, updated angle, reply scripts, 5 minutes.
>Action: READ THIS FIRST TOMORROW MORNING before opening any ad platform.
---
📄 *Vera — New Deliverable (Run 87)*
>File: `outputs/carla/june4_carla_activation_card_2026-05-25.md`
>What: Carla's June 4 press-GO card — 3 tracks: (1) enroll Medina leads via `python3 workers/lead_pipeline.py pending`, (2) pool service text blitz, (3) contractor revival texts for 6 priority contacts; 45 min total; coordinates with Danny's june4_enrollment_battle_card.
>Why: Danny had a June 4 battle card. Carla didn't. Now she does.
---
💡 *Vera — Upgrade Proposal (Run 87)*
>Idea: Write a self-storage-specific Mixmax sequence (distinct from generic PM sequence)
>Why: Self-storage has unique pitch angles (soft-wash for metal, large concrete pads, multi-facility deal) — a dedicated sequence with tailored subject lines + body copy will outperform the generic PM sequence for this segment
>Impact: Higher reply rate from storage DMs; ability to pitch multi-facility structure in Touch 1
>Reply YES to approve — Danny will write the 3-touch sequence copy (1 session, <30 min).
---
💡 *Vera — Upgrade Proposal (Run 87)*
>Idea: Workiz "job complete" → auto-review request text via Zapier + Twilio
>Why: Every completed job is a review opportunity. `review_request_sequence_2026-05-18.md` exists but requires manual send. Automating via Workiz webhook → Zapier → Twilio SMS = reviews on autopilot during peak season
>Impact: 5–10 Google reviews/month during peak season vs. 0 currently; ranking signal; trust signal for ad leads
>Needs: TWILIO credentials (add to .env). Donna will write the Zapier recipe + Twilio setup guide.
>Reply YES to approve.
---
✅ *Vera — Scan Complete 2026-05-25 (Run 87)*
>6 auto-upgrades shipped | 3 new deliverables | 2 proposals | 21 open issues (0 new, 0 closed)
>Self-storage commercial segment unlocked — keywords live in Apollo search, full brief in outputs/donna/
>Launch day contractor follow-up card written — read it FIRST tomorrow morning (5 min, 3 texts)
>Carla's June 4 activation card created — parallel to Danny's battle card, 3 tracks, 45 min
>TOMORROW (May 26 LAUNCH DAY): contractor texts first → may26_final_launch_brief → ads → gas station emails → GBP Post 1
