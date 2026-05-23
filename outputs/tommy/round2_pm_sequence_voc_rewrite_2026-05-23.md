# Round 2 PM Sequence — VOC Rewrite
### Using Marcus's Voice of Customer Library | 2026-05-23
*Tommy Greer | Content & Copy Writer*
*Source: outputs/marcus/voc_library_2026-05-23.md*

---

## What's Different From Round 1

Round 1 emails were written before Marcus had a VOC library. They were generic. This version uses the exact words and phrases NE Ohio property managers and HOA contacts have used in reviews — the "kept putting it off," the "green and slimy," the "I had no idea how bad it was until it was clean." That language is the difference between a cold email that gets deleted and one that gets a reply.

**Ship date:** June 4 enrollment run
**Sequence:** Property Manager Outreach (`6a048cfc110bc620ca0f1aee`)
**Decision:** Pick Touch 1 variant A, B, or C based on the A/B test results from Round 1 (if any opens had a pattern, use that angle)

---

## Touch 1 — Variant A: The "It Builds Up" Angle
*Subject: how it builds up on your properties*

Hi {{firstName}},

The algae doesn't announce itself. One season it's a faint green tinge on the north side. The next season the siding looks like it's been dipped in moss. By year three, tenants are complaining and you're getting quotes for a repaint job that's actually just a cleaning job.

We're Forest City Power Washing. We work with property managers across Cuyahoga, Summit, Lake, and Lorain counties — apartment complexes, HOA communities, commercial buildings. One visit and it looks like a completely different property.

Worth a quick conversation? I can give you a ballpark for {{company}} in about 5 minutes.

Bradley
Forest City Power Washing
[phone]

---

## Touch 1 — Variant B: The "Residents Notice" Angle
*Subject: what residents notice first*

Hi {{firstName}},

The most common thing we hear after cleaning a property: "I had no idea how bad it looked until it was clean."

The black streaks on the roof. The green film on the siding. The grimy sidewalks at the entrance. Residents notice. Prospective tenants notice. Board members notice. It's the kind of thing that's easy to put off — until someone mentions it in a review.

Forest City Power Washing serves HOA communities, apartment complexes, and commercial properties across Northeast Ohio. We're fast, we don't damage surfaces, and we leave it looking like the day it was built.

Any properties on your list that need attention this season?

Bradley
Forest City Power Washing
[phone]

---

## Touch 1 — Variant C: The Direct Question
*Subject: quick question about {{company}}*

Hi {{firstName}},

Do you currently have a vendor for exterior cleaning at {{company}} — roof, siding, parking areas?

If not, or if you're not happy with whoever you've got, I'd like to put a number in front of you. We serve property managers across seven Northeast Ohio counties. Fast response, no damage, before-and-after photos after every job.

One email back is all it takes.

Bradley
Forest City Power Washing
[phone]

---

## Touch 2 — "What Property Managers Tell Us"
*Subject: what PMs in your area are dealing with*

*Send: 5 days after Touch 1 if no reply*

Hi {{firstName}},

Following up from last week. Wanted to share something that keeps coming up from property managers we work with in NE Ohio:

The biggest issue isn't the cost of cleaning — it's the cost of waiting. Algae on a roof that goes untreated for two or three seasons starts to degrade the shingles. Siding that looks green and slimy ends up being an objection in every new tenant walk-through. One cleaning visit per year prevents all of that.

We do full-property packages — roof soft wash, house wash, driveway, parking areas — or individual surfaces if you just need one thing handled. Most complexes we work with book once in spring, once before winter.

If {{company}} is overdue, I'm happy to put a number together with no obligation.

Bradley
Forest City Power Washing
[phone]

---

## Touch 3 — "Last Email, Real Question"
*Subject: last one from me*

*Send: 5 days after Touch 2 if no reply*

Hi {{firstName}},

Last email, I promise.

We're in peak season in Northeast Ohio right now and booking fast. If {{company}} has anything that needs cleaning before summer — and most properties do after a NE Ohio winter — this is the right window to get it scheduled.

If you already have someone you trust, I respect that. If you're open to a second quote or just want to see what a job at your property would run, I'm an email away.

Bradley Neal
Forest City Power Washing
brad@forestcitypowerwashing.com | [phone]

---

## VOC Language Reference (used above)
From `outputs/marcus/voc_library_2026-05-23.md`:

| Phrase Used | Source Theme |
|-------------|-------------|
| "had no idea how bad it looked until it was clean" | Post-job revelation |
| "residents notice" | Commercial PM pain point |
| "kept putting it off" | Delay/avoidance pattern |
| "green and slimy siding" | Visual problem language |
| "black streaks on the roof" | Algae/staining language |
| "before a repaint job that's just a cleaning job" | Cost-of-waiting frame |
| "before-and-after photos after every job" | Trust signal that works |

---

## Send Instructions

**Mixmax setup:**
1. Go to Mixmax → Sequences → Property Manager sequence (`6a048cfc110bc620ca0f1aee`)
2. Click "Edit" → replace each email body with the copy above
3. Update subjects in Mixmax UI
4. Save → run enrollment: `python3 workers/lead_pipeline.py danny Summit` then `both`

**A/B testing:**
- If running all 3 Touch 1 variants, enroll in batches of 15–20 per variant
- Label batches in contacts_cache by adding `_variant_a/b/c` to `_source` field
- Check open rates after 72 hours in nina_report to determine winner

**Timing:**
- Touch 1: morning 8–10am Tuesday June 4
- Touch 2: Thursday June 9 (auto-send via Mixmax)
- Touch 3: Tuesday June 17 (auto-send via Mixmax)

---

*Tommy Greer | Forest City Power Washing | Generated 2026-05-23*
