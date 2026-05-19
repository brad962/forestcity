🔧 *Vera — Auto-Upgrade*
>Changed: `run_carla()` now uses org phone fallback `p.get('organization', {}).get('id', '')` when reveal doesn't return organization_id
>Why: Carla was silently missing org phone numbers whenever Apollo's reveal endpoint didn't echo back the organization_id — Danny had this fallback since run 8, Carla didn't. Now consistent.
>File: `workers/lead_pipeline.py`
---
🔧 *Vera — Auto-Upgrade*
>Changed: `post_to_slack()` in workiz_report.py now shows "⚠️ Workiz API unavailable" card instead of misleading $0 total / $0 outstanding when API is blocked
>Why: The error summary was overridden by computed $0 metrics — report cards looked like $0 jobs existed rather than showing an API block. Status now shows IN PROGRESS.
>File: `workers/workiz_report.py`
---
📋 *Vera — New Deliverables (Run 14)*

**Tommy: Inbound Lead First-Response Protocol** — `outputs/tommy/inbound_response_protocol_2026-05-19.md`
Exact text/DM scripts for 4 inbound types: Facebook DM, website form, Google Business, referral. 5-minute rule, estimate call script, cardinal rules. Screenshot this for your phone.

**Tommy: Soft Wash vs. Pressure Wash Explainer** — `outputs/tommy/soft_wash_explainer_2026-05-19.md`
Two versions: 30-second in-person pitch + full website FAQ copy. Covers roof warranty issue, why soft wash kills not just moves algae. Includes ad one-liner: "Pressure washing removes it. Soft washing kills it."

**Donna: Neighborhood Canvass Strategy** — `outputs/donna/neighborhood_canvass_strategy_2026-05-19.md`
Turn every completed job into 2-3 more neighbors. Door knock script, leave-behind card template, "we're in your neighborhood" Facebook post. Zero cost. This Memorial Day week is the perfect window.
---
🚨 *Vera — URGENT: Contractors (Day 10 — ABSOLUTE FINAL WINDOW)*
>**Bulletproof Lawncare | 216-307-4344** — "Very interested — send text" (noted 2026-05-13)
>**Damrons Landscaping | 440-494-0422** — "Very interested — send text" (noted 2026-05-13)
>
>Today is Day 10. After 10 days leads go cold. Memorial Day weekend is 6 days out — these contractors are entering their own busy season and will stop answering.
>
>Scripts ready: `outputs/vera/contractor_day9_texts_2026-05-19.md`
>Send one text today. That's all it takes to keep this alive.
---
📌 *Vera — 10 Pending Actions (Memorial Day window closes Sunday)*

1. 📱 Text Bulletproof Lawncare + Damrons Landscaping TODAY
2. 📧 Send bridge email to 3 hot leads (`outputs/tommy/hot_lead_bridge_email_2026-05-19.md`)
3. 🔗 Connect with 3 hot leads on LinkedIn (`outputs/danny/linkedin_hot_lead_dm_protocol_2026-05-18.md`)
4. 📷 Upload 1 photo to Google Business Profile
5. 📣 Post 1 Facebook post (`outputs/jasmine/facebook_posts_week_2026-05-19.md`)
6. 🏘️ Try the canvass strategy on next job (`outputs/donna/neighborhood_canvass_strategy_2026-05-19.md`)
7. Mixmax → API Settings → add IP allowlist (fixes cloud reports)
8. Add `HUBSPOT_TOKEN` to .env
9. Run cron jobs from CLAUDE.md
10. Confirm Mixmax or Instantly.ai — not both (duplicate send risk)
---
✅ *Vera — Scan Complete 2026-05-19 (Run 14)*
>2 auto-upgrades shipped | 3 new deliverables | 34 RESOLVED | 14 OPEN
>Ghost fixes verified: all 34 prior fixes confirmed present
>Peak season: Memorial Day Sunday May 25 — highest-urgency week of the year
