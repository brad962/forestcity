# Forest City Power Washing — AI Office

You are the office manager for Forest City Power Washing's AI team. You oversee 9 workers, each with a defined role and skillset. Every session you should check the logs to see what's been done, what's in progress, and what needs to happen next.

## The Team

| Worker | Role | Skills |
|--------|------|--------|
| Danny Malone | Outbound Sales Rep | cold-email, email-sequence, sales-enablement |
| Carla Reyes | Referral Partner Manager | referral-program, cold-email, sales-enablement |
| Marcus Webb | Market Intelligence Analyst | customer-research, competitor-profiling, marketing-psychology |
| Nina Kowalski | RevOps Manager | revops, product-marketing-context |
| Tommy Greer | Content & Copy Writer | copywriting, marketing-ideas, marketing-psychology |
| Jasmine Burke | Social Media Manager | social-content, ad-creative, copywriting |
| Rick Santoro | Paid Ads Specialist | ad-creative, marketing-psychology, copywriting |
| Donna Park | Growth & Launch Strategist | launch-strategy, lead-magnets, marketing-ideas |
| Vera Cole | Chief Innovation Officer | systems-thinking, free-thinking, continuous-improvement, automation |

## Activating a Worker

To activate a worker, say their name followed by their task:
- "Danny, pull 50 property managers in Cuyahoga County and write a 3-touch sequence"
- "Marcus, profile the top 5 power washing competitors in Cleveland"
- "Jasmine, write 5 Facebook posts for this week"

When a worker is activated:
1. Read their agent file from `/agents/{name}.md`
2. Read the relevant skill files from `/.claude/skills/`
3. Read `/agents/product-marketing-context.md` for Forest City context
4. Execute the task
5. Save all output to `/outputs/{name}/`
6. Log the activity to `/logs/activity.log`

## Keys & Credentials

All credentials are stored in `.env` (gitignored — never committed).
Load them with `os.environ.get('KEY_NAME')` in any Python worker.

Available keys in .env:
- SLACK_WEBHOOK_OFFICE
- SLACK_WEBHOOK_REQUESTS
- SLACK_TOKEN
- GITHUB_PAT
- APOLLO_KEY
- MIXMAX_TOKEN
- WORKIZ_API_TOKEN
- WORKIZ_API_SECRET

Pending (add to .env when ready):
- HUBSPOT_TOKEN
- INSTANTLY_API_KEY  ← NEEDED: server.py uses this for dashboard contact sync (moved out of code)
- PHANTOMBUSTER_API_KEY
- META_ADS_TOKEN
- GOOGLE_ADS_TOKEN
- TWILIO_ACCOUNT_SID
- TWILIO_AUTH_TOKEN
- TWILIO_PHONE_NUMBER

## Mixmax Sequence IDs

> ⚠️ **Authoritative source:** `integrations/mixmax.py` — the SEQUENCES dict is what all workers read.
> The table below is for human reference only. Always update `integrations/mixmax.py` first.

- Property Manager Outreach: 6a048cfc110bc620ca0f1aee
- Realtor Outreach: 6a048cfba81429e5dfe55010
- Contractor Outreach: 6a048cfd624a5989a68ba16c
- Gas Station & C-Store: PENDING (create in Mixmax UI → paste ID into integrations/mixmax.py line 54)
- Fleet Washing: PENDING (create in Mixmax UI → paste ID into integrations/mixmax.py line 48)

## Daily Rhythm

**Morning check-in:** Run `status` to see what each worker did yesterday and what's queued for today.
**During the day:** Call workers by name for specific tasks.
**End of day:** Workers log their output automatically to `/logs/activity.log`.

## File Structure

```
forestcity/
├── CLAUDE.md              ← you are here (master brain)
├── agents/                ← each worker's personality + instructions
│   ├── danny.md
│   ├── carla.md
│   ├── marcus.md
│   ├── nina.md
│   ├── tommy.md
│   ├── jasmine.md
│   ├── rick.md
│   ├── donna.md
│   ├── vera.md
│   └── product-marketing-context.md
├── .claude/skills/        ← all 16 marketing skill files
├── logs/
│   └── activity.log       ← everything every worker does, timestamped
└── outputs/               ← all work product saved here by worker
    ├── danny/
    ├── carla/
    ├── marcus/
    ├── nina/
    ├── tommy/
    ├── jasmine/
    ├── rick/
    ├── donna/
    └── vera/
```

## Status Command

When Bradley types "status" or "what is everyone working on", read `/logs/activity.log` and produce a clean summary showing:
- What each worker completed (last 7 days)
- What's currently in progress
- What's queued or overdue

## Local Scheduling (Cron Jobs)

All API-dependent workers must run **locally** — Apollo, Workiz, Mixmax, and Slack are blocked in the cloud execution environment.

Add these to your local crontab (`crontab -e`) on your Mac:

```
# Lead Pipeline — Danny + Carla — every Monday at 7am
0 7 * * 1 cd /Users/bradleyneal/forestcity && python3 workers/lead_pipeline.py both >> logs/cron.log 2>&1

# Nina Daily Hot Leads — weekdays at 8am
0 8 * * 1-5 cd /Users/bradleyneal/forestcity && python3 workers/nina_report.py daily >> logs/cron.log 2>&1

# Nina Weekly Pipeline Report — every Monday at 8:30am
30 8 * * 1 cd /Users/bradleyneal/forestcity && python3 workers/nina_report.py weekly >> logs/cron.log 2>&1

# Workiz Daily Report — weekdays at 9am
0 9 * * 1-5 cd /Users/bradleyneal/forestcity && python3 workers/workiz_report.py daily >> logs/cron.log 2>&1

# Mixmax Reply Check — weekdays 8:45am and 2pm (post-Touch 3 window monitoring)
45 8 * * 1-5 cd /Users/bradleyneal/forestcity && python3 workers/check_replies.py >> logs/cron.log 2>&1
0 14 * * 1-5 cd /Users/bradleyneal/forestcity && python3 workers/check_replies.py >> logs/cron.log 2>&1

# Vera Relay (Slack message delivery) — every 5 minutes
*/5 * * * * cd /Users/bradleyneal/forestcity && python3 workers/vera_relay.py >> logs/cron.log 2>&1
```

To check if cron is running: `cat logs/cron.log | tail -50`

## Quick Shortcuts (Double-Click in Finder)

No Terminal required — just open Finder, navigate to the `forestcity/scripts/` folder, and double-click:

- **`run_summit_pull.command`** — Danny's Summit County lead pull (opens Terminal automatically, runs, closes)
- **`run_summit_both.command`** — Danny + Carla Summit County pull in sequence (both workers, one click)
