from blog_router import get_local_path_for_blog_url, get_relative_link

def test_get_local_path_for_blog_url():
    assert get_local_path_for_blog_url("https://brainz.fun/blog/2026/06/01/mei-guo-zheng-fu-shi-ru-he-mei-shou-da-liang-bi-te-bi-de/") == "docs/external/how-us-government-seizes-bitcoins.md"
    assert get_local_path_for_blog_url("/blog/2025/09/15/tan-tan-wen-ding-bi/") is None  # Excluded

def test_get_relative_link():
    assert get_relative_link("docs/technical/blockchain/bitcoin-blockchain-part2.md", "docs/technical/blockchain/bitcoin-blockchain-part1.md") == "bitcoin-blockchain-part1.md"
    assert get_relative_link("docs/technical/lightning/hello-lightning-network-part3.md", "docs/external/bitcoin-past-present-future.md") == "../../external/bitcoin-past-present-future.md"

def test_transform_blog_html_to_markdown():
    from blog_transformer import transform_blog_html_to_markdown
    sample_html = """
    <html>
      <body>
        <div id="content">
          <article role="article">
            <header>
              <h1 class="entry-title">测试文章</h1>
            </header>
            <div class="entry-content">
              <p>Hello world. Check <a href="/blog/2019/01/21/bi-te-bi-de-blockchain-1/">part 1</a>.</p>
              <img src="/images/blog/diagram.png" alt="Diagram" />
              <div class="sharing">Share this on Twitter</div>
            </div>
          </article>
        </div>
      </body>
    </html>
    """
    md, imgs = transform_blog_html_to_markdown(sample_html, "docs/technical/blockchain/bitcoin-blockchain-part2.md")
    assert "part 1" in md
    assert "bitcoin-blockchain-part1.md" in md
    assert "../../images/blog_diagram.png" in md
    assert "Share this" not in md
    assert len(imgs) == 1
    assert imgs[0]["src_url"] == "https://brainz.fun/images/blog/diagram.png"
    assert imgs[0]["local_filename"] == "blog_diagram.png"
