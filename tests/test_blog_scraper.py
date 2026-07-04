import os
from blog_router import get_local_path_for_blog_url, get_relative_link

def test_get_local_path_for_blog_url():
    assert get_local_path_for_blog_url("https://brainz.fun/blog/2026/06/01/mei-guo-zheng-fu-shi-ru-he-mei-shou-da-liang-bi-te-bi-de/") == "docs/beginners/how-us-government-seized-bitcoins.md"
    assert get_local_path_for_blog_url("/blog/2025/09/15/tan-tan-wen-ding-bi/") is None  # Excluded

def test_get_relative_link():
    assert get_relative_link("docs/technical/blockchain/bitcoin-blockchain-part2.md", "docs/technical/blockchain/bitcoin-blockchain-part1.md") == "bitcoin-blockchain-part1.md"
    assert get_relative_link("docs/technical/lightning/hello-lightning-network-part3.md", "docs/beginners/bitcoin-past-present-future.md") == "../../beginners/bitcoin-past-present-future.md"
