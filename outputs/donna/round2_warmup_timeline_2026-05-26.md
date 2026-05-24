# Round 2 Enrollment Warmup Timeline
### May 26 → June 3 | Day-by-Day Deliverability + Prep Plan
*Donna Park | Growth & Launch Strategist | 2026-05-26*

---

## Why This Doc Exists

June 4 is Round 2 enrollment day. You have 9 days between Tuesday's ad launch and that enrollment run.

If you just wait and do nothing, the deliverability gap widens. The goal of this 9-day window is:
1. Let Instantly.ai pause recover fully (7–10 days minimum)
2. Send bridge emails from personal Gmail to keep warm contacts engaged
3. Pull fresh leads for the June 4 enrollment batch
4. Get the gas station sequence live so those 18 contacts go in on the same run
5. Run the readiness checklist the night before so June 4 morning is zero-friction

**The critical path: pause → bridge → pull → sequence → check → enroll**

---

## THE TIMELINE

### Tuesday May 26 — LAUNCH DAY (90-min morning sprint)
*Covered in detail in `outputs/donna/may26_week_priority_stack_2026-05-24.md`*

Key actions for deliverability:
- [ ] Run `check_replies.py` at 10am — last call for Round 1 replies
- [ ] Confirm `INSTANTLY_PAUSED=true` in `.env` — if not done over Memorial Day, do it NOW
- [ ] Google Ads launch (Rick's `outputs/rick/google_ads_first_week_monitoring_guide_2026-05-24.md`)
- [ ] Facebook Ads launch (Rick's `outputs/rick/facebook_lead_gen_launch_checklist_2026-05-24.md`)
- [ ] Send Tier 1 contractor texts (8:45am — `outputs/vera/memorial_day_contractor_text_card_2026-05-24.md`)
- [ ] Send 5 past customer re-engagement texts (`outputs/tommy/past_customer_june_text_scripts_2026-05-24.md`)

**Deliverability note:** Day 1 of Instantly.ai pause recovery begins today (if paused). 9 days to June 4.

---

### Wednesday May 27 — Bridge Email Day

*This is the most leveraged action in the 9-day window.*

Who to email: Your 5–10 hottest contacts (2+ Mixmax opens, no reply). Send from **personal Gmail — not Mixmax, not Instantly.**

Why: Personal email bypasses spam filters completely. Subject line is your name + a direct question. No sequence header, no unsubscribe footer. These people already engaged — they just didn't reply.

**Bridge email exists:** `outputs/tommy/hot_lead_bridge_email_may26_2026-05-22.md` — copy the template, personalize with company name, send.

- [ ] Send bridge emails to top 5 contacts (30 min)
- [ ] Log each email sent in `pipeline_data.json` as last_contact = today
- [ ] Check ads: did any leads come in yesterday? (Rick's Day 1 check)

**Deliverability note:** Day 2 of pause recovery.

---

### Thursday May 28 — Monitor + Respond

- [ ] Check Gmail for bridge email replies — respond SAME HOUR for any reply
- [ ] Check Facebook Lead Gen form — any leads from yesterday? Use `outputs/rick/facebook_lead_response_sop_2026-05-24.md` for response
- [ ] Check Google Ads CTR — is it > 1.5%? If not, check which keywords are spending (Day 3 monitor from Rick's guide)
- [ ] Nothing new to start — let bridge emails and ads do their job today

---

### Friday May 29 — Summit County Lead Pull (DEADLINE)

This is your last weekday before the Summit County deadline (May 31).

- [ ] Run Summit County lead pull: double-click `scripts/run_summit_pull.command` **OR** `python3 workers/lead_pipeline.py danny Summit`
- [ ] Run Carla Summit at the same time: `scripts/run_summit_both.command` runs both together
- [ ] Review output file in `outputs/danny/` — confirm leads have email + phone populated
- [ ] Check ads: any Facebook leads? Day 4 optimization check.

**Enrollment note:** These Summit County PMs will be in the June 4 enrollment batch. The pull MUST happen before June 4.

---

### Saturday–Sunday May 30–31 — Light Touch

- [ ] Check Gmail for any late bridge email replies (last call — 3-day window)
- [ ] Post GBP update using June content calendar (`outputs/vera/june_gbp_content_calendar_2026-05-24.md` — June 2 post)
- [ ] If Summit pull didn't happen Friday, do it Saturday May 30 — last day before Week 22

---

### Monday June 2 — Medina County Pull + Week 1 Sprint Launch

*Covered in `outputs/donna/june_week1_sprint_2026-05-24.md`*

- [ ] Run Medina County pull: double-click `scripts/run_medina_both.command`
  — OR: `python3 workers/lead_pipeline.py danny Medina` + `python3 workers/lead_pipeline.py carla Medina`
- [ ] Service pages live check — website ready before ads continue spending? (`outputs/tommy/website_copy_service_pages_2026-05-20.md`)
- [ ] Post June 2 GBP update (from June content calendar)
- [ ] Check Facebook Ads Week 1 tracker (`outputs/rick/facebook_ad_week1_revenue_tracker_2026-05-24.md`) — fill in Day 7 metrics

**Deliverability note:** Day 7 of Instantly.ai pause recovery. Minimum viable. Day 8+ is better.

---

### Tuesday June 3 — READINESS CHECKLIST NIGHT

Do this Tuesday evening before June 4 enrollment morning.

Run `outputs/donna/round2_enrollment_readiness_checklist_2026-05-23.md` — the full GO/NO-GO check.

**Minimum requirements to proceed with enrollment June 4:**
- [ ] `INSTANTLY_PAUSED=true` in `.env` — confirmed
- [ ] New PM email copy in Mixmax (VOC-rewritten Touch 1) — `outputs/tommy/round2_pm_sequence_voc_rewrite_2026-05-23.md`
- [ ] Fresh Apollo leads pulled (Summit + Medina) — files exist in `outputs/danny/`
- [ ] Gas station Mixmax sequence ID added to `integrations/mixmax.py` — OR: skip and enroll separately
- [ ] `contacts_cache.json` has no malformed data (quick sanity check: `python3 -c "import json; json.load(open('contacts_cache.json'))"`)

If any block is NO-GO → fix tonight OR delay enrollment by 24 hours. Do NOT enroll into a broken setup.

---

### Wednesday June 4 — ENROLLMENT DAY

Follow the press-GO execution card: `outputs/donna/june4_enrollment_battle_card_2026-05-24.md`

The exact commands are in that doc. This warmup timeline is what gets you to June 4 with everything in place.

Expected output:
- 30–60 fresh PMs enrolled (Summit + Medina pulls)
- 18 gas station contacts enrolled (if sequence ID is live)
- Contractor sequence VOC-rewritten and running on existing contacts
- Realtor sequence running

---

## CRITICAL PATH SUMMARY

```
May 26 → Pause Instantly confirmed + Bridge emails sent + Ads launch
May 27 → Bridge emails land in inboxes (personal Gmail, no spam)
May 29 → Summit County pull (Danny + Carla)
May 30–31 → Late reply window close; GBP post
June 1  → Medina County pull (Danny + Carla)
June 2  → Week 1 sprint; ads check; service pages
June 3  → Readiness checklist — GO/NO-GO
June 4  → Round 2 enrollment — PRESS GO
```

**If Instantly.ai is NOT paused by May 26:** Round 2 deliverability is at serious risk. 9 days of recovery is the minimum. 8 days (pause May 27) is borderline. 7 days or fewer = high spam risk on June 4. Pause first, everything else second.

---

*Donna Park | Forest City Power Washing AI Office*
*Round 2 prep timeline — May 26–June 3 | Generated: 2026-05-26*
