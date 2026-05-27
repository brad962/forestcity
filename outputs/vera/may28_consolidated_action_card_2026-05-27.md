# May 28 — Thursday Action Card
### Vera Cole | Generated 2026-05-27
*Read this first thing Thursday morning. Three blocks, 80 minutes total.*

---

## PRIORITY ORDER (do in this sequence)

| Block | Action | Time | Why First |
|-------|--------|------|-----------|
| 1 | Wave 2 contractor texts — 16 contacts | 60 min | Revenue-generating, overdue today |
| 2 | Summit County pull | 6 min | Unattended — runs while you do other work |
| 3 | Day 3 ads check | 10 min | Read-only, no changes allowed yet |

---

## BLOCK 1 — WAVE 2 CONTRACTOR TEXTS (60 min)
**16 contacts due today. These were never texted. Peak season — every day of delay = missed referral bookings.**

### First: Close the 3 overdue Contacted contacts
These are past-due. Different angle — they've already heard from you once.

**Bryan / CLE Lawn Care Plus — 216-402-1924**
```
Hey Bryan — sent you a note last week about partnering on referrals. Wanted to make a quick offer: I'll come out and do one of your client's properties free (just takes 2 hours) so you can see what we do firsthand. If you like it, we set something up. If not, no hard feelings. Worth a conversation? — Bradley, Forest City Power Washing
```

**Bulletproof Lawncare — 216-307-4344**
```
Hey — following up on the referral partner message from last week. We're in your area all week doing jobs. If you see anyone asking about exterior cleaning, I'd love to have your name behind the referral. $50 per job I close from you. Happy to do the same for you. — Bradley, Forest City
```

**Damrons Landscaping — 440-494-0422**
```
Hey — quick follow-up on the referral program. We work with landscapers all over NE Ohio — when customers ask about siding/driveway cleaning, we refer you; when they ask us about landscaping, we refer them to you. Easy money on both sides. Worth a quick call? — Bradley
```

### Then: 5 Tier 1 First-Touch (New Lead — send in order)

**Anthony / Land Pro Management — 440-320-2779**
```
Hey Anthony — this is Bradley from Forest City Power Washing. We do exterior cleaning for landscaping companies in NE Ohio. When you're at a client's property and they mention dirty siding or a stained driveway, I'd love to be your go-to referral. I pay $50 per closed job. Worth a quick conversation? — Bradley
```

**Dontez / GTP Landscaping — 440-396-0814**
```
Hey Dontez — Bradley from Forest City Power Washing. I work with a handful of landscapers around Cuyahoga and Lake County and thought you'd be a good fit for a referral partnership. When you see dirty driveways and siding at client properties, I close the job and you get $50. Interested? — Bradley
```

**Chris / Twin Improvements — 216-773-0757**
```
Hey Chris — Bradley here, Forest City Power Washing. We work alongside contractors in NE Ohio — we handle the exterior cleaning while you handle the improvements. Happy to refer your work when customers ask, and pay you $50 per referral you send our way. Want to set something up? — Bradley
```

**Venus / Reliable Roofing and Restoration — 216-810-2497**
```
Hey Venus — Bradley from Forest City Power Washing. Roofers and power washing go hand in hand — a lot of our customers need both. I'd love to exchange referrals. When you see algae-stained roofs that need soft wash cleaning, I handle it. When customers ask me about roofing work, I send them to you. $50 per job I close from your referral. — Bradley
```

**Logan / Pagels Quality Construction — 216-956-5263**
```
Hey Logan — this is Bradley, Forest City Power Washing. We work with construction companies on exterior cleaning before and after projects. Also happy to set up a referral exchange — I pay $50 per job you send my way. Interested in connecting? — Bradley
```

### Then: 8 more Wave 2 contacts from pipeline
Check pipeline_data.json for remaining contacts with stage=New Lead due today.

---

## BLOCK 2 — SUMMIT PULL (6 min, unattended)
**Run this WHILE you're working on contractor texts. It takes 6 minutes and runs by itself.**

**3 days until Sunday May 31 hard deadline.** Miss this and Summit doesn't pull until July 6 — peak season gap.

```bash
# Double-click in Finder (no Terminal needed):
scripts/run_summit_pull.command

# Or Terminal:
cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py danny Summit
```

**What it does:** Pulls 50 property managers / facility managers in Summit County + Akron, deduplicates, auto-enrolls in Mixmax. Zero intervention required after you hit enter.

---

## BLOCK 3 — DAY 3 ADS CHECK (10 min, READ-ONLY)
**Ads launched May 26. Today is Day 3 — the first valid check date.**

Full card: `outputs/vera/day3_ads_check_card_2026-05-26.md`

**Quick thresholds:**
- Facebook: CTR > 1% and CPL < $30 → leave it alone
- Google: Any impressions showing → leave it alone
- Lead log: check `outputs/rick/launch_week_lead_log_2026-05-26.md` — fill in Day 3 row

**ONE allowed tweak:** If Facebook CTR < 0.5% AND you've spent $30+, swap the ad hook to the VOC refresh version. Guide: `outputs/rick/facebook_ad_creative_voc_refresh_2026-05-24.md`.

**Do NOT change:**
- Budget (wait until Day 7)
- Targeting (learning phase needs consistency)
- Pause and restart (resets algorithm — costs $50+ to recover)

---

## WHAT'S STILL OPEN AFTER TODAY

| Item | Status | Deadline |
|------|--------|----------|
| Summit pull | 🚨 DO IT TODAY | May 31 (Sunday) |
| Gas station Mixmax sequence | ⏳ Create in Mixmax UI → paste ID | Before June 4 |
| Instantly.ai pause | ⏳ 3-min task at app.instantly.ai | Before June 4 |
| Wave 2 contractors (16) | 🔴 Due today | Today |
| Day 3 ads check | 📊 Read-only | Today |
| Medina County pull | 📅 June 1 (Monday) | June 1 |
| June 4 enrollment | 📅 Round 2 | June 4 |

---

## GAS STATION — QUICK PATH (if you have 5 extra minutes)
12 gas station contacts are sitting idle. Two options:

**Option A (fastest):** Gmail blast using the guide at `outputs/danny/gas_station_sequence_create_now_2026-05-27.md` — send individual emails from your Gmail without Mixmax.

**Option B (right way):** Create the sequence in Mixmax UI (10 min) → paste ID into `integrations/mixmax.py` → run `python3 workers/lead_pipeline.py pending` (auto-enrolls all 12).

The email copy for both options is in `outputs/danny/sequence_gas_stations_2026-05-19.md`.

---

*Vera Cole | CIO | May 27, 2026*
