# June 3 — Tuesday Evening Pre-Enrollment Checklist
*Donna Park | Run 100 | 2026-05-26*
*Use this: Tuesday evening June 3, BEFORE bed — 15 minutes*

---

## Context
**Tomorrow is June 4.** Round 2 enrollment launches in the morning.

This is the night-before GO/NO-GO check. If any item is ❌, fix it tonight or enrollment gets delayed.

Pairs with:
- `outputs/donna/round2_enrollment_readiness_checklist_2026-05-23.md` — full readiness checklist
- `outputs/donna/june4_enrollment_battle_card_2026-05-24.md` — tomorrow's press-GO execution card

---

## June 3 Evening Checklist (15 min)

### ✅ Block 1: Instantly.ai Confirmed Paused (2 min)

```bash
grep INSTANTLY_PAUSED /Users/bradleyneal/forestcity/.env
```

Expected output: `INSTANTLY_PAUSED=true`

If NOT there: go to app.instantly.ai → Campaigns → ⋮ → Pause a1c08c3d AND 626cd15d → add to .env **TONIGHT**. Without this, enrollment is blocked and Round 2 emails land in spam.

---

### ✅ Block 2: Medina County Pull Complete (1 min)

Check the log:
```bash
grep -i "medina" /Users/bradleyneal/forestcity/logs/activity.log | tail -5
```

Expected: A Danny pull entry for Medina County from June 1.

If missing: The Medina pull didn't run. Run it NOW tonight:
```bash
cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py danny Medina
```
(Takes 6 min. Worth running tonight rather than scrambling tomorrow morning.)

---

### ✅ Block 3: New Email Copy in Mixmax (3 min)

Log into Mixmax → Sequences → Forest City Power Washing – NE Ohio Property Managers → check that Email 1 subject line uses the VOC-rewritten version from `outputs/tommy/round2_pm_sequence_voc_rewrite_2026-05-23.md`.

If NOT updated: Open that file now and swap the copy in Mixmax. Takes 5 min. Critical — old copy = old results.

---

### ✅ Block 4: Gas Station Sequence or Gmail Blast Path Clear (2 min)

**Option A:** Gas station Mixmax sequence ID is live in `integrations/mixmax.py` (check line 54 — if no longer "PENDING", it's live).

**Option B:** Gmail blast was sent and responses logged. Check sent folder in Gmail for `outputs/danny/gas_station_manual_email_blast_2026-05-25.md` Tier 1 + Tier 2 sends.

If neither: Send the Gmail blast tonight for Tier 1 (7 contacts) — takes 20 min. Do NOT skip — 12 gas station contacts are sitting idle.

---

### ✅ Block 5: Summit County Pull Complete (1 min)

```bash
grep -i "summit" /Users/bradleyneal/forestcity/logs/activity.log | tail -5
```

Expected: Danny pull entry for Summit County from any date May 23–31.

If missing: Summit pull deadline was May 31. If it didn't run, use Medina fresh leads as primary June 4 batch. Note in log.

---

### ✅ Block 6: Set Tomorrow's Alarms (2 min)

Set 2 alarms on your phone:
- **7:30am** — "June 4 enrollment — read battle card"
- **12:00pm** — "June 4 mid-day check — any enrollment errors?"

---

### ✅ Block 7: Read the Battle Card (5 min)

Open and skim:
`outputs/donna/june4_enrollment_battle_card_2026-05-24.md`

Know the order of operations before you sleep. Tomorrow morning you execute — don't plan AND execute at the same time.

---

## GO / NO-GO Summary

| Check | Status | Action if ❌ |
|-------|--------|--------------|
| Instantly paused | ☐ | Pause tonight |
| Medina pull done | ☐ | Run tonight |
| New email copy in Mixmax | ☐ | Swap tonight |
| Gas station path clear | ☐ | Gmail blast tonight |
| Summit pull done | ☐ | Note/accept if missed |
| Alarms set | ☐ | Set before bed |
| Battle card read | ☐ | Read before bed |

**If all ✅: Go to sleep. Tomorrow is June 4. You're ready.**
**If any ❌: Fix it tonight. Morning Bradley will thank you.**

---

## Revenue Math — What's At Stake Tomorrow

| Track | Contacts | Realistic Close Rate | Revenue |
|-------|----------|---------------------|---------|
| Medina PM Round 2 | ~50 fresh leads | 5% | $3,500–$7,500 |
| Gas station blast | 12 contacts | 10% | $2,400–$6,000 |
| Past customer texts | ~20 contacts | 20% | $2,800–$5,600 |
| Contractor texts (21 untouched) | 21 contacts | 10% | $700–$2,100 |
| **Total June 4 pipeline** | | | **$9,400–$21,200** |

*Every $9K missed = roughly one week of peak season revenue.*
