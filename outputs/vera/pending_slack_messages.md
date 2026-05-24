🔧 *Vera — Auto-Upgrade*
>Changed: workers/check_replies.py — added "all clear" Slack confirmation when API is live and pipeline is quiet
>Why: Script was completely silent when api_ok=True but 0 replies and 0 hot leads — Bradley couldn't tell if the check ran clean or didn't run at all; now posts a ✅ timestamped confirmation so every check is visible
>File: workers/check_replies.py

---
🔧 *Vera — Auto-Upgrade*
>Changed: integrations/mixmax.py — added home inspector, property inspector, solar installer, solar panel to CONTRACTOR_TITLES
>Why: Home inspectors do 15-25 inspections/week, see dirty siding and algae roofs at every job, and are trusted advisors at buyer/seller moments; solar installers are on roofs constantly and work with homeowners already in "invest in my home" mode; both are untapped referral segments
>File: integrations/mixmax.py

---
🔧 *Vera — Auto-Upgrade*
>Changed: workers/lead_pipeline.py — added home inspection + solar installation to Carla contractor Apollo search keywords
>Why: Carla's searches now surface home inspector and solar company owners in each county alongside landscapers, roofers, and HVAC; these segments were invisible to the pipeline before
>File: workers/lead_pipeline.py

---
🔧 *Vera — Auto-Upgrade*
>Changed: agents/rick.md + agents/tommy.md + agents/donna.md — added 3 output format catalog entries
>Why: Three new deliverable types (ad week 1 revenue tracker, past customer June texts, June 4 enrollment battle card) now have canonical format names in their respective agent files
>Files: agents/rick.md, agents/tommy.md, agents/donna.md

---
📄 *Vera — Deliverable: June 4 Enrollment Battle Card*
>File: outputs/donna/june4_enrollment_battle_card_2026-05-24.md
>What: Operationalized press-GO guide for June 4 Round 2 enrollment. Pre-check night of June 3 (3 commands: verify Instantly paused, gas station ID filled, contact count). June 4 morning: Step 1 Summit pull → Step 2 Carla Medina pull → Step 3 pending sequence enrollment → Step 4 verify → Step 5 past customer texts. Exact copy-paste commands. Expected outputs. Failure modes covered.
>Different from: enrollment readiness checklist (go/no-go gate) and enrollment plan (strategy). This is the EXECUTION CARD.

---
📄 *Vera — Deliverable: Past Customer June Text Scripts*
>File: outputs/tommy/past_customer_june_text_scripts_2026-05-24.md
>What: 5 copy-paste text scripts for June 4 past customer blast — by service type (house wash, roof, driveway, annual plan upsell, neighbor referral pivot). Personalization guide, response handling for each scenario, timing guide (June 4 at 10am = peak window), revenue math. Pull past customers from Workiz (Completed jobs 2024-2025 not yet rebooked in 2026).
>Revenue math: 10 texts → 2-4 bookings at $600-$900 avg = $1,200-$3,600 at zero ad spend.

---
📄 *Vera — Deliverable: Facebook Ad Week 1 Revenue Tracker*
>File: outputs/rick/facebook_ad_week1_revenue_tracker_2026-05-24.md
>What: Fill-in-the-blank tracking sheet for Days 1/3/7/14 after ads launch Tuesday. Columns: spend, impressions, CTR, leads, cost per lead, quotes sent, jobs booked, revenue. Benchmark thresholds per metric. Decision tree for when to change vs. wait. Revenue projection table ($30/day → break-even math). Leads received log for the first 50 leads.
>Read before checking Ads Manager on Wednesday May 27 morning.

---
🚨 *CRITICAL — Reply Window Closes TOMORROW (Mon May 25, Memorial Day)*
>The 72-hour Touch 3 reply window ends tomorrow. This is the last chance to see a reply from Round 1 outreach.
>Action: Run `python3 workers/check_replies.py` at 10am Monday.
>Guide: outputs/donna/monday_memorial_day_final_check_2026-05-24.md
>If 0 replies: Pivot clean to Round 2 June 4. All assets are ready. Battle card: outputs/donna/june4_enrollment_battle_card_2026-05-24.md

---
🚨 *CRITICAL — Instantly.ai NOT Confirmed Paused (11 days until Round 2)*
>Round 2 enrollment: June 4 (11 days). Email deliverability recovery needs 7-10 days minimum.
>If not paused by Tuesday May 26, the recovery window drops to 9 days — minimum viable, and getting worse daily.
>Action (3 minutes): app.instantly.ai → Campaigns → ⋮ → Pause both a1c08c3d AND 626cd15d → Add INSTANTLY_PAUSED=true to .env
>Guide: outputs/vera/instantly_pause_guide_2026-05-22.md

---
💡 *Vera — Upgrade Proposal*
>Idea: Add home inspector companies as a Carla outreach segment — 2-touch LinkedIn + email sequence targeting home inspection company owners in Cuyahoga, Summit, Lake Counties
>Why: Home inspectors do 15-25 inspections/week. At every inspection, they see dirty siding, algae-stained roofs, and green driveways — and homeowners trust them. A simple referral card + $50/job commission = a pipeline of warm leads from someone already in front of your exact customer. Timing: buyer/seller = homeowner already spending money on the house.
>Impact: 1 active inspector partner × 5 referrals/month × $600 avg = $3,000/month recurring referral revenue. 5 inspector partners = game-changing. Carla already does home inspection keyword pulls now (auto-applied this run) — this is the outreach sequence to close those contacts.
>Action needed: Reply YES and Carla writes the 2-touch home inspector sequence for June 4 enrollment.

---
💡 *Vera — Upgrade Proposal*
>Idea: Post-5-star-review referral text ("Review Chain") — after every Google 5-star review, text the customer within 24 hours asking for a neighbor referral in exchange for $50 off their next service
>Why: Warm referrals from satisfied customers convert at 35-50% vs. 2-4% for cold email. A "no" on their own rebooking can still become a $50 referral that turns into a $600 job. Zero ad spend, zero new marketing cost — just a text 24 hours after the review posts.
>Impact: At 10 jobs/month × 1 referral request each × 40% conversion = 4 free leads/month = $2,400-$4,800/month in zero-cost revenue. Compounds as the customer base grows.
>Action needed: Reply YES and Tommy writes the 3-version post-review referral text (house wash / roof / driveway variant). Bradley sends manually for now; Twilio automation is the Phase 2.

---
✅ *Vera — Scan Complete 2026-05-24 (Run 71)*
>4 auto-upgrades shipped | 3 deliverables written | 2 proposals | 18 open issues carry forward | 0 new RESOLVED
>New this run: check_replies.py Slack silence bug fixed; home inspector + solar installer added as referral segments; June 4 enrollment battle card written (the last missing operational doc); past customer June text scripts; Facebook ad week 1 tracker
>Critical path to June 4: Pause Instantly.ai (3 min TODAY) → Summit County pull (5 min Tuesday) → Gas station Mixmax sequence (10 min Tuesday) → Run enrollment battle card June 4 morning
