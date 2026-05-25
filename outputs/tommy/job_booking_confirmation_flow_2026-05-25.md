# When They Say YES — 5-Step Booking Flow
### Tommy Greer | Job Booking Confirmation Flow | 2026-05-25
*Do these 5 steps before the next call. Total time: under 5 minutes.*

---

## Step 1 — Send Booking Confirmation Text (0–2 min)

**Do this within 2 minutes of hanging up.**

Open `outputs/tommy/booking_confirmation_text_2026-05-25.md` → copy the Confirmation Text → send.

Template (copy-paste, fill in blanks):
> Hey [First Name], it's Bradley from Forest City Power Washing. You're booked! We'll be there [DATE] between [TIME WINDOW]. We'll text you the night before to confirm. Any questions, reply here. Looking forward to it!

If you quoted a specific service (roof, driveway, full exterior), add one line:
> "We'll be doing the [service] — takes about [X hours]. You don't need to be home."

---

## Step 2 — Enter Job in Workiz (1–2 min)

Open Workiz → New Job. Fill these 6 fields exactly:

| Field | What to enter |
|-------|---------------|
| **JobType** | "Power Washing" (exact spelling — must match for revenue report) |
| **Client** | Search name → Create if new |
| **Address** | Job site address |
| **Date/Time** | Scheduled date + arrival window |
| **Revenue** | Quoted price |
| **Status** | Scheduled |

Full guide: `outputs/nina/workiz_job_entry_sop_2026-05-26.md`

> ⚠️ If you type "power wash" or "house wash" instead of "Power Washing" the job won't appear in the revenue report.

---

## Step 3 — Update pipeline_data.json (30 sec)

If this lead came from **Facebook/Google ads**: add them to `pipeline_data.json` → see `outputs/nina/ad_lead_tracker_2026-05-25.md` for the copy-paste template.

If this lead is **already in pipeline_data.json** (contractor, PM, realtor): update their stage field:

```json
"stage": "Booked",
"last_contact": "2026-05-25",
"job_date": "YYYY-MM-DD",
"revenue": 000
```

This makes their status visible in Nina's weekly report.

---

## Step 4 — Pitch the Annual Plan (30 sec — if not already done)

After confirming the job but before hanging up, say this:
> "One more thing — we do a lot of annual plans where we come out twice a year, spring and fall. It locks in your price, keeps the house looking great, and takes it off your plate. A lot of our customers do it. Want me to put you on the list? I'll send you a quick overview."

**YES** → send `outputs/tommy/annual_plan_customer_welcome_kit_[date].md`
**How much?** → "Spring + fall, usually around $X–$Y depending on what we're doing each visit."
**Maybe later** → "No problem. I'll follow up after the first job."

Full script: `outputs/tommy/annual_plan_pitch_script_2026-05-26.md`

---

## Step 5 — Neighbor Canvass Prep (30 sec)

Before you drive to the job, save or print this:
`outputs/tommy/neighbor_canvass_script_2026-05-26.md`

On the day of the job:
- Knock on 3–4 neighboring doors before you leave the site
- Text 2–3 neighbors who didn't answer
- Post "just finished in [neighborhood]" to Facebook while you're still in the driveway

This is the highest-ROI activity of peak season. Zero ad spend, zero travel, and the trust signal of a freshly cleaned neighbor's house is right there on the street.

---

## Quick Reference

| Step | Time | Key File |
|------|------|----------|
| Confirmation text | 2 min | `booking_confirmation_text_2026-05-25.md` |
| Workiz entry | 2 min | `workiz_job_entry_sop_2026-05-26.md` |
| Pipeline update | 30 sec | `ad_lead_tracker_2026-05-25.md` or pipeline_data.json |
| Annual plan pitch | 30 sec | `annual_plan_pitch_script_2026-05-26.md` |
| Neighbor canvass prep | 30 sec | `neighbor_canvass_script_2026-05-26.md` |

**Total: under 5 minutes. Every step has a ready-to-use file. Don't skip Step 5 — neighbor canvassing during peak season pays for itself in hours.**
