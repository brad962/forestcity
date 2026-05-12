# Zapier Automation Recipes
### Forest City Power Washing
*Nina Kowalski | RevOps Manager | 2026-05-12*

---

## Overview

These automations connect Forest City's key tools so leads flow automatically without manual data entry. Each "recipe" is a Zap — a trigger + action pair. Set these up once and they run forever.

**Tools in the stack:**
- HubSpot (CRM)
- Kit.com (email / lead magnets)
- Facebook Lead Ads (lead gen forms)
- Instantly.ai (cold email sequences — once connected)
- Google Sheets (manual backup / reporting)
- Twilio or Google Voice (SMS follow-up, optional)

---

## Recipe 1: Facebook Lead Ad → HubSpot Contact

**Trigger:** New lead in Facebook Lead Ads (any form)
**Action 1:** Create Contact in HubSpot
**Action 2:** Create Deal in HubSpot (Stage: New Lead)

**Field Mapping:**
| Facebook Form Field | HubSpot Field |
|--------------------|---------------|
| First Name | First Name |
| Last Name | Last Name |
| Email | Email |
| Phone | Phone Number |
| Address | Job Address (Deal property) |
| Service Interest | Services Interested In |

**Additional auto-tags:**
- Lead Source → "Inbound Form"
- Source Worker → "Inbound"
- Create Date → today

**Why this matters:** Every quote request from Rick's Facebook ads goes into HubSpot automatically. Bradley wakes up and all new leads are already in the pipeline.

---

## Recipe 2: Kit.com New Subscriber → HubSpot Contact

**Trigger:** New subscriber in Kit.com (checklist opt-in)
**Action:** Create or Update Contact in HubSpot

**Field Mapping:**
| Kit.com Field | HubSpot Field |
|--------------|---------------|
| Email | Email |
| First Name | First Name |
| Tag (lead magnet name) | Lead Source = "Lead Magnet" |
| County (if collected) | County |

**Additional auto-tags:**
- Lead Source → "Lead Magnet"
- Create Deal? No — these aren't ready yet. Just contact record.
- Add to HubSpot List: "Lead Magnet Subscribers"

**Why this matters:** When someone downloads Donna's checklist, they go into HubSpot so Bradley can see them. When they eventually call, he already has their name and when they opted in.

---

## Recipe 3: HubSpot Deal → Instantly.ai Sequence (Danny's Outbound)

**Trigger:** New Deal created in HubSpot (Lead Source = Danny Outbound)
**Action:** Add Contact to Sequence in Instantly.ai

**Sequence to trigger:** "Property Manager 3-Touch" (Danny's sequence)

**Filter:** Only trigger if Contact Email is not empty

**Why this matters:** When Danny's lead list gets imported, every contact auto-enrolls in the email sequence without Bradley having to do it manually.

---

## Recipe 4: HubSpot Deal Stage = Closed Won → Google Sheets Log

**Trigger:** Deal Stage changes to "Closed Won" in HubSpot
**Action:** Add Row to Google Sheet "Jobs Log"

**Fields to log:**
- Deal Name
- Contact Name
- Email
- County
- Service(s)
- Quote Amount
- Closed Date
- Source (Danny / Carla / Inbound / Referral)

**Why this matters:** Running tally of every job, auto-logged. Bradley can see total revenue, jobs by county, jobs by source — without touching HubSpot.

---

## Recipe 5: HubSpot Deal Stage = Closed Won → Review Request Delay

**Trigger:** Deal Stage changes to "Closed Won"
**Action:** Add 1-day delay
**Action 2:** Send Email from HubSpot template "Post-Job Review Request"

**Why this matters:** Review request goes out automatically 24 hours after the job is marked complete. No one has to remember.

---

## Recipe 6: Facebook Review or Google Review → Slack/Email Alert

**Trigger:** New Google Review (via Google My Business — requires Google Workspace)
**Action:** Send email or Slack message to Bradley

**Message:**
> "New [X]-star review on Google from [Reviewer Name]: '[Review excerpt]'"

**Why this matters:** Bradley knows immediately when a review comes in — good or bad. Bad reviews can be responded to within hours.

---

## Recipe 7: HubSpot Contact No Activity Alert → Bradley Email

**Trigger:** HubSpot Workflow (internal to HubSpot — no Zapier needed)
**Logic:** Contact in "Estimate Sent" stage + no activity for 3 days → send internal notification email to Bradley

**Internal email subject:** "⚠️ Stale estimate: [Contact Name] — 3 days no contact"
**Body:** "Contact: [Name] | Estimate: [Amount] | Stage: Estimate Sent | Last modified: [Date]"

**Why this matters:** Estimates don't fall through the cracks. Bradley gets a nudge at Day 3.

---

## Setup Priority Order

| Priority | Recipe | Effort | Impact |
|----------|--------|--------|--------|
| 1 | Facebook Lead Ad → HubSpot | Medium | High — every ad lead auto-captured |
| 2 | Kit.com → HubSpot | Easy | Medium — lead magnet subscribers tracked |
| 3 | HubSpot → Review Request Email | Easy | High — reviews on autopilot |
| 4 | Closed Won → Google Sheets | Easy | Medium — revenue tracking |
| 5 | HubSpot → Instantly.ai | Medium | High (once Instantly.ai is connected) |
| 6 | Stale estimate alert | Easy (HubSpot only) | High — prevents lost deals |

---

## Zapier Account Notes

**Free plan:** 5 Zaps, 100 tasks/month — enough to start
**Starter plan ($20/mo):** 20 Zaps, multi-step Zaps — needed for Recipe 3 and 5
**Recommendation:** Start free, upgrade once Recipe 3 is needed

---

*Nina Kowalski | Forest City Power Washing | 2026-05-12*
