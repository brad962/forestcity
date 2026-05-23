# June Commercial Pipeline Calendar
### Donna Park | Growth & Launch Strategist
*May 26 – June 18, 2026 | 4-Week Commercial Outreach Master View*
*Updated: 2026-05-23*

---

## The 4-Week Commercial Arc

```
Week 0 (May 26–30)    →  Reply Window Closes | Bridge Emails | Ads Launch | New Pull
Week 1 (June 2–6)     →  Round 2 Enrollment Gate | Gas Station Launch | LinkedIn Wave 2
Week 2 (June 9–13)    →  Round 2 Sequence Live | Contractor Follow-Up Wave 2
Week 3 (June 16–18)   →  Mid-sequence check | Hot lead pivot | Geauga/Portage pull
```

---

## WEEK 0: May 26–30 (Memorial Day Blitz Week)

### Monday May 26
**Critical path — do these in order:**

| Time | Task | Resource | Owner |
|------|------|----------|-------|
| 8:00am | Run check_replies.py | `python3 workers/check_replies.py` | Bradley |
| 8:30am | If any replies → respond within 1 hour | `outputs/tommy/touch3_reply_response_templates_2026-05-20.md` | Bradley |
| 9:00am | Danny pull — Medina County (Week 22 rotation) | `python3 workers/lead_pipeline.py both` | Bradley (local) |
| 9:00am | ALSO run Summit override (LAST CHANCE) | `python3 workers/lead_pipeline.py danny Summit` | Bradley (local) |
| 10:00am | Send bridge emails to top 5 hot leads (personal Gmail) | `outputs/tommy/hot_lead_bridge_email_may26_2026-05-22.md` | Bradley |
| 11:00am | Launch Google Ads | `outputs/vera/may26_ads_launch_checklist_2026-05-22.md` | Bradley |
| 11:30am | Launch Facebook Ads | same checklist | Bradley |
| 1:00pm | Contractor follow-up texts (5 contacts from open pipeline) | `outputs/tommy/may26_monday_morning_followup_texts.md` | Bradley |
| 2:00pm | Run check_replies.py again | local cron will also run at 2pm | Auto |
| EOD | Log: how many replies received? Ads launched? | Slack update | Bradley |

**Decision gate:** If 0 replies by end of May 26 → proceed with Round 2 enrollment plan (June 4 target).

### Tuesday May 27 – Thursday May 29
- Run `check_replies.py` daily (8:45am + 2pm cron handles this)
- Post LinkedIn content (Post 1 Mon, Post 2 Wed, Post 3 Fri) — `outputs/jasmine/linkedin_posts_may26_week_2026-05-23.md`
- Engage with any LinkedIn comments / DMs same day
- Monitor Facebook + Google ads performance daily (first 3 days are learning phase)

