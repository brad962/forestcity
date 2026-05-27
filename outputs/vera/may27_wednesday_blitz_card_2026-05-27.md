# May 27 — Wednesday Morning Blitz
### 20 Contacts DUE TODAY | 90-Minute Action Card
*Vera Cole | Run 103*

---

## Why Today Matters
Ads launched May 26. Pipeline contacts have been prepped and waiting. Today is the biggest contact day of the season so far. Moving 5 of these contacts to "Replied" or "Estimate Sent" = $5,000–$20,000 in annual recurring revenue in motion.

---

## BLOCK 1 — Contacted Contractors (15 min)
*3 contacts already in conversation. Priority first.*

### Bryan | CLE Lawn Care Plus | 216-402-1924
**Status:** Contacted, 14+ days cold. Multiple approaches failed. This is the final window.

**Text (send NOW — do not wait for 9am):**
> "Hey Bryan — just wanted to close the loop. If the referral thing isn't the right fit right now, totally understand. No hard feelings at all. Good luck with the season."

**Why this works:** "Closing the loop" triggers ~30% late replies — people respond when they think the door is closing. If no reply by Friday May 29: update pipeline to Closed Lost, redirect energy to the 16 Wave 2 contractors.

**Pipeline update after sending:** stage = Contacted | last_contact = 2026-05-27 | next_followup = 2026-05-29

---

### Bulletproof Lawncare | 216-307-4344
**Status:** Contacted. Due for follow-up.

**Text:**
> "Hey — Bradley from Forest City Power Washing. Just following up from last week. Still interested in talking referrals? We're getting into peak season and have been getting calls from areas you guys are probably working. Happy to connect this week."

**Pipeline update:** last_contact = 2026-05-27 | next_followup = 2026-06-03

---

### Damrons Landscaping | 440-494-0422
**Status:** Contacted. Due for follow-up.

**Text:**
> "Hey — Bradley here from Forest City Power Washing. Following up on the referral partner idea. We're heading into the busiest stretch of the year — would love to get something set up. 5 minutes to talk this week?"

**Pipeline update:** last_contact = 2026-05-27 | next_followup = 2026-06-03

---

## BLOCK 2 — Tier 1 New Lead Contractors (20 min)
*5 contacts. First touch. Use the standard referral intro text.*

**Standard Tier 1 First Touch:**
> "Hey [Name] — this is Bradley with Forest City Power Washing in Northeast Ohio. We work alongside a lot of landscapers and contractors in the area. Wanted to reach out about a simple referral setup — we send work your way when we're at properties, you send it back when you see driveways or siding that need cleaning. No cost, no commitment. Worth a quick chat?"

| Contact | Company | Phone | Notes |
|---------|---------|-------|-------|
| Anthony | Land Pro Management | 440-320-2779 | Landscaper |
| Dontez | GTP Landscaping | 440-396-0814 | Landscaper |
| Chris | Twin Improvements | 216-773-0757 | Home services |
| Venus | Reliable Roofing and Restoration | 216-810-2497 | Roofer — sees roof algae every job |
| Logan | Pagels Quality Construction | 216-956-5263 | Construction |

**Pipeline update after each text:** stage = Contacted | last_contact = 2026-05-27 | next_followup = 2026-06-03

---

## BLOCK 3 — Gas Station Manual Email Blast (55 min)
*12 contacts. Mixmax sequence still PENDING. Manual Gmail while you wait.*

**⚠️ NOTE:** The Mixmax "Gas Station & C-Store Outreach" sequence ID is PENDING — you must create it in the Mixmax UI first. Until that's done, send manually via Gmail.

### Step 1: Open Gmail (5 min)
Compose a new email. You'll send individually (or BCC all 12 with merge fields if you use a Gmail send tool).

### Email Template — Gas Station & C-Store Outreach

**Subject:** Quick question — parking lot + canopy cleaning

