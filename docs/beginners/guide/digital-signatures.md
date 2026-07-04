<img src="../../images/icons_loader-2.svg" alt="Loading Tool" style="height:32px; width:32px;" />

数字签名被用来展示你拥有与[公钥](public-keys.md)相关联的[私钥](private-keys.md)，**而无需透露该私钥**。

[<img src="../../images/beginners_guide_digital-signatures_01-digital-signature-usage.png" alt="展示数字签名如何由私钥创建并证明你是公钥拥有者的图表。" width="647" height="246" />](../../images/beginners_guide_digital-signatures_01-digital-signature-usage.png)

所以，如果有人问你是否拥有某个特定公钥（或[地址](../../technical/keys/address.md)）的私钥，你可以给他们一个数字签名来证明这一点。

## 为什么我们在比特币中使用数字签名？

当你进行[交易](transactions.md)时，你需要解锁你想花费的[输出](outputs.md)。

为此，你需要证明你“拥有”该输出。这可以通过证明你拥有该输出被[锁](locks.md)定的地址对应的私钥来实现：

[<img src="../../images/beginners_guide_digital-signatures_02-transaction-data.png" alt="展示包含带有锁的输入的交易数据图表。" width="487" height="102" />](../../images/beginners_guide_digital-signatures_02-transaction-data.png)

但是，如果你直接把私钥放入交易数据中，网络上的每个人都能够看到它：

[<img src="../../images/beginners_guide_digital-signatures_02-transaction-data-privkey.png" alt="展示包含直接使用私钥解锁的输入的交易数据图表。" width="637" height="337" />](../../images/beginners_guide_digital-signatures_02-transaction-data-privkey.png)

而如果任何人获得了你的私钥，他们就可以用它来解锁并花费锁定在相同地址下的任何其他输出。

那么，我们如何在不泄露私钥的情况下解锁输出呢？

### 数字签名登场

数字签名可以*由*私钥创建，以证明我们拥有该[地址](../../technical/keys/address.md)对应的私钥。

这意味着我们可以使用数字签名来解锁输出，而无需泄露我们的私钥：

[<img src="../../images/beginners_guide_digital-signatures_02-transaction-data-digsig.png" alt="展示包含使用数字签名解锁输入的交易数据图表。" width="683" height="392" />](../../images/beginners_guide_digital-signatures_02-transaction-data-digsig.png)

这就是为什么我们使用数字签名，而不是直接把私钥放入交易数据中的原因。

## 什么能防止别人重复使用数字签名？

好问题。毕竟，如果私钥能解锁锁定在某个地址下的任意输出，为什么别人不能把这个数字签名拿去用来做同样的事情呢？

答案：因为每个数字签名都与一笔特定的交易绑定。

换句话说：你不仅仅是使用你的私钥来生成数字签名，你使用的是你的私钥*以及*原始交易数据本身：

[<img src="../../images/beginners_guide_digital-signatures_03-digital-signature-components.png" alt="展示数字签名如何使用私钥和交易数据创建的图表。" width="451" height="153" />](../../images/beginners_guide_digital-signatures_03-digital-signature-components.png)

因此，每个数字签名都与它正在使用的交易*相连*：

[<img src="../../images/beginners_guide_digital-signatures_03-digital-signature-environment.png" alt="展示数字签名如何与正在使用的交易数据相绑定的图表。" width="397" height="94" />](../../images/beginners_guide_digital-signatures_03-digital-signature-environment.png)

所以如果有人尝试在不同的交易中使用这个数字签名，它将与用于生成它的原始交易数据不匹配，[比特币网络](network.md)上的[节点](node.md)将会拒绝它。

[<img src="../../images/beginners_guide_digital-signatures_03-digital-signature-environment-different.png" alt="展示数字签名必须包含在用于创建它的相同交易数据中才有效的图表。" width="665" height="422" />](../../images/beginners_guide_digital-signatures_03-digital-signature-environment-different.png)

此外，数字签名还能防止任何人篡改交易。因为如果交易数据被更改（例如有人企图更改发送的金额或发送的目的地），数字签名将不再起作用。

## 数字签名是如何工作的？

数学，纯粹的数学。

使用数字签名有两个部分：

1. **签名 (Signing)：** 你将私钥 + `交易数据`结合，并使用一些数学方法来生成数字签名。
2. **验证 (Verifying)：** 然后你可以把数字签名 + `交易数据` + 公钥拿来进行另外一些数学计算，结果将证实是否使用了合法的私钥来创建该数字签名。

因为请记住，**使用数字签名的目标是证明你是公钥的拥有者**。

不要忘记地址只是公钥的编码形式。所以即使你把比特币发送到一个地址，你实际上是将它们锁定到一个公钥上。

我知道这个过程一开始看起来像是魔法，但实际上在它底层只是数学。

## 你如何生成数字签名？

数字签名包含两个部分：

1. 一个**随机**部分。
2. 一个**签名**部分。

### 1. 随机部分

首先生成一个很大的随机数。

然后，你将此随机数与椭圆曲线上的生成点（也就是在生成[公钥](public-keys.md)时所使用的相同生成点）相乘：

[<img src="../../images/beginners_guide_digital-signatures_04-signing-random-point.png" alt="展示生成点与一个大随机数相乘的图表。" width="663" height="238" />](../../images/beginners_guide_digital-signatures_04-signing-random-point.png)

我们得到的数字签名中的**随机**部分，就是曲线上的那个点。但我们只需要取它的 x 坐标值：

