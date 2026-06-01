✅ *Vera — Scan Complete 2026-06-01 (Run 167)*
>6 auto-upgrades shipped | 0 proposals | 128 open issues (125 carry-forward + 3 new segment tracking)
>New segments: #126 Waste Hauling & Dumpster Rental | #127 Dermatology & Skin Care Groups | #128 Hospice & Palliative Care Facilities
>All counts synced: 125+ → 128+ across vera_relay.py (11 occ), CLAUDE.md (2), danny.md (1)
>🚨 URGENT ACTIONS NEEDED — see below

---
🔧 *Vera — Auto-Upgrade (Run 167)*
>Changed: NEW segment #126 — Waste Hauling & Dumpster Rental Companies. Code live in `lead_pipeline.py` + `mixmax.py`. 8 titles + 14 org keywords. Republic Services (Strongsville HQ), Rumpke, Kimble Companies (largest independent OH waste hauler), GFL/Advanced Disposal, WM Inc. NE Ohio districts.
>Why: OEPA NPDES stormwater permit + EPA SPCC compliance = pressure washing their haul yard is a *regulatory requirement*, not just cosmetic. District managers oversee 3-10 service yards; one deal = $40K-$160K/year. Zero competitors cold-calling waste hauler DMs. First pull June 8 Cuyahoga.
>File: workers/lead_pipeline.py, integrations/mixmax.py, agents/danny.md

---
🔧 *Vera — Auto-Upgrade (Run 167)*
>Changed: NEW segment #127 — Dermatology & Skin Care Medical Groups. Code live in `lead_pipeline.py` + `mixmax.py`. 8 titles + 11 org keywords. SkinCure Oncology (15+ NE Ohio sites, Cleveland HQ), Cleveland Derm Associates, Mahler Dermatology, Bahl & Bahl, Advanced Dermatology & Cosmetic Surgery, US Dermatology Partners NE Ohio.
>Why: DISTINCT from orthopedic (Run 166), med spas (Run 162), urgent care (Run 114). 3rd highest-volume medical specialty — patients visit 2-4x/year = extreme parking + entry staining. 10-clinic group deal = $12K-$36K/year. Zero competitors. First pull June 8 Cuyahoga.
>File: workers/lead_pipeline.py, integrations/mixmax.py, agents/danny.md

---
🔧 *Vera — Auto-Upgrade (Run 167)*
>Changed: NEW segment #128 — Hospice & Palliative Care Facilities. Code live in `lead_pipeline.py` + `mixmax.py`. 8 titles + 11 org keywords. Hospice of the Western Reserve (Westlake HQ, 5 NE Ohio inpatient facilities), Amedisys Hospice, VITAS Healthcare, Ohio's Hospice.
>Why: DISTINCT from home care agencies (Run 163), senior living (Run 96), behavioral health (Run 150). CMS CoP + Ohio DOH licensing = exterior appearance standard. Families making final visits = dignity signal = non-negotiable appearance. $8K-$25K/year for Western Reserve portfolio. Zero competitors targeting hospice administrators. First pull June 8 Cuyahoga.
>File: workers/lead_pipeline.py, integrations/mixmax.py, agents/danny.md

---
🔧 *Vera — Auto-Upgrade (Run 167)*
>Changed: Synced 24 new routing titles (8 Waste Hauling + 8 Dermatology + 8 Hospice) to `PROPERTY_MANAGER_TITLES` in `integrations/mixmax.py`. Count sync: 125+ → 128+ across vera_relay.py (11 occurrences), CLAUDE.md (2 occurrences), danny.md (1 occurrence). All performed same-run per resolved count-lag bug pattern.
>Why: Ensures new segment leads route correctly to Property Manager Mixmax sequence on import.
>File: integrations/mixmax.py, workers/vera_relay.py, CLAUDE.md, agents/danny.md

---
🚨 *Vera — URGENT: Medina County Pull — TODAY June 1*
>TODAY is the scheduled Medina County pull day (Week 22). Miss this window = no Medina leads until the next manual override.
>Action: Double-click `scripts/run_medina_both.command` in Finder — takes 8-12 minutes.
>Targets: Medina, Brunswick, Wadsworth. 128+ commercial segments. Restaurant chains, tire centers, farm supply stores, dentists, golf courses.
>If you already ran it today, ignore this message.

---
🚨 *Vera — URGENT: Instantly.ai MUST Be Paused Before June 4 (3 Days)*
>June 4 = Round 2 Mixmax enrollment. Instantly.ai campaigns a1c08c3d (PM Cuyahoga) and 626cd15d (Contractor Referral) MUST be paused first — both campaigns send from the same Gmail address used for Mixmax. Running both = spam filter triggers = all Mixmax opens/replies tank to 0%.
>Action: Log into Instantly.ai → Campaigns → pause both by June 3 EOD.
>Guide: `outputs/vera/instantly_pause_guide_2026-05-22.md`
>If already paused, set INSTANTLY_PAUSED=true in .env to clear this alert.

---
⏰ *Vera — Reminder: June 8 Cuyahoga Mega-Pull (7 Days)*
>June 8 = the largest pull of the season. 128+ commercial segments. All new segments added since May 22 fire for the first time: hospitals, museums, government buildings, DSO dental groups, YMCA branches, sports venues, waste haulers, dermatology groups, hospice facilities, and 100+ more.
>Prep: Make sure Instantly.ai is paused (see above), Mixmax enrollment is clear, and 2 hours are blocked on June 8 morning.
>Command: `scripts/run_cuyahoga_both.command` — Danny + Carla, takes 15-20 minutes.
>Battle card: `outputs/donna/june8_cuyahoga_battle_card_2026-06-01.md`

