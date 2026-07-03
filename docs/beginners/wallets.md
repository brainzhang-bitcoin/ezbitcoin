<img src="../images/icons_loader-2.svg" alt="Loading Tool" style="height:32px; width:32px;" />

[<img src="../images/beginners_wallets_electrum-screenshot.png" alt="Electrum 钱包的屏幕截图。" width="777" height="426" />](/docs/beginners/wallets/electrum-screenshot.png.md)


[Electrum](https://electrum.org/) 屏幕截图。

开始使用比特币的第一件事就是**获取你自己的钱包**。它们完全免费，只需几分钟即可[设置完成](#setup)。

一旦你拥有了钱包，你就拥有了开始接收和[发送](/docs/beginners/sending.md)比特币所需的一切。

## 最佳钱包

这是我列出的**最佳比特币钱包**清单。

这并非所有可用比特币钱包的详尽清单，而只是我个人使用过并*信任*的钱包简短列表。

### 桌面钱包

钱包 | 级别 | 操作系统 | 发布年份
--- | --- | --- | ---
[Electrum](https://electrum.org/) | 初学者/中级 | Linux/Windows/Mac | 2011
[Sparrow Wallet](https://www.sparrowwallet.com/) | 高级 | Linux/Windows/Mac | 2020

如果你是比特币的新手，我强烈建议你从*桌面钱包*开始。

桌面钱包通常比[移动钱包](#mobile-wallets)提供更多功能，并能让你更好地控制和管理你的比特币。

**我高度推荐 [Electrum](https://electrum.org/)。** 我已经使用它很多年了，它是我个人的最爱。

### 移动钱包

钱包 | 级别 | 操作系统 | 发布年份
--- | --- | --- | ---
[BlueWallet](https://bluewallet.io/) | 初学者 | iOS/Android | 2018
[Electrum](https://electrum.org/) | 初学者 | Android | 2016
[Blockstream Green](https://blockstream.com/green/) | 初学者 | iOS/Android | 2020
[Mycelium](https://wallet.mycelium.com/) | 中级 | Android | 2012

如果你没有台式计算机，移动钱包是一个不错的替代选择。

我不是特别喜欢移动钱包，因为它们提供的功能往往受限，而且我不喜欢随身携带你所有比特币的想法。

然而，如果移动钱包是你唯一可用的选择，或者你想用它来存放少量比特币进行支付，那么从移动钱包开始完全没有问题。我只是会避免在移动钱包中存放太多比特币，并在有机会时升级到[桌面钱包](#desktop-wallets)或[硬件钱包](#hardware-wallets)。

### 硬件钱包

钱包 | 级别 | 发布年份
--- | --- | ---
[Trezor](https://trezor.io/) | 初学者 | 2014
[Coldcard](https://coldcard.com/) | 高级 | 2018

硬件钱包是[安全存储](/docs/beginners/security.md)比特币的最佳选择。

购买硬件钱包需要花钱，而且不如桌面/移动钱包方便，但它们是*安全*的最佳选择。

我建议先从[桌面](#desktop-wallets)钱包开始，当你拥有了值得保护的比特币数量时，再升级到硬件钱包。

将用于日常消费的比特币放在桌面钱包中，将其余所有比特币保存在硬件钱包中。

## 设置

你如何设置比特币钱包？

在我的经历中，我设置过很多比特币钱包。

这相当简单，设置比特币钱包可以归纳为两个简单的步骤：

### 1. 下载并安装

[<img src="../images/diagrams_png_beginners-wallets-download.png" alt="展示直接从钱包网站下载比特币钱包的图表。" width="503" height="378" />](https://static.learnmeabitcoin.com/diagrams/png/beginners-wallets-download.png)

显然，第一步是下载并安装比特币钱包。

比特币钱包归根结底只是一个计算机小程序，所以你可以像下载和安装其他程序或 App 一样进行操作。

然而，关于比特币钱包最重要的一点是**直接从钱包的官方网站下载**。

比特币钱包管理着你访问比特币所需的所有[密钥](/docs/beginners/guide/keys-addresses.md)，其中一些密钥需要保持私密。因此，你最不希望看到的是从不可靠的来源下载钱包。如果你直接从钱包网站下载，你可以确信你获得的是真实版的软件。

所以请务必**双重确认你下载钱包的网站 URL**。

你还可以使用钱包网站（例如 [Electrum](https://electrum.org/)）上提供的签名来*验证*你的下载是否真实。这并非绝对必要，但如果可以做到，会让你更安心。

### 2. 抄写种子

在钱包的初始设置过程中，你将获得一个 12 或 24 个单词的[种子](/docs/technical/keys/hd-wallets/mnemonic-seed.md)。

**将此种子抄写在纸上并保存在安全的地方。**

[<img src="../images/diagrams_png_beginners-wallets-seed.png" alt="展示将种子抄写在纸上的图表。" width="601" height="371" />](https://static.learnmeabitcoin.com/diagrams/png/beginners-wallets-seed.png)


**这是一个种子的例子，请勿使用。** 你的种子必须是唯一的，并由你自己的钱包随机生成。

这个种子是你所有[密钥与地址](/docs/beginners/guide/keys-addresses.md)的来源。因此，如果你因为任何原因丢失了钱包，它允许你恢复所有的比特币。

[<img src="../images/diagrams_png_beginners-wallets-seed-addresses.png" alt="展示种子作为钱包中所有私钥和地址来源的图表。" width="578" height="423" />](https://static.learnmeabitcoin.com/diagrams/png/beginners-wallets-seed-addresses.png)


你所有的私钥和地址都是由种子生成的。

它基本上是发生意外时的终极备份。

但这也意味着任何只要能获取你种子的人都可以窃取你的比特币，因此确保其安全至关重要。

几个快速提示：

* **将种子抄写在*纸*上。** 将种子抄写在纸上是使其免受数字攻击的最快、最简单的方法。这听起来很原始，但很管用。
* **不要在计算机上以明文形式保存种子。** 如果你将种子保存在计算机上的某些文本文件中，一旦你的计算机被黑客入侵或有人获取了你的设备，种子就容易被盗。

我有一个朋友，他把种子的屏幕截图保存在共享的 Dropbox 文件夹中。我不太清楚具体是怎么被盗的，但没过多久里面的币就被全部转走了。

通过将种子写在纸上来保持离线状态，简单*且*有效。

* **在种子旁顺便记录下*钱包名称*和*日期*也是个好主意。** 这不是必须的，但对于你以后要恢复钱包时可能会有帮助。
* **如果你想以数字化方式存储种子，[KeePassXC](https://keepassxc.org/) 是一个不错的选择。** 但如果你对使用密码管理器没有信心，只需将其抄写在纸上即可。

## 功能

钱包是做什么的？

比特币钱包**管理密钥**，这些密钥是你发送和接收比特币所必需的。

当你想要*接收*付款时，你会使用你的一个[地址](/docs/technical/keys/address.md)。[比特币的工作方式](/docs/beginners/how-does-bitcoin-work.md)是在一笔[交易](/docs/beginners/guide/transactions.md)中，一定数量的比特币将被*锁*到你的地址上。

[<img src="../images/diagrams_png_beginners-wallets-receive.png" alt="展示钱包中的地址被用于接收比特币付款的图表。" width="608" height="257" />](https://static.learnmeabitcoin.com/diagrams/png/beginners-wallets-receive.png)

当你向其他人*发送*比特币时，你的钱包将创建一笔新交易，使用对应的[私钥](/docs/technical/keys/private-key.md)来*解锁*你已收到的比特币，并将一定数量的比特币锁到别人的地址上。

[<img src="../images/diagrams_png_beginners-wallets-send.png" alt="展示当你进行付款时，钱包创建交易并将其发送到网络中的图表。" width="771" height="325" />](https://static.learnmeabitcoin.com/diagrams/png/beginners-wallets-send.png)

总之，钱包主要做三件事：

1. 管理接收比特币所需的[地址](/docs/technical/keys/address.md)。
2. 管理发送比特币所需的对应[私钥](/docs/technical/keys/private-key.md)。
3. 创建[交易](/docs/technical/transaction.md)并将其发送到网络中。

* 钱包更像是*密钥管理*软件。
* 你通常在用钱包时只能看到你的地址——私钥是在后台进行管理的。

## 类型

钱包有哪些不同类型？

主要有两类钱包：

### 1. 软件钱包

又称热钱包 (Hot Wallet)

[<img src="../images/diagrams_png_beginners-wallets-software-wallet.png" alt="展示电脑上软件钱包直接连接互联网的图表。" width="435" height="318" />](https://static.learnmeabitcoin.com/diagrams/png/beginners-wallets-software-wallet.png)

软件钱包是你在电脑或手机上下载并运行的钱包。这些钱包**与互联网相连**，能让你快速方便地发送和接收比特币。

然而，缺点在于它们*与互联网相连*。因此，软件钱包**面临来自恶意软件和病毒的风险**。

如果你对计算机安全有把握，并且没有从不可靠来源下载危险软件的习惯，那么使用它们完全没问题。但自然地，风险总是存在的。

### 2. 硬件钱包

又称冷钱包 (Cold Wallet)

[<img src="../images/diagrams_png_beginners-wallets-hardware-wallet.png" alt="展示硬件钱包没有直接互联网连接的图表。" width="722" height="318" />](https://static.learnmeabitcoin.com/diagrams/png/beginners-wallets-hardware-wallet.png)

硬件钱包是专门用于存储比特币的*设备*。

这些设备**不与互联网连接**，这意味着它们受到了保护，免受软件钱包所面临的那些漏洞攻击。

硬件钱包在设备上存储你所有的[私钥](/docs/beginners/guide/private-keys.md)。因此，当你将硬件钱包连接到计算机进行[交易](/docs/beginners/guide/transactions.md)时，所有的[签名](/docs/beginners/guide/digital-signatures.md)都在设备上完成，你的私钥永远不会暴露给互联网。

购买硬件钱包需要花钱，而且与方便的软件钱包相比增加了一个步骤，但如果你有相当数量的比特币想要保护，你应该强烈考虑为自己配置一个硬件钱包。

硬件钱包是提高[比特币安全](/docs/beginners/security.md)你应该采取的第一步。

* **硬件钱包就像是在一台没有联网的独立笔记本电脑上设置软件钱包。** 在硬件钱包流行起来之前，我们以前就是这么做的。只是购买硬件钱包比购买第二台笔记本电脑更便宜、更方便。

## 常见问题

### Bitcoin Core 怎么样？

[Bitcoin Core](https://bitcoincore.org/en/download/) 是用作比特币钱包的一个极佳选择。

如果非要说的话，它是使用比特币的*终极*选择，因为它允许你验证你收到的每一笔付款**而无需信任**网络上的任何其他[节点](/docs/technical/networking/node.md)（因为你自己就是一个节点）。

缺点是在开始之前，你需要下载整个[区块链](/docs/technical/blockchain.md)，这会减慢初始的安装过程。但如果你有电脑硬件和时间来设置它，它作为一个比特币钱包是极好的选择。

然而，**下载一个简单的软件钱包要快得多、也容易得多**，这也是大多数人发送和接收比特币（包括我）所做的。这些钱包*连接*到网络上的节点以获取有关交易的信息，从而省去了你自己下载和存储整个区块链的麻烦。

[<img src="../images/diagrams_png_beginners-wallets-node-vs-wallet-trust.png" alt="展示软件钱包将信息发送到 Bitcoin Core 节点的图表。" width="983" height="654" />](https://static.learnmeabitcoin.com/diagrams/png/beginners-wallets-node-vs-wallet-trust.png)

但如果你喜欢，使用 Bitcoin Core 也完全没问题。

为了增加隐私，你也可以随时将软件钱包直接连接到你自己的 Bitcoin Core 节点上。

### 你需要钱包吗？

使用比特币钱包能让你**控制自己的比特币**。

如果你把比特币放在[交易所](/docs/beginners/exchanges.md)中，交易所则代替你控制着你的比特币。他们可以决定你可以提现多少，以及你可以将比特币发送到哪里。更糟糕的是，如果交易所消失了，你的比特币也就没有了。

[<img src="../images/diagrams_png_beginners-wallets-exchange-vs-wallet.png" alt="该图强调了在交易所持有比特币与在自己的钱包中持有比特币的区别。" width="624" height="529" />](https://static.learnmeabitcoin.com/diagrams/png/beginners-wallets-exchange-vs-wallet.png)

比特币中有一句流行语：

> 无私钥，非吾币 (Not your keys, not your coins)。

通过提现到自己的钱包，你就拥有了比特币的*保管权*。这给了你处理自己代币的自由，没有人可以决定把它们夺走。

但这也意味着你需要为自己的*安全*负责。

如果你信任交易所，胜过信任自己使用钱包的能力，那么将比特币留在交易所也没有什么*不对*。这听起来可能有点违背行业教条，但如果对你来说将比特币留在交易所感觉风险更小，那如果我试图说服你反其道而行之，我就是个傻瓜。

当然，我是比特币带来的自由的忠实拥趸，我鼓励任何人尽可能使用钱包来管理他们的比特币。但归根结底，你必须做最适合你的决定。

只需意识到，将代币留在交易所会带来其自身的一系列风险。

我建议至少尝试将少量比特币提取到钱包里，看看感觉如何。体验是最好的老师。

## 接下来该做什么？

一旦你的比特币钱包设置好了，你就已经准备好去[购买你的第一批比特币](/docs/beginners/exchanges.md)了。