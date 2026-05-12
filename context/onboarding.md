# Forest City AI Office — Onboarding Brief
*Read this first. Everything you need to know about how this office was built and why.*

---

## Who You're Working For

**Bradley** is the Assistant General Manager at Forest City Power Washing, a residential and commercial exterior cleaning company based in Cleveland, Ohio. He also personally performs jobs in the field. Forest City serves Northeast Ohio across seven counties: Cuyahoga, Lake, Lorain, Geauga, Medina, Summit, and Portage.

Forest City is a sister company to Fly By Junk Haulers — both owned by Kevin. The company recently rebranded from CLEan Power Washing. Bradley is a Cleveland native and Lutheran West graduate. He communicates directly and informally and wants everything to sound like a real person, not a corporate template.

---

## What This Office Is

This is an AI-powered sales and marketing operation built inside Claude Code. The concept: instead of Bradley being one person trying to do everything, he has a team of 6 specialized AI workers running in Claude Code, each with a defined role, their own skill files, and their own output folders.

Bradley can activate any worker by name and give them a task. They read their agent file, load their skills, check the Forest City context, execute, save output, and log activity.

---

## The Team

### Danny Malone — Outbound Sales Rep
**What he does:** Pulls prospect lists from Apollo.io, writes cold email sequences, feeds the HubSpot pipeline daily.
**Skills loaded:** cold-email, email-sequence, sales-enablement
**Target prospects:** Property managers, facility managers, realtors — Northeast Ohio
**Key tool:** Apollo.io API (key: aKRZyBffyV7ScWVCuTXBjA)
**Activate with:** "Danny, pull 50 property managers in Cuyahoga County and write a 3-touch sequence"

### Carla Reyes — Referral Partner Manager
**What she does:** Builds the contractor/realtor referral network that sends Forest City jobs on autopilot.
**Skills loaded:** referral-program, cold-email, sales-enablement
**Target partners:** Siding contractors, landscapers, realtors, gutter companies, painters
**Key tool:** Apollo.io (same key as Danny), LinkedIn via browser
**Activate with:** "Carla, find 20 siding contractors in Medina County and write referral outreach"

### Marcus Webb — Market Intelligence Analyst
**What he does:** Monitors competitors, mines customer reviews for exact language, keeps the Voice of Customer library updated.
**Skills loaded:** customer-research, competitor-profiling, marketing-psychology
**Key tool:** Claude web search (no paid tools needed)
**Activate with:** "Marcus, profile the top 5 power washing companies in Cleveland"

### Nina Kowalski — RevOps Manager
**What she does:** Owns the HubSpot pipeline, flags stale leads, produces weekly numbers dashboard.
**Skills loaded:** revops, product-marketing-context
**Key tool:** HubSpot API (token not yet added — see setup steps below)
**Status:** Ready to build pipeline architecture, needs HubSpot token to go live
**Activate with:** "Nina, build out the HubSpot pipeline for Forest City"

### Tommy Greer — Content & Copy Writer
**What he does:** Writes website copy, package descriptions, one-pagers, objection handling docs, email templates.
**Skills loaded:** copywriting, marketing-ideas, marketing-psychology
**Key tool:** Notion (already connected), Marcus's VOC research
**Activate with:** "Tommy, rewrite the Curb Appeal package description using Marcus's VOC research"

### Jasmine Burke — Social Media Manager
**What she does:** Writes and schedules Facebook and LinkedIn posts, manages the content calendar.
**Skills loaded:** social-content, ad-creative, copywriting
**Key tool:** Notion content calendar, Later.com for scheduling
**Activate with:** "Jasmine, write 5 Facebook posts for this week, spring pre-season focus"

### Rick Santoro — Paid Ads Specialist
**What he does:** Writes Facebook and Google ad copy, pulls performance data, iterates on winners.
**Skills loaded:** ad-creative, marketing-psychology, copywriting
**Key tool:** Meta Ads API, Google Ads API (neither connected yet — see setup steps)
**Status:** Ready to write ad creative, needs API tokens to pull performance data
**Activate with:** "Rick, write 10 Facebook ad variations for a spring campaign targeting Cleveland homeowners"

