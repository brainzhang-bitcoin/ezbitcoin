![Loading Tool](../../images/icons_loader-2.svg)

[![Diagram showing how a block hash is created by hashing the block header.](../../images/diagrams_png_block-hash.png)](https://static.learnmeabitcoin.com/diagrams/png/block-hash.png)

A block hash (or block ID) is a **unique reference** for a [block](/docs/technical/block.md) in the [blockchain](/docs/technical/blockchain.md).

Every block hash is unique and is determined by the contents of the block. You can therefore use the block hash to search for a specific block in a [blockchain explorer](/explorer/). For example:

* Most Recent Block: [000000000000000000006124edc0696e0918b53eb5132f0728f34a50f1fd24d5](/explorer/block/000000000000000000006124edc0696e0918b53eb5132f0728f34a50f1fd24d5)
* Block 123,456: [0000000000002917ed80650c6174aac8dfc46f5fe36480aaef682ff6cd83c3ca](/explorer/block/0000000000002917ed80650c6174aac8dfc46f5fe36480aaef682ff6cd83c3ca)
* Genesis Block: [000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f](/explorer/block/000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f)

There's nothing too interesting about these block hashes, as they're ultimately just a random-looking bunch of [bytes](/docs/technical/general/bytes.md).

However, you'll notice that all block hashes begin with a **bunch of zeros**. This is because for a block to be added to the blockchain, a [miner](/docs/technical/mining.md) must get a hash for their block below the current [target](/docs/technical/mining/target.md) value. And if the block hash is *below* this target value, then the block hash is naturally going to have a bunch of zeros at the start.

## Creating

How do you create a block hash?

A block hash is created by [hashing](/docs/technical/cryptography/hash-function.md) the [block header](/docs/technical/block.md#header).

Random Example

Block Header

`0 bytes`

Block Hash (Natural Byte Order)

Used internally inside raw block headers

`0 bytes`

Block Hash (Reverse Byte Order)

Used externally when searching for blocks on block explorers

`0 bytes`



0 secs

The steps for creating a block hash are as follows:

1. Construct a [block](/docs/technical/block.md) of [transactions](/docs/technical/transaction.md).
2. Construct a [block header](/docs/technical/block.md#header) for that block.
3. [HASH256](/docs/technical/cryptography/hash-function.md#hash256) the block header to get the block hash.
   * HASH256 is shorthand for *double SHA-256*; you put the block header through the SHA-256 hash function, then put the result through SHA-256 again.

### Code

```
![Copy](../../images/icons_clipboard-white.svg)



![Copied](../../images/icons_clipboard-check-white.svg)copied



![Failed](../../images/icons_clipboard-x-white.svg)copied

require 'digest'

# ------------
# block header (genesis block)
# ------------
version = "01000000"
previousblock = "0000000000000000000000000000000000000000000000000000000000000000"
merkleroot = "3ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4a"
time = "29ab5f49"
bits = "ffff001d"
nonce = "1dac2b7c"

blockheader = version + previousblock + merkleroot + time + bits + nonce

# ---------
# block hash
# ----------

# Note: Don't put the block header into the hash function as a string.
#       Convert it from hexadecimal to raw bytes first.

# convert hexadecimal string to byte sequence
bytes = [blockheader].pack("H*") # H = hex string (highest byte first), * = multiple bytes

# SHA-256 (first round)
hash1 = Digest::SHA256.digest(bytes)

# SHA-256 (second round)
hash2 = Digest::SHA256.digest(hash1)

# convert from byte sequence back to hexadecimal string
blockhash = hash2.unpack("H*")[0]

# print result (natural byte order)
puts blockhash #=> 6fe28c0ab6f1b372c1a6a246ae63f74f931e8365e15a089c68d6190000000000

# print result (reverse byte order)
puts blockhash.scan(/../).reverse.join #=> 000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f
```

**Transactions.** You'll notice that we're not directly hashing the transactions inside the block. However, the block header contains a [merkle root](/docs/technical/block/merkle-root.md), which *is* the hash of the transactions, so the transactions inside the block are part of the block header.

**Valid Block Hashes.** Not all block hashes will have a bunch of zeros at the start (at first). Miners increment the [nonce](/docs/technical/block/nonce.md) value in the block header to try and get a block hash that is below the target.

**Byte Order.** The actual result of hashing the block header will produce a block hash that is in [natural byte order](/docs/technical/general/byte-order.md#natural-byte-order). However, when searching for blocks in a blockchain explorer the block hash is in [reverse byte order](/docs/technical/general/byte-order.md#reverse-byte-order).

## Usage

Where are block hashes used in bitcoin?

Block hashes are used in two places:

1. They are used when **searching** for a specific block in the blockchain.
2. They are put inside the [previous block](/docs/technical/block/previous-block.md) field of the block header to **connect blocks** together in the blockchain.

[![Diagram showing blocks connected together through block hashes in the block header using the previous block field.](../../images/diagrams_png_block-previous-block.png)](https://static.learnmeabitcoin.com/diagrams/png/block-previous-block.png)


Blocks are connected by their block hashes.

So you'll most commonly use block hashes when searching for a specific block on a [blockchain explorer](/explorer/), but the previous block field is critically important as it's the glue that holds the blockchain together.

## FAQ

### Is the block hash just some bytes or is it a number?

It's both.

Anything that comes out of the SHA-256 [hash function](/docs/technical/cryptography/hash-function.md) is just a bunch of meaningless [bytes](/docs/technical/general/bytes.md). But they *are unique* (for that particular data), so they're perfect for use as a unique reference for some specific data. This allows you to confidently search for and reference previous blocks when building a [blockchain](/docs/technical/blockchain.md).

Again, this is the unique block hash for the genesis block:

```
000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f
```

The [hexadecimal](/docs/technical/general/hexadecimal.md) characters you see here are just representing **32 bytes** of meaningless data.

However, in bitcoin, during the process of [mining](/docs/technical/mining.md) these block hashes also get interpreted as **numbers**. If you convert this block hash from hexadecimal to decimal you get:

```
10628944869218562084050143519444549580389464591454674019345556079
```

By doing this you can check to see if the block hash is below the [target](/docs/technical/mining/target.md), and if it is, the block can be added on to the blockchain.

So it makes sense to think of the block hash as being a unique number.

![Tool Icon](../../images/icons_tool.svg) Number Converter

Binary (Base 2)

0b

`0 digits`

Decimal (Base 10)

0d

`0 digits`

Hexadecimal (Base 16)

0x

`0 digits`




+1



0 secs