# Wave 2 Contractor Follow-Up Schedule
### After May 28 First Touch | *Vera Cole — Run 109*
*For: 16 Wave 2 contractor contacts (landscapers + construction)*

---

## The Gap This Solves
You send 16 first-touch texts on May 28. Then what? Without a documented follow-up schedule, these contacts fall into the void — no next touchpoint, no pipeline_data.json update, and no second attempt before June 4 enrollment.

This card defines exactly what happens after May 28.

---

## Wave 2 Follow-Up Stack

### MAY 28 — Day 1 (First Touch)
**Action:** Send first-touch texts per `wave2_contractor_blitz_may28_2026-05-27.md`
**After sending:** Open pipeline_data.json and run:
```
python3 scripts/contact_done.py
```
For each contacted person: stage → "Contacted", last_contact → today, next_followup → May 31

---

### MAY 31 — Day 3 (Follow-Up #2)
**Who:** Everyone from May 28 who did NOT reply
**Script (landscapers):**
> "Hey [name] — sent you a note Wednesday about the $50 referral program. Just checking in. We pay cash the day the job closes. Happy to hop on a quick call if easier. — Brad"

**Script (construction/roofers):**
> "Hey [name] — following up from Wednesday. Any chance you work near homeowners who mention their driveway or siding? We split $50 every referral that books. Worth 2 minutes to talk? — Brad"

**After sending:** Update pipeline_data.json: next_followup → June 4

---

### JUNE 4 — Day 7 (Final Touch / Enrollment Day)
**Who:** Everyone who still hasn't replied
**Context:** June 4 is also Round 2 Mixmax enrollment day — Mixmax sequence will send them a more polished email version
**Script:**
> "Hey [name] — last text, promise. June is our busiest season and we're booking referral partners now. If it's not the right fit, no hard feelings — just let me know and I'll stop texting. If there's any interest, even a 10-min call would be great. — Brad"

**After June 4:** Move non-responders to "Closed Lost" — 3 attempts with no response = not the right fit. Redirect energy to new contacts.

---

## Response Handling

**They reply "Interested":**
1. Send full referral partner packet (see carla.md for pitch deck link)
2. Schedule 15-min call to walk through the $50 program
3. Stage → "Replied" in pipeline_data.json
4. next_followup → 3 days from call

**They reply "Not interested":**
1. Reply: "Totally understand — appreciate you getting back to me!"
2. Stage → "Closed Lost" in pipeline_data.json
3. No further outreach

**They reply "Maybe / Who are you?":**
1. Reply: "Brad at Forest City Power Washing — NE Ohio power washing. We refer jobs back and forth with local contractors. No commitment, easy $50 referral fee per closed job. Want to hear more?"
2. Stage stays "Contacted", next_followup → 2 days

---

## Pipeline Update Commands

After May 28 blitz, run:
```bash
python3 scripts/contact_done.py
```
This shows all May 28 due contacts. For each: mark Contacted, set next_followup = 2026-05-31.

After May 31 follow-up, run same command:
```bash
python3 scripts/contact_done.py
```
For each: confirm "Contacted", set next_followup = 2026-06-04.

---

## Revenue Math

| Scenario | Contacts | Response Rate | Referral Partners | Est. Annual Referral Revenue |
|----------|----------|---------------|-------------------|------------------------------|
| Conservative | 16 | 10% (2 partners) | 2 | $2,000–$5,000 |
| Realistic | 16 | 20% (3 partners) | 3 | $4,000–$12,000 |
| Strong | 16 | 30% (5 partners) | 5 | $8,000–$20,000 |

*Referral revenue = each partner sends 5–15 jobs/year at $300–$1,200 avg ticket.*

---

## Full Timeline View

| Date | Action | Time |
|------|--------|------|
| May 28 | First touch (16 texts) | 45 min |
| May 28 EOD | Update pipeline_data.json | 5 min |
| May 31 | Follow-up #2 (non-responders) | 20 min |
| May 31 EOD | Update pipeline_data.json | 3 min |
| June 4 | Final touch + Mixmax enrollment | 15 min |
| June 4 EOD | Close out non-responders | 2 min |

**Total time investment:** ~90 minutes over 7 days for $4K–$20K/year in referral revenue potential.

---

*Vera Cole | Run 109 | 2026-05-27*
