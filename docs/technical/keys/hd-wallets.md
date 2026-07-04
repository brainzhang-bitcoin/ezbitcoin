<img src="../../images/icons_loader-2.svg" alt="Loading Tool" style="height:32px; width:32px;" />

[BIP 32: Hierarchical Deterministic Wallets](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki)

[<img src="../../images/diagrams_png_hd-wallets.png" alt="Diagram showing the basic structure of an HD Wallet." width="983" height="673" />](../../images/diagrams_png_hd-wallets.png)

分层确定性钱包（或简称 "HD Wallets"）是一种从单一源生成其所有密钥和地址的钱包。

* **分层（Hierarchical）** – 密钥和地址可以组织成一棵 *树*。
* **确定性（Deterministic）** – 密钥和地址总是以 *相同的方式* 生成。

所以基本上，HD Wallets 允许你使用单个 [seed](hd-wallets/mnemonic-seed.md) 生成数十亿个[私钥](private-key.md)。因此，只要你记住 seed，你就始终能够恢复相同的密钥和[地址](address.md)。

这使得它们比早期单独生成和存储私钥的[比特币钱包](../../beginners/wallets.md)更加用户友好。

HD Wallets 最有趣的特性是你可以生成新的公钥，而 *无需* 同时生成它们对应的私钥。

## 示例

以下是我喜欢的一些流行的 HD Wallets 示例：

