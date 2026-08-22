# ARCHIVE MANIFEST
*Hub-and-spoke index for "archive/YYYY/Month/YYYY_Month_archive.md" files.*
*One line per `%archive` entry — date, one-line keyphrase, source file. Not a summary, not a schema. `%recall` reads this table first, then opens only the matching archive file.*
*Written by HANK in the same action as every `%archive` command. Never a separate step.*

---
# SYNTAX KEY
*One symbol, one definition — the shared notation every core file is read through.*

| Token | Meaning |
|---|---|
| `->` | Directional flow — output of the left feeds input of the right. Universal: pipeline steps, event chains, agent addressing (`HANK -> do X`), prompter instructions (`Michael -> HANK -> Colonel`). |
| `()` | Grouping — membership in a set. No hierarchy, no sequence implied. |
| `%` | Command prefix — the delegation trigger. Michael issues a `%` command; the CNS carries it out. |
| `\|` | Field separator (within single-line entries and tables). |
| `[F]` | Status — Final / Resolved. |
| `[O]` | Status — Open / Unresolved. |
| `[S]` | Status — Superseded. |
| `[R]` | Status — Retained for semantic reinforcement; not prunable by Meridian. |
| `[C]` | Status — Confirmed via live test (with explicit `%shipit`). |

---
# WRITE RULE
Every `%archive` command appends exactly one row here, in the same response that appends to the dated archive file. If the manifest row is missing, the archive write is incomplete — not a separate task to catch up on later.

---
## Entry Format
`YYYY-MM-DD HH:MM | [one-line keyphrase] | archive/YYYY/Month/YYYY_Month_archive.md`

Keyphrase must be specific enough to discriminate this entry from others in the same month — not generic filler ("discussion about project," "notes"). Meridian spot-checks this during `%REM`.

---
## Index
