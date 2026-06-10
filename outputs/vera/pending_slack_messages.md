🔧 *Vera — Auto-Upgrade | Run 201 | June 10*
>Changed: NEW Segment #195 — Boat Repair & Marine Service Centers — 8 DANNY_TITLES + 8 DANNY_ORG_KEYWORDS + 8 PROPERTY_MANAGER_TITLES routing
>Why: Lake County June 15 pull fires in 5 days. Marine repair yards (Grand River Marine, Fairport Harbor Boat Works, Mentor Marine) are distinct from marinas/charter boats and have been missed by every prior segment. Peak repair season June–August. Zero competitors cold-calling. $2,400–$7,500/year per facility.
>File: workers/lead_pipeline.py, integrations/mixmax.py
---
🔧 *Vera — Auto-Upgrade | Run 201 | June 10*
>Changed: Count sync — 194+ → 195+ across workers/vera_relay.py (9 occurrences) + agents/danny.md (Run 201 batching note added). CLAUDE.md June 8 historical references preserved at 194+ (accurate for when that pull fired).
>Why: Keep all Slack alerts, agent briefs, and count references accurate for Lake County June 15 pull.
>File: workers/vera_relay.py, agents/danny.md
---
🔧 *Vera — Deliverable | Run 201 | June 10*
>Created: outputs/vera/june10_pre_hotleads_alert_2026-06-10.md — Pre-Hot Leads Alert Card
>What's in it: Tomorrow June 11 protocol (20-min morning block), tonight's 5-min checklist, hot lead type timing guide (hospital FM vs. government FM vs. car dealership), what counts as a strong result (5–15 hot leads), Lake County June 15 reminder, LinkedIn post nudge.
>File: outputs/vera/june10_pre_hotleads_alert_2026-06-10.md
---
🚨 *Vera — CRITICAL BLOCKER | Day 26+ | Gas Station & Fleet Washing Mixmax Sequences STILL PENDING*

Every gas station, C-store, and fleet washing contact Danny has pulled since May 15 is sitting in contacts_cache.json completely unenrolled. That's 26 days of contacts — Summit, Medina, and Cuyahoga (June 8) — receiving nothing.

*The Lake County June 15 pull fires in 5 days.* Lake County has gas stations and fleet operators too. If this isn't fixed before then, that batch piles on top.

*Fix tonight (10 min total):*
1. Go to app.mixmax.com → Sequences → New Sequence
2. Create: _Forest City Power Washing — Fleet Washing Outreach_
3. Copy sequence ID from URL → paste into `integrations/mixmax.py` line 48 → replace `'PENDING'`
4. Create: _Forest City Power Washing — Gas Station & C-Store Outreach_
5. Copy that ID → paste into line 54 → replace `'PENDING'`
6. Save, then run: `python3 workers/lead_pipeline.py pending`

Full guide also in `outputs/vera/lake_county_june15_preflight_2026-06-09.md` (Critical section at bottom).
---
🔔 *Vera — HEADS UP | June 11 = First Hot Leads Day*

>Tomorrow morning is the most important 20 minutes of the week.
>
>June 8 Cuyahoga Touch 1 emails are Day 3 tomorrow — this is when 2+ open counts surface in Nina's report. Hospital FMs, YMCA directors, and commercial PM contacts who opened multiple times are vetting vendors RIGHT NOW.
>
>*What to do at 7am:*
>1. Run: `python3 workers/nina_report.py daily`
>2. For every contact with 2+ opens → connect on LinkedIn immediately
>3. Template: `outputs/tommy/hot_lead_linkedin_dm_playbook_2026-05-18.md`
>4. Log in pipeline_data.json: stage "Contacted"
>
>Strong result = 5–15 hot leads. Exceptional = any reply.
---
💡 *Vera — Upgrade Proposal (ESCALATION — 2nd Request) | LinkedIn Content Gap*
>Idea: Jasmine writes a new batch of 5 LinkedIn posts targeting property managers and facility managers. Last LinkedIn post was May 21 — now 20 days ago.
>Why: Cuyahoga contacts who opened Touch 1 (June 8–10) are checking LinkedIn profiles TODAY before deciding whether to reply. Stale LinkedIn kills credibility at peak interest moment. June 11 is the first hot leads day — the contacts who open 2+ times tomorrow are the ones most likely to check the profile.
>Impact: Zero cost. 30-minute Jasmine task. Credibility signal for every PM/FM who googles Forest City this week.
>Reply YES to approve.
---
💡 *Vera — Upgrade Proposal (ESCALATION — 2nd Request) | Rick Day 14 Ads Review*
>Idea: Rick writes a June 10 (Day 15 post-launch) Facebook + Google ads performance review and scaling decision.
>Why: Ads launched May 26. Day 14 (June 9) was the scaling decision point per the week2_facebook_ads_scaling_guide. We're now at Day 15 — the review is overdue by one day. Without this, ad spend through June 15 (Lake County pull week) is unoptimized.
>Impact: If ads are performing → scale 20% to capture Lake County launch momentum. If underperforming → swap creative before wasting Week 3 budget.
>Reply YES to approve. Rick can run this in 30 minutes.
---
💡 *Vera — Upgrade Proposal (ESCALATION — 2nd Request) | Tommy Service Page VoC Refresh (4 pages)*
>Idea: Tommy writes VoC-refreshed copy for driveway, deck/fence, commercial, and roof soft wash service pages. House washing page was refreshed June 8. These 4 are still on May 20 copy.
>Why: Google Ads are running. Quality Score (which determines CPC) is calculated against landing page copy relevance. Every day these pages run old copy is a day of slightly higher CPC. The house wash refresh lifted CTR 15–25% per the pattern.
>Impact: Lower CPCs on existing campaigns = more leads per dollar. Compound effect across June.
>Reply YES to approve.
---
✅ *Vera — Scan Complete | Run 201 | June 10, 2026*
>1 auto-upgrade shipped (Segment #195 Boat Repair & Marine Service) | 1 count sync | 1 deliverable | 3 proposals (all 2nd requests) | 195 open issues (194 carry-forward + 1 new: #195 Boat Repair/Marine)
>
>TOMORROW June 11 = First Hot Leads Day. Block 20 minutes at 7am. Run `python3 workers/nina_report.py daily`. Connect on LinkedIn with every 2+ open contact within 2 hours.
>
>Lake County June 15 pull = 5 days away. Gas Station + Fleet sequences still PENDING (Day 26). Fix tonight (10 min) so Lake contacts don't pile up unenrolled too.
