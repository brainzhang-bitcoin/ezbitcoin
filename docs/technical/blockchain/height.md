<img src="../../images/icons_loader-2.svg" alt="Loading Tool" style="height:32px; width:32px;" />

[<img src="../../images/diagrams_png_blockchain-height.png" alt="Diagram showing the height of a block in the blockchain as its distance from the genesis block." width="329" height="622" />](../../images/diagrams_png_blockchain-height.png)

当前高度:

[956,479](/explorer/956479#blockchain)

注意：这是处于区块链尖端（tip）的区块高度。

[区块](../block.md)的高度指示了它在**[区块链](../blockchain.md)中的位置**。

它是根据其与*创世区块*的距离计算出来的。

**计数从零开始。** 因此，区块链中的第一个区块（创世区块）是[区块 0](/explorer/0#blockchain)。

## 用途

区块高度在比特币中如何使用？

在比特币中，有**两个重大的调整**会在*特定的高度间隔*发生。

### 1. 目标调整 (Target Adjustment)

2,016 个区块

[<img src="../../images/diagrams_png_blockchain-height-target.png" alt="Diagram showing the target adjustment taking place on every 2016th block." width="314" height="524" />](../../images/diagrams_png_blockchain-height-target.png)

| | |
| --- | --- |
| 下一次调整 | 957,600 (还有 1,121 个区块) |
| 当前高度 | 956,479 |

[target](../mining/target.md)每隔 2,016 个区块（大约每 2 周）进行一次调整。

随着时间的推移，当[矿工](../mining.md)加入和离开网络时，这有助于保持**区块之间 10 分钟的时间间隔**。

例如，第一次目标调整发生在区块高度 [2,016](/explorer/2016#blockchain)，第二次发生在高度 [4,032](/explorer/4032#blockchain)，第三次发生在高度 [6,048](/explorer/6048#blockchain)，依此类推。

### 2. 区块补贴减半 (Block Subsidy Halving)

210,000 个区块

[<img src="../../images/diagrams_png_blockchain-height-halving.png" alt="Diagram showing the block subsidy halving on every 210,000th block." width="378" height="740" />](../../images/diagrams_png_blockchain-height-halving.png)

| | |
| --- | --- |
| 下一次减半 | 1,050,000 (还有 93,521 个区块) |
| 当前高度 | 956,479 |

[区块补贴](../mining/block-reward.md#block-subsidy)每隔 210,000 个区块（大约每 4 年）减半一次。

区块补贴的这种减半正是对比特币创建了**固定供应量**的机制，因为最终补贴将达到零，不会再发行新的比特币。

例如，区块补贴开始时为 **50 BTC**。然后，在区块高度 [210,000](/explorer/210000#blockchain) 处，它减半为 **25 BTC**，在区块高度 [420,000](/explorer/420000#blockchain) 处减半为 **12.5 BTC**，依此类推。在区块高度 6,930,000 处（在总共进行了 33 次[减半](../mining/block-reward.md#halving-table)之后），补贴将达到**零**。

### 其他用途

*高度*在比特币的其他几个地方也有使用，主要是为了判定[交易](../transaction.md)是否符合被挖掘的资格：

#### 锁定时间 (Locktime)

[<img src="../../images/diagrams_png_transaction-locktime.png" alt="Diagram showing how the locktime field can be used to prevent a transaction from being mined until a specific block height or time in the future." width="722" height="336" />](../../images/diagrams_png_transaction-locktime.png)

[locktime](../transaction/locktime.md) 字段可以用来**阻止交易在达到特定高度*之前*被挖掘**。

例如，如果您对一笔交易设置了 **500,000** 的 locktime，那么该交易只能被挖掘到高度为 **500,001** 或以上的区块中。

#### 相对锁定时间 (Relative Locktime)

[<img src="../../images/diagrams_png_transaction-sequence-relative-locktime.png" alt="Diagram showing the sequence field being used to set a relative locktime on the transaction." width="741" height="336" />](../../images/diagrams_png_transaction-sequence-relative-locktime.png)

[相对锁定时间](../transaction/input/sequence.md#relative-locktime)可以用来阻止一笔交易被挖掘，直到它所消费的[输出](../transaction/output.md)在区块链中达到了一定的*深度*。

例如，如果您在一笔消费区块 **500,000** 中交易输出的交易[输入](../transaction/input.md)上设置了 **100** 个区块的相对锁定时间，那么该交易只能被挖掘到高度为 **500,101** 或以上的区块中。

#### Coinbase 交易

[<img src="../../images/diagrams_png_blockchain-height-coinbase-transaction.png" alt="Diagram showing the height of the current block being included inside the coinbase transaction for that block." width="329" height="437" />](../../images/diagrams_png_blockchain-height-coinbase-transaction.png)

从区块 [227,836](/explorer/227836#blockchain) 开始，所有 [Coinbase](../mining/coinbase-transaction.md) 交易**都必须包含其即将被挖掘进去的区块高度**。

这强迫每个 Coinbase 交易都拥有唯一的 [TXID](../transaction/input/txid.md)，因为在此之前，不同区块中的 Coinbase 交易完全可能拥有[相同的 TXID](../transaction/input/txid.md#duplicate)。

## 引用

区块高度是区块的唯一标识符吗？

*高度* **不能保证是区块的唯一标识符**。

在[挖矿](../mining.md)过程中，有可能两个区块被同时挖出。因此，可能会有两个不同的区块在区块链中竞争相同的高度：

[<img src="../../images/diagrams_png_blockchain-height-competing.png" alt="Diagram showing two blocks competing for the same height at the top of the blockchain." width="477" height="630" />](../../images/diagrams_png_blockchain-height-competing.png)

这是比特币运作方式的正常部分。

因此，根据哪一个区块先被在其上进行后续构建，占据链尖端附近高度的区块有可能发生改变：

[<img src="../../images/diagrams_png_blockchain-height-competing-chain-reorganization.png" alt="Diagram showing a different block occupying a specific height in the blockchain after a chain reorganization." width="457" height="660" />](../../images/diagrams_png_blockchain-height-competing-chain-reorganization.png)

这被称为[区块重组](chain-reorganization.md)。

因此，虽然高度通常是引用区块链中区块的有用方法，但在引用*特定区块*时，它并不总是可靠的，尤其是当该区块接近区块链的尖端时。

* **[区块哈希](../block/hash.md)是引用区块最可靠的方法。** 区块哈希总是引用一个特定的区块，而高度更像是一个*描述符*，而不是一个唯一的标识符。
* **区块沉淀得越深，高度就越可靠。** 如果一个区块在区块链中达到了 3 个以上的区块深度，那么它因为[区块重组](chain-reorganization.md)而被替换的可能性极小。

## 命令

### `bitcoin-cli getblockcount`

此命令返回区块链当前的**高度**。

```
$ bitcoin-cli getblockcount
956479
```

当前区块链的高度为 956,479。但由于计数是从*零*开始的，所以从技术上讲，区块链中总共有 956,480 个区块。这并不是一个特别有用的事实，但我还是想顺便提一下。

### `bitcoin-cli getblockhash [height]`

此命令返回区块链中特定高度的区块哈希。

```
$ bitcoin-cli getblockhash 956479
000000000000000000005af9d7cca01756b552b02e5f5fac6422864439807264
```

如前所述，高度在引用区块链尖端附近的区块时是不可靠的。例如，如果您使用 `bitcoin-cli getblockhash 956479` 获取当前链顶端区块的区块哈希，如果发生了[区块重组](chain-reorganization.md)，结果可能会发生改变。

如果您的节点在同一高度持有多个区块，此命令将返回属于当前[最长链](longest-chain.md)的区块的区块哈希。如果您的链尖端有多个区块，您的节点会将它接收到的*第一个*区块视为当前最长链的一部分（但同样，如果发生区块重组，这很容易发生改变）。

### `bitcoin-cli getblockheader [hash]`

此命令提供关于区块的基本信息，包括其高度。

```
$ bitcoin-cli getblockheader 000000000000000000005af9d7cca01756b552b02e5f5fac6422864439807264
{
    "hash": "000000000000000000005af9d7cca01756b552b02e5f5fac6422864439807264",
    "confirmations": 1,
    "height": 956479,
    "version": 537010176,
    "versionHex": "20022000",
    "merkleroot": "ef0e0162fee593e41fe2c14d89a19046d706178ae5cf69956c3ff5ca87ca45cf",
    "time": 1783070289,
    "mediantime": 1783068995,
    "nonce": 3263904042,
    "bits": "17021a42",
    "target": "000000000000000000021a420000000000000000000000000000000000000000",
    "difficulty": 133869853540305.4,
    "chainwork": "000000000000000000000000000000000000000134d0e337eef3b345d0a8d660",
    "nTx": 6825,
    "previousblockhash": "000000000000000000000af753580e7b7bd555102cfbe9c72b4b625dbd3f48d8"
}
```

## 总结

高度用于引用在区块链中占据特定位置的区块。

但是，您最好还是使用[区块哈希](../block/hash.md)来可靠地引用区块，因为区块链尖端附近的区块可能会由于[区块重组](chain-reorganization.md)而发生改变。

然而，一旦区块达到 3 个或更多的区块深度，它就不太可能被另一个区块替换，高度也就足以作为唯一的标识符使用。不过，如果可以的话，使用区块哈希仍然是更安全的做法。