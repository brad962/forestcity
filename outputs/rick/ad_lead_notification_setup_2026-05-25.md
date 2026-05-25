# Ad Lead Notification Setup — Real-Time Alerts
### Rick Santoro | Paid Ads Specialist | 2026-05-25

> **WHY THIS MATTERS:** Facebook reports that leads contacted within 5 minutes convert at 9× the rate of leads contacted after 30 minutes. A lead form submission that sits for 3 hours is a dead lead. This guide makes sure Bradley's phone buzzes the moment a lead comes in — whether he's on a job, driving, or in Ads Manager.

---

## PART 1 — Facebook Lead Gen Notifications

### Step 1: Turn On Instant Email Notification (2 min)
1. Go to business.facebook.com → your Page
2. Click **Inbox** (top nav)
3. Click the ⚙️ **Settings** gear → **Notifications**
4. Under "Leads," set: **Email notifications** → ON
5. Set frequency: **Immediately**
6. Confirm your email matches where your phone receives email

> ✅ Every form submission now sends an email to your inbox. If email is linked to your phone, you get a push notification.

### Step 2: Facebook Business Suite App (iPhone/Android) — push notification
1. Download **Facebook Business Suite** from the App Store (free)
2. Log in → tap ☰ → **Notifications**
3. Enable: **Lead ads** → ON
4. Enable: **All notifications** (important: not just "highlights")
5. Make sure iOS/Android notification permission is allowed for the app

> ✅ You'll get a push notification within 60 seconds of any form submission.

### Step 3: Set Up Leads Access on Zapier (optional, 5 min, free tier)
If you want a text message instead of a push notification:
1. zapier.com → Create Zap
2. Trigger: **Facebook Lead Ads** → "New Lead"
3. Action: **Gmail** → "Send Email to myself" (or **Twilio** → "Send SMS" if you have it)
4. Test the Zap with a test lead submission
5. Turn Zap ON

> ✅ You get a text or email with the lead's name, phone, and email within 90 seconds.

### Step 4: Daily Lead Check Inside Ads Manager
Even with notifications on, do a manual check at these times:
- **8:00am** — first thing, before calls
- **12:00pm** — after any morning jobs
- **5:00pm** — end of day

Go to: business.facebook.com → **All tools** → **Ads Manager** → Campaign → Ad Set → Ad → **Lead Forms** → **Download leads CSV**

Or use the shortcut: Your Facebook Page → **Publishing Tools** → **Lead Ad Forms** → See all leads

---

## PART 2 — Google Ads Lead Notifications

### Step 1: Google Ads Call Extensions — Forwarding Number
When your Google Ads call extension rings, it goes through a Google forwarding number so Google can track it. You'll know it's a Google Ads lead because:
- Caller ID shows your forwarding number (starts with the same area code)
- Google Ads → Reports → Calls tab shows the call 15 min after it ends

No setup needed — just answer every call during business hours.

### Step 2: Google Ads Conversion Email Alerts
1. Sign in to ads.google.com
2. Tools → **Notifications** → **Email preferences**
3. Check: **Conversions** → Notify me when a conversion occurs
4. Frequency: **As they happen**

> ✅ Every completed Google Ads call conversion (>60 seconds) sends an alert.

### Step 3: Google Ads iOS/Android App
1. Download **Google Ads** app
2. Log in → tap the 🔔 bell → **Notification settings**
3. Enable: **Campaign alerts** + **Conversion alerts**

---

## PART 3 — First Response Protocol (When a Lead Comes In)

**Target: Call within 5 minutes. Text within 15 minutes if no answer.**

| Lead Type | How You Know | First Step |
|-----------|-------------|------------|
| Facebook Lead Gen | Phone push notification (Business Suite app) | Call the number in the form immediately |
| Google Ads call | Your phone rings directly | Answer and run `facebook_lead_response_sop_2026-05-24.md` call script |
| Google Ads form fill | Email alert from Google | Call the number in the conversion report |
| Organic Facebook DM | Facebook notification | Reply within 5 min with a quote request link |

**First 60 seconds on the call:**
> "Hey [Name], this is Bradley with Forest City Power Washing — I just saw your quote request come through. Do you have 2 minutes? I can give you a rough number right now."

**If they don't answer:**
> Text within 10 minutes: "Hey [Name], Bradley from Forest City Power Washing. I just missed your call — I can get you a free quote fast. What address are we looking at? —Bradley 📞"

---

## PART 4 — Lead Log (Fill Every Lead In)

Every ad lead gets logged immediately in `outputs/donna/launch_week_lead_log_2026-05-26.md`:
- Date | Source (FB/Google) | Name | Phone | Response Time | Quoted Y/N | Booked Y/N | Revenue

This is the only ground-truth record of whether ads are actually working. Ads Manager tracks clicks — this tracks jobs.

---

## SETUP CHECKLIST (Before Launch Day)

- [ ] Facebook Business Suite app downloaded and notifications ON
- [ ] Facebook Business email notification set to **Immediately**
- [ ] Google Ads app downloaded and conversion alerts ON
- [ ] Test: Submit a test lead using Facebook's test lead tool (Leads Ads Testing Tool in Meta for Developers — free) to confirm you receive the notification
- [ ] `launch_week_lead_log_2026-05-26.md` open on your phone for quick fill-in

---

*Rick Santoro — Paid Ads Specialist | Forest City Power Washing*
*Setup time: 15 minutes | Response time impact: 9× higher conversion rate*
