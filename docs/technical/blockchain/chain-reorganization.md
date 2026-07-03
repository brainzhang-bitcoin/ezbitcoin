<img src="../../images/icons_loader-2.svg" alt="Loading Tool" style="height:32px; width:32px;" />

[<img src="../../images/diagrams_png_blockchain-chain-reorganization.png" alt="Diagram showing a chain reorganization across nodes on the network." width="983" height="639" />](https://static.learnmeabitcoin.com/diagrams/png/blockchain-chain-reorganization.png)

Recent Chain Reorganizations:

| Height | Length | Date |
| --- | --- | --- |
| [956,337](/explorer/956337) | 1 | 02 July 2026 |
| [951,052](/explorer/951052) | 1 | 26 May 2026 |
| [945,189](/explorer/945189) | 1 | 15 April 2026 |
| [944,852](/explorer/944852) | 1 | 13 April 2026 |
| [941,882](/explorer/941882) | 2 | 23 March 2026 |
| [939,832](/explorer/939832) | 1 | 08 March 2026 |
| [935,497](/explorer/935497) | 1 | 08 February 2026 |
| [933,995](/explorer/933995) | 1 | 27 January 2026 |
| [928,484](/explorer/928484) | 1 | 19 December 2025 |
| [925,605](/explorer/925605) | 1 | 28 November 2025 |
| [920,138](/explorer/920138) | 1 | 21 October 2025 |
| [916,308](/explorer/916308) | 1 | 25 September 2025 |
| [904,623](/explorer/904623) | 1 | 08 July 2025 |
| [901,092](/explorer/901092) | 1 | 13 June 2025 |
| [894,657](/explorer/894657) | 1 | 30 April 2025 |
| [883,183](/explorer/883183) | 1 | 10 February 2025 |
| [881,953](/explorer/881953) | 1 | 02 February 2025 |
| [881,780](/explorer/881780) | 1 | 01 February 2025 |
| [877,770](/explorer/877770) | 1 | 04 January 2025 |
| [863,888](/explorer/863888) | 1 | 03 October 2024 |
| [856,689](/explorer/856689) | 1 | 14 August 2024 |
| [853,051](/explorer/853051) | 1 | 20 July 2024 |
| [851,248](/explorer/851248) | 1 | 08 July 2024 |
| [849,233](/explorer/849233) | 1 | 24 June 2024 |
| [848,477](/explorer/848477) | 1 | 18 June 2024 |
| [847,849](/explorer/847849) | 1 | 14 June 2024 |
| [829,613](/explorer/829613) | 1 | 09 February 2024 |
| [827,853](/explorer/827853) | 1 | 28 January 2024 |
| [819,343](/explorer/819343) | 1 | 01 December 2023 |
| [818,038](/explorer/818038) | 1 | 23 November 2023 |
| [815,202](/explorer/815202) | 1 | 04 November 2023 |
| [813,210](/explorer/813210) | 1 | 21 October 2023 |
| [803,389](/explorer/803389) | 1 | 16 August 2023 |
| [800,786](/explorer/800786) | 1 | 29 July 2023 |
| [792,379](/explorer/792379) | 1 | 01 June 2023 |
| [789,147](/explorer/789147) | 1 | 10 May 2023 |
| [788,837](/explorer/788837) | 1 | 08 May 2023 |
| [788,805](/explorer/788805) | 1 | 08 May 2023 |
| [781,487](/explorer/781487) | 1 | 19 March 2023 |
| [781,277](/explorer/781277) | 1 | 18 March 2023 |
| [730,848](/explorer/730848) | 1 | 07 April 2022 |
| [685,135](/explorer/685135) | 1 | 27 May 2021 |
| [675,407](/explorer/675407) | 1 | 20 March 2021 |
| [675,392](/explorer/675392) | 1 | 20 March 2021 |

A chain reorganization (or "reorg") takes place when your node receives blocks that are part of a new [longest chain](/docs/technical/blockchain/longest-chain.md). Your node will *deactivate* blocks in its old longest chain in favor of the blocks that build the **new longest chain**.

This process allows individual nodes across the network to **agree on the same version of the [blockchain](/docs/technical/blockchain.md)**, because the globally accepted view of the blockchain will always be the one with the longest\* chain of blocks.

\*Technically it's the chain with the most amount of *work*, but the most number of blocks is usually the same thing.

> It is strictly necessary that the longest chain is always considered the valid one.

Satoshi Nakamoto, [Cryptography Mailing List (Bitcoin P2P e-cash paper)](https://satoshi.nakamotoinstitute.org/emails/cryptography/6/)

## Scenario

When does a chain reorganization take place?

A chain reorganization most commonly takes place after **two [blocks](/docs/technical/block.md) have been [mined](/docs/technical/mining.md) at the same time**.

[<img src="../../images/diagrams_png_blockchain-chain-reorganization-example-two-blocks.png" alt="Diagram showing two blocks being mined at the same time on the Bitcoin network." width="983" height="582" />](https://static.learnmeabitcoin.com/diagrams/png/blockchain-chain-reorganization-example-two-blocks.png)


Although uncommon, it's perfectly normal for two blocks to get mined at the same time.

Due to the propagation speed of blocks across the [network](/docs/technical/networking.md), some nodes will receive the one block first, and some nodes will receive the other block first. Therefore, there will be a temporary disagreement about which of these blocks was actually "first" and belongs at the top of everyone's blockchain.

[<img src="../../images/diagrams_png_blockchain-chain-reorganization-example-chain-split.png" alt="Diagram showing a temporary fork in the blockchain due to two blocks being mined at the same time." width="983" height="559" />](https://static.learnmeabitcoin.com/diagrams/png/blockchain-chain-reorganization-example-chain-split.png)


Nodes will temporarily disagree on what the blockchain looks like.

So how can we resolve this dispute and make sure everyone agrees upon the same version of the blockchain?

Well, it's resolved when the *next block is mined*. The next block to be mined will build on top of *one* of these blocks, creating a new longest chain. When nodes receive this newest block, they will see that it creates a new longest chain, and they will perform a *chain reorganization* to adopt it.

[<img src="../../images/diagrams_png_blockchain-chain-reorganization-example-next-block-resolved.png" alt="Diagram showing a temporary fork being resolved when the next block is mined." width="983" height="597" />](https://static.learnmeabitcoin.com/diagrams/png/blockchain-chain-reorganization-example-next-block-resolved.png)


Blocks in the old shorter chain are deactivated, and blocks in the new longer chain are activated.

So thanks to chain reorganizations, each node eventually agrees on the same version of the blockchain as everyone else.

## Stale Blocks

What happens to the transactions in the old longest chain?

> **stale** – impaired in vigor or effectiveness

[Merriam-Webster](https://www.merriam-webster.com/dictionary/stale)

If a block is deactivated due to a chain reorganization ("stale block"), the transactions inside it are **no longer part of the blockchain**.

[<img src="../../images/diagrams_png_blockchain-chain-reorganization-stale-block.png" alt="Diagram showing a stale block after a chain reorganization." width="772" height="329" />](https://static.learnmeabitcoin.com/diagrams/png/blockchain-chain-reorganization-stale-block.png)


A stale block is a block that is no longer part of the longest chain.

So if you try to spend the [outputs](/docs/technical/transaction/output.md) from a transaction inside a *stale block*, nodes would reject your transaction because you are trying to spend bitcoins that do not exist in the valid chain.

[<img src="../../images/diagrams_png_blockchain-chain-reorganization-stale-block-invalid-transaction.png" alt="Diagram showing how the outputs from a transaction in a stale block cannot be spent." width="772" height="469" />](https://static.learnmeabitcoin.com/diagrams/png/blockchain-chain-reorganization-stale-block-invalid-transaction.png)


The outputs from transactions in a stale block cannot be spent; it's like the transaction never happened.

Practically speaking though, if two blocks are mined at the same time, they're probably going to include the same (or similar) transactions in them, so a reorg isn't usually going to cause a problem.

[<img src="../../images/diagrams_png_blockchain-chain-reorganization-stale-block-similar-transactions.png" alt="Diagram showing how competing blocks during a chain reorganization usually contain similar transactions." width="772" height="318" />](https://static.learnmeabitcoin.com/diagrams/png/blockchain-chain-reorganization-stale-block-similar-transactions.png)


Your transaction is most likely included in the "competing" block after a chain reorganization.

However, if there are transactions in the stale block that are *not* in the competing block, they will get sent back into your node's [memory pool](/docs/technical/mining/memory-pool.md) and propagated around the network again for the *chance* to be mined into a future block.

[<img src="../../images/diagrams_png_blockchain-chain-reorganization-stale-block-transactions-recycled.png" alt="Diagram showing a transaction from a stale block being recycled back into the mempool." width="772" height="480" />](https://static.learnmeabitcoin.com/diagrams/png/blockchain-chain-reorganization-stale-block-transactions-recycled.png)


Transactions from stale blocks will be recycled back into the memory pool if they're not in the competing block.

But this is not a guarantee, and if a transaction does not exist in the active chain, it may as well have never happened.

**It's worth waiting for a transaction to make it 2+ blocks into the blockchain before considering it as final.** There is always the chance that it will get reorg'd out, and you will have to wait/hope for it to be re-mined back into the longest chain.

**A "stale block" is sometimes referred to as an "orphan block", but "stale block" is the more accurate term.** An *orphan block* is when your node receives a block before receiving the parent block that it builds upon, and stale blocks aren't orphans because they have parents.

### Example

Here we can see an example of an actual chain reorganization that took place in the blockchain at block height [578,141](/explorer/578141).

[<img src="../../images/technical_blockchain_chain-reorganization_neo4j-reorg-5.jpg" alt="Diagram showing an actual example of chain reorganization and transactions from the stale block being re-mined in a later block." width="1151" height="621" />](/docs/technical/blockchain/chain-reorganization/neo4j-reorg-5.jpg.md)


Most of the transactions in the stale block were in the competing block, but some transactions were re-mined in to later blocks.

## Size

How big can chain reorganizations be?

A chain reorganization can be **any number of blocks in length**.

If your node receives a new chain of blocks that's longer than your current active chain, your node will do a chain reorganization to adopt the new chain, no matter how many blocks will be replaced.

This is why it's possible for a miner with a majority of hashing power to replace blocks and transactions in your current longest chain via a [51% attack](/docs/technical/blockchain/51-attack.md). The longest chain always wins.

However, "natural" chain reorganizations (ones that take place due to two blocks being mined at the same time) **rarely involve more than the top block in your chain**.

## Frequency

How often do chain reorganizations happen?

Not very often. For your node to experience an honest chain reorganization, the following needs to take place:

1. Two blocks are mined at the same time.
2. Your node receives one of the blocks first, but the *other* block gets built upon and becomes the new longest chain.

I don't know what the mathematical probability of this is, so here's the frequency of chain reorganizations based on the data from [my bitcoin node](/explorer/) (which has been running continuously since **March 2021**):

* **Actual Reorganizations:** 44 (1 every 6,451 blocks / 44.3 days)
  + We received a new longest chain and updated to it, deactivating blocks in our old longest chain.
* **Avoided Reorganizations:** 232 (1 every 1,223 blocks / 8.4 days)
  + We heard about a chain that could become the new longest chain, but our active chain at the time continued as the longest.

## Commands

How can you find chain reorganizations?

You can see the chain reorganizations your node has observed with the `bitcoin-cli getchaintips` command.

For example:

```
[
  {
    "height": 589919,
    "hash": "000000000000000000149b18e74316248d106e42ca410f509305ae58ccda6b13",
    "branchlen": 0,
    "status": "active"
  },
  {
    "height": 578141,
    "hash": "0000000000000000001253a5f37d3763dbe928d21f7d72a708f05268c044179c",
    "branchlen": 1,
    "status": "valid-fork"
  },
  {
    "height": 575695,
    "hash": "0000000000000000002409ed07fdbb1d0359a0c516014115c5451aea724baec8",
    "branchlen": 1,
    "status": "valid-headers"
  },
  ...
```

* `brachlen` – tells you how many blocks are in the competing chain of blocks.
* `status` – indicates the following:
  + `active` – This is our current active chain (the longest chain).
  + `valid-fork` – **Our node performed a chain reorganization.** We downloaded and validated these blocks and had them as part of our active chain, but we later deactivated them after receiving a new longer chain of blocks.
  + `valid-headers` – **Our node observed a possible chain reorganization.** We downloaded these blocks, but did not validate them as our active chain was equivalent and became longer.
  + `headers-only` – **Our node observed a possible chain reorganization.** We received the block headers for a competing chain but did not download the full blocks.
  + `invalid` – A branch that contains invalid blocks.

[<img src="../../images/diagrams_png_blockchain-chain-reorganization-getchaintips-status.png" alt="Diagram showing the difference between valid-fork, valid-headers, and headers-only." width="983" height="336" />](https://static.learnmeabitcoin.com/diagrams/png/blockchain-chain-reorganization-getchaintips-status.png)

The branches with the status of `valid-fork` are the ones with blocks that we originally considered part of our active blockchain, but we later deactivated them after receiving a new longer chain of blocks.

The branches with the status of `valid-headers` are competing chains that we received *after* already having an equivalent active chain. These could have resulted in a reorganization, but our chain continued as the longest chain, so no reorganization took place.

**You're unlikely to see any chain reorganizations if you have not been running your node continuously for a few weeks or months.** When your node [downloads the blockchain](/docs/technical/blockchain.md#download) it will only download the blocks in the current longest chain (and not blocks from any branches or old chain reorganizations). Your node needs to experience chain reorganizations *as they happen* for them to show up in `bitcoin-cli getchaintips`.

## Summary

Chain reorganizations are a *perfectly normal* part of a Bitcoin node's function. Adopting the longest known chain allows nodes across a network to agree on the same blockchain, and chain reorganizations are just a part of this process.

Transactions inside blocks that are deactivated due to a chain reorganization will become invalid, but they will be recycled into the memory pool for the opportunity to be mined into a block on the new longest chain.

So basically, if your transaction gets mined into a block, there's still a chance that it could get thrown back into the mempool due to a chain reorganization. However, these natural reorgs typically only happen to the **top block** on the chain, so you should wait for your transaction to make it 2 blocks deep to help avoid this scenario.

## Resources

* [How to detect a fork with bitcoin-cli?](https://bitcoin.stackexchange.com/questions/44437/how-to-detect-a-fork-with-bitcoin-cli)
* [Understanding getchaintips in terms of chain reorganisations](https://bitcoin.stackexchange.com/questions/91111/understanding-getchaintips-in-terms-of-chain-reorganisations)
* [The difference between stale and orphan blocks](https://technicaldifficulties.io/2022/07/29/the-difference-between-stale-and-orphan-blocks/)