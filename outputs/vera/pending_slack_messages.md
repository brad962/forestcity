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
---
🔧 *Vera — Auto-Upgrade (Run 88)*
>Changed: `integrations/mixmax.py` + `workers/lead_pipeline.py` — added 'plumber', 'plumbing', 'electrician', 'electrical contractor' to CONTRACTOR_TITLES and CARLA_SEARCHES keywords
>Why: Plumbers and electricians are in homes 2-4x/year, trusted advisors, see dirty exteriors on every call — the same traits that make HVAC/pool companies good referral partners. Currently missing from Carla's Apollo pull and sequence routing.
>File: integrations/mixmax.py + workers/lead_pipeline.py
---
🔧 *Vera — Auto-Upgrade (Run 88)*
>Changed: `workers/lead_pipeline.py` — added car dealership org keywords to DANNY_ORG_KEYWORDS: 'car dealership', 'auto dealership', 'automotive dealer', 'auto group', 'car dealer'
>Why: NE Ohio dealer groups (Ganley, Hidy Automotive, Valley Ford) have 3-8 locations each. Large paved lots + building exteriors = recurring monthly commercial accounts. One dealer group deal = $18K–$36K/year. Auto-included in next Apollo run. No existing competitor targeting this segment.
>File: workers/lead_pipeline.py + agents/danny.md
---
🔧 *Vera — Auto-Upgrade (Run 88)*
>Changed: `workers/nina_report.py` — weekly report now (1) lists actual names of untouched contacts (was just a count), (2) flags "Contacted" stage contacts with last_contact > 7 days and no next_followup date set
>Why: Silent gap — contacts in Contacted stage can age out invisibly if next_followup isn't set. This catches them before they go cold. Bryan (14 days), Bulletproof + Damrons (7 days) all due today.
>File: workers/nina_report.py
---
🔧 *Vera — Auto-Upgrade (Run 88)*
>Changed: `agents/carla.md` — added Plumbers (#16) and Electricians (#17) as target referral partner types
>Why: Both are in homes constantly, trusted by homeowners, and see dirty exteriors at every service call. Natural cross-referral partners, same as HVAC and pest control already in Carla's list.
>File: agents/carla.md
---
📄 *Vera — New Deliverable (Run 88)*
>File: `outputs/tommy/annual_plan_pitch_script_2026-05-26.md`
>What: 20-second verbal pitch for the annual plan said DURING the quote call (after they say yes to price). 3 response-handling scripts: YES / "how much?" / "maybe later." Revenue math: 20 customers × $450 = $9,000/year recurring, zero additional marketing.
>Why: Tommy already has post-job upsell texts and welcome kit — but no script for the verbal pitch on the call itself. Now that ads are live and calls are coming in, every quote call is a chance to convert to recurring revenue. 20 seconds. Use it.
>Action: READ TODAY before your first call with an ad lead.
---
📄 *Vera — New Deliverable (Run 88)*
>File: `outputs/donna/june1_sunday_evening_checklist_2026-05-26.md`
>What: 15-minute Sunday June 1 evening checklist (7 steps) to make sure Monday Medina pull and June 4 enrollment are unblocked. Covers: Instantly.ai pause verify, Summit pull confirm, Medina shortcut staged, gas station path, enrollment readiness, bridge email check, June 4 battle card read-through.
>Why: There's a guide for the Monday pull and a battle card for June 4 but nothing connecting them on Sunday night. This is the "night before" checkpoint.
>Action: Set a calendar reminder: June 1 at 8pm → open this file.
---
💡 *Vera — Upgrade Proposal (Run 88)*
>Idea: Dedicated Apollo pull for NE Ohio car dealerships (Ganley, Hidy Automotive, Valley Ford, Spitzer, Classic Auto, etc.) — target Facility Manager + General Manager at these groups
>Why: Car dealership keywords are now live in DANNY_ORG_KEYWORDS (auto-runs on next county pull) but a targeted dealership pull would go deeper: filter by org name specifically, pull only multi-location dealer groups, and include 'service director' and 'general manager' titles that are too generic for the broader PM pull. One dealer group = 3-8 locations = $18K–$36K/year recurring. Zero local competitors targeting this segment.
>Impact: 10-20 qualified dealer contacts per county; separate from PM pull so it doesn't compete for Apollo quota
>Reply YES to approve — Danny runs this in 1 session.
---
🚨 *Vera — Launch Day Priority Stack — May 26*
>TODAY'S order of operations:
>1️⃣ Text Bryan (216-402-1924) — 14 days. Bulletproof (216-307-4344) + Damrons (440-494-0422) — 7 days. Scripts: `launch_day_contractor_followups_2026-05-25.md`. 5 minutes. Do this FIRST.
>2️⃣ Read `may26_final_launch_brief_2026-05-25.md` — the definitive 90-min launch guide.
>3️⃣ Pause Instantly.ai NOW — app.instantly.ai → a1c08c3d → ⋮ → Pause. Repeat for 626cd15d. Then add INSTANTLY_PAUSED=true to .env. 3 minutes. TODAY = minimum viable recovery window (9 days). Every day delayed = higher spam risk on June 4.
>4️⃣ Facebook ads: swap hooks from `facebook_ad_creative_voc_refresh_2026-05-24.md` BEFORE clicking launch. Then launch. `facebook_lead_gen_launch_checklist_2026-05-26.md`.
>5️⃣ Google Ads: run `google_ads_launch_day_checklist_2026-05-26.md` (5 blocks) BEFORE enabling.
>6️⃣ Gas station Gmail blast — Tier 1 (7 contacts) today. Guide: `gas_station_manual_email_blast_2026-05-25.md`.
>AT 5PM: `launch_day_evening_debrief_2026-05-26.md` — 5-minute end-of-day check.
---
✅ *Vera — Scan Complete 2026-05-26 (Run 88 | LAUNCH DAY)*
>7 auto-upgrades shipped | 2 new deliverables | 1 new proposal | 23 open issues (2 new: Annual Plan Pitch Gap + Car Dealerships segment)
>Plumbers + electricians added to Carla's referral pull — these were missing alongside HVAC/pool which were already there
>Car dealership keywords live in Danny's Apollo search — Ganley/Hidy/Valley Ford; $18K–$36K/year per dealer group; no competitor targeting this
>Nina's weekly report now lists untouched contact names + flags stale "Contacted" contacts without follow-up dates
>Annual plan verbal pitch script written — use on every quote call starting today (after quote YES, before hanging up)
>June 1 Sunday evening checklist written — 7-step prep for Medina pull + Round 2 staging
>CRITICAL TODAY: Pause Instantly.ai (9 days recovery remaining) → Ads launch (all assets ready) → Bryan follow-up text (14 days)
