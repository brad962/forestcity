# June 4 → June 8 Bridge Card
*Vera Cole | Run 195 | 2026-06-04*

---

## The Situation Right Now

Today is June 4 — Round 2 enrollment day. June 8 (Monday) is the biggest pull of the year: **184+ commercial segments**, Cuyahoga County, every hospital/museum/government facility/school/aerospace plant in the region.

Four days between now and the mega-pull. This card tells you exactly what to do each day so you hit June 8 in perfect position.

---

## TONIGHT — June 4

**30 minutes. Three things.**

| # | Task | Time | Done? |
|---|------|------|-------|
| 1 | Verify Instantly.ai paused: [app.instantly.ai](https://app.instantly.ai) → Campaigns → a1c08c3d + 626cd15d → ⋮ → Pause | 2 min | ☐ |
| 2 | Confirm June 4 enrollment ran: `cat ~/forestcity/logs/activity.log \| grep "June 4\|run_summit\|run_medina"` | 3 min | ☐ |
| 3 | Gas Station Mixmax sequence — **create tonight, 10 minutes** (see section below) | 10 min | ☐ |
| 4 | Set Monday June 8 alarm: 7:30am — Cuyahoga mega-pull | 1 min | ☐ |

---

## FRIDAY June 5

**15 minutes. One thing.**

Run Nina's daily hot leads report. Any Round 1 or Round 2 contacts who opened emails are now Day 3–5 warm:

```bash
cd /Users/bradleyneal/forestcity && python3 workers/nina_report.py daily
```

If Nina flags anyone with 2+ opens + no reply → connect on LinkedIn same day, send this message:
> "Hey [FirstName] — just wanted to make sure my email landed. Happy to send over pricing info if that's helpful."

**That's it for Friday. Don't overthink it.**

---

## SATURDAY June 6

**No required action.** Check Google Ads/Facebook Ads performance in the ad platforms (5 minutes).

- Google: Is CTR above 3%? Are impressions growing?
- Facebook: Is CPL below $35? Are leads coming in?

If yes → keep running, scale slightly Monday after the pull.
If no → wait until Monday's review; don't change creative mid-weekend.

---

## SUNDAY June 7 — Pre-Flight Night

**20 minutes. Prepare for Monday.**

| # | Task | Done? |
|---|------|-------|
| 1 | Open Terminal: `cd /Users/bradleyneal/forestcity && cat scripts/run_cuyahoga_both.command` — confirm it exists and is readable | ☐ |
| 2 | Verify `.env` has APOLLO_KEY, MIXMAX_TOKEN set correctly: `cat .env \| grep -E "APOLLO\|MIXMAX"` | ☐ |
| 3 | Check contacts_cache.json to know your current contact count baseline: `python3 -c "import json; d=json.load(open('contacts_cache.json')); print(len(d))"` | ☐ |
| 4 | Read the June 8 exec guide: `outputs/donna/june8_cuyahoga_megapull_exec_guide_2026-06-03.md` | ☐ |
| 5 | Set 7:30am Monday alarm. This is not optional. The pull takes 12–20 minutes. Do it before client calls start. | ☐ |

---

## MONDAY June 8 — The Mega-Pull

**7:30am. One command.**

```bash
cd /Users/bradleyneal/forestcity && bash scripts/run_cuyahoga_both.command
```

This runs Danny + Carla for Cuyahoga County across all 184+ commercial segments. Expected runtime: 12–20 minutes. Do NOT interrupt it mid-run.

**After it completes:**
1. Check the terminal output for contact count: "X new contacts enrolled"
2. Run Nina's daily report to see the first batch: `python3 workers/nina_report.py daily`
3. Check Mixmax → Sequences → Property Manager sequence for enrollment confirmation
4. Log your contact count increase in `contacts_cache.json`

**Expected output:** 200–800 new commercial contacts enrolled into sequences, spanning hospitals, school districts, municipal governments, aerospace manufacturers, golf courses, funeral homes, marinas, and every other commercial segment added this season.

---

## The Gas Station / Fleet Problem — Do This Tonight

This has been PENDING for 19 days. 12 gas station contacts are sitting in `pipeline_data.json` unenrolled. Here's the 5-minute fix:

**Step 1:** Go to [app.mixmax.com/sequences](https://app.mixmax.com/sequences)
**Step 2:** Click "New Sequence" → Name it: `Forest City Power Washing — Gas Station & C-Store Outreach`
**Step 3:** Copy the sequence ID from the URL (looks like: 6a048c...)
**Step 4:** Open `integrations/mixmax.py` → find line 47–58 → replace `'PENDING'` on line 47 with your new sequence ID

Do the same for Fleet Washing sequence (name it: `Forest City Power Washing — Fleet Washing Outreach`).

**Then run:**
```bash
cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py pending
```

This enrolls all 12+ pending gas station and fleet contacts in under 2 minutes. Done.

---

## The Big Picture

| Date | Event | Status |
|------|-------|--------|
| June 4 | Summit + Medina Round 2 enrollment | Today |
| June 5–7 | Watch for early opens, respond to hot leads | Monitor |
| June 7 | Pre-flight checklist for June 8 | Plan |
| **June 8** | **Cuyahoga mega-pull — 184+ segments** | **THE PULL** |
| June 9–12 | First opens from June 8 batch (Touch 1 Day 3–5) | Monitor |
| June 11–14 | Touch 2 fires automatically (Day 3 cadence) | Auto |
| June 15 | Lake County pull (marina corridor) | Schedule |
| June 22 | Lorain County pull (Avon corridor) | Schedule |

---

*This card was generated by Vera Cole — Chief Innovation Officer, Forest City AI Office*
*Run 195 | 2026-06-04*
