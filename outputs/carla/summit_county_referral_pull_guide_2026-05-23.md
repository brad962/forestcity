# Carla — Summit County Referral Partner Pull Guide
*Vera Cole | Created 2026-05-23*

---

## Why This Matters

Danny is pulling Summit County property managers this week (deadline May 31).
Carla should pull Summit County referral partners **the same week** — same geography, same timing, coordinated approach.

**Summit County = Akron, Fairlawn, Stow, Cuyahoga Falls, Green**
- Fast-growing suburban market south of Cleveland
- Strong landscaping / roofing / HVAC presence
- Low overlap with existing Cuyahoga contacts

If Carla's Summit County contacts are enrolled in the contractor sequence the same week Danny's Summit PMs are in the PM sequence, the whole county gets worked simultaneously.

---

## Command to Run

```bash
cd /Users/bradleyneal/forestcity
python3 workers/lead_pipeline.py carla Summit
```

This runs the Summit County batch override for Carla — same as Danny's county override flag added in Run 63.

**Estimated time:** 3–5 minutes.

---

## What It Pulls

Apollo search targeting owners/founders/presidents of:
- Siding contractors in Summit County
- Landscaping / lawn care companies (Akron area)
- Gutter companies
- Roofing companies
- Painters
- Tree service / arborist companies
- HVAC / heating & cooling companies
- Pool service companies
- Realtors at major Summit County brokerages

All enrolled automatically in the contractor or realtor Mixmax sequences.

---

## When to Run

**Run with Danny's Summit pull on the same day.** The easiest path:

```bash
# Run both in one command:
python3 workers/lead_pipeline.py both
# (Week 21 rotation = Summit County for both Danny and Carla)
```

Or individually:
```bash
python3 workers/lead_pipeline.py danny Summit
python3 workers/lead_pipeline.py carla Summit
```

---

## Deadline

Same as Danny's: **May 31**. After June 1, the rotation moves to Medina County.

Summit County won't be the active rotation again until **July 6 (Week 27)**.

---

*Written by Vera | Mirrors Danny Summit pull to give Carla coordinated coverage.*
