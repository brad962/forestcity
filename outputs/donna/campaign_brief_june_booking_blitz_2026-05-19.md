# June Booking Blitz — Campaign Brief
### Donna Park | Growth & Launch Strategist
**Campaign window:** June 1–30, 2026
**Brief written:** 2026-05-19
**Status:** READY TO EXECUTE

---

## Why June Is Make-or-Break

June is Forest City's highest-revenue month. Property managers finalize summer vendor rosters in June. Homeowners book before summer cookouts and family visits. Any leads not converted by June 20 will push to fall at best.

We are entering June with:
- 45 enrolled contacts in Mixmax, 0 replies
- 18 gas station contacts queued but unsequenced
- 39 manual contractor contacts still untouched
- Zero Google Business Profile activity
- Zero Facebook ads running
- 13 hot leads with 2+ opens sitting without a direct outreach

This campaign is a 30-day blitz to convert what's already in the pipeline AND open new revenue channels before the mid-summer slowdown.

---

## Campaign Goal

**Book 8–12 new commercial or residential jobs in June.**
- Commercial target: 3 property manager accounts or 1 HOA contract
- Contractor referrals: 5 active referral partners texted/emailed this month
- Residential: 5 jobs from Facebook/Nextdoor or past customer re-engagement

---

## Phase 1: Activate the Existing Pipeline (June 1–7)

Everything needed is already built. Bradley just needs to execute.

| Action | Asset | Owner |
|--------|-------|-------|
| Text 5 Tier 1 contractors | `outputs/vera/sms_templates_contractors_2026-05-18.md` | Bradley |
| Send bridge email to 3 hottest Mixmax contacts | `outputs/tommy/hot_lead_bridge_email_2026-05-19.md` | Bradley |
| Create gas station Mixmax sequence + paste ID | `integrations/mixmax.py` line 54 | Bradley |
| Run `python3 workers/lead_pipeline.py danny` locally | Enrolls PM leads — 7 days overdue | Bradley |
| Send past customer re-engagement text | `outputs/tommy/past_customer_reengagement_2026-05-18.md` | Bradley |

**Estimated result:** 2–5 replies, 1–2 estimates sent in week 1.

---

## Phase 2: Turn On Commercial Lead Flow (June 8–14)

The PM pipeline has been idle for 7+ days. One run of the cron catches up.

| Action | Expected Result |
|--------|----------------|
| Danny cron runs Monday 6/8: `lead_pipeline.py both` | 20–30 fresh PM + contractor leads pulled, enrolled in Mixmax |
| LinkedIn: 5 connects to hot leads (3 PM + 2 realtor opens) | Direct channel that bypasses sequence fatigue |
| Post 2 LinkedIn articles (commercial/PM audience) | 1 post done via Jasmine |

**Sequence performance check (Nina Monday 6/8 weekly report):**
- If open rate drops below 30% → refresh subject lines (Tommy)
- If still 0 replies after 45+ enrolled → approve sequence rewrite (Tommy wrote drafts)

---

## Phase 3: Residential Push (June 15–21)

Memorial Day set the intent. Now convert it to bookings.

| Channel | Action | Asset |
|---------|--------|-------|
| Facebook | Post 3x this week — before/after + seasonal hook | Jasmine posts queue |
| Facebook Ads | Turn on Rick's June ad set ($10/day to start) | `outputs/rick/facebook_ads_june_2026-05-18.md` |
| Nextdoor | Post in 2 NE Ohio neighborhood groups | `outputs/donna/nextdoor_post_template_2026-05-19.md` |
| Google Business Profile | Upload 3 before/after photos from May jobs | 5 minutes, zero cost |
| Review requests | Text every May job customer after completion | `outputs/tommy/review_request_sequence_2026-05-18.md` |

---

## Phase 4: Double Down on What's Working (June 22–30)

By June 22, we'll know which channels are producing. Double budget on what's converting.

- If Facebook ads are converting → scale to $25/day, add retargeting audience
- If contractor texts are producing referrals → text remaining Tier 2 list
- If PM sequence gets any replies → prioritize follow-up, get estimates out same day
- If Workiz shows 5+ jobs booked → turn on the Annual Plan upsell after each job

---

## Core Message (June Angle)

**Before the summer gets away from you.**

> "It's June in Northeast Ohio. You've got 90 days of peak season left. Your property needs to look sharp for guests, tenants, and summer inspections. We're booking out — let's get yours on the schedule while we still have slots."

**For property managers:**
> "Your residents are outside all summer. Let's make sure the property looks like it's being managed. One call, and we handle the rest."

**For contractors:**
> "If you're quoting siding or painting this month, you need us on the call. Clients ask about pressure washing. Now you have an answer and $50 for every referral that books."

---

## Assets Needed

| Asset | Owner | Status |
|-------|-------|--------|
| Facebook ad copy (June) | Rick | ✅ Written — `facebook_ads_june_2026-05-18.md` |
| Gas station email sequence | Danny | ✅ Written — `sequence_gas_stations_2026-05-19.md` |
| PM sequence rewrite (if 0 replies by 6/8) | Tommy | ✅ Written — needs approval |
| Bridge email to 3 hot contacts | Tommy | ✅ Written — `hot_lead_bridge_email_2026-05-19.md` |
| LinkedIn posts (commercial) | Jasmine | ✅ Active per updated agent file |
| Before/after Facebook posts | Jasmine | ✅ Queued |
| Nextdoor post | Donna | ✅ Written — `nextdoor_post_template_2026-05-19.md` |
| Review request text | Tommy | ✅ Written — `review_request_sequence_2026-05-18.md` |
| Past customer text | Tommy | ✅ Written — `past_customer_reengagement_2026-05-18.md` |

**Every asset needed for June is already written. The only bottleneck is execution.**

---

## Success Metrics

| Metric | Target by June 30 |
|--------|------------------|
| Mixmax replies | 5+ (currently 0) |
| Estimates sent | 3+ |
| Jobs booked | 8+ |
| Referral partner intros | 5 contractors texted, 2 active |
| Facebook ad reach | 5,000+ impressions |
| Google reviews | +3 new reviews |
| Gas station contacts enrolled | 18 |

---

## Weekly Checkpoints

- **Monday 6/1:** Nina weekly report — confirm PM sequence is active
- **Monday 6/8:** First Danny cron after gap — confirm 20+ new leads pulled
- **Monday 6/15:** Mid-month check — any replies? Estimate pipeline?
- **Monday 6/22:** Final push — convert what's warm, close the gaps
- **Monday 6/29:** June close — count booked jobs vs. goal

---

*Donna Park | Growth & Launch Strategist*
*Forest City Power Washing — June 2026 Commercial Push*
