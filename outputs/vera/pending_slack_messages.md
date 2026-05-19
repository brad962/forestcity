🔧 *Vera — Auto-Upgrade*
>Changed: `PIPELINE_F` constant added to `workers/lead_pipeline.py`
>Why: Critical NameError — `run_pending_sequences()` used this variable on lines 592–643 but it was never defined, crashing every pipeline run and silently blocking all gas station / fleet auto-enrollment.
>File: `workers/lead_pipeline.py`

---

🔧 *Vera — Auto-Upgrade*
>Changed: `server.py` MIXMAX_SEQS and SEQ_LABELS now built dynamically from `integrations/mixmax.py` via `_build_seq_config()`
>Why: Was hardcoded to 3 sequences. When Bradley adds the gas station or fleet Mixmax ID, the dashboard will now auto-show those contacts without any second file to update. Fallback to hardcoded IDs keeps the dashboard working if the import fails.
>File: `server.py`

---

🔧 *Vera — Auto-Upgrade*
>Changed: `agents/danny.md` — added Gas Stations and Fleet Vehicle Washing as active secondary segments
>Why: Danny pulled 18 gas station contacts on 5/19 but the agent file still described him as PM-only. Added segment descriptions, current status, and enrollment instructions so the context is accurate next time Danny is activated.
>File: `agents/danny.md`

---

📋 *Vera — New Deliverable*
>Created: June Booking Blitz Campaign Brief — full 30-day execution plan for June 2026
>File: `outputs/donna/campaign_brief_june_booking_blitz_2026-05-19.md`
>Summary:
>• Phase 1 (June 1–7): Activate the existing pipeline — 5 contractor texts, 3 bridge emails, gas station enrollment, Danny cron
>• Phase 2 (June 8–14): Commercial lead flow — weekly PM pull resumes, LinkedIn outreach to hot leads
>• Phase 3 (June 15–21): Residential push — Facebook ads on, Nextdoor posts, GBP photos, review requests
>• Phase 4 (June 22–30): Double down on what's working
>
>⚠️ Key finding: Every asset needed for June is already written. Zero bottleneck except execution.

---

🚨 *Vera — MEMORIAL DAY FINAL COUNTDOWN — 7 Days*
>May 26 is 7 days away. This is the single highest-urgency window of the year. Here's what's ready RIGHT NOW — no writing needed, just send:
>
>*TEXT THESE 5 CONTRACTORS TODAY:*
>1. Land Pro Management — Anthony — 440-320-2779
>2. GTP Landscaping — Dontez — 440-396-0814
>3. Twin Improvements (number in pipeline_data.json)
>4. Reliable Roofing (number in pipeline_data.json)
>5. Pagels Construction (number in pipeline_data.json)
>→ Templates: `outputs/vera/sms_templates_contractors_2026-05-18.md`
>
>*ALSO THIS WEEK:*
>• Post 1 Facebook post (ready: `outputs/jasmine/` — Memorial Day posts batch)
>• Upload 1 photo to Google Business Profile (any clean job photo)
>• Text past customers: `outputs/tommy/past_customer_reengagement_2026-05-18.md`
>
>The window closes Sunday May 25. After that, the urgency is gone.

---

💡 *Vera — Upgrade Proposal*
>Idea: Create the "Gas Station & C-Store Outreach" Mixmax sequence — 18 verified contacts are staged and waiting
>Why: PIPELINE_F NameError is now fixed. `run_pending_sequences()` will actually work. The 18 gas station contacts are tagged with `_lead_type: gas_station` in `pipeline_data.json`. The sequence copy is written in `outputs/danny/sequence_gas_stations_2026-05-19.md`. All that's blocking enrollment is the Mixmax sequence ID.
>Impact: 18 commercial leads go live immediately on next pipeline run
>Action: Create sequence in Mixmax UI → copy the ID → paste into `integrations/mixmax.py` line 54 where it says `'id': 'PENDING'` → run `python3 workers/lead_pipeline.py` locally
>Reply YES to approve.

---

💡 *Vera — Upgrade Proposal*
>Idea: Approve Tommy's PM sequence rewrite — current copy has 42% opens but 0 replies
>Why: 45 enrolled, 0 replies means people are reading but not acting. Something in the body copy is failing. Tommy wrote a new 3-touch draft — better subject lines, harder CTAs, specific NE Ohio references.
>Impact: Even a 5% reply rate on 45 enrolled = 2–3 responses — could be worth $1,500–$3,000 in booked jobs
>File: `outputs/tommy/` — look for sequence rewrite files
>Reply YES to approve and Tommy will finalize the copy for upload to Mixmax.

---

✅ *Vera — Scan Complete 2026-05-19 (Run 17)*
>3 auto-upgrades shipped | 1 deliverable | 2 proposals | 42 RESOLVED | 12 OPEN
>
>🔑 Key fix this run: PIPELINE_F NameError — was silently crashing every pipeline run and blocking all gas station auto-enrollment. Now fixed.
>
>📋 New deliverable: June Booking Blitz brief — full 30-day commercial + residential plan. Every asset is already built. Execution is the only gap.
>
>⚠️ Top 3 actions for Bradley RIGHT NOW:
>1. TEXT 5 contractors today (Memorial Day 7 days out — numbers + templates ready)
>2. Run `python3 workers/lead_pipeline.py both` locally — 7 days overdue
>3. Create gas station Mixmax sequence (18 leads ready to enroll instantly)
