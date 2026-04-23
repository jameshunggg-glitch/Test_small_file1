# build_plan/build_CLAUDE_md.md

## Purpose
This file defines how to build `CLAUDE.md` for a target repository during installer execution.

`CLAUDE.md` is the root-level control file that tells every future agent how to operate in this repository: which files to read first, what change-time rules apply, and which precedence ordering governs conflicts.

The installer always produces a **distilled** `CLAUDE.md`, regardless of whether the target already has a `CLAUDE.md` or `AGENTS.md`. A distilled `CLAUDE.md` combines:

1. the SOP's fixed standard sections (reading order, change-time rules, source-of-truth priority), and
2. a Target-Specific section distilled from whatever rule material the target already had.

This guarantees that every project built with this SOP shares the same change-time discipline, while still preserving the target's own team rules.

This file does not define the final output format by itself.
Use the matching template for output structure.

This file does not define global agent rules.
Those are defined in `build_plan/installer_CLAUDE.md`.

---

## Output File
- `CLAUDE.md` (at the target repository root)

---

## Template Reference
Use:
- `build_plan/templates/CLAUDE.template.md`

Follow the template structure. Respect the placeholder legend at the top of the template.
Do not redesign the document shape unless clearly necessary.

---

## Role of the distilled `CLAUDE.md`
The distilled `CLAUDE.md` is the agent's first-stop control file. It should help any future agent answer:

- what global rules take precedence in this repository
- which files must be read before acting
- what must additionally be read before modifying repository content
- which document wins in case of conflict
- which sources are authoritative for behavior, validation, and history

It should not become:

- a detailed workflow manual (that belongs in `docs/change_principles.md`)
- an architecture reference (that belongs in `docs/architecture.md`)
- a task-type SOP
- an onboarding or training document

The distilled `CLAUDE.md` is intentionally short and stable.

---

## Required Inputs
Before building the distilled `CLAUDE.md`, inspect:

1. `build_plan/installer_CLAUDE.md` (it provides the SOP standard sections to be copied in verbatim)
2. `build_plan_overview.md` (for build-process wording and references)
3. target repository root structure
4. target `CLAUDE.md` if it already exists
5. target `AGENTS.md` if it already exists
6. any other maintained rule file at the target root (e.g. `CONTRIBUTING.md` with authoritative rules)

If none of 4/5/6 exists, the Target-Specific section will be a placeholder marked `Needs confirmation`.

---

## Pre-Build Detection
Before producing any output, detect the target's current rule state:

- **Scenario (a)** — no `CLAUDE.md`, no `AGENTS.md` at target root
- **Scenario (b)** — `AGENTS.md` exists, no `CLAUDE.md`
- **Scenario (c)** — `CLAUDE.md` exists (regardless of whether `AGENTS.md` also exists)

The three scenarios share the same build output shape, but differ in how the Target-Specific section is populated and how the overwrite is handled.

---

## Distillation Rules

### Standard Sections (fixed, always copied verbatim)
The following sections come from `build_plan/installer_CLAUDE.md`. They are copied into the output without paraphrasing, so that every target built with this SOP carries the same change-time discipline:

- Core Principles
- Required Reading Order
- Mandatory Rule for Change Tasks
- General Working Norms
- Documentation Behavior
- Change Scope Rules
- File Creation Rules
- Change Recording Awareness
- Source of Truth Priority
- Validation Rules
- Behavior Boundaries
- Style Expectations
- When Generating New Documentation
- When Updating Existing Documentation
- Escalation Cases
- Final Expectation

Do not rewrite these for stylistic reasons. Copy verbatim.

### Target-Specific Section (distilled per scenario)
The Target-Specific section captures rules that are unique to the target team or project.

- **Scenario (a)** — No source material. Insert placeholder headings marked `Needs confirmation`, covering at minimum: team conventions, domain constraints, forbidden actions, any project-specific review or approval norms.
- **Scenario (b)** — Distill from `AGENTS.md`. Preserve the original `AGENTS.md` at the target root unchanged; it remains the authoritative peer. In the distilled `CLAUDE.md`, capture only the *rules* content from `AGENTS.md`, not the full text, and include a cross-reference line at the top: `See AGENTS.md for the authoritative team rules; this section is a navigation summary.`
- **Scenario (c)** — Distill from the target's existing `CLAUDE.md`. Capture all rules that are clearly team-specific or project-specific (not generic SOP restatements). If `AGENTS.md` also exists, treat it as in scenario (b) and add the cross-reference line.

Distillation rule: preserve meaning, not wording. Condense long prose to rule-form bullets. Drop generic statements that duplicate the SOP Standard Sections. Mark anything ambiguous with `Needs confirmation` rather than guessing.

### Rule Precedence Section
The distilled `CLAUDE.md` must include an explicit Rule Precedence section listing:

1. `CLAUDE.md` (this file) — agent entry point and SOP-level rules
2. `AGENTS.md` (if present) — authoritative team rules, peer to this file
3. `docs/change_principles.md` — cross-module change principles
4. `docs/architecture.md` — module boundaries and repository structure
5. implementation files / tests / schemas — source of truth for behavior

