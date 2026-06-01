🔧 *Vera — Auto-Upgrade | Run 168 | 2026-06-01*
>Changed: Added Community Colleges & Technical Institutes as Segment #129 to lead_pipeline.py DANNY_TITLES (8 titles) + DANNY_ORG_KEYWORDS (8 keywords).
>Why: Tri-C has 4 Cuyahoga County campuses firing June 8; summer = buildings empty = maintenance window; facilities director signs multi-building contract; zero competitors; $32K-$100K/year from one FM contact. Apollo tags 'community college', 'technical college' return ZERO overlap with existing segments.
>File: workers/lead_pipeline.py
---
🔧 *Vera — Auto-Upgrade | Run 168 | 2026-06-01*
>Changed: Added Medical Equipment & Device Manufacturers as Segment #130 to lead_pipeline.py DANNY_TITLES (8 titles) + DANNY_ORG_KEYWORDS (9 keywords).
>Why: NE Ohio is a top-5 US medical device manufacturing cluster (Steris Mentor HQ, Invacare Elyria HQ, Nordson Westlake HQ). FDA 21 CFR Part 820 + ISO 13485 = exterior facility cleanliness documented as part of GMP compliance. Zero overlap with general manufacturing (run 118) or medical offices (run 101). Steris + Invacare = $50K-$200K/year potential.
>File: workers/lead_pipeline.py
---
🔧 *Vera — Auto-Upgrade | Run 168 | 2026-06-01*
>Changed: Added Pain Management & Spine Clinics as Segment #131 to lead_pipeline.py DANNY_TITLES (8 titles) + DANNY_ORG_KEYWORDS (9 keywords).
>Why: DISTINCT from ortho (run 166), chiropractic (run 152), PT (run 126). Pain management = chronic patients visit every 2-4 weeks = highest visit frequency of any specialty = highest parking/entry staining rate. Ohio Medical Board + DEA registration = facility licensing with appearance standard. Cleveland Clinic Pain Mgmt has 6+ NE Ohio sites; one practice manager contact = $16K-$50K/year. Zero competitors.
>File: workers/lead_pipeline.py
---
🔧 *Vera — Auto-Upgrade | Run 168 | 2026-06-01*
>Changed: Synced 24 new routing titles (8 Community Colleges + 8 Medical Device + 8 Pain Management) to PROPERTY_MANAGER_TITLES. Updated segment count 128+ → 131+ across vera_relay.py (11 occ), CLAUDE.md (2), agents/danny.md (2). Full segment briefs added to agents/danny.md for #129, #130, #131 with pitch angles, revenue math, NE Ohio target companies, Apollo keywords, and sequence routing.
>Why: Same-run count sync per resolved count-lag bug pattern (Run 164). Prevents stale counts in relay reminders.
>Files: integrations/mixmax.py, workers/vera_relay.py, CLAUDE.md, agents/danny.md
---
🚨 *Vera — URGENT: June 4 Deadline in 3 Days*
>Instantly.ai campaigns a1c08c3d (PM Cuyahoga) + 626cd15d (Contractor Referral) MUST be paused BEFORE June 4 enrollment or Mixmax will send duplicate emails → spam filter → 0% reply rate.
>Action: Go to app.instantly.ai → Campaigns → find both → ⋮ → Pause. Then add INSTANTLY_PAUSED=true to your .env file.
>Guide: outputs/vera/instantly_pause_guide_2026-05-22.md
>⏰ If you haven't done this yet — do it TODAY, not June 3.
---
🚨 *Vera — URGENT: Medina County Pull — TODAY (June 1)*
>Medina County pull was scheduled for today (June 1, ISO Week 22). If not yet run: double-click scripts/run_medina_both.command in Finder OR run:
>`python3 workers/lead_pipeline.py both Medina`
>Missing this = no fresh Medina leads for June 4 enrollment. Takes 6-8 minutes, fully unattended.
---
⛽ *Vera — Pending Action: Gas Station & Fleet Mixmax Sequences*
>Both sequences still PENDING — 12 gas station contacts + fleet contacts sitting unenrolled.
>Gas Station sequence: Create in Mixmax UI → paste ID into integrations/mixmax.py line 54
>Fleet Washing sequence: Create in Mixmax UI → paste ID into integrations/mixmax.py line 48
>Then run: `python3 workers/lead_pipeline.py pending` — enrolls all pending contacts in 2 minutes.
>Every week these sit PENDING = losing peak-season email response window.
---
📅 *Vera — June 8 Countdown: 7 Days Out*
>Cuyahoga mega-pull in 7 days — largest single-day commercial pull of the season.
>131+ commercial segments firing: hospitals, museums, government, Tri-C campuses, Steris Corp, pain clinics, hospice facilities, waste haulers, dermatology groups + 120+ more.
>Command: double-click scripts/run_cuyahoga_both.command OR:
>`python3 workers/lead_pipeline.py both Cuyahoga`
>Takes 12-20 minutes. Estimated output: 300-500+ new contacts enrolled in Mixmax.
>Pre-pull checklist: outputs/donna/june8_cuyahoga_battle_card_2026-06-01.md
---
✅ *Vera — Scan Complete 2026-06-01 (Run 168)*
>4 auto-upgrades shipped | 0 proposals | 131 open issues (128 carry-forward + 3 new segment tracking)
>New segments: #129 Community Colleges & Technical Institutes | #130 Medical Device Manufacturers | #131 Pain Management & Spine Clinics
>All counts synced: 128+ → 131+ across vera_relay.py (11 occ), CLAUDE.md (2), danny.md (2)
>🚨 URGENT: June 4 Instantly.ai pause deadline (3 days) | TODAY = Medina pull day | June 8 = Cuyahoga mega-pull (7 days)
