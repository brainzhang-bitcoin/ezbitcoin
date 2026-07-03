def test_environment():
    import requests
    import bs4
    import markdownify
    assert True


def test_extract_urls():
    from sitemap_parser import extract_urls
    dummy_html = """
    <html>
      <body>
        <a href="/beginners/what-is-bitcoin">What is Bitcoin</a>
        <a href="/technical/keys-addresses/wif">WIF</a>
        <a href="/tools/crypto">Tools</a>
        <a href="/about">About</a>
      </body>
    </html>
    """
    urls = extract_urls(dummy_html)
    assert "https://learnmeabitcoin.com/beginners/what-is-bitcoin" in urls
    assert "https://learnmeabitcoin.com/technical/keys-addresses/wif" in urls
    assert "https://learnmeabitcoin.com/tools/crypto" not in urls

