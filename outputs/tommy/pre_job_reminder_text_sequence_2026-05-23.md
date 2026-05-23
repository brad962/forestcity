# Pre-Job Reminder Text Sequence
### Tommy Greer | Content & Copy Writer
*Forest City Power Washing — NE Ohio*
*Created: 2026-05-23*

---

## Why This Exists

No-shows kill a scheduled day. Industry average no-show rate for unreminded service appointments: 8–15%. Two texts — one the night before, one two hours out — drop that to under 2%.

Secondary win: soft wash jobs have a smell (the cleaning solution) and a 24-hour "stay off" window for the driveway. Customers who aren't warned get surprised. Customers who ARE warned feel cared for. Same outcome — totally different experience.

---

## Text 1 — Night Before (Send: 6–7pm the evening before the job)

### Version A — Standard
```
Hey [FirstName], it's Bradley from Forest City Power Washing. Just a heads up — we've got you on the schedule for tomorrow between [TimeWindow]. 

A couple quick things: we use a low-pressure soft wash on the siding and roof (safe for your surfaces, kills the algae at the root). There's a mild detergent smell that clears within a few hours. If you have any plants near the foundation, we'll rinse them down — they're fine.

No need to be home — just make sure we have access to the outside faucet. Any questions? Text or call me at this number.

See you tomorrow!
— Bradley, Forest City Power Washing
```

### Version B — Shorter (if job is driveway/concrete only — no soft wash)
```
Hey [FirstName], it's Bradley from Forest City Power Washing. Confirming we're on for tomorrow between [TimeWindow]. No need to be home — just car out of the driveway and we're good. Any questions, text me here. See you tomorrow!
```

### Version C — Big job (Showstopper / full house + roof)
```
Hey [FirstName], Bradley here from Forest City. Big day tomorrow — we have you down for [TimeWindow] for the full exterior clean. Heads up: the roof soft wash uses a biodegradable solution with a noticeable smell — totally normal, gone in 2–3 hours. Keep kids and pets off the treated surfaces for about an hour after we're done.

We'll be there ready to go. Access to an outdoor spigot is all we need. Questions? I'm here. Looking forward to it!
— Bradley
```

---

## Text 2 — Day-of Reminder (Send: 2 hours before crew arrives)

### Version A — Standard
```
Hey [FirstName], Forest City Power Washing heading your way — we'll be there around [ArrivalTime]. See you soon!
```

### Version B — If customer is NOT home
```
Hey [FirstName], Forest City is on our way — arriving around [ArrivalTime]. We'll get started and send you a message when we're done. Reach me here if anything comes up.
```

### Version C — If there was a weather delay or reschedule
```
Hey [FirstName], good news — weather held and we're on our way. Arriving around [ArrivalTime]. Thanks for your patience — excited to get this done for you.
```

---

## Post-Job Text (send within 30 min of finishing)

```
Hey [FirstName], we just finished up at [Address]. Looks great — come check it out when you get a chance.

One reminder: avoid walking on the driveway for about [30min/1hr] while it dries. Everything else is good to go.

If you have a second, a Google review means the world to us — it helps other homeowners find us: [Google Review Link]

Thanks again! — Bradley, Forest City Power Washing
```

---

## Response Handling

**If they ask to reschedule (night-before text):**
```
No problem at all — what works better for you? We have openings [next available days]. Just let me know and I'll get you locked in.
```

**If they say they won't be home:**
```
That's totally fine — we just need access to the outdoor spigot. We'll send a text when we're done so you know it's complete.
```

**If they ask about the soft wash smell:**
```
Totally normal — it's a biodegradable sodium hypochlorite solution (same thing in pool water, basically). The smell clears within 2–3 hours, and it actually kills the algae at the root instead of just washing it off. You won't see it come back for 12–18 months.
```

---

## Timing Guide

| Action | When |
|--------|------|
| Text 1 (night before) | 6:00–7:00 PM the evening before |
| Text 2 (day of) | 2 hours before scheduled arrival time |
| Post-job text | Within 30 minutes of job completion |
| Annual plan upsell text | Within 2 hours of job completion (see `annual_plan_upsell_sequence_2026-05-23.md`) |
| Review request follow-up | 24–48 hours after job if no review yet |

**Don't text before 8am or after 8pm.** If the job is early morning (7am start), send the night-before text at 6:30pm the previous evening — that's the last touch before an early job.

---

## Workiz Integration Note

When this is automated (pending Twilio setup), the [TimeWindow], [ArrivalTime], and [FirstName] fields pull directly from the Workiz job record. Until Twilio is connected, copy-paste these manually from Workiz before each job. Takes 90 seconds per job.

---

*Tommy Greer | Forest City Power Washing*
*File: `outputs/tommy/pre_job_reminder_text_sequence_2026-05-23.md`*
