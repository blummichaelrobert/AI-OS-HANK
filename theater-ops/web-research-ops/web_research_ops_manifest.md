# Web Research Ops — Capability Catalog
*Canonical capability lookup for the `web-research-ops` arm — what each unit does, its tier, inputs, and outputs.*
*SPOKE of "theater-ops/colonel_reference.md" and "theater-ops/captain_reference.md".*

---
# FILE LOCATION REFERENCE:
| Location | Minimal Context Note |
|---|---|
| "ROOT/manifest.md" | Look up index for entire project |
| "ROOT/theater-ops/colonel_reference.md" | HUB — Colonel routing. This file is its SPOKE. |
| "ROOT/theater-ops/captain_reference.md" | HUB — Captain routing and placement law. |
| "ROOT/theater-ops/web-research-ops/web_research_ops_meridian_memory.md" | Pattern SPOKE for this folder — loaded whenever a unit here is evaluated. |
| "ROOT/theater-ops/_shared-captain-library/shared_manifest.md" | Catalog for the shared Captains this arm COMMANDS but does not own. |
| "ROOT/theater-ops/_standards/colonel_mission_brief.md" | Colonel spec standard (IFPA, Tier 2) — every unit below is authored against it. |
| "ROOT/meridian_memory.md" | pattern-library HUB — CORE patterns + SPOKE INDEX + PATTERN PLACEMENT RULE |
| "ROOT/validator.py" | Tier 1 deterministic validator (Validation Schema checker). |

**Unit specs catalogued in this file:** `browser_scrape_colonel.md` — resident in this folder, "ROOT/theater-ops/web-research-ops/".

---
## Scope
- **The domain of WORK:** turning a web address into data a mission can use — retrieve, structure, and file. The arm is named for that work, never for a browser, a connector, or a page (`NstSpn`, Nested Spine-and-Arms).
- **In scope:** judgment ABOUT web retrieval — which substrate rung to pay for, whether what came back serves the mission, whether to climb, and what to file.
- **Out of scope:** the retrieval capability itself. Every Captain this arm commands is domain-agnostic and lives in "_shared-captain-library/" — this arm owns no Captain and is not expected to.
- **Tier:** Tier 2 only. A Colonel emits judgment as prose or a composed brief, so `validator.py` never runs on a unit in this file; it runs at the Captain boundaries the Colonel declares.

---
## Active Colonel Registry — Web Research Ops

| Colonel | Tier | Purpose | Commands | Output | Status |
|---|---|---|---|---|---|
| `browser_scrape_colonel` | Tier 2 — IFPA v1.0, no validator | Extract the data a mission needs from one website and save it to a clean, structured file — at the cheapest rung that provably suffices, reporting what that cost. Holds the THREE-AXIS SUFFICIENCY TEST (thin / not-current / not-covering) and the escalation decision | `web_fetch` · `web_parse` · `web_export` (all shared) | `sufficiency_verdict` / `sufficiency_reasoning` / `substrate_used` / `climbed` + `climb_reason` / `content_length` / `extraction_scope` / `export_file_name` / `validator_verdicts` (Gate Ledger) | [C] v1.0 — 2 runs, 7 gates reconciled, escalation branch fired on named axis (c) |

**Gate declaration is not inherited.** This Colonel runs under `%compose` and therefore has no Battle Plan, so it declares its own Tier 1 Validator Gate at every Captain output boundary. Its `gates_expected` is a FORMULA — `3 + (1 if a rung is climbed else 0)` — because escalation is a genuine per-URL judgment; it resolves to an integer at the sufficiency step, before the conditional gate could fire.

---
## Captain Registry — EMPTY, and structurally so
*Absence here is a placement result, not an omission.*

Every capability this arm needs is **domain-agnostic**: fetching a URL, segmenting text, and writing a file know nothing about web research in particular, so under the Placement test in "captain_reference.md" they belong in the shared library and are catalogued in "shared_manifest.md". This arm owns judgment and commands capability — which is the Nested Spine-and-Arms pattern working as designed, not a gap to be filled.

If a Captain ever appears to belong here, test it first: can another arm use it unchanged? If yes, it is shared.

---
## Related Files
| File | Relationship |
|---|---|
| "theater-ops/colonel_reference.md" | The Colonel HUB this file is a spoke of — reading order and placement law. |
| "theater-ops/_shared-captain-library/shared_manifest.md" | Catalog for `web_fetch`, `web_parse` and `web_export` — the Captains this arm commands. |
| "web_research_ops_meridian_memory.md" | Meridian's pattern SPOKE for this folder; loaded alongside the hub whenever a unit here is under evaluation. |
| `browser_scrape_colonel.md` in this folder | The IFPA spec — seven layers, gate declaration, and Confirmation Discipline. This catalog says what the Colonel does; the spec says exactly how. |
---
