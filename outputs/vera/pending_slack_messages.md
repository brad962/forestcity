🔧 *Vera — Auto-Upgrade*
>Changed: `vera_relay.py` — `_check_medina_reminder()` now starts May 29 (was May 30)
>Why: May 29 is the last Friday before the June 1 Medina pull — the relay was dark on the last business day to prep.
>File: workers/vera_relay.py

---
🔧 *Vera — Auto-Upgrade*
>Changed: Added Warehouse Club & Membership Retail as a new commercial segment (Costco, Sam's Club, BJ's Wholesale)
>Why: These 9 NE Ohio locations are INVISIBLE in Apollo under 'grocery chain' — they only surface under 'warehouse club'/'wholesale retail' org tags. Lots are 8–15 acres + gas station concourse. $36K–$96K/year per Costco district deal. Real gap, fixed.
>File: workers/lead_pipeline.py, integrations/mixmax.py, agents/danny.md

---
🔧 *Vera — Auto-Upgrade*
>Changed: Synced 9 new warehouse club titles to `PROPERTY_MANAGER_TITLES` in mixmax.py for correct Mixmax sequence routing
>Why: Every new DANNY_TITLES block must be mirrored in PROPERTY_MANAGER_TITLES or manual imports route to the wrong sequence.
>File: integrations/mixmax.py

---
⏰ *Vera — Summit Deadline Alert*
>Summit County pull deadline is **Sunday, May 31** — 2 days away.
>Today (Friday) is the last business day to run it before the weekend deadline.
>Run now: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Summit`
>Or double-click: `scripts/run_summit_both.command` in Finder
>Miss this = no Summit leads until July 6 (next rotation). All 40+ commercial segments miss peak season there.

---
📍 *Vera — Medina Pull Reminder*
>Medina County pull is due **Sunday/Monday June 1** — 3 days away.
>Medina leads are required for the June 4 enrollment sprint.
>Run: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Medina`
>Or double-click: `scripts/run_medina_both.command` in Finder — both workers, one click.
>Guide: `outputs/donna/june1_medina_pull_guide_2026-05-26.md`

---
💡 *Vera — Upgrade Proposal*
>Idea: Father's Day (June 15) past-customer re-engagement blast — text + email campaign to all residential customers who booked in 2025 or early 2026.
>Why: Father's Day is 17 days away. "Give Dad a clean home for summer" is a seasonal message that converts warm customers without cold outreach. Tommy can write the copy in 30 minutes.
>Impact: Recaptures warm customers, fills the calendar for late June/early July, zero ad spend required.
>Reply YES to approve.

---
💡 *Vera — Upgrade Proposal*
>Idea: Create the Gas Station & Fleet Washing Mixmax sequences in Mixmax UI and paste the IDs into `integrations/mixmax.py`. These sequences have been PENDING since May 19 — 10 days of stranded leads.
>Why: 12 gas station contacts are sitting in `pipeline_data.json` with no sequence to enroll into. Every day they sit is a day the sequence clock isn't running.
>Impact: Unlocks enrollment for 12+ high-value multi-site accounts immediately.
>Action: Create two Mixmax sequences → paste IDs into integrations/mixmax.py lines 47 and 54 → run `python3 workers/lead_pipeline.py pending`. 10-minute task.
>Reply YES to approve OR just create the sequences and I'll handle the rest automatically.

---
✅ *Vera — Scan Complete 2026-05-29 (Run 138)*
>3 auto-upgrades shipped | 2 proposals | 69 total open issues (1 new Warehouse Club segment, 68 carry-forward)
>Key: Medina relay gap fixed (Fri warning now fires). Warehouse Club (Costco/Sam's/BJ's) segment added — real Apollo tag gap closed. Summit deadline in 2 days.
