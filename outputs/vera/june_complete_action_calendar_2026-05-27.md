# June 2026 Complete Action Calendar
### Forest City Power Washing — Full Month Reference
*Vera Cole | Run 114 | 2026-05-27*

This is the single-screen June reference. Every pull, enrollment, monitoring checkpoint, and revenue action for the entire month. Print it, pin it, run it.

---

## Pre-June Checklist (Complete by May 31)
| Item | Status | Deadline |
|------|--------|----------|
| Summit County pull (Danny + Carla) | ⬜ TODO | **May 31 — HARD DEADLINE** |
| Instantly.ai campaigns paused (a1c08c3d + 626cd15d) | ⬜ TODO | May 30 latest |
| Gas Station Mixmax sequence created + ID in mixmax.py | ⬜ TODO | June 1 |
| Wave 2 contractor Day 3 follow-up (16 contacts) | ⬜ TODO | **May 31** |
| Past customer blast (fastest revenue — Tommy's guide ready) | ⬜ TODO | Ongoing May 27–June 7 |
| Bryan CLE Lawn Care Plus final decision | ⬜ TODO | May 29 |

---

## June Week 1 (June 1–7)

### Monday June 1 — MEDINA COUNTY PULL
**The biggest pull of the season. ALL 25+ new commercial segments fire here for the first time.**
- [ ] Double-click `scripts/run_medina_both.command` (Danny + Carla, ~10 min unattended)
- [ ] While pull runs: create Gas Station Mixmax sequence (guide: `outputs/danny/gas_station_sequence_create_now_2026-05-27.md`)
- [ ] After pull: paste Gas Station sequence ID into `integrations/mixmax.py` line 54 → run `python3 workers/lead_pipeline.py pending`
- [ ] Check Nina's report: new funeral homes / urgent care / golf course / marina contacts from Medina
- [ ] Revenue math: 25+ segments × Medina county = estimated 40–80 new enrollments today
- **Relay fires:** Medina countdown reminder + (if gas station still PENDING) gas station escalation

### Tuesday June 2 — ADS DAY 7 REVIEW
- [ ] Facebook Ads Manager: 7-day performance review (CTR, CPL, reach)
- [ ] Google Ads: 7-day review (CTR, CPC, conversions)
- [ ] Decision matrix: `outputs/rick/week2_facebook_ads_scaling_guide_2026-05-26.md`
- [ ] If CTR >1.5% + CPL <$30 → bump budget 20%
- [ ] If mixed → swap creative (ONE change only)
- [ ] June 4 countdown: 2 days — verify all blockers are cleared
- **Relay fires:** Day 7 ads scaling reminder + June 4 enrollment countdown (2 days)

### Wednesday June 3 — NIGHT-BEFORE ENROLLMENT PREP
- [ ] Go/No-Go check: `outputs/vera/june4_enrollment_readiness_tracker_2026-05-27.md`
- [ ] Verify Instantly.ai IS paused (app.instantly.ai → Campaigns → confirm both paused)
- [ ] Confirm Medina pull output in `outputs/danny/` — new leads visible
- [ ] Confirm Summit pull output in `outputs/danny/` — summit leads visible
- [ ] Read June 4 battle card: `outputs/donna/june4_enrollment_battle_card_2026-05-24.md`
- [ ] Set alarms: 8am sharp to start
- **Relay fires:** June 4 enrollment countdown (TOMORROW)

### Thursday June 4 — ROUND 2 ENROLLMENT DAY
**The biggest outreach day of the season. Execute in 90 minutes.**
- [ ] **8:00am** — Run enrollment: `python3 workers/lead_pipeline.py both` (enrolls Summit + Medina PM contacts)
- [ ] **8:30am** — Gas station enrollment: `python3 workers/lead_pipeline.py pending` (if sequence created)
- [ ] **9:00am** — Wave 2 contractor Day 7 follow-up texts (16 contacts, scripts: `outputs/vera/wave2_contractor_followup_schedule_2026-05-27.md`)
- [ ] **9:30am** — Carla referral partner revival: `outputs/carla/june4_carla_activation_card_2026-05-xx.md`
- [ ] Log all activity in pipeline_data.json via `python3 scripts/contact_done.py`
- **Revenue at stake:** $55K–$144K potential pipeline activated today
- **Relay fires:** June 4 enrollment countdown (TODAY)

### Friday June 5 — POST-ENROLLMENT MONITORING STARTS
- [ ] Nina daily report (run locally): check for first opens (Touch 1 sent yesterday)
- [ ] Respond to ANY reply within 1 hour
- [ ] Check ads: are ad leads flowing in? Log every lead in pipeline_data.json
- [ ] Past customer blast follow-up (if sent this week, check responses)
- **Relay fires:** Post-enrollment monitoring Day 2 reminder

### Saturday June 6
- [ ] Check Facebook Business Suite → Leads Center for any weekend ad leads
- [ ] Social content: before/after photo from any jobs this week (Jasmine flyer)
- [ ] GBP post (Jasmine content calendar)

### Sunday June 7 — FIRST TOUCH 2 OPENS EXPECTED
- [ ] Touch 1 sent June 4. Open window opens ~Day 2–3 = June 6–7
- [ ] First replies could arrive TODAY — check email
- [ ] Nina daily report: `python3 workers/nina_report.py daily`
- **Relay fires:** Post-enrollment monitoring Day 4

---

## June Week 2 (June 8–14)

### Monday June 8 — GEAUGA + PORTAGE COUNTY PULL
*Smaller market (~15–25 leads) — Chardon, Chesterland, Kent, Ravenna*
- [ ] Cron fires automatically at 7am (Danny + Carla — Geauga+Portage rotation)
- [ ] If cron missed: `python3 workers/lead_pipeline.py both Geauga+Portage`
- [ ] Nina weekly report: `python3 workers/nina_report.py weekly` — first full enrollment week summary
- [ ] Review: reply rate from June 4 Touch 1 (benchmark: 1–3% = 1–5 replies from 100–160 contacts)
- [ ] Hot leads (2+ opens, no reply): connect on LinkedIn today → DM: "I saw you opened our note about NE Ohio properties"
- **Relay fires:** Geauga + Portage countdown (fires June 4–8)

### Tuesday June 9 — HOT LEAD RESPONSE DAY
- [ ] Nina daily: flag all 2+ open contacts
- [ ] LinkedIn connect with every hot lead from this week's Nina report
- [ ] For hot leads with phone numbers: call between 10am–2pm
- [ ] Touch 2 emails sent automatically around Day 3 (June 7) — some contacts will have received 2 touches

### Wednesday June 10
- [ ] Mid-week pipeline update: `python3 scripts/contact_done.py`
- [ ] Check ads performance (Week 2): are CPLs tracking to target?
- [ ] Respond to any gas station replies (if sequence fired)

### Thursday June 11 — TOUCH 2 WINDOW
*Round 2 Touch 2 sends ~Day 7 (June 11). Second open surge expected.*
- [ ] Nina daily: high priority — second-touch opens are often the buying signal
- [ ] Respond to ALL replies within 1 hour
- [ ] Book estimates for interested contacts — offer specific dates
- [ ] GBP post: schedule this week's before/after content
- **Relay fires:** Post-enrollment monitoring Day 8 (last day of post-June4 relay)

### Friday June 12 — MID-MONTH CHECK
- [ ] Nina weekly report: mid-month summary
- [ ] Pipeline triage: who needs a call vs email vs LinkedIn vs close?
- [ ] Past customer re-engagement: if not done May 27–June 7, do it NOW (Tommy guide: `outputs/tommy/past_customer_june_blast_2026-05-27.md`)
- [ ] Review ad spend to date: CPA calculation, budget adjustment if needed

### Saturday June 13 — FATHER'S DAY PREP
- [ ] Father's Day = Sunday June 15 — peak visitation at cemeteries, funeral homes, parks
- [ ] Jasmine: schedule Father's Day social post (residential curb appeal angle: "gift dad a clean driveway")
- [ ] GBP post: Father's Day timing content
- [ ] Funeral home + cemetery contacts from Medina pull: these are warm targets right now (high-visibility family visits)

### Sunday June 14 — FATHER'S DAY EVE
- [ ] Verify Father's Day social content is scheduled for 8am Sunday
- [ ] Check estimates pending from this week — follow up Monday if no response

---

## June Week 3 (June 15–21)

### Monday June 15 — CUYAHOGA COUNTY PULL + FATHER'S DAY
*Week 24: Cuyahoga = Cleveland, Parma, Lakewood, Strongsville, Solon — largest market in rotation*
- [ ] Cron fires at 7am (Danny + Carla — Cuyahoga rotation)
- [ ] If cron missed: `python3 workers/lead_pipeline.py both Cuyahoga`
- [ ] Cuyahoga = the largest commercial market; expect 40–60+ new leads from all 25+ segments
- [ ] Nina weekly report: week 2 post-enrollment summary
- [ ] Father's Day: Cemeteries and funeral homes are at maximum family visibility today — note for future timing

### Tuesday June 16 — ESTIMATE FOLLOW-UP SWEEP
- [ ] Any estimate sent last week? Follow up by phone today
- [ ] Nina report: flag any "Estimate Sent" contacts 5+ days ago (stale estimate alert)
- [ ] Cuyahoga new leads: check enrollment confirmation in Nina's report

### Wednesday June 17 — TOUCH 3 APPROACHES
*Touch 3 sends ~Day 14 after June 4 enrollment = June 18. Final touch before Mixmax sequence ends.*
- [ ] Prepare for Touch 3 replies — this is the highest-urgency reply window
- [ ] Review all hot leads from Cuyahoga pull (just enrolled)
- [ ] LinkedIn: connect with any Cuyahoga leads who opened already (fast movers)

### Thursday June 18 — TOUCH 3 SENDS
*Final touch for Round 2 PM sequence (~Day 14). Some contacts reply only after Touch 3.*
- [ ] Nina daily: priority check — Touch 3 opens are often last-chance engagement
- [ ] Respond to ALL replies immediately — these are the most sales-ready contacts
- [ ] For no-response hot leads: one direct call attempt today

### Friday June 19 — JUNETEENTH (Federal Holiday)
- [ ] Limited Bradley availability likely
- [ ] Check ads + Nina report from phone
- [ ] Social: Jasmine content if appropriate

### Saturday June 20 — SOCIAL PUSH
- [ ] Before/after job photos from Week 3 (Jasmine flyer)
- [ ] Facebook + Instagram post: summer content
- [ ] GBP post

### Sunday June 21
- [ ] Week-end check: pipeline, ads, upcoming pull (Lake County June 22)

---

## June Week 4 (June 22–30)

### Monday June 22 — LAKE COUNTY PULL — MARINA SEASON
*Week 25: Lake County = Mentor, Willoughby, Painesville + Lake Erie shoreline marinas*
- [ ] Cron fires at 7am (Danny + Carla — Lake County rotation)
- [ ] If cron missed: `python3 workers/lead_pipeline.py both Lake`
- [ ] **This is the MARINA county** — Mentor Harbor Yachting Club, Sheffield Lake Marina, Euclid marinas
- [ ] Marina managers: mid-season cleaning window is June–July (dock areas, boat ramps, fuel station concrete)
- [ ] Also: Mentor/Willoughby hotel corridor, senior living facilities, retail centers
- [ ] Expect 20–35 new leads; first marina contacts in the pipeline
- **Relay fires:** Lake County / Marina countdown (fires June 17–22)

### Tuesday June 23 — HOT LEAD RESPONSE DAY
- [ ] Nina daily: Lake County new leads + any Reply/hot from Cuyahoga
- [ ] Marina contacts if any replied: prioritize — these are novel relationships with zero competitor pressure

### Wednesday June 24
- [ ] GBP post: summer content
- [ ] Mid-month estimate follow-up (anyone from June 4–11 enrollment who got estimate but didn't book)

### Thursday June 25 — FINAL HOT LEAD PUSH
- [ ] Call any 2+ open contacts who haven't replied through 3 touches
- [ ] For gas station contacts: where are they in the sequence? Any replies?
- [ ] Review: which commercial segments from Medina pull have the highest open/reply rate?

### Friday June 26 — LORAIN COUNTY PULL
*Week 26: Lorain County = Elyria, Avon, North Ridgeville — suburban/commercial mix*
- [ ] Cron fires at 7am (Danny + Carla — Lorain rotation)
- [ ] If cron missed: `python3 workers/lead_pipeline.py both Lorain`
- [ ] Avon/Avon Lake corridor: retail centers, senior living, HOA communities

### Saturday June 27
- [ ] Job photos from week's work → Jasmine flyer
- [ ] Facebook/Instagram post

### Sunday June 28 — MONTH-END CHECK
- [ ] Count: how many estimates sent this month?
- [ ] Count: how many bookings closed?
- [ ] Ad spend vs revenue: CPA calculation for June
- [ ] Which commercial segments from June 1 Medina pull produced any replies?

### Monday June 29 — NEW MONTH PREP
- [ ] Plan July 6 Summit County pull (rotation restarts: Summit → Medina → Geauga+Portage → Cuyahoga → Lake → Lorain)
- [ ] Nina weekly report: full June summary
- [ ] Revenue tally: Workiz job report for all June bookings

### Tuesday June 30 — JUNE CLOSE
- [ ] Final revenue count: how much did June booking blitz produce?
- [ ] Open pipeline: any contacts who replied but haven't booked yet → schedule July follow-ups
- [ ] Commercial segments: make a note of which Medina/Summit leads produced results → tune Danny search for July
- [ ] Contractor referral network: any of the Wave 2 contractors sending jobs yet?

---

## June Revenue Targets (Reference)

| Source | Realistic Target | Stretch Target |
|--------|-----------------|----------------|
| Ad-generated bookings (Facebook + Google) | 3–6 jobs | 8–12 jobs |
| Mixmax PM/Commercial replies → bookings | 2–5 jobs | 6–10 jobs |
| Contractor referrals (from May–June texts) | 1–3 referral jobs | 4–8 jobs |
| Past customer re-engagement | 3–8 rebooked jobs | 10–15 rebooked |
| Gas station sequence (if created June 1) | 0–2 bookings | 3–5 bookings |
| **Total June revenue** | **$4,000–$12,000** | **$15,000–$30,000** |

---

## June Cron Health Check
Run this every Monday to verify cron is alive:
```bash
cat /Users/bradleyneal/forestcity/logs/cron.log | tail -20
```
Expected: entry from today or yesterday for danny/carla/nina/vera_relay.
If no recent entries: re-run `crontab -e` and verify all 5 jobs are there.

---

## Key Files Reference
| File | What It Does |
|------|-------------|
| `outputs/donna/june4_enrollment_battle_card_2026-05-24.md` | June 4 execution guide |
| `outputs/vera/june4_enrollment_readiness_tracker_2026-05-27.md` | Go/No-Go checklist |
| `outputs/vera/wave2_contractor_followup_schedule_2026-05-27.md` | May 31 + June 4 follow-up scripts |
| `outputs/vera/june1_june4_sprint_card_2026-05-27.md` | June 1–4 sprint plan |
| `outputs/vera/june5_post_enrollment_follow_through_2026-05-27.md` | June 5–11 monitoring guide |
| `outputs/rick/week2_facebook_ads_scaling_guide_2026-05-26.md` | June 2 ads decision matrix |
| `outputs/tommy/past_customer_june_blast_2026-05-27.md` | Past customer re-engagement |
| `outputs/danny/gas_station_sequence_create_now_2026-05-27.md` | Gas station Mixmax setup |

---

*Vera Cole | Run 114 | Generated 2026-05-27*
*Updates: vera_relay.py now covers June 8 (Geauga+Portage) and June 22 (Lake County/Marinas) with countdown reminders.*
