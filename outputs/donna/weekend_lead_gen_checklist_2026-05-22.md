# Memorial Day Weekend Lead Gen Checklist
### May 23–25, 2026 (Saturday–Monday)
*Donna Park | Growth Strategist*
*While you're monitoring the Touch 3 reply window — here's what to do with your spare time*

---

## Context

Touch 3 fired Thursday May 22. The 72-hour reply window runs through Sunday May 25. Most property managers won't reply over a holiday weekend — that's normal. **But homeowners ARE on Facebook and Nextdoor all weekend.**

This checklist runs parallel to the Mixmax monitoring. Do one item Saturday morning, one Sunday morning, and spend Monday on the paid blitz.

**Total time: ~90 minutes across the weekend.**

---

## Saturday Morning (May 23) — 30 min

### Task 1: Post in 3 NE Ohio Facebook Homeowner Groups (15 min)

Copy-paste this post into each group. Adjust city name for each group.

**Post copy:**
```
Heads up, [City] neighbors — if your house, driveway, or roof is looking rough after the spring rains, 
now is the best time to get it done before summer.

We're Forest City Power Washing. We serve the greater Cleveland area and we're booking into June now. 

House wash, roof soft wash, driveway/sidewalk, before & after photos included.

DM me or comment QUOTE and I'll get you a number. Fast turnaround on quotes.
```

**Target groups (search Facebook for these):**
1. Cleveland/Cuyahoga County: "Cleveland Ohio Homeowners" or "Parma/Lakewood/Strongsville area homeowners"
2. Lake County: "Lake County Ohio Community" or "Mentor/Willoughby Ohio area"
3. Summit/Medina: "Medina County Ohio Neighbors" or "Akron area home improvement"

**Rules:** Don't post in groups that ban business solicitation. Look for the group rules pinned post first. If they ban it, skip and find a different group.

### Task 2: Update GBP Cover Photo (15 min)

1. Go to business.google.com/dashboard
2. Upload the most recent before/after photo from `outputs/jasmine/`
3. Add a description: "Power washing in [city] — before and after. Forest City Power Washing serves NE Ohio."

**Why this weekend:** Google Business Profile photo uploads bump your appearance in "power washing near me" searches for the next 2–4 weeks — perfect for the June push.

---

## Sunday Morning (May 24) — 30 min

### Task 3: Set Up Nextdoor Post (15 min)

If you haven't used Nextdoor before:
1. Sign up at nextdoor.com with your home address
2. Once verified (1–2 days), post as a local business recommendation

**Post copy (for Nextdoor):**
```
Hi neighbors — I run Forest City Power Washing and we're booking exterior cleaning jobs 
in the area this month.

House washing, driveway cleaning, roof soft washing. Serving the Cleveland area.

If your house is due for a wash before summer, DM me here or text (your number). 
Happy to give a free quote.

— Bradley, Forest City Power Washing
```

**Note:** Nextdoor has a 2-day verification delay. Set this up today so you're verified for posts by Tuesday/Wednesday.

### Task 4: Send Past Customer Texts (15 min)

Pick 5 past customers you haven't heard from in 6+ months. Send this text:

```
Hey [Name], it's Bradley from Forest City Power Washing. 
Hope you're enjoying the spring! 

Your house/driveway is probably due for a wash — 
want me to swing by for a quick look and price? 

I have some May openings left.
```

Adjust "house/driveway" to match what you did for them. Personal, not mass-blast.

**Expected result:** 2–3 replies = 1–2 jobs = $400–$800. Zero ad spend.

Full template: `outputs/tommy/past_customer_reengagement_2026-05-18.md`

---

## Monday Morning — May 26 (Blitz Day)

**Do not rest on Monday.** This is the highest-value day of the Memorial Day sprint.

Full action card: `outputs/donna/may26_blitz_action_card.md`

Priority order for Monday morning:
1. **9am:** Run `python3 workers/check_replies.py` — see if anyone replied over the weekend
2. **9:15am:** Send the 5 contractor texts (from `outputs/tommy/contractor_followup_texts_2026-05-21.md`)
3. **9:30am:** Launch Facebook ads (guide: `outputs/vera/may26_ads_launch_checklist_2026-05-22.md`)
4. **10am:** Send past customer text blast (15–20 contacts, `outputs/donna/past_customer_reengagement_launch_2026-05-21.md`)
5. **11am:** Run Danny lead pull: `python3 workers/lead_pipeline.py danny`
6. **All day:** Respond to any Mixmax replies within 1 hour

---

## If You Get Inbound Leads This Weekend

Facebook DMs and Nextdoor messages often come in fast on weekends. Use the inbound response protocol: `outputs/tommy/inbound_response_protocol_2026-05-19.md`

Short version:
- Reply within 1 hour on weekends (converts at 3x vs. Monday reply)
- Get their address and a brief of what they need
- Text your quote (not email) — open rate is near 100%
- Offer a specific date: "I have Thursday May 28 open — does that work?"

---

## Weekend Metrics to Track

| Metric | Target | Your Number |
|--------|--------|-------------|
| Facebook group posts sent | 3 | |
| GBP photo uploaded | 1 | |
| Past customer texts sent | 5 | |
| Inbound DMs received | 1–3 | |
| Quotes requested | 1+ | |

---

## What Success Looks Like by Monday 9am

✅ 3 Facebook group posts live  
✅ 1 GBP photo updated  
✅ 5 past customer texts sent  
✅ Nextdoor verification submitted  
✅ Any inbound DMs responded to same day  
✅ Mixmax reply window check ready to run at 9am

Even 1 booked job from the weekend covers a week of ad spend at the $30/day budget.

---

*Donna Park | Growth Strategist | May 22, 2026*
