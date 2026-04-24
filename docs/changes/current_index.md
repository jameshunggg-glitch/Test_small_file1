# Recent Changes Index

## How to Read
- Each entry below uses a fixed seven-field format. Do not reorder or omit fields.
- Search by `area`, `modified_files`, `purpose`, or `case_number` before opening any detailed case record.
- Open the `detail_path` only when the index entry looks relevant to the current task.

## Entries

---
case_number: 20260423_case0001_summarizer-cleanup
change_date: 2026-04-23
area: summarizer
purpose: Strip boilerplate (Read more, subscribe, nav/footer) from extracted article text before summarization
modified_files:
  - app/summarizer.py
  - tests/test_summarizer.py
detail_path: docs/changes/cases/20260423_case0001_summarizer-cleanup/change.md
status: done
---

Fixed field legend (for reference when adding entries):

```
---
case_number: YYYYMMDD_caseNNNN_kebab-description
change_date: YYYY-MM-DD
area: module or area name
purpose: one-line purpose
modified_files:
  - path/to/file
detail_path: docs/changes/cases/<case-folder>/change.md
status: done | in-progress | blocked | reverted
---
```
