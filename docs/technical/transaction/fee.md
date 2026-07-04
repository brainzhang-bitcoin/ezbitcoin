<img src="../../images/icons_loader-2.svg" alt="Loading Tool" style="height:32px; width:32px;" />

[<img src="../../images/diagrams_png_transaction-fee.png" alt="Diagram showing the transaction fee as the remainder of the amount being sent." width="321" height="329" />](../../images/diagrams_png_transaction-fee.png)

交易手续费（transaction fee）是**交易中的剩余部分**。

如果你将所有 [input](input.md) 的数值相加，并减去所有 [output](output.md) 的数值，剩下的金额就是手续费。例如：

交易：[82b81a39d1b6bff8366eab2297f61db7ac34b7d901f5cfc40143ca704ded980e](/explorer/tx/82b81a39d1b6bff8366eab2297f61db7ac34b7d901f5cfc40143ca704ded980e)

```
input  0 = 2699815 satoshis

output 0 = 1593900 satoshis
output 1 = 1060915 satoshis

fee      =   45000 satoshis
```

如你所见，交易中并没有专门的“手续费”输出或类似的内容。手续费只是你在交易中没有用完的代币金额。

请务必小心，因为交易中留下的*任何*数量的 satoshis 都会被视作手续费。由于错误估算输出大小，有些人曾错误地在交易中设置了极高的手续费。例如，交易 [cc455ae816e6cdafdb58d54e35d4f46d860047458eacf1c7405dc634631c570d](/explorer/tx/cc455ae816e6cdafdb58d54e35d4f46d860047458eacf1c7405dc634631c570d) 中包含 291.240900 BTC 的手续费。

## 矿工激励

为什么要在交易中设置手续费？

交易手续费为[矿工](../mining.md)将你的交易包含在他们的[候选区块](../mining/candidate-block.md)中提供了**激励**。

这是因为矿工可以通过 [Coinbase](../mining/coinbase-transaction.md) 交易收集他们打包在区块中的所有交易手续费（如果他们能成功地将该区块开采到[区块链](../blockchain.md)上）。

[<img src="../../images/diagrams_png_block-coinbase-transaction.png" alt="Diagram showing transaction fees being collected by a miners via the coinbase transaction." width="655" height="329" />](../../images/diagrams_png_block-coinbase-transaction.png)

因此，如果[内存池](../mining/memory-pool.md)中的交易数量超出了下一个区块能容纳的范围，矿工就会选择用可获得的手续费最高的交易填满他们的候选区块。这能最大化他们在挖出区块时可以领取的比特币数量。

[<img src="../../images/diagrams_png_transaction-fee-miner-incentive.png" alt="Diagram showing the a miner selecting the highest-fee transactions from the memory pool for inclusion in their candidate block." width="752" height="435" />](../../images/diagrams_png_transaction-fee-miner-incentive.png)

因此，在你的交易中设置手续费允许你**与其他交易竞争下一个区块中的空间**。通常来说：

* 手续费越高，你的交易就会越快被打包挖出。
* 手续费越低，你的交易被打包挖出所需的时间就越长。

