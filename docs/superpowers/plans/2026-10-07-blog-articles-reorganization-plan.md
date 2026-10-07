# 导入博文重构与体系融合实施计划 (Implementation Plan)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development or sequential execution to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

- **目标**：根据已批准的规格说明书 [2026-10-07-blog-articles-reorganization-design.md](../specs/2026-10-07-blog-articles-reorganization-design.md)，完成从博客导入文章的去重、清洗、重命名与全书 5 大技术阶段的深度融合，并实现全局链接 100% 自愈。
- **技术栈**：Markdown (GFM), Python (校验脚本), Git
- **全局约束**：
  - 严禁随意删除博文中的高价值实战代码与核心技术推导。
  - 所有代码块必须统一为标准的 GFM 语法高亮格式（如 ` ```python `, ` ```bash `, ` ```json `）。
  - 所有图片相对路径（`../../images/...` 或 `../images/...`）必须根据文件新层级保持正确。
  - 全站所有 Markdown 内部相对链接必须自愈，不允许出现死链。

---

### Task 1: Phase 2 交易实战篇重构与去重

**目标文件**：
- 原文件：`docs/technical/transaction/bitcoin-transaction-part5.md`
- 目标文件：`docs/technical/transaction/raw-transaction-python.md`

- [ ] **Step 1: 重命名并重构文件内容**
  - 使用 `git mv` 将 `docs/technical/transaction/bitcoin-transaction-part5.md` 重命名为 `docs/technical/transaction/raw-transaction-python.md`。
  - 将 H1 标题更新为：`# 实战：用 Python 手工构造并签署裸交易 (Constructing Raw Transaction)`。
  - 去除开篇对不存在的“交易-3”、“HD钱包-2”的口头依赖，改为清晰独立的前置假定环境说明。
  - 将单列带行号的代码表格转换为纯净的 ` ```python ` 代码块。
  - 补充清晰的构造步骤说明（版本号、输入点、输出构造、Locktime、双重哈希签名与序列化组装）。

- [ ] **Step 2: 验证与提交**
  - 检查 Markdown 渲染格式与 Python 代码块有效性。
  - 提交：`git add docs/technical/transaction/raw-transaction-python.md && git commit -m "docs: refactor raw transaction python tutorial"`

---

### Task 2: Phase 3 & 4 区块与协议升级篇重构

**目标文件**：
- 原文件 1：`docs/technical/blockchain/bitcoin-blockchain-part1.md` ➔ `docs/technical/block/genesis-and-blkdat.md`
- 原文件 2：`docs/technical/transaction/bitcoin-transaction-part6.md` ➔ `docs/technical/upgrades/segwit-malleability-history.md`

- [ ] **Step 1: 迁移并精炼创世块与 blk.dat 考古篇**
  - 执行 `git mv docs/technical/blockchain/bitcoin-blockchain-part1.md docs/technical/block/genesis-and-blkdat.md`。
  - H1 标题更名为：`# 区块深度考古：创世区块谜题与 blk.dat 文件解析 (Genesis Block & blk.dat)`。
  - 大幅剪除与基础篇重复的区块头字段定义、PoW 计算公式、高度与最长链定义，加入指向基础篇 `[区块结构](../block.md)` 和 `[区块链总览](../blockchain.md)` 的引导。
  - 重点保留并高亮：
    1. 中本聪 v0.01 源代码考古（`blkindex.dat` 索引缺失导致 50 BTC 无法花费的机理）。
    2. Python 解析磁盘原始 `blk*.dat` 二进制文件的实战代码。
  - 修正图片路径（从 `../../images/...` 调整为 `../../images/...`，确保相对路径有效）。

- [ ] **Step 2: 迁移并精炼隔离见证溯源篇**
  - 执行 `git mv docs/technical/transaction/bitcoin-transaction-part6.md docs/technical/upgrades/segwit-malleability-history.md`。
  - H1 标题更名为：`# 隔离见证深度溯源：从交易延展性危机谈起 (SegWit Malleability & History)`。
  - 剪除口头化免责声明与博客寒暄。
  - 聚焦签名延展性（ECDSA $s$ 与 $N-s$）机理、Mt.Gox 双重提现漏洞与 SegWit 诞生历史。

