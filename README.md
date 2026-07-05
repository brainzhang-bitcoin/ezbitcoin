# EzBitcoin - 比特币入门

这个项目面向有一定计算机基础，对比特币技术好奇的读者，用尽可能通俗易懂的介绍比特币是如何工作的；里面的部分材料包含来自知名 Bitcoin 极简图解教学网站 [Learn Me A Bitcoin](https://learnmeabitcoin.com/) ，部分材料来自于[作者的blog历史文章](https://brainz.fun/blog/categories/blockchain/);

---

## 📚 文档目录 (Table of Contents)

### 🟢 1. 新手指南 (Beginners Guide)
适合完全没有技术背景的读者，用极简非技术语言介绍比特币基本概念。

*   **[新手导读及概览](docs/beginners.md)**
*   **[比特币是如何工作的？](docs/beginners/how-does-bitcoin-work.md)**
*   **[如何选择钱包 (Wallets)](docs/beginners/wallets.md)**
*   **[如何选择交易平台 (Exchanges)](docs/beginners/exchanges.md)**
*   **[如何发送与接收比特币 (Sending)](docs/beginners/sending.md)**
*   **[安全与存储防范 (Security)](docs/beginners/security.md)**
*   **📖 新手极简图解手册 (Beginners Short Guide)**
    *   [比特币网络 (Network)](docs/beginners/guide/network.md)
    *   [节点 (Node)](docs/beginners/guide/node.md)
    *   [挖矿 (Mining)](docs/beginners/guide/mining.md)
    *   [区块链 (Blockchain)](docs/beginners/guide/blockchain.md)
    *   [区块 (Blocks)](docs/beginners/guide/blocks.md)
    *   [难度 (Difficulty)](docs/beginners/guide/difficulty.md)
    *   [交易 (Transactions)](docs/beginners/guide/transactions.md)
    *   [交易输出 (Outputs)](docs/beginners/guide/outputs.md)
    *   [锁定与解锁 (Locks)](docs/beginners/guide/locks.md)
    *   [密钥与地址 (Keys & Addresses)](docs/beginners/guide/keys-addresses.md)
    *   [私钥 (Private Keys)](docs/beginners/guide/private-keys.md)
    *   [公钥 (Public Keys)](docs/beginners/guide/public-keys.md)
    *   [数字签名 (Digital Signatures)](docs/beginners/guide/digital-signatures.md)
    *   [隔离见证 (SegWit)](docs/beginners/guide/segwit.md)
*   **💡 推荐科普博文 (Blog Articles)**
    *   [澳本聪是中本聪吗？(二)](docs/beginners/is-craig-wright-real-satoshi-part2.md)
    *   [祝比特币10岁生日快乐](docs/beginners/happy-10th-birthday-bitcoin.md)

---

### 🔵 2. 技术指南 (Technical Guide)
适合想要深入理解比特币底层协议、密码学及进行比特币编程开发的读者。

*   **[技术指南导读主页](docs/technical.md)**

#### 📦 区块与区块链 (Blocks & Blockchain)
*   **[区块总览 (Block)](docs/technical/block.md)**
    *   [区块哈希值 (Hash)](docs/technical/block/hash.md)
    *   [前一区块哈希 (Previous Block)](docs/technical/block/previous-block.md)
    *   [默克尔根 (Merkle Root)](docs/technical/block/merkle-root.md)
    *   [时间戳 (Time)](docs/technical/block/time.md)
    *   [难度目标 Bits (Bits)](docs/technical/block/bits.md)
    *   [随机数 Nonce (Nonce)](docs/technical/block/nonce.md)
    *   [版本号 Version (Version)](docs/technical/block/version.md)
    *   [blk.dat 数据文件结构](docs/technical/block/blkdat.md)
*   **[区块链总览 (Blockchain)](docs/technical/blockchain.md)**
    *   [比特币的 Blockchain - Part 1](docs/technical/blockchain/bitcoin-blockchain-part1.md)
    *   [比特币的 Blockchain - Part 2](docs/technical/blockchain/bitcoin-blockchain-part2.md)
    *   [区块高度 (Height)](docs/technical/blockchain/height.md)
    *   [最长链原则 (Longest Chain)](docs/technical/blockchain/longest-chain.md)
    *   [51% 攻击 (51% Attack)](docs/technical/blockchain/51-attack.md)
    *   [硬分叉 (Hard Fork)](docs/technical/blockchain/hard-fork.md)
    *   [软分叉 (Soft Fork)](docs/technical/blockchain/soft-fork.md)

#### 🔐 密码学 (Cryptography)
*   **[密码学总览 (Cryptography)](docs/technical/cryptography.md)**
    *   [哈希函数 (Hash Function)](docs/technical/cryptography/hash-function.md)
    *   [椭圆曲线 (Elliptic Curve)](docs/technical/cryptography/elliptic-curve.md)
    *   [ECDSA 签名算法](docs/technical/cryptography/elliptic-curve/ecdsa.md)
    *   [Schnorr 签名算法](docs/technical/cryptography/elliptic-curve/schnorr.md)

#### 🔑 密钥、签名与地址 (Keys, Signatures & Addresses)
*   **[密钥总览 (Keys)](docs/technical/keys.md)**
    *   [私钥 (Private Key)](docs/technical/keys/private-key.md)
    *   [WIF 格式私钥 (WIF)](docs/technical/keys/private-key/wif.md)
    *   [公钥 (Public Key)](docs/technical/keys/public-key.md)
    *   [公钥哈希 (Public Key Hash)](docs/technical/keys/public-key/hash.md)
    *   [数字签名 (Signature)](docs/technical/keys/signature.md)
    *   [比特币地址 (Address)](docs/technical/keys/address.md)
    *   [Base58 校验和 (Checksum)](docs/technical/keys/checksum.md)
    *   [Bech32 格式编码 (Bech32)](docs/technical/keys/bech32.md)
    *   [HD 层次确定性钱包 (HD Wallets)](docs/technical/keys/hd-wallets.md)
        *   [助记词种子 (Mnemonic Seed)](docs/technical/keys/hd-wallets/mnemonic-seed.md)
        *   [扩展密钥 (Extended Keys)](docs/technical/keys/hd-wallets/extended-keys.md)
        *   [派生路径 (Derivation Paths)](docs/technical/keys/hd-wallets/derivation-paths.md)

#### 💸 比特币交易 (Transactions)
*   **[交易总览 (Transaction)](docs/technical/transaction.md)**
    *   [比特币的交易 - Part 5](docs/technical/transaction/bitcoin-transaction-part5.md)
    *   [比特币的交易 - Part 6](docs/technical/transaction/bitcoin-transaction-part6.md)
    *   [未花费交易输出 (UTXO)](docs/technical/transaction/utxo.md)
    *   [交易输入 (Input)](docs/technical/transaction/input.md)
        *   [ScriptSig 解锁脚本](docs/technical/transaction/input/scriptsig.md)
        *   [Sequence 序列号](docs/technical/transaction/input/sequence.md)
        *   [Vout 输出索引](docs/technical/transaction/input/vout.md)
    *   [交易输出 (Output)](docs/technical/transaction/output.md)
        *   [ScriptPubKey 锁定脚本](docs/technical/transaction/output/scriptpubkey.md)
    *   [交易手续费 (Fee)](docs/technical/transaction/fee.md)
    *   [锁定时间 Locktime (Locktime)](docs/technical/transaction/locktime.md)
    *   [交易大小与虚拟大小 (Size / Vsize)](docs/technical/transaction/size.md)
    *   [见证数据 (Witness)](docs/technical/transaction/witness.md)
    *   [Wtxid 见证交易哈希](docs/technical/transaction/wtxid.md)
    *   [部分签名的比特币交易 (PSBT)](docs/technical/transaction/psbt.md)

#### 📝 比特币脚本 (Script)
*   **[脚本语言总览 (Script)](docs/technical/script.md)**
    *   [P2PK (Pay-to-Public-Key)](docs/technical/script/p2pk.md)
    *   [P2PKH (Pay-to-Public-Key-Hash)](docs/technical/script/p2pkh.md)
    *   [P2MS (Pay-to-Multi-Sig)](docs/technical/script/p2ms.md)
    *   [P2SH (Pay-to-Script-Hash)](docs/technical/script/p2sh.md)
    *   [P2WPKH (Pay-to-Witness-Public-Key-Hash)](docs/technical/script/p2wpkh.md)
    *   [P2WSH (Pay-to-Witness-Script-Hash)](docs/technical/script/p2wsh.md)
    *   [P2SH-P2WPKH](docs/technical/script/p2sh-p2wpkh.md)
    *   [P2SH-P2WSH](docs/technical/script/p2sh-p2wsh.md)
    *   [P2TR (Pay-to-Taproot)](docs/technical/script/p2tr.md)
    *   [OP_RETURN 脚本 (Return)](docs/technical/script/return.md)

#### ⚡ 闪电网络与 Lnd 技术 (Lightning Network)
*   **[闪电网络与 Lnd 技术 (Lightning Network)](docs/technical/lightning.md)**
    *   [Lnd 启动扫描速度慢分析 (Lnd Low Rescan Speed)](docs/technical/lightning/lnd-low-rescan-speed-startup.md)
    *   [如何通过 lnd-cli 关闭通道 (How to Close Lightning Channels)](docs/technical/lightning/how-to-close-lightning-channels-by-lnd-cli.md)
    *   [闪电网络基础与原理 - Part 0](docs/technical/lightning/hello-lightning-network-part0.md)
    *   [闪电网络基础与原理 - Part 1](docs/technical/lightning/hello-lightning-network-part1.md)
    *   [闪电网络基础与原理 - Part 2](docs/technical/lightning/hello-lightning-network-part2.md)
    *   [闪电网络基础与原理 - Part 3](docs/technical/lightning/hello-lightning-network-part3.md)
    *   [闪电网络节点搭建与配置小抄](docs/technical/lightning/setup-lightning-node-cheat-sheet.md)
    *   [Eltoo 闪电和离线契约更新机制](docs/technical/lightning/eltoo-lightning-offchain-contracts.md)
    *   [闪电网络的慢慢成长之路](docs/technical/lightning/lightning-network-gradual-growth.md)

#### ⛏️ 挖矿与网络 (Mining & Networking)
*   **[挖矿总览 (Mining)](docs/technical/mining.md)**
    *   [区块奖励 (Block Reward)](docs/technical/mining/block-reward.md)
    *   [币基交易 (Coinbase Transaction)](docs/technical/mining/coinbase-transaction.md)
    *   [内存池 (Memory Pool)](docs/technical/mining/memory-pool.md)
    *   [候选区块 (Candidate Block)](docs/technical/mining/candidate-block.md)
    *   [目标值 (Target)](docs/technical/mining/target.md)
*   **[网络协议总览 (Networking)](docs/technical/networking.md)**
    *   [比特币 daemon 服务 Systemd 启动配置](docs/technical/networking/how-to-set-systemd-startup-script-for-bitcoind.md)
    *   [网络节点 (Node)](docs/technical/networking/node.md)
    *   [魔法字节 (Magic Bytes)](docs/technical/networking/magic-bytes.md)

#### ⚡ 比特币升级协议 (Upgrades)
*   [隔离见证 (Segregated Witness / SegWit)](docs/technical/upgrades/segregated-witness.md)
*   [主根升级 (Taproot)](docs/technical/upgrades/taproot.md)

#### ⚙️ CS 基础知识 (General CS Concepts)

*   [十六进制 (Hexadecimal)](docs/technical/general/hexadecimal.md)
*   [字节 (Bytes)](docs/technical/general/bytes.md)
*   [字节序 (Byte Order / Little-Endian)](docs/technical/general/byte-order.md)
*   [可变长度整数 VarInt (Compact Size)](docs/technical/general/compact-size.md)

---

### 🟡 3. 番外篇 (External Articles)
外部科普推荐、读书笔记与延伸思考。

*   **[比特币番外篇主页](docs/external.md)**
*   **💡 推荐科普博文 (Blog Articles)**
    *   [美国政府是如何没收大量比特币的](docs/external/how-us-government-seizes-bitcoins.md)
    *   [远古矿工转移8万枚比特币](docs/external/ancient-miners-move-bitcoins.md)
    *   [十行代码挑战世界金融体系](docs/external/ten-lines-of-code-challenge-financial-system.md)
    *   [《The Internet of Money》读书笔记](docs/external/the-internet-of-money-reading-notes.md)
    *   [《The Book of Satoshi》读书笔记](docs/external/the-book-of-satoshi-reading-notes.md)
    *   [比特币的过去，现在和未来](docs/external/bitcoin-past-present-future.md)
*   **⚙️ 延伸思考 (Extended Topics)**
    *   [提高比特币私钥碰撞几率的思路](docs/external/bitcoin-private-key-collision-ideas.md)
    *   [理想中的比特币全节点实现](docs/external/ideal-bitcoin-full-node-implementation.md)
