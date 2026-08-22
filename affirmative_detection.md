# CONFIG → Searched and Replaced Properties:
The Prompter = [the_prompter]

---
# AFFIRMATIVE DETECTION
*Author: Meridian — Universal QA Agent, AI OS*
*Written at every gate — Tier 1 Validator Gate (Captains) and Tier 2 Meridian Gate (Colonels). READ in full only during the %REM sweep.*
*Holds the INVOCATION LOG (raw invocation ticks, self-authored per pipeline run) and AFFIRMATIVE PATTERNS (processed automation candidates). Counted at %REM.*`

## SBO frequency loop.
- **THE GATE IS THE TICK.** Meridian appends one INVOCATION LOG line in the same action as every Tier 1 Validator Gate and every Tier 2 Meridian Gate on a Colonel — the gate and the tick are one act, not two; Colonel invocations earn their own line. Canonical spec: "meridian.md", Verification Stack. It lives there rather than here because it fires at Captain-invocation time and THIS FILE IS NOT READ AT BOOT — a rule the model cannot see when it must act is not a rule.
- Ticks are written on EVERY verdict — `pass`, `output_failed`, `schema_missing`, `schema_malformed`. A Captain that halts repeatedly is more automation-worthy, not less. Count invocations, never successes.
- Every tick carries `invoked_by` = calling Colonel name, or `%compose` when called on the fly. The field is already mandatory on every Captain schema; nothing new is collected.
- At `%REM`, Meridian counts ticks (per Captain and per `invoked_by`) over a rolling 7-day window and updates AFFIRMATIVE PATTERNS.
- Frequency Principle (2-3x/day or 4-5x/week) flags automation candidates → surfaced to HANK → [the_prompter] decides.
- Retention: do not prune INVOCATION LOG entries newer than 90 days.

## INVOCATION LOG
*Raw ticks. One line per invocation, appended self-authoring at pipeline completion; counted by Meridian at %REM.*
Format: `YYYY-MM-DD | [Captain/Colonel] | [pipeline] | %[command] | invoked_by=[caller]`


---

## AFFIRMATIVE PATTERNS
*Written by Meridian during %REM when invocation count crosses Frequency Principle threshold.*
*Frequency Principle: 2-3x/day or 4-5x/week = automation candidate.*

Format: `[TAG] | [Captain or Colonel] | [Invocation count] | [Window] | [Candidate: Y/N] | [Surfaced to HANK: Y/N] | [STATUS]`

---




