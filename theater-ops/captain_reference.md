# Captain Reference — "AI OS" System
*Canonical instructions and routing for all Captains — the placement law, the spoke pointer rows, the reading order, and the `%compose` brief template. HANK and Meridian consult it whenever reasoning turns on a Captain's capability.*
*HUB. This file carries NO unit rows of any kind. Every Captain — shared or arm-owned — is catalogued in a SPOKE: shared Captains in "theater-ops/_shared-captain-library/shared_manifest.md", arm Captains in that arm's "<arm>_manifest.md". One unit, one catalog.*

---
## Placement & Promotion
- **Placement (structural, now):** dependency test. A Captain defaults to `_shared-captain-library/` (shared, domain-agnostic). It moves into a domain arm ONLY if it depends on that domain's data or context. Placement decides catalog: a shared Captain gets its row in "_shared-captain-library/shared_manifest.md"; an arm Captain gets its row in that arm's "<arm>_manifest.md". Neither carries a row in THIS file — which spoke holds a Captain's row is what declares its placement, by construction, and that is why no spoke needs a `Domain` column.
- **Promotion (usage, roadmap):** usage-rate-driven elevation is deferred to the Affirmative Detection / telemetry roadmap. `AffDet`(Affirmative Detection) already counts per-Captain invocations — that is the substrate a future promotion rule will read. No threshold is codified until live invocation data exists (evals are hypotheses until live-tested).
- **Genericity (`GenNotSpec`, Generic Not Specific):** a Function Contract states the SHAPE of a constraint. A live external identifier — a CRM record, a contact ID, a named person — creates a dependency the AI OS cannot see and cannot maintain, so it belongs in a Confirmation Discipline note as evidence, never in a Constraints line, a `constants` entry, or a `conditional` rule. Test before the write: if that record were deleted tomorrow, would the contract still say what to do?

---
## Domain Arms — Spoke Catalogs
*Read the spoke for its Captain rows. Every row below is a pointer; no unit row lives in this file.*

| Arm | Spoke Catalog | Captains | Substrate |
|---|---|---|---|
| Shared Captain Library | "theater-ops/_shared-captain-library/shared_manifest.md" | `youtube_transcript` · `web_search` · `web_fetch` · `browser_scrape` · `rss_reader` | CoWork-native · Claude in Chrome MCP |
| CRM Ops | "theater-ops/crm-ops/crm-ops_manifest.md" | `hubspot_contact_lookup` · `hubspot_contact_create` · `hubspot_contact_update` · `hubspot_contact_search` · `hubspot_contact_note_create` | HubSpot MCP |

*The Shared Captain Library is not a domain arm — it is the default placement every Captain starts in. It earns a row here because it is a SPOKE, and every spoke must be reachable from this hub.*

---
## Reading Order
```
captain_reference.md (hub) -> pointer row -> "<spoke>_manifest.md" -> the Captain's Function Contract
```
Every Captain costs the same two hops — hub, spoke, spec. That symmetry is the point of the relocation: the hub stopped growing with every shared Captain added, and a shared Captain and an arm Captain are resolved by one identical procedure instead of two. Never read the spokes blind — same discipline "archive_manifest.md" gives `%recall`.

---
## `%compose` Lightweight Brief Template
*HANK fills this before `%shipit` on any `%compose` execution. Meridian verifies against it in lieu of a formal battle plan.*

```
## `%compose` Brief
Intent: [what the prompter asked for]
Captain sequence: [Captain 1 -> Captain 2 -> ...]
Required inputs: [what HANK must inject at each step, per the spoke catalog row]
Expected output: [what returns to HANK at end of pipeline, per the spoke catalog row]
Halt condition: [what causes Meridian to stop — missing input, empty return, API failure]
```
