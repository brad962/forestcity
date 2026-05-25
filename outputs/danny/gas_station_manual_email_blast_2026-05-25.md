# Gas Station / C-Store — Direct Gmail Blast Guide
### Created 2026-05-25 | Danny Malone | Outbound Sales
*Bypasses the PENDING Mixmax sequence. Send from Bradley's personal Gmail NOW.*

---

## WHY THIS FILE EXISTS

18 gas station district manager contacts have been sitting idle since May 19. That's 5+ weeks with zero outreach.

The Mixmax sequence for this segment is still PENDING (no sequence ID in Mixmax UI yet). But we don't need Mixmax to email them. Bradley can send from Gmail directly — no automation required. One by one or BCC'd in batches of 5-6. Takes about 20 minutes total.

Gas station district managers are **multi-site decision-makers**. One yes = recurring exterior cleaning at 5–15 locations. That's $2,400–$6,000/yr per account.

---

## SEND SCHEDULE

| Wave | When | Contacts | Estimated Time |
|------|------|----------|----------------|
| Wave 1 — Tier 1 | May 26 (Tuesday AM) | 7 contacts | 10 min |
| Wave 2 — Tier 2 | May 28 (Thursday AM) | 11 contacts | 10 min |
| Follow-up | June 2 (Tuesday) | Non-responders from Wave 1 | 5 min |

**Best send time:** Tuesday–Thursday 8–10am. District managers check email in the morning before site visits.

---

## TIER 1 — SEND WAVE 1 (May 26 Tuesday)

These are the highest-value targets: regional chains, senior DMs, presidents.

| # | Name | Title | Company | Email |
|---|------|-------|---------|-------|
| 1 | Jim Lavigne | District Manager | Certified Oil Company | jlavigne@certifiedoil.com |
| 2 | Kevin Kayden | District Manager | Speedway | kkayden@speedway.com |
| 3 | Stephan Saumid | Senior District Manager | Speedway | ssaumid332@speedway.com |
| 4 | Mark Elyden | President | truenorth Convenience Stores | melyden@truenorth.org |
| 5 | John Borchert | Senior Operations Manager | truenorth Convenience Stores | jborchert@truenorth.org |
| 6 | Amer Odat | President | Open Pantry | aodat@openpantry.com |
| 7 | Nicholas Goad | Area Facilities Manager | 7-Eleven | nicholas.goad@7-11.com |

---

## EMAIL TEMPLATES — USE THESE VERBATIM

### TEMPLATE A — For District Managers and Facilities Managers
**Subject:** Exterior cleaning for [Company] locations in NE Ohio

```
Hi [First Name],

I'm Bradley with Forest City Power Washing. We handle exterior cleaning for commercial operators across Northeast Ohio — gas station canopies, pump islands, concrete degreasing, building facades.

I know district managers deal with a lot of vendors. Here's why this one is worth 5 minutes:

One contract covers all your NE Ohio locations. We build the schedule around your operations — no shutdowns, no surprises. One invoice, one point of contact.

If you've got locations that need a refresh before summer, I'd like to put together a site-by-site quote. Happy to start with one pilot location if you want to see the work first.

Worth a quick call?

Bradley Neal
Forest City Power Washing
216-[your number]
forestcitypowerwashing.com
```

---

### TEMPLATE B — For Presidents / Owners
**Subject:** Exterior maintenance for [Company]'s NE Ohio locations

```
Hi [First Name],

Bradley here from Forest City Power Washing. We do exterior cleaning for commercial properties across all 7 NE Ohio counties.

For c-store and fuel operators, we handle:
- Canopy washing (diesel soot, weathering)
- Pump island and concrete degreasing
- Building facade washing
- Multi-site scheduling so everything stays on cycle

One point of contact, one contract, consistent results across locations.

I'd love to put together a proposal for [Company]'s NE Ohio footprint. Would a 15-minute call this week make sense?

Bradley Neal
Forest City Power Washing
216-[your number]
```

---

