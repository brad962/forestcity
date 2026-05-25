# June 4 — Carla's Referral Partner Activation Card
### Carla Reyes | Referral Partner Manager | 2026-05-25
*Carla's press-GO card for June 4 — parallel to Danny's PM enrollment battle card*

> **This is Carla's June 4 script.** Danny owns PM enrollment. Carla owns partner activation.
> Estimated time: 45 minutes total. Do this RIGHT AFTER Danny runs the enrollment commands.

---

## THE SITUATION

Bradley has 3 active sequences in Mixmax. June 4 is Round 2 enrollment day — the full office launches simultaneously. Carla's job on June 4 is to **activate the referral partner pipeline**, not just enroll contacts.

**What exists heading into June 4:**
- `contractor_referral_sequence_voc_rewrite_2026-05-23.md` — VOC-refreshed 3-touch sequence ready to enroll
- `realtor_summer_voc_sequence_2026-05-24.md` — summer listing season sequence, June 4 timing
- `june_referral_revival_texts_2026-05-23.md` — text scripts for pipeline contacts who went quiet
- `pool_service_referral_blitz_2026-05-24.md` — pool season blitz for pool companies servicing NE Ohio homes NOW
- Medina County Apollo pull (June 1) will have fresh contractor leads ready

---

## JUNE 4 EXECUTION — 3 TRACKS

### TRACK 1: Enroll Fresh Medina Leads (10 min)
Medina pull runs June 1 (Danny + Carla both). By June 4, fresh contractor + realtor leads are in contacts_cache.json. Run:
```bash
python3 workers/lead_pipeline.py pending
```
This enrolls ALL pending contacts across all live sequences — contractors and realtors from Medina pull go into sequences automatically. No extra steps.

**Check enrollment:**
```bash
python3 workers/nina_report.py daily
```
Verify contractor + realtor sequence counts went up.

---

### TRACK 2: Pool Service Text Blitz (15 min)
Pool companies are in customers' backyards RIGHT NOW. They see dirty decks, siding, driveways on every visit. This is peak referral moment.

**Full script and timing guide:** `outputs/carla/pool_service_referral_blitz_2026-05-24.md`

**Quick version — text this to any pool company you find locally:**
```
Hey [Name] — Bradley at Forest City Power Washing in NE Ohio. Pool season = we're both in yards all week. Any customers whose decks or siding look rough? We do before/after photos and pay $50 per referral job you send us. Simple deal, no paperwork. Let me know if it makes sense.
```

Find local pool companies: Google "pool service [city] Ohio" → call or text the owner directly.

**Target:** 5 outreach texts on June 4. Even 1 YES = recurring referrals all summer.

---

### TRACK 3: Contractor Pipeline Revival (20 min)
Use `june_referral_revival_texts_2026-05-23.md` to reactivate the contractors who were contacted earlier and went quiet.

**Priority contacts for June 4 revival (from pipeline_data.json):**

| Name | Company | Phone | Notes |
|------|---------|-------|-------|
| Anthony | Land Pro Management | 440-320-2779 | Landscaper — Memorial Day text pending |
| Dontez | GTP Landscaping | 440-396-0814 | Landscaper — Memorial Day text pending |
| Chris | Twin Improvements | 216-773-0757 | Siding contractor |
| Venus | Reliable Roofing | 216-810-2497 | Roofer — natural algae/soft-wash connection |
| Logan | Pagels Quality Construction | 216-956-5263 | Siding contractor |
| Bryan | CLE Lawn Care Plus | 216-402-1924 | Lawn care — 2nd follow-up by June 4 |

**June 4 angle (different from the first touch — use the season hook):**
```
Hey [Name] — Bradley, Forest City Power Washing. Summer's officially here and we're slammed with jobs. Circling back — if any of your customers are asking about getting their house or driveway cleaned, we're booking fast and we handle the whole thing same-day quote. $50 per referral job for you. Still interested?
```

**If they already responded YES to Memorial Day text:**
```
Hey [Name] — just wanted to follow up. We officially launched this week. If you have any customers ready for a quote, just text me their address. I'll turn it around same day.
```

---

## SUCCESS METRICS FOR JUNE 4

| Metric | Target |
|--------|--------|
| Fresh leads enrolled via `pending` | 10+ |
| Pool company texts sent | 5 |
| Contractor revival texts sent | 5–6 |
| YES responses (any channel) | 1–3 |
| Revenue pipeline added via referrals | $600–$1,800 (1–3 booked jobs @ $450–$600 avg) |

---

## AFTER JUNE 4

Check Mixmax replies at 2pm: `python3 workers/check_replies.py`

If any contractor replies YES, send them the referral partner onboarding card:
`outputs/carla/referral_partner_onboarding_2026-05-20.md`

---

## FILES FOR JUNE 4

| File | Purpose |
|------|---------|
| `workers/lead_pipeline.py pending` | Enroll Medina + Summit fresh leads |
| `outputs/carla/pool_service_referral_blitz_2026-05-24.md` | Pool company scripts |
| `outputs/carla/june_referral_revival_texts_2026-05-23.md` | Trade-specific revival texts |
| `outputs/carla/realtor_summer_voc_sequence_2026-05-24.md` | Realtor summer sequence enrolled via Mixmax |
| `outputs/donna/june4_enrollment_battle_card_2026-05-24.md` | Danny's parallel track (coordinate timing) |

---

*Carla's June 4 card created 2026-05-25 Run 87. Parallel to Danny's june4_enrollment_battle_card.*
