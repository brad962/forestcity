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
