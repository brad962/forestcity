# Mixmax Sequence Setup Guide
### Create Gas Station & Fleet Sequences — 20 Minutes Total
*Vera Cole | Run this once. It unlocks 30 contacts for auto-enrollment.*

---

## Why This Matters

All the infrastructure is built. The copy is written. The leads are pulled.

The ONLY thing blocking 18 gas station contacts and 12 fleet prospects from getting automated email outreach is a Mixmax sequence ID in `integrations/mixmax.py`.

Once you paste the IDs, running `python3 workers/lead_pipeline.py both` auto-enrolls everyone.

This guide takes 20 minutes. Gas station sequence alone = 18 multi-site district managers who control 5–15 locations each.

---

## SEQUENCE 1: Gas Station & C-Store Outreach (~10 minutes)

### Step 1 — Open Mixmax
Go to: mixmax.com → Sign in → click **Sequences** in the left sidebar

### Step 2 — Create New Sequence
Click **+ New Sequence** (top right)

### Step 3 — Name It
Name: `Forest City Power Washing — Gas Station & C-Store Outreach`

### Step 4 — Add Touch 1 (Email)
- Click **+ Add Step** → Select **Email**
- **Send on Day:** 1
- **Subject:** `Gas station canopy cleaning — NE Ohio`
- **Body:** Copy from `outputs/danny/sequence_gas_stations_2026-05-19.md` → Touch 1 section
- Replace `{{firstName}}` with Mixmax variable → Map to `firstName` field
- Replace `{{company}}` → Map to `company` field

### Step 5 — Add Touch 2 (Email, +5 days)
- Click **+ Add Step** → Email
- **Send on Day:** 6
- **Subject:** `Re: Gas station canopy cleaning`
- **Body:** Copy Touch 2 section from `outputs/danny/sequence_gas_stations_2026-05-19.md`

### Step 6 — Add Touch 3 (Email, +7 days)
- **Send on Day:** 13
- **Subject:** Copy Touch 3 subject from the sequence file
- **Body:** Copy Touch 3 body

### Step 7 — Save & Get the ID
Click **Save Sequence**

The sequence URL will look like:
`https://app.mixmax.com/sequences/6a048cXXXXXXXXXXXXXXXXXX`

**Copy that 24-character ID.**

### Step 8 — Paste ID into the code
Open `integrations/mixmax.py` in your editor

Find line ~54:
```python
'gas_station': {
    'id': 'PENDING',
```

Replace `'PENDING'` with your new ID:
```python
'gas_station': {
    'id': '6a048cXXXXXXXXXXXXXXXXXX',  ← paste your ID here
```

### Step 9 — Run the pipeline
```bash
cd /Users/bradleyneal/forestcity
python3 workers/lead_pipeline.py both
```

All 18 gas station contacts auto-enroll. You'll see them in Slack.

---

## SEQUENCE 2: Fleet Washing Outreach (~10 minutes)

### Step 1-3 — Same process, different name
Name: `Forest City Power Washing — Fleet Washing Outreach`

### Step 4-6 — Copy from fleet sequence file
Copy all 3 touches from: `outputs/danny/sequence_fleet_washing_2026-05-18.md`

Variables: `{{firstName}}`, `{{company}}`, `{{fleetType}}`
- `fleetType` maps to the `fleetType` Mixmax variable

### Step 7 — Get the fleet sequence ID
Copy the 24-character ID from the URL.

### Step 8 — Paste into code
In `integrations/mixmax.py`, find line ~47-48:
```python
'fleet_washing': {
    'id': 'PENDING',
```

Replace `'PENDING'` with the fleet sequence ID.

### Step 9 — Run again
```bash
python3 workers/lead_pipeline.py both
```

---

## After Both IDs Are Pasted

The next cloud run of Vera will automatically:
- Show gas station and fleet sequences in Nina's weekly report
- Include them in enrollment verification
- Display them on the dashboard pipeline view

**One-time setup. Permanent automation.**

---

## Troubleshooting

**"I don't see the sequence recipients after running the pipeline"**
→ Check that the sequence STATUS is "Active" in Mixmax (not Draft)
→ The pipeline only enrolls into sequences with non-PENDING IDs

**"Mixmax says contact already enrolled"**
→ That's the dedup guard working. Don't re-run — check Mixmax recipients list.

**"I pasted the ID but the pipeline still says PENDING"**
→ Make sure you saved the file and are running from `/Users/bradleyneal/forestcity`

---

*Created by Vera Cole — 2026-05-20*
*Resolves: Gas station contacts not enrolled + Fleet sequence not created (both open since 2026-05-18)*
