# June Week 1 Sprint — Return to Full Velocity
### Donna Park | Growth & Launch Strategist
*Created: 2026-05-20 | Execute: June 2–6, 2026*

---

## Context: What Happened in May

- Touch 3 fired May 22 — automated sequence complete for 45 enrolled PM contacts
- Memorial Day weekend: quiet window (no outreach)
- May 26: Day-after-Memorial-Day blitz (contractor texts, hot lead Gmail)
- **June 2 is the restart button.** Everything that's been queued since May 13 executes this week.

---

## The Week at a Glance

| Day | Primary Task | Time | Revenue Impact |
|-----|-------------|------|----------------|
| Mon June 2 | Summit County Apollo pull + Mixmax sequence setup | 60 min | ~15-20 new leads enrolled |
| Tue June 3 | Review Touch 3 results, tag Round 2 hot list | 30 min | Prioritize who gets personal outreach |
| Wed June 4 | Round 2 enrollment — 45 cooled PM contacts | 20 min | 45 leads back in sequence |
| Thu June 5 | LinkedIn connects to Summit County new enrollees | 30 min | Warm the new leads |
| Fri June 6 | Contractor text blast (all non-responders from May) | 45 min | Referral partner pipeline |

**Total week: ~3 hours. Revenue runway: 60-80 warm contacts active by June 6.**

---

## Monday June 2 — The Big Restart

**Goal:** Get Summit County leads into the pipeline. This is the county Danny missed in the May rotation.

### Step 1: Run the Apollo pull (30 min)
```bash
cd /Users/bradleyneal/forestcity
python3 workers/lead_pipeline.py danny
```
- Week 22 rotation = **Medina County** (Medina, Brunswick, Wadsworth)
- Expected: 15-20 new PM contacts
- All will auto-enroll in Property Manager Mixmax sequence

> ⚠️ **Summit County gap:** The rotation missed Summit during week 21. Summit County (Akron, Fairlawn, Stow) is the 2nd largest PM market in our 7-county area. After running the Medina pull Monday, do a **manual Summit County pull Tuesday** using:
> ```bash
> # Manually set Summit in DANNY_SEARCHES or temporarily patch the search
> python3 workers/lead_pipeline.py danny  # after updating location in lead_pipeline.py
> ```
> Reference: `outputs/donna/county_expansion_summit_2026-05-18.md` for Summit County context.

### Step 2: Create Mixmax Sequences (20 min)
**This unlocks 18 idle gas station contacts and sets up fleet washing.**

Gas Station Sequence:
1. Go to Mixmax UI → Sequences → New Sequence
2. Name: `Forest City Power Washing — Gas Station & C-Store Outreach`
3. Paste copy from: `outputs/danny/sequence_gas_stations_2026-05-19.md`
4. Copy the sequence ID from the URL
5. Paste into `integrations/mixmax.py` line 54: replace `'PENDING'`
6. Run `python3 workers/lead_pipeline.py both` — 18 gas station contacts auto-enroll

Fleet Washing Sequence:
1. Same process
2. Copy from: `outputs/danny/sequence_fleet_washing_2026-05-18.md`
3. Paste ID into `integrations/mixmax.py` line 48

### Step 3: Run Carla's Medina pull (10 min)
```bash
python3 workers/lead_pipeline.py carla
```
- Medina County referral partners: siding, gutter, landscaping, deck builders
- Reference: `agents/carla.md` for partner types

---

## Tuesday June 3 — Review + Tag

**Goal:** Understand what Touch 3 produced and set up Round 2 targeting.

### Review Touch 3 results in Mixmax:
1. Open Property Manager sequence in Mixmax
2. Check: any replies since May 22?
3. Sort by opens (highest first) — these are your warm leads
4. Tag the top 10 by opens as "Priority Round 2" — they've seen our name 3+ times

### What to do with replies (if any):
- Use templates from: `outputs/tommy/touch3_reply_response_templates_2026-05-20.md`
- Respond within 2 hours of first reply
- Goal: book a 15-minute intro call, not email a quote

### Cooling period check:
- Contacts enrolled May 12-13 → cooling period ends June 3-4
- They're eligible for Round 2 enrollment starting Wednesday

---

## Wednesday June 4 — Round 2 Enrollment

**Goal:** Re-enroll the 45 contacts who completed Round 1 in the revised sequence.

**Before enrolling — make this call:**
- If Touch 3 got 0 replies: **use the new sequence copy** from `outputs/danny/pm_sequence_touch1_rewrite_2026-05-19.md` (approved? see `outputs/vera/round2_decision_framework_2026-05-20.md`)
- If Touch 3 got replies: **use the same sequence** — don't change what's working

