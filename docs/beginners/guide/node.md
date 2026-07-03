<img src="../../images/icons_loader-2.svg" alt="Loading Tool" style="height:32px; width:32px;" />

[<img src="../../images/beginners_guide_network_05-nodes_network.png" alt="展示比特币网络上节点的图表。" width="600" height="416" />](/docs/beginners/guide/network/05-nodes_network.png.md)

比特币节点就是一**台运行[比特币程序](https://bitcoincore.org/en/download/)的计算机**。

更重要的是，它与运行相同程序的*其他计算机连接*在一起，形成了一个[网络](/docs/beginners/guide/network.md)。

## 节点是做什么的？

一个节点有三项工作：

1. 遵守规则
2. 分享信息
3. 保留一份已确认[交易](/docs/beginners/guide/transactions.md)的副本

### 1. 遵守规则

每个节点（比特币客户端）都被编程为遵守一组规则。通过遵守这些规则，节点能够检查它收到的交易，并且只有在一切正常的情况下才会转发它们。如果存在任何问题，交易就不会被传递下去。

[<img src="../../images/beginners_guide_node_01-node_rules.png" alt="展示节点在转发交易之前进行验证的图表。" width="503" height="520" />](/docs/beginners/guide/node/01-node_rules.png.md)

你的节点不会转发任何有问题的交易。

例如，一条规则是：一个人拥有的比特币数量必须等于或大于他们尝试发送的金额。因此，如果你的节点收到一笔某人企图发送比其拥有的更多比特币的交易，该交易将不会被传递给其他节点。

### 2. 分享信息

节点的主要工作是与其他节点共享信息，而节点共享的核心信息是**[交易](/docs/beginners/guide/transactions.md)**。

现在，节点共享的交易有两种类型：

1. **新鲜交易** – 最近才进入网络的交易。
2. **已确认交易** – 已经被“确认”并写入文件的交易。这些交易是以交易[区块](/docs/beginners/guide/blocks.md)的形式（而不是单独）进行共享的。

[<img src="../../images/beginners_guide_node_01-node_transaction_type_sharing.png" alt="展示节点共享新鲜交易和已确认交易区块的图表。" width="588" height="554" />](/docs/beginners/guide/node/01-node_transaction_type_sharing.png.md)

现在不用担心这两者之间的区别。在[挖矿](/docs/beginners/guide/mining.md)和[区块](/docs/beginners/guide/blocks.md)部分中，一切都会变得很清楚。

### 3. 保留一份已确认交易的副本

如前所述，每个节点还会保留*已确认*交易的区块。这些区块共同保存在一个被称为[区块链](/docs/beginners/guide/blockchain.md)的文件中。

[<img src="../../images/beginners_guide_node_02-node_blockchain.png" alt="展示节点保留已确认交易（区块链）副本的图表。" width="391" height="188" />](/docs/beginners/guide/node/02-node_blockchain.png.md)

新鲜交易在网络中来回传递，直到它们被刻入区块链中，区块链是交易的**永久存储库**。

每个节点都拥有一份用于安全保存的区块链副本，如果其他节点的副本不是最新的，它就会与它们共享。

向区块链中添加新鲜交易的过程被称为[挖矿](/docs/beginners/guide/mining.md)。

## 谁控制着比特币节点？

每个节点都是*自主的*。

> **自主的** – 不受他人或外部力量控制；独立的。

我的意思是，当你运行比特币客户端时，网络并不会“告诉你该怎么做”。相反，你的比特币客户端已经知道该怎么做，并且它*自己做出决定*。

所以，整个比特币网络由*自己做出决定*的节点组成，但它们做出的决定都互相同步且一致，这使得它成为一个完全*去中心化*但强大的网络。

如果其他所有节点都离线了，你的节点依然将支撑起整个比特币网络。

## 我必须运行一个节点才能使用比特币吗？

不需要。

你无需运行节点也可以发送和接收比特币。你只需要将交易*输入*到比特币网络中，一切就准备就绪了。

[<img src="../../images/beginners_guide_node_03-nodes_network_insert_transaction.png" alt="展示将一笔交易输入到单个节点中并在整个比特币网络中进行传播的图表。" width="566" height="321" />](/docs/beginners/guide/node/03-nodes_network_insert_transaction.png.md)

如果你仅仅向*一个*节点发送关于一笔交易的消息，它最终也会传播到整个网络。

例如，如果你正在使用[钱包](/docs/beginners/wallets.md)，它们会为你把你进行的交易输入到网络中。