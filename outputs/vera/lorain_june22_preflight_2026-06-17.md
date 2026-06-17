# Lorain County June 22 Pre-Flight Card
*Vera Cole | Run 208 | June 17, 2026 — 5 days out*

---

## 🎯 The Pull

**Date:** Sunday June 22, 2026 (Week 26)
**Script:** `scripts/run_lorain_both.command` (Danny + Carla)
**County:** Lorain County — Avon corridor, Elyria, North Ridgeville, Avon Lake, Sheffield Village, Vermilion

---

## ⭐ Priority Target Segments This Pull

| Segment | Why Lorain | Revenue Math |
|---------|-----------|-------------|
| **#199 Portable Restroom Rental** | Mr. John Inc. (Stow), Porta-Jon, United Site Services — all within service radius | $2K–$6K/facility; quarterly |
| **#200 FQHCs & Community Health Centers** | Lorain County General Health District (Elyria), Near West Healthcare satellite | $1.5K–$4K/facility; quarterly; government contract potential |
| **#201 Steel Fabrication & Structural Steel** | Lorain/Sheffield Village steel corridor; 50+ fab shops; scale + oil = heavy concrete staining | $2K–$6K/facility; quarterly |
| **Existing: Manufacturing (run 118)** | Ford Motor Avon Lake Assembly Plant — massive concrete footprint | $5K–$15K/facility |
| **Existing: Marina/Waterfront (run 109)** | Vermilion marina corridor; Showboat Marina, Spitzer Marine | $800–$2.5K/visit; 3x/year |

---

## 📋 Pre-Pull Checklist (Saturday June 21 Night)

- [ ] Gas/Fleet Mixmax sequences — if STILL PENDING, these leads wait again (Day 34+)
- [ ] `.env` file accessible locally at `/Users/bradleyneal/forestcity/`
- [ ] `contacts_cache.json` writable (no lock file in place)
- [ ] Internet connected and Apollo API accessible (check: `curl https://api.apollo.io`)
- [ ] Instantly.ai campaigns **PAUSED** before any enrollment fires

---

## 🏃 Day-of Execution (Sunday June 22)

**7:00–7:30am:**
```bash
cd /Users/bradleyneal/forestcity
./scripts/run_lorain_both.command
```
Expected runtime: 12–18 minutes (201+ segments = large pull)

**10:00am (after pull completes):**
```bash
python3 workers/nina_report.py daily
```
Open `outputs/nina/hot_leads_2026-06-22.md` — look for any immediate opens from Steel Fab / FQHC / Portable Sanitation contacts.

---

## 📍 Flagship Lorain County Targets

**Steel Fabrication (Segment #201 — new this run):**
- Sheffield Village steel corridor (along Lorain Road/I-90 corridor)
- Independent fab shops serving automotive, construction, and marine industries
- Look for Apollo contacts at companies with "fabrication," "steel," "iron works," "structural" in name

**FQHCs & Health Districts (Segment #200):**
- Lorain County General Health District (address: 9880 S. Murray Ridge Rd., Elyria)
- Neighborhood Health Association (if Lorain branch)
- Target title: "health district facilities director," "community health center administrator"

**Portable Restroom Rental (Segment #199):**
- Mr. John Inc. (based in Stow, serves Lorain County events)
- Pioneer Services Group (NE Ohio sanitation fleet operator)
- United Site Services (national, NE Ohio branch)
- Target title: "portable sanitation manager," "sanitation fleet manager"

**Marine Service Centers (Segment #195):**
- Vermilion-on-the-Lake marina service docks
- Sheffield Lake waterfront properties

**Manufacturing (existing — large opportunity):**
- Ford Motor Company Avon Lake Assembly Plant
- INEOS (Lorain — polypropylene plant)
- Lorain Products / Vertiv (industrial power equipment)

---

## 📅 What Happens After June 22

| Date | Action |
|------|--------|
| June 22 (night) | Lorain leads enrolled in Mixmax property_manager sequence |
| June 23–24 | Run Nina daily — first Lorain contacts may open immediately |
| June 27 | Cron fires Summit County 2nd pass (Week 27) |
| July 4 | **Holiday content opportunity** — deck/patio cleaning pitch (17 days away) |

---

## 🚨 Still Needs Bradley Action Before June 22

1. **Gas/Fleet Mixmax sequences** — complete email copy at `outputs/vera/gas_fleet_sequence_copy_2026-06-12.md`. 10 minutes. Lorain leads from these segments will queue unenrolled otherwise.
2. **GitHub Actions PAT** — add `workflow` scope at github.com/settings/tokens. 5 minutes. Enables Slack relay without cron dependency.

---

*Vera Cole | Pre-flight card written June 17 | Next pull: Lorain June 22 | Following: Summit 2nd pass June 29*
