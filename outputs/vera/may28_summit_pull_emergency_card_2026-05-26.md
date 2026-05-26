# Summit County Pull — Emergency Card
### 3 Days to Deadline | May 28 (Wednesday) | 25 Minutes
*Vera Cole | Auto-generated 2026-05-26*

---

## ⏰ DEADLINE: MAY 31 (SUNDAY) — 5 DAYS FROM TODAY

Every day you skip = fewer fresh Summit County leads for June 4 Round 2 enrollment.
**Wednesday May 28 is your best window** — ads running, contracts coming in, you're at your Mac.

---

## 🚀 DO THIS FIRST — Summit Pull (6 min, unattended)

**Option A (easiest):** Open Finder → navigate to `forestcity/scripts/` → double-click `run_summit_pull.command`
- Terminal opens, runs, closes automatically
- Check `logs/activity.log` when done — confirm line says "Danny | Apollo pull"

**Option B (terminal):**
```bash
cd /Users/bradleyneal/forestcity
python3 workers/lead_pipeline.py danny Summit
```

**What to expect:** 15–50 new PM leads from Summit County / Akron area. Enrolled in Mixmax automatically if API is live.

**While the pull runs (6 min):** Do Step 2 below — both happen simultaneously.

---

## 📱 STEP 2 — Contractor Texts (while pull runs)

These contacts are 14+ days overdue. Do 3 of them while Summit pull runs.

**Bryan — CLE Lawn Care Plus (216-402-1924)** ← DO FIRST (most overdue)
> "Hey Bryan, it's Bradley from Forest City Power Washing. Quick follow-up — still interested in doing a referral swap? I send my customers to you for lawn care, you send yours to me for pressure washing. Zero paperwork, $50 for every job you send my way. Worth a quick call?"

**Bulletproof Lawncare (216-307-4344)**
> "Hey, it's Bradley at Forest City Power Washing — following up on my message last week. We wash driveways, houses, and commercial properties for a lot of lawn care customers. $50/job referral if you want to send work my way. Interested?"

**Damrons Landscaping (440-494-0422)**
> "Hey, Bradley from Forest City Power Washing again. We do pressure washing + soft wash for landscapers' clients all over NE Ohio. If you ever have a customer who needs their house or driveway done, I'll send you $50 per job. Takes 30 seconds to refer. Worth it?"

**After each text:** Update pipeline_data.json → change stage from "Contacted" to "Contacted", update `last_contact` to today's date, set `next_followup` to June 2.

---

## 📱 STEP 3 — Tier 1 New Leads (pick 2)

These 5 contractors are 8+ days "New Lead" with zero personal outreach:

| Contact | Company | Phone | Best Text Opener |
|---------|---------|-------|-----------------|
| Anthony | Land Pro Management | 440-320-2779 | "landscapers' customers" angle |
| Dontez | GTP Landscaping | 440-396-0814 | "landscapers' customers" angle |
| Chris | Twin Improvements | 216-773-0757 | "home improvement" angle |
| Venus | Reliable Roofing | 216-810-2497 | "roofers refer a lot of wash jobs" |
| Logan | Pagels Quality Construction | 216-956-5263 | "construction handoff" angle |

**Text template (Anthony):**
> "Hey Anthony, it's Bradley from Forest City Power Washing. We do exterior cleaning for a lot of landscapers' customers — driveways, houses, gutters. Want to do a referral swap? No paperwork, $50 for every job you send our way. Happy to return the favor."

---

## ✅ SUCCESS LOOKS LIKE:

By end of Wednesday:
- [ ] `logs/activity.log` shows Summit County pull entry
- [ ] Bryan, Bulletproof, Damrons texted (3 texts)
- [ ] 2+ Tier 1 contractors texted (Anthony first)
- [ ] pipeline_data.json updated with today's date for all texted contacts

**Next window:** If Summit pull still not done by Friday May 30, Sunday May 31 is the absolute hard deadline.
After May 31 → Week 22 = Medina County (use `scripts/run_medina_pull.command` on June 1).

---

*Links: june4_readiness_snapshot_2026-05-26.md | launch_day_contractor_outreach_stack_2026-05-26.md | run_summit_pull.command*
