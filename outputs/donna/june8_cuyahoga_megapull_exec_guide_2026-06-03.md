# June 8 Cuyahoga Mega-Pull — Execution Guide
**Prepared by Vera Cole | Run 191 | 2026-06-03**
**Target date: Sunday June 8, 2026 | Week 24**

---

## Why This Pull Is Different

June 8 is not a routine county pull. It is the highest-volume commercial lead event of the entire year:

- **176+ commercial segments** — every segment added since launch fires on Cuyahoga County first
- **Cuyahoga County density** — Cleveland Clinic, University Hospitals, Progressive Field, Rocket Mortgage FieldHouse, Rock & Roll Hall of Fame, Cleveland Hopkins Airport, 50+ charter school campuses, Tri-C (Metro/Western/Eastern campuses), Costco Westlake/Macedonia, GCRTA depots, 100+ chain gym locations — all in a single county
- **Segments never pulled before** — every segment added run 131–191 (YMCA, car auctions, coin laundries, cannabis dispensaries, swimming pools, dollar stores, auto parts chains, etc.) hits Cuyahoga for the **first time** on June 8
- **Estimated contacts returned**: 800–1,400+ new leads (vs. 200–350 for a typical single-county pull)
- **Runtime**: 12–20 minutes minimum; Danny's 50-title batching runs many Apollo calls in sequence

---

## Night-Before Checklist (Evening of June 7, Sunday)

Do these the night before so June 8 morning is execution-only, no scrambling.

### 1. Confirm `.env` credentials are current
```
cat /Users/bradleyneal/forestcity/.env | grep -E "APOLLO|MIXMAX|SLACK|GITHUB"
```
All four must be present and non-empty. If APOLLO_KEY is expired, the pull returns 0 leads silently.

### 2. Confirm `photo_pairs.json` has no stuck unprocessed pairs
```
cat /Users/bradleyneal/forestcity/logs/photo_pairs.json | python3 -m json.tool | grep '"processed"' | grep false
```
If any pairs show `"processed": false`, run Jasmine first so she doesn't compete with the pull for resources.

### 3. Check `contacts_cache.json` is not corrupted
```
python3 -c "import json; d=json.load(open('/Users/bradleyneal/forestcity/logs/contacts_cache.json')); print(f'{len(d)} cached contacts')"
```
Should return a number ≥ 1,000. If it throws a JSON error, delete the file — it will regenerate on the pull.

### 4. Confirm Instantly.ai campaigns are PAUSED
Log into Instantly.ai and verify campaigns **a1c08c3d** and **626cd15d** both show `PAUSED` status.
If either is still running, June 8 enrollment will create duplicate sequences = spam filter hits = 0% reply rate.
**This is the single most important pre-flight check.**

### 5. Confirm gas station + fleet sequences are either LIVE or properly PENDING
Check `integrations/mixmax.py` — if `gas_station` and `fleet_washing` IDs are still `'PENDING'`, those contacts will be collected but NOT enrolled. That is acceptable — they queue in `logs/contacts_cache.json` for manual enrollment later.

### 6. Run a quick dry-run to verify Apollo connectivity
```
python3 workers/lead_pipeline.py danny Cuyahoga --dry-run 2>&1 | head -30
```
If `--dry-run` flag is not supported, just confirm the script imports cleanly:
```
python3 -c "import workers.lead_pipeline; print('OK')"
```

### 7. Clear the activity log of Run 191+ noise (optional but recommended)
The log will grow fast during a 176-segment pull. Having a clean starting point helps trace errors.
```
wc -l /Users/bradleyneal/forestcity/logs/activity.log
```
If it exceeds 5,000 lines, archive it:
```
cp /Users/bradleyneal/forestcity/logs/activity.log /Users/bradleyneal/forestcity/logs/activity_archive_$(date +%Y%m%d).log
echo "" > /Users/bradleyneal/forestcity/logs/activity.log
```

---

## Morning-of Execution (June 8)

### Step 1 — Danny + Carla Combined Pull (recommended)
Run both workers in a single command for Cuyahoga County:
```
cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Cuyahoga
```
Or double-click in Finder:
```
scripts/run_cuyahoga_both.command
```

**Expected output during run:**
- Danny: `Cuyahoga batch 1/N (50 titles)... N contacts found`
- Danny: repeats for each batch (expect 8–12 batches for 176+ segments × 50 titles/batch)
- Carla: `Cuyahoga contractors pull... N contacts found`
- Total runtime: 12–20 minutes

**Watch for these warning signs:**
- `Apollo API error: 429` → rate limited; wait 60 seconds and resume
- `0 contacts found` for 3+ consecutive batches → APOLLO_KEY may have expired; check `.env`
- `Mixmax enrollment failed` → sequence ID issue; check `integrations/mixmax.py` SEQUENCES dict

### Step 2 — Verify contact counts
```
python3 -c "
import json
d = json.load(open('/Users/bradleyneal/forestcity/logs/contacts_cache.json'))
print(f'Total cached contacts: {len(d)}')
by_seq = {}
for c in d.values():
    seq = c.get('sequence', 'unknown')
    by_seq[seq] = by_seq.get(seq, 0) + 1
for seq, count in sorted(by_seq.items(), key=lambda x: -x[1]):
    print(f'  {seq}: {count}')
"
```
Expected: property_manager will be the largest bucket (600–1,000+), realtor and contractor will be smaller.

