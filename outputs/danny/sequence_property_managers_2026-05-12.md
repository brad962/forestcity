# Cold Email Sequence — Property Managers
### Forest City Power Washing | Outbound Campaign
*Danny Malone | Outbound Sales Rep | 2026-05-12*

---

## Campaign Overview

**Target:** Property managers, facility managers, community managers, HOA managers
**Geography:** Cuyahoga, Lake, Lorain, Medina, Summit, Geauga, Portage counties
**Sequence:** 3 touches over 10 days
**Goal:** Get a reply or a call booked for an estimate
**Tone:** Direct, peer-to-peer, short — not a sales pitch

---

## TOUCH 1 — Day 1 (Initial Outreach)

**Subject:** Exterior cleaning vendor for your properties

---

[First Name],

I run the outbound side for Forest City Power Washing here in Northeast Ohio. We work with property managers across all 7 counties — Cuyahoga, Lake, Lorain, Medina, Summit, Geauga, and Portage.

Most of the property managers we work with found us after getting burned by someone else — no-show, wrong chemicals on the siding, that kind of thing. We try to be the opposite: we show up when we say, use the right method for each surface (soft wash for siding and roofs — not a pressure washer pointed at everything), and we give a straight price upfront.

If you're handling exterior cleaning for any of your properties right now, or you'll be looking for a vendor this spring, I'd like to introduce myself.

Quick question: how many properties are you managing in the area, and are you currently working with someone for exterior cleaning?

— Danny Malone
On behalf of Bradley at Forest City Power Washing
[phone]

---

## TOUCH 2 — Day 4 (Value Add)

**Subject:** Re: Exterior cleaning vendor for your properties

---

[First Name],

Following up on my last note — wanted to add something useful before you close this email.

One thing we do differently for property managers: we handle multi-property scheduling. If you've got 3-5 properties in a county that need washing in the same season, we route them together — you get a better per-property price and a cleaner schedule. Most of our property manager clients use us on an annual cycle (spring + pre-winter) so they're not thinking about it every year.

We're insured, we document the job with photos, and we flag anything concerning we see on the property (staining patterns that suggest drainage issues, soft spots on decks, that kind of thing). We're not inspectors, but we're eyes on the exterior that you'd otherwise pay someone else to be.

Worth a 10-minute call? I can run through how we handle multi-property accounts.

— Danny
Forest City Power Washing | [phone]

---

## TOUCH 3 — Day 10 (Last Touch)

**Subject:** Last note from Forest City

---

[First Name],

Last follow-up, then I'll leave you alone.

If exterior cleaning for your properties isn't something you're thinking about right now — fair. If you want to revisit it before spring gets fully underway, I'm easy to reach.

Two things I'll leave you with:

1. **Free property walk.** Bradley can stop by any property you're managing and give you an honest assessment — what needs attention, what can wait, and a rough price range. No commitment.

2. **The "bad vendor" problem is real.** If you've ever had a contractor no-show, use the wrong pressure on a surface, or leave without finishing — we hear it constantly. We're not perfect, but we show up and we finish what we quote.

Reply here or call Bradley directly at [phone] if you ever want to talk.

— Danny
Forest City Power Washing

---

## Email Writing Notes

**What makes this sequence work:**
1. **Touch 1** is peer-to-peer curiosity — one question at the end gets replies
2. **Touch 2** adds value (multi-property scheduling) — doesn't just nag
3. **Touch 3** is low-pressure last contact — offers something tangible (free walk)

**A/B test options:**
- Touch 1 subject: "Exterior cleaning vendor for your properties" vs. "Quick question — Forest City Power Washing"
- Touch 2 subject: Keep as reply thread vs. fresh subject "Multi-property pricing for NE Ohio PMs"
- Touch 1 CTA: "Quick question" vs. "15 minutes this week?"

---

## APOLLO LEAD PULL — Status & Instructions

**Status:** Apollo.io API returned an error during initial test. The API key (aKRZyBffyV7ScWVCuTXBjA) may need:
- Account verification or plan upgrade at apollo.io
- Different endpoint parameters
- Or use of the UI (app.apollo.io) to pull manually

**When you can pull from Apollo, use these parameters:**

### Pull 1: Cuyahoga County Property Managers
```json
POST https://api.apollo.io/v1/mixed_people/search
Headers: X-Api-Key: aKRZyBffyV7ScWVCuTXBjA

{
  "person_titles": [
    "property manager",
    "facility manager",
    "community manager",
    "HOA manager",
    "building manager",
    "property management director"
  ],
  "person_locations": ["Cuyahoga County, Ohio", "Cleveland, Ohio"],
  "per_page": 50
}
```

### Pull 2: Lake + Lorain Counties
```json
{
  "person_titles": ["property manager", "facility manager", "HOA manager"],
  "person_locations": ["Lake County, Ohio", "Lorain County, Ohio", "Mentor, Ohio", "Elyria, Ohio"],
  "per_page": 50
}
```

### Pull 3: Summit + Medina Counties
```json
{
  "person_titles": ["property manager", "facility manager"],
  "person_locations": ["Summit County, Ohio", "Medina County, Ohio", "Akron, Ohio"],
  "per_page": 50
}
```

**Manual alternative:** Go to app.apollo.io → Search → filter by title + location → export CSV. Same contacts, different method.

---

## Sample Lead Record Format (for when list is pulled)

| First Name | Last Name | Title | Company | Email | Phone | City | County | Properties (est.) |
|-----------|-----------|-------|---------|-------|-------|------|--------|-------------------|
| [PENDING APOLLO PULL] | | | | | | | | |

---

*Danny Malone | Forest City Power Washing | 2026-05-12*
