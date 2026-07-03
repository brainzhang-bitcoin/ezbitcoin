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


def test_path_helpers():
    from image_manager import sanitize_filename, get_relative_img_path
    
    # Check filename sanitization
    img_url = "https://learnmeabitcoin.com/images/beginners/transaction.png"
    assert sanitize_filename(img_url) == "beginners_transaction.png"
    
    # Check relative path generation from different markdown directories
    assert get_relative_img_path("docs/beginners/what-is-bitcoin.md", "beginners_transaction.png") == "../images/beginners_transaction.png"
    assert get_relative_img_path("docs/technical/keys-addresses/wif.md", "tech_wif.png") == "../../images/tech_wif.png"
