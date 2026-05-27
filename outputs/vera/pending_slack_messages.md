🔧 *Vera — Auto-Upgrade | Run 111 | 2026-05-27*
>Changed: `workers/vera_relay.py` — added 3 new relay reminder functions
>1. `_check_medina_reminder()` — fires May 30–June 4 daily; Medina pull countdown with exact command and guide link
>2. `_check_day7_ads_review()` — fires June 2 only; Day 7 post-launch scaling decision with Facebook + Google guide links
>3. `_check_june4_enrollment_countdown()` — fires June 2–3; Round 2 enrollment pre-flight with GO/NO-GO tracker and battle card links
>Why: The relay had no reminders covering Summit deadline (May 31) → Medina pull (June 1) → June 4 enrollment. 8-day gap now closed.
>File: `workers/vera_relay.py`
---
🔧 *Vera — Auto-Upgrade | Run 111 | 2026-05-27*
>Changed: `.github/workflows/vera_slack_relay.yml` — deployed GitHub Actions workflow to correct location
>Why: The workflow file has lived in `outputs/vera/` since Run 34 without being placed in `.github/workflows/` where GitHub Actions executes it. Moved to correct path. If PAT has workflow scope this now fires on every Vera push that changes pending_slack_messages.md — eliminating dependency on Mac cron.
>REQUIRES: Set `SLACK_WEBHOOK_OFFICE` secret in repo → Settings → Secrets and variables → Actions. If push fails with 403, PAT needs `workflow` scope at github.com → Settings → Developer settings → Personal access tokens.
>File: `.github/workflows/vera_slack_relay.yml`
---
💡 *Vera — Upgrade Proposal | Run 111*
>Idea: Add `_check_june4_past_customer_blast()` to vera_relay.py — fires once June 4 morning
>Why: Tommy wrote `outputs/tommy/past_customer_june_text_scripts_2026-05-27.md` with 5 copy-paste text scripts for prior customers. Scripts are ready. But there's no same-day Slack ping to actually send them ON June 4 morning. Without it this gets skipped in the Round 2 enrollment rush.
>Impact: 10 past customers texted → estimated 2–4 bookings → $1,200–$4,000 revenue at zero acquisition cost
>Reply YES to approve.
---
💡 *Vera — Upgrade Proposal | Run 111*
>Idea: Write a dedicated "Snow Removal Company Referral Pitch Guide" for Carla
>Why: Carla's Apollo search now includes snow removal keywords (added Run 107), but there's no specific pitch for this segment. Snow removal operators are COMPLETELY IDLE May–September and actively seeking summer revenue. They already service the exact driveways, parking lots, and commercial lots Forest City washes. Warm referral relationship built in — "You're already their winter vendor. Be their summer referral, we'll reciprocate in September."
>Impact: 10 snow removal owners activated = 5–15 warm referral jobs = $5K–$15K zero-cost summer revenue. NE Ohio has hundreds of idle snow removal operators right now.
>Reply YES to approve.
---
⏰ *Vera — Critical Path Reminders | Run 111 | 2026-05-27*
>🚨 SUMMIT COUNTY — 4 days left (deadline May 31)
>  All 15+ new commercial segments miss peak season if this doesn't run
>  Double-click `scripts/run_summit_pull.command` — 6 min unattended
>
>⛽ GAS STATION SEQUENCE — 12 contacts waiting since May 19 (8 days idle)
>  Guide: `outputs/danny/gas_station_sequence_create_now_2026-05-27.md` — 30 min
>
>⚠️ INSTANTLY.AI — must be paused before June 4 enrollment
>  Guide: `outputs/vera/instantly_pause_guide_2026-05-22.md` — 3 min
>
>📊 ADS DAY 3 CHECK — tomorrow May 28 (read-only, 10 min)
>  Card: `outputs/vera/day3_ads_check_card_2026-05-26.md`
>  Log any leads that came in: `outputs/rick/launch_week_lead_log_2026-05-26.md`
---
✅ *Vera — Scan Complete 2026-05-27*
>Run 111 | 2 auto-upgrades shipped | 2 proposals | 40 open issues (0 resolved this run)
>Upgrades: vera_relay.py 3 new reminder functions + .github/workflows deployment
>Critical path: Summit pull (May 31) → Medina pull (June 1) → June 4 Round 2 enrollment
>Next: May 28 = Day 3 ads check + Wave 2 contractor texts
