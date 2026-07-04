<img src="../../images/icons_loader-2.svg" alt="Loading Tool" style="height:32px; width:32px;" />

[BIP 141: 隔离见证 (Segregated Witness)](https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki)

2017 年的隔离见证 (*SegWit*) 升级改变了比特币中[交易数据](../../technical/transaction.md)的结构。

这次升级的主要原因是为了修复**交易延展性 (transaction malleability)**（我稍后会对此进行解释）。另一个重要的变化是**[区块大小](../../technical/block.md#weight)的增加**。

## 主要改变了什么？

### 传统交易

在[传统交易](../../technical/transaction.md#example-legacy)中，解锁代码（和[签名](../../technical/keys/signature.md)）位于每个[输入](../../technical/transaction/input.md)的*旁边*，因此解锁代码分布在整个交易数据中。

然后根据**整个交易数据**创建 [TXID](../../technical/transaction/input/txid.md)：

[<img src="../../images/beginners_guide_segwit_txid.png" alt="Diagram showing the position of signatures in a legacy transaction and the TXID being created from the entire transaction data." width="824" height="234" />](../../images/beginners_guide_segwit_txid.png)

### SegWit 交易

然而，在 [SegWit 交易](../../technical/transaction.md#example-segwit)中，所有的解锁代码（和签名）都被移到了交易数据的*末尾*。

然后，除了**解锁代码**之外，根据所有交易数据创建 TXID：

[<img src="../../images/beginners_guide_segwit_txid-segwit.png" alt="Diagram showing the position of signatures in a segwit transaction and the TXID being created from all of the transaction data excluding the signatures." width="824" height="275" />](../../images/beginners_guide_segwit_txid-segwit.png)

因此，**SegWit 交易**中的 TXID 仅受交易*效果*（比特币的转移）的影响，而不受*验证*交易所需代码（即用于解锁比特币以供消费所需的签名）的影响。

[<img src="../../images/beginners_guide_segwit_txid-segwit-structure.png" alt="Diagram highlighting how the unlocking code is no longer included as part of the TXID in a segwit transaction." width="760" height="261" />](../../images/beginners_guide_segwit_txid-segwit-structure.png)

所以从本质上讲，你已经将“验证”部分（解锁代码）与交易的其他部分分离开来。

如果你将此验证代码称为*见证 (witness)* 数据（如密码学家所做的那样），你可以说你“*隔离*了*见证*”。\*眨眼\*

## 有什么好处？

1. [修复交易延展性](#fixes-transaction-malleability)
2. [提高区块容量](#increased-block-capacity)

### 1. 修复交易延展性

在比特币中，**交易延展性 (transaction malleability)** 是指**可以通过修改[签名](../../technical/keys/signature.md)来改变交易的 [TXID](../../technical/transaction/input/txid.md)**：

[<img src="../../images/beginners_guide_segwit_transaction-malleability.png" alt="Diagram showing the TXID of a legacy transaction being changed by altering the signatures inside the transaction data." width="843" height="274" />](../../images/beginners_guide_segwit_transaction-malleability.png)

可以通过反转 [s 值](../../technical/keys/signature.md#legacy-step-6)来改变签名。签名依然有效，交易也具有相同的效果，但 TXID 会变得不同。

这意味着当你将传统交易发送到网络中时，任何[节点](node.md)都有能力在转发它之前修改其 TXID：

[<img src="../../images/beginners_guide_segwit_transaction-malleability-network.png" alt="Diagram showing the TXID of a legacy transaction being modified after the transaction has been sent into the bitcoin network." width="558" height="389" />](../../images/beginners_guide_segwit_transaction-malleability-network.png)

最终你的交易会被打包进区块链，但其 TXID 与你预期的不同，这会让人有些恼火。

然而，如果签名不再是 TXID 的一部分，其他人就再也无法在之后修改你交易的 TXID 了：

[<img src="../../images/beginners_guide_segwit_transaction-malleability-network-segwit.png" alt="Diagram showing the TXID of a segwit transaction remaining the same after being sent into the bitcoin network." width="500" height="389" />](../../images/beginners_guide_segwit_transaction-malleability-network-segwit.png)

So in other words, SegWit makes TXIDs *reliable*. -> 所以换句话说，SegWit 让 TXID 变得*可靠*。

### 2. 提高区块容量

由于解锁代码被移至交易数据中一个*全新*的[见证字段](../../technical/transaction/witness.md)，因此区块大小的计算方式也可以随之改变。

在此之前，交易是以[字节](../../technical/transaction/size.md#bytes)为单位进行测量的，区块大小限制为 1,000,000 字节 (1 MB)：

[<img src="../../images/beginners_guide_segwit_block-size-bytes.png" alt="Diagram showing transactions and block capacity measured in bytes." width="685" height="241" />](../../images/beginners_guide_segwit_block-size-bytes.png)

在 SegWit 中，交易*不再以字节为单位进行测量*。相反，交易和区块被赋予了一个新的度量标准，称为[重量](../../technical/transaction/size.md#weight)：

[<img src="../../images/beginners_guide_segwit_block-size-weight.png" alt="Diagram showing transactions and block capacity measured in weight units." width="822" height="298" />](../../images/beginners_guide_segwit_block-size-weight.png)

* 一个区块的最大大小为 `4,000,000` 重量单位。
  + 交易中的*普通*字节等于 `4` 重量单位。
  + 交易中的*见证*字节等于 `1` 重量单位。

所以基本上，区块大小限制乘以 4，就得到了新的*区块重量限制*。

交易中的每个字节也乘以 4，以得到 [交易重量](../../technical/transaction/size.md#weight)。但是，你只需将见证数据的字节数乘以 1，这基本上使得“解锁代码”在区块中所占的空间享受了 75% 的折扣。

因此可以说，解锁数据所占的空间只有过去的*四分之一*，这意味着区块中整体上有了更多空间来容纳交易数据。

## SegWit 是区块大小的增加吗？

是的，现在每个区块的大小都可以大于 1,000,000 字节 (1 MB)。

因此，虽然区块大小限制没有增加特定数量的*字节*，但解锁数据的重量折扣意味着区块可以超过先前的 1 MB 限制。

尽管区块大小限制从 1,000,000 字节变为了 4,000,000 重量单位，但这并不意味着 SegWit 将区块大小绝对增加到了 4 MB。

这是因为一个典型的区块不会全部填满见证数据（每字节 1 重量单位）。相反，交易包含普通 data（等等，普通数据）和见证数据（1 重量单位）的组合。因此，“区块大小的增加”取决于区块中交易的组成结构。
Wait, let's write it cleanly:
`这是因为一个典型的区块不会全部填满见证数据（每字节 1 重量单位）。相反，交易包含普通数据（4 重量单位）和见证数据（1 重量单位）的组合。因此，“区块大小的增加”取决于区块中交易的组成结构。`

### SegWit 带来了多大程度的区块大小增加？

SegWit 升级将*典型*区块的最大大小提高到了 **1.8 MB** 左右。

你看，一个典型的交易区块包含大约 **60% 的解锁数据**¹。因此，如果我们计算一个由“典型”交易数据组成的 1 MB 区块的*重量*，我们会得到：

```
400,000 bytes * 4 = 1,600,000 weight units
600,000 bytes * 1 =   600,000 weight units

Total Weight      = 2,200,000 weight units
```

现在，如果一个区块的最大重量限制为 4,000,000 重量单位，我们可以计算出这给我们带来了多少增长：

```
4,000,000 / 2,200,000 = 1.81
```

所以可以说，这实际上将区块大小限制提高到了 **1.8 MB**。

1. 我是通过遍历 [blk.dat](../../technical/block/blkdat.md) 文件并累加区块中所有交易的 `scriptSig` 数据，并将其与区块的总大小进行对比，从而得到了这 60% 的数据。我没有进行详尽的测试，但 60% 似乎是一个合理的平均值。例如，这里是 [blk00700.dat](blk00700_scriptsig.txt) 的结果。

## 为什么这些变化要以这种方式实现？

或者，换句话说……

如果你想修复交易延展性并增加区块容量，难道没有更*直接*的方法吗？为什么需要重构交易数据，并创建一个名为“区块重量”的新度量标准？

好问题。你是对的——这些修改本可以做得简单得多。例如，你原本可以直接这样做：

[<img src="../../images/beginners_guide_segwit_easy-implementation.png" alt="Diagram showing the unlocking code being ignored in a legacy transaction when creating a TXID, and a direct block size increase to 2MB." width="718" height="397" />](../../images/beginners_guide_segwit_easy-implementation.png)

然而，如果这样做，在当前的规则下，交易和区块将变得“无效”。

基本上，这意味着网络上的节点会拒绝这些新的交易和区块，因为它们不符合关于交易和区块应该“长什么样”的规则。

[<img src="../../images/beginners_guide_segwit_hardfork-network.png" alt="Diagram showing existing nodes on the network rejecting blocks using the new hard-forking changes." width="312" height="275" />](../../images/beginners_guide_segwit_hardfork-network.png)

例如，其中一条规则就是每个区块的大小必须在 1 MB 或以下。

因此，如果你想进行这些更改，**你需要让网络上的每个人都升级他们的软件**（并且显然要同意 these 更改）。
Wait, write it cleanly:
`因此，如果你想进行这些更改，**你需要让网络上的每个人都升级他们的软件**（并且显然要同意这些更改）。`

因为如果不这样做，最终会导致网络构建出两条不同的区块链——升级后的节点使用新规则构建区块链，而旧节点继续使用旧规则构建区块链。

[<img src="../../images/beginners_guide_segwit_hardfork-blockchain.png" alt="Diagram showing the blockchain being split in to two separate versions due to a hard-forking change." width="521" height="280" />](../../images/beginners_guide_segwit_hardfork-blockchain.png)

这被称为[硬分叉](../../technical/blockchain/hard-fork.md)。这可行，但极具风险，并且会给那些未升级的人带来问题。

### SegWit 是如何避免硬分叉的？

SegWit 并非硬分叉，而是作为[软分叉](../../technical/blockchain/soft-fork.md)实现的。

通过 SegWit 升级，**交易和区块*依然遵循*比特币网络的当前规则**，因此所有节点仍然认为 SegWit 区块是有效的。因此，“旧”节点也会接受这些“新”区块并将它们添加到自己的区块链中。

[<img src="../../images/beginners_guide_segwit_softfork-network.png" alt="Diagram showing old nodes who haven't upgraded accepting the new SegWit blocks and transactions." width="384" height="275" />](../../images/beginners_guide_segwit_softfork-network.png)

因此，旧节点仍然能跟上新节点的步伐，*即使它们没有升级*。

[<img src="../../images/beginners_guide_segwit_softfork-blockchain.png" alt="Diagram showing both old and upgraded nodes keeping up with the same version of the blockchain after a soft-forking change." width="214" height="280" />](../../images/beginners_guide_segwit_softfork-blockchain.png)

通过软分叉，每个人都保持与单一版本区块链的同步。

对于“旧”节点来说，缺点是它们在升级之前无法利用 SegWit 的新特性。然而，在那之前，它们可以像往常一样继续进行“旧式”交易，并**跟上区块链的进度**。

总而言之，SegWit 升级虽然看起来像是修复交易延展性和增加区块容量的一种“打补丁 (hacky)”的方式，但这种方法避免了试图让所有人升级到新软件（否则就会被抛在后面）的问题。

## SegWit 是何时激活的？

SegWit 于 2017 年 8 月 24 日 01:57:37 在区块高度 [481,824](/explorer/block/0000000000000000001c8018d9cb3b742ef25114f27563e3fc4a1902167f9893) 处被激活。

这是节点开始对所有新区块和交易强制执行 SegWit 升级的新共识规则的时间。

## SegWit 是如何生效的？

当 **95%** 的矿工表态支持时，隔离见证升级便开始生效。

矿工可以通过在他们开采的区块中使用指定的[版本号](../../technical/block/version.md)来表达他们的支持意愿。

[<img src="../../images/beginners_guide_segwit_signal-block-version.png" alt="Diagram showing the version field in the block header." width="538" height="227" />](../../images/beginners_guide_segwit_signal-block-version.png)

版本字段是[区块头](../../technical/block.md#header)的一部分。

因此，当 95% 的区块都带有这个版本号时，SegWit 便被安排激活：

[<img src="../../images/beginners_guide_segwit_signal-blockchain-activation.png" alt="Diagram showing how the SegWit upgrade was scheduled for the next retarget period after a successful signaling period." width="396" height="351" />](../../images/beginners_guide_segwit_signal-blockchain-activation.png)

这 95% 的门槛是在一个[目标](../../technical/mining/target.md)重新调整周期内计算的。如果达到了 95% 的门槛，软分叉将在*下一个*目标调整周期（即 2016 个区块，或大约 2 周）开始时激活。

### 激活是否有时间限制？

是的，这是激活窗口：

|  |  |
| --- | --- |
| 开始时间： | 2016 年 11 月 15 日, 00:00 |
| **截止时间：** | 2017 年 11 月 15 日, 00:00 |

如果到 2017 年 11 月 15 日午夜仍没有足够多的矿工表示支持隔离见证升级，该提案就会过期。

### 激活时间线

下面这张表格显示了在激活前的每个目标周期中，支持 SegWit 的区块数量：

| 开始时间 | 目标周期 | 支持区块数 | 百分比 |
| --- | --- | --- | --- |
| 2016年11月18日, 08:30:15 | [439,488](/explorer/439488#blockchain) 至 [441,503](/explorer/441503#blockchain) | 451/2016 | 22.37% |
| 2016年12月2日, 02:46:26 | [441,504](/explorer/441504#blockchain) 至 [443,519](/explorer/443519#blockchain) | 487/2016 | 24.16% |
| 2016年12月15日, 01:28:33 | [443,520](/explorer/443520#blockchain) 至 [445,535](/explorer/445535#blockchain) | 520/2016 | 25.79% |
| 2016年12月28日, 17:40:55 | [445,536](/explorer/445536#blockchain) 至 [447,551](/explorer/447551#blockchain) | 521/2016 | 25.84% |
| 2017年1月10日, 22:40:52 | [447,552](/explorer/447552#blockchain) 至 [449,567](/explorer/449567#blockchain) | 489/2016 | 24.26% |
| 2017年1月22日, 22:52:52 | [449,568](/explorer/449568#blockchain) 至 [451,583](/explorer/451583#blockchain) | 468/2016 | 23.21% |
| 2017年2月4日, 23:38:49 | [451,584](/explorer/451584#blockchain) 至 [453,599](/explorer/453599#blockchain) | 485/2016 | 24.06% |
| 2017年2月18日, 09:38:26 | [453,600](/explorer/453600#blockchain) 至 [455,615](/explorer/455615#blockchain) | 537/2016 | 26.64% |
| 2017年3月3日, 19:04:46 | [455,616](/explorer/455616#blockchain) 至 [457,631](/explorer/457631#blockchain) | 532/2016 | 26.39% |
| 2017年3月17日, 08:36:15 | [457,632](/explorer/457632#blockchain) 至 [459,647](/explorer/459647#blockchain) | 582/2016 | 28.87% |
| 2017年3月30日, 16:39:08 | [459,648](/explorer/459648#blockchain) 至 [461,663](/explorer/461663#blockchain) | 614/2016 | 30.46% |
| 2017年4月13日, 02:59:50 | [461,664](/explorer/461664#blockchain) 至 [463,679](/explorer/463679#blockchain) | 671/2016 | 33.28% |
| 2017年4月27日, 02:20:01 | [463,680](/explorer/463680#blockchain) 至 [465,695](/explorer/465695#blockchain) | 698/2016 | 34.62% |
| 2017年5月10日, 03:40:48 | [465,696](/explorer/465696#blockchain) 至 [467,711](/explorer/467711#blockchain) | 663/2016 | 32.89% |
| 2017年5月23日, 07:29:52 | [467,712](/explorer/467712#blockchain) 至 [469,727](/explorer/469727#blockchain) | 622/2016 | 30.85% |
| 2017年6月4日, 14:35:07 | [469,728](/explorer/469728#blockchain) 至 [471,743](/explorer/471743#blockchain) | 642/2016 | 31.85% |
| 2017年6月17日, 23:18:53 | [471,744](/explorer/471744#blockchain) 至 [473,759](/explorer/473759#blockchain) | 825/2016 | 40.92% |
| 2017年7月2日, 00:47:17 | [473,760](/explorer/473760#blockchain) 至 [475,775](/explorer/475775#blockchain) | 917/2016 | 45.49% |
| 2017年7月14日, 08:45:42 | [475,776](/explorer/475776#blockchain) 至 [477,791](/explorer/477791#blockchain) | 1440/2016 | 71.43% |
| 2017年7月27日, 11:03:54 | [477,792](/explorer/477792#blockchain) 至 [479,807](/explorer/479807#blockchain) | 2016/2016 | 100.00% |

如你所见，在区块 [477,792](/explorer/block/00000000000000000016ba7786309176445b838b36a16bd1ef3c3e3020473206) 和 [479,807](/explorer/block/00000000000000000053e2d10bd703ad5b7787614965711d6170b69b133aa366) 之间的目标调整周期内，矿工表态支持 SegWit 的比例超过了 95% 的门槛。

因此，大约 2 周（2,016 个区块）后，SegWit 升级在区块 [481,824](/explorer/block/0000000000000000001c8018d9cb3b742ef25114f27563e3fc4a1902167f9893) 处被激活：

| 开始时间 | 目标周期 | 备注 |
| --- | --- | --- |
| 2017年8月9日, 12:36:50 | [479,808](/explorer/479808#blockchain) 至 [481,823](/explorer/481823#blockchain) | SegWit 锁定 (Locked In) |
| 2017年8月24日, 01:57:37 | [481,824](/explorer/481824#blockchain) 起 | SegWit 激活 (Activated) |

* 从 439,488 到 441,503 的目标周期是激活窗口开启后的第一个表态周期。
* 在 477,792 和 479,807 之间的区块 100% 都表态支持 SegWit 升级。你可以在这里查看这些区块及其信号：<segwit-signals-version-bits.txt>（右起第二位表示支持 SegWit）。
* 在软分叉激活之前，有一个目标周期的间隔，此时软分叉处于“已锁定 (locked in)”状态。

### 为什么把激活的决定权交给*矿工*？

因为如果你希望软分叉成功，你需要大多数矿工在区块链上[挖矿](mining.md)产生“新”类型的区块。

这样一来，包含“新”区块的区块链在速度上就会超过任何由“旧”区块（可能仍有一些未升级的矿工在挖矿）构建的区块链。

结果，“新”区块链的构建速度比由“旧”区块构建的区块链更快，因此所有节点自然都会采用同一个[最长链](../../technical/blockchain/longest-chain.md)：

[<img src="../../images/beginners_guide_segwit_miners-softfork.png" alt="Diagram showing a majority of miners building the longest chain with new blocks after the SegWit upgrade." width="560" height="438" />](../../images/beginners_guide_segwit_miners-softfork.png)

拥有大多数算力可以使网络中的每个人都保持在同一条链上。

因此，获得绝大多数矿工的支持可以实现平滑升级，因为这确保了整个网络都将收敛到同一条区块链上。

这倒不一定是因为矿工是对判断软分叉升级优缺点最了解的群体；更多的是因为*需要*他们来确保整个网络能够平稳升级。

## 如果我不运行 SegWit 升级会怎么样？

如果你运行的是旧节点（例如 [Bitcoin Core v0.13.0](https://github.com/bitcoin/bitcoin/blob/master/doc/release-notes/release-notes-0.13.0.md) 或更低版本），你所连接的任何 SegWit 节点都会在向你发送交易之前，剥离交易中所有的[见证数据](../../technical/transaction/witness.md)。

[<img src="../../images/beginners_guide_segwit_old-node-witness-data.png" alt="Diagram showing an old node not receiving the witness data from segwit transactions when connected to an upgraded node." width="365" height="172" />](../../images/beginners_guide_segwit_old-node-witness-data.png)

这意味着：

* 你仍然会收到和大家一样的交易。
* 如果你收到一个 SegWit 交易，你会看到比特币的*转移*，但你不会看到任何*解锁代码*数据。

所以基本上，你的节点会得到一个 SegWit 交易的“轻量”版本。

## 我该如何升级？

这就对了！

* **Bitcoin Core** – 只要确保你使用的是 [0.13.1](https://github.com/bitcoin/bitcoin/blob/master/doc/release-notes/release-notes-0.13.1.md) 或更高版本。
* **其他钱包** – 如今几乎所有现代[钱包](../wallets.md)都支持 SegWit 交易。

SegWit 已经存在了如此之久，以至于你不太可能遇到任何不支持它的软件（除非它明显太老了）。

## 资源

* [BIP 141 (共识层)](https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki)
* [BIP 144 (对等网络服务)](https://github.com/bitcoin/bips/blob/master/bip-0144.mediawiki)
* [Bitcoin.org – 隔离见证的好处](https://bitcoincore.org/en/2016/01/26/segwit-benefits/)

### 致谢

* [Pieter Wuille](https://github.com/sipa) – 感谢其对 [SegWit 交易数据结构](https://bitcoin.stackexchange.com/questions/49097/what-does-a-segregated-witness-transaction-look-like)等内容的解释。
* [Gregory Maxwell](https://github.com/gmaxwell) 和 [Luke-jr](https://github.com/luke-jr) – 感谢其对[区块重量](https://www.reddit.com/r/Bitcoin/comments/5e7a8n/what_will_be_the_block_size_limit_if_segwit/)的解释。

### 延伸阅读

* [隔离见证详解](https://www.youtube.com/watch?v=DzBAG2Jp4bg) – 关于 SegWit 的优质视频解释，附有交易数据结构变化的直观可视化。