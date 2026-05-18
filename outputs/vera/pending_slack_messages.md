## 🔧 *Vera — Auto-Upgrades (Run 3, May 18)*

**1. apollo_search keyword filter now works**
>Changed: `q_organization_keyword_tags` now passed to Apollo API in Carla's contractor searches. Was defined but never sent — Carla was pulling any owner/president/founder regardless of industry.
>Why: Carla needs to reach siding/roofing/gutter/landscaping companies, not generic businesses.
>File: workers/lead_pipeline.py

**2. Enrollment repair loop protected against API failure**
>Changed: `get_mixmax_enrolled_emails()` returns `None` when ALL API calls fail. `verify_and_repair_enrollment` now skips instead of treating all cached contacts as "missing" and re-enrolling everyone.
>Why: From cloud environment, Mixmax returns 403 (IP blocked). Without this fix, every cloud run would attempt to mass re-enroll the entire contacts list.
>File: workers/lead_pipeline.py

**3. LinkedIn URL column added to Nina's daily hot leads report**
>Changed: Hot leads table now includes a clickable LinkedIn link. Cross-references the contacts cache so Bradley can connect in one click.
>Why: 13 contacts have opened emails 2+ times. LinkedIn connect is the next move. The link should be there when Bradley opens the report.
>File: workers/nina_report.py

**4. apollo_search + apollo_reveal now crash-protected**
>Changed: All Apollo JSON parse calls wrapped in try/except. Pipeline no longer crashes on malformed API responses.
>Why: If Apollo returns an error page or rate-limit response, pipeline was dying with no useful message.
>File: workers/lead_pipeline.py (merged from concurrent run 2)

---

## 🔁 *Vera — Troubleshooting Update*

>Issue: Mixmax API 403 from cloud environment
>Attempt: Tried apiToken param, Authorization header, X-API-Key — all 403. Error body: "Host not in allowlist"
>Result: Still blocked. Fixed dangerous side effect (mass re-enroll bug). Root cause requires Bradley action: Mixmax → API Settings → IP Allowlist → remove restriction.

>Issue: Workiz zero Power Washing jobs
>Attempt: Fixed script to match 10 job type variants (power wash, pressure washing, soft wash, etc.). Added diagnostic logging that prints actual JobType values when 0 matches found.
>Result: Code deployed. Next run will show either jobs OR the exact string Workiz is using so we can add it.

---

## 📋 *Vera — Open Issues Summary (May 18, Run 3)*

**URGENT (revenue now):**
- 🚨 Bulletproof Lawncare (216-307-4344) and Damrons Landscaping (440-494-0422) said "Very interested — send text." No follow-up logged. Text them today.
- 21 manual contractor leads in "New Lead" stage with no outreach. They have phone numbers.

**Awaiting Bradley approval:**
- Proposal 1: Fix 0% reply rate — P.S. question close + shorten emails + break-up email
- Proposal 2: LinkedIn connect template for 13 hot openers (report updated, template needs YES)
- Proposal 3: Activate Marcus/Tommy/Rick/Donna for peak season
- Proposal 5: Launch homeowner Facebook ads
- HubSpot token needed — Nina's CRM is built and waiting

**Needs Bradley action:**
- Instantly.ai vs Mixmax overlap — which platform is active for which contacts?
- Mixmax IP allowlist blocking cloud Vera runs
- Workiz JobType — log into Workiz, check how jobs are tagged
