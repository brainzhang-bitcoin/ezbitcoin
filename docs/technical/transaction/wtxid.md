<img src="../../images/icons_loader-2.svg" alt="Loading Tool" style="height:32px; width:32px;" />

wTXID 类似于 [TXID](/docs/technical/transaction/input/txid.md)，但 wTXID 包含了交易（[transaction](/docs/technical/transaction.md)）的 [witness](/docs/technical/transaction/witness.md) 数据。

例如：

**wTXID** 是对所有交易数据进行 [HASH256](/docs/technical/cryptography/hash-function.md#hash256) 计算的结果，*包括* [marker](/docs/technical/transaction.md#structure-marker)、[flag](/docs/technical/transaction.md#structure-flag) 和 [witness](/docs/technical/transaction.md#structure-witness)：

[<img src="../../images/diagrams_png_transaction-witness-wtxid.png" alt="Diagram showing the wTXID being calculated from the raw transaction data including the marker, flag, and witness." width="764" height="367" />](https://static.learnmeabitcoin.com/diagrams/png/transaction-witness-wtxid.png)

<img src="../../images/icons_tool.svg" alt="Tool Icon" style="width:20px; height:20px" /> wTXID

随机示例

交易数据

`0 bytes`

wTXID (自然字节序)

`0 bytes`

wTXID (反向字节序)

在使用 `bitcoin-cli` 命令时也被称为交易“哈希（hash）”

`0 bytes`



0 secs

而 **TXID** 是对除 marker、flag 和 witness *之外* 的所有交易数据进行 HASH256 计算的结果：

[<img src="../../images/diagrams_png_transaction-witness-txid.png" alt="Diagram showing the TXID being calculated from the raw transaction data excluding the marker, flag, and witness." width="764" height="367" />](https://static.learnmeabitcoin.com/diagrams/png/transaction-witness-txid.png)

<img src="../../images/icons_tool.svg" alt="Tool Icon" style="width:20px; height:20px" /> TXID

随机示例

交易数据

`0 bytes`


 显示详情


TXID (自然字节序)

在原始交易数据内部使用

`0 bytes`

TXID (反向字节序)

在区块链浏览器上搜索交易时在外部使用

`0 bytes`



0 secs

上面的图表没有显示 marker 和 flag 字段。

## 示例

如何创建 wTXID？

从技术角度来看，wTXID 是通过对序列化原始交易的以下字段进行[哈希](/docs/technical/cryptography/hash-function.md)计算得到的：

```
wTXID = HASH256([version][marker][flag][inputs][outputs][witness][locktime])
```

### SegWit 交易

这是一笔 SegWit 交易的原始交易数据。我高亮标记了新的 SegWit 字段：

```
01000000000101438afdb24e414d54cc4a17a95f3d40be90d23dfeeb07a48e9e782178efddd8890100000000fdffffff020db9a60000000000160014b549d227c9edd758288112fe3573c1f85240166880a81201000000001976a914ae28f233464e6da03c052155119a413d13f3380188ac024730440220200254b765f25126334b8de16ee4badf57315c047243942340c16cffd9b11196022074a9476633f093f229456ad904a9d97e26c271fc4f01d0501dec008e4aae71c2012102c37a3c5b21a5991d3d7b1e203be195be07104a1a19e5c2ed82329a56b431213000000000
```

**TXID** 是对除 marker、flag 和 witness 之外的所有交易数据进行 HASH256 计算的结果：

[c06aaaa2753dc4e74dd4fe817522dc3c126fd71792dd9acfefdaff11f8ff954d](/explorer/tx/c06aaaa2753dc4e74dd4fe817522dc3c126fd71792dd9acfefdaff11f8ff954d)

而 **wTXID** 则是包含 marker、flag 和 witness 在内的所有交易数据的 HASH256 计算结果：

`f12d56f2234e809129dbf59392961bbe7a89b6250651f6aea7852cc00ced63ff`

你可以通过手动将数据输入 HASH256 来亲自验证这一点：

<img src="../../images/icons_tool.svg" alt="Tool Icon" style="width:20px; height:20px" /> HASH256

随机交易数据

随机区块头

数据 (十六进制)

`0 bytes`


<img src="../../images/icons_hash-function.svg" alt="Hash Function Icon" style="width:52px; height:52px" />
SHA-256

<img src="../../images/icons_hash-function.svg" alt="Hash Function Icon" style="width:52px; height:52px" />
SHA-256

HASH256

SHA-256(SHA-256(data))

`0 bytes`



0 secs

<img src="../../images/icons_tool.svg" alt="Tool Icon" style="width:20px; height:20px" /> 字节反转 (Reverse Bytes)

随机示例

字节

`0 bytes`

反转后

`0 bytes`


 显示详情



0 secs

**字节顺序。** 不要忘记 TXIDs 和 wTXIDs 是以[反向字节序](/docs/technical/general/byte-order.md#reverse-byte-order)显示的，因此 HASH256 的初始结果将是自然字节序（这意味着该结果起初看起来是反的）。

### 旧版交易

非 SegWit 交易将具有相同的 TXID 和 wTXID。

例如，这是一笔旧版交易的原始交易数据：

```
0100000001ba1e48633efb7397536c3b45582cb763b1903b1364865f6de0f53387d306c87d010000006b483045022100df50e78ee42725165eceed6e6e1c534936015d3ef9e410d301de682a3655012f02203d21199bc19d982926fcf6bfe26773f4a0b2befdabb742542469f04e739764cb012103668b0f35effa223f001fb1c39d61bde513d5c6291b84227e84fd3e7daf0e3a6afeffffff02ce6d6002000000001976a9144ccb1bfd0099bf5ba2e2799a9f444f9583a74ce088ac35102408000000001976a914e5555373c7d95bb6a2cfcf7e9ffb3fcb5a305ba988ac711a0600
```

这就是 **TXID**：

[25346687d5d10239c25a88193c97228327826a4ff66a36c4ba7e038f3e2ae9ed](/explorer/tx/25346687d5d10239c25a88193c97228327826a4ff66a36c4ba7e038f3e2ae9ed)

并且鉴于旧版交易不包含 marker、flag 或 witness，它将具有相同的 **wTXID**：

`25346687d5d10239c25a88193c97228327826a4ff66a36c4ba7e038f3e2ae9ed`

<img src="../../images/icons_tool.svg" alt="Tool Icon" style="width:20px; height:20px" /> HASH256

随机交易数据

随机区块头

数据 (十六进制)

`0 bytes`


<img src="../../images/icons_hash-function.svg" alt="Hash Function Icon" style="width:52px; height:52px" />
SHA-256

<img src="../../images/icons_hash-function.svg" alt="Hash Function Icon" style="width:52px; height:52px" />
SHA-256

HASH256

SHA-256(SHA-256(data))

`0 bytes`



0 secs

<img src="../../images/icons_tool.svg" alt="Tool Icon" style="width:20px; height:20px" /> 字节反转 (Reverse Bytes)

随机示例

字节

`0 bytes`

反转后

`0 bytes`


 显示详情



0 secs

你可以通过运行 `bitcoin-cli getrawtransaction <txid> 1` 来查找交易的 wTXID。wTXID 将等于 "hash" 字段，因为这个 "hash" 是整个交易数据的 HASH256（反向字节序），目前它等于 wTXID。

## wTXID 承诺 (wTXID Commitment)

将交易的 witness 数据承诺到区块中

[<img src="../../images/diagrams_png_block-wtxid-commitment.png" alt="Diagram showing segwit data being committed to the block via the wtxid commitment in the scriptpubkey of the coinbase transaction." width="810" height="499" />](https://static.learnmeabitcoin.com/diagrams/png/block-wtxid-commitment.png)

wTXIDs 用于通过 **witness 默克尔根哈希 (witness root hash)** 将 SegWit 交易中的新数据*承诺*到区块中。

> 承诺（Commitment）用于将一方绑定到一个值上，使他们无法通过改动为其他消息来获取某种不正当的优势。
> 
> —— [cryptography.fandom.com](https://cryptography.fandom.com/wiki/Commitment_scheme)

例如，所有的旧版交易数据都是通过创建区块中所有 TXIDs 的[默克尔根](/docs/technical/block/merkle-root.md)承诺到[区块头](/docs/technical/block.md#header)中的。

然而，TXIDs 不包括 marker、flag 和 witness 数据。因此，对于自 [SegWit](/docs/technical/upgrades/segregated-witness.md) 升级以来的所有区块，我们还会**为所有 wTXIDs 创建一个默克尔根**，并通过创建一个 *witness root hash* 将其承诺到区块中。

这个 *witness root hash* 与 [*witness reserved value*](/docs/technical/transaction/witness.md#witness-reserved-value) 一起进行 HASH256 计算，从而创建 **wTXID 承诺**。它被放置在 [Coinbase](/docs/technical/mining/coinbase-transaction.md) 交易的其中一个 [outputs](/docs/technical/transaction/output.md) 的 [ScriptPubKey](/docs/technical/transaction/output/scriptpubkey.md) 中。

因此，现在在区块中放置了对所有新 SegWit 交易数据的承诺。如果有人试图更改区块中任何交易的 witness 数据内容，它将与 wTXID 承诺不匹配，该区块将变为无效。

wTXIDs 最终用于防止任何人篡改区块中包含的新隔离见证（segregated witness）交易数据。

### 示例

高度为 [553,724](/explorer/block/0000000000000000002849bd7ea6df81fa2f07652af0600ffa0f2b0bc47d736c) 的区块包含以下 4 笔交易：

[2d4cdcd29d0004c762790b579bc2541da788f042031fa87fc27e402244080394](/explorer/tx/2d4cdcd29d0004c762790b579bc2541da788f042031fa87fc27e402244080394)
[d367b86c0fa5cf0b7a202c41fdbb2e4e78314d50fdc12654b499bf33062f2f86](/explorer/tx/d367b86c0fa5cf0b7a202c41fdbb2e4e78314d50fdc12654b499bf33062f2f86)
[76d11f7e4a480dfb3168537299cba66ff32c53dc3f5c16223eeaec1e1f1c6ce6](/explorer/tx/76d11f7e4a480dfb3168537299cba66ff32c53dc3f5c16223eeaec1e1f1c6ce6)
[e51de361009ef955f182922647622f9662d1a77ca87c4eb2fd7996b2fe0d7785](/explorer/tx/e51de361009ef955f182922647622f9662d1a77ca87c4eb2fd7996b2fe0d7785)

前三笔是 SegWit 交易，因此它们包含无法仅通过其 TXIDs 承诺到区块头的 witness 数据。

以下是每笔交易的 wTXIDs：

`0000000000000000000000000000000000000000000000000000000000000000`
`8700d546b39e1a0faf34c98067356206db50fdef24e2f70b431006c59d548ea2`
`c54bab5960d3a416c40464fa67af1ddeb63a2ce60a0b3c36f11896ef26cbcb87`
`e51de361009ef955f182922647622f9662d1a77ca87c4eb2fd7996b2fe0d7785`

在计算 witness root hash 时，Coinbase 交易的 wTXID 必须设置为全零。这是因为它最终将在其内部包含承诺，因此这样可以避免[循环引用 (circular reference)](https://en.wikipedia.org/wiki/Circular_reference)。

最后一笔交易是非 SegWit 交易，因此其 wTXID 与其 TXID 相同。

如果我们从所有这些 wTXIDs 中创建一个默克尔根，我们就得到了 **witness root hash**：

```
witness root hash: dbee9a868a8caa2a1ddf683af1642a88dfb7ac7ce3ecb5d043586811a41fdbf2
```

<img src="../../images/icons_tool.svg" alt="Tool Icon" style="width:20px; height:20px" /> 默克尔根 (Merkle Root)

随机示例

区块

TXID 列表

由 *空格*、*逗号* 或 *换行符* 分隔的 TXID 列表。引号和括号会被忽略。

TXID 应该以 [反向字节序](/docs/technical/general/byte-order.md#reverse-byte-order)（如它们在区块链浏览器上显示的那样）输入，但在计算默克尔根之前，它们会被转换为 [自然字节序](/docs/technical/general/byte-order.md#natural-byte-order)。



TXIDs (0)
 

默克尔根 (自然字节序)

哈希函数输出的字节顺序

默克尔根 (反向字节序)

区块链浏览器上显示的字节顺序



0 secs

现在，如果我们查看 [Coinbase 交易的 input](/explorer/tx/2d4cdcd29d0004c762790b579bc2541da788f042031fa87fc27e402244080394#input-0) 内部，我们会找到 **witness reserved value**：

```
witness reserved value: 0000000000000000000000000000000000000000000000000000000000000000
```

最后，如果我们拼接并对 *witness root hash* 和 *witness reserved value* 进行 HASH256 计算，我们就得到了 **wTXID 承诺**：

```
wTXID commitment = HASH256(witness root hash | witness reserved value)
wTXID commitment = 6502e8637ba29cd8a820021915339c7341223d571e5e8d66edd83786d387e715
```

<img src="../../images/icons_tool.svg" alt="Tool Icon" style="width:20px; height:20px" /> HASH256

随机交易数据

随机区块头

数据 (十六进制)

`0 bytes`


<img src="../../images/icons_hash-function.svg" alt="Hash Function Icon" style="width:52px; height:52px" />
SHA-256

<img src="../../images/icons_hash-function.svg" alt="Hash Function Icon" style="width:52px; height:52px" />
SHA-256

HASH256

SHA-256(SHA-256(data))

`0 bytes`



0 secs

这个 wTXID 承诺被放置在 Coinbase 交易的*其中一个*输出的 ScriptPubKey 中。如果我们检查该区块的 Coinbase 交易的 [输出 1 (output 1)](/explorer/tx/2d4cdcd29d0004c762790b579bc2541da788f042031fa87fc27e402244080394#output-1) 的 ScriptPubKey，我们会找到以下脚本：

OP\_RETURN  
OP\_PUSHBYTES\_36  
aa21a9ed6502e8637ba29cd8a820021915339c7341223d571e5e8d66edd83786d387e715

你会看到 wTXID 承诺包含在该数据推送的最后 32 个字节中。

* 前 4 个字节 `aa21a9ed` 是一个固定头部，用于标识该输出包含 wTXID 承诺。
* 接下来的 32 个字节 `6502e8637ba29cd8a820021915339c7341223d571e5e8d66edd83786d387e715` 就是我们刚刚计算出的同一个 wTXID 承诺。

自 SegWit 升级以来的所有 Coinbase 交易都必须包含这个对 witness 数据的承诺。它们都必须包含一个具有以下脚本模式的输出：以 `OP_RETURN` 开始，后跟一个包含 4 字节头部和接下来的 32 字节 wTXID 承诺的 `OP_PUSHBYTES_36`。

wTXID 承诺可以包含在 Coinbase 交易的*任何*输出中。如果由于某种原因有多个符合此结构的输出，包含此 wTXID 承诺结构的最大[输出索引号](/docs/technical/transaction/input/vout.md)将被视为最终承诺。

## 使用

wTXIDs 在比特币中是如何使用的？

wTXIDs 仅在比特币内部用于为交易的新 SegWit 字段创建承诺。

> wTXID 仅用于计算 Witness 默克尔根，并在 Coinbase 中进行承诺。
> 
> —— Pieter Wuille，[bitcoin.stackexchange.com](https://bitcoin.stackexchange.com/questions/55337/segwit-and-previous-hash-txid-or-wtxid-or-either/55339#55339)

因此，你不会使用 wTXID 来在[区块链](/docs/technical/blockchain.md)中查找交易。

**你仍然使用 [TXID](/docs/technical/transaction/input/txid.md) 来在区块链中查找交易。** TXID 仍然是交易的唯一标识符，因为它依然哈希了交易的*效果*（将代币从已有的 [outputs](/docs/technical/transaction/output.md) 移动到新的输出中），这对于每笔交易来说始终是唯一的。[witness](/docs/technical/transaction/witness.md) 数据仅对于交易*验证*（解锁 inputs）重要，这并不会让交易数据变得比它原本的程度更具唯一性。

> 交易内的签名实际上并不描述交易的效果。一笔交易是在移动代币、重新分配它们。但签名的存在只是为了证明该交易是经过授权的，它并不会改变其效果。
> 
> —— Pieter Wuille，[SF Bitcoin Developers](https://youtu.be/NOYNZB5BCHM?t=113)

## 资源

* [BIP 141](https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki)
* [Why include the Segregated Witness Merkle Root in the input field of the coinbase transaction?](https://bitcoin.stackexchange.com/questions/58414/why-include-the-segregated-witness-merkle-root-in-the-input-field-of-the-coinbas)