# Facebook Ads — First Week Monitoring Guide
### Rick Santoro | Paid Ads Specialist
*2026-05-23 — For use starting Tuesday May 26 when ads launch*

---

## The Most Important Thing to Know Before You Launch

Facebook's algorithm needs 50 conversion events before it exits the "learning phase." For a small local business with a $15–$30/day budget, this takes about 7–14 days. **Do not make significant changes during this period.** Every edit resets the learning counter.

Your job week 1 is to **let it run, watch the right numbers, and resist the urge to kill ads that look slow on day 1.**

---

## Day 1 (Tuesday May 26 — Launch Day)

**What to do:**
- Launch all 3 campaigns (Awareness, Lead Gen, Retargeting) per the campaign structure in `outputs/rick/facebook_ads_peak_season_2026-05-20.md`
- Set up lead notifications (see below)
- Screenshot your starting dashboards (baseline for comparison)

**What to expect:**
- Spend will be low (Facebook is calibrating delivery)
- Impressions will be low
- 0 leads is normal on day 1
- Don't touch anything

**Lead notification setup (do this NOW — before ads launch):**
1. Facebook Ads Manager → hamburger menu → "Notifications"
2. Turn on "Lead form submission notifications" → Email + push
3. Also: in Meta Business Suite, set your "Response time goal" to Under 5 minutes
4. Test: submit your own lead form via the ad preview to confirm the notification fires

---

## Day 3 (Thursday May 28 — First Real Check)

**What to check:**
Go to Ads Manager → select your Lead Gen campaign → look at these 3 metrics:

| Metric | Good | Investigate if |
|--------|------|----------------|
| **Link Click-Through Rate (CTR)** | > 1.5% | < 0.8% |
| **Cost Per Link Click** | < $1.50 | > $3.00 |
| **CPL (Cost Per Lead)** | < $25 | > $50 |
| **Leads** | 1–3 | 0 (check form works) |

**If CTR < 0.8%:** The hook isn't working. Test a different primary text — the first line of the ad. Don't change the image yet.

**If CPL > $50:** Normal for day 3. Don't act yet. Check again day 7.

**If 0 leads after 3 days AND $30+ spent:** Submit a test lead yourself. If you don't get a notification, your form is broken. Check Meta Forms → preview → submit.

**What NOT to do on day 3:**
- Don't change the ad creative
- Don't change the audience
- Don't pause anything
- Don't increase budget yet

---

## Day 7 (Tuesday June 2 — First Optimization)

**What to check:**
Compare each ad variation's performance. Facebook should have started favoring the higher-performing ones.

**Action thresholds:**

| Situation | Action |
|-----------|--------|
| 0 leads after $50 spent | Duplicate the ad, change the opening hook line only |
| 1–2 leads but CPL > $40 | Test a different audience — try "Homeowners 35–55" vs "Home Improvement interest" |
| 3+ leads, CPL < $35 | ✅ Let it run. Do not touch. |
| 1+ booked job from ads | Scale budget by 20% ($30 → $36/day). Not more. |
| 0 responses from leads | See response protocol below — the problem is follow-up, not the ads |

**Week 1 metrics benchmark (Cleveland-area home services):**
- Target CPL (cost per lead): $15–$35
- Target close rate on ad leads: 30–50% (Google Guaranteed leads close higher)
- Expected bookings in week 1 at $15/day: 1–3 jobs
- Break-even: 1 booked house wash ($249–$399 job) covers 1–2 weeks of ad spend

---

## Lead Response Protocol (Critical — Do Not Skip)

**The #1 mistake that kills Facebook ad ROI: slow follow-up.**

Facebook ad leads are often comparison shopping. If you respond in 30 minutes and a competitor responds in 5, they book the competitor.

**The rule: every lead gets a text within 5 minutes.**

When a lead form comes in (you'll get a notification):
1. **Text them immediately (within 5 min):** "Hey [Name], this is Bradley from Forest City Power Washing — I saw you were interested in a quote. What's the address? I can get you a number today." Use a first name if available.
2. **If no text response in 30 min:** Call them. 
3. **If they don't answer:** Leave a voicemail, then text: "Just tried calling — let me know a good time to chat or I can just send you a quote by text if you share the address."
4. **If no response after 24h:** One more text: "Hey — still happy to get you a quote. No pressure. Text me the address and I can usually send something same day."

**Full response scripts in:** `outputs/rick/google_guaranteed_lead_response_sop_2026-05-23.md` (written for Google Guaranteed but the call/text scripts work for Facebook leads too)

---

## Budget Scaling Guide

Start at $15/day. Don't jump to $50/day on week 1 — you'll burn budget before Facebook knows who to target.

| Trigger | Action |
|---------|--------|
| 1 booked job from ads | Increase to $20/day |
| 3 booked jobs from ads | Increase to $30/day |
| 5+ booked jobs from ads | Increase to $50/day + turn on Retargeting campaign |
| CPL > $50 after 2 weeks | Pause lowest-performing ad, test new creative |

---

## What Will Confuse You (And What It Means)

**"Reach is low on day 1"** — Normal. Algorithm is calibrating. Reach grows over 48–72 hours.

**"I'm getting clicks but no leads"** — Your lead form is the bottleneck. Check that it auto-fills name/email/phone (it should — Facebook pulls from their profile). Fewer fields = more completions.

**"It's showing to people outside my area"** — Check your geo targeting. Should be set to each of the 7 NE Ohio counties with a 15-mile radius. If it's set to "United States" you have an audience problem.

**"Someone submitted but their info looks fake"** — Facebook lead quality varies. Use the Lead Gen form feature "Higher Intent" (asks users to review their info before submitting) — this cuts fake leads by ~40%.

**"CPL is $8 — is that too good to be true?"** — Maybe. Check if those leads are converting to quotes. A $8 CPL that never books is worse than a $30 CPL with a 50% booking rate.

**"The ad is running but I can't find it on Facebook"** — That's normal. You won't always see your own ad. Check Active status in Ads Manager.

---

## Weekly Check-in Schedule (First Month)

- **Tuesday:** Review prior week metrics. One optimization decision only.
- **Thursday:** Respond to any outstanding leads from the week.
- **Every 2 weeks:** Post a new before/after photo as an ad creative variation (Jasmine has the capture protocol).

---

## Files Referenced
- Campaign structure + ad copy: `outputs/rick/facebook_ads_peak_season_2026-05-20.md`
- Google Ads setup: `outputs/rick/google_ads_june_2026-05-19.md`
- Lead response scripts: `outputs/rick/google_guaranteed_lead_response_sop_2026-05-23.md`
- Before/after photo pipeline: `outputs/jasmine/before_after_photo_capture_protocol_2026-05-23.md`
- Annual plan upsell (for every booked job): `outputs/tommy/annual_plan_upsell_sequence_2026-05-23.md`

---

*Rick Santoro | Paid Ads Specialist | Forest City Power Washing | Generated 2026-05-23*
