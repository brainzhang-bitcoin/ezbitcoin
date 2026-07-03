<img src="../../images/icons_loader-2.svg" alt="Loading Tool" style="height:32px; width:32px;" />

[<img src="../../images/diagrams_png_bytes-compact-size.png" alt="Diagram showing how the compact size field indicates the upcoming size or item count." width="775" height="295" />](https://static.learnmeabitcoin.com/diagrams/png/bytes-compact-size.png)

紧凑大小 (compact size) 字段在[网络消息](/docs/technical/networking.md#messages)中用于指示**即将到来的字段的尺寸**或**即将到来的字段的数量**。

它可以存储介于 0 和 18446744073709551615 之间的数字。

该字段的尺寸随着其包含的数字的增大而变长。或者换句话说，较小的数字占用较少的空间。这意味着您不必在任何时候都使用一个较大的固定尺寸字段来容纳最大可接受的数字。

整数 (Integer)

0d

紧凑大小 (Compact Size)

`0 bytes`

前缀 (Prefix)

第一个字节指示哪些字节对整数进行编码：

 `<=FC`
– 该字节本身 (0 - 252)
 `FD`
– 接下来的 2 个字节 (253 - 65535)
 `FE`
– 接下来的 4 个字节 (65536 - 4294967295)
 `FF`
– 接下来的 8 个字节 (4294967296 - 18446744073709551615)

注意：对整数进行编码的字节采用 little endian (小端序)。

0 秒

## 结构

紧凑大小字段是一个可变长度的[字节](/docs/technical/general/bytes.md)结构。*首字节 (leading byte)*指示该字段的**尺寸**，并且还指示了包含该**数字**的那些字节。

[<img src="../../images/diagrams_png_bytes-compact-size-prefix.png" alt="Diagram showing the prefixes used for compact size fields and the corresponding field sizes." width="367" height="336" />](https://static.learnmeabitcoin.com/diagrams/png/bytes-compact-size-prefix.png)

| 首字节 | 数字存储位置 | 范围 | 字段尺寸 | 示例 |
| --- | --- | --- | --- | --- |
| `FC` (及以下) | 当前字节本身 | 0 - 252 | 1 字节 | `64` (100) |
| `FD` | 接下来的 2 字节 | 253 - 65535 | 3 字节 | `FDE803` (1,000) |
| `FE` | 接下来的 4 字节 | 65536 - 4294967295 | 5 字节 | `FEA0860100` (100,000) |
| `FF` | 接下来的 8 字节 | 4294967296 - 18446744073709551615 | 9 字节 | `FF00E40B5402000000` (10,000,000,000) |

**注意：** 包含数字的字节采用 [little-endian](/docs/technical/general/little-endian.md)。

因此，对于 252 或更小的数字，您只需使用单个字节。但对于较大的数字，您要使用 `FD`、`FE` 或 `FF` 的前缀，并且该整数包含在接下来的 2、4 或 8 个字节中。

紧凑大小字段可以容纳的最大值是 18446744073709551615，即 `FFFFFFFFFFFFFFFFFF`（前缀 `FF` 加上 `FFFFFFFFFFFFFFFFFF`）。

您最常看到的紧凑大小字段存储的都是 252 或更小的数字。所以起初您可能会以为您看到的是一个简单的 1 字节字段，而没有意识到您看到的是一个可以变化尺寸的特殊类型字段。

以 `FF` 开头（针对 8 字节数字）的紧凑大小字段属于完全过度设计，在比特币中从未被使用过。这会被用于指示接下来有超过 4 GB 的数据，这比能够装入实际数据区块中的容量要大得多。

您实际上可以使用 `FF` 前缀，然后使用接下来的 8 字节 `0000000000000001` 来指示值 1。这会是空间的浪费，但它仍与您仅使用单个字节 `01` 一样有效。

## 示例

以下是在[交易](/docs/technical/transaction.md)数据中发现的各种不同紧凑大小前缀的一些示例：

### `FC` (及以下)

单字节的 `FC` 或以下是目前为止最常见的形式：

* [a1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d](/explorer/tx/a1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d) – 这是著名的[披萨交易 (pizza transaction)](https://bitcointalk.org/index.php?topic=137.0)。为了形成这笔 10,000 BTC 的[输出](/docs/technical/transaction/output.md)，该交易将 131 个[输入](/docs/technical/transaction/input.md)收集在一起，因此其输入数量 count 是一个单字节紧凑大小字段 `83`。

这仅仅是一个简短示例。您可以在区块链中查询任意交易，您都会找到简单的单字节紧凑大小字段。它们无处不在。

### `FD`

您偶尔会遇到 `FD` 前缀。这发生于具有高于平均水平的输入/输出数量，或者当一个 [ScriptSig](/docs/technical/transaction/input/scriptsig.md)/[ScriptPubKey](/docs/technical/transaction/output/scriptpubkey.md) 异常庞大时：

* [6bb9c31f15c6940d4bd664054e398e420425339aadc65e8c491cf1151fe7ff4b](/explorer/tx/6bb9c31f15c6940d4bd664054e398e420425339aadc65e8c491cf1151fe7ff4b) – 该交易具有 965 个输入，因此紧凑大小字段为 `FDC503`（不要忘记最后两个字节是 [little-endian](/docs/technical/general/little-endian.md)，因此 `03C5` = 965）。
* [e411dbebd2f7d64dafeef9b14b5c59ec60c36779d43f850e5e347abee1e1a455](/explorer/tx/e411dbebd2f7d64dafeef9b14b5c59ec60c36779d43f850e5e347abee1e1a455) – 该交易具有一个异常庞大的 ScriptPubKey（由于某种原因，它重复了多次 `OP_CHECKSIG`）。该脚本长度为 4,026 字节，因此其紧凑大小字段为 `FDBA0F`。
* [3454605a6e24181a6061574720e93a79689865e7952c56c330ebcb98fa95e936](/explorer/tx/3454605a6e24181a6061574720e93a79689865e7952c56c330ebcb98fa95e936) – 该交易具有 254 个输出。虽然在正常情况下一个单字节可以容纳数字 254，但在使用紧凑大小字段时，最大单字节值是 252。所以在这种情况下使用了 `FD` 前缀，并将数字 254 编码在了接下来的 2 字节中，导致了紧凑大小字段为 `FDFE00`。

### `FE` 和 `FF`

您*极少*会遇到 `FE` 或 `FF` 前缀（针对大于 65,535 的数字）。

这是因为最大的 ScriptPubKey/ScriptSig 限制为 10,000 字节（参见 [script.h](https://github.com/bitcoin/bitcoin/blob/master/src/script/script.h)）。此外，由于区块大小被限制为 4,000,000 [权重](/docs/technical/block.md#weight)单位，在单笔交易中拥有超过 65,535 个输入是不可能的，并且拥有超过 65,535 个输出也将极度困难。

#### 最小交易输入和输出大小

* 最小*[输入](/docs/technical/transaction/input.md)*大小为 41 字节（32 字节 [txid](/docs/technical/transaction/input/txid.md) + 4 字节 [vout](/docs/technical/transaction/input/vout.md) + 1 字节 [ScriptSig](/docs/technical/transaction/input/scriptsig.md) + 4 字节 sequence）。因此，如果您在交易中放入 65,535 个此类输入，其大小将为 2.686 MB（10,747,740 权重单位），这比整个区块的最大大小还要大。
* 最小*[输出](/docs/technical/transaction/output.md)*大小为 9 字节（8 字节金额 + 1 字节 [ScriptPubKey](/docs/technical/transaction/output/scriptpubkey.md)）。因此，如果您在交易中放入 65,535 个此类输出，它将占用 0.589 MB（2,359,260 权重单位），这在技术上*确实*可以装入一个区块中。

在主网链上：

* 我见过的单笔交易中输出最多的是 13,107 个：[dd9f6bbf80ab36b722ca95d93268667a3ea6938288e0d4cf0e7d2e28a7a91ab3](/explorer/tx/dd9f6bbf80ab36b722ca95d93268667a3ea6938288e0d4cf0e7d2e28a7a91ab3)
* 我见过的最大的 ScriptPubKey 是 4,026 字节：[e411dbebd2f7d64dafeef9b14b5c59ec60c36779d43f850e5e347abee1e1a455](/explorer/tx/e411dbebd2f7d64dafeef9b14b5c59ec60c36779d43f850e5e347abee1e1a455)

但即便如此，两者也均远未达到需要使用紧凑大小前缀 `FE` 的程度。

野外发现 `FE` 或 `FF` 前缀的唯一时刻是它被错误地用于存储本可以放入更小紧凑大小字段的数字。

## 位置

以下是您最常发现紧凑大小字段的地方：

* [交易数据](#transaction-data)
* [区块数据](#block-data)
* [网络消息](#network-messages)

### 交易数据

紧凑大小字段贯穿于原始[交易](/docs/technical/transaction.md)数据中。它们用于指示：

* [输入](/docs/technical/transaction/input.md)的数量。
* [输出](/docs/technical/transaction/output.md)的数量。
* [ScriptSig](/docs/technical/transaction/input/scriptsig.md) 的大小。
* [ScriptPubKey](/docs/technical/transaction/output/scriptpubkey.md) 的大小。
* [witness](/docs/technical/transaction/witness.md) 元素的数量。（[SegWit](/docs/technical/upgrades/segregated-witness.md) 交易）
  + 每个 witness 元素的大小。

这里是一个传统的遗留交易示例（[414719d592b73341b77497165d9f46f6eff6c243469265f95d920b779c7a0492](/explorer/tx/414719d592b73341b77497165d9f46f6eff6c243469265f95d920b779c7a0492)）。我已将原始交易数据拆分为单独的字段，并用绿色高亮了紧凑大小字段：

```
01000000
  01 <-input count
    79fe743502ff8cd181121572fececac3feee5ef3034edfb3ccd2bfaa24537dae00000000
    6b <-scriptsig size
      483045022100d39e64d275f0e69d5a2722ad93e3e206e98bf03584525cec05b5fcb75dc3e5a8022071fc39e3784be3a76d8469ed13ade270d8da25677fc5a226c5e7223a85701c7c012102b0453d54d1e0c0b41a63b3ca898afc4cc4243ed0241a9cc116e37854969a2270
    ffffffff
  01 <-output count
    72c9000000000000
    19 <-scriptpubkey size
      76a91400bafac9185e183c1203025fbdac30a4be5af91088ac
00000000
```

这里是一个 SegWit 交易示例（[672d9428242a097e57c5def8b300d05068e0d85a1028ac3e93c9a487561f36c9](/explorer/tx/672d9428242a097e57c5def8b300d05068e0d85a1028ac3e93c9a487561f36c9)），同样以绿色突出显示了紧凑大小字段：

```
01000000
    0001
    01 <-input count
        53baeaeed4799240f2a48e99fcc6e504672120764d622e4e5af9fd04b37a8293
        05000000
        00 <-scriptsig size
        ffffffff
    01 <-output count
      4ac7010000000000
      17 <-scriptpubkey size
        a914f314b4ac619e1d3f96a5ffac796b17e0a47b52b987
    02 <-witness element count
      47 <- witness element size
        3044022064576f10eee1b679648965b72081a636ac46b21be3e36558585775fc523dbcdf0220440b31af77adcbc75cf79679406d8ba1e2c14ff03d02606725d29ffdaa028a5f01
      21 <- witness element size
          021ce981c19e4f998b62091ffd960549ead5f8ced3de7fc919d5d4a25e6edf42cd
00000000
```

### 区块数据

紧凑大小字段在原始区块数据中被使用了一次。它指示：

* 区块中的交易数量。

例如，这是创世区块（[000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f](/explorer/block/000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f)），其中仅有一笔交易：

```
01000000
0000000000000000000000000000000000000000000000000000000000000000
3ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4a
29ab5f49
ffff001d
1dac2b7c
01 <-transaction count
01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff4d04ffff001d0104455468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73ffffffff0100f2052a01000000434104678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5fac00000000
```

它位于[区块头](/docs/technical/block.md#header)和交易数据之间。这是紧凑大小字段在原始区块（不包括交易）中被使用的唯一时刻。

### 网络消息

紧凑大小字段在节点在比特币[网络](/docs/technical/networking.md)上互相发送的各种[消息](https://en.bitcoin.it/wiki/Protocol_documentation#Message_types)中被使用。

例如，["inv" 消息](/docs/technical/networking.md#inv)的有效载荷使用紧凑大小字段来指示即将到来的项目的数量：

```
01 01000000aa325e9122aa39ca18c75aabe2a3ceaf9802acd1a40720925bfd77fff58ed821
```

此消息指示列表中有一个项目，正是此 [txid](/docs/technical/general/byte-order.md#reverse-byte-order)：[21d88ef5ff77fd5b922007a4d1ac0298afcea3e2ab5ac718ca39aa22915e32aa](/explorer/tx/21d88ef5ff77fd5b922007a4d1ac0298afcea3e2ab5ac718ca39aa22915e32aa)。

*交易*和*区块*实际上也是在比特币网络上传输的消息。因此紧凑大小字段有助于在节点之间发送的序列化*消息*中节省空间。您总是希望在线路上发送尽可能少的数据（出于效率原因），这正是紧凑大小的用武之地。

## 优势

为什么比特币中要使用紧凑大小字段？

紧凑大小字段节省了几个字节的空间。

例如，您可以在一笔交易中非常轻松地装入几千个输出，但绝大多数时候您只创建一到两个输出。因此对于 *输出数量 count* 字段，基本的方案是让它在任何时候都成为一个固定的 2 字节字段，以便在罕见情况下容纳大量的输出，即使绝大多数时间都不需要。例如，跨越 10 笔交易，您可能会有以下字段：

```
固定 2 字节字段：

数量    | 字节表示
--------|------
 2      | 0002
 2      | 0002
 1      | 0001
 2      | 0002
 27     | 001B
 3      | 0003
 3000   | 0BB8
 2      | 0002
 1      | 0001
 2      | 0002

 总计字节数 = 40
```

但通过使用灵活的紧凑大小字段，我们可以在大部分时间里使用 1 字节的字段大小，并在少数需要容纳更大数字的罕见场合中扩展至 3 字节（1 字节前缀 + 2 字节数字）。以相同的 10 笔交易为例：

```
紧凑大小字段：

数量    | 字节表示
--------|------
 2      | 02
 2      | 02
 1      | 01
 2      | 02
 27     | 1B
 3      | 03
 3000   | FD0BB8
 2      | 02
 1      | 01
 2      | 02

 总计字节数 = 24
```

这是一种微小的空间节省技术。但当您在一笔交易中拥有多个此类字段，且每天有数十万笔交易在计算机之间传输（以及在[区块链](/docs/technical/blockchain.md)中存储数十亿笔交易）时，节省的字节数就会聚沙成塔。

## 代码

以下是一个展示如何在 Ruby 中进行整数与紧凑大小相互转换的快速代码示例：

```
# pack()       - converts an integer to raw bytes of a specific length and byte order (e.g. little-endian) based on the directive given
# unpack("H*") - converts raw bytes to a hexadecimal string

# Directives:
#
# C  =  8-bit integer
# S< = 16-bit integer, little-endian
# L< = 32-bit integer, little-endian
# Q< = 64-bit integer, little-endian

def encode(i)
    # convert integer to a hex string with the correct prefix depending on the size of the integer
    if (                     i <= 252)                  then compactsize =        [i].pack("C").unpack("H*")[0]
    elsif (i > 252        && i <= 65535)                then compactsize = 'fd' + [i].pack("S<").unpack("H*")[0]
    elsif (i > 65535      && i <= 4294967295)           then compactsize = 'fe' + [i].pack("L<").unpack("H*")[0]
    elsif (i > 4294967295 && i <= 18446744073709551615) then compactsize = 'ff' + [i].pack("Q<").unpack("H*")[0]
    end

    return compactsize
end

def decode(compactsize)
    # get the first byte
    first = compactsize[0...2]

    # get the correct number of bytes from the hex string, then convert this hex string to an integer
    if    (first == "fd") then i = [compactsize[2...6]].pack("H*").unpack("S<")[0]
    elsif (first == "fe") then i = [compactsize[2...10]].pack("H*").unpack("L<")[0]
    elsif (first == "ff") then i = [compactsize[2...18]].pack("H*").unpack("Q<")[0]
    else                       i = [compactsize[0...2]].pack("H*").unpack("C")[0]
    end

    return i
end


# Encode Examples
puts encode(0)                    #=> 00
puts encode(252)                  #=> fc

puts encode(253)                  #=> fdfd00
puts encode(65535)                #=> fdffff

puts encode(65536)                #=> fe00000100
puts encode(4294967295)           #=> feffffffff

puts encode(4294967296)           #=> ff0000000001000000
puts encode(18446744073709551615) #=> ffffffffffffffffff

# Decode Examples
puts decode("00")                 #=> 0
puts decode("fc")                 #=> 252

puts decode("fdfd00")             #=> 253
puts decode("fdffff")             #=> 65535

puts decode("fe00000100")         #=> 65536
puts decode("feffffffff")         #=> 4294967295

puts decode("ff0000000001000000") #=> 4294967296
puts decode("ffffffffffffffffff") #=> 18446744073709551615
```

## 总结

紧凑大小字段用于在网络消息（例如原始交易数据）中指示接下来的项目数量或后续数据的长度。它通常为 1 字节大小，但当需要对更大的数字进行编码时，可以扩展至 9 字节长度。

自比特币的第一个版本 (v0.1.0) 发布以来，它就已经是协议的一部分，可以在 [serialize.h](https://github.com/bitcoin/bitcoin/blob/master/src/serialize.h) 中找到。我相信这种紧凑大小的编码是中本聪在编程开发比特币时自己发明的，因为我还没在其他任何地方见过它被使用。

### Compact Size 与 VarInt 的对比

我曾经以为紧凑大小字段叫做 *VarInt*（可变整数）。它们都以紧凑格式对可变长度整数进行编码，但它们实际上具有不同的结构：

* **Compact Size** – 第一个字节指示您需要读取多少个字节来计算整数值。您会在许多在比特币网络中发送的序列化消息（例如交易和区块）中找到它。
* **VarInt** – 您持续读取字节，直到首个 bit 未被设置，然后将这些字节组合在一起以计算整数。您会在 [LevelDB Chainstate 数据库中找到 VarInt](https://github.com/in3rsha/bitcoin-chainstate-parser/blob/master/README.md#varints)。

因此，它们具有相似的目的，但工作方式截然不同。

我过去曾在这个网站上将紧凑大小字段称为“VarInt”。为引起混淆深表歉意。您也可以在 [BIP 141](https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki#transaction-id) 中发现紧凑大小字段被称为 var\_int。

其他程序中，这种针对整数的可变长度字节结构也被称为“可变长度编码”。它可以在 UTF-8 编码、MIDI 文件格式和 WAP（无线应用协议）中被发现。然而它们与比特币中发现的“紧凑大小”结构工作起来略有不同。

## 资源

* <https://developer.bitcoin.org/reference/transactions.html#compactsize-unsigned-integers>