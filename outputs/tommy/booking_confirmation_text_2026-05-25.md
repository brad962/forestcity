# Booking Confirmation Text & Email
### What Bradley Sends the Moment They Say YES
*Tommy Greer | Content & Copy Writer*

> **When to use:** The second a customer says "yes, book me" — whether by phone (after Facebook ad call), DM, web form follow-up, or in person. This fires BEFORE the pre-job reminder sequence. The gap between "yes" and the day-before reminder should not be silence.

---

## The Gap This Fills

**Rick's Facebook Lead SOP** ends with: "Book them, enter in Workiz."
**Tommy's Pre-Job Reminder** starts: "Day before the job."

The gap: **nothing goes to the customer the day they book.** First-time customers feel uncertain after hanging up. "Did he write it down? Do they have my address? Will they actually show up?" A single confirmation text closes that loop and sets the tone for the whole relationship.

---

## Text #1 — Instant Booking Confirmation
*Send within 5 minutes of hanging up. Can copy-paste from Notes app.*

**Template A — Residential (Facebook Ad / Inbound Call):**
```
Hey [First Name], it's Bradley from Forest City Power Washing. 
Just confirming your appointment — [DAY], [DATE] at [TIME]. 
Address: [ADDRESS] — let me know if that's right.
You'll get a reminder text the day before. Questions anytime. 
Can't wait to make it look brand new. – Bradley
```

**Template B — Short version (DM booking or if they seem busy):**
```
Confirmed! Forest City Power Washing — [DATE] at [TIME] at [ADDRESS]. 
Reminder coming the day before. Text me anytime. – Bradley 📞 [YOUR NUMBER]
```

**Template C — Commercial / Property Manager:**
```
Hi [First Name], Bradley here from Forest City Power Washing. 
Confirming your service at [PROPERTY/ADDRESS] — [DATE] at [TIME]. 
We'll need [ACCESS INFO if applicable]. Reminder text coming day before.
Questions: [YOUR NUMBER]. Looking forward to it.
```

---

## Text #2 — What to Expect (same day, send 30-60 min after confirmation)
*Only send if it's their first time using Forest City. Skip for returning customers.*

```
Quick heads up for [DATE]:

We do soft washing, not pressure washing — safe for siding, roofs, and wood. 
You might notice a mild soapy smell for a few hours after — totally normal, 
washes off with any rain or hose. 

No need to be home — we just need access to a hose spigot if possible.

See you [DAY]! – Bradley, Forest City Power Washing
```

> **Why this matters:** First-time ad leads have no idea what "soft washing" means. Setting expectations prevents the "why does my house smell?" call the next day. Avoids cancellations from people who think pressure washing will damage their siding.

---

## Text #3 — Address Confirmation (if you're not 100% sure you got it right)
*Use when address was given verbally or in a DM and you want to double-check.*

```
Quick check — want to confirm the address is: [ADDRESS].
And the best access point for a hose spigot is [FRONT/BACK/SIDE]?
Thanks! – Bradley
```

---

## Email Version — For Customers Who Prefer Email

*Same content as texts, formatted for email. Send from your business Gmail.*

**Subject:** Your Forest City Power Washing Appointment — [DATE]

```
Hi [First Name],

Just confirming your power washing appointment:

📅 Date: [FULL DATE]
⏰ Time: [TIME] (we'll be there within a 30-minute window)
📍 Address: [FULL ADDRESS]
🧼 Service: [HOUSE WASH / ROOF SOFT WASH / DRIVEWAY / etc.]

What to expect:
• We soft wash, not pressure wash — safe for siding, roofing, and wood surfaces
• Mild soapy smell for a few hours after (washes off with rain or a hose)
• You don't need to be home — just access to an outdoor spigot helps
• Full job takes about [1-2 / 2-3 / 3-4] hours depending on size

You'll get a reminder text the morning before your appointment.

Questions? Text or call: [YOUR NUMBER]

Looking forward to it,
Bradley Neal
Forest City Power Washing
[YOUR NUMBER]
forestcitypowerwashing.com
```

---

## Cancellation / Reschedule Handling

If they need to reschedule, here's your reply:

```
No problem at all! What dates/times work better for you? 
We have [OPTIONS] open. – Bradley
```

If it's a same-day cancellation (you're already en route):
```
No worries. We had a crew heading out but we can redirect them. 
What date works for a reschedule? We'll make it easy.
```

> **Don't sound frustrated.** Reschedulers often book again and sometimes refer friends. Keep the tone warm.

---

## Workiz Entry Checklist (do this right after confirming)

- [ ] Enter job in Workiz with: JobType = "Power Washing" (exact — needed for Nina's revenue report)
- [ ] Set date + time
- [ ] Add client name, phone, address
- [ ] Set status: "Scheduled"
- [ ] Add revenue estimate in JobTotalPrice

---

## The Full Sequence Timeline

| Trigger | Action | Owner |
|---------|--------|-------|
| Customer says YES | Text #1 (booking confirmation) | Bradley — send immediately |
| +30-60 min | Text #2 (what to expect) — first-time customers only | Bradley |
| Day before job | Day-before reminder | `pre_job_reminder_text_sequence` |
| 2 hours before | 2-hour heads up | `pre_job_reminder_text_sequence` |
| Job complete | Post-job text + Google review ask | `pre_job_reminder_text_sequence` |
| 2 hours post-job | Annual plan upsell | `annual_plan_upsell_sequence` |

---

*Tommy Greer | May 25, 2026*
*Pairs with: `outputs/rick/facebook_lead_response_sop_2026-05-24.md` (the call that gets the YES)*
*Followed by: `outputs/tommy/pre_job_reminder_text_sequence_2026-05-24.md` (day-before through post-job)*
