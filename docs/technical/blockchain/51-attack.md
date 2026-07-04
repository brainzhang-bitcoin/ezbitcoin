<img src="../../images/icons_loader-2.svg" alt="Loading Tool" style="height:32px; width:32px;" />

[<img src="../../images/diagrams_png_blockchain-51-attack.png" alt="Diagram showing a transaction being removed from the blockchain in a 51% attack." width="484" height="393" />](../../images/diagrams_png_blockchain-51-attack.png)

当前网络算力 (Current Network Hashrate):

每秒 958,292,360,507,524,907,008 次哈希运算

查看[计算方法](#hashpower)

51% 攻击是指故意构建一个新的[最长链](longest-chain.md)以替换[区块链](../blockchain.md)中已有[区块](../block.md)的行为。这允许您**替换那些此前已写入区块链的[交易](../transaction.md)**。

当您拥有**大多数挖矿算力 (majority of the mining power)**时，这种攻击最容易实施，这就是为什么它被称为“多数攻击 (majority attack)”或“51% 攻击”。

## 攻击方法

51% 攻击是如何进行的？

节点总是将[已知的最长链](longest-chain.md)视为区块链的*有效*版本。因此，如果您想在区块链中“撤销”一笔交易，您只需要**构建一个新的、更长的区块链接**，而在该链接中*不包含*那笔交易。

[<img src="../../images/diagrams_png_blockchain-51-attack-example-build-longest-chain.png" alt="Diagram showing a 51 attack to replace a transaction in a previous longest chain." width="544" height="370" />](../../images/diagrams_png_blockchain-51-attack-example-build-longest-chain.png)

假设我们用比特币买了一辆车并把它开走了。

当节点收到这个新的*更长*的区块链接时，它们会执行一次[区块重组](chain-reorganization.md)以*停用*其旧最长链中的区块，并*激活*您构建的新最长链中的区块。

[<img src="../../images/diagrams_png_blockchain-51-attack-example-chain-reorganization.png" alt="Diagram showing a 51 attack to replace a transaction in a previous longest chain." width="554" height="370" />](../../images/diagrams_png_blockchain-51-attack-example-chain-reorganization.png)

旧最长链中的交易现在失效了。这就好像购买这辆车的付款从未发生过一样。

因此，通过构建一个新的最长链来替换已有的最长链，您实际上是在**重写区块链**，并创建了一个[网络](../networking.md)上的所有节点都将采用的新交易历史。结果，您逆转了我们此前认为已永久成为区块链一部分的交易。

但成功实施 51% 攻击并不容易。

您会希望在新链中包含一笔*替代*交易，将比特币发送到*新的*目的地（例如，发送到您的[地址](../keys/address.md)而不是汽车经销商的地址）。否则，原始交易可能会在新链中被重新开采。

## 防范

如何防范 51% 攻击？

每个矿工都有动力在当前最长的区块链接之上继续构建。因此，如果网络上所有其他矿工的合并挖矿算力大于您的算力，那么要**超越其他矿工的工作量**去构建一条更长的链并替换已有链就会变得**极其困难**。

[<img src="../../images/diagrams_png_blockchain-51-attack-prevention-combined-mining.png" alt="Diagram showing miners working together to extend the current longest chain." width="733" height="654" />](../../images/diagrams_png_blockchain-51-attack-prevention-combined-mining.png)

矿工们协同工作，可以比您独自一人更快地构建起区块链。

但当然，如果您确实能获得比所有其他矿工合并起来*更多*的挖矿算力，那么您就有能力赶超当前的最长链，并构建一条新的最长链供所有人采用。

[<img src="../../images/diagrams_png_blockchain-51-attack-prevention-majority-power.png" alt="Diagram showing how you can build a longer chain faster than all other miners combined if you have the majority of the hashing power." width="730" height="707" />](../../images/diagrams_png_blockchain-51-attack-prevention-majority-power.png)

如果您拥有大多数的挖矿算力，那么构建出一条更长的链只是时间问题。

因此，为了防范这种情况的发生，我们希望使单个矿工难以获得大多数的挖矿算力。这是通过**允许世界上任何人参与挖矿**，并提供**[区块奖励](../mining/block-reward.md)作为动力**在已知最长链上继续构建来实现的。

[<img src="../../images/diagrams_png_blockchain-51-attack-prevention-incentive.png" alt="Diagram showing the block reward as an incentive for miners to extend the longest chain." width="733" height="907" />](../../images/diagrams_png_blockchain-51-attack-prevention-incentive.png)

区块奖励只有在最长链中达到 100 个区块深之后才能被消费。

结果，矿工们将精力集中在构建同一条链上，从而使任何个人试图重写区块链中区块的行为变得困难（或至少非常昂贵）。

<blockquote>
只要大多数的 CPU 算力被不协同向网络发起攻击的节点所控制，它们就会生成最长链并超越攻击者。
</blockquote>

中本聪, [比特币白皮书](/bitcoin.pdf)

## 可行性

实施 51% 攻击有多困难？

实施 51% 攻击最棘手的部分首先在于获得执行攻击所需的所有硬件，因为这将是极其昂贵的。

然而，如果您*确实*设法获得了大多数的挖矿算力，那么构建出一条新的最长链**仅仅是时间问题**。

话虽如此，要替换较大数量的区块比只替换几个区块需要做更多的工作。因此，交易在区块链中沉淀得越深，逆转它所需要花费的时间和能量就越多。

[<img src="../../images/diagrams_png_blockchain-51-attack-depth-work.png" alt="Diagram showing how it's harder to replace blocks the further they are down the blockchain." width="367" height="450" />](../../images/diagrams_png_blockchain-51-attack-depth-work.png)

交易在区块链中陷得越深，就越难以被替换。

但同样，这是假设您可以获得硬件以达到 51% 或更多的挖矿算力来超越所有其他矿工。

尽管如此，您仍然可以尝试以低于 50% 的挖矿算力执行此类攻击，但胜算会非常小……

## 概率

您能在拥有低于 50% 挖矿算力的情况下重写区块链吗？

挖矿算力

%

随机示例

0 秒

在*没有*占大多数挖矿算力的情况下重写区块链是可能的，但您需要**运气**。

挖矿是不可预测的，因此即使您只有少量的挖矿算力，也不能断定您运气不够好而无法连续开采接下来的 2 个区块。这虽然不太可能，但并非不可能。概率取决于您相对于其他人拥有多少挖矿算力。

[<img src="../../images/diagrams_png_blockchain-51-attack-rewrite-luck.png" alt="Diagram showing how you would need luck to rewrite the blockchain with a minority of the mining power." width="733" height="699" />](../../images/diagrams_png_blockchain-51-attack-rewrite-luck.png)

当然，交易在区块链中沉淀得越深，您连续开采 X 个区块所需要的运气就越多。如果在没有人拥有大多数挖矿算力的情况下，交易在区块链中沉淀得越深，替换它的难度就会呈*指数级增加*。

[<img src="../../images/diagrams_png_blockchain-51-attack-mining-power-success-chart.png" alt="Chart showing the probability of being able to replace blocks in the blockchain based on mining power." width="548" height="612" />](../../images/diagrams_png_blockchain-51-attack-mining-power-success-chart.png)

如果一个矿工拥有 40% 的挖矿算力，他们大约有 50% 的机会能替换掉在链中深达 5 个区块的交易。

因此，除非您在比特币网络中占有很大比例的算力，否则您替换掉已被开采交易的几率非常渺茫，并且随着交易进一步深入链中，这些几率会迅速减小。

以下是您确切几率的表格：

基于挖矿算力百分比替换区块链中顶部 X 个区块的概率。

| **区块数 (z)** | 50%+ 算力控制 | 40% 算力控制 | 30% 算力控制 | 20% 算力控制 | 10% 算力控制 |
|---|---|---|---|---|---|
| 1 | 100% | 73.6% | 44.6% | 20.4% | 5.1% |
| 2 | 100% | 66.4% | 32.5% | 10.3% | 1.3% |
| 3 | 100% | 60.3% | 23.9% | 5.3% | 0.4% |
| 4 | 100% | 55.0% | 17.7% | 2.7% | 0.1% |
| 5 | 100% | 50.4% | 13.2% | 1.4% | 0.02% |
| 6 | 100% | 46.2% | 9.9% | 0.7% | 0.006% |
| 7 | 100% | 42.5% | 7.4% | 0.4% | 0.001% |
| 8 | 100% | 39.1% | 5.6% | 0.2% | 0.0004% |
| 9 | 100% | 36.0% | 4.2% | 0.1% | 0.0001% |
| 10 | 100% | 33.2% | 3.1% | 0.06% | 0.00003% |

上表中的数字假定您正试图通过构建一条比当前最长链*长一个区块*的备选链来替换区块。

### 数学公式

能够重写区块链中区块的概率是**您拥有多少挖矿算力**以及**您想尝试替换多少个区块**的函数。

以下是来自[比特币白皮书](/bitcoin.pdf)（第 11 节）的公式：

[<img src="../../images/technical_blockchain_51-attack_equation-success.png" alt="The equation for attacking the blockchain from the Bitcoin whitepaper." width="523" height="264" />](../../images/technical_blockchain_51-attack_equation-success.png)

区块越深越难被替换的证明是系统完整性和安全性的重要部分。

无论如何，这就是该公式在 Ruby 代码中的实现：

```
# p = probability honest node finds the next block
# q = probability attacker finds the next block
# z = number of blocks to catch up

def attacker_success_probability(q, z)
  p = 1 - q
  lambda = z * (q / p) # expected number of occurrences in the poisson distribution
  sum = 1.0

  for k in 0..z
    poisson = Math.exp(-lambda) # exp() raises e (natural logarithm) to a number
    for i in 1..k
      poisson *= lambda / i
      puts poisson
    end

    sum -= poisson * (1 - (q/p)**(z-k) )
  end

  return sum
end

# Example
puts attacker_success_probability(0.4, 5) #=> 0.5506251290702077
```

上述公式计算了（在落后指定数量的区块时）*追赶上*最长链的概率。如果您想*替换*链中的区块，您需要比其*多出一个区块*。

### 图表

[<img src="../../images/technical_blockchain_51-attack_success_chart_50_blocks.png" alt="Chart showing the probability of success for replacing blocks in the blockchain." width="800" height="600" />](../../images/technical_blockchain_51-attack_success_chart_50_blocks.png)

交易在区块链中埋得越深，被替换的成功概率就呈指数级衰减。

## 常见问题

### 是否有人曾对比特币成功发起过 51% 攻击？

没有，从来没有过。

在比特币的历史上，一些矿池曾接近达到总算力的 50% 或更多，但实际上没有人发起过成功的 51% 攻击。

[<img src="../../images/technical_blockchain_51-attack_mining-distribution-ghash-2014.jpg" alt="Chart showing Ghash.io having close to 50% of the mining power in 2014." width="500" height="467" />](../../images/technical_blockchain_51-attack_mining-distribution-ghash-2014.jpg)

GHash.io 在 2014 年曾接近达到 50%。  
[github.com/in3rsha/bitcoin-mining-distribution](https://github.com/in3rsha/bitcoin-mining-distribution)

即使矿工获得了超过 50% 的算力，也不一定意味着他们真的会发起攻击；这只意味着他们*能够*这样做。无论如何，如果您拥有如此巨大的算力，继续挖矿并赚取区块奖励可能比逆转单笔交易（并因此让您的攻击导致比特币价值暴跌）更赚钱。

### 我需要多少算力才能发起 51% 攻击？

您可以使用当前的[target](../mining/target.md)值来估计获得网络控制权所需的算力大小。

目标值根据网络上所有矿工开采新区块的速度而上下浮动。因此，我们可以利用它来计算我们需要以多快的速度进行哈希，从而超越网络当前的速度。

#### 1. 查找当前目标值

首先，我们可以通过查看最近挖掘出的区块的区块头中的“[bits](../block/bits.md)”字段来获取当前的目标。

```
$ bitcoin-cli getblockcount
956479

$ bitcoin-cli getblockhash 956479
000000000000000000005af9d7cca01756b552b02e5f5fac6422864439807264

$ bitcoin-cli getblockheader 000000000000000000005af9d7cca01756b552b02e5f5fac6422864439807264 | grep bits
"bits": "17021a42",
```

这里，“bits”值就是压缩格式的目标值。因此，将 bits 转换为 target 我们得到：

```
0x000000000000000000021a420000000000000000000000000000000000000000
```

<img src="../../images/icons_tool.svg" alt="Tool Icon" style="width:20px; height:20px" /> 目标 Bits (Target Bits)

当前

随机示例

高度:

目标

0x

`0 bytes`

Bits`0 bytes`



0 秒

这就是所有矿工需要将[区块哈希](../block/hash.md)降至其下才能成功挖出区块的数字。

#### 2. 计算挖掘下一个区块所需的平均哈希次数

我们可以通过将所有可能哈希结果的范围除以目标值，来算出我们平均需要执行多少次哈希才能使结果低于该目标：

```
hashes = (2**256) / 0x000000000000000000021a420000000000000000000000000000000000000000
hashes = 574975416304515007119360
```

这告诉我们，我们平均需要进行 `574975416304515007119360` 次哈希运算才能挖掘出下一个区块。

或者说，这大约是网络上所有矿工**每 10 分钟**执行的哈希总次数。

请参阅[累积工作量计算说明](longest-chain.md#calculation)了解我们如何获得这一“预期哈希次数”的更多信息。

#### 3. 转换为每秒哈希数

无论如何，使用这个数字我们可以算出网络的每秒哈希次数（算力）：

```
hashes per second = 574975416304515007119360 / 600 # 10分钟有600秒
hashes per second = 958292360507524907008
```

因此，当前比特币网络上所有矿工的合并算力为每秒 `958292360507524907008` 次哈希。

将其转换为 **TH/s** (每秒万亿次哈希) 我们得到：

```
terahashes per second = 958292360507524907008 / 10**12
terahashes per second = 958292360
```

因此，要获得 50% 的区块挖矿控制权，我们需要建立一个能够运行超过 `958,292,360` TH/s 的矿场。

## 资源

* [Hashrate Distribution Chart](https://mainnet.observer/charts/mining-pools-hashrate-distribution/) — 很有用的饼图，展示了比特币的算力分布。
* [Coin Dance - Latest Blocks](https://coin.dance/blocks/today) – 另一个提供当前比特币挖矿分布饼图的网站。分布越分散越好。