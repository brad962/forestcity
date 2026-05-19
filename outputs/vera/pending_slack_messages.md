🔧 *Vera — Auto-Upgrade*
>Changed: server.py `sync_contacts()` — rewrote to MERGE Instantly leads into existing cache instead of overwriting. Also fixed `get_contacts()` to handle malformed JSON without crashing all dashboard endpoints. Fixed `/api/pipeline` and `/api/calls` GET crash on bad pipeline_data.json.
>Why: sync_contacts() was a data loss time bomb — the moment INSTANTLY_API_KEY landed in .env, one dashboard click would have wiped all Apollo contacts. Also hardened 3 crash points that would take down the entire dashboard.
>File: `server.py`
---
🔧 *Vera — Auto-Upgrade*
>Changed: `integrations/mixmax.py` — `get_sequence_recipients()` now normalizes dict vs list response (was returning raw JSON). Added PENDING guard.
>Why: Latent bug — would crash any caller expecting a list when Mixmax returns a dict response.
>File: `integrations/mixmax.py`
---
🔧 *Vera — Auto-Upgrade*
>Changed: `agents/donna.md` — updated Memorial Day Sprint to ACTIVE NOW (May 19–26). Added June Booking Blitz with file references.
>Why: The sprint is live this week. Donna's file reflected it as future planning — now updated to reflect active execution mode.
>File: `agents/donna.md`
---
🔧 *Vera — Auto-Upgrade*
>Changed: `agents/tommy.md` — added 4 deliverable format types (pipeline outreach, LinkedIn DM playbook, past customer reengagement, review request).
>Why: Tommy's been producing these but they weren't documented in his agent file. Missing formats = other agents don't know these deliverables exist.
>File: `agents/tommy.md`
---
📋 *Vera — New Deliverable*
>File: `outputs/tommy/hot_lead_linkedin_dm_playbook_2026-05-19.md`
>What: 3-step LinkedIn DM playbook for the 13 hot leads (2+ opens, 0 replies). Copy-paste templates for PMs, realtors, and contractors. Timed to warm contacts BEFORE Touch 3 fires May 22.
>How: Open each hot lead's LinkedIn → send connection request note → DM within 24h if accepted. 5 min/contact. Do today.
---
📋 *Vera — New Deliverable*
>File: `outputs/jasmine/facebook_posts_june_week1_2026-06-02.md`
>What: 5 Facebook posts for June 2–6. Post-Memorial Day momentum angle, commercial PM push, Strongsville before/after, referral share, deck season. Ready to schedule.
---
📋 *Vera — New Deliverable*
>File: `outputs/rick/google_ads_june_2026-05-19.md`
>What: Complete Google Ads for June. 2 campaigns, all ad copy written, all extensions. $15/day = 20–30 quote requests/month in NE Ohio. Forest City is currently invisible on "power washing near me."
>Action: Create Google Ads account to launch.
---
🚨 *Vera — URGENT: Touch 3 fires May 22 — Check Reply-To NOW*
>42% open rate. 0% reply rate. Most likely cause: Mixmax Reply-To pointing to wrong inbox.
>10-minute fix: Mixmax → PM Sequence → Settings → confirm Reply-To = your real inbox.
>Also: Send LinkedIn connects to 5 hot leads TODAY → `outputs/tommy/hot_lead_linkedin_dm_playbook_2026-05-19.md`
---
🚨 *Vera — URGENT: 40 Contacts Untouched — Memorial Day in 5 Days*
>Count unchanged from last run. Text these TODAY:
>• Land Pro Management — Anthony — 440-320-2779
>• GTP Landscaping — Dontez — 440-396-0814
>• + Twin Improvements, Reliable Roofing, Pagels Construction
>Templates: `outputs/vera/sms_templates_contractors_2026-05-18.md`
---
💡 *Vera — Upgrade Proposal*
>Idea: Launch Google Search Ads — $15/day for June
>Why: Forest City is invisible on "power washing near me" during peak season. All ad copy ready: `outputs/rick/google_ads_june_2026-05-19.md`
>Impact: Industry benchmark = 20–30 quote requests/month → at minimum 3 booked jobs → 3x return on $300/month.
>Action needed: Create Google Ads account at ads.google.com. Reply YES to approve.
---
💡 *Vera — Upgrade Proposal*
>Idea: Create Mixmax Gas Station sequence now
>Why: 18 contacts tagged and ready. Auto-enrolls the moment the ID is live. No extra work after that.
>Impact: Each gas station district manager controls 5–15 locations = potential recurring multi-site revenue.
>Action: Mixmax → New Sequence → use copy from `outputs/danny/sequence_gas_stations_2026-05-19.md` → paste ID into `integrations/mixmax.py` line 54. Reply YES + paste ID.
---
✅ *Vera — Scan Complete 2026-05-19 (Run 20)*
>4 auto-upgrades shipped | 3 deliverables produced | 13 open issues tracked
>CRITICAL TODAY: (1) Check Mixmax Reply-To (10 min) (2) Text 5 Tier 1 contractors (30 min) (3) LinkedIn connects to hot leads (15 min). ~1 hour total. Peak season — this hour matters.
