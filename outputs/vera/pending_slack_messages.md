🧊 *Vera — Auto-Upgrade #1 of 5 | Segment #97: Ice Rinks & Indoor Ice Arenas* _(Run 155 · 2026-05-31)_
>**New segment live** — 8 Apollo titles + 8 org keywords added to `lead_pipeline.py`. Titles synced to `mixmax.py` PROPERTY_MANAGER_TITLES for correct routing on manual imports.
>
>**Why now:** Summer is the maintenance window for NE Ohio ice rinks — ice out = full exterior access. Palace Ice Arenas (Solon + Twinsburg), Mentor Ice Arena, OBM Arena Parma, Brooklyn Ice Center. No competitors targeting this segment.
>
>**Revenue:** $1K–$4K/visit × 2/year = $2K–$8K/year per location. Multi-rink operator deal: $6K–$24K/year.
>
>**Apollo keywords live:** `ice rink`, `ice arena`, `ice skating rink`, `hockey rink`, `skating facility`, `ice sports complex`
>**Sequence routing:** → Property Manager sequence
>**Pitch:** "Summer is your window — when the ice is out, the exterior is exposed. One visit handles parking, entrance, zamboni bays, and loading docks."

---

📊 *Vera — Auto-Upgrade #2–5 | Count Sync: 96+ → 97+* _(Run 155 · 2026-05-31)_
>Updated all stale `96+` references to `97+` across:
>• `workers/vera_relay.py` — 11 occurrences (replace_all)
>• `CLAUDE.md` — 2 occurrences (Quick Shortcuts table + June 8 callout)
>• `agents/danny.md` — 1 targeted occurrence (title batching note; historical "94+ → 96+" note preserved)
>
>Full segment brief added to `agents/danny.md` with pitch angle, timing, revenue calc, and Apollo keyword reference.

---

🚨 *Vera — CRITICAL: Summit County Pull Due TODAY* _(Run 155 · 2026-05-31 — Day 10 escalation)_
>Summit County Week 21 is scheduled for **today, May 31**. This is the last day to run it on schedule.
>
>**Action required RIGHT NOW:**
>Open Finder → `forestcity/scripts/` → double-click `run_summit_both.command`
>
>This cannot run from the cloud — it calls Apollo and Mixmax directly from your Mac. Every day this slips is a day your Week 21 pipeline gets thinner.
>
>If you've already run it, reply "done" in Slack so I can close this issue.

---

⚠️ *Vera — Reminder: Medina County Pull Tomorrow (June 1)* _(Run 155 · 2026-05-31)_
>Medina County Week 22 is scheduled for **tomorrow, June 1**.
>
>**Script:** `run_medina_both.command` (Danny + Carla both)
>
>Set a calendar reminder now. This one follows Summit — if Summit slipped today, do both back-to-back tomorrow.

---

🔴 *Vera — BLOCKED: Instantly.ai Campaigns Still Active — Enrollment Blocked June 4* _(Run 155 · 2026-05-31 — Day 13 escalation)_
>Cuyahoga County Week 24 pull is **June 8 — 8 days away**. Enrollment is blocked until Instantly campaigns are paused.
>
>**What's at stake:** 97+ commercial segments × Cuyahoga County = largest Apollo pull of the year. Every lead in that pull will hit the `INSTANTLY_PAUSED` guard and be skipped if you don't act.
>
>**Two-step fix (5 minutes):**
>1. Go to `app.instantly.ai` → pause campaigns `a1c08c3d` and `626cd15d`
>2. Open `/Users/bradleyneal/forestcity/.env` → add line: `INSTANTLY_PAUSED=true`
>
>I cannot do this from the cloud. You must do it before June 8.

---

🔴 *Vera — BLOCKED: Gas Station & Fleet Sequences Still PENDING* _(Run 155 · 2026-05-31 — Day 13 escalation)_
>Gas Station and Fleet Washing Mixmax sequences have been `PENDING` since Run 142. Every lead with a gas station or fleet keyword is being enrolled into the **wrong sequence** or dropped.
>
>**Fix (10 minutes in Mixmax UI):**
>1. Log into Mixmax → Sequences → create "Gas Station & C-Store Outreach"
>2. Copy the sequence ID → paste into `integrations/mixmax.py` line 54
>3. Create "Fleet Washing Outreach"
>4. Copy that ID → paste into `integrations/mixmax.py` line 48
>5. Commit and push
>
>These two segments (gas stations, fleet accounts) are high-revenue targets sitting in a broken routing state. I can't create Mixmax sequences from the cloud — this one is yours.

---

✅ *Vera — Scan Complete 2026-05-31 (Run 155)*
>5 auto-upgrades shipped | 0 proposals | 97 open issues
>
>**Upgrades this run:**
>• Segment #97 Ice Rinks added to Apollo titles + org keywords (lead_pipeline.py)
>• Ice Rinks synced to PROPERTY_MANAGER_TITLES (mixmax.py) for correct routing
>• Full Ice Rinks brief added to danny.md (pitch, timing, revenue, Apollo keywords)
>• Count sync: 96+ → 97+ across vera_relay.py (11x), CLAUDE.md (2x), danny.md (1x)
>
>**Blocked on Bradley (unchanged):** Summit pull TODAY, Medina pull tomorrow, Instantly.ai pause before June 8, Gas Station sequence, Fleet sequence.
