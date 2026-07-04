<img src="../../images/icons_loader-2.svg" alt="Loading Tool" style="height:32px; width:32px;" />

[<img src="../../images/diagrams_png_block-nonce.png" alt="Diagram showing the location of the nonce field inside the block header." width="646" height="291" />](../../images/diagrams_png_block-nonce.png)

Nonce 是[区块头](../block.md#header)末尾的一个备用字段，用于[挖矿](../mining.md)。

> Nonce 是 **n**umber used **once**（使用一次的数字）的缩写。

[cryptography.fandom.com/wiki/Cryptographic\_nonce](https://cryptography.fandom.com/wiki/Cryptographic_nonce)

我喜欢称它为“挖矿字段”。

无论如何，理解其目的最简单的方法是调整区块头中的 Nonce，看看它如何影响[区块哈希](hash.md)：

随机示例

区块:

区块头 (Hex)

`0 bytes`


区块头 (字段)


Version


0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

Previous Block:
Merkle Root
Time

0d

Bits
Nonce

0d



+1



区块哈希 (Block Hash)

这是十六进制区块头的 HASH256。它也采用反向字节顺序，因为这是区块浏览器显示区块哈希的方式。




0 秒

## 用途

Nonce 字段用于做什么？

Nonce 是一个 4 字节的字段，可以保存 **0** 到 **4294967295** 之间的数字（十六进制中为 `0x0` 到 `0xffffffff`）。

矿工在挖矿时会递增 Nonce 值，以便为他们的[候选区块](../mining/candidate-block.md)的区块头获得完全不同的[哈希](../cryptography/hash-function.md)结果。他们希望偶然发现一个“魔术” Nonce 值，该值能够产生低于当前[target](../mining/target.md)值的区块哈希。

所以寻找起作用的 Nonce 并没有什么技术含量。它只是一个备用字段，允许矿工快速对区块头重新进行哈希，而无需重新构建整个区块。

[<img src="../../images/technical_block_nonce_miningsimulator.gif" alt="Mining simulator showing multiple hash attempts by incrementing the nonce." width="787" height="142" />](../../images/technical_block_nonce_miningsimulator.gif)

这是挖矿过程在底层的慢速模拟。

这个 [SHA-256 视频](https://www.youtube.com/watch?v=f9EbD6iY9zI&t=140s) 展示了挖矿过程的实际运作。

### 注意事项

关于 Nonce 运作方式的一些额外细节：

* **您并非随着每次哈希尝试而离挖出区块更近。** 仅仅因为您递增了 Nonce，并不意味着您正在“努力”挖出区块。[哈希函数](../cryptography/hash-function.md)的结果完全不可预测，因此每个结果都独立于上一个结果。您使用 Nonce 值为 0 挖出区块的几率与使用 Nonce 值为 4294967295 挖出区块的几率完全相同——这没有任何区别。
* **您不一定非要*递增* Nonce。** 在尝试挖出区块时，您可以倒着计算，甚至尝试随机的 Nonce 值。这没关系。只要您不重复使用相同的 Nonce 值，您尝试不同 Nonce 的方法对您挖出区块的几率不会产生任何影响。然而，每次尝试递增 Nonce 值是最简单也是最快的方法，因此矿工通常会这样做。
* **并不是每个区块都有一个魔术 Nonce 值。** 不能保证任何给定的区块头都存在一个“魔术” Nonce 值。事实上，很有可能没有任何 Nonce 值能产生低于目标的哈希结果。如果您耗尽了 Nonce，您需要使用新的区块头重新开始（例如，通过调整[time](time.md)字段，或更改区块中的[交易](../transaction.md)）。

## 局限性

每个区块都有“魔术” Nonce 值吗？

矿工通常会耗尽区块头中 4 字节的 Nonce 字段，而**无法**找到能产生低于当前目标的区块哈希的“魔术” Nonce 值。

所以，大部分区块都不会有“魔术” Nonce 值。

当矿工耗尽了 Nonce 字段时，显而易见的下一步是调整[time](time.md)（时间）字段。这会产生一个稍微不同的区块头，从而允许矿工再次递增 Nonce 字段以尝试挖出相同的交易区块。

然而，矿工的速度是如此之快，以至于他们会在不到 1 秒的时间内耗尽 Nonce 字段，因此在此情况下*时间*字段并不能提供太多帮助。因此，矿工会寻找其他方法来修改区块头，而无需重新构建整个交易区块（因为这会花费更多时间）……

在区块头中设置这样一个微小的 4 字节 Nonce 字段可能是中本聪的一个设计失误。

## ExtraNonce

[<img src="../../images/diagrams_png_block-extranonce.png" alt="The ExtraNonce is located inside the scriptSig of a coinbase transaction." width="767" height="310" />](../../images/diagrams_png_block-extranonce.png)

如果矿工耗尽了 Nonce 字段，他们将转向调整所谓的 "ExtraNonce"。

ExtraNonce 位于 [Coinbase](../mining/coinbase-transaction.md) 交易的 [scriptSig](../transaction/input/scriptsig.md) 内部。矿工可以自由在 scriptSig 中放入他们喜欢的任何数据，这意味着他们可以对其进行修改，以作为**附加 Nonce 值的非官方字段**。

其工作原理为：

1. 更改 [scriptSig](../transaction/input/scriptsig.md) 的内容会更改交易数据。
2. 更改 Coinbase 交易的交易数据会更改其 [TXID](../transaction/input/txid.md)。
3. 更改 Coinbase 交易的 TXID 会更改 [Merkle Root](merkle-root.md)。
4. 更改 Merkle Root 会更改区块头。

因此，更改 Coinbase 交易中的 scriptSig 是通过 Merkle Root 修改区块头的快速而简单的方法。

在 scriptsig 内部并没有 ExtraNonce 的“官方”位置，因此不一定容易识别出矿工将哪部分用于 ExtraNonce。然而，矿工通常会向 scriptsig 字段的开头递增一些数据。

* **最快的挖矿方式是直接调整 Nonce。** 如果您仅使用 ExtraNonce 字段进行挖矿，您必须在每次尝试时重新计算 Merkle Root，这会慢很多。
* [version](version.md)（版本）字段也可以用作额外的 Nonce。

## 术语

为什么它被称为 Nonce？

好问题。

这是密码学中用于“使用一次的数字 (number used once)”的术语，因此它基本上是指任何时候由于某些密码学目的而需要使用一次性随机数的情况。

当然，除非您是英国人，在这种情况下，它的意思完全不同。

## Gif 动图

这是我于 2016 年制作的一个很糟糕的 gif，展示了如何使用 Nonce 来更改区块哈希：

[<img src="../../images/technical_block_nonce_nonce-block-hash.gif" alt="Animated gif of the nonce being used to change the block hash." width="445" height="234" />](../../images/technical_block_nonce_nonce-block-hash.gif)

这是另一个模拟挖矿过程的粗略可视化 gif 动图：

[<img src="../../images/technical_block_nonce_nonce-mining.gif" alt="Animated gif of the nonce being used during the mining process." width="600" height="420" />](../../images/technical_block_nonce_nonce-mining.gif)

如果这些 gif 动图还不能解释一切，我就不知道还有什么能解释了。

## 资源

* [Why didn't Satoshi make the nonce space larger?](https://bitcoin.stackexchange.com/questions/32603/why-didnt-satoshi-make-the-nonce-space-larger)
* [Determining a Block's Extranonce Value](https://bitcoin.stackexchange.com/questions/36455/determining-a-blocks-extranonce-value)