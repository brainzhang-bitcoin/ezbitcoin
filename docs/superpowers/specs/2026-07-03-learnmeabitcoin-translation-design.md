# Design Spec: Parallel Markdown Translation for Learn Me A Bitcoin

This specification outlines the design for translating all scraped markdown documentation under `docs/` from English to Chinese using parallel LLM translation subagents.

## 1. Goal & Scope

- **Objective**: Translate all tutorial markdown files in `docs/` (excluding specs/plans) to Chinese.
- **Language**: Chinese (Simplified), concise and technically accurate.
- **Output format**: Directly overwrite the original English `.md` files to maintain existing folder structure and cross-document links.
- **Terminology Preservation**:
  - Keep untranslated: `UTXO`, `SegWit`, `Taproot`, `WIF`, `Bech32`, `Base58`, `PSBT`, `ECDSA`, `Schnorr`, `VarInt`, `Opcode` (e.g. `OP_RETURN`), `Coinbase`, `Nonce`, `Merkle Root`, `HD Wallets`, `txid`, `wtxid`, `vout`.
  - Translate standard terms: Private Key -> 私钥, Public Key -> 公钥, Address -> 地址, Blockchain -> 区块链, Mining -> 挖矿, Transaction -> 交易, Locktime -> 锁定时间.

## 2. Parallel Processing Architecture

To optimize performance and bypass rate limitations, files are partitioned into 4 distinct Group lists:

- **Group 1 (Beginners)**: `docs/beginners.md` and files under `docs/beginners/`.
- **Group 2 (Technical - Core & Basics)**: `docs/technical.md` and files under `docs/technical/block/`, `docs/technical/blockchain/`, `docs/technical/cryptography/`, `docs/technical/general/`.
- **Group 3 (Technical - Keys & Transaction)**: Files under `docs/technical/keys/` and `docs/technical/transaction/`.
- **Group 4 (Technical - Script, Mining & Networking)**: Files under `docs/technical/script/`, `docs/technical/mining/`, `docs/technical/networking/`, and `docs/technical/upgrades/`.

Each group is delegated to an independent subagent instance executing concurrently.

## 3. Subagent Translation Guidelines

Each subagent will adhere to the following rules:
1. **Format Conservation**: Under no circumstance should Markdown syntax elements, HTML tag structures, or hyperlinks (e.g. `[link](/docs/path.md)`) be broken or translated.
2. **Code Blocks**: Code and comments inside fenced code blocks (` ``` `) must remain unchanged.
3. **Overwriting**: Overwrite the original files to preserve the exact file structure.
