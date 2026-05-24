# June Week 2 Sprint — June 9–13
### Donna Park | Growth & Launch Strategist | 2026-05-24
*Assumes Week 1 (June 2–6) launched successfully: Medina pull done, Round 2 enrolled, ads live.*

---

## Week 2 Objective
Convert Round 2 pipeline warmth into booked quotes. Start Geauga+Portage county prep. Run first ad optimization pass. Keep contractor follow-up momentum.

Revenue target: **$3,200–$7,500** (Week 2 mix of Round 2 pipeline conversions + ad leads)

---

## MONDAY June 9 (90 min)

**8:00am — Pull Geauga + Portage leads (30 min)**
```bash
cd /Users/bradleyneal/forestcity
python3 workers/lead_pipeline.py danny "Geauga + Portage"
python3 workers/lead_pipeline.py carla "Geauga + Portage"
```
Expected: 15–30 new PM contacts, 8–12 new referral partners.

**8:30am — Nina weekly pipeline report (10 min)**
```bash
python3 workers/nina_report.py weekly
```
Check: How many Round 2 contacts opened? Any replies from June 4 enrollment? Hot leads to call.

**8:45am — Review Round 2 replies from last week (20 min)**
Read: `outputs/nina/hot_leads_[date].md`
- Anyone who replied → respond immediately (use `outputs/tommy/touch3_reply_response_templates_2026-05-20.md`)
- Anyone with 2+ opens + no reply → LinkedIn connect + personal email from Bradley's Gmail
- Use hot lead callback script if someone calls: `outputs/tommy/hot_lead_callback_script_2026-05-24.md`

**9:10am — Contractor follow-up Wave 2 (30 min)**
Referral partners who didn't reply to June 4 texts → different angle text this week.
Use: `outputs/tommy/contractor_referral_text_script_2026-05-23.md` (or similar in tommy outputs)
Focus: landscapers + HVAC first (highest referral volume in NE Ohio).

---

## TUESDAY June 10 (60 min)

**8:00am — Facebook ads Week 1 performance review (30 min)**
Fill in: `outputs/rick/facebook_ad_week1_revenue_tracker_2026-05-24.md`
Key thresholds to check:
- CTR < 0.8%? Swap to a different hook from `outputs/rick/facebook_ad_creative_voc_refresh_2026-05-24.md`
- CPL > $30? Tighten audience (add "homeowners" + remove renters signal)
- CPL < $20 and 3+ leads? Scale budget from $30/day → $45/day
- 0 leads after 5 days? Kill Campaign 2 (Lead Gen), keep Campaign 1 (Awareness only)

**8:30am — Google Ads Week 1 check (20 min)**
Fill in Day 7 column: `outputs/rick/google_ads_first_week_monitoring_guide_2026-05-24.md`
Check search terms report — add negatives for any irrelevant queries (pressure washing jobs, car washing, etc.)

**8:50am — Google Guaranteed status check (10 min)**
Filed Sunday May 24 or Tuesday May 26 → approval takes 7–14 days.
If still pending: no action. If approved: turn on immediately.

---

## WEDNESDAY June 11 (45 min)

**8:00am — GBP post (10 min)**
Post June Week 2 GBP update. Content: `outputs/vera/june_gbp_content_calendar_2026-05-24.md` (June 9 post)
Takes 2 minutes at business.google.com/dashboard. Free reach during peak search week.

**8:15am — Quote follow-up for any leads from Week 1 ads (20 min)**
Any leads from Facebook/Google that haven't booked → follow up with:
- Day 4 email from `outputs/tommy/quote_followup_sequence_2026-05-20.md`
- Text: "Hey [FirstName], just following up on the quote from Forest City. Any questions before you decide? Happy to chat."

**8:40am — Workiz report check (15 min)**
```bash
python3 workers/workiz_report.py daily
```
Revenue pacing for June. Any outstanding balances from June Week 1 jobs?

---

## THURSDAY June 12 (30 min)

**8:00am — Mixmax Round 2 check (20 min)**
```bash
python3 workers/check_replies.py
```
Day 8 post-enrollment — Touch 2 should be sending or sent.
Hot leads (2+ opens): LinkedIn connect + personal email within 24h.
Replies: respond same day, move to quote stage.

**8:20am — Enroll Geauga + Portage leads (10 min)**
```bash
python3 workers/lead_pipeline.py pending
```
Geauga+Portage contacts from Monday should now be verified and pending enrollment if any PENDING sequences went live.

---

## FRIDAY June 13 (30 min)

**8:00am — Week 2 review + Week 3 prep (30 min)**

Ask yourself:
1. How many ad leads this week? (Facebook + Google) Target: 3–8
2. How many quotes sent? Target: 2–5
3. How many jobs booked? Target: 1–3 from ads + 1–2 from outreach
4. Did any Round 2 Mixmax contacts reply? Target: 2–5
5. Did the Geauga+Portage pull run? (June 9) → enrollment ready for next week
6. Are any Tier 1 contractor texts still unanswered? → Try a different angle next week

**Revenue math check:**
- 2 booked ad jobs @ $200 avg = $400
- 1 PM referral job @ $350 = $350
- 1 contractor referral job @ $300 = $300
- 1 past customer rebooking @ $225 = $225
**Week 2 minimum viable target: $1,275 in new bookings**
**Week 2 stretch target: $3,000+ (5+ jobs from ads + pipeline)**

---

## Key Files to Reference This Week

| File | When to Use |
|------|------------|
| `outputs/rick/facebook_ad_week1_revenue_tracker_2026-05-24.md` | Tuesday ad review |
| `outputs/rick/google_ads_first_week_monitoring_guide_2026-05-24.md` | Tuesday Google check |
| `outputs/tommy/quote_followup_sequence_2026-05-20.md` | Wednesday lead follow-up |
| `outputs/tommy/hot_lead_callback_script_2026-05-24.md` | Any warm inbound call |
| `outputs/tommy/touch3_reply_response_templates_2026-05-20.md` | Any Mixmax reply |
| `outputs/vera/june_gbp_content_calendar_2026-05-24.md` | Wednesday GBP post |
| `outputs/nina/hot_leads_[date].md` | Monday pipeline review |

---

## What Comes Next (Week 3: June 16–20)
- Round 2 reply conversion: contacts who opened 3x+ with no reply → personal call attempt
- Upsell annual plan to any customers served in Week 1–2
- Annual plan upsell wave 1 (use `outputs/tommy/annual_plan_upsell_sequence_2026-05-24.md`)
- Ad optimization: any creative that's underperforming gets swapped
- Cuyahoga county pull prep (Week 24 = June 15)
- Full sprint: `outputs/donna/june_week3_4_commercial_sprint_2026-05-23.md`
