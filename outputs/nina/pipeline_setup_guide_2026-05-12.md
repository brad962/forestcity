# HubSpot Pipeline Setup Guide
### Forest City Power Washing
*Nina Kowalski | RevOps Manager | 2026-05-12*

---

## Overview

This guide sets up a clean, functional HubSpot CRM for Forest City Power Washing. Once you add your HubSpot token to CLAUDE.md, I can automate contact imports from Danny and Carla's lead lists. For now, here's the complete setup spec so you can get it configured manually in about 30–45 minutes.

---

## Step 1: Create Your Deal Pipeline

**Go to:** Settings → Objects → Deals → Pipelines → Create Pipeline

**Pipeline name:** Forest City Sales Pipeline

### Stages (in order)

| Stage Name | Stage Description | Win Probability |
|-----------|-------------------|-----------------|
| New Lead | Just entered — Danny outbound, Carla referral, or inbound form fill | 10% |
| Contacted | First email or call sent. We've made contact. | 20% |
| Replied | Prospect responded (positive or asking questions). Real signal. | 35% |
| Estimate Sent | Quote delivered via email or on-site | 55% |
| Follow-Up | Waiting on their decision. Last contact was our estimate. | 65% |
| Closed Won | Booked job — deposit or firm date confirmed | 100% |
| Closed Lost | Not booking. Log the reason (price / timing / competitor / no response) | 0% |

---

## Step 2: Custom Contact Properties

**Go to:** Settings → Properties → Contact Properties → Create Property

Create these custom fields:

### Forest City Custom Fields

| Property Name | Field Type | Options |
|--------------|-----------|---------|
| Lead Source | Dropdown | Danny Outbound / Carla Referral / Inbound Form / Walk-in / Referral (customer) / Other |
| Property Type | Dropdown | Residential / Commercial / HOA / Multi-Family |
| County | Dropdown | Cuyahoga / Lake / Lorain / Medina / Summit / Geauga / Portage / Other |
| Services Interested In | Checkbox | House Washing / Roof Soft Wash / Driveway / Deck or Fence / Commercial Building / Full Package |
| Estimated Job Value | Number | (dollar amount) |
| Last Contact Date | Date | |
| Next Follow-Up Date | Date | |
| Notes | Multi-line text | (freeform) |
| Job Completed | Checkbox | Yes/No |
| Review Requested | Checkbox | Yes/No |

---

## Step 3: Deal Properties

**Create these on the Deal object:**

| Property Name | Field Type |
|--------------|-----------|
| Job Address | Single-line text |
| Service(s) Quoted | Checkbox (same options as above) |
| Quote Amount | Number |
| Job Date | Date |
| Source Worker | Dropdown: Danny / Carla / Inbound / Bradley |
| Loss Reason | Dropdown: Price / Timing / Competitor / No Response / Other |

---

## Step 4: Required Views (Save These Filters)

### View 1: "Hot Leads" Dashboard
**Filter:** Deal Stage = Replied OR Estimate Sent | Last Modified Date = Last 7 days
**Sort by:** Last Modified Date (newest first)
**Purpose:** What needs attention today

### View 2: "Stale Leads" Alert
**Filter:** Deal Stage ≠ Closed Won / Closed Lost | Last Contact Date = More than 5 days ago
**Sort by:** Last Contact Date (oldest first)
**Purpose:** Bradley needs to see these every Monday

### View 3: "Danny's Pipeline"
**Filter:** Source Worker = Danny
**Group by:** Deal Stage
**Purpose:** Danny's performance by stage

### View 4: "Carla's Referral Pipeline"
**Filter:** Lead Source = Carla Referral
**Group by:** Deal Stage
**Purpose:** Track referral partner ROI

### View 5: "Spring 2026 Campaign"
**Filter:** Create Date = March 1, 2026 – May 31, 2026
**Purpose:** Campaign-period performance

---

## Step 5: Email Templates to Load in HubSpot

Load these into Settings → Tools → Templates:

1. **Estimate Follow-Up — Same Day** (see Tommy's output file)
2. **Estimate Follow-Up — Day 2**
3. **Estimate Follow-Up — Day 5 (Last Touch)**
4. **Post-Job Review Request**
5. **Referral Thank-You (from Carla)**

---

## Step 6: Task Automation (Manual Until Zapier Is Connected)

Until Zapier automation is live, Bradley should manually:

1. When a deal moves to **Estimate Sent** → create a task: "Follow up in 2 days"
2. When a deal moves to **Closed Won** → create a task: "Send review request in 24 hours"
3. Every Monday → check Stale Leads view and create follow-up tasks

---

## Step 7: Weekly Reporting Rhythm

**Every Monday, run this check:**

1. Open "Stale Leads" view — anything not contacted in 5+ days
2. Open "Hot Leads" view — anything in Replied or Estimate Sent
3. Check deals Closed Won last week → log job value
4. Check deals Closed Lost → log reason (this is gold for Marcus's research)
5. Review pipeline value by stage (sum of Estimate amounts)

---

*Nina Kowalski | Forest City Power Washing | 2026-05-12*
