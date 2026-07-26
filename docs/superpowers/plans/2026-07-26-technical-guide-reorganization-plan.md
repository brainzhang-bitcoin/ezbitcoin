# Technical Guide Reorganization Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reorganize the Technical Guide section of the docs into a "Transaction Lifecycle" learning path (5 phases) and fix markdown formatting issues across technical directories.

**Architecture:** We are updating the central table of contents (`docs/index.md` and `docs/technical/index.md`) to reflect the new 5-phase structure. Then, we perform a sweep of the root topic files within `docs/technical/` to fix broken markdown (missing H1s, tables, invalid anchors), similar to the Beginners Guide refactor.

**Tech Stack:** Markdown (GFM)

## Global Constraints

- No structural changes to files outside the Technical Guide section.
- Ensure all markdown formatting is valid GitHub Flavored Markdown (GFM).
- Ensure all relative image paths (`../images/...` or `../../images/...`) remain correct.
- Do NOT rewrite or delete technical content; only fix formatting, hierarchy, and navigation flow.

---

### Task 1: Update Table of Contents

**Files:**
- Modify: `docs/index.md`
- Modify: `docs/technical/index.md`

**Interfaces:**
- Consumes: Existing TOC layout.
- Produces: A unified 5-phase structure in the TOCs.

- [ ] **Step 1: Update `docs/index.md` Technical Guide Section**

Replace the existing "2. 技术指南" category list with the 5 phases defined in the spec:
- Phase 1: 基础工具箱 (Foundation & Toolbox) -> CS Basics, Cryptography, Keys
- Phase 2: 构建交易 (Constructing the Transaction) -> Transactions, Script
- Phase 3: 广播与确认 (Broadcast & Consensus) -> Networking, Mining, Block
- Phase 4: 账本与演进 (The Ledger & Protocol Evolution) -> Blockchain, Upgrades
- Phase 5: 二层扩展 (Layer 2 Scaling) -> Lightning Network

Ensure all links (e.g. `technical/cryptography.md`, `technical/block.md`) are preserved and nested correctly under these phases.

- [ ] **Step 2: Update `docs/technical/index.md`**

Mirror the exact same 5-phase structure in `docs/technical/index.md` so that users navigating directly to the technical root see the new learning path.

- [ ] **Step 3: Verify formatting visually/programmatically**

Run: `cat docs/index.md | grep "Phase 1: 基础工具箱"`
Expected: Matches found.

- [ ] **Step 4: Commit**

```bash
git add docs/index.md docs/technical/index.md
git commit -m "docs: reorganize technical guide TOC into 5 phases"
```

---

### Task 2: Formatting Sweep for Phase 1 & 2 (Foundation & Transactions)

**Files:**
- Modify: `docs/technical/cryptography.md`
- Modify: `docs/technical/keys.md`
- Modify: `docs/technical/transaction.md`
- Modify: `docs/technical/script.md`

**Interfaces:**
- Consumes: Phase 1 & 2 markdown files.
- Produces: Clean GFM files with proper H1 headers and correct relative links.

- [ ] **Step 1: Inspect Phase 1 & 2 root files**

Check if `docs/technical/cryptography.md`, `keys.md`, `transaction.md`, and `script.md` have top-level `#` (H1) headers. 
Check for broken tables, unformatted raw text, or broken relative links.

- [ ] **Step 2: Apply Formatting Fixes**

For each file, ensure it starts with an H1 header matching its title (e.g., `# 密码学总览 (Cryptography)`).
Fix any invalid inline markdown (like nested bold/italics) and ensure blockquotes or tables are properly separated by newlines.

- [ ] **Step 3: Verify**

Run: `grep -E "^# " docs/technical/cryptography.md docs/technical/keys.md docs/technical/transaction.md docs/technical/script.md`
Expected: Each file returns exactly one H1 header at the top.

- [ ] **Step 4: Commit**

```bash
git add docs/technical/cryptography.md docs/technical/keys.md docs/technical/transaction.md docs/technical/script.md
git commit -m "docs: fix formatting in phase 1 and 2 technical root files"
```

---

### Task 3: Formatting Sweep for Phase 3 & 4 (Broadcast, Ledger, Upgrades)

**Files:**
- Modify: `docs/technical/networking.md`
- Modify: `docs/technical/mining.md`
- Modify: `docs/technical/block.md`
- Modify: `docs/technical/blockchain.md`

**Interfaces:**
- Consumes: Phase 3 & 4 markdown files.
- Produces: Clean GFM files with proper H1 headers and correct relative links.

- [ ] **Step 1: Inspect Phase 3 & 4 root files**

Check if `docs/technical/networking.md`, `mining.md`, `block.md`, and `blockchain.md` have top-level `#` (H1) headers.
Check for broken tables, unformatted raw text, or broken relative links.

- [ ] **Step 2: Apply Formatting Fixes**

For each file, ensure it starts with an H1 header matching its title.
Fix any invalid inline markdown and verify anchor links.

- [ ] **Step 3: Verify**

Run: `grep -E "^# " docs/technical/networking.md docs/technical/mining.md docs/technical/block.md docs/technical/blockchain.md`
Expected: Each file returns exactly one H1 header at the top.

- [ ] **Step 4: Commit**

```bash
git add docs/technical/networking.md docs/technical/mining.md docs/technical/block.md docs/technical/blockchain.md
git commit -m "docs: fix formatting in phase 3 and 4 technical root files"
```

---

### Task 4: Formatting Sweep for Phase 5 (Lightning Network)

**Files:**
- Modify: `docs/technical/lightning.md`

**Interfaces:**
- Consumes: Phase 5 markdown files.
- Produces: Clean GFM files with proper H1 headers and correct relative links.

- [ ] **Step 1: Inspect Phase 5 root files**

Check if `docs/technical/lightning.md` has a top-level `#` (H1) header.
Check for broken tables, unformatted raw text, or broken relative links.

- [ ] **Step 2: Apply Formatting Fixes**

Ensure it starts with an H1 header.
Fix any invalid inline markdown and verify anchor links.

- [ ] **Step 3: Verify**

Run: `grep -E "^# " docs/technical/lightning.md`
Expected: Returns exactly one H1 header at the top.

- [ ] **Step 4: Commit**

```bash
git add docs/technical/lightning.md
git commit -m "docs: fix formatting in phase 5 technical root files"
```
