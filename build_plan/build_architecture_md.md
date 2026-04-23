# build_plan/build_architecture_md.md

## Purpose
This file defines how to build `docs/architecture.md` for this repository.

`docs/architecture.md` is the high-level repository structure document.
Its job is to help an agent or engineer quickly understand how the repository is organized, what the main areas are, and how the major control files, docs, and implementation areas relate to each other.

This file does not define the final output format by itself.
Use the matching template for output structure.

This file does not define change responsibilities.
Those belong in `docs/change_principles.md`.

---

## Output File
- `docs/architecture.md`

---

## Template Reference
Use:
- `build_plan/templates/architecture.template.md`

Follow the template structure unless the current repository requires a small repository-specific adjustment.
Respect the placeholder legend at the top of the template.

Do not redesign the document shape unless clearly necessary.

---

## Role of `docs/architecture.md`
`docs/architecture.md` is a repository structure map.

It should help the reader answer:

- what this repository is for
- what the main top-level areas are
- what the major implementation areas are
- what the main control files do
- where task-specific guidance lives
- where validation lives
- what should be treated as source of truth

It should provide structure understanding, not deep implementation detail.

It should not become:
- a code walkthrough
- a change log
- a process memo
- a business strategy document
- a line-by-line explanation of modules

---

## Required Inputs
To build `docs/architecture.md`, inspect these sources first:

1. repository root structure
2. `CLAUDE.md`
3. `llms.txt` if already built
4. `build_plan_overview.md`
5. `docs/` contents
6. `build_plan/` contents
7. major implementation directories
8. major test directories
9. `skills/` if present
10. support directories such as `scripts/` if present

Also inspect whether these files already exist:

- `docs/architecture.md`
- `docs/change_principles.md`
- `docs/changes/current_index.md`

If related files do not yet exist, do not invent detailed content for them.
You may still describe their planned role if they are standard outputs defined by the repository build process.

---

## What `docs/architecture.md` Must Include
The built `docs/architecture.md` should include:

1. the purpose of the repository
2. a repository overview
3. the main top-level areas
4. the major implementation areas
5. the role of root-level control files
6. the role of `docs/`
7. the role of `skills/` if present
8. the role of validation areas such as tests
9. a source-of-truth note

Keep the document high-level and structural.

---

## What `docs/architecture.md` Must Describe
At minimum, describe these areas if they exist:

- root-level control files such as `CLAUDE.md` and `llms.txt`
- `docs/`
- `build_plan/`
- `skills/` (root-level only; nested `<subproject>/skills/` is covered by the Independent Subproject Rules below)
- major implementation directories
- major test directories
- support directories such as `scripts/`

For implementation areas, describe them at directory or major module level.
Do not attempt a full file-by-file inventory.

---

## Repository-Specific Adaptation Rules
`docs/architecture.md` should follow the company-standard structure, but the content must be adapted to the actual repository.

Adapt these parts to the current repository:

- actual directory names
- actual major implementation areas
- actual test layout
- whether `skills/` exists
- whether `build_plan/` exists
- whether support utility areas exist
- whether the repository has one main code area or several

Do not paste a generic repository map without checking the real structure.

---

## Writing Rules
When writing `docs/architecture.md`:

- keep the content high-level
- focus on structure, boundaries, and roles
- use repository paths exactly as they exist
- describe areas briefly but concretely
- prefer grouped explanation over long prose
- avoid deep code detail
- avoid speculative design intent
- avoid repeating global behavior rules from `CLAUDE.md`
- avoid repeating change rules from `docs/change_principles.md`

`docs/architecture.md` should explain how the repository is organized, not how every part works internally.

---

## Implementation Area Rules
When describing implementation areas:

- describe the major directory or module purpose
- mention its relationship to the repository if useful
- keep descriptions brief
- do not list every file
- do not infer submodule responsibilities that cannot be verified

Good examples:
- "`src/routing/` contains core routing and path-planning logic."
- "`tests/` contains repository validation and regression coverage."

