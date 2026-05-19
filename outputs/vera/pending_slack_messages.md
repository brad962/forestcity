🔧 *Vera — Auto-Upgrade*
>Changed: `build_variables()` in `integrations/mixmax.py` — empty firstName now falls back to 'there'
>Why: If Apollo returns a contact with a blank first_name, every email sent to them opened with "Hi ," — a spam signal that could be contributing to the 0% reply rate. Now renders "Hi there," instead.
>File: `integrations/mixmax.py`

---

🔧 *Vera — Auto-Upgrade*
>Changed: `get_mixmax_enrolled_emails()` in `workers/lead_pipeline.py` — now reads sequence IDs dynamically from `integrations/mixmax.py` instead of a hardcoded 3-sequence list
>Why: When gas station and fleet sequences go live, the enrollment verification step was going to silently miss them — contacts could slip through and never be caught. Now auto-includes all live sequences.
>File: `workers/lead_pipeline.py`

---

🔧 *Vera — Auto-Upgrade*
>Changed: `run_weekly()` in `workers/nina_report.py` — added "Manual Pipeline Health" section
>Why: Nina's weekly report only showed Mixmax data. Bradley had no visibility into the 39 untouched manual contacts without opening the dashboard. Now the weekly report shows untouched count, contacted count, replied count — and ⚠️ warns if contacts have never been reached.
>File: `workers/nina_report.py`

---

🔧 *Vera — Auto-Upgrade*
>Changed: `agents/danny.md` — updated mission statement from "Fill the HubSpot pipeline" to "Fill the prospect pipeline (HubSpot pending)"
>Why: HubSpot has never been connected. The old mission statement was factually wrong and could confuse future sessions into thinking HubSpot is active.
>File: `agents/danny.md`

---

🔧 *Vera — Auto-Upgrade*
>Changed: `CLAUDE.md` — marked `integrations/mixmax.py` as authoritative source for sequence IDs; added PENDING entries for gas station and fleet sequences
>Why: Sequence IDs existed in two places (CLAUDE.md table + mixmax.py). If one was updated without the other, scripts would use stale IDs. Now CLAUDE.md explicitly defers to mixmax.py.
>File: `CLAUDE.md`

---

🔧 *Vera — Auto-Upgrade*
>Changed: `server.py` — added ⚠️ warning comment to INSTANTLY_CAMPAIGNS block
>Why: server.py has Instantly.ai campaign IDs for Property Managers and Referral Partners — the same segments Mixmax is actively sequencing. If INSTANTLY_API_KEY is ever added to .env, contacts would receive simultaneous duplicate emails from two platforms. Warning is now visible in code.
>File: `server.py`

---

