# 闪电网络与 Lnd 技术 (Lightning Network)

闪电网络（Lightning Network）是建立在比特币主网之上的二层（Layer 2）状态通道支付协议。它通过在链下建立双向支付通道，实现了秒级确认、近乎零手续费的高频微支付网络，同时依靠比特币主网的密码学与工作量证明保证资金安全。

本专栏系统梳理了从基础认知、核心博弈原理、日常节点运维到前沿协议演进的完整学习路径：

---

## 📚 专栏学习路径

### 1. 演进概览与极速入门
* **[闪电网络的演进与成长之路](lightning/lightning-network-gradual-growth.md)**
  * 回顾从极客命令行体验到全生态繁荣的演化历史，探讨轻节点、钱包形态与去中心化银行愿景。
* **[闪电网络极速入门与 LND 初体验](lightning/lnd-quickstart.md)**
  * 建立闪电网络心智模型，手把手在测试网搭建 LND 节点，开辟首条通道并完成第一笔即时支付。

### 2. 核心密码学与博弈机制
* **[核心机制深潜：深度图解 RSMC 与 HTLC](lightning/rsmc-and-htlc.md)**
  * 深入剖析序列到期可撤销合约（RSMC）的非对称承诺与违约惩罚闭环，推导哈希时间锁合约（HTLC）的多跳路由原理。

### 3. 流动性挑战与破局方案
* **[真实工程困境：通道入站容量谜题](lightning/inbound-capacity.md)**
  * 拆解通道沙漏模型（本地余额 vs 远程余额），剖析为何新通道无法收款以及商家的入站流动性瓶颈。
* **[容量破局之道：Loop 潜艇互换机制](lightning/submarine-swaps-loop.md)**
  * 深度解析 Lightning Labs Loop 与非托管潜艇互换（Submarine Swaps），实现链上与链下资金的自由呼吸调度。

### 4. 节点搭建与日常运维
* **[闪电网络节点搭建与配置小抄](lightning/setup-lightning-node-cheat-sheet.md)**
  * 汇总 Bitcoin Core、LND、Core Lightning (CLN) 与 Lightning Charge 的核心配置文件与常用 CLI 指令速查。
* **[运维实战：如何通过 lncli 安全关闭闪电通道](lightning/how-to-close-lightning-channels-by-lnd-cli.md)**
  * 区分协作关闭（Cooperative Close）与强制关闭（Force Close）的操作要点与避坑指南。
* **[运维实战：排查 LND 启动扫描慢问题](lightning/lnd-low-rescan-speed-startup.md)**
  * 分析 LND 冷启动区块重扫迟缓的根因与 I/O 调优方案。

### 5. 未来前沿协议
* **[未来前沿：Eltoo 离线契约更新机制](lightning/eltoo-lightning-offchain-contracts.md)**
  * 探讨摆脱惩罚机制包袱的下一代通道更新协议 Eltoo、`SIGHASH_ANYPREVOUT` 与多方通道工厂。
