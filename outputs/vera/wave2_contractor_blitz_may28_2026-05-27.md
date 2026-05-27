# Wave 2 Contractor Blitz — Thursday May 28
### Vera Cole | 2026-05-27 | 16 First-Touch Texts Due Tomorrow
*Run after Summit pull (if you haven't already). Do this while coffee is hot.*

---

## What This Is

16 contractor referral contacts in pipeline_data.json have `next_followup=2026-05-28`. These are Carla's Wave 2 landscapers and construction companies. None have been contacted yet. They've been in the pipeline since early May — it's peak season, and they're at client properties every day.

**One landscaper referral partner = 2-5 jobs per season.** At $350 avg, that's $700-$1,750 per partner. 16 partners = $11,200–$28,000 in potential referral revenue.

---

## The Text (Copy-Paste for All 16)

Adapt the opening line by trade type. The rest is identical.

**For landscapers:**
> "Hey [Name], I'm Bradley with Forest City Power Washing — we're the exterior cleaning company working alongside landscapers across NE Ohio. We do house washing, roof soft wash, driveways. Whenever your clients ask about exterior cleaning or you notice dirty siding, send them our way — we pay $50 cash per closed job. Quick question: do you ever get asked for power washing recommendations?"

**For construction/remodeling:**
> "Hey [Name], I'm Bradley with Forest City Power Washing. We do exterior cleaning — house wash, driveway, concrete. A lot of contractors send us work when they're finishing a job and the house needs a wash. We pay $50 per closed referral. Do you run into that with your clients?"

**For roofers:**
> "Hey [Name], I'm Bradley with Forest City Power Washing — we do roof soft wash (the algae removal). A lot of roofers we work with send us clients who have black streaks but don't need a full replacement — just a clean. We pay $50 cash per closed job. Does that come up with your customers?"

---

## The 16 Contacts (Wave 2 — Due May 28)

Pull phone numbers from `pipeline_data.json` — all 16 have `next_followup=2026-05-28`. Key contacts from the Carla contractor list:

1. Pyro Landscaping
2. Garten Gurus
3. Dales Landscaping
4. C&M Landscaping
5. Kays Express Lawn Care
6. Walkers Landscape
7. Islander Landscaping
8. Lawn Care for the World
9. Soldan Landscaping
10. Clemence Collaborations
11. Blue Line Restorations
12. Kardiac Construction
13. Don't Move Improve
14. Woolworth Construction
15. Everguard Pros
16. Camlin Contracting

---

## Time Required
- **Total: 25–35 minutes** (average ~2 min per text + reply scan)
- Do this after Summit pull (6 min unattended) — run Summit, text while it pulls

---

## If They Reply "Yes / Tell Me More"

> "Perfect. I'll send you a quick text with our referral link and pricing. Basically — you refer, we do the work, you get $50 cash or PayPal when the job closes. Zero paperwork. Most of our referral partners send us 2-3 jobs a season without even thinking about it. What kind of work do you mostly do — residential, commercial, or both?"

Then update `pipeline_data.json`: stage → "Replied", add last_contact and next_followup.

---

## If No Reply by May 30

Move to Carla's `june_referral_revival_texts_2026-05-23.md` for the trade-specific follow-up cadence. Don't abandon — landscapers are the single highest-referral-rate partner type in home services.

---

## After Texting — Update pipeline_data.json

For each contact you texted, update:
- `stage`: "Contacted"
- `last_contact`: "2026-05-28"
- `next_followup`: "2026-05-31"

---

## Context: Where These Contacts Fit

```
TODAY May 27:
  ✅ Block 1: Bryan close-loop | Bulletproof | Damrons (3 Contacted)
  ✅ Block 2: Anthony/Land Pro | Dontez/GTP | Chris/Twin | Venus/Reliable | Logan/Pagels (5 Tier 1 first touch)
  ⏳ Block 3: 12 Gas station email blast

TOMORROW May 28:
  → Run Summit pull (may28_summit_pull_emergency_card_2026-05-26.md)
  → These 16 Wave 2 contractor texts (this card)
  → Day 3 ads check at end of day (day3_ads_check_card_2026-05-26.md)

JUNE 1:
  → Medina County pull (run_medina_both.command)
  → Wave 3 follow-ups for anyone who hasn't replied

JUNE 4:
  → Round 2 enrollment battle card (june4_enrollment_battle_card_2026-05-24.md)
```