📋 *Vera — New Deliverable*
>File: `outputs/tommy/pipeline_contractor_outreach_2026-05-19.md`
>What: Personal email template for the 21 warm contractors in pipeline_data.json — the ones with phone numbers who've never been contacted. Different from Tommy's bridge email (that's for Mixmax hot leads) — this is for the pipeline contacts who are completely cold.
>Trade-specific personalization included for landscapers, roofers, siding contractors, gutter companies, and HVAC.
>Priority order matches: `outputs/vera/priority_outreach_list_2026-05-19.md`

---

🚨 *Vera — ESCALATION: Touch 3 fires MAY 22 — 3 days*
>42% open rate. 0% reply rate. Touch 3 is the last email in the sequence.
>
>Before it sends, spend 10 minutes:
>1. Mixmax → PM Sequence → Settings → check *Reply-To* address. If it's not your email, replies are in a dead inbox.
>2. Mixmax → Recipients → send test email to yourself. Confirm variables render (not literal {{firstName}}).
>3. Count unsubscribed contacts — if high, your email is being flagged as bulk.
>
>Full diagnostic: `outputs/vera/reply_rate_diagnostic_2026-05-19.md`
>Tommy's personal bridge email ready to send from Gmail NOW: `outputs/tommy/hot_lead_bridge_email_2026-05-19.md`

---

🚨 *Vera — MEMORIAL DAY 6 DAYS OUT — Execute NOW*
>All assets are done. This is a pure execution problem.
>
>TODAY (May 19):
>• Text Tier 1 contractors — templates in `outputs/vera/sms_templates_contractors_2026-05-18.md`
>• Land Pro Management (Anthony, 440-320-2779), GTP Landscaping (Dontez, 440-396-0814)
>• Post first Memorial Day Facebook post — `outputs/jasmine/memorial_day_posts_2026-05-19.md`
>
>This Week:
>• Send bridge email to top 3 Mixmax hot leads from Gmail (Tommy's template ready)
>• Upload 1 photo to Google Business Profile (15 min, zero cost)
>• Send review request to any recently completed jobs
>
>Warm contractor email template (for pipeline contacts with email only): `outputs/tommy/pipeline_contractor_outreach_2026-05-19.md`

---

💡 *Vera — Proposal: HOA Management Company Portfolio Sequence*
>Idea: Danny targets individual property managers at HOA companies. No one is pitching the OWNERS/PRESIDENTS of those same HOA management companies on a portfolio-level deal — "we handle exterior cleaning for all 15 communities you manage, one point of contact, we invoice you directly."
>Why: One HOA management company president = 5–20 jobs per year, not one. This is recurring annual revenue, not a one-off.
>Impact: Apollo pull of 'owner', 'president' at 'hoa management', 'community management', 'association management' firms in NE Ohio. New sequence from Tommy — different pitch angle from Danny's individual PM sequence.
>Action: Reply YES and Danny pulls leads + Tommy writes the sequence. Can be live within one run.

---

💡 *Vera — Proposal: Approve Sequence Rewrite Before Touch 3*
>Touch 3 sends May 22. 0% reply rate. Current body copy isn't converting.
>Idea: Update the Touch 3 copy in Mixmax NOW before it goes out. Replace generic close with specific offer: "Free exterior walk — I'll come to one of your properties, assess the condition, no commitment."
>New copy from Tommy ready: `outputs/vera/sequence_rewrites_proposal_2026-05-18.md`
>Impact: Even 1 reply from Touch 3 = potential $500–$1,500 job. Costs 15 minutes to update in Mixmax.
>Reply YES and it's done today.

---

💡 *Vera — Proposal: Gas Station Mixmax Sequence*
>18 contacts staged and waiting. All infrastructure fixed and verified.
>Action: Mixmax UI → New Sequence → "Forest City Power Washing — Gas Station & C-Store Outreach" → copy from `outputs/danny/sequence_gas_stations_2026-05-19.md` → paste ID into `integrations/mixmax.py` line 54 → run `python3 workers/lead_pipeline.py` locally. Auto-enrolls all 18.
>Reply YES to approve.

---

✅ *Vera — Scan Complete 2026-05-19 (Run 19)*
>6 auto-upgrades shipped | 3 proposals | 47 RESOLVED | 12 OPEN
>
>🔑 Key fixes this run:
>• "Hi ," bug fixed — empty firstName now falls back to "Hi there," (potential reply rate factor)
>• Enrollment verification now dynamic — gas station/fleet auto-verified once sequences go live
>• Nina's weekly report now shows manual pipeline health — Bradley has visibility without HubSpot
>• danny.md mission fixed — no longer says HubSpot is active
>• server.py Instantly overlap risk flagged in code
>
>📋 New deliverable: Personal contractor email template for warm pipeline contacts
>
>⚠️ Top 3 actions for Bradley RIGHT NOW:
>1. Check Mixmax Reply-To setting TODAY — Touch 3 fires May 22 (3 days)
>2. Text Tier 1 contractors today — Memorial Day is 6 days out
>3. Create gas station Mixmax sequence — 18 contacts ready, all infrastructure fixed
