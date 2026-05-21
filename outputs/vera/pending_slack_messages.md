🔧 *Vera — Auto-Upgrade*
>Changed: workers/nina_report.py — added "Overdue Follow-ups" + "Due This Week" sections to weekly pipeline report
>Why: The weekly report showed aggregate Contacted count but never surfaced which specific contacts are due for follow-up this week. Starting May 26 run, Nina will flag Bulletproof Lawncare, Damrons Landscaping, and CLE Lawn Care Plus by name with phone numbers.
>File: workers/nina_report.py

---

🔧 *Vera — Auto-Upgrade*
>Changed: workers/lead_pipeline.py — added 10 org-level keywords to Carla's realtor Apollo search
>Why: Realtor entry had `keywords: []` — empty. Any company with a "realtor" title in any industry would match. Now filters to actual NE Ohio brokerages (Keller Williams, Howard Hanna, RE/MAX, Coldwell Banker, Compass, eXp).
>File: workers/lead_pipeline.py

---

🔧 *Vera — Auto-Upgrade*
>Changed: agents/donna.md — Memorial Day Sprint section updated with Touch 3 zero-reply link; June Blitz section links to Round 2 enrollment plan
>Why: New deliverables written this run need to be discoverable from the agent file.
>File: agents/donna.md

---

📄 *Vera — New Deliverable: Round 2 Enrollment Plan*
>File: outputs/donna/round2_enrollment_plan_2026-05-21.md
>What: Specific June 4 enrollment plan — Summit + Medina county, 25–30 new PMs, 10:30am send time change, gas station parallel track. Decision gate table (when to rewrite vs. keep sequence). Enrollment checklist June 2–4.
>Next step: Read after Touch 3 results come in (May 22 evening).

---

📄 *Vera — New Deliverable: May 26 Contractor Follow-Up Texts*
>File: outputs/tommy/contractor_followup_texts_may26_2026-05-21.md
>What: Copy-paste follow-up texts for 3 contractors who were texted May 19 and haven't replied: Bulletproof Lawncare (216-307-4344), Damrons Landscaping (440-494-0422), CLE Lawn Care Plus (216-402-1924). Different angle from initial pitch — less about us, more about them. Timing guide and pipeline update instructions included.
>Send: Monday May 26 (spread 30 min apart, after noon).

---

📄 *Vera — New Deliverable: Touch 3 Zero-Reply Protocol*
>File: outputs/vera/touch3_zero_reply_protocol_2026-05-21.md
>What: Step-by-step playbook IF Touch 3 produces 0 replies by May 23 evening. Not panic — action. Step 1: Run Nina locally. Step 2: Call top 5 multi-open contacts. Step 3: Bridge emails. Step 4: LinkedIn connects. Step 5: Round 2 pivot decision by May 25.
>The headline: 42% open rate means the message works. 0 replies means the channel is the issue. Phone call converts what email doesn't.

---

🚨 *Vera — TONIGHT FINAL WINDOW (May 21)*
>Touch 3 fires TOMORROW. Last chance for these 4 things tonight:
>
>1. Verify Reply-To in Mixmax (10 min) — outputs/vera/mixmax_reply_to_check_2026-05-20.md
>2. Enable open notifications on phone (5 min) — outputs/vera/mixmax_open_notifications_setup_2026-05-21.md
>3. Text 5 contractors (15 min) — outputs/tommy/contractor_referral_text_script_2026-05-20.md
>   · Anthony/Land Pro: 440-320-2779
>   · Dontez/GTP: 440-396-0814
>   · Twin Improvements: 216-773-0757
>   · Reliable Roofing: 216-810-2497
>   · Pagels Construction: 216-956-5263
>4. Run Summit County pipeline (5 min — LAST CHANCE before week rolls to Medina):
>   cd ~/forestcity && python3 workers/lead_pipeline.py danny

---

📋 *Vera — MAY 26 MONDAY ACTION ORDER*
>When you come back from Memorial Day, in this exact order:
>
>1. (7am) Read Touch 3 results: outputs/nina/hot_leads_2026-05-22.md (run Nina locally first)
>2. (7:15am) If 0 replies: outputs/vera/touch3_zero_reply_protocol_2026-05-21.md
>3. (8am) Text 3 contractor follow-ups: outputs/tommy/contractor_followup_texts_may26_2026-05-21.md
>   · Bulletproof Lawncare: 216-307-4344
>   · Damrons Landscaping: 440-494-0422
>   · CLE Lawn Care Plus: 216-402-1924
>4. (8:30am) Run pipeline: python3 workers/lead_pipeline.py both
>5. (9am) Create gas station Mixmax sequence: outputs/vera/mixmax_sequence_setup_guide_2026-05-20.md
>6. (10am) Full sprint plan: outputs/donna/may26_cron_restart_brief.md

---

💡 *Vera — Upgrade Proposal: Disable Instantly.ai Integration (eliminate duplicate email risk)*
>Idea: Comment out INSTANTLY_CAMPAIGNS in server.py and remove the /api/instantly/ proxy handler.
>Why: server.py has active Instantly campaign IDs targeting the SAME segments as live Mixmax sequences. If INSTANTLY_API_KEY is ever added to .env, contacts get duplicate cold emails from two platforms simultaneously — compliance and reputation risk. Mixmax is the live platform. Instantly is dead code with a live risk attached.
>Impact: Zero functionality lost. Clean code. No dual-outreach risk ever.
>Reply YES to approve.

---

💡 *Vera — Upgrade Proposal: 10:30 AM Send Time for Round 2 (re-escalation)*
>Idea: Change Mixmax sequence send time from 8:00 AM to 10:30 AM before June 4 Round 2 enrollment.
>Why: 42% open rate proves the message works. 0 replies suggests timing — PMs are in morning stand-up/building walks 8–10am. They respond to email 10am–noon. One UI setting change, no sequence rewrite.
>Impact: +15–25% expected reply rate lift on 25–30 Round 2 contacts. Full plan: outputs/donna/round2_enrollment_plan_2026-05-21.md
>Reply YES to approve — 2 minutes in Mixmax UI.

---

✅ *Vera — Scan Complete 2026-05-21 (Run 42)*
>2 code fixes | 3 deliverables | 2 proposals | 15 open issues
>Code: Nina weekly report now names specific follow-up contacts due (with phones). Carla realtor search now filters to actual NE Ohio brokerages.
>Deliverables: Round 2 enrollment plan (June 4), May 26 contractor follow-up texts, Touch 3 zero-reply protocol.
>Touch 3 fires TOMORROW. All 10 playbook resources locked. Zero-reply contingency now complete.
