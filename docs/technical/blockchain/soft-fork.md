<img src="../../images/icons_loader-2.svg" alt="Loading Tool" style="height:32px; width:32px;" />

[<img src="../../images/diagrams_png_blockchain-forks-soft-fork.png" alt="Diagram showing a soft fork in the blockchain." width="543" height="457" />](https://static.learnmeabitcoin.com/diagrams/png/blockchain-forks-soft-fork.png)

A soft fork is when an upgrade is made to the Bitcoin software that is *compatible* with the previous versions of the software.

To summarize the difference between a soft fork and a [hard fork](/docs/technical/blockchain/hard-fork.md):

* A **hard fork** *expands* the rules on what makes a valid block/transaction.
* A **soft fork** *restricts* the rules on what makes a valid block/transaction.

With a soft fork, [nodes](/docs/technical/networking/node.md) that do not upgrade their software will still be able to accept [blocks](/docs/technical/block.md)/[transactions](/docs/technical/transaction.md) created by the upgraded software. Therefore, nodes that do not upgrade will be able to keep up to date with the [blockchain](/docs/technical/blockchain.md) and not get left behind.

[<img src="../../images/diagrams_png_blockchain-forks-soft-fork-network.png" alt="Diagram showing a soft fork on the bitcoin network, with old nodes that have not upgraded receiving the new blocks from the upgraded nodes." width="983" height="601" />](https://static.learnmeabitcoin.com/diagrams/png/blockchain-forks-soft-fork-network.png)

To make a soft-forking change successful, you only need a *majority* of the [miners](/docs/technical/mining.md) on the network to upgrade to the new version of the software. Because if you have a majority of miners upgrade, their mining power will build the [longest chain](/docs/technical/blockchain/longest-chain.md) of upgraded blocks (which the old nodes will adopt).

## Scenario

How do you create a soft fork?

To create a soft fork, you need to *restrict* the rules on what is considered a valid block or transaction.

In other words, you need to make **previously valid blocks/transactions invalid**.

For example, let's say the block size limit is 1 MB (block capacity is now measured in [weight](/docs/technical/block.md#weight), but don't worry about that for now). A soft-forking change would be to create a new rule that restricts the block size to **0.5 MB** instead (sounds like a step backwards, I know, but this is just an example).

When upgraded miners begin to mine these smaller blocks, old nodes will still see these new blocks as valid, so there will be no branching of the blockchain like there would be in a [hard fork](/docs/technical/blockchain/hard-fork.md).

[<img src="../../images/diagrams_png_blockchain-forks-soft-fork-compatibility.png" alt="Diagram showing old nodes on the network accepting the new blocks (from the soft fork upgrade) on to their blockchain." width="983" height="518" />](https://static.learnmeabitcoin.com/diagrams/png/blockchain-forks-soft-fork-compatibility.png)

## Method

How do you make a soft fork successful?

To make a soft fork successful, you want a **majority of miners to upgrade** to the new version of the software.

This is because nodes will always accept the [longest chain](/docs/technical/blockchain/longest-chain.md) of blocks, so if the majority of miners are working on mining the upgraded blocks with the restricted rules, the old nodes will naturally adopt it as their blockchain.

[<img src="../../images/diagrams_png_blockchain-forks-soft-fork-majority.png" alt="Diagram showing nodes adopting the longest chain of new blocks, despite some miners still mining old blocks." width="983" height="548" />](https://static.learnmeabitcoin.com/diagrams/png/blockchain-forks-soft-fork-majority.png)

So even if a minority of old miners continue to build the blockchain with old blocks, they will not be able to compete with the speed at which the new blocks are being mined by the upgraded miners, so old nodes will adopt the same version of the blockchain as the upgraded nodes.

## Risks

What are the risks of a soft fork?

The main risk with a soft fork is if you **do not get a majority of the miners to upgrade**.

This will result in the blockchain splitting in two, as a majority of old miners will continue to mine old blocks that are incompatible with the new version of the software.

[<img src="../../images/diagrams_png_blockchain-forks-soft-fork-split.png" alt="Diagram showing a majority of old miners building the longest chain with old blocks, creating a chain split between a blockchain with old blocks and a blockchain with upgraded blocks." width="983" height="601" />](https://static.learnmeabitcoin.com/diagrams/png/blockchain-forks-soft-fork-split.png)

And because old blocks form the longest available chain, old nodes will adopt this as their blockchain. However, the upgraded nodes will reject these old blocks (because those blocks are now invalid according to their upgraded rules), and they will adopt the longest available chain containing only the new blocks instead.

So once again, just like in a hard fork, you have two parallel versions of the blockchain; one containing old blocks, and another containing new blocks.

However, unlike a hard fork where the two chains can never converge, this chain split can be resolved by **getting more mining power on to the new chain**. If the upgraded miners are able to build the longest chain, the old nodes will perform a [chain reorganization](/docs/technical/blockchain/chain-reorganization.md) to adopt the blockchain made out of the new blocks.

[<img src="../../images/diagrams_png_blockchain-forks-soft-fork-reconverge.png" alt="Diagram showing old nodes reorganizing their chain once a majority of miners build the longest chain with the new blocks." width="983" height="601" />](https://static.learnmeabitcoin.com/diagrams/png/blockchain-forks-soft-fork-reconverge.png)

So by getting a majority of miners to upgrade, you "encourage" everyone on the network to keep up to date with the same version of the blockchain.

## Compromises

What is the downside to a soft fork?

The biggest downside to soft forks is that they tend to make the software **more complex** ([Segregated Witness](/docs/technical/upgrades/segregated-witness.md) is a prime example).

It would be easier to make direct upgrades to the software through [hard forks](/docs/technical/blockchain/hard-fork.md). However, a hard-forking change is undesirable due to the greater risk of a chain split (and having to force everyone to upgrade), so most upgrades are made through soft forks instead.

As a result, the fact that you have to keep the changes compatible with the *old software* means you have to make **more technical workarounds**, and this makes the software more complex than if you had the freedom to make changes that would be incompatible with old nodes.

In short:

* A **hard fork** allows you to directly replace rules and code.
* A **soft fork** involves *adding more code* to account for new rules.

## Examples

Have there been any soft forks in bitcoin?

All major upgrades to Bitcoin so far have been deployed as soft forks.

Here are some examples, including a summary of the *new restrictions* they introduced:

### 1. [BIP 16](https://github.com/bitcoin/bips/blob/master/bip-0016.mediawiki): Pay to Script Hash

03 January 2012

#### Problem

There was no convenient way to get other people to use custom locks of your choice when sending you bitcoins.

#### Restriction

A specific [ScriptPubKey](/docs/technical/transaction/output/scriptpubkey.md) pattern now has additional validation rules (see [P2SH](/docs/technical/script/p2sh.md)).

So whereas the locking script pattern `OP_HASH160` `OP_PUSHBYTES_20` `digest` `OP_EQUAL` previously only required you to provide some data that hashed to `digest` to unlock it, you now need to provide some data in the form of a custom locking script that hashes to `digest` *and* can be evaluated and unlocked in a second step of execution.

In other words, additional rules were added for how a specific locking script can be unlocked.

### 2. [BIP 30](https://github.com/bitcoin/bips/blob/master/bip-0030.mediawiki): Duplicate transactions

22 February 2012

#### Problem

It was not thought to be possible that you could have duplicate transactions in Bitcoin.

However, [coinbase transactions](/docs/technical/mining/coinbase-transaction.md) in different blocks could have the same [TXID](/docs/technical/transaction/input/txid.md), allowing for duplicate transactions in the blockchain. This would also allow for further duplicate transactions to be created later on.

#### Restriction

Blocks are not allowed to contain a transaction with a TXID that matches an earlier, not-fully-spent transaction in the same chain.

### 3. [BIP 34](https://github.com/bitcoin/bips/blob/master/bip-0034.mediawiki): Block v2, Height in Coinbase

06 July 2012

#### Problem

Even after the introduction of BIP 30 (see above), it was still possible for miners to construct duplicate coinbase transactions in different blocks.

#### Restriction

A [coinbase transactions](/docs/technical/mining/coinbase-transaction.md) must contain the block [height](/docs/technical/blockchain/height.md) as the first field in the [ScriptSig](/docs/technical/transaction/input/scriptsig.md). This ensures that every coinbase transaction will be unique (and therefore have a unique [TXID](/docs/technical/transaction/input/txid.md)).

Any coinbase transaction that did not contain the height of the current block would now be invalid.

### 4. [BIP 65](https://github.com/bitcoin/bips/blob/master/bip-0065.mediawiki): OP\_CHECKLOCKTIMEVERIFY

01 October 2014

#### Problem

There was no mechanism to make a transaction [output](/docs/technical/transaction/output.md) unspendable until a future date.

#### Restriction

The `OP_NOP2` opcode was repurposed for `OP_CHECKLOCKTIMEVERIFY`.

As a result, the `OP_NOP2` opcode no longer "did nothing", and scripts using it would no longer execute successfully without additional rules being satisfied.

### 5. [BIP 66](https://github.com/bitcoin/bips/blob/master/bip-0066.mediawiki): Strict DER signatures

10 January 2015

#### Problem

Lack of consistency with the encoding of [signatures](/docs/technical/keys/signature.md) in transactions due to a reliance on the [OpenSSL](https://www.openssl.org/) library.

#### Restriction

Restrict signatures to follow a single [encoding format](/docs/technical/keys/signature.md#der). This makes it easier for implementations of Bitcoin to not have to rely on OpenSSL as a dependency.

### 6. [BIP 141](https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki): [Segregated Witness](/docs/technical/upgrades/segregated-witness.md)

21 December 2015

#### Problem

The [TXID](/docs/technical/transaction/input/txid.md) could be modified after sending a [transaction](/docs/technical/transaction.md) into the [network](/docs/technical/networking.md), which meant you couldn't depend on the TXID for referencing the transaction later on.

This was because the TXID was made *including* the [signatures](/docs/technical/keys/signature.md) inside the transaction, and these signatures could be modified after they are created (yet still remain valid).

#### Restriction

Two new patterns of [ScriptPubKey](/docs/technical/transaction/output/scriptpubkey.md) ([P2WPKH](/docs/technical/script/p2wpkh.md), [P2WSH](/docs/technical/script/p2wsh.md)) that were once spendable by anyone are now only spendable under certain conditions.

This allows for a new transaction data structure, where the signatures sit at the end of the transaction data (in a new [witness](/docs/technical/transaction/witness.md) area) and are not included in the creation of the TXID.

**Segregated Witness also allowed for a block size increase.** This was made possible by not sending the new witness section of transactions (containing the signatures) to the old nodes. The old nodes would see these outputs as spendable by anyone anyway, so the signatures were not required for the transactions to be considered valid.

### 7. [BIP 341](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki): [Taproot](/docs/technical/upgrades/taproot.md)

19 January 2020

#### Problem

A [ScriptPubKey](/docs/technical/transaction/output/scriptpubkey.md) reveals all of its spending conditions inside the transaction data. These can be complex and large, and displaying all the spending conditions isn't good for privacy.

#### Restriction

A new pattern of ScriptPubKey ([P2TR](/docs/technical/script/p2tr.md)) that was once spendable by anyone is now only spendable under certain conditions. This allows for a new locking and unlocking mechanism that only reveals *one* spending condition (and not all the other spending conditions that may have existed for the lock).

## Deployment

How are soft forks deployed?

The goal of a successful soft fork is to get a majority of miners to agree to the upgrade.

So before the soft-forking change is activated, miners are asked to **signal their readiness** beforehand. Miners can signal readiness by setting a specific bit in the [version](/docs/technical/block/version.md) field of the block header.

For example:

```
00100000 00000000 00000000 00000001 = Bit 0 = CHECKSEQUENCEVERIFY (BIP 65)
00100000 00000000 00000000 00000010 = Bit 1 = Segregated Witness (BIP 141)
00100000 00000000 00000000 00000100 = Bit 2 = Taproot (BIP 341)
```

<img src="../../images/icons_tool.svg" alt="Tool Icon" style="width:20px; height:20px" /> Version Bits

Random Example

Bit Field

0

0

1

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



Hex

0x

`4 bytes`




* **Version Bits:** Enabled

When 90-95% of miners are signaling that they are in agreement with the upgrade within a [target adjustment period](/docs/technical/mining/target.md#period) (and that they will mine the new blocks with the new rules), the soft fork gets "locked in", and at a specific block [height](/docs/technical/blockchain/height.md) the miners will begin to mine the new blocks.

* The first 3 bits in the version must be set to `001` to be able to signal readiness for soft forks.
* Earlier soft forks (e.g. [BIP 16](https://github.com/bitcoin/bips/blob/master/bip-0016.mediawiki)) were deployed before this specific signaling system was set up.
* Soft forks usually require 95% of miners to signal for activation, but for [Taproot](/docs/technical/upgrades/taproot.md) this was changed to only require 90%.

## Summary

A *soft fork* is an upgrade to the Bitcoin software that is **compatible with old versions of the software**. It maintains this compatibility by *restricting the rules* around valid blocks/transactions, as opposed to relaxing them like in a [hard fork](/docs/technical/blockchain/hard-fork.md).

The primary benefit of a soft fork is that all [nodes](/docs/technical/networking/node.md) on the network can keep up to date with the [blockchain](/docs/technical/blockchain.md) even if they do not upgrade.

The key to a successful soft fork is to get a majority of miners to upgrade to the new version of the software. By doing so, miners will have the power to build the [longest chain](/docs/technical/blockchain/longest-chain.md) of new blocks/transactions, and old nodes will naturally adopt this longest chain containing the upgraded blocks.

All upgrades to the Bitcoin software so far have been made via soft forks.

## Resources

* [What is a soft fork? What is a hard fork? What are their differences?](https://bitcoin.stackexchange.com/questions/30817/what-is-a-soft-fork-what-is-a-hard-fork-what-are-their-differences)
* [Why is a softfork unable to divide the network?](https://bitcoin.stackexchange.com/questions/75543/why-is-a-softfork-unable-to-divide-the-network)
* [Where can I find a record of blockchain soft forks?](https://bitcoin.stackexchange.com/questions/43538/where-can-i-find-a-record-of-blockchain-soft-forks)
* [How is SegWit a soft fork?](https://bitcoin.stackexchange.com/questions/52152/how-is-segwit-a-soft-fork)