# Gas Station & Fleet Washing — Complete Sequence Copy
## Bradley: Paste This Directly Into Mixmax (10 Minutes)
*Vera Cole | Run 203 | June 12, 2026 — Day 28 of blocker*

---

> 🚨 **The hold-up:** You have 100+ gas station + fleet washing contacts sitting in contacts_cache.json UNENROLLED since May 15. They've received zero emails. Summit, Medina, AND Cuyahoga gas station / fleet contacts — all waiting. Lake County fires June 15 and will add more.
>
> **Previous fix guides asked you to "create a sequence in Mixmax UI."** That was too vague.
> **This guide gives you the COMPLETE EMAIL TEXT — just paste it in.**

---

## ⏱️ The 10-Minute Fix

**Step 1 (1 min):** Go to [app.mixmax.com/sequences](https://app.mixmax.com/sequences) → click **+ New Sequence**

**Step 2 (4 min):** Create Gas Station sequence — copy/paste the 3 emails below

**Step 3 (1 min):** Copy the sequence ID from the URL → paste into `integrations/mixmax.py` line 54

**Step 4 (3 min):** Repeat for Fleet sequence — copy/paste the 3 emails below

**Step 5 (1 min):** Copy Fleet sequence ID → paste into `integrations/mixmax.py` line 48

**Done.** Run `python3 workers/lead_pipeline.py pending` to enroll 100+ waiting contacts.

---

## SEQUENCE 1: Forest City Power Washing — Gas Station & C-Store Outreach

**Sequence Name:** `Forest City Power Washing — Gas Station & C-Store Outreach`
**Variables to create:** `firstName`, `company`, `Phone`

---

### Touch 1 — Day 0 (Send immediately)

**Subject:** `Quick question about {{company}}'s lot`

**Body:**
```
Hi {{firstName}},

Quick question — who handles the exterior cleaning and lot maintenance for {{company}}?

I run Forest City Power Washing and we specialize in fuel station and convenience store lots across Northeast Ohio. Canopy staining, fuel pad concrete, and dumpster areas are our bread and butter.

Most of our gas station clients run us quarterly — keeps the lot inspection-ready and the curb appeal up.

Would a quick estimate make sense?

Bradley Neal
Forest City Power Washing
Northeast Ohio
{{Phone}}
forestcitypowerwashing.com
```

---

### Touch 2 — Day 5

**Subject:** `Re: {{company}}'s lot — one more thought`

**Body:**
```
Hi {{firstName}},

Wanted to follow up briefly.

I know fuel station lots take a beating — fuel drips, road grime, rust from the canopy supports, and the area around the dumpster. Most of the station managers I work with say the #1 thing customers notice before they even get out of the car is whether the lot looks clean.

We do quarterly service for several stations in the area and can usually get it done on a slow morning without disrupting operations.

Happy to put together a quick estimate — no commitment, just a number.

Bradley
Forest City Power Washing
{{Phone}}
```

---

### Touch 3 — Day 12 (Final)

**Subject:** `{{company}} — last note from me`

**Body:**
```
Hi {{firstName}},

Last note — I don't want to keep filling up your inbox.

If the timing is off or you have someone handling this already, no worries at all. But if your lot is due for a cleaning before summer gets into full swing, we're booking into late June and July now and I'd love to get {{company}} on the schedule.

Either way, feel free to reach out anytime.

Bradley Neal
Forest City Power Washing
{{Phone}}
forestcitypowerwashing.com
```

---

## SEQUENCE 2: Forest City Power Washing — Fleet Washing Outreach

**Sequence Name:** `Forest City Power Washing — Fleet Washing Outreach`
**Variables to create:** `firstName`, `company`, `fleetType`, `Phone`

---

### Touch 1 — Day 0

**Subject:** `Fleet washing for {{company}}`

**Body:**
```
Hi {{firstName}},

I run Forest City Power Washing and we handle fleet exterior washing for service companies across Northeast Ohio — trucks, vans, trailers, heavy equipment.

Most fleet managers I work with schedule us monthly or quarterly depending on route density. We work around your vehicles' schedule and can do a full fleet wash at your yard or depot overnight.

Does {{company}}'s {{fleetType}} fleet have a regular exterior wash schedule right now?

Bradley Neal
Forest City Power Washing
{{Phone}}
forestcitypowerwashing.com
```

---

### Touch 2 — Day 5

**Subject:** `Re: {{company}} fleet — quick follow-up`

**Body:**
```
Hi {{firstName}},

Wanted to circle back quickly.

Clean fleet vehicles make a real impression on customers — especially for service businesses where the truck showing up at someone's home is part of the brand. A lot of the fleet managers we work with tell us the same thing: they've been meaning to get a regular schedule in place, they just haven't prioritized it.

We handle everything from pickup trucks to tractor-trailers and can be completely flexible on timing. Happy to come out, look at your fleet, and give you a flat per-vehicle number.

Bradley
Forest City Power Washing
{{Phone}}
```

---

### Touch 3 — Day 12 (Final)

**Subject:** `{{company}} fleet — last note`

**Body:**
```
Hi {{firstName}},

Last follow-up from me on this.

If fleet washing isn't a priority right now or you have it covered, I completely understand. But if your vehicles could use a good exterior clean before the summer season gets into full swing — we're taking on new fleet clients in June and July.

Feel free to reach out whenever the timing works.

Bradley Neal
Forest City Power Washing
{{Phone}}
forestcitypowerwashing.com
```

---

## After Creating Both Sequences

1. **Copy the Gas Station sequence ID** from the URL (looks like: `6a048xxx...`)
2. Open `integrations/mixmax.py` → find line 54 (the `'id': 'PENDING'` for `gas_station`)
3. Replace `'PENDING'` with the sequence ID
4. **Copy the Fleet sequence ID** from the URL
5. Find line 48 (the `'id': 'PENDING'` for `fleet_washing`)
6. Replace `'PENDING'` with the Fleet sequence ID
7. Run: `python3 workers/lead_pipeline.py pending`

**100+ contacts enrolled in under 10 minutes from when you create the sequences.**

---

*This deliverable was created because previous fix guides described WHAT to do, not HOW to do it with specific copy. Every day these contacts sit unenrolled = lost peak season revenue. Gas stations and fleet companies book recurring quarterly contracts — one enrolled gas station chain DM = $15K–$45K/year.*
