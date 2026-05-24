🔧 *Vera — Auto-Upgrade*
>Changed: `agents/danny.md` — corrected "Instantly.ai: Not active" to explicitly flag both active campaigns (a1c08c3d + 626cd15d) as ACTIVE and causing 0% reply rate via spam filtering
>Why: The file was actively misleading — any agent reading it would think Instantly.ai wasn't a factor. It's the #1 cause of the current 0% reply rate.
>File: agents/danny.md

---

🔧 *Vera — Auto-Upgrade*
>Changed: `workers/vera_relay.py` — increased git log window from -20 commits to -100 commits
>Why: If Vera pushes >20 commits between relay runs (e.g. cron down for a few hours), the relay silently misses older commits and drops their Slack messages. -100 covers ~5 hours of continuous Vera runs with no risk of overflow.
>File: workers/vera_relay.py

---

🔧 *Vera — Auto-Upgrade*
>Changed: `agents/rick.md` — added `facebook_ads_first_week_monitoring_guide_[date].md` to output format catalog
>Why: Ads launch Tuesday. Bradley has never run Facebook ads. A day-by-day monitoring guide now exists before he needs it. SOP lives in Rick's outputs.
>File: agents/rick.md

---

🔧 *Vera — Auto-Upgrade*
>Changed: `agents/tommy.md` — added `neighbor_canvass_script_[date].md` to output format catalog
>Why: Donna wrote a strategy doc but no word-for-word scripts. Tommy's version has 4 copy-ready versions (door-knock, leave-behind, same-street text, commercial) with exact language. Documented for future reference.
>File: agents/tommy.md

---

📋 *Vera — Deliverable: Facebook Ads First-Week Monitoring Guide*
>File: outputs/rick/facebook_ads_first_week_monitoring_guide_2026-05-23.md
>What: Day-by-day guide for first-time Facebook ad launch. Day 1: setup lead notifications, don't touch anything. Day 3: first metric check (CTR > 1.5%, CPL target < $25). Day 7: first optimization. Includes: metric benchmarks for Cleveland home services, lead response protocol (text within 5 min or you lose the booking), budget scaling triggers, and 7 "things that will confuse you" explained. Revenue math: 1 booked job covers 1–2 weeks of $15/day budget.
>Read this BEFORE the first ad lead arrives Tuesday.

---

📋 *Vera — Deliverable: "While We're Here" Neighbor Canvassing Scripts*
>File: outputs/tommy/neighbor_canvass_script_2026-05-23.md
>What: 4 word-for-word versions for turning every active job into neighbor leads — (1) Door knock script including "how much" and "I'll think about it" responses; (2) Leave-behind card copy (handwrite the address you just cleaned — that detail closes); (3) Same-street past customer text (run day before or morning of); (4) "In your neighborhood" commercial text for PM and referral partner contacts nearby. Revenue math: 10 jobs/week × 25% neighbor conversion × $300 = $750/week zero-cost bookings = ~$3,000/month. Equipment is already deployed. Travel cost = $0.
>Start using after the first job this week.

---

🔴 *Vera — TONIGHT: Instantly.ai Must Be Paused*
>Reply window closes TOMORROW (Sunday May 25). Whether there are replies or not, Instantly.ai must be paused before Round 2 enrollment June 4.
>
>Pause now = 12 days of deliverability recovery before June 4.
>Pause June 3 = 0 days. Every day not paused = worse Round 2 reply rate.
>
>3 minutes: app.instantly.ai → Campaigns → find a1c08c3d → ⋮ → Pause. Repeat for 626cd15d.
>Then double-click scripts/run_summit_pull.command in Finder — Summit County pull (5 min, no typing).
>That's 8 minutes total. Two of the biggest open issues resolved.

---

💡 *Vera — Upgrade Proposal*
>Idea: Build a "same-street" job routing feature into Workiz. When a job is booked, automatically check Workiz for past customers within 1 mile and show them as "nearby — text today." Could be a simple Python script that reads Workiz addresses, runs a distance check, and outputs a list each morning.
>Why: The neighbor canvass protocol needs this data. Right now Bradley would have to manually look up who's near each job. Automating the lookup removes the friction.
>Impact: Would make the $3,000/month neighbor revenue estimate actually executable without manual work.
>Reply YES to approve and I'll build the script.

