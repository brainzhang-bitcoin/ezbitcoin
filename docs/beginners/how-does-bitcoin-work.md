<img src="../images/icons_loader-2.svg" alt="Loading Tool" style="height:32px; width:32px;" />

比特币是一个**电子支付系统**，它允许任何人创建账户并向世界上任何地方的任何人发送任意金额的资金。

你可能想把这句话再读一遍。

它是作为当前金融系统的替代方案而创建的。在当前的系统中，由少数几家大型银行控制谁可以创建账户以及你可以进行什么交易。这集中了对货币的控制，我们别无选择，只能信任这些银行会公平、负责任地行事。

> 必须信任银行能够保管我们的钱并以电子方式进行转账，但它们却在信用泡沫的浪潮中将这些钱贷出去，而准备金却只占很小一部分。

中本聪 (Satoshi Nakamoto), 
[satoshi.nakamotoinstitute.org](https://satoshi.nakamotoinstitute.org/posts/p2pfoundation/1/)

比特币是为了应对因当前系统集权化而导致的 [2007-2008年金融危机](https://en.wikipedia.org/wiki/2007%E2%80%932008_financial_crisis) 而开发出来的。它由中本聪匿名设计，并于 [2009年1月发布](https://www.metzdowd.com/pipermail/cryptography/2009-January/014994.html)，是一个*没有*中央控制点的支付系统。

它也是[开源软件](https://github.com/bitcoin/bitcoin/)，这意味着任何人都可以运行该程序并与该系统进行交互。

以下是对其工作原理的简单解释。

## 什么是比特币？

比特币只是一个**计算机程序**。你可以[下载](https://bitcoin.org/en/download)它并在你的计算机上运行它。

[<img src="../images/beginners_how-does-bitcoin-work_1_1_program.png" alt="展示在计算机上下载比特币程序的插图。" width="800" height="168" />](../images/beginners_how-does-bitcoin-work_1_1_program.png)

当你第一次运行该程序时，它将连接到运行相同程序的其他计算机，并且它们将*开始与你共享一个文件*。这个文件被称为[**区块链**](../technical/blockchain.md)，它是一个包含[*交易*](../technical/transaction.md)的巨大列表。

[<img src="../images/beginners_how-does-bitcoin-work_1_2_network.png" alt="展示共享交易文件（区块链）的计算机网络的图表。" width="800" height="396" />](../images/beginners_how-does-bitcoin-work_1_2_network.png)

当一笔新交易进入网络时，它会在计算机之间*转发*，直到每个人都拥有该交易的副本。大约每隔 10 分钟，网络上的一个随机计算机（[节点](../technical/networking/node.md)）会将他们收到的最新交易添加到区块链中，并与所有人共享更新。

[<img src="../images/beginners_how-does-bitcoin-work_1_3_network_transactions.png" alt="展示一笔交易在被添加到共享文件（区块链）之前在网络计算机间转发的图表。" width="800" height="428" />](../images/beginners_how-does-bitcoin-work_1_3_network_transactions.png)

因此，比特币程序创建了一个相互通信的庞大**计算机[网络](../technical/networking.md)**，用于**共享一个文件并用新交易来更新它**。

## 比特币解决了什么问题？

比特币解决了在**没有中央控制点的情况下运行支付系统**的问题。

在比特币出现之前，在计算机网络中转发交易是可行的。然而，问题是**你可以在计算机网络中插入相互冲突的交易**。例如，你可以创建两笔独立的交易来消费*同一枚*数字硬币，并同时将这两笔交易发送到网络中。

这被称为“**双重支付**”（双花）：

[<img src="../images/beginners_how-does-bitcoin-work_2_1_why_double_spend.png" alt="展示两笔冲突交易被同时发送到计算机网络中的图表。" width="800" height="429" />](../images/beginners_how-does-bitcoin-work_2_1_why_double_spend.png)

有些计算机会先收到绿色交易，而有些计算机会先收到红色交易。

现在，如果你要在没有中央权威机构的情况下创建一个电子支付系统，你就会面临搞清楚这些交易中哪一个“先”发生的问题，而当计算机网络独立运行时，这是很难确定的。

那么，谁来*决定*哪笔交易“先”发生并应该是唯一写入文件的交易呢？

比特币解决这个问题的方法是：强制节点在将收到的交易写入文件之前，先保存在*内[存池](../technical/mining/memory-pool.md)*中。然后，大约每隔 10 分钟，网络上的一个*随机节点*会将他们内存中的交易添加到该文件中。

[<img src="../images/beginners_how-does-bitcoin-work_2_2_why_mining.png" alt="展示网络上的单个节点将他们内存中的交易添加到共享文件中的图表。" width="800" height="429" />](../images/beginners_how-does-bitcoin-work_2_2_why_mining.png)

然后，这个更新后的文件会与网络的其余部分共享。节点将接受更新文件中的交易为“正确”的交易，并从他们的内存中删除任何冲突的交易。

结果是，任何双重支付交易都不会被写入文件，并且所有节点都会定期更新到共享文件的相同版本。

[<img src="../images/beginners_how-does-bitcoin-work_2_3_why_solved.png" alt="展示网络节点接受更新后的文件版本并从内存中删除冲突交易的图表。" width="800" height="429" />](../images/beginners_how-does-bitcoin-work_2_3_why_solved.png)

这种向文件添加交易的过程被称为[**挖矿**](../technical/mining.md)，这是一场无法被网络上单个节点控制的全网*竞争*。

## 挖矿是如何工作的？

挖矿是将新的交易区块添加到区块链的过程。

首先，每个节点都会将他们收到的最新[交易](../technical/transaction.md)保存在[**内存池**](../technical/mining/memory-pool.md)中，这只是他们计算机上的临时内存。

然后，任何节点都可以尝试将他们内存池中的交易*开采*到共享文件（[**区块链**](../technical/blockchain.md)）中。

为此，节点会将内存池中的交易收集到一个名为[**区块**](../technical/block.md)的容器中，然后使用*计算能力*尝试将这个交易区块添加到区块链上。

[<img src="../images/beginners_how-does-bitcoin-work_3_1_mining.png" alt="展示网络节点将内存池中的交易收集到一个区块中并将其添加到区块链上的图表。" width="800" height="421" />](../images/beginners_how-does-bitcoin-work_3_1_mining.png)

那么，计算能力在什么地方起作用呢？要将这个区块添加到区块链，你必须将你的交易区块输入到被称为[**哈希函数**](../technical/cryptography/hash-function.md)的程序中。哈希函数基本上是一个微型的计算机程序，它会输入任意数量的数据，将其打乱，并输出一个完全唯一（且不可预测）的数字。

[<img src="../images/beginners_how-does-bitcoin-work_3_2_hash_function.png" alt="展示数据被输入到哈希函数并输出一个随机数的图表。" width="800" height="114" />](../images/beginners_how-does-bitcoin-work_3_2_hash_function.png)

为了让你的区块成功添加到区块链上，这个结果（或[**区块哈希**](../technical/block/hash.md)）必须**等于或低于****[目标**](../technical/mining/target.md)，这是网络上每个人都同意的阈值。

[<img src="../images/beginners_how-does-bitcoin-work_3_3_mining_block_hash.png" alt="展示区块哈希试图低于目标值的图表。" width="800" height="354" />](../images/beginners_how-does-bitcoin-work_3_3_mining_block_hash.png)

如果计算出的**区块哈希**没有低于目标，你可以对区块内部的数据进行微调，然后再次通过哈希函数运行。这将产生一个*完全不同*的数字，希望它能低于目标。如果还没有，就再次调整区块并重试。

[<img src="../images/beginners_how-does-bitcoin-work_3_4_mining_nonce.png" alt="展示矿工调整区块中的数据以产生不同的区块哈希的图表。" width="800" height="375" />](../images/beginners_how-does-bitcoin-work_3_4_mining_nonce.png)

最终，网络上的某个节点（或矿工）会找到一个低于目标的区块哈希，这个交易区块就会被添加到区块链中。

然后，挖矿过程重新开始，以向链中添加下一个区块。

总之，挖矿过程利用计算能力尽可能快地进行哈希计算，以尝试成为网络上第一个获得低于目标的区块哈希的计算机。如果成功，你就可以将你的交易区块添加到区块链上，并与网络上的其他人共享。

哈希函数与目标值的结合使用，创造了一场任何人都可以参与的全网竞争。这也意味着网络上没有哪一台单独的计算机能够完全控制向区块链添加交易，从而创建了一个没有中央控制点的文件共享网络。

**虽然任何人仍然可以尝试去挖矿，但在家用计算机上进行挖矿已经不再具有竞争力。** 现在的矿工使用专为尽可能快（且高效）地进行哈希计算而设计的专业硬件，这意味着挖矿现在主要由那些拥有专业硬件和廉价电力的人来完成。

### 比特币从哪里来？

作为使用计算能力来尝试添加新交易区块到区块链的激励，每个新区块都会产生固定数量的、以前不存在的比特币。因此，如果你能够成功开采一个区块，你就可以将这些新比特币“发送”给自己，作为你付出努力的奖励。

[<img src="../images/beginners_how-does-bitcoin-work_3_5_mining_block_reward.png" alt="展示在区块链上开采新区块的区块奖励的图表。" width="800" height="354" />](../images/beginners_how-does-bitcoin-work_3_5_mining_block_reward.png)

这一批新比特币被称为**[区块奖励](../technical/mining/block-reward.md)**，这也是该过程被称为“挖矿”的原因。

## 为什么这个文件被称为“区块链”？

交易并不是单独添加到文件中的——它们被收集在一起并以区块形式添加。每个新区块都*构建在*现有区块之上，因此该文件由一*链* **区块**组成；因此得名[**区块链**](../technical/blockchain.md)。

[<img src="../images/beginners_how-does-bitcoin-work_4_1_blockchain.png" alt="展示一个指定前一个区块以在此基础上构建的区块的图表。" width="800" height="232" />](../images/beginners_how-does-bitcoin-work_4_1_blockchain.png)

此外，网络上的每个节点**都将始终采用他们收到的[最长链](../technical/blockchain/longest-chain.md)的区块**作为区块链的“官方”版本。

这意味着矿工将始终尝试在已知最长区块链的“尖端”上进行构建，因为不属于最长链的任何交易都将是无效的。

[<img src="../images/beginners_how-does-bitcoin-work_4_2_blockchain_longest.png" alt="展示节点采用最长区块链作为其区块链，且不在最长链中的交易均无效的图表。" width="800" height="328" />](../images/beginners_how-does-bitcoin-work_4_2_blockchain_longest.png)

因此，如果有人想要重写交易历史，他们就需要重建一条更长的区块链，以创造一条供其他节点采用的新的最长链。然而，要实现这一点，单个矿工需要拥有比网络其他部分总和还要多的计算机处理能力。

[<img src="../images/beginners_how-does-bitcoin-work_4_3_blockchain_hashpower.png" alt="展示攻击者企图比网络其余部分总和更快地构建一条更长区块链的图表。" width="800" height="400" />](../images/beginners_how-does-bitcoin-work_4_3_blockchain_hashpower.png)

因此，整个网络的共同努力使得任何个人都很难“超越”网络并重写区块链。

换句话说，整个交易历史（以及你的资金）都受到挖矿所凝聚的能量的保护。

## 交易是如何工作的？

你可以将区块链看作是*保险箱*的保管设施，我们称之为[**输出**](../technical/transaction/output.md)。这些输出只是装有不同数量比特币的容器。

[<img src="../images/beginners_how-does-bitcoin-work_5_1_outputs.png" alt="展示区块链存储了许多独立输出的图表。" width="800" height="324" />](../images/beginners_how-does-bitcoin-work_5_1_outputs.png)

当你进行比特币[**交易**](../technical/transaction.md)时，你选择一些输出并*解锁*它们，然后创建新的输出并在它们上面加上新的[锁](../technical/transaction/output/scriptpubkey.md)。

[<img src="../images/beginners_how-does-bitcoin-work_5_2_transaction.png" alt="展示一笔交易选择区块链中的输出并从中创建新输出的图表。" width="800" height="299" />](../images/beginners_how-does-bitcoin-work_5_2_transaction.png)

因此，当你向某人“发送”比特币时，你实际上是将一定数量的比特币放入一个新的保险箱中，并给它上锁，只有你“发送”比特币对象的那个人才能解锁。

例如，如果我想给你发一些比特币，我会从区块链中选择一些我可以解锁的输出，并用它们创建一个只有*你*能解锁的新输出。此外，如果我不想把我解锁的所有比特币都发给你，我会创建一个额外的输出作为我的“找零”并将其锁给自己。

[<img src="../images/beginners_how-does-bitcoin-work_5_3_transaction_change.png" alt="展示一笔交易创建额外输出作为找零的图表。" width="800" height="299" />](../images/beginners_how-does-bitcoin-work_5_3_transaction_change.png)

以此类推，如果你想把你的比特币发给别人，你会重复选择现有输出（你可以解锁的输出）并从中创建新输出的过程。结果，比特币交易形成了一个类似图的结构，其中比特币的移动是由一系列交易连接起来的。

[<img src="../images/beginners_how-does-bitcoin-work_5_4_transaction_graph.png" alt="展示一系列交易解锁前一笔交易的输出并从中创建新输出的图表。" width="800" height="307" />](../images/beginners_how-does-bitcoin-work_5_4_transaction_graph.png)

最后，当一笔交易被开采到区块链上时，在交易中用完（花掉）的输出就不能在另一笔交易中使用了，而新创建的输出将可以在未来的交易中被花掉。

[<img src="../images/beginners_how-does-bitcoin-work_5_5_transaction_blockchain_outputs.png" alt="展示交易在区块链内部花费并创建输出的图表。" width="800" height="455" />](../images/beginners_how-does-bitcoin-work_5_5_transaction_blockchain_outputs.png)

## 你如何拥有比特币？

为了能够“接收”比特币，你需要有自己的一套[密钥](../technical/keys.md)。

这套密钥就像是你的*账号*和*密码*，只是在比特币中它们被称为你的[公钥](../technical/keys/public-key.md)和[私钥](../technical/keys/private-key.md)。

例如，如果我想给你发送一些比特币，你首先需要给我你的公钥。当我创建交易时，我会将你的公钥放入输出（保险箱）的锁*内部*。当你想要将这些比特币发送给其他人时，你会使用你的私钥来解锁这个输出。

[<img src="../images/beginners_how-does-bitcoin-work_6_1_keys.png" alt="展示公钥和私钥对被用于锁定和解锁交易中输出的图表。" width="800" height="362" />](../images/beginners_how-does-bitcoin-work_6_1_keys.png)

那么，你在哪里可以获得公钥和私钥呢？借助[密码学](../technical/cryptography.md)，你实际上可以**自己生成它们**。

简而言之，你的私钥只是一个很大的*随机数*，而你的公钥是通过这个私钥*计算*出来的数字。但聪明的地方在于：你可以把你的公钥给别人，但他们无法通过公钥反向推导计算出私钥。

[<img src="../images/beginners_how-does-bitcoin-work_6_2_keys_generate.png" alt="展示私钥和公钥示例的图表，公钥是由私钥计算出来的。" width="800" height="236" />](../images/beginners_how-does-bitcoin-work_6_2_keys_generate.png)

现在，当你想要解锁分配给你的公钥的比特币时，你可以使用你的私钥来创建所谓的[数字签名](../technical/keys/signature.md)。这个签名证明了你是该公钥的拥有者（因此可以解锁比特币），*而无需透露你的私钥*。该签名也仅对创建它的那笔交易有效，因此它不能被用于解锁锁定在相同公钥下的其他比特币。

[<img src="../images/beginners_how-does-bitcoin-work_6_3_keys_digital_signature.png" alt="展示私钥被用来创建数字签名，然后用于解锁交易中输出的图表。" width="800" height="375" />](../images/beginners_how-does-bitcoin-work_6_3_keys_digital_signature.png)

这种系统被称为[公钥密码学](../technical/cryptography.md#public-key-cryptography)，自 1978 年起就已投入使用（参见 [RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem))）。比特币利用这一系统，允许任何人创建用于安全发送和接收比特币的密钥，而无需中央机构来分发账号和密码。

在比特币中，我们将公钥转换成更加用户友好的[地址](../technical/keys/address.md)，这就是你通常在发送和接收付款时会使用的东西。

## 总结

[<img src="../images/beginners_how-does-bitcoin-work_7_1_bitcoin_system.png" alt="展示比特币工作原理总结的图表。" width="800" height="851" />](../images/beginners_how-does-bitcoin-work_7_1_bitcoin_system.png)

要使用比特币，你需要生成自己的[私钥](../technical/keys/private-key.md)和[公钥](../technical/keys/public-key.md)。你的私钥是一个非常大的随机数，你的公钥是由它计算出来的。这些密钥可以轻松地在你的计算机上生成，甚至在像计算器这样简单的工具上也可以生成。然而，大多数人使用[比特币钱包](wallets.md)来帮助生成和管理他们的密钥。

要接收比特币，你需要向发送方提供你的公钥。发送方随后会创建一笔[交易](../technical/transaction.md)，在其中解锁他们拥有的比特币，并创建一个装有比特币的新的“保险箱”，然后将你的公钥放入锁中。

然后，这笔交易被发送到一个[节点](../technical/networking/node.md)，在计算机之间进行转发，直到[网络](../technical/networking.md)上的每个节点都拥有该交易的副本。从这里开始，每个节点都有机会尝试将他们收到的最新交易*开采*到[区块链](../technical/blockchain.md)中。

[挖矿](../technical/mining.md)的过程包括：节点将[内存池](../technical/mining/memory-pool.md)中的交易收集到一个[区块](../technical/block.md)中，并对该区块进行重复[哈希](../technical/cryptography/hash-function.md)计算（每次进行微调），以尝试获得低于当前[目标](../technical/mining/target.md)值的[区块哈希](../technical/block/hash.md)。

第一个找到低于目标的区块哈希的矿工会将该区块添加到他们的[区块链](../technical/blockchain.md)中，并将该区块广播给网络上的其他节点。然后，每个节点将验证该区块并将其添加到自己的区块链中（在此过程中会从他们的内存池中删除任何冲突的交易），并重新开始挖矿过程，以尝试在该链中的这一新区块之上进行构建。

最后，开采该区块的矿工会在区块内放入他们自己的[特殊交易](../technical/mining/coinbase-transaction.md)，这允许他们收集固定数量的、以前不存在的比特币。这种[区块奖励](../technical/mining/block-reward.md)是促使节点继续构建区块链的激励，同时也将新硬币分发到整个比特币网络中。

## 结论

比特币是一个与世界上其他计算机共享安全文件的计算机程序。这个安全文件由交易组成，这些交易使用密码学允许人们发送和接收数字保险箱。

结果，这创建了一个电子支付系统，任何人都可以使用，并且在没有中央控制点的情况下运行。

自 2009 年 1 月发布以来，比特币网络一直处于不间断运行状态。在 2023 年，比特币网络处理了超过 **1.53亿笔交易**，移动的资金总额达到 **$12,820,677,140,286** (12.82 万亿美元)[1](#fn1)。

比特币程序本身也处于活跃的开发状态，自发布以来已有超过 **600** 人为代码做出了贡献[2](#fn2)。这是由于该软件是“开源”的，这意味着任何人都可以查看代码并为改进代码做出贡献。

* [bitcoin.pdf](/bitcoin.pdf) – 白皮书
* [github.com/bitcoin/bitcoin/](https://github.com/bitcoin/bitcoin/) – 源代码