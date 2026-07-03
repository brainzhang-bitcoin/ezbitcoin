<img src="../../images/icons_loader-2.svg" alt="Loading Tool" style="height:32px; width:32px;" />

[<img src="../../images/diagrams_png_blockchain-longest-chain.png" alt="Diagram showing the longest chain of blocks in a blockchain." width="320" height="376" />](https://static.learnmeabitcoin.com/diagrams/png/blockchain-longest-chain.png)

Current Longest Chain:

* **Height:** 956479
* **[Chainwork](#chainwork):** 0x000000000000000000000000000000000000000134d0e337eef3b345d0a8d660

The longest chain is what Bitcoin nodes accept as the **valid version** of the [blockchain](/docs/technical/blockchain.md).

The longest chain rule **allows every node on the network to agree** on what the blockchain looks like, and therefore agree on the same transaction history.

In other words, it means that computers acting independently over a network can maintain the same view of a globally updated file.

> The proof-of-work chain is the solution to the synchronisation problem, and to knowing what the globally shared view is without having to trust anyone.

Satoshi Nakamoto, [Cryptography Mailing List (Bitcoin P2P e-cash paper)](https://satoshi.nakamotoinstitute.org/emails/cryptography/7/)

## Definition

What is the longest chain?

The longest chain is the chain of blocks that took the **most effort to build**.

In short, to add a new block to the blockchain you need to [use processing power](/docs/technical/mining.md), which means that every block on the blockchain requires a certain amount of *energy* to get there.

[<img src="../../images/diagrams_png_blockchain-longest-chain-block-energy.png" alt="Diagram showing a computer processor being used to mine a block on to the blockchain." width="147" height="181" />](https://static.learnmeabitcoin.com/diagrams/png/blockchain-longest-chain-block-energy.png)


Blocks are mined using processing power.

Therefore, a blockchain with *more blocks* in it will have taken *more energy* to build than a chain with fewer blocks in it, and as a rule nodes will always adopt this chain over a "shorter" one.

[<img src="../../images/diagrams_png_blockchain-longest-chain-nodes-adopting.png" alt="Diagram showing nodes adopting a longer chain instead of a shorter chain." width="779" height="427" />](https://static.learnmeabitcoin.com/diagrams/png/blockchain-longest-chain-nodes-adopting.png)

As a result, nodes will always adopt the chain that took the most energy to build, and this is what we mean when we refer to the "longest chain".

> The majority decision is represented by the longest chain, which has the greatest proof-of-work effort invested in it.

Satoshi Nakamoto, [Bitcoin Whitepaper](/bitcoin.pdf)

## Misconception

Is the longest chain the one with the most blocks?

You'd think that the *longest* chain is simply the one with the most blocks in it, but the chain that required the most energy to build is **not necessarily the one with the most blocks in it**.

This is because changes to the [difficulty](/docs/beginners/guide/difficulty.md) mean that some blocks are going to require more energy to mine than others.

For example, within the same difficulty period every new block requires the same amount of effort to be mined, and therefore adds the same amount of "work" to the chain:

[<img src="../../images/diagrams_png_blockchain-longest-chain-difficulty.png" alt="Diagram showing the difficulty for the first blocks in the blockchain." width="722" height="193" />](https://static.learnmeabitcoin.com/diagrams/png/blockchain-longest-chain-difficulty.png)

However, if the difficulty increases (because blocks were mined more quickly than every 10 minutes on average), the blocks in the new difficulty period are going to take *more effort* to mine:

[<img src="../../images/diagrams_png_blockchain-longest-chain-difficulty-adjustment.png" alt="Diagram showing an increased difficulty after the first target adjustment." width="722" height="336" />](https://static.learnmeabitcoin.com/diagrams/png/blockchain-longest-chain-difficulty-adjustment.png)

Now, seeing as nodes adopt the chain with the most work, they wouldn't actually adopt a chain with *more* blocks in it if it didn't require as much work to build.

For example, if you construct two different blockchains spanning multiple difficulty periods, nodes will adopt the one that has the most cumulative "chainwork", and not simply the one with the most blocks in it:

[<img src="../../images/diagrams_png_blockchain-longest-chain-difficulty-adjustment-chainwork.png" alt="Diagram showing the difference between a chain with the most work and a chain with the most blocks." width="941" height="427" />](https://static.learnmeabitcoin.com/diagrams/png/blockchain-longest-chain-difficulty-adjustment-chainwork.png)


The chain on the right has been constructed to keep the difficulty artificially low.

So in summary, the phrase "longest chain" refers to **the blockchain that has taken the most energy to build**. For the most part this is usually the chain with the most blocks in it, but to be more precise it's the chain with the most amount of *work* in it.

In the [first version of Bitcoin](https://github.com/Dan-McG/bitcoin-0.1.0), Satoshi used the *number of blocks* as the metric for determining the longest chain, believing this to be the chain that would have taken the most work to build. However, this is vulnerable to manipulation, so it was later [changed](https://bitcoin.stackexchange.com/questions/29742/strongest-vs-longest-chain-and-orphaned-blocks/29744#29744) to using chainwork as the metric for the longest chain instead.

## Chainwork

How do you calculate the longest chain?

The longest chain is measured by a metric called "chainwork".

> [Chainwork] is the total number of hashes that are expected to have been necessary to produce the current chain.

Pieter Wuille, [bitcoin.stackexchange.com](https://bitcoin.stackexchange.com/questions/26869/what-is-chainwork/26894#26894)

To work out chainwork, you just need to work out **how many hashes you would have needed to perform to mine each block** in the chain, then add them up.

[<img src="../../images/diagrams_png_blockchain-longest-chain-chainwork.png" alt="Diagram showing the calculation for chainwork." width="937" height="386" />](https://static.learnmeabitcoin.com/diagrams/png/blockchain-longest-chain-chainwork.png)


The total chainwork is the sum of the average number of expected hashes to mine each block in the chain.

### Calculation

The process of [mining](/docs/technical/mining.md) involves hashing a [block header](/docs/technical/block.md#header).

Every time you perform a hash, the [hash function](/docs/technical/cryptography/hash-function.md) spits out a *256-bit number*, which can be any number from `0` to:

```
0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
```

To successfully mine this block on to the blockchain, this hash result needs to be *less than or equal to the [target](/docs/technical/mining/target.md) value* for that particular height in the chain. The target for the [first ever block](/explorer/block/000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f) was set at:

```
0x00000000ffff0000000000000000000000000000000000000000000000000000
```

So to work out how many hashes you'd need to perform (on average) to get below this value, you **divide** the *maximum range of numbers* by the *number you want to get below*.

```
range = 2^256
below = 0x00000000ffff0000000000000000000000000000000000000000000000000000 + 1

hashes = range / below
hashes = 0x0100010001
```

This means you would need to perform `0x0100010001` (4295032833) hashes on average to get a result below this target value. Therefore, this was the actual chainwork for that first block.

So to work out the **total chainwork of a chain**, you just work out the expected hashes for each block and add them all up.

You can find out what the target was for each block by looking at the [bits](/docs/technical/block/bits.md) field in the [block header](/docs/technical/block.md#header).

#### Average Hashes Explained

Let's say you're randomly generating numbers between 1 and 100, and you're hoping to randomly generate a number of **5 or below**. On average, how many numbers would you need to generate before you get one below your target?

```
100 / 5 = 20
```

So on average **you'll need to generate 20 numbers** to get one that is below **5**.

This is exactly the same kind of calculation that takes place in Bitcoin, but just with bigger numbers (and usually calculated using [hexadecimal](/docs/technical/general/hexadecimal.md) values instead).

### Example

To give a quick example of how chainwork is calculated, let's calculate the chainwork for the **fourth block** in the blockchain.

The target did not adjust for the first 2016 blocks, so the average number of hashes required to mine each of these first 4 blocks will be the same:

```
Block 0
  Target: 0x00000000ffff0000000000000000000000000000000000000000000000000000
  Average Hashes: 2**256 / (Target + 1) = 4295032833

Block 1
  Target: 0x00000000ffff0000000000000000000000000000000000000000000000000000
  Average Hashes: 2**256 / (Target + 1) = 4295032833

Block 2
  Target: 0x00000000ffff0000000000000000000000000000000000000000000000000000
  Average Hashes: 2**256 / (Target + 1) = 4295032833

Block 3
  Target: 0x00000000ffff0000000000000000000000000000000000000000000000000000
  Average Hashes: 2**256 / (Target + 1) = 4295032833
```

The total chainwork will be the sum of the average number of hashes to mine each of these blocks:

```
Total Chainwork
  = 4295032833 + 4295032833 + 4295032833 + 4295032833
  = 17180131332
  = 0x400040004
```

We can check that our calculation is correct using `bitcoin-cli`:

```
bitcoin-cli getblockhash 3
0000000082b5015589a3fdf2d4baff403e6f0be035a5d9742c1cae6295464449

bitcoin-cli getblock 0000000082b5015589a3fdf2d4baff403e6f0be035a5d9742c1cae6295464449
{
    ...
  "chainwork": "0000000000000000000000000000000000000000000000000000000400040004",
    ...
}
```

## Purpose

Why do nodes adopt the longest chain?

Having nodes adopt the longest available chain allows computers across a network to agree on the same version of the blockchain.

Here are two situations where this proves to be useful:

### 1. Resolving disagreements when two blocks are mined at the same time.

Due to the fact that bitcoin operates on a [network](/docs/technical/networking.md), it's possible for two independent computers to mine a block at the same time. In this situation, nodes across the network will end up being in disagreement about which of these two blocks should be at the top of the blockchain.

[<img src="../../images/diagrams_png_blockchain-longest-chain-two-blocks-mined.png" alt="Diagram showing two blocks mined at the same time across the network causing a temporary fork in the chain." width="983" height="609" />](https://static.learnmeabitcoin.com/diagrams/png/blockchain-longest-chain-two-blocks-mined.png)


Each node puts the *first* block they receive at the top of their blockchain.

However, this situation can be resolved by having nodes adopt the longest chain of blocks. This is because the **next block to be mined** will build upon *one* of these two blocks, creating a new longest chain that all nodes on the network will be happy to adopt.

[<img src="../../images/diagrams_png_blockchain-longest-chain-two-blocks-mined-reorg.png" alt="Diagram showing a temporary fork being resolved via a chain reorganization." width="983" height="582" />](https://static.learnmeabitcoin.com/diagrams/png/blockchain-longest-chain-two-blocks-mined-reorg.png)


Nodes are happy to abandon the shorter chain in favor of the new longer one. This is known as a [chain reorganization](/docs/technical/blockchain/chain-reorganization.md).

So even though nodes can be in disagreement at any given time (due to the unpredictability of mining and the speed of broadcasting data across a network), adopting the longest available chain means that nodes will always *eventually* agree on the same view of the blockchain.

### 2. Protecting blocks already mined on to the blockchain.

The fact that nodes always adopt the longest chain as the valid version of the blockchain means that it is very difficult to replace blocks (and therefore transactions) already in the chain.

If someone wanted to replace a [transaction](/docs/technical/transaction.md) in the blockchain, they would need to work to build a **new longest chain to replace the current one**.

However, if the majority of miners are continually working to extend the same current longest chain, an individual miner won't be able to compete to outwork the combined effort of all the other miners.

[<img src="../../images/diagrams_png_blockchain-longest-chain-protection.png" alt="Diagram showing how adopting the longest chain makes it difficult for attackers to rewrite the blockchain." width="979" height="586" />](https://static.learnmeabitcoin.com/diagrams/png/blockchain-longest-chain-protection.png)


You would need the majority of mining power to be able to out-run all other miners and build a new longest chain (known as a [51% Attack](/docs/technical/blockchain/51-attack.md)).

As a result, the combined effort of miners coordinating to extend the same chain protects existing blocks and transactions from being replaced by a single miner.

> Think of it as a cooperative effort to make a chain.

Satoshi Nakamoto, [bitcointalk.org](https://bitcointalk.org/index.php?topic=6.msg31#msg31)

## FAQ

### Why do miners choose to build on the longest chain?

Because a miner can claim a [block reward](/docs/technical/mining/block-reward.md) if they are able to mine a block.

However, the bitcoins from this block reward can only be spent if the block becomes **100 blocks deep in the *longest chain***. Therefore, this block reward incentivizes miners to always try and mine new blocks that will become part of the longest chain (by always trying to build on to the current longest one).

[<img src="../../images/diagrams_png_blockchain-longest-chain-block-reward.png" alt="Diagram showing how a block reward can only be spent when the block reaches 100 blocks deep in the longest chain." width="707" height="336" />](https://static.learnmeabitcoin.com/diagrams/png/blockchain-longest-chain-block-reward.png)


A block reward can only be spent if the block is part of the longest chain.

Miners initially claim the block reward through the [coinbase transaction](/docs/technical/mining/coinbase-transaction.md).

### What happens to transactions that are not part of the longest chain?

A [transaction](/docs/technical/transaction.md) inside a block that is not part of the longest chain is **invalid**.

If you try to spend the [outputs](/docs/technical/transaction/output.md) from a transaction that is not in the longest chain, nodes would not accept this new transaction nor try to mine it into a block. This is because nodes only consider the **longest chain as the valid history of transactions**, and anything outside of that is not a valid transaction.

[<img src="../../images/diagrams_png_blockchain-longest-chain-invalid-transaction.png" alt="Diagram showing a transaction that is not part of the longest chain as being invalid." width="983" height="590" />](https://static.learnmeabitcoin.com/diagrams/png/blockchain-longest-chain-invalid-transaction.png)


The outputs in a transaction not in the longest chain are unspendable.

So only the transactions inside the longest chain are considered to be part of the valid transaction history, and any transactions outside of it effectively never took place.

**I recommend that you wait for a transaction to make it to 2 or more blocks deep into the blockchain before you consider bitcoins to be "yours".** There is always a chance that the topmost blocks in the blockchain could change due to a [chain reorganization](/docs/technical/blockchain/chain-reorganization.md), making previously valid blocks and transactions invalid.

## Commands

You can find the chainwork values for yourself using these `bitcoin-cli` commands:

### `bitcoin-cli getblockchaininfo`

See the total chainwork for the current longest chain.

```
$ bitcoin-cli getblockchaininfo
{
  "chain": "main",
  "blocks": 599501,
  "headers": 599767,
  "bestblockhash": "0000000000000000000cb6141c8076e24f3a1799eef37201634ef392197668f3",
  "difficulty": 13008091666971.9,
  ...
  "chainwork": "0000000000000000000000000000000000000000094b1874d991d4e1fc51005a",
  ...
}
```

### `bitcoin-cli getblock [blockhash]`

See the chainwork for any given block in the chain.

```
$ bitcoin-cli getblock 00000000b8980ec1fe96bc1b4425788ddc88dd36699521a448ebca2020b38699
{
  "hash": "00000000b8980ec1fe96bc1b4425788ddc88dd36699521a448ebca2020b38699",
  ...
  "height": 12345,
  ...
  "bits": "1d00ffff",
  "difficulty": 1,
  "chainwork": "0000000000000000000000000000000000000000000000000000303a303a303a",
  ...
}
```

## Summary

The adoption of the longest chain of blocks allows nodes on a network of computers to be able to share a globally accepted view of the blockchain. Furthermore, the fact that it requires energy to add new blocks to the chain makes it very difficult for any individual to replace blocks that have already been mined into the chain.

The "longest chain" usually refers to the chain with the greatest number of consecutive blocks, but technically it refers to the chain that has the *most work* in it based on how difficult it was to mine each block.

## Resources

* [What does the term "Longest chain" mean?](https://bitcoin.stackexchange.com/questions/5540/what-does-the-term-longest-chain-mean)
* [chain.cpp](https://github.com/bitcoin/bitcoin/blob/master/src/chain.cpp)