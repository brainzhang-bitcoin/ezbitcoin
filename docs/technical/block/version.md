<img src="../../images/icons_loader-2.svg" alt="Loading Tool" style="height:32px; width:32px;" />

[<img src="../../images/diagrams_png_block-version.png" alt="Diagram showing the location of the nonce field inside the block header and how the last 29 bits are used to signal readiness for soft forks." width="639" height="404" />](../../images/diagrams_png_block-version.png)

矿工使用[区块头](../block.md#header)中 4 字节的 version（版本）字段来***指示 (signal)***对提议的[软分叉](../blockchain/soft-fork.md)的准备就绪状态。

版本号在软件中用于表示升级或添加新功能。然而，比特币是去中心化的，因此没有中央机构强制每个人升级到新版本的软件。因此，如果网络的大多数成员能提前对提议的更改达成一致，那将是最理想的。

所以 version 字段基本上用于对提议的软件升级进行“投票”。

> 尽管它们实际上并不是选票。任何占多数的矿工都可以开始实施新规则——他们不需要在区块中表明，甚至不需要告诉任何人。version 字段所做的是提供一种指示准备就绪状态的方法，从而可以找到一个安全且协调的过渡点。
> 
> Pieter Wuille, [bitcoin.stackexchange.com](https://bitcoin.stackexchange.com/questions/50446/what-are-the-possible-version-bits-votes)

## 版本号

在 2015 年之前，版本号被递增以指示对新升级的就绪状态。这一直持续到版本号为 4：

* `0x00000001` = 原始软件
  + 激活高度: [0](/explorer/0#blockchain)
* `0x00000002` = [BIP 34](https://github.com/bitcoin/bips/blob/master/bip-0034.mediawiki): Coinbase 中的高度
  + 激活高度: [227,931](/explorer/227931#blockchain)
* `0x00000003` = [BIP 66](https://github.com/bitcoin/bips/blob/master/bip-0066.mediawiki): 严格的 DER 签名
  + 激活高度: [363,725](/explorer/363725#blockchain)
* `0x00000004` = [BIP 65](https://github.com/bitcoin/bips/blob/master/bip-0065.mediawiki): OP\_CHECKLOCKTIMEVERIFY
  + 激活高度: [388,381](/explorer/388381#blockchain)

当在给定时间段内开采的 *1000 个区块中有 950 个* 使用新的版本号时，这些升级就变成了永久性的。一旦这些升级处于激活状态，所有新区块就必须使用新的版本号（或更大值）。

此系统行之有效，但缺点是您一次只能指示**一项更改**。

由于这些升级，现在区块所需的最低版本号为 `0x00000004`。任何低于该值的版本号都将被网络上的节点拒绝。

## 版本位 (Version Bits)

在 2015 年，version 字段被更改为用作[位字段](../general/bytes.md#bit-field)，这允许矿工同时指示多达 29 个提议的新功能。

32 位 (4字节) version 字段中的不同[位](../general/bytes.md#bit)可以同时被指定为指示对不同[软分叉](../blockchain/soft-fork.md)的就绪状态。所以您要指示对特定升级的就绪状态，只需将特定位置为“开”（即将其设置为 **1**）。

随机示例

位字段 (Bit Field)

0

0

1

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



十六进制 (Hex)

0x

`4 bytes`





* **Version Bits:** 已启用

以下位已被用于升级：

* **位 0 (Bit 0):** [BIP 112](https://github.com/bitcoin/bips/blob/master/bip-0112.mediawiki): CHECKSEQUENCEVERIFY
  + 示例: `0b00100000000000000000000000000001`
  + 激活高度: [419,328](/explorer/419328#blockchain)
* **位 1 (Bit 1):** [BIP 141](https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki): SegWit
  + 示例: `0b00100000000000000000000000000010`
  + 激活高度: [481,824](/explorer/481824#blockchain)
* **位 2 (Bit 2):** [BIP 341](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki): Taproot
  + 示例: `0b00100000000000000000000000000100`
  + 激活高度: [709,632](/explorer/709632#blockchain)

要使用“版本位”进行指示，您必须将前 3 位设置为 `0b001`（如 [BIP 9](https://github.com/bitcoin/bips/blob/master/bip-0009.mediawiki) 中所规定）。这只是一个要求，表明您正在使用 version 字段作为指示状态的位字段。所以这就是为什么您同时最多只能指示 29 个不同的升级（32 - 3 = 29 位）。

每个提案都有其自己的指示时间段，其中在特定窗口内必须有特定数量的区块指示该升级才能使其被激活。例如，在 [Taproot 升级](../upgrades/taproot.md)期间，在 2016 个区块的[target](../mining/target.md)调整周期内，必须有 90% 的区块指示该升级（从 2021 年 4 月 24 日开始到 2021 年 8 月 11 日结束），这最终确实发生了，并且部署在区块高度 [709,632](/explorer/709632#blockchain) 处激活。

您可以通过 `bitcoin-cli getblockchaininfo` 查看过去和当前投票支持的升级。

提议升级的所有位分配列表可以在 [BIP 9 assignments](https://github.com/bitcoin/bips/blob/master/bip-0009/assignments.mediawiki) 页面上找到，但我认为它不经常更新。

## 示例

以下是您在区块链历史中会发现的版本号的一些示例。

* `0x00000001` - 在区块高度 [200,000](/explorer/200000#blockchain) 之前的绝大多数区块使用此版本号。
  + 示例: [000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f](/explorer/block/000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f) (高度 [0](/explorer/0#blockchain))
* `0x00000002` - 在 [227,931](/explorer/227931#blockchain) 到 [363,724](/explorer/363724#blockchain) 之间的绝大多数区块使用此版本号。
  + 示例: [000000000000024b89b42a942fe0d9fea3bb44ab7bd1b19115dd6a759c0808b8](/explorer/block/000000000000024b89b42a942fe0d9fea3bb44ab7bd1b19115dd6a759c0808b8) (高度 [227,931](/explorer/227931#blockchain))
* `0x00000003` - 在 [363,725](/explorer/363725#blockchain) 到 [388,380](/explorer/388380#blockchain) 之间的绝大多数区块使用此版本号。
  + 示例: [00000000000000000379eaa19dce8c9b722d46ae6a57c2f1a988119488b50931](/explorer/block/00000000000000000379eaa19dce8c9b722d46ae6a57c2f1a988119488b50931) (高度 [363,725](/explorer/363725#blockchain))
* `0x00000004` - 在 [388,381](/explorer/388381#blockchain) 到大约 [411,000](/explorer/411000#blockchain) 之间的绝大多数区块使用此版本号。
  + 示例: [000000000000000004c2b624ed5d7756c508d90fd0da2c7c679febfa6c4735f0](/explorer/block/000000000000000004c2b624ed5d7756c508d90fd0da2c7c679febfa6c4735f0) (高度 [388,381](/explorer/388381#blockchain))

在大约区块高度 [411,000](/explorer/411000#blockchain) 之后，version 字段开始更频繁地被用作位字段（而不是一个简单的数字）。这就是为什么版本“数字”看起来要大得多的原因，因为前 3 位现在被设置为 `0b001`。

* `0x20000000` - 使用版本位，但没有指示任何具体的升级。
  + 版本位 (Version Bits): `0b00100000000000000000000000000000`
  + 示例: [000000000000000005025d88492c54a51ac3bccaaa15c12a05aee16a28d6b294](/explorer/block/000000000000000005025d88492c54a51ac3bccaaa15c12a05aee16a28d6b294) (高度 [410,370](/explorer/410370#blockchain))
* `0x20000001` - 用于指示 CSV 升级的版本位。
  + 版本位 (Version Bits): `0b00100000000000000000000000000001`
  + 示例: [000000000000000004983f04183f2a6ae7f1cdf6ddb8f4b3f79e39e14392db4c](/explorer/block/000000000000000004983f04183f2a6ae7f1cdf6ddb8f4b3f79e39e14392db4c) (高度 [416,498](/explorer/416498#blockchain))
* `0x20000002` - 用于指示 [SegWit 升级](../upgrades/segregated-witness.md)的版本位。
  + 版本位 (Version Bits): `0b00100000000000000000000000000010`
  + 示例: [0000000000000000001094a0145695e4228c21cbbc6be40507f728c6b7d6f16a](/explorer/block/0000000000000000001094a0145695e4228c21cbbc6be40507f728c6b7d6f16a) (高度 [471,329](/explorer/471329#blockchain))
* `0x20000004` - 用于指示 [Taproot 升级](../upgrades/taproot.md)的版本位。
  + 版本位 (Version Bits): `0b00100000000000000000000000000100`
  + 示例: [00000000000000000004f065fae967b93540f321076684fe926d4e7bfbcd77ab](/explorer/block/00000000000000000004f065fae967b93540f321076684fe926d4e7bfbcd77ab) (高度 [703,353](/explorer/703353#blockchain))

这里有一些不时弹出的“非标准”版本号：

* `0x30000000` - 我相信这可能是一个非官方的位，用于表明对 2 MB 区块的支持。它在区块 [398,364](/explorer/398364#blockchain) 和 [476,482](/explorer/476482#blockchain) 之间出现了 2,058 次。
  + 版本位 (Version Bits): `0b00110000000000000000000000000000`
  + 示例: [0000000000000000018c393bb66dac52e1a2131ab2332b4d6e2caed463209892](/explorer/block/0000000000000000018c393bb66dac52e1a2131ab2332b4d6e2caed463209892) (高度 [414,996](/explorer/414996#blockchain))
* `0x08000004` - 这是 [适应性区块大小 (adaptive block sizes)](https://github.com/bitpay/bips/blob/master/bip-adaptiveblocksize.mediawiki) 的另一个非官方指示。它在区块 [416,832](/explorer/416832#blockchain) 和 [455,757](/explorer/455757#blockchain) 之间出现了 39 次。
  + 版本位 (Version Bits): `0b00001000000000000000000000000100`
  + 示例: [00000000000000000479bbbf51d485ddc7b161998b6f54049e576b09fd72e363](/explorer/block/00000000000000000479bbbf51d485ddc7b161998b6f54049e576b09fd72e363) (高度 [416,832](/explorer/416832#blockchain))

## 当前默认值

区块头中的默认版本当前为：

```
0b00100000000000000000000000000000
```

其十六进制形式为：

```
0x20000000
```

这表明您正在使用“版本位”（即前 3 位设置为 `0b001`），但没有指示任何提议的新功能（所有其他位都设置为零）。

version 字段中的第一*位 (bit)*永远不能为 1，因为这将指示一个负数，这在比特币中是无效的。这是因为比特币对 [uint256](https://github.com/bitcoin/bitcoin/blob/master/src/arith_uint256.cpp) 值使用了一种自定义编码。

```
This bit cannot be set to 1, or the version will be invalid:

00000000000000000000000000000000
↑
```

## Extra Nonce

对您在 version 字段中放入什么值并没有太多的限制（除了它必须是最低 `0x00000004`，并且首位不能是 `1` 之外），因此矿工有时会在挖矿时将其用作 [extra nonce](nonce.md#extranonce)。

这就是为什么大约自区块高度 [600,000](/explorer/600000#blockchain) 以来（此前也有，但此后更多），您经常在区块头中看到一些“奇怪”的版本号，它们并不对应任何提议的升级。例如：

* `0x2844a000` - 使用包含一些被设置了的位的*版本位*，但它们都不对应于任何提议的升级。
  + 版本位 (Version Bits): `0b00101000010001001010000000000000`
  + 示例: [00000000000000000479bbbf51d485ddc7b161998b6f54049e576b09fd72e363](/explorer/block/00000000000000000479bbbf51d485ddc7b161998b6f54049e576b09fd72e363) (高度 [791,617](/explorer/791617#blockchain))

再次强调，这些版本号并不表示什么特定的信息；它们只是被矿工调整了，以便能够继续对当前的区块进行[哈希运算](../cryptography/hash-function.md)，而无需完全重建区块。

## 资源

* [Version bits FAQ for miners](https://bitcoincore.org/en/2016/06/08/version-bits-miners-faq/)
* [What restrictions does the version field in the block header have?](https://bitcoin.stackexchange.com/questions/117530/what-restrictions-does-the-version-field-in-the-block-header-have)
* [What are version bits?](https://bitcoin.stackexchange.com/questions/39216/what-are-version-bits)