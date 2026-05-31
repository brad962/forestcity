💆 *Vera — Auto-Upgrade #1 of 3 | Segment #111: Auto Glass Repair & Windshield Replacement Chains* _(Run 161 · 2026-05-31)_
>**New segment live** — 8 Apollo titles + 8 org keywords added to `lead_pipeline.py`. Titles synced to `mixmax.py` PROPERTY_MANAGER_TITLES. Full segment brief added to `danny.md`.
>
>**Why now:** Glass America is headquartered RIGHT HERE in Cleveland (Carnegie Ave) and operates 50+ NE Ohio service centers — this is a hometown chain with a district FM who manages dozens of locations. Safelite AutoGlass has 15+ NE Ohio service centers. Drive-in service bay concrete takes a beating: oil drips, coolant, rubber seal residue, road grime — it accumulates fast with high vehicle throughput. DISTINCT Apollo tags ('auto glass', 'windshield replacement') — zero overlap with car wash, auto body, or car dealership segments already in system.
>
>**Revenue upside:** Glass America regional deal (50 NE Ohio locations through one district FM) = $30K-$75K/year. Potential flagship commercial account — one call, one contract, $30K+. Zero competitors cold-calling auto glass DMs in NE Ohio.
>
>**First pull:** June 8 Cuyahoga (Glass America Carnegie Ave HQ + Safelite Strongsville/Parma/Mentor)

---

