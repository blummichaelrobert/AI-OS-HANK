# Captain Function Contract
**Captain Name:** hubspot_contact_create
**Version:** 1.0
**Runtime:** HubSpot MCP

---

## Prose Layers (human register)

| Layer | Description |
| --- | --- |
| Purpose | Create exactly one new contact record in HubSpot CRM from a name and email already confirmed not to exist. |
| Inputs | `firstname` (string, required), `lastname` (string, required), `email` (string, required) — the minimum HubSpot needs to create a contact. `invoked_by` (string, required) — the calling Colonel's name, or `%compose`, injected by HANK at orchestration time. The Captain accepts no other fields — profile enrichment (`company`, `jobtitle`, `phone`, `city`, etc.) is out of scope, routed to the `enrich_client` Captain (not yet built). |
| Outputs | `created` (boolean) — true if the contact was written. `captain_source` (string) — always "hubspot_contact_create". `identifier` (string) — the email used, echoed back for audit. `invoked_by` (string) — the caller, echoed back. When `created: true`: `contact_id` (string) — the new HubSpot object id, and `contact_url` (string) — the HubSpot record URL, built from the object id so HANK/[the_prompter] can open the record directly rather than trusting the id alone. When `created: false`: `error` (string) — the failure reason, and `conflict` (boolean) — true when HubSpot rejected the write specifically because the email already exists, false for any other rejection (e.g. missing required property). |
| Error Behavior | On HubSpot MCP rejection, returns `{ "created": false, "captain_source": "hubspot_contact_create", "identifier": "<email>", "invoked_by": "<caller>", "error": "<reason>", "conflict": true\|false }`. The Colonel must not proceed on error, and must not silently retry with altered data — surface to HANK per Halt Protocol. No fabrication: if the MCP does not return a field, the Captain returns `null` for it — it never invents a value to fill the gap. |
| Constraints | The Captain **creates**; it does **not decide whether creation is warranted**. Duplicate resolution is not this Captain's job — the calling Colonel/HANK must invoke `hubspot_contact_lookup` on the identifier first and confirm `found: false` before this Captain is ever called. HubSpot's own email-uniqueness enforcement is a Tier 1 safety net beneath that Tier 2 pre-check, not a substitute for it — `conflict: true` on a live run means the upstream pre-check should have caught this and didn't; that gap is itself worth surfacing, not just the individual failure. The underlying `manage_crm_objects` MCP tool requires its own explicit confirmation table plus `confirmationStatus: CONFIRMED` before it will execute — HANK presents that exact table to [the_prompter], and [the_prompter]'s `%shipit` on the table satisfies `confirmationStatus` directly. One approval, satisfied twice — never a second, independent gate stacked on top of `%shipit`. One contact per invocation — batching multiple creates into a loop is the Colonel's responsibility, not this Captain's. |

---

## Two-Tier Assignment

**Tier 1 (validator):** `created` present and boolean; `captain_source` present, string, equal to "hubspot_contact_create"; `invoked_by` present and string; when `created: true`, `contact_id` and `contact_url` present and non-null; when `created: false`, `error` and `conflict` present and non-null. Structural facts only.

**Tier 2 (Meridian / Colonel / HANK):** whether the pre-check via `hubspot_contact_lookup` was actually performed and honored before this Captain was invoked — a process fact this Captain's own output cannot attest to. Whether a `conflict: true` rejection represents a race condition or a broken pre-check upstream. Whether a non-conflict `error` indicates a data-quality issue (malformed email, missing portal-required custom property) worth surfacing to [the_prompter] rather than just retrying.

---

## Validation Schema (machine register)

<!-- AIOS-VALIDATION:START -->
```json
{
  "captain": "hubspot_contact_create",
  "required": ["created", "captain_source", "invoked_by"],
  "types": {
    "created": "boolean",
    "contact_id": "string",
    "contact_url": "string",
    "captain_source": "string",
    "identifier": "string",
    "invoked_by": "string",
    "error": "string",
    "conflict": "boolean"
  },
  "constants": {
    "captain_source": "hubspot_contact_create"
  },
  "conditional": [
    { "when": {"created": true}, "require_non_null": ["contact_id", "contact_url"] },
    { "when": {"created": false}, "require_non_null": ["error", "conflict"] }
  ]
}
```
<!-- AIOS-VALIDATION:END -->

---

## Confirmation Discipline
`Status: [O].` Hypothesis until live-tested. Pull contact that is pre-checked via `hubspot_contact_lookup`, `found: false` confirmed by name and by email against the live production portal. Live create test pending [the_prompter]'s `%shipit` on the confirmation table at execution time.
