# Gas Station & C-Store — Manual Email Blast Templates
*Danny Malone | Outbound Sales Rep*
*Generated: 2026-05-20*

---

## Situation

18 gas station / c-store district managers and operators have been pulled from Apollo and are sitting in `pipeline_data.json`. Their Mixmax sequence is PENDING (Bradley needs to create it and paste the ID). 

Rather than letting these warm contacts go cold while waiting on the sequence setup, Bradley can send these emails manually from Gmail right now. One email to each contact. Takes about 30 minutes total.

**Why send now:** Memorial Day weekend is when gas stations and convenience stores see their highest traffic of the season. Canopy washing, pump island cleaning, concrete degreasing, and signage cleaning all become visible priorities. The facility managers are thinking about their properties right now.

---

## Target List

| Name | Title | Company | Email | Priority |
|------|-------|---------|-------|---------|
| Jim Lavigne | District Manager | Certified Oil Company | jlavigne@certifiedoil.com | Tier 1 |
| Kevin Kayden | District Manager | Speedway | kkayden@speedway.com | Tier 1 |
| Stephan Saumid | Senior District Manager | Speedway | ssaumid332@speedway.com | Tier 1 |
| Mark Elyden | President | truenorth Convenience Stores | melyden@truenorth.org | Tier 1 |
| John Borchert | Senior Operations Manager | truenorth Convenience Stores | jborchert@truenorth.org | Tier 1 |
| Amer Odat | President | Open Pantry | aodat@openpantry.com | Tier 2 |
| Nicholas Goad | Area Facilities Manager | 7-Eleven | nicholas.goad@7-11.com | Tier 2 |
| Kevin Hoffman | Area Facilities Manager | 7-Eleven | kevin.hoffman@7-11.com | Tier 2 |

Full list of 18 contacts: `outputs/danny/leads_gas_stations_2026-05-19.md`

---

## Email Template — District Managers

**Subject:** Power washing for [Company] locations in NE Ohio

**Body:**
> Hi [First Name],
>
> I run Forest City Power Washing — we handle exterior cleaning for commercial properties across Northeast Ohio.
>
> Reaching out because district managers like you often end up responsible for the appearance of several locations at once. Canopy washing, pump island degreasing, concrete cleaning, signage — most of our commercial accounts are on a monthly or quarterly schedule, so it's one call instead of chasing individual station managers.
>
> Do you handle exterior maintenance across your locations, or does each site manager handle that separately?
>
> Happy to come out for a free walkthrough of one location if that would help.
>
> — Bradley Neal
> Forest City Power Washing
> [phone number]

---

## Email Template — Area Facilities Managers (7-Eleven, larger chains)

**Subject:** Commercial power washing for [Chain] locations — NE Ohio

**Body:**
> Hi [First Name],
>
> I'm Bradley with Forest City Power Washing — we do exterior cleaning for commercial properties across Northeast Ohio.
>
> I noticed you manage facilities for [Chain] in this area. We work with several regional chains on scheduled cleanings — canopy washing, concrete degreasing, pump islands, signage. Monthly or quarterly contracts. We coordinate with local staff so you don't have to.
>
> If exterior maintenance at your locations is something you or your team manages, I'd love to put a proposal together. No obligation — just a quick conversation.
>
> Worth 15 minutes this week or next?
>
> — Bradley Neal
> Forest City Power Washing
> [phone number]

---

## Email Template — Station Owners (shorter, direct)

**Subject:** Power washing for your station — Forest City

**Body:**
> Hi [First Name],
>
> Bradley with Forest City Power Washing. We clean canopies, pump islands, concrete, and building exteriors for gas stations across NE Ohio.
>
> One visit usually runs $250–$500 depending on size. Most stations book a seasonal cleaning before Memorial Day or 4th of July when traffic peaks.
>
> Interested in a free quote for your location?
>
> — Bradley Neal
> Forest City Power Washing
> [phone number]

---

## Sending Instructions

1. **Open Gmail.** Paste the appropriate template for each contact type.
2. **Personalize three things:** First name, company name, and one specific detail if you know it (e.g., "I noticed you have several locations in Cuyahoga County").
3. **Send from your personal work email** — not a bulk sender. These go one at a time.
4. **BCC yourself** on each so you have a record.
5. **Do NOT use "Hi there"** — always use their first name from the table above.

### Tier 1 targets (send these first — highest value):
1. Jim Lavigne — Certified Oil (district manager, regional chain)
2. Kevin Kayden + Stephan Saumid — Speedway (two separate DMs)
3. Mark Elyden + John Borchert — truenorth (decision-maker and ops manager)
4. Amer Odat — Open Pantry (president, small chain, easy to reach)

---

## After the Mixmax Sequence Goes Live

Once Bradley creates the sequence in Mixmax UI and pastes the ID into `integrations/mixmax.py` (line 54, replace `'PENDING'` with the real ID), the next run of `lead_pipeline.py` will automatically enroll all 18 contacts. Until then, these manual emails provide direct outreach coverage.

**Sequence copy:** `outputs/danny/sequence_gas_stations_2026-05-19.md`

---

*Danny Malone — Outbound Sales Rep | Forest City Power Washing AI Office*
