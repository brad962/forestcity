🔧 *Vera — Auto-Upgrade*
>Changed: integrations/mixmax.py PROPERTY_MANAGER_TITLES — removed duplicate 'leasing manager' entry
>Why: 'leasing manager' was listed twice (line 65 + added again in run 54). Duplicate entries waste loop iterations; now clean
>File: integrations/mixmax.py
---
🔧 *Vera — Auto-Upgrade*
>Changed: workers/lead_pipeline.py — added _write_danny_sentinel() + _write_carla_sentinel() helpers; both now write a .danny_last_pull_date / .carla_last_pull_date file after each successful Apollo run
>Why: vera_relay.py staleness detection was relying on log-file text-parsing (fragile); sentinel files are authoritative and survive log rotation
>File: workers/lead_pipeline.py
---
🔧 *Vera — Auto-Upgrade*
>Changed: workers/lead_pipeline.py — added `pending` mode: `python3 workers/lead_pipeline.py pending` enrolls pending contacts (gas stations, fleet) WITHOUT triggering a full Apollo pull
>Why: 18 gas station contacts have been waiting 3+ days. Once Bradley creates the Mixmax sequence, he can enroll them in 2 min without running a 5-min Apollo search
>File: workers/lead_pipeline.py
---
🔧 *Vera — Auto-Upgrade*
>Changed: workers/vera_relay.py _check_danny_staleness() + _check_carla_staleness() — both now check sentinel files first, fall back to log-parsing if sentinel missing
>Why: More reliable staleness detection; sentinel file is definitive, log parsing is a fallback; reduces false-alarm risk
>File: workers/vera_relay.py
---
🔧 *Vera — Auto-Upgrade*
>Changed: workers/nina_report.py run_daily() — added Instantly.ai overlap warning when API is live, 0 replies, and 10+ contacts enrolled
>Why: 0% reply rate has persisted for weeks with no daily reminder of the likely cause. Bradley now sees the specific Instantly.ai pause instruction in every daily report until resolved
>File: workers/nina_report.py
---
🔧 *Vera — Auto-Upgrade*
>Changed: agents/danny.md — added `python3 workers/lead_pipeline.py pending` command to gas station enrollment instructions
>Why: Previously said "run lead_pipeline.py" without clarifying the fast path; pending mode is faster (no Apollo pull) and better for this use case
>File: agents/danny.md
---
📄 *Vera — New Deliverable*
>File: outputs/vera/door_hanger_neighbor_farm_2026-05-22.md
>What: Memorial Day weekend door hanger strategy — after every job, drop 5 hangers on neighboring houses; print-ready copy included; FedEx Office locations; $15–20 to print 50
>Why: The freshly washed house is visible proof. 3–5% door hanger conversion rate vs 0.5% for cold mail. Every HVAC, roofing, and painting company does this — power washing operators don't. One weekend = 50+ hangers dropped, 1–3 quote calls by June.
---
📄 *Vera — New Deliverable*
>File: outputs/carla/rei_investor_outreach_2026-05-22.md
>What: Real estate investor / house flipper sub-segment for Carla — Apollo search params, 3-touch email sequence, text scripts, BiggerPockets + Facebook group strategy, REIA meeting channel
>Why: REI investors are the highest-value untapped segment: 4–12 jobs/year per investor vs 1–2/year for a realtor, zero price sensitivity (it's a business cost), and repeat business all season. NE Ohio has one of the highest fix-and-flip concentrations in the Midwest. Currently 0% covered.
---
🚨 *Vera — TONIGHT Priority (May 22 — Touch 3 Window LIVE)*

1. **Pause Instantly.ai** — 3 min — outputs/vera/instantly_pause_guide_2026-05-22.md
   Campaigns a1c08c3d + 626cd15d. This is the #1 suspect for 0% reply rate.

2. **LinkedIn connects** — 10–15 min — "just sent you an email" context expires by morning
   Open Mixmax → PM sequence → sort by opens → connect with top 5–7

3. **Check replies locally** — 2 min
   `python3 workers/check_replies.py`

4. **Evening debrief** — outputs/vera/touch3_evening_debrief_2026-05-22.md
   Full protocol for tonight + tomorrow morning

---
💡 *Vera — Upgrade Proposal*
>Idea: Memorial Day weekend door hanger neighbor farm — drop 5 hangers on neighboring houses after every job; print 50 door hangers at FedEx Office tonight for $15–20
>Why: The freshly washed house is visible from the street. Conversion rate is 3–5% — 10x better than cold mail. Costs almost nothing.
>Impact: 1–3 booked calls per 50 hangers dropped. Immediate weekend leads while ads aren't live yet.
>Full guide: outputs/vera/door_hanger_neighbor_farm_2026-05-22.md
>Reply YES to approve — Bradley prints tonight and deploys this weekend.
---
💡 *Vera — Upgrade Proposal*
>Idea: Real estate investor / house flipper segment for Carla — add to Apollo pull targeting investors managing 3+ NE Ohio flips/year
>Why: REI investors need power washing before every listing and between tenants; 4–12 jobs/year per account; no price sensitivity; currently 0% covered by Forest City outreach
>Impact: One investor relationship = $1,500–$3,000+/year; BiggerPockets and local REIA meetings = warm introduction channels
>Full guide + copy: outputs/carla/rei_investor_outreach_2026-05-22.md
>Reply YES to approve — Carla adds to next Apollo pull cycle.
---
✅ *Vera — Scan Complete 2026-05-22 (Run 55)*
>6 auto-upgrades shipped | 2 deliverables | 2 proposals | 62 RESOLVED | 17 OPEN
>Touch 3 reply window LIVE through May 25 (Sunday)
>Code: duplicate routing entry fixed, sentinel file reliability improved, pending enrollment mode added, Instantly.ai overlap warning in daily report
>Key tonight: Pause Instantly.ai + LinkedIn connects (context expires by morning)
