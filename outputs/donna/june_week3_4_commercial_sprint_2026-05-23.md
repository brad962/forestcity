# June Week 3–4 Commercial Sprint
### June 16–30, 2026 | Day-by-Day Action Plan
*Donna Park | Growth & Launch Strategist*

---

## Context (Where We'll Be)

By June 16, if the prior weeks went to plan:
- Round 2 PM sequence (June 4–11) has produced 2–8 replies
- Gas station sequence has been running for ~2 weeks
- Google Ads + Facebook Ads launched (May 26–June 3)
- Summit + Medina + Geauga/Portage county pulls complete
- First booked commercial jobs may already be in Workiz

Week 3–4 is the harvest + amplify phase. You're converting the pipeline, upselling the annual plan, and doubling down on what's working.

---

## Week 3: June 16–20 (Geauga + Portage Follow-Up + First Conversions)

### Monday June 16

**8:00am — Weekly Pipeline Check (10 min)**
```
python3 workers/nina_report.py weekly
python3 workers/check_replies.py
```
Target: 3+ replies in the system by now. If 0, go to escalation protocol.

**8:30am — Geauga + Portage County Pull (5 min)**
```
python3 workers/lead_pipeline.py danny Geauga+Portage
```
This is Week 23 in the rotation (June 16 = ISO Week 24, targets Lake County via standard rotation, but Geauga+Portage may need a manual override depending on exact date — verify: `python3 -c "from datetime import datetime; print(datetime.now().isocalendar()[1] % 6)"`)

**9:00am — Round 2 Reply Follow-Up (30 min)**
- For anyone who replied in Round 2 but hasn't booked: send quote within 24 hours
- Script: treat it like a warm inbound — call first, email second
- For no-reply hot leads (2+ opens): send LinkedIn DM using the connection context

**10:00am — Contractor Referral Wave 2 (20 min)**
- Pick 3 contractors from Carla's pipeline who were contacted in May but haven't replied
- Use the trade-specific revival texts: `outputs/carla/june_referral_revival_texts_2026-05-23.md`
- New angle for Wave 2: "We just did 3 jobs in [their service area]. Have any clients who need exterior cleaning?"

---

### Tuesday June 17

**8:00am — Ad Performance Check (10 min)**
- Google Ads: log in → check CTR + conversion rate. Kill any ad group with >50 clicks and 0 conversions.
- Facebook Ads: check cost per lead. Target ≤$35/lead. If >$50, pause lead gen campaign and double spend on retargeting.

**9:00am — Annual Plan Upsell — First Attempt (20 min)**
- For any jobs completed in May or June so far, send the annual plan upsell text
- Template: "Hey [name], Bradley here from Forest City. Really glad we got to do the [service] for you last week. We just started our Annual Plan for next year — spring wash + fall touchup for $[price]. Only a few slots left in [their area]. Want me to lock yours in?"
- This is the highest-margin sale in the whole business model. One annual plan = $400–$600/yr guaranteed.

---

### Wednesday June 18

**All-day: Commercial Job Blitz**
If any commercial prospects are in "Quote Sent" or "Follow-Up" stage in pipeline_data.json, today is the follow-up day. Rule: if they've had a quote for 7+ days, send a personal text. Not email — text.

Script: "Hey [first name], just checking in on the quote I sent for [property]. We have availability in [your area] the week of June 22 — wanted to make sure you got it."

---

### Thursday June 19

**9:00am — Google Business Profile Update (10 min)**
- Post 1 job photo from the week with a short caption
- Ask the completed job client for a Google review (text or in-person QR code handoff)
- Protocol: `outputs/vera/gbp_weekly_routine_2026-05-21.md`

**10:00am — LinkedIn Post (5 min to schedule)**
- Post from the May 26–30 batch or write a fresh one: "3 commercial properties cleaned in [county] this week. Property managers — here's what 6 months of algae looks like vs. 2 hours of soft washing."

---

### Friday June 20

**8:00am — Week 3 Metrics Review**
Track in pipeline_data.json or note manually:
- Replies received (target: 5+)
- Quotes sent (target: 3+)
- Jobs booked (target: 1–2 commercial, 3–5 residential)
- Annual plan upsells pitched