### TEMPLATE C — Follow-Up (Day 7, for non-responders)
**Subject:** Re: exterior cleaning for [Company] locations

```
Hi [First Name],

Circling back on exterior cleaning for [Company].

If this isn't the right time, no problem — I'll check back in the fall when sites need pre-winter cleaning.

If you do want to talk before summer, I have a few slots open this week.

Bradley Neal
Forest City Power Washing
216-[your number]
```

---

## HOW TO SEND (Step by Step)

### Option 1: Individual emails (recommended — highest reply rate)
1. Open Gmail
2. Click Compose
3. To: [paste email]
4. Subject: [paste subject, replace [Company] with company name]
5. Body: [paste template, fill in [First Name] and [Company]]
6. Send
7. Repeat for next contact

**Time per email: ~90 seconds once you're in a rhythm.**

### Option 2: BCC batch (faster, slightly lower reply rate)
1. Open Gmail → Compose
2. BCC: [paste all Tier 1 emails, comma-separated]
3. **Remove any company-specific personalization** — keep it generic
4. Use Template A without the [Company] fill-in: "your NE Ohio locations"
5. Send all 7 at once

**Use Option 1 for Tier 1 (7 contacts). Use Option 2 for Tier 2 (11 contacts).**

---

## TIER 2 — SEND WAVE 2 (May 28 Thursday)

| # | Name | Title | Company | Email |
|---|------|-------|---------|-------|
| 8 | Kevin Hoffman | Area Facilities Manager | 7-Eleven | kevin.hoffman@7-11.com |
| 9 | Dave Harrington | District Manager | Sunoco | dharrington@sunoco.com |
| 10 | Tom Winans | District Manager | Sunoco | tom.winans@sunoco.com |
| 11 | Ryan Lissick | Senior District Manager | Speedway | rlissick@speedway.com |
| 12 | Christopher Reno | Area Manager | Marathon Petroleum | christopher.reno@marathonpetroleum.com |
| 13 | Mike Strevel | Regional Director | Ferrellgas | mstrevel@ferrellgas.com |
| 14 | Rachel Winsor | Director of Operations | Open Pantry | rwinsor@openpantry.com |

*[Remaining 4 contacts from the 18 don't have confirmed emails — skip or try LinkedIn InMail.]*

---

## AFTER SENDING — WHAT TO TRACK

When a reply comes in, move to the NEXT STEP:
1. **Interested / wants a quote:** Reply within 1 hour. Use `outputs/tommy/quote_to_close_kit_[date].md` for the discovery call script and quote email template.
2. **"Not right now":** Log in pipeline_data.json with stage = "Contacted", next_followup = September 1. Gas stations often budget for fall cleaning.
3. **Wrong person / bounced:** Note the correct contact if they mention one. Search LinkedIn for the right DM.
4. **No reply after 7 days:** Send Template C follow-up.

---

## WHAT HAPPENS AFTER THE MIXMAX SEQUENCE GOES LIVE

Once Bradley creates the Gas Station sequence in Mixmax UI (guide: `outputs/danny/gas_station_mixmax_sequence_creation_2026-05-23.md`) and pastes the ID into `integrations/mixmax.py`:

```bash
python3 workers/lead_pipeline.py pending
```

This auto-enrolls the 18 contacts into the sequence. Anyone who already replied via Gmail would need to be marked `mixmax_enrolled: true` manually in pipeline_data.json to prevent re-enrollment.

---

## REVENUE MATH

- 18 contacts reached → typical 15–20% reply rate from District Managers = **3–4 replies**
- 3 replies → 1–2 site visits → 1 closed account (conservative)
- 1 gas station account = 5–15 locations × $150–$400/visit × 2 visits/year = **$1,500–$12,000/yr**
- Best case (truenorth, Speedway, 7-Eleven): multi-year recurring contract

**This is the highest per-contact revenue potential in the entire pipeline. 20 minutes of effort.**

---

*Danny Malone | Forest City AI Office | Generated 2026-05-25*
