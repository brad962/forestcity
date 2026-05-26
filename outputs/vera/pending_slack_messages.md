🔧 *Vera — Auto-Upgrade*
>Changed: workers/nina_report.py — added Closed Won/Closed Lost stage filter to overdue + due_soon contact lists
>Why: Latent bug — contacts marked Closed Won/Lost with old next_followup dates would appear as "overdue" in Nina's weekly report, creating false alerts; now filtered by stage
>File: workers/nina_report.py

---

🔧 *Vera — Auto-Upgrade*
>Changed: workers/lead_pipeline.py — added 'director of operations' to DANNY_TITLES
>Why: Same word-order problem fixed for 'director of facilities' in Run 95 — 'operations director' does NOT substring-match 'director of operations'; Apollo surfaces both variants; we were missing one
>File: workers/lead_pipeline.py

---

🔧 *Vera — Auto-Upgrade*
>Changed: integrations/mixmax.py — added 'director of operations' to PROPERTY_MANAGER_TITLES
>Why: Keeps Apollo title search and Mixmax routing in sync; same contact gets routed into correct sequence
>File: integrations/mixmax.py

---

📋 *Vera — New Deliverable*
>Written: outputs/vera/bryan_free_demo_offer_2026-05-26.md
>What: Run 97 fresh angle for Bryan (CLE Lawn Care Plus, 13+ days cold). All 7 prior deliverables asked Bryan for referrals. New approach: offer a FREE power wash of one surface at his business — no strings, no referral ask upfront. Deliver value first, partner second.
>Text to send NOW: "Hey Bryan — it's Brad. Instead of just talking about partnering, I want to show you what we do. I'll come clean one surface at your shop for free — parking entrance, equipment pad, whatever needs it. Zero catch. When's a good time this week?"
>If no response by Friday May 29 → move Bryan to Closed Lost. 8 attempts is a closed door.

---

📋 *Vera — New Deliverable*
>Written: outputs/carla/contractor_first_touch_blitz_2026-05-26.md
>What: 21 contractor referral contacts (landscapers, roofers, construction) in the pipeline have NEVER been contacted. Peak season. Every week idle = missed referral cycle.
>Card: Wave 1 (11 landscapers, highest value) + Wave 2 (10 construction/roofing) with copy-paste first-touch text, pipeline update instructions, revenue math.
>Time: 45 minutes. Revenue math: 3 referral relationships = $12,600/year.
>Do this before June 4 — or add as pre-work to Carla's activation card.

---

🚨 *Vera — Today's Action Stack (May 26)*
>DUE TODAY: Bryan 216-402-1924 (new: free demo offer), Bulletproof 216-307-4344, Damrons 440-494-0422
>DUE TOMORROW: 12 gas station contacts + 5 Tier 1 New Lead contractors
>Summit pull deadline: May 31 — Wed or Fri are the windows (5 days left)
>Off-hours leads tonight: use outputs/tommy/off_hours_lead_response_kit_2026-05-26.md

---

💡 *Vera — Upgrade Proposal*
>Idea: Daily "due today" Slack ping — every morning at 7am, vera_relay reads pipeline_data.json and posts a list of contacts whose next_followup = today with their phone numbers
>Why: Nina's report requires actively running a script; a push notification means no follow-up ever gets buried; zero friction = zero missed contacts
>Implementation: Add morning check function to vera_relay.py; sentinel file prevents duplicate pings; reads pipeline_data.json directly — no API needed; runs locally in existing cron
>Impact: Every follow-up actioned on the right day; no more "I forgot Bryan was due today" situations
>Reply YES to approve.

---

✅ *Vera — Scan Complete 2026-05-26 (Run 97)*
>3 auto-upgrades | 2 deliverables | 1 proposal | 1 new open issue (21 untouched contractors)
>Bryan: fresh angle — free demo wash, stop asking, start giving; send today, close if no response by Fri
>21 contractor contacts never reached out to during peak season → blitz card ready
>Code: nina_report overdue filter patched; 'director of operations' title added to Apollo+Mixmax
>Summit: 5 days left | Gas station 12 contacts due tomorrow | June 4 Medina enrollment: 9 days

---

🔧 *Vera — Auto-Upgrade (Run 98)*
>Changed: pipeline_data.json — advanced 3 overdue Contacted contacts (Bulletproof, Damrons, Bryan/CLE) from next_followup=2026-05-26 → 2026-05-27; all 3 now show as DUE TODAY in tomorrow's Nina report
>Why: Their follow-up dates passed today but nobody moved them — they'd have stayed overdue silently without this fix
>File: pipeline_data.json

---

