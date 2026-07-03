![Loading Tool](../../images/icons_loader-2.svg)

A bitcoin transaction is just a **bunch of data**.

It contains information about the **amount** being sent, the account it is being sent **from**, and the account it is being sent **to**.

[![Diagram showing a transaction as moving an amount of bitcoins from one address to another.](../../images/beginners_guide_transactions_01-transaction-table.png)](https://static.learnmeabitcoin.com/beginners/guide/transactions/01-transaction-table.png)

This is just information, so it can be easily represented in a single line of data:

[![Diagram showing a transaction as a line of data.](../../images/beginners_guide_transactions_01-transaction-table-data.png)](https://static.learnmeabitcoin.com/beginners/guide/transactions/01-transaction-table-data.png)

And when you "make a transaction", you just send this *transaction data* into the [bitcoin network](/beginners/guide/network/).

[![Diagram showing a transaction being sent into the bitcoin network.](../../images/beginners_guide_transactions_01-transaction-table-data-network.png)](https://static.learnmeabitcoin.com/beginners/guide/transactions/01-transaction-table-data-network.png)

Eventually, one of the [nodes](/beginners/guide/node/) on the network will [mine](/beginners/guide/mining/) your transaction into a [block](/beginners/guide/blocks/), and this block (with your transaction in it) will be added to the permanent file of transactions (called the [blockchain](/beginners/guide/blockchain/)).

[![Diagram showing a transaction being mined into a block on the blockchain.](../../images/beginners_guide_transactions_01-transaction-table-data-network-mined.png)](https://static.learnmeabitcoin.com/beginners/guide/transactions/01-transaction-table-data-network-mined.png)

And that's all a bitcoin transaction is – a simple line of data that gets sent into the bitcoin network so that it can get mined on to the blockchain.

## How does a bitcoin transaction work?

A bitcoin [address](/technical/keys/address/) is like an *account number* that holds bitcoins.

However, when you make a transaction, it's not like taking an exact amount of coins out of a pot and moving them into another.

[![Diagram showing how a transaction doesn't move an exact amount of coins from one pot (address) to another.](../../images/beginners_guide_transactions_02-pot.png)](https://static.learnmeabitcoin.com/beginners/guide/transactions/02-pot.png)

Instead, an address keeps track of *each individual payment* it has received:

[![Diagram showing how an address holding individual payment amounts (outputs).](../../images/beginners_guide_transactions_02-address1.png)](https://static.learnmeabitcoin.com/beginners/guide/transactions/02-address1.png)

So when you want to send bitcoins to someone else, you grab *whole amounts* that you have already received, and use them to send a *new amount* to a new address:

[![Diagram showing how a transaction spends outputs from one address and sends new outputs to a different address.](../../images/beginners_guide_transactions_02-address1-address2.png)](https://static.learnmeabitcoin.com/beginners/guide/transactions/02-address1-address2.png)

And when that someone else wants to send bitcoins to another person, they will use up whole amounts they have received in the same way:

[![Diagram showing a further transaction spending outputs and sending them to another address.](../../images/beginners_guide_transactions_02-address1-address2-address3.png)](https://static.learnmeabitcoin.com/beginners/guide/transactions/02-address1-address2-address3.png)

So in effect you receive bitcoins in *batches*, and you use those batches to create new batches to send to other people.

That's how transactions work.

### What if the batches add up to more than the amount I want to send?

Good question Sir/Madam.

In this instance (which it often is), you just add another *output* to the transaction and send the difference back to yourself:

[![Diagram showing a change output in a transaction.](../../images/beginners_guide_transactions_02-address1-address2-change.png)](https://static.learnmeabitcoin.com/beginners/guide/transactions/02-address1-address2-change.png)

This may seem awkward at first, I know, but it's a precise way of doing it from a programming perspective.

### Summary

1. Your [wallet](/beginners/wallets/) gives you a bitcoin address. Bitcoins arrive at this address in batches, called *outputs*.
2. A bitcoin transaction is the process of using these outputs (as inputs) to create new outputs that belong to someone else's address.
3. All of this can be represented by a single line of data.

[![Diagram showing a complete bitcoin transaction represented as a single line of data.](../../images/beginners_guide_transactions_02-address1-address2-change-data.png)](https://static.learnmeabitcoin.com/beginners/guide/transactions/02-address1-address2-change-data.png)

For more details on how this system of outputs works, check out [outputs](/beginners/guide/outputs/).

## What prevents other people from spending my bitcoins?

Or in other words…

**Question:** "If making a transaction is simply a case of feeding a line of data into the bitcoin network, why can't someone construct a transaction that includes *my address* and use it to send bitcoins to *their address*?"

**Answer:** Because each transaction output has a *lock* on it:

[![Diagram showing a lock on top of a transaction output.](../../images/beginners_guide_transactions_03-output-locks.png)](https://static.learnmeabitcoin.com/beginners/guide/transactions/03-output-locks.png)

And if you create a transaction *without* unlocking these outputs, nodes on the bitcoin network will reject the transaction:

[![Diagram showing a node rejecting a transaction where the inputs have not been unlocked.](../../images/beginners_guide_transactions_03-output-locks-rejected.png)](https://static.learnmeabitcoin.com/beginners/guide/transactions/03-output-locks-rejected.png)

But fortunately for you, each address comes with a unique [private key](/technical/keys/private-key/):

[![Diagram showing an address with a corresponding private key.](../../images/beginners_guide_transactions_03-address-key.png)](https://static.learnmeabitcoin.com/beginners/guide/transactions/03-address-key.png)

So if you want to send bitcoins in a transaction, you use this private key to create a one-time signature that can *unlock* the outputs located at your address.

[![Diagram showing a private key being used to unlock outputs that have been locked to an address.](../../images/beginners_guide_transactions_03-address-key-unlock.png)](https://static.learnmeabitcoin.com/beginners/guide/transactions/03-address-key-unlock.png)

After unlocking all of the outputs you want to use, the transaction will be accepted by nodes and propagated across the Bitcoin network.

[![Diagram showing a transaction with unlocked inputs being accepted by a node and propagated across the network.](../../images/beginners_guide_transactions_03-output-locks-accepted.png)](https://static.learnmeabitcoin.com/beginners/guide/transactions/03-output-locks-accepted.png)

And that's how bitcoin transactions work.