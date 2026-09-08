# Colonel Reference — "AI OS" System
*Canonical instructions and lookup for every arm that holds judgment roles. HANK and Meridian consult it whenever reasoning turns on a Colonel's judgment role.*
*HUB. One pointer row per domain arm. Colonels are domain-bound by definition — a Colonel carries judgment about a domain — so a Colonel's unit row ALWAYS lives in its arm's "<arm>_manifest.md", never here. This file answers "which arms hold judgment roles"; the arm catalog answers "what do they do".*

---
# FILE LOCATION REFERENCE:
| Location | Minimal Context Note |
|---|---|
| "ROOT/manifest.md" | Look up index for entire project |
| "ROOT/cos.md" | HANK identity + command reference |
| "ROOT/meridian.md" | Meridian identity — Inspector General / QA. |
| "ROOT/meridian_memory.md" | pattern-library HUB — CORE patterns + SPOKE INDEX + PATTERN PLACEMENT RULE |
| "ROOT/theater-ops/captain_reference.md" | HUB — Captain routing and placement law. |
| "ROOT/theater-ops/crm-ops/crm_ops_manifest.md" | SPOKE catalog — CRM Ops arm (Captains + Colonels). |
| "ROOT/theater-ops/web-research-ops/web_research_ops_manifest.md" | SPOKE catalog — Web Research Ops arm (Colonels only). |
| "ROOT/theater-ops/visual-production-ops/visual_production_ops_manifest.md" | SPOKE catalog — Visual Production Ops arm (Colonels only). |
| "ROOT/theater-ops/_standards/colonel_mission_brief.md" | Mission Brief template (IFPA Layer 1) — the Colonel spec standard. |
| "ROOT/theater-ops/_standards/cos_battle_plan.md" | Battle Plan template / source of truth for a pipeline |
| "ROOT/archive/archive_manifest.md" | Hub-and-spoke index for %archive — the retrieval precedent cited in Reading Order. |

---

## Domain Arms — Spoke Catalogs
*Read the arm's own catalog for its Colonel rows. A Colonel never carries a unit row in this file.*

| Arm | Spoke Catalog | Colonels | Status summary |
|---|---|---|---|
| CRM Ops | "theater-ops/crm-ops/crm_ops_manifest.md" | `enrich_hubspot_contact` | 1 unit — [O] |
| Web Research Ops | "theater-ops/web-research-ops/web_research_ops_manifest.md" | `browser_scrape_colonel` | 1 unit — [C] |
| Visual Production Ops | "theater-ops/visual-production-ops/visual_production_ops_manifest.md" | `visual_concept_colonel` | 1 unit — [C] |

---

## Reading Order
```
colonel_reference.md (hub) -> arm pointer row -> "<arm>_manifest.md" (spoke) -> the Colonel's IFPA spec
```
Never read the arms blind. Same hub-and-spoke discipline "archive_manifest.md" gives `%recall`.

---

## NAMING LAW — a Colonel's filename ends `_colonel.md`
*Placement law, stated here because this is the file an author reads at authoring time (`RuleWhrRd`, a rule must live where it fires). MANDATORY, not stylistic — Meridian flags a violation at spec review.*

```
<work_name>_colonel.md        e.g. browser_scrape_colonel.md
```

**Two reasons, and the second is the load-bearing one.**
1. A Colonel and a Captain sit side by side in an arm folder and are read by different rules at different tiers. The suffix makes the tier legible from the filename alone, before any file is opened.
2. `NstSpn`(Nested Spine-and-Arms) already forbids naming an ARM for the tool underneath it; the same discipline applies to the unit. **The `<work_name>` names the WORK the Colonel commands, never the Captain it happens to call** — a Colonel named after a Captain rebuilds the coupling the two-tier split exists to dissolve, and it goes stale the moment that Captain is retired.

**Scope:** every Colonel, in every arm, from this rule forward. Existing Colonels are renamed on their next touch, with references updated in the same action — a rename that leaves a stale pointer is worse than the old name.