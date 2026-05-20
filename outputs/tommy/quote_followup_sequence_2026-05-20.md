# Quote Follow-Up Sequence — Forest City Power Washing
*Tommy Greer | Content & Copy Writer*
*Written: 2026-05-20*

---

## The Gap This Fills

Right now, the pipeline works like this:

1. Danny emails a property manager → they open it → they request a quote
2. Bradley sends the quote
3. **Nothing happens after that.**

Most jobs are lost not in the pitch — they're lost in the silence after the quote. Research across home services shows:
- 60–70% of estimates never get a follow-up
- A single follow-up text within 48 hours closes an additional 20–25% of quotes
- Two follow-ups (text + email) close 35–40% of open quotes

This sequence fills that gap. It's not pushy. It's professional.

---

## When to Use This

**Trigger:** Anytime a prospect:
- Replies to a Mixmax email asking for a quote
- Calls and asks for a price
- Fills out a quote form (once Google Ads and the website are live)
- Reaches out via Facebook

Send Touch 1 within 24 hours of sending the quote. Touch 2 if no response after 3–4 days.

---

## Touch 1 — Text (Send 24–48 hours after quote)

```
Hey [First Name] — just following up on the quote I sent for [property/address].
Happy to answer any questions or adjust the scope if needed.
Shoot me a text when you're ready and I'll get you on the schedule.
— Bradley, Forest City Power Washing
```

**Why text, not email?** They already have the quote in their email. A text is lower friction — it reminds them without requiring them to dig through their inbox.

---

## Touch 2 — Email (Send 3–4 days after Touch 1 with no response)

**Subject:** Re: Quote for [address / company name]

```
Hi [First Name],

Still have a spot open on the schedule for you. Just wanted to check in before the summer rush fills up.

A few things that are worth knowing:

- We can usually get to you within 5–7 business days right now. That window gets longer as we get deeper into June.
- For most house washes in your area, the job takes 2–3 hours and you don't need to be home.
- We guarantee our work — if anything doesn't look right within 30 days, we come back.

If the price felt off or you have questions about what's included, I'm happy to talk it through.

Just reply here or text me at [Bradley's phone].

Thanks,
Bradley
Forest City Power Washing
```

**Why this works:** It's not "just checking in" filler. It adds new information (timeline, guarantee, process) that gives them a reason to act NOW instead of later.

---

## Touch 3 — Final Text (Optional — 7 days after Touch 2, if still no response)

```
Hey [First Name] — last check-in on this, I promise.

If the timing isn't right for this season, no worries. I'll reach back out in the fall.
But if you're still interested, reply here and I'll hold a spot for you.
— Bradley
```

**Why this works:** Gives them an easy out (so they don't feel pressured), but gives them ONE more chance to say yes. The "I'll reach back out in the fall" line is a soft rebook trigger — if they say "actually, let's do fall" you've just re-qualified a warm lead.

---

## Handling the "Too Expensive" Objection

If they reply saying the price is too high:

```
Totally understand — pricing can vary a lot in this area.

Can I ask what you were expecting? I might be able to adjust the scope — for example, if you want to start with just the driveway or just the house (not both), that brings the price down.

If it's still not a fit this year, no hard feelings. I'd rather you're happy than rush a decision.
```

**Never just drop the price.** Offer to scope down first. It usually closes better.

---

## Tracking (Until HubSpot Is Connected)

Use pipeline_data.json stages:
- **Estimate Sent** = quote has gone out, no response
- **Follow-Up** = Touch 1 sent, waiting on response
- **Replied** = responded (positive or not)
- **Closed Won** = booked
- **Closed Lost** = confirmed not booking this season

Set `next_followup` date when you send the quote. Check `outputs/vera/priority_outreach_list_2026-05-19.md` for the existing pipeline.

---

## For Contractor/Realtor Referral Quotes

Slightly different script — they're sending you the lead, not buying themselves.

**Touch 1 Text (24 hours after receiving their referral):**
```
Hey [First Name] — I reached out to [customer name] and they're going to get a quote this week.
I'll let you know how it goes. Appreciate the referral!
— Bradley, Forest City
```

**After the job is complete:**
```
Hey [First Name] — just wanted to let you know [customer name]'s job is done and they loved it.
I'll get your $50 referral credit over to you. Thanks again — keep them coming!
```

---

*Tommy Greer | Forest City Power Washing*
*Use this sequence after every quote sent. Set a reminder in your phone or in pipeline_data.json.*
