# June 1 Morning Prep Checklist — Medina County Kickoff
### Donna Park | Growth Strategist | Created May 23, 2026
*15-minute Monday morning checklist. Week 22 starts today. This is the first week of June Booking Blitz.*

---

## Before You Open Slack — 5 Minutes

### 1. Run Danny's Medina County Pull (2 min)
```bash
cd /Users/bradleyneal/forestcity
python3 workers/lead_pipeline.py danny Medina
```
> **Why now:** Week 22 = Medina County. This is the first normal cron week since the Memorial Day gap. Medina has Medina, Brunswick, Wadsworth — active commercial property market, lower competition than Cuyahoga.

### 2. Run Carla's Referral Partner Pull (2 min)
```bash
python3 workers/lead_pipeline.py carla
```
> **Why now:** Carla also uses the county rotation. Week 22 = Medina/Brunswick contractors and realtors. Fresh referral partners to outreach this week.

### 3. Run Nina's Weekly Report (1 min)
```bash
python3 workers/nina_report.py weekly
```
> **Why now:** Monday morning report gives you the full pipeline picture heading into the blitz week — how many enrolled, open rates, any replies from the May 26 bridge emails.

---

## Once Pulls Are Running (Check These in Parallel)

### 4. Did the May 26 Bridge Emails Go Out?
Check: did you send the 5 personal Gmail emails to hot leads on May 26?
- Script: `outputs/tommy/hot_lead_bridge_email_may26_2026-05-22.md`
- If yes: check replies in Gmail now — any warm responses need same-day follow-up
- If no: send them TODAY, just 2 days late — still actionable

### 5. Summit County Pull — Did It Happen?
Check `logs/cron.log` or run `python3 workers/check_replies.py`:
```bash
python3 workers/check_replies.py
```
- If Summit was never pulled (May 12 was last): use the county override right now:
  ```bash
  python3 workers/lead_pipeline.py danny Summit
  ```
  Then re-run Medina after. You can catch up both counties on June 1.

### 6. Instantly.ai — Are Campaigns Paused?
Before Round 2 enrollment: MUST confirm both campaigns are paused.
- Campaigns: `a1c08c3d` (PM Cuyahoga) + `626cd15d` (Contractor Referral)
- Guide: `outputs/vera/instantly_pause_guide_2026-05-22.md`
- If still running: pause them NOW before enrolling Round 2

---

## Round 2 Enrollment — June 4 Target (Thursday)

### The Plan:
| Day | Action |
|-----|--------|
| June 1 (Mon) | Medina + Summit pulls complete. Instantly.ai paused. |
| June 2 (Tue) | Review Nina's weekly report. Choose A/B subject lines. |
| June 3 (Wed) | Final check: contacts_cache.json updated, sequences ready. |
| June 4 (Thu) | Enroll Round 2 — aim for 50–75 new PM contacts |
| June 4 (Thu) | Create gas station sequence in Mixmax UI → paste ID → run `pending` mode |

### Round 2 Enrollment Command (June 4):
```bash
# Enroll all new Medina + Summit contacts that haven't been enrolled yet
python3 workers/lead_pipeline.py both
```

### A/B Subject Lines (already written — use these for Round 2):
See `outputs/tommy/email_subject_line_ab_test_2026-05-22.md`
- Pair 1: "Quick question about your properties" vs. "The algae problem at your buildings"
- Send at 10:30am Tuesday–Thursday — peak B2B open time

---

## Ads — Launch This Week

### Google Ads + Facebook Ads — Both Ready to Launch
All copy is written and waiting:
- Google Ads: `outputs/rick/google_ads_june_2026-05-19.md`
- Facebook Ads: `outputs/rick/facebook_ads_peak_season_2026-05-20.md`
- Launch checklist: `outputs/vera/may26_ads_launch_checklist_2026-05-22.md`

**If not launched on May 26:** Launch today (June 1). Every day of peak season without ads = bookings missed.

---

## Gas Station Sequence — 5 Minute Task
18 contacts are sitting unenrolled. As soon as you create the Mixmax sequence:
1. Go to Mixmax → New Sequence → use copy from `outputs/danny/sequence_gas_stations_2026-05-19.md`
2. Copy the sequence ID
3. Paste into `integrations/mixmax.py` line ~54 (gas_station → id: 'PASTE_HERE')
4. Run: `python3 workers/lead_pipeline.py pending`
Done. 18 district managers enrolled automatically.

---

## Weekly Targets — June 1–6

| Metric | Target |
|--------|--------|
| New PM leads pulled (Medina) | 20–30 |
| New referral partners pulled (Carla) | 10–15 |
| Round 2 enrollment date confirmed | June 4 |
| Ads live | Today or before June 3 |
| Gas station sequence created | Today |
| Bridge email replies followed up | Same day |

---

*This is the start of the most important commercial outreach week of the season. Medina County is underworked — most power washing competitors focus on Cuyahoga. Move fast.*
