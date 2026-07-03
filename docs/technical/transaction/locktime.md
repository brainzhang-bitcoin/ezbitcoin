<img src="../../images/icons_loader-2.svg" alt="Loading Tool" style="height:32px; width:32px;" />

[<img src="../../images/diagrams_png_transaction-locktime.png" alt="Diagram showing how the locktime field can be used to prevent a transaction from being mined until a specific block height or time in the future." width="722" height="336" />](https://static.learnmeabitcoin.com/diagrams/png/transaction-locktime.png)

locktime（锁定时间）字段允许你**阻止交易被打包挖出**，直到达到特定的区块**高度**或**[时间](/docs/technical/block/time.md)**之后。

包含未来 locktime 的交易也不会被节点接受或转发，因此你必须将其保存在本地，直到交易上设置的 locktime 过去。

换句话说，在交易上设置 locktime 相当于[远期支票](https://en.wikipedia.org/wiki/Post-dated_cheque)。

[<img src="../../images/technical_transaction_locktime_cheque.jpg" alt="An image of a post-dated cheque representing a transaction with a locktime of a specific block height." width="633" height="280" />](/docs/technical/transaction/locktime/cheque.jpg.md)

## 使用

locktime 是如何工作的？

locktime 字段大小为 4 字节，可容纳 0 (0x00000000) 到 4294967295 (0xffffffff) 之间的数值。

你可以通过使用不同的数值*范围*来设置特定的区块[高度](/docs/technical/blockchain/height.md)或[时间](/docs/technical/block/time.md)：

| Locktime | 描述 |
| --- | --- |
| <=499999999 | 交易在达到特定的**高度**之前不能被打包。 |
| >=500000000 | 交易在达到特定的**时间**之前不能被打包。 |

这也称为“绝对锁定时间（absolute locktime）”，因为你设置的是未来特定的高度或时间。如果需要，也可以在交易上设置[相对锁定时间](/docs/technical/transaction/input/sequence.md#relative-locktime)。

要启用 locktime 字段，[inputs](/docs/technical/transaction/input.md) 上的 [sequence](/docs/technical/transaction/input/sequence.md) 值中至少要有一个被设置为 0xfffffffe 或更低。如果所有 inputs 的 sequence 值都被设置为最大值 0xffffffff，则交易被视为“最终交易”，且 locktime 功能被禁用。

### 高度

0 到 499999999

[<img src="../../images/diagrams_png_transaction-locktime-height.png" alt="Diagram showing the locktime field being used to set a specific block height." width="724" height="344" />](https://static.learnmeabitcoin.com/diagrams/png/transaction-locktime-height.png)

通过将 locktime 设置在 0 (0x00000000) 和 499999999 (0x1dcd64ff) 之间，你可以指定该交易只能在特定的高度之后被打包到区块链中。

这是一个非常充足的范围，因为在未来的 **9488 年**内，区块链的高度预计不会达到 499,999,999。

### 时间

500000000 到 4294967295

[<img src="../../images/diagrams_png_transaction-locktime-time.png" alt="Diagram showing the locktime field being used to set a specific block time." width="722" height="336" />](https://static.learnmeabitcoin.com/diagrams/png/transaction-locktime-time.png)

通过将 locktime 设置在 500000000 (0x1dcd6500) 和最大值 4294967295 (0xffffffff) 之间，你可以指定该交易只能在特定的时间之后被打包到区块链中。

这个时间值是以 [Unix 时间 (Unix Time)](https://en.wikipedia.org/wiki/Unix_time) 表示的：

Unix 时间

0d

当前

日期

0 secs

实际的时间限制随后基于[区块头](/docs/technical/block.md#header)内部的[时间](/docs/technical/block/time.md)字段。区块内设置的时间由矿工控制，虽然它通常非常接近当前时间，但有时可能会有一到两个小时的误差。

这个范围允许你将 locktime 设置在 *1985 年 11 月 5 日，00:53:20* 和 *2106 年 2 月 7 日，06:28:15* 之间。

## 示例

这里有几个实际使用 locktime 的简单示例：

* [b0fa60f601d5fe6fb1501aa614503b9af688492f68bcf8268d7cdb30f3534079](/explorer/tx/b0fa60f601d5fe6fb1501aa614503b9af688492f68bcf8268d7cdb30f3534079)
  * Locktime: `199000`
  * 第一笔设置了特定区块高度 locktime 的有效交易。locktime 被设置为区块高度 [199,000](/explorer/199000)，该交易随后在区块 [199,002](/explorer/199002) 中被打包挖出。
* [648fe76b22bc1768b56facab73af046ea40fa190f2e882a7cc99a5b6fccf05de](/explorer/tx/648fe76b22bc1768b56facab73af046ea40fa190f2e882a7cc99a5b6fccf05de)
  * Locktime: `1358106524`
  * 第一笔设置了特定 Unix 时间 locktime 的有效交易。locktime 被设置为 1358106524（*2013 年 1 月 13 日，19:48:44*），该交易随后在时间戳为 1358111522（*2013 年 1 月 13 日，21:12:02*）的区块 [216,410](/explorer/216410) 中被打包挖出。

为了以防万一，这里有几个使用了 locktime 字段但实际上未生效的示例，因为没有一个 sequence 值被设置为低于最大值 0xffffffff：

* [13e100dd08b6da0a7426ea520b0bb3ae54cef79dd045e2e4f7116023df3a5c95](/explorer/tx/13e100dd08b6da0a7426ea520b0bb3ae54cef79dd045e2e4f7116023df3a5c95)
  * Locktime: `198370`
  * 这是有史以来第一笔为特定区块高度设置了 locktime 的交易。然而，由于唯一的 sequence 值被设置为 0xffffffff，locktime 功能未启用。locktime 被设置为区块高度 [198,370](/explorer/198370)，但它实际上在提前 11 个区块的 [198,359](/explorer/198359) 中就被打包挖出了。
* [938b171fdeabc7b99d1720c1df070ba373d892cd5aec3d6dda641ce67ed37ca2](/explorer/tx/938b171fdeabc7b99d1720c1df070ba373d892cd5aec3d6dda641ce67ed37ca2)
  * Locktime: `1409599601`
  * 该交易为特定 Unix 时间设置了 locktime，但因为唯一的 input 的 sequence 值为 0xffffffff，locktime 功能再次未启用。locktime 被设置为 1409599601（*2014 年 9 月 1 日，19:26:41*），但它实际上提前在区块 [287,080](/explorer/287080)（时间戳为 1393005249，即 *2014 年 2 月 21 日，17:54:09*）中就被打包挖出了。

### 原始交易 (Raw Transaction)

locktime 字段始终是交易的**最后 4 个字节**：

```
020000000001019a40d4b676ad05adea5a0aa1d093a5c16f298c4b7e31d70fd157e262e86d08900100000000feffffff0228e227000000000017a914ae72b0ccd1a65ec89a7be021e47eccc60a440bb3874dcbf91600000000160014553be08a6faa63e4038b4627996af76637522c500247304402200d9f0f85b355a29f4c14b3ee16257d92fc67429b47a15c1658d8b6737425a1c7022000d0c64c2004b0c1c47968b94c9d24820d1df20c13d37a66d20f62b8feca67b00121021853828191c3e1a4fa29c685e5e1da4710dd1dc35c9b85d6bab23c0e00109f45500e0c00
```

交易：[f168381d64b32d7b03b3f0b82cadba72e815351686e3bff2b8b5ab92f65a58bf](/explorer/tx/f168381d64b32d7b03b3f0b82cadba72e815351686e3bff2b8b5ab92f65a58bf)

原始交易中的 locktime 字段使用 [小端序 (little-endian)](/docs/technical/general/little-endian.md)。因此在上述示例中，如果我们将 `500e0c00` 的字节顺序反转，我们将得到 `000c0e50`，再将其从[十六进制](/docs/technical/general/hexadecimal.md)转换为十进制，我们得到 790096。

所以这笔交易将 locktime 设置为区块高度 [790,096](/explorer/790096)（并在该区块之后的区块中被打包挖出）。

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

 任意
 2 字节
 4 字节
 8 字节
 12 字节
 16 字节
 32 字节

0 secs

## 资源

* [Is my understanding of locktime correct?](https://bitcoin.stackexchange.com/questions/40764/is-my-understanding-of-locktime-correct)
* [How is locktime enforced in the standard client?](https://bitcoin.stackexchange.com/questions/5914/how-is-locktime-enforced-in-the-standard-client)
* [nLockTime](https://github.com/search?q=repo%3Abitcoin%2Fbitcoin+nLockTime&type=code)
* [validation.cpp](https://github.com/bitcoin/bitcoin/blob/master/src/validation.cpp) (寻找 IsFinalTx 函数)