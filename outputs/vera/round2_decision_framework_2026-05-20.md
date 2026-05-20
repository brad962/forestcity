# Round 2 Sequence Decision Framework
### Vera Cole | Chief Innovation Officer
*Created: 2026-05-20 | Applies to: Post-Touch-3 decisions (May 22 onward)*

---

## The Problem With Changing Everything at Once

After Touch 3 fires May 22, two variables are unresolved:
1. **Was the Reply-To address correct?** (10-minute check — do this tonight before Touch 3)
2. **Is the sequence copy the problem?** (Hard to know without isolating variables)

If we change the sequence copy AND fix Reply-To simultaneously and then get replies, we don't know what drove the improvement. That means we make the wrong decision for Round 3.

**Rule: Change one variable at a time.**

---

## Decision Tree — What Touch 3 Results Tell You

### Scenario A: Touch 3 gets replies ✅
**What it means:** The copy was fine. The Reply-To was probably the blocker.
**Round 2 action:** Keep the same sequence. Don't rewrite. Fix Reply-To (if not already done) and run Round 2 with the current copy. Enroll new Summit/Medina leads starting June 4.

### Scenario B: Touch 3 gets 0 replies, Reply-To is confirmed correct ⚠️
**What it means:** The copy isn't converting. This is an A/B test opportunity.
**Round 2 action:** Use the rewritten sequence. Apply it to the 45 re-enrolled Round 1 contacts AND new Summit/Medina enrollees. Send the same copy to all.
- Rewrite approval: `outputs/danny/pm_sequence_touch1_rewrite_2026-05-19.md`
- Reply "YES REWRITE" to approve — Vera will update the Mixmax sequence copy.

### Scenario C: Touch 3 gets 0 replies, Reply-To was wrong all along 🔴
**What it means:** Replies may have been going to the wrong inbox the entire time. You have no data on whether the copy works.
**Round 2 action:** Fix Reply-To first. Run Round 2 with the CURRENT copy. Don't change copy yet — you're still gathering clean data.
- If Round 2 with correct Reply-To and same copy gets 0 replies → THEN switch to rewrite.

### Scenario D: Touch 3 gets 0 replies, Reply-To fix uncertain ❓
**What it means:** You're not sure if Reply-To was wrong. Check the Mixmax setting immediately.
**Round 2 action:** Follow the `outputs/vera/mixmax_reply_to_check_2026-05-20.md` guide. If it was wrong, fix it → treat as Scenario C. If it was always correct → treat as Scenario B.

---

## The Specific Decision You Make on May 22

**After Touch 3 fires (check Mixmax at 9am):**

1. Open Mixmax → PM sequence → any new replies since May 22 midnight?
   - Yes, 1+ reply → **Scenario A** — Keep current copy. Celebrate.
   - No replies → Continue to step 2.

2. Go to Mixmax → PM sequence settings → Reply-To email. Is it your real Gmail?
   - No / blank / wrong → Fix it now. **Scenario C** — Don't change copy.
   - Yes, correct → **Scenario B** — Approve the rewrite.

3. Text Vera: "Reply-To was [correct / wrong]. Touch 3 got [X] replies. Decision: [keep copy / use rewrite]."

---

## The A/B Testing Constraint

We have 45 contacts going into Round 2. That's too small a sample to split-test (23 each). If we split, neither group will have statistical significance.

**Recommendation:** Run all 45 on the same copy in Round 2. Whichever copy we use, run all 45 through it. Then evaluate before Round 3 (July enrollment).

---

## What Vera Will Implement Once You Decide

**If "keep current copy":**
- No changes to Mixmax sequences
- Danny runs the Apollo pull as normal
- Vera monitors Round 2 reply rate and reports back June 9

**If "use rewrite" (approved):**
- Vera edits Touch 1 and Touch 2 in Mixmax using copy from `outputs/danny/pm_sequence_touch1_rewrite_2026-05-19.md`
- Verify edits saved before any enrollment begins
- Log change in activity.log

---

## Tracking (Fill in After Touch 3 — May 22)

| Variable | Status |
|----------|--------|
| Touch 3 replies received | ___ |
| Reply-To email confirmed | ___  (correct / was wrong / fixed to ___) |
| Decision | ___ (keep copy / use rewrite) |
| Round 2 sequence type | ___ |
| Enrollment start date | June ___, 2026 |

---

*Vera Cole | Chief Innovation Officer | Forest City Power Washing*
*Review on May 22 morning. Update tracking table above. File: `outputs/vera/round2_decision_framework_2026-05-20.md`*