---

💡 *Vera — Upgrade Proposal*
>Idea: Weekly "Open Rate by Subject Line" report from Mixmax — auto-runs every Monday, compares open rates across all 3 sequences by subject line variant. Even without replies, this tells us which subject lines are landing vs getting ignored. When Round 2 launches June 4, we'd have data to pick the winning subject line instead of guessing.
>Why: Tommy wrote 5 A/B subject line pairs (email_subject_line_ab_test_2026-05-22.md) for Round 2 enrollment. We should know which subject line won Round 1 before we test new ones.
>Impact: Better Round 2 open rate = more hot leads = more replies. This is analytics infrastructure that pays off every enrollment cycle.
>Blocker: Mixmax API blocked in cloud — would need to run locally via cron.
>Reply YES to approve and I'll add it to nina_report.py.

---

✅ *Vera — Scan Complete 2026-05-23 (Run 66)*
>4 auto-upgrades shipped | 2 deliverables written | 2 proposals | 0 new issues resolved
>
>Open issues (18): All require Bradley action. Top 3 by revenue impact:
>1. 🔴 Pause Instantly.ai (a1c08c3d + 626cd15d) — 3 min — 12 days until Round 2 enrollment
>2. 🔴 Summit County Danny pull — double-click scripts/run_summit_pull.command — deadline May 31
>3. 🔴 Launch Facebook + Google Ads Tuesday May 26 — all copy ready, monitoring guide now written
>
>New this run: Facebook ads first-week guide (Rick) + neighbor canvassing scripts (Tommy). Both ready to use Tuesday.

---

🔧 *Vera — Auto-Upgrade*
>Changed: `workers/lead_pipeline.py` — Danny Apollo per_page 25 → 50; Carla per_page 15 → 20
>Why: Peak season Summit County pull is the most important one until July 6. Doubling Danny's lead volume means more contacts enrolled in the PM sequence — more shots at a reply before Round 2. Carla's contractor pull also gets 33% more referral partner contacts per county.
>File: workers/lead_pipeline.py

---

🔧 *Vera — Auto-Upgrade*
>Changed: `agents/carla.md` — added 2 new output format entries (contractor_referral_sequence_voc_rewrite, summit_county_referral_pull_guide)
>Why: Both deliverables written this run; catalogued for future reference so Carla knows what to produce and where to save it.
>File: agents/carla.md

---

🔧 *Vera — Auto-Upgrade*
>Changed: New file `scripts/run_summit_both.command` — double-click Mac shortcut that runs BOTH Danny Summit AND Carla Summit pulls in sequence
>Why: The existing run_summit_pull.command only does Danny. Carla has been on the same county rotation but no Finder-shortcut existed. One double-click now pulls PMs + referral partners for Summit County simultaneously. Takes 5-8 minutes, no typing.
>File: scripts/run_summit_both.command

---

📋 *Vera — Deliverable: GBP Memorial Day Post*
>File: `outputs/vera/gbp_memorial_day_post_2026-05-23.md`
>Memorial Day weekend = peak search traffic for "power washing near me." GBP post for TODAY (Saturday May 23) — 2 minutes to post at business.google.com/dashboard. Two versions: with photo (better) + text-only. Free impressions, shows in local search panel this weekend.

---

📋 *Vera — Deliverable: Carla Contractor Sequence VOC Rewrite*
>File: `outputs/carla/contractor_referral_sequence_voc_rewrite_2026-05-23.md`
>The May 12 contractor outreach used generic B2B language. This version uses Marcus's NE Ohio VOC phrases ("green and slimy," "roof turned black") + trade-specific Touch 1 customizations for 10 partner types (landscaper, roofer, gutter, HVAC, tree service, pool, irrigation, etc.). Ships June 4 in Round 2 enrollment alongside the PM VOC rewrite.

---

📋 *Vera — Deliverable: Carla Summit County Pull Guide*
>File: `outputs/carla/summit_county_referral_pull_guide_2026-05-23.md`
>Guide for running Carla's Summit County pull this week — same geography, same timing as Danny's Summit PM pull. One double-click: `scripts/run_summit_both.command` pulls both Danny PMs and Carla contractors/realtors in one go.

