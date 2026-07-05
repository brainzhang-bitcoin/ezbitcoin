<img src="images/icons_loader-2.svg" alt="Loading Tool" style="height:32px; width:32px;" />

# <img src="images/icons_file-text.svg" alt="Technical Icon" style="width:52px; height:52px" /> 技术

这是一份完整的比特币技术指南。

每个页面都包含关于比特币不同部分如何工作的简明**文字解释**和**图表**。它们还包括实际的**示例**和**工具**，以帮助您处理比特币中的原始数据。

因此，如果您*真的*想了解比特币底层的运作方式，本指南就是为您准备的。

## 如何成为一名比特币程序员

我在这份技术指南中包含了大量的**代码示例**，以帮助您编写自己的脚本。

这是因为学习如何成为一名比特币开发人员的最佳方式就是实际去**编写代码**。

## 代码示例如下所示

<img src="images/icons_ruby.svg" alt="Ruby Icon" style="width:52px; height:52px" />

大多数代码示例都使用 [Ruby](https://www.ruby-lang.org/en/) 语言，因为我认为它是最容易阅读的语言。

如果您不使用 Ruby，您应该也可以将这些代码片段作为参考，用您选择的编程语言重写代码。

您可以尽情阅读关于比特币如何运作的内容，但在您开始编码、犯错（您一定会犯错）并构建一些有用的工具之前，您永远不会取得真正的进展。所以不要害怕尝试。我们都必须从某个地方开始。

如果我能学会用比特币制作东西，您也一样可以。

总之，开始研究比特币并没有单一的“最佳”途径，但如果您完全是个新手，不知道从哪里开始，我的建议是……

### 安装 Linux (可选)

这完全是可选的，但我建议安装 Linux。

* **[Xubuntu](https://xubuntu.org/)** – 这是我首选的 Linux 发行版。它就是流行的 [Ubuntu](https://ubuntu.com/) 捆绑了轻量且实用的 [XFCE](https://xfce.org/) 桌面环境。它易于使用，如果您是从 Mac 或 Windows 转过来的，它是一个很好的起点，因为一切都是开箱即用的。
    

  [<img src="images/technical_my-setup-2020.png" alt="Screenshot of my desktop." width="960" height="540" />](images/technical_my-setup-2020.png)


  这是我的桌面外观。我当时正在制作这个 [SHA256 动画](https://www.youtube.com/watch?v=f9EbD6iY9zI)。

I really like Linux for programming work. Linux gives you complete control over your system, and it feels like a natural environment for writing your own programs and tools, because nothing is hidden away from you for your own safety or convenience.

I switched to Linux over a decade ago, and I haven't looked back since – it felt like I gained freedom over my operating system and I've never wanted to go back.

Obviously, if you're proficient with your current development environment, stick with that. But if you want to get better at programming and have felt limited in some way up until now, try using Linux instead.

### 安装 Bitcoin Core

<img src="images/svg_bitcoin-logo.svg" alt="Bitcoin Logo" style="width: 24px; height: 24px;" />

如果您打算开始对比特币进行开发，安装 [Bitcoin Core](https://bitcoin.org/en/download)（原始的比特币程序）是一个好主意。

在本地运行您自己的比特币节点有以下几个好处：

* **获取原始比特币数据**。通过在本地计算机上运行全节点，您可以快速轻松地访问原始的[区块](block.md)和[交易](transaction.md)数据，而无需依赖第三方 API：  

  ```
  bitcoin-cli getrawtransaction <txid>
  bitcoin-cli getblock <hash>
  ```
* **实用的命令行工具**。Bitcoin Core 程序打包了一系列命令行工具，我经常用它们进行调试 and decoding. Here are a couple of useful examples:  

  ```
  bitcoin-cli decoderawtransaction <raw transaction data>
  bitcoin-cli decodescript <hex script>
  ```
* **发送原始交易**。如果您的工作是构建自己的原始[交易](transaction.md)，您可以通过自己的本地节点将它们发送到比特币网络中：  

  ```
  bitcoin-cli sendrawtransaction <raw transaction data>
  ```

根据您对比特币进行的开发工作类型，您可能需要或不需要运行您自己的 Bitcoin Core 全节点。但如果您不确定，最好还是安装一个。

您可以通过运行 `bitcoin-cli help` 列出所有可用的命令。

### 使用您最喜欢的编程语言

<img src="images/icons_python.svg" alt="Python Icon" style="width:52px; height:52px" />
<img src="images/icons_ruby.svg" alt="Ruby Icon" style="width:52px; height:52px" />
<img src="images/icons_javascript.svg" alt="Javascript Icon" style="width:52px; height:52px" />
<img src="images/icons_go.svg" alt="Golang Icon" style="width:52px; height:52px" />
<img src="images/icons_cpp.svg" alt="C++ Icon" style="width:52px; height:52px" />
<img src="images/icons_php.svg" alt="PHP Icon" style="width:52px; height:52px" />

**您可以使用*any*您喜欢的编程语言来处理比特币**，因此您不妨使用您最喜欢的语言。

如果您使用自己喜欢的编程语言，您更有可能取得成功，而不是出于某种原因强迫自己使用您认为“应该”使用的语言。

如果您还不懂得任何语言，请选择一个您认为看起来很酷的语言。

最坏的情况下，如果事实证明您选择的语言太慢或由于某种原因完全不合适，您以后可以随时用不同的语言重写您的项目。但只有尝试了您才会知道。重写第二次会容易得多，因为您已经有了一个可以参考的代码库。

所以不要为选择哪种编程语言而纠结。选一个去尝试就好。一些流行的选择包括：

* **[Python](https://www.python.org/)** – 适合初学者。
* **[Ruby](https://www.ruby-lang.org/en/)** – 我个人最喜欢的语言。也适合初学者。
* **Javascript** – 适合基于 Web 的开发。
* **[Go](https://go.dev/)** – 适合快速的服务器端程序。
* **[C++](https://en.cppreference.com/w/)** – 这是 Bitcoin Core 代码库所使用的语言。

如果您想成为一名 *Bitcoin Core 开发人员*，您将需要学习 **C++**。

我是 [PHP](https://www.php.net/) 和 [Ruby](https://www.ruby-lang.org/en/) 的忠实粉丝。PHP 是因为我是我最精通的语言（这个网站和我的个人比特币库就是用它编写的），而 Ruby 是因为它使用起来很愉快且易于阅读（本网站的大多数示例都是用它编写的）。

这并不是说您应该使用这些特定的语言。事实上，我可能会因为使用 PHP 和 Ruby 而在某些编程圈子里被嘲笑（这理所当然）。但它们对我来说很好用，而且我用它们创建了一些非常有用的工具，这才是最重要的。

所以谁现在在笑呢。

简而言之，不要纠结于哪种语言是比特币的“最佳”语言。最好的语言永远是您能用来实际**构建东西**的那种。

**如果您坚持使用一种相当[流行的语言](https://www.tiobe.com/tiobe-index/)，会有更多的帮助。** 如果您使用没有其他人使用的语言，您会发现在解决棘手问题时往往只能靠自己。

### 从哪里开始比特币编程

如果我必须给您提供一条具体的路径，我会说在学习如何对比特币进行编程时，这**三个**最实用（且令人满意）的里程碑是：

1. **生成您自己的[密钥](keys.md)**。这是完美的起点。尝试生成您自己的[private key](keys/private-key.md)、[public key](keys/public-key.md)和[地址](keys/address.md)。然后将 private key 导入钱包，看看是否能得到与您生成的地址相同的地址。  

   生成

   ```
   private key: 7f8d051973cb85a72916ab28966fb389656af5d4e1ff68c3f20e44706c15add3
   public key:  027287f9c695c85e5f292dd7169fc2739cbf52885425c5cb69045080ca8d4d25a5
   address:     1PZnUgqGQhjfC3vEPHMBxBQBVFmsxaxa7P
   ```
2. **解码[交易](transaction.md)**。学习如何解码原始交易将教给您很多关于比特币交易结构的知识，它们构成了[blockchain](blockchain.md)内99%的数据。  

   <img src="images/icons_tool.svg" alt="Tool Icon" style="width:20px; height:20px" /> 交易分割器 (Transaction Splitter)

   随机示例

   交易数据

   * `0 bytes`
   * `0 vbytes`

   结果

   ```
    
   ```



   0 秒
3. **创建您自己的交易**。在解码交易之后，您就可以开始创建自己的交易了。这是一个大得多的里程碑（所以慢慢来），但这是自然的下一步。对其进行[签名](keys/signature.md)将是棘手的部分，但如果您能成功将自己的比特币交易发送到[网络](networking.md)中，那么您就可以确认自己是一个相当不错的比特币程序员了。  

   <img src="images/icons_tool.svg" alt="Tool Icon" style="width:20px; height:20px" /> 交易构建器 (Transaction Builder)

   随机示例

   类型

    Legacy

    Segwit

   Version

   0d

   * 基础交易


   输入 (1)


   输入 0 


   TXID
   * **注意:** 这只是作为示例提供的占位 TXID。
   VOUT

   0d

   scriptSig (ASM)



   Sequence

   0x



   [+] 添加输入



   输出 (1)


   输出 0


   金额 (satoshis)

   0d


   scriptPubKey (ASM)



   类型

    Non-Standard
    P2PK (Pay To Pubkey)
    P2PKH (Pay To Pubkey Hash)
    P2MS (Multisig)
    P2SH (Pay To Script Hash)
    P2WPKH (Pay To Witness Pubkey Hash)
    P2WSH (Pay To Witness Script Hash)
    P2TR (Pay To Taproot)
    OP\_RETURN (数据)


   [+] 添加输出


   Locktime

   0d

   * 区块高度

   ---



   原始交易数据

   ```
   0100000001aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0000000000ffffffff0100000000000000000000000000
   ```

   * `60 bytes`
   * `60 vbytes`

   0 秒

如果您能创建自己的比特币交易，那么比特币中就没有什么事情能超出您的能力了。

### 编写命令行工具

[<img src="images/technical_command-line-tools.gif" alt="Screencast showing bitcoin command line tools being used in the terminal." width="728" height="183" />](images/technical_command-line-tools.gif)

编写命令行工具是开始对比特币进行编程的好方法。

如果您还没有项目的具体想法，这尤其适用。此外，如果您打算花时间处理比特币数据，手头备有一堆命令行实用工具总是会很方便。

从长远来看，一些非常有用的基础命令行工具包括：

* **哈希函数** - 能够快速且轻松地获取一些数据的 [HASH256](cryptography/hash-function.md#hash256) 或 [HASH160](cryptography/hash-function.md#hash160) 非常方便，因为它们在比特币中随处可见。  

  <img src="images/icons_tool.svg" alt="Tool Icon" style="width:20px; height:20px" /> HASH256

  随机交易数据

  随机区块头

  数据 (Hex)

  `0 bytes`


  <img src="images/icons_hash-function.svg" alt="Hash Function Icon" style="width:52px; height:52px" />
  SHA-256

  <img src="images/icons_hash-function.svg" alt="Hash Function Icon" style="width:52px; height:52px" />
  SHA-256

  HASH256

  SHA-256(SHA-256(data))

  `0 bytes`



  0 秒

  <img src="images/icons_tool.svg" alt="Tool Icon" style="width:20px; height:20px" /> HASH160

  数据 (Hex)

  例如公钥或脚本

  `0 bytes`


  <img src="images/icons_hash-function.svg" alt="Hash Function Icon" style="width:52px; height:52px" />
  SHA-256

  <img src="images/icons_hash-function.svg" alt="Hash Function Icon" style="width:52px; height:52px" />
  RIPEMD-160

  HASH160

  RIPEMD-160(SHA-256(data))

  `0 bytes`



  0 秒
* **反转字节顺序** - 这对我来说极其宝贵。您经常需要反转 [txid](transaction/input/txid.md) 和[block hashes](block/hash.md)的[byte order](general/byte-order.md)，因为在原始交易数据和区块数据中使用的字节顺序与在[blockchain explorer](/explorer/)中搜索它们时的字节顺序正好相反。此外，原始比特币数据中的大多数字段都是“[little-endian](general/little-endian.md)”，因此在将十六进制和十进制数相互转换时，您经常需要反转字节顺序。  

  <img src="images/icons_tool.svg" alt="Tool Icon" style="width:20px; height:20px" /> 反转字节 (Reverse Bytes)

  随机示例

  字节

  `0 bytes`

  已反转

  `0 bytes`


   显示详情



  0 秒
* **数字转换器** - 我记不清有多少次我需要将[hexadecimal](general/hexadecimal.md)转换成十进制（反之亦然）。如果您愿意，可以使用在线工具，但没有什么比打开终端并使用自己编写的脚本转换数字更好的了。  

  <img src="images/icons_tool.svg" alt="Tool Icon" style="width:20px; height:20px" /> 数字转换器 (Number Converter)

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



  0 秒

但不要仅仅为了写命令行工具而写。这只是个好的开始，但在您成为比特币程序员的道路上，您的主要焦点应该是开发自己的项目……

### 您的第一个比特币项目 (重要)

学习成为比特币程序员的最好方法就是尝试**构建一些东西**。

如果您对想要构建的东西有了想法，那就尽管去探索，并**在过程中学习您需要学习的知识**。您不需要了解比特币的每一个方面就能开始开发有用的东西。

开始时这似乎是一项艰巨的任务，特别是如果您是比特币和/或编程的新手，但如果您能一步一个脚印，您最终会达到目标。

因为正如生活中的任何事情一样，只要您拒绝放弃，就不可能失败。

总之，我猜您已经想好了自己想构建什么。但如果您 need some inspiration, here are some popular tools that other people have built:

#### Web 工具

* [Mnemonic Code Converter](https://iancoleman.io/bip39/)（作者 [Ian Coleman](https://iancoleman.io/)）
* [Bitfeed](https://bitfeed.live/)（作者 [mononaut](https://x.com/mononautical)）
* [Yogh Explorer](https://yogh.io/)（作者 [Jorn C](https://github.com/JornC)）
* [mainnet-observer](https://mainnet.observer/)（作者 [b10c](https://github.com/0xB10C)）
* [Bitcoin Mempool Size Statistics](https://jochen-hoenicke.de/queue/)（作者 [Jochen Hoenicke](https://jochen-hoenicke.de/)）

#### 桌面工具

* [Electrum](https://electrum.org/)（作者 [Thomas Voegtlin](https://github.com/ecdsa)）
* [Sparrow Wallet](https://www.sparrowwallet.com/)（作者 [Craig Raw](https://x.com/craigraw)）

#### 命令行工具

* [bitcoin-iterate](https://github.com/rustyrussell/bitcoin-iterate)（作者 [Rusty Russel](https://x.com/rusty_twit)）
* [vanitygen](https://github.com/samr7/vanitygen)（作者 [samr7](https://github.com/samr7)）
* [bitcoin-utxo-dump](https://github.com/in3rsha/bitcoin-utxo-dump)（作者 [Greg Walker](https://learnmeabitcoin.com/)）

这只是由*个人*开发的一些很酷的工具。我认为，如果您有好的创意和坚持到底的决心，它们对比特币的开发是大有裨益的。

所以，放手去创造一些尚不存在的有用工具，然后将其提供给其他人使用，看看会发生什么。

**要负责任**。如果您在创建一个处理 [private keys](keys/private-key.md) 或为其他人创建[transactions](transaction.md)的工具（例如钱包），您需要非常小心。自己犯错导致丢失自己的币是一回事，但犯错导致他人丢失币则是另一回事，所以千万不要掉以轻心。

**在 [GitHub](https://github.com/) 上分享您的工作**。这是与世界分享代码的好方法，也是在寻找工作时展示经验的好机会（如果您想朝这个方向发展）。

### 总结

不要让任何人让您觉得您不能成为一名比特币程序员。

比特币是去中心化的开源软件。如果您愿意，您可以生成自己的[keys](keys.md)并构建自己的[transactions](transaction.md)，没有人可以阻止您。这也是比特币之所以成为比特币的一部分。

我相信有些人会试图说服您需要某种资格才能对比特币进行开发，但请允许我告诉您，您不需要。您需要的一切都可以在互联网上免费学到，甚至只需通过阅读[bitcoin source code](https://github.com/bitcoin/bitcoin/)即可。对比特币进行开发唯一真正的资格就是贡献的愿望，其他一切都可以在过程中学到。

我们都必须从某个地方开始，如果您有想法和实现它的热情，那么您就和任何其他人一样有资格成为比特币程序员。

最好的钱包和工具正是由那些在某些时候对比特币毫无经验的人构建的。

## 📚 技术主题目录

* **📦 区块与区块链 (Blocks & Blockchain)**
  * [区块总览](block.md)
  * [区块链总览](blockchain.md)
    * [比特币的 Blockchain - Part 1](blockchain/bitcoin-blockchain-part1.md)
    * [比特币的 Blockchain - Part 2](blockchain/bitcoin-blockchain-part2.md)
* **🔐 密码学 (Cryptography)**
  * [密码学总览](cryptography.md)
* **🔑 密钥、签名与地址 (Keys & Addresses)**
  * [密钥总览](keys.md)
* **💸 比特币交易 (Transactions)**
  * [交易总览](transaction.md)
    * [比特币的交易 - Part 5](transaction/bitcoin-transaction-part5.md)
    * [比特币的交易 - Part 6](transaction/bitcoin-transaction-part6.md)
* **⚡ 闪电网络与 Lnd 技术 (Lightning Network)**
  * [Lnd 启动扫描速度慢分析](lightning/lnd-low-rescan-speed-startup.md)
  * [如何通过 lnd-cli 关闭通道](lightning/how-to-close-lightning-channels-by-lnd-cli.md)
  * [闪电网络基础与原理 - Part 0](lightning/hello-lightning-network-part0.md)
  * [闪电网络基础与原理 - Part 1](lightning/hello-lightning-network-part1.md)
  * [闪电网络基础与原理 - Part 2](lightning/hello-lightning-network-part2.md)
  * [闪电网络基础与原理 - Part 3](lightning/hello-lightning-network-part3.md)
  * [闪电网络节点搭建与配置小抄](lightning/setup-lightning-node-cheat-sheet.md)
  * [Eltoo 闪电和离线契约更新机制](lightning/eltoo-lightning-offchain-contracts.md)
  * [闪电网络的慢慢成长之路](lightning/lightning-network-gradual-growth.md)
* **⛏️ 挖矿与网络 (Mining & Networking)**
  * [挖矿总览](mining.md)
  * [网络协议总览](networking.md)
    * [比特币 daemon 服务 Systemd 启动配置](networking/how-to-set-systemd-startup-script-for-bitcoind.md)

### 其他资源

谁也不会再仅从一本书或一个网站了解一门完整的学科，所以这里有其他一些我发现非常有用的极好比特币技术资源：

#### 网站

* [Bitcoin Developer Guide](https://developer.bitcoin.org/devguide/) – 官方指南。非常技术化，但内容详实。
* [Bitcoin Wiki](https://en.bitcoin.it/wiki/Main_Page) – 许多在其他地方找不到的技术信息。
* [Bitcoin Stack Exchange](https://bitcoin.stackexchange.com/) – 寻求问题答案的最佳场所。
* [BIPs](https://bips.dev/) – 大多数提案都包含关于特定升级的极好技术信息。

#### 图书

* [Mastering Bitcoin](https://github.com/bitcoinbook/bitcoinbook)
* [Programming Bitcoin](https://github.com/jimmysong/programmingbitcoin)

#### 其他

* [lopp.net Resources](https://www.lopp.net/bitcoin-information.html) – 著名的比特币相关资源中心。
* [Royal Fork Blog](https://www.royalfork.org/) – 巧妙撰写的文章，解释了比特币的某些方面。其中的一些页面启发了本网站的创作。
* [Minimum Viable Block Chain](https://www.igvita.com/2014/05/05/minimum-viable-block-chain/) – 优秀的单页文章，由一位伟大的技术作家撰写，介绍区块链技术。
* [RaspiBolt](https://raspibolt.org/) – 在树莓派上设置比特币节点的指南。为了获得经验，值得至少尝试一次。

#### 库

学习比特币运作方式的聪明方法是从用您自己正在使用的语言编写的**现有比特币库**中学习。

您可以通过搜索“[语言] bitcoin library”找到几乎任何编程语言的比特币库。例如：

* Go: [btcd](https://github.com/btcsuite/btcd)（强烈推荐；极佳的代码注释）
* PHP: [bitcoin-php](https://github.com/Bit-Wasp/bitcoin-php)
* Ruby: [bitcoin-ruby](https://github.com/lian/bitcoin-ruby)
* Javascript: [bcoin](https://github.com/bcoin-org/bcoin)

外面有丰富的开源代码，有时最好看看别人是如何解决问题的，以帮助您弄清楚如何自己去实现它。

祝你好运。