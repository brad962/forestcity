# May 28 — Thursday Complete Action Card
### Vera Cole | Generated 2026-05-27

---

## Priority Stack (Total: ~90 minutes)

| Block | Time | Action | Revenue at Stake |
|-------|------|--------|-----------------|
| 1 | 9:00am (10 min) | Ads Day 3 check | Prevent algorithm reset |
| 2 | 9:15am (6 min unattended) | Summit County pull | $40K-$120K in new pipeline |
| 3 | While pull runs (20 min) | Wave 2 contractor texts | $11K-$28K referral pipeline |
| 4 | 10:00am (30 min) | Bryan close-file + gas station blast | $2K-$5K immediate |
| 5 | Anytime (30 min) | Past customer texts | $1,800-$3,000 fastest revenue |

---

## BLOCK 1 — Ads Day 3 Check (9am, 10 min)

Day 3 = the FIRST allowed tweak window. If you touch anything before today, you reset Facebook's learning phase.

**Facebook — check these numbers only:**
- CTR (Link Click-Through Rate): `<1%` = check creative | `1-3%` = normal | `>3%` = excellent
- Cost Per Lead: `>$50` = audience issue | `$20-$50` = acceptable | `<$20` = scale it
- Reach: `<500` = budget too low or audience too narrow

**Google — check these:**
- Impressions: `<50/day` = keywords not matching or Quality Score forming
- CTR: `<1%` = check ads | `1-3%` = normal for early learning phase
- CPC: `>$8` = bid strategy issue

**One-tweak rule:** If you're adjusting anything, change ONE thing only (creative OR audience OR budget — never all three).
**If numbers are acceptable: leave it alone. Facebook needs 7 days.**

Full check card: `outputs/vera/day3_ads_check_card_2026-05-26.md`

---

## BLOCK 2 — Summit County Pull (9:15am, 6 min unattended)

**3 DAYS LEFT** to Summit pull window (deadline May 31). Miss this = no Summit contacts until July 6.

**Double-click in Finder:** `scripts/run_summit_pull.command` (no Terminal typing required)

OR Terminal:
```bash
cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py danny Summit
```

- Pull runs unattended (5-10 min with all new commercial segments)
- DO NOT close the Terminal window
- Start your Wave 2 texts (Block 3) while it runs

**What you'll get:** Property managers + facility managers + hotel GMs + bank branch managers + grocery FMs + fitness center managers + golf course superintendents + cemetery directors + funeral home directors — all new this month, first time targeting Summit County.

---

## BLOCK 3 — Wave 2 Contractor First-Touch Texts (While Pull Runs, 20 min)

**16 contacts due TODAY.** These are wave 2 landscapers and construction contractors who haven't heard from you yet. Copy-paste texts.

**Text template by trade:**

**Landscapers:**
> Hey [Name], this is Bradley at Forest City Power Washing in Cleveland. We work with a lot of landscaping companies like yours — when clients ask your team about getting their driveway or house washed, we take care of it and send $50 your way for every job. No paperwork. Want to give it a shot?

**Construction/Siding:**
> Hey [Name], this is Bradley at Forest City Power Washing. We do a lot of prep work before siding and painting jobs — pressure washing the surface first. When you've got clients who need it done before you start, we handle it and pay $50 per referral. Worth connecting?

**General/Unknown Trade:**
> Hey [Name], Bradley from Forest City Power Washing. We do exterior cleaning throughout NE Ohio and partner with local contractors — $50 per job you send our way, or we trade referrals. Worth a quick chat?

**16 contacts to text:**

