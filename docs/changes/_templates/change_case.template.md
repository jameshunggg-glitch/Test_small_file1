<!-- Template Legend (do not copy into output)
  [ROLE TEXT]         = fill in repository-specific content in place of the bracketed text
  [PATH or DIR NAME]  = replace the entire bracket with an actual repository path
  [INSTRUCTION ...]   = editorial direction for the agent; follow it, do NOT copy into the output
-->

# [Case Title]
[INSTRUCTION: Use a short descriptive title, typically matching the `kebab-description` portion of the case folder name. Do not embed the case number or the date in the title; those live in the index entry.]

## 1. Summary
- [Write a one-sentence summary of what this change did.]

## 2. Background
- [Describe the problem, question, or trigger that led to this change.]
- [Reference related case numbers, issue IDs, or PRs when applicable.]
- [Do not restate general project context that belongs in `docs/architecture.md`.]

## 3. Changes Made
- [List the actual modifications, grouped by file or area.]
- [Keep descriptions short; reference code paths using `[PATH to file]` rather than pasting long code blocks.]
- [If a modification is already obvious from a linked commit or PR, summarize it rather than duplicating the diff.]

## 4. Affected Areas
- [List the modules, directories, or files touched.]
- [Flag cross-module effects if any.]
- [Use exact repository paths.]

## 5. Validation
- [Describe how the change was validated: tests run, behavior checked, manual verification performed.]
- [Reference test names or commands, not full test output.]
- [If validation is incomplete, state explicitly what was not verified.]

## 6. Follow-up
- [List any remaining TODOs, known limitations, or deferred work.]
- [Note if further cases are expected to depend on or extend this one.]
- [Use `None` if nothing is deferred; do not leave this section blank.]
