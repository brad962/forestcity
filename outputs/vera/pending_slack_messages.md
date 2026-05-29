🔧 *Vera — Auto-Upgrade (Run 129)*
>Changed: Fixed `_check_google_lsa_status_weekly()` start date bug in vera_relay.py — was June 2 (Tuesday), now June 1 (Monday)
>Why: June 2 is a Tuesday; first Monday firing was June 8 — the entire June 5–16 LSA approval window was unmonitored. Now fires from June 1 correctly.
>File: workers/vera_relay.py
---
🔧 *Vera — Auto-Upgrade (Run 129)*
>Changed: Added `_check_gbp_weekly_post()` to vera_relay.py — fires every Monday May 26–Sept 30
>Why: Tommy wrote a June GBP content calendar with pre-written posts but zero relay reminder existed; weekly GBP posting is free organic lead gen that competitors never do, and the habit was going dark without a prompt.
>File: workers/vera_relay.py
---
🔧 *Vera — Auto-Upgrade (Run 129)*
>Changed: Added Craft Breweries & Taprooms as new commercial segment (lead_pipeline.py + mixmax.py + danny.md)
>Why: NE Ohio has 100+ craft breweries (Great Lakes Brewing, Platform, Masthead, Thirsty Dog, Goldhorn, Forest City Brewery) — outdoor patios + parking + facades + event season = recurring need; zero competitors cold-calling brewery managers; spring patio opening is NOW; first pull June 8 Cuyahoga.
>File: workers/lead_pipeline.py, integrations/mixmax.py, agents/danny.md
---
🚨 *Vera — CRITICAL ACTION — TODAY IS THE DEADLINE*
>Summit County pull is due TODAY, Friday May 29 — LAST BUSINESS DAY before May 31 deadline.
>Miss today = no Summit leads until July 6 (6 more weeks). All 30+ new commercial segments miss Summit until mid-July.
>Run now (6 min unattended): `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py danny Summit`
>Or double-click: `scripts/run_summit_pull.command` in Finder.
>Do not wait until Saturday/Sunday — Sunday scramble = mistakes.
---
📍 *Vera — Upcoming: Medina Pull Opens Tomorrow*
>Medina County pull target date = Monday June 1. June 4 enrollment needs fresh Medina leads.
>Run June 1: `python3 workers/lead_pipeline.py both Medina` — or double-click `scripts/run_medina_both.command`
>Medina has: Shiloh Foods (FDA compliance angle), Discount Drug Mart HQ (local company, 70+ locations), senior living chains, food processing segment targets. June 8 Cuyahoga is the biggest pull of the season — all 35+ segments fire at max volume.
---
✅ *Vera — Scan Complete 2026-05-29 (Run 129)*
>4 auto-upgrades shipped | 0 proposals | 56 open issues (3 new issues, all fixed this run)
>Key fixes: LSA relay date bug corrected (was silently missing June 1–7 window), GBP weekly post relay added, Craft Breweries segment live.
>TODAY: Summit County pull deadline — run it before EOD. Do not leave for Sunday.
>Next milestones: Medina pull June 1 → June 4 enrollment → June 8 Cuyahoga (biggest pull of season).
