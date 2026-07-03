![Loading Tool](../../images/icons_loader-2.svg)

[![Diagram showing the UTXOs as the unspent outputs in a graph of transactions.](../../images/diagrams_png_transaction-utxo.png)](https://static.learnmeabitcoin.com/diagrams/png/transaction-utxo.png)

A UTXO is an ***unspent* transaction output**.

Every bitcoin [transaction](/docs/technical/transaction.md) creates [outputs](/docs/technical/transaction/output.md) that can be consumed as [inputs](/docs/technical/transaction/input.md) in future transactions. UTXOs are simply the transaction outputs that have not been consumed yet and can still be used for spending.

So if you think of bitcoins as being part of one big graph of transactions, the UTXOs are at the ends of it.

The collection of all the UTXOs is referred to as the UTXO set.

## Usage

How are UTXOs used in Bitcoin?

Keeping track of UTXOs is useful for two reasons:

1. [Validating transactions](#validating-transactions)
2. [Calculating address balances](#calculating-address-balances)

### 1. Validating transactions

When your node receives a new transaction from the [network](/docs/technical/networking.md), it needs to validate that all of its inputs are referencing outputs that have **not already been spent**.

If the transaction's inputs are all unspent outputs (UTXOs), then the transaction is valid:

[![Diagram showing a valid transaction spending an unspent output from a previous transaction.](../../images/diagrams_png_transaction-utxo-spending-valid.png)](https://static.learnmeabitcoin.com/diagrams/png/transaction-utxo-spending-valid.png)

However, if the transaction is trying to spend an output that has already been spent in a previous transaction, then the transaction is invalid and will be rejected:

[![Diagram showing an invalid transaction trying to spend an output from a previous transaction that has already been spent.](../../images/diagrams_png_transaction-utxo-spending-invalid.png)](https://static.learnmeabitcoin.com/diagrams/png/transaction-utxo-spending-invalid.png)

### 2. Calculating address balance

The "balance" of an [address](/docs/technical/keys/address.md) is the sum of all the UTXOs locked to that address:

[![Diagram showing the balance of an address as the sum of the unspent outputs that are locked to that address.](../../images/diagrams_png_transaction-utxo-address-balance.png)](https://static.learnmeabitcoin.com/diagrams/png/transaction-utxo-address-balance.png)

You can see the balance of addresses on blockchain explorers like [mempool.space](https://mempool.space) and [bitcoinexplorer.org](https://bitcoinexplorer.org).

**It's important to note that bitcoins don't "live" inside addresses.** Bitcoins are held inside [outputs](/docs/technical/transaction/output.md), and an address is essentially a *lock* that can be placed on top of an output. Therefore, the balance of an address is just the sum of all the UTXOs that have been locked to that address.

## Location

Where are UTXOs stored in Bitcoin?

In [Bitcoin Core](https://bitcoin.org/en/bitcoin-core/), all of the UTXOs are stored in the [chainstate database](https://github.com/in3rsha/bitcoin-chainstate-parser):

```
~/.bitcoin/chainstate
```

This is a separate database that gets stored in memory (RAM), which makes it faster to access than having to trawl through the [raw blockchain files](/docs/technical/block/blkdat.md) to check if an output has been spent or not.

The chainstate database is a simple [LevelDB](https://github.com/google/leveldb) **key:value** store that contains the following information:

* **Key** - This is made up of the [TXID](/docs/technical/transaction/input/txid.md):[VOUT](/docs/technical/transaction/input/vout.md) for each output. This is known as an "outpoint", and every output in the blockchain has its own unique outpoint, which means it can be used as a reference for looking up each individual output directly.
* **Value** - The value for each UTXO in the database contains the following fields:
  + **Height** - The [height](/docs/technical/blockchain/height.md) of the [block](/docs/technical/block.md) containing the UTXO.
  + **Coinbase** - Whether the UTXO is from a [coinbase transaction](/docs/technical/mining/coinbase-transaction.md) or not. This is important because outputs from coinbase transactions cannot be spent until the transaction is 100 blocks deep in the blockchain.
  + **Amount** - The value of the output in satoshis.
  + **Locking Code** - This is the [locking code](/docs/technical/transaction/output/scriptpubkey.md) that was placed on the output. This is important because every output needs to be *unlocked* when its being spent in a transaction, so this allows you to quickly check if the unlocking code on the input satisfies the conditions of the locking code on the output.

The chainstate database gets updated with each new transaction that gets mined into the [blockchain](/docs/technical/blockchain.md); UTXOs that get spent in a transaction are removed from the database, and the new outputs are added to the database.

You can find out some basic information about the UTXO set from your local node by running the `bitcoin-cli gettxoutsetinfo`:

```
$ bitcoin-cli gettxoutsetinfo

{
  "height": 796565,
  "bestblock": "00000000000000000002f63578950b747bfaa88dcd0bc0d8730827176d01b1f9",
  "txouts": 106662924,
  "bogosize": 8071055609,
  "hash_serialized_2": "596d06c8a5052e1d3e492ee26a811606f5fe30b20bbbd9db2fe64e44e411c17a",
  "total_amount": 19415818.12246298,
  "transactions": 68046641,
  "disk_size": 6827932282
}
```

The above is just an example of the output from `bitcoin-cli gettxoutsetinfo`. When you run this command it can take a few seconds to return the results.

### RAM

RAM is short for **R**andom **A**ccess **M**emory.

If you store data on your computer, it’s faster to read it from RAM than it is to read it from disk (i.e. your SSD or HDD). Your hard drive is for long-term storage, whereas your RAM is temporary storage that you can read from much more quickly.

The UTXO database is loaded into RAM when you run `bitcoind`, which helps to speed up validation of newly-received transactions.

You can change the amount of RAM used for the UTXO database with the `dbcache=` option in your bitcoin.conf file (default = 100 MB). Increasing this value will speed up the time it takes for your node to validate incoming transactions.

## Tools

* [bitcoin-utxo-dump](https://github.com/in3rsha/bitcoin-utxo-dump) - This tool reads the chainstate database from your local node and saves all of the UTXOs to a CSV file.
* [Statoshi.info (Unspent Transaction Output Set)](https://statoshi.info/d/000000009/unspent-transaction-output-set) - Real-time statistics on the state of the UTXO set from a running node.

## Summary

A UTXO is just a fancy name for an output of a transaction that hasn't been spent yet.

Therefore, the UTXO set refers to the **circulating supply of bitcoins**.

There are lots of acronyms in Bitcoin, but ultimately they're almost always complex-sounding names for things that are pretty straightforward. Don't let it put you off.

## Resources

* [Programming Bitcoin by Jimmy Song (Chapter 5: Transactions)](https://github.com/jimmysong/programmingbitcoin/blob/master/ch05.asciidoc#outputs)
* [Did Satoshi invent UTXOs?](https://bitcoin.stackexchange.com/questions/109961/did-satoshi-invent-utxos)
* [Where is the UTXO data stored?](https://bitcoin.stackexchange.com/questions/37397/where-is-the-utxo-data-stored)
* [UTXO uh-oh…](http://gavinandresen.ninja/utxo-uhoh)