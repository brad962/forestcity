# Round 2 Enrollment Readiness Checklist
### Run this on Monday June 3 — the day before Round 2 enrollment (June 4)
*Donna Park | Growth & Launch Strategist*

---

## The Goal
Enroll 20–40 fresh contacts into the PM sequence on June 4 with a rewritten Email 1 and the Instantly.ai overlap fixed. This is the second shot at the ~45 contacts who got 0 replies in Round 1.

---

## GO / NO-GO Checklist

Run through every item. If any item is NO, fix it before enrolling.

---

### ✅ Block 1 — Spam Fix (Required before ANY Round 2 enrollment)

| Check | Status | Notes |
|-------|--------|-------|
| **Instantly.ai campaigns a1c08c3d AND 626cd15d are PAUSED** | ☐ | app.instantly.ai → Campaigns → Status. Both must say Paused, not Active. |
| **Wait 48 hours after pausing before enrolling** | ☐ | Pausing on Monday = enroll Wednesday June 4. If paused earlier, you're clear. |
| **No other cold email platforms hitting the same contacts** | ☐ | Only Mixmax should be sending to your PM contact list. |

> 🔴 If Instantly is still ACTIVE, do not enroll. The overlap is confirmed as the #1 cause of 0% reply rate. Enrolling while it's active wastes all new contacts.

---

### ✅ Block 2 — New Email Copy Ready

| Check | Status | Notes |
|-------|--------|-------|
| **New Email 1 copy selected** | ☐ | Choose from `outputs/tommy/round2_pm_sequence_rewrite_2026-05-20.md` — pick Social Proof, Fear/Urgency, or Direct Question variant |
| **Email 1 updated in Mixmax sequence** | ☐ | Log in to Mixmax → Sequences → Property Managers → Edit Step 1. Paste new copy. Save. |
| **Subject line A/B set up** | ☐ | Pick 1 of the 5 pairs from `outputs/tommy/email_subject_line_ab_test_2026-05-22.md` and update the sequence subject line |

---

### ✅ Block 3 — Fresh Leads Ready

| Check | Status | Notes |
|-------|--------|-------|
| **Summit County pull completed by May 31** | ☐ | `python3 workers/lead_pipeline.py danny Summit` — or double-click `scripts/run_summit_pull.command` |
| **June 1 Medina County pull completed** | ☐ | `python3 workers/lead_pipeline.py danny` (runs automatically if cron is live, or run manually) |
| **New leads NOT already enrolled in Round 1 batch** | ☐ | lead_pipeline.py deduplicates against contacts_cache.json automatically — you're covered |

---

### ✅ Block 4 — Gas Station Sequence Live (Bonus — unlocks 18 idle contacts)

| Check | Status | Notes |
|-------|--------|-------|
| **Gas Station sequence created in Mixmax UI** | ☐ | Full guide: `outputs/danny/gas_station_mixmax_sequence_creation_2026-05-23.md`. 10 minutes. |
| **Gas Station sequence ID pasted into integrations/mixmax.py line 54** | ☐ | Replace 'PENDING' with the real ID from the Mixmax sequence URL |
| **Pending enrollment run** | ☐ | `python3 workers/lead_pipeline.py pending` — enrolls all 18 gas station contacts instantly |

---

### ✅ Block 5 — Hot Lead Follow-Up Done First (Don't Enroll Over Active Convos)

| Check | Status | Notes |
|-------|--------|-------|
| **Bridge emails sent to top 5 hot leads (2+ opens)** | ☐ | Templates: `outputs/tommy/hot_lead_bridge_email_may26_2026-05-22.md`. Send from personal Gmail. |
| **LinkedIn connects accepted / DMs sent** | ☐ | Connect with all 2+ open contacts. Send DM after acceptance. |
| **Any REPLIES responded to personally** | ☐ | Replies are closed won opportunities — respond before enrolling anyone new |

---

## Round 2 Enrollment — Day-of Execution (June 4, Tuesday)

```
8:00am — Run check_replies.py one final time before enrolling
          python3 workers/check_replies.py

8:15am — Run lead pipeline for fresh contacts
          python3 workers/lead_pipeline.py both

9:00am — Verify enrollment in Mixmax
          Log in → Sequences → check recipient counts increased

9:15am — Run pending sequences (gas station)
          python3 workers/lead_pipeline.py pending

9:30am — Done. Mark on calendar: Round 2 reply window opens June 11.
```

---

## Round 2 Reply Window (June 4–11)

Run check_replies.py each morning at 8:45am:
```
python3 workers/check_replies.py
```

Or rely on the crontab if it's set up (`crontab -l` to verify).

---

## Revenue Math

| Scenario | Outcome |
|----------|---------|
| 40 contacts enrolled, 5% reply rate | 2 replies = 1 booked job = ~$800 |
| 40 contacts enrolled, 10% reply rate | 4 replies = 2 jobs = ~$1,600 |
| Gas station sequence live (18 contacts) | 1 district manager = multi-site account, $2,400–$6,000/yr recurring |

> The biggest lever is NOT more contacts. It's fixing the Instantly overlap first. Fix that + new email copy = 5–10% reply rate is realistic.

---

## Files Referenced in This Checklist

| File | Purpose |
|------|---------|
| `outputs/tommy/round2_pm_sequence_rewrite_2026-05-20.md` | 3 new Email 1 variants |
| `outputs/tommy/email_subject_line_ab_test_2026-05-22.md` | 5 A/B subject line pairs |
| `outputs/danny/gas_station_mixmax_sequence_creation_2026-05-23.md` | Step-by-step gas station sequence setup |
| `outputs/tommy/hot_lead_bridge_email_may26_2026-05-22.md` | Personal Gmail bridge emails for top 5 hot leads |
| `outputs/vera/instantly_pause_guide_2026-05-22.md` | How to pause Instantly.ai (3 min) |
| `scripts/run_summit_pull.command` | Double-click to run Summit County pull |

---

*Created by Donna (Vera-assisted) | 2026-05-23*
*Use this checklist on June 3 — one day before Round 2 enrollment.*
