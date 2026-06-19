# Strategy Brief — June 19, 2026
*Donna Park | Growth & Launch Strategist | Forest City Power Washing*
*Father's Day Eve. Day 24 of ads. Lorain County pull in 3 days. 15 days to July 4th.*

---

## What's Working

**1. Facebook + Google Ads — Day 24, Best Creative Set of the Season**
Rick's June 15 refresh loaded five fully VOC-built Facebook variations and 10 new Google RSA headlines. Ad 2 ("Fourth of July Is 19 Days Out") is the lead rotation through June 28 — this is the right call. The July 4 deadline is 15 days away, credible, and universally understood. Ad 4 (sensory/mold hook: "If You Can Smell the North Side, It's Bad") is still the strongest cold audience stopper. The Day 21 scaling decision was yesterday, June 18 — if Bradley hasn't logged in to check CPL and booked jobs, do it this morning. The scale trigger is: 3+ booked jobs from ads + CPL under $25 → increase daily budget $30 → $36. Don't skip this check.

**2. Jasmine's Content — Fully Automated Through June 30**
Five posts were ready and queued for the week of June 16: before/after Monday, roof education Tuesday (Gloeocapsa magma soft wash explainer — our best educational post of the season), social proof Wednesday, summer event seasonal hook Thursday (Father's Day/cookout angle), behind-the-scenes Friday. This is the engine running on autopilot. Zero production needed from Bradley. The July 4 urgency language should be in every caption starting now.

**3. Marcus VOC Library — 59 Phrases, Mid-June Map Dialed In**
The June 15 VOC update is the sharpest batch of the season. The "Father's Day panic" language (expires Sunday), the "July 4 countdown" window, the "I've been ignoring it since April" delay-guilt hook, and the "I finally looked at it from the street and was mortified" curb-perspective trigger are all active and mapped to specific channels. Marcus also flagged the June 30 fiscal close window for commercial PMs — this is real and Danny should be hitting it right now. The VOC is the brief; it's telling us exactly what to say and when to stop saying it.

**4. Cuyahoga Mega-Pull — 192+ Segments Enrolled, Hot Leads Window Has Closed**
The June 8 Cuyahoga pull was the largest commercial outreach event of the season. The first-opens hot leads window (Days 5–7, June 13–15) is officially closed as of today. Any contact with 2+ opens who hasn't been connected on LinkedIn yet is cooling fast — each day past the open window drops connect acceptance rates. Check Nina's hot leads reports from June 13–15 and send any outstanding LinkedIn DMs today. After today, these go to the standard follow-up sequence.

**5. Annual Plan Pitch Script — Highest-Margin Sale, Zero Marketing Spend Needed**
Tommy built the 20-second pitch (`outputs/tommy/annual_plan_pitch_script_2026-05-26.md`). Every completed job from now through June 30 is a live upsell opportunity. The math: 5 annual plans = $2,250 pre-collected + $2,250 locked for fall. June 24 is Wave 2 past-customer push — but Bradley doesn't need to wait. Every job this week is a pitch opportunity the moment the job wraps.

---

## This Month's Priority

### Priority 1 — July 4th Residential Blitz (June 19–28) — Peak Window, 15 Days Out
**Rationale:** July 4th is 15 days out as of today. This is the tightest, most credible residential deadline of the summer season. The language to run: "4th of July slots going fast," "book before the holiday weekend," "want it done before the Fourth?" Marcus's June 15 VOC update is explicit — this language peaks June 21–28 and dies after June 28. Rick's Ad 2 is already running it. Jasmine's posts need to be adding "July 4th" CTA language to every caption. Tommy should be hitting the "Father's Day eve" text blast today before the window closes Sunday — that's the bridge from Father's Day into the July 4 sprint.

The neighbor canvass after every job is the highest-ROI amplifier during this window. Every house Bradley cleans between now and June 25 is a live demo for the 3 nearest neighbors. "We just finished next door — want a quote while I'm here? We have slots open before the Fourth." Zero cost, highest conversion rate of any channel.

**Scaling decision:** If the Day 21 check shows CPL under $25 + 3 booked jobs, increase budget from $30 → $36 and add the Lookalike audience layer. If not done yet, do it this morning.

### Priority 2 — Apollo API Fix + Lorain June 22 Pull — 3-Day Critical Window
**Rationale:** This is the most operationally damaging issue in the whole system right now and it's been running silently for 8+ days. `api.apollo.io` is not in the cloud environment's egress allowlist. Danny and Carla have pulled zero leads every single day since at least June 11. Eight days of zero lead flow in peak season. The Lorain County pull scheduled for June 22 — which hits Segments #201 (Steel Fabrication), #202 (Municipal Recreation Centers/Community Pools), and #203 (Private Colleges/Universities, including Oberlin College as the flagship target) — will also pull zero unless this is fixed in the next 3 days.

**The fix is not technical work — it's a settings change.** Either: (a) add `api.apollo.io` to the network egress allowlist in the Claude Code on the web environment settings at code.claude.com/docs/en/claude-code-on-the-web, or (b) run `python3 workers/lead_pipeline.py danny Lorain` locally from Bradley's Mac on June 22 instead of relying on the scheduled cloud run. Option B is the faster path and doesn't require environment configuration.

This is not optional. Every day the Apollo block persists is a day no new commercial contacts enter the pipeline. Lorain June 22 has three new high-value segments with zero competitor outreach — universities, rec centers, steel fabrication shops. That pull needs to fire.

---

## Campaign Ideas

### Idea 1 — "Father's Day → Fourth of July" Urgency Bridge (Today, June 19–June 28)
**Seasonal hook:** Father's Day is Sunday (June 21) and July 4th is 15 days out. These two deadlines create a natural urgency bridge — customers who didn't book for Father's Day see "family coming over" as a continuing seasonal reason through the holiday. The hook shifts on Monday, June 23: "Father's Day is over but July 4th is in 11 days — do you really want to spend the whole summer looking at it?"
**Audience:** Homeowners 35–65, all 7 NE Ohio counties; Facebook Lead Gen via Rick's Ad 2; organic via Jasmine's captions
**Offer:** Free estimate, guaranteed pre-July 4 scheduling if booked by June 25
**Channel:** Tommy text blast (TODAY for Father's Day hook); Facebook Ad 2 (July 4 urgency); Jasmine captions; Nextdoor posts in active job neighborhoods
**What's needed:** Tommy fires Father's Day text blast today using existing scripts. Rick holds Ad 2 in lead rotation through June 28 then retires it. Jasmine adds "July 4" to every caption through June 28.

### Idea 2 — "June 30 Budget Close" Commercial Conversion Sprint (June 19–27)
**Seasonal hook:** June 30 fiscal close is 11 days out. Property managers with unspent exterior maintenance budgets are in spend-or-lose mode. This is the hottest 2-week commercial window of the year — Marcus named it explicitly in the June 15 VOC update with exact PM language: "I need the invoice before June 30 or I lose the budget line." The 192+ enrolled Cuyahoga contacts are in sequence right now. A subject line update on Touch 2 or 3 that names the June 30 deadline is a 10-minute change that could spike commercial reply rates.
**Audience:** Enrolled Cuyahoga mega-pull contacts (192+ segments); Danny's Mixmax sequences; any Cuyahoga PM with 2+ email opens
**Offer:** Free site assessment + scheduling priority for June jobs; invoice deliverable by June 30
**Channel:** Mixmax sequence subject line update (Touch 2/3); LinkedIn DM to all contacts with 2+ opens; personal text if direct number exists
**What's needed:** Bradley (or Danny) updates Touch 2/3 subject line in Mixmax to: "Budget closing June 30 — exterior cleaning quote for your properties?" No new enrollment, no new contacts — just a subject line swap. Takes 10 minutes. Also: Bradley texts any PM in the pipeline who's been quoted but hasn't booked with: "Just checking in before June 30 — want to get this on the calendar before the budget resets?"

### Idea 3 — Roof Education Ownership Campaign — Own the Lane Before Late June (June 19–July 15)
**Seasonal hook:** Black roof streaks are fully visible right now. Marcus identified competitor gaps: Shine Right doesn't offer soft wash at all (their customers have algae-streaked roofs and no local vendor to call). Clean Pro markets it but has trust problems. Brothers doesn't promote it. This is Forest City's clearest lane to dominate in the next 4 weeks before competitors can react.
**Audience:** Homeowners 35–65, east-side Lake Erie corridor (Willoughby, Mentor, Euclid, Lyndhurst, Mayfield Heights — highest algae concentration in service area due to north-facing exposure and lake humidity); Shine Right's Avon/Westlake ZIP codes as secondary
**Offer:** "Free roof assessment included with every house washing quote"
**Channel:** Rick's Google RSA headlines already include "Roof Soft Wash · NE Ohio," "Soft Wash · Safe on Roofs," and "Green Siding? We Fix That" — loaded June 15. Jasmine's Tuesday June 17 roof education post is already live. Tommy adds the free roof assessment offer to the estimate follow-up email.
**Why now:** Rick's June 15 competitor intel shows Shine Right running no roof soft wash content and Eco/Brothers not specifically promoting the service. Jasmine's Tuesday post is already seeding this. If a targeted Facebook ad to east-side ZIPs runs the "black streak" hook with roof soft wash education, Forest City can establish category ownership before anyone else notices the opening. Zero competitive response possible in the next 2–3 weeks — their content pipelines can't move that fast.

---

## Lead Magnet Idea

### "NE Ohio Summer Home Maintenance Checklist" — Kit.com — Final Call (Week 4)
This is the fifth consecutive strategy brief carrying this item unchanged. It closes this week or it doesn't close before July.

**Urgency has increased since the last brief:** If the Day 21 scaling decision fires and budget increases from $30 → $36/day, traffic accelerates. Every homeowner who clicks an ad and doesn't immediately book is permanently lost without email capture. At the current ad spend, a conservative 0.5% email capture rate = 30–50 subscribers per month in a 3-email nurture sequence. At 5% nurture-to-booking = 2–3 additional jobs per month from a 30-minute one-time setup.

**Rename for the July 4 window:** "NE Ohio Summer Home Maintenance Checklist" hits the exact seasonal moment. The opt-in hook: "Northeast Ohio homeowners use this to prep their home before the summer's over — grab the free checklist." This converts better than a generic annual checklist because it's time-anchored to right now.

**30-minute setup, all assets pre-built:**
1. Create Kit.com account at kit.com (free up to 10K subscribers)
2. Content is built: `outputs/tommy/home_maintenance_checklist_content_2026-05-24.md`
3. Landing page copy is built: `outputs/donna/kit_email_capture_setup_2026-05-24.md`
4. Nurture sequence is built: `outputs/donna/nurture_sequence_home_maintenance_checklist_2026-05-12.md`
5. Text Rick the Kit.com landing page URL — he routes 10% of ad traffic to it as a capture layer

Every asset is already written. This is a copy-paste job, not a creative job. 30 minutes. The only question is whether it happens this week.

---

## Referral / Partnership Angle — For Carla

### Realtor Summer Listing Push — Pre-July 4 Window (This Week Only)
The summer listing surge is running at full peak. Realtors in Carla's pipeline who were contacted in the spring now have active listings going to market in June and July. The connection between July 4th and realtor motivation is direct: a house that books this week can be clean by June 23–25, giving the realtor 10 days before the holiday weekend for listing photos. Buyers slow down on July 4 weekend; a listing that goes live July 5 with great curb appeal competes harder.

**Carla's play — this week, 5–7 texts:**
Pull realtor contacts from the contractor/referral pipeline. Personal text, not bulk: "Hey [first name] — busy listing season. Any homes coming up that need exterior cleaning before photos? We're booking the week of June 23 and can usually get it done in 3–5 days. Happy to prioritize your listings before the Fourth." This is Carla calling an instinct every realtor already has. She's not selling them — she's calling a problem they're already feeling.

**Secondary setup:** Any realtor who books a job this month gets added to the Annual Plan pitch cadence. The new owner of a sold home will need exterior cleaning within 12–18 months — Carla's referral turns into a recurring customer. Bradley gives Carla the green light today, she runs it this week while the July 4 hook is live.

---

## Action Items for Bradley

- **TODAY — Father's Day text blast (before Sunday, window closes):** Tommy's scripts are built and ready. This is the last day the "Father's Day" hook lands naturally — tomorrow it sounds like an afterthought. Text blast to all past customers and open leads today using the Father's Day urgency hook. Then pivot to July 4 language Monday morning.

- **TODAY OR TOMORROW — Apollo API fix (3 days before Lorain June 22 pull):** The cloud environment has blocked `api.apollo.io` for 8+ days. Danny and Carla have pulled 0 leads every day since June 11. This is silently draining the commercial pipeline. Fix: either add the egress allowlist (docs at code.claude.com/docs/en/claude-code-on-the-web) OR block 20 minutes on June 22 to run `python3 workers/lead_pipeline.py danny Lorain` from your local Mac instead. Running it locally is the faster path. Don't let Lorain pull another 0-lead day — Oberlin College, Lorain Metro Parks recreation centers, and the Sheffield Village steel fabrication corridor are waiting to be hit.

- **TODAY — Ads Day 21 scaling decision (10 min):** Open Facebook Ads Manager. Count booked jobs since May 26. If 3+ and CPL under $25: increase daily budget $30 → $36 (nothing else — one change, nothing else). Also confirm Rick's Ad 2 ("Fourth of July Is 19 Days Out") is the lead rotation. If the budget doesn't scale, check again June 22.

- **This week — Kit.com setup (30 min, one time, final deadline):** All assets are built. This is a paste-and-launch job. Create Kit.com account (free up to 10K subscribers) → upload checklist → build landing page → activate nurture sequence → text Rick the URL. If the budget scales tomorrow, traffic accelerates. Every day without email capture is permanent traffic loss.

- **June 19–25 — Neighbor canvass after every job (highest-ROI channel right now):** After each completed job, knock the 3 nearest neighbor doors: "We just finished next door — have slots open before the Fourth of July, want a quote while I'm here?" The cleaned house is the demo. Target 1–2 additional jobs per job site. Use script in `outputs/tommy/neighbor_canvass_script_2026-05-26.md`.

- **Tell Carla — Realtor texts this week before July 4 window narrows:** 5–7 personal texts to active listing realtors in the referral pipeline: "Any homes coming up before the Fourth that need a power wash before listing photos? We're booking the week of June 23." Hook closes June 27 — after that, "before the Fourth" becomes implausible for scheduling.

- **Gas station sequences — close Day 36 today or defer to July:** This blocker has carried 36 days. If Mixmax sequence creation in the UI isn't happening, use the manual Gmail approach from `outputs/tommy/gas_station_sequence_copy_2026-06-03.md` — BCC all 12 contacts, 10 minutes. Send Touch 1 today. Don't let the peak-season window close on 12 commercial contacts that have been sitting untouched since May.

---

## Infrastructure Blockers (Bradley Action Required)

| Blocker | Days Open | Status | Fix |
|---------|----------|--------|-----|
| Apollo API egress block | 8 days | **CRITICAL** | Add api.apollo.io to egress allowlist OR run locally June 22 |
| Gas station Mixmax sequences | 36 days | **Closing on revenue** | Manual Gmail BCC to 12 contacts (10 min) OR create Mixmax sequences in UI |
| Kit.com email capture | 25+ days | **Budget scaling today** | 30-min setup, all assets built |
| GitHub Actions PAT workflow scope | 20+ days | Operational | github.com/settings/tokens → Edit → check "workflow" → Save |
| danny.md archive (482KB) | 10 days | Low urgency | Say YES or NO in Slack — Vera waits |

---

## Revenue Targets — Week of June 19–26

| Source | Conservative | Target |
|--------|-------------|--------|
| Facebook/Google ad leads → bookings | $1,200 | $2,800 |
| Neighbor canvass (1–2 jobs per job site) | $600 | $1,400 |
| Annual plan upsells (2–3 closed) | $800 | $1,400 |
| Carla realtor referrals (1–2 jobs) | $300 | $800 |
| Gas station first reply (if sent today) | $0 | $600 |
| Commercial PM June 30 close replies | $0 | $1,200 |
| **Week total** | **$2,900** | **$8,200** |

---

*Donna Park | Growth & Launch Strategist | Forest City Power Washing*
*Next brief: June 26, 2026 — July 4 blitz final week, Lorain pull results, Kit.com status, gas station reply window, commercial June 30 close outcomes, ads Day 31 budget review*
*File: `outputs/donna/strategy_brief_2026-06-19.md`*
