![Loading Tool](../../images/icons_loader-2.svg)

[![Diagram showing nodes on the Bitcoin network storing the latest transactions in their memory pool.](../../images/diagrams_png_memory-pool.png)](https://static.learnmeabitcoin.com/diagrams/png/memory-pool.png)

Current Mempool Size:

0.59 vMB

2,018 transactions

Note: This is the size of the mempool for my local node.  
The size of your memory pool will differ depending on how long your node has been online and which nodes you are connected to.

The memory pool (mempool) is a **waiting area** for new [transactions](/technical/transaction/).

New transactions are stored in a [node](/technical/networking/node/)'s memory pool while they're waiting to get [mined](/technical/mining/) on to the [blockchain](/technical/blockchain/).

**Do not rely on memory pool transactions.** Not all transactions will make it from the memory pool (temporary storage) to the blockchain (permanent storage).

## Purpose

Why does the memory pool exist?

The memory pool is used to **sort out conflicting transactions**.

You see, it's possible for two different transactions spending the same bitcoins to be inserted into different parts of the [network](/technical/networking/) at the same time. Some nodes will receive the one transaction first, and some nodes will receive the other transactions first:

[![Diagram showing two conflicting transactions (spending the same bitcoins) being inserted into different parts of the Bitcoin network.](../../images/diagrams_png_memory-pool-conflict.png)](https://static.learnmeabitcoin.com/diagrams/png/memory-pool-conflict.png)


Nodes will reject the second conflicting transaction they receive, but there will still be different versions of the conflicting transaction floating around the network.

Because both of these transactions are trying to spend the same bitcoins, only *one* of them should be written to the [blockchain](/technical/blockchain/). So which of these conflicting transactions should make it into the blockchain?

This conflict is resolved when one of the nodes on the network [mines](/technical/mining/) the transactions from *their* memory pool into a block:

[![Diagram showing one of the conflicting transactions getting mined into a block and the other getting kicked out of the memory pools.](../../images/diagrams_png_memory-pool-conflict-resolved.png)](https://static.learnmeabitcoin.com/diagrams/png/memory-pool-conflict-resolved.png)


One of the nodes will mine the next block of transactions and broadcast it across the network.

Upon receiving this newly-mined block, nodes will add this block on to the blockchain, and **kick out any conflicting transactions** from their memory pool.

So the memory pool is part of a *sorting mechanism* ([mining](/technical/mining/)) that prevents conflicting transactions from being written to the blockchain.

The memory pool plays a crucial role in preventing conflicting transactions from being written to the blockchain, and is the reason why you have to *wait* for transactions to get mined.

## Entry

How does a transaction enter the memory pool?

A transaction can enter a node's memory pool in a number of ways:

### 1. Inserted into a local node

(common)

[![Diagram showing a new transaction being inserted directly into a local node on the network.](../../images/diagrams_png_memory-pool-entry-insert.png)](https://static.learnmeabitcoin.com/diagrams/png/memory-pool-entry-insert.png)

A new transaction can be inserted directly into a node on the network.

From here the node will *broadcast* the transaction to the other nodes on the network so they can add it to their memory pool too.

You can manually insert a transaction into your local Bitcoin Core node using the `bitcoin-cli sendrawtransaction` command. Alternatively, your [wallet](/beginners/wallets/) will insert your transaction into a node when you send someone bitcoins.

### 2. Received from another node

(common)

[![Diagram showing a new transaction being received from another node on the network.](../../images/diagrams_png_memory-pool-entry-receive.png)](https://static.learnmeabitcoin.com/diagrams/png/memory-pool-entry-receive.png)

New transactions can be received from other nodes on the network.

Nodes continually broadcast the latest transactions they've received to the nodes they are connected to. So if a node advertises a transaction that your node does not have, your node will [request](/technical/networking/#requesting-transactions-and-blocks) it and add it to their memory pool too.

This process repeats until all nodes on the network have a copy of the latest transactions in their memory pools.

**Only valid transactions can enter the memory pool.** A node will check if each transaction they receive is valid (doesn't break any rules) before adding it to their memory pool or relaying it to the nodes they are connected to.

### 3. Re-entry after a chain reorganization

(uncommon)

[![Diagram showing a previously mined transactions re-entering the memory pool after a chain reorganization.](../../images/diagrams_png_memory-pool-entry-chain-reorganization.png)](https://static.learnmeabitcoin.com/diagrams/png/memory-pool-entry-chain-reorganization.png)

Previously mined transactions can re-enter the memory pool during a [chain reorganization](/technical/blockchain/chain-reorganization/).

Sometimes a node will perform a chain reorganization, where a new [longest chain](/technical/blockchain/longest-chain/) is found that replaces some of the blocks in the node's previous longest blockchain. If any of the transactions in the blocks being replaced are *not* found in the blocks of the new longest chain, they will get recycled back into your node's memory pool (and re-broadcast again) for the chance to get re-mined into a future block.

## Exit

How does a transaction leave the memory pool?

There are a number of reasons why a transaction will leave the memory pool:

### 1. Mined

[![Diagram showing a transaction leaving the memory pool due to being mined into a block.](../../images/diagrams_png_memory-pool-exit-mined.png)](https://static.learnmeabitcoin.com/diagrams/png/memory-pool-exit-mined.png)

This is the goal for all memory pool transactions.

When a miner [mines](/technical/mining/) a new block of transactions, they will broadcast it to the other nodes on the network. When a node receives this block, any transactions in their memory pool that are inside that block will be removed from their memory pool and connected to the block instead.

In other words, transactions are moved from temporary storage (the memory pool) to permanent storage (the blockchain).

### 2. Mined Conflict

[![Diagram showing a transaction leaving the memory pool due to a conflicting transaction being mined into a block.](../../images/diagrams_png_memory-pool-exit-mined-conflict.png)](https://static.learnmeabitcoin.com/diagrams/png/memory-pool-exit-mined-conflict.png)

Nodes will remove any transactions from their memory pool that conflict with the transactions inside a block.

The transactions inside a mined block are considered "correct", so if a node has a transaction in their memory pool that spends the same bitcoins as a transaction inside a block, they will kick that transaction out the memory pool.

In other words, the memory pool has done its job as being part of the sorting mechanism for conflicting transactions.

All the [descendants](#descendants) of a conflicting memory pool transaction will be removed at the same time.

### 3. Replaced

[![Diagram showing a transaction being removed from the memory pool due to being replaced by a higher-fee version.](../../images/diagrams_png_memory-pool-exit-replaced.png)](https://static.learnmeabitcoin.com/diagrams/png/memory-pool-exit-replaced.png)

A transaction will be removed from the memory pool if it gets replaced by a new higher-fee transaction.

This will happen if an existing transaction in the memory pool has the [replace-by-fee](/technical/transaction/input/sequence/#replace-by-fee) (RBF) setting, and then a new transaction gets broadcast to the network that *spends the same bitcoins* but with a suitably higher fee.

The new higher-fee version of the transaction is more likely to get mined on to the blockchain, so a node will kick out the old transaction in favor of the new one.

### 4. Time Limit

[![Diagram showing a transaction leaving the memory pool after a certain amount of time.](../../images/diagrams_png_memory-pool-exit-mempoolexpiry.png)](https://static.learnmeabitcoin.com/diagrams/png/memory-pool-exit-mempoolexpiry.png)

Each node has a [time limit setting](#mempoolexpiry) for how long they're willing to hold on to transactions in their memory pool.

So if a transaction in the memory pool doesn't get mined before it reaches the time limit, the node assumes the transaction *probably* isn't going to get mined and will remove it from their memory pool.

* The default time limit is **2 weeks**.
* You can always rebroadcast a transaction to the network if it leaves the memory pools due to exceeding the expiry time.

### 5. Size Limit

[![Diagram showing a low-fee transaction being removed from the memory pool when the memory pool reaches its maximum size setting.](../../images/diagrams_png_memory-pool-exit-maxmpool.png)](https://static.learnmeabitcoin.com/diagrams/png/memory-pool-exit-maxmpool.png)

Transactions will be removed from a node's memory pool when their memory pool reaches a certain size (in megabytes).

Each node has the ability to set a [maximum size](#maxmempool) for their memory pool. So when their memory pool exceeds this limit, they will start removing the lowest-fee transactions from their memory pool to make space for higher-fee transactions instead.

So if there are more transactions floating around the network than can fit in to your node's memory pool, your node will only keep the highest-fee transactions available.

* The default size limit is **300 MB**.
* Some nodes maintain very large memory pools, so it's unlikely that a low-fee transaction will completely leave the network due to other nodes' small memory pools.
* **The memory pool also stores *[metadata](#getmempoolentry)* for each transaction.** So only around 25% of memory pool data is made of raw transaction data.

## Settings

Each node keeps their own *individual* memory pool, and has the ability to use their own settings and rules for it.

If you're running a Bitcoin Core node, these are the most common [bitcoin.conf](https://github.com/bitcoin/bitcoin/blob/master/doc/bitcoin-conf.md) settings for your memory pool:

### `maxmempool=<n>`

default = 300 MB

This setting controls the **maximum size** of the memory pool in MB (megabytes).

Increasing the size of your nodes' memory pool with `maxmempool` is the easiest way to keep track of as many memory pool transactions as possible. However, this will use more RAM on your computer.

This setting includes the size of transaction *metadata* and is not the maximum size based on the size of raw transaction data alone.

### `mempoolexpiry=<n>`

default = 336 hours (2 weeks)

This setting controls **how many hours** your node will hold on to transactions in the memory pool after first receiving them.

### `minrelaytxfee=<amount>`

default = 0.00001 BTC/kvB (1 sat/vbyte)

This setting controls the **minimum transaction [feerate](/technical/transaction/fee/#feerates)** for a transaction to be added to your node's mempool.

This setting uses an awkward BTC/kvB (kilo [virtual byte](/technical/transaction/size/#vbytes)) setting for measuring feerates. The default of 0.00001 BTC/kvB is equivalent to 1 sat/vbyte.

![Tool Icon](../../images/icons_tool.svg) Unit Converter

BTC

whole bitcoin


mBTC

one-thousandth of a bitcoin


uBTC

one-millionth of a bitcoin


Sats

one-hundred-millionth of a bitcoin



0 secs

So although each memory pool can be unique, the most common setting for memory pools across the network are:

* A maximum size of **300 MB**.
* Keep transactions for up to **2 weeks**.
* Reject transactions that do not have a fee of at least **1 sat/byte**.

As a result, most nodes on the network will share a *similar* view of the memory pool at any given time.

## Minimum Fee

What is the minimum mempool fee?

[![Diagram showing the minimum feerate being dynamically calculated by the maximum size of the memory pool.](../../images/diagrams_png_memory-pool-minimum-fee.png)](https://static.learnmeabitcoin.com/diagrams/png/memory-pool-minimum-fee.png)

Each node maintains a **minimum feerate** to limit the transactions that are accepted into their memory pool.

This value increases when the memory pool exceeds its [size limit](#maxmempool).

For example, if the memory pool gets too big, the lowest-fee transactions will be evicted and the minimum feerate will increase to prevent lower-fee transactions from entering. Conversely, if the size of the memory pool drops back below its maximum size, the minimum feerate will drop to allow lower-fee transactions back in.

The default minimum mempool fee is **1 sat/byte**.

> When transactions are evicted from the mempool due to being at the bottom of a too-large mempool when sorted by feerate, the effective minrelayfee is raised to be the feerate of the evicted transactions.
>
> It continuously goes down, very slowly, halving every 3 to 12 hours, until it has to be bumped again due to an eviction.

Pieter Wuille, [bitcoin.stackexchange.com](https://bitcoin.stackexchange.com/questions/58083/is-it-possible-to-set-a-dynamic-minrelaytxfee)

### Calculation

This minimum feerate is controlled by `minrelayfee`.

* `minrelayfee` (dynamic) – This is the maximum of the following two values:
  + `minmempoolfee` (dynamic) – An internal value that moves up and down when your mempool hits its `maxmemool` size.
  + `minrelaytxfee` (static) – A fixed value that you can set in your node's [configuration file](https://github.com/bitcoin/bitcoin/blob/master/doc/bitcoin-conf.md).

So in other words, `minmempoolfee` is an internally-calculated value that dynamically adjusts based on the size of your mempool, and you can override this by setting a permanent minimum using `minrelaytxfee`. When Bitcoin is running, `minrelayfee` (the effective minimum feerate) is the greater of these two values.

## Structure

Does the memory pool have a structure?

The memory pool doesn't have a defined structure; it's just a **pool of unconfirmed transactions**.

However, the transactions in the memory pool include some additional [metadata](#getmempoolentry) to help with sorting for inclusion in a [candidate block](/technical/mining/candidate-block/).

This metadata includes things like; *[size](/technical/transaction/size/)*, *[fee](/technical/transaction/fee/)*, *[descendants](#descendants)*, and *[ancestors](#ancestors)*.

### Descendants

[![Diagram showing the descendants of a transaction in the memory pool.](../../images/diagrams_png_memory-pool-descendants.png)](https://static.learnmeabitcoin.com/diagrams/png/memory-pool-descendants.png)

A descendant is the **child of a memory pool transaction**.

In other words, it's a transaction that *spends an existing memory pool transaction*. So if a transaction is sitting in the memory pool, it's possible to create a *child* transaction that spends the [output](/technical/transaction/output/)(s) of that transaction, and send that transaction into the memory pool too.

Therefore, a transaction can have multiple descendants whilst it's sat in the memory pool.

**The parent of a child transaction must always get mined first.** A child transaction *depends* on its parent getting mined before it can get mined (because otherwise it would be trying to spend bitcoins that do not exist). The parent could get mined in an earlier block, or higher up in the same block as the child. Either way, you can't mine a child transaction without its parent.

**Descendant Limits.** A memory pool transaction can have a maximum of 25 descendants. The total size of the descendants is also limited to 101,000 [virtual bytes](/technical/transaction/size/#vbytes) (101 kvB). (see [policy.h](https://github.com/bitcoin/bitcoin/blob/master/src/policy/policy.h))

#### Descendant Feerate

Memory Pool Eviction

[![Diagram showing the descendant feerate as the average feerate of a transaction and all of its descendants.](../../images/diagrams_png_memory-pool-descendant-fee-rate.png)](https://static.learnmeabitcoin.com/diagrams/png/memory-pool-descendant-fee-rate.png)

The descendant feerate is the ***average feerate* of a transaction and all its descendants**.

It's used when determining *which transactions to evict* from the memory pool.

When a node's memory pool reaches its size limit, it will look to evict the lowest fee transactions first. But before evicting a transaction, it will look at its descendant feerate to see if it's worth keeping it in the memory pool.

For example:

* **Higher Descendant Feerate:** A single transaction may have a low-enough feerate to make it a candidate for eviction. However, if there is a descendant transaction with a very large feerate attached to it, the descendant feerate will be higher, so it might be worth keeping that particular transaction because it's more likely it will get mined into a block in the near future (because you can't mine a high-fee descendant without its parent).
* **Lower Descendant Feerate:** If a single transaction has a low enough feerate for eviction *and* the descendant feerate is the same (or lower), then we can happily evict that transaction and all of the descendants. This is because all the descendants *depend* on that transaction, so they're not going to be able to get mined into a block without it.

**Average Feerate.** The average feerate is the sum of the transaction fees divided by the sum of the transaction sizes. It's the same [feerate](/technical/transaction/fee/#feerates) calculation as with a single transaction, but spread across multiple transactions.

### Ancestors

[![Diagram showing the ancestors of a transaction in the memory pool.](../../images/diagrams_png_memory-pool-ancestors.png)](https://static.learnmeabitcoin.com/diagrams/png/memory-pool-ancestors.png)

An ancestor is the **parent of a memory pool transaction**.

A memory pool transaction *depends* on its ancestor(s) for getting mined into a block. This is because you can't include a transaction in a block that spends an [output](/technical/transaction/output/) that doesn't exist (or hasn't been created yet).

So if you look up any transaction in the memory pool, it's possible that it will have multiple ancestors, and these ancestors must get mined before that particular transaction can get mined.

#### Ancestor Feerate

Candidate Block Selection

[![Diagram showing the ancestor feerate as the average feerate of a transaction and all of its ancestors.](../../images/diagrams_png_memory-pool-ancestor-fee-rate.png)](https://static.learnmeabitcoin.com/diagrams/png/memory-pool-ancestor-fee-rate.png)

The ancestor feerate is the **average feerate of a transaction and all its ancestors**.

It's used when determining *which transactions to select* for inclusion in a [candidate block](/technical/mining/candidate-block/).

A miner has to include all the ancestors of a transaction in their block. So they work out the ancestor feerate for each transaction to determine whether it's worth including that specific transaction *and all of its ancestors*, versus including a different transaction with a similar feerate (but without any ancestors).

For example:

* **Lower Ancestor Feerate:** A single transaction may have a high-enough feerate to make it worth including in a candidate block. However, if it has ancestors with very low feerates, this brings the ancestor feerate down and could mean that it's not actually worth including the transaction in the block (compared to other transactions with a lower absolute feerate but no ancestors).
* **Higher Ancestor Feerate:** A higher ancestor feerate doesn't improve a transaction's chances of getting included in a block, as a miner can simply mine the ancestors and ignore the current transaction if the feerate isn't high enough.

**[Child Pays For Parent (CPFP)](/technical/transaction/fee/#cpfp).** You can increase the chances of getting a memory pool transaction mined by creating a child with a large fee. This will increase the average feerate, which makes the parent transaction more attractive to a miner.

## Location

Where is the memory pool stored?

The memory pool is stored in [RAM](https://www.crucial.com/articles/about-memory/support-what-does-computer-memory-do).

This means memory pool transactions can be **accessed as quickly as possible**, which provides multiple benefits:

* **Faster validation of new transactions.** Each new transaction needs to be checked to see if it conflicts with any of the transactions currently in the memory pool. Keeping memory pool transactions in RAM allows nodes to validate and relay new transactions more rapidly.
* **Faster relay of new blocks.** Every new block a node receives needs to be validated before it can be written to their blockchain and relayed to other nodes. If most of the transactions in the block are already in a node's mempool, it speeds up the validation of the block (as most of the transaction will have already been validated).
* **Faster candidate block construction.** Miners need to grab transactions from the memory pool when constructing their candidate blocks. If all of the memory pool transactions are held in RAM, it makes it much faster to sort them for selection.

In short, keeping the memory pool in RAM (as opposed to writing and reading to disk) helps a node to run more efficiently.

This also explains why the memory pool has a relatively "small" default [size](#maxmempool) of 300 MB (as RAM space is much smaller than disk space on a typical computer). However, this is still large enough to hold *multiple blocks* worth of transaction data in memory.

## Commands

There are three main commands for getting information about the memory pool from Bitcoin Core:

### `bitcoin-cli getmempoolinfo`

Shows statistics about your node's memory pool.

```
$ bitcoin-cli getmempoolinfo
{
    "loaded": true,
    "size": 2018,
    "bytes": 585810,
    "usage": 3687056,
    "total_fee": 0.00957916,
    "maxmempool": 200000000,
    "mempoolminfee": 1.0e-5,
    "minrelaytxfee": 1.0e-5,
    "incrementalrelayfee": 1.0e-5,
    "unbroadcastcount": 0,
    "fullrbf": true
}
```

### `bitcoin-cli getrawmempool`

Shows the [TXIDs](/technical/transaction/input/txid/) for all the transactions in your node's memory pool.

### `bitcoin-cli getmempoolentry <txid>`

Shows the details (including metadata) about a specific transaction in your node's memory pool.

For example:

```
{
  "vsize": 141,
  "weight": 561,
  "time": 1707864360,
  "height": 830390,
  "descendantcount": 2,
  "descendantsize": 282,
  "ancestorcount": 24,
  "ancestorsize": 4072,
  "wtxid": "2a088158bc6a69a1225de7e0465c749692bcf4f990db4b4c480fe804ea17851a",
  "fees": {
    "base": 0.00001128,
    "modified": 0.00001128,
    "ancestor": 0.00036896,
    "descendant": 0.00002538
  },
  "depends": [
    "95617833493987487f400cd8dc7c4874d6b8ec0898f2181f0a566ffc03b04a92"
  ],
  "spentby": [
    "d615139931d376c5f283db0259ca02d0ff1ee61f9b2b742fc7f82717675c9f41"
  ],
  "bip125-replaceable": true,
  "unbroadcast": false
}
```

## Notes

* **There is no such thing as "*the* memory pool".** In other words, there is no single memory pool that all new transactions go into, as each node keeps their own independent memory pool. As a result, the memory pools across nodes on the network will be slightly different at any given time.

  This is due to different mempool settings (e.g. `maxmempool`, `mempoolexpiry`, `minrelaytxfee`), transaction propagation speed, and the fact that there could be conflicting transactions floating around the network at the same time.

  However, there's typically a large overlap where most nodes will have similar transactions in their memory pools, so there's nothing wrong with using the term "the memory pool" to refer to the general state of the memory pools across the network.

  Just be prepared to be corrected on technical forums if you refer to it as "the memory pool".
* **The default mempool expiry time is 2 weeks.** It used to be 3 days, but it was increased to 14 days in 2017 with the release of Bitcoin Core [v0.14.0](https://github.com/bitcoin/bitcoin/blob/master/doc/release-notes/release-notes-0.14.0.md).
* **When a transaction leaves the memory pool, it's as though it never happened.** So don't rely on memory pool transactions when accepting payments. If the transaction leaves the memory pool without getting mined, then it might as well have never taken place. The only way to get it back into the memory pool would be to re-broadcast to the network.

## Resources

* [Brink Podcast – Episode 2: Mempool Ancestors and Descendants](https://brink.dev/podcast/2-mempool-ancestors-descendants/)
* [Bitcoin Optech – Waiting for confirmation: a series about mempool and relay policy](https://bitcoinops.org/en/blog/waiting-for-confirmation/)
* [Is it possible to set a dynamic -minrelaytxfee?](https://bitcoin.stackexchange.com/questions/58083/is-it-possible-to-set-a-dynamic-minrelaytxfee)