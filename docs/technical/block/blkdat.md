<img src="../../images/icons_loader-2.svg" alt="Loading Tool" style="height:32px; width:32px;" />

`~/.bitcoin/blocks/` 目录中的 blk.dat 文件包含您的 [*Bitcoin Core*](https://bitcoin.org/en/download) 节点接收到的**原始[区块](../block.md)数据**。

这些 blk.dat 文件基本上存储了整个[区块链](../blockchain.md)。

## 位置

区块链在您的计算机上存储在什么位置？

原始区块链文件在磁盘上的位置取决于您使用的操作系统。以下是默认位置：

* **Linux:** `~/.bitcoin/blocks/`
* **Mac:** `~/Library/Application Support/Bitcoin/blocks/`
* **Windows:**
  + `C:\Users\[username]\AppData\Roaming\Bitcoin\blocks\`（[v27.2](https://github.com/bitcoin/bitcoin/blob/master/doc/release-notes/release-notes-27.2.md) 及以下版本）
  + `C:\Users\[username]\AppData\Local\Bitcoin\blocks\`（[v28.0](https://github.com/bitcoin/bitcoin/blob/master/doc/release-notes/release-notes-28.0.md) 及以上版本）

您可以通过在 [bitcoin.conf 配置文件](https://github.com/bitcoin/bitcoin/blob/master/doc/bitcoin-conf.md) 中设置 `datadir=<dir>` 选项来更改区块数据目录的位置。

## 文件名

区块链文件是如何组织的？

您的节点接收到的每个[区块](../block.md)都会追加到 blk.dat 文件中。但是，为了避免将整个区块链存储在一个庞大的文件中，它们被拆分成了多个 blk\*.dat 文件。

* ~/.bitcoin/blocks/
  1. blk00000.dat
  2. blk00001.dat
  3. blk00002.dat
  4. blk00003.dat
  5. blk00004.dat
  6. 依此类推...

您的节点首先将区块添加到 blk00000.dat 中，当它写满时，会转移到 blk00001.dat，然后是 blk00002.dat...，依此类推。如果您使用的是 Linux，可以导航到数据目录并使用以下命令列出所有原始区块文件：

```
$ cd ~/.bitcoin/blocks/
$ ls blk*

blk00000.dat
blk00001.dat
blk00002.dat
blk00003.dat
blk00004.dat
blk00005.dat
blk00006.dat
...
```

blk.dat 文件的最大大小为 **128 MiB**（134,217,728 字节）。此限制由 [MAX\_BLOCKFILE\_SIZE](https://github.com/bitcoin/bitcoin/blob/master/src/node/blockstorage.h) 设置。

## 示例

原始区块看起来是什么样的？

blk.dat 文件中的数据是以二进制形式存储的，基本上是一堆 1 和 0，并不是人类可读的文本。

尽管如此，我们可以通过读取 blk00000.dat 的前 *293 个字节*来查看[创世区块](/explorer/block/000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f)。我拆分了各个字段，以便您可以更清楚地看到它们：

```
f9beb4d9 1d010000 01000000 0000000000000000000000000000000000000000000000000000000000000000 3ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4a 29ab5f49 ffff001d 1dac2b7c 01 01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff4d04ffff001d0104455468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e642062616e6b73ffffffff0100f2052a01000000434104678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5fac00000000
```

请参阅下面的 [od 命令](#od) 以从二进制文件中显示[十六进制字节](../general/bytes.md#representing-bytes)。

## 结构

原始区块的结构是怎样的？

[<img src="../../images/diagrams_png_block-blkdat.png" alt="Diagram showing structure of the raw block data inside the blk.dat files." width="431" height="378" />](../../images/diagrams_png_block-blkdat.png)

上面的数据可以分为五个部分：

1. [**魔术字节 (magic bytes)**](../networking/magic-bytes.md)（4 字节）是一个消息分隔符，用于指示区块的开始。
2. **大小 (size)**（4 字节）指示接下来的区块的大小（以[字节](../general/bytes.md)为单位）。
3. [**区块头 (block header)**](../block.md#header)（80 字节）是区块数据的摘要。
4. **交易数量 (tx count)**（[compact size](../general/compact-size.md)）指示区块中有多少笔交易。
5. [**交易数据 (transaction data)**](../transaction.md)（可变长度）是区块中所有一个接一个连接在一起的交易。

大小字段让我能够计算出在上面的示例中我需要读取 **293 字节** 才能获取整个区块。区块的大小表示为 `1d010000`，因此为了将其转换为人类可读的格式：

1. 将 `1d010000` 从 *小端序 (little-endian)* 转换为 *大端序 (big-endian)* 得到 `0000011d`。
2. 将 `0000011d` 从 *十六进制* 转换为 *十进制* 得到 `285`。

<img src="../../images/icons_tool.svg" alt="Tool Icon" style="width:20px; height:20px" /> 小端序 (Little Endian)

+1

十进制

0d

十六进制字节 (大端序)

0x

`0 bytes`

十六进制字节 (小端序)

0x

`0 bytes`


字段大小

 Any

 2 字节

 4 字节

 8 字节

 12 字节

 16 字节

 32 字节



0 秒

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

因此实际的区块本身只有 285 字节。但是，由于在开始处有额外的 8 字节用于存放 magic-bytes + size，因此我需要从原始区块链文件的开头读取 **293 字节** 才能获得完整的区块数据。

## Linux 工具

您如何读取原始区块链数据？

如前所述，blk.dat 文件中的数据是*二进制*的，因此如果您在常规文本编辑器中打开它，可能看不到任何有用的内容。不过没关系，因为二进制数据可以很容易地显示为[十六进制](../general/hexadecimal.md)字节，并且有几个命令可以提供帮助：

### 1. `xxd`

这是一个简单的工具。它以十六进制形式导出原始二进制文件的内容。

```
$ xxd -p -s 8 -l 285 blk00000.dat

010000000000000000000000000000000000000000000000000000000000
0000000000003ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a5132
3a9fb8aa4b1e5e4a29ab5f49ffff001d1dac2b7c01010000000100000000
00000000000000000000000000000000000000000000000000000000ffff
ffff4d04ffff001d0104455468652054696d65732030332f4a616e2f3230
3039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f
6e64206261696c6f757420666f722062616e6b73ffffffff0100f2052a01
000000434104678afdb0fe5548271967f1a67130b7105cd6a828e03909a6
7962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b
8d578a4c702b6bf11d5fac00000000

# -p      <- 显示纯十六进制字节
# -s 8    <- 定位到文件中的某个位置 (使用 8 跳过 magic bytes 和 block size 字段)
# -l 285  <- 要读取的字节数 (创世区块是接下来的 285 字节)
```

如果您运行的是 Bitcoin Core `v28.0` 或更高版本，您可能需要先*解密* ([XOR](#xor)) 原始区块数据才能获得与上面相同的结果。

### 2. `od`

这是另一个简单的工具。它以您选择的格式导出文件内容。

```
$ od -x --endian=big -N 293 -An blk00000.dat

 f9be b4d9 1d01 0000 0100 0000 0000 0000
 0000 0000 0000 0000 0000 0000 0000 0000
 0000 0000 0000 0000 0000 0000 3ba3 edfd
 7a7b 12b2 7ac7 2c3e 6776 8f61 7fc8 1bc3
 888a 5132 3a9f b8aa 4b1e 5e4a 29ab 5f49
 ffff 001d 1dac 2b7c 0101 0000 0001 0000
 0000 0000 0000 0000 0000 0000 0000 0000
 0000 0000 0000 0000 0000 0000 0000 ffff
 ffff 4d04 ffff 001d 0104 4554 6865 2054
 696d 6573 2030 332f 4a61 6e2f 3230 3039
 2043 6861 6e63 656c 6c6f 7220 6f6e 2062
 7269 6e6b 206f 6620 7365 636f 6e64 2062
 6169 6c6f 7574 2066 6f72 2062 616e 6b73
 ffff ffff 0100 f205 2a01 0000 0043 4104
 678a fdb0 fe55 4827 1967 f1a6 7130 b710
 5cd6 a828 e039 09a6 7962 e0ea 1f61 deb6
 49f6 bc3f 4cef 38c4 f355 04e5 1ec1 12de
 5c38 4df7 ba0b 8d57 8a4c 702b 6bf1 1d5f
 ac00 0000 0000

# -x           <- 显示十六进制
# --endian=big <- 以大端序显示字节
# -N 293       <- 要读取的字节数
# -An          <- 不显示文件偏移量
```

"od" 代表 **o**ctal **d**ump (八进制转储)，但您也可以将数据转储为除 [八进制](https://en.wikipedia.org/wiki/Octal) 之外的其他格式。

### 3. `hexdump`

这类似于 `xxd` 和 `od`，但它还提供了从数据中显示 [ASCII](../general/bytes.md#text) 文本的选项（这对于查看交易数据中包含的消息非常方便）。

```
$ hexdump -C -s 8 -n 285 blk00000.dat

00000008  01 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
00000018  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
00000028  00 00 00 00 3b a3 ed fd  7a 7b 12 b2 7a c7 2c 3e  |....;...z{..z.,>|
00000038  67 76 8f 61 7f c8 1b c3  88 8a 51 32 3a 9f b8 aa  |gv.a......Q2:...|
00000048  4b 1e 5e 4a 29 ab 5f 49  ff ff 00 1d 1d ac 2b 7c  |K.^J}._I......+||
00000058  01 01 00 00 00 01 00 00  00 00 00 00 00 00 00 00  |................|
00000068  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
00000078  00 00 00 00 00 00 ff ff  ff ff 4d 04 ff ff 00 1d  |..........M.....|
00000088  01 04 45 54 68 65 20 54  69 6d 65 73 20 30 33 2f  |..EThe Times 03/|
00000098  4a 61 6e 2f 32 30 30 39  20 43 68 61 6e 63 65 6c  |Jan/2009 Chancel|
000000a8  6c 6f 72 20 6f 6e 20 62  72 69 6e 6b 20 6f 66 20  |lor on brink of |
000000b8  73 65 63 6f 6e 64 20 62  61 69 6c 6f 75 74 20 66  |second bailout f|
000000c8  6f 72 20 62 61 6e 6b 73  ff ff ff ff 01 00 f2 05  |or banks........|
000000d8  2a 01 00 00 00 43 41 04  67 8a fd b0 fe 55 48 27  |*....CA.g....UH'|
000000e8  19 67 f1 a6 71 30 b7 10  5c d6 a8 28 e0 39 09 a6  |.g..q0..\..(.9..|
000000f8  79 62 e0 ea 1f 61 de b6  49 f6 bc 3f 4c ef 38 c4  |yb...a..I..?L.8.|
00000108  f3 55 04 e5 1e c1 12 de  5c 38 4d f7 ba 0b 8d 57  |.U......\8M....W|
00000118  8a 4c 70 2b 6b f1 1d 5f  ac 00 00 00 00           |.Lp+k.._.....|
0000125

# -C <- 以比特币中使用的相同字节顺序显示数据，同时显示 ascii 文本
# -s <- 起始点 (字节偏移量)
# -n <- 要读取的字节数
```

这是显示创世区块的流行方式，您会在互联网的各个地方看到它。

总之，如果您喜欢，您可以将一些命令连接在一起，这样您就可以在没有任何格式的情况下直接获得原始十六进制字节：

```
$ hexdump -C -s 8 -n 285 blk00000.dat | cut -c 11-58 | tr '\n' ' ' | tr -d ' '

0100000000000000000000000000000000000000000000000000000000000000000000003ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4a29ab5f49ffff001d1dac2b7c0101000000010000000000000000000000000000000000000000000000000000000000000000ffffffff4d04ffff001d0104455468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73ffffffff0100f2052a01000000434104678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5fac00000000%

# cut -c 11-58 <- 剪切掉每行中字符 11 到 58 列之外的所有内容
# tr '\n' ' ' <- 将换行符翻译为空格
# tr -d ' ' <- 删除所有空格
```

但是，如果您要花精力这么做，不妨直接使用以下命令从 Bitcoin Core 中提取原始区块数据：

```
$ bitcoin-cli getblock <hash> 0
```

### 4. bitcoin-iterate

[bitcoin-iterate](https://github.com/rustyrussell/bitcoin-iterate) 是一个用于从原始区块链文件中提取数据的极好工具。它的运行速度也出奇地快。以下是一些简单的示例：

```
# 用法
bitcoin-iterate -h

# 返回前 100 个区块的区块头 (block headers)
bitcoin-iterate -q --block='%bH' --end=100 > headers.txt

# 返回区块 123,456 中的所有原始交易
bitcoin-iterate -q --tx='%tX' --start=123456 --end=123456 > transactions.txt

# 返回区块链中的每一个 scriptpubkey 以及它们被包含的交易的 txid
bitcoin-iterate -q --output='%th %os' > scriptpubkeys.txt
```

我经常用它来寻找区块链中有趣的区块和交易。

## XOR

自 [v28.0](https://github.com/bitcoin/bitcoin/blob/master/doc/release-notes/release-notes-28.0.md) 起，blkXXXXX.dat 文件中的原始区块数据**默认已混淆 (obfuscated by default)**。对其进行*去混淆*非常简单，但这确实意味着原始区块数据不再像以前那样以“纯文本”形式存储。

> **obfuscate** — 故意使某事不那么清晰，更难理解
> 
> [剑桥词典](https://dictionary.cambridge.org/dictionary/english/obfuscate)

这样做的原因是因为您无法控制其他人可能决定在区块链中存储什么内容，因此为了[防止杀毒软件检测到原始区块数据有任何问题](https://github.com/bitcoin/bitcoin/pull/28052)，当数据存储在您的计算机上时会被轻微地“打乱”。但正如我所说，将它恢复到自然形态是非常容易的。

所以如果您想从磁盘上读取原始区块数据，您需要首先学习如何**对其进行去混淆**。

* 您可以通过在 `bitcoin.conf` 文件中设置 `blocksxor=0` 来关闭混淆。但是，这只有在您重新下载区块链时才有效。
* 如果您在升级到 v28.0 之前就在运行比特币节点，您的原始区块数据文件将保持纯文本状态。因此，现有的和新的区块数据在未来都不会被混淆。

### 示例

这是[创世区块](/explorer/block/000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f)在其自然形态下的样子：

```
$ hexdump -C -s 8 -n 285 blk00000.dat

00000008  01 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
00000018  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
00000028  00 00 00 00 3b a3 ed fd  7a 7b 12 b2 7a c7 2c 3e  |....;...z{..z.,>|
00000038  67 76 8f 61 7f c8 1b c3  88 8a 51 32 3a 9f b8 aa  |gv.a......Q2:...|
00000048  4b 1e 5e 4a 29 ab 5f 49  ff ff 00 1d 1d ac 2b 7c  |K.^J}._I......+||
00000058  01 01 00 00 00 01 00 00  00 00 00 00 00 00 00 00  |................|
00000068  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
00000078  00 00 00 00 00 00 ff ff  ff ff 4d 04 ff ff 00 1d  |..........M.....|
00000088  01 04 45 54 68 65 20 54  69 6d 65 73 20 30 33 2f  |..EThe Times 03/|
00000098  4a 61 6e 2f 32 30 30 39  20 43 68 61 6e 63 65 6c  |Jan/2009 Chancel|
000000a8  6c 6f 72 20 6f 6e 20 62  72 69 6e 6b 20 6f 66 20  |lor on brink of |
000000b8  73 65 63 6f 6e 64 20 62  61 69 6c 6f 75 74 20 66  |second bailout f|
000000c8  6f 72 20 62 61 6e 6b 73  ff ff ff ff 01 00 f2 05  |or banks........|
000000d8  2a 01 00 00 00 43 41 04  67 8a fd b0 fe 55 48 27  |*....CA.g....UH'|
000000e8  19 67 f1 a6 71 30 b7 10  5c d6 a8 28 e0 39 09 a6  |.g..q0..\..(.9..|
000000f8  79 62 e0 ea 1f 61 de b6  49 f6 bc 3f 4c ef 38 c4  |yb...a..I..?L.8.|
00000108  f3 55 04 e5 1e c1 12 de  5c 38 4d f7 ba 0b 8d 57  |.U......\8M....W|
00000118  8a 4c 70 2b 6b f1 1d 5f  ac 00 00 00 00           |.Lp+k.._.....|
0000125
```

然而，我的 `xor_key` 是 `17 7a 35 a3 e4 32 54 ff`，因此这是我的创世区块在磁盘上的样子：

```
$ hexdump -C -s 8 -n 285 blk00000.dat

00000008  16 7a 35 a3 e4 32 54 ff  17 7a 35 a3 e4 32 54 ff  |.z5..2T..z5..2T.|
00000018  17 7a 35 a3 e4 32 54 ff  17 7a 35 a3 e4 32 54 ff  |.z5..2T..z5..2T.|
00000028  17 7a 35 a3 df 91 b9 02  6d 01 27 11 9e f5 78 c1  |.z5.....m.'...x.|
00000038  70 0c ba c2 9b fa 4f 3c  9f f0 64 91 de ad ec 55  |p.....O<..d....U|
00000048  5c 64 6b e9 cd 99 0b b6  e8 85 35 be f9 9e 7f 83  |\dk.......5.....|
00000058  16 7b 35 a3 e4 33 54 ff  17 7a 35 a3 e4 32 54 ff  |.{5..3T..z5..2T.|
00000068  17 7a 35 a3 e4 32 54 ff  17 7a 35 a3 e4 32 54 ff  |.z5..2T..z5..2T.|
00000078  17 7a 35 a3 e4 32 ab 00  e8 85 78 a7 1b cd 54 e2  |.z5..2....x...T.|
00000088  16 7e 70 f7 8c 57 74 ab  7e 17 50 d0 c4 02 67 d0  |.~p..Wt.~.P...g.|
00000098  5d 1b 5b 8c d6 02 64 c6  37 39 5d c2 8a 51 31 93  |].[...d.79]..Q1.|
000000a8  7b 15 47 83 8b 5c 74 9d  65 13 5b c8 c4 5d 32 df  |{.G..\t.e.[..]2.|
000000b8  64 1f 56 cc 8a 56 74 9d  76 13 59 cc 91 46 74 99  |d.V..Vt.v.Y..Ft.|
000000c8  78 08 15 c1 85 5c 3f 8c  e8 85 ca 5c e5 32 a6 fa  |x....\?....\.2..|
000000d8  3d 7b 35 a3 e4 71 15 fb  70 f0 c8 13 1a 67 1c d8  |={5..q..p....g..|
000000e8  0e 1d c4 05 95 02 e3 ef  4b ac 9d 8b 04 0b 5d 59  |........K.....]Y|
000000f8  6e 18 d5 49 fb 53 8a 49  5e 8c 89 9c a8 dd 6c 3b  |n..I.S.I^.....l;|
00000108  e4 2f 31 46 fa f3 46 21  4b 42 78 54 5e 39 d9 a8  |./1F..F!KBxT^9..|
00000118  9d 36 45 88 8f c3 49 a0  bb 7a 35 a3 e4           |.6E...I..z5..|
0000125
```

`xor_key` 是由您的节点随机生成的，因此您磁盘上的创世区块看起来可能会有所不同。

### 去混淆

原始区块数据是使用存储在您的 `/blocks/` 文件夹中 `xor.dat` 文件里的 `xor_key` 来进行混淆的。

例如：

```
$ xxd -p ~/.bitcoin/blocks/xor.dat

177a35a3e43254ff
```

要对原始区块数据进行去混淆，您只需使用此 `xor_key` 与原始区块数据进行 XOR 运算，这会将“位翻转”回它们自然形态。

这个 `xor_key` 长度为 **8 字节**，因此您需要重复对原始区块数据的每 8 个字节进行 XOR 运算以对其进行去混淆。

[<img src="../../images/diagrams_png_block-blkdat-xor.png" alt="Diagram showing how to use the xor_key to deobfuscate raw block data from a blk.dat file." width="765" height="178" />](../../images/diagrams_png_block-blkdat-xor.png)

这是一些简单的代码，显示它是如何工作的：

```
# get the xor key
file_xor = File.open("/home/username/.bitcoin/blocks/xor.dat", "r") # don't forget to change the path
xor_key = file_xor.read # this is 8 bytes

# set the position you're reading from in the raw block data file
offset = 8 # skip the magic bytes (4 bytes) and block size (4 bytes) fields

# read the raw data for the genesis block from the blk.dat file
file_blk = File.open("/home/username/.bitcoin/blocks/blk00000.dat", "r") # don't forget to change the path
file_blk.seek(offset) # move to where you want to start reading from in the file
blk_data = file_blk.read(285) # the next 285 bytes is the actual block data (I already know this)

# convert the xor key and raw block data to byte arrays
xor_key_bytes = xor_key.bytes
blk_data_bytes = blk_data.bytes

# create an array for storing the resulting xor'd bytes
result = []

# run through each byte of the raw block data
blk_data_bytes.each_with_index do |byte, i|
	
  # there are only 8 bytes in the xor key, so use the modulo operator to loop around to use each byte as we go
  xor_i = (offset + i) % 8 # the offset allows us to start from the correct byte in the xor key

  # xor each byte from the raw block data using the next byte from the xor key, and store each byte in the result array
  result[i] = byte ^ xor_key_bytes[xor_i] # ^ is the XOR operator
end

# convert the result from a byte array to a byte string, then convert to a hexadecimal string (for display purposes)
result_hex = result.pack("C*").unpack("H*")

# show the result
puts result_hex #=> 0100000000000000000000000000000000000000000000000000000000000000000000003ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4a29ab5f49ffff001d1dac2b7c0101000000010000000000000000000000000000000000000000000000000000000000000000ffffffff4d04ffff001d0104455468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73ffffffff0100f2052a01000000434104678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5fac00000000
```

如您所见，重要的部分是确保为原始区块数据的每个字节使用来自 `xor_key` 的正确字节。

#### XOR 运算符

[XOR](https://stackoverflow.com/questions/14526584/what-does-the-xor-operator-do)（异或）按位运算符作用于二进制数据的位（`1` 和 `0`）。它的工作原理如下：

* 如果两个输入位不同，则返回 `1`。
* 如果两个输入位相同，则返回 `0`。

在实际操作中，该运算符对于“翻转位”非常有用。

例如：

```
0101010101 <- 原始数据
1111111111 <- 示例 xor_key
---------- XOR
1010101010 <- 结果
```

然后，如果您在结果上使用相同的 `xor_key`，就会将这些位翻转回它们原始形式：

```
1010101010 <- 原始数据
1111111111 <- 示例 xor_key
---------- XOR
0101010101 <- 结果
```

因此：

* 如果您使用全为 `1` 的 xor\_key，它将**翻转原始数据的每一位**。
* 如果您使用全为 `0` 的 xor 密钥，它将**不翻转任何位**（因此原始数据将保持不变）。

所以通过使用随机的 `xor_key`，不同的密钥在原始区块数据存储在您的磁盘上时会翻转不同的位。然后可以使用相同的 `xor_key` 对混淆后的结果进行“翻转”，恢复原样。

如果您从较早版本升级到 v28.0，您的 `xor_key` 将全为 `0`，因此原始区块数据在磁盘上将保持不变。

在 v28.0 之后必须对原始区块数据进行去混淆确实有点烦人，特别是如果您已经编写了读取 blkXXXXX.dat 文件的工具。但恢复原始数据还是非常简单明了的，因此更新您的代码并让它重新工作应该不会花费太多精力。

## 注意

### 区块顺序

如果您使用的是自己的脚本解析 blk.dat 文件，请注意区块**不会是有序的**。例如，当您运行文件时，您可能会以以下顺序遇到区块：

```
A B C E F D G
```

这是因为您的比特币节点将**并行下载区块**，以便能够尽快下载区块链。因此，您的节点在运行时会下载比当前区块更靠前的区块，而无需等待按顺序接收每个区块。

您的节点获取的最远领先距离（或“最大无序度”）由比特币源码中的 [BLOCK\_DOWNLOAD\_WINDOW](https://github.com/bitcoin/bitcoin/blob/master/src/net_processing.cpp) 控制。

## 资源

* [Bitcoin Core file system](https://github.com/bitcoin/bitcoin/blob/master/doc/files.md)
* [Why are blk\*.dat files ~134200000 bytes?](https://bitcoin.stackexchange.com/questions/50693/why-are-blk-dat-files-134200000-bytes)
* [Making Sense of Hexdump](https://www.suse.com/c/making-sense-hexdump/)