# Reorganize Documents into "External" (番外篇) Section Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reorganize doc files to move 8 specific articles under a new "External" (番外篇) section and verify that all links and tests pass.

**Architecture:** Create `docs/external/` directory, move files, create `docs/external.md` entry page, update `zensical.toml` navigation, update all Markdown links, and sync `README.md` to `docs/index.md`.

**Tech Stack:** Python, pytest, Git, Zensical.

## Global Constraints
- Do not break existing tests (ensure `pytest` runs cleanly after every change).
- Keep `docs/index.md` in sync with `README.md` using `scripts/sync_index.py`.

---

### Task 1: Create directory, move files and create entry page

**Files:**
- Create: `docs/external.md`
- Move: 8 markdown files into `docs/external/`

- [ ] **Step 1: Create the directory and move the files**

Run the following commands:
```bash
mkdir -p docs/external
mv docs/beginners/bitcoin-past-present-future.md docs/external/
mv docs/beginners/ancient-miners-move-bitcoins.md docs/external/
mv docs/beginners/how-us-government-seizes-bitcoins.md docs/external/
mv docs/beginners/ten-lines-of-code-challenge-financial-system.md docs/external/
mv docs/beginners/the-book-of-satoshi-reading-notes.md docs/external/
mv docs/beginners/the-internet-of-money-reading-notes.md docs/external/
mv docs/technical/cryptography/bitcoin-private-key-collision-ideas.md docs/external/
mv docs/technical/networking/ideal-bitcoin-full-node-implementation.md docs/external/
```

- [ ] **Step 2: Create the entry page `docs/external.md`**

Create `docs/external.md` with the following content:
```markdown
# 比特币番外篇

本部分收录了关于比特币科普、读书笔记以及其他精选外部推荐文章。

---

## 💡 推荐科普博文 (Blog Articles)
* [比特币的过去，现在和未来](external/bitcoin-past-present-future.md)
* [远古矿工转移8万枚比特币](external/ancient-miners-move-bitcoins.md)
* [美国政府是如何没收大量比特币的](external/how-us-government-seizes-bitcoins.md)
* [十行代码挑战世界金融体系](external/ten-lines-of-code-challenge-financial-system.md)

## 📖 读书笔记 (Reading Notes)
* [《The Book of Satoshi》读书笔记](external/the-book-of-satoshi-reading-notes.md)
* [《The Internet of Money》读书笔记](external/the-internet-of-money-reading-notes.md)

## ⚙️ 延伸探讨 (Extended Topics)
* [提高比特币私钥碰撞几率的思路](external/bitcoin-private-key-collision-ideas.md)
* [理想中的全节点实现](external/ideal-bitcoin-full-node-implementation.md)
```

- [ ] **Step 3: Commit**

```bash
git add docs/external/ docs/external.md
git commit -m "docs: move external articles and create external.md entry page"
```

---

### Task 2: Update site navigation in `zensical.toml`

**Files:**
- Modify: `zensical.toml`

- [ ] **Step 1: Modify `zensical.toml` navigation sections**

Edit `zensical.toml`:
1. In the `"新手指南"` block, remove the list items under `"推荐科普博文" = [...]`. Keep only:
```toml
    { "新手导读" = "beginners.md" },
    { "比特币是如何工作的？" = "beginners/how-does-bitcoin-work.md" },
    { "如何选择钱包" = "beginners/wallets.md" },
    { "如何选择交易所" = "beginners/exchanges.md" },
    { "如何发送与接收" = "beginners/sending.md" },
    { "安全与存储防范" = "beginners/security.md" },
    { "新手图解手册" = [
        ... (keep all guide entries)
    ]}
```
2. In the `"技术核心"` -> `"密码学"` block, remove the item `{ "提高比特币私钥碰撞几率的思路" = "technical/cryptography/bitcoin-private-key-collision-ideas.md" }`.
3. In the `"技术核心"` -> `"网络与挖矿"` block, remove the item `{ "理想中的全节点实现" = "technical/networking/ideal-bitcoin-full-node-implementation.md" }`.
4. At the end of the `[nav]` section, add a new section `"番外篇"`:
```toml
"番外篇" = [
    { "比特币番外篇" = "external.md" },
    { "比特币的过去，现在和未来" = "external/bitcoin-past-present-future.md" },
    { "远古矿工转移8万枚比特币" = "external/ancient-miners-move-bitcoins.md" },
    { "美国政府是如何没收大量比特币的" = "external/how-us-government-seizes-bitcoins.md" },
    { "十行代码挑战世界金融体系" = "external/ten-lines-of-code-challenge-financial-system.md" },
    { "《The Book of Satoshi》读书笔记" = "external/the-book-of-satoshi-reading-notes.md" },
    { "《The Internet of Money》读书笔记" = "external/the-internet-of-money-reading-notes.md" },
    { "提高比特币私钥碰撞几率的思路" = "external/bitcoin-private-key-collision-ideas.md" },
    { "理想中的全节点实现" = "external/ideal-bitcoin-full-node-implementation.md" }
]
```

