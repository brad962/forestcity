# Vera Cole — Open Issues Tracker

---

## OPEN — Mixmax API blocked in remote cloud environment

- First seen: 2026-05-18
- Description: api.mixmax.com is not in the network allowlist for the remote execution environment. Vera cannot pull live sequence data during cloud runs — pipeline audit is blind here.
- Impact: Can't verify real-time enrollment or catch drops in engagement from this environment.
- Attempts:
  - 2026-05-18: Tried WebFetch → 403 Forbidden. Tried curl → "Host not in allowlist". Domain is blocked.
- Workaround: Nina's reports run locally. Last known data (weekly_report_2026-05-18.md): 45 enrolled, 42% open rate, 0% reply rate, 13 hot leads.
- Next attempt: Check if server.py can serve cached Mixmax data that Vera can read as a local file.

---

## OPEN — 0% Reply Rate Across All Sequences (13 hot openers, 0 replies)

- First seen: 2026-05-18
- Description: 45 enrolled, 42% open rate, 13 contacts with 2+ opens — but zero replies. Emails are opening but not converting. Peak season makes this critical.
- Attempts:
  - 2026-05-18 (run 1): Proposal sent to Bradley — P.S. one-question close on Touch 1, shorten to <100 words, add break-up email as final touch. Awaiting approval.
  - 2026-05-18 (run 2): Escalating in Slack. Still pending.
- Note: Subject lines working (42% open rate is strong). Body copy / CTA is the bottleneck. Need Bradley approval to rewrite sequences.

---

## OPEN — 2 HOT MANUAL CONTRACTORS "VERY INTERESTED" — NO FOLLOW-UP

- First seen: 2026-05-18
- Description: pipeline_data.json shows 2 contractors in "Replied" stage, notes say "Very interested — send text":
  - Bulletproof Lawncare | 216-307-4344
  - Damrons Landscaping | 440-494-0422
  These are warm leads waiting for a text from Bradley. No follow-up logged.
- Attempts:
  - 2026-05-18: Flagged via high-priority Slack alert.
- Resolution criteria: Bradley texts both, logs response, moves to Estimate Sent.

---

## OPEN — 21 Manual Leads in "New Lead" — No Outreach

- First seen: 2026-05-18
- Description: 24 manual contacts in pipeline_data.json. 21 in "New Lead" with no contact logged. All contractors (landscapers, roofers, construction companies) with phone numbers. 1 contacted, 2 replied (above). 21 sitting untouched.
- Attempts:
  - 2026-05-18: Flagged to Bradley via Slack. Proposed Carla write SMS outreach templates.
- Resolution criteria: Each contact moved to Contacted or further.

---

## OPEN — Workiz Shows 0 Power Washing Jobs (JobType mismatch)

- First seen: 2026-05-18 (run 1)
- Description: workiz_report.py always returns "No Power Washing jobs found." Likely jobs use a different casing or variant string.
- Attempts:
  - 2026-05-18 (run 1): Proposed Bradley check Workiz.
  - 2026-05-18 (run 2): AUTO-FIXED — changed to case-insensitive matching against 10 variants (power washing, power wash, pressure washing, house washing, soft wash, etc.). Added diagnostic logging to print JobType values when 0 jobs found.
- Result: Code deployed. Next run will either show jobs or print the exact JobType string Workiz uses.
- Resolution criteria: Report shows job count > 0 on next run.

---

## OPEN — Creative Workers Idle Since May 12 (Marcus, Tommy, Rick, Donna)

- First seen: 2026-05-18 (run 1)
- Description: Marcus, Tommy, Rick, Donna — no new output since May 12. It is peak season.
- Attempts:
  - 2026-05-18 (run 1): Proposal sent to Bradley to activate all 4.
  - 2026-05-18 (run 2): Escalating in Slack.
- Resolution criteria: Each worker produces at least one new peak-season output.

---

## OPEN — HubSpot Not Connected (CRM blind)

- First seen: 2026-05-18 (run 1)
- Description: HUBSPOT_TOKEN pending. No CRM. Nina's full pipeline architecture is built and waiting. 6+ days idle.
- Attempts:
  - 2026-05-18 (run 1): Proposal sent.
  - 2026-05-18 (run 2): Escalating in Slack.
- Resolution criteria: HUBSPOT_TOKEN added to .env, Nina confirms CRM is live.

---

## OPEN — Instantly.ai vs Mixmax Overlap (Two Outreach Platforms Possibly Running)

- First seen: 2026-05-18 (run 2)
- Description: server.py references Instantly.ai with 2 active campaigns. lead_pipeline.py enrolls contacts in Mixmax. Unclear if contacts go into both or one. Risk of duplicate emails to same contacts.
- Attempts:
  - 2026-05-18: Flagged to Bradley via Slack.
- Resolution criteria: Bradley confirms which platform is active. Other is shut off or clearly scoped to different contacts.

---

*Last updated: 2026-05-18 by Vera Cole*