> Hi [First Name],
>
> I'm Bradley with Forest City Power Washing — we clean commercial properties across Northeast Ohio (Cuyahoga, Summit, Lake, Lorain, Medina counties).
>
> I work with a few convenience store and gas station operators in the area and wanted to reach out. Fuel canopies, parking lots, and building facades take a beating — oil stains, exhaust film, algae on the concrete. Customers notice.
>
> If you're open to it, I'd love to do a quick walk of one of your locations and put together a free estimate. No commitment, just a number in your hands.
>
> Would that be worth 20 minutes?
>
> — Bradley Neal
> Forest City Power Washing
> (Your phone number)

---

### Gas Station Contacts (12 total):

| Name | Company | Email | Notes |
|------|---------|-------|-------|
| Jim Lavigne | Certified Oil Company | (find via Apollo) | |
| Kevin Kayden | Speedway | (find via Apollo) | Large chain |
| Mark Elyden | truenorth Convenience Stores | mark@truenorth? | ph: 440-792-4200 |
| Amer Odat | Open Pantry | (find via Apollo) | |
| Nicholas Goad | 7-Eleven | (find via Apollo) | Large chain |
| Shaher Hassanain | SUNOCO GAS STATION | (find via Apollo) | |
| Brian Koenig | Circle K | (find via Apollo) | Large chain |
| Douglas Petersen | Love's Travel Stops | (find via Apollo) | |
| Richard Gale | Giant Eagle | (find via Apollo) | GetGo brand |
| Carlton | Sheetz | (verify email — see note) | ⚠️ Email may be pcarlton@sheetz.com — verify before sending |
| Daryl Gibson | Marathon Petroleum | (find via Apollo) | |
| Bill Campana | Ferrellgas | (find via Apollo) | |

**⚠️ Sheetz note:** First name "Carlton" — email in system may be `pcarlton@sheetz.com` (previously corrected from garbled import). Verify before sending.

### Step 2: Create the Mixmax Gas Station Sequence (30 min) — do this WHILE waiting on replies

1. Go to mixmax.com → Sequences → New Sequence
2. Name: `Forest City Power Washing — Gas Station & C-Store Outreach`
3. Touch 1 (Day 1): Subject "Quick question — parking lot + canopy cleaning" — use email template above
4. Touch 2 (Day 5): Brief follow-up — "Just following up on the below — worth a quick conversation?"
5. Touch 3 (Day 10): Final — "Last one — if timing is off let me know and I'll reach back out in the fall."
6. Variables needed: `firstName`, `company`, `Phone`
7. After creating: copy the Sequence ID from the URL bar
8. Open `integrations/mixmax.py` line 54 — paste the ID where it says `'PENDING'`
9. Run: `python3 workers/lead_pipeline.py pending` — this enrolls all 12 contacts automatically

---

## BLOCK 4 — Prep for Tomorrow (5 min)
16 Wave 2 contractors due tomorrow (May 28). Same Tier 1 first-touch text as Block 2.
Companies: Pyro, Garten Gurus, Dales, C&M, Kays, Walkers, Clemence, Islander, Lawn Care for World, Soldan, Blue Line, Kardiac, Don't Move Improve, Woolworth, Everguard, Camlin.

---

## Revenue Math — Today's Actions
- 3 Contacted follow-ups → 1 converts → 3-8 jobs/year at $200-600 = **$600-$4,800/year**
- 5 Tier 1 texts → 2 convert → same math → **$1,200-$9,600/year**
- 12 gas station emails → 2 respond → 1 books → $1,200-$4,000/year per chain = **$2,400-$8,000/year**
- **Total potential from today's 90 minutes: $4,200-$22,400 in annual recurring revenue**

---

## Timeline
| Time | Action | Duration |
|------|--------|----------|
| 8:00am | Bryan close-loop text | 2 min |
| 8:05am | Bulletproof + Damrons texts | 5 min |
| 8:10am | 5 Tier 1 first-touch texts | 15 min |
| 8:30am | Gas station Gmail blast | 45 min |
| 9:15am | Create Mixmax Gas Station sequence | 30 min |
| DONE | | |

---

## After You're Done
- Update pipeline_data.json for each contact (stage, last_contact, next_followup)
- Summit County pull: 4 days left. Window is tomorrow (Thu May 28) or Friday. See `summit_county_4day_deadline_2026-05-27.md`
*Generated by Vera Cole | 2026-05-27*
