# Email Deliverability Checklist — Touch 3 / 0% Reply Investigation
**Forest City Power Washing | May 22, 2026**
*Vera Cole — fresh angle on 0% reply rate after 3-touch sequence*

---

## The Hypothesis

45 contacts enrolled. Emails sent. 0 replies. Most likely cause is **not** a bad offer.
Cold email to property managers averages 3–8% reply rate in good conditions.
0 replies across 45 people after 3 touches is a deliverability signal — the emails may not be landing in the inbox.

---

## STEP 1 — Check Mixmax Sending Stats (5 min)

Log in to Mixmax → Sequences → Property Manager → click into the sequence.

What you're looking for:
- **Opens:** If 0 opens AND 0 replies → emails are hitting spam OR sequence isn't sending
- **Some opens, 0 replies:** Deliverability is OK. Problem is the message, not delivery.
- **Bounces:** Any contacts with "bounced" status → bad emails from Apollo

**If you see 0 opens on all 45 contacts:**
→ Jump to Step 3 (Spam Check) immediately.

---

## STEP 2 — Verify Sequence Is Actually Sending (2 min)

In Mixmax:
1. Click into Property Manager sequence
2. Click any recipient → check "Stages" tab
3. Confirm each stage shows "Sent" status (not "Scheduled" or "Paused")

If stages show "Paused" → the sequence may have been paused manually or by a Mixmax system flag.
Fix: Click "Resume" on the sequence.

---

## STEP 3 — Run a Spam Test on Your Sending Address (5 min)

1. Go to **mail-tester.com** (free, no account needed)
2. Copy the test email address shown
3. In Mixmax → compose a new email → send to that test address (any content)
4. Go back to mail-tester.com → click "Check your score"

**Score 7/10+:** Deliverability is fine. Issue is the message or offer.
**Score below 7/10:** Spam problem. Common fixes below.

---

## STEP 4 — Check SPF/DKIM/DMARC on Your Sending Domain (10 min)

Your Mixmax sends from your Gmail. Gmail handles DKIM by default — but if you're using a custom domain (e.g., info@forestcitypowerwashing.com), you need to verify:

1. Go to **mxtoolbox.com/SuperTool.aspx**
2. Enter your sending domain → run SPF Lookup, DKIM Lookup, and DMARC Lookup
3. All three should show "PASS" or be configured

**If using Gmail (firstname@gmail.com or firstname@gmail.com):** SPF/DKIM are fine — skip this step.
**If using a custom domain:** Missing SPF or DKIM → emails are likely hitting spam.

---

## STEP 5 — Check Instantly.ai for Duplicate Sending (5 min)

There's an active risk that Instantly.ai is also sending emails to the same contacts. If recipients got the same email twice from two different senders, they may have marked it as spam.

1. Log in to **instantly.ai**
2. Go to Campaigns → check all active campaigns
3. **Pause or stop ALL campaigns** — Mixmax is your sole active platform

This is the most likely cause of spam complaints if Instantly was running in parallel.

---

## STEP 6 — Check for Bounced Emails (3 min)

In Mixmax → Sequences → Property Manager → look for any contacts marked "bounced" or "invalid email."

Bounced contacts drag your sender reputation down. If 5+ contacts bounced, your domain may be flagged.
Fix: Remove bounced contacts from future sequences.

---

## STEP 7 — Warm Up Protocol (if score below 7/10)

If mail-tester gives you a low score:

1. Send 10–15 normal personal emails from your Gmail over the next 48 hours (to people you know)
2. Reply to emails in your inbox
3. Mark any Forest City emails in your spam folder as "Not Spam"
4. Wait 24–48 hours, then re-run mail-tester

Do NOT send new Mixmax sequences until score is back to 8/10+.

---

## DECISION TREE — After Running This Checklist

| Finding | Action |
|---------|--------|
| Score 7–10, sequence sending, some opens | Fix the message — use `round2_pm_sequence_rewrite_2026-05-21.md` |
| Score 7–10, 0 opens on all 45 contacts | Sequence paused or wrong email — check Mixmax sending log |
| Score below 7 | Warm up Gmail, disable Instantly.ai, wait 48h before Round 2 |
| 5+ bounces | Clean list before Round 2, don't re-enroll bounced contacts |
| Instantly.ai was running | Stop it, wait 72h for spam flags to clear, then resume Mixmax |

---

## If Everything Checks Out (Score 8+, No Issues)

The sequence is delivering. Replies will come — 0 replies after Touch 3 is unusual but not impossible with property managers (they're busy, cautious, not active email responders).

**Next step:** Round 2 with a rewritten Email 1 (see `outputs/tommy/round2_pm_sequence_rewrite_2026-05-21.md`).
Recommendation: Use Version C (Direct Question) — shortest, most direct, lowest friction to reply.

---
*Vera Cole — Forest City AI Office | Generated 2026-05-22*
