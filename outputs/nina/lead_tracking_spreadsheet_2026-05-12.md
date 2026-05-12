# Manual Lead Tracking Spreadsheet
### HubSpot Stopgap — Forest City Power Washing
*Nina Kowalski | RevOps Manager | 2026-05-12*

---

## Overview

Until HubSpot is connected, this is your pipeline. It's a Google Sheets setup you can run manually — or we can automate it with Zapier once the token is in.

**What this covers:**
- All leads from Danny (property managers) and Carla (referral partners)
- Inbound leads from the website, Facebook ads, and the checklist lead magnet
- Full pipeline visibility from first contact to closed job

---

## HOW TO SET UP (5 minutes)

1. Open Google Sheets: sheets.new
2. Create these tabs (one per section below):
   - **Pipeline** (main view)
   - **Danny Leads**
   - **Carla Leads**
   - **Inbound**
   - **Weekly Summary**
3. Copy the column headers from each section below
4. Share with Bradley (edit access)

---

## TAB 1: PIPELINE (Master View)

This is the tab you look at every day. One row per lead. Sorted by Stage.

### Columns:

| Column | Type | Values / Format |
|--------|------|-----------------|
| **Lead ID** | Auto | FC-001, FC-002, ... |
| **Name** | Text | First Last |
| **Company** | Text | Company name |
| **Phone** | Text | (xxx) xxx-xxxx |
| **Email** | Text | email@domain.com |
| **Lead Source** | Dropdown | Danny Outbound / Carla Referral / Inbound Website / Facebook Ad / Checklist / Walk-in / Other |
| **Lead Type** | Dropdown | Property Manager / Realtor / Contractor / Homeowner / HOA / Commercial |
| **County** | Dropdown | Cuyahoga / Lake / Lorain / Medina / Summit / Geauga / Portage / Other |
| **Services Interested** | Text | House Wash, Roof, Driveway, Deck, Gutters, Commercial |
| **Est. Job Value** | $ | e.g. $399 |
| **Stage** | Dropdown | New Lead / Contacted / Replied / Estimate Sent / Follow-Up / Closed Won / Closed Lost |
| **Last Contact Date** | Date | MM/DD/YY |
| **Next Follow-Up** | Date | MM/DD/YY |
| **Days Since Contact** | Formula | =TODAY()-[Last Contact Date] |
| **Stale?** | Formula | =IF([Days Since Contact]>5,"⚠️ STALE","") |
| **Notes** | Text | Free-form — what happened on last contact |
| **Assigned To** | Dropdown | Bradley / Danny / Carla |

### Pipeline Stages Defined:
1. **New Lead** — just entered, no contact yet
2. **Contacted** — first email or call sent
3. **Replied** — they responded (positive or negative)
4. **Estimate Sent** — quote delivered
5. **Follow-Up** — waiting on decision, checking back
6. **Closed Won** ✅ — job booked
7. **Closed Lost** ❌ — not booking right now (note the reason)

---

## TAB 2: DANNY LEADS (Property Managers)

Pre-populate from `/outputs/danny/leads_cuyahoga_property_managers_2026-05-12.md` and the expanded county files.

### Extra columns for Danny's outbound:
| Column | Values |
|--------|--------|
| **Instantly Campaign** | ba327e77 (Danny — Property Managers) |
| **Email Touch** | Touch 1 / Touch 2 / Touch 3 / Replied |
| **Email Sent Date** | Date |
| **Opened?** | Yes / No / Unknown |
| **Replied?** | Yes — Positive / Yes — Negative / No |
| **Reply Date** | Date |
| **Manual Follow-Up Needed?** | Yes / No |

### Seed data — paste these in when building the tab:

Danny has **81 property manager leads** loaded in Instantly campaign `ba327e77`:

**Original Cuyahoga batch (24):** See `/outputs/danny/leads_cuyahoga_property_managers_2026-05-12.md`

**Expanded counties (57 new leads):**
- Lake County — ~15 leads
- Lorain County — ~15 leads
- Summit County — ~14 leads
- Medina County — ~13 leads

*Pull contact details from Instantly dashboard or `/tmp/apollo_new_contacts.json`*

---

## TAB 3: CARLA LEADS (Referral Partners)

### Extra columns for Carla's outbound:
| Column | Values |
|--------|--------|
| **Partner Type** | Contractor / Realtor |
| **Instantly Campaign** | b251be1b (Carla — Referral Partners) |
| **Email Touch** | Touch 1 / Touch 2 / Touch 3 / Replied |
| **Referrals Generated** | Number |
| **Est. Lifetime Value** | $ (3 jobs/yr × avg job value) |
| **Co-Brand Interest?** | Yes / No / Unknown |

### Carla's **33 leads** in campaign `b251be1b`:

**Contractors (~11 leads):**
Remodelers, roofers, painters, gutter crews who encounter power washing needs on every job.
See `/outputs/carla/partners_contractors_cuyahoga_2026-05-12.md`

