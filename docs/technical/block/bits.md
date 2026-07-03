<img src="../../images/icons_loader-2.svg" alt="Loading Tool" style="height:32px; width:32px;" />

[<img src="../../images/diagrams_png_block-bits.png" alt="Diagram showing the target being stored in the bits field of a block header." width="646" height="291" />](https://static.learnmeabitcoin.com/diagrams/png/block-bits.png)

bits 字段包含[target](/docs/technical/mining/target.md)的紧凑表示形式。

它指示了区块哈希（[block hash](/docs/technical/block/hash.md)）必须低于多少才能被[开采](/docs/technical/mining.md)，并且它必须表示比特币[区块链](/docs/technical/blockchain.md)中该区块高度的正确目标值。

当前

随机示例

高度:

目标

0x

`0 bytes`

Bits`0 bytes`



0 秒

## 结构

bits 字段是如何表示目标的？

[<img src="../../images/diagrams_png_block-bits-to-target.png" alt="Diagram showing the exponent and coefficient of the bits field and how they convert to a full 32-byte target value." width="832" height="223" />](https://static.learnmeabitcoin.com/diagrams/png/block-bits-to-target.png)

bits 字段包含两部分：

1. **指数 (Exponent，首字节)：** 这是系数“向上移动”了多少。
2. **系数 (Coefficient，接下来的3个字节)：** 这包含了完整目标值中的一些精度。

## 转换

如何在目标和 bits 之间进行转换？

### Bits 转换为 Target

要将 *bits* 转换为 *target*，您需要将**系数向左移动指数所指示的指定*字节*数**。

例如：

```
Bits: 1705dd01

                           coefficient (05dd01)
                           ------
Target: 00000000000000000005dd010000000000000000000000000000000000000000
                           <---------------------------------------------
                           exponent (0x17 = 23 bytes)
```

## 代码

```
# bits
exponent = 0x17
coefficient = 0x05dd01

# target
target = coefficient * 2**(8 * (exponent - 3))
# 2**            = using a power of two for bit-shifting
# (8 *           = there are 8 bits in a byte
# (exponent - 3) = leave space for the coefficient to fill 

# target (hex)
target_hex = target.to_s(16)

puts target_hex #=> 5dd010000000000000000000000000000000000000000
```

### Target 转换为 Bits

将目标转换为 bits 字段是 bits 转换为目标的逆过程。您从目标中提取前 3 个有效字节，然后计算出它们向左移动了多少个字节。

例如：

```
                           coefficient (05ae3af)
                           ------
Target: 00000000000000000005ae3af5b1628dc0000000000000000000000000000000
                           <---------------------------------------------
                           exponent (0x17 = 23 bytes)

Bits: 1705ae3a
```

不要忘记您要寻找系数的第一个有效**字节**。这就是为什么第一个有效字节是 `05` 而不是 `5a`，因为 `5` 和 `a` 属于两个不同的字节。

系数的第一个有效字节必须低于 `80`。如果不是，您必须在前面加上 `00` 作为第一个字节。

这是因为比特币对比特币的 [uint256](https://github.com/bitcoin/bitcoin/blob/master/src/arith_uint256.cpp) 值使用了一种自定义的编码方式；如果设置了 `00800000` 位，则表示它是一个负值。所以如果这个系数高于 `007fffff`，就表示它是一个负值，而目标值不能是负数。

例如，区块 [489,888](/explorer/489888#blockchain) 的完整目标是：

```
Target: 000000000000000000eb304f6a76a77000000000000000000000000000000000
```

然而，第一个有效字节是 `eb`。这大于 `7f`，所以我们必须在它前面使用 `00` 字节，以防止该系数表示一个负数：

```
                        coefficient
                        ------
Target: 000000000000000000eb30000000000000000000000000000000000000000000
                        <-----------------------------------------------
                        exponent (0x18 = 24 bytes)
              
Coefficient: 00eb30
Exponent: 18

Bits: 1800eb30
```

如果不是因为这种自定义的 uint256 编码，bits 字段本来会是 `17eb304f`。

这就是为什么某些 bits 字段的系数以 `00` 开头的原因。

参见此处：[Why 1D00FFFF and not 1CFFFFFF as target in genesis block](https://bitcoin.stackexchange.com/questions/113535/why-1d00ffff-and-not-1cffffff-as-target-in-genesis-block)

无论如何，这种目标到 bits 的转换就是矿工在进行[目标重新计算](/docs/technical/mining/target.md#adjustment)后为他们的区块头创建 bits 字段时所做的事情。

<img src="../../images/icons_tool.svg" alt="Tool Icon" style="width:20px; height:20px" /> 目标调整 (Target Adjustment)

上一次调整
当前目标

0x

`0 bytes`


时间 (秒)

实际

0d

预期

0d

目标调整周期为 2016 个区块。一个区块平均每 600 秒（10 分钟）开采一次，因此预期时间为 2016 \* 600 = 1209600 秒。

比例

实际时间除以预期时间。我们将当前目标乘以该比例以获得新目标。

新目标 (全精度)

0x

新目标

0x

`0 bytes`

注意：此目标值已被轻微截断，以便存储在区块头的 bits 字段中，而这正是挖矿时实际使用的目标值。



0 秒

将目标转换为 bits 时，您确实会丢失一些精度。但是，数字是如此之大，以至于它并没有什么实质性影响，所以没有必要在区块头中存储目标的绝对精度。

目标的 "bits" 表示是矿工需要低于的实际值，以便开采区块。

## 好处

为什么我们要将目标转换为 bits 呢？

*bits* 字段可以节省区块头中的空间。

所以，我们不存储完整的 32 字节目标，而是存储它的 4 字节紧凑表示形式。

## 目的

为什么区块头包含目标？

*bits* 字段有两个主要功能：

1. **用于快速找出该区块的目标是什么。**
2. **它是区块哈希必须低于的*实际*精度级别，以便开采区块。** 因此，即使目标重新计算后的完整目标值具有更高的精度，区块哈希实际需要低于的也是 bits 字段的精度。

例如，在区块 [40,320](/explorer/40320#blockchain) 处的目标重新计算期间，这本来是完整的目标：

```
Target: 00000000654657a76a76a8000000000000000000000000000000000000000000
```

但矿工需要低于的*实际*目标是 bits 字段中可以存储的精度大小，即：

```
Target: 0000000065465700000000000000000000000000000000000000000000000000
```

但正如我所说，这里的精度丢失并不是什么大问题。我从未见过任何一个区块是以低于截断的目标但高于原始目标计算的哈希值开采出来的。

然而，中本聪并没有必要在区块头中包含目标的紧凑表示形式。节点会在内部计算目标值，因此在区块头中包含目标是冗余的。

尽管如此，中本聪还是决定这么做，可能是为了某种便利。移除它需要进行一次[硬分叉](/docs/technical/blockchain/hard-fork.md)，并且这样做不值得，所以这就是为什么它今天仍然是区块头的一部分。

## 术语

为什么它被称为 "bits"？

我不知道为什么这个字段被称为 "bits"。中本聪从未解释过他们选择这个字段名称背后的原因。

但这有点尴尬，因为“[bit](/docs/technical/general/bytes.md#bit)”（位）是用于最小数据单位的单词（即一个字节有 8 位），这有点令人困惑。

也许是因为他们从目标中存储了*一些位*（而不是完整的精度），所以 "bits" 是该字段的一个快速且简单的名称。我的意思是，在编程时我们都使用快速的变量名，而它们并不总是完美的。

## 资源

* [Do Miners have to get below the Target or the Bits value?](https://bitcoin.stackexchange.com/questions/43722/do-miners-have-to-get-below-the-target-or-the-bits-value)
* [Why is the target stored in compact form in the block header?](https://bitcoin.stackexchange.com/questions/36744/why-is-the-target-stored-in-compact-form-in-the-block-header)
* [Why are block header bits necessary?](https://bitcoin.stackexchange.com/questions/81574/why-are-block-header-bits-necessary-valid-difficulty-is-already-implied-by-cha)