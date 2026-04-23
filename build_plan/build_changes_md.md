# build_plan/build_changes_md.md

## Purpose
This file defines how to build and maintain the `docs/changes/` tracking system for this repository.

`docs/changes/` is the repository's internal change-tracking system.
It is a two-layer structure:

- a lightweight, searchable index of recent modifications
- detailed per-case records located under `cases/`

This system is not a public changelog or release notes. It exists so that agents and engineers can answer, at low token cost, what was changed recently in a given area before editing or debugging.

This file does not define the final output format by itself.
Use the matching templates for output structure.

---

## Output Files
- `docs/changes/current_index.md`
- `docs/changes/archive_index_YYYY_MM.md` (one per archived month, created on rotation)
- `docs/changes/cases/<case-folder>/change.md` (one folder per change)

---

## Template References
Use:

- `build_plan/templates/current_index.template.md` — for both `current_index.md` and archive index files
- `build_plan/templates/change_case.template.md` — for each `cases/<case-folder>/change.md`

Follow the template structure unless repository-specific conditions require a small adjustment.
Respect the placeholder legend at the top of each template.

Do not redesign the format unless clearly necessary.

---

## Role of `docs/changes/`
The changes system should help the reader answer:

- what was changed recently
- which files or areas were touched
- why a change was made
- where to find detailed background, validation, and follow-up
- whether a recent change is related to a current problem

It supports searching by:

- module or area name
- file path
- purpose keywords
- case number
- date

It should not become:

- a public release-notes document
- a marketing changelog
- a comprehensive commit log (Git already provides that)
- a detailed per-file edit journal

Git history remains the authoritative source for every file's edit history. The changes system is for *curated* records of meaningful changes an agent should know about before editing nearby code.

---

## Dual-Layer Design

### Layer 1: Index (lightweight)
Fixed-field entries that can be scanned quickly. Two index files:

- `current_index.md` — recent entries, typically covering the most recent month
- `archive_index_YYYY_MM.md` — one per past month, containing that month's entries

Agents read the index first to decide whether a given change is relevant to the current task.

### Layer 2: Detail (per case)
One folder per change, under `cases/`, containing a `change.md` with full background, modifications, validation, and follow-up.

Folder naming convention: `YYYYMMDD_caseNNNN_kebab-description`

- `YYYYMMDD` — date of the change (8 digits, no separator)
- `caseNNNN` — case number, typically from an internal tracker
- `kebab-description` — lowercase, hyphen-separated short description

Example: `20260420_case4834_land-crossing-fix`

Agents open a `change.md` only after the index entry looks relevant. Keep the index lightweight so the first-pass scan is cheap.

---

## Index Entry Fixed Fields
Every entry in `current_index.md` and archive indexes must use these seven fields, in this order:

1. `case_number` — matches the case folder name
2. `change_date` — `YYYY-MM-DD`
3. `area` — module or area name (for example `routing`, `pipeline`, `shared`)
4. `purpose` — one-line purpose
5. `modified_files` — list of file paths touched
6. `detail_path` — path to the `cases/<case-folder>/change.md` file
7. `status` — one of `done`, `in-progress`, `blocked`, `reverted`

Do not reorder or omit fields.
Use `Unknown` or `Needs confirmation` for a field that truly cannot be determined.

Entries are separated by `---` lines. Most recent entries appear first.

---

## Rotation Rule
`current_index.md` should contain approximately the most recent month of entries.

When entries older than one month have accumulated:

1. Create `docs/changes/archive_index_YYYY_MM.md` for the relevant month if it does not exist.
2. Move the old entries from `current_index.md` into that archive index.
3. Leave `current_index.md` with only recent entries.

This keeps `current_index.md` short and fast to scan. It does not delete history — archives remain searchable.

If the repository has a naturally low rate of recorded changes, rotation may happen less frequently. Do not rotate if `current_index.md` is still short.

---

## Case Folder Rules
For each recorded change:

1. Create folder `docs/changes/cases/<folder-name>/` following the naming convention.
2. Create `change.md` inside that folder, following `change_case.template.md`.
3. Add or update the corresponding entry in `current_index.md`.

Case folders may contain additional files if useful (screenshots, small data samples, before/after diagrams). `change.md` remains the canonical entry point.

Do not rename case folders after they have been referenced by any index entry. The `detail_path` field in the index would otherwise break.

### Naming Convention Details
The folder name format is `YYYYMMDD_caseNNNN_kebab-description`. Additional constraints:

- `case_number` (the `caseNNNN` portion, or the full `YYYYMMDD_caseNNNN_kebab-description` when used as a key) must be unique within this repository. If two changes share the same external tracker ID, disambiguate by appending a short suffix (e.g. `caseNNNN-a`, `caseNNNN-b`).
- If the repository has no external issue tracker in use (no Gitea/GitHub/GitLab/Jira Issues, or a local-only repo), use a local sequential number starting from `case0001` and incrementing for each new change within this repository (`case0001`, `case0002`, ...). The sequence is per-repository and has no relation to any external system's numbering.
- Once the repository adopts an external tracker mid-stream, existing local-sequence case numbers remain unchanged; new cases from that point on use the tracker-assigned number. The two number spaces coexist; do not renumber history.
- `kebab-description` is restricted to `[a-z0-9-]+` (lowercase ASCII letters, digits, and hyphens). No spaces, no underscores, no uppercase, no non-ASCII characters.
- `kebab-description` length: maximum 40 characters. Truncate meaningfully rather than abbreviating cryptically.
- The full folder name should be readable at a glance and searchable. If the description must be longer to be clear, prefer a slightly longer folder name over an opaque one — but keep within the 40-character limit for the description portion.

