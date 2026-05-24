# June 4, 2026 — Round 2 Enrollment Battle Card
*Donna Park | Growth & Launch Strategist*
*Created: 2026-05-24 | Execute: June 3 (pre-check) + June 4 (launch)*

---

## What This Is
Single-page execution guide for Round 2 Mixmax enrollment. Every command is copy-paste ready.
This is NOT the plan (see `campaign_brief_june_booking_blitz`). This is the GO button.

---

## JUNE 3 EVENING — Pre-Check (5 minutes, 8pm)

Open Terminal. Run these 3 checks in sequence:

**Check 1 — Instantly.ai confirmed paused?**
```bash
grep INSTANTLY_PAUSED /Users/bradleyneal/forestcity/.env
```
Expected output: `INSTANTLY_PAUSED=true`
If missing: Go to app.instantly.ai → Campaigns → Pause a1c08c3d AND 626cd15d → add `INSTANTLY_PAUSED=true` to .env

**Check 2 — Gas station sequence ID in Mixmax?**
```bash
grep -A2 gas_station /Users/bradleyneal/forestcity/integrations/mixmax.py
```
Expected output: `'id': '6a048cXXXXXXXX...'` (not PENDING)
If still PENDING: Open Mixmax → Sequences → create "Forest City Power Washing — Gas Station & C-Store Outreach" → paste ID at line 54 of integrations/mixmax.py

**Check 3 — How many contacts are queued?**
```bash
python3 -c "import json; d=json.load(open('/Users/bradleyneal/forestcity/contacts_cache.json')); not_enrolled=[c for c in d['contacts'] if not c.get('mixmax_enrolled') and c.get('email')]; print(f'{len(d[\"contacts\"])} total | {len(not_enrolled)} pending enrollment')"
```
Expected: 60-100 total, 18+ pending (gas station + any gaps)

GO/NO-GO: If Instantly confirmed paused AND gas station ID filled in → GO for June 4.

---

## JUNE 4 MORNING — Enrollment Launch (7:00am – 8:15am)

### 7:00am — Open Terminal

```bash
cd /Users/bradleyneal/forestcity
```

---

### 7:00am – 7:12am — STEP 1: Danny Summit County Pull (12 min)

Summit County is Week 21 (May 25 – May 31). June 4 = Week 23, which rotates to Geauga+Portage.
Run Summit manually one final time to capture any remaining contacts:

```bash
python3 workers/lead_pipeline.py danny Summit
```

Expected terminal output:
```
🔵 Danny — Property Manager Lead Pull
  County batch: Summit [MANUAL OVERRIDE]
  Found XX people from Apollo
  New unique leads: 15-40
  → Logged: Danny | Apollo pull — XX new property managers in Summit...
```

If Apollo returns 0: Rate limited — skip to Step 2. Geauga+Portage auto-runs June 8 on cron.

---

### 7:15am – 7:25am — STEP 2: Carla Medina County Pull (10 min)

June 4 = Week 23 rotation = Geauga+Portage for Danny but Medina for Carla (independent rotation).
Override to Medina for peak-season referral partner density:

```bash
python3 workers/lead_pipeline.py carla Medina
```

Expected terminal output:
```
🟣 Carla — Referral Partner Lead Pull
  County batch: Medina [MANUAL OVERRIDE]
  Contractors: Found XX people | Home Services: Found XX people | Realtors: Found XX people
  Total new referral partners: 15-30
  → Logged: Carla | Apollo pull — XX new referral partners in Medina...
```

---

### 7:30am – 7:35am — STEP 3: Enroll Pending Sequences (5 min)

This enrolls gas station contacts (18 waiting since May 19) + any fleet contacts:

```bash
python3 workers/lead_pipeline.py pending
```

Expected terminal output:
```
⏳ Enrolling 18+ pending contacts now that sequences are live...
  ✅ [Name] [Company] → Forest City Power Washing — Gas Station & C-Store Outreach
  ✅ [Name] [Company] → ...
Pending sequence enrollment — 18/18 enrolled
```

If gas station sequence still PENDING: This step skips those contacts (they stay in pending). Complete Mixmax sequence creation ASAP.

---

### 7:40am – 7:45am — STEP 4: Verify Enrollment (automatic)

The lead_pipeline.py script auto-runs `verify_and_repair_enrollment()` after every pull.
Watch terminal output — look for:

```
✅ All contacts confirmed in Mixmax.
```

OR:

```
↻ Re-enrolled: [Name] [email]
  ✅ X re-enrolled | 0 could not be enrolled
```

Both are good. "X failed" means those contacts have no email — expected.

---

### 7:50am – 8:00am — STEP 5: Check the Log (2 min)

```bash
tail -20 logs/activity.log
```

You should see:
- `[2026-06-04 07:XX] Danny | Apollo pull — XX new property managers in Summit...`
- `[2026-06-04 07:XX] Carla | Apollo pull — XX new referral partners in Medina...`
- `[2026-06-04 07:XX] pipeline | Pending sequence enrollment — XX/XX enrolled`
- `[2026-06-04 07:XX] pipeline | Enrollment verification — all contacts confirmed`

---

### 8:00am – 8:15am — STEP 6: Past Customer Text Blast (15 min)

Open `outputs/tommy/past_customer_june_text_scripts_2026-05-24.md`.
Send 10 texts to past customers from your phone. Best send window: 8am-10am.
Do NOT use an automated tool for this — personal texts from your number convert 3x better.

---

## EXPECTED ROUND 2 OUTCOMES

| Segment | Contacts Enrolled | Expected Replies | Expected Jobs |
|---------|------------------|-----------------|--------------|
| Property Managers (new Summit) | 15-40 | 1-4 | 1-3 commercial |
| Referral Partners (new Medina) | 15-30 | 1-3 | 2-6 referral |
| Gas Stations (18 idle since May 19) | 18 | 1-3 | 1-2 multi-site |
| PM Round 2 (re-enrolled from Round 1) | Varies | 2-5 | 2-4 commercial |
| **Total** | **50-88** | **5-15** | **6-15** |

Revenue math: 6 jobs × $600 avg = $3,600 floor / 15 jobs × $900 = $13,500 ceiling

---

## IF SOMETHING BREAKS

**Apollo returns 0 leads:** Rate limited. Skip that worker. Run again tomorrow morning.

**Mixmax enrollment errors:** Check INSTANTLY_PAUSED=true in .env. If Instantly.ai is still running, deliverability is shot — pause it first, then re-run enrollment.

**Gas station contacts skip:** Sequence ID is still PENDING. Create it in Mixmax UI (10 min), paste ID into integrations/mixmax.py line 54, then run `python3 workers/lead_pipeline.py pending` again.

**No terminal / Mac issues:** Double-click `scripts/run_summit_both.command` in Finder — runs Danny + Carla Summit in one step.

---

## REFERENCE: Mixmax Sequence IDs
- Property Managers: `6a048cfc110bc620ca0f1aee`
- Realtors: `6a048cfba81429e5dfe55010`
- Contractors: `6a048cfd624a5989a68ba16c`
- Gas Station & C-Store: PENDING — create in Mixmax UI

---

*Donna Park | This is the EXECUTION card. Strategy: `campaign_brief_june_booking_blitz_2026-05-19.md`. Go/No-Go: `round2_enrollment_readiness_checklist_2026-05-23.md`*
