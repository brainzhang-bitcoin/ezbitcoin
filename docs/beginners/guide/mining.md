<img src="../../images/icons_loader-2.svg" alt="Loading Tool" style="height:32px; width:32px;" />

比特币挖矿是将**[交易](/docs/beginners/guide/transactions.md)添加到[区块链](/docs/beginners/guide/blockchain.md)**的过程。

## 挖矿是如何工作的？

[比特币网络](/docs/beginners/guide/network.md)上的每个[节点](/docs/beginners/guide/node.md)都会共享有关新交易的信息。

每个节点都将接收到的新交易保存在其*内存池*中。

[<img src="../../images/beginners_guide_mining_01-network-memory-pool.png" alt="展示比特币网络中每个节点内部的内存池图表。" width="776" height="392" />](/docs/beginners/guide/mining/01-network-memory-pool.png.md)

*内存池*是节点存放新交易的临时存储区。

每个节点还可以选择尝试将内存池中的交易“开采”到永久的**文件**中。这个文件是每笔比特币交易的分类账，被称为*区块链*。

[<img src="../../images/beginners_guide_mining_02-node-pool-block.png" alt="展示每个节点包含内存池和区块链的图表。" width="417" height="212" />](/docs/beginners/guide/mining/02-node-pool-block.png.md)

你可以将内存池看作包含“浮动”交易的区域，而将区块链看作包含“存档”交易的区域。

然而，要将交易从内存池添加到区块链，节点必须使用大量的计算机**计算能力**。

由于某种特定类型*挑战*的存在，这种计算能力是必不可少的。

### 挑战是什么？

好的，想象一下你是一个节点。在任何时刻，你都可以将内存池中的交易压缩成一串由数字和字母组成的单个“字符串”。

[<img src="../../images/beginners_guide_mining_03-node-pool-string.png" alt="展示内存池中所有交易哈希值的图表。" width="449" height="221" />](/docs/beginners/guide/mining/03-node-pool-string.png.md)

这个字符串代表了你内存池中的所有交易。

这个“字符串”基本上是内存池中所有交易的[哈希值](/docs/technical/cryptography/hash-function.md)。

现在，你的目标是将这个字符串与*另一个数字*（被称为 *[Nonce](/docs/technical/block/nonce.md)*）一起进行[哈希](/docs/technical/cryptography/hash-function.md)计算，以尝试获得一个**以一定数量的零开头**的新字符串。

大多数情况下，你会得到一个相差甚远的结果：

[<img src="../../images/beginners_guide_mining_04-node-pool-string-nonce.png" alt="展示内存池中所有交易的哈希值以及一个未成功 Nonce 的图表。" width="632" height="212" />](/docs/beginners/guide/mining/04-node-pool-string-nonce.png.md)

但是如果你继续下去，你可能会碰巧找到一个起作用的数字：

[<img src="../../images/beginners_guide_mining_04-node-pool-string-nonce-success.png" alt="展示内存池中所有交易的哈希值以及一个成功 Nonce 的图表。" width="627" height="211" />](/docs/beginners/guide/mining/04-node-pool-string-nonce-success.png.md)

<img src="../../images/icons_tool.svg" alt="Tool Icon" style="width:20px; height:20px" /> 哈希函数示例

Text

输入任意字符

`0 字符`


<img src="../../images/icons_hash-function.svg" alt="Hash Function Icon" style="width:52px; height:52px" />
SHA-256

SHA-256(text)

`0 字节`



0 secs

**这只是 SHA-256 哈希函数的一个快速示例。** 它对文本（ASCII 字符）进行哈希处理，而不是十六进制字节。在比特币中使用 SHA-256 和 HASH256 来对实际原始数据进行 SHA-256 哈希计算。

现在，这听起来足够容易，但实际上非常困难。这个过程完全是*随机*的，你只能寄希望于通过不断的尝试和错误来找到胜出的结果。这就是挖矿的*本质*——进行大量的哈希计算（使用计算能力）并希望能碰上**好运气**。

但是，如果你有幸找到了一个成功的哈希结果，你内存池中的交易就会被添加到区块链中，并且网络上的所有其他节点也会将你的交易区块添加到他们的区块链中。

此外，你还将因为付出努力而获得[区块奖励](/docs/technical/mining/block-reward.md)（这也包括你添加到区块链中的交易带来的所有[交易费](/docs/technical/transaction/fee.md)）。

[<img src="../../images/beginners_guide_mining_04-node-pool-string-nonce-success-reward.png" alt="展示在成功开采区块后赢得区块奖励的图表。" width="441" height="275" />](/docs/beginners/guide/mining/04-node-pool-string-nonce-success-reward.png.md)

