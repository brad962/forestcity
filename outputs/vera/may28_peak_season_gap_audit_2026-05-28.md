# Peak Season Gap Audit — May 28, 2026
### Vera Cole | Run 116 | Focus: What's Not Happening That Should Be

---

## The Revenue Gaps Right Now

### 1. 🔴 ZERO GOOGLE REVIEW REQUESTS BEING SENT

**What's happening:** Every completed job ends with the customer happy and that's it.
**What should happen:** Text every completed customer within 2 hours asking for a Google review.
**Why it matters:**
- Most NE Ohio power washing competitors: 25–50 reviews
- Google Maps algorithm favors businesses with more recent reviews (recency matters as much as count)
- Google Local Services Ads (LSAs) — which you applied for — rank by review count + response rate
- Getting to 100 reviews before competitors puts Forest City in a different category entirely

**5-review/week target = 100 new reviews by end of season = top local ranking by September**

**The text (copy this and save it in your phone notes):**
> "Hey [Name], Bradley here from Forest City Power Washing. Hope everything looks great today!
> If you have 30 seconds, would mean the world if you left us a quick Google review:
> [YOUR GOOGLE MAPS REVIEW LINK]  Thanks!"

**Get your review link:**
Google Maps → search "Forest City Power Washing" → click Reviews tab → "Get more reviews" button → copy the short link

---

### 2. 🔴 SUMMIT COUNTY PULL — 3 DAYS LEFT (Deadline: May 31)

**Status:** Summit County (Akron area) has NOT been pulled. Deadline is Sunday May 31.
**After May 31:** Summit doesn't rotate back until July 6. That's 6 weeks of missed leads during peak season.

**What Summit has that hasn't been pulled yet:**
- Akron metro property managers (large multifamily + commercial portfolio)
- NEW segments first time in rotation: restaurants, banks/credit unions, fitness centers, medical offices, distribution centers, universities, car dealerships, auto body shops, event venues
- Carla's contractor + realtor contacts in Summit area

**Command (6 min, runs unattended):**
```
cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py danny Summit
```
**Or:** Double-click `scripts/run_summit_pull.command` in Finder

---

### 3. 🟡 INSTANTLY.AI STILL NOT CONFIRMED PAUSED

**Status:** Two campaigns still not confirmed paused — a1c08c3d (PM Cuyahoga) + 626cd15d (Contractor Referral).
**Risk:** Round 2 enrollment starts June 4. Duplicate sends = spam filter = 0% reply rate again.
**Fix (3 min):** app.instantly.ai → Campaigns → ⋮ → Pause both → add `INSTANTLY_PAUSED=true` to .env

---

### 4. 🟡 GAS STATION SEQUENCE STILL PENDING

**Status:** 12 gas station contacts in pipeline waiting. Mixmax sequence ID = PENDING since May 19.
**Fix (30 min):** Create the sequence in Mixmax UI → paste ID into `integrations/mixmax.py` line ~54.
**Guide:** `outputs/danny/gas_station_sequence_create_now_2026-05-27.md`

---

### 5. 🟡 3 CONTRACTOR REFERRAL CONTACTS STALE — BRYAN 14+ DAYS

**Bryan / CLE Lawn Care Plus:** Last contact unknown. 14+ days no follow-up.
**Text now:**
> "Hey Bryan — sent you a couple notes about partnering on referrals. Quick offer: I'll do one of your client's properties free so you see what we do firsthand. If you like it, we set something up. Interested? — Bradley, Forest City"

---

### 6. 🟡 21 WAVE 2 CONTRACTOR FIRST-TOUCH TEXTS DUE TODAY (May 28)

**Status:** 16 new contractor contacts (New Lead stage) have NEVER been texted. Due today.
**Day 3 follow-up due:** May 31 (the `_check_wave2_day3_followup()` relay fires that day)
**Full wave 2 blitz card:** `outputs/vera/wave2_contractor_blitz_may28_2026-05-27.md`

---

### 7. 🔵 RESIDENTIAL HOMEOWNER OUTREACH — NO ACTIVE CHANNEL

**What's happening:** Zero systematic residential outreach beyond ads.
**What best-in-class power washing businesses do:**
- After every job, flyer/door-knock 15 nearest homes while equipment is still in the area
- "Your neighbor just had their [driveway/house/roof] washed — we're in the area today. Want a quote?"
- Converts at 5–10% (1–2 jobs per neighborhood visit)
- Equipment is already there — marginal cost is 15 minutes of Bradley's time

**Door hanger campaign guide:** `outputs/vera/door_hanger_neighbor_farm_2026-05-22.md`
**Proposal pending Bradley approval:** Systematic post-job neighborhood canvassing protocol

---

## What's Working

- **Facebook + Google ads launched May 26** — in 7-day learning phase, check June 2 (Day 7)
- **Relay calendar fully covered** through June 30 (Summit → Medina → Geauga/Portage → Cuyahoga → Lake → Lorain)
- **3 Mixmax sequences active** — PM, Realtor, Contractor sequences live
- **Round 2 enrollment plan in place** for June 4 (Medina + Summit leads)
- **Nina daily reports** running (check `outputs/nina/hot_leads_*.md` for 2+ open contacts)
- **25 commercial segments** now in Danny's Apollo title list ready for June county pulls

---

## The 60-Minute Priority Stack for Today (May 28)

| Order | Action | Time | Command/Guide |
|-------|--------|------|---------------|
| 1 | Wave 2 contractor texts (16 first-touch) | 45 min | `outputs/vera/wave2_contractor_blitz_may28_2026-05-27.md` |
| 2 | Summit County pull | 6 min unattended | `python3 workers/lead_pipeline.py danny Summit` |
| 3 | Day 3 ads check | 10 min | `outputs/vera/day3_ads_check_card_2026-05-26.md` |
| 4 | Google review requests (today's jobs) | 5 min | Text template above |

**Total: ~66 min** — do Summit pull while writing texts (it runs in background)
