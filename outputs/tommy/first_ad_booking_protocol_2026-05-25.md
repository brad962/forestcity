# First Ad Booking Protocol — When the First Ad Lead Books a Job
### Tommy Greer | Content & Copy Writer | 2026-05-25

> **This is a different moment than a regular booking.** The first job booked from a paid ad is a landmark — it validates the entire campaign, creates your first piece of ad-grade social proof, and sets the template for how every future ad lead gets handled. Do these 7 steps every time, but especially the first time.

---

## The 7-Step Protocol (Total time: ~12 minutes, spread across the day)

### Step 1 — Confirm and Log Immediately (2 min)
The moment they say YES to your quote:
1. Run `outputs/tommy/job_booking_confirmation_flow_2026-05-25.md` (all 5 steps — confirmation text, Workiz entry, pipeline update, annual plan pitch, canvass script print)
2. In `outputs/donna/launch_week_lead_log_2026-05-26.md` — mark Booked Y, fill in Revenue column
3. Note the **lead source** exactly: "Facebook Lead Gen - Ad Set: [your targeting name]" or "Google - Keyword: power washing cleveland"
   - This is your first cost-per-acquisition data point. Write it down while you have it.

**CPA math (fill in right now):**
- Total ad spend so far: $___
- Divided by jobs booked: 1
- = Cost per acquisition: $___
- Job value: $___
- ROI: positive if job value > CPA

---

### Step 2 — Before Photo Within 1 Hour of Arrival (2 min on site)
Before touching anything at the property:
- Take 3-4 photos: wide angle of front of house, close-up of worst algae/stain, driveway or roof if applicable
- Use the same spot you'll take the "after" photo from — consistency makes the before/after more dramatic
- File naming: `before_[date]_[street].jpg` (example: `before_2026-05-27_elm-st.jpg`)

**Lighting tip:** Overcast days are better than direct sun — no harsh shadows hiding the grime.

---

### Step 3 — After Photo Before Packing Up (2 min on site)
Before loading the truck:
- Same angles as before photos — exact same spot
- Step back a little further if in doubt — wider shot shows more of the transformation
- Take one dramatic close-up of the cleaned surface
- Immediately text or AirDrop before+after pair to your phone if shot on another device

**Don't leave the job without the after photos.** You can't go back.

---

### Step 4 — Pitch Annual Plan Before Leaving (1 min on site)
Use `outputs/tommy/annual_plan_pitch_script_2026-05-26.md`:
> "One more thing before I go — we do a spring visit and a pre-winter visit for a flat rate of $X. Locks in your price, nothing to remember, we just show up. A lot of customers do it. Want me to add you?"

If YES → note their email, send annual plan welcome kit `outputs/tommy/annual_plan_customer_welcome_kit_[date].md` tonight.

---

### Step 5 — Google Review Request Text (send within 2 hours of job completion)
Use `outputs/tommy/review_request_sequence_2026-05-18.md` or this template:

> "Hey [Name], it's Bradley from Forest City Power Washing — hope the place looks great! If you have 60 seconds, a Google review would mean a lot to us: [your Google review link]. Thanks for having us out. —Bradley"

**Why now matters:** Satisfaction peaks within 2 hours of service. After 48 hours, review rate drops by 70%.

**Your Google review link:** business.google.com → Get more reviews → Share review form → copy the link. Do this once, save it to your phone contacts as "Forest City Review Link."

---

### Step 6 — Post Before/After to Facebook + Instagram (15-30 min, can do evening)
This is the most valuable organic content you can post.

**Facebook caption template (customize for this job):**
```
Before vs. after — this one in [City/neighborhood] this week.

The owner said the algae had been building up for [X years] and they'd been putting it off. One visit and it's completely gone.

We serve all 7 counties of Northeast Ohio — house washing, roof soft wash, driveway, deck, and commercial.

📞 DM us or comment QUOTE to get on the schedule.

#ClevelandOhio #NortheastOhio #PowerWashing #CurbAppeal #ForestCityPowerWashing
```

**Steps:**
1. Add to `logs/photo_pairs.json` so Jasmine's flyer builder creates the composite image automatically (see `outputs/jasmine/before_after_photo_capture_protocol_[date].md` for the format)
2. Post composite to Facebook Page + Instagram Feed (same image works for both)
3. If you're in a local Facebook group covering that neighborhood (Nextdoor groups, "[City] OH Community" groups) — post there too with the neighborhood name in the caption

**If you don't have a before photo:** Post just the after + "We cleaned this today" — still valuable, just less dramatic.

---

### Step 7 — Update Pipeline and Track Source (2 min, can do evening)
In `pipeline_data.json`:
```json
{
  "first_name": "[Name]",
  "last_name": "[Last]",
  "company": "",
  "stage": "Closed Won",
  "lead_source": "Facebook Lead Gen - Ad",
  "last_contact": "2026-05-XX",
  "job_value": 000,
  "notes": "First ad lead. Job: house wash. Before/after posted."
}
```

In `outputs/donna/launch_week_lead_log_2026-05-26.md`:
- Fill in Booked Y, Revenue, Response Time
- Add a note if it was the first ad lead — this is your benchmark

---

## What This Job Does For You Going Forward

| Asset Created | How It's Used |
|---------------|---------------|
| Before/after photos | Best Facebook/Instagram content, 3× more engagement than any other post |
| Google review (if they write one) | Ranks you higher in "power washing [city]" searches |
| Annual plan customer (if they said yes) | $X recurring revenue next fall, zero acquisition cost |
| CPA data point | Tells you if ads are working before you've spent $500 |
| Social proof post | Goes into next Facebook ad cycle as testimonial creative |

---

## Quick Reference: Files to Have Open on Launch Week

| Task | File |
|------|------|
| Booking confirmation | `outputs/tommy/job_booking_confirmation_flow_2026-05-25.md` |
| Annual plan pitch | `outputs/tommy/annual_plan_pitch_script_2026-05-26.md` |
| Review request | `outputs/tommy/review_request_sequence_2026-05-18.md` |
| Lead log | `outputs/donna/launch_week_lead_log_2026-05-26.md` |
| Facebook post caption | Section 6 above (bookmark this file) |

---

*Tommy Greer — Content & Copy Writer | Forest City Power Washing*
*This protocol fires once per booked job from paid ads. The before/after photos are the highest-ROI 4 minutes you'll spend all week.*
