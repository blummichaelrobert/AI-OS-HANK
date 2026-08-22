# Captain Function Contract
**AI OS Apps or Software — V3 Standard**
**Captain Name:** youtube_transcript
**Version:** 1.0
**Runtime:** Claude in Chrome MCP

---
The **Function Contract** is the Captain standard.
The Function Contract defines a unit of work and the unit of governance in the same object.
No Ethos or Initiative — those belong to the Colonel commanding it.
The Colonel brings judgment. The Captain brings capability.

**Bilingual:** the prose layers below are for the human; the **Validation Schema** block is for the validator — a deterministic twin the engine consumes to return pass/fail without judgment.

---

## Prose Layers (human register)

| Layer | Description |
| --- | --- |
| Purpose | Navigate to a YouTube URL via Claude in Chrome, expand the description ("...more"), click "Show transcript," extract the full transcript text, and return it with video metadata. |
| Inputs | `video_url` (string, required) — full YouTube watch URL (e.g. `https://www.youtube.com/watch?v=VIDEO_ID`). `invoked_by` (string, required) — calling Colonel, or `%compose` when called on the fly; injected by HANK at orchestration time. |
| Outputs | `extracted` (boolean) — `true` if the transcript was pulled from the page, `false` otherwise; always present. `video_url` (string) — the URL passed in; always present. `captain_source` (string) — always `"youtube_transcript"`. `invoked_by` (string) — echoed caller. `video_title` (string) — page title of the video; present on success. `transcript_raw` (string) — full transcript text extracted from the page; present on success. `failure_reason` (string) — describes the specific failure point; present on failure. |
| Error Behavior | If "Show transcript" is not found, or the panel is still empty after the full async poll-and-retry (Extraction Method note 4) — never on a still-loading/spinner panel: return `extracted: false`, omit or null `transcript_raw` and `video_title`, and populate `failure_reason` with the specific failure point. Do not attempt to summarize, infer, or reconstruct on failure. Surface to the Colonel. |
| Constraints | Requires Claude in Chrome MCP connected — no fallback to WebFetch. Operates on the single URL passed in — does not follow links or navigate to related videos. Does not click play or interact with the video player. Transcript must be present on page before extraction is returned — no inference or reconstruction of missing content. |

---

## Two-Tier Verification

**Tier 1 — Code (the validator).** Structural truth: `extracted`, `video_url`, `captain_source`, `invoked_by` present and correctly typed on every run; `captain_source` equals the constant; conditional non-null holds for the success and failure branches. Deterministic, unappealable.

**Tier 2 — Model (Meridian).** Semantic truth the schema cannot check: is `transcript_raw` the *actual* transcript rather than captions of an ad or a partial panel; is `video_title` the real title; is a `failure_reason` accurate. Stays with the Colonel and Meridian.

---

## Validation Schema (machine register) — MANDATORY

<!-- AIOS-VALIDATION:START -->
```json
{
  "captain": "youtube_transcript",
  "required": ["extracted", "video_url", "captain_source", "invoked_by"],
  "types": {
    "extracted": "boolean",
    "video_url": "string",
    "video_title": "string",
    "transcript_raw": "string",
    "failure_reason": "string",
    "captain_source": "string",
    "invoked_by": "string"
  },
  "constants": {
    "captain_source": "youtube_transcript"
  },
  "conditional": [
    { "when": {"extracted": true}, "require_non_null": ["video_title", "transcript_raw"] },
    { "when": {"extracted": false}, "require_non_null": ["failure_reason"] }
  ]
}
```
<!-- AIOS-VALIDATION:END -->

Read against the contract: `extracted`, `video_url`, `captain_source`, `invoked_by` always present (`required`); `video_title` + `transcript_raw` non-null only on success, `failure_reason` non-null only on failure (`conditional`); `captain_source` pinned to the Captain's own name (`constants`). Presence and type are Tier 1; whether the extracted text is the true, complete transcript is Tier 2 — the Colonel's call.

