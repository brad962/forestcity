# Fleet Washing Outreach Sequence
### Forest City Power Washing | Created 2026-05-18
*Danny Malone | Outbound Sales*

---

## Sequence Name (enter exactly in Mixmax)
**Forest City Power Washing — Fleet Washing Outreach**

## Variables Required
- `firstName`
- `company`
- `fleetType` (trucks / equipment / vans / vehicles)
- `Phone`

## Target Contacts
- Fleet managers, operations managers, logistics directors
- Shop foremen, general managers at trucking/landscaping/construction companies
- Municipal fleet managers (county, city, township)
- Companies in NE Ohio with 3+ vehicles: landscaping, trucking, utilities, delivery, tree service, HVAC, plumbing, roofing crews

---

## TOUCH 1 — Day 0
**Subject:** Your fleet is your business card, {{firstName}}

**Body:**
Hi {{firstName}},

Every truck that rolls out from {{company}} is a moving advertisement.

When it's clean, people notice. When it's not — they notice that too.

I'm Bradley with Forest City Power Washing in NE Ohio. We handle recurring fleet washing for local companies — on-site at your lot, scheduled around your operation so you're never down a vehicle.

Would it make sense to get a quick quote for {{company}}'s {{fleetType}}?

— Bradley
Forest City Power Washing
{{Phone}}

---

## TOUCH 2 — Day 5
**Subject:** Re: fleet washing for {{company}}

**Body:**
Hi {{firstName}},

Wanted to follow up on fleet washing for {{company}}.

A few things we do that most guys don't:

→ We come to you — no dropping vehicles off
→ We work around your schedule — early morning, weekends, whatever works
→ Monthly contracts available so it's one less thing to think about
→ We use the right soap for each surface — no streaking, no damage to lettering or decals

We've worked with landscaping crews, tree services, and contractors across NE Ohio. Happy to send references.

Worth a 10-minute call this week?

— Bradley
{{Phone}}

---

## TOUCH 3 — Day 12
**Subject:** Last note — {{company}} fleet washing

**Body:**
Hi {{firstName}},

I'll keep this short — last note from me on fleet washing.

If keeping the {{company}} fleet clean is something on your radar, I'd love to put a number together. No obligation, no pressure.

If the timing's off, no worries at all — I'll check back in a few months.

Either way, feel free to reach out anytime.

— Bradley
Forest City Power Washing
{{Phone}}

---

## HOW TO CREATE THIS IN MIXMAX

1. Go to **app.mixmax.com → Sequences → New Sequence**
2. Name it exactly: `Forest City Power Washing — Fleet Washing Outreach`
3. Add 3 stages using the email copy above
   - Stage 1: Delay = 0 days
   - Stage 2: Delay = 5 days
   - Stage 3: Delay = 12 days
4. Set variables: `firstName`, `company`, `fleetType`, `Phone`
5. Save and copy the Sequence ID from the URL
6. Send the ID to Claude — it will wire up the rest automatically

---

## WHAT HAPPENS AFTER YOU ADD THE ID

Once you provide the Mixmax sequence ID, the following will be updated automatically:

- `integrations/mixmax.py` — new `fleet_washing` entry in SEQUENCES dict
- `workers/lead_pipeline.py` — new `run_fleet()` function targeting fleet operators
- `agents/danny.md` — fleet washing Apollo pull parameters
- Lead type detection keywords added for: fleet manager, operations manager, logistics, trucking, delivery

### Apollo Search Parameters (ready to run once wired up)
```json
{
  "person_titles": [
    "fleet manager", "operations manager", "logistics manager",
    "shop foreman", "general manager", "fleet supervisor",
    "transportation manager", "equipment manager"
  ],
  "organization_industry_tag_ids": [],
  "person_locations": [
    "Cuyahoga County, Ohio", "Geauga County, Ohio",
    "Lake County, Ohio", "Lorain County, Ohio",
    "Portage County, Ohio", "Summit County, Ohio",
    "Medina County, Ohio"
  ],
  "per_page": 50
}
```

### Known Manual Targets (from Newbury Township tree companies)
| Company | Contact | Phone |
|---------|---------|-------|
| VanCuren Tree Service | David VanCuren | (440) 338-5005 |
| Ripley Tree Service LLC | Mike Ripley | (440) 463-7379 |
| Independent Tree LLC | Alan Kraus | (440) 367-8119 |
| Veneer Tree Service | Mark Gamiere | (216) 956-8149 |
| Dash Tree Service Inc | Dave Pitz | (440) 564-5925 |
| Reid's Tree Care | — | (440) 564-7878 |
