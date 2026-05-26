🔧 *Vera — Auto-Upgrade (Run 91 | May 26 Launch Day)*
>Changed: agents/rick.md — removed stale "Launch target: May 26" language
>Why: Ads are live today (or launching now); target date language becomes misleading the moment it passes; replaced with monitoring guide references and Day 3 card link
>File: agents/rick.md

---

🔧 *Vera — Auto-Upgrade (Run 91 | May 26 Launch Day)*
>Changed: .github/workflows/vera_slack_relay.yml — deployed GitHub Action from outputs/vera/ to proper location
>Why: The Action was written Run 34 but never deployed — all Slack messages have been accumulating undelivered; fresh push attempt; if the PAT now has workflow scope, this message is the first to arrive via the Action
>File: .github/workflows/vera_slack_relay.yml

---

🔧 *Vera — Auto-Upgrade (Run 91 | May 26 Launch Day)*
>Changed: agents/rick.md — added day3_ads_check_card_[date].md to output format catalog
>Why: Day 3 (Thursday May 28) is the first window where Facebook ads data is meaningful; no guide existed for what to check and what NOT to touch before that; gap between launch_day_evening_debrief and the 7-day review
>File: agents/rick.md

---

📄 *Vera — Deliverable (Run 91)*
>File: `outputs/vera/day3_ads_check_card_2026-05-26.md`
>What: 10-minute Thursday May 28 ad monitoring card
>Content: Facebook CTR/spend/CPM thresholds (green/yellow/red); Google impressions/CPC benchmarks; "one allowed tweak" rule (only if CTR <0.5%); what NOT to do (don't turn off ads); Day 7 review schedule
>Action: Open Thursday morning at 8am. Do not open Ads Manager before reading this.

---

📄 *Vera — Deliverable (Run 91)*
>File: `outputs/vera/launch_day_contractor_outreach_stack_2026-05-26.md`
>What: 8-contact stack for today — 3 overdue follow-ups + 5 Tier 1 first outreach
>Why: This has been open since Run 86 (May 25). Bryan is now 13 days since last contact. All 3 Contacted contractors have follow-up overdue TODAY. The 5 Tier 1 New Leads have been sitting 7+ days without any personal touch.
>Content: Copy-paste texts for all 8 contacts. Pipeline update instructions. 17 minutes total.
>Action: Text BEFORE opening Ads Manager. Trades respond 8-10am.

---

🚨 *Vera — TODAY Action Required (Launch Day Stack)*
>It's May 26. Here's what's on the critical path RIGHT NOW:

>1. 📱 Text 8 contractors — `outputs/vera/launch_day_contractor_outreach_stack_2026-05-26.md` (17 min)
>2. 🔔 Set up lead notifications — `outputs/rick/ad_lead_notification_setup_2026-05-25.md` (15 min, BEFORE launching ads)
>3. 🏃 Summit pull — double-click `scripts/run_summit_pull.command` (6 min unattended, deadline May 31)
>4. ⏸️ Pause Instantly.ai — app.instantly.ai → a1c08c3d + 626cd15d → ⋮ → Pause (3 min; 9 days to recover before June 4)
>5. 🚀 Launch ads — `outputs/donna/may26_final_launch_brief_2026-05-25.md` (90-min complete guide)
>6. 📬 Gas station Wave 1 emails — `outputs/danny/gas_station_manual_email_blast_2026-05-25.md` (7 contacts)
>7. 📊 Day 3 check this Thursday — `outputs/vera/day3_ads_check_card_2026-05-26.md`

---

💡 *Vera — Upgrade Proposal (Run 91)*
>Idea: Create the Gas Station Mixmax sequence in Mixmax UI (10 minutes)
>Why: 12 gas station contacts have been sitting as "New Lead" since May 19. Copy is written (`outputs/danny/sequence_gas_stations_2026-05-19.md`). Creation guide exists (`outputs/danny/gas_station_mixmax_sequence_creation_2026-05-23.md`). Only missing step: open Mixmax, paste copy, paste generated ID into `integrations/mixmax.py` line 48.
>Impact: Unlocks 12 gas station district manager contacts for enrollment. One account = 5-15 locations. Multi-site recurring revenue.
>Reply YES to approve.

---

✅ *Vera — Scan Complete 2026-05-26 (Run 91)*
>3 auto-upgrades shipped | 2 new deliverables | 1 GitHub Action deployed | 24 open issues
>Key action today: `launch_day_contractor_outreach_stack_2026-05-26.md` — 8 contacts, 17 minutes, do before ads launch
>GitHub Action: Deployed to .github/workflows/ — if this message arrived via Slack, it worked. If not: GitHub → Settings → Developer settings → Personal access tokens → Edit → check workflow → Save
>Next dates: May 28 (Day 3 ad check) → May 31 (Summit pull deadline) → June 1 (Medina pull) → June 4 (Round 2 enrollment)