注意：区块奖励已不再是 25 BTC（我最初写这篇文章是在 2015 年）。

“一定数量的零”来源于[难度](/docs/beginners/guide/difficulty.md)。这会根据整个网络的挖矿速度而发生变化——人们开采的速度越快，难度就越高，开头所需要的零也就越多（这有助于保持区块之间的时间间隔稳定）。

这是对区块如何添加到区块链的略微简化的版本。欲了解更多细节，请查看[区块](/docs/beginners/guide/blocks.md)。

## 为什么挖矿很重要？

好问题。为什么不直接将交易添加到区块链中呢？

因为挖矿允许整个比特币网络就哪些交易被“存档”达成一致，这就是你在数字货币中处理欺诈交易的方法。

### 怎么说呢？

当你进行一笔比特币交易时，网络上的所有节点并不会立即收到通知。相反，交易通过在节点之间传递来在比特币网络中进行传播。

[<img src="../../images/beginners_guide_mining_05-network-transaction-propagation.png" alt="展示交易在网络中传播的图表。" width="899" height="392" />](/docs/beginners/guide/mining/05-network-transaction-propagation.png.md)

*传播*是用来描述交易在网络中传输方式的词。

然而，实际上完全可以创建*另一笔*花费相同比特币的交易，并将这第二笔交易插入到网络的不同部分。

例如，你可以用一些比特币买一瓶啤酒，然后迅速尝试用*这同一批*比特币去买一片披萨。

换句话说，这就是某种**欺诈**。

[<img src="../../images/beginners_guide_mining_06-network-transaction-propagation-pizza.png" alt="展示第二笔交易与第一笔交易同时在网络中传播的图表。" width="899" height="471" />](/docs/beginners/guide/mining/06-network-transaction-propagation-pizza.png.md)

那么这里发生了什么？

* 有些节点先收到了披萨交易（并忽略了啤酒交易）。
* 有些节点先收到了啤酒交易（并忽略了披萨交易）。

然而，即使我们知道你先进行了啤酒交易，由于交易在比特币网络中传输的方式，网络对于你是该得到啤酒还是披萨将存在分歧。

### 那么网络如何决定保留哪笔交易呢？

当然是通过挖矿。

网络上**第一个**完成挑战的节点会将*其*内存池中的交易添加到区块链中。

[<img src="../../images/beginners_guide_mining_07-network-transaction-resolution.png" alt="展示当新区块被开采时，比特币网络如何解决双重支付的图表。" width="899" height="489" />](/docs/beginners/guide/mining/07-network-transaction-resolution.png.md)

例如，如果包含披萨交易的节点成功开采了一个区块，那么该交易就会被添加到区块链中，而啤酒交易则会被踢出网络。

我知道这看起来像是一种非主流的交易选择方式，但这就是比特币网络在处理冲突交易（也称为“双重支付”或“双花”）时，用来达成*共识*的解决方案。

每个新的交易区块被添加到区块链只需大约 10 分钟，因此你只需等待 10 分钟就能获得比特币已“到达”新地址（并且没有被发送到替代地址）的确认。

### 挖矿的另一个好处

如果你想尝试控制被添加到区块链的区块（即交易），你必须与比特币网络上的每个其他挖矿节点竞争来解决区块谜题。

换句话说：你需要拥有一台其计算能力足以超过所有其他比特币矿工计算能力总和的电脑。

这完全是可能的——你只需在硬件上投入几十亿美元就可以了（尽管这一数字随着更多挖矿能力加入网络而增加）。

所以换句话说，这种挖矿竞争防止了任何单一矿工完全控制哪些交易被添加到区块链。

## 我如何开始挖矿？

通过 Bitcoin Core 客户端进行挖矿已不再可能。

[<img src="../../images/beginners_guide_mining_setgenerate-true.jpg" alt="在 Bitcoin Core 中用于挖矿的 setgenerate 命令屏幕截图。" width="478" height="453" />](/docs/beginners/guide/mining/setgenerate-true.jpg.md)

此功能已在 2016 年被完全移除：

> 由于 CPU 挖矿早已无用，内部矿工已在此版本中被移除，并替换为一个更简单的测试框架实现。

[Bitcoin 0.13.0 版本发布说明](https://github.com/bitcoin/bitcoin/blob/master/doc/release-notes/release-notes-0.13.0.md#removal-of-internal-miner)

如果你想开始挖矿，你将需要考虑购买自己的专用硬件并加入所谓的“矿池”。