- [ ] **Step 2: Commit**

```bash
git add zensical.toml
git commit -m "config: add External section to zensical.toml nav"
```

---

### Task 3: Update links in markdown files and index

**Files:**
- Modify: `README.md`, `docs/beginners.md`, `docs/technical.md`, and any other cross-references
- Run: `python scripts/sync_index.py`

- [ ] **Step 1: Update links in `README.md`**

In `README.md`:
1. Move the 6 articles under `"🟢 1. 新手指南 (Beginners Guide)"` -> `"* 💡 推荐科普博文 (Blog Articles)"` block. Move them to a new third section:
```markdown
### 🟡 3. 番外篇 (External Articles)
外部科普推荐、读书笔记与延伸思考。

*   **[比特币番外篇主页](docs/external.md)**
*   **💡 推荐科普博文 (Blog Articles)**
    *   [美国政府是如何没收大量比特币的](docs/external/how-us-government-seizes-bitcoins.md)
    *   [远古矿工转移8万枚比特币](docs/external/ancient-miners-move-bitcoins.md)
    *   [十行代码挑战世界金融体系](docs/external/ten-lines-of-code-challenge-financial-system.md)
    *   [《The Internet of Money》读书笔记](docs/external/the-internet-of-money-reading-notes.md)
    *   [《The Book of Satoshi》读书笔记](docs/external/the-book-of-satoshi-reading-notes.md)
    *   [比特币的过去，现在和未来](docs/external/bitcoin-past-present-future.md)
*   **⚙️ 延伸思考 (Extended Topics)**
    *   [提高比特币私钥碰撞几率的思路](docs/external/bitcoin-private-key-collision-ideas.md)
    *   [理想中的比特币全节点实现](docs/external/ideal-bitcoin-full-node-implementation.md)
```
2. Remove `"提高比特币私钥碰撞几率的思路"` and `"理想中的比特币全节点实现"` from `"技术核心"` section in `README.md`.

- [ ] **Step 2: Update links in `docs/beginners.md`**

In `docs/beginners.md`:
1. Remove `## 💡 推荐科普博文` section.
2. In `docs/beginners.md` line 61, update the link `[技术部分](technical.md)` and add a reference to `[番外部分](external.md)`.
3. Check and correct other links if necessary.

- [ ] **Step 3: Update links in `docs/technical.md`**

In `docs/technical.md`:
1. Remove references to `"提高比特币私钥碰撞几率的思路"` and `"理想中的比特币全节点实现"`.

- [ ] **Step 4: Update internal links in the moved files**

Check if the moved files reference images or other files using relative paths, and adjust.
Specifically:
- Check if they link to `images/...` using relative paths.
Since they were in `docs/beginners/xxx.md` (one directory deep), they linked to `images/yyy.png` (using `images/yyy.png` or `../images/yyy.png`?). Wait!
Let's see: `docs/beginners/xxx.md` is one directory deep, so its relative link to `docs/images/` is `images/` or `../images/`?
Let's check `content_transformer.py` line 63:
`relative_path = get_relative_img_path(md_filepath, local_filename)`
Let's check `image_manager.py` or run a search.
Wait, let's make sure the image paths in the moved files are updated if needed.
The moved files will live in `docs/external/xxx.md`, which is also one directory deep (under `docs/external`). So their relative path to `docs/images/` remains exactly the same!
No change to image relative paths is required since `docs/beginners/` and `docs/external/` are both exactly one level deep from `docs/`.

- [ ] **Step 5: Run the sync script**

Run: `python scripts/sync_index.py`

- [ ] **Step 6: Verify and commit**

Run `python -m pytest` and commit:
```bash
git add README.md docs/beginners.md docs/technical.md docs/index.md
git commit -m "docs: update document links and sync index"
```

---

### Task 4: Fix script blog router mappings

**Files:**
- Modify: `blog_router.py`

- [ ] **Step 1: Update path mapping in `blog_router.py`**

In `blog_router.py`, the path mappings for imported blogs need to reflect their new locations.
Let's view `blog_router.py` to see the exact mappings.
Wait, let's view it in this step or now. Yes, we will modify `blog_router.py` to match the new locations.
For example:
- `"docs/beginners/how-us-government-seized-bitcoins.md"` should be `"docs/external/how-us-government-seizes-bitcoins.md"` (or check spelling of files).
- Run: `pytest` to ensure scraper/blog router tests pass.

- [ ] **Step 2: Commit**

```bash
git add blog_router.py
git commit -m "refactor: update blog router mappings to use docs/external"
```

---

### Task 5: Final verification and build

- [ ] **Step 1: Run all tests**

Run: `conda run -n ezbitcoin python -m pytest`
Expected: 9/9 passed.

- [ ] **Step 2: Rebuild site**

Run: `conda run -n ezbitcoin zensical build`
Expected: Succeeds.
