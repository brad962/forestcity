# June 9–14 Bridge Sprint
*Donna Park | Growth & Launch Strategist | Run 199 | 2026-06-08*

---

## Context
June 8 Cuyahoga mega-pull is done. 192+ segments enrolled. The June 9–14 window is the **first-opens monitoring period** — the highest-leverage week of the commercial season. Hot leads surface June 11–13. Miss this window and the momentum from the biggest pull of the year dissipates without converting.

**Estimated weekly time: 30–45 minutes total (5–7 min/day)**

---

## Day-by-Day Actions

### Monday June 9
**No action needed for the pull.** Touch 1 emails are sending automatically.

- [ ] Check Nina's daily hot leads report: `outputs/nina/hot_leads_2026-06-09.md` (auto-generates at 8am)
  - Confirm total enrolled count is visible
  - If 0 enrolled → troubleshoot (see post-pull card)
- [ ] Quick check: Are Facebook + Google ads still running?
  - Open Meta Ads Manager — any campaigns paused or flagged?
  - 2 minutes max. Don't make changes unless something is clearly broken.
- [ ] If you haven't already: run `python3 workers/lead_pipeline.py pending` to enroll gas station/fleet contacts (only if sequences created in Mixmax UI)

---

### Tuesday June 10
**Quiet day. Let the sequences run.**

- [ ] Nina daily report check — 8am auto-generates. Look for: any replies already (rare this early, but possible)
- [ ] LinkedIn: Check if any Cuyahoga contacts are connecting organically after seeing Touch 1

**One optional action (15 min):**
- Send 2-3 personal "saw your profile" messages on LinkedIn to the highest-value companies from the June 8 pull (Cleveland Clinic FM, Rock Hall FM, YMCA director — look these up and send a warm personal note before Touch 1 even completes its sequence)

---

### Wednesday June 11 — FIRST HOT LEADS DAY 🔥
**The most important day of the week. Block 20 minutes.**

- [ ] Check Nina's hot leads report the moment you wake up: `outputs/nina/hot_leads_2026-06-11.md`
- [ ] For every contact with 2+ opens:
  1. **Connect on LinkedIn immediately** — within 2 hours of seeing the open
  2. Use message template: `outputs/tommy/hot_lead_linkedin_dm_playbook_2026-05-18.md`
  3. Note the company — high-opens means active evaluation; they're vetting vendors right now
- [ ] For any contact who REPLIED: respond personally within 2 hours. Copy-paste response from `outputs/tommy/touch3_reply_response_templates_2026-05-20.md`
- [ ] Log all hot lead LinkedIn connects in `pipeline_data.json` — stage: "Contacted", add next_followup date

**What to expect June 11:**
- 3-8 hot leads is a strong result for Day 3
- Hospital/health system FMs and YMCA directors are most likely to open early (they have structured vendor review processes)
- Government FM contacts open slower (longer decision cycles)

---

### Thursday June 12
**Hot leads follow-up day.**

- [ ] Did you connect on LinkedIn with everyone from yesterday's hot leads? If not, do it now — LinkedIn connect window = first 48 hours of open
- [ ] Nina daily report — any new hot leads today?
- [ ] Did anyone ACCEPT your LinkedIn connection request? If yes: send the post-connect DM immediately
  - Use `outputs/tommy/linkedin_followup_post_connect_2026-05-18.md` (Version A or B depending on contact type)
- [ ] Check Google Ads: any calls or form fills from this week's traffic?
  - Look at Google Ads "Call Details" report — note any calls from this week

**Optional:**
- Post a Facebook content piece — June week 2 content should be live. Use `outputs/jasmine/facebook_posts_june_week2_4_2026-05-24.md`

---

### Friday June 13
**End-of-week triage.**

- [ ] Quick 5-minute pipeline check: How many contacts enrolled (June 8 total), how many hot leads (2+ opens), how many connected on LinkedIn
- [ ] Log all LinkedIn connect statuses in `pipeline_data.json`
- [ ] Any "Estimate Sent" contacts from earlier pipeline? Follow up today (Friday = last business day window this week)
- [ ] Read Nina's daily report — look for any new replies

**Set up for next week:**
- [ ] Confirm `run_lake_both.command` is ready in `scripts/` folder — Lake County pull is Monday June 15
- [ ] Set a 7:30am alarm for Monday June 15

---

### Saturday June 14
**Optional: GBP post + neighborhood canvass if jobs are running**

- [ ] If you had any jobs this week: Post the before/after on Google Business Profile and Facebook
  - GBP post template: `outputs/jasmine/gbp_post_may21_2026.md` (update with current photo)
- [ ] If you're on a job site: run the neighbor canvass script → `outputs/tommy/neighbor_canvass_script_2026-05-26.md`
- [ ] Past customer re-engagement? If you haven't sent the June past customer texts yet: `outputs/tommy/past_customer_june_text_scripts_2026-05-26.md` — 5 texts, 10 min, $1,200-$4,000 expected revenue

---

## Week Success Metrics

| Metric | Minimum | Good | Great |
|--------|---------|------|-------|
| Contacts enrolled from June 8 pull | 80+ | 150+ | 250+ |
| Hot leads (2+ opens) by Friday June 13 | 5+ | 10+ | 20+ |
| LinkedIn connects sent | 3+ | 8+ | 15+ |
| LinkedIn connections accepted | 1+ | 3+ | 6+ |
| Replies received | 0-1 (normal) | 2-3 | 4+ |
| Quotes sent | 0-1 | 1-2 | 2-3 |

---

## Key Files This Week

| File | Purpose |
|------|---------|
| `outputs/nina/hot_leads_2026-06-11.md` | First hot leads report — check morning of June 11 |
| `outputs/tommy/hot_lead_linkedin_dm_playbook_2026-05-18.md` | LinkedIn connect messages for hot leads |
| `outputs/tommy/linkedin_followup_post_connect_2026-05-18.md` | Post-connect DM scripts |
| `outputs/tommy/touch3_reply_response_templates_2026-05-20.md` | Reply response copy-paste scripts |
| `outputs/vera/june8_post_pull_action_card_2026-06-08.md` | What happened June 8 + troubleshooting |

---

## Monday June 15 Preview — Lake County Pull

Next Monday = Lake County pull. Marina corridor. Mentor, Willoughby, Painesville.

Key new segments for Lake County:
- **Marinas & waterfront properties** — Lake Erie shoreline; peak season; boat launches + dock areas + storage lots
- **Charter fishing operators** — owner-operators on Lake Erie; peak walleye season June-August
- **Corporate park / office campus FMs** — Mentor/Willoughby suburban corridor

Double-click: `scripts/run_lake_both.command`
Time: 7:30am Monday June 15 (6-10 minutes unattended)

---

*Generated by Donna Park | June 8, 2026 | Run 199*
