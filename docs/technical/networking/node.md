![Loading Tool](../../images/icons_loader-2.svg)

[![Diagram showing a node as part of a network of computers running the Bitcoin program.](../../images/diagrams_png_node.png)](https://static.learnmeabitcoin.com/diagrams/png/node.png)

A node is a computer running the Bitcoin program.

It connects to other nodes on the [network](/docs/technical/networking.md) to share information about [transactions](/docs/technical/transaction.md) and [blocks](/docs/technical/block.md).

> A node is any device that sends, receives, or processes data connected to a network.

[techjury.net](https://web.archive.org/web/20250419134646/https://techjury.net/blog/what-is-a-node-in-networking/)

The easiest way to become a node is to download and run the [Bitcoin Core](https://bitcoincore.org/en/download/) software.

## Job

What does a node do?

A node has two main jobs:

### 1. Keep a copy of the blockchain

[![Diagram showing a node joining the Bitcoin network and downloading a copy of the blockchain.](../../images/diagrams_png_node-blockchain.png)](https://static.learnmeabitcoin.com/diagrams/png/node-blockchain.png)

When you run Bitcoin for the first time, it will connect to other nodes on the network to download a full copy of the [blockchain](/docs/technical/blockchain.md).

This allows your node to **get up to date** with the current state of the blockchain, so you can start receiving (and validating) the latest transactions and blocks being sent around the network.

Downloading the full blockchain also means that it's **replicated on another computer**. This *reinforces* the network, because anyone looking to destroy Bitcoin would need to try and remove every copy of the blockchain. And by keeping a copy of the blockchain you will help to replicate it to other nodes who join the network in the future.

Current Blockchain Size:

856.91 GB

956,472 blocks

Note: This is the size of the blockchain for my local node.  
The size of your blockchain will differ depending on how many [chain reorganizations](/docs/technical/blockchain/chain-reorganization.md) your node has experienced and how many [stale blocks](/docs/technical/blockchain/chain-reorganization.md#stale-blocks) you have stored on disk.

Bitcoin is a lot like [torrent](https://en.wikipedia.org/wiki/BitTorrent), where many different computers are seeding the same file (the blockchain).

### 2. Validate and relay new transactions and blocks.

After downloading the latest copy of the blockchain, a node can **start receiving the latest [transactions](/docs/technical/transaction.md) and [blocks](/docs/technical/block.md)**.

Each node checks the transactions and blocks it receive against a set of rules to make sure they are *valid*, before relaying them on to the nodes they are connected to.

As a result, a node is constantly working to **enforce rules** and **transmit data** across the network.

#### Transaction relay:

[![Diagram showing nodes relaying new transactions across the network and adding them to their memory pools.](../../images/diagrams_png_node-relay-transaction.png)](https://static.learnmeabitcoin.com/diagrams/png/node-relay-transaction.png)


New transactions get added to the [memory pool](/docs/technical/mining/memory-pool.md).

#### Block relay:

[![Diagram showing nodes relaying new blocks across the network and adding them to their blockchains.](../../images/diagrams_png_node-relay-block.png)](https://static.learnmeabitcoin.com/diagrams/png/node-relay-block.png)


New blocks get written to the [blockchain](/docs/technical/blockchain.md).

## Requirements

What do you need to run a Bitcoin node?

Bitcoin is just a computer program, so all you need to run a Bitcoin node is a **computer** and an **Internet connection**.

There are a few system requirements that will help the program run smoothly:

### Disk Space
:   Recommended: 2+ TB

    * Current Blockchain Size: 856.91 GB

    First and foremost, you'll need a big enough hard drive to store the [blockchain](/docs/technical/blockchain.md).

    The blockchain also grows at a rate of around **100 GB/year**, so you'll need to have enough available disk space to keep up if you plan on running a node for an extended period of time.

    You can drastically reduce the disk space required by running a [pruned node](#pruned-node).

### RAM
:   Recommended: 2+ GB

    * Current Mempool Size: 0.68 vMB

    RAM is used for storing the latest transactions in the [mempool](/docs/technical/mining/memory-pool.md), as well as for storing [UTXOs](/docs/technical/transaction/utxo.md) to help speed up the validation of new transactions and blocks.

    You don't need a huge amount of RAM to run Bitcoin, but the more you can give it, the more efficiently it will run.

### Bandwidth
:   Recommended: 2+ TB/month

    * Incoming: 2.24 GB/day (average)
    * Outgoing: 25.21 GB/day (average)

    A node is constantly sending and receiving data ([transactions](/docs/technical/transaction.md) and [blocks](/docs/technical/block.md)) to and from other nodes on the network, so you will need enough bandwidth to cover this.

    It's not an exorbitant amount of data, but a Bitcoin node is going to use significantly more bandwidth than you'd use browsing websites and sending emails.

    If you're a torrent user, your monthly bandwidth won't be too dissimilar to what you see when downloading and seeding torrent files.

    You can limit the amount of bandwidth your node uses with the `maxuploadtarget` configuration setting.

The biggest requirements are having the **disk space** to store the blockchain, and enough **bandwidth** for sending and receiving the latest data on the network.

So Bitcoin isn't the most *lightweight* program in the world, but it's perfectly possible to run it on an everyday laptop or desktop computer. In fact, it's common for people to [set up a Bitcoin node on a Raspberry Pi](https://raspibolt.org/).

**You don't have to keep a Bitcoin node running 24/7.**

It's helpful to the network if you can keep it running as much as possible, but you can start and stop the program as often as you need.

> Messages are broadcasted on a best effort basis, and nodes can leave and rejoin the network at will, accepting the longest proof-of-work chain as proof of what happened while they were gone.

Satoshi Nakamoto, [Cryptography Mailing List (Bitcoin P2P e-cash paper)](https://satoshi.nakamotoinstitute.org/emails/cryptography/1/)

## Communication

How does a node communicate with other nodes?

[![Diagram showing a node communicating with another node by sending a message over a TCP connection.](../../images/diagrams_png_node-communication.png)](https://static.learnmeabitcoin.com/diagrams/png/node-communication.png)

A node communicates with other nodes by sending lots of individual [messages](/docs/technical/networking.md#messages).

These messages are sent via TCP (Transmission Control Protocol), which is a common way for two computers on a network to communicate with each other.

Each node must also follow a specific *Bitcoin protocol* when communicating, which is basically just a set of rules on the structure and order of messages sent between nodes.

So other than following a unique protocol, there's nothing special about the way nodes communicate with each other. In the same way your computer and my server had to connect to each other and follow a protocol for downloading this webpage ([HTTP](https://en.wikipedia.org/wiki/HTTP)), Bitcoin nodes have their own custom protocol for sending and receiving transactions and blocks (Bitcoin Protocol).

Your node will maintain a TCP connection with a number of other nodes on the network, so your node will be sending and receiving lots of messages between multiple computers at the same time. For example, the node running on this website currently has **`114` incoming** and **`10` outgoing** connections.

**The Bitcoin Network is completely open and accessible to anyone.** So as long as you follow the rules for connecting and sending messages, anyone can write their own software for communicating with a node. See [networking](/docs/technical/networking.md) for details.

## Benefits

Why run your own node?

There are a few reasons why you might want to run your own Bitcoin node.

### 1. Trust

[![Diagram showing a person relying on a third-party node for information about a transaction.](../../images/diagrams_png_node-trust.png)](https://static.learnmeabitcoin.com/diagrams/png/node-trust.png)

Running your own node means you **don't have to trust anyone else for information about transactions**.

This means you can know with 100% certainty that every payment you receive is valid, and every query you make about the blockchain is correct. If you're not running your own node, you're trusting someone else who *is* running a node to send you correct information about transactions and blocks.

I've never had a problem with getting data from other nodes before, but if you want to cut out the middle-man completely and not have to rely on anyone else, running your own node is the way to do it.

In its purest form, this is what Bitcoin is all about.

> Don't trust, verify.

Common phrase used in Bitcoin

### 2. Privacy

[![Diagram showing a person broadcasting a transaction via a third-party server.](../../images/diagrams_png_node-privacy.png)](https://static.learnmeabitcoin.com/diagrams/png/node-privacy.png)

Running your own node means you **do not have to share your [transactions](/docs/technical/transaction.md) with third-party services**.

If you're not running your own node, you need to use a third-party website or wallet that *is* running a node to send transactions into the [network](/docs/technical/networking.md) for you. These third-party services can track your requests along with your IP to help build a picture of your activities.

As you can imagine, this isn't great for privacy.

However, by running your own node you can broadcast transactions directly via your own node, so they're no longer going through a middle-man before making it into the network. Similarly, you can get data from your own blockchain without having to use a third-party blockchain explorer website.

Again, I've never had a problem with using trustworthy [wallets](/docs/beginners/wallets.md) or [blockchain explorers](/explorer/) (yet), but it's important to be aware that there's a *potential* privacy leak if you do.

### 3. Support the network

Running your own node supports the network in two ways:

1. **Blockchain replication.** Bitcoin is hard to kill because the entire history of transactions is replicated around the world, so adding another node to the network makes Bitcoin *more resilient*. For example, if every other node on the network blew up and lost its copy of the [blockchain](/docs/technical/blockchain.md), you would effectively be holding up the entire system until other nodes could re-download the blockchain from you.
2. **Data transmission.** Bitcoin works because lots of individual nodes cooperate to spread the latest [transactions](/docs/technical/transaction.md) and [blocks](/docs/technical/block.md) across the network. So by running a node, you're adding another relay to the network. For example, if a bunch of nodes went down and some nodes couldn't connect to each other for some reason, your node could end up being a vital link between different parts of the network.

Running a node is like seeding a torrent file; and everyone loves a seeder.

In short, by running a node you help the network to *stay alive*.

Of course, the benefit of increasing the number of nodes diminishes after the network reaches a certain size. After all, if there are 10,000 copies of the blockchain spread across the world and all the nodes have healthy connections to each other, adding another node isn't going to make a huge difference. So it's not crucial that every man, woman, and smart refrigerator does their best to run a node.

Nonetheless, Bitcoin is a decentralized system that only exists because people volunteer to run nodes, and by doing so you're contributing toward the shared vision that keeps it alive.

And a network can never be *too resilient*.

### 4. Development

Running your own node is useful if you're planning on becoming a Bitcoin developer.

There are a couple of benefits:

1. **Data.** If you have your own full node, you'll have access to all the bitcoin data on your local computer. For example, you can quickly query for block, transaction, and network data using `bitcoin-cli` commands, or you can analyze the entire blockchain using tools like [bitcoin-iterate](https://github.com/rustyrussell/bitcoin-iterate). Some of these tasks would be slow and/or difficult if you're relying on a third-party API for your data.
2. **Source Code.** If you compile Bitcoin Core from scratch, you'll have access to the code that makes it run. This allows you to browse the code on your computer to see how something works, and play with it to try and make improvements to the software.

In short, if you're going to be working *with* a program, you probably want your own copy of it.

Of course, running your own node is not a *requirement* for making your own tools for Bitcoin, but it's nice to have it there. I install [Bitcoin Core](https://bitcoincore.org/en/download/) on all my computers, even if I'm not running it continuously as a node.

## Definitions

What are the different types of node?

There are a few different terms that describe the different *types* of node on the Bitcoin network.

### Full Node

[![Diagram showing a full node validating all of the new blocks and transactions they receive.](../../images/diagrams_png_node-full-node.png)](https://static.learnmeabitcoin.com/diagrams/png/node-full-node.png)

A full node is a node that can keep up with the blockchain and **validate** the blocks and transactions it receives.

A full node *receives* a complete copy of the blockchain, which means that it has a memory of the complete history of transactions and can determine whether any new block or transaction it receives is valid.

In other words, a full node is able to **enforce the rules of the system** on all the data that passes through it, and is therefore an *active participant* in the network.

There are two types of "full node":

#### 1. Archival Node

[![Diagram showing a archival node keeping a complete copy of the blockchain.](../../images/diagrams_png_node-full-node-archival.png)](https://static.learnmeabitcoin.com/diagrams/png/node-full-node-archival.png)

An archival node keeps a **full copy of the blockchain**.

This means it can replicate the entire blockchain to any new nodes joining the network.

#### 2. Pruned Node

[![Diagram showing a pruned node deleting older blocks from its blockchain.](../../images/diagrams_png_node-full-node-pruned.png)](https://static.learnmeabitcoin.com/diagrams/png/node-full-node-pruned.png)

A pruned node **does not keep a full copy of the blockchain**.

Instead, a pruned node *receives* a complete copy of the blockchain, but it deletes older blocks further down the chain as it goes to save on [disk space](#disk-space).

So whilst a pruned node is useful because it can still enforce the rules of the system (i.e. validate and relay new blocks and transactions), the only thing it cannot do is serve a complete copy of the blockchain to new nodes joining the network.

A node keeps a copy of all the [UTXOs](/docs/technical/transaction/utxo.md) in a separate database, so even though a pruned node deletes older blocks as it goes, it will always have a full copy of UTXOs to reference to allow it to validate new transactions and blocks.

### Lightweight Node

"Thin Node", "Thin Client", "Lightweight Client"

A lightweight node is a node that can keep up with the blockchain, but it **cannot validate** the blocks and transactions it receives.

Instead, a lightweight node can verify that a block or transaction *exists* in the blockchain, but it cannot confirm that they are valid.

In other words, a lightweight node is **unable to enforce the rules of the system** and is therefore *not an active participant* in the network.

It's more accurate to refer to a "lightweight node" as a *client*. A node is an active participant on the network, whereas a client effectively just reads data from other nodes on the network.

#### SPV Wallet

Simple Payment Verification

A common type of lightweight node is what's known as an SPV wallet (e.g. [Electrum](https://electrum.org/)).

An SPV wallet only receives the [block headers](/docs/technical/block.md#header) of the blockchain (which are much smaller than complete blocks), which allows them to keep up with what the longest chain **looks like**:

[![Diagram showing an SPV client only receiving block headers instead of full blocks.](../../images/diagrams_png_node-spv-client.png)](https://static.learnmeabitcoin.com/diagrams/png/node-spv-client.png)


Block headers are only 160 bytes. Complete blocks are typically 1,000,000+ bytes.

It can then request *proof* from a full node to confirm whether a specific transaction is in a specific block:

[![Diagram showing an SPV client receiving a proof that can be used with a block header to confirm a transaction is part of a block.](../../images/diagrams_png_node-spv-client-proof.png)](https://static.learnmeabitcoin.com/diagrams/png/node-spv-client-proof.png)


This is known as a [merkle proof](/docs/technical/block/merkle-root.md#merkle-proof).

Thanks to this proof, the SPV wallet can be confident that the transaction is indeed inside the block, and they can update the balance of the wallet.

However, whilst an SPV wallet uses minimal bandwidth and disk space (and can verify that transactions exist in the blockchain), it has to **trust that the information they're being sent from a full node is valid**.

For example, a full node could construct a valid block header and send it to an SPV wallet, but the *actual* block could contain invalid transactions. In other words, a full node can **lie** to a lightweight node if they want to.

[![Diagram showing an SPV client receiving a proof with a block header created from an invalid block.](../../images/diagrams_png_node-spv-client-proof-invalid-block.png)](https://static.learnmeabitcoin.com/diagrams/png/node-spv-client-proof-invalid-block.png)


The proof and block header are valid, but the block header was created from an invalid block of transactions. So the SPV client thinks it has received a payment, but the transaction inside the block is actually invalid.

It would take a lot of effort for a full node to lie to an SPV wallet in this way, as the full node would need to [mine](/docs/technical/mining.md) an invalid block on purpose. So an SPV wallet operates under the assumption that it would be too costly for a full node to want to lie to them.

If you want to be *sure* that all the transactions you're seeing are valid without having to trust anyone, you need to run a full node.

### Miner

A miner is someone who works to take transactions from the [memory pool](/docs/technical/mining/memory-pool.md) and add them to the [blockchain](/docs/technical/blockchain.md).

However:

* A node is not always a miner.
* A miner does not have to be a node.

In the [Bitcoin Whitepaper](/bitcoin.pdf), nodes are sometimes referred to as miners, and miners are always considered to be running as full nodes.

However, **a miner does not need to be performing the job of a node**. Instead, a miner can simply connect to a full node to get the information they need to build a [candidate block](/docs/technical/mining/candidate-block.md), and then send the block back to the full node when they're done.

So whilst it's easiest to think of a *miner* as being a "full node that mines blocks", technically speaking a *node* and a *miner* can be separated to perform two distinct roles.

A lot of the diagrams on this website assume that a miner is always running as a full node. I've done this to keep the diagrams as simple as possible.

## Implementations

What software do I need to run a full node?

The easiest way to run a full node is to download the original implementation:

* [Bitcoin Core](https://bitcoincore.org/en/download/)

However, there are *alternative* implementations for running a Bitcoin node if you prefer:

* [btcd](https://github.com/btcsuite/btcd) (most popular alternative)
* [bcoin](https://github.com/bcoin-org/bcoin)
* [BitcoinJ](https://bitcoinj.org/)

These are all far less popular than the original client though, and I'd recommend sticking with Bitcoin Core if you're new to setting up a full node.

All the `bitcoin-cli` commands mentioned on this website assume you're running a Bitcoin Core node.

### Custom Software

There's nothing stopping you from writing **your own node software** if you want to.

The Bitcoin [network](/docs/technical/networking.md) is completely open, so if you can figure out how to [connect](/docs/technical/networking.md#connecting) to other nodes and follow the rules of the network (i.e. you can send and receive [transactions](/docs/technical/transaction.md) and [blocks](/docs/technical/block.md)), then you'll be able to use Bitcoin using your very own software. Which is pretty cool.

However, some people think it would be better if there weren't too many (or any) competing implementations of the Bitcoin software:

> I don't believe a second, compatible implementation of Bitcoin will ever be a good idea. So much of the design depends on all nodes getting exactly identical results in lockstep that a second implementation would be a menace to the network.

Satoshi Nakamoto, [bitcointalk.org](ttps://bitcointalk.org/index.php?topic=195.msg1611#msg1611)

On the other hand, if you have *multiple* implementations, then it's less likely that they're going to be affected by the same bugs. So if all the nodes on the network running one particular implementation went down due to a serious bug, nodes running a different implementation would remain online and keep the network running (assuming they didn't suffer from the same bugs).

So I can understand why only having a single implementation would be preferable in terms of streamlining development, but I think it's a good thing to have nodes on the network running different implementations of the software.

But most importantly, **nobody can stop you** from writing your own node software if you wanted to anyway.

And that's what Bitcoin is all about.

## Resources

* [Running A Full Node](https://bitcoin.org/en/full-node)
* [What is the meaning of the term "full-node"?](https://bitcoin.stackexchange.com/questions/48436/what-is-the-meaning-of-the-term-full-node)