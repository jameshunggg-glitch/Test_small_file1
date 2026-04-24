# Change Principles

## 1. Purpose
- Defines cross-module change principles for this repository. Not a per-module workflow, not a task-type SOP.
- Meant to stay short and stable; update only when a principle itself changes.

## 2. Rule Precedence
Higher items win on conflict:

1. `CLAUDE.md` — SOP-level agent rules and entry point.
2. `AGENTS.md` — authoritative team rules, peer to `CLAUDE.md`. In case of conflict between `CLAUDE.md` and `AGENTS.md` on team rules, `AGENTS.md` wins.
3. This document (`docs/change_principles.md`).
4. `docs/architecture.md` — module boundaries and repository structure.
5. `skills/*/SKILL.md` — task-specific workflow guidance (authoritative for the workflow it covers).
6. Implementation files, tests, schemas — source of truth for behavior.

## 3. Read Before Change
Before modifying repository content, read:
- `CLAUDE.md` and `AGENTS.md` for scope and guardrails.
- `docs/architecture.md` when a change touches more than one module or crosses a module boundary in `app/`.
- `docs/changes/current_index.md` when the affected area may have recent activity; open the referenced `cases/<folder>/change.md` only if an index entry looks relevant.
- The relevant `skills/<name>/SKILL.md` when the task matches an existing skill (e.g. topic news search, article digest writing).

## 4. Scope Control
- Keep changes limited to the task's direct scope. Version 1 scope is fixed; do not expand without explicit request (`AGENTS.md` §Current Scope).
- Unrelated cleanup, refactors, or renames must be surfaced separately, not bundled silently.
- "Broader" changes in this repository include: adding new modules under `app/`, introducing new skills under `skills/`, restructuring the output format, or changing cross-module interfaces in `app/models.py`. These require separation from the triggering task.

## 5. Validation Principles
- Minimum validation for any code change: run the tests under `tests/` covering the affected module (`test_search.py`, `test_summarizer.py`, `test_writer.py`, `test_main.py`).
- Validation expectations per `AGENTS.md` §Testing Expectations: search output structure, summarizer output structure, Markdown file generation.
- No CI pipeline is currently documented at the repository root; validation is currently manual via `pytest`. `Needs confirmation` whether a CI gate exists.
- Unvalidated changes must be flagged explicitly in the change record and in the commit or PR description. Do not imply validation that was not performed.

## 6. Documentation Sync Principles
- Update `docs/architecture.md` when module boundaries, top-level directories, or the role of a major area changes.
- Update `skills/<name>/SKILL.md` when the recurring workflow it covers changes.
- Record a new case under `docs/changes/cases/<folder>/change.md` and add a matching entry to `docs/changes/current_index.md` for any meaningful change an agent should know about before editing adjacent code. Curated, not exhaustive — see `docs/changes/cases/README.md` for naming and scope.
- Missing documentation should be added or explicitly flagged (`TODO`, `Needs confirmation`), not silently skipped.

## 7. Escalation / Approval
- Changes that expand scope beyond Version 1 (`AGENTS.md` §Current Scope) require explicit owner approval before execution.
- Changes to `CLAUDE.md`, `AGENTS.md`, or this file require owner approval — these are rule-layer files.
- No formal code-review or `CODEOWNERS` mechanism is currently documented; approval mechanism is `Needs confirmation`.
- When approval cannot be obtained promptly, pause the change, record the blocker in `docs/changes/current_index.md` with `status: blocked`, and surface the issue to the repository owner.
