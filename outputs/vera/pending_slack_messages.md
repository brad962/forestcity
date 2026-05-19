🔧 *Vera — Auto-Upgrade*
>Changed: `integrations/mixmax.py` + `workers/lead_pipeline.py` — fixed sequence misrouting bug for Carla's realtor leads
>Why: `detect_lead_type()` ignored the `_lead_type` field set by the pipeline, so realtors with non-standard titles (e.g. "Sales Associate") were falling through to the contractor sequence. Now honors explicit intent first. Verified with 5-test suite.
>Files: `integrations/mixmax.py`, `workers/lead_pipeline.py`
---
🔧 *Vera — Auto-Upgrade*
>Changed: `server.py` — manual contact name now falls back to company name when no individual name is recorded
>Why: Bulletproof Lawncare and Damrons Landscaping were showing as blank names in the pipeline dashboard — confusing. Now they display their company name.
>File: `server.py`
---
🔧 *Vera — Auto-Upgrade*
>Changed: `workers/lead_pipeline.py` + `agents/carla.md` — added HVAC, pool service, pest control, junk removal as Carla referral partner search targets
>Why: These are 4 high-value adjacent service categories that visit NE Ohio homes weekly and have natural referral conversations with homeowners — but we weren't pulling them from Apollo at all.
>Files: `workers/lead_pipeline.py`, `agents/carla.md`
---
🚨 *Vera — URGENT: Day 9 — Text Bulletproof Lawncare + Damrons NOW*
>Both contractors said "very interested" when called 9 days ago (May 13). Neither has been texted.
>Reply rate drops ~60% after Day 10. Memorial Day is Sunday — this is the FINAL window.
>
>📱 Bulletproof Lawncare — 216-307-4344:
>"Hey, this is Bradley from Forest City Power Washing. We spoke last week — you mentioned partnering on referrals. Memorial Day weekend is our busiest push. $50 per closed job either way. Worth a 5-min call?"
>
>📱 Damrons Landscaping — 440-494-0422:
>"Hey, Bradley here from Forest City Power Washing. We talked last week — you were interested in teaming up on referrals. Memorial Day is this Sunday. $50 cash for every job you send our way. Can we nail down the details this week?"
>
>Full scripts + follow-ups: `outputs/vera/contractor_day9_texts_2026-05-19.md`
>Full sprint plan: `outputs/vera/memorial_day_execution_checklist_2026-05-19.md`
---
📋 *Vera — Memorial Day Sprint Execution Checklist*
>Everything is built. You just need to execute. Here's what to do in the next 5 days:
>
>TODAY (May 19, 45 min):
>1. Text Bulletproof Lawncare (216-307-4344) — script above
>2. Text Damrons Landscaping (440-494-0422) — script above
>3. Post Facebook post #1 from `outputs/jasmine/memorial_day_posts_2026-05-19.md`
>4. Text past customers — template: `outputs/tommy/past_customer_reengagement_2026-05-18.md`
>5. Text top 5 contractor leads — list in `outputs/vera/memorial_day_execution_checklist_2026-05-19.md`
>
>WEDNESDAY (May 21): Upload 1 GBP photo, post Facebook #2, text remaining leads
>FRIDAY (May 23): Post urgency Facebook + LinkedIn, send bridge email to 3 hot leads
>WEEKEND: Memorial Day post, reply to anyone who texted back
>
>Goal: 2 estimate requests by Sunday. All assets ready. 2 hours total across 5 days.
---
💡 *Vera — Proposal: Approve Sequence Rewrite*
>Idea: Rewrite all 3 Mixmax email sequences (Property Manager, Realtor, Contractor)
>Why: 45 contacts enrolled, 42% open rate, 0 replies in 7 days. Emails are being opened — the body copy isn't converting. Full rewrites ready with shorter copy, yes/no close, and break-up email as touch 4.
>Impact: Even moving from 0% to 5% reply rate = 2-3 hot conversations per week from existing enrolled leads — with no new work.
>Files ready: `outputs/vera/sequence_rewrites_proposal_2026-05-18.md`
>Reply YES to approve and I'll update the Mixmax sequences immediately.
---
💡 *Vera — Proposal: Send Bridge Email to 3 Hot Leads This Week*
>Idea: Bradley manually sends the bridge email to the 3 hottest open-but-no-reply leads from his Gmail
>Why: Faster than waiting for sequence rewrite approval. Personal 1:1 email from a real inbox gets ~30-40% reply rate vs. 0% from the sequence right now. Best done Memorial Day week when PMs are making summer vendor plans.
>Template: `outputs/tommy/hot_lead_bridge_email_2026-05-19.md` — edit name and hit send.
>Reply YES and I'll pull the top 3 contact names from the hot leads report.
---
✅ *Vera — Scan Complete 2026-05-19 (Run 12)*
>3 auto-upgrades shipped | 2 proposals | 14 open issues
>
>Upgrades: Mixmax sequence misrouting bug fixed | Dashboard blank names fixed | Carla now pulls HVAC/pool/pest leads
>New deliverables: Day-9 contractor texts | Memorial Day execution checklist
>
>🚨 Top action: Text Bulletproof Lawncare + Damrons TODAY. Day 9. Memorial Day is Sunday. This is the last window.
