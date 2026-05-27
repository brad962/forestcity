# May 28 Thursday — 60-Minute Morning Execution
*Vera Cole | Run 110 | Use this first thing Thursday morning*

---

## The 60-Minute Stack

**Open time needed: 7:30am – 8:30am**

All three things below run in parallel. Start Summit, then text while it runs.

---

## BLOCK 1 — Start Summit Pull FIRST (5 min click, runs unattended)
> 🚨 3 DAYS LEFT. Miss May 31 → no Summit leads until July 6.

**Double-click:** `scripts/run_summit_pull.command` in Finder  
**OR Terminal:** `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py danny Summit`

Wait for the "Starting pull..." message, then LEAVE IT RUNNING. Go to Block 2 immediately.
- Runtime: 5–10 minutes unattended
- Output: leads saved to `outputs/danny/`
- When done: Mixmax enrollment happens automatically

> **Bonus:** If you want Carla's Summit referral partners too, double-click `scripts/run_summit_both.command` instead.

---

## BLOCK 2 — Wave 2 Contractor Texts: 16 contacts (45 min)
> Full script in: `outputs/vera/wave2_contractor_blitz_may28_2026-05-27.md`

Send while Summit pull runs in background.

**LANDSCAPERS (11 contacts):**
```
Hey [Name], this is Bradley with Forest City Power Washing. We do exterior
cleaning for homes and commercial properties across NE Ohio and I wanted to
reach out to a few landscapers in the area. We cross-refer a lot — when your
clients ask about washing we send them your way, same back. Worth a quick
call? I'm at [your number].
```

**CONSTRUCTION/ROOFERS (5 contacts):**
```
Hey [Name], Bradley here from Forest City Power Washing. We work with a lot
of contractors on exterior cleaning — pre-paint wash, post-construction
cleanup, homeowners asking about it. Wanted to connect and see if there's
a referral fit. Quick call this week? [your number]
```

**16 contacts in order (all have next_followup = 2026-05-28):**

| # | Contact | Company | Phone |
|---|---------|---------|-------|
| 1 | Pyro Landscaping | — | Check pipeline |
| 2 | Garten Gurus | — | Check pipeline |
| 3 | Dales | — | Check pipeline |
| 4 | C&M Landscaping | — | Check pipeline |
| 5 | Kays Express Lawn Care | — | Check pipeline |
| 6 | Walkers Landscape | — | Check pipeline |
| 7 | Islander Landscaping | — | Check pipeline |
| 8 | Lawn Care for the World | — | Check pipeline |
| 9 | Soldan Landscaping | — | Check pipeline |
| 10 | Clemence Collaborations | — | Check pipeline |
| 11 | Blue Line Restorations | — | Check pipeline |
| 12 | Kardiac Construction | — | Check pipeline |
| 13 | Don't Move Improve | — | Check pipeline |
| 14 | Woolworth Construction | — | Check pipeline |
| 15 | Everguard Pros | — | Check pipeline |
| 16 | Camlin Contracting | — | Check pipeline |

> After sending: Run `python3 scripts/contact_done.py` to mark all as Contacted, last_contact = today, next_followup = 2026-05-31 (Day 3 follow-up)

---

## BLOCK 3 — Day 3 Ads Check: 10 minutes (after texting)
> Full guide: `outputs/vera/day3_ads_check_card_2026-05-26.md`

**What to check (read-only — DO NOT EDIT):**
- Facebook Ads Manager: CTR > 1%? ✅ Wait. < 1%? Read the card.
- Google Ads: Any impressions? Any clicks? Any calls?
- Lead log: `outputs/rick/launch_week_lead_log_2026-05-26.md` — fill in any leads from Days 1-2
- ONE allowed change only: creative swap if CTR < 0.5% on Facebook

**Do NOT:**
- Pause campaigns
- Change budget
- Edit targeting
- Make more than one change

---

## Pipeline Update After This Block

```bash
python3 scripts/contact_done.py
```
- Mark Wave 2 contacts: stage = Contacted, last_contact = 2026-05-28, next_followup = 2026-05-31
- If Summit pull finished: check `outputs/danny/` for the new leads file

---

## Success Criteria by 9am

- [ ] Summit pull started (running or completed)
- [ ] 16 Wave 2 texts sent
- [ ] Day 3 ads check done (10 min read-only)
- [ ] Pipeline updated via contact_done.py
- [ ] Lead log filled in

---

## What's Coming Next

| Date | Event | Action |
|------|-------|--------|
| May 28 (today) | Day 3 ads check | Read-only — Day 3 card |
| May 31 | Summit pull HARD DEADLINE | Must be done |
| May 31 | Wave 2 Day 3 follow-up | 16 contractor follow-up texts |
| June 1 | Medina County pull | Double-click `run_medina_pull.command` |
| June 3 (evening) | Go/No-Go check | `june3_tuesday_evening_checklist` |
| June 4 | Round 2 enrollment | 60-160 contacts into Mixmax |

---

*Revenue math on this morning's work:*
- Wave 2 contractors: $4K–$20K/year referral potential per yes
- Summit pull: 30–80 new PM/commercial leads entering Mixmax
- Total 60-min investment: potentially $100K+ in new pipeline value

---
*Vera Cole | Run 110 | 2026-05-27*
