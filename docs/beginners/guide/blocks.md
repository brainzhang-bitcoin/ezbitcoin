<img src="../../images/icons_loader-2.svg" alt="Loading Tool" style="height:32px; width:32px;" />

A block is a bunch of [transactions](/docs/beginners/guide/transactions.md) that have been added to the [blockchain](/docs/beginners/guide/blockchain.md).

## How are blocks formed?

Blocks are constructed during the process of [mining](/docs/beginners/guide/mining.md).

### Mining basics

When you make a bitcoin transaction, it isn't added to the blockchain straight away. Instead, it is held in a temporary pool of transactions.

[<img src="../../images/beginners_guide_blocks_01-transaction_pool.png" alt="Diagram showing the memory pool inside a node on the bitcoin network." width="328" height="360" />](/docs/beginners/guide/blocks/01-transaction_pool.png.md)

I've called it a "transaction pool" here, but the official term is *[memory pool](/docs/technical/mining/memory-pool.md)*.

If you are a miner, your job is to gather transactions from the transaction pool into a "[candidate block](/docs/technical/mining/candidate-block.md)", and to *try* and add this candidate block to the blockchain.

[<img src="../../images/beginners_guide_blocks_02-candidate_block.png" alt="Diagram showing a transactions from the memory pool being collected into a candidate block." width="421" height="360" />](/docs/beginners/guide/blocks/02-candidate_block.png.md)

#### Block header

Each candidate block is given a [block header](/docs/technical/block.md#header), which is basically a bunch of *metadata* containing information about the contents of the block.

[<img src="../../images/beginners_guide_blocks_03-block_header.png" alt="Diagram showing a block header being constructed for a candidate block." width="484" height="369" />](/docs/beginners/guide/blocks/03-block_header.png.md)

Miners use this block header as the starting point when trying to add a block to the blockchain.

> **Metadata** – data that describes other data, serving as an informative label.



##### Block header fields

The details of the block header fields isn't important right now, but here's a quick summary anyway:

[Version](/docs/technical/block/version.md)
:   Version number for the block.

Previous Block
:   An identification number for the previous block that we want to build upon.

[Merkle Root](/docs/technical/block/merkle-root.md)
:   A fingerprint for all the transactions in the block (basically all of the transactions [hashed](/docs/technical/cryptography/hash-function.md) together). This as the most significant part of the block header.

[Time](/docs/technical/block/time.md)
:   The current time. Always handy.

Target
:   The value that miners work with to try and add this block to the blockchain. This will make more sense in a moment.

## How are blocks added to the blockchain?

To add a candidate block to the blockchain, you **[hash](/docs/technical/cryptography/hash-function.md) the data in the block header** and hope that the result is *below a certain [target](/docs/technical/mining/target.md) value*.

[<img src="../../images/beginners_guide_blocks_05-block_target.png" alt="Diagram showing a block hash for a candidate block being compared to the current target." width="610" height="359" />](/docs/beginners/guide/blocks/05-block_target.png.md)

The *target* is calculated from the [difficulty](/docs/beginners/guide/difficulty.md), which is a value set by the bitcoin network to regulate how difficult it is to add a block of transactions to the blockchain.

Don't worry, I know this *difficulty* and *target* business is a little confusing at first, but it will make more sense over time.

[Difficulty](/docs/beginners/guide/difficulty.md)
:   A value used to regulate how quickly blocks are solved. All nodes agree on the same calculation of the difficulty for the current height of the blockchain. It adjusts every 2,016 blocks (roughly every 2 weeks) to help create an average of 10 minutes between blocks.

Think of the target as the limbo pole for candidate blocks – the greater the difficulty, the lower the target, and the more difficult it is to find a [block hash](/docs/technical/block/hash.md) that is below this value.

### An extra number

I lied. You don't actually hash the block header on its own. You actually hash it with *an extra number*.

[<img src="../../images/beginners_guide_blocks_06-block_nonce.png" alt="Diagram showing a nonce being used to change the resulting block hash for a block header." width="610" height="359" />](/docs/beginners/guide/blocks/06-block_nonce.png.md)

This extra number is called a [nonce](/docs/technical/block/nonce.md), and it's basically a dummy field that miners use to help them get a block hash below the target value.

> **Nonce** – an arbitrary number used only once in a cryptographic communication.

If the first nonce doesn't work (starting at 0), *keep incrementing it and hashing the block header*. If you're lucky you'll find a nonce that returns a block hash that is *below* the current target value.

[<img src="../../images/beginners_guide_blocks_06-block_nonce_success.png" alt="Diagram showing a successful nonce producing a block hash below the current target." width="610" height="359" />](/docs/beginners/guide/blocks/06-block_nonce_success.png.md)

I know these hash values contain letters, but you can still think of them as numbers like any other. They're simply [hexadecimal](/docs/technical/general/hexadecimal.md) values, and computers love working with them.

### Solving the block

Once you've found a nonce that produces a low-enough block hash, the block is "solved" and all of the transactions in this block are added to the blockchain.

[<img src="../../images/beginners_guide_blocks_07-block_complete.png" alt="Diagram showing a successfully mined block being added on to the blockchain." width="610" height="413" />](/docs/beginners/guide/blocks/07-block_complete.png.md)

All miners will now head back to the transaction pool and start working on the next candidate block. They will use your successful block hash in their next block header (so they can build upon the block you've just mined), and the race to add a new block of transactions to the blockchain starts again.

Good work.