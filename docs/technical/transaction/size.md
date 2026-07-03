![Loading Tool](../../images/icons_loader-2.svg)

You can measure the size of a bitcoin [transaction](/docs/technical/transaction.md) in 3 ways:

1. **[Bytes](#bytes) (b)** – Transaction size on disk.
2. **[Weight Units](#weight) (wu)** – For fitting transactions into a block.
3. **[Virtual Bytes](#vbytes) (vB)** – For comparing [feerates](/docs/technical/transaction/fee.md) between transactions.

*Bytes* is the most straightforward unit. It's used for measuring any amount of data on a computer.

*Weight Units* and *Virtual Bytes* are measurements unique to bitcoin. They both measure the size of a transaction in terms of bytes too, but they give a **discount to some parts of the transaction data** and are used when calculating how many transactions can fit inside a [block](/docs/technical/block.md).

![Tool Icon](../../images/icons_tool.svg) Transaction Splitter

Random Example

Transaction Data


* `0 bytes`
* `0 vbytes`

Result

```
 
```



0 secs

## 1. Bytes (b)

[![Diagram showing the measurement of a bitcoin transaction in bytes.](../../images/diagrams_png_transaction-size.png)](https://static.learnmeabitcoin.com/diagrams/png/transaction-size.png)

This is the natural way to measure the size of a transaction. It's a transaction's *actual* size in terms of how many [bytes](/docs/technical/general/bytes.md) of space it takes up.

Bytes are used when measuring how big a transaction is when it's being sent across the [network](/docs/technical/networking.md), or how much space it takes up on disk (e.g. when stored in [blockchain files](/docs/technical/block/blkdat.md)).

Measuring the size of a transaction in bytes was more important when the block size limit was also measured in bytes (1,000,000 bytes, or 1 megabyte). However, the block size limit is now based on *weight* instead.

### Example

Transaction: [30dcd74b7fd8a585db3b2beddd4a7fc0edcfe9b8a1bac9abee695648659f8a6a](/explorer/tx/30dcd74b7fd8a585db3b2beddd4a7fc0edcfe9b8a1bac9abee695648659f8a6a)

```
01000000000101dd40a8d7f105055e781afa632207f5d3c4b4f4cad9f0fb320d0f0aa8e1ba904b0000000000ffffffff021027000000000000160014858e1f88ff6f383f45a75088e15a095f20fc663f841c0000000000001976a9142241a6c3d4cc3367efaa88b58d24748caef79a7288ac02483045022100d66341c3e6ce846b92bedcf9bc673ab8e47b770c616618eb91009e44816f4c2f0220622b5ebf6afabee3f4255bbcb84609e1185d4b6b1055602f5eed2541e26324620121022ed6c7d33a59cc16d37ad9ba54230696bd5424b8931c2a68ce76b0dbbc222f6500000000
```

Size: 226 bytes

There are 226 bytes in this transaction.

You can check this for yourself, because every 2 [hexadecimal](/docs/technical/general/hexadecimal.md) characters represents 1 byte.

#### Typical transaction sizes

The size of a transaction in *bytes* mostly **depends on how many [inputs](/docs/technical/transaction/input.md) and [outputs](/docs/technical/transaction/output.md)** are in the transaction. Here are the average sizes for typical transactions (with standard [P2PKH](/docs/technical/script/p2pkh.md) locking scripts on the outputs):

* Inputs: 1, Outputs: 1 = 191 or 192 bytes
* Inputs: 1, Outputs: 2 = 225 or 226 bytes *(most common)*
* Inputs: 2, Outputs: 1 = 338 or 339 bytes
* Inputs: 2, Outputs: 2 = 373 or 374 bytes *(very common)*

The more inputs and outputs there are in a transaction, the bigger it gets.

There is no limit to how big a transaction can be in terms of bytes, other than the fact that it needs to be able to fit inside a [block](/docs/technical/block.md).

## 2. Weight Units (wu)

[BIP 141](https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki)

[![Diagram showing the measurement of a bitcoin transaction in weight units.](../../images/diagrams_png_transaction-weight.png)](https://static.learnmeabitcoin.com/diagrams/png/transaction-weight.png)

Every transaction has a *weight* measurement. This measurement was introduced in the [segregated witness](/docs/technical/upgrades/segregated-witness.md) upgrade. A transaction's weight is calculated by multiplying the size (in bytes) of different parts of the [transaction](/docs/technical/transaction.md) by either 4 or 1:

| Field | Multiplier |
| --- | --- |
| version | x4 |
| marker | x1 |
| flag | x1 |
| input | x4 |
| output | x4 |
| witness | x1 |
| locktime | x4 |

This therefore gives a *discount* to the [witness](/docs/technical/transaction/witness.md) data.

### Example

Transaction: [30dcd74b7fd8a585db3b2beddd4a7fc0edcfe9b8a1bac9abee695648659f8a6a](/explorer/tx/30dcd74b7fd8a585db3b2beddd4a7fc0edcfe9b8a1bac9abee695648659f8a6a)

```
01000000000101dd40a8d7f105055e781afa632207f5d3c4b4f4cad9f0fb320d0f0aa8e1ba904b0000000000ffffffff021027000000000000160014858e1f88ff6f383f45a75088e15a095f20fc663f841c0000000000001976a9142241a6c3d4cc3367efaa88b58d24748caef79a7288ac02483045022100d66341c3e6ce846b92bedcf9bc673ab8e47b770c616618eb91009e44816f4c2f0220622b5ebf6afabee3f4255bbcb84609e1185d4b6b1055602f5eed2541e26324620121022ed6c7d33a59cc16d37ad9ba54230696bd5424b8931c2a68ce76b0dbbc222f6500000000
```

Size: 226 bytes

Weight: 574 weight units (`116 x 4` + `110 x 1`)

There are 226 bytes in this transaction. Out of those, 116 bytes are `non-witness` data so they get multiplied by 4, and 110 bytes are `witness` data so they get multiplied by 1. Add those together and you get 574 weight units.

### Block Limit (4,000,000 weight units)

The weight measurement is important because **[blocks](/docs/technical/block.md) can hold up to 4,000,000 weight units** of transaction data.

So when [miners](/docs/technical/mining.md) fill up their [candidate blocks](/docs/technical/mining/candidate-block.md) with transactions, they use transaction weight to determine how many transactions they can fit in their block.

[![Diagram showing a block being filled up with transactions using weight as the measurement for each transaction's size.](../../images/diagrams_png_block-weight.png)](https://static.learnmeabitcoin.com/diagrams/png/block-weight.png)

Using bytes for transaction sizes and the block limit was more straightforward. But this new weight measurement introduces *fairness* to the cost of spending outputs.




### Why does witness data weigh less?

Because it helps to bring more of a balance between the cost of creating an output and the cost of spending an output (in terms of [transaction fees](/docs/technical/transaction/fee.md)).

The amount of data required to unlock an output (i.e. [signature](/docs/technical/keys/signature.md) data) is unfairly larger than the amount of data required to put a [lock](/docs/technical/transaction/output/scriptpubkey.md) on an output in the first place. So the new weight measurement brings the "size" of outputs and inputs in a transaction more in line with each other.

[![Diagram showing the comparative size of an output and and input when measured in bytes and in weight units.](../../images/diagrams_png_transaction-weight-spending-sending-balance.png)](https://static.learnmeabitcoin.com/diagrams/png/transaction-weight-spending-sending-balance.png)

## 3. Virtual Bytes (vBytes, vB)

[![Diagram showing the measurement of a bitcoin transaction in virtual bytes.](../../images/diagrams_png_transaction-vsize.png)](https://static.learnmeabitcoin.com/diagrams/png/transaction-vsize.png)

The *virtual size* of a transaction is the same as its *weight* divided by 4.

Or to put it another way, instead of multiplying some parts of a transaction by 4 to create a discount for the witness data, you discount the witness data directly by multiplying it by 0.25 instead:

| Field | Multiplier |
| --- | --- |
| version | x1 |
| marker | x0.25 |
| flag | x0.25 |
| input | x1 |
| output | x1 |
| witness | x0.25 |
| locktime | x1 |

So "weight" and "virtual size" provide the same measurement, just with different units. But using virtual bytes makes it easier to compare the feerate of new segwit transactions with the feerate of legacy transactions (which had previously used *sats-per-byte*).

A legacy transaction will be the same size in *bytes* as it is in *vbytes*.

A block can hold 1,000,000 virtual bytes.

### Example

Transaction: [30dcd74b7fd8a585db3b2beddd4a7fc0edcfe9b8a1bac9abee695648659f8a6a](/explorer/tx/30dcd74b7fd8a585db3b2beddd4a7fc0edcfe9b8a1bac9abee695648659f8a6a)

```
01000000000101dd40a8d7f105055e781afa632207f5d3c4b4f4cad9f0fb320d0f0aa8e1ba904b0000000000ffffffff021027000000000000160014858e1f88ff6f383f45a75088e15a095f20fc663f841c0000000000001976a9142241a6c3d4cc3367efaa88b58d24748caef79a7288ac02483045022100d66341c3e6ce846b92bedcf9bc673ab8e47b770c616618eb91009e44816f4c2f0220622b5ebf6afabee3f4255bbcb84609e1185d4b6b1055602f5eed2541e26324620121022ed6c7d33a59cc16d37ad9ba54230696bd5424b8931c2a68ce76b0dbbc222f6500000000
```

Size: 226 bytes

vSize: 143.50 virtual bytes (`116 x 1` + `110 x 0.25`)

There are 226 bytes in this transaction. Out of those, 116 bytes are `non-witness` data so they get multiplied by 1, and 110 bytes are `witness` data so they get multiplied by 0.25. Add those together and you get 143.50 virtual bytes.

As you can see, the weight and vsize calculations work in the same way.

### Why do we use vbytes?

So why do we have both weight and vbytes? Why not calculate the weight of a transaction by multiplying some parts by 0.25 and just use that instead?

In other words, why have two measurements that do the same thing?

> Because virtual size is fractional when computed accurately. Weight is an integer. We only use integers in consensus code.

Pieter Wuille, [bitcoin.stackexchange.com](https://bitcoin.stackexchange.com/questions/53623/why-does-bip141-define-both-virtual-transaction-size-and-weight)

You see, working with fractional numbers on computers can often lead to [rounding errors](https://floating-point-gui.de/errors/rounding/), which is why in Bitcoin we prefer to work with *whole numbers* when performing critically important calculations. **Integer arithmetic always returns consistent and reliable results, whereas floating point arithmetic does not.**

So in summary:

* **Weight Units** — Used *internally* when working out how many transactions can fit into a block.
* **Virtual Bytes** — Used by *humans* when comparing the different feerates on transactions.

## Resources

* [BIP 141 (Transaction size calculations)](https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki#transaction-size-calculations)
* [Is there a difference between bytes and virtual bytes (vbytes)?](https://bitcoin.stackexchange.com/questions/89385/is-there-a-difference-between-bytes-and-virtual-bytes-vbytes)
* Thanks to [luke-jr](https://github.com/luke-jr) for explaining to me on IRC how multiplying non-witness data by 4 helps to create a balance between the costs of creating and spending [UTXOs](/docs/technical/transaction/utxo.md).