---

## Confirmation Discipline

This schema is a **hypothesis until a live extraction runs against it** and earns `[C]`. Browser automation is DOM-fragile — the "...more" and "Show transcript" click path, panel load timing, and the title selector are exactly the facts a live run reveals. Expect Schema Fold-Back candidates after first contact. Per **Captain Authorship Lanes** (canonical in `captain_function_contract.md`): HANK authored this contract behind `%shipit`; any fold-back tightening of a live run routes through [the_prompter]'s gate — Meridian surfaces and re-verifies, never writes the Captain it audits.

---

## Extraction Method — Live Notes from fold-back

**1. Transcript panel selectors — two variants, poll both.**
YouTube serves one of two transcript panels; either may appear, so support both and extract
from whichever populates — do not assume modern (observed: modern on some videos, legacy on others).
- Modern: panel target-id `PAmodern_transcript_view`; segments `transcript-segment-view-model`;
  text node `span[role="text"]` (a.k.a. `span.ytAttributedStringHost`); timestamp in
  `div.ytwTranscriptSegmentViewModelTimestamp`.
- Legacy: panel target-id `engagement-panel-searchable-transcript`; segments
  `ytd-transcript-segment-renderer`; text node `.segment-text` (a.k.a.
  `yt-formatted-string.segment-text`); timestamp in `.segment-timestamp`.
- Timestamps never enter `transcript_raw` — excluded by selecting only the text node in both variants.
- Scope extraction to the panel whose visibility is `ENGAGEMENT_PANEL_VISIBILITY_EXPANDED`.
  Hidden duplicate panels exist and double-count (observed 1,084 raw nodes across panels vs 542
  in the expanded one).

**2. Clear obstructions BEFORE clicking "Show transcript."**
- Dismiss the "YouTube Premium" promo popup ("No thanks") if present — it can occlude the transcript controls.
- Click the video's "Skip"/"Skip ad" button as soon as it becomes clickable. Poll for it and click the moment it is available — an active ad overlay blocks interaction and can inject ad captions into the panel. Skip first, then proceed.

**3. Use a real click, not a programmatic one.**
A JS `.click()` on the "Show transcript" button did not open the panel. Locate the element, then issue a genuine user-level click to trigger the engagement panel.

**4. Panel loads asynchronously — poll segments, retry the open, fail only at the end.**
The transcript panel fetches its content async and is the most fragile step; the click is not
the finish line.
- On open, the panel first renders a loading spinner (`tp-yt-paper-spinner` /
  `yt-content-loading-renderer`) with zero segments, and can briefly stay
  `ENGAGEMENT_PANEL_VISIBILITY_HIDDEN`. Observed: a first click landed the panel in a
  hidden/spinner state and a ~14s poll returned zero; a second click + longer wait populated
  143 segments.
- Poll on the COMBINED segment count of both selectors (`transcript-segment-view-model` +
  `ytd-transcript-segment-renderer`) inside the expanded panel — not on panel presence, not on
  the modern selector alone — with a generous ceiling (~18–20s).
- Retry SAFELY: "Show transcript" is a toggle, and re-clicking an opening panel CLOSES it
  (observed: a blind re-click collapsed the panel). Before any re-click, confirm the panel is
  still `ENGAGEMENT_PANEL_VISIBILITY_HIDDEN`, with zero segments and no loading spinner. Only
  then re-click once. Otherwise keep polling without clicking.
- Failure discipline: an empty panel still showing the spinner = still loading, keep waiting.
  Return `extracted: false` ONLY after the full timeout elapses with the panel expanded and
  zero segments. An empty-but-loading panel must never be read as "no transcript" — that is
  the false-negative this note exists to prevent.
- Two "Show transcript" instances exist on the page (primary + duplicate); target the first
  and re-click the same one for consistency.
