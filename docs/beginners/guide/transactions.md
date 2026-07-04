<img src="../../images/icons_loader-2.svg" alt="Loading Tool" style="height:32px; width:32px;" />

比特币交易只是一**堆数据**。

它包含有关发送**金额**、发送**自**哪个账户以及发送**至**哪个账户的信息。

[<img src="../../images/beginners_guide_transactions_01-transaction-table.png" alt="展示一笔交易将一定数量的比特币从一个地址转移到另一个地址的图表。" width="487" height="93" />](../../images/beginners_guide_transactions_01-transaction-table.png)

这只是信息，因此很容易用单行数据表示：

[<img src="../../images/beginners_guide_transactions_01-transaction-table-data.png" alt="展示一笔交易作为单行数据的图表。" width="479" height="162" />](../../images/beginners_guide_transactions_01-transaction-table-data.png)

当你“进行一笔交易”时，你只需将此*交易数据*发送到[比特币网络](network.md)中。

[<img src="../../images/beginners_guide_transactions_01-transaction-table-data-network.png" alt="展示交易被发送到比特币网络中的图表。" width="506" height="480" />](../../images/beginners_guide_transactions_01-transaction-table-data-network.png)

最终，网络上的某个[节点](node.md)会将你的交易[开采](mining.md)进一个[区块](blocks.md)中，这个区块（连同你的交易）将被添加到永久的交易文件中（该文件被称为[区块链](blockchain.md)）。

[<img src="../../images/beginners_guide_transactions_01-transaction-table-data-network-mined.png" alt="展示一笔交易在区块链上被开采进一个区块的图表。" width="132" height="254" />](../../images/beginners_guide_transactions_01-transaction-table-data-network-mined.png)

这就是比特币交易的全部——发送到比特币网络中的一单行简单数据，以便它可以被开采进区块链中。

## 比特币交易是如何工作的？

比特币[地址](../../technical/keys/address.md)就像一个存有比特币的*账号*。

然而，当你进行一笔交易时，并不像是从一个罐子里取出特定数量的硬币并放入另一个罐子。

[<img src="../../images/beginners_guide_transactions_02-pot.png" alt="展示交易并非把精确数量的硬币从一个罐子（地址）移动到另一个罐子的图表。" width="415" height="178" />](../../images/beginners_guide_transactions_02-pot.png)

相反，地址记录着它所收到的*每一笔独立付款*：

[<img src="../../images/beginners_guide_transactions_02-address1.png" alt="展示地址保存多笔独立付款金额（输出）的图表。" width="142" height="149" />](../../images/beginners_guide_transactions_02-address1.png)

所以当你想给别人发送比特币时，你拿取已经收到的*完整金额*，并用它们向新地址发送一个*新金额*：

[<img src="../../images/beginners_guide_transactions_02-address1-address2.png" alt="展示交易如何花费一个地址的输出并向不同地址发送新输出的图表。" width="518" height="197" />](../../images/beginners_guide_transactions_02-address1-address2.png)

当那个别人又想把比特币发送给另一个人时，他们也会以同样的方式用完他们收到的完整金额：

[<img src="../../images/beginners_guide_transactions_02-address1-address2-address3.png" alt="展示另一笔交易花费输出并发送到另外地址的图表。" width="699" height="173" />](../../images/beginners_guide_transactions_02-address1-address2-address3.png)

所以实际上，你是一*批*一*批*地接收比特币，并且使用这些批次来创建新的批次发送给其他人。

这就是交易的工作原理。

### 如果接收批次的总和大于我想发送的金额怎么办？

好问题，先生/女士。

在这种情况下（通常也是如此），你只需向交易中添加另一个*输出 (output)*，并将差额（找零）发回给自己：

[<img src="../../images/beginners_guide_transactions_02-address1-address2-change.png" alt="展示交易中找零输出的图表。" width="469" height="224" />](../../images/beginners_guide_transactions_02-address1-address2-change.png)

我知道这开始看起来可能有点尴尬，但从编程的角度来看，这是一种精确的处理方式。

### 总结

1. 你的[钱包](../wallets.md)给你一个比特币地址。比特币以批次的形式到达该地址，这些批次被称为*输出 (outputs)*。
2. 比特币交易就是使用这些输出（作为输入）来创建属于别人地址的新输出的过程。
3. 所有这些都可以由单行数据来表示。

[<img src="../../images/beginners_guide_transactions_02-address1-address2-change-data.png" alt="展示用单行数据表示的完整比特币交易图表。" width="477" height="382" />](../../images/beginners_guide_transactions_02-address1-address2-change-data.png)

有关此输出系统如何运作的更多细节，请查看[输出](outputs.md)。

## 什么能防止其他人花费我的比特币？

换句话说……

**问题：**“如果进行交易只是向比特币网络中输送一行数据，为什么别人不能构建一笔包含*我的地址*的交易，并用它把比特币发送到*他们的地址*呢？”

**答案：**因为每个交易输出上都有一个*锁*：

[<img src="../../images/beginners_guide_transactions_03-output-locks.png" alt="展示交易输出上方锁的图表。" width="379" height="237" />](../../images/beginners_guide_transactions_03-output-locks.png)

如果你在构建一笔交易时*不*解锁这些输出，比特币网络上的节点就会拒绝这笔交易：

[<img src="../../images/beginners_guide_transactions_03-output-locks-rejected.png" alt="展示节点拒绝输入未解锁的交易图表。" width="489" height="434" />](../../images/beginners_guide_transactions_03-output-locks-rejected.png)

但对你来说幸运的是，每个地址都配有一个唯一的[私钥](../../technical/keys/private-key.md)：

[<img src="../../images/beginners_guide_transactions_03-address-key.png" alt="展示地址以及对应私钥的图表。" width="435" height="73" />](../../images/beginners_guide_transactions_03-address-key.png)

所以，如果你想在一笔交易中发送比特币，你需要使用这个私钥来创建一个一次性的签名，该签名可以*解锁*你地址上的输出。

[<img src="../../images/beginners_guide_transactions_03-address-key-unlock.png" alt="展示使用私钥解锁已锁定在地址上的输出的图表。" width="345" height="228" />](../../images/beginners_guide_transactions_03-address-key-unlock.png)

在解锁了所有你想使用的输出之后，这笔交易就会被节点接受，并在比特币网络中进行传播。

[<img src="../../images/beginners_guide_transactions_03-output-locks-accepted.png" alt="展示具有已解锁输入的交易被节点接受并在网络中传播的图表。" width="489" height="539" />](../../images/beginners_guide_transactions_03-output-locks-accepted.png)

这就是比特币交易的工作原理。