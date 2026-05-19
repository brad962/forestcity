🔧 *Vera — Auto-Upgrade*
>Changed: `server.py` — removed hardcoded Apollo API key from `/api/apollo/linkedin` endpoint; added `APOLLO_KEY = os.environ.get('APOLLO_KEY', '')` at module level
>Why: Live API credential was committed to GitHub in plain text — same security class as MIXMAX_TOKEN (run 7) and Workiz credentials (run 8) already fixed
>File: `server.py`
---
🔧 *Vera — Auto-Upgrade*
>Changed: `utils/report_card.py` — added Linux font fallback via `_find_font()` helper; now uses Liberation Sans on Linux/cloud before falling back to PIL bitmap default
>Why: All Mac font paths (`/System/Library/Fonts/...`) were silently failing in the cloud CI environment — report cards rendered with unreadable tiny text
>File: `utils/report_card.py`
---
🔧 *Vera — Auto-Upgrade*
>Changed: `agents/danny.md` — corrected Tools section: Mixmax marked as active enrollment platform, Instantly.ai marked "not active," HubSpot marked "pending," Apollo endpoint URL corrected to match actual script
>Why: Agent file referenced dead tools as if they were active — Instantly.ai and HubSpot have never been connected; Mixmax is what's actually running leads
>File: `agents/danny.md`
---
🚨 *Vera — URGENT | Day 6 — Contractors Still Waiting*
>*Bulletproof Lawncare* | 📞 216-307-4344 — said "very interested" on May 13
>*Damrons Landscaping* | 📞 440-494-0422 — said "very interested" on May 13
>
>That was 6 days ago. No text sent. Confirmed in pipeline_data.json.
>
>Text to send NOW: *"Hey [name], Bradley from Forest City Power Washing — we spoke last week about the referral program. Still interested? Happy to jump on a quick call or chat by text."*
>
>Every day you wait, this cools. These are contractor referral partners — one deal = recurring jobs all season.
>Full conversation tree for every reply: `outputs/vera/contractor_conversation_tree_2026-05-18.md`
---
💡 *Vera — Upgrade Proposal*
>Idea: Add week-over-week delta to Nina's weekly pipeline report (e.g. "Enrolled: 45 ▲+12 vs. last week")
>Why: Current report shows absolute numbers with no trend — Bradley can't tell if the pipeline is growing or stagnating without doing manual math each week
>Impact: Instant signal on pipeline health; flags weeks with 0 new enrollments before they compound into a dry spell
>Reply YES to approve and I'll implement it in `workers/nina_report.py`.
---
💡 *Vera — Upgrade Proposal*
>Idea: Monday morning SMS batch prep — auto-generate a ready-to-send text for every "New Lead" in pipeline_data.json with blank `last_contact`
>Why: 21 manual contacts currently have "Send text" in notes and no last_contact date — stale detection can't fire, and they're just sitting. A Monday batch list means Bradley opens his phone and texts 3–5 people in 10 minutes instead of figuring out who to contact.
>Impact: Converts warm manual leads into booked estimates. Currently zero automated follow-up system for these contacts.
>Reply YES to approve and I'll build the SMS prep worker.
---
💡 *Vera — Pending Approvals (Still Open)*
>These proposals are ready to ship — no new work needed, just your YES:
>1. Sequence rewrite (0% reply rate) → `outputs/vera/sequence_rewrites_proposal_2026-05-18.md`
>2. LinkedIn for 13 hot leads (3/day) → `outputs/danny/linkedin_hot_lead_dm_protocol_2026-05-18.md`
>3. GBP activation (free, immediate) → `outputs/marcus/gbp_optimization_guide_2026-05-18.md`
>4. Review request texts after jobs → `outputs/tommy/review_request_sequence_2026-05-18.md`
---
✅ *Vera — Scan Complete 2026-05-19 (Run 9)*
>3 auto-upgrades shipped | 2 new proposals | 14 open issues | 22 resolved all-time
>
>Security fixes complete: All 3 hardcoded API credentials now removed from source (MIXMAX_TOKEN run 7, WORKIZ run 8, APOLLO_KEY run 9).
>
>Top 3 for Bradley TODAY:
>1. 📱 Text Bulletproof + Damrons — Day 6. Use the conversation tree. 5 minutes.
>2. 🌐 Open Google Business Profile — 30 min setup = free homeowner leads all summer.
>3. ⚙️ Paste cron jobs from CLAUDE.md into `crontab -e` — pipeline hasn't pulled leads in 7 days.
