🔧 *Vera — Auto-Upgrade Run 147*
>Changed: Added Party/Event Rental Companies as commercial segment #84 — NE Ohio wedding/event season peak
>Why: A-1 Party Rental (Solon), Taylor Rental Centers (4 NE Ohio locations), Fun Planners, Abbey Rents — large outdoor storage yards packed with tents/tables/chairs coming out of winter storage = heavy grime. Spring = dirty equipment season + most motivated to spend before June weddings. Owner-operators sign directly, no procurement. Zero NE Ohio competitors targeting this segment. 8 Apollo titles + 9 org keywords added. First pull June 8 Cuyahoga.
>File: workers/lead_pipeline.py, integrations/mixmax.py, agents/danny.md
---
🔧 *Vera — Auto-Upgrade Run 147*
>Changed: Fixed stale segment count across all 11 relay functions — "82+" → "84+" (was: "82+", corrected Run 146 to "83+", corrected again now after adding Party/Event Rental as segment #84)
>Why: Ice Cream Chains (#83, Run 146) and Party/Event Rental (#84, Run 147) both added since the relay was last updated. All countdown messages, verification functions, and Early Cuyahoga opportunity message now show correct count.
>File: workers/vera_relay.py
---
🔧 *Vera — Auto-Upgrade Run 147*
>Changed: Updated June 8 Cuyahoga countdown message to include Marine/Boat Dealers + Ice Cream Chains + Party/Event Rental in the segment list
>Why: All three segments were added after the June 8 relay message was originally written. Their FIRST Apollo pull fires June 8. Bradley needs to know these are in this run so he recognizes contacts from these industries in his inbox post-enrollment.
>File: workers/vera_relay.py
---
🔧 *Vera — Auto-Upgrade Run 147*
>Changed: Updated June 15 Lake County countdown to explicitly call out Marine/Boat Dealers (Skipper Buds/Mentor, Inland Seas Yachts/Vermilion) as a FIRST PULL on that run
>Why: The Marine/Boat Dealer segment brief in danny.md says "first pull June 15 Lake County" but the relay message didn't mention it. Now Bradley knows to expect boat dealer contacts in the Lake County batch.
>File: workers/vera_relay.py
---
💡 *Vera — Upgrade Proposal*
>Idea: Tommy writes a batch of June 1–7 Facebook posts immediately (4–5 posts for the full first week of June)
>Why: The last Facebook batch covers through May 26–30 week. June 1 is tomorrow — the page will go dark for the highest-traffic residential booking week of the year. Peak season Facebook content (before/after photos, local references, booking CTAs) keeps inbound warm while Danny's commercial email sequences do their work. Memorial Day weekend jobs are done — photos should exist now.
>Impact: 3–5 residential inbound leads per week from organic Facebook; zero cost; keeps Forest City active in NE Ohio homeowner feeds during the best booking window of the year.
>Reply YES to approve and I'll have Tommy write the June 1–7 batch immediately.
---
🚨 *Summit County Pull — TODAY IS THE LAST DAY (Deadline May 31 = TOMORROW)*
>Today (Saturday May 30) is your last low-pressure day to run it. Tomorrow (Sunday May 31) is the deadline — then Summit County misses all 84+ commercial segments until June 29 auto-rotation.
>Run it now — 6 minutes, fully unattended:
>Double-click: `scripts/run_summit_both.command` in Finder
>Or: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Summit`
>Saturday is the best day to run it — nothing competing for your attention.
---
⛽ *Gas Station + Fleet Sequences Still PENDING — June 4 Enrollment is 5 Days Away*
>Gas station contacts stranded since May 19 (11 days). Fleet contacts waiting indefinitely.
>Each day = more contacts who may get cold-called by a competitor first.
>FASTEST FIX — Gmail blast all gas station contacts today (3 min): `outputs/danny/gas_station_manual_email_blast_2026-05-19.md`
>Or: Mixmax → Sequences → New → create both → paste IDs into integrations/mixmax.py lines 48 + 54.
---
⚠️ *Instantly.ai STILL Not Paused — June 4 Enrollment in 5 Days*
>Every day Instantly.ai runs = domain reputation damage = lower deliverability on June 4.
>Fix (3 min): app.instantly.ai → Campaigns → ⋮ → Pause a1c08c3d AND 626cd15d → add INSTANTLY_PAUSED=true to .env
>5 days of recovery left before Round 2. Minimum viable is 7 days. Pause today.
---
✅ *Vera — Scan Complete 2026-05-30 (Run 147)*
>4 auto-upgrades shipped | 1 proposal (Tommy Facebook batch) | 84 open issues (82 carry-forward + 2 new segment tracking: Party/Event Rental now live in code)
>New this run: Segment #84 Party/Event Rental Companies added. All "82+"/"83+" → "84+" corrected across relay (11 instances). June 8 + June 15 relay messages updated with new segments. Summit pull FINAL WINDOW = today.
