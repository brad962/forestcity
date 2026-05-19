# 0% Reply Rate — Diagnostic & Action Plan
*Vera Cole | Run 18 | 2026-05-19*
*URGENT: Touch 3 fires May 22 — 3 days. Act before it sends.*

---

## The Data

| Metric | Value |
|--------|-------|
| Enrolled contacts | 45 |
| Open rate | 42% (~19 contacts opened) |
| Reply rate | 0% |
| Days running | 7 (Touch 1: May 12, Touch 2: ~May 16) |
| Touch 3 scheduled | ~May 22 |

42% open rate is **strong** — subject lines are working. 0% reply rate means the body or the mechanics are broken.

---

## 5 Hypotheses (Most Likely First)

### Hypothesis 1: Reply-To address isn't Bradley's inbox
**Why this is #1:** The most common Mixmax gotcha. If "Reply-To" in the sequence is set to the Mixmax sending address (or a shared inbox Bradley doesn't check), replies are arriving somewhere he's not looking.

**Test:** Log into Mixmax → open the PM sequence → check Settings → verify "Reply-To" is `bradley@forestcitypowerwashing.com` or wherever Bradley wants replies.

---

### Hypothesis 2: Variables aren't substituting — emails look broken
**Why:** If `{{firstName}}` or `{{company}}` renders as literal text or blank, the email immediately reads as bulk spam. Nobody replies to "Hi {{firstName}}, I work with property managers…"

**Test:** Mixmax → PM Sequence → click "Test" → send to Bradley's own Gmail. Read it exactly as recipients see it. Check: Does it say "Hi Bradley" or "Hi {{firstName}}"? Does the phone number show or show "N/A"?

---

### Hypothesis 3: Emails landing in Promotions/Spam tab after opening
**Why:** Open tracking pixel can fire even if Gmail auto-opens emails in the background (preview pane). The contact may have never actually read the email.

**Signal:** 42% open rate on a cold B2B sequence is above average — could indicate tracking inflation, not actual engagement.

**Test:** Ask a friendly contact to let you know if they received it in their inbox or spam.

---

### Hypothesis 4: Unsubscribes hidden — contacts opted out instead of replying
**Why:** Mixmax reports "replied" separately from "opted out." If people clicked "Unsubscribe" instead of replying, the reply count shows 0 but people did engage — just negatively.

**Test:** Mixmax → PM Sequence → Recipients → sort by status → count how many are "Unsubscribed" vs "Active."

---

### Hypothesis 5: Touch 1 CTA is a 2-part question — too much friction
**Why:** The Touch 1 email ends with:
> "Quick question: how many properties are you managing in the area, and are you currently working with someone for exterior cleaning?"

Two questions = friction. Most cold email responses happen when you ask ONE simple thing.

**Fix:** For Touch 3 and future sequences, end with: "Worth a 15-minute call this week?" — one clear ask.

---

## Action Plan Before Touch 3 Fires (May 22)

### TODAY (May 19) — 10 minutes
1. **Log into Mixmax → PM Sequence → Settings → check Reply-To address**
   - If it's wrong: fix it before Touch 3 sends
   - If it's right: check your inbox for any replies you might have missed

2. **Send yourself a test enrollment**
   - Mixmax → PM Sequence → Recipients → "Add recipient" → your own email
   - Read the email as a recipient would
   - Confirm variables render correctly

3. **Check unsubscribe count**
   - Mixmax → PM Sequence → Recipients → filter by status
   - Report back: how many Unsubscribed vs. Active

### BEFORE Touch 3 Sends (May 22) — 15 minutes
4. **If Reply-To is wrong:** Fix it. Replies are sitting in an inbox somewhere.
5. **If variables are broken:** Edit the sequence to fix the template before Touch 3 sends
6. **If everything looks fine:** Touch 3 is your last shot — make it count by adding the specific offer: "Free exterior walk — I'll come to one of your properties, give you an honest assessment, no commitment."

---

## If All 3 Tests Pass and Reply Rate Is Still 0

That means the body copy is the problem. Approve Tommy's sequence rewrite. New copy is in `outputs/vera/sequence_rewrites_proposal_2026-05-18.md`.

The new version: shorter, harder CTA, stronger NE Ohio specificity.

---

*Vera Cole | Run 18 | Generated 2026-05-19*