### Donna Park — Growth & Launch Strategist
**What she does:** Plans 60-90 days ahead — county expansions, seasonal campaigns, lead magnets, big-picture growth.
**Skills loaded:** launch-strategy, lead-magnets, marketing-ideas
**Key tool:** Notion campaign planner, Kit.com for lead magnet delivery
**Activate with:** "Donna, build a launch plan for expanding into Summit County next quarter"

---

## Skills Loaded (16 total)

All skill files live in `.claude/skills/`. Every worker reads the relevant ones before executing a task.

| Skill | Used By |
|-------|---------|
| cold-email | Danny, Carla |
| email-sequence | Danny |
| revops | Nina |
| customer-research | Marcus |
| marketing-psychology | Marcus, Tommy, Rick |
| competitor-profiling | Marcus |
| sales-enablement | Danny, Carla |
| copywriting | Tommy, Jasmine, Rick |
| social-content | Jasmine |
| lead-magnets | Donna |
| referral-program | Carla |
| launch-strategy | Donna |
| marketing-ideas | Tommy, Donna |
| ad-creative | Jasmine, Rick |
| product-marketing-context | All workers read this |

---

## Forest City Product Context

Full context lives at `/agents/product-marketing-context.md`. Key facts:

**Services:** House washing, roof soft washing, driveway/concrete cleaning, deck/fence cleaning, commercial building washing. Soft wash AND pressure wash depending on surface.

**Packages:**
- The Fresh Start — entry-level, single surface or basic whole-home
- The Curb Appeal — mid-tier, full exterior (most popular)
- The Showstopper — premium, everything plus roof wash and detail work
- Annual maintenance plans — spring clean + pre-winter clean (two visits)

**Service area:** 7 counties — Cuyahoga, Lake, Lorain, Geauga, Medina, Summit, Portage

**ICP:**
- Residential: Homeowners 35-65, own their home, Northeast Ohio suburbs, care about curb appeal
- Commercial: Property managers, HOA management companies, facility managers
- Referral partners: Siding contractors, landscapers, realtors, gutter companies, painters

**Top objections:**
1. "I can get it cheaper on Facebook" → We're not the cheapest, we're the one that shows up and does it right
2. "I'll just rent a pressure washer" → Soft washing roofs/siding with a pressure washer voids warranties and causes damage
3. "I don't need it that often" → Algae and mold come back in 12-18 months in Northeast Ohio's climate

**Brand voice:** Direct, friendly, local. Sounds like Bradley — a real Cleveland guy who knows his stuff. Not corporate, not salesy.

---

## API Keys & Credentials

| Tool | Key/Token | Status |
|------|-----------|--------|
| Apollo.io | aKRZyBffyV7ScWVCuTXBjA | Connected — Danny and Carla use this |
| HubSpot | Not yet added | Create Private App in HubSpot Settings → Integrations |
| Instantly.ai | Not yet added | Create account at instantly.ai (~$37/mo) |
| Meta Ads | Not yet added | Create app at developers.facebook.com |
| Google Ads | Not yet added | Create credentials in Google Cloud Console |
| Later.com | Not yet added | Free account at later.com |
| Kit.com | Not yet added | Free account at kit.com (up to 10k subscribers) |
| Zapier | Not yet added | Free tier at zapier.com |

---

## Setup Steps Still Pending (in priority order)

### Immediate (free, do today)
1. **Zapier free account** — connects everything together. zapier.com
2. **Later.com free account** — social scheduling. later.com. Connect Facebook Business page and LinkedIn.
3. **HubSpot Private App token** — Settings → Integrations → Private Apps → Create app → give CRM read/write. Paste token into CLAUDE.md.
4. **Notion databases** — Nina and Marcus need these built. Tell Claude Code: "Nina, set up the HubSpot pipeline" and "Marcus, create the Notion intelligence databases"

### Soon (paid, when ready)
5. **Instantly.ai account** (~$37/mo) — Danny's cold email sending engine. Connect your sending Gmail address.
6. **Meta for Developers account** (free to create, spend money on ads) — developers.facebook.com → create app → get System User token. Paste into CLAUDE.md.

