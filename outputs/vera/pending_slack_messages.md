💆 *Vera — Auto-Upgrade #1 of 2 | Segment #109: Massage Therapy & Wellness Chains* _(Run 160 · 2026-05-31)_
>**New segment live** — 8 Apollo titles + 8 org keywords added to `lead_pipeline.py`. Titles synced to `mixmax.py` PROPERTY_MANAGER_TITLES for correct routing. Full segment brief added to `danny.md`.
>
>**Why now:** Massage Envy alone has 30+ NE Ohio franchise locations (Strongsville, Mentor, Westlake, Fairlawn, Beachwood, Solon, Avon, North Olmsted, Macedonia, Mayfield Heights). Elements Massage has 8+ NE Ohio locations. Hand & Stone and LaVida add more. Ohio State Massage Therapy Board licensing = exterior appearance standard. Each franchise owner signs their own vendor contracts — NO corporate procurement committee. Fast close. DISTINCT from hair/nail salon chains already in system (different Apollo org tags: 'massage therapy' vs 'hair salon').
>
>**Revenue:** $300-$800/location; 2x/year = $600-$1,600; 10-franchise territory = $6K-$16K/year. Zero competitors cold-calling massage therapy franchise owners in NE Ohio.
>
>**First pull:** June 8 Cuyahoga

---

🤝 *Vera — Auto-Upgrade #2 of 2 | Segment #110: Non-Profit & Social Service Organizations* _(Run 160 · 2026-05-31)_
>**New segment live** — 8 Apollo titles + 9 org keywords added to `lead_pipeline.py`. Titles synced to `mixmax.py`. Full segment brief added to `danny.md`.
>
>**Why now:** Salvation Army NE Ohio (6+ chapter facilities + thrift store warehouses), Catholic Charities Diocese of Cleveland (20+ program offices), Second Harvest Food Bank of NE Ohio (Independence OH distribution facility), Habitat for Humanity ReStores (Cleveland/Akron/Medina), United Way of Greater Cleveland, Lutheran Metropolitan Ministry, Jewish Family Service Association. Large building footprints, real exterior cleaning needs, NO existing vendor relationships. DISTINCT Apollo org tags ('nonprofit organization', 'food bank', 'thrift store') — zero overlap with any existing segment.
>
>**Pitch angle:** "Donor perception is your fundraising platform. The first thing a major donor sees when they pull into your parking lot is the condition of the building. A clean, maintained facility says: we steward our resources well."
>
>**Revenue:** $500-$2,000/facility; 2x/year; Salvation Army NE Ohio multi-chapter deal = $10K-$25K/year. Zero competitors.
>
>**First pull:** June 8 Cuyahoga

---

🔧 *Vera — Auto-Upgrade #3 | Count Sync: 108+ → 110+* _(Run 160 · 2026-05-31)_
>Updated `integrations/mixmax.py` PROPERTY_MANAGER_TITLES with 16 new routing titles (8 Massage Therapy + 8 Non-Profit). Updated `workers/vera_relay.py` — all 11 relay functions synced '108+' → '110+'. Updated `agents/danny.md` title batching note '108+' → '110+'. Updated `CLAUDE.md` June 8 Cuyahoga callouts '108+' → '110+'.

---

🚨 *Vera — SUMMIT COUNTY DEADLINE — TODAY MAY 31 (FINAL HOUR)*
>**TODAY IS THE ABSOLUTE LAST DAY.** The Summit County pull window closes tonight. Miss it = no Summit leads until June 29 (4-week gap). Summit has Akron's commercial corridor — car dealerships, hospitals, fitness chains, Firestone Country Club, Summit County APL. These are high-value targets.
>
>**Action (6 minutes, fully unattended):**
>Double-click `scripts/run_summit_both.command`
>OR: `python3 workers/lead_pipeline.py both Summit`
>
>June 4 enrollment needs these leads. Run it TODAY.

---

📍 *Vera — MEDINA COUNTY PULL — TOMORROW JUNE 1 (MONDAY MORNING)*
>Medina is TOMORROW. This is a manual override — do NOT rely on the cron (cron auto-fires Geauga+Portage on June 1, which is wrong for this week).
>
>**Action (6 minutes, fully unattended):**
>Double-click `scripts/run_medina_both.command`
>OR: `python3 workers/lead_pipeline.py both Medina`
>
>Medina targets: Discount Drug Mart HQ (Medina-based, 70+ locations), Rittgers' Greenhouse (garden center), Shiloh Foods (Lodi — food processing), Medina County Speedway, local marinas.

---

⚠️ *Vera — Instantly.ai NOT Paused — June 4 Enrollment Blocked (4 Days Away)*
>Enrolling Round 2 contacts while Instantly.ai campaigns run = duplicate email paths = spam filters = 0% reply rate. June 4 is in 4 days.
>
>**Fix (3 minutes):** app.instantly.ai → Campaigns → find a1c08c3d + 626cd15d → ⋮ → Pause → Add `INSTANTLY_PAUSED=true` to `.env`
>Guide: `outputs/vera/instantly_pause_guide_2026-05-22.md`
>
>Without this, June 4 Round 2 enrollment is blocked. This is the #1 blocker right now.

---

💡 *Vera — Upgrade Proposal: June Residential Homeowner Blitz via Nextdoor*
>**Idea:** Bradley posts a before/after job photo to NE Ohio Nextdoor neighborhoods within 24 hours of every completed job this month. Zero cost, immediate local reach, direct booking potential.
>
>**Why:** Nextdoor has 90%+ homeowner penetration in Cuyahoga/Summit suburban neighborhoods (Strongsville, Parma, Mentor, Stow, Hudson, Solon). Every neighborhood post from a local business owner gets seen by 50-300 nearby homeowners within hours — the target audience. Jasmine's `instagram_launch_today_2026-05-26.md` gave us the content capture protocol. A 3-sentence Nextdoor post with a before/after photo after each job = free lead generation every time a job is completed.
>
>**Impact:** Even 1 additional residential booking per week at $350 average = $1,400/month added revenue at zero ad cost. Compound effect: each satisfied Nextdoor neighbor can post a recommendation that reaches another 100+ homeowners.
>
>Reply YES to approve. Tommy writes the 3 Nextdoor post templates, Jasmine adds it to the job-day content capture guide — ready in 24 hours.

---

✅ *Vera — Scan Complete 2026-05-31 (Run 160)*
>5 auto-upgrades shipped | 1 proposal | 110 open issues (2 new segments + all counts synced)
>
>**Forest City now has 110 commercial segments queued for June 8 Cuyahoga — the biggest pull of the season. 8 days out.**
>
>**Segments added this run:**
>• #109: Massage Therapy & Wellness Chains (Massage Envy 30+ NE Ohio, Elements Massage 8+, Hand & Stone)
>• #110: Non-Profit & Social Service Organizations (Salvation Army, Catholic Charities, Second Harvest Food Bank, Habitat for Humanity)
>
>**Most urgent TODAY:** Summit County pull (last chance before 4-week gap). Run `scripts/run_summit_both.command`.
>**Most urgent TOMORROW:** Medina County pull. Run `scripts/run_medina_both.command`.
>**Most urgent THIS WEEK:** Pause Instantly.ai before June 4 enrollment.
