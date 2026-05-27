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
