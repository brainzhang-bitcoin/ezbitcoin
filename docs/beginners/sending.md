<img src="../images/icons_loader-2.svg" alt="Loading Tool" style="height:32px; width:32px;" />

你刚刚[购买了一些比特币](/docs/beginners/exchanges.md)并将其提现到你的[钱包](/docs/beginners/wallets.md)。现在你想向其他人*发送*一些比特币。

这就是你需要进行*交易*的地方。

在本指南中，我将为你快速概述**如何进行你的第一笔比特币交易**。

## 基础知识

你如何进行交易？

[<img src="../images/diagrams_png_beginners-sending-wallet.png" alt="展示钱包交易基础的图表。" width="632" height="367" />](https://static.learnmeabitcoin.com/diagrams/png/beginners-sending-wallet.png)

无论你使用哪种[比特币钱包](/docs/beginners/wallets.md)，进行比特币交易的过程都是相同的：

1. **输入地址。** 这是你想将比特币“发送”到的地方。
2. **输入金额。** 你想发送的比特币数量。这很可能是以 BTC 或 satoshis（聪）为单位。

   <img src="../images/icons_tool.svg" alt="Tool Icon" style="width:20px; height:20px" /> 单位换算器

   BTC

   完整的比特币


   mBTC

   千分之一的比特币


   uBTC

   百万分之一的比特币


   Sats

   亿分之一的比特币



   0 secs
3. **设置费用。*(可选)*** 这基本上设置了交易最终确定速度的“优先级”。

然后只需点击“发送”即可。

从这里开始，你只需要等待交易被添加到*区块链*中……

**务必三遍确认*金额*和*地址*。** 你无法“撤销”比特币交易，所以如果你把比特币发到了错误的地址，你就无法把它们拿回来了。

**不用太担心地址中的拼写错误。** 地址中包含一个[校验和](/docs/technical/keys/checksum.md)，这意味着你的钱包会检测它是否无效。所以你不需要逐个字符检查以确保地址正确——我通常只检查开头和结尾的 4 或 5 个字符。

**使用 TXID 跟踪你的交易。** 当你*发送*交易时，你的钱包会给你一个 [TXID](/docs/technical/transaction/input/txid.md)，这是一个唯一的*参考编号*，你可以用它在任何[区块链浏览器](/explorer/)上检查你的交易状态。

## 流程

当你进行交易时会发生什么？

当你点击“发送”时，你的钱包会将你的交易发送到[比特币网络](/docs/beginners/guide/network.md)上的一个[节点](/docs/beginners/guide/node.md)。

从这里开始，交易在节点之间转发，直到网络上的每个节点都拥有你的交易副本。

[<img src="../images/beginners_sending_send-transaction.gif" alt="展示一笔比特币交易被发送到节点并在网络上被转发的动画。" width="800" height="502" />](/docs/beginners/sending/send-transaction.gif.md)

起初，你的交易被保存在每个节点的[内存池](/docs/technical/mining/memory-pool.md)中，这就像是一个临时“等待区”，存放最近在网络上广播的交易。

[<img src="../images/beginners_sending_memory-pool.gif" alt="展示交易被保存在每个节点内存中的动画。" width="800" height="502" />](/docs/beginners/sending/memory-pool.gif.md)

大约 10 分钟后，网络上的一个节点会将其内存池中的最新交易[开采](/docs/beginners/guide/mining.md)到他们的[区块链](/docs/beginners/guide/blockchain.md)上。

然后，他们会将这个包含交易的全新[区块](/docs/beginners/guide/blocks.md)共享给网络上的其他节点。

[<img src="../images/beginners_sending_transaction-blockchain.gif" alt="展示一个新交易区块被添加到区块链上的动画。" width="800" height="427" />](/docs/beginners/sending/transaction-blockchain.gif.md)

收到该区块后，每个节点也会对其进行验证并将其添加到自己的区块链中。

结果，每个节点都会更新其区块链，以包括那些已从内存池（临时存储）移动到区块链（永久存储）中的最新交易：

[<img src="../images/diagrams_png_beginners-sending-blockchain-network.png" alt="展示区块链作为交易永久存储的图表。" width="983" height="525" />](https://static.learnmeabitcoin.com/diagrams/png/beginners-sending-blockchain-network.png)

如果你的交易被包含在一个区块中，那么你的交易就已经被**确认**，付款即告完成。

如果没有，你只需继续等待你的交易从内存池移动到区块链中。

**平均每隔 10 分钟就会有新区块添加到区块链中。** 因此，这取决于你在交易上设置的[费用](#fees)，你不需要等待太长时间就能让交易获得确认。

**不要依赖内存池中的交易。** 内存池交易不是永久性的，所以在交易进入区块链之前，不要认为付款已经“完成”。

## 挖矿

交易是如何进入区块链的？

每个节点都有机会尝试将其内存池中的交易添加到自己的区块链中。这个过程被称为[**挖矿**](/docs/beginners/guide/mining.md)。

为了将交易添加到区块链上，*矿工*会将其内存池中的交易收集到一个名为[候选区块](/docs/technical/mining/candidate-block.md)的容器中。从这里开始，矿工*使用能量*尝试在区块链上“开采”这个区块。

[<img src="../images/diagrams_png_beginners-sending-miner.png" alt="展示矿工使用计算能力尝试在区块链上开采候选区块的图表。" width="983" height="503" />](https://static.learnmeabitcoin.com/diagrams/png/beginners-sending-miner.png)

网络上的任何节点都可以成为矿工。

因此，挖矿过程基本上是一场**全网范围的竞争**，网络上的任何节点都有机会开采下一个区块。能够更快进行开采的节点有更好的机会开采下一个区块，但挖矿过程是*不可预测的*，所以没有哪一个单独的节点能控制向区块链添加区块的过程。

[<img src="../images/diagrams_png_beginners-sending-miners.png" alt="展示网络上的多个矿工尝试将下一个区块添加到区块链上的图表。" width="983" height="529" />](https://static.learnmeabitcoin.com/diagrams/png/beginners-sending-miners.png)

这些矿工中的任何一个都可能是开采区块链上下一个区块的人。

大约 10 分钟后（平均），其中一个矿工最终会开采出下一个交易区块，并与网络上的所有其他节点共享。然后，每个节点都会检查该区块（以确保其有效且已被正确开采）并将其也添加到自己的区块链中。

[<img src="../images/diagrams_png_beginners-sending-mined-block.png" alt="展示矿工开采一个区块并将其发送给网络上其他节点的图表。" width="983" height="503" />](https://static.learnmeabitcoin.com/diagrams/png/beginners-sending-mined-block.png)

网络中的节点用新开采的区块更新他们的区块链。

从这里开始，每个矿工都会构建一个新的候选区块（包含来自内存池的新交易），并开始尝试在链上开采下一个区块。

结果是，矿工们不断工作，用其内存池中的新交易区块来延长区块链。

### 为什么交易必须被开采？

[挖矿](/docs/technical/mining.md)的机制对于以下原因非常重要：

1. **防止冲突的交易被写入区块链。** 如果两笔冲突的交易被发送到网络中（例如尝试将相同的比特币发送到两个不同的地方），那么只有*其中一笔*交易会被写入区块链。
2. **任何节点都可以开采下一个交易区块。** 由于挖矿机制是不可预测的，*任何*节点都有机会开采下一个区块，这意味着没有哪一个单独的节点能完全控制被添加到区块链的交易。
3. **很难从区块链中删除交易。** 开采一个区块需要能量，这使得任何单独的矿工都很难获得足够的能量来重写区块链。

总而言之，*挖矿*是允许多台计算机在去中心化网络上就定期更新文件的同一副本达成一致的原因。

或者换句话说，这就是允许比特币维持安全交易账本的要素。

## 费用

什么是交易费？

每笔比特币交易都包含[费用](/docs/technical/transaction/fee.md)。

这些费用由矿工收集，因此作为**激励，促使矿工将你的交易包含在[区块](/docs/technical/block.md)中**。

为什么？

因为[候选区块](/docs/technical/mining/candidate-block.md)只能容纳一定量的数据。所以如果很多人同时进行交易，内存池中的交易可能比一个区块所能容纳的还要多：

[<img src="../images/diagrams_png_beginners-sending-memory-pool-overflow.png" alt="展示内存池中的交易多于候选区块所能容纳的图表。" width="371" height="450" />](https://static.learnmeabitcoin.com/diagrams/png/beginners-sending-memory-pool-overflow.png)

**注意：** 一个区块可以容纳[大约 2MB](/docs/technical/block.md#weight)的交易数据，但内存池可以容纳 [300MB+](/docs/technical/mining/memory-pool.md#size-limit)

因此，矿工将选择在他们的候选区块中填充带有**最高费用**的交易，因为如果他们成功开采出该区块，他们就可以（通过 [Coinbase](/docs/technical/mining/coinbase-transaction.md) 交易）收集这些费用。

[<img src="../images/diagrams_png_beginners-sending-miner-highest-fees.png" alt="展示矿工从内存池中选择费用最高的交易来填充其候选区块的图表。" width="371" height="450" />](https://static.learnmeabitcoin.com/diagrams/png/beginners-sending-miner-highest-fees.png)

因为归根结底，大多数矿工都希望从挖矿中赚取尽可能多的钱。

所以当内存池中有很多交易时，你在交易上设置的费用越高，你的交易在被包含在区块中的“优先级”就越高，开采速度也就越快。

[<img src="../images/beginners_sending_wallet-set-fee.gif" alt="展示当从钱包发送比特币时，你如何设置交易费用的动画。" width="800" height="366" />](/docs/beginners/sending/wallet-set-fee.gif.md)

* **内存池就像排队。** 带有最高费用的交易排在最前面。
* **交易费用实际上决定了交易在内存池中的*位置*。** 费用越高，开采速度*越快*。
* **一个好的钱包会允许你设置自己的费用。** 钱包还应该根据你的费用大小，为你估算交易被开采所需的时间。

### 我应该在我的交易上放多少费用？

这取决于**你希望你的交易以多快的速度被开采**，以及目前有多少交易在[内存池](/docs/technical/mining/memory-pool.md)中等待：

当前内存池大小：

2.38 vMB

8,900 笔交易

注意：这是我本地节点的内存池大小。  
根据你的节点在线时间以及你连接的节点，你的内存池大小会有所不同。

你希望交易开采得越快，你就应该使用越高的费用。

因此，一个好的钱包会使用**内存池的当前大小**，根据你希望交易在几个*区块*内被开采，来推荐各种[费率](/docs/technical/transaction/fee.md#feerates)：

| 区块数 | 时间（预估） | 费率 |
| --- | --- | --- |
| 2 | 20 分钟 | 1 sats/vbyte |
| 3 | 30 分钟 | 1 sats/vbyte |
| 6 | 1 小时 | 1 sats/vbyte |
| 12 | 2 小时 | 1 sats/vbyte |
| 144 | 1 天 | 1 sats/vbyte |
| 432 | 3 天 | 1 sats/vbyte |

注意：平均每 10 分钟[开采](/docs/technical/mining.md)一个新区块。

* **这些费率来自 Bitcoin Core 的 `bitcoin-cli estimatesmartfee` 命令。** 这是大多数[比特币钱包](/docs/beginners/wallets.md)用于费用推荐的命令。
* **这些是*预测值*。** 没有人能保证你的交易何时会被开采，因为在你进行交易之后，可能会有更多交易进入[网络](/docs/technical/networking.md)，并将你的交易推向队列的后方。
* **费用大小按 [sats/vbyte](/docs/technical/transaction/fee.md#sats-per-vbyte) 排序。** 这是以 *satoshis* 为单位的费用除以以 *virtual bytes*（虚拟字节）为单位的交易大小。这是因为矿工希望在每个交易在[区块](/docs/technical/block.md)中占用的空间里获得最多的费用。

你也可以随时在交易上设置自己的**自定义费用**。你可以自己查看内存池的当前状态，并决定一个你认为最适合你需求的费用。

但通常来说：

* 如果内存池中的交易**多于**一个[候选区块](/docs/technical/mining/candidate-block.md)所能容纳的量，你将需要使用适当的高费用来与内存池中的其他交易竞争，以进入即将到来的区块。
* 如果内存池中的交易**少于**候选区块所能容纳的量，你可以将费用设置为 1 sats/vbyte 的[最低费用](/docs/technical/mining/memory-pool.md#minimum-fee)。

* **在决定使用什么大小的交易费用时，查看内存池的状态很有用：**
  + [mempool.space](https://mempool.space) – 显示即将到来的区块以及每个区块内交易费用范围的可视化。
  + [Johoe's Bitcoin Mempool Size Statistics](https://jochen-hoenicke.de/queue/#0,24h) – 显示内存池当前状态的详细图表。
* **除非真的需要，否则不要在交易上放置太高的费用。** 如果你乐意等待一段时间，请使用较低的费用。

### 如果我在交易上放了很低的费用会怎么样？

在交易上设置**低费用**意味着你将其置于内存池的“队列末尾”。

这没关系，但这意味着你将等待一个内存池被清空的*空闲期*，以便你的交易能被包含在区块中。

[<img src="../images/beginners_sending_mempool-low-fee.gif" alt="展示低费用交易在内存池中所有高费用交易被开采完毕后，最终被包含在区块中的动画。" width="800" height="366" />](/docs/beginners/sending/mempool-low-fee.gif.md)

如果内存池中没有剩下更高费用的交易，较低费用的交易最终会被包含在区块中。

然而，交易在节点的内存池中只会保留 **2 周**（参见 [mempoolexpiry](/docs/technical/mining/memory-pool.md#mempoolexpiry)），在此时间段后，节点将**从其内存池中删除该交易**。如果发生这种情况，你的交易将从网络中消失，就好像你的交易从未发生过一样。

[<img src="../images/diagrams_png_beginners-sending-mempool-expiry.png" alt="展示如果交易在一定时间内未被开采，将从内存池中删除的图表。" width="262" height="506" />](https://static.learnmeabitcoin.com/diagrams/png/beginners-sending-mempool-expiry.png)

交易只在内存池中等待一段固定的时间。

* **大多数钱包允许你在交易仍在内存池中时[提高费用](/docs/technical/transaction/input/sequence.md#replace-by-fee)。** 所以如果你的交易花费了太长时间才被开采，你可以增加该交易的费用大小以加速该过程。
* 如果交易离开内存池，你可以随时将其重新广播到网络。

**在比特币交易获得确认之前，不要将其视为最终交易。** 费用非常低的交易可能无法被开采，并且如果它们在内存池中停留的时间太长，就会从网络中消失。

## 确认

我应该等待几个确认？

作为快速指南：

* **1 个确认**通常足够好。
* **2 个确认**更好，如果你想防止少见的[区块链重组](/docs/technical/blockchain/chain-reorganization.md)。
* 只有当你担心[网络规模的攻击](/docs/technical/blockchain/51-attack.md)以逆转你的交易时，才需要 **3 个以上确认**。

*确认*是指你的交易被开采进一个区块。额外的确认是指在包含你交易的区块*之上*开采出更多的区块。

[<img src="../images/beginners_sending_confirmations.gif" alt="展示确认数作为交易在区块链中深度的图表。" width="800" height="519" />](/docs/beginners/sending/confirmations.gif.md)

确认数量是指你的交易在区块链中的深度。

为什么这很重要？

虽然我说过你无法从区块链中删除交易，但技术上这是可能发生的。由于[区块链](/docs/technical/blockchain.md)的工作方式，拥有大量采矿能力的[不良矿工](/docs/technical/blockchain/51-attack.md)可以利用他们的能量来建立一个新的[更长区块链](/docs/technical/blockchain/longest-chain.md)供节点采用，并替换链中已有的区块（和交易）。

这在比特币中还没有发生过，但正如我所说，这在*技术上*是可能的。

[<img src="../images/diagrams_png_beginners-sending-replacing-blocks.png" alt="展示矿工在区块链顶部替换越来越多区块的可能性逐渐降低的图表。" width="983" height="639" />](https://static.learnmeabitcoin.com/diagrams/png/beginners-sending-replacing-blocks.png)

随着交易在区块链中向下移动的深度增加，矿工删除交易的难度呈指数级增加。

所以这就是为什么有时建议等待 **6 个确认**（或更多）以确保交易无法被逆转，因为此时对于矿工来说，替换那么多区块在“计算上是不可行的”。然而，除非你是在保护自己免受针对整个网络的不良矿工攻击，否则这是大材小用。

要对交易不会被撤销充满信心，等待 **2 个确认**是一个更合理的预估。这是因为在自然的[区块链重组](/docs/technical/blockchain/chain-reorganization.md)期间，区块链中的顶部区块往往会与另一个区块互换。

[<img src="../images/diagrams_png_beginners-sending-chain-reorganization.png" alt="展示区块链顶部区块被另一个区块替换的链重组图表。" width="983" height="639" />](https://static.learnmeabitcoin.com/diagrams/png/beginners-sending-chain-reorganization.png)

当两个区块在同一时间被开采出来并在链中竞争同一个位置时，就会发生链重组。

所以当你的交易通过了*第一个*区块（即 2 个确认）后，你可以确信它不会由于区块链构建方式的自然运行而被撤销。

链重组大约每 `44.3` 天发生一次（每 `6,451` 个区块发生一次）。

就个人而言，**1 个确认在大多数情况下对我来说已经足够了**，如果我收到一笔大额付款，我希望加倍确定它不会被撤销，我会等待 2 个确认。

只有当我用房子换比特币，并且我积极担心区块链可能会受到攻击时，我才会等待大约 6 个以上的确认。

## 监控

我该如何检查我的交易状态？

比特币最酷的事情之一是你可以使用[区块链浏览器](/explorer/)实时查看你的交易状态。

当你进行比特币交易时，你的钱包应该会给你该交易的 [TXID](/docs/technical/transaction/input/txid.md)。这就像是交易的唯一参考编号，你可以用它在区块链浏览器中查找交易。

以下是几个好用的区块链浏览器：

* [mempool.space](https://mempool.space) – 可能是最受欢迎的浏览器，名副其实。易于使用且时尚。
* [bitref.com](https://bitref.com) – 一个干净、快速的区块链浏览器。简洁友好。
* [learnmeabitcoin.com/explorer/](/explorer/) – 这是我做的一个浏览器。虽然用的人不多，但它确实是一个功能齐全的区块链浏览器。

现在，区块链浏览器基本上只是一个作为比特币[节点](/docs/technical/networking/node.md)*窗口*的网站。所以通过输入你的 TXID，你只是要求浏览器查看其区块链（或内存池）并向你展示它收到的交易的详细信息。

[<img src="../images/diagrams_png_beginners-sending-blockchain-explorers.png" alt="展示区块链浏览器作为查看正在运行的比特币节点数据窗口的图表。" width="983" height="529" />](https://static.learnmeabitcoin.com/diagrams/png/beginners-sending-blockchain-explorers.png)

区块链浏览器只是显示来自其区块链（和内存池）内部的数据。

我不会涵盖浏览器能向你展示的所有细节，但我发现最有用的一些内容是：

* **确认数量。** 我的交易仍在[内存池](/docs/technical/mining/memory-pool.md)中，还是已经被开采进一个[区块](/docs/technical/block.md)中了？
* **比特币的流动。** 比特币来自哪些[地址](/docs/technical/keys/address.md)，又被锁入哪些地址？
* **比特币上的锁。** 比特币上放置了什么[锁定脚本](/docs/technical/script.md)？

总之，你的钱包可能会告诉你关于你的交易的基本信息（比如它是否已被确认），但区块链浏览器允许你深入了解交易的细节，这非常酷。

你也可以使用 `bitcoin-cli gettransaction [txid]` 从你自己的 Bitcoin Core 节点查找交易的状态。

## 总结

以下是我进行比特币交易的首要建议：

* 使用让你感觉舒适的[钱包](/docs/beginners/wallets.md)。
* 设置你能接受的**最低费用**。
* 用[区块链浏览器](/explorer/)关注交易的进度。
  + 大多数时候 **1 个确认**就足够了。
  + 2 个确认更好，如果你想在罕见的自然[区块链重组](/docs/technical/blockchain/chain-reorganization.md)中做到万无一失。
  + 3 个以上确认是多余的，除非你害怕有人会精心策划一次[网络规模的攻击](/docs/technical/blockchain/51-attack.md)来撤销你的交易。

在你进行前几次交易后，你就会掌握窍门。

我已试图让本指南尽可能全面，但归根结底**经验始终是最好的老师**。所以慢慢来，试一试吧。