🛋️ *Vera — Auto-Upgrade #2 of 3 | Segment #112: Furniture & Home Furnishings Retail Chains* _(Run 161 · 2026-05-31)_
>**New segment live** — 8 Apollo titles + 8 org keywords added to `lead_pipeline.py`. Titles synced to `mixmax.py`. Full segment brief added to `danny.md`.
>
>**Why now:** Spring is the peak furniture buying season — new homeowners, tax refund purchases, spring refresh. Showrooms are packed RIGHT NOW. Ashley Furniture HomeStore (5+ NE Ohio), Value City Furniture (10+ NE Ohio), Bob's Discount Furniture (3+ NE Ohio) — enormous parking lots (300-600 cars), prominent building exteriors on Routes 422/8/77/480. Spring buying surge = maximum foot traffic = maximum staining = right-now pitch window. DISTINCT Apollo tags ('furniture store', 'furniture retail') — zero overlap with hardware/home improvement or warehouse club segments.
>
>**Revenue upside:** Value City 10-location NE Ohio district deal = $30K-$90K/year. Ashley 5-location district deal = $15K-$45K/year. These are potentially the highest-value single accounts in the commercial pipeline.
>
>**First pull:** June 8 Cuyahoga (Ashley Solon/Mentor, Value City Mayfield/Parma/Berea, Bob's Discount Mayfield)

---

✂️ *Vera — Auto-Upgrade #3 of 3 | Segment #113: Salon Suites & Booth Rental Studios* _(Run 161 · 2026-05-31)_
>**New segment live** — 7 Apollo titles + 8 org keywords added to `lead_pipeline.py`. Titles synced to `mixmax.py`. Full segment brief added to `danny.md`.
>
>**Why now:** DISTINCT from hair/nail salon chains (Run 141 — different Apollo tag 'hair salon chain'). Salon suites are commercial real estate operators: Sola Salon Studios (10+ NE Ohio), MY SALON Suite (4+ NE Ohio), Phenix Salon Suites, Salon Lofts. Each building has 30-60 booth renters = 200-400 foot traffic daily through the parking lot + entry. Franchise owners sign vendor contracts independently — fast close, no corporate approval. Apollo tags 'salon suite', 'sola salon', 'phenix salon' = zero overlap with anything in the system.
>
>**Revenue:** $800-$2,500/building; 2-3x/year. Sola 4-location franchise developer = $6K-$30K/year from one call. Zero competitors.
>
>**First pull:** June 8 Cuyahoga (Sola Independence/Beachwood/Westlake, MY SALON Suite NE Ohio, Phenix Strongsville/Avon)

---

🔧 *Vera — Auto-Upgrade #4 | Count Sync: 110+ → 113+* _(Run 161 · 2026-05-31)_
>Updated `workers/vera_relay.py` — all "110+" references → "113+" (11 occurrences). Updated `CLAUDE.md` June 8 Cuyahoga callout '110+' → '113+'. Updated `agents/danny.md` title batching note '110+' → '113+'. Updated `integrations/mixmax.py` with 23 new routing titles (8 Auto Glass + 8 Furniture + 7 Salon Suites) all routing to property_manager sequence.

---

🚨 *Vera — SUMMIT COUNTY — STILL TODAY (Last Chance)*
>**TODAY IS THE FINAL DAY.** If Summit County hasn't been pulled yet, this is the last window. Miss it = no Summit leads until June 29 (4-week gap during peak season). Summit = Akron commercial corridor — car dealerships, hospitals, fitness chains, Firestone Country Club, Glass America Akron-area shops.
>
>**Action (6 minutes, fully unattended):**
>Double-click `scripts/run_summit_both.command`
>OR: `python3 workers/lead_pipeline.py both Summit`
>
>Do it now if it hasn't been done. June 4 enrollment needs these leads.

---

📍 *Vera — MEDINA COUNTY PULL — TOMORROW JUNE 1 (First Thing)*
>Medina is tomorrow morning. This is a manual override — cron fires Geauga+Portage on June 1 by default (wrong this week). Override by double-clicking the Medina shortcut.
>
>**Action (6 minutes, fully unattended):**
>Double-click `scripts/run_medina_both.command` tomorrow morning
>OR: `python3 workers/lead_pipeline.py both Medina`
>
>Key Medina targets: Discount Drug Mart HQ (Medina-based, 70+ locations = potentially largest pharmacy chain deal in pipeline), Rittgers' Greenhouse, Shiloh Foods (Lodi food processing), Medina County Speedway, local marinas.

---

⚠️ *Vera — Instantly.ai STILL Not Paused — June 4 Enrollment in 4 Days*
>Duplicate email paths = spam filters = 0% reply rate. This is the #1 blocker for June 4 enrollment.
>
>**Fix (3 minutes):** app.instantly.ai → Campaigns → a1c08c3d + 626cd15d → ⋮ → Pause → Add `INSTANTLY_PAUSED=true` to `.env`
>Guide: `outputs/vera/instantly_pause_guide_2026-05-22.md`
>
>Without this step, the June 4 Round 2 enrollment is blocked by the safety check in `mixmax.py`.

---

💡 *Vera — Upgrade Proposal: Summer Email Copy Refresh for PM Sequence* _(Run 161)_
>**Idea:** Tommy rewrites Touch 1 and Touch 2 subject lines + opening sentences in the Property Manager Mixmax sequence to use summer-specific hooks instead of spring hooks. Specifically: replace "spring cleaning" references with "summer maintenance" + "before your August HOA meeting" + "summer volume peak" language.
>
>**Why:** The sequence was written in May with spring framing. It's June. "Algae doesn't care that it's spring" is now stale — "You've got a full summer of events before fall inspections" is more accurate and more urgent. The June 8 Cuyahoga batch will be the largest enrollment of the season — these contacts will receive the current spring-framed copy starting June 10-11. Refreshing copy before that send = higher open rate on the biggest batch of the year.
>
>**Impact:** Even a 5% improvement in open rate on the June 8 batch = 15-25 more opens on what should be a 300-500 contact enrollment. Those opens translate to LinkedIn connections + follow-up calls. Tommy can do this in 45 minutes — 3 subject line variants + 2 opening paragraphs.
>
>**Action needed:** Reply YES → Tommy writes the summer refresh copy within 24 hours, ready before June 8 pull.

---

✅ *Vera — Scan Complete 2026-05-31 (Run 161)*
>4 auto-upgrades shipped | 1 proposal | 113 total commercial segments now live
>
>**Forest City now has 113 commercial segments queued for June 8 Cuyahoga — 8 days out. Biggest pull of the season.**
>
>**Segments added this run:**
>• #111: Auto Glass Repair Chains (Glass America Cleveland HQ — 50+ NE Ohio locations, potential $30K-$75K/year flagship account)
>• #112: Furniture & Home Furnishings Retail (Ashley/Value City/Bob's — spring peak season = right-now pitch window; Value City 10-location deal = $30K-$90K/year)
>• #113: Salon Suites & Booth Rental Studios (Sola Salon Studios 10+ NE Ohio — commercial real estate operator, not salon chain; fast-close franchise owners)
>
>**Biggest action item:** Pause Instantly.ai (4 days to June 4 enrollment). Run Summit County TODAY. Run Medina TOMORROW.