When `AGENTS.md` is present, state clearly: `In case of conflict between this file and AGENTS.md on team rules, AGENTS.md wins.`

---

## Overwrite Safety Rules

### Scenario (a) — No existing CLAUDE.md
- Write the distilled file directly to target root.
- No backup needed.

### Scenario (b) — Only AGENTS.md exists
- Write the distilled file directly to target root as `CLAUDE.md`.
- Do not modify `AGENTS.md`.
- No backup needed for `CLAUDE.md` (none existed).

### Scenario (c) — Target already has CLAUDE.md
Mandatory safety flow:

1. Copy the existing file to `CLAUDE.md.pre_install.bak` at target root.
2. Produce the distilled file in memory or to a temp path; do not overwrite yet.
3. Show the repository owner a diff between the original and the distilled version.
4. Wait for explicit owner confirmation.
5. Only after confirmation, overwrite `CLAUDE.md` with the distilled content.
6. Leave `CLAUDE.md.pre_install.bak` in place; the owner can delete it later when satisfied.

If the owner rejects the diff or does not confirm, do not overwrite. Keep the original `CLAUDE.md` intact, surface the blocker, and stop the build process at this step until the owner decides how to proceed.

---

## Post-Install Cleanup
After the distilled `CLAUDE.md` is successfully written and the rest of the build has completed, the installer's own control files must be removed from the target root so that they do not compete with the distilled outputs:

- delete `build_plan_overview.md` at target root
- delete the `build_plan/` directory (including `build_plan/installer_CLAUDE.md` and `build_plan/templates/`)

After deletion, sanity check that only one `CLAUDE.md` remains at target root (the distilled one).

Do not delete:
- the distilled `CLAUDE.md`
- `AGENTS.md`
- `CLAUDE.md.pre_install.bak` (owner may inspect or remove it manually)
- any `docs/` outputs
- `llms.txt`
- anything not part of the installer package

This cleanup is part of the build's completion criteria, not a separate optional step.

---

## Writing Rules
When writing the distilled `CLAUDE.md`:

- copy the Standard Sections verbatim from `build_plan/installer_CLAUDE.md`
- keep the Target-Specific section short; bullets over prose
- use repository paths exactly as they exist
- avoid restating SOP rules inside the Target-Specific section
- avoid inventing team-specific rules that are not evidenced by source material
- avoid business-context essays

Always record the `sop_version` and `generated_at` values in the output's frontmatter. These allow future re-installs to detect whether an upgrade is due.

---

## Evidence Rules
When populating the Target-Specific section, use evidence from:

1. the target's existing `CLAUDE.md` (scenario c)
2. the target's `AGENTS.md` (scenarios b and c)
3. any other explicitly-authoritative rule file at target root
4. repository-wide enforcement signals visible in the repo (CI config, pre-commit hooks, `CODEOWNERS`, linters) — but treat these as hints, not rules, unless they are referenced by an existing rule file

Do not infer rules from code style alone.
Do not invent approval or escalation rules that the repository does not enforce.

---

## Unknown Handling
If source material is thin or ambiguous:

- keep the Target-Specific section short
- use `Unknown`, `Needs confirmation`, or `Not yet documented` for specifics
- a legitimate output for a new repository is a Target-Specific section that mostly says "Needs confirmation; the repository owner should document team conventions here."

Do not fabricate team rules.

---

## Update Rules
If `CLAUDE.md` already exists at target root when the installer is re-run:

- The installer's default behavior on pre-existing `CLAUDE.md` is governed by `build_plan_overview.md` §Installer Positioning. In the current v1 this means: for a re-install where the target `CLAUDE.md` was produced by a previous SOP run (detectable via `sop_version` frontmatter), stop and ask the owner whether to upgrade.
- Upgrade mechanics (version comparison, selective section refresh) are not defined in v1 and belong to the Future Roadmap.

Do not silently overwrite a `CLAUDE.md` produced by a previous SOP run.

---

## Completion Criteria
The `CLAUDE.md` build is complete when:

- the file exists at target root
- it follows the template structure including frontmatter
- the Standard Sections are present and copied verbatim from `build_plan/installer_CLAUDE.md`
- the Target-Specific section is populated per the applicable scenario, with unknowns clearly marked
- the Rule Precedence section is explicit
- `sop_version` and `generated_at` are filled
- scenario (c) safety flow (backup + diff + confirm) was honored if applicable
- post-install cleanup of installer control files has been executed (or is queued as the final build step)

---

## Final Reminder
Build the distilled `CLAUDE.md` as the single authoritative entry point for agent behavior in the target repository.

It should help a future agent answer:
- what must I read first
- what additional rules apply when I change anything
- who wins in case of conflict
- where do I verify behavior

Do not use it as a workflow manual.
Do not use it as an architecture reference.
Do not embed team-specific rules that cannot be evidenced.
