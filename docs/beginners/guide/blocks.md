<img src="../../images/icons_loader-2.svg" alt="Loading Tool" style="height:32px; width:32px;" />

区块是已添加到[区块链](blockchain.md)中的一堆[交易](transactions.md)。

## 区块是如何形成的？

区块是在[挖矿](mining.md)过程中构建的。

### 挖矿基础

当你进行一笔比特币交易时，它不会立即被添加到区块链上。相反，它会被保存在一个临时的交易池中。

[<img src="../../images/beginners_guide_blocks_01-transaction_pool.png" alt="展示比特币网络节点内内存池的图表。" width="328" height="360" />](../../images/beginners_guide_blocks_01-transaction_pool.png)

我在这里称其为“交易池”，但官方术语是*[内存池](../../technical/mining/memory-pool.md)*。

如果你是一名矿工，你的工作就是将交易池中的交易收集到一个“[候选区块](../../technical/mining/candidate-block.md)”中，并*尝试*将这个候选区块添加到区块链上。

[<img src="../../images/beginners_guide_blocks_02-candidate_block.png" alt="展示将内存池中的交易收集到候选区块中的图表。" width="421" height="360" />](../../images/beginners_guide_blocks_02-candidate_block.png)

#### 区块头

每个候选区块都会被赋予一个[区块头](../../technical/block.md#header)，这基本上是一组包含有关区块内容信息的*元数据*。

[<img src="../../images/beginners_guide_blocks_03-block_header.png" alt="展示为候选区块构建区块头的图表。" width="484" height="369" />](../../images/beginners_guide_blocks_03-block_header.png)

矿工在尝试向区块链添加区块时，以这个区块头为起点。

> **元数据** – 描述其他数据的数据，用作提供信息的信息标签。

##### 区块头字段

区块头字段的细节现在并不重要，但这里还是做一个简单的总结：

[Version](../../technical/block/version.md)
:   区块的版本号。

前一个区块
:   我们想要在其上进行构建的前一个区块的识别号。

[Merkle Root](../../technical/block/merkle-root.md)
:   区块中所有交易的指纹（基本上是将所有交易[哈希](../../technical/cryptography/hash-function.md)在一起）。这是区块头中最重要的部分。

[时间](../../technical/block/time.md)
:   当前时间。总是很有用。

Target（目标）
:   矿工在尝试将此区块添加到区块链时所用的数值。稍后这会变得更容易理解。

## 区块是如何添加到区块链上的？

要将候选区块添加到区块链上，你需要**对区块头中的数据进行[哈希](../../technical/cryptography/hash-function.md)计算**，并希望结果*低于某个[目标](../../technical/mining/target.md)值*。

[<img src="../../images/beginners_guide_blocks_05-block_target.png" alt="展示候选区块的区块哈希与当前目标进行对比的图表。" width="610" height="359" />](../../images/beginners_guide_blocks_05-block_target.png)

*目标*是通过[难度](difficulty.md)计算出来的，难度是比特币网络设置的一个值，用于调节向区块链添加交易区块的难易程度。

别担心，我知道这个*难度*和*目标*的概念一开始可能有点令人困惑，但随着时间的推移它会变得更容易理解。

[难度](difficulty.md)
:   用于调节区块解决速度的值。所有节点都同意对区块链当前高度的相同难度计算。它每 2,016 个区块（大约每 2 周）调整一次，以帮助在区块之间创造平均 10 分钟的时间间隔。

把目标想象成候选区块的极限运动杆——难度越大，目标越低，就越难找到低于此值的[区块哈希](../../technical/block/hash.md)。

### 一个额外的数字

我撒了谎。你实际上并不仅仅只对区块头本身进行哈希计算。你实际上是用*一个额外的数字*和它一起进行哈希。

[<img src="../../images/beginners_guide_blocks_06-block_nonce.png" alt="展示使用 Nonce 来更改区块头所得区块哈希的图表。" width="610" height="359" />](../../images/beginners_guide_blocks_06-block_nonce.png)

这个额外的数字被称为 [Nonce](../../technical/block/nonce.md)，它基本上是一个哑字段（dummy field），矿工用来帮助他们获得低于目标值的区块哈希。

> **Nonce** – 在密码学通信中仅使用一次的任意数字。

如果第一个 Nonce 不起作用（从 0 开始），*就继续递增它并对区块头进行哈希计算*。如果你运气好，你会找到一个返回低于当前目标值的区块哈希的 Nonce。

[<img src="../../images/beginners_guide_blocks_06-block_nonce_success.png" alt="展示成功的 Nonce 产生低于当前目标的区块哈希的图表。" width="610" height="359" />](../../images/beginners_guide_blocks_06-block_nonce_success.png)

我知道这些哈希值包含字母，但你仍然可以将它们像其他任何数字一样看待。它们只是[十六进制](../../technical/general/hexadecimal.md)值，计算机非常喜欢处理它们。

### 解决区块

一旦你找到了一个产生足够低区块哈希的 Nonce，该区块就被“解决”了，这个区块中的所有交易都会被添加到区块链中。

[<img src="../../images/beginners_guide_blocks_07-block_complete.png" alt="展示成功开采的区块被添加到区块链上的图表。" width="610" height="413" />](../../images/beginners_guide_blocks_07-block_complete.png)

现在，所有矿工都将回到交易池并开始处理下一个候选区块。他们将在下一个区块头中使用你成功的区块哈希（这样他们就可以在你刚刚开采的区块之上进行构建），向区块链添加新交易区块的竞争再次开始。

干得漂亮。