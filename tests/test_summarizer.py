from app.models import ArticleCandidate, ArticleDigest
from app.summarizer import (
    _build_simple_summary,
    _extract_text_from_html,
    summarize_article,
)


def test_summarize_article_returns_digest():
    candidate = ArticleCandidate(
        title="AI News 1",
        url="https://example.com/article1",
        source="BBC",
        published_date="2026-04-08",
        note="Stub result",
    )

    digest = summarize_article(candidate)

    assert isinstance(digest, ArticleDigest)
    assert digest.title == "AI News 1"
    assert digest.url == "https://example.com/article1"
    assert digest.source == "BBC"
    assert digest.published_date == "2026-04-08"
    assert digest.extraction_status == "Success"
    assert "AI News 1" in digest.summary
    assert len(digest.key_points) == 2
    assert len(digest.warnings) == 1


def test_extract_text_strips_boilerplate_chrome():
    html = """
    <html><body>
      <nav>Home | About | Contact</nav>
      <header>Site Header</header>
      <article>
        <p>The first paragraph has enough substantive content to satisfy the length threshold comfortably.</p>
        <p>The second paragraph also carries substantive sentences for a reader to consume in full.</p>
        <a href="/next">Read more</a>
        <aside class="subscribe-box">Subscribe to our newsletter</aside>
      </article>
      <footer>Copyright 2026 | Terms of Service</footer>
    </body></html>
    """

    cleaned = _extract_text_from_html(html).lower()

    assert "read more" not in cleaned
    assert "subscribe" not in cleaned
    assert "site header" not in cleaned
    assert "copyright" not in cleaned
    assert "home | about | contact" not in cleaned
    assert "first paragraph" in cleaned
    assert "second paragraph" in cleaned


def test_extract_text_removes_class_hint_containers():
    html = """
    <html><body><article>
      <p>Artificial intelligence continues to reshape how people work and learn every single day.</p>
      <div class="more-stories">You may also like: Ten AI tools</div>
      <div id="related-articles">Related: How AI changes medicine</div>
    </article></body></html>
    """

    cleaned = _extract_text_from_html(html).lower()

    assert "you may also like" not in cleaned
    assert "related: how ai" not in cleaned
    assert "artificial intelligence" in cleaned


def test_build_simple_summary_drops_boilerplate_sentence():
    text = (
        "Read more. "
        "Artificial intelligence continues to reshape how we work and learn every day."
    )

    summary, points = _build_simple_summary(text, max_sentences=2)

    assert "Read more" not in summary
    assert "Artificial intelligence" in summary
    assert all("Read more" not in point for point in points)