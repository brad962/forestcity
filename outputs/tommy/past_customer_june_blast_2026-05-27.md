# Past Customer June Blast — Action Card
### May 27, 2026 | Tommy Greer | Copywriter

---

## Why Now — Not June 4

Ads launched May 26. The fastest ROI path is NOT strangers clicking ads — it's people who already paid you and know your work. One text to 5 past customers can book a job THIS WEEK while the ad algorithm warms up.

Don't wait until June 4's big enrollment blitz. **Send today. Send tomorrow. Send before the weekend.**

---

## The Texts (Copy-Paste Ready)

**Text 1 — House Washing (most common)**
> Hey [Name], it's Bradley at Forest City Power Washing. We washed your house last [year/season] — you still on the annual plan? Slots are filling fast this month. Reply back and I'll get you on the schedule.

**Text 2 — If they did driveway or deck before**
> Hey [Name], it's Bradley with Forest City. Just checking in — that driveway/deck we did for you last [year/season], due for a refresh? We're booking into June now. Let me know.

**Text 3 — Annual Plan Upsell (hadn't done annual plan)**
> Hey [Name], Bradley at Forest City Power Washing. Had a quick idea — we started an annual plan this year (spring + fall for one flat rate) and a few of your neighbors in [area] are already on it. Interested? Takes 2 minutes to set up.

**Text 4 — If you haven't texted them in 12+ months**
> Hey [Name] — Bradley from Forest City. Don't want to bug you but wanted to reach out before summer fills up. Are you due for a house wash this year? Happy to swing by and give you a quick look.

**Text 5 — Referral ask (if they were a great customer)**
> Hey [Name], Bradley at Forest City. Hope you're doing well. Any chance you know someone who needs their house/driveway washed this summer? I'm offering $50 to anyone who refers a job to us. Just wanted to put it out there.

---

## Who to Text

Open Workiz and look for any job marked "Done" or "Completed" in 2024 or early 2025. These are your targets.

Priority order:
1. Customers who paid in full on time — easiest re-book
2. Customers who had multiple services done — annual plan candidates
3. Customers in neighborhoods where you want more work — neighbor canvass potential

---

## Response Handling

**"Sure, what's your availability?"**
→ Reply: "I have a few spots opening up the week of June 2. What day works? I'll send you a quick quote first."

**"How much?"**
→ Reply: "For a house your size it's usually around $[X] depending on the details. Want me to drive by this week and give you an exact number? Takes 5 min."

**"Not right now"**
→ Reply: "No problem! I'll reach out again in the fall. Have a great summer." (They're still in the pipeline — don't delete.)

**No reply after 48 hours**
→ Send one follow-up: "Hey [Name] — just wanted to make sure my text came through. No pressure either way, just checking in."

---

## Update pipeline_data.json

After each text, log it:
```json
{
  "id": "past_[first_last]",
  "first_name": "[Name]",
  "last_name": "",
  "company": "",
  "phone": "[number]",
  "email": "",
  "lead_type": "residential",
  "stage": "Contacted",
  "last_contact": "2026-05-27",
  "next_followup": "2026-05-29",
  "notes": "Past customer re-engagement text sent May 27"
}
```

---

## Revenue Math

5 past customers texted → typical 40–60% re-book rate
3 booked jobs × average $350 = **$1,050 this week**
1 annual plan upsell × $450 = **$450 recurring x2/year**
1 referral converts → **$300–$500 bonus job**

Total potential: **$1,800–$3,000 from 30 minutes of texts**

---

*Written by Tommy Greer | May 27, 2026*
*Use alongside `past_customer_reengagement` and `annual_plan_pitch_script_2026-05-26.md`*
