# build_plan_overview.md

## Purpose
This file is the master build entry for repository documentation setup.

Use this file to build the repository documentation system in the correct order.
Follow the build sequence defined here.
For each target file, read the corresponding file under `build_plan/`.
Then use the referenced template to create or update the final output.

Build route:
`build_plan_overview.md` → `build_*.md` → `*.template.*`

---

## Scope
This file defines:
- the documentation build order
- the target files to create or update
- the mapping between outputs, build specs, and templates
- initialization rules
- update rules
- completion expectations

This file does not define:
- global agent behavior rules
- detailed writing rules for each output file
- final output templates
- project architecture content
- change management content

For those, read the appropriate files.

---

## Installer Positioning
This file, together with `build_plan/` (which contains `installer_CLAUDE.md`, the build specs, and `templates/`), forms an installer package.
The package is dropped into a target repository so that an agent can build a standardized documentation tree.

Package contents fall into two categories:

1. Control files (`build_plan_overview.md` and `build_plan/installer_CLAUDE.md`):
   - The installer's `installer_CLAUDE.md` serves as the **build-time driver only** — it is the rules file the agent follows while executing this SOP. It is not the final `CLAUDE.md` that will govern the target repository afterwards.
   - The final target-level `CLAUDE.md` is produced during the build by `build_plan/build_CLAUDE_md.md` as a **distilled** file that merges SOP standard sections with the target's existing rule material. See that build spec for scenario handling (no existing file / only AGENTS.md / existing CLAUDE.md) and the Scenario (c) backup + diff + owner-confirm safety flow.
   - If the target repository already contains `build_plan_overview.md`, do not overwrite. Surface the conflict and ask the repository owner how to proceed.

2. Build specs and templates (`build_plan/`, `build_plan/templates/`):
   - If the target repository has no `build_plan/`, install the package version.
   - If the target repository already has a `build_plan/` of any kind (including what appears to be an older version of the same package), do not overwrite and do not merge. Stop and ask the repository owner how to proceed.

General rule for control-package conflicts: stop and ask. Do not default to replace. Do not default to merge. This applies to `build_plan_overview.md`, `build_plan/`, `build_plan/templates/`, and any future control-layer file added to the package. The distilled `CLAUDE.md` written at target root during build is handled specifically by `build_plan/build_CLAUDE_md.md` and is exempt from this general rule.

Build outputs (`llms.txt`, `docs/architecture.md`, and so on) are governed by the Update Rules below, not by installer policy.

Do not assume the package is the source of truth for repository content.
It is the source of truth for structure and build process only.

### Target Root Identification
The **target repository root** is defined as the directory containing `build_plan_overview.md` after the installer package has been dropped in.

Before starting any build step, the agent must confirm that its current working directory is the target root. All paths referenced throughout this build process (`docs/`, `build_plan/`, `llms.txt`, etc.) are resolved relative to that directory. Running the build from a parent or sibling directory will produce files at the wrong location.

If the agent cannot unambiguously identify the target root (e.g. `build_plan_overview.md` is found in multiple candidate directories), stop and ask the repository owner to confirm.

### Target Sanity Check
Before creating any output files, perform a lightweight sanity check on the target root:

- does it contain any implementation files (code, scripts, notebooks), test directories, a README, or a package/dependency manifest?

If none of these exist, the directory may not be a software project at all — the installer may have been dropped in the wrong place (home directory, an empty scratch folder, etc.). Warn the repository owner and require explicit confirmation before proceeding with the build.

This check is advisory. If the owner confirms, proceed normally and mark any Unknown fields with `Needs confirmation`.

### Post-Build Cleanup
Once the build completes (all target outputs produced and verified), the installer's own control files must be removed from the target root so that they do not compete with the distilled outputs. Delete:

- `build_plan_overview.md`
- `build_plan/` (the whole directory, including `build_plan/templates/`)

The installer's build-time driver at `build_plan/installer_CLAUDE.md` is removed as part of the `build_plan/` deletion above. Perform a sanity check that only one `CLAUDE.md` remains at target root (the distilled one).

Do not delete: the distilled `CLAUDE.md`, `AGENTS.md`, `llms.txt`, `docs/`, `CLAUDE.md.pre_install.bak`, or anything outside the installer package.

Cleanup completion is part of the overall Completion Criteria. An install with outputs produced but installer files still present at target root is not considered complete.

---

## Required First Reads
Before starting the build process, read:

