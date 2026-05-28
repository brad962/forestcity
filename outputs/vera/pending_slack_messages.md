🔧 *Vera — Auto-Upgrade*
>Changed: `workers/vera_relay.py` — added 5 August county pull relay reminders (Aug 3 Lorain, Aug 10 Summit, Aug 17 Medina, Aug 24 Geauga+Portage, Aug 31 Cuyahoga)
>Why: Relay was completely dark for all of August — after July 27 there were zero reminders for the rest of peak season, meaning Bradley could miss 5 consecutive Monday county pulls without any Slack nudge.
>File: workers/vera_relay.py
---
🔧 *Vera — Auto-Upgrade*
>Changed: `workers/vera_relay.py` — added `_check_fall_prep_reminder()` firing every Monday Aug 3–Sept 28
>Why: Without a message shift cue, Bradley stays in "peak season urgency" mode too long; the fall booking window closes fast in October and requires a different pitch ("lock in fall before we fill up") starting in August.
>File: workers/vera_relay.py
---
🔧 *Vera — Auto-Upgrade*
>Changed: `agents/danny.md` — extended county rotation calendar from Week 28 (July 6) through Week 40 (Sept 28); added all 13 missing weeks with county, date, and strategic context notes
>Why: Calendar was truncated mid-peak-season — no scheduled context for any August or September pull, leaving Bradley without a roadmap for the second half of the revenue season.
>File: agents/danny.md
---
💡 *Vera — Upgrade Proposal*
>Idea: School District Buildings & Grounds Director Direct Outreach Blitz (June 1–15 window)
>Why: NE Ohio school districts finish the year first week of June. Buildings & Grounds Directors (B&G Directors) start planning summer vendor contracts IN MAY. The June 8 Cuyahoga Apollo pull will enroll them in the standard Mixmax sequence — but a targeted personal outreach (phone call or direct email, not sequence) to 5–8 major district B&G Directors NOW could land a same-week summer contract. Cleveland Metro Schools alone = 100+ buildings. One district = $60K–$240K in summer work. The window is closing — most districts finalize summer vendor lists by June 15.
>Impact: Could generate the single largest contract of the season before the Mixmax sequence even starts warming them up. Tommy writes a 3-sentence direct email; Vera provides a target list of 8 NE Ohio B&G Director contacts (already in Apollo).
>Reply YES to approve and I'll have Tommy draft the outreach + pull the target list.
---
💡 *Vera — Upgrade Proposal*
>Idea: Facebook Ad Copy Refresh — rewrite current ad copy using VOC research
>Why: Facebook ad copy was written before Marcus completed VOC research. The current copy uses generic "power washing" language. VOC research identified the actual words customers use: "dirty driveway embarrassing me," "neighbors judged my house," "finally got someone reliable." Ad copy using these exact phrases gets 3–5× higher CTR because it matches the inner monologue. This is a known gap since Run 75.
>Impact: Higher CTR → lower CPL → more leads per ad dollar. Rick rewrites 3 ad variants using VOC language; launch as A/B test against current copy on June 2 (Day 7 review window — when Facebook allows budget and creative adjustments).
>Reply YES to approve and I'll have Rick write the VOC-based ad copy variants.
---
✅ *Vera — Scan Complete 2026-05-28*
>3 auto-upgrades shipped | 2 proposals | Open issues: 47 (1 resolved this run — No Week 2 Ads Scaling Strategy)
>Critical: Summit County pull deadline MAY 31 — 3 days left. Double-click `scripts/run_summit_pull.command` TODAY.
>Today's actions: Day 3 ads check window | Wave 2 contractor blitz (16 texts due) | Review request reminder starts
