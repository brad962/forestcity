🔧 *Vera — Auto-Upgrade*
>Changed: `workers/nina_report.py` run_weekly() — added individual Hot Leads section with names, company, opens count, and LinkedIn connect links
>Why: Monday weekly report showed only aggregate stats — Bradley had no "who to call" list. Now the weekly report surfaces every 2+ open contact by name with a direct LinkedIn link.
>File: workers/nina_report.py

---

🔧 *Vera — Auto-Upgrade*
>Changed: `integrations/mixmax.py` + `workers/lead_pipeline.py` — added 'association manager' to PROPERTY_MANAGER_TITLES and DANNY_TITLES
>Why: Some CAI-certified community managers list just "Association Manager" as their title. This standalone variant was missing while longer variants ('community association manager') were already present. Both files kept in sync.
>Files: integrations/mixmax.py, workers/lead_pipeline.py

---

🔧 *Vera — Auto-Upgrade*
>Changed: `agents/donna.md` — added `june_week1_sprint_2026-05-20.md` reference to June Booking Blitz campaign section
>Why: File existed in outputs/donna/ since run 48 but wasn't referenced in Donna's agent file. Now it's in the campaign section where Donna will find it.
>File: agents/donna.md

---

📋 *Vera — Deliverable*
>Created: `outputs/donna/memorial_day_week_full_playbook_2026-05-22.md`
>What: Full day-by-day action plan for May 26–30 (Memorial Day week). Covers each day with specific actions, time estimates, and linked scripts. Fills the gap between the May 26 blitz action card and the June week 1 sprint.
>Highlights: Mon May 26 (blitz), Tue May 27 (FB ads launch + LinkedIn connects), Wed May 28 (phone calls + Danny status check), Thu May 29 (Medina prep + content), Fri May 30 (weekly review + June entry criteria)

---

🔴 *Vera — TOUCH 3 WINDOW CLOSING*
>Touch 3 fired May 22. If you haven't connected on LinkedIn with your top 2+ open contacts yet — do it NOW.
>The "just sent an email" context is what makes the connection land. Every hour past the send reduces conversion.
>Action: Open Mixmax → sort recipients by opens → connect on LinkedIn with top 5 today.
>Script: outputs/tommy/touch3_open_trigger_protocol_2026-05-21.md
>72h reply window closes May 25 — check results before May 26 blitz: outputs/donna/may25_round2_decision_gate_2026-05-22.md

---

🔴 *Vera — ADS STILL NOT LAUNCHED — PEAK SEASON*
>Today is May 22. Rick wrote the ads on May 19–20. Every day unspent is bookings going to competitors.
>Google Ads copy: outputs/rick/google_ads_june_2026-05-19.md
>Facebook Ads copy: outputs/rick/facebook_ads_peak_season_2026-05-20.md
>Google Guaranteed badge application: outputs/rick/google_guaranteed_setup_2026-05-22.md (1–3 days to approve — apply TODAY, live by May 27)
>Launch target: May 26. Everything is written. Just needs to go live.

---

⚡ *Vera — INSTANTLY.AI OVERLAP — 3-MINUTE FIX*
>This is the most likely cause of your 0% reply rate. Two Instantly.ai campaigns are running against the same contacts as your Mixmax sequences.
>Campaign a1c08c3d = Property Managers Cuyahoga County (duplicates Mixmax PM sequence)
>Campaign 626cd15d = Contractor Referral Partners (duplicates Mixmax contractor sequence)
>Fix: app.instantly.ai → Campaigns → Pause both. 3 minutes.
>Full guide: outputs/vera/instantly_pause_guide_2026-05-22.md
>Do this BEFORE Round 2 enrollment or the same problem will repeat.

---

