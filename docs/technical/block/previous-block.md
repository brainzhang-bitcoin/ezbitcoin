<img src="../../images/icons_loader-2.svg" alt="Loading Tool" style="height:32px; width:32px;" />

[<img src="../../images/diagrams_png_block-previous-block.png" alt="Diagram showing the location of the previous block field inside the block header and how it connects the current block to the block below it in the blockchain." width="397" height="529" />](https://static.learnmeabitcoin.com/diagrams/png/block-previous-block.png)

The previous block field in the [block header](/docs/technical/block.md#header) contains the [hash](/docs/technical/block/hash.md) of a previous block that the block **builds on**.

Each block links to a previous block, and this creates a *chain of blocks*. Or, as it's more commonly known, a [blockchain](/docs/technical/blockchain.md).

## Example

Below are the top 5 blocks in the blockchain. If you check them out, you'll see that they each contain the hash of the block below it in their block headers.

Height | Block Hash || 956,479 | [000000000000000000000af753580e7b7bd555102cfbe9c72b4b625dbd3f48d8](/explorer/block/000000000000000000000af753580e7b7bd555102cfbe9c72b4b625dbd3f48d8) |
| 956,478 | [000000000000000000002c0a4bbbd933f15946021264162b74ce5c45b49a2100](/explorer/block/000000000000000000002c0a4bbbd933f15946021264162b74ce5c45b49a2100) |
| 956,477 | [000000000000000000000be1b133d433b3e0b0bf69f9368c20715ccf22ce85ce](/explorer/block/000000000000000000000be1b133d433b3e0b0bf69f9368c20715ccf22ce85ce) |
| 956,476 | [000000000000000000000aad5f4e9a1b745a856f53e4c613253b8275284221e9](/explorer/block/000000000000000000000aad5f4e9a1b745a856f53e4c613253b8275284221e9) |
| 956,475 | [000000000000000000001075120ee6594b359a02eda683e7c1ec3830838e281a](/explorer/block/000000000000000000001075120ee6594b359a02eda683e7c1ec3830838e281a) |

You can visit every block in the blockchain by starting at the tip and following the *previous block*s all the way to the bottom.

## Usage

When constructing a [candidate block](/docs/technical/mining/candidate-block.md), a [miner](/docs/technical/mining.md) will put the block hash of the current **tip of the blockchain** in the previous block field.

[<img src="../../images/diagrams_png_block-previous-block-tip.png" alt="Diagram showing how a candidate block referencing the tip of the blockchain through the previous block field in the block header." width="454" height="696" />](https://static.learnmeabitcoin.com/diagrams/png/block-previous-block-tip.png)

All miners want to extend the current longest known chain of blocks, because the [longest chain](/docs/technical/blockchain/longest-chain.md) is what all nodes adopt as the *canonical* version of the blockchain, and they can only collect the [block reward](/docs/technical/mining/block-reward.md) if the block makes it 100 blocks deep into the longest chain.

> **canonical** – authorized; recognized; accepted

[collinsdictionary.com](https://www.collinsdictionary.com/dictionary/english/canonical)

You can find the block at the current tip of the blockchain by running `bitcoin-cli getbestblockhash`.

**All blocks must build upon an existing previous block.** If you put a hash in the previous block field of a block that does not exist, the block will be invalid and will be rejected by nodes on the [network](/docs/technical/networking.md).

## Purpose

Why do blocks contain the hash of a previous block?

The previous block field is what **connects blocks together** in the blockchain.

A [block hash](/docs/technical/block/hash.md) is a unique reference for a block, and it's determined by the contents of the block. So by including a previous block's hash in the block header, you can create a reliable chain of data, where each chunk of data (i.e. block of transactions) is linked to the one before it.

[<img src="../../images/diagrams_png_block-previous-block-hash-chain.png" alt="Diagram showing how block hashes are used to create a chain of blocks." width="386" height="461" />](https://static.learnmeabitcoin.com/diagrams/png/block-previous-block-hash-chain.png)


The blockchain is just a chain of blocks connected by block hashes.

So if you tried to modify the content of an older block (e.g. by replacing or removing a [transaction](/docs/technical/transaction.md)), this will change the hash for that block, and it will no longer be part of the same chain of blocks, because the block that builds upon it will no longer be referring to it anymore.

[<img src="../../images/diagrams_png_block-previous-block-hash-chain-break.png" alt="Diagram showing how changing the contents of a block will change its hash, and will therefore break the link in the blockchain." width="557" height="518" />](https://static.learnmeabitcoin.com/diagrams/png/block-previous-block-hash-chain-break.png)


If you change one of the block hashes you're removing it from the chain.

So basically, this chain of block hashes is what prevents anyone from going back in time and changing the blockchain. Because if you did, nodes would ignore the modified block as it would not be a part of longest-known chain.

This is what people mean when they refer to the blockchain as being an "immutable ledger".

> **immutable** – Something that is immutable will never change or cannot be changed.

[collinsdictionary.com](https://www.collinsdictionary.com/dictionary/english/immutable)

## Genesis Block

The [genesis block](/explorer/block/000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f) is unique in that its previous block field contains **all zeros**. This is because it's the very first block in the blockchain, and so there is no "previous block" for it to build upon.

That's the only interesting fact I have about the previous block field in the block header.

## Resources

* <https://en.wikipedia.org/wiki/Hash_chain>
* [Blockchain Demo](https://andersbrownworth.com/blockchain/) - Cool interactive website that shows how blocks are connected in a blockchain by block hashes.