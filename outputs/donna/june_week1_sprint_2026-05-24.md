# June Week 1 Sprint — Day-by-Day Action Plan
*Donna Park | Growth & Launch Strategist*
*Written: 2026-05-24 (refreshed from May 20 version with all current context)*

**June 2–6 (Mon–Fri) — The Week Round 2 Launches**

---

## Pre-Week Prerequisites (Check by June 3 Night)

Use `outputs/donna/round2_enrollment_readiness_checklist_2026-05-23.md` as your GO/NO-GO gate.

Quick pre-check (5 min, June 3 evening):
```bash
grep INSTANTLY_PAUSED .env              # should show true
python3 workers/lead_pipeline.py danny Summit   # should confirm pull done by May 31
ls outputs/danny/ | grep summit         # confirm lead file exists
cat integrations/mixmax.py | grep gas_station -A2  # check if gas station ID is still PENDING
```

If Instantly.ai is NOT paused → Round 2 will land in spam. Stop. Pause first.
Then proceed to: `outputs/donna/june4_enrollment_battle_card_2026-05-24.md`

---

## MONDAY June 2

**Total time: ~60 min**

### 8:00am — Medina County Lead Pull (15 min)
It's ISO Week 22 → Medina County in the rotation.
```bash
python3 workers/lead_pipeline.py danny Medina
python3 workers/lead_pipeline.py carla Medina
```
Expected output: `outputs/danny/leads_medina_property_managers_[date].md`

### 8:20am — Nina Weekly Report (5 min)
```bash
python3 workers/nina_report.py weekly
```
Review: How many enrolled? Any replies came in over the weekend?

### 9:00am — GBP Post Week 1 (5 min)
business.google.com/dashboard → Add Update → Paste Week 1 post from `outputs/vera/june_gbp_content_calendar_2026-05-24.md`
Free organic search traffic during peak season.

### 9:10am — Facebook Ads Performance Review (10 min)
Ads launched Tuesday May 26. Now Day 8. Check:
- Cost per lead (target: < $40)
- Are calls coming in? (track in Workiz or a note)
- Add negative keywords if needed → `outputs/rick/google_ads_first_week_monitoring_guide_2026-05-24.md`
- Add negative keywords to Facebook too if getting non-homeowner clicks

### Afternoon — Round 2 Readiness Final Check (15 min)
Work through `outputs/donna/round2_enrollment_readiness_checklist_2026-05-23.md`
Note any red flags before Wednesday enrollment.

---

## TUESDAY June 3

**Total time: ~30 min**

### 8:00am — Pre-Enrollment Go/No-Go (30 min)
This is the night-before check before tomorrow's enrollment.

**6 blocks to confirm:**
- [ ] Instantly.ai paused? (`grep INSTANTLY_PAUSED .env`)
- [ ] New email copy ready? (round2_pm_sequence_voc_rewrite + contractor_referral_sequence_voc_rewrite in Mixmax)
- [ ] Fresh leads pulled? (Summit done by May 31, Medina done Monday June 2)
- [ ] Gas station Mixmax sequence ID updated? (if still PENDING, enroll manually)
- [ ] Bridge emails sent to top 5 hot leads from Round 1?
- [ ] Workiz job booked (or checked) from any Round 1 replies?

If all 6 = ✅ → Enroll tomorrow.
If any = ❌ → Fix tonight or note as known gap.

---

## WEDNESDAY June 4 — ENROLLMENT DAY

**Total time: 90 min**

Use `outputs/donna/june4_enrollment_battle_card_2026-05-24.md` — this is your press-GO card.

### 8:00am — Summit County Enrollment
```bash
python3 workers/lead_pipeline.py danny Summit
```

### 8:20am — Medina + Fresh Leads Enrollment
Enrolls all contacts from June 2 pull who haven't been enrolled yet.

### 9:00am — Pending Sequence Enrollment
```bash
python3 workers/lead_pipeline.py pending
```
Enrolls gas station contacts IF their Mixmax sequence ID was added.

### 10:00am — Past Customer Text Blast
Open `outputs/tommy/past_customer_june_text_scripts_2026-05-24.md`
Send 10 texts to past customers from Workiz. Takes 15 min.
Expected yield: 2–4 responses → $1,200–$4,000 in bookings.

### 10:20am — GBP Week 2 Post (5 min)
Post Week 2 from `outputs/vera/june_gbp_content_calendar_2026-05-24.md`

