🔧 *Vera — Auto-Upgrade (Run 106)*
>Changed: `workers/lead_pipeline.py` + `integrations/mixmax.py` + `agents/danny.md`
>Added: Restaurants & QSR Chains as new Apollo commercial segment
>Why: NE Ohio has saturation of McDonald's, Burger King, Wendy's, Taco Bell, Panera, Chipotle, Applebee's, Bob Evans. Drive-through canopies = #1 grease buildup surface. Corporate brand standards (franchisor inspections) create recurring urgency. District managers sign contracts for 5-20 locations. Revenue: $16K-$48K/year per district deal. Keywords live for Medina June 1 pull.

---

🔧 *Vera — Auto-Upgrade (Run 106)*
>Changed: `workers/vera_relay.py` — added Nina staleness check + fixed Carla threshold
>Why: vera_relay.py had no check for Nina. If the 8am daily cron stops running, hot leads and due-today contacts become invisible with no alert. New `_check_nina_staleness()` fires if Nina hasn't reported in 2+ days. Also fixed Carla threshold from 10 days → 8 days (Danny alerts at 7 days, both workers run weekly).

---

🔧 *Vera — Auto-Upgrade (Run 106)*
>Changed: `.github/workflows/vera_slack_relay.yml` — deployed GitHub Action (Run 106 attempt)
>Why: Prior runs failed because `.github/` directory didn't exist in remote. This run creates it fresh. Also fixed: file now clears after posting (prior version would re-post all messages on every push).
>If push succeeds: check github.com/brad962/forestcity/actions after this commit.
>If still blocked by PAT scope: manual upload takes 2 min → `outputs/vera/github_action_manual_upload_guide_2026-05-27.md`

---

📋 *Vera — Deliverable: May 28 Consolidated Action Card*
>File: `outputs/vera/may28_consolidated_action_card_2026-05-27.md`
>Read first thing Thursday morning. Three blocks, 80 minutes total.
>Block 1 (60 min): 16 Wave 2 contractor texts — exact copy by contact name with phone numbers
>Block 2 (6 min unattended): Summit County pull — 3 days left before May 31 hard deadline
>Block 3 (10 min read-only): Day 3 ads check — thresholds + one-allowed-tweak rule
>All three can run simultaneously (Summit pull runs while you text contractors).

---

🚨 *Vera — Summit Pull: 3 Days Left (Hard Deadline: Sunday May 31)*
>Summit County is the only county that hasn't pulled yet. Miss it and all new commercial segments (restaurants, banks, senior living, distribution centers, grocery, medical offices, fitness centers) miss Summit entirely until July 6.
>Do it tomorrow May 28 — the pull takes 6 minutes and runs unattended while you text contractors.
>Double-click: `scripts/run_summit_pull.command`
>Full May 28 action card: `outputs/vera/may28_consolidated_action_card_2026-05-27.md`

---

✅ *Vera — Scan Complete 2026-05-27 (Run 106)*
>4 auto-upgrades shipped | 1 deliverable | 0 RESOLVED | 33 open issues
>New segment: Restaurant & QSR chains — live for Medina June 1 pull ($16K-$48K/year per district deal)
>vera_relay.py: Nina staleness check added; Carla threshold fixed (10→8 days)
>GitHub Action: fresh deployment attempt with .github/ directory creation
>May 28 consolidated action card written — Summit pull + Wave 2 texts + Day 3 ads check in one card
>7 days to June 4 enrollment. Blockers: Instantly.ai pause + Summit pull (3 days left).