**Weekend**: Zero required tasks. Optional: one Facebook group post or Nextdoor post for residential leads.

---

## Week 4: June 23–30 (Closing + Summer Setup)

### Monday June 23

**8:00am — Final Push Pipeline Check**
```
python3 workers/nina_report.py weekly
```
Goal by June 23: 8+ total replies across all sequences since May 22.

**Cuyahoga County Pull (June 23 = Week 25 rotation)**
```
python3 workers/lead_pipeline.py danny
```
Cuyahoga is your highest-density county. This pull seeds the July pipeline.

---

### Tuesday June 24

**Annual Plan Upsell — Wave 2 (30 min)**
- Every completed job from June gets the annual plan pitch today
- Follow up on any Wave 1 pitches that didn't respond
- Target: 3 annual plans locked in by June 30

---

### Wednesday June 25

**Facebook Ads — Midpoint Optimization (15 min)**
- Review cost per lead vs. booking rate
- Shift budget to best-performing ad and best-performing audience
- Turn off any ad with >100 clicks and <2 leads

**Hot Lead LinkedIn Re-Engagement (20 min)**
For any PM or contractor contact in the sequences with 3+ opens who STILL hasn't replied:
- Send connection request if not connected
- Follow up DM if connected: "Hey [first name], I saw you checked out what I sent — any questions about how we handle commercial properties in [county]?"

---

### Thursday June 26

**Realtor Summer Push (20 min)**
Summer listing surge is at peak. Realtors in Carla's pipeline who were contacted in May may now have active listings that need to look great.
Text script: "Hey [first name], it's [Bradley] from Forest City. Busy listing season — any homes coming up that need a power wash before photos? We're booking into July now and can usually turn around in 3–5 days."

---

### Friday June 27

**Month-End Commercial Pipeline Review**
- Count: total commercial replies, quotes sent, jobs booked in June
- Identify: which county produced the best leads?
- Identify: which sequence had the best reply rate?
- Decide: is Round 3 enrollment (July) worth running against same segments, or do we need to refresh the list?

**End-of-Month Report Prep (Nina runs this Monday July 1)**
```
python3 workers/nina_report.py weekly
python3 workers/workiz_report.py daily
```

---

## June Week 3–4 Revenue Targets

| Revenue Source | Conservative | Target |
|----------------|-------------|--------|
| Commercial reply conversions (2–4 booked) | $1,200 | $3,200 |
| Residential Facebook/Google ads (10–20 leads) | $2,400 | $4,800 |
| Annual plan upsells (2–4 closed) | $800 | $1,600 |
| Gas station accounts (1–2 sites) | $600 | $2,400 |
| Contractor referrals (1–3 jobs) | $600 | $1,800 |
| **Total June Week 3–4** | **$5,600** | **$13,800** |

---

## Critical Dependencies (What Must Happen in Weeks 1–2 for This to Work)

| Dependency | Status |
|-----------|--------|
| Instantly.ai paused before Round 2 | ☐ — must happen by June 1 |
| Round 2 PM emails sent with new copy | ☐ — June 4 |
| Gas station sequence live | ☐ — June 4 |
| Facebook + Google Ads running | ☐ — May 26 |
| Bridge emails sent to top 5 hot leads | ☐ — May 26 |

---

## Files Referenced

| File | Purpose |
|------|---------|
| `outputs/donna/round2_enrollment_readiness_checklist_2026-05-23.md` | June 3 GO/NO-GO checklist |
| `outputs/donna/june_week1_sprint_2026-05-20.md` | Week 1 reference |
| `outputs/donna/june_week2_sprint_2026-05-22.md` | Week 2 reference |
| `outputs/carla/june_referral_revival_texts_2026-05-23.md` | Trade-specific revival texts |
| `outputs/vera/gbp_weekly_routine_2026-05-21.md` | GBP posting protocol |
| `outputs/donna/past_customer_reengagement_launch_2026-05-21.md` | Annual plan upsell + re-engagement |

---

*Created by Donna | 2026-05-23 | Part of the June Commercial Push series*
*Previous: week1 (June 2-6), week2 (June 9-13), commercial_calendar (May 26-June 18)*
