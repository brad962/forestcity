# Gas Station & C-Store — Ready-to-Send Email Copy
*Written by Vera (on behalf of Tommy) | June 3, 2026 | Run 187*
*Purpose: 12 contacts have been sitting idle since May 19. Use this TODAY.*

---

## Why This Exists

The gas station/fleet Mixmax sequences are still PENDING (no ID yet — Bradley needs to create them in Mixmax UI). But 12 gas station contacts have been waiting 15+ days with zero outreach.

**New approach:** Skip Mixmax for now. Send direct from Gmail. This is a manual 3-touch sequence — copy/paste text below, BCC all 12, done in 10 minutes.

---

## The 12 Gas Station Contacts

Check `pipeline_data.json` → `manual_contacts` (type: `gas_station`).
Or check `contacts_cache.json` for `_lead_type: gas_station`.

Extract their emails. BCC all of them in Gmail (never CC — they shouldn't see each other).

---

## Touch 1 — Send Today, June 4

**Subject:** Quick question about your lot

---

Hi [First Name],

I run a commercial power washing operation in Northeast Ohio — we handle parking lots, canopies, and building exteriors for gas stations and C-stores from Cleveland to Akron.

Quick question: who handles the maintenance on your lot and canopy?

Most operators I talk to are either doing it in-house (and it takes forever) or it just never gets done because there's no vendor set up. We specialize in this — fuel islands, canopy fascia, concrete aprons, dumpster areas. In and out in 2-3 hours, early morning before your rush.

Worth a 5-minute call?

— Bradley Neal
Forest City Power Washing
[phone]

---

## Touch 2 — Send June 9 (5 Days Later)

**Subject:** Re: Quick question about your lot

---

Hi [First Name],

Just circling back on this.

We just finished a job at a BP station in [nearby city] — their fuel island concrete was pretty bad, covered in 3 years of drip and grime. They had it done in one morning and said it "looked like a new station." Their words.

If you've been putting this off, now's actually the right time — summer traffic is picking up, and the lot takes more of a beating in high season.

Happy to do a free walkthrough and quote this week. What day works?

— Bradley

---

## Touch 3 — Send June 16 (7 Days After Touch 2)

**Subject:** Last one from me

---

Hi [First Name],

I'll keep this short — reaching out one last time about power washing for your station.

If now's not the right time, no problem. We're running through our summer schedule and booking 4-6 weeks out, so if you want a late July or August date, now's when to lock it.

Reply with "interested" or "not now" and I'll act accordingly.

— Bradley
Forest City Power Washing
[phone]

---

## Send Instructions

1. Open Gmail
2. Compose new email
3. Subject: "Quick question about your lot"
4. Paste Touch 1 text
5. Replace `[First Name]` with the first name of ONE contact (send individually, or BCC)
6. **BCC all 12 gas station email addresses** (they won't see each other)
7. Send

> **Tip:** If sending to multiple contacts with different first names, use "Hi there" instead of "[First Name]" in the BCC version. Or send 12 individual emails — takes 4 extra minutes but higher reply rate.

---

## After Sending — Log It
Add to `logs/activity.log`:
```
[2026-06-04 08:45] Danny | Gas station Touch 1 manual Gmail blast — 12 contacts | pipeline_data.json | Done
```

---

## Creating the Mixmax Sequence (Do This Once — Unlocks Auto-Enrollment)

When you're ready to build the sequence properly in Mixmax:

1. Open [mixmax.com](https://mixmax.com) → Sequences → New Sequence
2. Name it: "Gas Station & C-Store Outreach"
3. Add 3 steps using the copy above (Touch 1 = Day 0, Touch 2 = Day 5, Touch 3 = Day 12)
4. Copy the sequence ID from the URL (looks like `6a048cfc110bc620ca0f1xxx`)
5. Open `integrations/mixmax.py` line 55 — change `'id': 'PENDING'` to `'id': 'YOUR_ID_HERE'`
6. Run: `python3 workers/lead_pipeline.py pending`
7. All 12 contacts auto-enroll immediately

**One-time setup. 15 minutes. Unlocks auto-enrollment for all future gas station leads.**

---

## Fleet Washing Sequence (Same Situation)

Same approach applies. Check `pipeline_data.json` for `_lead_type: fleet_washing` contacts.
Fleet sequence copy is needed — ask Tommy to write it if not already done.
Fleet Mixmax ID lives at `integrations/mixmax.py` line 48.
