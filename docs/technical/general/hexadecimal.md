<img src="../../images/icons_loader-2.svg" alt="Loading Tool" style="height:32px; width:32px;" />

[<img src="../../images/diagrams_png_numbers-hexadecimal-key.png" alt="Table showing hexadecimal numbers with corresponding decimal numbers." width="779" height="79" />](https://static.learnmeabitcoin.com/diagrams/png/numbers-hexadecimal-key.png)

十六进制数字系统使用**数字 0-9 和字母 A-F** 来表示 **0-15** 的数字。

简单来说，十六进制系统（16 个符号）是十进制系统（10 个符号）的扩展。这意味着你只需用一个符号就能表示 0 到 15 之间的数字。

该系统非常适合表示[字节](/docs/technical/general/bytes.md)，因为半个字节有 16 种不同的组合，因此可以用两个十六进制符号来表示一个完整的字节。这就是为什么在比特币中你会看到很多数据（例如[私钥](/docs/technical/keys/private-key.md)、[交易](/docs/technical/transaction.md)）都以十六进制形式呈现。

十六进制中的字母**大小写均可**，没有区别（例如 1337af 与 1337AF 相同）。

Hexa = 6，Deci = 10。因此 *hexadeci*mal 表示该数字系统共有 16 个不同的字符。

Binary (Base 2)

0b

`0 digits`

Decimal (Base 10)

0d

`0 digits`

Hexadecimal (Base 16)

0x

`0 digits`



+1



0 secs

## 数字前缀

我们使用前缀来标识十六进制、十进制和二进制数字。

* 0x = 十六进制
* 0d = 十进制
* 0b = 二进制

例如：

* 0x100 = 256
* 0d100 = 100
* 0b100 = 4

通常不会用 0d 给十进制数字加前缀（除非确实有意义）。所以如果你看到 100，可以直接认为它是一百。

## 十六进制转十进制

[<img src="../../images/diagrams_png_numbers-hexadecimal-decimal-conversion.png" alt="Diagram showing how to convert hexadecimal to decimal." width="768" height="181" />](https://static.learnmeabitcoin.com/diagrams/png/numbers-hexadecimal-decimal-conversion.png)

要将十六进制转换为十进制，需要将每个字符乘以 16 的递增幂次。

1. 将每个十六进制符号转换为对应的十进制值。
2. 将这些十进制值（从最小到最大）分别乘以 16 的递增幂次（例如 16⁰、16¹、16²、16³ 等）。
3. 将所有结果相加，即可得到最终的十进制值。

例如：

```
Hexadecimal = 02A13B

B = 11 * 160 = 11
3 = 3  * 161 = 48
1 = 1  * 162 = 256
A = 10 * 163 = 40960
2 = 2  * 164 = 131072
0 = 0  * 165 = 0

Decimal = 0 + 131072 + 40960 + 256 + 48 + 11 = 172347
```

这听起来有点复杂，但其实和十进制系统的原理完全相同。十进制中每个数位对应 10 的递增幂次（因为十进制有 10 个数字，即"base 10"）。例如，数字 123 表示 (1 × 10²) + (2 × 10¹) + (3 × 10⁰)，即"一个百、两个十、三个一"。

任何数字的零次幂等于 1，例如 10⁰ = 1，16⁰ = 1。

你不必在脑海中进行十六进制到十进制的转换，但要记住：你看到十六进制数字和字母时，本质上还是在看数字。

**[Little-Endian](/docs/technical/general/little-endian.md)。** 比特币数据中大多数字段里存储的整数（例如 [vout](/docs/technical/transaction.md#structure-inputs-vout)、[amount](/docs/technical/transaction.md#structure-outputs-amount)）都采用*小端序*（字节顺序相反），因此在转换为十进制之前需要先颠倒字节顺序。

### 代码示例

在任何主流编程语言中都可以将十六进制字符串转换为十进制。通常有内置函数可以轻松完成，无需手动计算。

```
# hexadecimal to decimal
puts "02A13B".to_i(16) #=> 172347
```

```
# hexadecimal to decimal
echo "ibase=16; 02A13B" | bc #=> 172347
```

## 十进制转十六进制

[<img src="../../images/diagrams_png_numbers-decimal-hexadecimal-conversion.png" alt="Diagram showing how to convert decimal to hexadecimal." width="620" height="344" />](https://static.learnmeabitcoin.com/diagrams/png/numbers-decimal-hexadecimal-conversion.png)

要将十进制转换为十六进制，只需持续除以 16 即可。

每次除法的*余数*对应一个十六进制字符（从最小到最大）。然后取每次除法的商继续进行，直到商为零为止。

例如：

```
Decimal = 6735

6735 / 16 = 420 (remainder 15)
 420 / 16 =  26 (remainder  4)
  26 / 16 =   1 (remainder 10)
   1 / 16 =   0 (remainder  1)

Hexadecimal = 1A4F
```

**取模运算。** 取模运算符（%）返回除法后的*余数*。

### 代码示例

```
# decimal to hexadecimal
puts 6735.to_s(16) #=> 1a4f
```

```
# decimal to hexadecimal
echo "obase=16; 6735" | bc #=> 1A4F
```

## [字节](/docs/technical/general/bytes.md)

十六进制有什么用？

[<img src="../../images/diagrams_png_bytes-hexadecimal.png" alt="Diagram showing bytes of data represented in binary, decimal, and hexadecimal." width="772" height="223" />](https://static.learnmeabitcoin.com/diagrams/png/bytes-hexadecimal.png)

在处理比特币的原始数据时，你会频繁遇到十六进制字符。例如，下面是一个随机私钥：

```
b97bb553a077ee8bc49337a4e920ff0535ac2e8a00e22c26660d38663da3b6b6
```

这个私钥代表 32 字节的数据。

为什么用十六进制来表示字节？因为半个字节有 16 种可能的组合，而十六进制恰好有 16 个字符。因此，可以用一个十六进制字符表示半个字节，用两个十六进制字符表示一个完整的字节。

这简直是计算领域天作之合。

Binary

Byte

0

0

0

0

0

0

0

0

Hexadecimal

`0`
`0`

提示：*最低位*在右边 →

提示：半个字节称为"nibble"（半字节），但这对比特币来说并不重要。

例如，与其用二进制显示所有八个[位](/docs/technical/general/bytes.md#bit)（如 `10110101`），不如用两个十六进制字符 `B5` 来缩写（因为 `1011` = `B`，`0101` = `5`）。

所以简而言之，十六进制系统是一种用于显示原始字节数据的*便捷*系统。

## 参考资料

* [Practical Guide to Binary, Decimal and Hexadecimal Numbers](https://web.archive.org/web/20170628180513/http://www.myhome.org/pg/numbers.html)
* [A Brief Explanation of Hexadecimal Numbers](https://tseggleston.com/hex-numbers/)