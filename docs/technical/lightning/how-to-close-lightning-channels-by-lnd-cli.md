# 运维实战：如何通过 lncli 安全关闭闪电通道 (Closing Channels via CLI)

在日常运营 LND 节点时，关闭通道（Close Channel）是一个基础但极其容易踩坑的常见操作。

---

## 1. 关闭通道核心命令

关闭通道需要指定注资输出的 `channel_point`（即 `funding_txid:vout_index`）：

```bash
lncli closechannel <funding_txid> <funding_tx_vout>
```

> **注意**：切记必须附带 `funding_tx_vout`（通常为 `0` 或 `1`）。如果只传 txid 而遗漏了输出索引号，LND 会直接报错 `channel not found`。

---

## 2. 协作关闭 vs 强制关闭

### 1. 协作关闭 (Cooperative Close)
如果对端节点在线且正常响应，默认执行协作关闭：双方协商构建一笔链上互惠交易，将各自资金全额退回，耗时仅需几个区块确认。

### 2. 强制关闭 (Force Close)
当对端节点长期离线、宕机或拒绝合作时，若需要单方面赎回本地资金，可追加 `--force` 参数：

```bash
lncli closechannel --force <funding_txid> <funding_tx_vout>
```

> **风险警示**：强制关闭会触发 RSMC 相对时间锁机制，你的本地余额会被冻结若干个区块（如 144 ~ 2016 个区块，约 1 天至两周不等）以等待挑战期过去，且链上手续费通常更高。非紧急情况下应尽量优先采用协作关闭。
