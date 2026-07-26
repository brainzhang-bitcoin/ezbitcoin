# Technical Guide Reorganization Design

## Objective
Reorganize the "Technical Guide (技术指南)" section of EzBitcoin into a "Transaction Lifecycle" learning path. This transforms the existing disconnected technical modules into a cohesive, story-driven progression from low-level data and cryptography all the way up to lightning network scalability.

## Current State
Currently, `docs/index.md` lists the Technical Guide as a set of parallel reference topics (e.g. Blocks, Cryptography, Keys, Transactions, Script, Networking, Lightning, CS Basics).

## Target Structure (Phase-Based Approach)

### Phase 1: 基础工具箱 (Foundation & Toolbox)
*Focus: The building blocks of bitcoin: bytes, hashes, curves, and identity.*
- **CS 基础 (General CS Concepts):** Hex, Bytes, Byte Order, VarInt
- **密码学 (Cryptography):** Hash Function, Elliptic Curve, ECDSA, Schnorr
- **密钥与地址 (Keys & Addresses):** Private Key, WIF, Public Key, PK Hash, Signature, Address, Checksum, Bech32, HD Wallets

### Phase 2: 构建交易 (Constructing the Transaction)
*Focus: How a user spends bitcoin by constructing and signing a transaction.*
- **交易机制 (Transactions):** UTXO, Input, Output, Fee, Locktime, Size/Vsize, PSBT
- **比特币脚本 (Script):** Script Intro, P2PK, P2PKH, P2MS, P2SH, P2TR, OP_RETURN

### Phase 3: 广播与确认 (Broadcast & Consensus)
*Focus: The journey of a transaction from the mempool to being embedded in a block.*
- **网络层 (Networking):** Node, Magic Bytes, bitcoind setup
- **内存池与挖矿 (Mempool & Mining):** Mempool, Block Reward, Coinbase, Candidate Block, Target
- **区块结构 (Block Anatomy):** Block Hash, Previous Block, Merkle Root, Time, Bits, Nonce, Version, blk.dat

### Phase 4: 账本与演进 (The Ledger & Protocol Evolution)
*Focus: How blocks chain together securely, and how the network upgrades.*
- **区块链 (Blockchain):** Chain structure, Height, Longest Chain, 51% Attack
- **分叉与升级 (Forks & Upgrades):** Hard Fork, Soft Fork, SegWit, Taproot

### Phase 5: 二层扩展 (Layer 2 Scaling)
*Focus: Scaling bitcoin for the world via the Lightning Network.*
- **闪电网络 (Lightning Network):** Fundamentals (Part 0-3), Channels, Eltoo, Node Setup

## Implementation Plan
1. **Update `docs/index.md`**: Rewrite the TOC for the Technical Guide using the above 5 phases. Ensure all links accurately point to existing Markdown files.
2. **Formatting Fixes**: Sweep the `technical/` directory for any broken markdown (e.g., missing H1s, invalid anchors) just like in the Beginners Guide.
3. **Internal Nav Flow**: Ensure that `technical/index.md` is updated to reflect this new flow, or removed if redundant.

## Out of Scope
- Rewriting technical content.
- Changing the directory structure aggressively. The files will stay where they are, we are merely reorganizing the *presentation* in the Table of Contents and cleaning up the files.