Non-ASCII characters are disallowed to avoid cross-filesystem compatibility issues (Windows, case-insensitive filesystems, filename length limits on older systems, filename escaping in URLs and search tools).

### Cases README Content

`docs/changes/cases/README.md` is the ongoing reference for the case-folder naming convention after Post-Build Cleanup removes `build_plan/`. During build, seed this file with:

- the folder naming convention (`YYYYMMDD_caseNNNN_kebab-description`)
- the `caseNNNN` source rule (external tracker ID when available; `case0001` sequence fallback otherwise, continuing the local sequence even if a tracker is adopted later)
- the `kebab-description` constraints (ASCII lowercase, digits, hyphens; max 40 chars)
- the uniqueness requirement

Keep the README short and scannable. Do not duplicate the full build spec; the README is a quick-reference card for engineers and agents recording new cases.

---

## Template Preservation for Ongoing Use
After first-install build completes, `change_case.template.md` and `current_index.template.md` remain needed on an ongoing basis — the former for every new case, the latter for monthly archive rotation. Because `build_plan_overview.md` §Post-Build Cleanup deletes the entire `build_plan/` directory in Stage 8, these two templates are copied out during Build Order Stage 6:

- `build_plan/templates/change_case.template.md` → `docs/changes/_templates/change_case.template.md`
- `build_plan/templates/current_index.template.md` → `docs/changes/_templates/current_index.template.md`

After Stage 8 cleanup, the copied templates remain under `docs/changes/_templates/` and serve as the canonical reference for future change recording. Refer to the copies, not the deleted source path, when drafting new case records or rotating the index.

The install-time-only templates (`CLAUDE.template.md`, `architecture.template.md`, `change_principles.template.md`, `llms.template.txt`) are not preserved — they are single-use during install and have no ongoing role.

---

## What `change.md` Must Include
Each `change.md` should contain these six sections, in this order:

1. Case title
2. Summary — one sentence
3. Background — problem or trigger
4. Changes Made — what was modified, grouped by file or area
5. Affected Areas — modules, directories, files touched
6. Validation — how the change was verified
7. Follow-up — remaining work, limitations, deferred items

See `change_case.template.md` for the exact structure.

---

## Required Inputs
To build or update any part of `docs/changes/`, inspect:

1. the actual change being recorded (code diff, commit, PR, or issue reference)
2. `CLAUDE.md` for any validation or record-keeping constraints
3. `docs/architecture.md` so `area` can be tagged with an actual module name
4. existing `current_index.md` to avoid duplicate entries
5. existing archive indexes to confirm a case has not already been recorded historically

---

## Writing Rules

### When writing index entries
- use the exact seven-field order
- keep `purpose` to a single line
- list only files meaningfully modified, not incidentally touched
- use real repository paths for `modified_files` and `detail_path`

### When writing detail `change.md`
- keep `Summary` to one sentence
- describe `Changes Made` at the granularity of files or areas, not line-by-line diffs
- reference test names or commands under `Validation`, not full test output
- under `Follow-up`, record real outstanding work, not aspirational ideas

### Always avoid
- pasting long code blocks into `change.md` — link to file paths instead
- duplicating Git commit messages verbatim — summarize the meaningful change
- editorializing about design choices beyond what is needed to explain the change
- creating records for speculative future changes

---

## Evidence Rules
Every entry must describe an actual change that occurred or is actively underway.

Status usage:

- `done` — change is complete and validated per this repository's Validation Principles
- `in-progress` — work is genuinely underway; `change.md` may be a stub but must exist
- `blocked` — work paused pending external input; record the blocker in `Follow-up`
- `reverted` — change was rolled back; keep the record for traceability

Do not create entries for planned changes that have not started. The changes system is curated, not exhaustive. Not every past commit needs an entry — only meaningful ones an agent should know about before editing adjacent code.

---

## Unknown Handling
If a field's value cannot be determined:

- use `Unknown` or `Needs confirmation`
- do not leave the field blank
- do not invent a plausible value

If the case boundary itself is ambiguous (for example, two related PRs or a multi-commit refactor), either record one entry with both references under `modified_files`, or create two entries that cross-reference each other in `purpose`.

---

## Update Rules

### For `current_index.md`
- add new entries at the top
- never rewrite past entries except to correct clear errors or update `status`
- do not reorder by any key other than recency
- when moving entries to an archive on rotation, preserve their content exactly

### For a `change.md`
- add new observations under the existing structure
- do not revise history silently; note when post-hoc updates occur
- if scope expanded after the original recording, update `modified_files` in the index entry and note the expansion under `Follow-up`

---

## Completion Criteria

### Per-change recording is complete when
- the case folder exists with the correct naming convention
- `change.md` follows the template and all six content sections have real content
- `current_index.md` has an entry with all seven fields filled in
- the `detail_path` in the index entry correctly resolves to the `change.md` file
- `status` reflects the actual state of the work

### The overall changes system is healthy when
- `current_index.md` remains scannable (approximately one month of entries)
- rotation to archive indexes has occurred as required
- no case folder exists without a matching index entry
- no index entry points to a missing `change.md`

### First-install exception
On the very first install of this SOP into a repository, there are no historical changes to record. An empty `current_index.md` containing only the template's fixed-field legend (no actual entries) is a legitimate "done" state and does not violate §Evidence Rules. The first real change entry is added later, when a genuine repository modification is recorded. Do not fabricate a seed entry simply to make the file look non-empty.

---

## Final Reminder
The changes system is a curated, searchable record — not a log of everything that ever happened.

It should help an agent answer:

- what changed recently in the area I am about to modify
- why a specific file was touched
- where to find background before assuming a behavior is a bug

Do not use it as a commit log.
Do not use it as release notes.
Do not use it to replace Git history.
