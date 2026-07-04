<img src="../../images/icons_loader-2.svg" alt="Loading Tool" style="height:32px; width:32px;" />

[<img src="../../images/diagrams_png_keys-private-key.png" alt="Diagram showing a private key as a random number." width="316" height="102" />](../../images/diagrams_png_keys-private-key.png)

A private key is a very large **random number**.

It's used as the source for creating a [public key](public-key.md).

Generate Random
Reset


Bits

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

二进制 (Binary)

0b

`0 bits`

十进制 (Decimal)

0d

十六进制 (Hexadecimal)

0x

`0 bytes`






**切勿使用由网站生成的私钥，或在网站中输入你的私钥。** 网站很容易保存私钥并利用它窃取你的比特币。

0 secs

## 生成

如何创建一个私钥？

要创建私钥，你只需要**生成一个随机的 256-[位](../general/bytes.md#bit)数字**[\*](#range)。

生成私钥的关键部分是使用*可靠*的随机源。如果你使用的是 Linux，一个可靠的随机源是 [/dev/urandom](https://linux.die.net/man/4/urandom)：

```
# generate 256 bits of random data
urandom = File.open("/dev/urandom")    # urandom is a "file"
bytes = urandom.read(32)               # read 32 bytes from it (256 bits)
privatekey = bytes.unpack("H*")[0]     # the data is binary, so unpack it to hexadecimal

# print the private key
puts privatekey
```

### 私钥范围

一个有效的私钥是处于（并包括）以下范围内的任何数字：

```
min: 1
max: 115792089237316195423570985008687907852837564279074904382605163141518161494336
```

该最大值为 `n-1`，其中 [`n`](../cryptography/elliptic-curve.md#parameters-n) 是比特币中使用的[椭圆曲线](../cryptography/elliptic-curve.md)（*secp256k1*）上的点数。这比 256 位数字的最大值稍小一些。

因此，如果你在生成一个随机的 256 位（32-[字节](../general/bytes.md)）数字，你会想要在开始使用它之前检查它没有超出最大值。

### 密码学安全的随机数

编程语言中的默认随机数函数对于生成私钥来说通常是不够安全的。

大多数语言中的标准 "`rand()`" 函数只是生成“看起来随机”数字的快速简便方法，但对于加密目的（例如生成私钥）来说，它们不够随机。

例如：

```
# simple random number (do not use for generating private keys)
puts rand(1..115792089237316195423570985008687907852837564279074904382605163141518161494336)

# cryptographically secure random number (can use for generating private keys)
require 'securerandom'
puts SecureRandom.random_number(1..115792089237316195423570985008687907852837564279074904382605163141518161494336)

# NOTE: These random number functions include the given minimum and maximum values as part of the range of possible results.
```

因此，无论你使用的是什么编程语言，都要确保搜索如何生成“密码学安全的随机数”以找出你应该使用哪个函数（而不是你可能熟悉的默认函数）。

例如，[libbitcoin](https://github.com/libbitcoin) 库（特别是 `bx seed` 命令行工具）在 2023 年由于没有使用密码学安全的随机数来生成[助记词](hd-wallets/mnemonic-seed.md)，导致了价值超过 900,000 美元的比特币丢失。有关发生的事情以及原因的完整说明，请参阅 [Milk Sad](https://milksad.info/disclosure.html)。

有时生成*随机字节*比生成随机数更容易。所以你可以直接生成 32 个随机字节，然后将其用作你的私钥，因为这等同于生成一个 256 位数字。

如果你使用的是 Linux，安全的随机数通常源自 /dev/urandom，因此直接从该源获取你的字节更为直接。

## 格式

私钥看起来像什么？

生成

### 十进制

私钥归根结底只是一个随机数，因此将其存储为十进制数是完全没有问题的。例如：

### 十六进制（最常见）

在教程和网站上，你通常会看到原始私钥显示为 32 字节的[十六进制](../general/hexadecimal.md)字符串。例如：

这与**随机数是相同的**，只是不同的显示方式（使用十六进制数字代替十进制数字）。

<img src="../../images/icons_tool.svg" alt="Tool Icon" style="width:20px; height:20px" /> 进制转换器 (Number Converter)

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

### WIF (钱包导入格式)

为了方便起见，私钥可以转换为 [WIF](private-key/wif.md)（Wallet Import Format）。例如：

这就像私钥的[地址](address.md)格式。有时在将私钥导入钱包（例如 [Electrum](https://electrum.org/)）时会用到它。

生成随机


前缀`1 byte`

网络

 主网
 测试网

私钥`0 bytes`

压缩`1 byte`

已压缩

 是 (默认)
 否

校验和`0 bytes`

WIF 私钥

以上数据的 Base58 编码

`0 characters`



**切勿在网站中输入你的私钥，或使用由网站生成的私钥。** 网站很容易保存私钥并利用它窃取你的比特币。

0 secs

## 使用

私钥在比特币中是如何使用的？

[<img src="../../images/diagrams_png_keys.png" alt="Diagram showing how a private key is used to create a public key and signatures, and how they're used to lock and unlock bitcoins in transactions." width="696" height="378" />](../../images/diagrams_png_keys.png)

私钥是计算公钥的起点。

私钥还用于生成[签名](signature.md)，并且这些签名与公钥有数学上的联系。这些数学联系正是你在进行[交易](../transaction.md)时能够[锁定](../transaction/output/scriptpubkey.md)和[解锁](../transaction/input/scriptsig.md)比特币的原因。

私钥本身不会公开发现在[区块链](../blockchain.md)中。私钥的目的是为了保持私密（因此得名），因此它们应该安全地存储在你的计算机上，并且只在生成签名以解锁比特币时使用（这就是当你进行交易时[比特币钱包](../../beginners/wallets.md)所做的事情）。

## 安全性

私钥有多安全？

*切勿* 泄露你的私钥。

阻止他人窃取你比特币的唯一方法就是他们无法猜出或随机生成与你相同的私钥。

可能生成的私钥范围（“密钥空间”）是如此难以想象的巨大，以至于**两个不同的人/计算机生成相同私钥的情况实际上是不可能的**（只要它们是安全地生成的）。

这可能很难让人相信，但为了给你一些直观的感受，大约有 2^256 或 10^77 种可能的私钥，而宇宙中大约有 10^78 个原子 [[1]](#fn1)。因此，这就像让两个不同的人随机选择宇宙中的一个原子，并且两个人都选择完全相同的一个。

```
# number of private keys (roughly)
10^77 = 100000000000000000000000000000000000000000000000000000000000000000000000000000

# number of atoms in the universe (roughly)
10^78 = 1000000000000000000000000000000000000000000000000000000000000000000000000000000
```

换句话说，这就像两个人从地球上的任何地方选择同一粒沙子 (10^18) [[2]](#fn2)。只是每一粒沙子都包含另一个地球那么多的沙子，而那些沙子中的每一粒又包含另一个地球那么多的沙子，依此类推，递归 4 次。

即便如此，沙子的总数量依然远远少于可能的私钥总数。

```
# grains of sand on the earth (roughly)
10^18 = 1000000000000000000

# grains of sand on the earth where each grain of sand contains an earth of sand (4 times recursively)
10^18 * 10^18 * 10^18 * 10^18 
= 1000000000000000000000000000000000000000000000000000000000000000000000000
```

所以你可以看到，我们很难想象这个数字有多大。

无论如何，这个故事的启示就是你**绝对不要在网站中输入你的私钥**，也不要把它留在别人可能接触到的地方；因为这是别人发现你私钥的唯一途径。

[keys.lol](https://keys.lol) 是一个有趣的网站，允许你浏览现存的每一个可能的私钥。除了那些过去用过、明显不安全的小数字私钥外，祝你好运能找到一个真正随机且有余额的私钥。

## 总结

如果你可以在计算机上安全地生成随机数，你就可以生成你自己的私钥。

不过，最关键（键）的是要弄清楚如何生成*密码学安全*的随机数，因此值得花时间在选定的编程语言中学会如何正确地实现。因为如果你的随机数不够随机，你将会失去比特币。

但不要因此而退缩。我相信许多指南都会建议不要生成自己的私钥，但那只是因为他们不想为你犯的任何错误负责。但如果你很小心并学会了如何正确操作，如果你想的话，自己生成私钥也没什么不可以的。而且，凡事总要有个开始。

我在进行测试交易时经常这么做，并且从未遇到过问题。

另外，能够生成自己的密钥并向其发送比特币是件很酷的事情。而且，如果你对编写比特币程序感兴趣，生成自己的私钥是一个很好的起点。

祝你好运。

我使用钱包来存储我的比特币。这比生成和管理单个私钥要容易得多。

### 感谢

* **David Plotz** – 指出了我关于私钥最大值的复制粘贴错误。David 有一个很酷的网站，提供实用的 [Excel spreadsheets for Bitcoin](https://www.modulo.network/)。).