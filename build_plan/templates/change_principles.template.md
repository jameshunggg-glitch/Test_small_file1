<!-- Template Legend (do not copy into output)
  [ROLE TEXT]         = fill in repository-specific content in place of the bracketed text
  [PATH or DIR NAME]  = replace the entire bracket with an actual repository path
  [INSTRUCTION ...]   = editorial direction for the agent; follow it, do NOT copy into the output
-->

# Change Principles

## 1. Purpose
- [Briefly state what this document governs within the repository.]
- [State clearly: this document defines cross-module change principles, not per-module workflows or task-type SOPs.]
- [Note that this document is meant to stay short and stable.]

## 2. Rule Precedence
- [List the files that override this document, typically `CLAUDE.md` and `AGENTS.md` if present.]
- [Describe how to resolve conflicts between this document and other docs such as `docs/architecture.md` or files under `skills/`.]
- [State which document wins in edge cases; avoid ambiguity.]

## 3. Read Before Change
- [State what an agent or engineer must read before modifying repository content.]
- [Reference `docs/architecture.md` for module boundaries when a change touches multiple modules.]
- [Reference `docs/changes/current_index.md` when the change area has recent activity.]
- [Reference any relevant `skills/<name>/SKILL.md` when the task matches a known recurring workflow.]

## 4. Scope Control
- [State the principle that changes should be limited to the task's direct scope.]
- [State that unrelated cleanup, refactors, or renames must be surfaced separately, not bundled silently.]
- [Describe what category of change counts as "broader" in this repository and therefore requires separation.]

## 5. Validation Principles
- [State the minimum validation expected for any change.]
- [Reference the repository's primary validation mechanism if one exists, for example `[PATH to test runner or CI config]`.]
- [Describe what "validation" means when full test coverage is unavailable.]
- [State that unvalidated changes must be flagged explicitly, not silently submitted.]

## 6. Documentation Sync Principles
- [State when a change requires updates to `docs/architecture.md`.]
- [State when a change requires updates under `skills/`.]
- [State when a change requires a new record under `docs/changes/`.]
- [State that missing documentation should be added or flagged, not silently skipped.]

## 7. Escalation / Approval
- [List the types of change that require approval before execution.]
- [State what "approval" looks like in this repository's workflow: PR review, code owner sign-off, issue approval, etc.]
- [Describe who or what system grants approval.]
- [State what to do when approval cannot be obtained promptly.]
