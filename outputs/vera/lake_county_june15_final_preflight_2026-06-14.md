# Lake County Pull — TOMORROW MORNING June 15 (Monday)
*Vera Run 205 | June 14, 2026 | Final Preflight Card*

---

## THE ONE ACTION: 7:30am Monday

Open Finder → `forestcity/scripts/` → double-click **`run_lake_both.command`**

That's it. Walk away. It runs 12–20 minutes unattended.

---

## What Fires Tomorrow

**199 commercial segments** pull simultaneously across Lake County.

**Lake County flagship targets (unique to this pull):**

| Target | Why It Matters | Segment |
|--------|---------------|---------|
| Willoughby Hopkins Airport FBO (LNN) | Only GA airport in Lake County; ramp concrete + hangar floors = fuel/oil staining; $3K–$10K/visit | #197 |
| Willoughby Brewing | Largest Lake County craft brewery; outdoor patio + parking + facade; spring patio opening angle | #196 |
| Lake County Nursery Exchange / Willoway Nurseries / Berns Nurseries | Lake County = "Nursery Capital of Ohio" (200+ wholesale nurseries); production facility scale; $2K–$8K/facility | #198 |
| Grand River Marine Service / Fairport Harbor Boat Works | Boat repair yards have algae + oil on concrete + equipment bays; peak repair season now | #195 |
| Integer Holdings (formerly Greatbatch) / Parker Hannifin Electronics (Mayfield Heights) | ISO 14001 + OEPA NPDES compliance angle; semiconductor/electronics manufacturing | #194 |

---

## After the Pull Fires

**Within 1 hour (10am or sooner):**
```
python3 workers/nina_report.py daily
```
Check for any contacts with existing Mixmax engagement. Lake County has a 3-day hot leads window — June 16–18. Start watching on June 16.

---

## 🚨 Gas/Fleet STILL PENDING (Day 31)

If you complete the Mixmax sequence setup **before** Monday's pull, run this immediately after:
```
python3 workers/lead_pipeline.py pending
```
This enrolls ALL unenrolled gas station + fleet contacts from Summit, Medina, Cuyahoga, and Lake County in one shot.

Sequence copy is ready to paste (no writing needed):
`outputs/vera/gas_fleet_sequence_copy_2026-06-12.md`

---

## Pre-Pull Checklist (Sunday Night / Monday Morning)

- [ ] Laptop charged (stays on desk — don't need it during the run)
- [ ] `scripts/run_lake_both.command` is in Finder (double-click ready)
- [ ] Gas/Fleet sequences created in Mixmax? (If yes, run `pending` immediately after pull)
- [ ] Set a 9:45am reminder to check terminal output

---

## Lake County Pull Timeline (June 15)

| Time | Action |
|------|--------|
| 7:30am | Double-click `run_lake_both.command` |
| 7:30–7:50am | Runs unattended (do other things) |
| ~7:50am | Pull completes — output appears in terminal |
| 9:45am | Run `python3 workers/nina_report.py daily` |
| Ongoing June 16–18 | Monitor daily for hot leads (2+ opens) |

---

*Next county: Lorain — June 22 (Week 26). Double-click `run_lorain_both.command`.*
