# Touch 3 Reply Window Tracker
### May 22–26, 2026 — 72-Hour Decision Window
*Vera Cole | Run 52 | 2026-05-22*

---

## The Window: Touch 3 fired May 22. Replies expected by May 25.

Three days. That's the meaningful reply window for a cold email sequence.
After 72 hours, any reply is increasingly unlikely to convert. Act fast on anything that comes in.

**Quick reply check:** `cd /Users/bradleyneal/forestcity && python3 workers/check_replies.py`
Run this every morning May 23–26. Takes 30 seconds. Posts to Slack automatically if replies found.

---

## Day-by-Day Protocol

### Day 0 — Tonight (May 22, evening)
- [ ] Pause Instantly.ai campaigns (`outputs/vera/instantly_pause_guide_2026-05-22.md`) — 3 minutes
- [ ] Verify Mixmax Reply-To is set to Bradley's real email (not a noreply address)
- [ ] Send Tier 1 contractor texts: use scripts in `outputs/tommy/contractor_referral_text_script_2026-05-20.md`
  - Anthony / Land Pro: 440-320-2779
  - Dontez / GTP: 440-396-0814
  - Chris / Twin Improvements: 216-773-0757
  - Venus / Reliable Roofing: 216-810-2497
  - Logan / Pagels: 216-956-5263

### Day 1 — Friday May 23 (morning)
- [ ] Run `python3 workers/check_replies.py` — check for overnight replies
- [ ] If 0 replies: call top opens list per `outputs/tommy/may23_morning_call_protocol_2026-05-22.md`
  - Sort Mixmax by opens (highest first) → call top 5
  - Call window: 9:00–11:30am (highest answer rates)
- [ ] Connect on LinkedIn with anyone who opened 2+ times
  - Use templates: `outputs/tommy/touch3_open_trigger_protocol_2026-05-21.md`
- [ ] Update pipeline_data.json stage for anyone you reach

### Day 2 — Saturday May 24
- [ ] Run `python3 workers/check_replies.py` at 9am — check for delayed replies
- [ ] If any hot lead replied overnight: respond within 1 hour, use templates in `outputs/tommy/touch3_reply_response_templates_2026-05-20.md`
- [ ] LinkedIn passive: accept any connection requests from people in your sequence
- [ ] No active outreach needed today — let it breathe

### Day 3 — Sunday May 25 (decision day)
- [ ] Run `python3 workers/check_replies.py` — final count before Round 2 decision
- [ ] Review the decision gate: `outputs/donna/may25_round2_decision_gate_2026-05-22.md`
  - 0 replies: pause Instantly.ai (if not done), rewrite Email 1 for Round 2 using `outputs/tommy/round2_pm_sequence_rewrite_2026-05-21.md`
  - 1–2 replies: keep sequence, add urgency framing for Round 2
  - 3–5 replies: sequence is working, scale to Summit + Medina counties
  - 6+ replies: scale aggressively, consider adding Lake County to Round 2

### Day 4 — Monday May 26 (Memorial Day blitz)
- [ ] Run `python3 workers/check_replies.py` at 8am sharp
- [ ] Start ads launch: `outputs/vera/may26_ads_launch_checklist_2026-05-22.md`
- [ ] Manual Danny pull (cron still down): `python3 workers/lead_pipeline.py both`
- [ ] Past customer text blast: `outputs/donna/past_customer_reengagement_launch_2026-05-21.md`
- [ ] Full May 26 playbook: `outputs/donna/may26_blitz_action_card.md`

---

## Reply Response Protocol (when someone DOES reply)

**Respond within 60 minutes maximum.** This is the single biggest conversion lever.

Use the correct template from `outputs/tommy/touch3_reply_response_templates_2026-05-20.md`:
- Interested / wants quote → Template A
- Wants more info → Template B
- Soft no → Template C
- Wrong person → Template D
- Already has vendor → Template E
- Contractor/referral confusion → Template F

**After responding:**
1. Update pipeline_data.json stage to "Replied"
2. Set next_followup date (+3 days)
3. Send LinkedIn connection request if not connected
4. Log in activity.log: `[date] Bradley | replied to [name] at [company] | manual | Done`

---

## Metrics to Track

| Date | Check_replies Run | Replies | Hot Leads | Action Taken |
|------|-------------------|---------|-----------|--------------|
| May 22 | — | 0 | — | Touch 3 fired |
| May 23 | ☐ | — | — | Calls if 0 |
| May 24 | ☐ | — | — | LinkedIn |
| May 25 | ☐ | — | — | Decision gate |
| May 26 | ☐ | — | — | Blitz day |

---

## Round 2 Enrollment Target: June 4

If reply rate stays at 0%:
1. Pause Instantly.ai (3 min) — eliminates the #1 suspected cause of spam filtering
2. Rewrite Email 1 (copy is ready — just choose version from round2_pm_sequence_rewrite)
3. Enroll Summit + Medina county leads (requires Danny cron to run by June 2)
4. Change send time to 10:30am (current: unknown — check Mixmax sequence settings)

Full plan: `outputs/donna/round2_enrollment_plan_2026-05-21.md`

---

*Generated: 2026-05-22 | Next check: May 23 9am*
