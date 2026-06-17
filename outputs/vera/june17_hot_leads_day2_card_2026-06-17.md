# Hot Leads Window — Day 2 of 3
*Vera Cole | Run 208 | June 17, 2026*
*Window: June 16–18 | TODAY is Day 2 — window closes TOMORROW night*

---

## ⚡ Morning Protocol (Do This First — 10 Minutes)

```bash
cd /Users/bradleyneal/forestcity
python3 workers/nina_report.py daily
```

Open: `outputs/nina/hot_leads_2026-06-17.md`

**If you see 2+ opens on any contact → LinkedIn connect within 2 hours.**

The 2-hour window matters: contacts are most likely to accept and respond same day they open. After 24 hours, connection rate drops 60%.

---

## 🔥 What to Do With Hot Leads

| Signal | Action | Script |
|--------|--------|--------|
| 2+ opens, no reply | LinkedIn connect NOW | "Hey [name], noticed you looked at our exterior cleaning info — happy to answer any questions..." |
| Replied to email | Respond within 1 hour | "Appreciate you writing back — what's the best time for a quick call?" |
| Replied asking price | Give ballpark + book site visit | "For a facility like [company], typical range is $X–$Y. I can take a look this week and give you an exact number." |

---

## 📊 What Lake County Sent (June 15 Pull)

Segments that should now have contacts enrolled and opening:

| Segment | Key Targets |
|---------|-------------|
| #195 Boat Repair & Marine Service | Grand River Marine, Fairport Harbor Boat Works |
| #196 Craft Breweries & Taprooms | **Willoughby Brewing** (flagship), Cornerstone Brewing |
| #197 General Aviation / FBO | **Willoughby Hopkins Airport (LNN)** — highest-value target |
| #198 Wholesale Nurseries | Willoway Nurseries, Lake County Nursery Exchange |
| Manufacturing (existing) | Integer Holdings (Greatbatch), Parker Hannifin Electronics |

**FBO Note:** Airport contacts open slowly (2–5 days after delivery). If no opens yet from LNN, check back June 19–21. FAA compliance angle = they READ carefully before responding.

**Brewery Note:** Taproom managers tend to open quickly (same day or next morning). If Willoughby Brewing opens — act immediately, they're booking summer events now.

---

## 📋 Priority If Hot Leads Appear

**Tier 1 (act within 2 hours):**
- Hospital FMs / Health System contacts
- Airport / FBO managers
- Brewery / taproom managers
- Wholesale nursery managers (June = peak growing season = site is accessible for assessment)

**Tier 2 (act within 24 hours):**
- Manufacturing plant FMs
- Marine service center managers
- Electronics manufacturer facility managers

---

## ⚡ If 0 Hot Leads Again Today

Not a problem — sequences typically generate opens on Days 3–7 after send.

The June 15 pull only fired 2 days ago. Some contacts won't open until next week.

**Check instead:**
- Did the Lake County pull actually complete? `cat logs/cron.log | tail -30`
- Any contacts enrolled? `python3 -c "import json; d=json.load(open('contacts_cache.json')); print(len([c for c in d.get('contacts',[]) if c.get('mixmax_enrolled')]),' enrolled')`

---

## 📅 What's Coming After This Window Closes

| Date | Event |
|------|-------|
| June 18 (tomorrow) | Hot leads window closes — final day |
| June 22 (Sunday) | **Lorain County pull** — `scripts/run_lorain_both.command` |
| June 23–25 | Lorain contacts start opening |
| July 4 | Holiday booking urgency (deck/patio pre-holiday wash) |

---

## 🚨 Still Pending (Bradley Action)

- **Gas/Fleet sequences** — Day 34+. Summit + Medina + Cuyahoga + Lake contacts sitting unenrolled.
  → Copy ready: `outputs/vera/gas_fleet_sequence_copy_2026-06-12.md` (10 min in Mixmax)
- **GitHub Actions relay** — PAT needs `workflow` scope. Messages queued in `outputs/vera/pending_slack_messages.md`.
  → Fix: github.com/settings/tokens → Edit → check `workflow` → Save

---

*Vera Cole | June 17 | Day 2 of hot leads window — closes June 18*
