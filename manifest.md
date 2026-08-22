# MANIFEST.md
*AI OS File System/Pointers*
*The Index for the whole project*
*File Names and Drive ID's only -> keeps the manifest lightweight*

## `%sync` EXCLUSION LIST: (this is parent copy)
`%sync` operations do not apply to the folders on this list. The folders on this list are exluded from the **Drive File ID Retrieval** rule. 
| Path | Reason |
|---|---|
| __pycache__/ (any location) | Python runtime artifact. Known, ignored. |
| .DS_Store (any location) | macOS Finder metadata artifact. Local-mount only — never present in Drive, so it can produce no manifest gap. Same class as __pycache__/. Known, ignored. |
| peggy-io/peggy-output/ | Peggy-generated output files — not part of AI OS boot sequence or memory/learning processes. |
| cos-output/ | HANK-generated output files — not part of AI OS boot sequence or memory/learning processes. |
| .git/, .gitignore, .gitattributes, .gdriveignore (ROOT only) | Git/version-control infrastructure — not part of AI OS boot sequence or memory/learning processes. |
|staging-area/| transit center, not for long term storage. |

---
### START REGION: DELETABLE INITIAL SYNC BLOCK
[IF this tag exists, THEN perform the following steps]
```
1. IF Drive ID's are not present THEN initial %sync has not been performed.
2. Perform inital %sync and replace the tags "[Drive ID HERE]" below with the files Google Drive ID.
3. Remove this REGION.
4. IF there are any commented lines that start with a '#' character THEN uncomment the lines by deleting JUST the '#' character. `grep` for "# manifest.md" within .gitignore.
5. Writes and %sync are approved %shipi
5. Writes and %sync are approved %shipit.
6. Confirm to (The Prompter)[the_prompter] that gitignore has been updated and all folders/subfolders have been mapped.
```
### END REGION: DELETABLE INITIAL SYNC BLOCK 

## ROOT/
**Folder ID:** [Drive ID HERE]

| File | ID |
|---|---|
| pi.md | [Drive ID HERE] |
| manifest.md | [Drive ID HERE] |
| cos.md | [Drive ID HERE] |
| cos_memory.md | [Drive ID HERE] |
| meridian.md | [Drive ID HERE] |
| meridian_memory.md | [Drive ID HERE] |
| ps_peggy_winters.md | [Drive ID HERE] |
| field_manual.md | [Drive ID HERE] |
| affirmative_detection.md |[Drive ID HERE] |
| REM.md | [Drive ID HERE] |
| validator.py | [Drive ID HERE] |

**Subfolders:**
| Folder | ID |
|---|---|
| _code-tools | [Drive ID HERE] |
| archive | [Drive ID HERE] |
| theater-ops | [Drive ID HERE] |

---

## theater-ops/
**Folder ID:** [Drive ID HERE]

| File | ID |
|---|---|
| captain_reference.md | [Drive ID HERE] |
| colonel_reference.md | [Drive ID HERE] |

**Subfolders:**
| Folder | ID |
|---|---|
| _standards | [Drive ID HERE] |
| _shared-captain-library |
| crm-ops | [Drive ID HERE] |

---

### theater-ops/_standards/
**Folder ID:** [Drive ID HERE]

| File | ID |
|---|---|
| captain_function_contract.md | [Drive ID HERE] |
| cos_battle_plan.md | [Drive ID HERE] |
| colonel_mission_brief.md | [Drive ID HERE] |

**Subfolders:** none.

---

### theater-ops/_shared-captain-library/
**Folder ID:** [Drive ID HERE]

| File | ID |
|---|---|
| youtube_transcript.md | [Drive ID HERE] |
| web_search.md | [Drive ID HERE] |
| web_fetch.md | [Drive ID HERE] |
| browser_scrape.md | [Drive ID HERE] |
| rss_reader.md | [Drive ID HERE] |
| shared_meridian_memory.md | [Drive ID HERE] |

**Subfolders:** none.

---

### theater-ops/crm-ops/
**Folder ID:** [Drive ID HERE]

| File | ID |
|---|---|
| crm-ops_manifest.md | [Drive ID HERE] |
| enrich_hubspot_contact.md | [Drive ID HERE] |
| hubspot_contact_lookup.md | [Drive ID HERE] |
| hubspot_contact_create.md | [Drive ID HERE] |
| hubspot_contact_update.md | [Drive ID HERE] |
| hubspot_contact_search.md | [Drive ID HERE] |
| hubspot_contact_note_create.md | [Drive ID HERE] |
| crm-ops_meridian_memory.md | [Drive ID HERE] |

**Subfolders:** none.

---

## _code-tools/
**Folder ID:** [Drive ID HERE]
**Files:** none at ROOT of this folder.

**Subfolders:**
| Folder | ID |
|---|---|
| _python-tools | [Drive ID HERE] |
| _html-tools | [Drive ID HERE]|
| _web-script-tools | [Drive ID HERE] |

---

### _code-tools/_python-tools/
**Folder ID:** [Drive ID HERE]

| File | ID |
|---|---|
| fetch_decode.py | [Drive ID HERE] |

**Subfolders:** none.

---

### _code-tools/_html-tools/
**Folder ID:** [Drive ID HERE]

**Files:** none. Empty at creation 2026-08-13.
**Subfolders:** none.

---

### _code-tools/_web-script-tools/
**Folder ID:** [Drive ID HERE]

**Files:** none.

**Subfolders:**
| Folder | ID |
|---|---|
| _javascript-tools | [Drive ID HERE] | NEW, created 2026-08-13. `.js` lane per FileLane. EMPTY at creation. |
| _typescript-tools | [Drive ID HERE] | NEW, created 2026-08-13. `.tsx` lane per FileLane — closes the gap Meridian flagged (FileLane names four file types; the original three-folder proposal left `.tsx` homeless). EMPTY at creation. |

---

## archive/
**Folder ID:** [Drive ID HERE]

| File | ID |
|---|---|
| archive_manifest.md | [Drive ID HERE] | Hub-and-spoke index for %archive. Populated — 21 rows (through 2026-08-12). Row count corrected 2026-08-14 (%REM MG-02); previously read 17 rows through 2026-07-14. |

**Subfolders:**
| Folder | ID |
|---|---|
| 2026 | [Drive ID HERE] |

---

### archive/2026/
**Folder ID:** [Drive ID HERE]

**Files:** none at this level.

**Subfolders:**
| Folder | ID |
|---|---|
| June | [Drive ID HERE] |
| July | [Drive ID HERE] |
| August | [Drive ID HERE] |

---

### archive/2026/August/
**Folder ID:** [Drive ID HERE]

| File | ID |
|---|---|
none.

**Subfolders:** none.

---