### Enroll new Summit County leads (from Monday pull):
These go into the sequence automatically via `lead_pipeline.py`.

### Manual re-enrollment for Round 1 contacts:
New Mixmax sequence → upload contact list from `outputs/danny/leads_cuyahoga_property_managers_2026-05-12.md` + `outputs/danny/leads_lorain_property_managers_2026-05-13.md`

Expected: 40-45 re-enrolled (some will have unsubscribed or bounced — that's normal, expect 85-90% re-enrollment rate).

---

## Thursday June 5 — LinkedIn Warm-Up

**Goal:** Make sure the 10 hottest Round 1 leads see your face on LinkedIn before Round 2 Touch 1 lands.

Connect requests today → Round 2 Touch 1 arrives in their inbox → they recognize your name → higher reply rate.

### Process:
1. Open Mixmax PM sequence → sort by opens → top 10 contacts
2. Find their LinkedIn profiles (URLs in contacts_cache.json or Google "[Name] [Company] LinkedIn")
3. Send connection requests using template from `outputs/danny/linkedin_hot_lead_dm_protocol_2026-05-18.md`
4. Note: connection request = no message, just connect. Message comes after they accept.

**Time:** 30 minutes. Target: 10 connection requests sent.

---

## Friday June 6 — Contractor Text Follow-Up

**Goal:** Re-engage all contractor contacts who didn't respond to May outreach.

### Who to text:
From `outputs/vera/priority_outreach_list_2026-05-19.md` — anyone who:
- Never responded to May 20-26 texts
- Stage is still "New Lead" in pipeline
- Has a phone number

### Script:
Use `outputs/vera/sms_templates_contractors_2026-05-18.md` — specifically the "follow-up" template (softer than the opener).

**Target:** 10-15 texts in 45 minutes.

---

## What Success Looks Like — End of June 6

By Friday June 6:
- ✅ Medina County (15-20 new PMs) enrolled in Mixmax
- ✅ Summit County pulled (backfill for the missed week)
- ✅ 18 gas station contacts enrolled in new sequence (if ID pasted Monday)
- ✅ 40-45 Round 1 contacts re-enrolled in Round 2
- ✅ 10 hot leads connected on LinkedIn
- ✅ 10-15 contractor texts sent
- **Total active in sequences by end of week: 95-115 contacts**

---

## Revenue Math: What This Week Sets Up

| Contact Type | Count | Expected Reply Rate | Expected Replies | Quote Conversion |
|-------------|-------|---------------------|-----------------|-----------------|
| Round 2 PM (re-enrolled) | 45 | 3-5% | 1-2 | 1-2 quote calls |
| Medina PM (new) | 20 | 3-5% | 0-1 | 0-1 quote calls |
| Summit PM (new) | 20 | 3-5% | 0-1 | 0-1 quote calls |
| Gas station (new seq) | 18 | 5-8% | 1-2 | 1-2 quote calls |
| Contractors (text) | 15 | 10-15% | 1-2 | 1-2 referral partnerships |

**Conservative total: 4-8 quote opportunities from June outreach**
At Forest City's average job value (~$300-500 residential / $800-1,500 commercial):
- 4 quotes × 50% close rate × $700 avg = **~$1,400 in new June revenue**
- 8 quotes × 50% × $700 avg = **~$2,800 in new June revenue**

This doesn't count referral business from contractor partnerships.

---

## Resources

| Task | File |
|------|------|
| Round 2 sequence decision | `outputs/vera/round2_decision_framework_2026-05-20.md` |
| Sequence rewrite copy | `outputs/danny/pm_sequence_touch1_rewrite_2026-05-19.md` |
| Round 2 enrollment plan | `outputs/danny/round2_enrollment_plan_2026-05-20.md` |
| Summit County context | `outputs/donna/county_expansion_summit_2026-05-18.md` |
| Gas station sequence copy | `outputs/danny/sequence_gas_stations_2026-05-19.md` |
| Fleet washing sequence copy | `outputs/danny/sequence_fleet_washing_2026-05-18.md` |
| Contractor text templates | `outputs/vera/sms_templates_contractors_2026-05-18.md` |
| Hot lead LinkedIn protocol | `outputs/danny/linkedin_hot_lead_dm_protocol_2026-05-18.md` |

---

*Donna Park | Growth & Launch Strategist | Forest City Power Washing*
