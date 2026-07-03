<img src="../../images/icons_loader-2.svg" alt="Loading Tool" style="height:32px; width:32px;" />

A bitcoin transaction is just a **bunch of data**.

It contains information about the **amount** being sent, the account it is being sent **from**, and the account it is being sent **to**.

[<img src="../../images/beginners_guide_transactions_01-transaction-table.png" alt="Diagram showing a transaction as moving an amount of bitcoins from one address to another." width="487" height="93" />](/docs/beginners/guide/transactions/01-transaction-table.png.md)

This is just information, so it can be easily represented in a single line of data:

[<img src="../../images/beginners_guide_transactions_01-transaction-table-data.png" alt="Diagram showing a transaction as a line of data." width="479" height="162" />](/docs/beginners/guide/transactions/01-transaction-table-data.png.md)

And when you "make a transaction", you just send this *transaction data* into the [bitcoin network](/docs/beginners/guide/network.md).

[<img src="../../images/beginners_guide_transactions_01-transaction-table-data-network.png" alt="Diagram showing a transaction being sent into the bitcoin network." width="506" height="480" />](/docs/beginners/guide/transactions/01-transaction-table-data-network.png.md)

Eventually, one of the [nodes](/docs/beginners/guide/node.md) on the network will [mine](/docs/beginners/guide/mining.md) your transaction into a [block](/docs/beginners/guide/blocks.md), and this block (with your transaction in it) will be added to the permanent file of transactions (called the [blockchain](/docs/beginners/guide/blockchain.md)).

[<img src="../../images/beginners_guide_transactions_01-transaction-table-data-network-mined.png" alt="Diagram showing a transaction being mined into a block on the blockchain." width="132" height="254" />](/docs/beginners/guide/transactions/01-transaction-table-data-network-mined.png.md)

And that's all a bitcoin transaction is – a simple line of data that gets sent into the bitcoin network so that it can get mined on to the blockchain.

## How does a bitcoin transaction work?

A bitcoin [address](/docs/technical/keys/address.md) is like an *account number* that holds bitcoins.

However, when you make a transaction, it's not like taking an exact amount of coins out of a pot and moving them into another.

[<img src="../../images/beginners_guide_transactions_02-pot.png" alt="Diagram showing how a transaction doesn't move an exact amount of coins from one pot (address) to another." width="415" height="178" />](/docs/beginners/guide/transactions/02-pot.png.md)

Instead, an address keeps track of *each individual payment* it has received:

[<img src="../../images/beginners_guide_transactions_02-address1.png" alt="Diagram showing how an address holding individual payment amounts (outputs)." width="142" height="149" />](/docs/beginners/guide/transactions/02-address1.png.md)

So when you want to send bitcoins to someone else, you grab *whole amounts* that you have already received, and use them to send a *new amount* to a new address:

[<img src="../../images/beginners_guide_transactions_02-address1-address2.png" alt="Diagram showing how a transaction spends outputs from one address and sends new outputs to a different address." width="518" height="197" />](/docs/beginners/guide/transactions/02-address1-address2.png.md)

And when that someone else wants to send bitcoins to another person, they will use up whole amounts they have received in the same way:

[<img src="../../images/beginners_guide_transactions_02-address1-address2-address3.png" alt="Diagram showing a further transaction spending outputs and sending them to another address." width="699" height="173" />](/docs/beginners/guide/transactions/02-address1-address2-address3.png.md)

So in effect you receive bitcoins in *batches*, and you use those batches to create new batches to send to other people.

That's how transactions work.

### What if the batches add up to more than the amount I want to send?

Good question Sir/Madam.

In this instance (which it often is), you just add another *output* to the transaction and send the difference back to yourself:

[<img src="../../images/beginners_guide_transactions_02-address1-address2-change.png" alt="Diagram showing a change output in a transaction." width="469" height="224" />](/docs/beginners/guide/transactions/02-address1-address2-change.png.md)

This may seem awkward at first, I know, but it's a precise way of doing it from a programming perspective.

### Summary

1. Your [wallet](/docs/beginners/wallets.md) gives you a bitcoin address. Bitcoins arrive at this address in batches, called *outputs*.
2. A bitcoin transaction is the process of using these outputs (as inputs) to create new outputs that belong to someone else's address.
3. All of this can be represented by a single line of data.

[<img src="../../images/beginners_guide_transactions_02-address1-address2-change-data.png" alt="Diagram showing a complete bitcoin transaction represented as a single line of data." width="477" height="382" />](/docs/beginners/guide/transactions/02-address1-address2-change-data.png.md)

For more details on how this system of outputs works, check out [outputs](/docs/beginners/guide/outputs.md).

## What prevents other people from spending my bitcoins?

Or in other words…

**Question:** "If making a transaction is simply a case of feeding a line of data into the bitcoin network, why can't someone construct a transaction that includes *my address* and use it to send bitcoins to *their address*?"

**Answer:** Because each transaction output has a *lock* on it:

[<img src="../../images/beginners_guide_transactions_03-output-locks.png" alt="Diagram showing a lock on top of a transaction output." width="379" height="237" />](/docs/beginners/guide/transactions/03-output-locks.png.md)

And if you create a transaction *without* unlocking these outputs, nodes on the bitcoin network will reject the transaction:

[<img src="../../images/beginners_guide_transactions_03-output-locks-rejected.png" alt="Diagram showing a node rejecting a transaction where the inputs have not been unlocked." width="489" height="434" />](/docs/beginners/guide/transactions/03-output-locks-rejected.png.md)

But fortunately for you, each address comes with a unique [private key](/docs/technical/keys/private-key.md):

[<img src="../../images/beginners_guide_transactions_03-address-key.png" alt="Diagram showing an address with a corresponding private key." width="435" height="73" />](/docs/beginners/guide/transactions/03-address-key.png.md)

So if you want to send bitcoins in a transaction, you use this private key to create a one-time signature that can *unlock* the outputs located at your address.

[<img src="../../images/beginners_guide_transactions_03-address-key-unlock.png" alt="Diagram showing a private key being used to unlock outputs that have been locked to an address." width="345" height="228" />](/docs/beginners/guide/transactions/03-address-key-unlock.png.md)

After unlocking all of the outputs you want to use, the transaction will be accepted by nodes and propagated across the Bitcoin network.

[<img src="../../images/beginners_guide_transactions_03-output-locks-accepted.png" alt="Diagram showing a transaction with unlocked inputs being accepted by a node and propagated across the network." width="489" height="539" />](/docs/beginners/guide/transactions/03-output-locks-accepted.png.md)

And that's how bitcoin transactions work.