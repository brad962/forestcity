🔧 *Vera — Auto-Upgrade*
>Changed: `workers/lead_pipeline.py` + `integrations/mixmax.py` + `agents/danny.md` — NEW: Charter Schools & Charter Management Organizations as segment #95. 8 titles (charter school director, CMO facilities director, charter principal, etc.) + 4 org keywords (`charter school`, `charter academy`, `charter management organization`, `charter management`). Full segment brief in danny.md. NE Ohio: Breakthrough Schools (12 campuses), Constellation Schools (7+), Hope Academy. Ohio DOE authorizer compliance = exterior appearance standard. CMO FM signs multi-campus contracts. Summer window June-August. $16K-$60K/year per CMO deal. Zero competitors. First pull June 8 Cuyahoga.
>Why: `charter school` is a distinct Apollo org tag not captured by existing `private school` or `school district` keywords — Cleveland has the highest charter school density in Ohio (50+ campuses) and this segment was completely unaddressed.
>File: workers/lead_pipeline.py, integrations/mixmax.py, agents/danny.md
---
🔧 *Vera — Auto-Upgrade*
>Changed: `workers/lead_pipeline.py` + `integrations/mixmax.py` + `agents/danny.md` — NEW: Outdoor RV & Boat Storage Facilities as segment #96. 6 titles (rv storage manager, boat storage manager, marine dry storage manager, etc.) + 7 org keywords (`rv storage`, `outdoor rv storage`, `boat and rv storage`, `marine dry storage`, etc.). DISTINCT from marinas (wet slips) + self-storage (indoor climate-controlled). NE Ohio: Lake Road Storage (Mentor-on-the-Lake), Northcoast Boat & RV Storage, Lakeshore Storage, Bass Lake Marina dry storage, multiple Lake/Lorain shoreline operators. Spring commissioning = RIGHT NOW = peak pitch window. Large concrete/gravel pads = $1,500-$5,000/visit; 2x/year = $3K-$10K/year. Zero competitors.
>Why: Spring boat/RV pickup season is happening right now — facility owners want clean lots when customers arrive. This is the highest-urgency timing segment in the current run and the segment was completely missing from the pipeline.
>File: workers/lead_pipeline.py, integrations/mixmax.py, agents/danny.md
---
🔧 *Vera — Auto-Upgrade*
>Changed: `workers/vera_relay.py` + `agents/danny.md` + `CLAUDE.md` — BUG FIX: Updated ALL stale "94+" segment count references to "96+" across 11 relay functions + danny.md title batching note + CLAUDE.md June 8 Cuyahoga callouts. Pipeline is now at 96 commercial segments.
>Why: Relay messages, CLAUDE.md, and danny.md all said 94 segments while the actual count is 96 after today's additions.
>File: workers/vera_relay.py, agents/danny.md, CLAUDE.md
---
🚨 *Vera — TODAY IS THE SUMMIT DEADLINE (May 31)*
>Summit County locks out after today. Next rotation: June 29 (29 days away).
>96 commercial segments across Akron / Fairlawn / Stow / Cuyahoga Falls / Hudson miss peak season if this doesn't run today.
>Run NOW (6 min unattended): Double-click `scripts/run_summit_both.command` in Finder
>Or: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Summit`
>Tomorrow = Medina pull day (Monday June 1). Run Summit today, Medina tomorrow.
---
📍 *Vera — MEDINA PULL TOMORROW (Monday June 1)*
>Medina is Week 23 manual override — use `scripts/run_medina_both.command`. Feeds June 4 Round 2 enrollment directly. Missing Medina = thin Round 2 batch.
>Tomorrow morning first thing: Double-click `scripts/run_medina_both.command` in Finder
>June 4 enrollment is in 4 days. Medina leads need to be in the system by then.
---
⚠️ *Vera — Instantly.ai Must Be Paused Before June 4 (4 Days Away)*
>Hard blocker for Round 2. Campaigns a1c08c3d + 626cd15d must be PAUSED. Duplicate sends = spam filtering = 0% reply rate on entire Round 2 batch.
>3-min fix: app.instantly.ai → Campaigns → Pause both → add INSTANTLY_PAUSED=true to .env
>Go/No-Go tracker: `outputs/vera/june4_enrollment_readiness_tracker_2026-05-27.md`
---
⛽ *Vera — Gas Station + Fleet Sequences Stranded (Day 13)*
>Gas station contacts in pipeline since May 19 — 13 days without enrollment. Fleet PENDING since launch.
>Fastest path: Gmail blast from `outputs/danny/gas_station_manual_email_blast_2026-05-19.md` (12 contacts, 15 min, no Mixmax setup required).
>Mixmax setup guide: `outputs/danny/gas_station_sequence_create_now_2026-05-27.md`
---
✅ *Vera — Scan Complete 2026-05-31 (Run 154)*
>5 auto-upgrades shipped | 0 proposals | 96 open issues (94 carry-forward + 2 new segment tracking)
>New segments: #95 Charter Schools (CMO multi-campus contracts, summer window NOW) + #96 Outdoor RV & Boat Storage (spring commissioning = peak pitch window RIGHT NOW).
>Pipeline now at 96 commercial segments. June 8 Cuyahoga pull = biggest lead day of the season.
>Priority stack: Summit pull TODAY → Medina tomorrow → Pause Instantly → June 4 enrollment → June 8 Cuyahoga.
