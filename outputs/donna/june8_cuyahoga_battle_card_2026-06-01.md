# June 8 Cuyahoga Battle Card
*Authored by Vera — 2026-06-01 | 7 days out*

---

## What This Day Is

June 8 is the largest single lead pull of the entire 2026 season.

Cuyahoga County = Cleveland metro — the biggest commercial market in NE Ohio. 125+ commercial segments including hospitals, museums, sports venues, car dealerships, distribution centers, DSO dental groups, government facilities, school districts, and every new segment added in runs 155-166. This pull fills 6-8 weeks of Mixmax sequence enrollments across the biggest commercial market in the region.

**Do not skip. Do not delay.**

---

## Pre-Pull Checklist (Night of June 7 — Sunday Evening)

- [ ] **Instantly.ai PAUSED** — check `.env` file: `INSTANTLY_PAUSED=true` must be present. Without this, enrollment is blocked by the safety gate in `mixmax.py`.
- [ ] **Mixmax Round 2 copy loaded** — confirm new email copy is live in Property Manager, Realtor, and Contractor sequences.
- [ ] **Gas station sequence** — if STILL pending, proceed anyway. Gas station contacts route to `pending` status and can be enrolled separately after Mixmax ID is added.
- [ ] **Fleet washing sequence** — same as gas station. Pending contacts will be skipped safely and logged.
- [ ] `scripts/run_cuyahoga_both.command` is accessible in Finder (or know the Terminal command below).
- [ ] Set a Monday morning alarm for 8:00 AM.

---

## Execution — Monday June 8, Morning

### Option A: Finder (No Terminal Required)
1. Open Finder → navigate to `forestcity/scripts/`
2. Double-click **`run_cuyahoga_both.command`**
3. A Terminal window opens and runs unattended
4. **Expected runtime: 12-20 minutes** (125 segments × multi-county batches × API pagination)
5. Do NOT close the Terminal window until it shows `✅ Done`

### Option B: Terminal
```bash
cd /Users/bradleyneal/forestcity
python3 workers/lead_pipeline.py both Cuyahoga
```

---

## What Happens During the Pull

`lead_pipeline.py both Cuyahoga` does the following in sequence:
1. **Danny batch** — Apollo searches across 125+ segments in Cuyahoga County using batched title groups (50 titles/call). Deduplicates against `contacts_cache.json`.
2. **Mixmax enrollment** — New contacts enrolled into the correct sequence (Property Manager, Realtor, or Contractor) based on title/company routing in `mixmax.py`.
3. **Carla batch** — Apollo searches for contractors and realtors in Cuyahoga County for Carla's referral pipeline.
4. **Slack report** — Auto-posts a summary to the office Slack channel with enrollment counts by segment.
5. **Git commit** — Saves output files and cache to GitHub automatically.

**You can do other things while it runs.** Just don't close the Terminal window.

---

## Expected Output

Based on previous county pulls (Summit: ~80 new contacts, Medina: ~60 new contacts), expect:
- **Cuyahoga estimate: 120-200 new Danny contacts** (largest market, most segments)
- **Carla estimate: 40-80 new contractor/realtor contacts**
- **Enrollment to Mixmax: ~80-90% of new contacts** (remainder: no email, already enrolled, or pending sequence)

---

## After the Pull — Same-Day Actions (15 min total)

1. **Read the Slack report** — check enrollment count and any errors logged.
2. **Check for `pending` contacts** — if gas station or fleet washing sequences are now live, run:
   ```bash
   cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py pending
   ```
3. **Log the pull** in `pipeline_data.json` if any contacts need manual follow-up.
4. **Post a GBP update** — Jasmine has June week 2-4 posts ready at `outputs/jasmine/facebook_posts_june_week2_4_2026-05-24.md`.
5. **Nina's daily hot leads** — run `check_replies.py` at 8:45 AM to catch any Touch 3 late replies before the new wave starts.

---

## Revenue Math

| Scenario | Contacts Enrolled | Open Rate | Replies | Est. Booked Jobs | Revenue |
|----------|-------------------|-----------|---------|------------------|---------|
| Conservative | 100 | 35% | 3% | 2-3 | $3,000-$9,000 |
| Expected | 150 | 40% | 5% | 5-8 | $7,500-$24,000 |
| Strong | 200 | 45% | 8% | 10-15 | $15,000-$45,000 |

Multi-location commercial contracts compound this: one DSO dental group contact = 10 clinics = $30,000-$60,000/year. One distribution center district = $24,000-$72,000/year.

---

## Key New Segments in This Pull (Added Runs 155-166)

Segments that were **never pulled before** and fire for the first time June 8:
- Ice Rinks & Indoor Ice Arenas (#103-#108 range)
- Staffing & Employment Agencies (#120)
- Big Box Electronics — Best Buy/Micro Center (#121)
- Rent-to-Own Chains — Rent-A-Center/Aaron's (#122)
- Insurance Agency Offices — State Farm/Allstate/Erie (#123)
- Orthopedic & Sports Medicine Clinics — OrthoNEOA/UH Ortho (#124) ← NEW this run
- Financial Advisory Offices — Edward Jones/Ameriprise (#125) ← NEW this run

Total new-segment contacts hitting Cuyahoga for the first time: estimated 30-50 contacts from segments #120-125 alone.

---

## If Something Goes Wrong

| Problem | Fix |
|---------|-----|
| Terminal shows `ENROLLMENT BLOCKED — INSTANTLY.AI NOT CONFIRMED PAUSED` | Add `INSTANTLY_PAUSED=true` to `.env` and re-run |
| `APOLLO_KEY not found` error | Check `.env` file has `APOLLO_KEY=...` entry |
| Script runs but 0 contacts enrolled | Apollo API rate limit hit — wait 5 min and re-run |
| Mixmax enrollment errors for specific contacts | Normal — contacts without email skip automatically; logged in output file |
| Terminal closes before Done | Re-run from Terminal — `contacts_cache.json` deduplication prevents re-enrollment |

---

*Next pull after June 8: Lake County — June 15. Marina/waterfront corridor.*
