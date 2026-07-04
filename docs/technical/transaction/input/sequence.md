<img src="../../../images/icons_loader-2.svg" alt="Loading Tool" style="height:32px; width:32px;" />

[<img src="../../../images/diagrams_png_transaction-sequence.png" alt="Diagram of showing the sequence fields alongside each transaction input." width="503" height="423" />](../../../images/diagrams_png_transaction-sequence.png)

sequence（序列号）字段存在于每个交易 [input](../input.md) 内部。它允许你控制一笔交易**何时可以被打包挖出**，或者一笔交易在[内存池 (mempool)](../../mining/memory-pool.md) 中时**是否可以被替换**。

用更具技术性的术语来说，可以说 sequence 字段控制着交易的“终结性 (finality)”，即一笔交易在被打包挖入区块之前是否处于其“最终”状态。如果它不处于“最终”状态，那么在它最终进入[区块链](../../blockchain.md)之前，它是有可能被替换的。

以下是最常见的设置：

* <=0xFFFFFFFE — **Locktime**。
  此设置允许使用交易的 [locktime](../locktime.md) 字段。
* <=0xFFFFFFFD — **Replace By Fee (RBF)**。
  此设置启用了 RBF 功能，如果交易仍处于内存池中，允许你用手续费更高的一笔交易替换它。
* <=0xEFFFFFFF — **相对锁定时间 (Relative Locktime)**。
  此设置允许你根据被花费的输出何时被挖出，在交易上设置相对锁定时间。
  * 0x00000000 到 0x0000FFFF — **区块。** 以区块数量设置相对锁定时间。
  * 0x00400000 到 0x0040FFFF — **时间。** 以秒数设置相对锁定时间。

一个普遍的选择是为你的 sequence 字段使用 0xFFFFFFFD，因为这既启用了 locktime 字段（如果你想使用它的话），也启用了 replace-by-fee（这通常很有用）。

Sequence (小端序)

原始交易数据中的 sequence 形式

0x

`4 bytes`

Sequence (大端序)

0x

`4 bytes`

功能

 锁定时间 (Locktime)
 提升费用替换 (Replace-by-Fee)
 相对锁定时间 (Relative Locktime)

相对锁定时间类型

 时间 (Time)
 秒 (seconds)
 区块 (Blocks)

数量 (Count)



0 secs

如果你将一笔交易中 *所有* inputs 的 sequence 都设置为最大值 0xFFFFFFFF，那么这整笔交易就被认为是“最终确定”的，无法被替换，也无法阻止其被打包挖出。

你只需设置 *其中一个* sequence 字段即可启用 **locktime** 或 **RBF**（即使一笔交易中包含多个 inputs 和 sequence 字段）。然而，**相对锁定时间 (relative locktime)** 设置对于每个 input 都是特定的。

## Locktime

[<img src="../../../images/diagrams_png_transaction-sequence-locktime.png" alt="Diagram showing the sequence field being set to enable the locktime field of a transaction." width="722" height="336" />](../../../images/diagrams_png_transaction-sequence-locktime.png)

如果你将 *任何* input 的 sequence 值设置为 0xFFFFFFFE 或更低，你就可以为整笔交易启用 [locktime](../locktime.md) 字段。

例如：

```
0xFFFFFFFE <- 启用 locktime
```

如前所述，将交易中的所有 sequence 值设置为 0xFFFFFFFF 表示该交易是 *最终确定* 的。因此，通过将任何 sequence 设置为 *低于最大值* 0xFFFFFFFF，即表示该交易是 *非最终确定* 的，因此 locktime 字段将被启用。