**Realtors (~22 leads):**
NE Ohio agents who work with sellers who need pre-listing curb appeal.
*Pull from `/tmp/apollo_realtors.json`*

---

## TAB 4: INBOUND LEADS

All leads that come in from the website, Facebook ads, or lead magnets.

### Columns:
| Column | Values |
|--------|--------|
| **Date In** | Date |
| **Name** | Text |
| **Email** | Text |
| **Phone** | Text |
| **Source** | Website Form / Facebook Ad / Google Ad / Checklist Download / Referral / Other |
| **Service Requested** | Text |
| **Address / Area** | Text |
| **Est. Job Value** | $ |
| **Stage** | Pipeline stages |
| **Estimate Date** | Date |
| **Follow-Up 1** | Date |
| **Follow-Up 2** | Date |
| **Closed** | Won / Lost / Pending |
| **Job Value (Actual)** | $ |
| **Notes** | Text |

---

## TAB 5: WEEKLY SUMMARY

Run this every Monday. Takes 10 minutes.

### Template:

```
WEEK OF: [date]

=== NEW LEADS THIS WEEK ===
Danny pipeline new leads:       ___
Carla pipeline new leads:       ___
Inbound leads:                  ___
TOTAL NEW:                      ___

=== PIPELINE SNAPSHOT ===
New Lead:          ___ leads
Contacted:         ___ leads
Replied:           ___ leads
Estimate Sent:     ___ leads
Follow-Up:         ___ leads
Closed Won:        ___ jobs  |  $_____ revenue
Closed Lost:       ___ leads

=== STALE LEADS (5+ days no contact) ===
[List name, stage, days since contact, assigned to]

=== DANNY — INSTANTLY STATS ===
Campaign: Property Managers (ba327e77)
Emails sent this week:          ___
Open rate:                      ___%
Reply rate:                     ___%
Positive replies:               ___
Meetings / Calls booked:        ___

=== CARLA — INSTANTLY STATS ===
Campaign: Referral Partners (b251be1b)
Emails sent this week:          ___
Open rate:                      ___%
Reply rate:                     ___%
Active referral partners:       ___
Referral jobs this week:        ___

=== WINS THIS WEEK ===
[List closed jobs, referral conversations, notable replies]

=== BLOCKED / NEEDS BRADLEY ===
[List anything that needs a decision or action from Bradley]
```

---

## STALE LEAD RULES

Flag a lead as stale (⚠️) if:

| Stage | Stale After |
|-------|-------------|
| New Lead | 2 days |
| Contacted | 5 days |
| Replied | 2 days (hot — respond fast) |
| Estimate Sent | 3 days |
| Follow-Up | 5 days |

When a lead goes stale, it shows up in the **Stale?** column automatically (the formula above).

**Weekly action:** Every Monday, filter the Pipeline tab by Stale? = ⚠️ STALE and do outreach or close them out.

---

## WHEN HUBSPOT IS CONNECTED

When Bradley adds the HubSpot token to CLAUDE.md, Nina will:
1. Import all rows from this spreadsheet into HubSpot
2. Map columns to HubSpot contact + deal properties
3. Set up Zapier automations so new leads auto-enter the pipeline
4. Move to automated weekly reports pulled from HubSpot API

The spreadsheet is designed to match HubSpot's data model — the migration will be clean.

---

## QUICK REFERENCE — INSTANTLY CAMPAIGN IDs

| Campaign | ID | Owner | Leads |
|----------|----|-------|-------|
| Property Managers (NE Ohio) | `ba327e77-308a-4bf1-86e3-daf1a70d4c76` | Danny | 81 |
| Referral Partners (Contractors + Realtors) | `b251be1b-f3c8-4f14-803b-767fc14d7d7e` | Carla | 33 |

**To pull reply data from Instantly:**
1. Log in at app.instantly.ai
2. Go to Campaigns → select campaign → Leads tab
3. Filter by "Replied" to see hot leads
4. Copy to this spreadsheet immediately

---

## ONE-TIME SETUP CHECKLIST

- [ ] Create Google Sheet at sheets.new
- [ ] Add all 5 tabs
- [ ] Copy column headers from this doc
- [ ] Paste Danny's 24 Cuyahoga contacts into Danny Leads tab
- [ ] Pull expanded county leads from Instantly → paste in
- [ ] Paste Carla's 11 contractors into Carla Leads tab
- [ ] Paste Carla's 22 realtors into Carla Leads tab
- [ ] Add conditional formatting: Stage "Closed Won" = green, "Closed Lost" = gray, Stale = orange
- [ ] Set up weekly reminder (every Monday morning) to fill in Weekly Summary tab
- [ ] Share with Bradley

**Estimated time: 30 minutes, one time.**

---

*Nina Kowalski | Forest City Power Washing | 2026-05-12*
