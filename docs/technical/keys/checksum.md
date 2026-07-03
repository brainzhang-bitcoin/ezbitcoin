<img src="../../images/icons_loader-2.svg" alt="Loading Tool" style="height:32px; width:32px;" />

[<img src="../../images/diagrams_png_bytes-checksum.png" alt="Diagram showing how a checksum is used for detecting errors in data." width="544" height="140" />](https://static.learnmeabitcoin.com/diagrams/png/bytes-checksum.png)

校验和（checksum）是一小段数据，用于允许你检查另一段**数据是否与预期相符**。

它们最常见于[地址](/docs/technical/keys/address.md)中以检测拼写错误。这有助于防止将比特币发送到错误的地址。

随机示例

数据

你想要为其创建校验和的一些数据字节

`0 bytes`

校验和

[hash256](/docs/technical/cryptography/hash-function.md#hash256)(data) 的前 4 个字节

`Expected:`

带有校验和的数据

原数据后面附加校验和

`0 bytes`



0 secs

更准确地说，可以将校验和添加到某些数据的末尾，以创建组合的 `data+checksum`。

因此，当你稍后在其他地方重新输入这整段数据时，可以通过检查 `data` 是否仍与 `checksum` 匹配来确保一切正确：

[<img src="../../images/diagrams_png_bytes-checksum-valid.png" alt="Diagram showing some data with a valid checksum." width="650" height="200" />](https://static.learnmeabitcoin.com/diagrams/png/bytes-checksum-valid.png)

如果你犯了错误，`data` 将与 `checksum` 不匹配（反之亦然），系统会提醒你数据在某些方面是不正确的：

[<img src="../../images/diagrams_png_bytes-checksum-invalid.png" alt="Diagram showing some data with an invalid checksum." width="706" height="247" />](https://static.learnmeabitcoin.com/diagrams/png/bytes-checksum-invalid.png)

**这种类型的校验和无法用于错误 *纠正*。** 校验和只能 *检测* 错误，但无法告诉你错误在哪里，或者应该如何纠正它。

## 使用位置

校验和在比特币中用于哪些地方？

以下是比特币中使用校验和的几个示例：

* **[地址](/docs/technical/keys/address.md)** – 每个 Base58 地址（以 1 或 3 开头的地址）都包含一个校验和。这有助于防止在输入拼写错误时将比特币发送到错误地址而造成损失。
* **[WIF 私钥](/docs/technical/keys/private-key/wif.md)** – WIF 私钥是私钥的地址格式。这些也包含校验和，因此在将错误的私钥导入钱包时会收到通知。
* **[扩展密钥](/docs/technical/keys/hd-wallets/extended-keys.md)** – 每个扩展私钥和扩展公钥都包含其自己的校验和。这同样允许你在转录它们时检测错误。
* **[网络消息](/docs/technical/networking.md#messages)** – 在网络节点之间发送的每条消息都附带一个校验和。这使你能够检测消息在传输过程中是否被篡改或损坏。

现代 [Bech32](/docs/technical/keys/bech32.md) 地址也包含校验和，但它们比本页面介绍的简单校验和更为复杂。

## 创建

如何创建校验和？

[<img src="../../images/diagrams_png_bytes-checksum-create.png" alt="Diagram showing a checksum as the first 4 bytes of the HASH256 of some data." width="771" height="223" />](https://static.learnmeabitcoin.com/diagrams/png/bytes-checksum-create.png)

校验和是通过取**某些数据的 [HASH256](/docs/technical/cryptography/hash-function.md#hash256) 的前 4 个[字节](/docs/technical/general/bytes.md)**来创建的。

例如：

```
data          = aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
hash256(data) = 05c4de7c1069e9de703efd172e58c1919f48ae03910277a49c9afd7ded58bbeb
checksum      = 05c4de7c
```

<img src="../../images/icons_tool.svg" alt="Tool Icon" style="width:20px; height:20px" /> HASH256

随机交易数据

随机区块头

数据 (十六进制)

`0 bytes`


<img src="../../images/icons_hash-function.svg" alt="Hash Function Icon" style="width:52px; height:52px" />
SHA-256

<img src="../../images/icons_hash-function.svg" alt="Hash Function Icon" style="width:52px; height:52px" />
SHA-256

HASH256

SHA-256(SHA-256(data))

`0 bytes`



0 secs

```
# ---------
# Functions
# ---------

require 'digest'

# hash256 function (checksums use hash256)
def hash256(hex)
  binary = [hex].pack("H*")
  hash1 = Digest::SHA256.digest(binary)
  hash2 = Digest::SHA256.digest(hash1)
  result = hash2.unpack("H*")[0]
  return result
end

# checksum function
def checksum(hex)
  hash = hash256(hex) # Hash the data through SHA256 twice
  return hash[0...8]  # Return the first 4 bytes (8 characters)
end

# ---------------
# Create Checksum
# ---------------

# data
data = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

# checksum
puts checksum(data) #=> 05c4de7c
```

## 验证

如何验证校验和？

要验证校验和，你只需检查该数据哈希后的校验和是否与随数据一起提供的校验和相符。

换句话说，只需**重新计算校验和**：

```
# original data
data+checksum = aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa05c4de7c
data          = aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
checksum      = 05c4de7c

# checksum verification
hash256(data) = 05c4de7c1069e9de703efd172e58c1919f48ae03910277a49c9afd7ded58bbeb
checksum      = 05c4de7c <- it matches
```

这只是一个简单的示例，但该过程在整个比特币中都是相同的。

```
# ---------
# Functions
# ---------

require 'digest'

# hash256 function (checksums use hash256)
def hash256(hex)
  binary = [hex].pack("H*")
  hash1 = Digest::SHA256.digest(binary)
  hash2 = Digest::SHA256.digest(hash1)
  result = hash2.unpack("H*")[0]
  return result
end

# checksum function
def checksum(hex)
  hash = hash256(hex) # Hash the data through SHA256 twice
  return hash[0...8]  # Return the first 4 bytes (8 characters)
end

# ---------------
# Verify Checksum
# ---------------

# data+checksum
datachecksum = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa05c4de7c"

# data
data = datachecksum[0...40]

# checksum
checksum = datachecksum[40...48]

# verify
puts checksum(data) == checksum #=> true
```

## 可靠性

比特币中的校验和有多可靠？

校验和无法检测到错误的概率只有 **4,294,967,295 分之一**。

校验和的大小为 4 [字节](/docs/technical/general/bytes.md)。这意味着总共只有 0xFFFFFFFF (4,294,967,295) 种可能的校验和，因此两个不同的数据片段有可能具有相同的校验和。

换句话说，如果你在输入地址时犯了拼写错误，大约有**四十亿分之一**的几率导致生成的校验和意外地相同，从而**无法检测到该拼写错误**。

所以这极不可能，但并非不可能。

使用完整的 32 字节哈希结果作为校验和会更加可靠。然而，这会使地址变得更长，因此仅取前 4 个字节是在实用性与保持地址尽可能短之间取得了平衡。

## 术语

为什么叫“校验和”？

早期的校验和字面意思就是某些数据的“和（sum）”。例如，假设我想存储以下字符串：

```
abc
```

为了给它创建一个简单的校验和，我可以为每个字符指定一个数字（例如 a = 1, b = 2, c = 3），并将它们的总和加到末尾：

```
abc+6
```

如果我稍后在转录此字符串时犯了错误，像这样：

```
abb+6
```

校验和将不再与字符的总和匹配（`abb` = 1 + 2 + 2 = 5），我就会知道自己在某个地方犯了错误。因此，通过“检查（checking）”“总和（sum）”，我可以发现某些地方出错了。这就是“校验和（checksum）”这个名字的由来。

不过，在比特币中，我们实际上是使用[哈希函数](/docs/technical/cryptography/hash-function.md)来创建校验和，这比简单地对字符求和更可靠。尽管如此，它起到了相同的作用，所以我们仍然将这段额外的错误检测数据称为 *校验和*。

感谢 [Greg Maxwell](https://nt4tn.net/) 给我们上了一堂关于校验和（以及校验和历史）的快速计算机科学课。

## 总结

校验和是**检测拼写错误**的有用工具。

作为用户，知道像地址这样的内容包含校验和是件好事。因此，如果你在将地址输入钱包时犯了错误，基本上可以确定钱包会检测到任何错误，并阻止你将比特币发送到错误地址而导致它们永远丢失。

**最好将校验和视为后备安全网。** 任何时候都无法替代对地址的双重（或三重）检查。

作为开发者，如果某些内容包含校验和，你应该始终使用它来验证数据是否正确。这就是它们存在的作用。而且，如果你能挽救*一个人*免于丢失代币，那么编写校验和验证代码所花费的少量时间就是值得的。

校验和广泛应用于计算机科学中，它们对于简单的错误检测非常方便，因此也是你编程工具箱中一件很好用的工具。

## 资源

* [en.wikipedia.org/wiki/Checksum](https://en.wikipedia.org/wiki/Checksum)