[<img src="../../images/beginners_guide_digital-signatures_04-signing-random-point-x.png" alt="展示从曲线上随机点提取 x 坐标的图表。" width="238" height="299" />](../../images/beginners_guide_digital-signatures_04-signing-random-point-x.png)

我们简称为 `r`。

[<img src="../../images/beginners_guide_digital-signatures_04-signing-random-r.png" alt="展示 r (随机点的 x 坐标) 作为数字签名第一部分的图表。" width="78" height="140" />](../../images/beginners_guide_digital-signatures_04-signing-random-r.png)

* 这基本上与生成私钥和公钥的过程相同。只不过在这里，我们这样做是为了在我们的数字签名中加入一个随机元素。
* 这个随机元素有助于确保每个数字签名都是唯一的。

现在我们已经准备好了数字签名的*第一部分*，但我们还没有把私钥用在任何地方。这就是第二部分起作用的地方……

### 2. 签名部分

接下来，我们使用我们的私钥，并乘以 `r`（也就是我们刚刚找到的曲线上的那个随机点的 x 坐标）。

[<img src="../../images/beginners_guide_digital-signatures_04-signing-signature-r-privkey.png" alt="展示 r 与私钥相乘的图表。" width="229" height="134" />](../../images/beginners_guide_digital-signatures_04-signing-signature-r-privkey.png)

接着，我们加上*我们要签名的内容*。这被称为 `message`（消息）。在比特币中，这个 `message` 就是包含我们想要解锁的输出的整个交易数据的哈希值：

[<img src="../../images/beginners_guide_digital-signatures_04-signing-signature-r-privkey-thing.png" alt="展示我们要签名的消息被加到（r 乘以私钥）上的图表。" width="429" height="198" />](../../images/beginners_guide_digital-signatures_04-signing-signature-r-privkey-thing.png)

包含交易哈希会将签名绑定到某一笔特定交易上（这样它就不能被用于其他不同的交易中）。

最后，为了达到效果，我们把所有这些除以我们最开始生成的那个初始随机数：

[<img src="../../images/beginners_guide_digital-signatures_04-signing-signature-r-privkey-thing-randnum.png" alt="展示签名的随机部分除以 r 的图表。" width="443" height="155" />](../../images/beginners_guide_digital-signatures_04-signing-signature-r-privkey-thing-randnum.png)

好了！我们就得到了数字签名中至关重要的“签名”部分。我们简称为 `s`。

[<img src="../../images/beginners_guide_digital-signatures_04-signing-signature-rs.png" alt="展示作为数字签名两个部分的 r 和 s 的图表。" width="169" height="140" />](../../images/beginners_guide_digital-signatures_04-signing-signature-rs.png)

数字签名先生。

这整个签名随后会被放入交易的[解锁代码](../../technical/transaction/input/scriptsig.md)部分中：

[<img src="../../images/beginners_guide_digital-signatures_05-verifying-goal.png" alt="展示数字签名在交易内部大概位置的图表。" width="515" height="189" />](../../images/beginners_guide_digital-signatures_05-verifying-goal.png)

注意：我们用来创建签名的私钥是与输出锁定的公钥相关联的那一个。

现在有趣的地方来了……

如果有人要求我们证明我们拥有某个公钥对应的私钥，我们可以向他们提供我们的数字签名（`r` 和 `s`）作为证明。

但是，别人究竟该如何利用这个作为证明呢？

## 你如何验证数字签名？

要验证一个数字签名是否由正确的私钥创建，你向其提供该数字签名的对象需要使用这两个部分在椭圆曲线上找到**两个新点**：

### 点 1

将 `message`（消息）除以 `s`。第一个点就是**生成点**乘以这个值：

[<img src="../../images/beginners_guide_digital-signatures_05-verifying-point1.png" alt="展示签名验证期间椭圆曲线上的点 1 的图表。" width="482" height="223" />](../../images/beginners_guide_digital-signatures_05-verifying-point1.png)

### 点 2

将 `r` 除以 `s`。第二个点就是公钥乘以这个值：

[<img src="../../images/beginners_guide_digital-signatures_05-verifying-point2.png" alt="展示签名验证期间椭圆曲线上的点 2 的图表。" width="482" height="233" />](../../images/beginners_guide_digital-signatures_05-verifying-point2.png)

### 验证

现在如果我们把这两个点加在一起，我们将在曲线上得到*第三个*点：

[<img src="../../images/beginners_guide_digital-signatures_05-verifying-add.png" alt="展示在椭圆曲线上将点 1 和点 2 相加结果的图表。" width="238" height="248" />](../../images/beginners_guide_digital-signatures_05-verifying-add.png)

如果这第三个点的 x 坐标与我们开始时的那个随机点的 x 坐标（也就是 `r`）相同，那么这就是该数字签名确实是使用与该公钥相关联的私钥所生成的证明。

[<img src="../../images/beginners_guide_digital-signatures_05-verifying-final.png" alt="展示点 3 的 x 坐标等于签名中随机点 x 坐标的图表。" width="577" height="340" />](../../images/beginners_guide_digital-signatures_05-verifying-final.png)

**这是对数字签名所涉数学原理的简化解释。** 更技术性的解释请参阅 [ECDSA](../../technical/cryptography/elliptic-curve/ecdsa.md)。

## 资源

* [Bitcoin 101: The Magic of Signing & Verifying](https://www.youtube.com/watch?v=U2bw_N6kQL8) – 极好的入门视频，涵盖了签名生成与验证的实际数学细节。