| Contact | Company | Phone | Trade |
|---------|---------|-------|-------|
| Eric Pylo | Pyro Landscaping | 216-303-0154 | Landscaping |
| — | Garten Gurus | 216-983-9088 | Landscaping |
| Dale | Dales Landscaping | 216-421-5121 | Landscaping |
| Chris | C and M Landscaping | 440-781-3864 | Landscaping |
| McKayla | Kays Express Lawn Care | 216-527-3030 | Landscaping |
| Michael | Walkers Landscape | 216-217-9715 | Landscaping |
| Colleen | Clemence Collaborations | 440-391-9903 | Unknown |
| Samuel | Islander Landscaping | 216-659-3028 | Landscaping |
| Dominic | Lawn Care for the World | 216-575-8038 | Landscaping |
| Donald | Soldan Landscaping | 216-576-2549 | Landscaping |
| Daniel | Blue Line Restorations | 440-724-8400 | Construction |
| John | Kardiac Construction | 216-609-6575 | Construction |
| Tim Fleenor | Don't Move Improve | 216-399-8075 | Construction |
| Howard | Woolworth Construction | 216-502-5787 | Construction |
| Paul | Everguard Pros | 440-554-6892 | Unknown |
| Pat | Camlin Contracting | 440-240-3456 | Contracting |

After texting: run `python3 scripts/contact_done.py` and set stage → Contacted, last_contact → today, next_followup → May 31 (Day 3 follow-up).

Follow-up schedule: `outputs/vera/wave2_contractor_followup_schedule_2026-05-27.md`

---

## BLOCK 4 — Bryan Close-File Decision (10am, 15 min)

**Bryan / CLE Lawn Care Plus — 216-402-1924 — 15+ days cold**

Bryan has been in "Contacted" stage since May 13. Today is May 28 — 15 days with no reply to any attempt.

**Decision tree:**

Option A — Send close-the-loop text (TODAY):
> "Hey Bryan, following up one last time. We have availability for power washing referrals in your area and wanted to partner with CLE Lawn Care Plus. If this isn't the right fit, totally understand — just wanted to close the loop. Let me know either way."

This text gets ~30% late-reply rate (people feel the loop closing and respond).

Option B — If no reply by tomorrow May 29 → close file, move to "Closed Lost" in pipeline, pivot to 21 untouched contacts.

Close-file guidance: `outputs/vera/bryan_close_file_text_2026-05-26.md`

---

## BLOCK 5 — Past Customer Texts (Anytime, 30 min)

**Fastest revenue while ads are in learning phase.** Ads launched 3 days ago. The learning phase (7 days) means minimal leads right now. Past customers = warm leads, 30-60% re-engagement rate.

**What to do:**
1. Open Workiz → Jobs → filter to 2025 + spring 2026 jobs marked Paid/Complete
2. For each past customer, look up their phone
3. Text using the script for their situation (house wash, deck, annual plan, etc.)

Full guide + 5 copy-paste scripts: `outputs/tommy/past_customer_june_blast_2026-05-27.md`

**Revenue math:** 10 texts → 3 conversations → 2 booked jobs → avg $600/job = $1,200 minimum. That's 30 minutes.

---

## Blockers — Update These Today

| Blocker | Status | Action |
|---------|--------|--------|
| Instantly.ai NOT paused | 🔴 CRITICAL | app.instantly.ai → pause a1c08c3d + 626cd15d → add INSTANTLY_PAUSED=true to .env |
| Gas station sequence PENDING | 🔴 | 30-min guide: `outputs/danny/gas_station_sequence_create_now_2026-05-27.md` |
| Summit pull not done | 🟡 | Do it TODAY (Block 2 above) |

---

## Wave 2 Follow-Up Schedule

| Day | Date | Action |
|-----|------|--------|
| Day 3 | May 31 (Sunday) | Follow-up text to Wave 2 — any who didn't reply to Day 1 text |
| Day 7 | June 4 | Final follow-up — or redirect their referral capacity to your June 4 enrollment blitz |

---

## Tomorrow Preview (May 29 — Friday)

- Summit pull if not done today (FINAL BUSINESS DAY before May 31 weekend deadline)
- Ads: Day 4 — read-only glance, don't touch anything
- Bryan: close-file text if no response
- Gas station: last chance to create sequence before June 4 enrollment sprint

Card: `outputs/vera/may29_friday_summit_deadline_card_2026-05-26.md`

---

*Vera Cole | Chief Innovation Officer | Generated 2026-05-27*
