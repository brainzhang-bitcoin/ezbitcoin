# 设计规格说明书：导入博文重构与全书体系深度融合 (Design Spec)

- **日期**：2026-10-07
- **状态**：已批准 (Approved)
- **目标**：重构并精炼从博客导入的系列文章，消除与原版教程基础内容的重复与割裂感，将其重塑为与全书主线深度融合的“进阶专题与实战工坊”，全面提升教程的连贯性、生动性与专业度。

---

## 1. 现状背景与核心痛点

本项目集合了两个优质内容源：
1. **基础图解教程**：译自知名极简教学项目 [Learn Me A Bitcoin](https://learnmeabitcoin.com/)，结构严密，侧重于协议字段图解、基础概念由浅入深的阐释。
2. **作者原创深度博文**：来自 [brainz.fun](https://brainz.fun/)，具有极高的实战价值，包含纯手工字节级交易构造、Satoshi v0.01 源码考古、交易延展性与 Mt.Gox 危机解析、闪电网络工程实操等。

### 当前痛点
1. **标题生硬割裂**：博文保留了原博客的连载标题（如“比特币的交易-5”、“比特币的blockchain-1/2”、“Hello Lightning Network -0/1/2/3”），读者在本书中无法找到前序篇章，阅读体验突兀。
2. **概念大量重复**：博文前半段往往花费大量篇幅重复科普区块链、交易结构、PoW 等基础概念，与书中已有的系统化基础章节存在大量重叠。
3. **格式与引言残留**：原博文多篇开头包含一模一样的数百字博客寒暄，部分代码块因当初 HTML 转 Markdown 缺陷被嵌套在单列表格中，影响阅读。
4. **分类错位**：如讲述“侧链与跨链”的博文被挂在基础区块链目录下（`bitcoin-blockchain-part2.md`），讲述“延展性危机与隔离见证起源”的博文被孤立在交易目录下（`bitcoin-transaction-part6.md`）。

---

## 2. 总体架构设计：【进阶专题与实战工坊】

采用矩阵式融合策略：**保留原创深度实战与源码考古，剪除重复铺垫与博客套话，重塑主题式标题，按知识归属回填到技术指南 5 大阶段**。

```
┌────────────────────────────────────────────────────────┐
│                      EzBitcoin 教程体系                 │
├──────────────────────────┬─────────────────────────────┤
│   基础理论与协议结构图解   │    进阶专题与极客实战工坊     │
│  (Learn Me A Bitcoin)    │     (Curated Deep Dives)    │
├──────────────────────────┼─────────────────────────────┤
│ Phase 1: 基础工具箱      │                             │
│ Phase 2: 构建交易        │ 实战：Python 手工构造裸交易   │
│ Phase 3: 广播与共识      │ 考古：创世块谜题与 blk.dat  │
│ Phase 4: 账本与演进      │ 深度：从延展性危机看 SegWit  │
│ Phase 5: 二层网络与扩展  │ 侧链演进 + 闪电网络工程专栏 │
└──────────────────────────┴─────────────────────────────┘
```

---

## 3. 文件重命名与目录映射矩阵 (Mapping Matrix)

### 3.1 Phase 2: 构建交易 (Constructing the Transaction)
* **原文件**：`docs/technical/transaction/bitcoin-transaction-part5.md`
* **新文件**：`docs/technical/transaction/raw-transaction-python.md`
* **新标题**：`# 实战：用 Python 手工构造并签署裸交易 (Constructing Raw Transaction)`
* **定位**：紧随 `psbt.md` 之后，作为交易构建章节的压轴动手实战篇。

### 3.2 Phase 3 & 4: 区块、共识与演进 (Blocks, Consensus & Evolution)
* **原文件**：`docs/technical/blockchain/bitcoin-blockchain-part1.md`
* **新文件**：`docs/technical/block/genesis-and-blkdat.md`（移入 `block/` 目录）
* **新标题**：`# 区块深度考古：创世区块谜题与 blk.dat 文件解析 (Genesis Block & blk.dat)`
* **定位**：紧随 `blkdat.md` 之后，承接原始区块文件话题，深挖 Satoshi v0.01 源码考古与 Python 二进制解析。

* **原文件**：`docs/technical/transaction/bitcoin-transaction-part6.md`
* **新文件**：`docs/technical/upgrades/segwit-malleability-history.md`（移入 `upgrades/` 目录）
* **新标题**：`# 隔离见证深度溯源：从交易延展性危机谈起 (SegWit Malleability & History)`
* **定位**：放置在 `upgrades/segregated-witness.md` 之后，讲解延展性攻击历史和 SegWit 诞生的前因后果。

### 3.3 Phase 5: 二层网络与扩展技术 (Layer 2 & Scaling)
将原“二层扩展”升级为**二层网络与扩展技术**体系，下设“侧链与跨链”与“闪电网络专栏”：

* **侧链与扩展技术**：
  * **原文件**：`docs/technical/blockchain/bitcoin-blockchain-part2.md`
  * **新文件**：`docs/technical/upgrades/sidechains-and-crosschain.md`
  * **新标题**：`# 侧链与跨链技术演进：从 BitDNS、Namecoin 到 Liquid (Sidechains & Cross-chain)`
* **闪电网络专栏 (Lightning Network)**：
  * `docs/technical/lightning/lightning-network-gradual-growth.md`
    * 标题：`# 闪电网络的演进与成长之路 (Evolution of Lightning Network)`
  * `docs/technical/lightning/hello-lightning-network-part0.md` ➔ `docs/technical/lightning/lnd-quickstart.md`
    * 标题：`# 闪电网络极速入门与 LND 初体验 (LND Quickstart)`
  * `docs/technical/lightning/hello-lightning-network-part2.md` ➔ `docs/technical/lightning/rsmc-and-htlc.md`
    * 标题：`# 核心机制深潜：深度图解 RSMC 与 HTLC (RSMC & HTLC Deep Dive)`
  * `docs/technical/lightning/hello-lightning-network-part1.md` ➔ `docs/technical/lightning/inbound-capacity.md`
    * 标题：`# 真实工程困境：通道入站容量谜题 (Inbound Capacity)`
  * `docs/technical/lightning/hello-lightning-network-part3.md` ➔ `docs/technical/lightning/submarine-swaps-loop.md`
    * 标题：`# 容量破局之道：Loop 潜艇互换机制 (Submarine Swaps & Loop)`
  * `docs/technical/lightning/setup-lightning-node-cheat-sheet.md`
    * 标题：`# 闪电网络节点搭建与配置小抄 (Node Setup Cheat Sheet)`
  * `docs/technical/lightning/how-to-close-lightning-channels-by-lnd-cli.md`
    * 标题：`# 运维实战：如何安全关闭闪电通道 (Closing Channels via CLI)`
  * `docs/technical/lightning/lnd-low-rescan-speed-startup.md`
    * 标题：`# 运维实战：排查 LND 启动扫描慢问题 (LND Rescan Troubleshooting)`
  * `docs/technical/lightning/eltoo-lightning-offchain-contracts.md`
    * 标题：`# 未来前沿：Eltoo 离线契约更新机制 (Eltoo Offchain Contracts)`

---

## 4. 内容精炼与清洗规范 (Content Pruning & Refactoring)

### 4.1 通用清洗标准
1. **剔除博客连载寒暄**：彻底清理开篇诸如“在上一篇博客中”、“我们之前写文章评价道……”等博文套话，开门见山。
2. **规范化代码块**：将从 HTML 继承的单列带行号表格（`| ``` 1 2 3 ``` | ``` code ``` |`）转换为标准 GFM 代码块（` ```python `, ` ```json `, ` ```bash `）。
3. **自愈内链**：将外部原博客链接（如 `https://brain-zhang.github.io/blog/...`）重写为当前书籍内部的相对 Markdown 链接。

### 4.2 核心篇章精炼细则
* **`raw-transaction-python.md`**：
  * 去除对不存在的“交易-3”的口头依赖，设置独立明确的参数前置假设。
  * 保留从版本号、输入、输出、LockTime、双重 SHA256 到私钥 ECDSA 签名及序列化的完整 Python 代码。
* **`genesis-and-blkdat.md`**：
  * 大幅删减对区块头（version, prev_hash, merkle_root, bits, nonce）、PoW、最长链的重复定义，以一行链接引导至基础篇。
  * 浓墨重彩展现中本聪 v0.01 源代码剖析：为什么创世块 50 BTC 没被索引导致不可花费。
  * 完整保留 Python 解析磁盘二进制原始 `blk*.dat` 文件的实操。
* **`segwit-malleability-history.md`**：
  * 删除口语化免责声明，以权威技术视点剖析签名延展性。
  * 详细推导 ECDSA $(r, s)$ 与 $(r, N - s)$ 带来的签名可变性及 TXID 变异风险。
  * 详细讲解 Mt.Gox 面临的双重提现攻击，推导 BIP62/BIP66 和 SegWit 的必然性。
* **闪电网络系列**：
  * 消除 4 篇文章开头重复的 300 字引言。
  * 将 `rsmc-and-htlc.md` 打造为核心机制专篇，重点呈现 Funding Tx、Commitment Tx、撤销交付与违约惩罚（Breach Remedy）的博弈推导。
  * 将 `inbound-capacity.md` 与 `submarine-swaps-loop.md` 组织为前后衔接的“问题-解法”叙事。

---

## 5. 导航与全局集成 (Navigation & Global Integration)

### 5.1 目录更新
同步更新：
1. `docs/index.md`
2. `README.md`
3. `docs/technical/index.md`
4. `docs/technical/lightning.md`

### 5.2 链接自愈保障
通过自动化脚本遍历全站 Markdown 文件，确保所有指向旧文件名的引用自动重定向至新文件名，并在 CI/本地校验中保证相对路径有效率 100%。

---

## 6. 验证与验收标准 (Acceptance Criteria)

1. **结构完整性**：所有旧博文无孤立残留，新文件均正确定位于指定目录。
2. **内容质量**：
   * 所有篇章均已移除重复博客开头与口头化引言。
   * 无损坏的 HTML 假表格代码块，代码格式标准且可读。
3. **导航与链接**：
   * `docs/index.md`、`README.md`、`docs/technical/index.md`、`docs/technical/lightning.md` 目录与文件系统 100% 对应。
   * 运行链接校验脚本，全站 Markdown 相对链接零 404 死链。
