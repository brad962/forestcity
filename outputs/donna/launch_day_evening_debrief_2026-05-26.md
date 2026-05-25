# Launch Day Evening Debrief — Tuesday May 26, 2026
*5-minute check at 5pm. Do this before closing the laptop.*
*Written by Vera Cole | Donna Park*

---

## Step 1: Did Ads Go Live? (2 min)

**Facebook Ads:**
- Go to Ads Manager (business.facebook.com/adsmanager)
- Status column:
  - ✅ **"Active"** — live and running
  - ⏳ **"In Review"** — normal; approves in a few hours or overnight; nothing to do
  - ❌ **"Error"** — check the specific error (usually billing or a policy issue on image/text)
- Normal Day 1 expectation: 500–2,000 impressions, possibly 0–3 leads (Facebook takes time to find the audience)

**Google Ads:**
- Go to ads.google.com → Campaigns
- Status column:
  - ✅ **"Eligible"** — approved; may or may not show impressions today
  - ⚠️ **"Limited"** — budget too low or billing issue; increase daily budget to $10+ minimum
  - ❌ **"Suspended"** — policy violation; check the alert
- Normal Day 1 expectation: **0 impressions is normal for Google on Day 1.** Google takes 24-48 hours to approve new ads AND build initial Quality Score. Check again Wednesday morning — if still 0 impressions by Wednesday afternoon, there's a real problem.

---

## Step 2: Did the Summit Pull Happen? (30 sec)

Check: `cat /Users/bradleyneal/forestcity/logs/activity.log | tail -20`
Look for a line like: `[2026-05-26 ...] Danny | Apollo pull — X new property managers in Summit`

**If it DID run:** ✅ Nothing to do.
**If it DIDN'T run:** Run it now — takes 5 minutes.
```
python3 /Users/bradleyneal/forestcity/workers/lead_pipeline.py danny Summit
```
Or double-click: `scripts/run_summit_pull.command` in Finder.

Deadline: **May 31** (5 days). Don't skip — Round 2 enrollment June 4 needs fresh Summit leads.

---

## Step 3: Any Leads Come In? (1 min)

Check all three channels:
1. **Phone** — any missed calls or voicemails from unknown numbers?
2. **Facebook Lead Gen** — Ads Manager → Campaigns → Lead columns (if Campaign 2 is a Lead Gen type)
3. **Gmail** — any "power washing" or "quote request" subject lines?

**If a lead came in and you haven't called back yet:** Call NOW.
- Script: `outputs/rick/facebook_lead_response_sop_2026-05-24.md`
- Target response time: within 5 minutes for Facebook Lead Gen; within 60 minutes for everything else
- After the call: log in Workiz (JobType = "Power Washing") + send booking confirmation text (`outputs/tommy/booking_confirmation_text_2026-05-25.md`)

---

## Step 4: GBP Post 1 Published? (30 sec)

Check: business.google.com/dashboard → Posts tab → Is today's post showing?

If not: Copy Post 1 from `outputs/vera/launch_week_gbp_posts_2026-05-25.md` and publish now (2 min). It's the "Launch Day" hook post timed to coincide with ads going live.

---

## Step 5: Gas Station Emails Sent? (30 sec check)

Check Gmail → Sent folder → Any power washing emails to gas station contacts today?

**If sent (Wave 1, 7 contacts):** ✅ Wave 2 (11 contacts) goes Thursday May 28.
**If not sent yet:** Open `outputs/danny/gas_station_manual_email_blast_2026-05-25.md` — takes 20 minutes. Wave 1 can still go out tonight or first thing Wednesday.

---

## Step 6: Contractor Texts — Anthony & Others (30 sec check)

Check phone texts — Did Anthony/Land Pro (440-320-2779) get a text today?

**If yes:** ✅ Watch for reply tomorrow morning.
**If not:** Text tonight or first thing Wednesday morning (still valid). Scripts: `outputs/vera/memorial_day_contractor_text_card_2026-05-24.md`

---

## Step 7: Instantly.ai Pause (3 min — DO THIS TONIGHT IF NOT DONE)

Open `app.instantly.ai` → Campaigns → find `a1c08c3d` and `626cd15d` → ⋮ → Pause both

Then: add `INSTANTLY_PAUSED=true` to `.env`

Recovery math: **Pause tonight = 9 days recovery before June 4.** Every day not paused = one less day of deliverability recovery. If not paused by Friday May 29 = only 6 days = high spam risk on June 4.

---

## What Success Looks Like After Day 1

| Action | Success | Red Flag |
|--------|---------|----------|
| Facebook ads | Active or In Review | Error status |
| Google ads | Eligible (any status) | Suspended |
| Summit pull | Done in activity.log | Not done by May 27 |
| First lead | Called back within 5 min | Missed call, no callback |
| GBP Post 1 | Published | Not published |
| Instantly.ai | Paused + .env updated | Still running |

---

## Tomorrow (Wednesday May 27) — 3 Things

1. **Google Ads first look** — check impression count (should have data by now); if 0 impressions, follow Day 1 troubleshooting in `outputs/rick/google_ads_first_week_monitoring_guide_2026-05-24.md`
2. **Facebook first look** — check CPL (cost per lead); if leads are under $15 → scale budget; if $30+ → check hook performance
3. **GBP Post 2** — takes 2 min; copy from `outputs/vera/launch_week_gbp_posts_2026-05-25.md` Post 2

---

*Reference files:*
- *Launch brief: `outputs/donna/may26_final_launch_brief_2026-05-25.md`*
- *Day 3 Google check: `outputs/rick/google_ads_first_week_monitoring_guide_2026-05-24.md`*
- *Revenue tracker: `outputs/rick/facebook_ad_week1_revenue_tracker_2026-05-24.md`*
- *GBP posts: `outputs/vera/launch_week_gbp_posts_2026-05-25.md`*
- *Booking confirmation: `outputs/tommy/booking_confirmation_text_2026-05-25.md`*

*Generated: 2026-05-25 | Vera Cole, Chief Innovation Officer*