1. `build_plan/installer_CLAUDE.md` (the installer's build-time driver)
2. `build_plan_overview.md`
3. `build_plan/build_CLAUDE_md.md` (because the distilled `CLAUDE.md` is the first target built and affects everything downstream)

Then, for each target you plan to build, also read its matching `build_*.md` under `build_plan/` before starting that target.

After that, follow this file step by step.
Do not skip directly to templates.
Do not generate final files without first reading the matching build spec.

---

## Build Targets
The standard documentation outputs for this repository are:

- `CLAUDE.md` (distilled, written at target root during build)
- `llms.txt`
- `docs/architecture.md`
- `docs/change_principles.md`
- `docs/changes/current_index.md`
- `docs/changes/cases/README.md`
- `docs/changes/cases/.../change.md` structure and template pattern

These are the final output files.
Do not treat files under `build_plan/` or `build_plan/templates/` as final project documentation. Those are removed during Post-Build Cleanup.

---

## File Tree Setup
Before building any content, ensure the repository has the expected file tree skeleton.
Content is built on top of this skeleton; if paths are missing, later build steps will fail or produce inconsistent references.

Expected skeleton (during build — before Post-Build Cleanup removes the installer files):

```
/project-root
├── build_plan_overview.md         (removed by Post-Build Cleanup)
├── build_plan/                    (removed by Post-Build Cleanup)
│   ├── installer_CLAUDE.md        (the build-time driver; read first during build)
│   ├── build_CLAUDE_md.md
│   ├── build_llms_txt.md
│   ├── build_architecture_md.md
│   ├── build_change_principles_md.md
│   ├── build_changes_md.md
│   └── templates/
│       ├── CLAUDE.template.md
│       ├── llms.template.txt
│       ├── architecture.template.md
│       ├── change_principles.template.md
│       ├── change_case.template.md
│       └── current_index.template.md
│
├── CLAUDE.md                      (distilled; produced by Stage 2; see build_plan/build_CLAUDE_md.md for Scenario (a)/(b)/(c) handling)
├── llms.txt
└── docs/
    ├── architecture.md
    ├── change_principles.md
    └── changes/
        ├── current_index.md
        ├── _templates/
        │   ├── change_case.template.md    (copied from build_plan/templates/ in Stage 6)
        │   └── current_index.template.md  (copied from build_plan/templates/ in Stage 6)
        └── cases/
            └── README.md          (seed file documenting naming convention)
```

Final target root after Post-Build Cleanup keeps the following. Pre-existing project files (e.g. `src/`, `tests/`, `scripts/`) are left untouched throughout the install and are not shown here.

```
/project-root
├── CLAUDE.md                      (distilled)
├── CLAUDE.md.pre_install.bak      (only if Scenario c was triggered)
├── AGENTS.md                      (only if it pre-existed; untouched by install)
├── README.md                      (only if it pre-existed; untouched by install)
├── llms.txt
└── docs/
    ├── architecture.md
    ├── change_principles.md
    └── changes/
        ├── current_index.md
        ├── _templates/
        │   ├── change_case.template.md
        │   └── current_index.template.md
        └── cases/
            └── README.md
```

Note that `build_plan_overview.md` and `build_plan/` are absent — they are removed by Post-Build Cleanup per §Post-Build Cleanup.

Setup rules:

1. Install or verify the package files first (see Installer Positioning above).
2. For each path in the expected skeleton, verify whether it already exists.
3. If a path is missing, create it.
   - Folders: create empty.
   - Files: create as empty placeholders unless the package already supplies a seed version (such as `CLAUDE.md`, `build_plan_overview.md`, or the templates).
4. If a path exists with a name that resembles but does not match an expected skeleton path (for example `CLAUDE.md.md`, or `Architecture.md` where `architecture.template.md` is expected), do not rename automatically. Similarity is subjective; such names may be intentional user choices.
   - Surface the apparent mismatch to the repository owner. Show both the existing path and the expected path.
   - Rename only under explicit owner instruction.
   - If no instruction is given, leave the existing file in place and create the expected path as an empty placeholder only if the expected path is still missing.
5. Do not delete existing files. Do not flatten or reorganize existing directories outside this list.
6. If the repository already contains additional directories (for example `src/`, `tests/`, `scripts/`, or sample subprojects), leave them untouched. They are described later by `docs/architecture.md`, not modified here.
7. Do not edit the content of existing target files unless explicitly required by the build target mapping (i.e. the distilled `CLAUDE.md` Scenario c flow with owner-confirmed diff). All other pre-existing files at target root or elsewhere — including user-authored source files, notes, goal docs, and progress logs — are read-only during install. Apparent defects such as filename typos or stale content are not silently corrected; surface them to the owner at most, never mutate them.

Skeleton setup must complete before content building begins.

---

## Initialization Rules
If this is the first documentation build for the repository:

1. Ensure the file tree skeleton exists (see File Tree Setup above).
2. Create any further missing required folders discovered during build (for example specific subfolders under `docs/changes/cases/`).
3. Then build outputs in the order defined below.

Use minimal useful first versions.
If repository evidence is limited, create a correct skeleton with explicit unknown markers.

---

## Update Rules
If target files already exist:

- update existing files instead of rebuilding everything from scratch
- preserve sections that are already correct
- correct outdated or missing parts
- keep stable naming and structure where possible
- avoid unnecessary full rewrites

Only replace an entire file when the existing file is clearly unusable or fundamentally inconsistent with the required structure.

When updating or appending entries in `docs/changes/current_index.md`, check whether rotation is due per `build_plan/build_changes_md.md` §Rotation Rule, and move entries older than roughly one month into the appropriate `docs/changes/archive_index_YYYY_MM.md`.

---

## Build Order
Build outputs in this order. `llms.txt` is intentionally split into a first-pass and a second-pass because it references files that have not been created when it is first touched; see Stages below.

**Before Stage 0 (recommended).** Commit the installer package to git as a pre-build snapshot: `git add build_plan_overview.md build_plan/ && git commit -m 'snapshot: installer package before build'`. Stage 8 Post-Build Cleanup deletes these files; without a snapshot, restoration is not trivial.

0. Confirm or create the required file tree skeleton (see File Tree Setup). Run the Target Sanity Check.
1. Confirm or create any task-specific subfolders not covered by the skeleton.
2. Build `CLAUDE.md` (distilled) — see `build_plan/build_CLAUDE_md.md`. In Scenario (c) wait for owner confirmation before proceeding past this step.
3. Build `llms.txt` **first-pass**: produce a skeleton that references only files already known to exist by path — `CLAUDE.md`, `AGENTS.md` (if present), and the planned `docs/` layout. Task routes and file role summaries may use short placeholders that will be filled in during Stage 7.
4. Build `docs/architecture.md`
5. Build `docs/change_principles.md`
6. Build `docs/changes/current_index.md` (empty skeleton is acceptable on first install; see `build_plan/build_changes_md.md` §Completion Criteria) and create `docs/changes/cases/README.md`. Prepare the standard pattern for `docs/changes/cases/<case-folder>/change.md` (no case folders are created on first install unless a real change is being recorded). Additionally, copy `build_plan/templates/change_case.template.md` and `build_plan/templates/current_index.template.md` to `docs/changes/_templates/` so ongoing change recording has local templates available after Post-Build Cleanup (see `build_plan/build_changes_md.md` §Template Preservation for Ongoing Use).
7. Build `llms.txt` **second-pass**: revisit `llms.txt` and fill in the now-existing references — task routes, file role summaries, and any references that required the now-built docs. This closes the architecture ↔ llms.txt cross-reference gap.
8. **Pause for owner review.** Before executing Post-Build Cleanup, surface the produced `docs/` layout, `llms.txt`, and the distilled `CLAUDE.md` to the repository owner and wait for explicit confirmation. On owner approval, execute Post-Build Cleanup: remove `build_plan_overview.md` and the entire `build_plan/` directory from target root per §Installer Positioning. The two ongoing-use templates copied into `docs/changes/_templates/` in Stage 6 survive this cleanup.

Do not change this order unless a repository-specific constraint makes it impossible.

---

## Build Route Mapping

### 1. Build `CLAUDE.md` (distilled)
- Read: `build_plan/build_CLAUDE_md.md`
- Use template: `build_plan/templates/CLAUDE.template.md`
- Output: `CLAUDE.md` at target root

### 2. Build `llms.txt`
- Read: `build_plan/build_llms_txt.md`
- Use template: `build_plan/templates/llms.template.txt`
- Output: `llms.txt`

### 3. Build `docs/architecture.md`
- Read: `build_plan/build_architecture_md.md`
- Use template: `build_plan/templates/architecture.template.md`
- Output: `docs/architecture.md`

### 4. Build `docs/change_principles.md`
- Read: `build_plan/build_change_principles_md.md`
- Use template: `build_plan/templates/change_principles.template.md`
- Output: `docs/change_principles.md`

### 5. Build `docs/changes/current_index.md` and case pattern
- Read: `build_plan/build_changes_md.md`
- Use templates:
  - `build_plan/templates/current_index.template.md` (for `current_index.md` and archive indexes)
  - `build_plan/templates/change_case.template.md` (for each per-case `change.md`)
- Output:
  - `docs/changes/current_index.md`
  - `docs/changes/cases/README.md`
  - `docs/changes/cases/.../change.md` (only when recording a real change)

For each output, read the build spec before using the template.
Templates define output shape.
Build specs define how to gather and write the content.

---

## Evidence Rules
When building documentation, prefer evidence from:

1. repository structure
2. existing maintained project docs
3. implementation files
4. tests
5. existing change records

Do not invent repository-specific facts.
Do not present assumptions as confirmed project truth.

If evidence is weak, write a minimal accurate draft and mark uncertainty clearly.

Special rule for repository purpose:
If the repository does not document its own purpose anywhere (no `README.md`, no overview doc, no purpose statement in any maintained doc), do not invent one.
Fill the purpose field with `Needs confirmation` and note that the repository owner should provide a one-line purpose.
A blocked purpose field is acceptable. A fabricated purpose is not.

---

## Unknown Handling
If required information is missing or cannot be verified:

- use `Unknown`
- use `Needs confirmation`
- use `TODO`
- use `Not yet documented`

Do not fill missing content with guesses.
Do not force completeness when repository evidence does not support it.

A correct partial file is better than a complete but fabricated file.

---

## Working Rules During Build
During this build process:

- follow `CLAUDE.md` for global behavior boundaries
- follow each `build_*.md` for target-specific writing rules
- use the matching template for output structure
- create only the required outputs
- do not create extra documentation outside the defined targets unless explicitly requested
- keep first-pass outputs concise, structured, and easy to update

### Output Language Policy
Default output language is **English**, matching the templates. This keeps outputs consistent across repositories and teams.

The repository owner may override by stating a specific language in the build prompt (e.g. "build in Traditional Chinese"). When overridden, translate placeholder legends and section headings accordingly, but keep frontmatter keys (`sop_version`, `generated_at`, etc.) and template reference paths in their original form.

Do not infer the language from the target's existing docs or code comments. Only override on explicit owner instruction.

---

## Design Principle (v1.0.0)
SOP v1.0.0 prefers uniform rules over context-dependent judgment. When a rule would require an agent to decide what counts as "authoritative", "important enough", or "worth mentioning", the rule is redesigned to remove the judgment call — either by including all instances or by excluding all of them.

Add rules reactively when evidence shows gaps, not proactively to cover hypothetical cases. A future SOP version can reintroduce nuance once real-use feedback identifies where it is needed. The primary v1.0.0 goal is agent predictability: a build should produce the same shape regardless of which agent runs it.

---

## Completion Criteria
This build process is complete when:

- the file tree skeleton exists
- required folders exist
- required target files exist (`CLAUDE.md`, `llms.txt`, `docs/architecture.md`, `docs/change_principles.md`, `docs/changes/current_index.md`, `docs/changes/cases/README.md`)
- each target follows the correct template structure
- each target contains repository-grounded content where evidence is available
- unknowns are explicitly marked where evidence is missing
- no fabricated project-specific content has been added
- build outputs do not contradict higher-priority control files (the distilled `CLAUDE.md`, and the corresponding `build_*.md` that produced each output),
  e.g. `llms.txt` must not point to files or routes not defined by the current build plan, and `docs/architecture.md` must not describe repository areas that cannot be verified from repository evidence.
- **Post-Build Cleanup has been executed**: `build_plan_overview.md` and `build_plan/` no longer exist at target root, and exactly one `CLAUDE.md` (the distilled one) remains there.

---

## Final Reminder
This file controls build order and routing.
Each `build_*.md` controls how one target should be built.
Each template controls the final output format.

Follow the process in order.
Build from evidence.
Prefer correct structure and grounded content over speculative completeness.

---

## Future Roadmap (v2, not part of v1 scope)
The following are known extensions that are intentionally out of scope for v1. They are listed here so that v1 agents do not treat them as gaps, and so that future SOP revisions know where to extend.

- **Automation scripts under `/scripts/`** — a draft earlier version contemplated `build_llms_txt.py` and `validate_docs_links.py` to automate or validate the build. v1 is executed manually by an agent; script-based automation is deferred until multiple real targets have been installed and pain points are evidence-based.
- **SOP upgrade / re-install flow** — v1 rejects any pre-existing `build_plan/` (stop and ask). A future version will compare the `sop_version` recorded in the target's distilled `CLAUDE.md` frontmatter against the incoming installer's version, and define a selective-update flow for changed sections only.
- **Additional domain documents** — `business_context.md`, `data_contracts.md`, `integration.md`, `security.md`, `deployment.md` are not part of the v1 basis. Projects that need them may add them later without touching the v1 skeleton.
- **Multi-subproject build** — v1 treats one `project-root` at a time. Repositories composed of multiple independent subprojects may in the future run the build per subproject; the Independent Subproject Rules in `build_plan/build_architecture_md.md` and `build_plan/build_llms_txt.md` already anticipate the shape.
