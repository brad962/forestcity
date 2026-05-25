# Self-Storage Facilities — Commercial Segment Brief
### Donna Park | Growth & Launch Strategist | 2026-05-25
*New commercial segment approved for Apollo pull and PM sequence outreach*

---

## Why Self-Storage

Self-storage facilities in NE Ohio are algae magnets. Large concrete pads, metal and vinyl-sided buildings, dumpster areas, and signage panels sit through 8 months of lake-effect humidity. The result: green-black algae streaks across concrete and facades that building managers notice but don't know how to fix without damaging metal siding.

**The math:** Extra Space Storage has 11 NE Ohio locations. Life Storage (formerly Uncle Bob's) has 9. CubeSmart has 7. StorageMart has 5. That's 32+ facilities for just 4 chains — not counting 40+ local operators. One district manager who says yes = 3–5 facilities, each needing quarterly or annual service.

**Revenue math:**
- Average facility: 4,000 sq ft of concrete pad + 2,000 sq ft building exterior = $450–$800/wash
- 4 facilities per district manager = $1,800–$3,200 per contract
- Quarterly service = $7,200–$12,800/year per account
- **10 accounts = $72,000–$128,000 in recurring annual revenue**

---

## The Target

**Primary:** District/Area Manager (oversees 3–5 facilities, signs vendor contracts)
- Title variants: "District Manager," "Area Manager," "Regional Manager" at self-storage companies
- These people already exist in Apollo under `self storage` + `storage facility` org keywords

**Secondary:** Facility Manager / Property Manager at single-location operators
- Title: "Property Manager," "Facility Manager," "Self Storage Manager"
- Already captured by DANNY_TITLES `self storage manager` (added May 25)

**NE Ohio chains to target:**
| Chain | NE Ohio Locations | HQ |
|-------|-------------------|----|
| Extra Space Storage | 11 | Salt Lake City (but DMs are regional) |
| Life Storage | 9 | Buffalo NY |
| CubeSmart | 7 | Malvern PA |
| StorageMart | 5 | Columbia MO |
| Public Storage | 8 | Glendale CA |
| Uncle Bob's | 3 | Legacy brand, now Life Storage |
| All-American Mini Storage | 4 | Cleveland (local) |
| Storage Today | 3 | Akron (local) |

---

## Apollo Pull Parameters

Run alongside the next county rotation (Week 22 Medina, June 1):

```json
{
  "person_titles": [
    "district manager", "area manager", "regional manager",
    "property manager", "facility manager",
    "self storage manager", "storage facility manager"
  ],
  "q_organization_keyword_tags": [
    "self storage", "self-storage", "storage facility",
    "storage units", "mini storage"
  ],
  "person_locations": ["Northeast Ohio", "Cleveland, Ohio", "Akron, Ohio"],
  "per_page": 30
}
```

**Command:**
```bash
python3 workers/lead_pipeline.py danny
# Will auto-include self-storage via DANNY_ORG_KEYWORDS (added May 25 run 87)
```

---

## The Pitch Angle

**Don't lead with "power washing."** Lead with what they see every day:

> "Hi [Name], I work with a few storage facilities in the Cleveland area — the concrete pads and building sides tend to collect algae from the lake humidity. We use soft-wash techniques that are safe for metal siding. Most facilities we work with schedule 1–2 visits per season. Would it make sense to send you a quick quote for [their facility]?"

**Why they say yes:**
1. Curb appeal matters — dirty facilities signal neglect to renters
2. Soft-wash protects the metal panels (pressure washing damages them)
3. One-call, multi-site deal = minimal effort on their end
4. No other local power washing company is actively targeting this segment (blue ocean)

---

## Sequence Assignment

Route into the **Property Manager sequence** (`6a048cfc110bc620ca0f1aee`) using the `_lead_type: property_manager` flag. Apollo search will auto-route via DANNY_ORG_KEYWORDS.

**Subject line to test:** "Algae on the concrete pads — quick question"
**Touch 1 angle:** Problem (algae on concrete/facade) → soft-wash solution → quick quote offer

---

## Timing

- **Pull:** Weeks 21–22 (now through June 1) alongside existing county rotation
- **Enrollment:** June 4 Round 2 batch (all new leads from May 25–June 1 pulls)
- **Estimated pipeline value:** 5 district managers = $36,000–$64,000/year recurring if converted

---

## Action Items

- [ ] Danny runs Apollo pull with self-storage keywords (auto-included in Week 22 Medina run)
- [ ] Review leads file — filter for `self storage` / `storage` in company name
- [ ] Enroll in PM sequence on June 4 with Round 2 batch
- [ ] Consider writing a 3-touch self-storage-specific sequence (distinct from PM sequence) for June Booking Blitz

---
*Self-storage Apollo keywords added to `integrations/mixmax.py` (PROPERTY_MANAGER_TITLES) and `workers/lead_pipeline.py` (DANNY_TITLES + DANNY_ORG_KEYWORDS) on 2026-05-25 Run 87.*
