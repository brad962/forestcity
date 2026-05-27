# June 4 Enrollment Readiness Tracker
### Live Status — Check This Any Time Between Now and June 4
*Vera Cole — Run 109 | Last updated: 2026-05-27*

---

## GO / NO-GO DASHBOARD

Check this card every morning. Update the status column as blockers clear.

| # | Blocker / Requirement | Status | Who | How to Clear |
|---|----------------------|--------|-----|--------------|
| 1 | **Instantly.ai paused** | 🔴 NOT DONE | Bradley | app.instantly.ai → Campaigns → Pause a1c08c3d + 626cd15d → add `INSTANTLY_PAUSED=true` to .env |
| 2 | **Summit County pull complete** | 🔴 NOT DONE | Bradley | Double-click `scripts/run_summit_pull.command` — DEADLINE MAY 31 |
| 3 | **Medina County pull complete** | ⏳ SCHEDULED | System | Runs June 1 (week 22 rotation) — just run `scripts/run_medina_pull.command` June 1 morning |
| 4 | **Gas Station Mixmax sequence created** | 🔴 PENDING | Bradley | Follow `outputs/danny/gas_station_sequence_create_now_2026-05-27.md` — 30 min |
| 5 | **Wave 2 contractor texts sent (May 28)** | ⏳ TOMORROW | Bradley | `wave2_contractor_blitz_may28_2026-05-27.md` — 45 min |
| 6 | **Round 2 email copy in Mixmax** | 🟡 PARTIAL | Bradley | Sequence already exists, verify subject lines refreshed before June 4 |
| 7 | **Past customer blast sent** | 🔴 NOT DONE | Bradley | `outputs/tommy/past_customer_june_blast_2026-05-27.md` — 30 min, DO TODAY |
| 8 | **pipeline_data.json contacts updated** | 🟡 PARTIAL | Bradley | After each text/call, run `python3 scripts/contact_done.py` |

---

## WHAT EACH BLOCKER MEANS IF MISSED

**1 — Instantly.ai not paused by June 4:**
> Contacts in Round 2 batch also received Instantly.ai emails in Round 1. If Instantly is still running, they get a second email sequence from a different email address the same week. Two cold email sequences = spam filter trigger = 0% reply rate on BOTH. This is the single highest-risk blocker.

**2 — Summit County pull not done by May 31:**
> Summit County next comes up in the 6-county rotation on July 6 (week 27). That's 5 weeks after June 4 — meaning all the new commercial segments (restaurants, banks, gyms, medical offices, distribution centers) miss Summit County entirely for peak season. Summit has strong commercial density (Akron metro). Missing it = smaller Round 2 batch.

**3 — Medina pull not run June 1:**
> Medina is the week 22 county. If missed, it falls back to June 8 (week 23 = Geauga/Portage, next Medina is week 28 = July 13). June 1 Medina pull is your biggest single-day lead event of the season — all 20+ new segments pulling simultaneously for the first time.

**4 — Gas Station sequence still PENDING:**
> 12 contacts are waiting and have been since May 19. They cannot receive any Mixmax outreach until the sequence is created and the ID is pasted into integrations/mixmax.py line 54. Every day that passes = another day these contacts drift colder.

**7 — Past customer blast not sent:**
> This is the fastest revenue of the week — $1,800–$3,000 in 30 minutes. Ads are in learning phase. Past customers trust you already. Zero acquisition cost. Send this TODAY before anything else.

---

## ENROLLMENT DAY CHECKLIST (June 4 Morning)

Run through this in order:

```
[ ] 1. Confirm Instantly.ai is paused — check app.instantly.ai
[ ] 2. Confirm INSTANTLY_PAUSED=true is in .env
[ ] 3. Confirm Medina pull ran June 1 — check logs/activity.log
[ ] 4. Confirm Summit pull ran — check logs/activity.log
[ ] 5. Review new contacts from June 1 Medina pull
[ ] 6. Review new contacts from Summit pull
[ ] 7. Run enrollment: python3 workers/lead_pipeline.py both
[ ] 8. Watch terminal output for any BLOCKED or PENDING warnings
[ ] 9. Open Nina's daily report to confirm enrollment counts
```

---

## BATCH SIZING ESTIMATE

Based on what we expect from pending county pulls:

| Source | Estimated New Contacts | Notes |
|--------|----------------------|-------|
| Summit County pull | 30–80 | 20+ new segments in search for first time |
| Medina June 1 pull | 30–80 | Same — first time all new segments run |
| Pending (existing cache) | 0 | All previously pulled contacts already enrolled |
| **Total Round 2 batch** | **60–160 contacts** | |

*Previous Round 1 (Cuyahoga, May 12) pulled ~50 property managers. Round 2 will be larger due to new commercial segments.*

---

## REVENUE PROJECTION

| Scenario | Batch Size | Open Rate | Replies | Close Rate | Jobs | Avg Ticket | Revenue |
|----------|-----------|-----------|---------|------------|------|-----------|---------|
| Conservative | 60 | 35% | 5% (3) | 50% | 1–2 | $450 | $450–$900 |
| Realistic | 100 | 42% | 8% (8) | 60% | 5 | $500 | $2,500 |
| Strong | 150 | 45% | 10% (15) | 70% | 10 | $600 | $6,000 |
| Best case (commercial FM) | 150 | 45% | 10% (15) | 70% | 3 commercial + 7 residential | $1,200 avg | $18,000 |

*Commercial FM (restaurant, bank, distribution) accounts skew ticket significantly higher.*

---

## BLOCKERS DASHBOARD KEY
- 🟢 **DONE** — cleared, no action needed
- 🟡 **PARTIAL** — in progress or needs verification
- ⏳ **SCHEDULED** — planned, date is set
- 🔴 **NOT DONE** — requires Bradley action before June 4

---

*Update this tracker daily. When a 🔴 turns 🟢, you're one step closer to GO.*
*Vera Cole | Run 109 | 2026-05-27*
