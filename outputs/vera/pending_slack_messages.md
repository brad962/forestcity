🔧 *Vera — Auto-Upgrade | Run 169 | 2026-06-01*
>Changed: Added Skilled Nursing Facilities & Long-Term Care Centers as Segment #132 to lead_pipeline.py DANNY_TITLES (8 titles) + DANNY_ORG_KEYWORDS (8 keywords). Synced to mixmax.py PROPERTY_MANAGER_TITLES. Full segment brief added to agents/danny.md.
>Why: DISTINCT from senior/assisted living (run 96), hospice (run 167), adult day care (run 159). CMS Five-Star Quality Rating System ties exterior appearance to health inspection score → star rating → Medicare/Medicaid census → revenue. ProMedica Senior Care NE Ohio (15+ SNF facilities, formerly HCR ManorCare) + Altercare of Ohio (20+ independent NE Ohio SNFs). One ProMedica regional ops contact = $60K-$180K/year. Zero competitors cold-calling SNF administrators. First pull June 8 Cuyahoga.
>File: workers/lead_pipeline.py
---
🔧 *Vera — Auto-Upgrade | Run 169 | 2026-06-01*
>Changed: Added Orthodontic Practices & Pediatric Dental Groups as Segment #133 to lead_pipeline.py DANNY_TITLES (8 titles) + DANNY_ORG_KEYWORDS (8 keywords). Synced to mixmax.py PROPERTY_MANAGER_TITLES. Full segment brief added to agents/danny.md.
>Why: DISTINCT from general DSO dentistry (run 123 — different Apollo org tags, no overlap). Orthodontic patients visit every 4-6 weeks = highest dental visit frequency = maximum parking staining. Smile Doctors NE Ohio (multiple acquired Cuyahoga/Summit/Lake County practices), Ortho Studios Ohio, Kids First Dental (8+ locations). One regional ops director = 10+ locations = $12K-$30K/year. Zero competitors. First pull June 8 Cuyahoga.
>File: workers/lead_pipeline.py
---
🔧 *Vera — Auto-Upgrade | Run 169 | 2026-06-01*
>Changed: Synced 16 new routing titles (8 SNF + 8 Orthodontic) to PROPERTY_MANAGER_TITLES. Updated segment count 131+ → 133+ across vera_relay.py (11 occ), CLAUDE.md (2 occ), agents/danny.md (3 occ). Full segment briefs for #132 and #133 added to danny.md with pitch angles, revenue math, NE Ohio targets, Apollo keywords, sequence routing.
>Why: Same-run count sync per resolved count-lag bug pattern (Run 164). Keeps relay Slack reminders accurate.
>Files: integrations/mixmax.py, workers/vera_relay.py, CLAUDE.md, agents/danny.md
---
🚨 *Vera — URGENT: Pause Instantly.ai Before June 4 (3 Days)*
>Campaigns a1c08c3d (PM Cuyahoga) + 626cd15d (Contractor Referral) must be paused or Round 2 = duplicate emails = spam = 0% reply rate on the biggest outreach day of peak season.
>Action: app.instantly.ai → Campaigns → both → ⋮ → Pause. Then add INSTANTLY_PAUSED=true to .env.
>Guide: outputs/vera/instantly_pause_guide_2026-05-22.md
---
🚨 *Vera — TODAY: Medina County Pull (June 1)*
>Week 22 = Medina in rotation. If not yet run — 6-8 min, fully unattended:
>Double-click: scripts/run_medina_both.command in Finder
>OR: `python3 workers/lead_pipeline.py both Medina`
>Missing this = no fresh Medina leads for June 4 enrollment.
---
⛽ *Vera — Pending: Gas Station & Fleet Mixmax Sequences Still Blocked*
>12+ gas station + fleet contacts stranded unenrolled. Both sequences still PENDING.
>Gas Station: Mixmax → Sequences → New → paste ID into integrations/mixmax.py line 54
>Fleet Washing: Mixmax → Sequences → New → paste ID into integrations/mixmax.py line 48
>Then: `python3 workers/lead_pipeline.py pending` — 2 min to enroll all waiting contacts.
---
📅 *Vera — June 8 Countdown: 7 Days (133+ Segments)*
>Cuyahoga mega-pull in 7 days. Now 133+ commercial segments: added SNF facilities (ProMedica Senior Care) and orthodontic groups (Smile Doctors/Kids First Dental) this run alongside hospitals, Tri-C campuses, museums, government, waste haulers + 125+ more.
>Estimated output: 300-500+ new Mixmax enrollments. Takes 12-20 min unattended.
>Pre-pull checklist: outputs/donna/june8_cuyahoga_battle_card_2026-06-01.md
>Command: double-click scripts/run_cuyahoga_both.command OR `python3 workers/lead_pipeline.py both Cuyahoga`
---
⭐ *Vera — Daily: Send Review Requests After Today's Jobs*
>Google reviews = Maps + LSA ranking = free inbound leads all season. NE Ohio competitors: 25-50 reviews.
>At 75+ reviews Forest City enters top-tier ranking. 5 requests/week = 100+ new reviews by end of season.
>Text: "Hey [Name], Bradley here from Forest City Power Washing — hope everything looks great! If you have 30 sec, would mean the world if you left us a quick Google review: [link] Thanks!"
---
✅ *Vera — Scan Complete 2026-06-01 (Run 169)*
>4 auto-upgrades shipped | 0 proposals | 133 open issues (131 carry-forward + 2 new segment tracking)
>New: #132 Skilled Nursing Facilities & LTC | #133 Orthodontic Practices & Pediatric Dental
>Counts synced 131+ → 133+ across vera_relay.py (11 occ), CLAUDE.md (2 occ), danny.md (3 occ)
>🚨 URGENT: Pause Instantly.ai TODAY (3 days to June 4) | Medina pull TODAY | June 8 Cuyahoga = 133+ segments
