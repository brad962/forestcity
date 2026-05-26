🔧 *Vera — Auto-Upgrade*
>Changed: workers/nina_report.py — added Closed Won/Closed Lost stage filter to overdue + due_soon contact lists
>Why: Latent bug — contacts marked Closed Won/Lost with old next_followup dates would appear as "overdue" in Nina's weekly report, creating false alerts; now filtered by stage
>File: workers/nina_report.py

---

🔧 *Vera — Auto-Upgrade*
>Changed: workers/lead_pipeline.py — added 'director of operations' to DANNY_TITLES
>Why: Same word-order problem fixed for 'director of facilities' in Run 95 — 'operations director' does NOT substring-match 'director of operations'; Apollo surfaces both variants; we were missing one
>File: workers/lead_pipeline.py

---

🔧 *Vera — Auto-Upgrade*
>Changed: integrations/mixmax.py — added 'director of operations' to PROPERTY_MANAGER_TITLES
>Why: Keeps Apollo title search and Mixmax routing in sync; same contact gets routed into correct sequence
>File: integrations/mixmax.py

---

📋 *Vera — New Deliverable*
>Written: outputs/vera/bryan_free_demo_offer_2026-05-26.md
>What: Run 97 fresh angle for Bryan (CLE Lawn Care Plus, 13+ days cold). All 7 prior deliverables asked Bryan for referrals. New approach: offer a FREE power wash of one surface at his business — no strings, no referral ask upfront. Deliver value first, partner second.
>Text to send NOW: "Hey Bryan — it's Brad. Instead of just talking about partnering, I want to show you what we do. I'll come clean one surface at your shop for free — parking entrance, equipment pad, whatever needs it. Zero catch. When's a good time this week?"
>If no response by Friday May 29 → move Bryan to Closed Lost. 8 attempts is a closed door.

---

📋 *Vera — New Deliverable*
>Written: outputs/carla/contractor_first_touch_blitz_2026-05-26.md
>What: 21 contractor referral contacts (landscapers, roofers, construction) in the pipeline have NEVER been contacted. Peak season. Every week idle = missed referral cycle.
>Card: Wave 1 (11 landscapers, highest value) + Wave 2 (10 construction/roofing) with copy-paste first-touch text, pipeline update instructions, revenue math.
>Time: 45 minutes. Revenue math: 3 referral relationships = $12,600/year.
>Do this before June 4 — or add as pre-work to Carla's activation card.

---

🚨 *Vera — Today's Action Stack (May 26)*
>DUE TODAY: Bryan 216-402-1924 (new: free demo offer), Bulletproof 216-307-4344, Damrons 440-494-0422
>DUE TOMORROW: 12 gas station contacts + 5 Tier 1 New Lead contractors
>Summit pull deadline: May 31 — Wed or Fri are the windows (5 days left)
>Off-hours leads tonight: use outputs/tommy/off_hours_lead_response_kit_2026-05-26.md

---

💡 *Vera — Upgrade Proposal*
>Idea: Daily "due today" Slack ping — every morning at 7am, vera_relay reads pipeline_data.json and posts a list of contacts whose next_followup = today with their phone numbers
>Why: Nina's report requires actively running a script; a push notification means no follow-up ever gets buried; zero friction = zero missed contacts
>Implementation: Add morning check function to vera_relay.py; sentinel file prevents duplicate pings; reads pipeline_data.json directly — no API needed; runs locally in existing cron
>Impact: Every follow-up actioned on the right day; no more "I forgot Bryan was due today" situations
>Reply YES to approve.

---

✅ *Vera — Scan Complete 2026-05-26 (Run 97)*
>3 auto-upgrades | 2 deliverables | 1 proposal | 1 new open issue (21 untouched contractors)
>Bryan: fresh angle — free demo wash, stop asking, start giving; send today, close if no response by Fri
>21 contractor contacts never reached out to during peak season → blitz card ready
>Code: nina_report overdue filter patched; 'director of operations' title added to Apollo+Mixmax
>Summit: 5 days left | Gas station 12 contacts due tomorrow | June 4 Medina enrollment: 9 days
