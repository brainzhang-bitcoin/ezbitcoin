<img src="../../images/icons_loader-2.svg" alt="Loading Tool" style="height:32px; width:32px;" />

[<img src="../../images/diagrams_png_mining-block-reward.png" alt="Diagram showing the height of a block in the blockchain as its distance from the genesis block." width="490" height="400" />](https://static.learnmeabitcoin.com/diagrams/png/mining-block-reward.png)

最新区块奖励：

高度: [913,801](/explorer/913801#blockchain)

[3.1308941](/explorer/tx/7d78089b332d721ee9e960c61959c49cad3896cc2b6141846014fb9e5628ec66) BTC

区块补贴：    3.125 BTC

交易手续费： 0.0058941 BTC

区块奖励是矿工通过[挖矿](/docs/technical/mining.md)[区块](/docs/technical/block.md)可以收集的比特币数量。

它通过 [Coinbase](/docs/technical/mining/coinbase-transaction.md) 交易来索取，并为矿工在[区块链](/docs/technical/blockchain.md)上挖掘新区块提供**激励**。

## 来源

区块奖励来自哪里？

[<img src="../../images/diagrams_png_mining-block-reward-source.png" alt="Diagram showing the block reward being collected by a coinbase transaction and as the sum of the block subsidy and transaction fees in the block." width="691" height="302" />](https://static.learnmeabitcoin.com/diagrams/png/mining-block-reward-source.png)

区块奖励由两部分组成：

1. [区块补贴](#block-subsidy)
2. [交易手续费](#transaction-fees)

### 1. 区块补贴

当前区块补贴：

3.125 BTC

高度: [913,801](/explorer/913801#blockchain)

区块补贴是允许矿工在挖出区块时发送给自己的**新比特币**的固定数量。

区块补贴的大小基于区块的[高度](/docs/technical/blockchain/height.md)。

有关过去、当前和未来区块补贴的完整表格，请参阅[减半](#halving)部分。

### 2. 交易手续费

最新交易手续费：

0.0058941 BTC

高度: [913,801](/explorer/913801#blockchain)

区块奖励还包括区块中包含的交易的所有**手续费**。

[交易手续费](/docs/technical/transaction/fee.md)是在交易中没有被“消耗掉”的比特币数量，矿工也可以将这些“剩余”的比特币作为区块奖励的一部分来索取。

矿工用来自[内存池](/docs/technical/mining/memory-pool.md)的包含最高手续费的交易来填充他们的[候选区块](/docs/technical/mining/candidate-block.md)，以最大化他们可以从区块奖励中索取的比特币数量。因此，在交易中设置高额手续费可以作为激励矿工将您的交易包含在他们的下一个区块中。

> 奖励也可以通过交易手续费来资助。如果交易的输出值小于其输入值，则差额就是交易手续费，该手续费会被添加到包含该交易的区块的奖励价值中。

中本聪，[比特币白皮书](/bitcoin.pdf)

当没有区块补贴剩余时，区块奖励将完全由[交易手续费](/docs/technical/transaction/fee.md)组成。

## 目的

区块奖励的目的是什么？

区块奖励有两个目的：

### 1. 激励

[<img src="../../images/diagrams_png_mining-block-reward-incentive.png" alt="Diagram showing a miner collecting the block reward as compensation for the cost of mining a block on to the blockchain." width="431" height="522" />](https://static.learnmeabitcoin.com/diagrams/png/mining-block-reward-incentive.png)

如前所述，区块奖励为**矿工向[区块链](/docs/technical/blockchain.md)添加新区块提供了激励**。

在区块链上尝试挖掘新区块需要消耗*能量*，因此区块奖励补偿了矿工在[挖矿](/docs/technical/mining.md)过程中使用的计算能力。

如果区块奖励足够可观，它会鼓励*更多*矿工加入网络来帮助构建区块链，从而使区块链更加安全（因为单个矿工企图重写区块链需要消耗更多能量）。

#### 51% 攻击

区块奖励还有助于防止[51% 攻击](/docs/technical/blockchain/51-attack.md)。

如果矿工能够获得大部分挖矿算力，他们就有能力重写区块链，从而使他们能够逆转交易并从他们之前的交易中“偷回”比特币。

然而，由于区块奖励的存在，我们可以假设，继续挖掘区块并索取区块奖励，比通过逆转交易来企图窃取比特币更有利可图。

因此，区块奖励并不能*阻止*矿工进行 51% 攻击，但它确实会阻碍他们破坏系统完整性，从而促使他们仅去索取区块奖励。

### 2. 分发

[<img src="../../images/diagrams_png_mining-block-reward-distribution.png" alt="Diagram showing an interval of 10 minutes between new block rewards being issued, and the block rewards as the source of bitcoins in new transactions." width="575" height="627" />](https://static.learnmeabitcoin.com/diagrams/png/mining-block-reward-distribution.png)

区块奖励（确切地说是*区块补贴*）用于**向网络中分发新的比特币**。

比特币是一种去中心化货币，这意味着没有中央“银行”来控制进入网络的新比特币数量，或它们被发送给谁。因此，新比特币通过挖矿过程进入网络，这意味着新比特币以*定期的时间间隔*发行，并且*任何矿工*都有机会索取它们。

> [区块补贴]提供了一种最初将代币分发到流通中的方法，因为没有中央机构来发行它们。

中本聪，[比特币白皮书](/bitcoin.pdf)

## 减半

什么是“减半”？

区块补贴从 **50 BTC** 开始，并且**每 210,000 个区块减半一次**（大约每 4 年）。

这创造了比特币的*固定供应量*，新币的发行随着时间的推移而减少，直到达到零。

### 表格

此表格显示了以前和未来的比特币减半日期和数量。当前的区块补贴已突出显示。

当前高度：956,479

| 减半 | 高度 | 补贴 (BTC) | 日期 | 已挖出总量 (BTC) |
| --- | --- | --- | --- | --- |
| 0 | [0](/explorer/0#blockchain) | 50.00000000 | 2009年1月3日, 18:15:05 | 0.00000000 |
| 1 | [210,000](/explorer/210000#blockchain) | 25.00000000 | 2012年11月28日, 15:24:38 | 10,500,000.00000000 |
| 2 | [420,000](/explorer/420000#blockchain) | 12.50000000 | 2016年7月9日, 16:46:13 | 15,750,000.00000000 |
| 3 | [630,000](/explorer/630000#blockchain) | 6.25000000 | 2020年5月11日, 19:23:43 | 18,375,000.00000000 |
| 4 | [840,000](/explorer/840000#blockchain) | 3.12500000 | 2024年4月20日, 00:09:27 | 19,687,500.00000000 |
| 5 | 1,050,000 | 1.56250000 | 2028年4月12日 (预估) | 20,343,750.00000000 |
| 6 | 1,260,000 | 0.78125000 | 2032年4月10日 (预估) | 20,671,875.00000000 |
| 7 | 1,470,000 | 0.39062500 | 2036年4月7日 (预估) | 20,835,937.50000000 |
| 8 | 1,680,000 | 0.19531250 | 2040年4月4日 (预估) | 20,917,968.75000000 |
| 9 | 1,890,000 | 0.09765625 | 2044年4月2日 (预估) | 20,958,984.37500000 |
| 10 | 2,100,000 | 0.04882812 | 2048年3月30日 (预估) | 20,979,492.18750000 |
| 11 | 2,310,000 | 0.02441406 | 2052年3月27日 (预估) | 20,989,746.09270000 |
| 12 | 2,520,000 | 0.01220703 | 2056年3月25日 (预估) | 20,994,873.04530000 |
| 13 | 2,730,000 | 0.00610351 | 2060年3月22日 (预估) | 20,997,436.52160000 |
| 14 | 2,940,000 | 0.00305175 | 2064年3月19日 (预估) | 20,998,718.25870000 |
| 15 | 3,150,000 | 0.00152587 | 2068年3月17日 (预估) | 20,999,359.12620000 |
| 16 | 3,360,000 | 0.00076293 | 2072年3月14日 (预估) | 20,999,679.55890000 |
| 17 | 3,570,000 | 0.00038146 | 2076年3月11日 (预估) | 20,999,839.77420000 |
| 18 | 3,780,000 | 0.00019073 | 2080年3月9日 (预估) | 20,999,919.88080000 |
| 19 | 3,990,000 | 0.00009536 | 2084年3月6日 (预估) | 20,999,959.93410000 |
| 20 | 4,200,000 | 0.00004768 | 2088年3月3日 (预估) | 20,999,979.95970000 |
| 21 | 4,410,000 | 0.00002384 | 2092年3月1日 (预估) | 20,999,989.97250000 |
| 22 | 4,620,000 | 0.00001192 | 2096年2月27日 (预估) | 20,999,994.97890000 |
| 23 | 4,830,000 | 0.00000596 | 2100年2月24日 (预估) | 20,999,997.48210000 |
| 24 | 5,040,000 | 0.00000298 | 2104年2月23日 (预估) | 20,999,998.73370000 |
| 25 | 5,250,000 | 0.00000149 | 2108年2月20日 (预估) | 20,999,999.35950000 |
| 26 | 5,460,000 | 0.00000074 | 2112年2月17日 (预估) | 20,999,999.67240000 |
| 27 | 5,670,000 | 0.00000037 | 2116年2月15日 (预估) | 20,999,999.82780000 |
| 28 | 5,880,000 | 0.00000018 | 2120年2月12日 (预估) | 20,999,999.90550000 |
| 29 | 6,090,000 | 0.00000009 | 2124年2月9日 (预估) | 20,999,999.94330000 |
| 30 | 6,300,000 | 0.00000004 | 2128年2月7日 (预估) | 20,999,999.96220000 |
| 31 | 6,510,000 | 0.00000002 | 2132年2月4日 (预估) | 20,999,999.97060000 |
| 32 | 6,720,000 | 0.00000001 | 2136年2月1日 (预估) | 20,999,999.97480000 |
| 33 | 6,930,000 | 0.00000000 | 2140年1月30日 (预估) | 20,999,999.97690000 |

总供应量：20,999,999.9769 BTC

### 代码

这里有一些用于根据区块高度计算区块补贴的简单 Ruby 代码。

```
# function for calculating the subsidy for a given height (in satoshis)
def subsidy(height) 
  # calculate how many halvings there have been based on the height
  halvings = height / 210000 # halving is every 210,000 blocks

  # set the starting block subsidy
  subsidy_initial = 5000000000 # 50 BTC in satoshis

  # calculate the current block subsidy based on the height
  subsidy_current = subsidy_initial >> halvings # bit shift right for every halving
  # TIP: A right bit shift is a quick and easy way to divide by 2 (rounded down)

  return subsidy_current
end

# get block subsidy for a specific height
puts subsidy(300000) #=> 250000000 sats
```

实际的减半代码可以在 [validation.cpp](https://github.com/bitcoin/bitcoin/blob/master/src/validation.cpp) 中找到（搜索 `GetBlockSubsidy`）

#### 位移

减半实际上是一个**右[位移](https://www.interviewcake.com/concept/java/bit-shift)。**

这与*除以 2* 几乎完全相同，只是如果起始数是奇数，除法的结果会*向下取整*。

你可以通过在下面的进制转换器工具的 *decimal* 字段中输入 5000000000（以聪为单位的初始区块补贴），然后从 *binary* 字段中删除最右边的位（这相当于执行右位移）来理解我的意思：

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

因此，与其称其为“比特币减半”，不如亲切地将其称为“[右位移](https://www.reddit.com/r/Bitcoin/comments/173ljh7/the_halving_aka_the_bitshift_righting/)”。

## 示例

以下是区块链中以前区块的区块奖励的一些示例：

* 高度: [100](/explorer/100#blockchain)
* 区块奖励: [50 BTC](/explorer/tx/2d05f0c9c3e1c226e63b5fac240137687544cf631cd616fd34fd188fc9020866)
  + 区块补贴: 50 BTC
  + 交易手续费: 0 BTC
* 这是最早的区块之一。它索取了最大的 50 BTC 区块补贴，但区块中没有包含任何交易（除了 Coinbase 交易），因此无法在区块补贴之外索取交易手续费。

* 高度: [2,817](/explorer/2817#blockchain)
* 区块奖励: [52.01 BTC](/explorer/tx/e958faf790304fc4185b377552e93fddae3a513c255f8bb09526b5886ab83936)
  + 区块补贴: 50 BTC
  + 交易手续费: 2.01 BTC
* 这是**第一个将交易手续费收集为区块奖励一部分的区块**。此区块中的交易完全没有必要支付手续费，但它依然是矿工连同区块补贴一起收集手续费的第一个例子。

* 高度: [100,000](/explorer/100000#blockchain)
* 区块奖励: [50 BTC](/explorer/tx/8c14f0db3df150123e6f3dbbf30f8b955a8249b62ac1d1ff16284aefa3d06d87)
  + 区块补贴: 50 BTC
  + 交易手续费: 0 BTC
* 该区块包含 3 笔交易（不包括 Coinbase 交易）。然而，当时打包进区块的竞争并不激烈，因此交易不需要包含手续费就能被开采。

* 高度: [124,724](/explorer/124724#blockchain)
* 区块奖励: [49.99999999 BTC](/explorer/tx/5d80a29be1609db91658b401f85921a86ab4755969729b65257651bb9fd2c10d)
  + 区块补贴: 50 BTC
  + 交易手续费: 0.01 BTC
* 这是一个**矿工未索取全部区块奖励**的例子。这个特定的区块没有索取最大可用的 50 BTC 补贴，也没有索取同样可用的 0.01 BTC 交易手续费。

  所以，矿工在他们的 Coinbase 交易中*不*索取全部区块奖励是完全有效的，尽管这通常是由于矿工的失误造成的。

* 高度: [210,000](/explorer/210000#blockchain)
* 区块奖励: [38.56295554 BTC](/explorer/tx/76a30f7eefb41cd01733b23218faea8a1a1a2f6bbf1a2c11e4bc77f62c8e7ce9)
  + 区块补贴: 25 BTC
  + 交易手续费: 13.56295554 BTC
* 这是**第一次减半**的区块。区块补贴从 50 BTC 减半至 25 BTC。

* 高度: [788,695](/explorer/788695#blockchain)
* 区块奖励: [12.95074657 BTC](/explorer/tx/8174154423ceb97ead7356b8fd2109795edda6444a0e76f13526d2ad9f895e37)
  + 区块补贴: 6.25 BTC
  + 交易手续费: 6.70074657 BTC
* 这是第一个**交易手续费大小大于区块补贴**的区块。

## 花费

你什么时候可以花费区块奖励？

只有当区块在区块链中的深度达到 **100 个区块以上**时，矿工才能花费区块奖励。

参见 [Coinbase 成熟度](/docs/technical/mining/coinbase-transaction.md#coinbase-maturity)。

## 备注

* **矿工并不*必须*索取区块奖励。** 虽然没有理由不索取，但没有什么能阻止矿工在他们不想索取时放弃索取全部区块奖励。在这种情况下，这些比特币将永远丢失，因为无法在未来的交易中花费这些比特币。例如，区块 [501,726](/explorer/block/0000000000000000004b27f9ee7ba33d6f048f684aaeb0eea4befd80f1701126) 的区块奖励是 12.5 BTC，但矿工在[该区块的 Coinbase 交易中](/explorer/tx/9bf8853b3a823bbfa1e54017ae11a9e1f4d08a854dcce9f24e08114f2c921182)没有向自己发送任何比特币，因此这些比特币永远丢失了。这很可能是一个错误。
* **“区块补贴”经常被误称为“区块奖励”。** 将新发行的比特币称为“区块奖励”很常见，但从技术上讲，区块奖励由“区块补贴”（新发行的比特币）+“交易手续费”组成。如果你弄错了，我想也不会给你带来任何问题，但我只是想提一下，因为我过去也犯过这个错误。
* **白皮书中没有使用“区块奖励”这个词。** 中本聪只将挖矿奖励称为一种“激励”，直到[一年多以后在 bitcointalk 论坛上](https://satoshi.nakamotoinstitute.org/posts/bitcointalk/441/)才使用“区块奖励”一词。这只是给你在下一次酒吧问答时准备的一个趣闻。
* **比特币的总供应量为 20,999,999.9769 BTC。** 所以从技术上讲，它少于你一直听到的“2100万上限”。这部分是由于减半是右位移，这意味着如果之前的区块补贴是奇数，区块补贴会被向下取整。同样，这是另一个在酒吧问答中绝佳的问题。