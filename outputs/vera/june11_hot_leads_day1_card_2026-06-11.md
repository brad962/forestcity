# June 11 Hot Leads Day 1 Card
*Vera Cole | Run 202 | 2026-06-11*

---

## Today Is Day 3 of the June 8 Cuyahoga Send Window

**This is the first day hot leads are expected.** Touch 1 went out June 8–9. Day 3 open patterns typically surface the early-adopter openers — hospital FMs, YMCA directors, property management firms who have a systematic vendor review process.

**Run Nina's report NOW:**
```bash
python3 workers/nina_report.py daily
```

---

## What "Hot Lead" Means Today

A contact is hot if they've opened Touch 1 **2+ times** without replying. This means they read it, went back to it, and are thinking about it. That is buying behavior.

For every hot lead:
1. **Connect on LinkedIn within 2 hours** of seeing the open
   - Template: `outputs/tommy/hot_lead_linkedin_dm_playbook_2026-05-18.md`
   - Search: "[First Name] [Last Name] [Company Name] property manager Cleveland"
   - Message after connecting (24h): reference the company name, ask a single question
2. **Log in pipeline_data.json** — stage: "Contacted", add `next_followup` date (7 days out)
3. **Do NOT email them again today** — Touch 2 fires automatically via Mixmax. Let it work.

---

## Priority Segment Hot Leads to Watch For

Based on June 8 Cuyahoga pull — these segments have the highest expected open rates:

| Segment | Why They Open Early | What LinkedIn Profile to Look For |
|---------|---------------------|-----------------------------------|
| Hospital / Health System FM | Vendor review is systematic; reads everything in first 48h | "Facilities Manager — Cleveland Clinic / UH System" |
| YMCA / Rec Center Director | Community-org mindset; higher email engagement | "Executive Director — YMCA Greater Cleveland" |
| Commercial Property PM | Opens multiple times before replying — ghost reader pattern | "Property Manager — [management company name]" |
| Car Dealership Fixed Ops | High open rate; low reply rate; LinkedIn connect converts better | "Fixed Operations Director — [dealership group]" |
| Senior Living Executive Director | ED/Admin controls vendor budget directly | "Executive Director — [senior living campus]" |

---

## If Nina Report Shows 0 Hot Leads

**This is not a failure signal yet.** Some behavior patterns:
- Government/municipal FMs: Day 4–7 openers (public-sector slower decision pace)
- Corporate park FMs: frequently open on mobile without recording full opens
- Mixmax occasionally delays open counts 12–24h in high-volume sends

**If 0 hot leads on June 11:** Check again at 2pm via `python3 workers/check_replies.py`. If still 0, check again June 12 morning — Day 4 is historically the second major open wave.

---

## Parallel Action: LinkedIn Profile Health

**Last Forest City LinkedIn post: May 21 (21 days ago).** Contacts who opened Touch 1 on June 8–11 may check the LinkedIn profile before deciding to reply. A 21-day-old last post weakens the credibility signal at the exact moment it matters most.

**If you have 15 minutes today:**
1. Post one of the pre-written LinkedIn posts from `outputs/jasmine/linkedin_posts_june_2026-05-24.md`
2. Any June post works — "Property managers in NE Ohio" angle is best for this contact batch
3. Takes 5 minutes to copy-paste and post from LinkedIn on your phone

---

## Gas/Fleet Sequences — Day 27 Final Window

⚠️ **Lake County pull fires June 15 — 4 days away.** If the gas_station and fleet_washing sequences aren't created before June 15, those new Lake County contacts will sit unenrolled alongside all the Summit/Medina/Cuyahoga gas + fleet contacts already waiting.

**Tonight or tomorrow night (June 11–14):**
1. app.mixmax.com → Sequences → New Sequence
2. Name: `Forest City Power Washing — Gas Station & C-Store Outreach`
3. Copy ID from URL → paste into `integrations/mixmax.py` line 54
4. Name: `Forest City Power Washing — Fleet Washing Outreach`
5. Copy ID → paste into `integrations/mixmax.py` line 48
6. `python3 workers/lead_pipeline.py pending` → enrolls all waiting contacts
**Total time: 10–12 minutes.**

---

## New This Run: Segment #196 — Craft Breweries & Taprooms

Added to `workers/lead_pipeline.py` and `integrations/mixmax.py` today.

**Why now:** June is peak outdoor seating season in NE Ohio. Breweries with outdoor patios, loading docks, and parking lots are actively prepping for summer events. **Willoughby Brewing** (downtown Willoughby, one of Ohio's oldest craft breweries) is a flagship Lake County target that fires in the June 15 pull.

**Other NE Ohio targets:** Platform Beer (Cleveland), Great Lakes Brewing (Ohio City), Market Garden, Fat Head's (Middleburg Heights), Forest City Brewery, Hoppin' Frog (Akron), Thirsty Dog (Akron), Elliot Brewing (Willoughby).

Revenue: $800–$2,500/visit × 3x/year = **$2,400–$7,500/year per brewery**. Zero competitors cold-calling this segment.

---

## Today's Priorities (In Order)

| Time | Action | Tool |
|------|--------|------|
| 7:00–7:20am | Run Nina hot leads report | `python3 workers/nina_report.py daily` |
| 7:20–8:00am | For each 2+ open contact: LinkedIn connect + pipeline log | Tommy playbook |
| Anytime today | Post one LinkedIn update | `outputs/jasmine/linkedin_posts_june_2026-05-24.md` |
| Tonight | Gas/Fleet Mixmax sequences (if not done) | app.mixmax.com |
| June 14 night | Lake County pre-flight | `outputs/vera/lake_county_june15_preflight_2026-06-09.md` |
| June 15, 7:30am | Lake County pull | `scripts/run_lake_both.command` |

---

*Vera Cole | Run 202 | 2026-06-11*
