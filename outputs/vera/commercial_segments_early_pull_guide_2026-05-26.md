# Commercial Segments Early Pull Guide
**Vera Cole | Chief Innovation Officer**
*Written: 2026-05-26 | Use: anytime this week before June 1*

---

## Why Do This Now Instead of Waiting for June 1

The June 1 Medina rotation will pick up ALL the new segments automatically. But there's a problem:

**June 1 → contacts pulled → enrolled in Mixmax → Touch 1 sends → June 4 is only 3 days later**

That's 3 days of open/engage time before Round 2 enrollment. That's not enough.

If you pull the **3 highest-value new segments TODAY** and enroll them in the PM sequence, they'll have 9 days before June 4. That's 3× more time to open emails, which means:
- More hot leads (2+ opens) flagged by Nina before enrollment day
- More contacts with established context when you send Round 2
- Higher reply rate on the follow-up sequence

**Time required: 30 minutes total (unattended after first 5 minutes)**

---

## The 3 Segments to Pull Early (in priority order)

| Segment | Why First | Est. NE Ohio Contacts | Revenue/Deal |
|---------|-----------|----------------------|--------------|
| Banks & Credit Unions | 300+ branches, appearance is brand standard, zero competitors targeting | 25–50 decision-makers | $6K–$24K/year |
| Senior Living Facilities | 80+ facilities, compliance pitch angle, quarterly recurring | 30–60 contacts | $6K–$16K/year |
| Medical Office Parks | Dozens of Cleveland Clinic/UH campuses, patient trust = clean exterior | 20–40 contacts | $3K–$10K/year |

---

## How to Run the Early Pull

This uses a **manual Danny override** — pulls Cuyahoga County for ONLY the new segment keywords. Does NOT interfere with the June 1 Medina rotation.

### Step 1: Open Terminal (2 minutes)

```bash
cd /Users/bradleyneal/forestcity
python3 workers/lead_pipeline.py danny Cuyahoga
```

This runs Danny's regular pull for Cuyahoga County. The new segment keywords (banks, senior living, medical) are already in DANNY_ORG_KEYWORDS — they'll surface in this pull automatically alongside any remaining Cuyahoga PMs not yet in the cache.

**It runs unattended — takes 3–8 minutes depending on Apollo response time.**

### Step 2: Check the Output (2 minutes)

```bash
# See what was pulled
ls outputs/danny/ | tail -5
# Read the latest file
cat outputs/danny/leads_cuyahoga_property_managers_$(date +%Y-%m-%d).md | head -30
```

### Step 3: Verify Enrollment

The script auto-enrolls new leads in the PM sequence and sends a Slack notification. Check Slack for the Danny report card.

---

## For Summit County (if you want even more coverage before June 4)

Summit County pull is overdue since May 12 (deadline May 31). Running the Summit pull this week does double duty:
1. Picks up the overdue Week 21 rotation leads (PMs in Akron/Fairlawn/Stow)
2. Surfaces banks, senior living, and medical campuses in Summit County

```bash
python3 workers/lead_pipeline.py danny Summit
```

Or double-click `scripts/run_summit_pull.command` in Finder — no typing required.

---

## After the Pull: What to Watch

By June 1, check Nina's weekly report for:
- Any "Hot Leads" (2+ opens) from the new segment contacts
- Any replies — bank district managers respond quickly to professional outreach
- Flag any senior living contacts who open — compliance pitch = fast conversions

If you see a bank or senior living contact with 2+ opens before June 4, send them a **personal LinkedIn message** immediately. Don't wait for Touch 3. These are high-value accounts.

---

## Why Not Wait?

Every day of delay:
- = 1 fewer day for Touch 1 to generate opens
- = 1 fewer day for hot leads to surface
- = 1 fewer data point for which contacts to prioritize on June 4

The June 1 Medina pull is still happening and still captures Medina-area versions of these segments. This early Cuyahoga/Summit pull is additive — it doesn't replace anything, it adds leads earlier so you have more pipeline momentum going into June 4.

---

*This guide is an optional additive action — not on the critical path. Do it if you have 30 minutes this week.*
*Critical path: Summit pull (deadline May 31) > June 4 enrollment (battle card) > Medina pull (June 1)*
