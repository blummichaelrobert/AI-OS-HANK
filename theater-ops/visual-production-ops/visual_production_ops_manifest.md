# Visual Production Ops — Arm Capability Catalog
*Canonical capability lookup for every unit that lives in this arm — Captains and Colonels both.*
*Arm: Visual Production Ops — explaining a decided concept as a produced visual asset, as a domain of work. A generative image app reached through a browser is the current substrate, not the arm's identity (`DIP`, Dependency Inversion).*

**PROMOTED 2026-09-06.** This arm lives at "ROOT/theater-ops/visual-production-ops/". Its files carry Drive IDs in "manifest.md", its pattern spoke carries a SPOKE INDEX row in "meridian_memory.md", and "colonel_reference.md" carries its pointer and arm rows — all filed in one action, per `CatMnt`(Capability Catalog Maintenance). A unit is not "done" until it is indexed.

---
# FILE LOCATION REFERENCE:
| Location | Minimal Context Note |
|---|---|
| "ROOT/manifest.md" | Look up index for entire project |
| "ROOT/theater-ops/captain_reference.md" | HUB — Captain routing and placement law. This file is its SPOKE at promotion. |
| "ROOT/theater-ops/colonel_reference.md" | HUB — Colonel routing. This file is its SPOKE at promotion. |
| "ROOT/theater-ops/visual-production-ops/visual_production_ops_meridian_memory.md" | Pattern SPOKE for this arm — loaded whenever a unit here is evaluated. |
| "ROOT/theater-ops/_shared-captain-library/shared_manifest.md" | SPOKE catalog for the shared Captains this arm depends on. |
| "ROOT/theater-ops/_standards/captain_function_contract.md" | Captain spec standard (Tier 1) |
| "ROOT/theater-ops/_standards/colonel_mission_brief.md" | Mission Brief template (IFPA Layer 1) — the Colonel spec standard. |
| "ROOT/meridian_memory.md" | pattern-library HUB — CORE patterns + SPOKE INDEX + PATTERN PLACEMENT RULE |
| "ROOT/validator.py" | Tier 1 deterministic validator (Validation Schema checker). |
| "ROOT/affirmative_detection.md" | Affirmative Detection — where each unit below ticks at its gate. |

**Unit specs catalogued in this file:** `visual_concept_colonel.md` (Colonel) — the sole arm-owned unit.

---

## Arm Scope
- **In scope:** composing a visual brief from a decided concept; driving a generative visual app; **judging whether the returned asset teaches the intended idea**; producing finished assets for outward use.
- **Out of scope:** domain-agnostic browser capability — navigation, submission, asset retrieval. Those are generic drivers and live in "_shared-captain-library/" per the Placement test in "captain_reference.md".
- **Out of scope:** the outward voice. Copy that accompanies an asset is Peggy's (`%peggy`), never this arm's.
- **Substrate today:** **Rung 4b — Claude in Chrome, ATTENDED**, because the target sits behind a sign-in wall and the wall is the evidence for the rung ("pi.md", Captain Substrate Selection). ATTENDED is empirical, not doctrinal: both known defects on this chain are OBSERVATION-WINDOW failures, so an unattended run would report clean and ship nothing. **This chain never runs unattended.** A future Rung 3 image-generation MCP joins this arm without renaming it (`DIP`).

---

## Active Captain Registry
**None. The absence is structural, not an omission.**

Every Captain this arm's Colonel commands — `navigate_and_confirm`, `submit_and_await`, `download_asset` — names nothing specific to visual production. They open a URL, submit text, and retrieve an asset; each would serve any browser-driven domain unchanged. Under the Placement test they are domain-agnostic by construction and belong in the Shared Captain Library.

An arm-owned Captain would earn a row here only if it carried visual-production domain knowledge a generic driver cannot.

---

## Active Colonel Registry

| Colonel | Mission (standing charge) | Output | Status |
|---|---|---|---|
| `visual_concept_colonel` | Turn a decided concept into an image that does its job on sight — compose the prompt, drive the app through three shared Captains, **choose among the assets that come back**, and **judge whether the chosen one actually serves the intent**, retrying or reporting an honest miss inside `max_attempts` | Composed brief — `mission_complete`, echoed injections, `prompt_composed`, `asset_count`, `candidate_selected` + `selection_rationale`, `intent_served`, `judgment_rationale`, `substrate_device_id`, and the reconciled Gate Ledger | **[C]** at v1.0 — live-confirmed 2026-09-06, ledger 3/3 reconciled independently by Meridian, all `pass`. **The hypothesis that blocked `[C]` since 2026-08-19 is closed:** it rendered `intent_served: false` on a technically excellent image, on a good-faith brief rather than a rigged one. Untested: a real SELECTION on `asset_count > 1` |

---

## Shared Captains This Arm Depends On
*Listed for reasoning convenience only. These live in "theater-ops/_shared-captain-library/" and are catalogued in "shared_manifest.md" — never duplicated here as owned rows. Route through the hub: "captain_reference.md" -> Shared Captain Library pointer row -> "shared_manifest.md".*

`navigate_and_confirm` · `submit_and_await` · `download_asset`

---
