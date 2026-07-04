# Blog Import Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a custom Python crawler to download and import selected Bitcoin/Lightning-related blog posts from brainz.fun into the local documentation repository with clean markdown format, local images, and relative link mappings.

**Architecture:** A modular scraper consisting of a URL mapper (`blog_router.py`), an HTML/DOM cleaning and markdown transformer (`blog_transformer.py`), and a CLI runner (`scrape_blog.py`) with unit tests.

**Tech Stack:** Python 3, requests, BeautifulSoup (bs4), markdownify, pytest

## Global Constraints

- Technical terms MUST remain untranslated in the body content (already in Chinese, but keep body intact).
- Output Markdown file paths and filenames must match the defined mapping table.
- Images downloaded must be saved in `docs/images/` and prefixed with `blog_` to avoid conflicts.
- Crawl requests must have rate limiting (0.2s - 0.5s sleep) to be polite.

---

### Task 1: Blog URL Mapping & Router

**Files:**
- Create: `blog_router.py`
- Create: `tests/test_blog_scraper.py`

**Interfaces:**
- Consumes: None
- Produces:
  - `get_local_path_for_blog_url(url: str) -> str | None`
  - `get_relative_link(source_filepath: str, target_filepath: str) -> str`

- [ ] **Step 1: Write the failing test**

Write router tests in `tests/test_blog_scraper.py`:
```python
import os
from blog_router import get_local_path_for_blog_url, get_relative_link

def test_get_local_path_for_blog_url():
    assert get_local_path_for_blog_url("https://brainz.fun/blog/2026/06/01/mei-guo-zheng-fu-shi-ru-he-mei-shou-da-liang-bi-te-bi-de/") == "docs/beginners/how-us-government-seized-bitcoins.md"
    assert get_local_path_for_blog_url("/blog/2025/09/15/tan-tan-wen-ding-bi/") is None  # Excluded

def test_get_relative_link():
    assert get_relative_link("docs/technical/blockchain/bitcoin-blockchain-part2.md", "docs/technical/blockchain/bitcoin-blockchain-part1.md") == "bitcoin-blockchain-part1.md"
    assert get_relative_link("docs/technical/lightning/hello-lightning-network-part3.md", "docs/beginners/bitcoin-past-present-future.md") == "../../beginners/bitcoin-past-present-future.md"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `conda run -n ezbitcoin python -m pytest tests/test_blog_scraper.py -v`
Expected: FAIL (ModuleNotFoundError: No module named 'blog_router')

- [ ] **Step 3: Write minimal implementation**

Create `blog_router.py` with URL_MAP and path resolver functions:
```python
import os
from urllib.parse import urlparse

URL_MAP = {
    "mei-guo-zheng-fu-shi-ru-he-mei-shou-da-liang-bi-te-bi-de": "docs/beginners/how-us-government-seized-bitcoins.md",
    "yuan-gu-kuang-gong-zhuan-yi-8mo-mei-bi-te-bi": "docs/beginners/ancient-miners-move-bitcoins.md",
    "shi-xing-dai-ma-dian-fu-shi-jie-jin-rong-ti-xi": "docs/beginners/ten-lines-of-code-challenge-financial-system.md",
    "is-craig-wright-real-satoshi-nakamoto-2": "docs/beginners/is-craig-wright-real-satoshi-part2.md",
    "the-internet-of-money-du-shu-bi-ji": "docs/beginners/the-internet-of-money-reading-notes.md",
    "the-book-of-satoshi-du-shu-bi-ji": "docs/beginners/the-book-of-satoshi-reading-notes.md",
    "bi-te-bi-de-guo-qu-xian-zai-he-wei-lai": "docs/beginners/bitcoin-past-present-future.md",
    "happy-10th-birthday-bitcoin": "docs/beginners/happy-10th-birthday-bitcoin.md",
    "lnd-low-rescan-speed-for-startup": "docs/technical/lightning/lnd-low-rescan-speed-startup.md",
    "how-to-close-lightning-channels-by-lnd-cli": "docs/technical/lightning/how-to-close-lightning-channels-by-lnd-cli.md",
    "hello-lightning-network-3": "docs/technical/lightning/hello-lightning-network-part3.md",
    "hello-lightning-network-2": "docs/technical/lightning/hello-lightning-network-part2.md",
    "hello-lightning-network-1": "docs/technical/lightning/hello-lightning-network-part1.md",
    "hello-lightning-network-0": "docs/technical/lightning/hello-lightning-network-part0.md",
    "setup-lightning-node-cheat-sheet": "docs/technical/lightning/setup-lightning-node-cheat-sheet.md",
    "eltoo-shan-dian-he-chi-xian-qi-yue-geng-xin-ji-zhi": "docs/technical/lightning/eltoo-lightning-offchain-contracts.md",
    "shan-dian-wang-luo-man-man-cheng-chang": "docs/technical/lightning/lightning-network-gradual-growth.md",
    "how-to-set-systemd-startup-script-for-bitcoind": "docs/technical/networking/how-to-set-systemd-startup-script-for-bitcoind.md",
    "li-xiang-zhong-de-bi-te-bi-quan-jie-dian-shi-xian": "docs/technical/networking/ideal-bitcoin-full-node-implementation.md",
    "bi-te-bi-de-blockchain-2": "docs/technical/blockchain/bitcoin-blockchain-part2.md",
    "bi-te-bi-de-blockchain-1": "docs/technical/blockchain/bitcoin-blockchain-part1.md",
    "yi-chong-ti-gao-bi-te-bi-si-yao-peng-zhuang-ji-lu-de-si-lu": "docs/technical/cryptography/bitcoin-private-key-collision-ideas.md",
    "bi-te-bi-de-jiao-yi-6": "docs/technical/transaction/bitcoin-transaction-part6.md",
    "bi-te-bi-de-jiao-yi-5": "docs/technical/transaction/bitcoin-transaction-part5.md",
}

