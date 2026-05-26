# June 4 Enrollment — 9-Day Readiness Snapshot
*Vera Cole | Run 92 | 2026-05-26*

---

**You have 9 days until Round 2 enrollment. Here is exactly where things stand.**

---

## ✅ READY — No action needed

| Item | Status | File |
|------|--------|------|
| PM sequence (VOC-rewritten) | READY | `outputs/tommy/round2_pm_sequence_voc_rewrite_2026-05-23.md` |
| Contractor sequence (VOC-rewritten) | READY | `outputs/carla/contractor_referral_sequence_voc_rewrite_2026-05-23.md` |
| June 4 press-GO battle card (Danny) | READY | `outputs/donna/june4_enrollment_battle_card_2026-05-24.md` |
| June 4 press-GO card (Carla) | READY | `outputs/carla/june4_carla_activation_card_2026-05-25.md` |
| Medina County pull shortcut | READY | `scripts/run_medina_both.command` |
| Round 2 enrollment readiness checklist | READY | `outputs/donna/round2_enrollment_readiness_checklist_2026-05-23.md` |
| Past customer June texts | READY | `outputs/tommy/past_customer_june_text_scripts_2026-05-24.md` |
| Enrollment code block (prevents accidental send) | LIVE | `integrations/mixmax.py` — enroll_batch() aborts if not paused |

---

## 🔴 BLOCKERS — Bradley action required

### 1. Instantly.ai — NOT CONFIRMED PAUSED
**Risk:** Every day Instantly campaigns a1c08c3d + 626cd15d stay active = domain reputation damage.
**Deliverability math:**
- Pause today (May 26) = 9 days recovery = minimum viable ✓
- Pause May 28 = 7 days = borderline risk 
- Pause May 31+ = under 6 days = HIGH risk June 4 lands in spam again

**Action (3 minutes):**
1. Go to `app.instantly.ai` → Campaigns
2. Find `a1c08c3d` (PM Cuyahoga) → ⋮ → Pause
3. Find `626cd15d` (Contractor Referral) → ⋮ → Pause
4. Add `INSTANTLY_PAUSED=true` to your `.env` file

**Verification:** `grep INSTANTLY_PAUSED .env` — should return `INSTANTLY_PAUSED=true`

---

### 2. Summit County Pull — OVERDUE (deadline May 31)
**Risk:** No fresh Summit leads for June 4 enrollment batch.
**Days left:** 5

**Action (6 minutes, unattended):**
- Double-click `scripts/run_summit_pull.command` in Finder
- OR: `python3 workers/lead_pipeline.py danny Summit`

**Best remaining window:** Today or tomorrow. After Wednesday, Summit pull is still possible but margins are tight before the June 1 Medina pull.

---

### 3. Gas Station Mixmax Sequence — PENDING (18 contacts idle)
**Risk:** 18 gas station DM contacts have been pulled for 7 days with no enrollment.
**Two paths — pick one:**

**Path A (faster, no new tools):** Gmail blast using `outputs/danny/gas_station_manual_email_blast_2026-05-25.md`
- Wave 1 (7 Tier 1 contacts): send today
- Wave 2 (11 contacts): send Thursday May 28
- Time: 20 minutes

**Path B (automated, permanent):** Create Mixmax sequence
- Guide: `outputs/danny/gas_station_mixmax_sequence_creation_2026-05-23.md`
- After creating, run: `python3 workers/lead_pipeline.py pending`
- Time: 10 minutes

---

### 4. Contractor Tier 1 — 8+ Days "New Lead"
**5 Tier 1 contractors with no personal outreach in 8+ days:**
- Anthony / Land Pro Management — 440-320-2779
- Dontez / GTP Landscaping — 440-396-0814
- Chris / Twin Improvements — 216-773-0757
- Venus / Reliable Roofing — 216-810-2497
- Logan / Pagels Quality Construction — 216-956-5263

**Action (15 minutes):** `outputs/vera/launch_day_contractor_outreach_stack_2026-05-26.md`
Scripts + overdue Contacted follow-ups all in one place.

---

## 📅 9-Day Countdown Calendar

| Day | Date | Action |
|-----|------|--------|
| Day 1 (TODAY) | May 26 | Pause Instantly.ai. Run Summit pull. Send gas station Wave 1. |
| Day 2 | May 27 | Gas station Wave 1 follow-up if no reply. Contractor texts. GBP Post 2. |
| Day 3 | May 28 | Day 3 ad check (`day3_ads_check_card_2026-05-26.md`). Gas station Wave 2. |
| Day 4–5 | May 29–30 | Monitor ads. Check replies. GBP posts. |
| Day 6 | May 31 | **SUMMIT PULL DEADLINE.** Run if not already done. GBP Post 5. |
| Day 7 | June 1 | Medina County pull (double-click `run_medina_both.command`). |
| Day 8 | June 2 | Bridge emails to hot leads. Monitor Medina enrollment list. |
| Day 9 (eve) | June 3 | Run `round2_enrollment_readiness_checklist_2026-05-23.md`. GO/NO-GO decision. |
| Day 10 | **June 4** | Press GO: `june4_enrollment_battle_card_2026-05-24.md` + Carla card + past customer blast. |

---

## Revenue on the table at June 4

| Source | Contacts | Projected Pipeline |
|--------|----------|--------------------|
| PM sequence (Round 2, VOC copy) | 45+ enrolled | $15,000–$50,000 |
| Contractor referral (VOC copy) | 20+ enrolled | $10,000–$30,000 |
| Gas station sequence | 18 idle | $18,000–$36,000 |
| Past customer blast | Est. 30 contacts | $4,000–$8,000 |
| Medina fresh pull | Est. 25 new leads | $8,000–$20,000 |

**Total potential pipeline unlocked June 4: $55,000–$144,000**

---

*Status accurate as of May 26 Run 92. Update this when Instantly.ai is confirmed paused.*
