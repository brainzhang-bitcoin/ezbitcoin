<img src="../../images/icons_loader-2.svg" alt="Loading Tool" style="height:32px; width:32px;" />

[<img src="../../images/diagrams_png_block-time.png" alt="Diagram showing the location of the time field inside the block header." width="609" height="291" />](../../images/diagrams_png_block-time.png)

[区块头](../block.md#header)中的 time 字段指示了**区块被创建的粗略时间**。

矿工在构建其[候选区块](../mining/candidate-block.md)时，会将当前时间存入区块头。它包含一个 Unix 时间戳 (Unix Timestamp，即自 1970 年 1 月 1 日以来的秒数)，这是计算机程序通常用来存储特定时间点的形式。

例如，[创世区块](/explorer/block/000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f)包含时间戳 1231006505，代表日期 *2009 年 1 月 3 日 18:15:05*。

Unix 时间

0d

当前

日期

0 秒

## 区块顺序

区块时间是否影响区块的顺序？

时间戳**不会**影响[区块链](../blockchain.md)中区块的顺序。

事实上，一个区块的时间戳完全有可能早于它所构建在其上的区块。例如：

* 区块 [790,402](/explorer/790402#blockchain) = 2023 年 5 月 19 日 04:22（比[前一个区块](previous-block.md)“早”了 2 分钟）
* 区块 [790,401](/explorer/790401#blockchain) = 2023 年 5 月 19 日 04:24

另一个特别极端的例子是 2011 年的一个区块，其时间比前一个区块“早”了近 2 个小时：

* 区块 [156,114](/explorer/156114#blockchain) = 2011 年 12 月 5 日 06:17（比前一个区块“早”了 1 小时 59 分钟）
* 区块 [156,113](/explorer/156113#blockchain) = 2011 年 12 月 5 日 08:16

因此，尽管时间戳通常相当准确，但有时区块并不是按“时间顺序”排列的，这完全没有问题。

每个区块的时间戳通常非常接近当前时间，但您不应该依赖它们 100% 正确。您会发现“乱序”的区块每个月都会在区块链中出现几次，所以这并不算罕见。

## 要求

区块时间的最大和最小值是多少？

[<img src="../../images/diagrams_png_block-time-range.png" alt="Diagram showing the valid time range that can be placed in the block header." width="355" height="639" />](../../images/diagrams_png_block-time-range.png)

时间戳必须在特定范围内才有效：

* 它必须**大于前 11 个区块的中间时间**（即在其下方第 6 个区块处的时间）。
* 它必须**小于[网络调整时间](#network-adjusted-time) +2 小时**。

因此，时间戳的确定具有一定的弹性。对于任何新挖掘出的区块，time 字段可以在实际当前时间的 -1 到 +2 小时（粗略计算）内，并且它仍然是有效的。

这种弹性允许节点的本地时间设置不准确（例如由于[夏令时](https://en.wikipedia.org/wiki/Daylight_saving_time)导致的误差），并包容了跨网络传输区块时的延迟。

将范围限定在前 11 个区块的中间时间到未来的 +2 小时之间并没有严格的数学依据。它们是中本聪在编写第一版比特币代码时选择的“足够好”的数值，我们今天仍然在使用它们。

> 这两小时的规则真的很奇怪。它是唯一一个不基于区块链数据而是基于本地数据的“共识”规则。
> 
> John Newbery, [Bitcoin Core PR Review Club (Jun 19, 2019)](https://bitcoincore.reviews/15481)

### 网络调整时间

[本地节点](/explorer/):

本地计算机时间:   2026 年 7 月 3 日 09:18:09

网络调整时间: 2026 年 7 月 3 日 08:56:35 (-21 分 34 秒)

网络调整时间是您的本地时间加上您所连接的所有节点的中间偏移量。

[<img src="../../images/diagrams_png_networking-network-adjusted-time.png" alt="Diagram showing the network average time being calculated based on the timestamps sent by connected nodes" width="786" height="404" />](../../images/diagrams_png_networking-network-adjusted-time.png)

节点在相互[连接](../networking.md)时，会发送其本地时间的 UTC 时间戳。

例如：

```
Local Time = 1685010124

Connected Nodes:
  Node 1     = 1685010121 (-3 seconds)
  Node 2     = 1685010122 (-2 seconds)
  Node 3     = 1685010122 (-2 seconds)
  Node 4     = 1685010125 (+1 second)
  Node 5     = 1685010125 (+1 second)
  Node 6     = 1685010127 (+3 seconds)
  Node 7     = 1685010128 (+3600 seconds)
  Median Offset = +1 second

Network Adjusted Time = 1685010125

Note: This is just a quick example.  
Nodes are usually connected to more than 7 peers at a time.
```

我们使用网络调整时间的原因是去中心化网络上的计算机很难就当前的确切时间达成一致。

网络调整时间允许节点在它们之间商定一个时间，同时限制任何单个节点操纵“当前”商定时间的能力。

#### 网络调整时间 Bug

在 [timedata.cpp](https://github.com/bitcoin/bitcoin/blob/26.x/src/timedata.cpp) 中，网络调整时间的计算存在一个众所周知的 [Bug](https://github.com/bitcoin/bitcoin/issues/4521)。

基本上，如果您有一个长期运行的节点，在发生 199 次连接后，您的节点将“卡”在基于前 199 次连接的中间偏移量上，因为任何后续连接都不会在中间偏移量计算中被注册。

然而，[ Gregory Maxwell 表示](https://github.com/bitcoin/bitcoin/pull/4526#issuecomment-49115517)，此 Bug 保护了节点免受其他类型的攻击，因此它是有意未被修复的。

## 用途

区块头中的 time 字段是用于做什么的？

除了作为区块挖掘出的大致时间指标外，区块的时间戳在比特币中还有其他几个用途：

### 目标重新计算

[<img src="../../images/diagrams_png_target-period.png" alt="Diagram showing a target recalculation based on the time between the last 2015 blocks." width="983" height="189" />](../../images/diagrams_png_target-period.png)

区块头中的时间戳用于计算在 2016 个区块的周期内，区块的挖掘速度是快于还是慢于预期，并据此调整[target](../mining/target.md)。

<img src="../../images/icons_tool.svg" alt="Tool Icon" style="width:20px; height:20px" /> 目标调整 (Target Adjustment)

上一次调整
当前目标

0x

`0 bytes`


时间 (秒)

实际

0d

预期

0d

目标调整周期为 2016 个区块。一个区块平均每 600 秒（10 分钟）开采一次，因此预期时间为 2016 \* 600 = 1209600 秒。

比例

实际时间除以预期时间。我们将当前目标乘以该比例以获得新目标。

新目标 (全精度)

0x

新目标

0x

`0 bytes`

注意：此目标值已被轻微截断，以便存储在区块头的 bits 字段中，而这正是挖矿时实际使用的目标值。



0 秒

### 交易锁定时间 (Transaction Locktime)

[<img src="../../images/diagrams_png_transaction-locktime.png" alt="Diagram showing the locktime being used to prevent a transaction being mined until a specific time in the future." width="722" height="336" />](../../images/diagrams_png_transaction-locktime.png)

交易可以包含特定的 [locktime](../transaction/locktime.md)，以防止在它小于区块头中有效 time 字段的设定之前被挖掘到区块中。

## 注意事项

* **交易不包含时间戳。** 原始交易不包含时间戳字段。要弄清楚交易有多“旧”，您必须找到包含该交易的区块并从中获取时间戳。或者，您可以手动跟踪您的节点第一次从网络上的另一个节点接收到该交易的时间（这正是 Bitcoin Core 所做的，也是为什么您在运行 `bitcoin-cli getmempoolentry [txid]` 时可以看到交易的“时间”的原因，但该信息仅会临时存储）。

## 资源

* [From where does the 2 hours limitation on bitcoin time stamp come?](https://bitcoin.stackexchange.com/questions/77755/where-does-the-2-hour-limit-on-the-timestamp-come-from)
* [Why don't the timestamps in the block chain always increase?](https://bitcoin.stackexchange.com/questions/915/why-dont-the-timestamps-in-the-block-chain-always-increase)
* [mediantime.go](https://github.com/btcsuite/btcd/blob/master/blockchain/mediantime.go) – Bitcoin 的 btcd 实现中，用于*网络调整时间*计算的源代码。包含极好的注释。