---

🚨 *Vera — TODAY ACTION ALERT (Saturday May 23)*
>*(1) POST GBP NOW — go to business.google.com/dashboard → Add update → paste from outputs/vera/gbp_memorial_day_post_2026-05-23.md — 2 minutes, free impressions this weekend*
>*(2) PAUSE INSTANTLY.AI — app.instantly.ai → Campaigns → ⋮ → Pause a1c08c3d + 626cd15d — 3 minutes — 12 days of deliverability recovery before Round 2 enrollment*
>*(3) POST FACEBOOK — 3 posts written for Sat/Sun/Mon in outputs/jasmine/facebook_posts_memorial_day_weekend_2026-05-23.md — first one posts TODAY*

---

💡 *Vera — Upgrade Proposal*
>Idea: Update `scripts/run_summit_pull.command` description in CLAUDE.md to mention the new `run_summit_both.command` option that pulls Danny + Carla simultaneously
>Why: CLAUDE.md currently only documents the Danny-only shortcut. Bradley may not know the combined version exists.
>Impact: One command instead of two — Summit County PMs and referral partners both covered on the same run.
>Reply YES to approve and I'll update CLAUDE.md.

---

💡 *Vera — Upgrade Proposal*
>Idea: Add a "Carla Summit catch-up" alert to `vera_relay.py` — same logic as the Danny staleness check, fires if Carla hasn't pulled Summit County this week
>Why: Danny's missed Summit pull has been flagged for 12+ days. Carla's missed Summit pull has never been flagged because no staleness check exists for county-specific misses. Carla's Summit contacts are valuable — contractors and realtors in Akron/Summit area = a different network than Cuyahoga.
>Impact: Bradley gets a Slack nudge for Carla the same way he does for Danny.
>Reply YES to approve and I'll add the check to vera_relay.py.

---

✅ *Vera — Scan Complete 2026-05-23 (Run 67)*
>3 auto-upgrades shipped | 3 deliverables written | 2 proposals | 0 new issues resolved
>
>Open issues (18): All require Bradley action. Today's priority stack:
>1. 🔴 POST GBP right now — business.google.com/dashboard — 2 min — free Memorial Day weekend impressions
>2. 🔴 Pause Instantly.ai — app.instantly.ai — 3 min — 12 days until Round 2 enrollment starts
>3. 🔴 Double-click scripts/run_summit_both.command — pulls Danny + Carla Summit County in one go — 6 min
>4. 🔴 Post Saturday Facebook post — outputs/jasmine/facebook_posts_memorial_day_weekend_2026-05-23.md — 2 min
>5. 🟡 Text Anthony/Land Pro 440-320-2779 — referral swap pitch — any time today
>
>Tuesday May 26 priority stack still live: `outputs/donna/tuesday_may26_launch_card_2026-05-23.md`

---

🔧 *Vera — Auto-Upgrade (Run 68)*
>Changed: `workers/lead_pipeline.py` — Carla's output filename now includes county label (e.g., `leads_referral_partners_summit_2026-05-24.md` instead of `leads_referral_partners_2026-05-24.md`)
>Why: If Bradley ran Summit pull today and a second county tomorrow, the second file silently overwrote the first — county-labeled filename prevents data loss on same-day runs
>File: workers/lead_pipeline.py

---

🔧 *Vera — Auto-Upgrade (Run 68)*
>Changed: `workers/vera_relay.py` — Carla staleness alert now shows `run_summit_both.command` double-click shortcut alongside the manual command
>Why: The Danny alert already had the shortcut; Carla alert was missing it. One double-click covers both workers simultaneously.
>File: workers/vera_relay.py

---

🔧 *Vera — Auto-Upgrade (Run 68)*
>Changed: `agents/nina.md` — added `check_replies.py` to Nina's tools section
>Why: Nina "owns" check_replies.py (it scans her sequences and posts Slack) but her agent file never mentioned it. Gap between what the script does and what the agent knows about.
>File: agents/nina.md

---

