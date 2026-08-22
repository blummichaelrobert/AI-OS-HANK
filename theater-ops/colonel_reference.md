# Colonel Reference — "AI OS" System
*Canonical instructions and lookup for every arm that holds judgment roles. HANK and Meridian consult it whenever reasoning turns on a Colonel's judgment role.*
*HUB. One pointer row per domain arm. Colonels are domain-bound by definition — a Colonel carries judgment about a domain — so a Colonel's unit row ALWAYS lives in its arm's "<arm>_manifest.md", never here. This file answers "which arms hold judgment roles"; the arm catalog answers "what do they do".*

---

## Domain Arms — Spoke Catalogs
*Read the arm's own catalog for its Colonel rows. A Colonel never carries a unit row in this file.*

| Arm | Spoke Catalog | Colonels | Status summary |
|---|---|---|---|
| CRM Ops | "theater-ops/crm-ops/crm-ops_manifest.md" | `enrich_hubspot_contact` | 1 unit — [O] |

---

## Reading Order
```
colonel_reference.md (hub) -> arm pointer row -> "<arm>_manifest.md" (spoke) -> the Colonel's IFPA spec
```
Never read the arms blind. Same hub-and-spoke discipline "archive_manifest.md" gives `%recall`.