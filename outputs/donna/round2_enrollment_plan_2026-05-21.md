# Round 2 Enrollment Plan — June 4, 2026
### Donna Park | Growth & Launch Strategist
*Written: May 21, 2026 — to be executed based on Touch 3 results (May 22)*

---

## The Setup

Touch 3 fires May 22. Round 2 enrollment target: **June 4** (two weeks out, giving Bradley time to review Touch 3 results and make the sequence refresh decision).

Round 2 is not a restart — it's a second wave of **new contacts** with **one tactical adjustment** (send time) layered in.

---

## What Changes in Round 2 vs. Round 1

| Element | Round 1 | Round 2 |
|---------|---------|---------|
| Send time | 8:00 AM | 10:30 AM |
| Contacts | Cuyahoga + Lake county PMs | Summit + Medina county PMs |
| Sequence | Existing 3-touch | Same (unless Vera rewrite proposal approved) |
| Volume | ~45 enrolled | Target: 25–30 new |
| Subject lines | Current | Add 1 A/B variant if Bradley approves |

**Why 10:30 AM:** Property managers are in morning standup/building walks 8–10am. They read and reply to email 10am–noon. This one change, with no sequence rewrite, typically lifts reply rate 15–25% in B2B home services sequences.

---

## County Targets for Round 2

### Primary: Summit County (Akron/Fairlawn/Stow)
- Week 21 (current week) pull is Summit — **run the cron TONIGHT if possible**
- If cron doesn't run this week, manually trigger:
  ```
  cd ~/forestcity && python3 workers/lead_pipeline.py danny
  ```
- Expect: 15–20 new PM contacts with emails

### Secondary: Medina County (Medina/Brunswick/Wadsworth)
- Week 22 (June 1 week) cron will pull Medina automatically
- Or manually add to this run: edit `DANNY_SEARCHES` index temporarily

### Total target for Round 2: 25–30 new unique contacts enrolled June 4

---

## June 4 Enrollment Checklist

**Monday June 2 (Day 1):**
- [ ] Confirm Summit County leads pulled (check `outputs/danny/` for new file)
- [ ] Verify Mixmax sequence is set to 10:30 AM send time (Settings → Sequences → [Property Manager Sequence] → Schedule)
- [ ] Pull Medina County contacts if Summit < 15 leads

**Tuesday June 3:**
- [ ] Review leads list — remove any obvious non-fits (apartments with <10 units, individual PMs at large national firms)
- [ ] Check contacts_cache.json dedupe worked (no Round 1 contacts re-enrolled)

**Wednesday June 4 (Enrollment Day):**
- [ ] Run `python3 workers/lead_pipeline.py danny` locally
- [ ] Confirm enrollment: Nina's daily report will show new enrolled count
- [ ] Post confirmation in Slack (or check nina's hot_leads report next morning)

---

## Decision Gate: When to Rewrite vs. Keep the Sequence

This decision should be made by **May 25** (before Memorial Day ends):

| Touch 3 Result | Round 2 Action |
|----------------|----------------|
| 2+ replies | Keep sequence as-is. The sequence works — we just need volume. |
| 1 reply | Keep sequence. Small tweak: test new subject line on 50% of Round 2 contacts. |
| 0 replies, some opens | Change send time to 10:30am only. Volume + timing fix. |
| 0 replies, low opens (<25%) | Sequence refresh needed. Vera will rewrite Touch 1 subject + first 2 lines. |

Current status as of May 21: Open rate ≈ 42% but 0 replies across all 3 touches.
→ If Touch 3 = 0 replies: change send time, test new CTA in Touch 1 ("would it make sense to connect?")

---

## The Pipeline Math

| Scenario | Round 2 Contacts | Expected Open Rate | Expected Reply Rate | Expected Leads |
|----------|-----------------|--------------------|---------------------|----------------|
| Optimistic (with send time fix) | 30 | 45% | 4–6% | 1–2 |
| Realistic | 25 | 35% | 2–4% | 1 |
| Conservative | 20 | 30% | 1–2% | 0–1 |

**One PM account = recurring $300–500/visit, 2–3 visits/year, 5–15 properties.** Even one conversion from Round 2 pays for the entire pipeline investment.

---

## Gas Station / Fleet (Parallel Track — also June 4 target)

18 gas station contacts are sitting in contacts_cache.json ready to enroll.
They enroll automatically as soon as the Mixmax sequence ID is added to `integrations/mixmax.py`.

**Action required from Bradley before June 4:**
1. Create gas station sequence in Mixmax UI (copy from `outputs/danny/sequence_gas_stations_2026-05-19.md`)
2. Paste the new sequence ID into `integrations/mixmax.py` line ~47 (replace `'PENDING'`)
3. Running lead_pipeline.py next time will auto-enroll all 18 contacts

Setup guide: `outputs/vera/mixmax_sequence_setup_guide_2026-05-20.md`

---

## Files Referenced
- Touch 3 results → `outputs/nina/hot_leads_2026-05-22.md` (run Nina locally May 22 evening)
- Round 2 sequence setup → `outputs/vera/round2_decision_framework_2026-05-20.md`
- Gas station sequence copy → `outputs/danny/sequence_gas_stations_2026-05-19.md`
- Gas station setup guide → `outputs/vera/mixmax_sequence_setup_guide_2026-05-20.md`
- Mixmax send time change → Mixmax UI: Settings → Sequences → Schedule tab

---

*Donna Park | Growth & Launch Strategist | Generated May 21, 2026*