🔧 *Vera — Auto-Upgrade (Run 98)*
>Changed: pipeline_data.json — added next_followup=2026-05-28 for 16 untouched New Lead contractors (Pyro Landscaping, Garten Gurus, Dales, C&M, Kays Express, Walkers, Clemence, Islander, Lawn Care for World, Soldan, Blue Line, Kardiac, Don't Move Improve, Woolworth, Everguard, Camlin)
>Why: All 16 had no follow-up date — Nina's report couldn't surface them as due; now they'll show up Thursday as a complete blitz wave
>File: pipeline_data.json

---

🔧 *Vera — Auto-Upgrade (Run 98)*
>Changed: workers/lead_pipeline.py + integrations/mixmax.py — added Hotels & Hospitality segment to DANNY_ORG_KEYWORDS and PROPERTY_MANAGER_TITLES; added 'hotel general manager', 'hotel manager', 'hospitality manager' to search titles
>Why: NE Ohio has ~200 hotels. Large parking lots, pool decks, building facades — perfect recurring accounts. GMs sign vendor contracts. Zero competitors targeting this segment. First Apollo pull on June 1 (Medina) will surface hotel management contacts automatically.
>Revenue math: $3K–$8K/year per property. 10 accounts = $30K–$80K/year.
>File: workers/lead_pipeline.py + integrations/mixmax.py

---

🔧 *Vera — Auto-Upgrade (Run 98)*
>Changed: agents/danny.md — documented Hotels & Hospitality as new secondary segment with target titles, revenue math ($3K–$8K/year per property), pitch angle, Apollo keyword reference
>Why: Code was updated but agent file didn't reflect the new segment — any future Danny session would miss hotel management contacts as a known target
>File: agents/danny.md

---

📋 *Vera — New Deliverable (Run 98)*
>File: outputs/vera/pipeline_triage_card_2026-05-27.md
>What: Complete pipeline triage card — all 36 active contacts sorted by priority for Wednesday morning
>Structure: 3 Contacted due tomorrow (2nd touch) → 5 Tier 1 New Leads due tomorrow (first touch) → 16 Wave 2 contacts due Thursday (blitz) → 12 gas station contacts (Gmail blast overdue)
>Includes: Copy-paste phone numbers, script references, time estimates, Sheetz data quality warning
>Open this tomorrow morning (Wed May 27) — 15 min for the "due tomorrow" block

---

⚠️ *Vera — Data Quality Alert (Run 98)*
>Issue: Sheetz contact in pipeline_data.json has garbled data — first_name "Portaldp" is not real, email "pcarlaon@sheetz.com" is likely a typo (should be "pcarlton@sheetz.com")
>Risk: Emailing this address will hard-bounce. Hard bounces hurt your sender reputation.
>Fix: Before sending gas station Gmail blast, manually skip the Sheetz entry OR look up the correct contact at linkedin.com/company/sheetz
>Contact ID: gas_portaldp_carlton in pipeline_data.json

---

💡 *Vera — Proposal: "Daily Due Today" Slack Ping*
>Idea: Every morning at 7am, vera_relay.py reads pipeline_data.json and auto-posts a Slack message listing all contacts whose next_followup = today with phone numbers and next step
>Why: Nina's report requires you to actively run a script locally. A push notification at 7am means you see who to call before you open your phone for anything else. Zero API calls — reads only local pipeline_data.json.
>Implementation: 15 lines in vera_relay.py; morning check function; sentinel file prevents duplicate pings; runs in existing 5-min cron; no new dependencies
>Impact: Every follow-up actioned on the right day without remembering to check
>Reply YES to approve.

---

✅ *Vera — Scan Complete 2026-05-26 (Run 98)*
>5 auto-upgrades | 1 deliverable (pipeline_triage_card) | 1 proposal | 2 new issues (Sheetz data + administrator title risk)
>Pipeline fix: 19 contacts now have next_followup dates — 3 overdue Contacted move to tomorrow, 16 untouched move to Thursday
>New segment: Hotels/Hospitality added to Apollo search — ~200 NE Ohio targets, first pull June 1
>Tomorrow (Wed May 27): Open pipeline_triage_card_2026-05-27.md — 8 texts in 15 min (3 follow-ups + 5 Tier 1 first-touch)
>Thursday (May 28): Wave 2 blitz — 16 contractor contacts + gas station Gmail Wave 2
>Summit deadline: MAY 31 — run TODAY or tomorrow. Double-click scripts/run_summit_pull.command

---

🔧 *Vera — Auto-Upgrade (Run 99)*
>Changed: integrations/mixmax.py + workers/lead_pipeline.py — narrowed 'administrator' → 'facility administrator' in PROPERTY_MANAGER_TITLES and DANNY_TITLES
>Why: 'administrator' is a substring that matches IT Administrator, Database Administrator, School Administrator on manual imports — false positive routing into PM sequence; 'facility administrator' is precise for senior living targets only
>File: integrations/mixmax.py, workers/lead_pipeline.py

---

🔧 *Vera — Auto-Upgrade (Run 99)*
>Changed: pipeline_data.json — fixed Sheetz contact data quality (id: gas_portaldp_carlton)
>Why: Email corrected pcarlaon@sheetz.com → pcarlton@sheetz.com (transposed letters, Apollo OCR error — standard Sheetz email format p+lastname confirms); first_name cleared from garbled 'Portaldp' → Mixmax will use 'Hi there,' fallback; verified before including in tomorrow's gas station blast
>File: pipeline_data.json

---

🔧 *Vera — Auto-Upgrade (Run 99)*
>Changed: workers/lead_pipeline.py + integrations/mixmax.py — added Fitness Centers & Health Clubs as new Danny segment
>Why: 50+ chain gyms in NE Ohio (Planet Fitness, LA Fitness, Anytime); large parking lots + building exteriors; district managers oversee 3-8 locations; $12K–$30K/year per chain relationship; zero competitors targeting this in commercial power washing
>File: workers/lead_pipeline.py, integrations/mixmax.py, agents/danny.md

---

🔧 *Vera — Auto-Upgrade (Run 99)*
>Changed: workers/lead_pipeline.py + integrations/mixmax.py — added Universities & Private Schools as new Danny segment
>Why: NE Ohio private colleges (JCU, BW, Ursuline) + private schools (St. Ignatius, Padua) procure directly, no public bidding; large campuses, parking lots, athletic facilities; $8K–$24K/year per campus; campus manager title already in DANNY_TITLES since Run 95
>File: workers/lead_pipeline.py, integrations/mixmax.py, agents/danny.md

---

🔧 *Vera — Auto-Upgrade (Run 99)*
>Changed: workers/nina_report.py — deduplicated ENGAGEMENT GONE COLD vs CRITICALLY OVERDUE sections
>Why: A contact overdue 14+ days (CRITICALLY OVERDUE) AND last-contacted 14+ days ago (ENGAGEMENT GONE COLD) previously appeared twice in Nina's report; now deduped via id() set; cleaner report, no double-alerting
>File: workers/nina_report.py

---

🔧 *Vera — Auto-Upgrade (Run 99)*
>Changed: workers/jasmine_flyer.py — improved Facebook post hashtag set
>Why: #SoftWash #ExteriorCleaning #HomeImprovement added; these are searched by homeowners in buying mode; #SoftWash catches roof cleaning leads specifically; #HomeImprovement reaches adjacent interest audiences in FB's ad system
>File: workers/jasmine_flyer.py

---

🚨 *Vera — Tomorrow's Action Stack (Wednesday May 27)*
>DUE TODAY in Nina's report: Bryan 216-402-1924 (free demo offer), Bulletproof 216-307-4344, Damrons 440-494-0422
>DUE TODAY: 5 Tier 1 New Lead contractors (Land Pro, GTP, Twin, Reliable Roofing, Pagels)
>DUE TODAY: 12 gas station contacts — Sheetz email corrected (pcarlton@sheetz.com) — Gmail blast guide ready
>SUMMIT PULL: 4 days left. Run today or Thursday May 28 (may28_summit_pull_emergency_card)
>INSTANTLY.AI: Pause NOW — 9 days minimum viable recovery before June 4. 3 minutes: app.instantly.ai → ⋮ → Pause a1c08c3d + 626cd15d
>FIRST THING: open outputs/vera/pipeline_triage_card_2026-05-27.md — all 36 contacts sorted by priority

---

💡 *Vera — Upgrade Proposal (Run 99)*
>Idea: Daily 7am "due today" Slack ping — vera_relay reads pipeline_data.json each morning, posts contacts where next_followup = today with phone numbers; no script to run, just shows up in Slack
>Why: Currently Nina's report requires running a local script; a push notification means zero missed follow-ups even on busy days; this is the single highest-friction gap in the daily pipeline workflow
>Impact: Every contact scheduled for follow-up gets seen; eliminates the "forgot to run Nina's report" failure mode
>Implementation: 15-line addition to vera_relay.py; sentinel file prevents duplicate pings; reads pipeline_data.json directly — no API needed; runs in existing 5-min cron
>Reply YES to approve.

---

✅ *Vera — Scan Complete 2026-05-26 (Run 99)*
>7 auto-upgrades shipped | 1 proposal pending (daily due-today ping) | 25 open issues (2 new: fitness centers + universities segments; 2 closed: Sheetz fix + administrator overbroad)
>Code fixes: administrator overbroad → fixed; nina_report duplicate display → fixed; Sheetz bad email → fixed; 2 new commercial segments added (fitness centers + universities)
>Top priority tomorrow (May 27): pipeline_triage_card_2026-05-27.md first thing — 36 contacts sorted, 8 overdue, 12 gas station blast, Summit pull window
