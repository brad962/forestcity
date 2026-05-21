# Memorial Day Weekend — Monitoring & Follow-Up Guide
### May 22 (Touch 3 Day) → May 26 (Blitz Day)
*Tommy Greer | Content & Copy Writer — compiled for Bradley*

---

## Quick Reference: Which File to Open

| When | Action | File |
|------|--------|------|
| Thu May 22 — 8am | First reply check | `outputs/vera/touch3_morning_brief_2026-05-22.md` |
| Thu May 22 — each open | Real-time trigger | `outputs/tommy/touch3_open_trigger_protocol_2026-05-21.md` |
| Thu May 22 — reply received | Respond | `outputs/tommy/touch3_reply_response_templates_2026-05-20.md` |
| Thu May 22 — no replies by noon | Start calling | `outputs/tommy/hot_lead_phone_script_2026-05-22.md` |
| Thu May 22 — 6pm | Day wrap-up | `outputs/vera/touch3_evening_debrief_2026-05-22.md` |
| **Fri May 23 — 8am** | **Late reply check + calls** | **This file** |
| Sat–Mon May 24–26 | Passive monitoring | **This file** |
| Tue May 26 — 9am | Full blitz | `outputs/donna/may26_outreach_blitz_brief_2026-05-20.md` |

---

## FRIDAY, MAY 23 — Morning Actions (45 min)

### 1. Late Reply Check (5 min)
Open Mixmax → Sequences → check all 3 sequences for:
- New replies since yesterday
- New openers (Touch 3 may fire throughout the day on May 22 — opens trickle in)

If you got a late opener Thursday night or early Friday: **connect on LinkedIn NOW** (business hours end at noon Friday before a long weekend).

### 2. Phone Calls — Priority List (30 min)
**Friday morning calls land better than voicemails.** Many PMs are wrapping up before the long weekend — they're at their desks.

Call the top 5 from the hot leads list (2+ opens, no reply):
- Script: `outputs/tommy/hot_lead_phone_script_2026-05-22.md`
- Goal: Get a verbal "yes, send me a quote" before the weekend
- If you get a verbal yes → send the quote EMAIL before noon Friday so they can think over the weekend

### 3. Send Quotes (before noon Friday)
If anyone said "yes, what do you charge?" on May 22 or 23:
- Kit: `outputs/tommy/quote_to_close_kit_2026-05-20.md`
- Get the quote to them by noon — they'll think about it over the weekend and you'll be top of mind Tuesday
- Follow-up text: `outputs/tommy/quote_followup_sequence_2026-05-20.md` (Touch 1 = text 24h after quote → sends Monday morning automatically if you schedule it)

### 4. Update Pipeline (5 min)
For anyone you called Friday: update `pipeline_data.json` via the dashboard or directly:
- Got quote request → stage: "Replied", notes: "Requested quote 5/23, sent quote 5/23"
- Left voicemail → stage: "Contacted", notes: "Left voicemail 5/23 — follow up 5/26"
- No answer → stage: "Contacted", notes: "Called 5/23, no answer — retry 5/26"

---

## SATURDAY MAY 24 — SUNDAY MAY 25 — Passive Mode

**Rule: Don't START new outreach. DO respond to anything inbound.**

### What to Watch For
- **Email replies** to Touch 3 (some PMs read email over the weekend): reply within 4 hours, even a short "Thanks — I'll send details Monday morning" keeps momentum
- **LinkedIn messages** from connects you sent Thursday: same — respond same day
- **Facebook DM or comment** from any organic post: respond within 1 hour (social platforms reward fast response with more reach)
- **Text replies** from contractor contacts: if a contractor says "yes, interested" on Sunday — reply immediately, don't wait until Monday

### What NOT to Do
- Don't call business numbers (voicemail goes to the abyss over a holiday)
- Don't send cold emails on Sat/Sun/Mon (looks bad, low deliverability)
- Don't add new contacts to Mixmax sequences over the weekend

### Optional: Organic Social (15 min either day)
Post one of Jasmine's pre-written Memorial Day posts:
- `outputs/jasmine/facebook_posts_memorial_day_week_2026-05-20.md`
- Best time: Saturday 10am or Monday 11am
- Organic content on holiday weekends gets strong reach (less competition, people scrolling)

---

## TUESDAY MAY 26 — BLITZ DAY

This is the highest-value workday of the week. Everyone is back at their desks after the holiday.

### 1. Start with: `outputs/donna/may26_outreach_blitz_brief_2026-05-20.md`
That document is the master plan for the day. Read it first — it covers:
- Follow-up order (warm leads → then cold)
- Contractor text follow-ups (Bulletproof Lawncare, Damrons, CLE Lawn Care Plus → all next_followup = 5/26)
- PM personal email (top 5 hot leads from round 2 framework)
- LinkedIn message to connected contacts (accepts from May 22-23)

### 2. Then: Update Pipeline + Enroll New Contacts
- Run `python3 workers/lead_pipeline.py danny` → pulls Summit County (week 21, 11+ days overdue)
- Once Summit leads are enrolled → they go straight into Touch 1 of the PM sequence
- Check `outputs/danny/round2_enrollment_plan_2026-05-20.md` for the June county rotation schedule

### 3. Revenue Check
- Open Workiz → check for any new jobs entered over the weekend
- Run `python3 workers/workiz_report.py daily` locally for the revenue snapshot
- Any jobs from over the weekend should be on the Slack report by 9:30am

---

## KEY METRICS — Track These Through the Weekend

| What | How to Check | Target by May 26 |
|------|-------------|-----------------|
| Touch 3 replies | Mixmax UI → Sequences | At least 1 |
| PM calls made May 23 | Your call log | 5+ calls |
| Verbal yeses for quotes | Notes | 2+ |
| Quotes sent | Gmail sent folder | 2+ |
| Contractor texts replied | Messages app | 1+ yes from Tier 1 |
| LinkedIn accepts | LinkedIn notifications | 3+ |

---

## If It's May 26 and Still 0 Replies from Touch 3

That's OK. It's not over. Here's the decision tree:

**Was the Reply-To address correct in Mixmax?**
- If NO (just discovered) → Run Round 2 with the SAME copy but correct Reply-To. People just couldn't respond.
- If YES → Run Round 2 with the REWRITTEN sequence. The copy needs refreshing.

See: `outputs/vera/round2_decision_framework_2026-05-20.md`

**Round 2 start date:** June 2 (after cooling period). `outputs/danny/round2_enrollment_plan_2026-05-20.md`

---

*Compiled by Tommy Greer | 2026-05-21 | Forest City Power Washing*
