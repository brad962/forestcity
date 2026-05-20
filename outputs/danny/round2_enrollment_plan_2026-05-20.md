# Round 2 Enrollment Plan — After Touch 3
### Danny Malone | Outbound Sales Rep
*Created 2026-05-20 — for execution starting June 4, 2026*

---

## Status: Where We Are

- **Round 1:** 45 contacts enrolled (Cuyahoga + Lorain counties, pulled May 12–13)
- **Touch 3 fires:** May 22, 2026 — final email in the sequence
- **Results:** 42% open rate, 0 replies (through Touch 2)
- **After Touch 3:** Round 1 contacts remain in sequence but no more automated emails. Personal outreach takes over.

---

## Round 2 Timeline

| Date | Action |
|------|--------|
| May 22 | Touch 3 fires — sequence complete for Round 1 |
| May 22–25 | Monitor for replies. Respond same-day using `outputs/tommy/touch3_reply_response_templates_2026-05-20.md` |
| May 26–June 3 | **Cooling period** — 2 weeks minimum between sequence touches for same contacts. Don't re-enroll Round 1 contacts yet. |
| June 2 | Run `python3 workers/lead_pipeline.py danny` — pulls **Summit County** batch (~15–25 new PMs). Auto-enrolls in Mixmax. |
| June 4–7 | **Round 2 enrollment window.** Enroll Summit County PMs in the REWRITTEN sequence (see below). |
| June 9 | Run **Medina County** pull (next in rotation after Summit). |
| June 16 | Run **Geauga + Portage County** pull. |
| ~June 23 | Re-enroll Round 1 contacts (Cuyahoga + Lorain) in the rewritten sequence IF no reply yet. |

---

## The Rewrite: What Changes for Round 2

The current sequence has 42% open rate but 0 replies. Opens prove delivery works. Body copy is the issue.

Approved changes waiting: `outputs/danny/pm_sequence_touch1_rewrite_2026-05-19.md`

**Key changes:**
- Touch 1: 62-word body max (down from ~120 words). Single CTA: "15-minute call or reply with a photo."
- Touch 2: Subject line starts with "Re:" — leverages threaded email psychology. Body references Touch 1.
- Touch 3: NEW — add a specific local proof point (county + job type). "We wrapped up a 3-building job for a PM in [County] last week."
- All touches: Lake/humidity angle, not generic "your property looks dirty."

**Action needed from Bradley:**
1. Review `outputs/danny/pm_sequence_touch1_rewrite_2026-05-19.md`
2. Log into Mixmax → Property Manager sequence → Edit each stage body
3. Reply YES to Vera's Slack proposal to confirm approval

---

## What Counties Haven't Been Hit Yet

| County | Status | Recommended Pull Date |
|--------|--------|-----------------------|
| Cuyahoga | ✅ Done (May 12) — Round 1 |  |
| Lorain | ✅ Done (May 13) — Round 1 |  |
| Lake | 🟡 Not done since May 2026 | June 2 (after Summit) |
| **Summit** | 🔴 OVERDUE — was scheduled Week 21 (May 13–19) | **TODAY — run locally** |
| Medina | 🔴 Not done | June 9 |
| Geauga + Portage | 🔴 Not done | June 16 |

**Summit County should have run last week.** This is the Akron/Fairlawn/Stow market — a major commercial real estate and HOA cluster. Running the pipeline TODAY pulls 15–25 new Summit County PMs.

---

## Gas Station Round 2 (Depends on Mixmax ID)

18 gas station contacts (Certified Oil, truenorth, etc.) have been in the pipeline since May 19 with no sequence. Once Bradley creates the Mixmax sequence:

1. Mixmax → New Sequence → paste copy from `outputs/danny/sequence_gas_stations_2026-05-19.md`
2. Copy the new sequence ID
3. Open `integrations/mixmax.py` → line 54 → replace `'PENDING'` with the ID
4. Run `python3 workers/lead_pipeline.py danny` — all 18 auto-enroll

Best window: **Before Memorial Day.** "Stations are thinking about their summer appearance" angle.

---

## Fleet Washing Round 1 (Also Depends on Mixmax ID)

Fleet washing sequence copy is ready since May 18 (`outputs/danny/sequence_fleet_washing_2026-05-18.md`). Same steps as gas station. High-value: one account = 5–15 vehicles, recurring monthly revenue.

---

## Immediate Action Items

1. **TODAY (May 20):** Run `python3 workers/lead_pipeline.py danny` locally — pulls Summit County PMs
2. **Before May 24:** Create gas station Mixmax sequence → paste ID into mixmax.py line 54
3. **Before May 24:** Create fleet washing Mixmax sequence → paste ID into mixmax.py line 48
4. **May 22 (Touch 3 day):** Monitor Mixmax for replies all day
5. **June 2:** Run lead pipeline again — Lake + Medina County

---

*Danny Malone | Forest City Power Washing | 2026-05-20*
