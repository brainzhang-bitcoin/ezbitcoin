<img src="../../images/icons_loader-2.svg" alt="Loading Tool" style="height:32px; width:32px;" />

[<img src="../../images/diagrams_png_block-previous-block.png" alt="Diagram showing the location of the previous block field inside the block header and how it connects the current block to the block below it in the blockchain." width="397" height="529" />](https://static.learnmeabitcoin.com/diagrams/png/block-previous-block.png)

[区块头](/docs/technical/block.md#header)中的 previous block 字段包含了该区块所**构建于其上**的前一个区块的[哈希](/docs/technical/block/hash.md)。

每个区块都链接到前一个区块，这便创建了一个*区块的链条*。或者，正如它更广为人知的名称：[区块链](/docs/technical/blockchain.md)。

## 示例

下面是区块链中最高的 5 个区块。如果您查看它们，就会发现它们各自的区块头中都包含其下方区块的哈希。

高度 | 区块哈希
---|---
956,479 | [000000000000000000000af753580e7b7bd555102cfbe9c72b4b625dbd3f48d8](/explorer/block/000000000000000000000af753580e7b7bd555102cfbe9c72b4b625dbd3f48d8) |
956,478 | [000000000000000000002c0a4bbbd933f15946021264162b74ce5c45b49a2100](/explorer/block/000000000000000000002c0a4bbbd933f15946021264162b74ce5c45b49a2100) |
956,477 | [000000000000000000000be1b133d433b3e0b0bf69f9368c20715ccf22ce85ce](/explorer/block/000000000000000000000be1b133d433b3e0b0bf69f9368c20715ccf22ce85ce) |
956,476 | [000000000000000000000aad5f4e9a1b745a856f53e4c613253b8275284221e9](/explorer/block/000000000000000000000aad5f4e9a1b745a856f53e4c613253b8275284221e9) |
956,475 | [000000000000000000001075120ee6594b359a02eda683e7c1ec3830838e281a](/explorer/block/000000000000000000001075120ee6594b359a02eda683e7c1ec3830838e281a) |

您可以通过从区块顶端开始并一路跟随 *previous block* 字段，访问区块链中的每一个区块，直至最底部。

## 用途

当构建[候选区块](/docs/technical/mining/candidate-block.md)时，[矿工](/docs/technical/mining.md)会在 previous block 字段中放入当前**区块链尖端**的区块哈希。

[<img src="../../images/diagrams_png_block-previous-block-tip.png" alt="Diagram showing how a candidate block referencing the tip of the blockchain through the previous block field in the block header." width="454" height="696" />](https://static.learnmeabitcoin.com/diagrams/png/block-previous-block-tip.png)

所有的矿工都希望延长当前已知最长的区块链接，因为[最长链](/docs/technical/blockchain/longest-chain.md)是所有节点采用的区块链的*权威 (canonical)*版本，并且矿工只有在区块成功进入最长链达 100 个区块深之后，才能收回其[区块奖励](/docs/technical/mining/block-reward.md)。

> **canonical** – 经授权的；公认的；被接受的
> 
> [collinsdictionary.com](https://www.collinsdictionary.com/dictionary/english/canonical)

您可以通过运行 `bitcoin-cli getbestblockhash` 来查找当前区块链尖端的区块。

**所有区块都必须构建在现有的前一个区块之上。** 如果您在区块的 previous block 字段中放入一个不存在的哈希值，该区块将是无效的，并会被[网络](/docs/technical/networking.md)上的节点拒绝。

## 目的

为什么区块要包含前一个区块的哈希值？

previous block 字段的作用是**将区块连接在一起**构成区块链。

[区块哈希](/docs/technical/block/hash.md)是区块的唯一引用，并由区块的内容决定。因此，通过在区块头中包含前一个区块的哈希值，您可以创建一个可靠的数据链，其中每个数据块（即交易区块）都链接到它前面的那个区块。

[<img src="../../images/diagrams_png_block-previous-block-hash-chain.png" alt="Diagram showing how block hashes are used to create a chain of blocks." width="386" height="461" />](https://static.learnmeabitcoin.com/diagrams/png/block-previous-block-hash-chain.png)

区块链只是通过区块哈希连接起来的区块链接。

因此，如果您试图修改较旧区块的内容（例如替换或删除某笔[交易](/docs/technical/transaction.md)），这将更改该区块的哈希值，并且它将不再是同一区块链接的一部分，因为构建于其上的区块将不再引用它。

[<img src="../../images/diagrams_png_block-previous-block-hash-chain-break.png" alt="Diagram showing how changing the contents of a block will change its hash, and will therefore break the link in the blockchain." width="557" height="518" />](https://static.learnmeabitcoin.com/diagrams/png/block-previous-block-hash-chain-break.png)

如果您更改了其中一个区块哈希，您就将其从链条中移除了。

所以基本上，这条区块哈希链条就是防止任何人回到过去更改区块链的机制。因为如果您这样做，节点将忽略修改后的区块，因为它不会成为已知最长链的一部分。

这就是人们将区块链称为“不可篡改账本 (immutable ledger)”的意思。

> **immutable** – 不可改变的；某物是不可改变的，将永远不会改变或无法改变。
> 
> [collinsdictionary.com](https://www.collinsdictionary.com/dictionary/english/immutable)

## 创世区块

[创世区块](/explorer/block/000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f)的独特之处在于其 previous block 字段**全为零**。这是因为它是区块链中的第一个区块，因此没有“前一个区块”可供其构建于其上。

这就是我关于区块头中 previous block 字段仅有的有趣事实。

## 资源

* <https://en.wikipedia.org/wiki/Hash_chain>
* [Blockchain Demo](https://andersbrownworth.com/blockchain/) - 酷炫的互动网站，展示了如何通过区块哈希将区块连接在区块链中。