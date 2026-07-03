<img src="../../images/icons_loader-2.svg" alt="Loading Tool" style="height:32px; width:32px;" />

[交易](/docs/beginners/guide/transactions.md)中的每个[输出](/docs/beginners/guide/outputs.md)都有一个锁。这个锁是未来交易中花费该输出所必须满足的**一组要求**。

换句话说，这些锁可以防止比特币被盗（即其他人花费你的比特币），因为我们收到的每个输出都由一个锁*限制*。

例如，一个典型的锁看起来像这样：

[<img src="../../images/beginners_guide_locks_01-output-lock-english.png" alt="展示放置在交易输出上的简单锁的图表。" width="576" height="116" />](/docs/beginners/guide/locks/01-output-lock-english.png.md)

## 锁是在什么时候加在输出上的？

正如我们所知，[交易](/docs/beginners/guide/transactions.md)使用现有的输出并从中创建新的输出：

[<img src="../../images/beginners_guide_locks_02-transaction.png" alt="展示包含输入和输出的简单交易图表。" width="360" height="148" />](/docs/beginners/guide/locks/02-transaction.png.md)

正是在创建这些输出的过程中，我们为每个输出赋予了它们自己的“锁”：

[<img src="../../images/beginners_guide_locks_02-transaction-locks.png" alt="展示包含输入和输出，且输出上带有锁的简单交易图表。" width="364" height="161" />](/docs/beginners/guide/locks/02-transaction-locks.png.md)

所以当我们要给朋友发送比特币时，我们创建一个新输出，并添加一个锁，上面写着“只有地址 1friend1234567890... 的拥有者才能使用此输出”：

[<img src="../../images/beginners_guide_locks_02-transaction-locks-addresses.png" alt="展示输出锁定到具体地址的简单交易图表。" width="661" height="270" />](/docs/beginners/guide/locks/02-transaction-locks-addresses.png.md)

因此，这个新输出将有效地“属于”我们的朋友，因为他们是唯一拥有解锁锁定到此[地址](/docs/technical/keys/address.md)的比特币所需[私钥](/docs/beginners/guide/private-keys.md)的人，所以没有其他人能够花费它。

### 比特币存在哪里？

你可能已经注意到了，你从未真正把比特币直接从你的电脑“发送”到别人的电脑上。

相反，你是在构建一笔创建新输出（上面带有锁）的交易，将此交易数据发送到[比特币网络](/docs/beginners/guide/network.md)中，并等待它被开采进[区块链](/docs/beginners/guide/blockchain.md)中。

[<img src="../../images/beginners_guide_locks_aside-overview.png" alt="展示一笔包含输入和输出的交易被开采进区块链的图表。" width="314" height="493" />](/docs/beginners/guide/locks/aside-overview.png.md)

所以，尽管区块链是一个交易文件，但在实用层面上，你可以把它看作是**输出的存储库**。

[<img src="../../images/beginners_guide_locks_aside-blockchain-outputs.png" alt="展示区块链中区块内部各个输出的图表。" width="91" height="269" />](/docs/beginners/guide/locks/aside-blockchain-outputs.png.md)

区块链就是一个巨大的输出存储单元。

当你想要把“你的”比特币发送给某人时，你只需选择区块链中你可以解锁的输出：

[<img src="../../images/beginners_guide_locks_aside-blockchain-outputs-transaction.png" alt="展示交易选择区块链中输出的图表。" width="495" height="272" />](/docs/beginners/guide/locks/aside-blockchain-outputs-transaction.png.md)

而当这笔交易被开采到区块链中后，你用作输入的输出就不能再被使用了。

[<img src="../../images/beginners_guide_locks_aside-blockchain-outputs-transaction-mined.png" alt="展示一笔交易花费现有输出并将新输出添加到区块链的图表。" width="608" height="718" />](/docs/beginners/guide/locks/aside-blockchain-outputs-transaction-mined.png.md)

因此，区块链存储输出，你可以随时花费这些输出中的任何一个（当然，前提是你可以解锁它们）。

## 锁看起来像什么？

