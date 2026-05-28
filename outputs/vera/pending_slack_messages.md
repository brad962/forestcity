🔧 *Vera — Auto-Upgrade*
>Changed: `integrations/mixmax.py` — added 3 missing titles to PROPERTY_MANAGER_TITLES routing table: `automotive service center director`, `cinema general manager`, `bowling center director`
>Why: These titles existed in DANNY_TITLES (what Apollo searches for) but were absent from the Mixmax routing table — any contact Apollo pulls with these exact titles would silently misroute or fall through to wrong sequence. Found by cross-checking DANNY_TITLES against PROPERTY_MANAGER_TITLES line by line.
>File: integrations/mixmax.py
---
🔧 *Vera — Auto-Upgrade*
>Changed: `workers/vera_relay.py` — added 4 September county pull countdown relay functions: `_check_sept7_lake_3` (Sept 7), `_check_sept14_lorain_3` (Sept 14), `_check_sept21_summit_3` (Sept 21), `_check_sept28_medina_4` (Sept 28); all wired into `_main_body()`
>Why: Danny's calendar (added Run 121) covers Weeks 37–40 (Sept 7–28) but relay had ZERO Slack reminders for all of September. Each function fires the week of its Monday pull date with county-specific context.
>File: workers/vera_relay.py
---
💡 *Vera — Upgrade Proposal*
>Idea: VOC-based Facebook & Google Ad Copy Refresh — 3 new variants per platform
>Why: Current ad copy predates VOC research. VOC identified exact phrases customers use: "dirty driveway embarrassing me," "neighbors judging my house," "finally found someone reliable." Mirror-language ads get 3–5× higher CTR. Day 3 (today) is the first Facebook allowed tweak window — ideal time to A/B test new creative.
>Impact: Lower CPL → more leads per ad dollar at no extra spend. Rick writes 3 Facebook + 3 Google variants. Launch as A/B test today.
>Reply YES and I'll have Rick write the copy today.
---
💡 *Vera — Upgrade Proposal*
>Idea: Activate GBP Weekly Posting Routine — Jasmine owns it starting this week
>Why: Jasmine already wrote the GBP weekly routine guide and June content calendar — neither has been executed. GBP posts appear directly in Google Maps results (free traffic from buyers already searching). 10 min/week. Competitors who post 1x/week outrank those who don't.
>Impact: Higher Maps ranking in 7-county service area during peak season at zero cost. Jasmine posts 1 GBP update + 1 job photo per week starting June 1.
>Reply YES and I'll move the guides to outputs/jasmine/ and have Jasmine write the first 4 June posts.
---
💡 *Vera — Upgrade Proposal*
>Idea: Re-engage Bryan + 21 untouched contractor referral contacts before June 4 enrollment day
>Why: Bryan (CLE Lawn Care Plus) 14+ days cold — no follow-up since first touch. 21 other contractor referral contacts from earlier pulls have never received a first-touch text or email. One active referral partner who books 3 jobs = $1,200–$2,400 this season. June 4 is 7 days away — referral channel should be warm before email sequences go out.
>Impact: Carla writes a re-warm text for Bryan + first-touch sequence for the 21 untouched contacts. 30 min of sending.
>Reply YES and I'll have Carla draft the full outreach kit today.
---
✅ *Vera — Scan Complete 2026-05-28 (Run 122)*
>2 auto-upgrades shipped | 3 proposals | Open issues: 45 (2 resolved — routing sync gap + September relay gap)
>Critical: Summit County pull deadline MAY 31 (3 days). Run: `python3 workers/lead_pipeline.py danny Summit` or double-click `scripts/run_summit_pull.command`
>Today is Day 3 ads check window + Wave 2 contractor blitz day (16 texts). Past customer blast reminder active.
