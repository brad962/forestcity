🔧 *Vera — Auto-Upgrade*
>Changed: `detect_lead_type()` in `integrations/mixmax.py` now checks `GAS_STATION_KEYWORDS` and `FLEET_KEYWORDS`
>Why: Both keyword lists were defined but never called — gas station or fleet leads without an explicit `_lead_type` would silently route to the PM sequence. Now correctly detected and routed to their own sequences.
>File: `integrations/mixmax.py`

---

🔧 *Vera — Auto-Upgrade*
>Changed: `run_pending_sequences()` cache write in `workers/lead_pipeline.py` — fixed silent data loss bug
>Why: After enrolling pending contacts, the function was re-reading the cache file from disk and writing it back unchanged — discarding all `mixmax_enrolled = True` marks set in memory. Same contacts would be re-attempted every pipeline run forever. Now writes the in-memory `cache` dict directly.
>File: `workers/lead_pipeline.py`

---

🚨 *Vera — URGENT: Touch 3 fires May 22 — check Mixmax NOW*
>Your PM sequence Touch 3 sends in 3 days. 42% open rate. 0 replies. Before the last email goes out, spend 10 minutes diagnosing WHY.
>
>**Step 1:** Mixmax → PM Sequence → Settings → check Reply-To address. If it's NOT your email — replies are sitting somewhere you're not looking. Fix it today.
>
>**Step 2:** Send a test enrollment to yourself. Read it as a recipient. Does `{{firstName}}` render as your name or as literal text?
>
>**Step 3:** Mixmax → Recipients → filter by status → how many are "Unsubscribed"?
>
>Full diagnostic: `outputs/vera/reply_rate_diagnostic_2026-05-19.md`
>
>If Reply-To is wrong: replies already came in — you just can't see them. Fix the address and check the Mixmax-side inbox.

---

🚨 *Vera — MEMORIAL DAY IS 5 DAYS OUT — Execute Today*
>Assets are built. Zero writing needed. This is an action list.
>
>*TODAY (May 19):*
>• Text Bulletproof Lawncare (216-307-4344) — Day-9 template ready in `outputs/vera/contractor_day9_texts_2026-05-19.md`
>• Text Damrons Landscaping (440-494-0422) — same file
>• Post Facebook post #1 — `outputs/jasmine/memorial_day_posts_2026-05-19.md`
>• Text 3 past customers — `outputs/tommy/past_customer_reengagement_2026-05-18.md`
>
>*Wednesday May 21:*
>• Upload 1 job photo to Google Business Profile (15 min)
>• Text remaining Tier 1 contractor leads
>
>*Friday May 23 (last push):*
>• Post urgency Facebook post + LinkedIn post
>• Send bridge email to top 3 hot leads from your Gmail (NOT Mixmax)

---

💡 *Vera — Proposal: Approve Sequence Rewrite Before Touch 3*
>Idea: Approve Tommy's PM sequence rewrite and upload new copy to Mixmax before May 22
>Why: 0% reply rate means the current body copy isn't converting. Touch 3 is the last email — it's also the last chance to present a specific offer. Tommy's rewrite has a harder CTA and includes the "free property walk" offer as a concrete ask.
>Impact: Even getting 1 reply from Touch 3 = potential $500–$1,500 job
>Action: Reply YES and Tommy will finalize 3-touch copy for Mixmax upload. Done same day.

---

💡 *Vera — Proposal: Gas Station Mixmax Sequence*
>18 contacts staged and waiting. run_pending_sequences() bug now fixed. As soon as the ID goes live, they auto-enroll.
>Action: Mixmax UI → New Sequence → name it "Forest City Power Washing — Gas Station & C-Store Outreach" → copy sequence from `outputs/danny/sequence_gas_stations_2026-05-19.md` → paste the sequence ID into `integrations/mixmax.py` line 54 where it says `'id': 'PENDING'` → run `python3 workers/lead_pipeline.py` locally.
>Reply YES to approve.

---

✅ *Vera — Scan Complete 2026-05-19 (Run 18)*
>2 auto-upgrades shipped | 2 proposals | 44 RESOLVED | 12 OPEN
>
>🔑 Key fixes this run:
>• Silent bug: run_pending_sequences() was discarding enrollment marks on every run — fixed
>• Logic gap: GAS_STATION_KEYWORDS and FLEET_KEYWORDS were defined but never used in routing — fixed
>
>📋 New deliverable: Reply rate diagnostic with 5 hypotheses + specific test steps for Bradley
>
>⚠️ Top 3 actions for Bradley RIGHT NOW:
>1. Check Mixmax Reply-To setting TODAY (Touch 3 fires May 22 — replies may be in wrong inbox)
>2. Execute Memorial Day texts today (5 days left — templates all ready)
>3. Create gas station Mixmax sequence (18 leads waiting — infrastructure now fully fixed)
