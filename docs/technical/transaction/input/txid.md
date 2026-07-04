<img src="../../../images/icons_loader-2.svg" alt="Loading Tool" style="height:32px; width:32px;" />

[<img src="../../../images/diagrams_png_transaction-txid.png" alt="Diagram showing how a TXID is the hash of a transaction." width="764" height="276" />](../../../images/diagrams_png_transaction-txid.png)

TXID（交易 ID）是**比特币交易（[transaction](../../transaction.md)）的唯一标识引用**。

它们用于在[区块链浏览器](/explorer/)中查找特定的交易。例如：

* [f4184fc596403b9d638783cf57adfe4c75c605f6356fbc91338530e9831e9e16](/explorer/tx/f4184fc596403b9d638783cf57adfe4c75c605f6356fbc91338530e9831e9e16) — 2009 年给 Hal Finney 的有史以来第一笔比特币交易。
* [a1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d](/explorer/tx/a1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d) — 2010 年花费 10,000 BTC 的[比萨交易](https://bitcointalk.org/index.php?topic=137.0)。
* [4ce18f49ba153a51bcda9bb80d7f978e3de6e81b5fc326f00465464530c052f4](/explorer/tx/4ce18f49ba153a51bcda9bb80d7f978e3de6e81b5fc326f00465464530c052f4) — 包含我因制作本网站而收到的第一笔捐赠的交易。

TXID 中的字母和数字没有特殊的含义。它们只是一组看起来随机的 32 [字节](../../general/bytes.md)数据（表示为 64 个[十六进制](../../general/hexadecimal.md)字符）。但它们对每笔交易来说都是 *唯一* 的。

## 创建

如何创建一个 TXID？

[<img src="../../../images/diagrams_png_transaction-txid-structure.png" alt="Diagram showing how a TXID is created by HASH256'ing specific parts of raw transaction data." width="624" height="200" />](../../../images/diagrams_png_transaction-txid-structure.png)

TXID 是通过对交易数据进行[哈希](../../cryptography/hash-function.md)创建的。更确切地说，它是通过将交易数据的特定部分输入 SHA256 哈希函数，然后再次将结果进行 SHA256 哈希计算（这种双重 SHA256 哈希被称为 *HASH256*）来创建的。

* 对于 **[旧版交易](../../transaction.md#example-legacy)**，你对所有交易数据进行 [HASH256](../../cryptography/hash-function.md#hash256) 计算。
* 对于 **[SegWit 交易](../../transaction.md#example-segwit)**，你对除 [marker](../../transaction.md#structure-marker)、[flag](../../transaction.md#structure-flag) 和 [witness](../../transaction.md#structure-witness) 字段之外的所有交易数据进行 HASH256 计算。

因此，对于 SegWit 交易，[签名](../../keys/signature.md)不再包含在 TXID 中。

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

你在区块链浏览器上看到的 TXID 实际上是**[反向字节序](../../general/byte-order.md#reverse-byte-order)**的。这只是比特币的一个特点。

### 代码

TXID 的创建方式与[区块哈希](../../block/hash.md)相同。你只需对交易数据的正确部分进行 **HASH256** 计算即可创建 TXID：

```
require 'digest'

# ----------------
# transaction data
# ----------------
data = "0100000001c997a5e56e104102fa209c6a852dd90660a20b2d9c352423edce25857fcd3704000000004847304402204e45e16932b8af514961a1d3a1a25fdf3f4f7732e9d624c6c61548ab5fb8cd410220181522ec8eca07de4860a4acdd12909d831cc56cbbac4622082221a8768d1d0901ffffffff0200ca9a3b00000000434104ae1a62fe09c5f51b13905f07f06b99a2f7159b2225f374cd378d71302fa28414e7aab37397f554a7df5f142c21c1b7303b8a0626f1baded5c72a704f7e6cd84cac00286bee0000000043410411db93e1dcdb8a016b49840f8c53bc1eb68a382e97b1482ecad7b148a6909a5cb2e0eaddfb84ccf9744464f82e160bfa9b8b64f9d4c03f999b8643f656b412a3ac00000000"

# ----
# TXID
# ----

# Note: Don't put the transaction data into the hash function as a string.
#       Convert it from hexadecimal to raw bytes first.

# convert hexadecimal string to byte sequence
bytes = [data].pack("H*") # H = hex string (highest byte first), * = multiple bytes

# SHA-256 (first round)
hash1 = Digest::SHA256.digest(bytes)

# SHA-256 (second round)
hash2 = Digest::SHA256.digest(hash1)

# convert from byte sequence back to hexadecimal string
txid = hash2.unpack("H*")[0]

# print result (natural byte order)
puts txid #=> 169e1e83e930853391bc6f35f605c6754cfead57cf8387639d3b4096c54f18f4

# print result (reverse byte order)
puts txid.scan(/../).reverse.join #=> f4184fc596403b9d638783cf57adfe4c75c605f6356fbc91338530e9831e9e16
```

请记住，在处理 SegWit 交易时，你不应将 marker、flag 和 [witness](../witness.md) 包含在要进行哈希的交易数据中。

## 示例

TXID 看起来像什么？

### 1. 旧版交易

要为旧版交易创建 TXID，你对**所有**交易数据进行 HASH256 计算：

```
0100000001c997a5e56e104102fa209c6a852dd90660a20b2d9c352423edce25857fcd3704000000004847304402204e45e16932b8af514961a1d3a1a25fdf3f4f7732e9d624c6c61548ab5fb8cd410220181522ec8eca07de4860a4acdd12909d831cc56cbbac4622082221a8768d1d0901ffffffff0200ca9a3b00000000434104ae1a62fe09c5f51b13905f07f06b99a2f7159b2225f374cd378d71302fa28414e7aab37397f554a7df5f142c21c1b7303b8a0626f1baded5c72a704f7e6cd84cac00286bee0000000043410411db93e1dcdb8a016b49840f8c53bc1eb68a382e97b1482ecad7b148a6909a5cb2e0eaddfb84ccf9744464f82e160bfa9b8b64f9d4c03f999b8643f656b412a3ac00000000
```

注意：被哈希以创建 TXID 的数据被高亮标记为绿色。

如果你对所有这些数据进行 HASH256 计算，你会得到 `169e1e83e930853391bc6f35f605c6754cfead57cf8387639d3b4096c54f18f4`，这是[自然字节序](../../general/byte-order.md#natural-byte-order)的 TXID，也是原始交易数据内部所发现的格式。

然后，如果你反转字节顺序，你就会得到 TXID [f4184fc596403b9d638783cf57adfe4c75c605f6356fbc91338530e9831e9e16](/explorer/tx/f4184fc596403b9d638783cf57adfe4c75c605f6356fbc91338530e9831e9e16)，这是在区块链浏览器上搜索交易时使用的字节序。

### 2. SegWit 交易

要为 SegWit 交易创建 TXID，你对除 marker、flag 和 witness 字段之外的所有交易数据进行 HASH256 计算。

```
020000000001013a53de6e1fe821452674c5435e3989eecdf35cb1de1c8bafb674f543a55d658c3600000000fdffffff01599aea0400000000160014cfbd92a6337e8b6043552d6fc5c35c7e5062281e0247304402201250febbce0a5b333c2d715b869cb960f5abf1702192c7af6e112c6d6030be880220073c55f4814a064bf804d9ed16b57eaaeaafb536c4187e6260ef3fc61ca98a77012102e71911951e1f9799d5ccd05200ea0c18f786cb1bb45754d4a0799a06c2b80e8000000000
```

注意：被哈希以创建 TXID 的数据被高亮标记为绿色。

如果你对高亮的数据进行 HASH256 计算，你会得到 `01cda497b58d876f207b74c1f0b741f397c376852b3c68b0b6db042a24ffd96c`，然后反转字节序，你就得到了 TXID [6cd9ff242a04dbb6b0683c2b8576c397f341b7f0c1747b206f878db597a4cd01](/explorer/tx/6cd9ff242a04dbb6b0683c2b8576c397f341b7f0c1747b206f878db597a4cd01)。

在为 SegWit 交易创建 TXID 时，你**不哈希 SegWit 交易中的新字段**。这避免了将任何[签名](../../keys/signature.md)数据作为 TXID 的一部分（签名现在放置于 [witness](../witness.md) 中），因为签名在交易发送到[网络](../../networking.md)后可以被篡改以改变 TXID（这很罕见，但它使 TXID 变得不够可靠）。

这是进行 [SegWit](../../upgrades/segregated-witness.md) 升级的首要原因。

### 亲自尝试

你可以通过使用 HASH256 直接手动哈希相同的数据来验证上述数据生成了正确的 TXIDs：

随机交易数据

随机区块头

数据 (十六进制)

`0 bytes`


<img src="../../../images/icons_hash-function.svg" alt="Hash Function Icon" style="width:52px; height:52px" />
SHA-256

<img src="../../../images/icons_hash-function.svg" alt="Hash Function Icon" style="width:52px; height:52px" />
SHA-256

HASH256

SHA-256(SHA-256(data))

`0 bytes`



0 secs

然后不要忘记反转字节序：

随机示例

字节

`0 bytes`

反转后

`0 bytes`


 显示详情



0 secs

## 用途

TXIDs 在比特币中是如何使用的？

TXIDs 在比特币的工作方式中起着重要作用。它们用于以下场景：

### 1. 搜索交易

你通常使用 TXIDs 来在[区块链浏览器](/explorer/)上或从本地节点查找特定交易：

```
$ bitcoin-cli getrawtransaction f4184fc596403b9d638783cf57adfe4c75c605f6356fbc91338530e9831e9e16

0100000001c997a5e56e104102fa209c6a852dd90660a20b2d9c352423edce25857fcd3704000000004847304402204e45e16932b8af514961a1d3a1a25fdf3f4f7732e9d624c6c61548ab5fb8cd410220181522ec8eca07de4860a4acdd12909d831cc56cbbac4622082221a8768d1d0901ffffffff0200ca9a3b00000000434104ae1a62fe09c5f51b13905f07f06b99a2f7159b2225f374cd378d71302fa28414e7aab37397f554a7df5f142c21c1b7303b8a0626f1baded5c72a704f7e6cd84cac00286bee0000000043410411db93e1dcdb8a016b49840f8c53bc1eb68a382e97b1482ecad7b148a6909a5cb2e0eaddfb84ccf9744464f82e160bfa9b8b64f9d4c03f999b8643f656b412a3ac00000000

# Note: You need to set txindex=1 in bitcoin.conf to look up all the transactions in the blockchain.
```

这在你想要查看交易详情或找出其位置（即它是否已被打包进[区块链](../../blockchain.md)，或者它是否依然在[内存池](../../mining/memory-pool.md)中）时非常有用。

### 2. 引用以前的输出进行花费

你在创建比特币交易时，使用 TXIDs 来引用以往交易中的 [outputs](../output.md) 用作 [inputs](../input.md)。

[<img src="../../../images/diagrams_png_transaction-input-select.png" alt="Diagram showing how an input is selected by referencing the TXID and VOUT from a previous transaction." width="740" height="352" />](../../../images/diagrams_png_transaction-input-select.png)

TXIDs 是唯一的，因此你可以将它们与 [VOUT](vout.md) 结合使用，引用区块链中的任何特定输出进行花费。

### 3. 创建默克尔根

TXIDs 用于为[区块头](../../block.md#header)创建[默克尔根](../../block/merkle-root.md)：

[<img src="../../../images/diagrams_png_block-merkle-root.png" alt="Diagram showing how TXIDs are used to create a merkle root." width="767" height="310" />](../../../images/diagrams_png_block-merkle-root.png)

默克尔根基本上是通过以树状结构对区块中所有的 TXIDs 进行哈希创建的。这为区块内的所有交易创建了一个唯一的指纹，随后该指纹会被放置在区块头中，以防止区块内容在以后被篡改。

这是因为对交易数据的任何更改都会改变 TXID，而对 TXID 的任何更改都会对生成的默克尔根产生连锁反应。

<img src="../../../images/icons_tool.svg" alt="Tool Icon" style="width:20px; height:20px" /> 默克尔根 (Merkle Root)

随机示例

区块

TXID 列表

由 *空格*、*逗号* 或 *换行符* 分隔的 TXID 列表。引号和括号会被忽略。

TXID 应该以 [反向字节序](../../general/byte-order.md#reverse-byte-order)（如它们在区块链浏览器上显示的那样）输入，但在计算默克尔根之前，它们会被转换为 [自然字节序](../../general/byte-order.md#natural-byte-order)。



TXIDs (0)
 

默克尔根 (自然字节序)

哈希函数输出的字节顺序

默克尔根 (反向字节序)

区块链浏览器上显示的字节顺序



0 secs

## 重复的 TXIDs

对于每笔交易来说，TXID 都是唯一的。

然而，在区块链中实际上出现过两个重复 TXIDs 的例子：

1. [e3bf3d07d4b0375638d5f1db5255fe07ba2c4cb067cd81b84ee974b6585fb468](/explorer/tx/e3bf3d07d4b0375638d5f1db5255fe07ba2c4cb067cd81b84ee974b6585fb468)
   * [区块 91,880](/explorer/block/00000000000743f190a18c5577a3c2d2a1f610ae9601ac046a38084ccb7cd721) (2010 年 11 月 15 日, 00:36)
   * [区块 91,722](/explorer/block/00000000000271a2dc26e7667f8419f2e15416dc6955e5a6c6cdf3f2574dd08e) (2010 年 11 月 14 日, 08:37)
2. [d5d27987d2a3dfc724e359870c6644b40e497bdc0589a033220fe15429d88599](/explorer/tx/d5d27987d2a3dfc724e359870c6644b40e497bdc0589a033220fe15429d88599)
   * [区块 91,842](/explorer/block/00000000000a4d0a398161ffc163c503763b1f4360639393e0e4c8e300e0caec) (2010 年 11 月 14 日, 21:04)
   * [区块 91,812](/explorer/block/00000000000af0aed4792b1acee3d966af36cf5def14935db8de83d6f9306f2f) (2010 年 11 月 14 日, 17:59)

从技术上讲，每次出现的都是*同一笔交易*，因为它们都具有相同的底层[交易数据](../../transaction.md#structure)。这并不是说两笔完全不同的交易最终得到了相同的 TXID（即[哈希碰撞](../../cryptography/hash-function.md#strong-hash-function)）——而只是同一笔交易最终出现在了多个区块中。

无论如何，这种重复 TXID 的情况发生，仅仅是因为它们是 **[coinbase 交易](../../mining/coinbase-transaction.md)**。

你要知道，coinbase 交易的 [input](../input.md) 的 TXID 和 [VOUT](vout.md) 字段是*固定*的，而不是像所有其他交易那样是*动态*的。这意味着 input 并不被迫要求唯一，所以如果你决定保持输出也完全相同（通过使用相同的[锁定脚本](../output/scriptpubkey.md)来认领相同金额的[区块奖励](../../mining/block-reward.md)，这两个例子中发生的就是这种情况），那么过去没有什么能阻止你创建重复的 coinbase 交易并将其打包进区块链。

当然，你其实并不希望区块链中出现重复的交易，因为 **TXIDs 被用来引用先前的交易**。如果你有多笔具有相同 TXID 的交易，那么只有其中*一笔*交易（最近的那笔）的未花费 [outputs](../output.md) 是可以被花费的，因为根本没有办法唯一引用其他的交易（较早的那些交易）。

### 解决方案

1. [BIP 30](https://github.com/bitcoin/bips/blob/master/bip-0030.mediawiki) **（2012 年 2 月 22 日）**：引入了一条规则，阻止区块包含已存在的 TXID（尽管这只包括检查 [UTXO](../utxo.md) 集中的 TXIDs）。
2. [BIP 34](https://github.com/bitcoin/bips/blob/master/bip-0034.mediawiki) **（2012 年 7 月 6 日）**：要求 coinbase 交易在其交易数据中[包含当前的区块高度](../../mining/coinbase-transaction.md#bip34)，这意味着 coinbase 交易数据将始终是唯一的。

这些修复措施意味着现在已经不可能创建重复的 coinbase 交易了。

然而，对于上面的两笔重复交易来说已经太迟了。因此，只有每笔交易的最新副本才可以花费其输出，因为早期重复交易的输出（50 BTC）是无法访问的，因此永远“丢失”了（我用“丢失”是因为我们知道它们在哪里……只是无法访问它们）。

无论如何，这两笔交易是区块链历史上一个有趣的遗迹，也很适合作为酒吧问答比赛的一个好题目。

**如果你要在数据库中存储交易，了解这些重复的 TXIDs 非常重要。** 这是一个小问题，但如果你正在插入一行并期望每个 TXID 都不存在，它可能会让你措手不及。因此你只需在你的导入脚本中考虑这两个边界情况即可正常工作。

* [handle historic transactions with duplicate IDs.](https://github.com/bitpay/insight-api/issues/42)
* [What would happened if two transactions have the same hash?](https://bitcoin.stackexchange.com/questions/75300/what-would-happened-if-two-transactions-have-the-same-hash)
* [Two blocks, two transactions, same hash](https://bitcoin.stackexchange.com/questions/3030/two-blocks-two-transactions-same-hash)
* [Can the outputs of transactions with duplicate hashes be spent?](https://bitcoin.stackexchange.com/questions/11999/can-the-outputs-of-transactions-with-duplicate-hashes-be-spent)

感谢 DJBunnies [指出这一点](https://www.reddit.com/r/Bitcoin/comments/5waqc1/comment/de8m12j/)。