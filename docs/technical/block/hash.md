<img src="../../images/icons_loader-2.svg" alt="Loading Tool" style="height:32px; width:32px;" />

[<img src="../../images/diagrams_png_block-hash.png" alt="Diagram showing how a block hash is created by hashing the block header." width="775" height="563" />](../../images/diagrams_png_block-hash.png)

区块哈希 (block hash，或区块 ID) 是[区块链](../blockchain.md)中[区块](../block.md)的**唯一引用标识**。

每个区块哈希都是唯一的，由区块的内容决定。因此，您可以使用区块哈希在[区块链浏览器](/explorer/)中搜索特定区块。例如：

* 最近的区块: [000000000000000000005af9d7cca01756b552b02e5f5fac6422864439807264](/explorer/block/000000000000000000005af9d7cca01756b552b02e5f5fac6422864439807264)
* 区块 123,456: [0000000000002917ed80650c6174aac8dfc46f5fe36480aaef682ff6cd83c3ca](/explorer/block/0000000000002917ed80650c6174aac8dfc46f5fe36480aaef682ff6cd83c3ca)
* 创世区块: [000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f](/explorer/block/000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f)

这些区块哈希本身并没有什么特别有趣的地方，因为它们最终只是一堆看起来随机的[字节](../general/bytes.md)。

然而，您会注意到所有的区块哈希都以**一堆零**开头。这是因为区块要被添加到区块链中，[矿工](../mining.md)必须使他们区块的哈希值低于当前的[target](../mining/target.md)值。而如果区块哈希*低于*这个目标值，那么区块哈希的开头自然就会有一堆零。

## 创建

如何创建区块哈希？

区块哈希是通过对[区块头](../block.md#header)进行[哈希运算](../cryptography/hash-function.md)创建的。

随机示例

区块头 (Block Header)

`0 bytes`

区块哈希 (自然字节顺序)

在原始区块头内部使用

`0 bytes`

区块哈希 (反向字节顺序)

在区块浏览器上搜索区块时在外部使用

`0 bytes`



0 秒

创建区块哈希的步骤如下：

1. 构建包含[交易](../transaction.md)的[区块](../block.md)。
2. 为该区块构建一个[区块头](../block.md#header)。
3. 对区块头进行 [HASH256](../cryptography/hash-function.md#hash256) 运算以获得区块哈希。
   * HASH256 是*双重 SHA-256 (double SHA-256)*的简写；您将区块头输入 SHA-256 哈希函数，然后将结果再次输入 SHA-256。

### 代码

```
require 'digest'

# ------------
# block header (genesis block)
# ------------
version = "01000000"
previousblock = "0000000000000000000000000000000000000000000000000000000000000000"
merkleroot = "3ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4a"
time = "29ab5f49"
bits = "ffff001d"
nonce = "1dac2b7c"

blockheader = version + previousblock + merkleroot + time + bits + nonce

# ---------
# block hash
# ----------

# Note: Don't put the block header into the hash function as a string.
#       Convert it from hexadecimal to raw bytes first.

# convert hexadecimal string to byte sequence
bytes = [blockheader].pack("H*") # H = hex string (highest byte first), * = multiple bytes

# SHA-256 (first round)
hash1 = Digest::SHA256.digest(bytes)

# SHA-256 (second round)
hash2 = Digest::SHA256.digest(hash1)

# convert from byte sequence back to hexadecimal string
blockhash = hash2.unpack("H*")[0]

# print result (natural byte order)
puts blockhash #=> 6fe28c0ab6f1b372c1a6a246ae63f74f931e8365e15a089c68d6190000000000

# print result (reverse byte order)
puts blockhash.scan(/../).reverse.join #=> 000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f
```

**交易。** 您会注意到我们并没有直接对区块内的交易进行哈希运算。然而，区块头包含了一个 [Merkle Root](merkle-root.md)，它是交易的哈希值，因此区块内的交易是区块头的一部分。

**有效的区块哈希。** 并不是所有的区块哈希（最初）都会以一堆零开头。矿工会递增区块头中的 [Nonce](nonce.md) 值，以尝试获得低于目标的区块哈希。

**字节顺序。** 对区块头进行哈希的实际结果将产生一个处于[自然字节顺序](../general/byte-order.md#natural-byte-order)的区块哈希。然而，在区块链浏览器中搜索区块时，区块哈希采用的是[反向字节顺序](../general/byte-order.md#reverse-byte-order)。

## 用途

区块哈希在比特币中用于何处？

区块哈希在两个地方使用：

1. 用于在区块链中**搜索**特定的区块。
2. 它们被放入区块头的 [previous block](previous-block.md) 字段中，以在区块链中**连接区块**。

[<img src="../../images/diagrams_png_block-previous-block.png" alt="Diagram showing blocks connected together through block hashes in the block header using the previous block field." width="397" height="529" />](../../images/diagrams_png_block-previous-block.png)

区块通过它们的区块哈希连接在一起。

因此，您最常在区块链浏览器中搜索特定区块时使用区块哈希，但 previous block 字段至关重要，因为它是将区块链粘合在一起的粘合剂。

## 常见问题

### 区块哈希只是某些字节，还是一个数字？

两者都是。

任何来自 SHA-256 [哈希函数](../cryptography/hash-function.md) 的结果都只是一堆无意义的[字节](../general/bytes.md)。但它们（对于该特定数据）是*唯一的*，因此非常适合用作特定数据的唯一引用标识。这使您在构建[区块链](../blockchain.md)时能够自信地搜索和引用之前的区块。

同样，这是创世区块的唯一区块哈希：

```
000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f
```

您在此处看到的[十六进制](../general/hexadecimal.md)字符仅表示 **32 字节** 的无意义数据。

然而，在比特币中，在[开采](../mining.md)过程中，这些区块哈希也被解释为**数字**。如果您将此区块哈希从十六进制转换为十进制，您将得到：

```
10628944869218562084050143519444549580389464591454674019345556079
```

通过这样做，您可以检查区块哈希是否低于[target](../mining/target.md)值，如果是，该区块就可以被添加到区块链中。

因此，将区块哈希视为一个唯一的数字是有意义的。

<img src="../../images/icons_tool.svg" alt="Tool Icon" style="width:20px; height:20px" /> 数字转换器 (Number Converter)

二进制 (Base 2)

0b

`0 digits`

十进制 (Base 10)

0d

`0 digits`

十六进制 (Base 16)

0x

`0 digits`




+1



0 秒