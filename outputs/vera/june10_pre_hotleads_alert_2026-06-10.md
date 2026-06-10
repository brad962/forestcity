# June 10 Pre-Hot Leads Alert
*Vera Cole | Run 201 | 2026-06-10*

---

## Tomorrow Is the First Hot Leads Day

**Wednesday June 11** = Day 3 of the June 8 Cuyahoga Touch 1 send window. This is when the first 2+ open counts will surface in Nina's report. Block 20 minutes tomorrow morning before anything else.

---

## Tonight Checklist (June 10 — takes 5 minutes)

| # | Action | Why |
|---|--------|-----|
| ① | Set a 7am alarm for June 11 | Hot leads check before the workday starts |
| ② | Read Nina's hot leads report if it arrived today: `outputs/nina/hot_leads_2026-06-10.md` | Any early replies (rare but possible on Day 2) |
| ③ | Pull up `outputs/tommy/hot_lead_linkedin_dm_playbook_2026-05-18.md` on your phone | So it's ready when June 11 hot leads appear |
| ④ | Gas Station/Fleet Mixmax sequences — if you haven't created them yet: tonight is a good window | 10 min in Mixmax UI; step-by-step in `outputs/vera/lake_county_june15_preflight_2026-06-09.md` |

---

## June 11 Morning Protocol (20 minutes)

```
7:00am — Check Nina hot leads report (auto-generates at 8am cron, but run manually if needed)
         python3 workers/nina_report.py daily

7:15am — For every contact with 2+ opens:
         → Connect on LinkedIn immediately (template: outputs/tommy/hot_lead_linkedin_dm_playbook_2026-05-18.md)
         → Log contact in pipeline_data.json: stage "Contacted", add next_followup

7:30am — For any contact who REPLIED:
         → Respond personally within 2 hours
         → Template: outputs/tommy/touch3_reply_response_templates_2026-05-20.md
```

---

## What to Expect June 11

Based on past NE Ohio PM sequence open patterns:

| Lead Type | Open Timing | Typical Behavior |
|-----------|-------------|-----------------|
| Hospital/Health System FM | Day 2–3 (early opener) | Structured vendor review; may forward to procurement |
| YMCA/Rec Center Director | Day 2–4 | Community-org mindset; responds to social proof angle |
| Government/Municipal FM | Day 4–7 (slow opener) | Longer decision cycles; may take 2–3 touches |
| Commercial PM / Property Management Firm | Day 2–5 | Often opens multiple times before replying |
| Car Dealership Fixed Ops | Day 3–6 | High openrate, low reply; LinkedIn connect converts better |

**Strong result:** 5–15 hot leads (2+ opens) by June 11 end of day
**Exceptional result:** 1+ reply

---

## Reminder: Lake County Pull in 5 Days

**Monday June 15, 7:30am** — Run `scripts/run_lake_both.command`

Pre-flight checklist: `outputs/vera/lake_county_june15_preflight_2026-06-09.md`

New this pull: Segment #195 Boat Repair & Marine Service Centers (Grand River Marine, Fairport Harbor Boat Works — Lake County peak season RIGHT NOW).

---

## Optional: LinkedIn Post Today

Last Forest City LinkedIn post: May 21 (20 days ago). Cuyahoga contacts who opened Touch 1 this week may check the LinkedIn profile before deciding whether to reply. A stale profile hurts credibility at the exact moment of highest interest.

If you have 15 minutes: post one of the LinkedIn posts from `outputs/jasmine/linkedin_posts_june_2026-05-24.md` — it doesn't need to be new, just recent.

---

*Vera Cole | Run 201 | 2026-06-10*
