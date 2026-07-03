![Loading Tool](../../images/icons_loader-2.svg)

[![Diagram showing a candidate block as a collection of transactions from the memory pool.](../../images/diagrams_png_mining-candidate-block.png)](https://static.learnmeabitcoin.com/diagrams/png/mining-candidate-block.png)

A candidate block is a **[block](/docs/technical/block.md) of [transactions](/docs/technical/transaction.md) a miner attempts to add to the [blockchain](/docs/technical/blockchain.md)**.

During the [mining](/) process, each miner will collect transactions from their [memory pool](/docs/technical/mining/memory-pool.md) into a *candidate block*. They will then repeatedly [hash](/docs/technical/cryptography/hash-function.md) this block to try and get a [block hash](/docs/technical/block/hash.md) below the [target](/docs/technical/mining/target.md).

If a miner can get a block hash below the target, their candidate block can be added on to the blockchain.

They will then broadcast this "mined" candidate block to the other [nodes](/docs/technical/networking/node.md) on the network, where each node will verify and add it to their blockchain too.

[![Diagram showing a miner broadcasting their mined candidate block to the other nodes on the network.](../../images/diagrams_png_mining-block-broadcast.png)](https://static.learnmeabitcoin.com/diagrams/png/mining-block-broadcast.png)

In other words, a candidate block *represents* the **next block of transactions** to be added on to the blockchain.

## Example

What does the current candidate block look like?

Here's what the *current* candidate block looks like according to my [local node](/explorer/):

### Block Header Candidate Block Header Refreshing

|  |  |
| --- | --- |
| [Version](/docs/technical/block/version.md) | 0x20000000 |
| [Previous Block](/docs/technical/block/previous-block.md) | 00000000000000000001b9c4dc446b059b686ba5a38bd1e5cf4692d4420e2f54 |
| [Merkle Root](/docs/technical/block/merkle-root.md) | `c6797e1c1183cc9c289e4aa10ff7b2b73f5f22bac1579912a34da873d8150e66` |
| [Time](/docs/technical/block/time.md) | 03 Jul 2026, 08:37:58 |
| [Bits](/docs/technical/block/bits.md) | `17021a42` |
| [Nonce](/docs/technical/block/nonce.md) | 0 |

### Transactions

Show Transactions ![Loading Transactions](../../images/icons_loader-2.svg)

* **I'm not actively trying to mine this block.** If I was, I would be adjusting the [nonce](/docs/technical/block/nonce.md) in the block header to try and get a block hash below the current target.
* I haven't put my own [coinbase transaction](/docs/technical/mining/coinbase-transaction.md) in this candidate block either, so it wouldn't be valid if I mined it anyway. This example is here to show you what a current candidate block looks like.
* If the [merkle root](/docs/technical/block/merkle-root.md) changes, you know the transactions in the block have changed.
* The lower-fee transactions toward the bottom of the candidate block are more likely to change.

## Construction

How do you construct a candidate block?

[![Diagram showing the steps for constructing a candidate block.](../../images/diagrams_png_block-candidate-block-construction.png)](https://static.learnmeabitcoin.com/diagrams/png/block-candidate-block-construction.png)

There are three basic steps to constructing a candidate block:

### 1. Select transactions

The first step is to **[select transactions](#transaction-selection) from the memory pool** that you want to include in your candidate block.

A miner will typically fill their candidate block with the highest-[fee](/docs/technical/transaction/fee.md) transactions to maximize the amount they can claim from the [block reward](/docs/technical/mining/block-reward.md).

### 2. Construct the coinbase transaction

The [coinbase transaction](/docs/technical/mining/coinbase-transaction.md) is the very first transaction in a block, and it's used by the miner to claim the [block reward](/docs/technical/mining/block-reward.md).

The reason for constructing the coinbase transaction *after* selecting the transactions is because it needs to contain a [witness root hash](/docs/technical/transaction/wtxid.md#commitment), which is calculated based on the transactions that have been included in the block.

### 3. Construct the block header

The [block header](/docs/technical/block.md#header) is a small amount of metadata that summarizes all the data inside the block. This is what a miner will be hashing as they attempt to [mine](/docs/technical/mining.md) the candidate block.

The block header contains six different fields ([version](/docs/technical/block/version.md), [previous block](/docs/technical/block/previous-block.md), [merkle root](/docs/technical/block/merkle-root.md), [time](/docs/technical/block/time.md), [bits](/docs/technical/block/bits.md), [nonce](/docs/technical/block/nonce.md)), but these two are the most pertinent:

* **Previous Block:** This field is used to specify an existing block that the candidate block will be built on top of. Miners always want to build on top of the *tip* of the blockchain, because they can only claim the block reward if the block they mine ends up becoming part of the [longest chain](/docs/technical/blockchain/longest-chain.md).
* **Merkle Root:** The merkle root is a fingerprint for all the transactions included in the block. This is important, because it means that you cannot change the contents of the block without changing the fingerprint. So again, this is why we construct the block header *after* selecting the transactions for the candidate block.

![Tool Icon](../../images/icons_tool.svg) Block Header

Random Example

Block:

Block Header (Hex)

`0 bytes`


Block Header (Fields)


Version


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

Previous Block:
Merkle Root
Time

0d

Bits
Nonce

0d



+1



Block Hash

This is the HASH256 of the hex block header. It's also in reverse byte order, because that's how block hashes are displayed in block explorers.




0 secs

And that's the construction of the candidate block complete.

From here, a miner can now start working on [mining](/docs/technical/mining.md) the candidate block to try and add it on to the [blockchain](/docs/technical/blockchain.md).

## Requirements

What are the requirements for a candidate block?

[![Diagram showing the requirements for a candidate block.](../../images/diagrams_png_block-candidate-block-requirements.png)](https://static.learnmeabitcoin.com/diagrams/png/block-candidate-block-requirements.png)

A candidate block has a few basic requirements:

### 1. Coinbase transaction

The **first transaction** in the candidate block must be the [coinbase transaction](/docs/technical/mining/coinbase-transaction.md).

This transaction is placed in the block by the miner to claim the [block reward](/docs/technical/mining/block-reward.md).

This means that all blocks will always contain **at least *one* transaction**.

### 2. Valid transactions

All the transactions a miner includes in their candidate block **must be valid**.

For example, each transaction can only spend coins that already exist.

If a miner mines a block containing invalid transactions and broadcasts it to the network, all of the nodes will reject it, and all of their effort for mining the block will be wasted.

### 3. Transaction parents

[![Diagram showing a parent transaction coming before a child transaction in a block.](../../images/diagrams_png_transaction-child-pays-for-parent.png)](https://static.learnmeabitcoin.com/diagrams/png/transaction-child-pays-for-parent.png)

The parent(s) of a transaction must always come *before* the child transaction.

For example, if a transaction has [ancestors](/docs/technical/mining/memory-pool.md#ancestors) that are currently in the mempool, those ancestors must be included **above it in the candidate block**.

Each node validates the transactions in a block from *top to bottom*, so if you include a parent *after* a child, it will appear as though that child transaction is spending [outputs](/docs/technical/transaction/output.md) that do not already exist (and would therefore be invalid).

### 4. Size limit

[![Diagram showing the block size limit in terms of weight.](../../images/diagrams_png_block-weight.png)](https://static.learnmeabitcoin.com/diagrams/png/block-weight.png)

The maximum size of a block is **4,000,000 [weight](/docs/technical/transaction/size.md#weight) units**.

So the transactions you include in your candidate block (including the size of the block header and transaction count) must be within this size limit.

The block size limit can be found in [consensus.h](https://github.com/bitcoin/bitcoin/blob/master/src/consensus/consensus.h)

### 5. Signature operations

A block is limited to a maximum of **80,000 [signature](/docs/technical/keys/signature.md) check operations**. So the transactions you include in your candidate block must be within this limit.

This is because [signature verification](/docs/technical/cryptography/elliptic-curve/ecdsa.md#verify) is time-consuming, so this limit prevents miners from creating blocks that would be exceptionally slow to validate.

Signature check operations are performed by [Script](/docs/technical/script.md) opcodes such as: `OP_CHECKSIG`, `OP_CHECKMULTISIG`, `OP_CHECKSIGVERIFY`, `OP_CHECKMULTISIGVERIFY`

* The sigops limit can also be found in [consensus.h](https://github.com/bitcoin/bitcoin/blob/master/src/consensus/consensus.h)
* [Segregated Witness](/docs/technical/upgrades/segregated-witness.md): Similar to how bytes in a [legacy transaction](/docs/technical/transaction.md#example-legacy) are multiplied by 4 to calculate their equivalent weight, the count of signature operations in legacy transactions is also **multiplied by 4**. So whereas a single `OP_CHECKSIG` counts as 1 signature operation when in the [Witness](/docs/technical/transaction/witness.md) field (as expected), it actually counts as 4 signature operations when in the [ScriptSig](/docs/technical/transaction/input/scriptsig.md) (see [validation.cpp](https://github.com/bitcoin/bitcoin/blob/master/src/validation.cpp)).

## Transaction Selection

How do miners select transactions for their candidate block?

[![Diagram showing the highest fee transactions being selected from the memory pool for inclusion in a candidate block.](../../images/diagrams_png_block-candidate-block-transaction-selection.png)](https://static.learnmeabitcoin.com/diagrams/png/block-candidate-block-transaction-selection.png)

A miner can fill their candidate block with **any transactions** they like from the [memory pool](/docs/technical/mining/memory-pool.md).

However, miners will typically look to fill their candidate block with the highest-[fee](/docs/technical/transaction/fee.md) transactions available to maximize the amount they can claim from the [block reward](/docs/technical/mining/block-reward.md).

So if there are more transactions in the memory pool than can fit into a candidate block, a miner will **prioritize the transactions with the highest fees** for inclusion in their block.

### Ancestor Feerate

[![Diagram showing a miner working out the ancestor feerate for the transactions in their memory pool.](../../images/diagrams_png_block-candidate-block-transaction-selection-ancestor-fee-rate.png)](https://static.learnmeabitcoin.com/diagrams/png/block-candidate-block-transaction-selection-ancestor-fee-rate.png)

There is one important rule that miners must follow when selecting transactions:

You can only include a transaction in a block if you also include all of its parents first.

Therefore, if a memory pool transaction has [ancestors](/docs/technical/mining/memory-pool.md#ancestors), a miner will calculate the **[ancestor feerate](/docs/technical/mining/memory-pool.md#ancestor-feerate)** to work out whether it's worth including that transaction compared to another transaction that doesn't have any ancestors.

When you've got ancestors in the memory pool, the process of selecting the optimum combination of transactions is complex, and the only way to get the "perfect" block in terms of maximizing fees is to try *all possible combinations*. Therefore, most miners will make a best-effort attempt at constructing a block with high-fee transactions, without wasting time on trying to calculate the "perfect" block each time.

## Empty Blocks

Why do miners mine empty blocks of transactions?

[![Diagram showing a miner constructing an empty candidate block to work on while they select the optimum combination of transactions from the memory pool to fill it with.](../../images/diagrams_png_block-candidate-block-empty-blocks.png)](https://static.learnmeabitcoin.com/diagrams/png/block-candidate-block-empty-blocks.png)

You sometimes find "empty blocks" appearing in the blockchain with only *one* transaction in them.

For example, block [828,012](/explorer/828012#blockchain) doesn't contain any transactions (other than the required [coinbase transaction](/docs/technical/mining/coinbase-transaction.md)), whereas the blocks above and below it are full of transactions:

| [Height](/docs/technical/blockchain/height.md) | [Block Hash](/docs/technical/block/hash.md) | Txs | Size | Avg [Feerate](/docs/technical/transaction/fee.md#sats-per-vbyte) AFR | Time (UTC) |
| --- | --- | --- | --- | --- | --- |
| [828,015](/explorer/block/00000000000000000000a9c619c4af8c09f10c11a8262bcde576450e45a126ca) 828,015 | [00000000000000000000a9c619c4af8c09f10c11a8262bcde576450e45a126ca](/explorer/block/00000000000000000000a9c619c4af8c09f10c11a8262bcde576450e45a126ca) | 3,142 | 1.00/1.00 vMB | 31 | 29 Jan 2024, 21:54 |
| [828,014](/explorer/block/000000000000000000015b4c953a7636418316bee66575d79edf407a3f9640ae) 828,014 | [000000000000000000015b4c953a7636418316bee66575d79edf407a3f9640ae](/explorer/block/000000000000000000015b4c953a7636418316bee66575d79edf407a3f9640ae) | 5,222 | 1.00/1.00 vMB | 30 | 29 Jan 2024, 21:48 |
| [828,013](/explorer/block/000000000000000000023cbbedc89f62a4e38db462bb45b5214d12f0f85f1972) 828,013 | [000000000000000000023cbbedc89f62a4e38db462bb45b5214d12f0f85f1972](/explorer/block/000000000000000000023cbbedc89f62a4e38db462bb45b5214d12f0f85f1972) | 4,385 | 1.00/1.00 vMB | 33 | 29 Jan 2024, 21:44 |
| [828,012](/explorer/block/00000000000000000003eb119d2115448bea2d14e18bf19c00020dd23fee79cb) 828,012 | [00000000000000000003eb119d2115448bea2d14e18bf19c00020dd23fee79cb](/explorer/block/00000000000000000003eb119d2115448bea2d14e18bf19c00020dd23fee79cb) | 1 | 0.00/1.00 vMB | 0 | 29 Jan 2024, 21:41 |
| [828,011](/explorer/block/0000000000000000000300773e6ec30fbed5d49a07568114c5824c7f89401fc9) 828,011 | [0000000000000000000300773e6ec30fbed5d49a07568114c5824c7f89401fc9](/explorer/block/0000000000000000000300773e6ec30fbed5d49a07568114c5824c7f89401fc9) | 5,639 | 1.00/1.00 vMB | 29 | 29 Jan 2024, 21:33 |
| [828,010](/explorer/block/000000000000000000004cdc62634f083ec10dffc7bb4777c792d67c0aefbf8b) 828,010 | [000000000000000000004cdc62634f083ec10dffc7bb4777c792d67c0aefbf8b](/explorer/block/000000000000000000004cdc62634f083ec10dffc7bb4777c792d67c0aefbf8b) | 3,881 | 1.00/1.00 vMB | 29 | 29 Jan 2024, 21:32 |
| [828,009](/explorer/block/00000000000000000000ce872172185086c9c6cfbedd0e78e90b6d0a7bd93f07) 828,009 | [00000000000000000000ce872172185086c9c6cfbedd0e78e90b6d0a7bd93f07](/explorer/block/00000000000000000000ce872172185086c9c6cfbedd0e78e90b6d0a7bd93f07) | 2,557 | 1.00/1.00 vMB | 38 | 29 Jan 2024, 21:31 |

This is because miners will typically **start working on an empty candidate block** while they select transactions from the memory pool.

Because, as mentioned, it takes a while for a miner to calculate an optimal combination of transactions to maximize the amount in [fees](/docs/technical/transaction/fee.md) they can claim. So instead of doing nothing while they calculate which transactions to include in their block, they will immediately start work on mining an *empty block* first.

Consequently, a miner will sometimes get *lucky* and mine their empty block before they get around to working on a candidate block that has been filled with transactions.

It doesn't happen very often, but that explains why you sometimes see "empty blocks" in the blockchain.

Whilst a miner will miss out on claiming transaction fees by mining an empty block, it's more profitable for them to start work on mining an empty block for the opportunity to claim the [block subsidy](/docs/technical/mining/block-reward.md#block-subsidy) in the meantime.

## Commands

### `bitcoin-cli getblocktemplate [template_request]`

Returns transactions from your node's memory pool that you can use to construct a candidate block.

Annoyingly, you also have to provide an awkward array to specify the kind of block template you want (see [BIP22](https://github.com/bitcoin/bips/blob/master/bip-0022.mediawiki)). This is what I typically use: `bitcoin-cli getblocktemplate '{"rules": ["segwit"]}'`

You will need to construct the block header manually from this block template before you start mining. For example, you will need to construct your own coinbase transaction, as well as calculate the merkle root. So it's more of a "starting point", but it does the hard work of **selecting an optimum combination of transactions** from the memory pool for maximizing the fees you can claim.

## Notes

* **There is no "single" candidate block that all miners work on.** Each miner selects transactions from their *own* mempool, so whilst there's usually a big overlap, there are typically slight differences between candidate blocks. So if you see that your transaction is currently sitting in a candidate block, it's not *guaranteed* to be included in the next block (although it's likely it will).

## Resources

* [What is sigop (signature operation)?](https://bitcoin.stackexchange.com/questions/117356/what-is-sigop-signature-operation)