def get_local_path_for_blog_url(url: str) -> str | None:
    path = urlparse(url).path
    parts = [p for p in path.split("/") if p]
    if not parts:
        return None
    slug = parts[-1]
    return URL_MAP.get(slug)

def get_relative_link(source_filepath: str, target_filepath: str) -> str:
    source_dir = os.path.dirname(source_filepath)
    rel = os.path.relpath(target_filepath, source_dir)
    return rel.replace("\\", "/")
```

- [ ] **Step 4: Run test to verify it passes**

Run: `conda run -n ezbitcoin python -m pytest tests/test_blog_scraper.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add blog_router.py tests/test_blog_scraper.py
git commit -m "feat: add blog router and unit tests"
```

---

### Task 2: HTML Content Transformer

**Files:**
- Create: `blog_transformer.py`
- Modify: `tests/test_blog_scraper.py`

**Interfaces:**
- Consumes:
  - `blog_router.get_local_path_for_blog_url`
  - `blog_router.get_relative_link`
- Produces:
  - `transform_blog_html_to_markdown(html_content: str, md_filepath: str) -> tuple[str, list[dict]]`

- [ ] **Step 1: Write the failing test**

Append transformer tests in `tests/test_blog_scraper.py`:
```python
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
```

- [ ] **Step 2: Run test to verify it fails**

Run: `conda run -n ezbitcoin python -m pytest tests/test_blog_scraper.py -k test_transform_blog_html_to_markdown -v`
Expected: FAIL (ImportError or ModuleNotFoundError)

- [ ] **Step 3: Write minimal implementation**

Create `blog_transformer.py`:
```python
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from markdownify import MarkdownConverter
from blog_router import get_local_path_for_blog_url, get_relative_link
from image_manager import sanitize_filename, get_relative_img_path

class BlogConverter(MarkdownConverter):
    pass

def transform_blog_html_to_markdown(html_content: str, md_filepath: str) -> tuple[str, list[dict]]:
    soup = BeautifulSoup(html_content, "lxml")
    content_area = soup.find("article") or soup.find(class_="entry-content")
    if not content_area:
        content_area = soup.find("body") or soup

    # Decompose sharing, disqus, and meta elements
    for tag in content_area.find_all(class_=["sharing", "meta"]):
        tag.decompose()
    disqus = content_area.find(id="disqus_thread")
    if disqus:
        disqus.decompose()

    # Process images and rewrite sources
    images_to_download = []
    base_url = "https://brainz.fun/"

    for img in content_area.find_all("img"):
        src = img.get("src")
        if src:
            absolute_img_url = urljoin(base_url, src)
            # Prefix filename with blog_
            orig_filename = sanitize_filename(absolute_img_url)
            local_filename = f"blog_{orig_filename}"
            relative_path = get_relative_img_path(md_filepath, local_filename)
            
            img["src"] = relative_path
            images_to_download.append({
                "src_url": absolute_img_url,
                "local_filename": local_filename
            })

    # Rewrite internal links
    for a in content_area.find_all("a", href=True):
        href = a["href"]
        parsed = urlparse(href)
        # Check if internal blog link
        if "/blog/" in href:
            local_target = get_local_path_for_blog_url(href)
            if local_target:
                rel_href = get_relative_link(md_filepath, local_target)
                if parsed.fragment:
                    rel_href += f"#{parsed.fragment}"
                a["href"] = rel_href

    converter = BlogConverter(heading_style="ATX")
    markdown_content = converter.convert(str(content_area))
    return markdown_content.strip(), images_to_download
