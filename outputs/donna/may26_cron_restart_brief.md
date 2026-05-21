# May 26 — First Day Back Brief
### Monday Morning, Post-Memorial Day
*Donna Park — Growth Strategist | Run 39 | 2026-05-21*

---

## SITUATION GOING INTO THE WEEKEND

- **Touch 3 fired May 22** — check for replies FIRST THING
- **Danny cron: 13+ days overdue** — Summit County leads untouched
- **36 pipeline contacts** — 33 never texted, 3 contacted (Bulletproof/Damrons/CLE Lawn Care need follow-up)
- **Gas/fleet sequences**: still PENDING in Mixmax (target: create today, June 2)
- **June Residential Push**: launches this week — service pages + ads need to go live

---

## STEP-BY-STEP: FIRST 2 HOURS (Monday May 26)

### 8:00 AM — Check Touch 3 Results (5 min)

Open Mixmax → Sequences → Property Manager sequence → Recipients.

**If you see replies:** Open `outputs/tommy/touch3_reply_response_templates_2026-05-20.md` and respond within 30 minutes. Warm leads cool fast.

**If 0 replies:** That's OK. Open `outputs/vera/round2_decision_framework_2026-05-20.md` and decide which Round 2 scenario applies. Round 2 enrollment (Summit County) starts June 2.

---

### 8:10 AM — Text 5 Tier 1 Contractors (10 min)

If you didn't text these on May 20 or 21, send now. Memorial Day weekend is over — they're back at work:

| Name | Phone | Script |
|------|-------|--------|
| Anthony / Land Pro | 440-320-2779 | A (landscaper) |
| Dontez / GTP | 440-396-0814 | A (landscaper) |
| Twin Improvements | 216-773-0757 | B (siding) |
| Reliable Roofing | 216-810-2497 | C (roofing) |
| Pagels Construction | 216-956-5263 | C (roofing) |

Scripts: `outputs/tommy/contractor_referral_text_script_2026-05-20.md` — copy/paste, personalize name only.

---

### 8:25 AM — Run Danny Pipeline (Summit County) (5 min to launch)

Danny's cron hasn't run since May 13. This is 13+ days of missed Summit County leads (Akron, Fairlawn, Stow — NE Ohio's 2nd largest PM market).

**Run this command on your Mac:**
```bash
cd /Users/bradleyneal/forestcity
python3 workers/lead_pipeline.py danny
```

Expected output: 15–25 new property manager leads from Summit County pulled and enrolled in the PM sequence. If it says "Apollo returned 0 people — API blocked," check that your `.env` APOLLO_KEY is still valid.

While that's running, move to the next step.

---

### 8:30 AM — Set Up Cron Jobs (10 min)

This prevents the "Danny overdue" problem from happening again.

**Run this command:**
```bash
crontab -e
```

Paste these lines at the bottom (copy from CLAUDE.md if needed):

```
# Lead Pipeline — Danny + Carla — every Monday at 7am
0 7 * * 1 cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both >> logs/cron.log 2>&1

# Nina Daily Hot Leads — weekdays at 8am
0 8 * * 1-5 cd /Users/bradleyneal/forestcity && python3 workers/nina_report.py daily >> logs/cron.log 2>&1

# Nina Weekly Pipeline Report — every Monday at 8:30am
30 8 * * 1 cd /Users/bradleyneal/forestcity && python3 workers/nina_report.py weekly >> logs/cron.log 2>&1

# Workiz Daily Report — weekdays at 9am
0 9 * * 1-5 cd /Users/bradleyneal/forestcity && python3 workers/workiz_report.py daily >> logs/cron.log 2>&1

# Vera Relay (Slack message delivery) — every 5 minutes
*/5 * * * * cd /Users/bradleyneal/forestcity && python3 workers/vera_relay.py >> logs/cron.log 2>&1
```

Save and exit (`:wq` in vim, or Ctrl+X → Y → Enter in nano).

**Verify it worked:** `crontab -l` — should show 5 jobs.

---

### 9:00 AM — Create Gas Station Mixmax Sequence (20 min)

Follow the step-by-step guide: `outputs/vera/mixmax_sequence_setup_guide_2026-05-20.md`

The sequence copy is already written: `outputs/danny/sequence_gas_stations_2026-05-19.md`

Steps:
1. Open Mixmax → Sequences → New Sequence
2. Name it: "Forest City Power Washing — Gas Station & C-Store Outreach"
3. Paste the 3 emails from the sequence copy file
4. Copy the new sequence ID from the URL
5. Paste into `integrations/mixmax.py` line 54: replace `'PENDING'`
6. Run `python3 workers/lead_pipeline.py both` — 18 gas station contacts auto-enroll

---

### 9:30 AM — Follow Up with Bulletproof, Damrons, CLE Lawn Care Plus

All 3 were contacted May 13–19. No replies noted. It's been 1–2 weeks.

**CLE Lawn Care Plus** (called May 13 — notes say "left off here"):
- Call them back: use the referral pitch from `outputs/carla/referral_partner_onboarding_2026-05-20.md`

**Bulletproof Lawncare + Damrons Landscaping** (texted May 19):
- If no reply: send a follow-up text. "Hey — wanted to check back. Did you get a chance to think about the referral deal? Happy to keep it simple, just want to get something going before June gets busy."

---

## THIS WEEK'S LAUNCH TARGETS

Per the June Residential Push brief (`outputs/donna/june_residential_push_2026-05-20.md`):

| Day | Action |
|-----|--------|
| Mon May 26 | Danny pipeline (Summit County) + contractor texts + cron setup |
| Tue May 27 | Past customer re-engagement text blast (pull from Workiz first) |
| Wed May 28 | Build Roof Soft Wash service page (copy: `outputs/tommy/website_copy_service_pages_2026-05-20.md`) |
| Thu May 29 | Build House Washing service page |
| Fri May 30 | Review all pages, check for broken links |
| Mon June 2 | Summit County Round 2 enrollment (60-day cooling from round 1 starts June 3) |
| Tue June 3 | Launch Facebook ads ($30/day to start — `outputs/rick/facebook_ads_peak_season_2026-05-20.md`) |
| Wed June 4 | Launch Google Ads (`outputs/rick/google_ads_june_2026-05-19.md`) |

---

## NUMBERS TO HIT THIS WEEK

- 5 Tier 1 contractor texts sent ✓
- Danny Summit County pipeline run ✓
- Cron jobs active ✓
- Gas station sequence live ✓
- Roof Soft Wash service page published
- 1 past customer re-engagement text sent

---

*Vera | Run 39 | 2026-05-21*
