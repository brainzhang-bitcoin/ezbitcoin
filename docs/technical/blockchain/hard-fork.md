<img src="../../images/icons_loader-2.svg" alt="Loading Tool" style="height:32px; width:32px;" />

[<img src="../../images/diagrams_png_blockchain-forks-hard-fork.png" alt="Diagram showing a hard fork in the blockchain." width="560" height="457" />](https://static.learnmeabitcoin.com/diagrams/png/blockchain-forks-hard-fork.png)

A hard fork happens when an upgrade is made to the Bitcoin software that is *incompatible* with previous versions of the software.

This is when changes are made to the rules so that previously invalid [blocks](/docs/technical/block.md)/[transactions](/docs/technical/transaction.md) will now be considered valid in the new version of the software.

As a result, unless everyone upgrades to the new software, the [blockchain](/docs/technical/blockchain.md) will split in two different directions:

1. A chain that is made up of blocks that follow the **old rules**.
2. A chain that is made up of blocks that follow the **new rules**.

[<img src="../../images/diagrams_png_blockchain-forks-hard-fork-network.png" alt="Diagram showing a hard fork on the bitcoin network." width="983" height="601" />](https://static.learnmeabitcoin.com/diagrams/png/blockchain-forks-hard-fork-network.png)

The old [nodes](/docs/technical/networking/node.md) cannot accept these new blocks, so **two parallel blockchains** will exist. This is known as a "hard fork" in the chain.

Therefore, if you want a hard-forking change to the software to be successful, you want every node on the network to agree with the changes and upgrade their software. This is the only way everyone will keep up to date with the same version of the blockchain after the upgrade.

A "hard fork" can refer to a change made to the Bitcoin *software*, or the state of the *blockchain* after the change has been made. In this article I will use the following terms:

* *hard-forking change* – The upgrade to the software.
* *hard fork* – What happens to the blockchain when new incompatible blocks are mined.

## Scenario

How do you create a hard fork?

To create a hard fork, you need to change the rules of the software to allow for **previously invalid blocks/transactions to be considered valid**.

To give a simple example, let's say the block size limit is 1 MB (block capacity is now measured in [weight](/docs/technical/block.md#weight), but don't worry about that for now), and let's say we upgrade the software to accept blocks up to **10 MB**.

The hard-forking change begins when miners upgrade to the new version. The actual hard fork in the blockchain takes place when the first 10 MB block is mined.

* New miners will start building a chain with 10 MB blocks.
* Old miners will continue building a chain with 1 MB blocks only, and reject the new 10 MB blocks.

[<img src="../../images/diagrams_png_blockchain-forks-hard-fork-start.png" alt="Diagram showing the start of a hard fork in the blockchain when a new block is mined breaking the old rules." width="983" height="601" />](https://static.learnmeabitcoin.com/diagrams/png/blockchain-forks-hard-fork-start.png)

This hard fork will persist as long as the new chain (containing incompatible 10 MB blocks) remains as the [longest chain](/docs/technical/blockchain/longest-chain.md) on the network.

If the old miners are in the majority and build the longest chain with 1 MB blocks, the upgraded nodes will accept this as their version of the blockchain (because they still accept the old blocks), and the hard fork will be nullified.

## Causes

What can cause a hard fork?

Anything that **breaks the existing consensus rules** will result in a hard fork.

For example:

1. **Changes to block structure.**
   * e.g. A direct increase to the maximum block size.
2. **Changes to transaction structure.**
   * e.g. Changing the [cryptography](/docs/technical/cryptography.md) used for [signatures](/docs/technical/keys/signature.md) on existing transactions.
3. **Changes to other consensus rules.**
   * e.g. Increasing the maximum supply of bitcoin.
   * e.g. Manually adjusting the [target](/docs/technical/mining/target.md) to make it easier to mine blocks.

So whilst not all updates to Bitcoin require a hard fork, anything that changes the way Bitcoin fundamentally operates can only be achieved via a hard fork.

## Motivation

Why would you create a hard fork?

A hard-forking change is the **only way to make consensus-breaking updates** to the bitcoin software.

So if you want to make an upgrade to bitcoin, but the only way to do it is to break the rules that all of the nodes on the network are currently following, then a hard fork is your only option.

You can make changes to the rules using what's known as a [soft fork](/docs/technical/blockchain/soft-fork.md). However, depending on the complexity of the upgrade, a hard fork would typically be the *simpler* option for making changes to the Bitcoin software.

## Problems

Why wouldn't you want to create a hard fork?

There are two main problems with a hard fork:

### 1. Everyone has to upgrade.

**Anyone who does not upgrade will be left behind.** They will not receive the new incompatible blocks, and so they will be left in the dark about the latest transactions on the network.

[<img src="../../images/diagrams_png_blockchain-forks-hard-fork-left-behind.png" alt="Diagram showing a node's blockchain falling behind due to not upgrading after a hard-forking change has been made to the software." width="983" height="601" />](https://static.learnmeabitcoin.com/diagrams/png/blockchain-forks-hard-fork-left-behind.png)

In other words, people running the old software will fall behind and will be unaware of any new payments they may have received. They will not lose any of their bitcoins, but they will no longer be able to participate in the system as normal.

This is not a user-friendly way to upgrade a peer-to-peer [network](/docs/technical/networking.md).

### 2. A disagreement will divide the network.

The worst case scenario would be a "contentious hard fork". This is where some miners on the network agree to the upgrade, but a significant portion does not.

This will result in the blockchain branching into two parallel blockchains, effectively **splitting the currency** in two different directions.

[<img src="../../images/diagrams_png_blockchain-forks-hard-fork-currency-split.png" alt="Diagram showing bitcoin as a currency splitting in two different directions after a contentious hard fork." width="983" height="601" />](https://static.learnmeabitcoin.com/diagrams/png/blockchain-forks-hard-fork-currency-split.png)

This would cause confusion amongst users and merchants; who accepts which branch of the currency? How do you make sure you are transacting on the correct branch of the chain?

This confusion would undermine the overall trust in the system, and would likely cause a collapse in the value of bitcoin that it may not recover from. This is not an ideal outcome if the goal is to create a stable digital currency.

> The incentive for consensus is huge, as disagreement effectively means granting every old coin held to spend it once on each side.

Pieter Wuille, [Bitcoin StackExchange](https://bitcoin.stackexchange.com/questions/9986/how-is-a-hard-fork-resolved)

**A split between miners will also split the mining power between the two chains.** Each chain would therefore be *less secure*, as each chain will have less power to protect against a [51% attack](/docs/technical/blockchain/51-attack.md).

**Old miners could nullify the upgrade by continuing to build the longest available chain of old blocks.** Unless of course the upgrade also made the old blocks invalid from the upgrade onwards for some reason, in which case there would be a permanent chain split.

## Benefits

When would you want to create a hard-forking change to Bitcoin?

Due to the risk of splitting the blockchain in to two, a hard-forking change is **avoided** to make *general improvements* to the Bitcoin software.

For example, there are a few minor bugs that could be easily fixed with a hard fork:

* **Fixing the `OP_CHECKMULTISIG` [Script](/docs/technical/script.md) opcode.** This opcode pops off one more item from the stack than it should (see [P2MS](/docs/technical/script/p2ms.md)).
* **Increasing the size of the [nonce](/docs/technical/block/nonce.md) field in the block header.** The nonce field is too small, which means miners have to resort to modifying the [coinbase transaction](/docs/technical/mining/coinbase-transaction.md) (see [ExtraNonce](/docs/technical/block/nonce.md#extranonce)) to continue [mining](/docs/technical/mining.md) the block after all the possible numbers in the nonce field have been exhausted.
* **Consistency with [byte order](/docs/technical/general/byte-order.md).** The [block hash](/docs/technical/block/hash.md) is displayed in [reverse byte order](/docs/technical/general/byte-order.md#reverse-byte-order) when searching for a block on an [explorer](/explorer/), but the block hashes used inside raw block data are in [natural byte order](/docs/technical/general/byte-order.md#natural-byte-order). It would be easier for developers if all block hashes were in *reverse byte order* internally.

However, the minor benefits of these changes would not outweigh the risks of getting everyone to upgrade in a hard-forking change to the software.

As a result, hard fork updates are reserved for **urgent fixes** to potentially catastrophic events. This could be something like:

* **Switching away from the SHA-256 [hash function](/docs/technical/cryptography/hash-function.md).** This would be required if a weakness is found that undermines the effort required to mine blocks.
* **Manually increasing the target value (i.e. reducing the [difficulty](/docs/beginners/guide/difficulty.md)).** This would be required if there was an irrecoverable loss of mining power on the network, which would result in painfully slow block intervals. Without a hard fork, it could take months before the next target adjustment and for transactions to be mined in a timely manner again.

This is why all upgrades to Bitcoin so far have been implemented as soft forks; a hard fork is only likely to happen in the event of a fundamental problem arising with how the system works.

## Examples

Have there been any hard forks in Bitcoin's history?

There have been no *intentional* hard-forking changes put forward by Bitcoin Core developers.

However, there have been two software upgrades that caused (or could have caused) an accidental hard fork:

### 1. BerkeleyDB to LevelDB upgrade

[v0.7.0]( https://github.com/bitcoin/bitcoin/blob/master/doc/release-notes/release-notes-0.7.0.md) to [v0.8.0](https://github.com/bitcoin/bitcoin/blob/master/doc/release-notes/release-notes-0.8.0.md)

Bitcoin uses a separate [chainstate database](https://github.com/in3rsha/bitcoin-chainstate-parser) to keep track of all the [UTXOs](/docs/technical/transaction/utxo.md). Versions prior to v0.8.0 used the [BerkeleyDB](https://www.oracle.com/database/technologies/related/berkeleydb.html) database.

Due to the way BerkeleyDB works, it imposed a limit on the number of [inputs](/docs/technical/transaction/input.md) that could be included inside a [block](/docs/technical/block.md). This created an unexpected and unintentional network consensus rule about what makes a valid block.

When BerkeleyDB was replaced by [LevelDB](https://github.com/google/leveldb) in v0.8.0, this unknown limitation was removed. On 12 March 2013, a block was mined containing more inputs than a pre-v0.8.0 node would accept, creating an unintentional hard fork between nodes on v0.7.0 and nodes on v0.8.0.

This was initially remedied by asking miners to downgrade to v0.7.0, which meant that the majority of the mining power was back on the old v0.7.0 chain. This led to the v0.7.0 chain becoming the longest chain once again, and all nodes on v0.8.0 [reorganized](/docs/technical/blockchain/chain-reorganization.md) back to this chain, temporarily solving the problem and forcing all nodes back on to the v0.7.0 chain.

Over the next two months, all nodes on v0.7.0 were urged to upgrade to the latest version of v0.8.1. A permanent hard-forking block was then mined on 16 August 2013 at block height [252,451](/explorer/block/0000000000000024b58eeb1134432f00497a6a860412996e7a260f47126eed07), removing the limit on the number of inputs that could be included in a block.

* [Original thread documenting the v0.8.0 hard fork](https://bitcointalk.org/index.php?topic=152348.0)
* [BIP: 50 (March 2013 Chain Fork Post-Mortem)](https://github.com/bitcoin/bips/blob/master/bip-0050.mediawiki)

### 2. Double spend vulnerability (CVE-2018-17144)

[v0.14.0](https://github.com/bitcoin/bitcoin/blob/master/doc/release-notes/release-notes-0.14.0.md) to [v0.15.0](https://github.com/bitcoin/bitcoin/blob/master/doc/release-notes/release-notes-0.15.0.md)/[v0.16.2](https://github.com/bitcoin/bitcoin/blob/master/doc/release-notes/release-notes-0.16.2.md)

The software versions between 0.15.0 and 0.16.2 *could* have caused a potential hard fork, but the vulnerability was patched before it could be exploited, so no actual hard fork took place.

In short, versions 0.15.0 to 0.16.2 would allow for a miner to double-spend the same UTXO if it was included as an [input](/docs/technical/transaction/input.md) multiple times in the same transaction. Only miners would be able to perform this attack, as nodes would only accept this transaction if it was already mined into a block (they would reject the transaction on its own otherwise).

This double-spend vulnerability was fixed in [0.16.3](https://github.com/bitcoin/bitcoin/blob/master/doc/release-notes/release-notes-0.16.3.md), and no actual hard fork took place.

* [Bitcoin Core Bug CVE-2018–17144: An Analysis](https://hackernoon.com/bitcoin-core-bug-cve-2018-17144-an-analysis-f80d9d373362)

## Summary

A *hard fork* is when you make an upgrade to the Bitcoin software that will produce new [blocks](/docs/technical/block.md)/[transactions](/docs/technical/transaction.md) that are **incompatible with the old version of the software**.

To make a successful hard fork, you want everyone running Bitcoin (i.e. [nodes](/docs/technical/networking/node.md) and [miners](/docs/technical/mining.md)) to upgrade to the new version of the software. This is so everyone will receive these new blocks, and agree on the same upgraded version of the [blockchain](/docs/technical/blockchain.md).

If miners disagree about the upgrade and continue to mine blocks with both the old and new versions of the software, the blockchain will branch into two parallel blockchains. This would split bitcoin into two separate currencies and undermine the integrity of the system, which would be bad for Bitcoin.

There have yet to be any intentional hard-forking changes to Bitcoin. Instead, general upgrades to the software are preferred to be made using [soft forks](/docs/technical/blockchain/soft-fork.md).

## Resources

* [bitcoin.it/wiki/Hardfork](https://en.bitcoin.it/wiki/Hardfork)
* [bitcoin.it/wiki/Hardfork\_Wishlist](https://en.bitcoin.it/wiki/Hardfork_Wishlist)
* [Has a hard fork ever occurred?](https://bitcoin.stackexchange.com/questions/36090/has-a-hard-fork-ever-occurred)
* [Why is it dangerous to hard fork the Bitcoin network?](https://bitcoin.stackexchange.com/questions/42442/why-is-it-dangerous-to-hard-fork-the-bitcoin-network)
* [How is a hard fork resolved?](https://bitcoin.stackexchange.com/questions/9986/how-is-a-hard-fork-resolved)
* [Does a soft fork result in two different blockchain versions?](https://bitcoin.stackexchange.com/questions/99221/does-a-soft-fork-result-in-two-different-blockchain-versions)
* [After hard fork won't every new transaction go on both chains?](https://bitcoin.stackexchange.com/questions/52245/after-hard-fork-wont-every-new-transaction-go-on-both-chains)