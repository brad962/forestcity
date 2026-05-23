# Gas Station Sequence — Mixmax Creation Guide
### Danny Malone | 2026-05-23
*18 contacts ready and waiting. This is a 5-minute task to unlock a new revenue segment.*

---

## Why Now
- 18 district manager contacts pulled May 19 (file: `outputs/danny/leads_gas_stations_2026-05-19.md`)
- District managers control 5–15 locations each → one deal = recurring multi-site revenue
- Sequence copy is fully written: `outputs/danny/sequence_gas_stations_2026-05-19.md`
- Mixmax ID = PENDING. Only Bradley can create the sequence in the Mixmax UI.
- Once ID is pasted into `integrations/mixmax.py`, run: `python3 workers/lead_pipeline.py pending` → all 18 contacts auto-enroll in 2 minutes.

---

## Step-by-Step: Create the Sequence in Mixmax

**Time required:** ~5 minutes

### Step 1 — Open Mixmax Sequences
Go to: https://app.mixmax.com/sequences
Click **"+ New Sequence"**

---

### Step 2 — Name the Sequence
Exact name to use:
```
Forest City Power Washing — Gas Station & C-Store Outreach
```

---

### Step 3 — Add Recipients (skip for now — you'll do this programmatically)
Leave empty. You'll enroll the 18 contacts via script after the ID is created.

---

### Step 4 — Configure Email 1

**Subject line:**
```
Quick question for you — [company] locations in Northeast Ohio
```
*Note: Use Mixmax variable {{company}} in place of [company]*

**Body:**
```
Hi {{firstName}},

I wanted to reach out because we do exterior cleaning for a number of gas stations and c-stores in Northeast Ohio — canopy washing, lot cleaning, dumpster pad cleanup. Keeps the locations looking sharp and compliant.

Quick question: do you handle vendor decisions for your Ohio locations, or is that managed at the district or regional level?

Happy to share a few examples if it's relevant.

Bradley
Forest City Power Washing
[phone number]
```

**Send timing:** Immediately

---

### Step 5 — Add Email 2 (follow-up, Day 5)

**Subject line:**
```
Re: [company] locations
```

**Body:**
```
Hi {{firstName}},

Following up on my note from last week. I know you're managing multiple locations so I'll keep this short — we handle exterior cleaning for gas stations and c-stores in NE Ohio, priced per-location with volume discounts for district managers.

Would a quick 10-minute call make sense?

Bradley
```

**Send timing:** 5 business days after Email 1

---

### Step 6 — Add Email 3 (final follow-up, Day 10)

**Subject line:**
```
Last note — [company] exterior cleaning
```

**Body:**
```
Hi {{firstName}},

One last reach-out. If exterior cleaning for your Ohio locations is handled elsewhere or not a priority right now, totally understand — just wanted to make sure this landed.

If timing changes, we're at [phone number].

Bradley
Forest City Power Washing
```

**Send timing:** 5 business days after Email 2

---

### Step 7 — Save Sequence and Copy the ID

After saving, the sequence will appear in your Mixmax sequence list. The **Sequence ID** is in the URL:
```
https://app.mixmax.com/sequences/[SEQUENCE_ID_HERE]
```

Copy that ID. It's a 24-character string like: `6a048cfd624a5989a68ba16c`

---

### Step 8 — Paste ID into mixmax.py

Open: `integrations/mixmax.py`

Find this block (around line 54):
```python
'gas_station': {
    'id': 'PENDING',
    ...
}
```

Replace `'PENDING'` with your copied ID:
```python
'gas_station': {
    'id': '6a048cXXXXXXXXXXXXXXX',   ← paste your ID here
    ...
}
```

Save the file.

---

### Step 9 — Enroll All 18 Contacts

Run this command from your forestcity directory:
```bash
python3 workers/lead_pipeline.py pending
```

This will enroll all 18 contacts automatically. You'll see each enrollment confirmed in the terminal.

---

### Step 10 — Confirm Enrollment

Open Mixmax → Sequences → Gas Station sequence.
Should show 18 recipients added. Done.

---

## What This Unlocks
| Metric | Value |
|--------|-------|
| Contacts ready to enroll | 18 |
| Avg locations per district manager | 5–15 |
| Potential jobs if 2 DMs reply | 5–30 locations |
| Revenue per location per clean | $150–400 |
| Estimated pipeline value | $750–$12,000+ |

---

*Sequence copy reference: `outputs/danny/sequence_gas_stations_2026-05-19.md`*
*Leads file: `outputs/danny/leads_gas_stations_2026-05-19.md`*
