# 闪电网络极速入门与 LND 初体验 (LND Quickstart)

比特币主网最为人诟病的一点便是交易吞吐量与确认延迟：全网每秒处理约 7 笔交易（TPS），等待 6 个区块的可信确认通常需要约 1 个小时，在网络拥堵时链上手续费更是难以支撑小额即时支付。

为了彻底突破这一瓶颈，社区在 2015 年提出了**闪电网络（Lightning Network）**——将海量高频的微支付搬到比特币区块链之外（链下）进行，仅在通道开启与最终结算时与主链交互。本章将帮助您快速建立对闪电网络的心智模型，并带您在测试网中搭建一个真正的 LND 节点，亲手体验第一笔秒级闪电支付。

---

## 1. 闪电网络的核心心智模型

如果两个参与方（Alice 和 Bob）之间存在频繁的资金往来，最自然的链下协作模型是什么？

1. **资金池（通道开启）**：双方共同在一笔链上 2/2 多重签名交易中存入一笔保证金（Funding Tx）。在通道关闭前，这笔保证金被锁定在链上。
2. **状态更新（链下结算）**：每次发生交易时，双方在本地协同更新资金分配比例并互相交换签名，同时作废上一版本的分配方案。这一过程无需广播上链，**只消耗网络带宽，能够实现每秒数十万笔的即时结算，手续费近乎为零**。
3. **最终轧账（通道关闭）**：当合作终止时，将最新的资金分配状态广播上链，主链矿工一次性为双方清算资金。

为了在无信任的环境下保证双方无法作恶，闪电网络构建了两大核心支柱协议：
* **RSMC（序列到期可撤销合约）**：解决了单条双向通道内的博弈惩罚与撤销机制，确保任何一方广播旧状态都会被对方全额没收资金。
* **HTLC（哈希时间锁合约）**：解决了跨节点支付路由问题。即便 Alice 和 Bob 之间没有直接建立通道，只要全网存在串联二者的中继节点，资金便能通过密码学原像哈希跨跳安全传递。

> 深入的密码学推导、交易结构与博弈论证明，请参阅下一专题：[核心机制深潜：深度图解 RSMC 与 HTLC](rsmc-and-htlc.md)。

---

## 2. 实战准备：运行 bitcoind 测试网全节点

闪电节点必须依附于一个比特币全节点来监听链上事件（如通道注资上链、对端违约广播等）。我们以 Testnet 测试网为例：

### 配置 `bitcoin.conf`
```ini
# ~/.bitcoin/bitcoin.conf
testnet=1
server=1
rest=1
rpcuser=testuser
rpcpassword=testpassword
rpcallowip=127.0.0.1
rpcport=18332

# LND 需要通过 ZeroMQ 实时接收新区块与新交易通知
zmqpubrawblock=tcp://127.0.0.1:28332
zmqpubrawtx=tcp://127.0.0.1:28333
```

启动 `bitcoind` 测试网服务：
```bash
bitcoind -daemon
```

---

## 3. 安装与启动 LND 闪电节点

[LND (Lightning Network Daemon)](https://github.com/lightningnetwork/lnd) 是目前最流行的 Go 语言闪电网络全功能节点实现。

### 1. 编译安装
```bash
# 确保本地已安装 Go 环境 (>= 1.16)
git clone https://github.com/lightningnetwork/lnd
cd lnd
make && make install
```

### 2. 启动 LND
```bash
lnd --bitcoin.active \
    --bitcoin.testnet \
    --bitcoin.node=bitcoind \
    --bitcoind.rpcuser=testuser \
    --bitcoind.rpcpass=testpassword \
    --bitcoind.zmqpubrawblock=tcp://127.0.0.1:28332 \
    --bitcoind.zmqpubrawtx=tcp://127.0.0.1:28333
```

---

## 4. 创建钱包、充值与通道连接

### 1. 创建钱包
在另一个终端中使用客户端命令行工具 `lncli`：
```bash
lncli --network=testnet create
```
根据提示设置钱包密码并妥善备份 24 个助记词。

### 2. 生成充值地址并获取测试币
```bash
lncli --network=testnet newaddress np2wkh
# 返回: tb1q... (测试网地址)
```
前往任意 Testnet 水龙头（Faucet）为该地址领取测试比特币，并等待几个区块确认后查看余额：
```bash
lncli --network=testnet walletbalance
```

### 3. 连接对端节点
前往闪电网络区块浏览器（如 [1ML](https://1ml.com/testnet/)）选取一个活跃的公网节点。例如连接目标公钥和 IP：
```bash
lncli --network=testnet connect 03a8334aba5660e241468e2f0deb2526bfd50d0e3fe808d882913e39094dc1a028@138.229.205.237:9735
```

### 4. 开启支付通道 (Open Channel)
向该节点存入 1,000,000 satoshi（0.01 BTC）作为本地通道容量：
```bash
lncli --network=testnet openchannel --node_key=03a8334aba5660e241468e2f0deb2526bfd50d0e3fe808d882913e39094dc1a028 --local_amt=1000000
```
该命令会在比特币主链上生成一笔注资交易（Funding Tx），在等待 3~6 个区块确认后，通道正式激活：
```bash
lncli --network=testnet listchannels
```

---

## 5. 完成你的第一笔闪电支付！

通道打开后，我们就可以脱离区块链、在毫秒级别完成支付。

1. **获取发票 (Invoice)**：在任何支持闪电支付的测试网网站（例如涂鸦画板 [Satoshi's Place](https://testnet.satoshis.place/)）购买像素，获得一段类似 `lntb...` 开头的发票编码。
2. **在命令行执行即时支付**：
```bash
lncli --network=testnet sendpayment --pay_req=lntb25480n1pwrn3czpp5em4jyjp85rfq5l...
```
指令执行后瞬间提示付款成功！无需矿工打包，没有繁冗等待，通道状态即时更新。

---

## 6. 闪电网络的现实考量与挑战

虽然体验惊艳，但在工程实践中闪电网络仍面临特有的权衡：
1. **热钱包安全与在线要求**：节点为了实时签名路由与撤销欺诈，私钥必须常驻内存；离线节点面临对端广播旧状态偷币的风险，因此衍生出了由第三方充当的**瞭望塔（Watchtower）**机制。
2. **路由寻路复杂度**：当网络规模扩大时，寻找具备足够余额的流动性路径是一个高维图搜索难题。
3. **入站容量（Inbound Capacity）问题**：刚建立通道的用户只能对外发款，却无法向他人收款，这促使了流动性市场与潜艇互换的诞生。

在下一节中，我们将深入其内部骨架，探寻 [RSMC 与 HTLC 的精妙博弈设计](rsmc-and-htlc.md)。
