# CONFIG → Searched and Replaced Properties:
The Prompter = [the_prompter]

---
# FILE LOCATION REFERENCE:
| Location | Minimal Context Note |
|---|---|
| "ROOT/meridian.md" | Meridian identity — Inspector General / QA. Canonical spec for THE PASS IS THE TICK. |
| "ROOT/REM.md" | Nightly %REM sweep instructions — where this file is READ and counted. |
| "ROOT/meridian_memory.md" | pattern-library HUB — CORE patterns + SPOKE INDEX + PATTERN PLACEMENT RULE |
| "ROOT/validator.py" | Tier 1 deterministic validator (Validation Schema checker) — the gate this file ticks alongside. |
| "ROOT/theater-ops/captain_reference.md" | HUB — Captain routing and placement law. |
| "ROOT/theater-ops/colonel_reference.md" | HUB — Colonel routing. |

---
# AFFIRMATIVE DETECTION
*Author: Meridian — Universal QA Agent, AI OS*
*Written on SUCCESSFUL run completion only — Captains and Colonels alike. READ in full only during the %REM sweep.*
*Holds the INVOCATION LOG (ticks for runs that landed, self-authored at run completion) and AFFIRMATIVE PATTERNS (processed automation candidates). Counted at %REM.*`

## SBO frequency loop.
- **THE PASS IS THE TICK.** Meridian appends one INVOCATION LOG line on the successful completion of a run — Captain or Colonel — and on nothing else. Canonical spec: "meridian.md", Verification Stack. It lives there rather than here because it fires at run-completion time and THIS FILE IS NOT READ AT BOOT — a rule the model cannot see when it must act is not a rule.
- **PASS-ONLY.** A `pass` verdict writes a line. `output_failed`, `schema_missing`, `schema_malformed`, and any run made in test or build mode write NOTHING. This log answers "what works often," never "what was attempted."
- **Why failures are absent by design.** `[C]` is the production gate, so a unit that fails is not in service to be counted. Failure surfaces to [the_prompter] live, while an arm is being built — it is not a frequency signal and does not belong in a log read once a night.
- Every tick carries `invoked_by` = calling Colonel name, or `%compose` when the composition stood in the Colonel's slot. The field is already mandatory on every Captain schema; nothing new is collected.
- At `%REM`, Meridian counts ticks (per Captain and per `invoked_by`) over a rolling 7-day window and updates AFFIRMATIVE PATTERNS.
- Frequency Principle (2-3x/day or 4-5x/week) flags automation candidates → surfaced to HANK → [the_prompter] decides.
- Retention: do not prune INVOCATION LOG entries newer than 90 days.

## INVOCATION LOG
*Ticks for runs that landed. One line per SUCCESSFUL completion, appended self-authoring at run completion; counted by Meridian at %REM. A halted or failed run appears nowhere below.*
Format: `YYYY-MM-DD | [Captain/Colonel] | [pipeline] | %[command] | invoked_by=[caller]`


---

## AFFIRMATIVE PATTERNS
*Written by Meridian during %REM when invocation count crosses Frequency Principle threshold.*
*Frequency Principle: 2-3x/day or 4-5x/week = automation candidate.*

Format: `[TAG] | [Captain or Colonel] | [Invocation count] | [Window] | [Candidate: Y/N] | [Surfaced to HANK: Y/N] | [STATUS]`

---




