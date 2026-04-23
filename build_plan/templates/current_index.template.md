<!-- Template Legend (do not copy into output)
  [ROLE TEXT]         = fill in repository-specific content in place of the bracketed text
  [PATH or DIR NAME]  = replace the entire bracket with an actual repository path
  [INSTRUCTION ...]   = editorial direction for the agent; follow it, do NOT copy into the output

  Note for index entries below: bracketed placeholders may cover dates (YYYY-MM-DD),
  enum values (done | in-progress | blocked | reverted), and structured case-number
  strings. These are all still [ROLE TEXT] — fill with the appropriate value.
  They are not special syntax; the brackets are placeholder markers only.
-->

# Recent Changes Index
[INSTRUCTION: This file contains the most recent change index entries, typically covering the last month. When this file exceeds roughly one month of entries, move older blocks into `archive_index_YYYY_MM.md`; do not rotate if the file is still short. This same template is also used for `archive_index_YYYY_MM.md` files; only the title and the time range of entries differ.]

## How to Read
- Each entry below uses a fixed seven-field format. Do not reorder or omit fields.
- Search by `area`, `modified_files`, `purpose`, or `case_number` before opening any detailed case record.
- Open the `detail_path` only when the index entry looks relevant to the current task.

## Entries

---
case_number: [YYYYMMDD_caseNNNN_kebab-description]
change_date: [YYYY-MM-DD]
area: [module or area name, e.g. routing / pipeline / shared]
purpose: [one-line purpose of this change]
modified_files:
  - [PATH to file]
  - [PATH to file]
detail_path: [PATH to docs/changes/cases/<case-folder>/change.md]
status: [done | in-progress | blocked | reverted]
---

[INSTRUCTION: Add one block per change, separated by a `---` line before and after each entry. Most recent entries appear first. When this file exceeds roughly one month of entries, move older blocks into `archive_index_YYYY_MM.md`; do not rotate if the file is still short.]
