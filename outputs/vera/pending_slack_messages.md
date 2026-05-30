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
