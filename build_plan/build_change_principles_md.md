# build_plan/build_change_principles_md.md

## Purpose
This file defines how to build `docs/change_principles.md` for this repository.

`docs/change_principles.md` is the repository's cross-module change principles document.
Its job is to state the principles every change must respect — not to define workflows for each module or task type.

This file does not define the final output format by itself.
Use the matching template for output structure.

This file does not define global agent rules.
Those are defined in `CLAUDE.md`.

---

## Output File
- `docs/change_principles.md`

---

## Template Reference
Use:
- `build_plan/templates/change_principles.template.md`

Follow the template structure unless the current repository requires a small repository-specific adjustment.
Respect the placeholder legend at the top of the template.

Do not redesign the document shape unless clearly necessary.

---

## Role of `docs/change_principles.md`
`docs/change_principles.md` is a principles document, not a workflow manual.

It should help the reader answer:

- which global rules take precedence when making any change
- what must be read before modifying content
- how change scope should be controlled
- what the minimum validation expectations are
- when documentation or change records must be updated in sync
- which situations require approval or escalation

It provides stable, cross-module principles that should remain valid even as specific modules evolve.

It should not become:

- a per-module development workflow
- a task-type-specific SOP (new feature vs bug fix vs refactor)
- an onboarding or training document
- a detailed operational checklist
- a restatement of `CLAUDE.md`

The principles layer stays short and stable. Principles do not need to be rewritten when modules change.

---

## Required Inputs
To build `docs/change_principles.md`, inspect these sources first:

1. `CLAUDE.md`
2. `build_plan_overview.md`
3. existing maintained repository docs that describe modification policy, if any
4. repository-wide enforcement signals visible in the repo (CI config, pre-commit hooks, PR templates, `CODEOWNERS`, linters)
5. `docs/architecture.md` for module boundary references

Also inspect whether these files already exist:

- `docs/change_principles.md`
- `AGENTS.md` (if present, treat as peer to `CLAUDE.md` for Rule Precedence)
- `docs/changes/current_index.md`

If related files do not yet exist, describe their expected role only where standard to the build process. Do not invent their contents.

---

## What `docs/change_principles.md` Must Include
The built document should include these seven sections, in this order:

1. Purpose
2. Rule Precedence
3. Read Before Change
4. Scope Control
5. Validation Principles
6. Documentation Sync Principles
7. Escalation / Approval

Keep each section short. Bullet form is preferred over prose.

---

## Per-Section Guidance

### Section 1: Purpose
State what this document governs. State explicitly that it defines cross-module change principles, not workflows. Note that this document is meant to stay short and stable.

### Section 2: Rule Precedence
List the files that override this document, typically `CLAUDE.md` and `AGENTS.md` if present. Describe how conflicts with other docs (e.g. `docs/architecture.md`, `skills/`) are resolved.

### Section 3: Read Before Change
State what must be read before modifying repository content. Reference `docs/architecture.md` for module boundaries when changes cross modules. Reference `docs/changes/current_index.md` when the affected area has recent activity. Reference any relevant `skills/<name>/SKILL.md` when the task matches a known workflow.

### Section 4: Scope Control
State that changes should be limited to the task's direct scope. State that unrelated cleanup or refactors should be surfaced separately, not bundled silently. Define what counts as "broader" and requires separation.

### Section 5: Validation Principles
State the minimum validation expected for any change. If the repository has a primary test runner, CI pipeline, or linter, reference it. Describe what "validation" means when full test coverage is unavailable. State that unvalidated changes must be flagged explicitly, not silently submitted.

### Section 6: Documentation Sync Principles
State when a change requires updates to `docs/architecture.md`, `skills/`, or a new record under `docs/changes/`. State that missing documentation should be added or flagged, not silently skipped.

### Section 7: Escalation / Approval
List the types of change that require approval before execution. State what "approval" looks like in this repository (PR review, code owner sign-off, issue approval, etc.). Describe who or what system grants approval. State what to do when approval cannot be obtained promptly.

---

## Repository-Specific Adaptation Rules
`docs/change_principles.md` should follow the company-standard structure, but the content must be adapted to the actual repository.

Adapt these parts to the current repository:

- actual rule files present (`CLAUDE.md`, `AGENTS.md`, neither, or custom equivalents)
- actual validation mechanism (pytest, jest, CI gate, manual, etc.)
- actual approval mechanism (PR review, `CODEOWNERS`, Slack sign-off, etc.)
- actual documentation sync points the repository already uses
- module boundaries visible in `docs/architecture.md`

Do not paste a generic principles document without checking the real repository.

---

## Writing Rules
When writing `docs/change_principles.md`:

- write principles, not procedures
- keep each section short; bullets preferred over prose
- use repository paths exactly as they exist
- avoid listing task-type-specific steps (new feature vs bug fix vs refactor)
- avoid restating global behavior rules from `CLAUDE.md`
- avoid explaining the project's business context
- avoid declaring principles the repository does not actually enforce

This document should remain stable across changes to specific modules. If it needs frequent rewrites, it is probably mixing in workflow content that does not belong here.

---

## Evidence Rules
When deciding what to include, use evidence from:

1. actual enforcement signals in the repo (CI config, pre-commit hooks, PR templates, `CODEOWNERS`)
2. existing rule files (`CLAUDE.md`, `AGENTS.md`)
3. existing maintained docs that reference modification policy
4. existing change records if present

Do not invent approval or validation rules the repository does not enforce.

If evidence is weak, describe the principle in neutral, minimal terms and mark uncertainty.

---

## Unknown Handling
If a section's content cannot be grounded in repository evidence:

- state the principle at high level only
- use `Unknown`, `Needs confirmation`, or `Not yet documented` for specifics that cannot be verified
- do not invent a detailed workflow to fill the section

A legitimate principle may read: "The repository does not yet document this; follow project owner decision case-by-case." This is acceptable output for an early-stage repository.

---

## Update Rules
If `docs/change_principles.md` already exists:

- preserve correct stable sections
- update outdated references (old CI system names, obsolete approval channels, moved paths)
- avoid full rewrites unless the file is fundamentally inconsistent with current practice
- keep section order stable where possible

Prefer precise correction over stylistic rewriting.

---

## Completion Criteria
The `docs/change_principles.md` build is complete when:

- the file exists and follows the template structure
- all seven sections are present
- each section contains repository-grounded principles, not fabricated procedures
- unknowns are explicitly marked
- the document remains short enough to read end-to-end in one pass
- nothing in the document contradicts `CLAUDE.md` or other higher-priority control files

---

## Final Reminder
Build `docs/change_principles.md` as a principles document.

It should help an agent answer:

- what rules override this file
- what must be read before any change
- what bounds a change
- what validates a change
- when to sync other docs or change records
- when a change must be escalated

Do not use it as a workflow manual.
Do not use it as a per-module SOP.
Do not use it to explain the system's business logic.
