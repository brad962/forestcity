# Ad Lead Tracker — Logging Facebook & Google Leads
### Nina Kowalski | RevOps | 2026-05-25
*Ads are live. Every Facebook and Google lead needs to be in pipeline_data.json so Nina's weekly report can see it.*

---

## Why This Matters

Facebook Lead Gen form submissions and Google Ads calls don't automatically appear in any report. If you don't log them, the AI system doesn't know they exist — Nina's pipeline health shows 0 ad leads even if you've booked 5 jobs this week. This 60-second process fixes that.

---

## How to Add an Ad Lead to pipeline_data.json

**File location:** `/Users/bradleyneal/forestcity/pipeline_data.json`

Open the file in any text editor (TextEdit, VS Code, etc.). Find the `"manual_contacts"` array. Add a new entry at the **top** of the array (after the `[`).

### Copy-Paste Template

```json
{
  "first_name": "FIRST",
  "last_name": "LAST",
  "company": "",
  "phone": "XXX-XXX-XXXX",
  "email": "email@example.com",
  "lead_source": "facebook_ad",
  "stage": "New Lead",
  "last_contact": "2026-05-25",
  "next_followup": "2026-05-26",
  "notes": "Facebook Lead Gen form — interested in house washing",
  "revenue": 0
},
```

**`lead_source` options:**
- `"facebook_ad"` — Facebook Lead Gen form submission
- `"google_ad"` — Google Ads call or website click
- `"google_guaranteed"` — Google Local Services Ad call
- `"organic"` — website form, Facebook comment, word of mouth

---

## Pipeline Stages for Ad Leads

Ad leads move faster than cold outbound. Expected timeline:

| Stage | Trigger | Time |
|-------|---------|------|
| **New Lead** | Lead form submitted / call comes in | Immediate |
| **Contacted** | You called or texted back | Same day (within 5 min for max conversion) |
| **Estimate Sent** | You gave a quote | Day 1–3 |
| **Booked** | They said yes | Day 1–7 |
| **Completed** | Job done | Job date |

### Updating Stage

Each time a lead moves:
```json
"stage": "Contacted",
"last_contact": "2026-05-26",
"next_followup": "2026-05-29",
"notes": "Called back — interested in full exterior. Sending estimate."
```

---

## What Nina's Report Shows

Once a contact is in `pipeline_data.json`, Nina's weekly pipeline report (`workers/nina_report.py weekly`) shows:

- **Untouched contacts** (New Lead, no last_contact > 2 days)
- **Stale Contacted** (Contacted > 7 days ago, no next_followup set)
- **Overdue follow-ups** (next_followup ≤ today)

If an ad lead sits in "New Lead" for more than 48 hours without a `last_contact` date, Nina flags it as untouched. This is your catch-net.

---

## Revenue Tracking

When a lead books:
```json
"stage": "Booked",
"revenue": 350,
"job_date": "2026-05-30"
```

Nina's Workiz report tracks completed jobs. The pipeline_data.json entry tracks the sales funnel. Both together = full picture from lead to revenue.

---

## Quick Steps (60 seconds)

1. Open `pipeline_data.json` in any editor
2. Find `"manual_contacts": [`
3. After the `[`, paste the template above
4. Fill in: name, phone, email, lead_source, notes
5. Set stage: `"New Lead"`
6. Set last_contact: today's date
7. Set next_followup: tomorrow (call within 5 min → set next_followup = 2 days out)
8. Save file

That's it. The next time Nina's report runs, this contact appears.

---

## Week 1 Target (May 26 – June 1)

| Source | Goal | Notes |
|--------|------|-------|
| Facebook ads | 3–10 leads | Lead Gen form → check Facebook Leads Manager |
| Google ads | 1–5 calls | Phone rings directly — answer live if possible |
| Google Guaranteed | 1–3 leads | Once badge approved (7–14 days) |
| Organic | 1–3 | Facebook comments, word of mouth, GBP |

If you book 2+ jobs in week 1, ads are working. Scale budget $5–10/day after Day 7 check.
