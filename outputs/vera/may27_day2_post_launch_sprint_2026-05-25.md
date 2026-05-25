# Day 2 Post-Launch Sprint — Wednesday May 27
### Vera Cole | 2026-05-25
*The gap between Day 1 evening debrief (5pm Tue) and Day 3 ad check (Thu). Fill it here.*

---

## CONTEXT

- **Day 1 (Tue May 26):** Ads launched. Check_replies ran. GBP Post 1 published. Lead log started.
- **Day 2 (Wed May 27) — This card.** First 24h of ad data is in. Likely no leads yet (learning phase) or 1–2 early leads. Don't panic at small numbers.
- **Day 3 (Thu May 28):** First real monitoring check — use `outputs/rick/facebook_ads_first_week_monitoring_guide_2026-05-23.md` and `outputs/rick/google_ads_first_week_monitoring_guide_2026-05-24.md`.

---

## WEDNESDAY MORNING — 15 MINUTES

**Do these in order:**

### 1. Check lead log (2 min)
Open `outputs/donna/launch_week_lead_log_2026-05-26.md`
- Did any leads come in from Day 1?
- If YES → call within 5 min of seeing it. Use `outputs/rick/facebook_lead_response_sop_2026-05-24.md`.
- If NO → normal for Day 1. Ads are still in learning phase.

### 2. Glance at Ads Manager (3 min)
Facebook: Check spend and impressions only. Ignore conversions on Day 2 — too early.
- Spend: Is the $30/day budget being spent? If 0 spend = billing issue, fix now.
- Impressions: >500 = ads are showing. <100 = possible targeting issue (check audience size).

Google: Same — did it spend anything? If 0 spend, check campaign status is "Enabled."

**Do NOT make any changes to targeting, budget, or copy on Day 2.** The algorithm needs 7+ days uninterrupted.

### 3. GBP Post 2 (5 min)
Post the second GBP post from `outputs/vera/launch_week_gbp_posts_2026-05-25.md` (Post 2).
business.google.com → Posts → Create. Copy from the file. 2 min to publish.
**Why now:** GBP posts during ad launch week compound the search visibility. Post 1 shows up in local search while ads run alongside.

### 4. Gas station Wave 2 emails (3 min)
Per `outputs/danny/gas_station_manual_email_blast_2026-05-25.md`:
Wave 1 (7 Tier 1 contacts) — sent May 26.
Wave 2 (11 Tier 2 contacts) — due **today May 27**.
If Wave 1 was sent, send Wave 2 now. Gmail → use the Tier 2 template from the blast guide.

### 5. Check contractor texts sent (2 min)
Did the Tier 1 contractor texts go out (Anthony, Dontez, Chris, Venus, Logan)?
- If YES with any replies → use `outputs/tommy/hot_lead_callback_script_2026-05-24.md`
- If NOT yet → send today. The ads are live now so your phone will get busy. Do it before leads start calling.
- Text: "Hey Anthony, it's Bradley from Forest City Power Washing — just launched Facebook ads and we're picking up jobs in your area. Still open to a referral swap? $50 per job you send our way." (No paperwork, 30 sec to send.)

---

## IF A LEAD COMES IN WEDNESDAY

This is the moment. **5-minute response window matters more than anything else.**

1. Call immediately. Script: `outputs/rick/facebook_lead_response_sop_2026-05-24.md`
2. If they don't answer: leave voicemail + text within 1 min
3. Log in `outputs/donna/launch_week_lead_log_2026-05-26.md`
4. If they want a quote: `outputs/tommy/quote_to_close_kit_2026-05-20.md`
5. If they say YES: `outputs/tommy/booking_confirmation_text_2026-05-25.md` — send immediately

**First lead = the proof of concept.** How you handle it sets the tone for all Week 1 revenue.

---

## WEDNESDAY AFTERNOON — OPTIONAL

If you did a job today:
- **Neighbor canvass:** Before leaving, knock 5 houses near the job site. Script: `outputs/tommy/neighbor_canvass_script_2026-05-26.md`
- **Before/after photo:** Shoot before + after. Drop in `assets/photos/` with naming convention `before_YYYY-MM-DD_IMG_XXXX.jpg`. Jasmine auto-processes these.
- **Annual plan pitch:** Within 2 hours of job completion, send the annual plan text: `outputs/tommy/annual_plan_upsell_sequence_2026-05-23.md`

---

## CRITICAL: DON'T TOUCH ADS ON DAY 2

Every time you edit an ad campaign in its first 7 days, you reset the learning phase. The algorithm needs at minimum 50 conversions to optimize. On Day 2 it has 0. Let it run. The only thing that justifies a Day 2 pause is if the budget is 0 (billing issue) or if an ad was flagged/rejected.

Edits to make on **Day 7**, not before:
- Turning off underperforming ad sets
- Expanding audiences
- Changing ad copy

---

## TONIGHT (WEDNESDAY)

- Check lead log one more time at 7pm
- Set alarm for 8:45am Thursday — that's when check_replies.py auto-runs (cron)
- Thursday is Day 3: run `outputs/rick/facebook_ads_first_week_monitoring_guide_2026-05-23.md` + `outputs/rick/google_ads_first_week_monitoring_guide_2026-05-24.md` — first real optimization checkpoint

---

## WEEK 1 TARGETS (for context)

| Metric | Day 2 Target | Day 7 Target |
|--------|-------------|-------------|
| FB ad spend | ~$30 | ~$150–$210 |
| FB impressions | 1,000–3,000 | 10,000+ |
| Leads (total) | 0–1 | 3–10 |
| Jobs booked | 0–1 | 2–5 |
| GBP posts published | 2 | 5 |
| Contractor texts sent | 5 | 5 |

---

*Vera Cole | Chief Innovation Officer | Generated 2026-05-25*
*Fills the gap between: `launch_day_evening_debrief_2026-05-26.md` (Day 1 5pm) and `facebook_ads_first_week_monitoring_guide_2026-05-23.md` (Day 3)*
