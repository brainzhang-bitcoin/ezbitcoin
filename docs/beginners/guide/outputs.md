![Loading Tool](../../images/icons_loader-2.svg)

The bitcoin [transaction](/beginners/guide/transactions/) system involves sending and receiving whole "batches" of bitcoins, called outputs.

Simple enough, but the only way to really understand how outputs work is to look at a few example transactions.

## Where do outputs come from?

Let's begin this explanation of transaction outputs with the birth of a fresh batch of bitcoins…

You are [mining](/beginners/guide/mining/) bitcoins on your own. By some miracle, you have managed to mine a [block](/beginners/guide/blocks/) of transactions and earn yourself a [block reward](/technical/mining/block-reward/).

[![Diagram showing the block reward being sent to an address via the coinbase transaction.](../../images/beginners_guide_outputs_00-generation-transaction.png)](https://static.learnmeabitcoin.com/beginners/guide/outputs/00-generation-transaction.png)

Every miner includes their own address at the top of each block, so if they manage to mine the block, the block reward can be sent to their address. This is claimed via a [coinbase transaction](/technical/mining/coinbase-transaction/) (or as it used to be referred to, the "generation transaction").

So this is the current state of your bitcoin address:

[![Diagram showing a single 25 BTC output locked to an address.](../../images/beginners_guide_outputs_01-transaction1-before.png)](https://static.learnmeabitcoin.com/beginners/guide/outputs/01-transaction1-before.png)

The block reward was 25 BTC when I first wrote this article.

Naturally, your first instinct is to celebrate. So let's use 1 of these bitcoins to buy some beer.

[![A badly-drawn pint of beer.](../../images/beginners_guide_outputs_01-beer.png)](https://static.learnmeabitcoin.com/beginners/guide/outputs/01-beer.png)

Beer.

Now, your other first instinct would be to chip off 1 of these bitcoins (from the block reward) to pay for this beer. This would make sense, but it's not quite how transactions work.

[![Diagram showing a 1 BTC incorrectly being chipped off a larger 25 BTC input.](../../images/beginners_guide_outputs_01-transaction1-chip.png)](https://static.learnmeabitcoin.com/beginners/guide/outputs/01-transaction1-chip.png)

Not quite. And that's one expensive beer.

Instead, we have to **send the entire batch of 25 bitcoins** in the transaction.

But to make sure we *don't spend all 25 bitcoins* in a "1 bitcoin" payment, we **split the batch up** and send it to *two destinations*:

1. To the beer shop as payment
2. Back to our own address as change

[![Diagram showing a transaction where a single 25 BTC input is split into a 1 BTC and a 24 BTC output.](../../images/beginners_guide_outputs_01-transaction1.png)](https://static.learnmeabitcoin.com/beginners/guide/outputs/01-transaction1.png)

The newly created batches are called *outputs*.

It's a bit of an around-the-houses way of doing it, but it achieves the same end-result.

Anyway, this is what the bitcoin addresses look like *after* the transaction:

[![Diagram showing a balance of 24 BTC at one address, and 1 BTC at another address.](../../images/beginners_guide_outputs_01-transaction1-after.png)](https://static.learnmeabitcoin.com/beginners/guide/outputs/01-transaction1-after.png)

The beer shop has a new batch of 1 bitcoin, and we've sent ourselves a new batch of 24 bitcoins (as change). The original batch of 25 bitcoins has now been "used up" and can't be spent again.

So effectively it's as though we took 1 bitcoin from our address and sent it to another address… but now we know what's *really* going on under the hood.

### Summary:

A transaction:

1. Takes existing output(s) as inputs.
2. Creates newly-sized output(s) from the inputs.
3. Locks the output(s) to different addresses.

The reason transactions use this "outputs" system is because it's an easy way of constructing payments from a programming perspective.

## How do you spend multiple outputs in a transaction?

Okay, from now on we're going to use the word *output* instead of "batch".

Anyway, a few days have passed since the beer shop sold us that beer. And judging by the current state of their bitcoin address, the beer business is booming:

[![Diagram showing an address with 5 unspent outputs totalling 7.5 BTC.](../../images/beginners_guide_outputs_02-transaction2-before.png)](https://static.learnmeabitcoin.com/beginners/guide/outputs/02-transaction2-before.png)

The beer shop has received four new payments since we bought our beer.

But as we all know, beer doesn't grow on trees. So the beer shop is on the lookout for a brand-new beer machine.

[![A badly-drawn imaginary beer-making machine.](../../images/beginners_guide_outputs_02-beer-machine.png)](https://static.learnmeabitcoin.com/beginners/guide/outputs/02-beer-machine.png)

This is what my friends call me on nights out.

Oh look, a lovely beer machine for the low, low price of 4.2 bitcoins.

Let's buy it…

[![Diagram showing a transaction spending multiple inputs and creating multiple outputs.](../../images/beginners_guide_outputs_02-transaction2.png)](https://static.learnmeabitcoin.com/beginners/guide/outputs/02-transaction2.png)

Constructing the transaction for the beer machine.

Alright, I realize I've just cranked the diagram up a few notches on this one, but it's not too difficult to understand:

1. The beer shop doesn't have a single output at their address to cover the cost of the beer machine (4.2 BTC). So instead, we *gather a handful of outputs together* to get a total greater than 4.2 BTC.
2. When we construct a transaction, the outputs we gather for spending are referred to as the transaction *inputs*.
3. Using the total input amount of **4.5 BTC**, the beer shop creates two new outputs of **4.2 BTC** and **0.3 BTC**.

When you're *spending* an output in a transaction, it's referred to as an **input**.

And here's the state of the beer shop's bitcoin address after the transaction:

[![Diagram showing an address with 4 spent outputs and 2 unspent outputs totalling 3.3 BTC.](../../images/beginners_guide_outputs_02-transaction2-after.png)](https://static.learnmeabitcoin.com/beginners/guide/outputs/02-transaction2-after.png)

The beer shop has used up 4 outputs, and has one new 0.3 BTC output (from the change).

Once again, the *outputs* that were used as *inputs* have been "spent", and can't be used again.

The "unspent" outputs, however, are still good for spending, so we call these the *unspent transaction outputs* ([UTXOs](/technical/transaction/utxo/)).

The balance of an address is the sum of the address's UTXOs.

### UTXO selection

We chose the outputs of `[1] + [0.5] + [2] + [1]` as the inputs for the transaction. But as long as the total is greater than the amount we want to send, we can use any combination of outputs (well, *inputs*) we want.

For example:

```
[1] + [3] + [0.5]             = 4.5
[3] + [2]                     = 5
[1] + [3] + [0.5] + [2] + [1] = 7.5
```

Any of these combinations of inputs would be fine. You can figure out the change for each one yourself.

## Where do transaction fees come from?

Ah yes, we've not included a [transaction fee](/technical/transaction/fee/) in either of the last two transactions.

Without a transaction fee, those two transactions will probably take a while to get included in a block (if ever). This is because a transaction fee gives your transaction *priority*.

You see, transaction fees are picked up by miners when they mine a block. So if there are lots of transactions waiting in the [memory pool](/technical/mining/memory-pool/), adding a transaction fee provides an *incentive* for miners to include your transaction in their next block.

Anyhow, pretend we didn't send that last transaction into the network, and let's add a transaction fee to it:

[![Diagram showing a transaction with a remainder that is used as the fee.](../../images/beginners_guide_outputs_03-transaction2-fee.png)](https://static.learnmeabitcoin.com/beginners/guide/outputs/03-transaction2-fee.png)

Okay, so where the hell is the output for the transaction fee? Well, there isn't one. But **look at the size of the outputs**.

The total of the outputs is less than the total of the inputs, which means that there are some remaining bitcoins that aren't being used up. This "left over" amount is the transaction fee.

And that's all transaction fees are – the remainder of a transaction.

**The amount that's left over in a transaction always gets picked up by a miner.** So if you manually constructed a transaction and forgot to create a change output for yourself, the miner would pick up the amount you left behind, no matter how much it is. This is not something to worry about if you're using a [wallet](/beginners/wallets/) to construct your transactions for you though, as they will always take care of the change for you.