✅ *Vera — Scan Complete 2026-05-22 (Run 49)*
>4 auto-upgrades shipped | 1 deliverable | 16 open issues (0 new, 0 closed)
>Best code fix: nina_report.py weekly now shows individual hot leads by name — Bradley gets a real "who to call" list every Monday
>Top 3 Bradley actions RIGHT NOW: (1) LinkedIn connects with 2+ open contacts today, (2) Pause Instantly.ai campaigns (3 min), (3) Launch ads by May 26
>May 26 playbook: outputs/donna/may26_blitz_action_card.md
>May 26–30 playbook: outputs/donna/memorial_day_week_full_playbook_2026-05-22.md

---

🔧 *Vera — Auto-Upgrade*
>Changed: `workers/vera_relay.py` — added `_check_danny_staleness()` function
>Why: vera_relay.py never proactively alerted on Danny cron being overdue. Now every time vera_relay.py runs locally (every 5 min), it checks activity.log for the last Danny pull. If >7 days old: posts a Slack alert directly. Fires once per day (sentinel prevents spam). Bradley will now get an automatic ping every day Danny's cron is down.
>File: workers/vera_relay.py

---

🔧 *Vera — Auto-Upgrade*
>Changed: `workers/nina_report.py` — added `_load_phone_map()` + Phone column to hot leads tables
>Why: Daily and weekly hot leads reports showed Name, Email, Opens, LinkedIn — but no phone number. When Bradley wants to call a hot lead, he had to manually dig through contacts_cache.json. Phone is now pulled from the cache and shown in both daily and weekly hot leads tables.
>Files: workers/nina_report.py

---

🔧 *Vera — Auto-Upgrade*
>Changed: `integrations/mixmax.py` + `workers/lead_pipeline.py` — added 'condominium manager' to routing and search
>Why: Substring bug — 'condo manager' does NOT match 'condominium manager' (different strings). Contacts with that exact title were falling through to default routing. Also added 'condominium management', 'condo association', 'condominium association' to DANNY_ORG_KEYWORDS — entire condo HOA segment was missing from org-level keyword filter.
>Files: integrations/mixmax.py, workers/lead_pipeline.py

---

🔧 *Vera — Auto-Upgrade*
>Changed: `workers/lead_pipeline.py` CARLA_SEARCHES — added 'irrigation', 'sprinkler system', 'lawn irrigation' to contractors keywords
>Why: Irrigation companies service properties every spring + fall — they're inside the yard when the house is dirty and have a built-in reason to recommend power washing. High-value referral segment that was entirely missing from Carla's Apollo search.
>File: workers/lead_pipeline.py

---

📋 *Vera — Deliverable*
>Created: `outputs/tommy/email_subject_line_ab_test_2026-05-22.md`
>What: 5 A/B subject line pairs for Round 2 PM sequence — each pair tests a different psychological trigger (specificity, social proof, fear, ultra-short, direct question). Mixmax A/B setup instructions included (step-by-step). Success metrics defined: ≥40% open rate, ≥5% reply rate. Timeline May 25 decision → June 4 enrollment → June 11 check.
>Use: If Touch 3 = 0 replies, deploy Pair A ("Before the tenants complain...") on May 26 for Round 2.

---

📋 *Vera — Deliverable*
>Created: `scripts/danny_cron_check.sh`
>What: Mac terminal diagnostic script. Checks: (1) active crontab entries, (2) launchd plist status, (3) days since last Danny pull with overdue flag, (4) last 10 lines of cron.log. Run: `bash scripts/danny_cron_check.sh`. Gives Bradley a one-command health check on the entire pipeline scheduler.

---

✅ *Vera — Scan Complete 2026-05-22 (Run 50)*
>6 auto-upgrades shipped | 2 deliverables | 16 open issues (4 new RESOLVED, 0 new OPEN)
>Best fix this run: vera_relay.py now auto-alerts Slack if Danny hasn't run in 7+ days — pipeline staleness detection is now fully automated
>Phone numbers added to hot leads tables — Bradley now sees who to call AND their number in the same report
>Subject line A/B test plan ready for Round 2 (use if Touch 3 = 0 replies)
>Today's priority: Check Mixmax open stats → LinkedIn connects with 2+ open contacts → Pause Instantly.ai (3 min)
