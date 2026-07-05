# EzBitcoin - 比特币入门

这个项目面向有一定计算机基础，对比特币技术好奇的读者，用尽可能通俗易懂的介绍比特币是如何工作的；里面的部分材料包含来自知名 Bitcoin 极简图解教学网站 [Learn Me A Bitcoin](https://learnmeabitcoin.com/) ，部分材料来自于[作者的blog历史文章](https://brainz.fun/blog/categories/blockchain/);

---

## 📚 文档目录 (Table of Contents)

### 🟢 1. 新手指南 (Beginners Guide)
适合完全没有技术背景的读者，用极简非技术语言介绍比特币基本概念。

*   **[新手导读及概览](beginners.md)**
*   **[比特币是如何工作的？](beginners/how-does-bitcoin-work.md)**
*   **[如何选择钱包 (Wallets)](beginners/wallets.md)**
*   **[如何选择交易平台 (Exchanges)](beginners/exchanges.md)**
*   **[如何发送与接收比特币 (Sending)](beginners/sending.md)**
*   **[安全与存储防范 (Security)](beginners/security.md)**
*   **📖 新手极简图解手册 (Beginners Short Guide)**
    *   [比特币网络 (Network)](beginners/guide/network.md)
    *   [节点 (Node)](beginners/guide/node.md)
    *   [挖矿 (Mining)](beginners/guide/mining.md)
    *   [区块链 (Blockchain)](beginners/guide/blockchain.md)
    *   [区块 (Blocks)](beginners/guide/blocks.md)
    *   [难度 (Difficulty)](beginners/guide/difficulty.md)
    *   [交易 (Transactions)](beginners/guide/transactions.md)
    *   [交易输出 (Outputs)](beginners/guide/outputs.md)
    *   [锁定与解锁 (Locks)](beginners/guide/locks.md)
    *   [密钥与地址 (Keys & Addresses)](beginners/guide/keys-addresses.md)
    *   [私钥 (Private Keys)](beginners/guide/private-keys.md)
    *   [公钥 (Public Keys)](beginners/guide/public-keys.md)
    *   [数字签名 (Digital Signatures)](beginners/guide/digital-signatures.md)
    *   [隔离见证 (SegWit)](beginners/guide/segwit.md)
*   **💡 推荐科普博文 (Blog Articles)**
    *   [美国政府是如何没收大量比特币的](beginners/how-us-government-seizes-bitcoins.md)
    *   [远古矿工转移8万枚比特币](beginners/ancient-miners-move-bitcoins.md)
    *   [十行代码挑战世界金融体系](beginners/ten-lines-of-code-challenge-financial-system.md)
    *   [澳本聪是中本聪吗？(二)](beginners/is-craig-wright-real-satoshi-part2.md)
    *   [《The Internet of Money》读书笔记](beginners/the-internet-of-money-reading-notes.md)
    *   [《The Book of Satoshi》读书笔记](beginners/the-book-of-satoshi-reading-notes.md)
    *   [比特币的过去，现在和未来](beginners/bitcoin-past-present-future.md)
    *   [祝比特币10岁生日快乐](beginners/happy-10th-birthday-bitcoin.md)

---

### 🔵 2. 技术指南 (Technical Guide)
适合想要深入理解比特币底层协议、密码学及进行比特币编程开发的读者。

*   **[技术指南导读主页](technical.md)**

#### 📦 区块与区块链 (Blocks & Blockchain)
*   **[区块总览 (Block)](technical/block.md)**
    *   [区块哈希值 (Hash)](technical/block/hash.md)
    *   [前一区块哈希 (Previous Block)](technical/block/previous-block.md)
    *   [默克尔根 (Merkle Root)](technical/block/merkle-root.md)
    *   [时间戳 (Time)](technical/block/time.md)
    *   [难度目标 Bits (Bits)](technical/block/bits.md)
    *   [随机数 Nonce (Nonce)](technical/block/nonce.md)
    *   [版本号 Version (Version)](technical/block/version.md)
    *   [blk.dat 数据文件结构](technical/block/blkdat.md)
*   **[区块链总览 (Blockchain)](technical/blockchain.md)**
    *   [比特币的 Blockchain - Part 1](technical/blockchain/bitcoin-blockchain-part1.md)
    *   [比特币的 Blockchain - Part 2](technical/blockchain/bitcoin-blockchain-part2.md)
    *   [区块高度 (Height)](technical/blockchain/height.md)
    *   [最长链原则 (Longest Chain)](technical/blockchain/longest-chain.md)
    *   [51% 攻击 (51% Attack)](technical/blockchain/51-attack.md)
    *   [硬分叉 (Hard Fork)](technical/blockchain/hard-fork.md)
    *   [软分叉 (Soft Fork)](technical/blockchain/soft-fork.md)

#### 🔐 密码学 (Cryptography)
*   **[密码学总览 (Cryptography)](technical/cryptography.md)**
    *   [提高比特币私钥碰撞几率的思路](technical/cryptography/bitcoin-private-key-collision-ideas.md)
    *   [哈希函数 (Hash Function)](technical/cryptography/hash-function.md)
    *   [椭圆曲线 (Elliptic Curve)](technical/cryptography/elliptic-curve.md)
    *   [ECDSA 签名算法](technical/cryptography/elliptic-curve/ecdsa.md)
    *   [Schnorr 签名算法](technical/cryptography/elliptic-curve/schnorr.md)

#### 🔑 密钥、签名与地址 (Keys, Signatures & Addresses)
*   **[密钥总览 (Keys)](technical/keys.md)**
    *   [私钥 (Private Key)](technical/keys/private-key.md)
    *   [WIF 格式私钥 (WIF)](technical/keys/private-key/wif.md)
    *   [公钥 (Public Key)](technical/keys/public-key.md)
    *   [公钥哈希 (Public Key Hash)](technical/keys/public-key/hash.md)
    *   [数字签名 (Signature)](technical/keys/signature.md)
    *   [比特币地址 (Address)](technical/keys/address.md)
    *   [Base58 校验和 (Checksum)](technical/keys/checksum.md)
    *   [Bech32 格式编码 (Bech32)](technical/keys/bech32.md)
    *   [HD 层次确定性钱包 (HD Wallets)](technical/keys/hd-wallets.md)
        *   [助记词种子 (Mnemonic Seed)](technical/keys/hd-wallets/mnemonic-seed.md)
        *   [扩展密钥 (Extended Keys)](technical/keys/hd-wallets/extended-keys.md)
        *   [派生路径 (Derivation Paths)](technical/keys/hd-wallets/derivation-paths.md)

#### 💸 比特币交易 (Transactions)
*   **[交易总览 (Transaction)](technical/transaction.md)**
    *   [比特币的交易 - Part 5](technical/transaction/bitcoin-transaction-part5.md)
    *   [比特币的交易 - Part 6](technical/transaction/bitcoin-transaction-part6.md)
    *   [未花费交易输出 (UTXO)](technical/transaction/utxo.md)
    *   [交易输入 (Input)](technical/transaction/input.md)
        *   [ScriptSig 解锁脚本](technical/transaction/input/scriptsig.md)
        *   [Sequence 序列号](technical/transaction/input/sequence.md)
        *   [Vout 输出索引](technical/transaction/input/vout.md)
    *   [交易输出 (Output)](technical/transaction/output.md)
        *   [ScriptPubKey 锁定脚本](technical/transaction/output/scriptpubkey.md)
    *   [交易手续费 (Fee)](technical/transaction/fee.md)
    *   [锁定时间 Locktime (Locktime)](technical/transaction/locktime.md)
    *   [交易大小与虚拟大小 (Size / Vsize)](technical/transaction/size.md)
    *   [见证数据 (Witness)](technical/transaction/witness.md)
    *   [Wtxid 见证交易哈希](technical/transaction/wtxid.md)
    *   [部分签名的比特币交易 (PSBT)](technical/transaction/psbt.md)

#### 📝 比特币脚本 (Script)
*   **[脚本语言总览 (Script)](technical/script.md)**
    *   [P2PK (Pay-to-Public-Key)](technical/script/p2pk.md)
    *   [P2PKH (Pay-to-Public-Key-Hash)](technical/script/p2pkh.md)
    *   [P2MS (Pay-to-Multi-Sig)](technical/script/p2ms.md)
    *   [P2SH (Pay-to-Script-Hash)](technical/script/p2sh.md)
    *   [P2WPKH (Pay-to-Witness-Public-Key-Hash)](technical/script/p2wpkh.md)
    *   [P2WSH (Pay-to-Witness-Script-Hash)](technical/script/p2wsh.md)
    *   [P2SH-P2WPKH](technical/script/p2sh-p2wpkh.md)
    *   [P2SH-P2WSH](technical/script/p2sh-p2wsh.md)
    *   [P2TR (Pay-to-Taproot)](technical/script/p2tr.md)
    *   [OP_RETURN 脚本 (Return)](technical/script/return.md)

#### ⚡ 闪电网络与 Lnd 技术 (Lightning Network)
*   **[闪电网络与 Lnd 技术 (Lightning Network)](technical/lightning.md)**
    *   [Lnd 启动扫描速度慢分析 (Lnd Low Rescan Speed)](technical/lightning/lnd-low-rescan-speed-startup.md)
    *   [如何通过 lnd-cli 关闭通道 (How to Close Lightning Channels)](technical/lightning/how-to-close-lightning-channels-by-lnd-cli.md)
    *   [闪电网络基础与原理 - Part 0](technical/lightning/hello-lightning-network-part0.md)
    *   [闪电网络基础与原理 - Part 1](technical/lightning/hello-lightning-network-part1.md)
    *   [闪电网络基础与原理 - Part 2](technical/lightning/hello-lightning-network-part2.md)
    *   [闪电网络基础与原理 - Part 3](technical/lightning/hello-lightning-network-part3.md)
    *   [闪电网络节点搭建与配置小抄](technical/lightning/setup-lightning-node-cheat-sheet.md)
    *   [Eltoo 闪电和离线契约更新机制](technical/lightning/eltoo-lightning-offchain-contracts.md)
    *   [闪电网络的慢慢成长之路](technical/lightning/lightning-network-gradual-growth.md)

#### ⛏️ 挖矿与网络 (Mining & Networking)
*   **[挖矿总览 (Mining)](technical/mining.md)**
    *   [区块奖励 (Block Reward)](technical/mining/block-reward.md)
    *   [币基交易 (Coinbase Transaction)](technical/mining/coinbase-transaction.md)
    *   [内存池 (Memory Pool)](technical/mining/memory-pool.md)
    *   [候选区块 (Candidate Block)](technical/mining/candidate-block.md)
    *   [目标值 (Target)](technical/mining/target.md)
*   **[网络协议总览 (Networking)](technical/networking.md)**
    *   [比特币 daemon 服务 Systemd 启动配置](technical/networking/how-to-set-systemd-startup-script-for-bitcoind.md)
    *   [理想中的比特币全节点实现](technical/networking/ideal-bitcoin-full-node-implementation.md)
    *   [网络节点 (Node)](technical/networking/node.md)
    *   [魔法字节 (Magic Bytes)](technical/networking/magic-bytes.md)

#### ⚡ 比特币升级协议 (Upgrades)
*   [隔离见证 (Segregated Witness / SegWit)](technical/upgrades/segregated-witness.md)
*   [主根升级 (Taproot)](technical/upgrades/taproot.md)

#### ⚙️ CS 基础知识 (General CS Concepts)

*   [十六进制 (Hexadecimal)](technical/general/hexadecimal.md)
*   [字节 (Bytes)](technical/general/bytes.md)
*   [字节序 (Byte Order / Little-Endian)](technical/general/byte-order.md)
*   [可变长度整数 VarInt (Compact Size)](technical/general/compact-size.md)
