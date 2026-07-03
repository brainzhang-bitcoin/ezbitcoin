# Learn Me A Bitcoin Scraper Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Scrape the Beginners and Technical guide content from learnmeabitcoin.com and export it to Markdown files with local image assets under `docs/`.

**Architecture:** A modular Python crawler utilizing `requests` for fetching, `BeautifulSoup4` for parsing/filtering, and `markdownify` for converting HTML to clean Markdown.

**Tech Stack:** Python 3, `requests`, `beautifulsoup4`, `markdownify`, `lxml` (for faster HTML parsing).

## Global Constraints
- Target URL: `https://learnmeabitcoin.com/`
- Directories to fetch: `/beginners/` and `/technical/`
- Markdown destination: `docs/`
- Image destination: `docs/images/`
- Implement rate limiting (0.2s - 0.5s sleep between calls).

---

### Task 1: Project Setup and Dependencies

**Files:**
- Create: `requirements.txt`
- Create: `tests/test_scraper.py`

**Interfaces:**
- Consumes: None
- Produces: Installed python dependencies and verification test suite structure.

- [ ] **Step 1: Write requirements.txt file**

```text
requests>=2.31.0
beautifulsoup4>=4.12.0
markdownify>=0.11.6
lxml>=4.9.3
pytest>=7.4.0
```

- [ ] **Step 2: Install dependencies**

Run: `pip install -r requirements.txt`
Expected: Installation completes successfully.

- [ ] **Step 3: Write basic test validation in tests/test_scraper.py**

```python
def test_environment():
    import requests
    import bs4
    import markdownify
    assert True
```

- [ ] **Step 4: Run pytest to verify the environment test passes**

Run: `pytest tests/test_scraper.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add requirements.txt tests/test_scraper.py
git commit -m "feat: project setup and environment test"
```

---

### Task 2: Implement SitemapParser

**Files:**
- Create: `sitemap_parser.py`
- Modify: `tests/test_scraper.py`

**Interfaces:**
- Consumes: None
- Produces: `extract_urls(html_content: str) -> list[str]`

- [ ] **Step 1: Write the test for SitemapParser in tests/test_scraper.py**

Append to `tests/test_scraper.py`:
```python
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
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_scraper.py::test_extract_urls -v`
Expected: FAIL with "ImportError: cannot import name 'extract_urls'"

- [ ] **Step 3: Write SitemapParser implementation**

Write `sitemap_parser.py`:
```python
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def extract_urls(html_content: str) -> list[str]:
    soup = BeautifulSoup(html_content, "lxml")
    links = []
    base_url = "https://learnmeabitcoin.com/"
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.startswith("/beginners/") or href.startswith("/technical/"):
            links.append(urljoin(base_url, href))
    return sorted(list(set(links)))
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_scraper.py::test_extract_urls -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add sitemap_parser.py tests/test_scraper.py
git commit -m "feat: implement sitemap parser"
```

---

### Task 3: Implement ImageManager and Path Utilities

**Files:**
- Create: `image_manager.py`
- Modify: `tests/test_scraper.py`

**Interfaces:**
- Consumes: None
- Produces: `sanitize_filename(url_path: str) -> str`, `get_relative_img_path(md_file_path: str, image_name: str) -> str`

- [ ] **Step 1: Write tests for helper paths in tests/test_scraper.py**

Append to `tests/test_scraper.py`:
```python
def test_path_helpers():
    from image_manager import sanitize_filename, get_relative_img_path
    
    # Check filename sanitization
    img_url = "https://learnmeabitcoin.com/images/beginners/transaction.png"
    assert sanitize_filename(img_url) == "beginners_transaction.png"
    
    # Check relative path generation from different markdown directories
    assert get_relative_img_path("docs/beginners/what-is-bitcoin.md", "beginners_transaction.png") == "../images/beginners_transaction.png"
    assert get_relative_img_path("docs/technical/keys-addresses/wif.md", "tech_wif.png") == "../../images/tech_wif.png"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_scraper.py::test_path_helpers -v`
Expected: FAIL with "ImportError: cannot import name 'sanitize_filename'"

- [ ] **Step 3: Write ImageManager implementation**

Write `image_manager.py`:
```python
import os
import re

def sanitize_filename(url: str) -> str:
    # Extract path portion and replace slashes and special chars with underscores
    path = url.split("learnmeabitcoin.com/")[-1]
    path = path.replace("images/", "").replace("assets/", "")
    sanitized = re.sub(r"[^a-zA-Z0-9\.\-_]", "_", path)
    return sanitized.strip("_")

def get_relative_img_path(md_file_path: str, image_name: str) -> str:
    # Count directories between docs/ and target markdown file
    parts = md_file_path.split("/")
    # Format: docs/dir1/dir2/file.md -> parts has len 4 (docs, dir1, dir2, file.md)
    # The image path is always in docs/images/.
    # Number of up-steps is len(parts) - 2
    steps = len(parts) - 2
    prefix = "../" * steps if steps > 0 else ""
    return f"{prefix}images/{image_name}"
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_scraper.py::test_path_helpers -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add image_manager.py tests/test_scraper.py
git commit -m "feat: implement image path helpers"
```

---

### Task 4: ContentTransformer & DocWriter

**Files:**
- Create: `content_transformer.py`
- Modify: `tests/test_scraper.py`

**Interfaces:**
- Consumes: `image_manager`
- Produces: `transform_html_to_markdown(html_content: str, md_filepath: str) -> tuple[str, list[dict]]` where list contains `{"src_url": ..., "local_filename": ...}`

- [ ] **Step 1: Write unit tests for ContentTransformer in tests/test_scraper.py**

