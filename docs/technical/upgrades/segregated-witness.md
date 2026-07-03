<img src="../../images/icons_loader-2.svg" alt="Loading Tool" style="height:32px; width:32px;" />

* [BIP 141: Segregated Witness (Consensus layer)](https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki)
* [BIP 143: Transaction Signature Verification for Version 0 Witness Program](https://github.com/bitcoin/bips/blob/master/bip-0143.mediawiki)
* [BIP 144: Segregated Witness (Peer Services)](https://github.com/bitcoin/bips/blob/master/bip-0144.mediawiki)

[<img src="../../images/icons_segwit.svg" alt="SegWit Logo" width="3923" height="995" style="width: 24px; height: 24px;" />](https://static.learnmeabitcoin.com/assets/icons/segwit.svg)

Segregated Witness (SegWit) 是 2017 年激活的比特币软件的一次重大升级（区块 [481,824](/explorer/block/0000000000000000001c8018d9cb3b742ef25114f27563e3fc4a1902167f9893)）。

主要变化是**新的交易结构**、**区块大小的增加**以及**新增的地址格式**。

**本页列出了 Segregated Witness 升级中引入的*技术变化*。** 有关该升级发生的原因和过程的介绍，请查看 [SegWit 初学者指南](/docs/beginners/guide/segwit.md)。

## 动机

为什么要引入 Segregated Witness？

引入 Segregated Witness 的首要原因是为了**修复交易延展性 (transaction malleability)**。

在 Segregated Witness 之前，[旧版交易](/docs/technical/transaction.md#example-legacy)的 [txid](/docs/technical/transaction/input/txid.md) 是从*整个交易数据*（包括[签名](/docs/technical/keys/signature.md)）中创建的。

然而，可以[调整交易内部的签名](/docs/technical/keys/signature.md#legacy-step-6)并使它们保持有效，这会对 txid 产生连锁反应。这意味着有人可以在你将交易发送到[网络](/docs/technical/networking.md)后更改你交易的 txid。

这带来的问题是，任何依赖于此 txid 的交易（即在交易仍在[内存池](/docs/technical/mining/memory-pool.md)中时花费其[输出](/docs/technical/transaction/output.md)的交易）都将变得无效。换句话说，矿工可以“取消”内存池交易的[后代](/docs/technical/mining/memory-pool.md#descendants)并阻止它们被[开采](/docs/technical/mining.md)到区块中。

因此，Segregated Witness 升级中的主要变化是对交易数据结构的修改，使得签名不再包含在 txid 计算中，从而使 txid 变得可靠，并允许你在交易仍处于内存池中时自信地花费它们的输出。

这种新的交易数据同时允许区块大小的增加，这就是为什么 Segregated Witness 在一次重大软件升级中作为**一系列变更**引入的原因。

## 技术变化

比特币发生了哪些变化？

以下是随着 Segregated Witness 升级在比特币中发生的所有**变化列表**。

我将从最重大的变化开始（开发者最可能遇到的变化），然后逐渐介绍较小的变化。

### 1. 交易结构

[<img src="../../images/diagrams_png_transaction-witness.png" alt="Diagram showing the new witness section of a transaction used for unlocking inputs." width="450" height="420" />](https://static.learnmeabitcoin.com/diagrams/png/transaction-witness.png)

主要变化是增加了新的 [SegWit 交易](/docs/technical/transaction.md#example-segwit)结构。

这些新的 SegWit 交易包含一个**新的 [witness](/docs/technical/transaction/witness.md) 部分**，该部分保存用于解锁升级中引入的[新锁定脚本](#locking-scripts)的解锁代码（即签名）。

因此，虽然旧版交易使用 [ScriptSig](/docs/technical/transaction/input/scriptsig.md) 字段来解锁输入，但 SegWit 交易现在使用新的 *witness* 部分来代替。

* 旧版锁定脚本（例如 [P2PKH](/docs/technical/script/p2pkh.md), [P2SH](/docs/technical/script/p2sh.md)）仍然需要使用 ScriptSig 字段进行解锁。只有新的锁定脚本（例如 [P2WPKH](/docs/technical/script/p2wpkh.md), [P2WSH](/docs/technical/script/p2wsh.md)）才使用新的 witness 字段进行解锁。
* 因此，不使用 witness 部分解锁输入的旧版交易仍然容易受到交易延展性的影响。

<img src="../../images/icons_tool.svg" alt="Tool Icon" style="width:20px; height:20px" /> 交易拆分器

随机示例

交易数据


* `0 bytes`
* `0 vbytes`

结果

```
 
```



0 secs

### 2. 交易大小计算

[<img src="../../images/diagrams_png_transaction-weight.png" alt="Diagram showing the size calculation of a transaction in terms of weight." width="699" height="197" />](https://static.learnmeabitcoin.com/diagrams/png/transaction-weight.png)

随着[新 witness 字段](#transaction-structure)的增加，交易还获得了一种**名为[重量 (weight)](/docs/technical/transaction/size.md#weight) 的新[大小](/docs/technical/transaction/size.md)计算方法**。

不同于纯粹根据字节数衡量交易大小，交易数据的不同部分被赋予了*特定的乘数*，从而使交易的某些部分比其他部分“重量更轻”：

|  |  |
| --- | --- |
| 旧版数据 (Legacy Data) | 字节数 x 4 |
| SegWit 数据 (Segwit Data) | 字节数 x 1 |

结果，SegWit 交易中的解锁代码比旧版交易中的解锁代码*重量更轻*，有效地为使用新 SegWit 交易的任何人提供了大小折扣（并降低了[手续费](/docs/technical/transaction/fee.md)成本）。

#### [虚拟字节 (vbytes)](/docs/technical/transaction/size.md#vbytes)

虚拟字节测量相当于*重量*测量，但使用不同的乘数：

|  |  |
| --- | --- |
| 旧版数据 (Legacy Data) | 字节数 x 1 |
| SegWit 数据 (Segwit Data) | 字节数 x 0.25 |

使用虚拟字节，旧版交易保持相同的大小计量，而新 SegWit 交易可以在“虚拟字节”方面与旧版交易的大小进行*对比*。

你通常会在[区块链浏览器](/explorer/)上看到虚拟字节测量，但在内部，比特币使用重量来确定一个[区块](/docs/technical/block.md)中可以容纳多少交易。

<img src="../../images/icons_tool.svg" alt="Tool Icon" style="width:20px; height:20px" /> 交易拆分器

随机示例

交易数据


* `0 bytes`
* `0 vbytes`

结果

```
 
```



0 secs

### 3. 区块大小增加

[<img src="../../images/diagrams_png_block-weight.png" alt="Diagram showing the block size limit in terms of weight." width="660" height="310" />](https://static.learnmeabitcoin.com/diagrams/png/block-weight.png)

为交易使用[新的重量计算方法](#transaction-size-calculation)后，[区块大小限制](/docs/technical/block.md#weight)从 **1,000,000 *字节*** 更改为 **4,000,000 *重量单位***。

这导致区块大小增加，平均比旧的区块大小限制**大 4 倍**。

鉴于交易数据中总是包含*一些旧版数据*以及新的 SegWit 数据，*实际的*区块大小增加在平均水平上约为 **1,700,000 至 2,000,000 *字节***（具体取决于区块中包含 of 交易组成）。

### 4. 锁定脚本

引入了两种新的锁定脚本模式，以利用[新的 witness 字段](#transaction-structure)解锁特定类型的输出：

1. [P2WPKH](/docs/technical/script/p2wpkh.md)
   [<img src="../../images/diagrams_png_script-p2wpkh.png" alt="A diagram showing the structure of a P2WPKH." width="858" height="299" />](https://static.learnmeabitcoin.com/diagrams/png/script-p2wpkh.png)
2. [P2WSH](/docs/technical/script/p2wsh.md)
   [<img src="../../images/diagrams_png_script-p2wsh.png" alt="A diagram showing the structure of a P2WSH." width="964" height="379" />](https://static.learnmeabitcoin.com/diagrams/png/script-p2wsh.png)

它们在功能上与旧版 [P2PKH](/docs/technical/script/p2pkh.md) 和 [P2SH](/docs/technical/script/p2sh.md) 锁定脚本相同。

主要区别在于 P2WPKH 和 P2WSH 是使用交易的 [witness](/docs/technical/transaction/witness.md) 区域而不是 [ScriptSig](/docs/technical/transaction/input/scriptsig.md) 解锁的。

**新的 P2WPKH 和 P2WSH 锁定脚本*不*使用传统的 [Script](/docs/technical/script.md) 语言进行锁定和解锁。** 它们使用固定的字节结构，并有自己的硬编码执行方法。但尽管如此，它们在功能上仍与 P2PKH 和 P2SH 相同。

<img src="../../images/icons_tool.svg" alt="Tool Icon" style="width:20px; height:20px" /> 脚本

随机 ScriptPubKey
随机 ScriptSig

十六进制


`0 bytes`

ASM
类型

 非标准
 P2PK (Pay To Pubkey)
 P2PKH (Pay To Pubkey Hash)
 P2MS (Multisig)
 P2SH (Pay To Script Hash)
 P2WPKH (Pay To Witness Pubkey Hash)
 P2WSH (Pay To Witness Script Hash)
 P2TR (Pay To Taproot)
 OP_RETURN (Data)


地址`0 characters`



0 secs

### 5. 地址格式

[新的 P2WPKH 和 P2WSH 锁定脚本](#locking-scripts)使用新的 **[Bech32](/docs/technical/keys/bech32.md) 地址格式**。

这些 Bech32 地址允许**更好的错误检测**，且**更易于抄写**。

<img src="../../images/icons_tool.svg" alt="Tool Icon" style="width:20px; height:20px" /> 地址 (Bech32)

随机生成


ScriptPubKey

Version
 `OP_0` (P2WPKH or P2WSH)
 `OP_1` (P2TR)

Data
(public key hash or script hash)
`0 bytes`

Hex

`0 bytes`
`Type:`

Network
 Mainnet
 Testnet
 Regtest

Address

Bech32 encoding of the ScriptPubKey

`0 characters`



0 secs

因此，旧版 P2PKH 和 P2SH 锁定脚本继续使用 [Base58](/docs/technical/keys/base58.md) 地址，而新的 P2WPKH 和 P2WSH 锁定脚本使用 Bech32 地址来代替。

### 6. 签名算法

[新的 P2WPKH 和 P2WSH 锁定脚本](#locking-scripts)还使用了一种**[新的签名算法](/docs/technical/keys/signature.md#segwit-algorithm)**。

这种新的“SegWit 签名算法”旨在比[旧版签名算法](/docs/technical/keys/signature.md#legacy-algorithm)更高效。

所以现在，创建签名来解锁 P2WPKH 和 P2WSH 锁定脚本的过程与为旧版锁定脚本（例如 P2PKH 和 P2SH）创建签名的过程是不同的。

**旧版签名算法和新 SegWit 签名算法都仍然使用 [ECDSA](/docs/technical/cryptography/elliptic-curve/ecdsa.md)。** 只是当你想解锁 P2WPKH 和 P2WSH 锁定脚本时，*准备用于签名的交易数据*的方法是不同的。

### 7. wTXID 承诺

[<img src="../../images/diagrams_png_block-wtxid-commitment.png" alt="Diagram showing the wtxid commitment inside a block." width="810" height="499" />](https://static.learnmeabitcoin.com/diagrams/png/block-wtxid-commitment.png)

由于[新的 SegWit 交易](#transaction-structure)包含不再属于 [txid](/docs/technical/transaction/input/txid.md) 一部分的数据，因此需要通过 [wTXID 承诺](/docs/technical/transaction/wtxid.md#commitment)将此新见证数据*提交*到区块。

所以，除了 txid（不包括 SegWit 交易中的新字段）之外，每个交易还具有一个 [wtxid](/docs/technical/transaction/wtxid.md)，该 id 是通过对 SegWit 交易中的所有数据（包括 SegWit 交易中的新字段）进行哈希运算计算得出的。

[<img src="../../images/diagrams_png_transaction-witness-wtxid.png" alt="Diagram showing the wTXID being calculated from the raw transaction data including the new segwit fields." width="764" height="367" />](https://static.learnmeabitcoin.com/diagrams/png/transaction-witness-wtxid.png)

<img src="../../images/icons_tool.svg" alt="Tool Icon" style="width:20px; height:20px" /> TXID

随机示例

交易数据

`0 bytes`


 显示详情



TXID (自然字节顺序)

内部在原始交易数据中使用

`0 bytes`

TXID (反向字节顺序)

在区块浏览器上搜索交易时外部使用

`0 bytes`



0 secs

<img src="../../images/icons_tool.svg" alt="Tool Icon" style="width:20px; height:20px" /> wTXID

随机示例

交易数据

`0 bytes`

wTXID (自然字节顺序)

`0 bytes`

wTXID (反向字节顺序)

使用 `bitcoin-cli` 命令时也称为交易“哈希”

`0 bytes`



0 secs

所以当构建区块时，矿工现在还将为区块中的所有 wtxid 计算一个 [merkle root](/docs/technical/block/merkle-root.md)，并通过 [Coinbase](/docs/technical/mining/coinbase-transaction.md) 交易中的 wTXID 承诺将该根哈希包含在区块中。

结果，这个 wTXID 承诺**防止任何人修改见证数据**用于区块中包含的交易。

* wtxid 被放入 Coinbase 交易中，因为它是区块中唯一可以包含新附加数据而不会引起[硬分叉](/docs/technical/blockchain/hard-fork.md)的部分。
* 鉴于[旧版交易](/docs/technical/transaction.md#example-legacy)不包含任何新 SegWit 字段，其 wtxid 将与其 txid 相同。

### 8. 网络消息

当与[网络](/docs/technical/networking.md)上的其他节点通信时，你现在必须专门**请求节点发送 SegWit 交易的完整交易数据**（即包括[新见证数据](#transaction-structure)）。

所以，在 [`getdata`](/docs/technical/networking.md#getdata) 消息中，*type* 字段本来是以下之一：

* `01000000 = MSG_TX`
* `02000000 = MSG_BLOCK`

要请求包括新见证数据在内的交易或区块，你需要使用以下 *type* 字段来代替：

* `01000040 = MSG_WITNESS_TX`
* `02000040 = MSG_WITNESS_BLOCK`

### 9. 其他

* 除了在[新交易大小计算](#transaction-size-calculation)期间旧版字节数乘以 4 外，旧版交易中的所有[签名](/docs/technical/keys/signature.md)操作（例如 `OP_CHECKSIG`, `OP_CHECKMULTISIG`, `OP_CHECKSIGVERIFY`, `OP_CHECKMULTISIGVERIFY`）也会乘以 4。这在计算区块中包含多少个签名操作时很重要，因为一个区块具有 [**80,000** 个签名操作的限制](/docs/technical/mining/candidate-block.md#requirement-sigops) (sigops)。

## 总结

正如你所看到的，Segregated Witness 一次性为比特币引入了**多项技术变革**。

其中的许多改变起初似乎有些不必要地复杂，但那是因为需要技术性权衡才能将这些变化作为[软分叉而不是硬分叉](/docs/beginners/guide/segwit.md#why-were-the-changes-implemented-in-this-way)引入。

然而，根据你所从事的项目，你可能不需要在你的软件中实现所有的变化；你可以仅实现与你的工具相关的改变（例如，如果你在开发钱包，你可能不需要担心新的[网络消息](#network-messages)）。

不过，了解已发生的所有变化以及它们如何结合在一起构成比特币自发布以来最大的一次升级，还是非常有用的。

最初实现对 SegWit 的支持可能看起来是一项艰巨的技术挑战，但如果你按步骤逐步引入每一项更改，你最终会实现的。一步一步来。