锁是用一种被称为 [Script](/docs/technical/script.md) 的基础编程语言编写的。

要用一张图表解释整门编程语言的工作原理有点困难，但我们试一下：

[<img src="../../images/beginners_guide_locks_03-locking-script.png" alt="展示输出上锁定脚本示例的图表。" width="416" height="153" />](/docs/beginners/guide/locks/03-locking-script.png.md)

这是一个简化版的锁定脚本示例；它不完全是 Script 的真实样子。

现在，这个锁定脚本中最有趣的部分是 `CHECKPRIVATEKEY` 部分，这是我们用来帮助设置锁要求的一个*函数*。

所以对于这个特定的输出，我们*设置了一个锁*，该锁想要将地址 1EUXSxuUVy2PC5enGXR1a3yxbEjNWMHuem 与一个[私钥](/docs/beginners/guide/private-keys.md)进行比较。

如果我们能为这个锁提供正确的私钥（该地址拥有者保持私密的那一个），我们就可以解锁它并在交易中花费它。

## 你如何解锁一个锁？

当你构建交易数据时，你会在要花费的每个输出旁边包含一个“解锁脚本”：

[<img src="../../images/beginners_guide_locks_04-unlocking-script.png" alt="展示交易输入旁的解锁脚本图表。" width="564" height="122" />](/docs/beginners/guide/locks/04-unlocking-script.png.md)

例如，要解锁一个典型的锁定脚本（例如 `[address] CHECKPRIVATEKEY`），我们需要证明我们*拥有*锁内部的地址。为此，我们提供与该地址相连的私钥。

[<img src="../../images/beginners_guide_locks_04-unlocking-script-privkey.png" alt="展示放入交易输入解锁脚本中私钥的图表。" width="609" height="122" />](/docs/beginners/guide/locks/04-unlocking-script-privkey.png.md)

因此，当节点收到此交易数据时，他们将一起运行“锁定”+“解锁”脚本，以查看你的私钥是否在数学上与该地址相连。

[<img src="../../images/beginners_guide_locks_04-locking-unlocking-script-simple.png" alt="展示锁定和解锁脚本计算为真的图表。" width="704" height="73" />](/docs/beginners/guide/locks/04-locking-unlocking-script-simple.png.md)

如果一切正常，该节点就会接受该交易并将其传递给其他节点，其他节点在接受交易之前也会依次运行“锁定”+“解锁”脚本。

这就是你解锁输出上的锁的方法。

### 我们这不是在泄露我们的私钥吗？

敏锐的观察。

坦白说：我们实际上并没有把我们的私钥放入解锁脚本中。

为了避免我们在交易数据中泄露私钥，我们使用私钥创建了一个被称为[数字签名](/docs/beginners/guide/digital-signatures.md)的东西来代替：

[<img src="../../images/beginners_guide_locks_05-unlocking-script-digitalsignature.png" alt="展示由私钥创建数字签名并放入解锁脚本的图表。" width="497" height="116" />](/docs/beginners/guide/locks/05-unlocking-script-digitalsignature.png.md)

显然，关于那个 `CHECKPRIVATEKEY` 函数我也撒了谎。

然而，确实*存在*一个比较地址与数字签名的函数，它被称为 `CHECKSIG`：

[<img src="../../images/beginners_guide_locks_05-unlocking-script-digitalsignature-simple.png" alt="展示数字签名解锁交易输入的图表。" width="393" height="34" />](/docs/beginners/guide/locks/05-unlocking-script-digitalsignature-simple.png.md)

多亏了数字签名的数学原理和 `CHECKSIG` 函数，我们仍然可以将输出锁定到地址，并在不泄露私钥的情况下解锁它们。

太棒了。

在 [Script](/docs/technical/script.md) 编程语言中有许多不同的可用函数。`CHECKSIG` 函数设计用于将输出锁定到特定地址，但你可以使用其他函数（以及进行各种组合）来创建复杂得多的锁。

例如，你可以创建一个只能在特定日期之后解锁的锁，或者一个只能由两个（或更多）不同地址的拥有者共同解锁的锁。

这就是为什么比特币有时被称为“可编程货币”的原因。