### Friday May 30
- Weekly Nina report fires 8:30am (shows enrolled count, open rate, any replies)
- Ads report: is cost-per-click reasonable? Kill any ad set spending with 0 clicks
- LinkedIn connects: send 5 new connects to Medina County PMs (from Danny's new pull)
- **Decision check:** Total replies from sequence? ≥ 1 = continue; 0 = Round 2 confirmed for June 4

---

## WEEK 1: June 2–6 (Round 2 Enrollment Gate)

### Pre-enrollment checklist (complete before June 4):
- [ ] Pause Instantly.ai campaigns a1c08c3d + 626cd15d (3 minutes — `outputs/vera/instantly_pause_guide_2026-05-22.md`)
- [ ] Danny Medina County pull ran May 26 (verify in activity.log)
- [ ] Danny Summit County pull ran (verify — either May 24/25 override or May 26 override)
- [ ] New leads in contacts_cache.json (target: 25+ new PMs from Medina + Summit)
- [ ] Subject lines revised (A/B test setup) — `outputs/tommy/email_subject_line_ab_test_2026-05-22.md`
- [ ] Email 1 rewrite ready — `outputs/tommy/round2_pm_sequence_rewrite_2026-05-21.md`
- [ ] Gas Station sequence ID: create in Mixmax → paste into `integrations/mixmax.py` line 54

### Monday June 2 (Week 23 rotation → Geauga + Portage)
| Time | Task | Notes |
|------|------|-------|
| 7:00am | Danny auto-cron fires | Geauga + Portage pull (Week 23) |
| 8:00am | Nina weekly report fires | Shows total enrolled, open rates |
| EOD | Confirm cron ran | Check activity.log |

### Wednesday June 4 — ROUND 2 ENROLLMENT DAY
**This is the critical date. All of the above must be done first.**

1. Pause Instantly.ai (if not already paused)
2. Update Mixmax sequence with new Email 1 from round2_pm_sequence_rewrite — use Version B or C based on which performed better in Round 1
3. Enroll new Medina + Summit + any Lake/Lorain leads pulled since May 12
4. Enroll gas station contacts if Mixmax ID is set: `python3 workers/lead_pipeline.py pending`
5. Set send time: **10:30am Tuesday/Wednesday/Thursday** (avoid Monday AM which is crowded)
6. Target enrollment: 30–50 new contacts across PM + gas station sequences

**Round 2 sequence: PM sequence**
- Email 1: New subject line (A/B per `email_subject_line_ab_test_2026-05-22.md`)
- Email 2 (Day 5): Same as Round 1 (performance was unknown; keep baseline)
- Email 3 (Day 9): HOA spring meeting angle — `outputs/tommy/hoa_spring_meeting_email_2026-05-22.md`
- Touch window: June 4 → June 18 (14 days)

### Thursday June 5
- LinkedIn Wave 2: connect with Geauga + Portage PMs from June 2 pull
- Contractor check-in: any contractor opened email + no reply? Personal text — `outputs/tommy/may26_monday_morning_followup_texts.md`
- Google Ads: check first full week. If CPL < $50, increase daily budget by $10

---

## WEEK 2: June 9–13 (Sequences Running + Contractor Wave 2)

| Day | Action | File |
|-----|--------|------|
| Mon June 9 | Danny cron — Cuyahoga (Week 25) | Auto |
| Mon June 9 | Nina weekly report — shows Round 2 early open rates | Auto |
| Tue June 10 | Round 2 PM sequence: Email 1 has been out ~1 week. Check open rates. | nina_report or check_replies |
| Wed June 11 | Contractor follow-up wave 2 | `outputs/tommy/contractor_followup_texts` |
| Thu June 12 | LinkedIn: post commercial content (Jasmine to write June week 2 posts) | TBD |
| Fri June 13 | Ads review: week 2 performance. Kill losing ad sets, scale winners. | Google Ads + Meta dashboard |

**Key metric to watch:** Round 2 open rate vs. Round 1. If Round 1 was < 20%, Round 2 should hit 25%+ with new subject lines. If still < 20%, the deliverability issue isn't Instantly — it's domain reputation or list quality.

---

## WEEK 3: June 16–18 (Mid-Sequence Pivot)

| Day | Action |
|-----|--------|
| Mon June 16 | Nina weekly report — first Round 2 reply data visible |
| Mon June 16 | Hot leads from Round 2: connect on LinkedIn + call if 2+ opens |
| Tue June 17 | Round 2 Email 3 (HOA spring meeting angle) fires for Day 9 enrollees |
| Wed June 18 | Geauga + Portage pull (Week 25 catch-up if missed) |
| Thu June 18 | Decision: enough replies to keep sequence running? Plan Round 3? |

---

## Key Dependencies & Critical Path

```
Summit County pull (by May 25) ──┐
                                  ├──→ Round 2 enrollment (June 4) ──→ replies by June 18
Medina County pull (May 26) ─────┘
Instantly.ai paused (before June 4)
Email 1 rewrite ready (before June 4)
Gas station Mixmax ID (before June 4)
```

---

## Revenue Math — What This 4-Week Push Is Worth

| Channel | Jobs if sequence converts at 2% | Avg job value | Revenue |
|---------|--------------------------------|---------------|---------|
| PM sequence Round 2 (40 new enrollees) | 0.8 → 1 job | $800 | $800 |
| Gas station (18 enrollees, 1 response) | 1 account = 3 locations | $1,200 | $1,200 |
| Facebook Ads ($30/day × 28 days = $840 spend) | 4–8 booked at $125 CPL | $600 avg | $2,400–$4,800 |
| Google Ads ($20/day × 28 days = $560 spend) | 6–12 booked at $50 CPL | $500 avg | $3,000–$6,000 |
| Contractor referrals (2 active partners × 1 referral/week) | 8 jobs | $400 avg | $3,200 |

**Total potential: $10,600–$16,000 in new revenue, June 2–30**

---

## Weekly Tracking Table

| Week | Danny Pull | Enrolled | Replies | Ads Jobs | Total Revenue |
|------|-----------|----------|---------|----------|---------------|
| May 26–30 | Summit + Medina | — | — | 0 | — |
| June 2–6 | Geauga + Portage | 30–50 | 0–2 | 1–2 | — |
| June 9–13 | Cuyahoga | 25 more | 1–3 | 2–4 | — |
| June 16–18 | Review | — | 2–5 | 3–6 | — |

*Fill in actual numbers weekly. Update in Slack or in this file.*

---

*Donna Park | Growth & Launch Strategist | 2026-05-23*
*See also: `outputs/donna/round2_enrollment_plan_2026-05-21.md` | `outputs/donna/june_week1_sprint_2026-05-20.md` | `outputs/vera/may26_ads_launch_checklist_2026-05-22.md`*
