# Contractor LinkedIn Revival — Fresh Channel Approach
### 2026-05-26 | Vera Cole | Run 96
*For stale contractors who haven't replied to texts/calls — LinkedIn is a completely different psychology*

---

## Why LinkedIn Now

Bryan at CLE Lawn Care Plus = 14+ days since last contact. Bulletproof, Damrons = 7+ days.
Texts feel casual. LinkedIn feels professional. When a contractor gets a LinkedIn connection + message from another local business owner, they read it differently. It's not spam — it's a peer.

**Use this AFTER texts haven't gotten a reply.** It's not a replacement — it's a second channel.

---

## Step 1: Find them on LinkedIn (2 min)

Search: `[First Name] [Last Name] [Company Name] landscaping Cleveland`
Or go to linkedin.com/in/ and search the company name.

If you can't find them on LinkedIn, skip to the "cold reconnect text" below.

---

## LinkedIn Messages (after connecting)

### Bryan — CLE Lawn Care Plus (14+ days cold)
**Connection request note (300 chars max):**
> Hey Bryan — Bradley Neal here, Forest City Power Washing. We work with a lot of landscapers in NE Ohio on a referral swap — figured it's worth a quick connect. No pitch, just wanted to be on your radar.

**Follow-up DM (send same day they accept):**
> Thanks for connecting, Bryan. I'll keep it short — we're doing exterior cleaning for several landscaping customers in the area and consistently hear "do you know a good landscaper?" We'd love to send those your way. And when your customers ask about cleaning driveways, roofs, or siding, we'd appreciate the same. No paperwork, just a $50 referral fee per closed job. Worth a quick chat?

---

### Bulletproof Lawncare (7+ days cold)
**Connection request note:**
> Hey — Bradley from Forest City Power Washing. We work alongside several lawn care companies in NE Ohio on a referral swap. Figured it's worth connecting — happy to share more if interested.

**Follow-up DM:**
> Thanks for connecting. Quick version: we regularly work with landscapers' customers on pressure washing and exterior cleaning. When your customers ask who to call for driveways, siding, or roof cleaning, we'd love to be the name you give. We return the favor with $50 per closed referral. Our customers ask about landscapers constantly. Want to set up something informal?

---

### Damrons Landscaping (7+ days cold)
**Connection request note:**
> Bradley from Forest City Power Washing here — we work with a few NE Ohio landscapers on referral swaps. Thought it was worth connecting.

**Follow-up DM:**
> Thanks for the connect. Short version: we do exterior cleaning (house wash, roof, driveway, commercial) for homeowners across NE Ohio. Your customers probably ask about pressure washing all the time — we'd love to handle those calls and return the favor with landscaper referrals and $50 per job. No formal contract. Just a handshake deal that pays for both of us. Interested?

---

## Step 2: Update pipeline_data.json after sending

Find each contact and update:
```json
{
  "last_contact": "2026-05-27",
  "notes": "LinkedIn connection request sent + DM — follow up in 5 days if no reply",
  "next_followup": "2026-06-01"
}
```

---

## If They Accept + Don't Reply Within 5 Days

Send one more DM:
> Hey [Name] — just wanted to make sure my last message didn't get buried. Happy to grab a 5-min call whenever is good for you, or just a quick reply works too. Either way, appreciate the connect.

After that, move to "Closed Lost — try again in 90 days."

---

## If They Reply YES

Use `outputs/tommy/contractor_referral_text_script_[date].md` for next steps.
Add to pipeline_data.json: stage → "Replied", next_followup → 5 days out for onboarding.

---

## Tier 1 New Leads — LinkedIn as Parallel Outreach

For the 5 Tier 1 New Lead contractors (Land Pro, GTP, Twin, Reliable, Pagels) who haven't received a personal text yet:
→ Send the text FIRST (it's warmer and faster)
→ THEN connect on LinkedIn same day

A contact who gets a text AND a LinkedIn connect in the same 24-hour window has 3× higher recall when you follow up.

Numbers for the texts: `outputs/vera/launch_day_contractor_outreach_stack_2026-05-26.md`

---

*This is Run 96's fresh angle on the Bryan issue. All previous outreach (6 deliverables) used text/call channel only. LinkedIn is a completely different context — professional platform, different psychological framing, no spam filter.*
