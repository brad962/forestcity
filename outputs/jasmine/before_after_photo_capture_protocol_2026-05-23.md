# Before/After Photo Capture Protocol
### Jasmine Burke | Social Media Manager
*Forest City Power Washing — NE Ohio*
*Created: 2026-05-23*

---

## Why This Protocol Exists

Before/after content is the single highest-converting content format for exterior cleaning. It stops the scroll, requires zero copywriting, and builds trust instantly. The problem isn't that Forest City doesn't do great work — it's that the photos aren't being captured systematically at every job.

This protocol turns every job into a content opportunity. One 60-second photo routine per job = 3–5 new posts per week in peak season.

---

## The Capture Routine (60 Seconds Per Job)

### BEFORE — Take these before you touch anything

**4 required shots:**
1. **Wide shot** — standing back from the street or driveway end, full house in frame. This is your "before" anchor.
2. **Siding close-up** — pick the dirtiest section. Get close enough to see the algae/streaks. This is the gross shot — it converts.
3. **Roof shot** (if roof job) — from the street, tilt up to show the black streaks.
4. **Driveway/surface shot** (if driveway job) — stand at one end, shoot down the length. Shows tire marks, staining, oil spots.

**Save with filename:** `[date]_[city]_BEFORE_[1/2/3/4].jpg`
Example: `2026-05-23_strongsville_BEFORE_1.jpg`

---

### AFTER — Take the same shots from the same angles

Same 4 shots, same positions. The match is what makes the before/after powerful — your eye goes straight to the difference.

**Save with filename:** `[date]_[city]_AFTER_[1/2/3/4].jpg`
Example: `2026-05-23_strongsville_AFTER_1.jpg`

---

## Lighting Tips

- **Best light:** overcast days or early morning (diffused light, no harsh shadows)
- **Avoid:** shooting directly into the sun, or when half the surface is in shadow
- **For wet surfaces:** shoot immediately after washing (when wet = highest shine/contrast), or wait 20 minutes (once dried and clean, color contrast is cleaner)
- **Phone tip:** tap to focus on the surface, not the sky

---

## How to Log the Pair for Jasmine's Flyer Pipeline

Once photos are saved, add the pair to `logs/photo_pairs.json`:

```json
{
  "pairs": [
    {
      "id": "2026-05-23-strongsville-001",
      "before": "assets/photos/2026-05-23_strongsville_BEFORE_1.jpg",
      "after": "assets/photos/2026-05-23_strongsville_AFTER_1.jpg",
      "date": "2026-05-23",
      "description": "House washing in Strongsville — 3 years of algae on siding. Green/black streaks gone in 90 minutes.",
      "processed": false
    }
  ]
}
```

Then run `python3 workers/jasmine_flyer.py` and it will:
- Stitch the before/after side-by-side with the Forest City logo
- Push the flyer to GitHub
- Post it to Slack with a ready-to-copy Facebook post

**Photo storage location:** `assets/photos/` (create this folder if it doesn't exist)

---

## Facebook Caption Templates (pick one per job)

### Short version — works for any job
```
Before → After. [City], Ohio.

[One-line job description]

We serve the greater Cleveland area. DM us or comment QUOTE to book.

#ForestCityPowerWashing #ClevelandOhio #NortheastOhio #PowerWashing #CurbAppeal
```

### Version with the problem
```
This roof had [X] years of algae on it. Client in [City] called us and asked if it was repairable. 

Two hours later — you tell us.

Soft wash only. No pressure on the shingles. Safe for all roof types.

DM us or comment QUOTE to get on the schedule.

#ForestCityPowerWashing #RoofCleaning #ClevelandOhio #NortheastOhio #SoftWash
```

### Version with neighbor angle
```
We finished this one in [neighborhood/city] today and the neighbors literally stopped to watch.

Before: [one-line description of the before state]
After: this.

Slots this week still open. DM or comment QUOTE.

#PowerWashing #CurbAppeal #ForestCityPowerWashing #NortheastOhio
```

---

## Instagram Story Version (15-second format)

For Instagram Stories using the before/after:
- **Slide 1:** Before photo — add text overlay: "Would you believe this was someone's house in [City]?"
- **Slide 2:** After photo — add text overlay: "2 hours. Soft wash. Forest City Power Washing."
- **Slide 3:** Sticker: "Get a quote" → link to contact/booking page

---

## LinkedIn Version (for commercial audience)

For property manager / HOA audience — post the same before/after but frame it commercially:

```
Before/after from this week: commercial property wash in Northeast Ohio.

Property managers — this is what a single maintenance visit does to tenant perception. Clean exteriors mean lower vacancy, happier tenants, and fewer complaints about the building's condition.

We work with HOAs and property management companies across all 7 NE Ohio counties. One vendor, recurring maintenance, reliable schedule.

DM to discuss a service agreement.
```

---

## Weekly Target

| Volume | Goal |
|--------|------|
| Photos per job | 4 before + 4 after (takes 60 seconds) |
| Jobs per week (peak season) | Varies — capture ALL of them |
| Posts per week from before/after | 2–3 minimum |
| Post timing | Within 24–48 hours of job (while it's current) |

---

## What Doesn't Work (Avoid These)

- **Blurry close-ups** — if you can't see the stain, the contrast doesn't register
- **Photos taken at night or in bad light** — unusable for social
- **Only shooting the good parts** — the DIRTY before is the hook; don't sanitize it
- **Shooting from one angle but not the other** — both shots need to match for the transformation to land
- **Waiting a week to post** — freshness matters; post within 48 hours

---

## Automation Roadmap (pending approval)

When Bradley approves:
- Workiz job completion trigger → automated text to Bradley: "Job done at [address] — time to take the after photos"
- After photos uploaded to Dropbox/Google Drive → `jasmine_flyer.py` auto-picks them up
- Before/after flyer posted to Slack within 30 minutes of job completion
- Jasmine queues Facebook post for next morning

This is currently a manual protocol. The automation just removes the reminder step.

---

*Jasmine Burke | Forest City Power Washing*
*File: `outputs/jasmine/before_after_photo_capture_protocol_2026-05-23.md`*
