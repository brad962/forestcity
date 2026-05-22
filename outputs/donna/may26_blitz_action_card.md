# May 26 Blitz Day — Action Card
**Monday Morning | Memorial Day Recovery | Forest City Power Washing**
*Bradley — open this at 8am on May 26.*

---

## 1. CHECK TOUCH 3 RESULTS (10 min)
> Touch 3 fired May 22. You have 4 days of reply data.

**Log in to Mixmax → Sequences → Property Manager**
- Any replies? → Use `outputs/tommy/touch3_reply_response_templates_2026-05-20.md`
- Contacts with 3+ opens and no reply? → Bridge email today from your Gmail (`outputs/tommy/hot_lead_bridge_email_2026-05-19.md`)
- 0 replies total? → Decision: swap Email 1 for Round 2 (`outputs/tommy/round2_pm_sequence_rewrite_2026-05-21.md`) — pick Version A (social proof)

---

## 2. CONTRACTOR FOLLOW-UPS (15 min)
> Three contractors due for follow-up today. Contacted May 13–19.

**Text these TODAY:**
| Contact | Company | Phone |
|---------|---------|-------|
| (call/text) | Bulletproof Lawncare | 216-307-4344 |
| (call/text) | Damrons Landscaping | 440-494-0422 |
| Bryan | CLE Lawn Care Plus | 216-402-1924 |

Scripts: `outputs/tommy/contractor_followup_texts_may26_2026-05-21.md`

---

## 3. TIER 1 NEW LEAD TEXTS (20 min)
> 33 contacts in New Lead stage. These 5 are the highest-value.

**Text or call:**
| Name | Company | Phone |
|------|---------|-------|
| Anthony | Land Pro Management | 440-320-2779 |
| Dontez | GTP Landscaping | 440-396-0814 |
| Chris | Twin Improvements | 216-773-0757 |
| Venus | Reliable Roofing | 216-810-2497 |
| Logan | Pagels | 216-956-5263 |

Scripts: `outputs/tommy/contractor_referral_text_script_2026-05-20.md`

---

## 4. RUN DANNY SUMMIT COUNTY PULL (5 min setup + 15 min runs)
> 10 days overdue. Round 2 enrollment June 4 requires this.

```
cd /Users/bradleyneal/forestcity
python3 workers/lead_pipeline.py danny
```
Expected: 15–25 new property manager leads from Summit County / Akron area.

---

## 5. SET UP CRONTAB (5 min — one time only)
> Prevents this 10-day gap from happening again.

```
crontab -e
```
Paste the contents of `scripts/crontab_setup.txt` → save → done.
Verify: `crontab -l`

---

## 6. CREATE GAS STATION MIXMAX SEQUENCE (15 min)
> 18 gas station contacts in pipeline — idle since May 19.

1. Go to Mixmax → Sequences → Create New
2. Name: `Forest City Power Washing — Gas Station & C-Store Outreach`
3. Copy emails from `outputs/danny/sequence_gas_stations_2026-05-19.md`
4. Paste the Sequence ID into `integrations/mixmax.py` line ~54 (`'gas_station': {'id': 'PASTE_HERE'}`)
5. Run: `python3 workers/lead_pipeline.py danny` → auto-enrolls all 18

Setup guide: `outputs/vera/mixmax_sequence_setup_guide_2026-05-20.md`

---

## 7. PAST CUSTOMER TEXT BLAST (20 min)
> Highest-ROI action of the week. Revenue estimate: $1,400–$4,000.

1. Pull your past customer list from Workiz or your phone contacts
2. Use template from `outputs/tommy/past_customer_reengagement_2026-05-18.md`
3. Text or call 20–30 people — aim for 20% response

Launch guide: `outputs/donna/past_customer_reengagement_launch_2026-05-21.md`

---

## 8. POST TO GOOGLE BUSINESS PROFILE (5 min)
> Free. Drives local search ranking. First post = fast win.

Go to **business.google.com** → Posts → Create Post
- Use template from `outputs/vera/gbp_post_may21_2026.md`
- Photo: any good job photo from your phone

Routine: `outputs/vera/gbp_weekly_routine_2026-05-21.md`

---

## SCORECARD
Check off by end of day:
- [ ] Touch 3 replies checked + responses sent
- [ ] 3 follow-up texts sent (Bulletproof, Damrons, CLE Lawn)
- [ ] 5 Tier 1 new lead texts sent
- [ ] Danny Summit County pull complete
- [ ] Crontab installed (one time)
- [ ] Gas station Mixmax sequence created
- [ ] Past customer blast sent
- [ ] First GBP post live

**If you only have 45 minutes: do #1, #2, #4, #7 in that order.**

---
*Vera Cole — Forest City AI Office | 2026-05-22*