默认情况下，[Bitcoin Core](https://bitcoin.org/en/bitcoin-core/) 钱包为每个 input 的 sequence 字段设置为 0xFFFFFFFE。这会启用交易的 locktime 字段，但不会启用其他功能。

### 使用

如果你希望交易仅在未来的某个时间点才能被[打包挖出](../../mining.md)，你需要利用交易末尾的 locktime 字段。

要启用 locktime 字段，你需要将交易中的 sequence 值之一设置为 0xFFFFFFFE 或更低。

然后，你可以将 locktime 字段设置为 0 到 499999999 之间，以使交易能够在特定的区块[高度](../../blockchain/height.md)之后被打包挖出；或者设置为 500000000 到 4294967295 之间，以使其在特定时间点（即 Unix 时间戳）之后被打包挖出。

<img src="../../../images/icons_tool.svg" alt="Tool Icon" style="width:20px; height:20px" /> Unix 时间 (Unix Time)

Unix 时间

0d

当前

日期

0 secs

## Replace By Fee (RBF)

[BIP 125](https://github.com/bitcoin/bips/blob/master/bip-0125.mediawiki)

[<img src="../../../images/diagrams_png_transaction-sequence-replace-by-fee.png" alt="Diagram showing the sequence field being set to enable the replace by fee feature on a transaction." width="733" height="503" />](../../../images/diagrams_png_transaction-sequence-replace-by-fee.png)

你可以通过将 *任何* input 的 sequence 值设置为 0xFFFFFFFD 或更低，来允许交易稍后（在它仍处于[内存池](../../mining/memory-pool.md)中时）被手续费更高的一笔交易替换。

例如：

```
0xFFFFFFFD <- 启用 replace-by-fee
```

这个值比上面的 [locktime](#locktime) 设置**小 1**，这意味着你可以仅启用 locktime 而 *不* 启用 replace-by-fee.

### 使用

假设你创建了一笔交易并将其发送到了[网络](../../networking.md)中，但你在其上设置了一个极低的[手续费](../fee.md)。

如果网络上有大量的高手续费交易，你的交易可能会一直悬在内存池中等待被打包挖出。通常情况下，你无法撤销或替换此交易，直到它被打包挖出或在内存池中过期，但这可能需要几天时间。

但是，如果你在交易的任何 input 上将 sequence 值设置为 0xFFFFFFFD，你就是在发出信号：任何这些 inputs 都可以被一笔带有更高手续费的新交易花费。因此，你不用等第一笔交易被打包挖出，而是可以发送一笔替代交易来加快这一过程。

节点和矿工会意识到某笔交易的 sequence 被设置为 0xFFFFFFFD 或更低，因此，如果有手续费更高的一笔交易到来，他们会乐意在内存池中替换掉那笔旧交易。

关于使用 RBF 的几点注意事项：

* **你不需要在替代交易中增加或减少 sequence 数值。** 唯一关键的是替代交易具有更高的手续费。
* **只要新交易的手续费比你要替换的交易更高，你就可以一次又一次地替换交易。** 替换的次数越多，每次就需要更高的手续费来超越之前的替代交易手续费。
* **如果你愿意，你可以在替代交易中把代币发送到不同的目的地（即创建不同的 [outputs](../output.md)）。** 这也是为什么这有时被称为“Full RBF”（完全 RBF）的原因，因为其他 RBF 提案要求替代交易具有相同的 outputs。

**RBF 是整笔交易范围的，而不是 input 特定的。** 在任何一个 input 上将 sequence 设置为 0xFFFFFFFD 或更低都会使*整笔交易*可被替换。因此，即使你在同一交易中的其他 inputs 上赋予了最大值 0xFFFFFFFF，那些独立的 inputs 也可以在高手续费的替代交易中被花费。

### 设置更高手续费

[<img src="../../../images/diagrams_png_transaction-replace-by-fee-increase.png" alt="Diagram showing the transactions fees on replacement transactions including the size of the fees of the transactions they are replacing." width="355" height="284" />](../../../images/diagrams_png_transaction-replace-by-fee-increase.png)

替代交易上的手续费必须足以覆盖*最低中继费*，**外加它所替代的交易的手续费大小**。

```
RBF 交易最低手续费 = 最低中继费 + 前一笔交易手续费
```

**[最低中继费](../fee.md#minimum-relay-fee)：**

这是你必须在交易中设置的*最低*手续费，以便节点能够将其接受到内存池中。每个节点都可以独立设置此费用，但默认是 1 sat/[vbyte](../size.md#virtual-bytes)。这有助于防止有人用“免费”交易对网络进行垃圾邮件攻击。

### RBF 示例

假设当前最低中继费是 **1 sat/[vbyte](../size.md#virtual-bytes)**。

对于一个简单的*提升费用*交易（替代交易与原交易完全相同），替代交易的手续费只需至少是你要替换交易手续费的*两倍*：

```
最低中继费：1 sat/vbyte

交易          | 大小      | 最低中继费   | 前一交易费      | 最低费用     | 费率
--------------|-----------|---------------|-----------------|--------------|------------
原始交易      | 200 字节  | 200 sats      | 0               | 200 sats     | 1 sat/vbyte
替代交易 1    | 200 字节  | 200 sats      | 200 sats        | 400 sats     | 2 sat/vbyte
```

因此在这个例子中，替代交易的手续费本身需要至少 200 sats（以满足 1 sat/vbyte 的最低中继费），*外加* 我们要替换的交易的 200 sats 手续费，使得最低手续费总共为 400 sats。如果你愿意，你可以设置比这高得多的费用，而且为了创造更有吸引力的费率你可能确实会这么做，但这就是*最低要求*。

现在，如果你要多次替换交易（反复调高手续费），下一笔交易的最低费用需要大于**你要替换的所有先前交易的手续费总和** *外加* 当前交易的最低中继费（如往常一样）：

```
最低中继费：1 sat/vbyte

交易          | 大小      | 最低中继费   | 前一交易费      | 最低费用     | 费率
--------------|-----------|---------------|-----------------|--------------|------------
原始交易      | 200 字节  | 200 sats      | 0               | 200 sats     | 1 sat/vbyte
替代交易 1    | 200 字节  | 200 sats      | 200 sats        | 400 sats     | 2 sat/vbyte
替代交易 2    | 200 字节  | 200 sats      | 400 sats        | 600 sats     | 3 sat/vbyte
```

下面是另一个替代交易体积大小不同（这也是完全允许的）的例子：

```
最低中继费：1 sat/vbyte

交易          | 大小      | 最低中继费   | 前一交易费      | 最低费用     | 费率
--------------|-----------|---------------|-----------------|--------------|---------------
原始交易      | 200 字节  | 200 sats      | 0               |  200 sats    | 1 sat/vbyte
替代交易 1    | 800 字节  | 800 sats      | 200 sats        | 1000 sats    | 1.25 sat/vbyte
替代交易 2    | 300 字节  | 300 sats      | 1000 sats       | 1300 sats    | 4.33 sat/vbyte
替代交易 3    | 200 字节  | 200 sats      | 1300 sats       | 1500 sats    | 7.50 sat/vbyte
```

所以基本上，要算出下一个更高的手续费，你只需把你要替换的交易手续费相加。*最低费用*便是所有这些先前费用与当前交易最低中继费的总和。

但一般而言，对于简单的 RBF 交易，你只需将前一笔交易的手续费增加一倍即可。

## 相对锁定时间 (Relative Locktime)

[BIP 68](https://github.com/bitcoin/bips/blob/master/bip-0068.mediawiki)

[<img src="../../../images/diagrams_png_transaction-sequence-relative-locktime.png" alt="Diagram showing the sequence field being used to set a relative locktime on the transaction." width="741" height="336" />](../../../images/diagrams_png_transaction-sequence-relative-locktime.png)

> 相对锁定时间（RLT）使已签名的交易输入在其相对应的输出确认后的一段指定时间内保持无效。
> 
> —— [BIP 68](https://github.com/bitcoin/bips/blob/master/bip-0068.mediawiki)

相对锁定时间允许你**指定在被花费的输出被确认打包之后，经过多长时间或多少个区块，花费该输出的交易才会生效**。

交易的 locktime 允许你指定交易可以被打包挖出的*绝对*时间，而相对锁定时间允许你指定相对时间（从被花费输出被打包的那刻起算）。

要在某个 input 上设置相对锁定时间，你需要将 sequence 视作一个包含 32 个独立位的字段（即[位字段 (bit field)](../../general/bytes.md#bit-field)）：

Sequence (小端序)

原始交易数据中的 sequence 形式

0x

`4 bytes`

Sequence (大端序)

0x

`4 bytes`

Sequence (位字段)

0
0
0
0
0
0
0
0
0
1
0
0
0
0
0
0
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1

设置

 禁用标志 (Disable Flag)
 类型标志 (Type Flag)

相对锁定时间

 时间 (Time)
 数值 (Value)
 `x 512 = 0 seconds`

 区块 (Blocks)
 数值 (Value)

0 secs

* **第 31 位：禁用标志 (Disable Flag)**
  * 1 = 相对锁定时间已禁用
  * 0 = 相对锁定时间已启用
* **第 22 位：类型标志 (Type Flag)**
  * 1 = 时间（其值乘以 512，得到以秒为单位的时间）
  * 0 = 区块
* **第 15-0 位：数值 (Value)**
  * 这 16 位可以容纳 0 到 65535 (0x0000 到 0xffff) 之间的任何数值

首先，要启用相对锁定时间设置，你需要将**禁用标志 (disable flag)**（第 31 位）设置为 0。虽然将某项设置为零来开启它有点反直觉，但这里就是这样工作的。因为第一位被设置为零，所以所有的相对锁定时间设置都将始终小于或等于 0xEFFFFFFF。

其次我们有**类型标志 (type flag)**（第 22 位），它允许你选择以*时间量*还是*区块数量*来设置自从被花费输出被确认以来的相对锁定时间。

最后，最后 16 位包含以*区块*或*时间*计算的实际**数值**（第 15-0 位）。如果你选择*时间*，该值会乘以 512 得到以秒为单位的相对锁定时间。

当使用相对锁定时间时，RBF 和绝对锁定时间将被自动启用。

要启用相对锁定时间，交易的**版本 (version) 必须为 2 或更大**。

### 为什么时间值会乘以 512？

因为这会在设置区块数与秒数之间创造一个类似的范围。

例如，区块之间平均有 600 秒（10 分钟），而对于两种相对锁定时间类型，你能放置的最大值都是 65535 (0xffff)，因此：

```
最大区块数 = 65535 * 600 = 39321600 秒 = 455.11111 天
最大时间   = 65535 * 512 = 33553920 秒 = 388.35556 天
```

所以无论你使用的是区块*或*时间的类型标志，你都能将**最大相对锁定时间设置为未来略多于一年的时间**。

但为什么要乘以 512 而不是 600？因为 512 是 2^9，这意味着你可以快速进行向左移位 9 位的位运算来将该值转换为秒。这比乘以 600 更加高效，且 512 是你能得到的、最接近 600 的 2 的幂。

```
0b0000000001 = 1
0b1000000000 = 512（在计算机上进行位移比乘法更快）
```

> 位移非常廉价。
> 
> —— Mark Friedenbach（BIP 68 作者），（通过电子邮件）

### 相对锁定时间示例

设置 65535 \* 512 = 33553920 秒的相对锁定时间：

```
┌─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┐
│0│0│0│0│0│0│0│0│0│1│0│0│0│0│0│0│1│1│1│1│1│1│1│1│1│1│1│1│1│1│1│1│
└─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┘
  
0x0040ffff
```

设置 1 \* 512 = 512 秒的相对锁定时间：

```
┌─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┐
│0│0│0│0│0│0│0│0│0│1│0│0│0│0│0│0│0│0│0│0│0│0│0│0│0│0│0│0│0│0│0│1│
└─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┘

0x00400001
```

设置 65535 个区块的相对锁定时间：

```
┌─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┐
│0│0│0│0│0│0│0│0│0│0│0│0│0│0│0│0│1│1│1│1│1│1│1│1│1│1│1│1│1│1│1│1│
└─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┘

0x0000ffff
```

设置 1 个区块的相对锁定时间：

```
┌─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┐
│0│0│0│0│0│0│0│0│0│0│0│0│0│0│0│0│0│0│0│0│0│0│0│0│0│0│0│0│0│0│0│1│
└─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┘

0x00000001
```

完全禁用相对锁定时间：

```
┌─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┐
│1│0│0│0│0│0│0│0│0│0│0│0│0│0│0│0│0│0│0│0│0│0│0│0│0│0│0│0│0│0│0│0│
└─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┘
  
0x80000000
```

0 个区块的相对锁定时间 (0x00000000) 意味着该 input 可以立即打包进区块而无需等待。这相当于没有设置相对锁定时间，因此你也可以使用 0xFFFFFFFF 序列号。

任何 0x80000000 或以上的 sequence 值都将禁用相对锁定时间功能。

### 代码

```
# -----------------
# Bitwise Operators
# -----------------
#
# The easiest way to work with bits directly is by using "bitwise operators". These are available in all good programming languages:
#
#  << - "SHIFT LEFT" - Move bits a number of positions to the left
#  |  - "OR"         - Combine two sets of bits
#  &  - "AND"        - Extract bits from a set of bits using a "bit mask"

# ---------------------------
# Construct Relative Locktime
# ---------------------------

# Set Disable Flag (0 = enabled, 1 = disabled)
disable = 0<<31 # Move a zero 31 bits to the left. Pointless really as this is just 0, but whatever
# 00000000000000000000000000000000

# Set Type Flag (0 = blocks, 1 = time)
type    = 1<<22 # Move a one 22 bits to the left.
#          10000000000000000000000

# Set Value
value   = 10000 # This is just an integer; every integer has its own underlying bit representation
#                   10011100010000

# Combine all of the bits together into a single field
sequence = 0<<31 | 1<<22 | 10000
# disable  = 00000000000000000000000000000000
# type     =          10000000000000000000000 |
# value    =                   10011100010000 | (The OR bitwise operator returns a 1 if either bit is set)
#            --------------------------------
#            00000000010000000010011100010000


# Ruby will print this value as an integer by default, but for display purposes we can convert it to a string of bits (base 2)
bits = sequence.to_s(2)
puts bits #=> 10000000010011100010000

# We can also convert the sequence value to a hexadecimal string (base 16)
hex  = sequence.to_s(16)
puts hex #=> "402710"


# ------
# Decode
# ------

# Sequence
sequence = 0x00402710

# Extract Disable Flag
disable = 1<<31 & sequence
# 1<31     = 10000000000000000000000000000000
# sequence = 00000000010000000010011100010000 & (The AND operator returns a 1 if both bits are set)
#            --------------------------------
#            00000000000000000000000000000000 = 0

# Extract Type Flag
type = 1<<22 & sequence
# 1<22     = 00000000010000000000000000000000
# sequence = 00000000010000000010011100010000 &
#            --------------------------------
#            00000000010000000000000000000000 = 4194304 (Anything other than zero means this bit has been set)

# Extract Value
value = 0xffff & sequence # 0xffff is the bit mask
# 0xffff   = 00000000000000001111111111111111
# sequence = 00000000010000000010011100010000 &
#            --------------------------------
#            00000000000000000010011100010000 = 10000

# Show results
puts (disable ? 'true' : 'false')
puts (type ? 'time' : 'blocks')
puts value #=> 10000
```

## 示例

这里有几个在区块链实际交易中使用 sequence 值的例子：

* [2833fece3b1c38dffc11a7f211b05512512b0f8dec7055b6d7e7c155d83e7dec](/explorer/tx/2833fece3b1c38dffc11a7f211b05512512b0f8dec7055b6d7e7c155d83e7dec#input-0) (Input 0)
  * Sequence = `fffffffe`
  * **锁定时间启用。** 并且 locktime 字段的值为 699999，所以这笔交易在区块 699,999 *之后*才能被打包挖出。它最终在区块 [700,000](/explorer/700000) 中被确认。
* [163558ace2946d805b688d89d8ba0dd607d9f947073b45f393d9757eef1a4af7](/explorer/tx/163558ace2946d805b688d89d8ba0dd607d9f947073b45f393d9757eef1a4af7#input-0) (Input 0)
  * Sequence = `fffffffd`
  * **RBF 启用。** 无法判断这笔交易是否被替换过，但当它在内存池中时它是可以被替换的。
* [62fb5ecd3f022a2f09b73723b56410db0545923516b611013aed5218e4979322](/explorer/tx/62fb5ecd3f022a2f09b73723b56410db0545923516b611013aed5218e4979322#input-0) (Input 0)
  * Sequence = `00000090`
  * **相对锁定时间启用 (区块)。** 这交易在被花费输出被确认打包后的 144 个区块 (0x0090 = 144) *之后*才能打包挖出。被花费输出是在区块 [603,018](/explorer/603018) 中被确认的，这笔交易则在 **146 个区块之后**的 [603,164](/explorer/603164) 中被打包挖出。
* [12fa403cb22bf08c4c5542cc00673495a0c54c9cc8181bea850a12d40d7593a2](/explorer/tx/12fa403cb22bf08c4c5542cc00673495a0c54c9cc8181bea850a12d40d7593a2#input-0) (Input 0)
  * Sequence = `00400007`
  * **相对锁定时间启用 (时间)。** 这交易在被花费输出确认打包后的 3584 秒 (0x0007 = 7, 7 \* 512 = 3584) *之后*才能被打包挖出。被花费输出在区块 [603,434](/explorer/603434) 中打包，其时间戳为 1573549241（*2019 年 11 月 12 日，09:00:41*），此交易则在 **6426 秒之后**的区块 [603,450](/explorer/603450) 中被确认打包，时间戳为 1573555667（*2019 年 11 月 12 日，10:47:47*）。

## 历史

sequence 字段最初设计是为了允许在交易处于内存池中时对其进行替换。

最初，你会为未来的某个时间在交易上设置 locktime，如果任何 sequence 字段低于最大值 0xFFFFFFFF，你就可以用一个具有更高 sequence 值的新版本交易来替换它。

节点和矿工被期望保留这些非最终确定的交易，直到达到 locktime，或者直到接收到一个所有 sequence 值都设置为 0xFFFFFFFF 的替代交易（意味着它最终可以打包进区块）。然而，矿工没有在内存中保留这些非最终交易的动力，所以 sequence 字段从未真正被完全用于这个目的，并在 2010 年被中本聪在 Bitcoin v0.3.12 中[悄然禁用](https://github.com/bitcoin/bitcoin/commit/05454818dc7ed92f577a1a1ef6798049f17a52e7#diff-118fcbaaba162ba17933c7893247df3aR522)。

此后，sequence 字段被多次重新设计用途，但 sequence 字段的所有更改依然与交易的“终结性”或者说在进入内存池中时（或之前）替换交易的能力相关。

## 资源

* [BIP 125: Opt-in Full Replace-by-Fee Signaling](https://github.com/bitcoin/bips/blob/master/bip-0125.mediawiki)
* [BIP 68: Relative lock-time using consensus-enforced sequence numbers](https://github.com/bitcoin/bips/blob/master/bip-0068.mediawiki)
* [What does the sequence in a transaction input mean?](https://bitcoin.stackexchange.com/questions/87372/what-does-the-sequence-in-a-transaction-input-mean)
* [Sequence number semantics](https://bitcoin.stackexchange.com/questions/53398/sequence-number-semantics)
* [What is the recommended sequence for signalling RBF?](https://bitcoin.stackexchange.com/questions/55112/what-is-the-recommended-sequence-for-signalling-rbf)
* [What is transaction "finality"?](https://bitcoin.stackexchange.com/questions/88289/what-is-transaction-finality)