# 闪电网络节点搭建与配置小抄 (Node Setup Cheat Sheet)

本小抄整理了运营闪电网络节点最核心的配置模板与常用运维指令，覆盖 **Bitcoin Core**、**LND** 以及 **Core Lightning (CLN)**。

---

## 1. Bitcoin Core 节点配合配置

### `bitcoin.conf` 核心配置模板
```ini
# ~/.bitcoin/bitcoin.conf
testnet=1
server=1
rest=1
rpcuser=user
rpcpassword=password
rpcallowip=127.0.0.1
rpcport=18332
test.rpcport=18332
rpcthreads=10

# ZeroMQ 通知（闪电节点监听新区块与新交易必需）
zmqpubrawblock=tcp://127.0.0.1:28332
zmqpubrawtx=tcp://127.0.0.1:28333
```

### 节点启停与查询
```bash
# 启动守护进程
bitcoind -daemon --conf=/opt/bitcoin/blockdata/bitcoin.conf --datadir=/opt/bitcoin/blockdata/

# 查询同步状态与钱包信息
bitcoin-cli getblockchaininfo
bitcoin-cli getwalletinfo
```

---

## 2. LND (Lightning Network Daemon)

[LND](https://github.com/lightningnetwork/lnd) 是目前最流行的 Go 语言闪电节点实现，提供丰富的 gRPC 与 REST 接口。

### 启动 LND
```bash
lnd --bitcoin.active \
    --bitcoin.testnet \
    --debuglevel=debug \
    --bitcoin.node=bitcoind \
    --bitcoind.rpcuser=user \
    --bitcoind.rpcpass=password \
    --bitcoind.zmqpubrawblock=tcp://127.0.0.1:28332 \
    --bitcoind.zmqpubrawtx=tcp://127.0.0.1:28333 \
    --listen=0.0.0.0:9735 \
    --externalip=x.x.x.x:9735
```

### `lncli` 常用运维指令
```bash
# 解锁钱包
lncli --network=testnet unlock

# 获取收款地址 (原生隔离见证)
lncli --network=testnet newaddress p2wkh

# 查看钱包链上余额与通道余额
lncli --network=testnet walletbalance
lncli --network=testnet channelbalance

# 连接对端节点
lncli --network=testnet connect <pubkey>@<ip>:9735

# 开启通道 (存入 100,000 satoshi)
lncli --network=testnet openchannel --node_key <pubkey> --local_amt 100000

# 查看当前活跃通道
lncli --network=testnet listchannels

# 发送闪电支付 (向 BOLT11 发票付款)
lncli --network=testnet sendpayment --pay_req <invoice_string>

# 生成收款发票 (金额 100,000 satoshi)
lncli --network=testnet addinvoice --memo "test invoice" --amt 100000

# 协作关闭通道
lncli --network=testnet closechannel <channel_point>
```

---

## 3. Core Lightning (CLN)

[Core Lightning](https://github.com/ElementsProject/lightning)（原 c-lightning）由 Blockstream 维护，采用 C 语言编写，性能优异且资源占用极低。

### Systemd 服务配置模板 (`/etc/systemd/system/lightning.service`)
```ini
[Unit]
Description=Core Lightning daemon
After=network.target bitcoind.service

[Service]
ExecStart=/usr/bin/lightningd --pid-file=/root/.lightning/lightning.pid --daemon
PIDFile=/root/.lightning/lightning.pid
User=root
Type=forking
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

### 配置文件 `~/.lightning/config`
```ini
alias=ezbitcoin_node
log-level=debug
network=testnet
bitcoin-rpcuser=user
bitcoin-rpcpassword=password
bitcoin-rpcconnect=127.0.0.1
bitcoin-rpcport=18332
log-file=/var/log/lightning.log
bind-addr=0.0.0.0:9735
announce-addr=x.x.x.x:9735
```

### `lightning-cli` 常用指令
```bash
# 获取新地址
lightning-cli newaddr

# 连接公网节点
lightning-cli connect <pubkey>@<ip>:9735

# 注资开启通道
lightning-cli fundchannel <node_id> <amount_satoshi>

# 查看资金池概况
lightning-cli listfunds

# 支付发票
lightning-cli pay <bolt11_invoice>

# 创建发票 (金额单位 millisatoshi)
lightning-cli invoice <msatoshi> <label> <description>
```

---

## 4. 搭配 Lightning Charge 搭建微支付网关

[Lightning Charge](https://github.com/ElementsProject/lightning-charge) 是为 Core Lightning 提供的开箱即用 REST API 收银网关，适合电商网站集成：

```bash
docker run -d --name lightning-charge \
  -v /data/lightning:/data \
  -p 9112:9112 \
  -e API_TOKEN=mySecretToken \
  -e NETWORK=testnet \
  -e BITCOIND_URI="http://user:password@127.0.0.1:18332" \
  shesek/lightning-charge
```

健康检查：
```bash
curl http://api-token:mySecretToken@localhost:9112/info
```