* [Electrum](https://electrum.org/) (桌面端)
* [Sparrow Wallet](https://www.sparrowwallet.com/) (桌面端)
* [Trezor](https://trezor.io/) (硬件钱包)
* [Coldcard](https://coldcard.com/) (硬件钱包)

几乎所有现代钱包（自 2013 年以来）都是分层确定性的。

### 助记词

当你创建 HD Wallets 时，你会获得一个包含 12 或 24 个单词的[助记词](hd-wallets/mnemonic-seed.md)。这是 *seed* 的来源，然后用于生成钱包中的所有密钥和地址。

例如：

新 Seed

**切勿使用由网站生成的 seed，也不要在网站中输入你的 seed。** 网站很容易保存 seed 并利用它窃取你的所有比特币。




### 派生路径

你的 HD Wallets 中的密钥将根据你想使用的[地址](address.md)类型，使用以下[派生路径](hd-wallets/derivation-paths.md)之一生成：

```
m/44'/0'/0' <- 1地址 (P2PKH)
m/49'/0'/0' <- 3地址 (P2SH-P2WPKH)
m/84'/0'/0' <- bc1地址 (P2WPKH)
```

## 优势

HD Wallets 的优势是什么？

### 1. 单一备份

在基础钱包中，每次你想接收比特币时，都会独立生成[私钥](private-key.md)和[公钥](public-key.md)对。

[<img src="../../images/technical_keys_hd-wallets_basic-wallet.gif" alt="Diagram showing individual private and public keys generated in a non-HD Wallet." width="900" height="301" />](../../images/technical_keys_hd-wallets_basic-wallet.gif)


基础钱包。

这运行得很好，但这意味着*每次你收到新的付款时*，你都需要备份你的钱包。

然而，在分层确定性钱包中，你可以使用单个 **[seed](hd-wallets/mnemonic-seed.md)** 来创建 **[主私钥](hd-wallets/extended-keys.md#master-extended-key)**，并可以使用它来生成数十亿个“子”私钥和公钥。

[<img src="../../images/technical_keys_hd-wallets_hd-wallet.gif" alt="Diagram showing private and public keys generated from a single seed in an HD Wallet." width="900" height="425" />](../../images/technical_keys_hd-wallets_hd-wallet.gif)


HD Wallets（确定性）。

所以现在你唯一需要备份的就是 **seed**，因为你从中创建的主私钥将始终以相同的方式（*确定性地*）生成你钱包的密钥。

### 2. 组织性

分层确定性钱包的另一个酷炫之处在于其 *分层* 部分。

钱包中的每个[**子密钥**](hd-wallets/extended-keys.md#child-key-derivation)也可以**生成它自己的密钥**，这意味着你可以创建一个**树状结构**（或*层级*）来组织钱包中的密钥。

[<img src="../../images/technical_keys_hd-wallets_hierarchical.gif" alt="Diagram showing the hierarchical structure of keys in an HD wallet." width="900" height="332" />](../../images/technical_keys_hd-wallets_hierarchical.gif)


HD Wallets（分层）。

然后，你使用树的不同部分将密钥分入不同的“账户”中。

### 3. 独立生成公钥

但是，**主私钥**真正酷炫的地方在于它有一个相对应的**主公钥**，这可以在没有私钥的情况下生成相同的子公钥。

[<img src="../../images/technical_keys_hd-wallets_extended-public-key.gif" alt="Diagram showing how you can generate public keys independently of their corresponding private keys in an HD Wallet." width="900" height="336" />](../../images/technical_keys_hd-wallets_extended-public-key.gif)


你可以独立于相对应的私钥生成公钥。

因此，你可以将 **主公钥** 发送到另一台计算机（例如网络商店服务器）以生成新的接收地址，而不必担心如果服务器被黑客入侵，私钥会被窃取。

这看起来像魔法，但这全是数学。

这也适用于像**硬件钱包**这样的设备 – 你可以将私钥保存在安全设备上，并在另一台计算机上生成新的地址来接收付款。

## HD Wallets 是如何工作的？

以下是 HD Wallets 工作原理的**视觉概述**。

有关技术细节，请参阅[扩展密钥](hd-wallets/extended-keys.md)。

### 1. Seed

[<img src="../../images/diagrams_png_hd-wallets-seed.png" alt="Diagram showing a 64-byte seed used as the source for an HD Wallet." width="393" height="110" />](../../images/diagrams_png_hd-wallets-seed.png)

要创建 HD Wallets，首先要生成 64 个随机[字节](../general/bytes.md)。这就是我们的 **seed**。

#### 示例


新 Seed

### 2. 主私钥

[<img src="../../images/technical_keys_hd-wallets_master-key.gif" alt="Animation showing the creation of a master private key from a 64-byte seed." width="900" height="554" />](../../images/technical_keys_hd-wallets_master-key.gif)

“主密钥”是通过将 seed 输入到哈希函数（称为 HMAC）中以生成*另一*组 64 字节来创建的。

<img src="../../images/icons_tool.svg" alt="Tool Icon" style="width:20px; height:20px" /> HMAC-SHA512

随机示例

数据 (十六进制)

seed 或 (私钥/公钥 + 4字节索引)

`0 bytes`

密匙 (十六进制)

"Bitcoin seed" 或 链码

`0 bytes`

"Bitcoin seed"
(ASCII)

<img src="../../images/icons_hash-function-hmac.svg" alt="HMAC Icon" style="width:128px; height:128px" />
HMAC-SHA512

结果

HMAC-SHA512(data, key)

`0 bytes`



0 secs

我们使用这 64 字节来创建我们的**主**扩展私钥。

* **前** 32 字节是私钥。
* **后** 32 字节是链码。

链码只是额外的 32 字节，我们将它与私钥结合起来创建我们所说的[扩展密钥](hd-wallets/extended-keys.md)。

#### 示例

“扩展密钥”只是与链码相结合的普通密钥。

**我们为什么要对 seed 进行哈希？** 我们*本来可以*直接使用 64 字节的 seed 来创建主扩展私钥。然而，未来的子扩展密钥是使用 HMAC 创建的，因此与我们的创建方式保持一致是件好事。

扩展密钥内嵌入的私钥可以像往常一样用于创建相对应的[公钥](public-key.md)：

<img src="../../images/icons_tool.svg" alt="Tool Icon" style="width:20px; height:20px" /> 公钥

生成随机

私钥

`0 bytes`

公钥坐标

x:

0d

y:

0d

奇偶性:

公钥只是椭圆曲线上的一个点。最终的公钥是这些坐标的十六进制形式。

压缩
 压缩 (02 或 03 前缀)
 未压缩 (04 前缀)
 仅 x (无前缀)

椭圆曲线沿 x 轴对称，因此*压缩*公钥只需存储完整的 x 坐标以及 y 坐标是偶数还是奇数。

仅 x 公钥用于 [Taproot](../upgrades/taproot.md) 输出。相对应的 y 坐标被假定为偶数。

`0 bytes`



**切勿在网站中输入你的私钥，或使用由网站生成的私钥。** 网站很容易保存私钥并利用它窃取你的比特币。

0 secs

*实际* 的**主**扩展私钥本身就只是私钥和链码。

### 3. 子密钥 (基础)

派生私钥和公钥

通过将扩展私钥（私钥和链码）输入到 HMAC 函数中，从扩展私钥生成新的子私钥。

我们每次还会包含一个**索引**号，这允许我们从单个主密钥创建多个子密钥。

[<img src="../../images/technical_keys_hd-wallets_child-keys-basic-private.gif" alt="Animation showing the derivation of hardened extended private key children." width="900" height="533" />](../../images/technical_keys_hd-wallets_child-keys-basic-private.gif)


通过更改**索引**，你会从哈希函数中得到完全不同的结果。

所以本质上，新的私钥是通过将主扩展私钥与**索引**号一起进行[哈希](../cryptography/hash-function.md)生成的。




#### 示例

在哈希父扩展私钥后计算子私钥时有一个额外的数学步骤。这就是为什么你无法通过简单地将 (32字节私钥 | 4字节索引) 和 (32字节链码) 输入到 HMAC 中来获得正确结果。详情请参阅[扩展密钥](hd-wallets/extended-keys.md)。

一个扩展密钥可以生成 2,147,483,648 个此类“基础”（硬化）子密钥。

### 4. 子密钥 (高级)

派生私钥和公钥，并独立派生公钥

这是有趣的部分。

如果我们想让扩展私钥创建子私钥和公钥，但同时也想让它相对应的扩展公钥能够生成相同的子公钥呢？

换句话说，我们如何在没有私钥的情况下生成公钥？

#### 1. 扩展公钥

首先，我们需要构建扩展公钥。

这只是来自扩展私钥的公钥与相同的链码相结合：

[<img src="../../images/technical_keys_hd-wallets_corresponding-extended-public-key.gif" alt="Animation showing the creation of an extended public key." width="900" height="107" />](../../images/technical_keys_hd-wallets_corresponding-extended-public-key.gif)

<img src="../../images/icons_tool.svg" alt="Tool Icon" style="width:20px; height:20px" /> 公钥

生成随机

私钥

`0 bytes`

公钥坐标

x:

0d

y:

0d

奇偶性:

公钥只是椭圆曲线上的一个点。最终的公钥是这些坐标的十六进制形式。

压缩
 压缩 (02 或 03 前缀)
 未压缩 (04 前缀)
 仅 x (无前缀)

椭圆曲线沿 x 轴对称，因此*压缩*公钥只需存储完整的 x 坐标以及 y 坐标是偶数还是奇数。

仅 x 公钥用于 [Taproot](../upgrades/taproot.md) 输出。相对应的 y 坐标被假定为偶数。

`0 bytes`



**切勿在网站中输入你的私钥，或使用由网站生成的私钥。** 网站很容易保存私钥并利用它窃取你的比特币。

0 secs

#### 示例



#### 2. 扩展私钥子密钥

主扩展私钥通过将其相对应的扩展公钥的内容输入到 HMAC 函数中，并将结果*相加*到*原始*私钥来创建**子**私钥。

[<img src="../../images/technical_keys_hd-wallets_child-keys-advanced-private.gif" alt="Animation showing the derivation of normal extended private key children." width="900" height="533" />](../../images/technical_keys_hd-wallets_child-keys-advanced-private.gif)



#### 示例

#### 3. 扩展公钥子密钥

主扩展公钥通过将其内容输入到 HMAC 函数中，并将结果*相加*到*原始*公钥来创建**子**公钥。

[<img src="../../images/technical_keys_hd-wallets_child-keys-advanced-public.gif" alt="Animation showing the derivation of normal extended public key children." width="900" height="533" />](../../images/technical_keys_hd-wallets_child-keys-advanced-public.gif)



#### 示例

* 一个扩展密钥可以生成 2,147,483,648 个这些“高级”（普通）子密钥。
* 因此，一个扩展密钥总共可以派生出 4,294,967,296 个子密钥：
  * **普通（Normal）** = 2,147,483,648 (索引 `0` 到 `2147483647`)
  * **硬化（Hardened）** = 2,147,483,648 (索引 `2147483648` 到 `4294967295`)

现在，因为这次子密钥已根据**父**私钥和公钥进行了*调整*，[椭圆曲线](../cryptography/elliptic-curve.md)数学的魔力意味着**子**私钥和公钥将一一对应。

[<img src="../../images/technical_keys_hd-wallets_child-keys-advanced-private-public.gif" alt="Animation showing the derivation of normal extended private key and extended public key children." width="900" height="533" />](../../images/technical_keys_hd-wallets_child-keys-advanced-private-public.gif)

我知道这看起来像魔法，但这只是数学。

## 常见问题

### 为什么我们使用链码？

添加链码意味着子密钥不是*仅*从密钥中派生出来的。

例如，我们可能使用树中的一个公钥来接收付款，这将使它在[区块链](../blockchain.md)上可见。如果我们不使用链码，任何人都可以获取此公钥并派生它的所有子密钥：

[<img src="../../images/technical_keys_hd-wallets_without-chain-code.png" alt="Diagram showing how you can derive child public keys if a chain code is not used." width="900" height="232" />](../../images/technical_keys_hd-wallets_without-chain-code.png)

但是通过使用不公开到区块链上的链码，其他人就无法从公钥派生出子密钥：

[<img src="../../images/technical_keys_hd-wallets_with-chain-code.png" alt="Diagram showing how you can't derive child public keys if a chain code is used." width="900" height="232" />](../../images/technical_keys_hd-wallets_with-chain-code.png)

因此，换句话说，链码是额外的秘密数据，可防止其他人派生密钥的子密钥。

### HD Wallets 中的密钥是否相连？

**不相连**。

你无法看出树中的任何两个公钥（或[地址](address.md)）是否属于同一个钱包（即从同一个主扩展密钥派生而来）。

即使子密钥是从主扩展密钥确定性地派生出来的，实际的私钥和公钥本身之间也没有任何相似之处。

因此，对外部世界来说，所有的私钥和公钥就像是完全独立生成的一样。

[<img src="../../images/technical_keys_hd-wallets_hd-wallet-are-keys-connected.png" alt="Diagram showing how the public keys in an HD wallet appear to be completely independent to the outside world." width="900" height="353" />](../../images/technical_keys_hd-wallets_hd-wallet-are-keys-connected.png)

### HD Wallets 中的密钥安全吗？

安全，你从 HD Wallets 获得的所有私钥和公钥，都与你使用随机数生成器独立生成的密钥一样安全。

然而，**扩展密钥应该格外安全地保存**，因为任何有权访问它们的人都可以派生出它们所有的子密钥。

例如，如果你透露了你的主扩展公钥，其他人将能够找到你钱包中的所有地址。他们 *无法偷走任何东西*，因为他们无法为它们生成私钥，但他们仍然可以看到你拥有多少比特币。

[<img src="../../images/technical_keys_hd-wallets_security-extended-public-key.png" alt="Diagram showing how someone can derive all the child public keys from an extended public key." width="900" height="235" />](../../images/technical_keys_hd-wallets_security-extended-public-key.png)

泄漏父扩展公钥 *以及* 任何子私钥，会允许他人计算出父扩展私钥。

如果他们能计算出扩展私钥，他们就可以生成该层级（及以下）钱包的所有私钥，**并窃取你的比特币**：

[<img src="../../images/technical_keys_hd-wallets_security-extended-public-key-child-private-key.png" alt="Diagram showing how someone can derive all the child private keys from an extended public key and a single private key." width="900" height="298" />](../../images/technical_keys_hd-wallets_security-extended-public-key-child-private-key.png)

你起初可能认为这不可能，但确实可以，所以请注意这一点。

* 尽量不要透露你的扩展公钥。如果透露了，其他人就可以找到你钱包中的地址。
* 如果你*还*透露了子私钥，那就和透露扩展私钥一样糟糕了。

## 地址

HD Wallets 中的扩展私钥和扩展公钥有它们自己的地址格式。

<img src="../../images/icons_tool.svg" alt="Tool Icon" style="width:20px; height:20px" /> 地址（扩展密钥）

生成随机示例


扩展密匙数据


类型

 传统 ([BIP 44](https://github.com/bitcoin/bips/blob/master/bip-0044.mediawiki))
  扩展私钥 (xprv)
  扩展公钥 (xpub)

注意：1地址 ([P2PKH](../script/p2pkh.md))


 Segwit ([BIP 49](https://github.com/bitcoin/bips/blob/master/bip-0049.mediawiki))
  扩展私钥 (yprv)
  扩展公钥 (ypub)

注意：3地址 (P2SH-P2WPKH)


 Segwit ([BIP 84](https://github.com/bitcoin/bips/blob/master/bip-0084.mediawiki))
  扩展私钥 (zprv)
  扩展公钥 (zpub)

注意：bc1地址 ([P2WPKH](../script/p2wpkh.md))

深度

从主密钥派生的深度（如果是主密钥则为 0）

0d


+1

指纹

父公钥 HASH160 的前 4 个字节（如果是主密钥则为 00000000）

索引

此密钥与其父密钥的索引号（如果是主密钥则为 0）

0d


+1

链码

父密钥 HMAC-SHA512 的最后 32 字节（密钥+索引，链码）或（seed，密码学密码）

`0 bytes`

密匙

原始私钥（32字节）或公钥（33字节）

`0 bytes`


序列化 (十六进制)

`0 bytes`

校验和`0 bytes`

地址

序列化扩展密钥和校验和的 Base58 编码

`0 characters`



**切勿使用由网站生成的私钥，或在网站中输入你的私钥。** 网站很容易保存私钥并利用它窃取你的比特币。

0 secs

例如，这是我们的主扩展私钥序列化后的样子：

然后，我们可以通过对其进行 [base58check](base58.md#base58check) 编码来使其成为地址：

这现在是我们的扩展私钥更有用的格式，因为它更容易在计算机之间共享并导入到钱包中。

详情请参阅[扩展密钥地址](hd-wallets/extended-keys.md#address)。

## 历史

谁发明了 HD Wallets？

1. [**Gregory Maxwell**](https://github.com/gmaxwell) 提出了最初的想法，即你可以微调公钥以获取新的公钥，而无需知道它们对应的私钥，这也被称为 *同态派生（homomorphic derivation）*。
2. [**Armory**](https://btcarmory.com/) 是第一个实现这种同态派生的钱包，并且还引入了使用链码的概念。
3. [**Pieter Wuille**](https://github.com/sipa) 提出了使用 *分层* 结构的想法，并基于 Armory 使用的方案创建了 [BIP 32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki) 规范。

> FSF 想要接受比特币捐赠，并希望为每个用户生成新的地址，但不希望在他们的 Web 服务器上留有私钥。

Gregory Maxwell, (于 IRC)


> HD Wallets (BIP32) 是基于 Armory 的方案，但具有更大的灵活性（分层结构），以及在索引中的随机访问（Armory 的方案要求在派生地址编号 n 之前，生成 n 之前的所有 N 个地址）。

Pieter Wuille, (于 IRC)

## 总结

[<img src="../../images/technical_keys_hd-wallets_hierarchical-deterministic-wallets.gif" alt="Animation showing the overall structure of an HD wallet." width="900" height="616" />](../../images/technical_keys_hd-wallets_hierarchical-deterministic-wallets.gif)

**分层确定性钱包**提供了一种生成新[私钥](private-key.md)和[公钥](public-key.md)的有用方法。

它是 *确定性* 的，因为所有的子密钥每次都是以 **相同的方式** 从单个 seed 生成的；它是 *分层* 的，因为你可以将密钥组织成 **树状结构**（或层级）。额外的好处是可以在完全不了解私钥的情况下派生钱包中的公钥，这非常神奇。

如果你对 HD Wallets 的细节感兴趣，这里有一些更具技术性的解释：

* [助记词](hd-wallets/mnemonic-seed.md) – 为你的 HD Wallets 生成对用户友好的 seed。
* [扩展密钥](hd-wallets/extended-keys.md) – 创建主扩展密钥，并从中派生子密钥。
* [派生路径](hd-wallets/derivation-paths.md) – 钱包用于组织密钥的常见层级结构。

## 资源

* <https://bitcointalk.org/index.php?topic=19137> – Gregory Maxwell 讨论关于确定性钱包的贴子
* <https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki> – Pieter Wuille 撰写的 BIP
* <https://iancoleman.io/bip39/> – 一个用于生成 HD Wallets 的优秀网页工具
* <https://github.com/lian/bitcoin-ruby/blob/master/lib/bitcoin/ext_key.rb> – Ruby 语言的简洁实现
* <https://www.youtube.com/watch?v=OVvue2dXkJo> – James Chiang 的演讲
* <https://www.cs.cornell.edu/~iddo/detwal.pdf> – Gregory Maxwell 关于确定性钱包的幻灯片
* <https://eprint.iacr.org/2014/998.pdf> – Gus Gutoski 和 Douglas Stebila 撰写的有趣论文
* [Hierarchical determinism: how Bitcoin's HD wallets are born](https://bennet.org/learn/hierarchical-determinism-how-bitcoin-hd-wallets-are-born/) – 带有交互式工具的 HD Wallets 介绍