# Wednesday May 27 — Afternoon Action Card
*Vera Cole | Run 108 | 2026-05-27*

---

## 🚨 SUMMIT COUNTY — 4 DAYS LEFT (Deadline: May 31)

Summit pull is 12 days overdue. Every day of delay = fewer fresh Summit leads for June 4 enrollment.  
**Runs unattended in 6 minutes:**

```bash
cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py danny Summit
```
Or double-click: **scripts/run_summit_pull.command** in Finder.

> If Summit is missed, it doesn't come back until July 6 (after Medina June 1, Geauga+Portage June 8, Cuyahoga June 15, Lake June 22, Lorain June 29). All new commercial segments — restaurants, banks, gyms, medical offices, event venues, auto body — miss peak season in Summit County.

---

## ⛽ GAS STATION SEQUENCE — 12 CONTACTS WAITING (30-min task)

12 gas station contacts in the pipeline (Jim Lavigne/Certified Oil, Kevin Kayden/Speedway, Mark Elyden/TrueNorth, and 9 more) cannot be enrolled until you create the Mixmax sequence.

**Guide:** `outputs/danny/gas_station_sequence_create_now_2026-05-27.md`

Steps:
1. Open Mixmax → Sequences → New → name it "Forest City Power Washing — Gas Station & C-Store Outreach"
2. Build 3-touch sequence (copy is already written in the guide)
3. Copy the sequence ID from the URL
4. Open `integrations/mixmax.py` line 54 → paste ID replacing `'PENDING'`
5. Run: `python3 workers/lead_pipeline.py pending` — enrolls all 12 instantly

---

## 🏃 20 CONTACTS DUE TODAY — Quick Execution Guide

### Block 1 — Contractor Texts (15 min)
These 3 contractor referral contacts need immediate outreach:

**Bryan | CLE Lawn Care Plus** (Contacted 14+ days ago — high close-loss risk)
```
Hey Bryan, following up one more time on the referral partnership idea — you send us a customer, we pay you $50 cash, no paperwork. A lot of landscapers are using us during their peak season to add revenue without extra overhead. Worth 5 minutes this week?
```

**Bulletproof Lawncare** (Contacted — no reply)
```
Hey [name], quick question — do you ever get asked by customers about power washing or driveway cleaning? We pay a $50 referral fee, no strings. Happy to grab coffee and explain how it works.
```

**Damrons Landscaping** (Contacted — no reply)
```
Hey [name], we pay $50 cash for any customer you send us that books a job. No forms, no hassle. If you've got customers asking about exterior cleaning this spring, we'd love to be your go-to referral. Sound useful?
```

### Block 2 — Wave 2 Contractor Texts (30 min)
4 Tier 1 New Leads due today — first-touch texts:  
See: `outputs/vera/wave2_contractor_blitz_may28_2026-05-27.md` for exact copy by trade type.

### Block 3 — Past Customer Blast (15 min)
Fast revenue. 5 copy-paste texts to past customers.  
See: `outputs/tommy/past_customer_june_blast_2026-05-27.md`

---

## 📊 PIPELINE SNAPSHOT (May 27)
- Total manual contacts: 36
- Untouched (never contacted): 33
- Due today: 20
- Contacted: 3 (Bryan, Bulletproof, Damrons)
- Enrolled in Mixmax: Pending (Summit + Medina pulls needed)

---

## ⏰ THIS WEEK PRIORITY STACK

| Priority | Task | Time | Revenue Potential |
|----------|------|------|------------------|
| 🔴 #1 | Summit County Pull | 6 min | $9K-$21K leads |
| 🔴 #2 | Bryan / Bulletproof / Damrons texts | 15 min | $600-$1,800/referral |
| 🔴 #3 | Gas Station Mixmax sequence | 30 min | $12 contacts enrolled |
| 🟡 #4 | Past customer blast | 15 min | $1,800-$3,000 |
| 🟡 #5 | Wave 2 contractor texts (16 contacts) | 45 min | $11K-$28K referral pipeline |
| 🟢 #6 | Medina pull (June 1) | 6 min | New commercial segments |

---

*Next milestone: June 4 — Round 2 Mixmax enrollment. Summit + Medina leads must be pulled BEFORE then.*
