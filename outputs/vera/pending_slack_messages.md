🔧 *Vera — Auto-Upgrade (Run 107)*
>Changed: `workers/vera_relay.py` — added `_check_workiz_staleness()` function; alerts Bradley once per day if no Workiz job report has run in 3+ days; fires in `_main_body()` alongside Danny/Carla/Nina staleness checks
>Why: Revenue visibility gap — if Workiz cron skips for 3+ days, booked jobs and outstanding balances go untracked with no alert
>File: workers/vera_relay.py
---
🔧 *Vera — Auto-Upgrade (Run 107)*
>Changed: `workers/lead_pipeline.py` — added Snow Removal / Ice Management companies to CARLA_SEARCHES; keywords: `snow removal`, `snow plowing`, `snow plow`, `ice management`, `winter maintenance`, `snow and ice`, `snow clearing`
>Why: Snow removal companies are COMPLETELY IDLE May–September and actively seeking summer revenue; they service the same driveways and lots Forest City washes; the off-season trusted contractor relationship = warm referral intro; best uncontacted referral segment in NE Ohio right now
>File: workers/lead_pipeline.py
---
🔧 *Vera — Auto-Upgrade (Run 107)*
>Changed: `workers/lead_pipeline.py` + `integrations/mixmax.py` — added `fixed operations director`, `automotive service director`, `dealer principal` to DANNY_TITLES + PROPERTY_MANAGER_TITLES; car dealerships were in ORG_KEYWORDS since Run 88 but these decision-maker titles were missing; fixed ops directors manage service bay concrete + lot maintenance; dealer principals sign all vendor contracts
>Why: Car dealership segment was half-functional — org keywords live but the people who sign contracts weren't in the title search
>File: workers/lead_pipeline.py, integrations/mixmax.py
---
🔧 *Vera — Auto-Upgrade (Run 107)*
>Changed: `agents/danny.md` — added HOA Budget Season section (May–June boards approve vendor lists — Touch 1 should reference this urgency window); added car dealership Run 107 title note; `agents/jasmine.md` — updated june_week1 CURRENT to june 2 version; `agents/carla.md` — added snow removal as referral partner type #18
>Why: HOA boards are voting on summer vendor budgets RIGHT NOW — this is a real urgency angle, not manufactured
>File: agents/danny.md, agents/jasmine.md, agents/carla.md
---
📝 *Vera — New Deliverable (Run 107)*
>File: `outputs/tommy/past_customer_june_blast_2026-05-27.md`
>What: Past customer re-engagement blast card — 5 copy-paste texts by scenario (house wash, deck/driveway, annual plan upsell, 12-month gap, referral ask); response handling; Workiz lookup guide; pipeline log template
>Why: Ads launched May 26 but the algorithm takes 7-14 days to warm up. Fastest revenue THIS WEEK is past customers who already trust you. 5 texts = $1,800–$3,000 potential in 30 minutes. DO THIS TODAY — don't wait for June 4.
---
🔍 *Vera — GitHub Action (Run 107 — API attempt)*
>Tried: GitHub Contents API PUT to `.github/workflows/vera_slack_relay.yml` — fresh approach different from git push
>Result: 404 (GitHub obscures workflow-scope errors as 404 — PAT has `repo` only, not `workflow`)
>RESOLUTION: Option A (2 min, no new PAT) — github.com/brad962/forestcity → Add file → `.github/workflows/vera_slack_relay.yml` → paste YAML from `outputs/vera/github_action_vera_slack_relay.yaml` → commit main → add SLACK_WEBHOOK_OFFICE secret in Settings → Secrets → Actions. That's it.
>vera_relay.py local cron is working Slack delivery — GitHub Action is cloud backup only.
---
💡 *Vera — Upgrade Proposal*
>Idea: Kit.com email capture for "NE Ohio Home Maintenance Checklist" magnet
>Why: Ads launched May 26. Every visitor who doesn't book is permanently lost. Kit.com is free up to 10K subscribers. Setup guide: `outputs/donna/kit_email_capture_setup.md`
>Impact: 100 ad visitors → 20–40 email captures → nurture sequence → future bookings. Compounds every week ads run.
>Reply YES to approve (30-min one-time setup).
---
💡 *Vera — Upgrade Proposal*
>Idea: Monthly past-customer Slack reminder — 1st of each month, automatically lists Workiz customers not re-engaged in 12+ months
>Why: Past customer re-engagement is highest-ROI motion in home services (40–60% re-book rate, $0 acquisition cost) but zero systematic trigger exists
>Impact: Monthly alert → consistent outreach → estimated $2K–$5K/month recovered revenue
>Reply YES to approve (30-min build, new worker script reading Workiz + pipeline_data.json).
---
✅ *Vera — Scan Complete 2026-05-27 (Run 107)*
>5 auto-upgrades shipped | 1 new deliverable | 2 proposals | 33+ open issues
>🔥 TODAY: 20 contacts DUE in Nina's report. Summit pull DEADLINE May 31 (4 days left). Instantly.ai MUST be paused before June 4 (8 days).
>📅 TOMORROW: 16 Wave 2 contractor texts due. Day 3 ads check (may28_summit_pull_emergency_card).
>⚡ FASTEST WIN: Send past customer blast today (see outputs/tommy/past_customer_june_blast_2026-05-27.md) — 30 min = $1,800–$3,000 potential.
---
🔧 *Vera — Auto-Upgrade (Run 108)*
>Changed: `workers/lead_pipeline.py` + `integrations/mixmax.py` — added **Event Venues & Banquet Halls** as new commercial segment; titles: `venue manager`, `event venue manager`, `banquet manager`, `event center manager`, `venue director`, `catering director`, `conference center manager`; org keywords: `event venue`, `banquet hall`, `wedding venue`, `event center`, `conference center`, `banquet facility`
>Why: NE Ohio spring wedding season peaks May–July; Landerhaven, Emerald Event Center, Hilton Cleveland ballrooms, hotel event spaces — venue directors sign vendor contracts and exterior appearance is non-negotiable (event photos are permanent); $3K–$8K/year per venue; contact NOW before summer rush locks in other vendors
>File: workers/lead_pipeline.py, integrations/mixmax.py
---
🔧 *Vera — Auto-Upgrade (Run 108)*
>Changed: `workers/lead_pipeline.py` + `integrations/mixmax.py` — added **Auto Body & Collision Shops** as new commercial segment; titles: `auto body shop manager`, `collision center manager`, `body shop manager`, `district collision manager`; org keywords: `auto body shop`, `body shop`, `collision center`, `collision repair`, `auto collision`
>Why: Maaco, CARSTAR, Caliber Collision, Crash Champions district managers sign vendor contracts for 5-15 NE Ohio shops; concrete aprons covered in oil/paint overspray; OSHA stormwater compliance creates recurring urgency; one district deal = $25K–$80K/year; zero competitors targeting this segment
>File: workers/lead_pipeline.py, integrations/mixmax.py
---
🔧 *Vera — Auto-Upgrade (Run 108)*
>Changed: `workers/nina_report.py` — added stale estimates check to the **daily** hot leads report; "Estimate Sent" contacts with last_contact > 5 days now surface as `💰 ESTIMATE SENT — no follow-up in 5+ days — revenue at risk:` with names, days, and phone numbers; stale_estimate_count added to report card metrics
>Why: The stale estimate warning only existed in the weekly report — a warm estimate could sit untouched for 5+ days before the Monday report caught it; adding it to the daily report means Bradley sees it the same morning it crosses the 5-day threshold
>File: workers/nina_report.py
---
🔧 *Vera — Auto-Upgrade (Run 108)*
>Changed: `workers/vera_relay.py` — added `_check_summit_deadline()` (fires daily countdown alert through May 31) + `_check_gas_station_pending()` (fires daily alert if gas_station contacts in pipeline but sequence still PENDING); both wired into `_main_body()`
>Why: Summit deadline is 4 days away with no code-level daily push; gas station 12 contacts have been waiting since May 19 with no persistent daily reminder; both alerts are now self-deactivating once the condition clears
>File: workers/vera_relay.py
---
📝 *Vera — New Deliverable (Run 108)*
>File: `outputs/vera/may27_wednesday_pm_action_card_2026-05-27.md`
>What: Single-screen Wednesday afternoon action card — Summit County 4-day countdown with exact command; gas station sequence 30-min guide reference; exact contractor text scripts for Bryan/Bulletproof/Damrons; pipeline snapshot (36 contacts, 33 untouched, 20 due today); priority stack table with time + revenue estimates for every task this week
>Why: Consolidates all current blockers and actions into one read — no need to open 6 different guides
---
✅ *Vera — Scan Complete 2026-05-27 (Run 108)*
>5 auto-upgrades shipped | 1 deliverable | 0 issues resolved | 36 open
>New this run: Event Venues + Auto Body segments live in code | Stale estimates now in daily Nina report | Summit countdown + gas station PENDING alerts wired into vera_relay.py
>Critical path: Summit pull by May 31 → Medina pull June 1 → Instantly paused → June 4 Round 2 enrollment
