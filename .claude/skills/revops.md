# Skill: RevOps

## HubSpot Pipeline Architecture for Forest City

### Deal Pipeline Stages

| Stage | Definition | Next Action |
|-------|-----------|-------------|
| 1. New Lead | Contact entered system | Send initial outreach within 24h |
| 2. Contacted | First outreach sent | Follow up at Day 4 if no reply |
| 3. Replied | Prospect responded | Qualify and move to estimate or nurture |
| 4. Estimate Sent | Quote delivered | Follow up at 48h and 5 days |
| 5. Follow-Up | Waiting on decision | Check in at Day 3, Day 7 |
| 6. Closed Won | Job booked | Create deal record, tag source |
| 7. Closed Lost | Not booking now | Tag reason, add to re-engagement sequence |
| 8. Nurture | Not ready yet | Quarterly check-in, seasonal outreach |

### Contact Properties to Track
- **Lead source:** Danny Outbound / Carla Referral / Inbound / Referral Partner / Walk-in
- **Property type:** Residential / Commercial / HOA
- **County:** Cuyahoga / Lake / Lorain / Geauga / Medina / Summit / Portage
- **Services interested in:** House Wash / Roof / Driveway / Deck / Commercial / Annual Plan
- **Estimated job value:** Dollar amount
- **Last contact date:** Auto-stamped
- **Next follow-up date:** Set by owner
- **Sales rep:** Danny / Carla / Bradley

### Stale Lead Rules
Flag any contact that hasn't been touched in:
- 5 days if in "Contacted" stage
- 3 days if in "Estimate Sent" stage
- 7 days if in "Follow-Up" stage

### Weekly RevOps Report (every Monday)
Produce a report covering:
1. **Pipeline snapshot:** Count of deals by stage
2. **New leads this week:** Total, by source
3. **Closed Won this week:** Total, revenue, avg deal size
4. **Stale leads:** List of contacts needing immediate follow-up
5. **Conversion rate:** Lead → Estimate, Estimate → Closed Won
6. **Actions needed:** Specific contacts for Bradley to call this week

### Zapier Automation Recipes

| Trigger | Action | Purpose |
|---------|--------|---------|
| Instantly reply received | Move to "Replied" + create follow-up task | Danny's sequences |
| HubSpot contact tagged "Partner" | Draft referral email to Gmail drafts | Carla's partner workflow |
| Deal marked Closed Won | Draft Facebook before/after post in Notion | Jasmine's content pipeline |
| Contact stale 5+ days | Send Bradley text/email alert | Pipeline hygiene |
| New Kit.com subscriber | Add to HubSpot + start nurture sequence | Donna's lead magnet flow |

### KPIs to Track Weekly
- New leads added
- Reply rate (Danny's cold email)
- Quote-to-close rate
- Avg deal value
- Revenue this week vs. last week
- Revenue this month vs. goal
