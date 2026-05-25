# Google Ads Conversion Tracking Setup
### Before Launch — May 26, 2026
*Rick Santoro | Paid Ads Specialist*

> ⚠️ **DO THIS BEFORE LAUNCHING ADS.** Without conversion tracking, Google Ads optimizes toward clicks — not bookings. Quality Score can't form correctly without conversion signals. You'll spend $30/day blind. This takes 20 minutes.

---

## Why This Matters

Google Ads bidding works on signals. Without conversions:
- Smart bidding (Target CPA, Maximize Conversions) has nothing to optimize toward
- You can't calculate true cost per lead or cost per booking
- Quality Score stays low = higher CPC than competitors who have it set up
- You have no idea which keywords, ads, or audiences are actually driving calls

With conversion tracking:
- Google learns which clicks turn into calls/form-fills → bids more on those
- CPL drops 20-40% over the first 30 days as the algorithm learns
- You know exactly which campaign → which ad → which keyword drove each booking

---

## What to Track (3 Conversion Actions)

### 1. Phone Calls From Ads
When someone clicks the phone number in your ad on mobile → counts as a conversion.
Threshold: Calls ≥ 60 seconds (filters out wrong numbers).

### 2. Phone Calls From Website
When someone clicks the phone number on your website after arriving via a Google Ad.
Requires Google Tag on your site.

### 3. Form Submissions (If You Have a Contact Form)
If your website has a quote request form, track the thank-you page visit as a conversion.

---

## Step-by-Step Setup

### STEP 1: Install Google Tag on Your Website (5 min)
*(Skip if you already have Google Analytics 4 on your site)*

1. Go to **ads.google.com** → Tools & Settings (⚙️ top right) → **Tag Manager**
2. Or go directly to: Tools → **Measurement** → **Google Tag**
3. Copy the Google tag code snippet
4. Paste it into the `<head>` section of every page on your website
   - If on Squarespace/Wix/Shopify: use their "Custom Code / Header" section
   - If on WordPress: use a plugin like "Insert Headers and Footers"

### STEP 2: Set Up Phone Call Conversions From Ads (5 min)

1. **ads.google.com** → Tools & Settings → **Measurement** → **Conversions**
2. Click **+ New conversion action**
3. Choose: **Phone calls** → **Calls from ads using call extensions or call-only ads**
4. Settings:
   - Conversion name: `Calls from ads`
   - Value: Leave blank (or enter your average job value ~$350)
   - Count: **One** (1 call per customer visit)
   - Click-through conversion window: **30 days**
   - Call length: **60 seconds** ← minimum to count (filters hangups)
   - Attribution model: **Data-driven** (or Last click if new account)
5. Click **Save and continue** → **Done**

This auto-creates a Google forwarding number that replaces your number in ads — tracks which clicks turned into calls automatically. Zero website changes needed.

### STEP 3: Set Up Phone Call Conversions From Website (5 min)
*(Requires Google Tag installed from Step 1)*

1. **Conversions** → **+ New conversion action**
2. Choose: **Phone calls** → **Clicks on your number on your website**
3. Settings:
   - Conversion name: `Website phone clicks`
   - Call length: **60 seconds**
   - Count: **One**
4. Google gives you a small code snippet to wrap around your phone number link
   - Your phone link currently: `<a href="tel:+1XXXXXXXXXX">Call us</a>`
   - Becomes: `<a href="tel:+1XXXXXXXXXX" onclick="gtag('event', 'conversion', ...)">Call us</a>`
   - Copy the exact snippet Google gives you and paste it around your phone link

### STEP 4: Set Up Form Submission Conversion (if applicable, 5 min)
*(Only if your website has a quote request form)*

1. **Conversions** → **+ New conversion action**
2. Choose: **Website** → **Page view** (tracking the thank-you page)
3. Settings:
   - Conversion name: `Quote form submitted`
   - Value: leave blank or $350 (average job value)
   - Count: **One**
   - Conversion window: **30 days**
4. URL condition: **URL equals** `https://yoursite.com/thank-you` (or whatever your form redirect URL is)
5. Save → Install the tag (same Google Tag from Step 1 handles this automatically if installed)

---

## Quick Verification Checklist

Before launching, verify in Google Ads:

- [ ] Go to **Tools → Conversions** — you should see your 3 conversion actions listed
- [ ] Status shows **"Recording conversions"** (may say "Unverified" for 24-48h — normal)
- [ ] In your campaigns: go to **Columns** → add "Conversions" and "Cost per conversion" to your view
- [ ] In your ad extensions: confirm call extension is active and uses a Google forwarding number

---

## What Happens Day 1

- Google starts recording calls from ad clicks immediately
- The dashboard will show 0 conversions for the first 24-72 hours (normal — data processing delay)
- By Day 3: first conversions appear
- By Day 7: Smart Bidding has enough data to start optimizing (if you get 5+ conversions)

If using **Manual CPC** bidding (recommended for first 7 days per monitoring guide):
- Conversions still record even without Smart Bidding
- You switch to "Maximize Conversions" bidding after Day 7 once data is in

---

## Ongoing: What to Check Weekly

1. **Cost per conversion**: Target ≤ $50 for a NE Ohio power washing call. If higher, check which keywords are eating budget with no calls.
2. **Top converting keywords**: In Search Terms report — these are gold, add them as exact match
3. **Call duration report**: Calls < 60 seconds not counted. If you see lots of short calls, increase duration threshold or improve your number's visibility in ads.

---

## If You Don't Have a Website Yet

Without a website, you can still track:
- Phone calls from ads (Step 2 above — no website required)
- Skip Steps 1, 3, 4

For Facebook Lead Gen form leads: those are tracked directly in Facebook Ads Manager as "Leads" — no extra setup needed. Google Ads = separate tracking.

---

*Written by Rick Santoro | May 25, 2026*
*Read before launching: `outputs/rick/google_ads_first_week_monitoring_guide_2026-05-24.md`*
