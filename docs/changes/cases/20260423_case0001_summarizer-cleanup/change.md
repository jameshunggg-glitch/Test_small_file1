# summarizer-cleanup

## 1. Summary
- Strengthen HTML-to-text cleanup in `app/summarizer.py` so boilerplate such as "Read more", subscribe prompts, and navigation chrome no longer leaks into article summaries.

## 2. Background
- User reported that digests still contained "Read more" and similar boilerplate after summarization.
- Root cause traced to `_extract_text_from_html`, which only stripped `script`, `style`, `noscript` and then called `soup.get_text()` on the whole document, pulling in nav / footer / aside / related-articles / subscribe widgets.
- Secondary gap in `_build_simple_summary`: sentences were filtered only by length, so residual boilerplate sentences could survive.

## 3. Changes Made
- `app/summarizer.py`
  - Added module-level constants `BOILERPLATE_TAGS`, `BOILERPLATE_CLASS_HINTS`, `BOILERPLATE_PHRASES`, `_BOILERPLATE_PHRASE_RE`, `ANCHOR_TEXT_MAX_LEN`.
  - Added helper `_node_has_boilerplate_hint` for class/id token matching.
  - Rewrote `_extract_text_from_html`:
    1. Decompose expanded tag blacklist (adds `nav`, `header`, `footer`, `aside`, `form`, `button`, `iframe`, `figure`, `figcaption`).
    2. Decompose any element whose `class`/`id` contains a boilerplate hint token (whole-substring match on joined lowercase tokens).
    3. Decompose `<a>` elements whose stripped text is short (<= `ANCHOR_TEXT_MAX_LEN`) and exactly matches a boilerplate phrase.
    4. Prefer `<article>` / `<main>` / `[role="main"]` as extraction root; fall back to whole document.
    5. Line-level sweep: split extracted text on newlines and drop lines that wholly match a boilerplate phrase.
  - Updated `_build_simple_summary` to skip sentences matching `_BOILERPLATE_PHRASE_RE` before the length filter.
- `tests/test_summarizer.py`
  - Imported `_extract_text_from_html` and `_build_simple_summary` for direct unit testing.
  - Added `test_extract_text_strips_boilerplate_chrome` covering nav / header / footer / "Read more" anchor / subscribe aside.
  - Added `test_extract_text_removes_class_hint_containers` covering `class="more-stories"` and `id="related-articles"`.
  - Added `test_build_simple_summary_drops_boilerplate_sentence`.
  - Left `test_summarize_article_returns_digest` unchanged.

## 4. Affected Areas
- `app/summarizer.py`
- `tests/test_summarizer.py`
- `docs/changes/current_index.md` (index entry for this case)
- No changes to `app/search.py`, `app/writer.py`, `app/models.py`, `app/main.py`, or module boundaries in `docs/architecture.md`.

## 5. Validation
- Automated test execution was **not** performed in the working environment: the active Python interpreter (CPython 3.14) lacks the third-party dependencies declared in `app/summarizer.py` (`requests`, `bs4`, `googlenewsdecoder`), and the repository has no dependency manifest (see `docs/architecture.md` §10), so `pytest tests/test_summarizer.py` fails at import time with `ModuleNotFoundError: No module named 'requests'`. This blocker predates this change.
- Manual logic review of the three new tests confirmed they are deterministic offline tests (no network) and exercise each new cleanup stage.
- End-to-end behavior against real news pages is **not** verified here.
- Needs confirmation: run `pytest tests/` in an environment with dependencies installed, then run `app/main.py` end-to-end and spot-check `outputs/*.md` for residual "Read more" / subscribe / cookie-banner text.

## 6. Follow-up
- Run full `pytest` once a working dependency environment is available and update this case's Validation section.
- Known limitation: boilerplate phrase list is English-only; non-English pages' boilerplate may still leak.
- Known limitation: class/id hint matching is heuristic; sites using unusual class names may either retain boilerplate or, rarely, lose legitimate content.
- Deferred (not in scope): extractor/summarizer split per `summraizer_future_work.md`; adoption of `readability-lxml` or `trafilatura` for higher-quality extraction (new dependency — requires owner approval per `AGENTS.md` §Current Scope).