Avoid unsupported detail such as exact flows or responsibilities that are not visible from the repository.

---

## Project Meta Files Handling
Root-level auxiliary files — such as `*_goal.md`, `*_progress.md`, `*_future_work.md`, `test_output.md`, `notes.md`, or similar free-form working documents — are **not listed in `docs/architecture.md`**, regardless of whether other documents reference them.

`docs/architecture.md` describes structural areas: root-level control files (as defined by the template), `docs/`, `build_plan/` (during build only), `skills/` (if present), major implementation directories, major test directories, support directories. Auxiliary notes at root level are not part of this structural skeleton and do not belong here, regardless of how many exist or what topics they cover.

These files must still not be deleted, renamed, or rewritten (per `build_plan_overview.md` §File Tree Setup).

Rationale: listing auxiliary files would require a judgment call about "what counts as authoritative enough to list". SOP v1.0.0 removes such judgment calls (see `build_plan_overview.md` §Design Principle).

A corresponding rule exists in `build_plan/build_llms_txt.md` so the two outputs stay consistent.

---

## Independent Subproject Rules
If the repository contains independent subprojects residing under the repository root — each with its own entrypoint, dependency file, tests, or goal/progress doc — treat each subproject as a separate top-level area in §5 Main Implementation Areas.

Indicators a directory is an independent subproject:
- it has its own entrypoint file (`main.py`, `index.ts`, `app.py`, etc.)
- it has its own dependency manifest (`requirements.txt`, `package.json`, etc.)
- it has its own test directory
- it has its own goal, progress, or README file at the subproject root

Rules:
- List each subproject as a distinct one-line entry. Do not merge them into a single implementation description.
- Describe the subproject's purpose at high level only. Do not recurse into its internal modules.
- If a subproject has its own local `skills/`, `tests/`, or docs, mention that they exist at the subproject level, and stop.
- Do not invent cross-subproject architecture that the repository does not document.

A subdirectory that only contains shared utilities, or that is clearly part of a single codebase, should not be treated as independent.

---

## Root-Level File Rules
When describing root-level control files, focus on role only.

Examples of role-level descriptions:
- `CLAUDE.md` defines global operating rules for agents.
- `llms.txt` provides a navigation path for reading the repository.
- `README.md` provides human-oriented project onboarding if present.

Do not restate their full content.
Do not duplicate instructions already contained in those files.

---

## Evidence Rules
When deciding what to include in `docs/architecture.md`, use evidence from:

1. actual repository structure
2. existing core docs
3. implementation directory names and organization
4. test layout
5. explicit repository conventions visible in the repo

Do not infer architecture details that are not supported by repository evidence.

If a major area is unclear, describe it cautiously and at a high level.

---

## Unknown Handling
If some repository areas exist but their exact role is unclear:

- describe only what can be verified
- keep the description broad and neutral
- use `Unknown`, `Needs confirmation`, or `Not yet documented` when needed

Do not invent detailed module purpose.
Do not invent workflow relationships.
Do not force precision where the repository does not support it.

---

## Update Rules
If `docs/architecture.md` already exists:

- preserve correct stable sections
- update outdated structure references
- add missing major areas if needed
- keep section order stable where possible
- avoid unnecessary full rewrites unless the file is fundamentally unusable

Prefer structural correction over stylistic rewriting.

---

## Completion Criteria
The `docs/architecture.md` build is complete when:

- the file exists
- it follows the template structure
- it reflects the actual major repository areas
- it describes the main control files and top-level areas
- it stays high-level rather than file-by-file
- it avoids fabricated repository-specific details
- it remains concise, clear, and easy to scan

---

## Final Reminder
Build `docs/architecture.md` as a high-level repository map.

It should help a reader answer:
- what is in this repository
- where the main areas are
- what the important top-level files do
- which areas hold implementation, documentation, skills, and validation

Do not use it as a change log.
Do not use it as a code walkthrough.
Do not use it to guess undocumented architecture intent.