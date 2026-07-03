![Loading Tool](../../images/icons_loader-2.svg)

[![Diagram showing the bitcoin network as a network people running the same computer program.](../../images/beginners_guide_network_01-software_network.png)](https://static.learnmeabitcoin.com/beginners/guide/network/01-software_network.png)

The Bitcoin Network is made up of individuals running the [bitcoin software](https://bitcoincore.org/en/download/).

This software is known as a "bitcoin client".

## What does the network do?

People (well, *bitcoin clients*) on the network **talk to each other**.

[![Diagram showing the computers on the bitcoin network talking to each other.](../../images/beginners_guide_network_02-software_network_talking.png)](https://static.learnmeabitcoin.com/beginners/guide/network/02-software_network_talking.png)

And by "talk to each other" I mean *pass on information* about what's going on in other parts of the network. This is done by sending each other *[messages](/docs/technical/networking.md#messages)*.

For example, a message could be **information about a new *[transaction](/docs/beginners/guide/transactions.md)***.

[![Diagram showing the computers on the bitcoin network sharing information about new transactions.](../../images/beginners_guide_network_03-software_network_talking_transaction.png)](https://static.learnmeabitcoin.com/beginners/guide/network/03-software_network_talking_transaction.png)

The sharing of information (e.g. transactions) is what allows everyone on the network to keep up-to-date, which is pretty important if you want to run a digital currency on the Internet.

[![Diagram showing the computers on the bitcoin network all having a copy of the latest transaction on the network.](../../images/beginners_guide_network_04-software_network_talking_transaction_consensus.png)](https://static.learnmeabitcoin.com/beginners/guide/network/04-software_network_talking_transaction_consensus.png)

And because all the nodes on the network work to share transactions, everyone on the network will eventually know about the latest transactions.

Good network.

The Bitcoin Network is described as a "[peer-to-peer](https://en.wikipedia.org/wiki/Peer-to-peer) (P2P) network", because:

1. Everyone is connected to each other, so it's a *network*.
2. Everyone on the network is equal, so we are *peers*.

## Who makes up the network?

As mentioned, **anyone with an active Internet connection and running a bitcoin client**.

Seriously, *anyone can join the bitcoin network*. All you need is an internet connection and a [bitcoin client](https://bitcoin.org/en/download), which is a piece of software like any other.

And once you're up and running, you'll be referred to as a **[node](/docs/beginners/guide/node.md)** on the bitcoin network.

[![Diagram showing nodes on the bitcoin network.](../../images/beginners_guide_network_05-nodes_network.png)](https://static.learnmeabitcoin.com/beginners/guide/network/05-nodes_network.png)

"Node" is a slightly more concise way of saying "an individual running a bitcoin client and relaying information around the network".

## How can I join the network?

That's the spirit.

All you need to do is download (and run) a [bitcoin client](https://bitcoincore.org/en/download/).

When you run the client it will connect to other nodes and start downloading a full copy of the [blockchain](/docs/beginners/guide/blockchain.md) (the file that contains all the verified transactions). After that, your client will start receiving transactions from other nodes and relaying them around the network.

Congratulations, you are now a node on the bitcoin network.

You may need to [edit some settings in your router to allow other nodes to connect to you](https://bitcoin.org/en/full-node#enabling-connections), but this is just a minor configuration. By downloading and running a bitcoin client you are 95% of the way to becoming an active node on the bitcoin network.