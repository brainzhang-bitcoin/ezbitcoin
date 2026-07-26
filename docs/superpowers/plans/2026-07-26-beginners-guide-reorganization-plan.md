# Beginners Guide Reorganization Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reorganize the Beginners Guide section into logical phases and fix formatting/logic issues in the markdown files.

**Architecture:** We are updating existing Markdown documentation (`docs/index.md` and `docs/beginners/*.md`) to improve the reading flow and fix formatting issues like broken links and heading hierarchies.

**Tech Stack:** Markdown

## Global Constraints

- No structural changes outside of the "Beginners Guide" section in `index.md`.
- Ensure all markdown formatting is valid GitHub Flavored Markdown.
- Ensure all relative image paths (`../images/...`) remain correct if files are moved, though files are not planned to be moved, just edited.

---

### Task 1: Reorganize Table of Contents

**Files:**
- Modify: `docs/index.md`

**Interfaces:**
- Consumes: Existing structure of `docs/index.md`
- Produces: An updated "Beginners Guide" section in `docs/index.md` with 5 distinct phases.

- [ ] **Step 1: Write the updated structure (Implementation)**
Update `docs/index.md` to reflect the new structure.

Replace the current Beginners Guide section with:
```markdown
### 🟢 1. 新手指南 (Beginners Guide)
适合完全没有技术背景的读者，用极简非技术语言介绍比特币基本概念。

#### Phase 1: Introduction & Core Concepts
*   **[新手导读及概览](beginners.md)**
*   **[比特币是如何工作的？](beginners/how-does-bitcoin-work.md)**

#### Phase 2: Acquisition (Getting Bitcoin)
*   **[如何选择交易平台 (Exchanges)](beginners/exchanges.md)**

#### Phase 3: Storage & Safety
*   **[如何选择钱包 (Wallets)](beginners/wallets.md)**
*   **[安全与存储防范 (Security)](beginners/security.md)**

#### Phase 4: Usage
*   **[如何发送与接收比特币 (Sending)](beginners/sending.md)**

#### Phase 5: Technical Primer
*   **📖 新手极简图解手册 (Beginners Short Guide)**
    *   [比特币网络 (Network)](beginners/guide/network.md)
    *   [节点 (Node)](beginners/guide/node.md)
    *   [挖矿 (Mining)](beginners/guide/mining.md)
    *   [区块链 (Blockchain)](beginners/guide/blockchain.md)
    *   [区块 (Blocks)](beginners/guide/blocks.md)
    *   [难度 (Difficulty)](beginners/guide/difficulty.md)
    *   [交易 (Transactions)](beginners/guide/transactions.md)
    *   [交易输出 (Outputs)](beginners/guide/outputs.md)
    *   [锁定与解锁 (Locks)](beginners/guide/locks.md)
    *   [密钥与地址 (Keys & Addresses)](beginners/guide/keys-addresses.md)
    *   [私钥 (Private Keys)](beginners/guide/private-keys.md)
    *   [公钥 (Public Keys)](beginners/guide/public-keys.md)
    *   [数字签名 (Digital Signatures)](beginners/guide/digital-signatures.md)
    *   [隔离见证 (SegWit)](beginners/guide/segwit.md)
```

- [ ] **Step 2: Verify changes**
Ensure the Markdown syntax is correct and all links point to the right files.

- [ ] **Step 3: Commit**
```bash
git add docs/index.md
git commit -m "docs: reorganize beginners guide table of contents"
```

---

### Task 2: Fix Formatting in Intro and How it Works

**Files:**
- Modify: `docs/beginners.md` (if exists and has issues)
- Modify: `docs/beginners/how-does-bitcoin-work.md`

**Interfaces:**
- Consumes: Markdown content
- Produces: Corrected Markdown content

- [ ] **Step 1: Inspect `beginners.md` and `how-does-bitcoin-work.md` for formatting issues**
Use `grep` or `cat` (via `view_file`) to check for misaligned tables, broken links, and bad heading hierarchies.

- [ ] **Step 2: Apply fixes**
Fix any identified issues (e.g., ensure `#` headings are sequential, image links like `../images/...` are valid, bold/italic syntax is closed).

- [ ] **Step 3: Commit**
```bash
git add docs/beginners.md docs/beginners/how-does-bitcoin-work.md
git commit -m "docs: fix formatting in beginners intro chapters"
```

---

### Task 3: Fix Formatting in Acquisition and Storage Chapters

**Files:**
- Modify: `docs/beginners/exchanges.md`
- Modify: `docs/beginners/wallets.md`
- Modify: `docs/beginners/security.md`

**Interfaces:**
- Consumes: Markdown content
- Produces: Corrected Markdown content

- [ ] **Step 1: Inspect files for formatting issues**
Check for misaligned tables, broken links, and bad heading hierarchies. Focus on `wallets.md` and `exchanges.md` to ensure logic flows correctly (e.g., buying first, then storing).

- [ ] **Step 2: Apply fixes**
Fix formatting. Make minor text adjustments if necessary to ensure smooth narrative flow between chapters.

- [ ] **Step 3: Commit**
```bash
git add docs/beginners/exchanges.md docs/beginners/wallets.md docs/beginners/security.md
git commit -m "docs: fix formatting and logic in exchanges, wallets, and security chapters"
```

---

### Task 4: Fix Formatting in Usage Chapter

**Files:**
- Modify: `docs/beginners/sending.md`

**Interfaces:**
- Consumes: Markdown content
- Produces: Corrected Markdown content

- [ ] **Step 1: Inspect `sending.md` for formatting issues**
Check for misaligned tables, broken links, and bad heading hierarchies.

- [ ] **Step 2: Apply fixes**
Fix formatting and logic issues.

- [ ] **Step 3: Commit**
```bash
git add docs/beginners/sending.md
git commit -m "docs: fix formatting in sending chapter"
```