🔧 *Vera — Auto-Upgrade (Run 68)*
>Changed: `agents/carla.md` — added pool_service_referral_blitz format to output catalog
>Why: Pool service is the highest-value untapped referral segment in NE Ohio right now (Memorial Day pool openings happening TODAY). New deliverable written this run.
>File: agents/carla.md

---

📄 *Vera — Deliverable (Run 68)*
>New file: `outputs/donna/monday_memorial_day_final_check_2026-05-24.md`
>What: Memorial Day morning 10-minute protocol — reply window closes TOMORROW (Monday May 25). Run check_replies.py at 10am. Decision tree for what to do based on reply count.
>Why: Tomorrow is the last day of the Touch 3 reply window AND a holiday. This gives Bradley a clear, short action for one specific moment without requiring a full work day.

---

📄 *Vera — Deliverable (Run 68)*
>New file: `outputs/carla/pool_service_referral_blitz_2026-05-24.md`
>What: Memorial Day pool season pitch for pool service companies — Apollo search query, LinkedIn DM, email script, text, follow-up sequence, objection handling, revenue math
>Why: NE Ohio pool openings happen Memorial Day weekend. Pool techs are in customers' backyards RIGHT NOW seeing dirty decks and siding. This is the best week of the year to pitch this trade. One pool company with 100 customers = ~$5,250 in referred revenue.

---

📄 *Vera — Deliverable (Run 68)*
>New file: `outputs/rick/facebook_lead_gen_launch_checklist_2026-05-24.md`
>What: 5-block pre-launch checklist: Pixel setup, lead notification email, Lead Gen Form settings, budget/targeting confirmation, lead response SOP confirmation
>Why: Most first-time Facebook ad launchers miss the lead notification setup — leads sit silently in Ads Manager until manually downloaded. This checklist prevents the single most common mistake that kills a first-week launch. Read BEFORE clicking Publish Tuesday.

---

💡 *Vera — Upgrade Proposal (Run 68)*
>Idea: Apollo search for pool service companies in Cuyahoga, Lake, Summit, Lorain Counties — Memorial Day week pull as a one-time Carla addition
>Why: Pool service companies are booking customers THIS WEEK. A pitch sent Monday or Tuesday gets read when they're on the road between pool appointments — phone always on, good headspace. If we wait until June, the emotional peak of "pool opening week" is gone.
>Impact: 15–30 pool company contacts → potentially 15–25 referrals per season per partner × $350 average = $5k+ annually per company
>Reply YES to approve and I'll add pool_service to the next Carla Apollo pull in lead_pipeline.py

---

⏰ *Vera — REPLY WINDOW CLOSE ALERT (Run 68)*
>Touch 3 reply window closes TOMORROW (Monday May 25 = Memorial Day)
>
>TODAY (Sunday May 24) last-chance actions:
>1. 🔴 Pause Instantly.ai — 3 min — app.instantly.ai → Campaigns → Pause a1c08c3d + 626cd15d
>2. 🔴 Text Anthony/Land Pro 440-320-2779 — trades working today — referral swap pitch
>3. 🟡 Pool company LinkedIn pitches — `outputs/carla/pool_service_referral_blitz_2026-05-24.md`
>
>TOMORROW (Memorial Day): 10am check_replies.py → 10 min → `outputs/donna/monday_memorial_day_final_check_2026-05-24.md`
>
>TUESDAY: Read facebook_lead_gen_launch_checklist FIRST → then full 90-min blitz

---

✅ *Vera — Scan Complete 2026-05-24 (Run 68)*
>4 auto-upgrades shipped | 3 deliverables written | 1 proposal | 0 new issues resolved
>
>Open issues (18): All require Bradley action.
>
>Today's priority (Sun May 24):
>1. 🔴 Text Anthony/Land Pro 440-320-2779 — 2 min — trades are working this weekend
>2. 🔴 Pause Instantly.ai — 3 min — app.instantly.ai → Campaigns → Pause a1c08c3d + 626cd15d
>3. 🟡 LinkedIn pool company pitches — `outputs/carla/pool_service_referral_blitz_2026-05-24.md`
>
>Tomorrow (Memorial Day): 10am check_replies.py only — 10 min — then enjoy the holiday
>Tuesday May 26: Read facebook_lead_gen_launch_checklist → full launch → 90 min