### Revenue math for June 4:
- 50 PM contacts enrolled in Round 2 → 3–5 expected replies ($2,100–$3,500/job avg)
- 10 past customer texts → 2–4 responses ($350–$600 each)
- Ads running Day 9 → 2–4 leads ($700–$2,400 if closed)
- **Total June 4 pipeline activation: $4,000–$10,000 potential**

---

## THURSDAY June 5

**Total time: ~30 min**

### 8:45am — check_replies.py
```bash
python3 workers/check_replies.py
```
Round 2 Touch 1 sent yesterday. Anyone open-notified or replied today?

### 9:00am — Past Customer Follow-up
Any responses from Wednesday's texts? Reply same-day using:
`outputs/tommy/hot_lead_callback_script_2026-05-24.md` (for warm inbounds)

### 9:15am — LinkedIn Connects
Check Nina hot leads report. Any 2+ opens from PM sequence?
Connect on LinkedIn using `outputs/danny/linkedin_hot_lead_dm_protocol_[date].md`

### Ad performance (5 min)
Check Facebook + Google Ads Day 10:
- Cost per lead trending?
- Budget pacing correctly?

---

## FRIDAY June 6

**Total time: ~30 min**

### 8:30am — Week 1 Revenue Review
Fill in `outputs/rick/facebook_ad_week1_revenue_tracker_2026-05-24.md` → Day 14 column
(Ads launched May 26 → June 6 = Day 12)

Questions to answer:
- How many ad leads came in?
- How many quotes sent?
- How many jobs booked?
- Cost per booking?

### 9:00am — Workiz Report
```bash
python3 workers/workiz_report.py daily
```
See jobs scheduled for June. Revenue pipeline visible.

### 9:15am — Contractor Referral Check
Did any of Carla's contractor referral partners reply or engage?
Check Contractor sequence in Mixmax (or run check_replies.py again).

### Afternoon — GBP Review
Did Week 1 GBP post get views? Check business.google.com/dashboard → Insights.
Post Week 3 content from `outputs/vera/june_gbp_content_calendar_2026-05-24.md`.

---

## Critical Path Summary — June Week 1

| Day | Action | Owner | Must-Complete? |
|-----|--------|-------|---------------|
| Mon June 2 | Medina pull (Danny + Carla) | Bradley | YES — feeds June 4 enrollment |
| Mon June 2 | Nina weekly report | Bradley | YES — see pipeline health |
| Tue June 3 | Enrollment readiness check | Bradley | YES — go/no-go gate |
| Wed June 4 | **Round 2 Enrollment** | Bradley | YES — THE week's anchor action |
| Wed June 4 | Past customer text blast | Bradley | YES — fastest revenue path |
| Thu June 5 | check_replies.py | Bradley | YES — catch early replies |
| Fri June 6 | Week 1 revenue review | Bradley | YES — data-driven next steps |

---

## Revenue Targets — June Week 1

| Channel | Expected | If It Works | Low End |
|---------|----------|-------------|---------|
| Facebook ads (Day 8–14) | 3–6 leads | $1,050–$3,600 | $700 |
| Google ads (Day 8–14) | 2–4 calls | $700–$2,400 | $350 |
| Past customer texts | 2–4 jobs | $700–$2,400 | $350 |
| Round 2 PM enrollment replies | 1–3 replies | $2,100–$6,300 | $0 (replies take 2–5 days) |
| **Week 1 total** | — | **$4,550–$14,700** | **$1,400** |

---

## Files Referenced in This Sprint

| File | Use |
|------|-----|
| `outputs/donna/round2_enrollment_readiness_checklist_2026-05-23.md` | GO/NO-GO gate (June 3) |
| `outputs/donna/june4_enrollment_battle_card_2026-05-24.md` | Enrollment press-GO card |
| `outputs/tommy/past_customer_june_text_scripts_2026-05-24.md` | June 4 text blast scripts |
| `outputs/rick/google_ads_first_week_monitoring_guide_2026-05-24.md` | Google Ads Day 8–14 |
| `outputs/rick/facebook_ad_week1_revenue_tracker_2026-05-24.md` | Week 1 revenue tracking |
| `outputs/vera/june_gbp_content_calendar_2026-05-24.md` | GBP posts all of June |
| `outputs/tommy/hot_lead_callback_script_2026-05-24.md` | Inbound warm lead calls |
| `outputs/tommy/round2_pm_sequence_voc_rewrite_2026-05-23.md` | Round 2 PM email copy |
| `outputs/carla/contractor_referral_sequence_voc_rewrite_2026-05-23.md` | Round 2 contractor copy |

---

*This replaces the May 20 version — fully updated with VOC rewrites, enrollment battle card, and all current context.*
