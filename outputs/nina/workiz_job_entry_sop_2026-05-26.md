# Workiz Job Entry SOP
### How to Enter Jobs So They Appear in the Power Washing Report
*Nina Kowalski | RevOps Manager | 2026-05-26*

---

## The Problem

`workiz_report.py` pulls jobs filtered to Power Washing job types. If jobs are entered with a different JobType (or no JobType), they show as 0 in the report — even if revenue is real.

This SOP takes 60 seconds per job. One wrong field = job disappears from every report.

---

## CRITICAL FIELD: JobType

When creating or editing a job in Workiz, the **Job Type** field must exactly match one of these values:

### Accepted Job Types (any of these will work):
- Power Washing ✅ ← **USE THIS** (most common)
- Pressure Washing ✅
- House Washing ✅
- Roof Washing ✅
- Soft Wash ✅
- Exterior Cleaning ✅
- Driveway Washing ✅
- Deck Cleaning ✅
- Commercial Washing ✅

### Common Mistakes That Break the Report:
- "Cleaning" (too generic — not matched)
- "Service" (not matched)
- Leaving JobType blank (not matched)
- "Power Wash" without the "ing" (actually works — both accepted)
- Typos: "Power Washings" or "Preasure Washing" (not matched)

---

## HOW TO ENTER A JOB CORRECTLY

### Step 1: Create the job in Workiz
- Go to `app.workiz.com` → Jobs → New Job
- Fill in client name, address, phone

### Step 2: Set Job Type correctly
- Field label: **"Job Type"** (sometimes "Service Type" depending on your plan)
- Type: **Power Washing**
- If the field is a dropdown: scroll to find "Power Washing" — if it doesn't exist, create it (see Step 4 below)

### Step 3: Set the job price
- Field: **Job Total Price** — enter the quoted amount
- Field: **Job Amount Due** — enter what's still owed (outstanding balance)
- These two fields feed directly into the revenue report

### Step 4: If "Power Washing" isn't in the dropdown
- Go to Settings → Job Types → Add Type → Type "Power Washing" → Save
- Add the others from the accepted list above while you're there
- This is a one-time setup

---

## HOW TO FIX EXISTING JOBS

If you have jobs in Workiz that aren't showing up in the report:

1. Go to `app.workiz.com` → Jobs → All Jobs
2. Filter by date range or client name to find the job
3. Click the job → Edit
4. Update Job Type to "Power Washing" → Save
5. Run `python3 workers/workiz_report.py daily` locally — it should now appear

---

## HOW TO VERIFY THE REPORT IS WORKING

Run locally (not from cloud — Workiz API is blocked in the cloud environment):

```bash
cd /Users/bradleyneal/forestcity
python3 workers/workiz_report.py daily
```

Expected output:
```
Workiz: [X] total jobs, [X] power washing jobs
```

If you see `0 power washing jobs` but total jobs > 0: the JobType field is wrong on those jobs.

The report also logs the JobType values it sees (first 20 jobs) when 0 power washing jobs are found — that output will show you exactly what's in the field vs. what it expects.

---

## REVENUE FIELDS GUIDE

| Field in Workiz | What the Report Uses | Description |
|----------------|---------------------|-------------|
| Job Total Price | Total Job Value | Full quoted amount |
| Job Amount Due | Outstanding | What hasn't been paid |
| Job Total Price - Job Amount Due | Collected | What's been paid |
| Job Status | Status breakdown | Scheduled / In Progress / Done / Paid |
| Job Date | Upcoming / Recent | Used for 30-day upcoming + 7-day recent |

---

## DAILY REPORTING RHYTHM

The Workiz report runs Monday–Friday at 9am (if cron is set up).

To run manually at any time:
```bash
python3 workers/workiz_report.py daily
```

For a weekly view (total jobs this week):
```bash
python3 workers/workiz_report.py weekly
```

Report saves to `outputs/nina/workiz_daily_YYYY-MM-DD.md` and posts to Slack automatically.

---

## IF WORKIZ API RETURNS 0 JOBS (LOCAL RUN)

1. Check that `WORKIZ_API_TOKEN` and `WORKIZ_API_SECRET` are in `.env`
2. Check Workiz plan — some plans require a higher tier for API access
3. Try: `curl -s -H "Authorization: YOUR_SECRET" "https://api.workiz.com/api/v1/YOUR_TOKEN/job/all/"` — if it returns jobs, the script will work
4. Check job type values in the API response output (the script prints them when 0 are matched)

---

*Nina Kowalski | Forest City Power Washing AI Office*
*Generated: 2026-05-26*
