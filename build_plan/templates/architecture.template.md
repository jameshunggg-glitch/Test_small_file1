<!-- Template Legend (do not copy into output)
  [ROLE TEXT]         = fill in repository-specific content in place of the bracketed text
  [PATH or DIR NAME]  = replace the entire bracket with an actual repository path
  [INSTRUCTION ...]   = editorial direction for the agent; follow it, do NOT copy into the output
-->

# Architecture

## 1. Purpose
- [Briefly state what this repository is for.]
- [State that this document provides a high-level structure map of the repository.]

## 2. Repository Overview
- [Brief overview of the repository as a whole.]
- [Summarize the roles of the main top-level areas.]
- [Keep this section high-level.]

## 3. Root-Level Control Files
- `CLAUDE.md` — [global agent rules summary]
- `llms.txt` — [repository navigation summary]
- `README.md` — [human-oriented onboarding summary, if present]
- `build_plan_overview.md` — [documentation build process overview summary, if present]

## 4. Documentation and Build Planning Areas
- `docs/` — [repository documentation summary]
- `docs/changes/` — [change-tracking summary, if present]
- `build_plan/` — [documentation build spec summary, if present]
- `build_plan/templates/` — [documentation template summary, if present]

## 5. Main Implementation Areas
- `[main implementation directory]` — [brief role]
- `[main implementation directory]` — [brief role]
- `[main implementation directory]` — [brief role]

[Add or remove entries based on the actual repository.]

## 6. Skills and Task-Specific Guidance
- `skills/` — [task-specific workflow guidance summary, if present]
- `[skills/<name>/SKILL.md]` — [optional brief example summary if useful]

[Omit this section if no `skills/` area exists.]

## 7. Validation Areas
- `[test directory]` — [brief validation role]
- `[test directory]` — [brief validation role]

[Add or remove entries based on the actual repository.]

## 8. Support and Utility Areas
- `[support directory]` — [brief support role]
- `[support directory]` — [brief support role]

[Examples may include scripts, tooling, helpers, or other non-core support areas.]
[Omit this section if not needed.]

## 9. Source of Truth Guidance
- Implementation files are the main source of truth for behavior.
- Tests are the main source of truth for validation expectations when present.
- Documentation should describe structure and roles, but should not override implementation evidence.
- Archived records should be treated as historical context, not stronger than current implementation.

## 10. Notes and Limitations
- [Optional: note any areas that are incomplete, unclear, planned, or not yet documented.]
- [Use `Unknown`, `Needs confirmation`, or `Not yet documented` when needed.]