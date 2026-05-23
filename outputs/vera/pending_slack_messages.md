🔧 *Vera — Auto-Upgrade*
>Changed: Created `scripts/run_summit_pull.command` — double-click file in Finder to run Summit County lead pull without opening Terminal or typing anything
>Why: 12 days since last Danny pull. Summit County deadline May 31. Lowest-friction path = zero-typing double-click. File is in `scripts/` folder of the repo.
>File: scripts/run_summit_pull.command

---

🔧 *Vera — Auto-Upgrade*
>Changed: donna.md output format catalog — added `round2_enrollment_readiness_checklist` and `june_week3_4_commercial_sprint` format entries
>Why: Both deliverables written this run; catalog kept current so future agents don't re-create work
>File: agents/donna.md

---

🔧 *Vera — Auto-Upgrade*
>Changed: tommy.md output format catalog — added `annual_plan_upsell_sequence` format entry
>Why: No post-job upsell script exists yet; entry added so Tommy knows this is his deliverable to write
>File: agents/tommy.md

---

🔧 *Vera — Auto-Upgrade*
>Changed: rick.md output format catalog — added `google_guaranteed_lead_response_sop` format entry
>Why: Google Guaranteed measures response time and penalizes slow responders with fewer leads; SOP must exist BEFORE ads go live
>File: agents/rick.md

---

📋 *Vera — Deliverable: Round 2 Enrollment Readiness Checklist*
>File: outputs/donna/round2_enrollment_readiness_checklist_2026-05-23.md
>What: GO / NO-GO checklist for June 3 — the day before Round 2 enrollment (June 4). 5 blocks: Instantly.ai paused, new email copy in Mixmax, fresh Apollo leads pulled, gas station sequence live, bridge emails sent to hot leads. If any block is NO, enrollment is blocked. Prevents re-enrolling into the same broken setup that produced 0% reply rate in Round 1.
>Use it: Open on June 3, run through each checkbox, then and only then run `python3 workers/lead_pipeline.py both`

---

📋 *Vera — Deliverable: June Week 3–4 Commercial Sprint*
>File: outputs/donna/june_week3_4_commercial_sprint_2026-05-23.md
>What: Day-by-day commercial action plan for June 16–30. Includes: Round 2 reply conversion, Cuyahoga County pull, annual plan upsell waves 1+2, ad performance optimization, realtor summer listing push, June month-end review. Revenue targets $5,600–$13,800. Completes the June sprint trilogy (weeks 1, 2, now 3-4).

---

🔴 *Vera — CRITICAL: Pause Instantly.ai RIGHT NOW (3 min)*
>The reply window closes TOMORROW (Sunday May 25). Whether there are replies or not, Instantly.ai must be paused BEFORE Round 2 enrollment on June 4.
>Pausing today = 12 days of deliverability recovery before Round 2 sends.
>Pausing June 3 = 0 days. Every day you wait = worse Round 2 results.
>
>Steps (3 min): app.instantly.ai → Campaigns → find a1c08c3d (PM Cuyahoga) → ⋮ → Pause. Repeat for 626cd15d (Contractor Referral).
>
>Once paused: run `scripts/run_summit_pull.command` (double-click in Finder, 5 min). Two done. That's 8 minutes total.

---

💡 *Vera — Upgrade Proposal: Annual Plan Upsell Sequence (Tommy to write)*
>Idea: Tommy writes a 2-touch post-job annual plan upsell: (1) same-day text within 2 hours of job completion, (2) 30-day follow-up email when the wow factor is fading and they're thinking about next year
>Why: Annual Plan = $400–$600/yr per customer guaranteed. Once Google Ads go live, every new customer is also an annual plan opportunity. Closing even 5 annual plans this summer = $2,000–$3,000/yr recurring with zero new lead spend.
>Impact: Locks in recurring revenue at peak conversion moment (right after a great job). Also creates a review request hook in the same sequence.
>File Tommy will create: `outputs/tommy/annual_plan_upsell_sequence_2026-05-[date].md`
>Reply YES to approve — Tommy can write this in one session.

---

💡 *Vera — Upgrade Proposal: Roof Soft Wash Mini-Campaign*
>Idea: Write a separate 2-touch email to the existing 45 enrolled PM contacts specifically about roof soft washing — a different ask from the original exterior cleaning pitch
>Why: Roof soft wash is Forest City's highest-margin service ($600–$1,200 for a roof). Competitors in Cleveland rarely pitch it to commercial property managers. HOA boards and apartment managers have roofs that are visibly stained — this is a pain they recognize. A targeted "have you noticed the black streaks on your roof?" subject line will outperform a generic re-engagement.
>Impact: Even 1 commercial roof soft wash job = $800+. 45 already-warm contacts. Zero new Apollo spend.
>Note: This should NOT run while Instantly.ai is still active (same deliverability risk). Queue it for June 4+ after Instantly is paused.
>Reply YES to approve — Tommy writes the 2-touch copy, Danny handles enrollment as part of Round 2.

---

✅ *Vera — Scan Complete 2026-05-23 (Run 62)*
>4 auto-upgrades shipped | 3 deliverables | 2 proposals | 18 open issues
>
>Key addition this run: `scripts/run_summit_pull.command` — lowest-friction Summit County pull ever (double-click in Finder). Also: Round 2 Enrollment Readiness Checklist (June 3 GO/NO-GO) and June Week 3-4 Sprint now complete the full June planning suite.
>
>TODAY: (1) Pause Instantly.ai — 3 min (2) Text Anthony/Land Pro 440-320-2779 — 5 min (3) Double-click `scripts/run_summit_pull.command` — 5 min. Total: 13 minutes. All 3 are overdue.
>TUESDAY May 26: `outputs/donna/tuesday_may26_launch_card_2026-05-23.md` — 90 min blitz
>JUNE 3: `outputs/donna/round2_enrollment_readiness_checklist_2026-05-23.md` — GO/NO-GO before Round 2
