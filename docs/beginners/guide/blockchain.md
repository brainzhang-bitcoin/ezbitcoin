<img src="../../images/icons_loader-2.svg" alt="Loading Tool" style="height:32px; width:32px;" />

区块链是一个包含比特币[交易](transactions.md)列表的文件。

[<img src="../../images/beginners_guide_blockchain_01-blockchain_file.png" alt="展示区块链作为计算机上一个文件的图表。" width="194" height="237" />](../../images/beginners_guide_blockchain_01-blockchain_file.png)

[比特币网络](network.md)上的每个人都共享这个文件的一个副本，它会定期用最新的交易进行更新。

[<img src="../../images/beginners_guide_blockchain_02-bitcoin_network.png" alt="展示区块链作为网络上计算机共享的文件的图表。" width="481" height="544" />](../../images/beginners_guide_blockchain_02-bitcoin_network.png)

## 为什么区块链很重要？

区块链告诉你**每个人拥有多少比特币**。

这是因为拥有*完整的交易列表*允许你计算出每个[地址](../../technical/keys/address.md)处有多少比特币。因此，你可以搞清楚每个人拥有多少比特币。

所以区块链就像是一个账簿，或者说*分类账*。

> **分类账** – 记录企业货币交易（以借记和贷记形式发布）的账簿。

## 为什么它被称为区块链？

因为交易并不是单独添加到文件中的。相反，它们被打包在一起并以区块形式添加。因此被称为**区块**链（blockchain）。

此外，这些区块被*链接*在一起，这可以防止任何人修改已经存在于链中的区块（因为任何修改都会破坏它们之间的链接）。所以是**链接**的区块，或者称之为区块**链**。

[<img src="../../images/beginners_guide_blockchain_03-blocks_chains.png" alt="展示区块链作为一系列链接在一起的区块（交易）的图表。" width="515" height="433" />](../../images/beginners_guide_blockchain_03-blocks_chains.png)

区块的*链式连接*是一个安全特性。这使得任何人在不引起注意的情况下篡改区块链变得不可能。

此外，以*区块*形式添加交易的过程使每个人共享区块链副本变得更容易；与共享一个每秒更新多次的文件相比，共享一个每 10 分钟更新一次的文件要容易得多。

## 区块链是如何共享的？

区块链由[比特币网络](network.md)上的[节点](node.md)共享，类似于在 [BitTorrent 网络](https://en.wikipedia.org/wiki/BitTorrent)上共享一个完全合法且没有版权争议的视频文件。

[<img src="../../images/beginners_guide_blockchain_04-blocks_sharing.png" alt="展示区块链在网络上与新区块共享并更新的图表。" width="481" height="544" />](../../images/beginners_guide_blockchain_04-blocks_sharing.png)

所以，如果我的文件没有包含最新的交易区块，有人会把它们分享给我，让我保持最新状态。

P2P 文件共享是一个独立的话题，但现在只需知道区块链像 BitTorrent 文件一样在比特币网络中共享。

## 我在哪里可以获得区块链的副本？

你可以通过下载原始的[比特币客户端](https://bitcoin.org/en/download)来获得一份属于你自己的、真实且充满能量的区块链副本。

一旦安装并运行，客户端将连接到网络上的其他节点，并开始下载区块链。目前它的大小大约在 `857` GB，所以请给它一些时间。

什么？它确实包含了自 2009 年 1 月 3 日以来的每一笔比特币交易，所以 `857` GB 是合理的。此外，完整区块链的首次下载是一次性的。在那之后就轻松了——你的区块链会随着最新的区块而更新，而它们的大小只有 1 MB 左右。

下载完成后，你将拥有一份完整的区块链副本，所有比特币交易的列表就在你手中。此外，每次你运行比特币客户端时，你都将帮助向加入网络的其他人共享这个文件。你的一些朋友甚至可能会开始叫你“全节点”。

通过保存一份区块链副本并将其与网络上的其他人共享，你可以让比特币变得更强大。

如果你是种子下载的粉丝，你可以认为自己是在**做种（seeding）**区块链。大家都喜欢做种的人。

## 区块链文件存储在我电脑的什么位置？

你的区块链副本位置取决于你使用的是什么操作系统：

Linux
:   `/home/[username]/.bitcoin/blocks/`

Windows
:   * `C:\Users\[username]\AppData\Roaming\Bitcoin\blocks\`（[v27.2](https://github.com/bitcoin/bitcoin/blob/master/doc/release-notes/release-notes-27.2.md) 及以下版本）
    * `C:\Users\[username]\AppData\Local\Bitcoin\blocks\`（[v28.0](https://github.com/bitcoin/bitcoin/blob/master/doc/release-notes/release-notes-28.0.md) 及以上版本）

Mac
:   `~/Library/Application Support/Bitcoin/blocks/`

实际的区块链数据存储在名称类似 `blk00000.dat` 的文件中。还有 `blk00001.dat`、`blk00002.dat` 等等。将区块链分割成多个文件，比拥有一个庞大的单文件更容易处理。

然而，这些 [.dat 文件](../../technical/block/blkdat.md)包含的数据是设计给计算机阅读的，所以如果你用文本编辑器打开它，你会看到一堆乱码。但请相信我，所有的交易都在里面。

如果你想浏览可读版本的区块链，可以试试我的[区块链浏览器](/explorer/)。我基本上是从原始区块链文件（和你拥有的副本完全相同）中提取数据，对其进行*解析*，然后显示在网页上。