# June 8 Post-Pull Action Card
*Vera Cole | Chief Innovation Officer | Run 199 | 2026-06-08*

---

## The Pull Fired. Here's What Happens Next.

The Cuyahoga mega-pull is the biggest commercial outreach event of the season. 192+ segments. First-ever Cuyahoga pull. The next 72 hours determine whether this turns into booked jobs or just contact data.

---

## Immediately After the Pull Completes (8am–9am)

### ① Confirm Enrollment Count
The terminal output shows how many contacts were pulled and enrolled. Look for:
```
[Danny] Enrolled: X new contacts → Property Manager sequence
[Carla] Enrolled: X new contacts → Contractor sequence
```
Target: 100–300+ new contacts enrolled across Danny + Carla. If 0 — call immediately.

### ② Run Pending Enrollment (if Gas Station/Fleet Sequences Are Now Live)
If you created the Gas Station + Fleet sequences in Mixmax UI last night:
```bash
python3 workers/lead_pipeline.py pending
```
This enrolls the 12+ gas station + fleet contacts that have waited since May 15. Takes 2 minutes.

### ③ Check Mixmax — Confirm Enrollments Appear
- Open `app.mixmax.com → Sequences → Property Manager sequence`
- Confirm new contacts show in the "Enrolled" tab with today's date
- If contacts don't appear within 30 minutes → check the terminal output for API errors

### ④ Run Nina's Daily Report
```bash
python3 workers/nina_report.py daily
```
Confirms enrollment counts are visible in the pipeline. File: `outputs/nina/hot_leads_2026-06-08.md`

---

## Post-Pull Timeline — What to Expect

| Day | What Happens |
|-----|-------------|
| **June 8 (Today)** | Contacts enrolled. Touch 1 emails scheduled. |
| **June 9-10** | First Touch 1 emails send (Mixmax sends on schedule). No action needed. |
| **June 11-13** | **First opens expected.** Hospital FM, YMCA, museum, govt contacts who opened Touch 1 will appear in Nina's hot leads report. |
| **June 11-13** | Connect on LinkedIn with any contact who opened 2+ times. Use `outputs/tommy/hot_lead_linkedin_dm_playbook_2026-05-18.md`. |
| **June 14-15** | Mixmax sends Touch 2 to contacts who haven't replied to Touch 1. No action needed. |
| **June 15 (Mon)** | **Lake County pull** — `run_lake_both.command` (marina/waterfront corridor). |
| **June 18-20** | Second wave of opens (Touch 2 opens). LinkedIn connect pace picks up. |
| **June 21-22** | First replies expected from highest-intent contacts. |
| **June 22 (Mon)** | **Lorain County pull** — `run_lorain_both.command` (Avon growth corridor). |
| **June 28-29** | Touch 3 fires for earliest-enrolled Cuyahoga contacts. |

---

## What the Hottest Leads Look Like (First 2 Weeks)

The June 8 Cuyahoga pull will produce hot leads that look different from the Summit/Medina pulls. Here's what to watch for:

### Tier 1 — Drop Everything Leads
| Signal | What It Means | Action |
|--------|--------------|--------|
| Hospital FM: 3+ opens | Cleveland Clinic / UH / MetroHealth facility director — $20K+ account potential | LinkedIn connect within 2 hours. Use senior facility compliance angle. |
| YMCA Director: 2+ opens | YMCA of Greater Cleveland — 12 branches, one deal = $15K-$30K/year | DM: "Noticed you opened our email about exterior cleaning for YMCA branches..." |
| Museum: 2+ opens | Rock Hall / CMA / Great Lakes Science Center — donor events = appearance non-negotiable | Personal email from Bradley: compliance + donor event angle |
| DSO dental group: 2+ opens | 10-20 clinic district deal | Call same day. Use: "ORC dental licensing = exterior appearance standard" |
| Sports venue: 2+ opens | Rocket Mortgage FieldHouse / Progressive Field FM | Connect immediately — single contract = $15K-$50K/year |

### Tier 2 — Follow the Sequence, Then DM
- Transit agency contacts (GCRTA) — large contracts, long sales cycle, patience wins
- School district facilities directors — summer maintenance budget window open now
- Municipal facility managers — small direct-award contracts common

---

## Revenue Projections From This Pull

| Segment | Contacts Expected | Deals Likely | Revenue/Deal | Pipeline Value |
|---------|------------------|-------------|-------------|----------------|
| Commercial PM / HOA | 40-80 | 3-5 | $1,500-$4,000 | $4.5K-$20K |
| Senior/Assisted Living | 15-30 | 2-3 | $3,000-$8,000 | $6K-$24K |
| Distribution/Warehouse | 20-40 | 2-4 | $3,000-$10,000 | $6K-$40K |
| Hospital/Health System | 10-20 | 1-2 | $10,000-$40,000 | $10K-$80K |
| Government/Municipal | 15-25 | 1-3 | $2,000-$8,000 | $2K-$24K |
| Schools (summer window) | 10-20 | 1-2 | $5,000-$20,000 | $5K-$40K |
| DSO Dental Groups | 10-20 | 1-2 | $6,000-$15,000 | $6K-$30K |
| **TOTAL** | **120-235+** | **11-21** | | **$39.5K-$258K** |

---

## If Something Went Wrong — Troubleshooting

### Pull returned 0 contacts
1. Check `.env` for `APOLLO_KEY` — make sure it's present and valid
2. Run manually: `python3 workers/lead_pipeline.py danny Cuyahoga`
3. Check `logs/cron.log` for the error

### Enrollment returned 0
1. Check `MIXMAX_TOKEN` in `.env`
2. Verify the Property Manager sequence ID is still correct in `integrations/mixmax.py` line 31
3. Run manually: `python3 workers/lead_pipeline.py pending`

### Terminal showed API errors
1. Note the exact error message
2. If Apollo API: check if you've hit the monthly search limit
3. If Mixmax API: check if the sequence is in "active" or "paused" state in the UI

---

## Next Scheduled Actions This Week

| Date | Action | Time |
|------|--------|------|
| **June 9 (Tue)** | Check Nina's daily report — confirm Touch 1 sending | 8am auto |
| **June 11 (Thu)** | First opens check — look for hot leads in Nina report | 8am auto |
| **June 11-13** | LinkedIn connect with any 2+ open contacts | 10 min/day |
| **June 15 (Mon)** | Lake County pull — `run_lake_both.command` | 7:30am |
| **June 15 (Mon)** | Nina weekly pipeline report — confirms Cuyahoga enrollment | 8:30am auto |

---

*Generated by Vera Cole | June 8, 2026 | Run 199*
