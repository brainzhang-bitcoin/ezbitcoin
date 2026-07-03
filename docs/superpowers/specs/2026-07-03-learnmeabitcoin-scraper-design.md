# Design Spec: Learn Me A Bitcoin Scraper to Markdown

This specification outlines the design for a Python-based utility to scrape and convert tutorials from [Learn Me A Bitcoin](https://learnmeabitcoin.com/) into local Markdown files, preserving the chapter directory hierarchy and images.

## 1. Goal & Scope

- **Source website**: `https://learnmeabitcoin.com/`
- **Scope**: Extract all tutorial content from the **Beginners** and **Technical** sections.
- **Output structure**: 
  - Markdown files under `docs/` matching the URL paths (e.g. `docs/beginners/what-is-bitcoin.md`, `docs/technical/keys-addresses/wif.md`).
  - Downloaded images in `docs/images/` with sanitized, collision-free names (e.g., `beginners_what-is-bitcoin_blockchain.png`).
  - Markdown image links rewritten to relative paths (e.g., `../images/beginners_what-is-bitcoin_blockchain.png`).

## 2. Architecture & Components

The script `scrape_to_markdown.py` is modular and structured as follows:

```
+-------------------------------------------------------------+
|                     scrape_to_markdown.py                   |
|                                                             |
|  +--------------------+      +---------------------------+  |
|  |   SitemapParser    | ---> |      PageDownloader       |  |
|  | (Extract targets)  |      |   (HTTP reqs w/ retry)    |  |
|  +--------------------+      +-------------+-------------+  |
|                                            |                |
|                                            v                |
|  +--------------------+      +---------------------------+  |
|  |     DocWriter      | <--- |    ContentTransformer     |  |
|  | (Ensure dir/write) |      | (Parse DOM, clean, convert)  |  |
|  +--------------------+      +---------------------------+  |
+-------------------------------------------------------------+
```

### A. SitemapParser
- Fetch `https://learnmeabitcoin.com/sitemap`.
- Parse page using `BeautifulSoup`.
- Extract all `href` links matching:
  - `/beginners/*`
  - `/technical/*`
- Deduplicate and normalize to absolute URLs.

### B. PageDownloader
- Manage HTTP session using `requests.Session` with a custom `User-Agent`.
- Mount an HTTPAdapter with a retry strategy (3 retries, backoff factor) to handle transient errors.
- Implement polite scraping: enforce a delay of `0.2 - 0.5` seconds between consecutive network requests.

### C. ContentTransformer
- Parse each page's HTML:
  - Locate the main content element (typically the primary container containing the article, e.g., `<article>` or `#content`).
  - Strip navigation, sidebar, pagination, and header/footer elements.
- Extract `<img>` elements:
  - Download target images and save them in `docs/images/`.
  - Prefix image filename with the slug path of the chapter (e.g., `technical_keys-addresses_wif_image.png`) to avoid collisions.
  - Calculate relative paths dynamically based on the directory depth of the target Markdown file (e.g. `../../images/...`).
  - Rewrite `<img src="...">` to the relative local path.
- Convert HTML to Markdown using `markdownify`.

### D. DocWriter
- Determine relative folder structure based on URL.
- Ensure the destination directory exists.
- Write content to `.md` files.
- Track progress, skipping files that already exist to support resuming interrupted crawls.

## 3. Security & Rate Limiting

- **Polite Requests**: Introduce short sleep intervals (`time.sleep`) to prevent high traffic load on the source server.
- **Dependency Validation**:
  - We use standard Python libraries (`requests`, `beautifulsoup4`, `markdownify`). No complex binary or system-level installs are required.