### Step 3 — Enroll pending contacts immediately
If any contacts landed in `pending` status (gas_station or fleet_washing sequences still PENDING):
```
python3 workers/lead_pipeline.py pending
```
This enrolls any contacts that were collected but not yet enrolled due to PENDING sequence IDs.

### Step 4 — Run Nina's daily report to confirm enrollment
```
python3 workers/nina_report.py daily
```
Nina will report how many Mixmax recipients are now in each active sequence. Confirm the number jumped by the expected amount.

### Step 5 — Git commit and push outputs
```
cd /Users/bradleyneal/forestcity && git add outputs/ logs/ && git commit -m "June 8 Cuyahoga mega-pull — 176+ segments" && git push origin main
```

---

## What Fires on June 8 for the First Time

These segments have **never been pulled in Cuyahoga County before** and will generate fresh contacts with zero prior touchpoints:

| Run Added | Segment | Key NE Ohio Targets |
|-----------|---------|---------------------|
| 131 | YMCA & Community Centers | YMCA Greater Cleveland 12+ branches |
| 133 | Car Auctions & Vehicle Wholesale | Manheim Cleveland (Cox Automotive) |
| 135 | Cannabis Dispensaries | Ohio rec cannabis — dispensaries opening monthly |
| 136 | Community Swimming Pools | Municipal rec pools in 20+ suburbs |
| 136 | Dollar Stores | Dollar General 100+ NE Ohio, Family Dollar |
| 136 | Auto Parts Stores | O'Reilly 50+ NE Ohio, AutoZone 60+ |
| 136 | Hardware & Home Improvement | Home Depot 20+ NE Ohio, Lowe's 15+ |
| 137 | Wireless & Telecom Retail | AT&T, Verizon, T-Mobile strip mall stores |
| 139 | Optical/Vision Centers | LensCrafters, MyEyeDr, Visionworks |
| 139 | Medical/Clinical Labs | Quest Diagnostics, LabCorp |
| 140 | Coffee & Drive-Through Chains | Starbucks, Dunkin', Tim Hortons |
| 143 | Ambulatory Surgery Centers | Cleveland Clinic surgery centers |
| 143 | Boutique Fitness | Orangetheory, F45, Club Pilates |
| 146 | Ice Cream Chains | Dairy Queen, Handel's, Cold Stone |
| 148 | Trampoline Parks | Sky Zone, Urban Air |
| 150 | Behavioral Health Clinics | Signature Health 30+ NE Ohio sites |
| 154 | Charter Schools | 50+ campuses in Cleveland alone |
| 155 | Ice Rinks & Hockey Facilities | Palace Ice Arenas, OBM Arena |
| 158 | Animal Shelters | Cleveland APL Tremont campus |
| 159 | Senior Adult Day Programs | 60+ NE Ohio programs |
| 159 | Diagnostic Imaging Centers | HealthSpan Radiology, UH Radiology |
| 160 | Non-Profit Organizations | Salvation Army, Catholic Charities |
| 162 | Tutoring Centers | Kumon, Sylvan, Mathnasium |
| 163 | Pawn Shops & Cash Advance | Cashland, Advance America |
| 164 | Big Box Electronics | Best Buy 10+ NE Ohio |
| 164 | Rent-to-Own Chains | Rent-A-Center 25+ NE Ohio |
| 165 | Insurance Agency Offices | State Farm, Allstate, Erie |
| 168 | Community Colleges | Tri-C Metro/Western/Eastern |
| 169 | Skilled Nursing Facilities | ProMedica Senior Care Cuyahoga |
| 171 | Fire Stations | Cleveland Fire 26 stations |
| 175 | Restaurant Equipment Supply | Eastern Restaurant Supply, Wasserstrom |
| 176 | Specialty Chemical Plants | Lubrizol Wickliffe, Materion Mayfield |

---

## If Something Goes Wrong

**Apollo returns 0 contacts:**
1. Check API key: `echo $APOLLO_KEY` in terminal after sourcing `.env`
2. Check network: `curl -I https://api.apollo.io` — should return 200
3. If 403: Apollo key expired; log into Apollo.io and regenerate

**Mixmax enrollment fails for all contacts:**
1. Check MIXMAX_TOKEN: `echo $MIXMAX_TOKEN`
2. Check sequence IDs in `integrations/mixmax.py` — property_manager ID should be `6a048cfc110bc620ca0f1aee`
3. Test enrollment manually: `python3 workers/lead_pipeline.py pending`

**Pull runs but only returns 50–100 contacts (much lower than expected):**
Apollo may be rate-limiting or the county name spelling is off. Verify:
```
python3 -c "from workers.lead_pipeline import DANNY_SEARCHES; [print(s['county']) for s in DANNY_SEARCHES]"
```
County should match Apollo's exact spelling: "Cuyahoga County" (with "County" suffix).

**Git push fails:**
```
git -C /Users/bradleyneal/forestcity push origin main --force-with-lease
```

---

## Post-Pull: What to Expect

- **Day 0 (June 8)**: Mixmax Touch 1 sends immediately after enrollment
- **Day 3 (June 11)**: First open data available in Nina's daily report
- **Day 5–7 (June 13–15)**: Touch 2 fires for all enrolled contacts
- **Day 10–14 (June 18–22)**: Reply window opens — first commercial responses expected
- **June 8 metric target**: 800+ new contacts enrolled across all active sequences

---

*Guide generated by Vera Cole | Run 191 | 2026-06-03*
*Next review: June 8 post-pull retrospective*
