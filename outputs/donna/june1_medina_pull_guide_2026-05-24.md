# June 1 Medina County Pull Guide
### Week 22 — Monday June 1, 2026
*Vera Cole | Generated 2026-05-24*

---

## What This Is

Medina County is Week 22 in Danny's county rotation. June 1 (Monday) is the first day of Week 22. This guide operationalizes that pull — same approach as the Summit County pull from Week 21.

**Why Medina matters:**
- Brunswick, Wadsworth, Medina city = dense residential + HOA communities
- Strong property management presence in the I-71 corridor
- Less crowded Apollo data pool than Cuyahoga (less duplication)
- June 4 = Round 2 enrollment — Medina leads from June 1 go into enrollment June 4 (3 days later)

---

## Option 1 — Double-Click (Fastest)

In Finder, navigate to `forestcity/scripts/` and double-click:
- **`run_medina_pull.command`** — Danny only (property managers)
- **`run_medina_both.command`** — Danny + Carla together (both workers)

Terminal opens, runs the pull, shows results, closes when you press any key.

**Run time:** 2-3 minutes (Danny only) or 5-8 minutes (both workers)

---

## Option 2 — Terminal

```bash
# Danny only
cd /Users/bradleyneal/forestcity
python3 workers/lead_pipeline.py danny Medina

# Both Danny + Carla
python3 workers/lead_pipeline.py danny Medina
python3 workers/lead_pipeline.py carla Medina
```

---

## What Happens

1. Apollo searches Medina County, Ohio + Medina, Ohio for property managers and facility managers
2. Danny: pulls up to 50 leads, reveals emails, enrolls in Mixmax (PM sequence)
3. Carla: pulls contractors, landscapers, roofers for referral outreach in Medina area
4. Leads saved to `outputs/danny/leads_medina_property_managers_2026-06-01.md`
5. Activity logged to `logs/activity.log`
6. Sentinel file updated (vera_relay staleness check resets)

---

## Pre-Pull Check (June 3 evening, night before enrollment)

Before pulling on June 1, verify these are ready:
- [ ] INSTANTLY_PAUSED=true in .env (required for enrollment — see instantly_pause_guide_2026-05-22.md)
- [ ] Mixmax PM sequence is still live (check: python3 -c "from integrations.mixmax import SEQUENCES; print(SEQUENCES)")
- [ ] Cron is running: tail -20 logs/cron.log

---

## June 4 Connection (Round 2 Enrollment)

Fresh Medina leads from June 1 go into Mixmax enrollment June 4 via the june4_enrollment_battle_card_2026-05-24.md:

```bash
# Run on June 4 morning
python3 workers/lead_pipeline.py both     # fresh weekly pull auto-selects correct county
python3 workers/lead_pipeline.py pending  # enrolls gas station + fleet contacts once sequence IDs are live
```

Medina leads pulled June 1 are already enrolled by lead_pipeline.py (enrollment happens during the pull). The June 4 battle card adds the gas station + fleet contacts on top.

---

## Medina-Specific Apollo Targets

The lead_pipeline.py auto-applies Danny's full title list and org keywords. Medina-specific companies worth watching for:

- **HOA management firms:** Medina has 50+ HOA communities in the Brunswick-Medina-Wadsworth triangle
- **Multifamily:** Several large apartment complexes along Rte 42 and I-71
- **Commercial:** Light industrial/office in Medina Business Park area

These will surface automatically — no custom configuration needed.

---

## After the Pull

1. Check `outputs/danny/leads_medina_property_managers_2026-06-01.md` — confirm lead count > 10
2. If < 10 leads (duplicate-heavy): run `python3 workers/lead_pipeline.py danny Geauga` to supplement
3. Log the run: it's automatic via lead_pipeline.py
4. Proceed to june4_enrollment_battle_card_2026-05-24.md
