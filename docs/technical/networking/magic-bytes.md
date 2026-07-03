<img src="../../images/icons_loader-2.svg" alt="Loading Tool" style="height:32px; width:32px;" />

[<img src="../../images/diagrams_png_networking-magic-bytes.png" alt="Diagram showing a message being sent to another node with the magic bytes at the start of the message." width="635" height="170" />](https://static.learnmeabitcoin.com/diagrams/png/networking-magic-bytes.png)

魔术字节（Magic bytes）有助于**识别在[比特币网络](/docs/technical/networking.md)节点之间发送的独立消息**。

例如，当使用你自己的代码[连接到节点](/docs/technical/networking.md#connecting)时，你从该节点收到的*每条消息*都将以 `f9beb4d9` 开头，并且你发送的每条消息也应该以相同的魔术字节开头。

## 比特币

比特币中的魔术字节是什么？

比特币中使用的魔术字节长度为 4 字节，每个网络都不同：

| 网络 | 魔术字节 |
| --- | --- |
| Mainnet | `f9beb4d9` |
| Testnet3 | `0b110907` |
| Regtest | `fabfb5da` |

## 示例

在哪里可以找到魔术字节？

这是一条原始的 “[version](/docs/technical/networking.md#version)” 消息，它是你连接到节点时收到的第一条消息：

```
f9beb4d976657273696f6e00000000006f0000004aae42a47c11010005000000000000001436396400000000010000000000000000000000000000000000ffffc1207f8db0d0050000000000000000000000000000000000ffff8a4414c5208df66af23ecba5bd68192f5361746f7368693a302e31322e3128626974636f7265292fc8fb0b0001
```

而这是一条包含单笔[交易](/docs/technical/transaction.md)的原始 “tx” 消息：

```
f9beb4d9747800000000000000000000e00000006a86deb701000000015ac5ae0a2ba96622c9b79de2c339084c8b1d30f63bb55a315f354db4d9a6abcf010000006b4830450221009ad52459e1e8bd5e758399cc0be963c75726c5089499465d9aa79ffb304ecd3802207d73ea58047f4d1f857b400cbff725ef562b7ada1c26e763c5a1aa6d29d2fdf401210234b7b614fcc0e4d926747d491992d8cc133f076bd79095eddf60c34b0e3fef4affffffff02390205000000000017a914ea3b6d7e92e05370bc8a61d3f05dbfdc90bb1d9587d1df3000000000001976a91425f0800454530549ed93747a6449aefe2618203988ac00000000
```

如果你打印出本地节点[原始区块链文件](/docs/technical/block/blkdat.md)中的创世区块，你会发现它在磁盘上也是与魔术字节一起存储的：

```
$ hexdump -C -n 293 blk00000.dat

00000000  f9 be b4 d9 1d 01 00 00  01 00 00 00 00 00 00 00  |................|
00000010  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
00000020  00 00 00 00 00 00 00 00  00 00 00 00 3b a3 ed fd  |............;...|
00000030  7a 7b 12 b2 7a c7 2c 3e  67 76 8f 61 7f c8 1b c3  |z{..z.,>gv.a....|
00000040  88 8a 51 32 3a 9f b8 aa  4b 1e 5e 4a 29 ab 5f 49  |..Q2:...K.^J)._I|
00000050  ff ff 00 1d 1d ac 2b 7c  01 01 00 00 00 01 00 00  |......+|........|
00000060  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
00000070  00 00 00 00 00 00 00 00  00 00 00 00 00 00 ff ff  |................|
00000080  ff ff 4d 04 ff ff 00 1d  01 04 45 54 68 65 20 54  |..M.......EThe T|
00000090  69 6d 65 73 20 30 33 2f  4a 61 6e 2f 32 30 30 39  |imes 03/Jan/2009|
000000a0  20 43 68 61 6e 63 65 6c  6c 6f 72 20 6f 6e 20 62  | Chancellor on b|
000000b0  72 69 6e 6b 20 6f 66 20  73 65 63 6f 6e 64 20 62  |rink of second b|
000000c0  61 69 6c 6f 75 74 20 66  6f 72 20 62 61 6e 6b 73  |ailout for banks|
000000d0  ff ff ff ff 01 00 f2 05  2a 01 00 00 00 43 41 04  |........*....CA.|
000000e0  67 8a fd b0 fe 55 48 27  19 67 f1 a6 71 30 b7 10  |g....UH'.g..q0..|
000000f0  5c d6 a8 28 e0 39 09 a6  79 62 e0 ea 1f 61 de b6  |\..(.9..yb...a..|
00000100  49 f6 bc 3f 4c ef 38 c4  f3 55 04 e5 1e c1 12 de  |I..?L.8..U......|
00000110  5c 38 4d f7 ba 0b 8d 57  8a 4c 70 2b 6b f1 1d 5f  |\8M....W.Lp+k.._|
00000120  ac 00 00 00 00                                    |.....|
00000125
```

这是另一条 “version” 消息，但这次它是在 **Testnet3** 网络上，因此魔术字节是不同的：

```
0b11090776657273696f6e000000000066000000c0094f817e1101000d000000000000004659775800000000000000000000000000000000000000000000ffff0000000000000d000000000000000000000000000000000000000000000000003d2324b2fc764108102f5361746f7368693a302e31332e312fab3d100001
```

## 目的

我们为什么使用魔术字节？

如果你连接到一个比特币节点，你收到的消息是连续数据流的一部分。

[<img src="../../images/technical_networking_magic-bytes_magic-bytes-terminal.gif" alt="Diagram showing a message being sent to another node with the magic bytes at the start of the message." width="802" height="191" />](/docs/technical/networking/magic-bytes/magic-bytes-terminal.gif.md)

节点在字节流中接收数据。

如果你试图读取这些数据，最好能有一种方法来确定新消息何时可能开始。这就是为什么使用一组特定的**魔术字节**作为**标记**，以便你能够更轻松地识别新消息的开始。

所以，魔术字节实际上并没有什么“魔力”；它们只是用来帮助划定数据流的界限。

## 来源

为什么选择这些特定的字节？

> 消息起始字符串的设计旨在使其在正常数据中不太可能出现。这些字符是极少使用的上部 ASCII，在 UTF-8 中无效，并且在任何对齐方式下都会产生一个很大的 32 位整数。

[chainparams.cpp](https://github.com/bitcoin/bitcoin/blob/306ccd4927a2efe325c8d84be1bdb79edeb29b04/src/chainparams.cpp)

上面的这段引言最初存在于 chainparams.cpp 文件中，但后来已被[移除](https://github.com/bitcoin/bitcoin/commit/382b692a503355df7347efd9c128aff465b5583e#diff-ff53e63501a5e89fd650b378c9708274df8ad5d38fcffa6c64be417c4d438b6d)。

所以它们也可以是其他的，但这 4 个字节的属性刚好适合在比特币网络上作为足够好的魔术字节。

* **ASCII。** 如果你将字节 `f9beb4d9` 转换为[扩展 ASCII](https://en.wikipedia.org/wiki/Extended_ASCII)，你会得到 `ù¾´Ù`，对于矿工来说，这不太可能被无意中放入 [Coinbase](/docs/technical/mining/coinbase-transaction.md) 交易的 [scriptsig](/docs/technical/transaction/input/scriptsig.md) 中，或作为 [OP_RETURN](/docs/technical/script/return.md) 输出中的文本字符串。
* **UTF-8。** [基础拉丁 UTF-8 字符集](https://www.w3schools.com/charsets/ref_utf_basic_latin.asp)不会超过 `7e`，所以如果你使用基础 UTF-8 编码一些文本，你不会与任何魔术字节冲突（因为它们都大于 `7e`）。
* **整数。** 如果你将 `f9beb4d9` 转换为整数，你会得到 **4190024921**。如果你还将字节顺序反转为 `d9b4bef9` 并转换为整数，你会得到 **3652501241**。这两个都是非常大的数字，因此它们不太可能被用在原始[交易](/docs/technical/transaction.md)数据的其中一个字段中（例如 [version](/docs/technical/transaction.md#structure-version)、输入数量、[vout](/docs/technical/transaction.md#structure-inputs-vout)、输出数量、金额、脚本大小等）。

<img src="../../images/icons_tool.svg" alt="Tool Icon" style="width:20px; height:20px" /> 进制转换器

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



0 secs

<img src="../../images/icons_tool.svg" alt="Tool Icon" style="width:20px; height:20px" /> 字节反转

随机示例

字节

`0 bytes`

已反转

`0 bytes`


 显示详情



0 secs

在区块或交易中出现这组特定字节并非不可能，但它们自然发生的可能性较低，这已经是次好的情况了。

所以你不会完全依赖魔术字节来识别每条消息的开始，但它有助于识别**消息可能从哪里开始**，并识别**你正在处理哪个网络**（即主网、测试网或私有测试网 regtest）。

这组特定的魔术字节在比特币协议中也是独一无二的。

## 资源

* <https://en.bitcoin.it/wiki/Protocol_documentation#Message_structure>
* <https://en.wikipedia.org/wiki/Magic_number_(programming)>