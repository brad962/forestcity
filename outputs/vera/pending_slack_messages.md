🔧 *Vera — Auto-Upgrade*
>Changed: Added 13 home-services keywords to CONTRACTOR_TITLES (chimney, hvac, pool service, pest control, junk removal, etc.)
>Why: Carla's new Home Services search category was pulling these leads but they'd misroute to property_manager sequence because their titles weren't in the classifier.
>File: `integrations/mixmax.py`
---
🔧 *Vera — Auto-Upgrade*
>Changed: run_carla() now logs + sends report_card when zero new leads found (all duplicates)
>Why: When Carla found no new contacts, the run was completely invisible — no log entry, no Slack notification. Now matches Danny's behavior.
>File: `workers/lead_pipeline.py`
---
🔧 *Vera — Auto-Upgrade*
>Changed: Added 'commercial real estate' and 'commercial property management' to DANNY_ORG_KEYWORDS
>Why: Office buildings, retail plazas, and warehouse complexes have facility managers who need exterior cleaning — they were invisible to Apollo's org-level filter because "commercial real estate" wasn't in the tag list.
>File: `workers/lead_pipeline.py`
---
📋 *Vera — New Deliverables (Run 13)*
>
>**Tommy: Objection Handling Cheat Sheet** — `outputs/tommy/objection_cheatsheet_2026-05-19.md`
>5 real objections with word-for-word responses + text versions + quick reference card.
>Objections covered: too expensive, do it myself, wait until later, didn't last before, need to ask partner.
>Bradley: print this and keep it in the truck.
>
>**Tommy: Estimate Follow-Up Template** — `outputs/tommy/estimate_followup_template_2026-05-19.md`
>3-touch post-quote sequence (same day / day 3 / day 7 break-up). Email + text versions. B2B PM version included.
>
>**Rick: Memorial Day Ads** — `outputs/rick/memorial_day_ads_2026-05-19.md`
>5 Facebook ad variations + 2 Google ad variations for May 21–27 surge. Budget recommendations included.
---
🚨 *Vera — URGENT: Contractors Still Waiting (Day 9)*
>**Bulletproof Lawncare | 216-307-4344** — "Very interested — send text"
>**Damrons Landscaping | 440-494-0422** — "Very interested — send text"
>
>Day-9 final texts: `outputs/vera/contractor_day9_texts_2026-05-19.md`
>Memorial Day execution checklist: `outputs/vera/memorial_day_execution_checklist_2026-05-19.md`
>
>Bradley: These 2 leads said they're interested. Today is the last window before reply rate drops below recovery. 5 minutes, 2 texts.
---
📌 *Vera — Pending Approvals (still waiting)*
>
>1. **Sequence rewrite** — 4-touch email copy, under 100 words each. Approve → I update Mixmax. File: `outputs/vera/sequence_rewrites_proposal_2026-05-18.md`
>2. **Bridge email** — send 1:1 from Gmail to 13 hot leads (2+ opens, no reply). File: `outputs/tommy/hot_lead_bridge_email_2026-05-19.md`
>3. **Memorial Day ads** — 5 Facebook variations, boost $30–40/day May 21–27. File: `outputs/rick/memorial_day_ads_2026-05-19.md`
>4. **LinkedIn outreach** — connect with 3–5 hot leads. Protocol: `outputs/danny/linkedin_hot_lead_dm_protocol_2026-05-18.md`
>
>Any 1 of these = progress this week.
---
✅ *Vera — Scan Complete 2026-05-19 (Run 13)*
>3 auto-upgrades shipped | 3 new deliverables | 32 total resolved issues | 14 open
>
>Biggest gap: 22 manual contractors at "New Lead" with no texts sent. SMS templates ready. Memorial Day window closes Friday May 23.
>
>Next: Bradley texts 2 hot contractors + activates 1 pending proposal.
