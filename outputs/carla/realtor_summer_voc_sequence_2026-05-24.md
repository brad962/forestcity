# Realtor Summer VOC Sequence — Carla Reyes
### Forest City Power Washing | NE Ohio Referral Outreach
*Created 2026-05-24 | Uses Marcus's NE Ohio VOC Library (outputs/marcus/voc_library_2026-05-23.md)*

---

## Why Realtors Right Now
It's late May in NE Ohio. Summer listing season is in full swing — more listings are going live in June/July than any other time of year. A realtor listing a house in Cuyahoga, Summit, or Lake County needs it to look good *fast*. Power washing is the cheapest per-dollar curb appeal fix available (typically 3–5x ROI on sale price vs. cost of the wash). One good realtor relationship = 3–8 referrals per season, no ad spend required.

**Last realtor outreach from Carla: May 12/13 (6+ weeks ago). This rewrite ships June 4 with Round 2 enrollment.**

---

## Sequence: 3-Touch Realtor Referral Outreach

---

### TOUCH 1 — Subject: Before the lockbox goes up

Hi [firstName],

Quick thought for you — before your next listing goes live, does the exterior look the way it should?

We do exterior cleaning for agents across [city] and Cuyahoga, Summit, and Lake Counties. Most of the time we can turn a house around in a few hours — roof, siding, driveway, everything — for a few hundred dollars. Sellers love it because it shows instantly in listing photos. You love it because the first showing goes better.

A handful of agents just send us an address and we handle the rest. If that sounds useful for any of your upcoming listings, happy to set something up.

— Bradley
Forest City Power Washing
[phone]

**VOC phrases used:** "before the lockbox goes up" (prep anxiety), fast turnaround, listing photos ROI

---

### TOUCH 2 — Subject: Re: curb appeal before you list

Hi [firstName],

Sent this a few days ago — wanted to follow up quickly.

We do a lot of work for realtors who just want the exterior looking right before photos go up. Black roof stains, green siding, stained driveways — we see it constantly on listings in Northeast Ohio. Takes a couple hours to fix. Usually makes a noticeable difference in photos.

No contracts, no minimums. We just want one shot to impress your clients so they send more of their friends to you.

If you've got a listing coming up in the next few weeks, I'd love to take a look. Takes 5 minutes on a walkthrough.

— Bradley
Forest City Power Washing
[phone]

**VOC phrases used:** "black roof stains," "green siding," "stained driveways," "takes a couple hours," "noticeable difference in photos"

---

### TOUCH 3 — Subject: Last note — one listing, that's all I'm asking for

Hi [firstName],

Last message — don't want to clutter your inbox.

I work with a few realtors in [county] on an ongoing basis. Whenever they've got a listing that needs some exterior work before photos, they text me an address and I handle it. Most of them tell me it paid for itself on the first job.

If you ever want to run an experiment on one listing — just to see the difference — I'll make sure the price is right. That's it.

If not, no hard feelings. Good luck with your summer listings either way.

— Bradley
Forest City Power Washing
[phone]

**VOC phrases used:** "clutter your inbox" (direct apology), "run an experiment," "paid for itself," "good luck with your summer listings"

---

## Trade-Specific Touch 1 Variants (swap in for specific realtor types)

### Howard Hanna / Keller Williams / RE/MAX agents
> *"I've been working with a few agents at [brokerage] in [city] — they send me addresses, I make the exterior look right before photos go up. Easier than most vendors they work with."*

### Listing agents with large social presence
> *"I see your listings get a lot of attention on Instagram. Exterior always looks clean — if you ever want help making sure it IS clean before your photographer shows up, that's exactly what we do."*

### Buyer's agents transitioning to listings
> *"I know buyer's agents sometimes move into listings when the market shifts. If you're taking on listings this summer and want a reliable vendor for exterior cleaning, we cover all 7 NE Ohio counties and can usually get there in 48 hours."*

---

## Send Schedule

| Touch | Timing | Subject |
|-------|--------|---------|
| Touch 1 | June 4 (Round 2 enrollment day) | Before the lockbox goes up |
| Touch 2 | June 11 (+7 days) | Re: curb appeal before you list |
| Touch 3 | June 18 (+7 days) | Last note — one listing, that's all I'm asking for |

---

## Response Handling

**YES / "I have a listing coming up":**
→ Respond within 1 hour. Get the address. Schedule a walkthrough or commit to a date.
→ Send quote within 24 hours of seeing the property.
→ Template: "Great — send me the address and I'll get you a number today. We can usually get there within 48 hours of approval."

**"Not right now, maybe later":**
→ "No problem — I'll check back when summer listings pick up. Best of luck with the market."
→ Flag in pipeline for July follow-up.

**"Do you do commercial / HOA work?"**
→ "Yes — that's actually a big part of what we do. Property managers, HOA boards, commercial buildings across NE Ohio. Want me to send some info?"
→ Route to Danny if they manage properties.

**"How much does it cost?"**
→ "Depends on the house, but for a typical listing we're usually $300–$600 for the full exterior. Roof is separate if needed. Happy to send a ballpark if you share the address."

---

## Enrollment Instructions

1. Pull realtor contacts from Apollo using `run_carla()` — Realtors search block
2. Set `_lead_type: realtor` in each lead object
3. Paste the VOC-rewritten Touch 1 subject + body into the Mixmax realtor sequence (ID: 6a048cfba81429e5dfe55010)
4. Run: `python3 workers/lead_pipeline.py carla` (auto-routes to realtor sequence)
5. Time the enrollment for June 4 alongside Round 2 PM enrollment

---

*Revenue math: 10 realtor partners × 4 referrals/summer × $450/job = $18,000 incremental revenue from zero ad spend*
