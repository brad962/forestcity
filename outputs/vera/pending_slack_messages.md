🔴 *Vera — Blocked Issue: GitHub Action (Runs 34, 91, 102)*
>Issue: The Slack relay GitHub Action can't be deployed because the PAT doesn't have `workflow` scope. Same error all 3 attempts.
>Fix (3 minutes): Go to github.com/settings/tokens → Generate new token → check both `repo` AND `workflow` → replace GITHUB_PAT in your .env file → Vera will deploy the Action on her next run
>Why it matters: Right now Slack delivery depends on vera_relay.py running on your local Mac cron every 5 min. GitHub Action would fire the instant Vera pushes, even when your Mac is closed.

---

🔧 *Vera — Auto-Upgrade*
>Changed: `workers/lead_pipeline.py` — added 5 hotel/lodging org keywords to DANNY_ORG_KEYWORDS
>Why: Some NE Ohio hotel operators tag themselves as "lodging management" or "hotel group" rather than "hotel management" in Apollo; these companies were invisible to Danny's search; keywords added: lodging management, lodging facilities, hotel group, motel chain, resort management
>File: workers/lead_pipeline.py

---

🔧 *Vera — Auto-Upgrade*
>Changed: `agents/jasmine.md` — added GBP (Google Business Profile) post formats to Jasmine's output catalog
>Why: GBP post content was floating in outputs/vera/ with no formal ownership; Jasmine is the Social Media Manager — GBP posts ARE social media; now documented as her domain; existing GBP files in outputs/vera/ should be migrated to outputs/jasmine/ on next Jasmine task
>File: agents/jasmine.md

---

📋 *Vera — New Deliverable*
>Written: `outputs/jasmine/job_site_content_capture_guide_2026-05-26.md`
>What: One-page protocol for capturing before/after photos + video at every job. Read once, use every time.
>Shots: Establishing Before (wide) → Detail Before (close-up) → after job: Establishing After → Detail After. Plus optional 30-second video for 3-5× organic reach.
>Caption template included. photo_pairs.json integration with Jasmine's flyer builder.
>Why now: Ads are live. First jobs are coming. Content captured today = 2 weeks of organic social fuel. Video gets 3-5× more reach than photos at zero extra ad cost.
>Action: Read this before your next job. Takes 5 extra minutes on-site.

---

📋 *Vera — New Deliverable*
>Written: `outputs/rick/google_lsa_status_check_2026-05-26.md`
>What: 3-minute guide to check whether your Google Local Services Ads (Google Guaranteed) application has been submitted and what to do next.
>Context: Rick wrote the full setup guide May 22 (4 days ago). If you applied then, you could be approved by June 2–9 — right at the start of the June booking blitz. If you haven't applied yet, do it in the next 30 min.
>Why it matters: LSAs appear ABOVE your regular Google Ads AND every organic result. Google Guaranteed badge. Pay per lead ($15-35) not per click. Most NE Ohio power washers haven't set these up — first-mover advantage.
>Action: Check status at ads.google.com/local-services-ads OR apply NOW using outputs/rick/google_guaranteed_setup_2026-05-22.md

---

🚨 *Vera — TODAY (May 26) Priority Stack*
>1. DUE TODAY: Bryan 216-402-1924 (free demo offer text from outputs/vera/bryan_free_demo_offer_2026-05-26.md) | Bulletproof 216-307-4344 | Damrons 440-494-0422
>2. DUE TOMORROW (May 27): 12 gas station contacts + Anthony/Land Pro 440-320-2779 + Dontez/GTP 440-396-0814
>3. Summit pull: 5 days left (May 31). Wed May 28 or Fri May 29 are your windows. Double-click scripts/run_summit_pull.command
>4. Instantly.ai: CRITICAL. Pause before June 4 enrollment. Guide: outputs/vera/instantly_pause_guide_2026-05-22.md
>5. Google LSA: Check if you've applied — read outputs/rick/google_lsa_status_check_2026-05-26.md (3 min)

---

✅ *Vera — Scan Complete 2026-05-26 (Run 102)*
>3 auto-upgrades shipped | 2 deliverables | 0 RESOLVED | 30 open issues (2 new)
>Biggest action needed: Create a new GitHub PAT with `workflow` scope (3 min) — then Vera can finally deploy the Slack relay Action that's been blocked since Run 34
>Biggest revenue opportunity: Google LSA status check — read outputs/rick/google_lsa_status_check_2026-05-26.md; if not applied, do it in the next 30 min; approval by June 4 = highest-converting lead source for the June booking blitz