### Later (when running ads)
7. **Google Ads account** — free to create, pay per click. Then Google Cloud Console for API credentials.
8. **LinkedIn Sales Navigator** (~$99/mo) — Carla uses for partner prospecting. Can start without it.

---

## Zapier Automations to Build

Once Zapier is connected, these run the office on autopilot:

| Trigger | Action | Worker |
|---------|--------|--------|
| Instantly reply received | Move HubSpot contact to "Replied" + create follow-up task | Danny |
| HubSpot contact tagged as Partner | Draft referral email to Gmail drafts | Carla |
| HubSpot deal marked Closed Won | Draft Facebook before/after post to Notion content calendar | Jasmine |
| HubSpot contact stale 5+ days | Send Bradley a text/email alert | Nina |
| New Kit.com subscriber | Add to HubSpot as lead + start nurture sequence | Donna |

---

## File Structure

```
forestcity/
├── CLAUDE.md                    ← master brain, read on every session
├── context/
│   └── onboarding.md            ← this file
├── agents/                      ← each worker's personality + instructions
│   ├── danny.md
│   ├── carla.md
│   ├── marcus.md
│   ├── nina.md
│   ├── tommy.md
│   ├── jasmine.md
│   ├── rick.md
│   ├── donna.md
│   └── product-marketing-context.md
├── .claude/skills/              ← all 16 marketing skill files
│   ├── cold-email.md
│   ├── email-sequence.md
│   ├── revops.md
│   └── ... (16 total)
├── logs/
│   └── activity.log             ← timestamped log of everything every worker does
├── outputs/                     ← all work product saved here
│   ├── danny/                   ← lead lists, email sequences
│   ├── carla/                   ← partner lists, outreach copy
│   ├── marcus/                  ← competitor profiles, VOC library
│   ├── nina/                    ← pipeline reports, stale lead alerts
│   ├── tommy/                   ← website copy, one-pagers, objection docs
│   ├── jasmine/                 ← social posts, content calendar batches
│   ├── rick/                    ← ad creative batches, performance reports
│   └── donna/                   ← campaign briefs, lead magnets
└── dashboard.html               ← open in browser to see team status
```

---

## How to Run the Office

### Starting a session
Open terminal, navigate to the forestcity folder, run `claude`. Claude Code reads CLAUDE.md automatically.

### Activating a worker
Just say their name and the task:
- "Danny, pull 50 property managers in Cuyahoga County and write a 3-touch sequence"
- "Marcus, mine Google reviews for power washing companies in Cleveland and pull the top 20 customer phrases"
- "Jasmine, write this week's 5 Facebook posts — focus on spring pre-season"
- "Tommy, write a one-pager leave-behind for after estimates"
- "Donna, build a lead magnet for Northeast Ohio homeowners"

### Checking on everyone
Type `status` — Claude reads the activity log and gives you a summary of what each worker has done and what needs attention.

### Morning routine (recommended)
1. Type `status` to see what's been done
2. Pick 1-2 workers to activate based on the priority queue
3. Review their output in the `/outputs/` folder
4. Approve anything that needs your sign-off before it goes out

---

## Priority Queue — Where to Start

1. **Danny** — Pull first lead list from Apollo, write first cold email sequence
2. **Marcus** — Profile top 5 Cleveland competitors, start VOC library
3. **Carla** — First siding contractor outreach batch
4. **Tommy** — Objection handling cheat sheet for Bradley's calls
5. **Jasmine** — This week's Facebook posts
6. **Nina** — Build HubSpot pipeline (needs token first)
7. **Donna** — Northeast Ohio Home Maintenance Checklist lead magnet
8. **Rick** — First Facebook ad creative batch (can do copy now, needs API for performance data later)

---

## Important Notes for Claude Code

- Always read `/agents/product-marketing-context.md` before any worker executes a task
- All output goes to `/outputs/{worker-name}/` — never anywhere else
- Every completed task gets a log entry in `/logs/activity.log` format: `[YYYY-MM-DD HH:MM] WORKER | TASK | OUTPUT FILE | STATUS`
- Bradley's voice is direct and informal — never corporate, never "leverage synergies"
- Ohio context matters — reference Northeast Ohio, specific counties, local seasons
- When in doubt, sound like a real Cleveland guy who takes pride in his work