Append to `tests/test_scraper.py`:
```python
def test_transform_html_to_markdown():
    from content_transformer import transform_html_to_markdown
    
    html = """
    <html>
      <body>
        <div id="content">
          <h1>What is Bitcoin?</h1>
          <p>Bitcoin is a currency.</p>
          <img src="/images/beginners/what-is-bitcoin/btc.png" alt="Bitcoin logo" />
        </div>
      </body>
    </html>
    """
    
    md_content, images = transform_html_to_markdown(html, "docs/beginners/what-is-bitcoin.md")
    
    assert "# What is Bitcoin?" in md_content
    assert "Bitcoin is a currency." in md_content
    # Link should be converted to relative local link
    assert "![](../images/beginners_what-is-bitcoin_btc.png)" in md_content
    assert len(images) == 1
    assert images[0]["local_filename"] == "beginners_what-is-bitcoin_btc.png"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_scraper.py::test_transform_html_to_markdown -v`
Expected: FAIL with "ImportError: cannot import name 'transform_html_to_markdown'"

- [ ] **Step 3: Write ContentTransformer implementation**

Write `content_transformer.py`:
```python
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from urllib.parse import urljoin
from image_manager import sanitize_filename, get_relative_img_path

def transform_html_to_markdown(html_content: str, md_filepath: str) -> tuple[str, list[dict]]:
    soup = BeautifulSoup(html_content, "lxml")
    
    # Locate article body. learnmeabitcoin content usually sits in <main> or class "content" or id "content"
    content_area = soup.find("article") or soup.find(id="content") or soup.find(class_="content")
    if not content_area:
        content_area = soup.find("body") or soup
        
    # Strip unnecessary elements (e.g., pagination buttons, navigation, scripts)
    for tag in content_area.find_all(["script", "style", "nav", "header", "footer"]):
        tag.decompose()
        
    # Process images and rewrite sources
    images_to_download = []
    base_url = "https://learnmeabitcoin.com/"
    
    for img in content_area.find_all("img"):
        src = img.get("src")
        if src:
            absolute_img_url = urljoin(base_url, src)
            local_filename = sanitize_filename(absolute_img_url)
            relative_path = get_relative_img_path(md_filepath, local_filename)
            
            img["src"] = relative_path
            images_to_download.append({
                "src_url": absolute_img_url,
                "local_filename": local_filename
            })
            
    # Convert cleaned HTML to markdown
    markdown_content = md(str(content_area), heading_style="ATX")
    return markdown_content.strip(), images_to_download
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_scraper.py::test_transform_html_to_markdown -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add content_transformer.py tests/test_scraper.py
git commit -m "feat: implement content transformer"
```

---

### Task 5: Integration Scraper Script

**Files:**
- Create: `scrape_to_markdown.py`

**Interfaces:**
- Consumes: `sitemap_parser`, `image_manager`, `content_transformer`
- Produces: Executable command-line script to scrape learnmeabitcoin.com into `docs/`

- [ ] **Step 1: Write integration scraper implementation**

Write `scrape_to_markdown.py`:
```python
import os
import time
import random
import requests
from sitemap_parser import extract_urls
from content_transformer import transform_html_to_markdown

def main():
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    })
    
    # 1. Fetch and Parse Sitemap
    print("Fetching Sitemap...")
    try:
        sitemap_resp = session.get("https://learnmeabitcoin.com/sitemap", timeout=15)
        sitemap_resp.raise_for_status()
    except Exception as e:
        print(f"Error fetching sitemap: {e}")
        return
        
    urls = extract_urls(sitemap_resp.text)
    print(f"Found {len(urls)} matching urls.")
    
    # Ensure local directory structure
    os.makedirs("docs/images", exist_ok=True)
    
    # 2. Scrape each URL
    for i, url in enumerate(urls, 1):
        # Determine output file path
        path_suffix = url.split("learnmeabitcoin.com/")[-1]
        md_file_path = f"docs/{path_suffix.strip('/')}.md"
        
        print(f"[{i}/{len(urls)}] Processing {url} -> {md_file_path}")
        
        # Check if already processed
        if os.path.exists(md_file_path):
            print(f"  Skipped (already exists)")
            continue
            
        # Get content
        try:
            resp = session.get(url, timeout=15)
            resp.raise_for_status()
        except Exception as e:
            print(f"  Failed to fetch: {e}")
            continue
            
        os.makedirs(os.path.dirname(md_file_path), exist_ok=True)
        
        # Transform content
        md_content, images = transform_html_to_markdown(resp.text, md_file_path)
        
        # Download images
        for img in images:
            img_dest = os.path.join("docs/images", img["local_filename"])
            if os.path.exists(img_dest):
                continue
            
            # Rate limiting sleep before fetching image
            time.sleep(random.uniform(0.1, 0.3))
            try:
                img_resp = session.get(img["src_url"], timeout=15)
                img_resp.raise_for_status()
                with open(img_dest, "wb") as f:
                    f.write(img_resp.content)
                print(f"    Downloaded image: {img['local_filename']}")
            except Exception as e:
                print(f"    Failed to download image {img['src_url']}: {e}")
                
        # Write Markdown
        with open(md_file_path, "w", encoding="utf-8") as f:
            f.write(md_content)
            
        # Sleep to be polite
        time.sleep(random.uniform(0.2, 0.5))

if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run pytest across all test suites to ensure sanity**

Run: `pytest tests/test_scraper.py -v`
Expected: PASS

- [ ] **Step 3: Execute integration run (Verify by scraping first few pages)**

Run: `python scrape_to_markdown.py`
Expected: Program starts fetching, outputs progress, downloads images, and writes to `docs/` hierarchy successfully.

- [ ] **Step 4: Commit**

```bash
git add scrape_to_markdown.py
git commit -m "feat: complete scraper implementation and verify execution"
```