如果内存池中的所有交易都能装入下一个区块中，你只需在交易中设置 *[最低限制](#minimum-relay-fee)* 手续费即可，因为此时没有进入下一个区块的竞争。

## 费率

交易手续费是如何衡量的？

矿工希望从其区块中获得最大化的手续费。为了实现这一目标，他们会根据每笔交易提供的费用**与其在区块中占用的空间大小**来衡量交易。

例如，一笔手续费较高的小额交易，比一笔手续费相同但体积较大的交易对矿工而言更有价值。

[<img src="../../images/diagrams_png_transaction-fee-rate-basics.png" alt="Diagram showing the two separate transaction with the same size fee, but one is larger than the other so has a lower fee/byte." width="688" height="325" />](../../images/diagrams_png_transaction-fee-rate-basics.png)

因此，在比较交易费用时，我们会将**手续费大小**除以**交易大小**（根据交易在区块中占用的空间计算）。这被称为*费率（feerate）*，它允许我们对比交易，以找出哪些交易对矿工来说更具价值。

* *费率* 越高，你的交易就越快被挖出。
* *费率* 越低，你的交易就越难被挖出。

有 3 种不同的方法来衡量费率：

1. [sats/byte](#satsbyte) (已弃用)
2. [sats/wu](#satswu) (内部使用)
3. [sats/vbyte](#satsvbyte) (最常见)

### sats/byte

[<img src="../../images/diagrams_png_transaction-fee-rate-sats-per-byte.png" alt="Diagram showing the sats/byte feerate calculation as the fee divided by the number of bytes in the transaction." width="627" height="257" />](../../images/diagrams_png_transaction-fee-rate-sats-per-byte.png)

区块限制曾经是 **1,000,000 字节** (1 MB)。

因此，交易对矿工的价值自然是以**每字节多少聪**（或简称为 **sats/byte**）来衡量的。

然而，自 [SegWit](../upgrades/segregated-witness.md) 升级（[BIP 141](https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki)）以来，我们现在使用一种新的 *重量* 测量方法来确定区块中可以容纳多少笔交易……

### sats/wu

[<img src="../../images/diagrams_png_transaction-fee-rate-sats-per-weight-unit.png" alt="Diagram showing the sats/wu feerate calculation as the fee divided by the number of weight units in the transaction." width="703" height="312" />](../../images/diagrams_png_transaction-fee-rate-sats-per-weight-unit.png)

[区块限制](../block.md#weight)现在是 **4,000,000 重量单位 (weight units)**。

交易的大小现在根据其[重量](size.md#weight)来衡量，这会将大多数交易数据的体积乘以 4。然而，新的 [witness](witness.md) 数据会乘以 1，这相当于相对于交易的其他部分给予了折扣。

因为现在的区块有最大 *重量* 限制，矿工会以**每重量单位聪数**（或简称为 **sats/wu**）来衡量交易的费率。

但是，此 **sats/wu** 采用的是与旧的 **sats/byte** 测量不同的刻度。因此，为了与仍在使用 **sats/byte** 的旧软件保持向后兼容性，我们有了最后一种费率度量方法……

### sats/vbyte

[<img src="../../images/diagrams_png_transaction-fee-rate-sats-per-vbyte.png" alt="Diagram showing the sats/vbyte feerate calculation as the fee divided by the number of virtual bytes in the transaction, which is the weight divided by 4." width="605" height="310" />](../../images/diagrams_png_transaction-fee-rate-sats-per-vbyte.png)

如果将 4,000,000 重量单位的区块限制除以 4，你将得到 **1,000,000 虚拟字节 (virtual bytes)**。

同样地，如果将交易的重量也除以 4，你将回到几乎与之前相同的 **sats/byte** 度量标准。但现在，每字节 witness 数据仅算作 0.25 字节，这就是我们将该度量标准称为[虚拟字节](size.md#vbytes)而非实际字节的原因。

**sats/vbyte** 测量意味着较新的 [SegWit](../transaction.md#example-segwit) 交易费率保持与旧版交易按 **sats/byte** 测量的费率一致。例如：

旧版交易：[a04c291e586b10f6db4d38bcba414dea2fd39d53745763d13c49026af1f09262](/explorer/tx/a04c291e586b10f6db4d38bcba414dea2fd39d53745763d13c49026af1f09262)

```
fee:          15977 sats

size:         223 bytes
virtual size: 223 vbytes

sats/byte:    72
sats/vbyte:   72
```

SegWit 交易：[7169e93ede0096c32e4fb90f267ea29fb539324cfc3927ea9ded9066b879a1e8](/explorer/tx/7169e93ede0096c32e4fb90f267ea29fb539324cfc3927ea9ded9066b879a1e8)

```
fee:          10317 sats

size:         226 bytes
virtual size: 143.50 vbytes

sats/byte:    46
sats/vbyte:   72
```

如你所见，旧版交易具有相同的 **sats/byte** 和 **sats/vbyte** 费率。

因此，与其在两者中都使用新的 *重量* 测量，我们将新的 SegWit 交易的重量拉回到与以前相同的**刻度**上。这使得在仍在使用 **sats/byte** 的软件上轻松对比交易费率。

在比特币内部，我们只关心重量单位（weight units）的交易。但在诸如[区块链浏览器](/explorer/)这类工具中，我们更倾向于使用 **sats/vbyte** 而不是 **sats/wu**。

## 提升费用 (Fee Bumping)

如何增加交易的手续费？

如果[内存池](../mining/memory-pool.md)中有许多交易，并且你在[网络](../networking.md)中发送了一笔**低手续费交易**，你可能需要等待相当长的时间交易才会被挖出。

如果发生这种情况，你可能希望在交易仍在内存池中等待时*增加其手续费*。这会*增加矿工*将你的交易打包进他们下一个区块的意愿，从而加速你的交易被打包挖出的时间。

此过程称为“提升费用”，有以下两种方法：

1. [Replace By Fee (RBF)](#1-replace-by-fee-rbf)
2. [Child Pays For Parent (CPFP)](#2-child-pays-for-parent-cpfp)

### 1. Replace By Fee (RBF)

[BIP 125](https://github.com/bitcoin/bips/blob/master/bip-0125.mediawiki)

[<img src="../../images/diagrams_png_transaction-replace-by-fee.png" alt="Diagram showing a lower-fee transaction in the memory pool being replaced with a higher-fee transaction." width="753" height="416" />](../../images/diagrams_png_transaction-replace-by-fee.png)

这是最简单的方法。

要启用此功能，你只需将交易中的 [sequence](input/sequence.md) 值之一设置为 0xFFFFFFFD 或更低。接着，当这笔交易待在内存池中时，你可以选择将一个包含更高手续费的新版本交易发送到内存池中，这笔高手续费交易将直接替代旧的低手续费交易。

就是这样。如果节点或矿工收到一笔花费相同 input 的交易（但这次手续费更高），他们会乐意从他们的内存池中驱逐原始交易，并保留新的高手续费交易。

Replace By Fee 允许你*直接*替换内存池中的交易。

如果内存池中的当前交易没有启用 RBF，那么你无能为力。你只能等待，或者改用 CPFP（见下文）。

### 2. Child Pays For Parent (CPFP)

[<img src="../../images/diagrams_png_transaction-child-pays-for-parent.png" alt="Diagram showing a child transaction increasing the overall feerate of both the child and the parent transaction." width="752" height="544" />](../../images/diagrams_png_transaction-child-pays-for-parent.png)

这是一项古老的技术，但至今依然有效。

基本上，该技术利用了两个事实：

1. 你可以在交易仍在内存池中时花费其 [output](output.md)。
2. 矿工必须始终包含他们放入区块中的任何交易的“父交易”（如果父交易也在内存池中）。

因此，如果你有一笔低手续费的交易停留在内存池中，你可以通过在新交易中花费其输出之一，并为该新交易设置足够高的手续费，来激励矿工将该交易包含在下一个区块中，**使其值得打包第一笔交易**。

因此，子交易包含的高额手续费使得矿工打包低费用的父交易也是值得的。更准确地说，子交易提高了两笔交易的*平均费率*。

在可以使用 RBF 的情况下，没有理由使用 CPFP。但如果你的交易在未启用 RBF 的情况下被卡在内存池中，它仍然是一个非常方便的备选方案。

## Minimum Relay Fee

你能在一笔交易中设置的最低手续费是多少？

[<img src="../../images/diagrams_png_networking-minrelayfee.png" alt="Diagram showing a nodes on the network rejecting transactions with feerates that do not meet their own individual minimum relay fee settings." width="786" height="522" />](../../images/diagrams_png_networking-minrelayfee.png)

由于节点使用的*最低中继费*设置，你通常需要在交易中设置至少 `1 sat/vbyte` 的手续费。

每个节点都可以选择自己的最低中继费。使用此设置的目的是为了让节点无需为了处理和保留几乎不付或不付手续费的低价值交易而浪费资源。所以这有点像垃圾邮件过滤器。

当前默认的最低中继费是 `1 sat/vbyte`。

不过，最低中继费是一项*策略*，而不是共识规则，因此零手续费的交易被开采到[区块链](../blockchain.md)上并非不可能。它只意味着你发送的费率低于此设置的任何节点都不会接受该交易，也不会将其转发给其他节点。

因此，基本上，除非你认识矿工或者可以自己开采该交易，否则你设置的手续费必须高于你向其广播交易的节点/矿工的最低中继费。

你可以通过运行 `bitcoin-cli getmempoolinfo` 来找到节点的当前最低中继费。你可以通过在 Bitcoin Core 配置文件中设置 `minrelaytxfee=<amt>` 选项来调整此设置。

Bitcoin Core 设置的默认最低中继费可以在 [validation.h](https://github.com/bitcoin/bitcoin/blob/master/src/validation.h) 中找到。出于某种原因，这被定义为 1000 sat/kb，而不是 1 sat/vbyte，但它们表示的意思是完全相同的。

## 总结

> 届时将有交易手续费，因此 [矿工] 将会有动力接收并包含他们能打包的所有交易。
> 
> —— 中本聪，[密码学邮件列表（比特币 P2P 电子现金白皮书）](https://satoshi.nakamotoinstitute.org/emails/cryptography/13/)

交易手续费是比特币交易中的剩余部分，它用于激励矿工将你的交易包含在区块中。

矿工根据**每重量单位的费用**来选择交易，这衡量了交易在区块中占用的每单位空间可以让矿工获得多少手续费。这意味着如果同时有大量的交易被发送到网络中，竞争就会加剧，费率也会随之上升。

如果你在交易中设置了较低的手续费，并发现它被开采的速度不够快，你总是可以使用 RBF 用手续费更高的交易来代替它。如果未启用 RBF，你也可以使用 CPFP 来激励矿工将你的交易打包在他们的下一个区块中。

最后，如果你在手动构建比特币交易，**务必仔细检查你的输出大小**。因为算错找零输出大小而被矿工吃掉大笔 satoshis，可不是学习如何正确构建交易的愉快经历。以下是一些不幸的例子：

* [cc455ae816e6cdafdb58d54e35d4f46d860047458eacf1c7405dc634631c570d](/explorer/tx/cc455ae816e6cdafdb58d54e35d4f46d860047458eacf1c7405dc634631c570d)：291.2409 BTC 手续费 ([bitcointalk 帖子](https://bitcointalk.org/index.php?topic=1451924.0))
* [7e8fce9686572d8308d8c40fa3cb96fdbf96c0787c147d3159c893fd560aabc7](/explorer/tx/7e8fce9686572d8308d8c40fa3cb96fdbf96c0787c147d3159c893fd560aabc7)：30 BTC 手续费 ([Reddit 帖子](https://www.reddit.com/r/Bitcoin/comments/1eh57i/messed_up_transaction_feeplease_help/))
* [891af6431550ece772e2e2ebee13e856b971402763533babb2c49475ec260445](/explorer/tx/891af6431550ece772e2e2ebee13e856b971402763533babb2c49475ec260445)：7 BTC 手续费（虽然当时只有大约 $85，但依然没有必要）