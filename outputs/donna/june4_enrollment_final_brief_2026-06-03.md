# June 4 Enrollment Day — Final Brief
*Written by Vera | June 3, 2026 | Run 187*
*Tomorrow is the day. This is your press-GO card.*

---

## GO/NO-GO — Check Before You Do Anything Else

| Check | Status | Action if Not Done |
|-------|--------|--------------------|
| Instantly.ai campaigns PAUSED | ❓ Verify | app.instantly.ai → Campaigns → ⋮ → Pause `a1c08c3d` + `626cd15d` |
| Medina County leads in contacts_cache.json | ❓ Verify | Run `python3 workers/lead_pipeline.py danny Medina` if not done |
| Summit County leads in contacts_cache.json | ❓ Verify | Run `python3 workers/lead_pipeline.py danny Summit` if not done |
| `.env` has `INSTANTLY_PAUSED=true` | ❓ Set | Open `.env`, add line: `INSTANTLY_PAUSED=true` |
| Mixmax Property Manager sequence confirmed live | ✅ ID: `6a048cfc110bc620ca0f1aee` | No action needed |

**If Instantly is NOT paused → STOP. Pause it first. 5 minutes. Then come back.**

---

## The June 4 Morning Plan (60 Minutes Total)

### Block 1 — 8:00am: Confirm Pause + Set .env (5 min)
1. Open `app.instantly.ai` → Campaigns
2. Confirm both campaigns show **Paused** (not Active)
3. Open `/Users/bradleyneal/forestcity/.env`
4. Add line: `INSTANTLY_PAUSED=true`
5. Save

### Block 2 — 8:05am: Run Medina Pull (if not done) (8 min)
Double-click `scripts/run_medina_both.command`
OR: `python3 workers/lead_pipeline.py danny Medina`

*Skip if Medina pull already ran June 1 — check `logs/activity.log` for "Danny | Medina" entry.*

### Block 3 — 8:15am: Run Summit Pull (if not done) (8 min)
Double-click `scripts/run_summit_both.command`
OR: `python3 workers/lead_pipeline.py danny Summit`

*Skip if Summit pull already ran this week — check `logs/activity.log` for "Danny | Summit" entry.*

### Block 4 — 8:25am: Run Round 2 Enrollment (10 min)
```bash
python3 workers/lead_pipeline.py both
```
This will:
- Pull any fresh contacts from today's county rotation
- Auto-enroll all unenrolled contacts into Mixmax sequences
- Run enrollment verification to catch any silent failures
- Commit the updated contacts_cache.json to GitHub

### Block 5 — 8:35am: Confirm Enrollment in Mixmax (5 min)
1. Open Mixmax → Sequences → Property Manager Outreach
2. Confirm new contacts appear as "Active" or "Step 1"
3. Spot-check 2-3 names against your contacts_cache.json

### Block 6 — 8:40am: Gas Station Manual Blast (10 min)
12 gas station contacts sitting idle since May 19. They've never been messaged.
Use the ready-to-send email script: `outputs/tommy/gas_station_sequence_copy_2026-06-03.md`
Copy the Touch 1 text → send from Gmail BCC to all 12 contacts.
(Full send guide in the Tommy file.)

### Block 7 — 8:50am: Ads Check (5 min)
Check Facebook Ads Manager for any campaigns with low budget pacing.
Confirm Lead Gen campaign is still active.

---

## What You're Enrolling Today

| Segment | Expected Contacts | Sequence |
|---------|------------------|----------|
| Medina PM / HOA managers | 15-30 | Property Manager |
| Summit PM / HOA managers | 10-20 | Property Manager |
| New county rotation contacts (any) | varies | Auto-assigned |
| Gas station contacts (12 idle) | 12 | Manual Gmail blast |

**Total expected new enrollments: 40-60 contacts**

---

## The Numbers This Unlocks

If even 10% of 50 enrolled PM contacts reply → 5 quotes
Average quote close rate in June peak season: 40%
That's **2 new commercial accounts from today's 60-minute session**

At $2,000/account average first job: **$4,000 in expected revenue from this morning**

---

## After You're Done — Post to Slack
Tell the team you ran enrollment. Post: "Round 2 enrollment complete — [X] contacts enrolled. Sequence running."

Vera will pick this up and log it.

---

## If Something Breaks

**"Enrollment blocked — Instantly not paused"** → Add `INSTANTLY_PAUSED=true` to `.env`

**"Apollo returned 0 contacts"** → Check `logs/cron.log` for API error. Try: `python3 workers/lead_pipeline.py danny Cuyahoga` instead.

**"Mixmax enrollment rejected"** → Email may already be in a sequence. Check Mixmax contact search.

**Can't log in to Instantly.ai** → Use "Forgot Password" flow. The campaigns are already running — you just need to pause them, not configure anything new.

---

*Next milestone after today: June 8 Cuyahoga mega-pull — 170+ segments, largest pull of the season.*