- [ ] **Step 3: 验证与提交**
  - 检查两个文件的排版、图片链接与代码块。
  - 提交：`git add docs/technical/block/genesis-and-blkdat.md docs/technical/upgrades/segwit-malleability-history.md && git commit -m "docs: refactor genesis block archaeology and segwit history articles"`

---

### Task 3: 侧链与跨链技术演进篇重构

**目标文件**：
- 原文件：`docs/technical/blockchain/bitcoin-blockchain-part2.md`
- 目标文件：`docs/technical/upgrades/sidechains-and-crosschain.md`

- [ ] **Step 1: 迁移并重构侧链篇**
  - 执行 `git mv docs/technical/blockchain/bitcoin-blockchain-part2.md docs/technical/upgrades/sidechains-and-crosschain.md`。
  - H1 标题更名为：`# 侧链与跨链技术演进：从 BitDNS、Namecoin 到 Liquid (Sidechains & Cross-chain)`。
  - 规范化代码块，去除原博客碎片化引言，精炼语言风格。
  - 确保内部技术名词和链接顺畅。

- [ ] **Step 2: 验证与提交**
  - 提交：`git add docs/technical/upgrades/sidechains-and-crosschain.md && git commit -m "docs: relocate and refactor sidechains and crosschain article"`

---

### Task 4: Phase 5 闪电网络专栏全面净化与结构化

**目标目录**：`docs/technical/lightning/`

- [ ] **Step 1: 文件重命名与定位**
  - `git mv docs/technical/lightning/hello-lightning-network-part0.md docs/technical/lightning/lnd-quickstart.md`
  - `git mv docs/technical/lightning/hello-lightning-network-part2.md docs/technical/lightning/rsmc-and-htlc.md`
  - `git mv docs/technical/lightning/hello-lightning-network-part1.md docs/technical/lightning/inbound-capacity.md`
  - `git mv docs/technical/lightning/hello-lightning-network-part3.md docs/technical/lightning/submarine-swaps-loop.md`

- [ ] **Step 2: 深度清洗内容**
  - 在以上 4 个文件中，彻底删除开头一模一样且长达 300 字的博客引言（*“有许多比特币社区的先行者们……”*）。
  - 更新对应 H1 标题：
    - `lnd-quickstart.md`: `# 闪电网络极速入门与 LND 初体验 (LND Quickstart)`
    - `rsmc-and-htlc.md`: `# 核心机制深潜：深度图解 RSMC 与 HTLC (RSMC & HTLC Deep Dive)`
    - `inbound-capacity.md`: `# 真实工程困境：通道入站容量谜题 (Inbound Capacity)`
    - `submarine-swaps-loop.md`: `# 容量破局之道：Loop 潜艇互换机制 (Submarine Swaps & Loop)`
  - 更新 `setup-lightning-node-cheat-sheet.md`、`how-to-close-lightning-channels-by-lnd-cli.md`、`lnd-low-rescan-speed-startup.md`、`eltoo-lightning-offchain-contracts.md`、`lightning-network-gradual-growth.md` 的标题与格式，确保全套风格统一。
  - 修复所有伪表格代码块，还原为 ` ```json `, ` ```bash `。

- [ ] **Step 3: 更新闪电网络目录主页**
  - 重写 `docs/technical/lightning.md`，呈现结构清晰的闪电网络进阶指南。

- [ ] **Step 4: 验证与提交**
  - 提交：`git add docs/technical/lightning/ docs/technical/lightning.md && git commit -m "docs: restructure lightning network section and remove duplicate intros"`

---

### Task 5: 全站导航同步与链接自愈校验

- [ ] **Step 1: 更新全局目录**
  - 更新 `docs/index.md`，同步各 Phase 的新章节名与新路径。
  - 更新 `README.md` 与 `docs/technical/index.md`，确保保持严格一致。

- [ ] **Step 2: 自动化全站链接修复**
  - 编写 Python 脚本扫描 `docs/` 下的所有 Markdown 文件，将所有旧文件名（`bitcoin-transaction-part5.md`、`bitcoin-blockchain-part1.md`、`hello-lightning-network-part*.md` 等）自动更新为新路径。
  - 运行链接有效性校验脚本，检测所有 `[...](...)` 相对路径，确保死链数为 0。

- [ ] **Step 3: 最终审查与提交**
  - 运行 `git diff` 验证所有改动。
  - 提交：`git add docs/ README.md && git commit -m "docs: update site-wide navigation and heal cross-references"`
