# June 1–4 Sprint Card
*Vera Cole | Chief Innovation Officer | Written 2026-05-27*
**The 4-day push that turns a Medina county pull into $55K–$144K in qualified pipeline.**

---

## OVERVIEW

| Day | Date | What Happens |
|-----|------|-------------|
| Day 0 | Sun June 1 | Medina pull + Round 2 staging (2 hrs total, mostly unattended) |
| Day 1 | Mon June 2 | Ad Day 7 review + lead follow-ups + gas station blast (if not done) |
| Day 2 | Tue June 3 | Final enrollment prep + Medina contacts staged for June 4 |
| Day 3 | Wed June 4 | ROUND 2 ENROLLMENT — Danny + Carla Medina leads go into sequences |

---

## JUNE 1 — SUNDAY EVENING (2 hours, ~30 min active)

**Pre-check (5 min):**
- [ ] Instantly.ai confirmed paused (`INSTANTLY_PAUSED=true` in .env) — if not, STOP and pause NOW
- [ ] `python3 workers/check_replies.py` — any late gas station or contractor replies?

**Run Medina pull (6 min, mostly unattended):**
```bash
cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both Medina
```
Or double-click: `scripts/run_medina_both.command` in Finder

**While pull runs (25 min):**
- Text any Wave 2 contractors you haven't reached yet (pipeline_data.json next_followup=2026-05-28 contacts)
- Check Workiz — any jobs booked from Facebook/Google ads this week?
- Check `outputs/donna/launch_week_lead_log_2026-05-26.md` — fill in Week 1 totals

**After pull completes:**
- [ ] Check `outputs/danny/leads_medina_property_managers_[date].md` — how many fresh leads?
- [ ] Update pipeline_data.json for any gas station contacts reached this week
- [ ] Read June 3 evening checklist (`outputs/donna/june3_tuesday_evening_checklist_2026-05-26.md`)

**Reference:** `outputs/donna/june1_medina_pull_guide_2026-05-24.md`

---

## JUNE 2 — MONDAY MORNING (45 min)

**Priority 1 — Ad Day 7 Review (20 min):**
- Open Facebook Ads Manager → check: spend, reach, CPM, CTR, link clicks, leads submitted
- Open Google Ads → check: impressions, clicks, calls, conversions
- Benchmarks (Week 1 targets): 3–10 FB lead gen form fills, 2–5 Google calls
- Decision guide: `outputs/rick/week2_facebook_ads_scaling_guide_2026-05-26.md`
- If working (leads + calls): bump FB budget +20%, hold Google steady
- If not working: read Week 2 scaling guide before touching anything

**Priority 2 — Ad Lead Follow-Up (15 min):**
- Any FB/Google leads from the past 7 days not yet called back?
- `outputs/tommy/inbound_response_protocol_2026-05-24.md` — Section 2 for call-back scripts
- Log all lead outcomes in `outputs/donna/launch_week_lead_log_2026-05-26.md`

**Priority 3 — Gas Station Blast Wave 2 (10 min, if not done):**
- 6 Tier 2 gas station contacts not yet emailed
- Guide: `outputs/danny/gas_station_manual_email_blast_2026-05-25.md` Section B

---

## JUNE 3 — TUESDAY EVENING (15 min — final prep)

Read: `outputs/donna/june3_tuesday_evening_checklist_2026-05-26.md`

**7 go/no-go checks:**
1. [ ] `grep INSTANTLY_PAUSED /Users/bradleyneal/forestcity/.env` → must show `true`
2. [ ] Medina pull completed June 1 → `outputs/danny/leads_medina_*.md` exists
3. [ ] New Mixmax email copy (VOC rewrite) loaded into sequence
4. [ ] Gas station path: either Mixmax sequence created OR manual blast sent
5. [ ] Summit pull completed (ran anytime May 27–31) — check logs/activity.log
6. [ ] Alarms set for 7:30am June 4
7. [ ] Read June 4 battle card tonight: `outputs/donna/june4_enrollment_battle_card_2026-05-24.md`

**GO/NO-GO table:**
| Condition | Status | Action if NO |
|-----------|--------|-------------|
| Instantly.ai paused | ??? | Stop — pause NOW (3 min) |
| Medina leads pulled | ??? | Run `lead_pipeline.py both Medina` tonight |
| VOC copy in Mixmax | ??? | Paste from `round2_pm_sequence_voc_rewrite_2026-05-23.md` |
| Gas station path clear | ??? | Send manual blast tonight (20 min) |

---

## JUNE 4 — WEDNESDAY MORNING (90 min — ENROLLMENT DAY)

Read first: `outputs/donna/june4_enrollment_battle_card_2026-05-24.md`

**7:30am — Carla activation (45 min):**
- Read: `outputs/carla/june4_carla_activation_card_2026-05-25.md`
- Enroll Medina contractor/referral contacts: `python3 workers/lead_pipeline.py pending`
- Pool service text blitz (5 contacts from `outputs/carla/pool_service_referral_blitz_2026-05-24.md`)
- Contractor pipeline revival texts (6 stale contacts)

**8:00am — Danny enrollment (30 min):**
- Run: `python3 workers/lead_pipeline.py pending` (enrolls all pending Medina PM contacts)
- Verify in Mixmax: sequences show new recipients
- Update pipeline_data.json for any manually-imported gas station contacts

**8:30am — Confirm & monitor:**
- `python3 workers/nina_report.py daily` — verify new enrollments show up
- Set reminder for June 7 (Day 3 check) to review open rates on new batch

---

## REVENUE MATH — WHY THIS MATTERS

| Segment | Contacts (est.) | Sequence | Reply Rate | Revenue per booking |
|---------|-----------------|----------|------------|---------------------|
| Medina PMs | 20-40 | PM VOC | 5-8% | $1,800-$5,000/yr |
| Gas Stations | 12 | Gas Station | 8-12% | $3,600-$9,600/yr |
| Contractors (referral) | 6-10 | Contractor | 10-15% | $2,400-$8,400/yr referral value |

**Conservative scenario (5% reply across 50 contacts):** 2-3 replies → 1-2 bookings → $3,600–$14,000/year ARR from one enrollment run.
**Optimistic scenario (8% reply + Medina commercial contacts):** 4-6 replies → $14,000–$40,000/year ARR.

---

## BLOCKERS — CHECK THESE NOW (May 27)

| Blocker | Deadline | Status | Action |
|---------|----------|--------|--------|
| Instantly.ai pause | ASAP (9 days recovery) | ❓ | app.instantly.ai → pause a1c08c3d + 626cd15d |
| Summit pull | May 31 (4 days) | ❓ | Double-click `scripts/run_summit_pull.command` |
| Gas station Mixmax sequence | June 3 latest | ❓ | Create in Mixmax UI → paste ID into mixmax.py line 54 |
| VOC copy in PM sequence | June 3 latest | ❓ | `outputs/tommy/round2_pm_sequence_voc_rewrite_2026-05-23.md` |

---

*All referenced files are in `/outputs/`. Read the June 4 battle card the night of June 3.*
