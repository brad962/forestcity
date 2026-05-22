🔧 *Vera — Auto-Upgrade*
>Changed: check_replies.py — sequences now import dynamically from integrations/mixmax.py
>Why: When gas_station and fleet_washing sequences go live in Mixmax, they'll be scanned automatically without any code change needed.
>File: workers/check_replies.py
---
🔧 *Vera — Auto-Upgrade*
>Changed: integrations/mixmax.py PROPERTY_MANAGER_TITLES — added 'property management director'
>Why: This title was in Danny's Apollo search list but missing from routing detection — any manually imported "Property Management Director" contact would fall through to the default instead of hitting the PM sequence.
>File: integrations/mixmax.py
---
🔧 *Vera — Auto-Upgrade*
>Changed: workers/nina_report.py — added Company column to hot leads tables (daily + weekly)
>Why: When Bradley sees a hot lead, the first thing he needs is the company name — not just a name and email. Added _load_company_map() and injected it into both report tables.
>File: workers/nina_report.py
---
🔧 *Vera — Auto-Upgrade*
>Changed: workers/lead_pipeline.py Carla contractors search — added 'window cleaning' alongside 'window washing'
>Why: Both terms are widely used in Apollo profiles; they return different companies from the same industry.
>File: workers/lead_pipeline.py
---
🔧 *Vera — Auto-Upgrade*
>Changed: agents/danny.md — updated Summit County urgency note date from "May 21/22" to "May 22+"
>Why: Stale dates in agent files erode credibility of the urgency signal.
>File: agents/danny.md
---
📋 *Vera — New Deliverable: Free Lead Harvest Protocol*
>File: outputs/donna/free_lead_harvest_protocol_2026-05-22.md
>What: Zero-spend residential lead harvest for peak season. 4 channels: (1) 5 NE Ohio Facebook homeowner groups — copy-paste post + reply scripts ready, (2) Nextdoor business page — 5-step setup + post copy, (3) GBP before/after photo upload cadence, (4) past customer referral text campaign.
>Why now: Ads aren't live. Touch 3 is in the reply window. This protocol can generate 5–15 inbound inquiries before May 27 with ~100 minutes of effort spread over 5 days. POST IN FACEBOOK GROUPS TODAY — 20 minutes.
---
🚨 *Vera — Tonight Action Required (2 items)*
>1. *Pause Instantly.ai* — both campaigns overlap your Mixmax contacts → duplicate emails → spam filters → root cause of 0 replies. Guide: outputs/vera/instantly_pause_guide_2026-05-22.md. Takes 3 minutes.
>2. *Text Tier 1 contractors* — Anthony/Land Pro (440-320-2779), Dontez/GTP (440-396-0814), Chris/Twin (216-773-0757), Venus/Reliable (216-810-2497), Logan/Pagels (216-956-5263). Scripts: outputs/tommy/contractor_referral_text_script_2026-05-20.md
---
💡 *Vera — Upgrade Proposal: LinkedIn Company Page*
>Idea: Set up a LinkedIn Company Page for Forest City Power Washing
>Why: When Bradley cold-connects on LinkedIn, prospects click through to verify the business. A company page with logo, about, and before/after photos converts "who is this?" into "legit local business." 20 minutes to set up.
>Impact: Higher connect acceptance rate on all PM outreach. Social proof layer behind every sequence.
>Reply YES to approve and I'll write the setup guide + all profile copy.
---
✅ *Vera — Scan Complete 2026-05-22 (Run 53)*
>5 auto-upgrades shipped | 1 deliverable | 1 proposal | 17 open issues (0 new)
>
>Bradley's top 4 actions TODAY:
>1. 🔴 Pause Instantly.ai — 3 min → outputs/vera/instantly_pause_guide_2026-05-22.md
>2. 📱 Post in NE Ohio Facebook groups — 20 min → outputs/donna/free_lead_harvest_protocol_2026-05-22.md
>3. 📞 Text Tier 1 contractors tonight → outputs/tommy/contractor_referral_text_script_2026-05-20.md
>4. 🖥️ Run Danny lead pull: `cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both`
