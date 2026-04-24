# Architecture

## 1. Purpose
- This repository contains the Week 4 project: AI News Digest System, which searches for topic-based news, extracts article information, generates structured summaries, and saves results as Markdown files.
- This document provides a high-level structure map of the repository.

## 2. Repository Overview
- Single-codebase Python project. Core workflow lives under `app/`; reusable skill instructions live under `skills/`; tests live under `tests/`; generated Markdown digests live under `outputs/`.
- Project scope is fixed to Version 1; see `AGENTS.md` §Current Scope for included and excluded features.
- Keep the layout narrow: implementation, skills, tests, outputs. No broad framework scaffolding is expected.

## 3. Root-Level Control Files
- `CLAUDE.md` — global agent operating rules, distilled with SOP standard sections + team-specific rules.
- `llms.txt` — repository navigation index for agents.
- `AGENTS.md` — authoritative team rules (project scope, engineering principles, guardrails).
- `README.md` — present but currently empty; `Needs confirmation` whether human onboarding notes are planned here.
- `build_plan_overview.md` — installer SOP build-process overview (present during build; removed by Post-Build Cleanup).

## 4. Documentation and Build Planning Areas
- `docs/` — repository documentation root (`architecture.md`, `change_principles.md`, `changes/`).
- `docs/changes/` — curated change-tracking system with a current index, archive indexes, case folders under `cases/`, and local `_templates/` for ongoing recording.
- `build_plan/` — documentation build specs (present during build only; removed by Post-Build Cleanup).
- `build_plan/templates/` — build-time templates (present during build only; two of them — `change_case.template.md` and `current_index.template.md` — are preserved under `docs/changes/_templates/`).

## 5. Main Implementation Areas
- `app/` — core application code for the digest workflow.
  - `app/search.py` — search for topic-related news articles; returns structured candidate results.
  - `app/summarizer.py` — summarize extracted article text; returns summary and key points.
  - `app/writer.py` — save digest results as Markdown files.
  - `app/models.py` — shared data structures.
  - `app/main.py` — minimal entrypoint for running the workflow.
- Keep responsibilities separated per `AGENTS.md` §Expected Module Responsibilities. Do not merge unrelated logic into one module.

## 6. Skills and Task-Specific Guidance
- `skills/` — reusable skill instructions for recurring workflows.
  - `skills/topic_news_search/SKILL.md` — skill instructions for topic-based news search.
  - `skills/article_digest_writer/SKILL.md` — skill instructions for writing article digests.

## 7. Validation Areas
- `tests/` — test suite covering search, summarizer, writer, and entrypoint behavior.
  - `tests/test_search.py`, `tests/test_summarizer.py`, `tests/test_writer.py`, `tests/test_main.py`, `tests/test_scratch.py`.
- At minimum, tests are expected to validate search output structure, summarizer output structure, and Markdown file generation (`AGENTS.md` §Testing Expectations).

## 8. Support and Utility Areas
- `outputs/` — generated Markdown digest files. Listed in `.gitignore`; treated as workflow artifacts, not source.

## 9. Source of Truth Guidance
- Implementation files under `app/` are the main source of truth for behavior.
- Tests under `tests/` are the main source of truth for validation expectations.
- `AGENTS.md` is the authoritative source for team rules; this document should not override it.
- Documentation under `docs/` describes structure and roles, not implementation detail.

## 10. Notes and Limitations
- No dependency manifest (e.g. `requirements.txt`, `pyproject.toml`) is present at the repository root; the exact runtime dependency set is `Not yet documented`.
- No CI configuration is present at the repository root; automated validation gating is `Not yet documented`.
- `README.md` exists but is empty; the repository purpose is sourced from `AGENTS.md` §Project Overview for this document.
