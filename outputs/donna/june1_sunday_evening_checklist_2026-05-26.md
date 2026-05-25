# June 1 Sunday Evening Checklist
## The Night Before Medina County Pull + 3 Days Before Round 2 Enrollment
*Donna Park | Forest City Power Washing | 2026-05-26*

**When:** Sunday June 1 at 8–9pm (before you close your laptop for the night)
**Time required:** 15 minutes
**Purpose:** Make sure Monday June 2 starts clean and June 4 enrollment is on track.

---

## STEP 1 — Confirm Instantly.ai Is Still Paused (2 minutes)
[ ] Go to app.instantly.ai → Campaigns
[ ] Verify campaign a1c08c3d (PM Cuyahoga) shows "Paused" status
[ ] Verify campaign 626cd15d (Contractor Referral) shows "Paused" status
[ ] Confirm `INSTANTLY_PAUSED=true` is in your .env file: `grep INSTANTLY_PAUSED /Users/bradleyneal/forestcity/.env`
- ✅ Both paused + flag in .env → June 4 enrollment is mechanically unblocked
- ❌ Still running → Pause NOW. 3 days left. See: `outputs/vera/instantly_pause_guide_2026-05-22.md`

---

## STEP 2 — Confirm Summit County Pull Done (1 minute)
[ ] Run: `grep "Summit" /Users/bradleyneal/forestcity/logs/activity.log | tail -5`
- ✅ Shows Danny | Summit County pull line → Medina is next (tomorrow morning)
- ❌ Not there → Run it TONIGHT or first thing tomorrow: `python3 workers/lead_pipeline.py danny Summit`
  - Double-click shortcut also works: `scripts/run_summit_pull.command`
  - Summit deadline was May 31. If it's not done, do it before Medina.

---

## STEP 3 — Queue Tomorrow's Medina Pull (1 minute)
[ ] Find `scripts/run_medina_both.command` in Finder (Danny + Carla together)
[ ] Move it to your Desktop or keep it visible for Monday morning
[ ] First task Monday June 2: double-click that command before doing anything else. It takes 6 minutes unattended.
- Why: Fresh Medina leads + Carla's Medina contractor list = ready for June 4 enrollment. If you run it Monday, the contacts cache has 3 full days to confirm before enrollment.

---

## STEP 4 — Verify Gas Station Path (2 minutes)
[ ] Option A (if you created the Mixmax gas station sequence): `grep "gas_station" /Users/bradleyneal/forestcity/integrations/mixmax.py | grep -v PENDING`
  - If it shows a real sequence ID (not PENDING) → gas station contacts will auto-enroll via `lead_pipeline.py pending` on June 4 ✅
[ ] Option B (if Mixmax sequence still not created): Check `outputs/danny/gas_station_manual_email_blast_2026-05-25.md` — Tier 1 + Tier 2 blast may already be done. Verify.
[ ] Either way, 18 gas station contacts should be contacted before June 4. Verify status.

---

## STEP 5 — Read the June 4 Enrollment Readiness Checklist (3 minutes)
[ ] Open: `outputs/donna/round2_enrollment_readiness_checklist_2026-05-23.md`
[ ] Score each item GO / NO-GO
[ ] As of tonight:
  - Instantly.ai paused = ✅ or ❌ (see Step 1)
  - New VOC-rewritten PM email copy in Mixmax = should be there (Tommy wrote `round2_pm_sequence_voc_rewrite_2026-05-23.md` with full 3-touch rewrite)
  - Fresh Summit County leads in cache = ✅ if Step 2 done
  - Fresh Medina leads = tomorrow morning's job
  - Gas station sequence = see Step 4
[ ] If any item is NO-GO, add to Monday morning task list

---

## STEP 6 — Quick Bridge Email Check (2 minutes)
[ ] Did you send bridge emails to top hot leads last week? (Tommy's `hot_lead_bridge_email_2026-05-20.md`)
[ ] If you got any replies → add to pipeline_data.json with new stage + notes
[ ] Any unanswered replies from ads leads this week → respond before Monday 9am

---

## STEP 7 — Confirm June 4 Battle Card Is Ready to Go (1 minute)
[ ] Open: `outputs/donna/june4_enrollment_battle_card_2026-05-24.md`
[ ] Read through once so Tuesday morning is just execution, no thinking
[ ] Set a calendar reminder for Tuesday June 4 at 8am: "Enrollment Day — run battle card"

---

## Sunday Night Green Light Criteria

If all of these are true, you're in good shape for the week:
- ✅ Instantly.ai paused + INSTANTLY_PAUSED=true in .env
- ✅ Summit County pull logged in activity.log
- ✅ Medina pull shortcut ready for Monday morning
- ✅ Gas station contacts contacted (either Mixmax or Gmail blast)
- ✅ June 4 battle card reviewed

If any are missing → note them for Monday morning. Don't leave Sunday without knowing what's blocking.

---

## What Happens After This Week

| Date | Action | Who |
|------|--------|-----|
| Mon June 2 | Medina County pull (Danny + Carla) | run_medina_both.command |
| Mon June 2 | Nina weekly report | python3 workers/nina_report.py weekly |
| Tue June 3 | Enrollment readiness final check | Danny's round2_enrollment_readiness_checklist |
| Wed June 4 | ROUND 2 ENROLLMENT DAY | june4_enrollment_battle_card |
| Wed June 4 | Past customer text blast (10 contacts) | Tommy's past_customer_june_text_scripts |
| Wed June 4 | Carla activation card | june4_carla_activation_card |

---

*Donna Park | Forest City Power Washing | Saved: outputs/donna/june1_sunday_evening_checklist_2026-05-26.md*
