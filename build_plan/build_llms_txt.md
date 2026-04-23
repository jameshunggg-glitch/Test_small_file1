# build_plan/build_llms_txt.md

## Purpose
This file defines how to build `llms.txt` for this repository.

`llms.txt` is the repository navigation index for AI agents.
Its job is to help an agent find the right entry point quickly.

It is a thin routing layer.
It is not a reading procedure document.
It is not a full architecture document.
It is not a behavior-rules file.

Behavior rules belong in `CLAUDE.md`.
Repository structure belongs in `docs/architecture.md`.
Change rules belong in `docs/change_principles.md`.

Use the matching template for final output structure.

---

## Output File
- `llms.txt`

---

## Template Reference
Use:
- `build_plan/templates/llms.template.txt`

Follow the template structure unless repository-specific conditions require a small adjustment.
Respect the placeholder legend at the top of the template.

Do not redesign the file format unless clearly necessary.

---

## Role of `llms.txt`
`llms.txt` is a repository entry index.

It should help an agent answer:

- where should I start for this task
- which file is the right entry point
- where is the repository map
- where are recent changes tracked
- where are recurring workflow guides located

`llms.txt` should reduce entry cost.
It should not try to teach the whole repository inline.

---

## Design Intent (Informative)
This short section explains the design standard for `llms.txt`.

- **Thin navigation layer.** `llms.txt` should act like a repository menu or landing page. It points to useful entry files and areas. It should not expand into long task procedures.
- **Link-and-note first.** The primary unit of value in `llms.txt` is a short path entry with a short note explaining when to open it.
- **Architecture is delegated.** `llms.txt` should point to `docs/architecture.md` for repository structure instead of restating that structure in detail.
- **Task phrasing over command phrasing.** Prefer entries such as "Understand repo layout" or "Check recent work" over imperative instructions such as "Read in this order".
- **Concise by default.** If a line does not help an agent choose the next file to open, it probably does not belong here.

These principles govern edge-case decisions.

---

## Required Inputs
To build `llms.txt`, inspect these sources first:

1. `CLAUDE.md`
2. `build_plan_overview.md`
3. repository root structure
4. `docs/`
5. major implementation directories
6. test directories
7. `skills/` if present
8. `docs/changes/` if present

Also inspect whether these files already exist:

- `AGENTS.md`
- `docs/architecture.md`
- `docs/change_principles.md`
- `docs/changes/current_index.md`
- `docs/changes/cases/README.md`

If they do not yet exist, still write `llms.txt` according to the planned standard structure, but do not invent detail for files that are not yet built.

---

## Two-Pass Build
`llms.txt` is built in two passes to resolve the `llms.txt` ↔ `docs/architecture.md` dependency:

- **First-pass** (Build Order Stage 3): produce a thin skeleton using only paths already known to exist or planned standard outputs.
- **Second-pass** (Build Order Stage 7): fill in the now-existing references and refine notes so the file becomes a useful navigation index.

Do not try to write the fullest final version during first-pass.

---

## What `llms.txt` Must Include
The built `llms.txt` should include:

1. a short purpose line
2. a pointer to `CLAUDE.md` for behavior rules
3. task-based entry points
4. a brief repository map
5. a brief set of reference pointers
6. optional entries when useful

Keep it concise and easy to scan.

---

## What `llms.txt` Must Point To
At minimum, `llms.txt` should point to:

- `CLAUDE.md`
- `docs/architecture.md`
- `docs/change_principles.md`
- `docs/changes/current_index.md`

If present and relevant, it should also point to:

- `AGENTS.md`
- `skills/` or specific `skills/.../SKILL.md`
- major implementation directories
- major test directories
- `docs/changes/cases/README.md`

Do not include paths that do not exist unless they are standard outputs currently being created in the same build process.

---

## Repository-Specific Adaptation Rules
`llms.txt` should follow the standard navigation shape, but it must still reflect the current repository.

Adapt these parts to the actual repository:

- names of implementation directories
- names of test directories
- whether `AGENTS.md` exists
- whether `skills/` exists
- whether there are multiple major code areas
- whether there are important stable docs worth using as entry points

Do not copy a generic navigation file without checking the actual repo structure.

---

## Project Meta Files Handling
Root-level auxiliary files — such as `*_goal.md`, `*_progress.md`, `*_future_work.md`, `test_output.md`, `notes.md`, or similar free-form working documents — are not listed in `llms.txt`.

`llms.txt` lists only stable navigation targets:
- `CLAUDE.md`
- `AGENTS.md` if present
- standard `docs/` outputs
- `skills/` if present
- major implementation directories
- major test directories
- stable reference pointers

Agents discover auxiliary files through directory scan or references from maintained docs.

---

## Independent Subproject Handling
If the repository contains independent subprojects:

- list each subproject as a brief entry under Repository Map
- do not provide deep internal routing from the top-level `llms.txt`
- if a subproject has its own local docs or skills, note that they exist and stop there

Detailed navigation belongs in the subproject’s own documents.

---

## Writing Rules
When writing `llms.txt`:

- keep it concise
- keep it structured
- prefer short sections over long paragraphs
- prefer task entry labels over reading procedures
- prefer path entries with short notes
- use repository paths exactly as they exist
- keep notes brief and selection-oriented
- avoid persuasive explanations
- avoid design rationale in the output
- avoid repeating rules already defined in `CLAUDE.md`
- avoid restating repository structure in detail when `docs/architecture.md` already covers it

`llms.txt` is a navigation index, not a full project guide.

---

## Task Entry Rules
The task entries in `llms.txt` should cover at least these scenarios:

- understand repo layout
- make repository changes
- check recent work or debug existing behavior
- run a recurring workflow
- find team-specific conventions

Write these as entry labels pointing to the right file or directory.
Do not turn them into detailed workflows.

---

## Evidence Rules
When deciding what to include in `llms.txt`, use evidence from:

1. actual repository structure
2. existing core docs
3. existing skills
4. existing major code and test directories

Do not include guessed modules, guessed workflows, or guessed folders.

If a directory is absent, do not mention it as if it exists.

---

## Unknown Handling
If the repository is missing expected documentation files during the build:

- still include the standard navigation path if that file is part of the planned output
- keep its note minimal and neutral
- do not claim detail that cannot yet be verified

Example:
- [docs/architecture.md](docs/architecture.md) — repository structure and major areas.

Do not add unsupported detail just to make the note richer.

---

## Update Rules
If `llms.txt` already exists:

- preserve correct stable structure
- correct outdated paths
- update notes when repository structure has changed
- keep the file concise
- avoid unnecessary full rewrites unless the file is fundamentally unusable

Prefer targeted correction over stylistic rewriting.

---

## Completion Criteria
The `llms.txt` build is complete when:

- the file exists
- it follows the template structure
- it points to the correct repository control files
- it provides useful entry points for common tasks
- it reflects the actual major repository areas
- it avoids fabricated repository-specific detail
- it remains concise and easy to scan
- it does not duplicate `CLAUDE.md` behavior rules
- it does not try to replace `docs/architecture.md`

---

## Final Reminder
Build `llms.txt` as a thin repository navigation index.

It should help an agent answer:
- where should I start
- which file should I open next
- where is the right entry point for this task

Do not use it to explain the whole project.
Do not use it to restate `CLAUDE.md`.
Do not use it to replace `docs/architecture.md`.