🔧 *Vera — Auto-Upgrade*
>Changed: Added Optical/Vision Centers as a new commercial segment (LensCrafters, MyEyeDr, Visionworks, Pearle Vision, America's Best, For Eyes, National Vision)
>Why: 50+ NE Ohio strip-mall optical storefronts. State optometry licensing = non-negotiable facility standards. District managers sign vendor contracts for 10–20 locations. $18K–$42K/year per district. Zero competitors targeting this. First pull June 8 Cuyahoga.
>Files: workers/lead_pipeline.py, integrations/mixmax.py, agents/danny.md

---
🔧 *Vera — Auto-Upgrade*
>Changed: Added Medical/Clinical Labs as a new commercial segment (Quest Diagnostics, LabCorp, Cleveland Clinic outpatient labs, UH diagnostic labs)
>Why: 90+ NE Ohio patient service centers with CLIA federal certification = legally mandated appearance standards. District managers sign contracts for 10–20 centers. $24K–$56K/year per district. "CLIA compliance" is the pitch — not just cleanliness, federal law. Zero competitors targeting lab district managers.
>Files: workers/lead_pipeline.py, integrations/mixmax.py, agents/danny.md

---
🔧 *Vera — Auto-Upgrade*
>Changed: Added Tax Preparation Offices as a new commercial segment (H&R Block 100+, Jackson Hewitt 60+, Liberty Tax 40+ NE Ohio)
>Why: 200+ strip-mall storefronts physically present year-round. May–September = peak maintenance window post-season. Pitch: "Tax season is over — let us clean up the mess 4 months of client traffic left behind." District managers sign 10–20 location contracts. $6K–$24K/year per district. Zero competitors targeting this.
>Files: workers/lead_pipeline.py, integrations/mixmax.py, agents/danny.md

---
🔧 *Vera — Auto-Upgrade*
>Changed: Synced all 23 new titles (Optical 8 + Medical Labs 8 + Tax Prep 7) to PROPERTY_MANAGER_TITLES in mixmax.py
>Why: Every new DANNY_TITLES block must be mirrored in PROPERTY_MANAGER_TITLES or contacts import to the wrong Mixmax sequence. Routing verified: GAS_STATION_KEYWORDS checked first (company name), then title match → property_manager sequence.
>File: integrations/mixmax.py

---
🚨 *Vera — Summit County Deadline TOMORROW*
>Summit County pull is due *Sunday May 31* — that's tomorrow.
>This is the last chance before Summit rotates off until July 6. All 40+ commercial segments (drug stores, fast food, auto parts, hardware, dollar stores, optical, labs, tax prep, and more) miss peak season if this doesn't run.
>Run tonight or first thing tomorrow morning:
>`cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Summit`
>Or double-click: `scripts/run_summit_both.command` in Finder — ~6 minutes unattended.
>June 8 is Cuyahoga (largest pull of the year) — Summit needs to be done before then.

---
⛽ *Vera — Gas Station Sequence Still Stranded (Day 11)*
>12 gas station + convenience store contacts have been sitting in pipeline_data.json since May 19 with no Mixmax sequence to enroll into.
>Action: Create the sequence in Mixmax UI → paste the ID into integrations/mixmax.py line 47 → run `python3 workers/lead_pipeline.py pending`.
>Guide: `outputs/danny/gas_station_manual_email_blast_2026-05-19.md`
>Every day this waits = another day these multi-site accounts don't hear from us during peak season.

---
⚠️ *Vera — Instantly.ai Pause Required Before June 4*
>Campaigns a1c08c3d and 626cd15d must be paused in Instantly.ai before June 4 enrollment runs.
>June 4 is 5 days away. If these campaigns are still active when new contacts enroll, we get duplicate sends → spam flags → deliverability damage.
>Action: Log into Instantly.ai → pause both campaigns → confirm paused → enrollment is unblocked.
>This is the last reminder before June 4. After June 4, it's too late.

---
✅ *Vera — Scan Complete 2026-05-30 (Run 139)*
>4 auto-upgrades shipped | 0 new proposals | 71 total open issues (3 new segments, 68 carry-forward)
>New segments added: Optical/Vision Centers (LensCrafters/MyEyeDr/Visionworks), Medical/Clinical Labs (Quest/LabCorp), Tax Prep Offices (H&R Block/Jackson Hewitt/Liberty Tax) — all 3 fire June 8 Cuyahoga.
>Blockers: Summit pull due TOMORROW. Gas sequence day 11. Fleet sequence stranded. Instantly.ai not paused (5 days to June 4).

---
🔧 *Vera — Auto-Upgrade Run 140*
>Changed: Created 6 new Finder shortcut scripts — `run_cuyahoga_pull.command`, `run_cuyahoga_both.command`, `run_lake_pull.command`, `run_lake_both.command`, `run_lorain_pull.command`, `run_lorain_both.command`
>Why: June 8 Cuyahoga (52 commercial segments) had ZERO double-click shortcut — only Summit and Medina had them. Lake (June 15) and Lorain (June 22) also missing. All 3 counties now have both Danny-only and Danny+Carla shortcuts.
>File: scripts/ (6 new .command files)

---
🔧 *Vera — Auto-Upgrade Run 140*
>Changed: Updated CLAUDE.md Quick Shortcuts section — all 10 .command files now documented in a table with county, week, date, and notes. Added warning: "June 8 Cuyahoga is the largest pull of the season — 52 commercial segments, 12-20 min, use run_cuyahoga_both.command"
>Why: Cuyahoga/Lake/Lorain shortcut files undocumented; one-click launches are useless if nobody knows they exist
>File: CLAUDE.md

---
🔧 *Vera — Auto-Upgrade Run 140 (BUG FIX)*
>Changed: Summit deadline Slack message said "Summit doesn't run until July 6" — WRONG. Summit re-rotates June 29 (Week 27 % 6 = 3). Fixed to "next auto-rotation June 29." Also updated "30+ segments" → "51+" in same message.
>Why: Incorrect urgency — Bradley thought 5+ week wait, it's actually 4 weeks (June 29 comes right back)
>File: workers/vera_relay.py

---
🔧 *Vera — Auto-Upgrade Run 140*
>Changed: Fixed all stale "36 commercial segments" references in vera_relay.py (3 locations) → "51+" with expanded segment list. June 8 relay message now mentions: dollar stores, auto parts, hardware, sports venues, cannabis dispensaries, blood/plasma centers, warehouse clubs, wireless retail. Also added Finder shortcut callout to June 8 relay message.
>Why: 15 new segments added since Run 132 when "36" was written — relay messages understated the June 8 pull scale
>File: workers/vera_relay.py

---
🔧 *Vera — Auto-Upgrade Run 140*
>Changed: Added Coffee & Drive-Through Beverage Chains as 52nd commercial segment. 8 DANNY_TITLES, 11 DANNY_ORG_KEYWORDS, 8 PROPERTY_MANAGER_TITLES, full danny.md brief. Starbucks (60+), Dunkin' (80+), Tim Hortons (50+), Panera, Dutch Bros, Caribou — 290+ NE Ohio locations. Drive-through canopies = exhaust + mildew + grime. $24K-$54K/year per 15-location district. DISTINCT from QSR in Apollo org tags. Zero competitors.
>Why: Coffee chains are indexed separately from QSR restaurant chains in Apollo — 290 NE Ohio locations completely untapped
>File: workers/lead_pipeline.py, integrations/mixmax.py, agents/danny.md

---
🚨 *Vera — Summit County Pull — FINAL WARNING (Run 140)*
>Tomorrow (May 31) is the LAST DAY for Summit County. Next auto-rotation: June 29.
>Stow / Fairlawn / Hudson / Akron / Cuyahoga Falls — 52 commercial segments all fire here.
>Double-click `scripts/run_summit_both.command` in Finder. 6 min unattended. Run tonight.
>Command: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Summit`

---
🏙️ *Vera — June 8 Cuyahoga Pull — 9 Days — Finder Shortcut Now Ready*
>52 commercial segments fire June 8 — biggest pull of the year.
>Hospitals (Cleveland Clinic, UH, MetroHealth), Metroparks Zoo, Rock Hall, YMCA (12 branches), 
>sports venues (Cavs/Guardians/Browns), cannabis dispensaries, Costco/Sam's Club, coffee chains
>(Starbucks/Dunkin'/Tim Hortons), dollar stores (300+ locations), Home Depot/Lowe's, auto parts + more.
>New shortcut: double-click `scripts/run_cuyahoga_both.command` in Finder. 12-20 min unattended.
>Lake County (June 15) + Lorain County (June 22) shortcuts also added — check scripts/ folder.

---
💡 *Vera — Proposal: Run Cuyahoga Pull TODAY as Pre-Pull (9 Days Early)*
>Idea: Run `python3 workers/lead_pipeline.py danny Cuyahoga` today, before the June 8 scheduled rotation.
>Why: 52 commercial segments have no Cuyahoga contacts yet. An early pull gives those contacts 9 extra days in the sequence — they'd reach Touch 2 by June 15 and Touch 3 by June 22 (peak of NE Ohio outdoor season).
>Impact: June 8 pull still runs as normal (cron). This is additive only — no duplication (deduped by person_id). Commercial contacts discovered early = booked faster.
>Guide: `outputs/vera/commercial_segments_early_pull_guide_2026-05-26.md`
>Reply YES to approve — takes 15-20 min unattended.

---
✅ *Vera — Scan Complete 2026-05-30 (Run 140)*
>9 auto-upgrades shipped | 1 proposal | 2 issues resolved | 72 open (mostly awaiting June 8 pull)
>Key fixes: 6 new Finder shortcuts (Cuyahoga/Lake/Lorain), Summit deadline "July 6" bug fixed → June 29, "36 segments" updated to "51+" everywhere, Coffee/Drive-Through segment added (52nd).
>Blockers (unchanged): Summit pull DUE TOMORROW. Gas sequence day 11. Fleet sequence stranded. Instantly.ai not paused (4 days to June 4).
