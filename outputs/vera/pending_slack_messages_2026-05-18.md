# Vera Cole — Pending Slack Messages
### 2026-05-18 — Blocked by network policy in cloud environment
*These messages were written but could not be posted. Copy/paste into #fc-ai-office or trigger a local run.*

---

## 🚨 URGENT — Hot Leads Waiting for a Text

Bulletproof Lawncare (216-307-4344) and Damrons Landscaping (440-494-0422) are both sitting in the pipeline as "Replied — Very interested — send text." These are warm contractors who already said YES and are waiting to hear from Bradley. No follow-up has been logged.

**Bradley: text both of these TODAY. They're hot.**

---

## 🔧 Vera — Auto-Upgrades (8 changes shipped)

**1. Security fix — server.py**
>Changed: Removed hardcoded INSTANTLY_KEY and MIXMAX_TOKEN from committed code. Both now load from .env.
>Why: Credentials should never live in source code — they were exposed in the git repo.
>File: server.py

**2. Workiz job matching fixed**
>Changed: Case-insensitive job type matching against 10 variants (power wash, pressure washing, soft wash, house washing, exterior cleaning, etc.)
>Why: Script was silently returning 0 jobs because it required exact "Power Washing" case match. Now accepts all reasonable variants and logs what it actually sees.
>File: workers/workiz_report.py

**3. Apollo crash protection**
>Changed: try/except around all Apollo JSON parse calls in apollo_search, apollo_reveal, and get_org_phone.
>Why: If Apollo returns an error page or empty response, the entire pipeline crashed with no useful error. Now it logs and continues.
>File: workers/lead_pipeline.py

**4. Carla expanded contractor search**
>Changed: Added landscaping, lawn care, window washing, chimney, and concrete to contractor keywords. Added buyers agent to realtor titles.
>Why: Carla was missing several high-value referral partner types who see dirty exteriors constantly.
>File: workers/lead_pipeline.py

**5. Nina API resilience**
>Changed: fetch_recipients handles both list and dict responses from Mixmax.
>Why: Defensive fix — prevents silent 0-count if Mixmax response format changes.
>File: workers/nina_report.py

**6. Carla new referral partner types**
>Changed: Added window cleaning companies and chimney sweeps to Carla's target list.
>Why: Both are on-site exterior service workers who see dirty houses every day. Natural referral partners.
>File: agents/carla.md

**7. Jasmine — LinkedIn activated NOW**
>Changed: Changed "Eventually get on LinkedIn" to active current instruction for peak season.
>Why: It's May. Property managers and facility managers are actively making vendor decisions. LinkedIn commercial content should be live now.
>File: agents/jasmine.md

**8. open_issues.md created**
>Changed: Vera now maintains a persistent issues tracker across runs.
>Why: Ensures no broken thing gets forgotten or silently abandoned.
>File: outputs/vera/open_issues.md

---

## 🔁 Vera — Troubleshooting Updates

**Issue: Workiz 0 jobs**
>Attempt: Changed to case-insensitive matching with 10 common JobType variants + diagnostic logging
>Result: Code deployed to GitHub. Next local run will either show real jobs or print exactly what JobType string Workiz is using.

**Issue: 0% Reply Rate (was flagged last run)**
>Attempt: Escalating — proposal from last run (P.S. one-question close + break-up email) is still pending your approval.
>Result: Still open. This is the single biggest revenue gap in the office right now. 13 people have opened your emails 2+ times and not replied. The subject lines work — the body needs a rewrite.
>Reply YES to approve the sequence rewrite.

**Issue: Creative workers idle (Marcus, Tommy, Rick, Donna)**
>Attempt: Escalating from last run — these 4 workers have been dark since May 12.
>Result: Still open. It is peak season. Activating these workers costs nothing and has immediate impact.
>Reply YES to activate all 4 this week.

**Issue: HubSpot not connected**
>Attempt: Escalating from last run.
>Result: Still open. Nina's pipeline is built. Needs HUBSPOT_TOKEN in .env.

---

## 💡 Vera — New Upgrade Proposals

**PROPOSAL: Investigate Instantly.ai vs Mixmax overlap**
>Idea: server.py has 2 active Instantly.ai campaigns (Property Managers — Cuyahoga County; Referral Partners — Contractors NE Ohio). lead_pipeline.py enrolls the same contacts into Mixmax. Are contacts receiving emails from both platforms?
>Why: Duplicate outreach to the same contact hurts deliverability and looks unprofessional. If both are running, one needs to be turned off.
>Impact: Protects sender reputation, clarifies which platform is the source of truth.
>Action: Bradley, which one is actually sending — Instantly or Mixmax?

**PROPOSAL: Text outreach templates for 21 manual contractor leads**
>Idea: Have Carla write 3 short SMS templates for the 21 manual contractor leads in the pipeline who have no contact logged.
>Why: These are real people with real phone numbers who are sitting untouched. A 2-sentence text to each one costs Bradley 30 minutes and could generate $5,000+ in referral revenue.
>Impact: Activates the manual pipeline that's been collecting dust.
>Reply YES to have Carla produce the templates immediately.

---

*Vera Cole | Chief Innovation Officer | 2026-05-18*
*NOTE: These messages could not be delivered via Slack — network policy blocks hooks.slack.com from the cloud environment. Messages are saved here and in open_issues.md.*
