# Touch 3 Zero-Reply Protocol
### Vera Cole | CIO
*Use this if Touch 3 sends May 22 and produces 0 replies by May 23 evening*

---

## First: Don't Panic. Here's the Reality.

A 0% reply rate from a cold email sequence to property managers in NE Ohio isn't a failure — it's normal for round 1. Industry average for cold B2B email is 1–3% reply rate. With 45 contacts, that's 0–1 expected replies statistically.

The sequence has 42% opens. The message is being READ. They're just not responding to the email.

The issue isn't the business — it's the channel. Busy property managers read email; they reply to the phone.

---

## What to Do — In Order

### Step 1: Run Nina's Report (May 22 evening or May 23 morning)

```
cd ~/forestcity && python3 workers/nina_report.py daily
```

This shows:
- How many opens did Touch 3 get?
- Anyone open Touch 3 AND Touch 1 or 2 (multiple opens = hottest lead)
- Exact names and emails of everyone with 2+ opens

---

### Step 2: Call Your Top 5 Multi-Open Contacts

Anyone with 3+ opens across the sequence is a warm lead. They've read your emails multiple times and haven't unsubscribed. That's interest.

**Script:** Use `outputs/tommy/hot_lead_phone_script_2026-05-22.md`
- Version A: Live call (open with "I sent you a few emails about exterior cleaning...")
- Version B: Voicemail (brief, 30 seconds, callback number)
- Version C: SMS follow-up (if no callback after 24h)

Do this May 23–24. Don't wait until May 26.

---

### Step 3: Send Bridge Emails to Top 5 (Personal Gmail)

**Template:** `outputs/tommy/hot_lead_bridge_email_2026-05-20.md`

This is a personal email from Bradley's Gmail (not Mixmax) to the 5 highest-engagement contacts. It breaks the "automated sequence" frame and feels like a real person reaching out. Subject line: their name.

Send May 23 or 24. One per day max — you want to respond fast if they reply.

---

### Step 4: LinkedIn Connect to Everyone Who Opened

Anyone who opened Touch 3 = active interest signal. Send a LinkedIn connection request with a short note:

> "Hi [Name] — I've reached out a few times about exterior cleaning services for your properties. Wanted to connect here as well. —Bradley"

**Template:** `outputs/tommy/linkedin_followup_post_connect_2026-05-21.md` (Version A)

LinkedIn message converts when email doesn't. This is the multi-channel close.

---

### Step 5: Pivot Decision — Make It by May 25

Before Memorial Day ends, decide:

| Condition | Decision |
|-----------|----------|
| 0 replies, opens > 40% | Keep sequence. Change send time to 10:30am for Round 2. Volume is the fix. |
| 0 replies, opens 25–40% | Keep sequence text, change send time. Add A/B subject line test for Round 2. |
| 0 replies, opens < 25% | Sequence needs a refresh. Let Vera rewrite Touch 1. |

Current open rate: ~42%. → **Keep the sequence. Change the send time. Add volume.**

Round 2 plan: `outputs/donna/round2_enrollment_plan_2026-05-21.md`

---

### Step 6: Text Your Tier 1 Contractors (No Email Needed)

While you're waiting on PM replies, your contractors are a parallel track:

- Land Pro / Anthony (440-320-2779) — if not already texted
- GTP Landscaping / Dontez (440-396-0814) — if not already texted
- Follow-ups May 26: Bulletproof (216-307-4344), Damrons (440-494-0422), CLE Lawn Care Plus (216-402-1924)

**Templates:** `outputs/tommy/contractor_followup_texts_may26_2026-05-21.md`

A contractor referral partner converts faster than a cold PM email lead. One "yes" from a busy landscaper who sees 30 properties/week = 5–10 jobs/season.

---

## What NOT to Do

- **Don't rewrite the sequence from scratch.** You have 42% opens. The copy isn't the problem.
- **Don't wait for June 1 to start Round 2 enrollment.** Summit County leads should be in the pipeline before Memorial Day. Run the cron tonight.
- **Don't close out the 45 contacts.** They're still active in Mixmax. They may reply to Touch 3 after the weekend (Tuesday–Wednesday next week is when people catch up on email).

---

## Files Referenced

| When | File |
|------|------|
| May 22 evening | `outputs/nina/hot_leads_2026-05-22.md` (run locally) |
| May 23–24 calls | `outputs/tommy/hot_lead_phone_script_2026-05-22.md` |
| May 23–24 emails | `outputs/tommy/hot_lead_bridge_email_2026-05-20.md` |
| May 23–24 LinkedIn | `outputs/tommy/linkedin_followup_post_connect_2026-05-21.md` |
| May 25 decision | `outputs/vera/round2_decision_framework_2026-05-20.md` |
| May 26 Round 2 plan | `outputs/donna/round2_enrollment_plan_2026-05-21.md` |
| May 26 contractor texts | `outputs/tommy/contractor_followup_texts_may26_2026-05-21.md` |

---

## The Headline

Zero replies from Touch 3 is NOT a reason to stop. It's a signal to:
1. Call the warm ones (they're reading your emails)
2. Add more contacts (Round 2, June 4)
3. Fix the send time (10:30am)

The pipeline is alive. Keep feeding it.

---

*Vera Cole | Chief Innovation Officer | Generated May 21, 2026*