```

- [ ] **Step 4: Run test to verify it passes**

Run: `conda run -n ezbitcoin python -m pytest tests/test_blog_scraper.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add blog_transformer.py tests/test_blog_scraper.py
git commit -m "feat: add blog HTML content transformer and unit tests"
```

---

### Task 3: Integration Blog Scraper Script

**Files:**
- Create: `scrape_blog.py`

**Interfaces:**
- Consumes:
  - `blog_router.URL_MAP`
  - `blog_router.get_local_path_for_blog_url`
  - `blog_transformer.transform_blog_html_to_markdown`
- Produces: Command-line interface to run the crawl.

- [ ] **Step 1: Write integration runner**

Create `scrape_blog.py`:
```python
import os
import time
import random
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from blog_router import URL_MAP, get_local_path_for_blog_url
from blog_transformer import transform_blog_html_to_markdown

def scrape_blog():
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    })
    
    category_url = "https://brainz.fun/blog/categories/blockchain/"
    print(f"Fetching category page: {category_url}")
    try:
        resp = session.get(category_url, timeout=15)
        resp.raise_for_status()
    except Exception as e:
        print(f"Error fetching category page: {e}")
        return
        
    soup = BeautifulSoup(resp.text, "lxml")
    article_links = []
    
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if "/blog/" in href:
            absolute_url = urljoin(category_url, href)
            # Filter by matching URL slugs
            local_target = get_local_path_for_blog_url(absolute_url)
            if local_target and absolute_url not in article_links:
                article_links.append(absolute_url)
                
    print(f"Found {len(article_links)} matching articles to import.")
    os.makedirs("docs/images", exist_ok=True)
    
    for i, url in enumerate(article_links, 1):
        md_file_path = get_local_path_for_blog_url(url)
        print(f"[{i}/{len(article_links)}] Processing {url} -> {md_file_path}")
        
        # Rate limit sleep
        time.sleep(random.uniform(0.2, 0.5))
        
        try:
            art_resp = session.get(url, timeout=15)
            art_resp.raise_for_status()
        except Exception as e:
            print(f"  Failed to fetch: {e}")
            continue
            
        os.makedirs(os.path.dirname(md_file_path), exist_ok=True)
        md_content, images = transform_blog_html_to_markdown(art_resp.text, md_file_path)
        
        # Download images
        for img in images:
            img_dest = os.path.join("docs/images", img["local_filename"])
            if os.path.exists(img_dest):
                continue
                
            time.sleep(random.uniform(0.1, 0.3))
            try:
                img_resp = session.get(img["src_url"], timeout=15)
                img_resp.raise_for_status()
                with open(img_dest, "wb") as f:
                    f.write(img_resp.content)
                print(f"    Downloaded image: {img['local_filename']}")
            except Exception as e:
                print(f"    Failed to download image {img['src_url']}: {e}")
                
        # Write Markdown file
        with open(md_file_path, "w", encoding="utf-8") as f:
            f.write(md_content)
            
    print("Blog import completed successfully!")

if __name__ == "__main__":
    scrape_blog()
```

- [ ] **Step 2: Run execution to import files**

Run: `conda run -n ezbitcoin python scrape_blog.py`
Expected: Download and write all 24 mapped files with images successfully.

- [ ] **Step 3: Run translation verification test**

Run: `conda run -n ezbitcoin python -m pytest tests/test_translation.py -v`
Expected: PASS (All links in imported files are clean of non-ASCII characters).

- [ ] **Step 4: Commit**

```bash
git add scrape_blog.py docs/
git commit -m "feat: run blog scraper and import articles to repo"
```
