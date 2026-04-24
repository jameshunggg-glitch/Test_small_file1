# Change Cases

This directory holds detailed per-change records. Each recorded change gets its own folder containing a `change.md`. The lightweight index in `docs/changes/current_index.md` is the first stop — open a case folder only after its index entry looks relevant.

## Folder Naming Convention

Format: `YYYYMMDD_caseNNNN_kebab-description`

- `YYYYMMDD` — date of the change (8 digits, no separator).
- `caseNNNN` — case number. Use the external tracker ID when the repository has one in use. Otherwise use a local sequential number starting at `case0001` and incrementing per change within this repository.
- `kebab-description` — lowercase ASCII letters, digits, and hyphens only (`[a-z0-9-]+`). No spaces, no underscores, no uppercase, no non-ASCII. Maximum 40 characters; truncate meaningfully rather than abbreviating cryptically.

Example: `20260420_case4834_land-crossing-fix`

## Uniqueness

The `caseNNNN` portion (and the full folder name) must be unique within this repository. If two changes share the same external tracker ID, disambiguate by appending a short suffix (e.g. `caseNNNN-a`, `caseNNNN-b`).

If the repository adopts an external tracker mid-stream, existing local-sequence case numbers remain unchanged; new cases from that point on use the tracker-assigned number. The two number spaces coexist — do not renumber history.

## Templates

Templates for ongoing use live in `docs/changes/_templates/`:

- `change_case.template.md` — shape for each per-case `change.md`.
- `current_index.template.md` — shape for `current_index.md` and monthly archive indexes.

Do not rename a case folder after it has been referenced by an index entry; the `detail_path` field would otherwise break.
