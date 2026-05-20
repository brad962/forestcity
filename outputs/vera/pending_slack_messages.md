🔧 *Vera — Auto-Upgrade*
>Changed: `workers/workiz_report.py` — null-safety fix in `_is_power_washing_job()`
>Why: If Workiz returns `"JobType": null` in JSON, `None.strip()` crashes the reporter. Added guard: `if not job_type: return False`.
>File: `workers/workiz_report.py`
---
🔧 *Vera — Auto-Upgrade*
>Changed: `workers/jasmine_flyer.py` — wrapped `datetime.strptime` in try/except
>Why: Malformed date string in `photo_pairs.json` would crash `write_facebook_post()` and fail the whole flyer run. Now falls back to today's date on parse error.
>File: `workers/jasmine_flyer.py`
---
🔧 *Vera — Auto-Upgrade*
>Changed: `agents/rick.md` — added Ready Assets section pointing to June Google Ads file
>Why: Rick's Google Ads copy has been written and ready since May 19 (`outputs/rick/google_ads_june_2026-05-19.md`). The agent file didn't reference it, so future Claude sessions wouldn't know to use it.
>File: `agents/rick.md`
---
🔧 *Vera — Auto-Upgrade*
>Changed: `agents/marcus.md` — added peak season priority note + cloud limitation note
>Why: Marcus needs to know it's peak season, what to prioritize (competitor summer pricing, fresh VOC), and that web search only works in local sessions. Prevents wasted cloud runs.
>File: `agents/marcus.md`
---
📋 *Vera — New Deliverable*
>File: `outputs/vera/peak_season_daily_sprint_may20_26.md`
>What: Day-by-day action calendar for Bradley, May 20–26. Every task mapped to an existing file. Estimated times. May 20 (today) = LinkedIn connects + Tier 1 contractor texts. May 26 = 70-minute outreach blitz.
>Action: Open this now. The May 20 tasks take 60 minutes and should happen today before Touch 3 fires tomorrow.
---
📋 *Vera — New Deliverable*
>File: `outputs/tommy/google_business_profile_post_templates_2026-05-20.md`
>What: 4 GBP post templates Bradley can post weekly during peak season. Job spotlight, algae education, social proof, property manager pitch. Each one takes 3 minutes to post.
>Why: GBP posts directly improve local search ranking for "power washing near me." Zero cost. Currently unused.
>Action: Copy Template 1, add a recent job photo, post to Google Business Profile today.
---
📋 *Vera — New Deliverable*
>File: `outputs/danny/gas_station_manual_email_blast_2026-05-20.md`
>What: 3 email templates (district managers, facilities managers, station owners) + prioritized send order for the 18 gas station contacts sitting idle since May 19.
>Why: Mixmax sequence still PENDING. These contacts are getting cold. Memorial Day is the perfect trigger — stations think about canopy washing before their busiest weekend.
>Action: Send Tier 1 emails today (30 min). Or create the Mixmax sequence and paste the ID — system auto-enrolls all 18.
---
📋 *Vera — New Deliverable*
>File: `outputs/rick/facebook_ads_peak_season_2026-05-20.md`
>What: Full Facebook ad campaign — 3-campaign structure, 7 ad variations. Awareness, lead gen, retargeting. Setup checklist included.
>Why: Google Ads copy is ready but Facebook ads haven't been set up. Facebook is the #1 residential home services channel in NE Ohio.
>Action: Set up in Facebook Ads Manager. Start at $30/day. Memorial Day week is the best time to launch.
---
🚨 *Vera — CRITICAL: Touch 3 fires TOMORROW (May 21)*
>45 contacts get their final email tomorrow. Here's what to do TODAY (60 min total):
>
>*LinkedIn connects — 30 min:*
>→ `outputs/tommy/hot_lead_linkedin_dm_playbook_2026-05-19.md`
>Send connection requests to 13 hot leads (2+ opens). Include the short note from the playbook.
>
>*Tier 1 contractor texts — 15 min:*
>• Anthony, Land Pro Management: 440-320-2779
>• Dontez, GTP Landscaping: 440-396-0814
>• Chris, Twin Improvements | Venus, Reliable Roofing | Logan, Pagels Construction
>
>*Write Gmail drafts for May 26 — 15 min:*
>→ `outputs/tommy/hot_lead_bridge_email_2026-05-19.md`
>5 personalized drafts to top hot leads. Save as drafts. Send Monday May 26.
>
>Full day-by-day plan: `outputs/vera/peak_season_daily_sprint_may20_26.md`
---
💡 *Vera — Upgrade Proposal*
>Idea: Create Fleet Washing Mixmax sequence — copy ready, just needs 10 minutes.
>Why: `outputs/danny/sequence_fleet_washing_2026-05-18.md` has the full 3-touch sequence copy. Infrastructure wired (mixmax.py line 47-51). The moment the ID goes live, the pipeline auto-enrolls fleet leads.
>Impact: Fleet washing = recurring commercial revenue. One landscaping company account = $500+/year.
>Action: Mixmax → New Sequence → paste copy → get ID → paste into `integrations/mixmax.py` line 48. Reply YES + paste the ID.
---
💡 *Vera — Upgrade Proposal*
>Idea: Approve PM sequence Touch 1 & 2 rewrite — 0% reply rate demands action.
>Why: 42% open rate, 0 replies. Opens prove delivery works. Body copy doesn't convert. Rewrite: 62-word body, single CTA, "Re:" subject on Touch 2, NE Ohio lake humidity angle.
>Impact: Applies to NEW contacts enrolled after approval. Current 45 get Touch 3 as-is.
>File: `outputs/danny/pm_sequence_touch1_rewrite_2026-05-19.md`
>Action: Reply YES. I update sequence notes. You update email body in Mixmax UI.
---
💡 *Vera — Upgrade Proposal*
>Idea: Past customer text blast — highest ROI activity this season.
>Why: Past customers convert at 3-5x cold leads. It's Memorial Day week. One hour of texting = multiple bookings.
>Templates: `outputs/tommy/past_customer_reengagement_2026-05-18.md`
>What's needed: Run `python3 workers/workiz_report.py daily` locally to get completed jobs list.
>Action: Run Workiz report locally → text past customers → book June slots.
---
✅ *Vera — Scan Complete 2026-05-20 (Run 23)*
>4 auto-upgrades shipped | 4 deliverables produced | 3 proposals | 14 open issues (2 new, 4 escalated)
>
>CRITICAL TODAY (before Touch 3 fires tomorrow):
>① LinkedIn connects to 13 hot leads — 30 min
>② Text 5 Tier 1 contractors — 15 min (numbers above)
>③ Write 5 Gmail drafts for May 26 — 15 min
>④ Post GBP photo — 5 min
>
>MONEY DAY = May 26. Full brief: `outputs/donna/may26_outreach_blitz_brief_2026-05-20.md`
