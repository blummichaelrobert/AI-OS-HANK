# Captain Function Contract
**Captain Name:** hubspot_contact_note_create
**Version:** 1.0
**Runtime:** HubSpot MCP

---

## Prose Layers (human register)

| Layer | Description |
| --- | --- |
| Purpose | Create one free-text `NOTE` engagement in HubSpot, associated to exactly one existing contact — the AI OS's answer to per-contact context storage HubSpot already provides natively. |
| Inputs | `contact_id` (string, required) — the contact the note attaches to. `note_body` (string, required) — the text content, maps to HubSpot's `hs_note_body`. `timestamp` (string, optional, ISO 8601) — maps to `hs_timestamp`. If omitted, the Captain supplies invocation time itself rather than relying on an unconfirmed HubSpot default. `invoked_by` (string, required) — the calling Colonel's name, or `%compose`, injected by HANK at orchestration time. `hubspot_owner_id` is deliberately not exposed as an input — this portal has exactly one possible value; add only if a live test proves HubSpot requires it explicitly. |
| Outputs | `created` (boolean) — true if the note was written and associated. `captain_source` (string) — always "hubspot_contact_note_create". `contact_id` (string) — echoed back regardless of outcome. `invoked_by` (string) — the caller, echoed back. When `created: true`: `note_id` (string) — the new HubSpot engagement id. When `created: false`: `error` (string) — the failure reason. |
| Error Behavior | On HubSpot MCP rejection (`contact_id` does not resolve, or the association fails), returns `{ "created": false, "captain_source": "hubspot_contact_note_create", "contact_id": "<id>", "invoked_by": "<caller>", "error": "<reason>" }`. No fabrication: a field the MCP doesn't return comes back `null`, never invented. The Colonel must not proceed on error, and must not silently retry with altered data — surface to HANK per Halt Protocol. |
| Constraints | Runtime: HubSpot MCP (`manage_crm_objects`, create path) only. Must be associated to exactly one contact at creation — no orphan notes; uses the tool's `associations` field (`targetObjectId: contact_id`, `targetObjectType`). **Two things are hypotheses, not confirmed facts, until the first live test:** the exact `objectType` string this Captain passes for a note (`"notes"`, inferred by analogy with the lowercase-plural convention already confirmed for `contacts` — `discover_hubspot_schema` itself calls the type `NOTE`, which is not what the working create/update calls needed for contacts, so the discovery-tool name is not assumed authoritative here either), and the exact `targetObjectType` casing the association expects. Either surfaces as a clean MCP rejection on first run if wrong, not a silent failure — fold back into this contract once confirmed. One note per invocation — batch note-writing is the Colonel's responsibility. Text only — does not attach files (`hs_attachment_ids` exists on the object but is out of scope). Does not create or update the contact itself — separate Captain, same SRP boundary already held by `hubspot_contact_create` and `hubspot_contact_update`. The underlying `manage_crm_objects` MCP tool requires its own explicit confirmation table plus `confirmationStatus: CONFIRMED` before it will execute — HANK presents that exact table to [the_prompter], and [the_prompter]'s `%shipit` on the table satisfies `confirmationStatus` directly. One approval, satisfied twice — never a second, independent gate. `note_body` may come back HTML-entity-encoded rather than verbatim — confirmed live: sending `&` was stored and returned as `&amp;`. Not a Captain failure and not fabrication; a Colonel comparing sent content against stored content should expect that encoding on this field, not treat it as corruption. |

---

## Two-Tier Assignment

**Tier 1 (validator):** `created` present and boolean; `captain_source` present, string, equal to "hubspot_contact_note_create"; `invoked_by` present and string; `contact_id` present and non-null (always echoed); when `created: true`, `note_id` present and non-null; when `created: false`, `error` present and non-null. Structural facts only.

**Tier 2 (Meridian / Colonel / HANK):** whether `contact_id` names the intended contact — this Captain trusts the id given, same as `hubspot_contact_update`. Whether `note_body` content is accurate or appropriate for the mission — this Captain stores it, it does not evaluate it. On the first live run specifically: whether the `objectType`/`targetObjectType` hypotheses held, and if not, what the confirmed values actually are — a fold-back candidate the moment that's known.

---

## Validation Schema (machine register)

<!-- AIOS-VALIDATION:START -->
```json
{
  "captain": "hubspot_contact_note_create",
  "required": ["created", "captain_source", "invoked_by", "contact_id"],
  "types": {
    "created": "boolean",
    "captain_source": "string",
    "contact_id": "string",
    "note_id": "string",
    "invoked_by": "string",
    "error": "string"
  },
  "constants": {
    "captain_source": "hubspot_contact_note_create"
  },
  "conditional": [
    { "when": {"created": true}, "require_non_null": ["note_id"] },
    { "when": {"created": false}, "require_non_null": ["error"] }
  ]
}
```
<!-- AIOS-VALIDATION:END -->

---

## Confirmation Discipline
`Status: [C]` — live-confirmed. Both hypothesized strings — `objectType: "notes"` and `targetObjectType: "contacts"` — confirmed correct on first attempt, no retry needed. Independently re-read via `get_crm_objects` — content and association both confirmed, not just trusted from the create response (which again returned an empty `properties: {}`). One finding folded back into Constraints: `hs_note_body` is HTML-entity-encoded on write (`&` -> `&amp;`).
