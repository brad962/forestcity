🔧 *Vera — Auto-Upgrade*
>Changed: `lead_pipeline.py` run_danny() and run_carla() — `p['id']` direct key access replaced with `p.get('id', '')` + skip-if-empty guard. Also added explicit `_lead_type: 'property_manager'` to Danny's lead dict so it persists in cache even if Mixmax enrollment is blocked mid-run.
>Why: If Apollo returns a malformed person object without an `id` key, the entire pipeline run crashes with KeyError — all remaining leads skipped, no log, no output. Now malformed objects are safely skipped.
>File: workers/lead_pipeline.py

---

📋 *Vera — New Deliverable: June Week 1 Sprint*
>File: outputs/donna/june_week1_sprint_2026-05-20.md
>What it is: Day-by-day action calendar for June 2–6 — the "return to full velocity" week after Memorial Day.
>Monday June 2: Summit County Apollo pull (missed in May rotation) + create Mixmax sequences for gas station and fleet (2 PENDING sequences, 30 min in Mixmax UI, unlocks 18 idle contacts).
>Tue–Wed: Review Touch 3 results, re-enroll 45 Round 1 contacts in Round 2.
>Thu–Fri: LinkedIn connects to new hot leads + contractor text follow-up.
>Revenue math: 95–115 contacts active by end of week = 4–8 quote opportunities in June.

---

📋 *Vera — New Deliverable: Round 2 Decision Framework*
>File: outputs/vera/round2_decision_framework_2026-05-20.md
>What: Go/no-go criteria for whether to use the rewritten sequence copy in Round 2.
>The key insight: Don't change copy AND Reply-To simultaneously — you won't know what drove any improvement. Fix one variable at a time.
>Decision tree (read Thursday morning May 22): Scenario A = replies received → keep copy. Scenario B = 0 replies + Reply-To confirmed correct → use rewrite. Scenario C = 0 replies + Reply-To was wrong → fix Reply-To first, keep copy.
>Action: Open this file Thursday morning, check 2 things in Mixmax, make the call. 5 minutes.

---

🚨 *Vera — TONIGHT (May 20) — Last Window Before Touch 3*
>Touch 3 fires IN ~12 HOURS. 55-minute checklist: `outputs/vera/touch3_eve_final_checklist_2026-05-20.md`
>① Check Mixmax Reply-To (10 min) → `outputs/vera/mixmax_reply_to_check_2026-05-20.md`
>② LinkedIn connects to 13 hot leads (30 min) → `outputs/tommy/hot_lead_linkedin_dm_playbook_2026-05-19.md`
>③ Text Tier 1 contractors (15 min): Anthony/Land Pro 440-320-2779, Dontez/GTP 440-396-0814, Twin Improvements 216-773-0757, Reliable Roofing 216-810-2497, Pagels Construction 216-956-5263
>Templates: `outputs/vera/sms_templates_contractors_2026-05-18.md`

---

📅 *Vera — Thursday May 22 — Touch 3 Morning*
>READ THIS FIRST: `outputs/vera/touch3_morning_brief_2026-05-22.md`
>Then open: `outputs/vera/round2_decision_framework_2026-05-20.md` → follow the decision tree → decide Round 2 sequence copy in 5 min.
>If replies come in → `outputs/tommy/touch3_reply_response_templates_2026-05-20.md`
>If 0 replies, start phone calls → `outputs/tommy/hot_lead_phone_script_2026-05-22.md`

---

✅ *Vera — Scan Complete 2026-05-20 (Run 28)*
>2 auto-upgrades shipped | 2 deliverables | 15 open issues
>Auto-upgrades: lead_pipeline.py p['id'] KeyError crash fix + _lead_type cache persistence
>Deliverables: June Week 1 Sprint (outputs/donna/), Round 2 Decision Framework (outputs/vera/)
>🚨 Touch 3 fires in ~12 hours. Tonight: eve checklist outputs/vera/touch3_eve_final_checklist_2026-05-20.md
>June 2: Pipeline restart, Mixmax sequences, Summit County pull → outputs/donna/june_week1_sprint_2026-05-20.md
