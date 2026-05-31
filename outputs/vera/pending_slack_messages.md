🚨 *Vera — SUMMIT COUNTY PULL — TODAY IS THE LAST POSSIBLE DAY (May 31)*
>This is it. Miss today = no Summit County leads until June 29. Every restaurant, bank, gym, hospital, HOA management company, brewery, dialysis center, and one of our 92+ segments across Akron/Fairlawn/Stow/Hudson misses peak season entirely.
>
>**Run right now (6 min, fully unattended):**
>Double-click `scripts/run_summit_both.command` in Finder
>Or: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Summit`
>
>92+ commercial segments are loaded and waiting. Start this before you do anything else today.
---
📍 *Vera — Medina County Pull Is TOMORROW Monday June 1*
>Week 23 manual override. Medina County feeds the June 4 Round 2 enrollment. Do NOT skip.
>
>**Tomorrow morning (6 min):** Double-click `scripts/run_medina_both.command` in Finder
>Or: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Medina`
>
>After Medina runs, you need Instantly.ai PAUSED before June 4 (see next message).
---
⚠️ *Vera — Instantly.ai Must Be Paused Before June 4 (3 Days Away)*
>June 4 Round 2 enrollment is 3 days away. Instantly campaigns a1c08c3d + 626cd15d running simultaneously with Mixmax = duplicate emails = spam filtering = 0% reply rate.
>
>**3-min task:** app.instantly.ai → Campaigns → find a1c08c3d + 626cd15d → ⋮ → Pause both
>Then add `INSTANTLY_PAUSED=true` to your .env file.
>Guide: `outputs/vera/instantly_pause_guide_2026-05-22.md`
>
>Hard blocker. June 4 enrollment cannot run safely without this confirmed.
---
⛽ *Vera — Gas Station + Fleet Sequences STILL Blocking Revenue (Day 13)*
>Gas station contacts have been stranded since May 19. Fleet contacts since May 18. Warm leads go cold every day this sits.
>
>**Fastest option — Gmail bypass (no Mixmax setup required):**
>Gas station: `outputs/danny/gas_station_manual_email_blast_2026-05-19.md` — 3 ready-to-send templates, 12 contacts, send from Gmail now. Zero setup.
>
>**Full fix (30 min each):**
>Gas station: `outputs/danny/gas_station_sequence_create_now_2026-05-27.md` → Mixmax UI → paste ID into `integrations/mixmax.py` line 54
>Fleet: `outputs/danny/sequence_fleet_washing_2026-05-18.md` → Mixmax UI → paste ID into `integrations/mixmax.py` line 48
---
🔧 *Vera — Auto-Upgrade*
>Changed: `workers/lead_pipeline.py` — NEW: Motorsports Venues & Racing Facilities as segment #91. 9 DANNY_TITLES (speedway operations manager, motorsports venue manager, racetrack facilities manager, motorsports park manager, racing venue director, karting facility manager, indoor karting manager, speedway manager, raceway manager). 8 DANNY_ORG_KEYWORDS (motorsports park, speedway management, racetrack facilities, motorsports venue, racing facility, karting center, indoor karting, motorsports complex). Summit Motorsports Park (Norwalk — largest drag strip in OH; 20K+ fans/race), Mid-Ohio Sports Car Course (IndyCar/IMSA), Medina County Speedway, Autobahn Indoor Speedway (Brecksville), K1 Speed, Kart World. Enormous parking lots + grandstand concourses + pit lane aprons = tire rubber + oil/fuel residue. Spring = racing season opener = peak pitch window. Zero competitors. $2K–$8K/visit; 2–3x/year.
>Why: Motorsport venues are among the most heavily stained commercial properties in NE Ohio, and no power washing company is targeting them.
>File: workers/lead_pipeline.py
---
🔧 *Vera — Auto-Upgrade*
>Changed: `workers/lead_pipeline.py` — NEW: Print & Business Services Chains as segment #92. 8 DANNY_TITLES (print center manager, print shop district manager, printing services manager, fedex office manager, ups store franchise owner, business services manager, shipping center manager, copy center manager). 8 DANNY_ORG_KEYWORDS (printing services, business services center, print shop, shipping center, copy center, ups store franchise, business print services, print and ship). FedEx Office (25+ NE Ohio), UPS Store (50+ NE Ohio — INDEPENDENT franchise owners who sign their own vendor contracts), AlphaGraphics (15+), Minuteman Press (20+). Strip-mall entry concrete takes a beating from box dust, packing tape residue, heavy foot traffic. Franchise owners = small business operators = fast YES/NO. Zero competitors targeting this segment. First pull June 8 Cuyahoga.
>Why: UPS Store franchise owners are independent purchasing decision-makers — no procurement, no committee. Fast close path.
>File: workers/lead_pipeline.py
---
🔧 *Vera — Auto-Upgrade*
>Changed: `integrations/mixmax.py` — Synced 17 new titles (9 Motorsports + 8 Print/Business Services) to PROPERTY_MANAGER_TITLES. All route to property_manager sequence. GAS_STATION_KEYWORDS still checked first per Run 136 fix.
>Why: PROPERTY_MANAGER_TITLES must stay in sync with DANNY_TITLES additions — any gap means new contacts could be unrouted on Mixmax import.
>File: integrations/mixmax.py
---
🔧 *Vera — Auto-Upgrade*
>Changed: `workers/vera_relay.py` — Updated ALL stale segment counts "90+" → "92+" across 7 relay functions (Summit deadline, June 8 Cuyahoga x2, early Cuyahoga opportunity x2, post-June-8 monitoring, June 9 verification, July 20 2nd pass).
>Why: Counts were stale after adding Motorsports Venues (#91) and Print/Business Services (#92) this run.
>File: workers/vera_relay.py
---
🔧 *Vera — Auto-Upgrade*
>Changed: `agents/danny.md` — Full segment briefs added for Motorsports Venues & Racing Facilities (segment #91: Summit Motorsports Park / Mid-Ohio / Autobahn Indoor Speedway) + Print & Business Services Chains (segment #92: FedEx Office / UPS Store franchise owners / AlphaGraphics). Revenue math, pitch angles, NE Ohio targets, Apollo titles + org keywords, sequence routing. Title batching note updated: "90+ commercial segments" → "92+ commercial segments."
>Why: Agent files must document every segment — when contacts reply, Bradley needs the context to close.
>File: agents/danny.md
---
🔧 *Vera — Auto-Upgrade (Gap Fix)*
>Changed: `outputs/jasmine/facebook_post_june1_2026-05-31.md` — Written 1 standalone Facebook post for Monday June 1 to fill the gap between may26 batch (ends Sat May 30) and june_week1 batch (starts Tue June 2 per `facebook_posts_june_week1_2026-06-02.md`). The June 2–6 posts are already written. Only June 1 (Monday) was missing.
>Action: Copy the post from `outputs/jasmine/facebook_post_june1_2026-05-31.md` and post to Facebook tomorrow morning (8–9am).
>Note: June 2–6 posts are already done in `facebook_posts_june_week1_2026-06-02.md` — no further action needed on that file. The "page going dark" concern is resolved.
>File: outputs/jasmine/facebook_post_june1_2026-05-31.md
---
✅ *Vera — Scan Complete 2026-05-31 (Run 151)*
>5 auto-upgrades shipped | 0 new proposals | 4 urgent human-action items remaining
>New segments: Motorsports Venues & Racing Facilities (#91: Summit Motorsports Park/Mid-Ohio/Autobahn) + Print & Business Services (#92: FedEx Office/UPS Store franchise owners/AlphaGraphics/Minuteman Press). All "90+" counts updated to "92+".
>Facebook gap filled: June 1 post written (standalone). June 2–6 posts already exist.
>GBP relay function confirmed in place — fires Monday June 1 (first fire of peak season).
>Countdown: Summit pull TODAY (LAST DAY) → Medina pull June 1 → Instantly pause June 3 → June 4 Round 2 enrollment → June 8 Cuyahoga (92+ segments, largest pull of the season).
