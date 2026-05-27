# June 5–11 Post-Enrollment Follow-Through Plan
### Forest City Power Washing — Run 112 | 2026-05-27
*Vera Cole | Chief Innovation Officer*

---

## What Just Happened (June 4)
Round 2 enrollment fired. Fresh Medina County contacts (60–160 expected) are now receiving Touch 1 of the Property Manager + Contractor Referral sequences. The outreach machine is running. Now your job is **response triage, not action creation.**

---

## Day-by-Day Guide: June 5–11

### June 5 (Thu) — Day 1 Post-Enrollment
- [ ] Run Nina's daily report: `python3 workers/nina_report.py daily` (local)
- [ ] Check for any immediate "unsubscribe" or bounces — address within 24h if any
- [ ] Verify Instantly.ai is still paused (check .env: `INSTANTLY_PAUSED=true`)
- [ ] No opens or replies yet = normal. Sequences are warming.

### June 6 (Fri) — Day 2
- [ ] Run Nina's daily report
- [ ] First opens may start appearing (some contacts open immediately, most open Day 3–5)
- [ ] Any hot leads (2+ opens) → connect on LinkedIn TODAY, message: "Saw you opened our note — wanted to connect directly"
- [ ] Check ads Day 12 performance (launch May 26 = Day 12 on June 6)

### June 7 (Sat) — Day 3 | **FIRST REPLY WINDOW**
- Touch 2 fires for contacts enrolled June 4 — second email in their inbox
- [ ] Run Nina's report first thing Saturday morning
- [ ] First replies may arrive today or Sunday — respond SAME DAY
- [ ] If a PM replies → book estimate call immediately (phone > email)
- [ ] If a contractor replies → schedule a coffee or site walk-through

### June 8 (Sun) — Day 4
- [ ] Any unanswered replies from Saturday → respond TODAY before Monday
- [ ] Check pipeline_data.json — are ad leads still being logged with lead_source?
- [ ] Post-enrollment status: "enrollment is running, first replies expected" → update pipeline

### June 9 (Mon) — Day 5 | **PEAK OPEN WINDOW**
- [ ] Run Nina's daily report + weekly report (Monday = weekly run)
- [ ] Days 3–7 are historically peak open window for cold email sequences
- [ ] LinkedIn connection requests from Days 5–7 contacts who opened but didn't reply
- [ ] Script for LinkedIn after opened but no reply:
  > "Hey [Name], I sent you a note about exterior cleaning for your properties — saw you had a chance to look at it. I'm in [their area] frequently. Would it be easier to do a quick call this week?"
- [ ] If Workiz shows jobs booked from ad leads → calculate CPA (cost per acquisition)

### June 10 (Tue) — Day 6
- [ ] Nina's daily report
- [ ] Chase any estimate requests that came in over the weekend
- [ ] Update pipeline_data.json stages for any new ad leads that came in

### June 11 (Wed) — Day 7 | **TOUCH 3 WINDOW**
- Touch 3 fires for enrolled contacts — final email in the 3-touch sequence
- [ ] This is the highest-urgency day of the sequence — last chance for a reply before they go cold
- [ ] Run Nina's report — surface all hot leads before Touch 3 lands in their inbox
- [ ] Any contact who opened twice and got three emails → personal LinkedIn connect + DM today
- [ ] At end of day: count replies received since June 4 enrollment → update open_issues.md

---

## Metrics to Track June 5–11

| Metric | Target Range | How to Check |
|--------|-------------|--------------|
| Open rate | 20–40% by Day 7 | Nina's weekly report |
| Reply rate | 3–8% by Day 7 | Nina's daily/weekly report |
| Hot leads (2+ opens) | 10–30+ | Nina's daily report |
| Ad leads from Facebook | 1–5/day by Week 2 | pipeline_data.json + Google Ads call log |
| Estimates booked from enrollment | 2–8 | Workiz + pipeline_data.json |

---

## Response Scripts (copy-paste ready)

### When a Property Manager Replies (any positive signal)
> "Hey [Name] — thanks for getting back to me. We're in [their area] regularly this time of year. I can get you a quote by the end of this week — what works better, a quick call or I can just swing by the property?"

### When a Contractor Replies
> "Great to hear from you, [Name]. I've got jobs coming in from the [their area] area and the referral setup is simple — $50 for every job you send our way, no paperwork. Want to grab coffee this week?"

### LinkedIn Connect After 2+ Opens (no reply)
> "[Name] — sent you an email about exterior cleaning for your properties last week and saw you had a chance to look. Sometimes LinkedIn is easier. Happy to connect and chat if the timing's right."

---

## What Not to Do This Week
- ❌ Don't edit the Mixmax sequence mid-run (resets learning phase)
- ❌ Don't add more contacts to the sequence before Day 7 (pollutes analytics)
- ❌ Don't panic if open rate is low Day 1–2 (opens cluster around Day 3–7)
- ❌ Don't respond to replies with a "can we hop on a call?" ask before acknowledging their message first
- ❌ Don't forget to log every estimate in pipeline_data.json with `lead_source: "Round 2 PM sequence"`

---

## What Success Looks Like by June 11
- 3–10 replies asking for quotes or more info
- 15–40 hot leads (2+ opens) on LinkedIn connect list
- 2–5 estimates booked
- Pipeline moving from "New Lead" to "Estimate Sent"
- Ad leads also logging in parallel (Week 2 of Facebook + Google)

*Reference: wave2_contractor_followup_schedule_2026-05-27.md | june4_enrollment_readiness_tracker_2026-05-27.md | june4_enrollment_battle_card_2026-05-24.md*

---
*Generated: 2026-05-27 | Vera Cole — Chief Innovation Officer*
