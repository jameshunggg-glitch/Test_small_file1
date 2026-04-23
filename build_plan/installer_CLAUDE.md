# CLAUDE.md

## Purpose
This file defines the global operating rules for AI agents working in this repository.
It sets behavior boundaries, working norms, and high-level principles.
It does not explain system details, module internals, or project-specific architecture.

Unless a more specific local instruction file explicitly overrides part of it, this file applies across the repository.

---

## What This File Is For
This file defines:
- repository-wide agent behavior
- general writing and change boundaries
- documentation and modification norms
- source-of-truth priorities
- escalation conditions

This file does not define:
- system architecture details
- module-by-module design
- task-specific workflows
- change-record formats
- detailed reading maps

For those, read the appropriate repository documents.

---

## Core Principles
1. Read before writing.
2. Follow existing structure before inventing new structure.
3. Prefer small, scoped, evidence-based changes.
4. Do not fabricate missing details.
5. Keep outputs clear, maintainable, and easy to verify.
6. Treat implementation evidence as stronger than prose.
7. Mark uncertainty explicitly instead of guessing.
8. Preserve repository consistency unless change is required.
9. Do not expand task scope without clear reason.
10. When in doubt, choose accuracy over fluency.

---

## Required Reading Order
When starting work in this repository, read in this order:

1. `CLAUDE.md`
2. `llms.txt`
3. relevant repository docs for the task
4. relevant implementation files
5. relevant tests
6. relevant change records when the task involves existing behavior, recent changes, bugs, or ongoing work

Do not jump directly into broad edits before building minimum necessary context.

---

## Mandatory Rule for Change Tasks
If the task requires modifying repository content, the agent must read:
- `docs/change_principles.md`

This includes tasks such as:
- editing code
- editing docs
- creating files
- deleting files
- restructuring content
- updating repository records

Do not make repository changes before reading that file.

---

## General Working Norms
The agent should:
- understand the relevant area before changing it
- stay within the task scope
- preserve useful existing structure
- prefer minimal correct changes over broad rewrites
- keep related outputs internally consistent
- leave explicit placeholders when information is missing
- avoid assumptions not supported by repository evidence

Useful placeholders include:
- `TODO`
- `Unknown`
- `Needs confirmation`
- `Not yet documented`

---

## Documentation Behavior
When writing documentation:
- prefer concise, structured, factual writing
- use stable headings and predictable sections
- capture high-value information, not line-by-line code restatements
- keep docs easy to scan and easy to update
- avoid persuasive or explanatory essays unless explicitly requested
- avoid copying implementation details that are better read from code

Good documentation usually focuses on:
- purpose
- boundaries
- relationships
- expectations
- constraints
- known limitations
- validation notes

Documentation should not pretend certainty where certainty does not exist.

---

## Change Scope Rules
When making changes:
- modify only what is necessary for the task
- do not perform unrelated cleanup or refactors
- do not rename or reorganize files unless required
- do not introduce new conventions without clear need
- preserve existing naming and placement patterns where possible
- separate required change from optional improvement

If you identify a broader improvement that is not required for the current task, surface it separately instead of silently applying it.

---

## File Creation Rules
When creating new files:
- follow the repository's existing structure and conventions
- use existing templates or patterns when available
- keep first versions minimal but useful
- prefer a clean skeleton over speculative completeness
- create only files required by the task or repository standard

Do not create extra files just because they might be useful.

---

## Change Recording Awareness
When a task makes meaningful repository changes, check whether the repository expects change-tracking updates.
If the repository uses change records, keep those records aligned with the actual modification.
Do not create fake history.
Do not claim a change was recorded if it was not recorded.

---

## Source of Truth Priority
When determining what is true, use this priority:

1. executable code
2. tests
3. schemas, interfaces, and configs
4. current maintained docs
5. archived records

If sources conflict, prefer stronger implementation evidence unless the task is explicitly about future design or proposal writing.

---

## Validation Rules
Do not claim validation was performed unless it was actually performed.
Do not claim tests passed unless they were actually run and passed.
Do not imply completeness without evidence.

When validation is incomplete, say so clearly.
When repository evidence is partial, keep the output partial rather than invented.

---

## Behavior Boundaries
The agent must not:
- invent business rules without evidence
- invent architecture intent without evidence
- present guesses as facts
- rewrite unrelated material only for style consistency
- perform broad refactors outside task scope
- create process overhead not required by the repository
- replace precise facts with vague summary when precision is available
- hide uncertainty behind confident wording

---

## Style Expectations
Default output style should be:
- concise
- neutral
- structured
- repository-specific
- explicit about uncertainty
- easy to review in diffs

Avoid:
- marketing language
- memo-style persuasion
- unnecessary repetition
- inflated wording
- generic statements with low operational value

---

## When Generating New Documentation
If asked to generate documentation:
1. inspect the repository first
2. identify what already exists
3. reuse existing patterns where possible
4. generate only what is required
5. ground content in observable repository evidence
6. mark unknowns clearly instead of guessing

Do not treat missing information as permission to fabricate a complete document.

---

## When Updating Existing Documentation
If asked to revise existing docs:
1. preserve correct stable sections
2. update only outdated, incorrect, or missing parts
3. avoid full rewrites unless the document is clearly unusable
4. keep naming, ordering, and cross-links stable where possible

Prefer precise correction over unnecessary rewriting.

---

## Escalation Cases
Pause and clearly surface the issue instead of guessing when:
- documented structure and actual structure strongly conflict
- the task requires broad interpretation with weak evidence
- multiple sources disagree and no stronger evidence is available
- the requested output conflicts with repository conventions
- the task implies architectural or business intent not documented anywhere

In these cases, prefer a minimal accurate draft with clearly marked unknowns.

---

## Final Expectation
Good agent work in this repository is:
- accurate
- scoped
- evidence-based
- easy for humans to review
- easy for future agents to extend

When unsure, choose:
- clarity over volume
- evidence over assumption
- precision over polish
- minimal correctness over broad speculation