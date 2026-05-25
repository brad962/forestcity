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
