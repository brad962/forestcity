# Sunday Evening Protocol — May 25 Reply Window Close
### Tommy Greer | 2026-05-23
*72-hour reply window closes tonight. Here's exactly what to do at 8pm Sunday.*

---

## The Situation
Touch 3 fired Thursday May 22. The 72-hour reply window closes **tonight, Sunday May 25**.

After tonight, the automated sequence is spent. Monday May 26 you start fresh with personal outreach.

This protocol takes 15 minutes at 8pm Sunday. Do it before bed.

---

## Step 1 — Run the Reply Check (2 minutes)
```bash
python3 workers/check_replies.py
```

This will show you the exact state: replies, hot leads, open counts.

**If this returns API errors** (cloud blocked), log into Mixmax directly:
- Go to app.mixmax.com → Sequences → Property Managers
- Look for any "Replied" contacts

---

## Step 2 — If You Have Replies

For each reply, use this decision tree:

**"Interested / what's your pricing?"**
→ Respond within 30 minutes. Use: `outputs/tommy/touch3_reply_response_templates_2026-05-20.md` (Template A or B)
→ Goal: book a site visit or phone call for Monday May 26

**"Not the right person"**
→ Reply: "No problem — do you know who handles vendor decisions for the property? Happy to reach out to them directly."

**"We already have a vendor"**
→ Reply: "Totally understand. If they ever fall short or you're looking for a comparison quote, keep us in mind — we're in [their county] regularly."
→ Move to "Follow-Up" stage in pipeline_data.json with next_followup = 2026-08-01

**"Not interested"**
→ Move to "Closed Lost" in pipeline_data.json. No reply needed.

---

## Step 3 — If You Have 0 Replies

This means the 72-hour window closed with no response. Don't panic — it's common.

**Tonight (Sunday May 25) — do these in order:**

### 3a. Pause Instantly.ai (3 minutes)
This is the #1 suspected cause of 0 replies. Pausing it protects Round 2 from the same fate.
- Guide: `outputs/vera/instantly_pause_guide_2026-05-22.md`
- Go to app.instantly.ai → Campaigns
- Pause campaigns: a1c08c3d (PM Cuyahoga) + 626cd15d (Contractor Referral)
- Takes 2 clicks each. Done.

### 3b. Pull up your 5 hottest leads
From the `check_replies.py` output or Mixmax sequences — find the 5 contacts with the most email opens.

Write their names here (for Monday morning):
1. ___________________________
2. ___________________________
3. ___________________________
4. ___________________________
5. ___________________________

### 3c. Send LinkedIn connects to hot leads (5 minutes)
Look up each of the 5 on LinkedIn. Send a connect request with a personal note.

Note template:
```
Hi [firstName], noticed you manage properties in [county] — I do power washing for 
HOAs and commercial properties in that area. Would love to connect.
```

LinkedIn connects sent Sunday evening are seen Monday morning = perfect timing for the Monday pivot.

### 3d. Queue Monday morning bridge emails
Prep (don't send yet) personal Gmail emails to your top 3 hot leads.
Template: `outputs/tommy/hot_lead_bridge_email_may26_2026-05-22.md`

Set a 9am reminder to send these Monday. They go from your personal email — bypasses spam filters that may have killed the Mixmax sequence.

---

## Step 4 — Log the Window Close
Add to pipeline_data.json notes or your paper notes:
- Window closed: May 25 at 11:59pm
- Replies received: _____
- Hot leads (2+ opens): _____
- Instantly.ai paused: YES / NO
- LinkedIn connects sent: _____ names
- Bridge emails queued: YES / NO

---

## Step 5 — Set Your Monday Morning Alarm

**Monday May 26 — first 90 minutes:**
| Time | Task |
|------|------|
| 8:00am | Run `check_replies.py` one final time — sometimes people reply Sunday night |
| 8:15am | Run Danny Summit pull: `python3 workers/lead_pipeline.py danny Summit` |
| 8:30am | Send bridge emails to top 3 hot leads (from Step 3d) |
| 9:00am | Launch Facebook Ads (checklist: `outputs/vera/may26_ads_launch_checklist_2026-05-22.md`) |
| 9:30am | Text the Tier 1 contractors: `outputs/tommy/may26_monday_morning_followup_texts.md` |
| 10:00am | Create gas station Mixmax sequence (guide: `outputs/danny/gas_station_mixmax_sequence_creation_2026-05-23.md`) |

---

## If You Get a Late Reply (Sunday Night / Monday Morning)

Respond within 1 hour. Use the exact scripts in:
`outputs/tommy/touch3_reply_response_templates_2026-05-20.md`

**The fastest path to a booked job:**
1. Reply acknowledging their message (under 30 words — short = confident)
2. Propose a specific time: "Are you free for a 10-minute call Tuesday at 10am or 2pm?"
3. Once they confirm → send a quick estimate or book a site visit
4. Log in pipeline_data.json as "Replied" stage

---

## Reference Files
- Touch 3 reply templates: `outputs/tommy/touch3_reply_response_templates_2026-05-20.md`
- Bridge emails (May 26): `outputs/tommy/hot_lead_bridge_email_may26_2026-05-22.md`
- Monday texts: `outputs/tommy/may26_monday_morning_followup_texts.md`
- Ads launch checklist: `outputs/vera/may26_ads_launch_checklist_2026-05-22.md`
- Instantly.ai pause guide: `outputs/vera/instantly_pause_guide_2026-05-22.md`
- Gas station sequence creation: `outputs/danny/gas_station_mixmax_sequence_creation_2026-05-23.md`
