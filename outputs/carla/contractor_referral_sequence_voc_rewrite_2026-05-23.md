# Carla's Contractor Referral Sequence — VOC Rewrite
*Carla Reyes | Rewritten 2026-05-23 using Marcus's NE Ohio VOC Library*
*Source VOC: `outputs/marcus/voc_library_2026-05-23.md`*

---

## What Changed and Why

The original contractor outreach (`outreach_contractors_2026-05-12.md`) was written before:
- Tree service / arborist partners were added (Run 57)
- HVAC, pool service, pest control, irrigation were added (Run 54)
- Marcus built the NE Ohio VOC library with real customer language (Run 64)

This version uses **the exact words contractors' customers use** when they call about dirty exteriors.
It works for all 15 Carla partner types — the language is universal because every trades person hears it.

**Ship this version for Round 2 enrollment (June 4 target).**

---

## Sequence Variables

- `{{recipientFirstName}}` — contact's first name
- `{{recipientCompany}}` — their business name
- `{{senderFirstName}}` — Bradley
- `{{senderCompany}}` — Forest City Power Washing

---

## TOUCH 1 — Subject: You see this every day

**Subject:** You see this every day

Hi {{recipientFirstName}},

You're at properties every single week. You've definitely walked past a house with green algae up the siding, a roof that's turned black, or a driveway that looks like it hasn't been touched in years.

Your customers notice it too. They just don't always know who to call.

I run Forest City Power Washing. We do exterior cleaning across all 7 Northeast Ohio counties — house washing, roof soft wash, driveways, commercial properties. When your customers ask about the grime, I want them calling us.

Here's the deal: you send us a job, we send you $50. No paperwork, no formal agreement. Just a handshake deal between two local businesses.

Worth a quick call this week?

{{senderFirstName}}
Forest City Power Washing
[phone]

---

**Touch 1 notes:**
- "green algae up the siding" and "roof that's turned black" = VOC phrases from Marcus's library
- "They just don't always know who to call" = the pain point that makes the referral ask land
- No pitch about Forest City's services — they're a referral partner, not a customer

---

## TOUCH 2 — Subject: Quick example

**Subject:** Quick example

Hi {{recipientFirstName}},

Last week we did a house in Strongsville. Landscaper had been mowing the lawn there for three years. Finally told the homeowner the siding looked "green and slimy." They called us.

That's the kind of referral I'm talking about.

If someone on your schedule mentions the algae, the stained roof, the driveway that looks like it hasn't been touched — drop them our number. We'll do the rest. You get $50 when the job closes.

We're booking into June now. Would love to have {{recipientCompany}} as a partner this season.

{{senderFirstName}}
Forest City Power Washing
[phone]

---

**Touch 2 notes:**
- Specific job story (Strongsville = NE Ohio local reference) — sounds like a real person
- "green and slimy" = exact VOC phrase from Marcus's library (landscaper used this exact phrase)
- Recreates the scenario the contractor already experiences weekly — recognition, not pitch

---

## TOUCH 3 — Subject: Last note

**Subject:** Last note (and a good one)

Hi {{recipientFirstName}},

One more note before I stop bugging you.

This is peak season — we're staying busy in {{senderCompany}}'s service area all the way through September. The referral deal is simple: someone on your schedule asks about the exterior, you send them our number, we close the job, you get $50.

We've got contractors sending us 3–4 jobs a month right now. Zero paperwork. They text us the customer name, we handle everything.

If the timing is ever right, you know where to find me.

{{senderFirstName}}
Forest City Power Washing
[phone]

---

**Touch 3 notes:**
- "stop bugging you" = real-person language, disarms the prospect
- Social proof: "contractors sending us 3–4 jobs a month" — make it feel established
- Leaves the door open without a hard close — referral partnerships are trust-based, not pressure-based

---

## Partner-Type Customizations

For higher reply rates, add ONE line to Touch 1 that's specific to their trade:

| Partner Type | Add to Touch 1 — after "You're at properties every single week." |
|---|---|
| Landscaper | "Every time you mow, you can see the algae on the siding better than the homeowner can." |
| Roofer | "You're on roofs where the black streaks are so bad homeowners think they need a full replacement — half the time it's just algae and a soft wash fixes it for a fraction of the cost." |
| Gutter cleaner | "You're up there seeing the moss on the shingles and the green staining on the fascia — stuff the homeowner doesn't even know is there until you point it out." |
| Siding contractor | "You go out there to quote a siding job and half the time the house just needs a proper wash first." |
| Painter | "You've walked away from jobs where the surface prep was a soft wash job, not a paint job." |
| HVAC | "You're inside every home twice a year for tune-ups. You've walked past a lot of siding that looks like it hasn't been touched since the house was built." |
| Pool service | "You're in the backyard all summer. You see the deck furniture, the concrete, the fence — all of it." |
| Tree service/Arborist | "You're up in the tree looking at roofs with black streaks and moss. Your customers ask about it." |
| Irrigation | "You're in the yard every spring turning on the system. You're looking at the siding while you're out there." |
| Pest control | "You're on every doorstep twice a year. You see what the exterior looks like better than anyone." |
| Chimney sweep | "You're on the roof. You see the staining from up there." |

---

## Sending Guide

**Volume:** Enroll batch via Mixmax contractor sequence (`6a048cfd624a5989a68ba16c`) during the June 4 enrollment run.

**Manual customization:** For the top 10 Carla contacts in `pipeline_data.json` (New Lead stage), use partner-type customizations above. Send manually from Bradley's Gmail for highest reply rate.

**Existing contacts:** The `june_referral_revival_texts_2026-05-23.md` has text-first approach for Tier 1 contractor pipeline contacts who've never replied to email — text before adding to a new email sequence.

---

## Round 2 Integration

This sequence goes live in parallel with Danny's PM sequence VOC rewrite (`outputs/tommy/round2_pm_sequence_voc_rewrite_2026-05-23.md`) on June 4.

**Before enrolling:** Confirm Instantly.ai campaigns paused (a1c08c3d + 626cd15d). This affects contractor sequence deliverability too, not just PM.

---

*Written by Vera using Marcus VOC library | 2026-05-23*
