<img src="../../images/icons_loader-2.svg" alt="Loading Tool" style="height:32px; width:32px;" />

[<img src="../../images/diagrams_png_block-version.png" alt="Diagram showing the location of the nonce field inside the block header and how the last 29 bits are used to signal readiness for soft forks." width="639" height="404" />](https://static.learnmeabitcoin.com/diagrams/png/block-version.png)

The 4-byte version field in the [block header](/docs/technical/block.md#header) is used by miners to ***signal* readiness for proposed [soft-forks](/docs/technical/blockchain/soft-fork.md)**.

Version numbers are used in software to signify upgrades or the addition of new features. However, bitcoin is decentralized, so there's no central authority to force everyone to upgrade to new versions of the software. Therefore, it's ideal if the majority of the network can agree to proposed changes in advance.

So the version field is basically used to "vote" for proposed upgrades to the software.

> They're not actually votes though. Any majority of miners can start enforcing a new rule - they don't need to indicate it in blocks, or even tell anyone about it. What [the version field] does is prove a way to signal readiness, so that a safe and coordinated transition point can be found.

Pieter Wuille, [bitcoin.stackexchange.com](https://bitcoin.stackexchange.com/questions/50446/what-are-the-possible-version-bits-votes)

## Version Numbers

Up until 2015, the version number was incremented to signal readiness for new for upgrades. This happened until the version number was 4:

* `0x00000001` = The original software
  + Height Activated: [0](/explorer/0#blockchain)
* `0x00000002` = [BIP 34](https://github.com/bitcoin/bips/blob/master/bip-0034.mediawiki): Height in Coinbase
  + Height Activated: [227,931](/explorer/227931#blockchain)
* `0x00000003` = [BIP 66](https://github.com/bitcoin/bips/blob/master/bip-0066.mediawiki): Strict DER signatures
  + Height Activated: [363,725](/explorer/363725#blockchain)
* `0x00000004` = [BIP 65](https://github.com/bitcoin/bips/blob/master/bip-0065.mediawiki): OP\_CHECKLOCKTIMEVERIFY
  + Height Activated: [388,381](/explorer/388381#blockchain)

These upgrades became permanent when *950 out of 1000* blocks over a given time period were mined using the new version number. And once those upgrades were active, all new blocks had to use the new version number (or greater).

This system works, but the drawback is that you can only signal for **one change at a time**.

Due to these upgrades, the required minimum version number for a block is now `0x00000004`. Any version number below that will be rejected by nodes on the network.

## Version Bits

In 2015 the version field was changed to be used as a [bit field](/docs/technical/general/bytes.md#bit-field), which allows miners to signal for up to 29 proposed new features at the same time.

Different [bits](/docs/technical/general/bytes.md#bit) in the 32-bit (4-byte) version field can be designated at the same time to signal readiness for a different [soft fork](/docs/technical/blockchain/soft-fork.md). So all you have to do to signal readiness for a specific upgrade is turn a specific bit "on" (i.e. set it to **1**).

Random Example

Bit Field

0

0

1

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0

0



Hex

0x

`4 bytes`




* **Version Bits:** Enabled

The following bits have been used for upgrades:

* **Bit 0:** [BIP 112](https://github.com/bitcoin/bips/blob/master/bip-0112.mediawiki): CHECKSEQUENCEVERIFY
  + Example: `0b00100000000000000000000000000001`
  + Height Activated: [419,328](/explorer/419328#blockchain)
* **Bit 1:** [BIP 141](https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki): Segwit
  + Example: `0b00100000000000000000000000000010`
  + Height Activated: [481,824](/explorer/481824#blockchain)
* **Bit 2:** [BIP 341](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki): Taproot
  + Example: `0b00100000000000000000000000000100`
  + Height Activated: [709,632](/explorer/709632#blockchain)

To use "version bits" for signaling, you have to set the first 3 bits to `0b001` (as specified in [BIP 9](https://github.com/bitcoin/bips/blob/master/bip-0009.mediawiki)). This is just a requirement that indicates that you're making use of the version field as a bit field for signaling. So this is why you can only signal for a maximum of 29 different upgrades at the same time (32 - 3 = 29 bits).

Each proposal has its own time period for signaling, where a specific number of blocks have to signal for the upgrade over a specific window for it to become activated. With the [taproot upgrade](/docs/technical/upgrades/taproot.md) for example, 90% of blocks over a 2016-block [target](/docs/technical/mining/target.md) adjustment period had to signal for the upgrade (starting on 24 April 2021 and ending 11 August 2021), which eventually did happen, and the deployment activated at block height [709,632](/explorer/709632#blockchain).

You can view the past and current upgrades being voted for via `bitcoin-cli getblockchaininfo`.

A list of all the bit assignments for proposed upgrades can be found on the [BIP 9 assignments](https://github.com/bitcoin/bips/blob/master/bip-0009/assignments.mediawiki) page, but I don't think it's frequently updated.

## Examples

Here are some examples of version numbers you'll find in the history of the blockchain.

* `0x00000001` - The majority of blocks up until block height [200,000](/explorer/200000#blockchain) use this version number.
  + Example: [000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f](/explorer/block/000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f) (Height [0](/explorer/0#blockchain))
* `0x00000002` - The majority of blocks between [227,931](/explorer/227931#blockchain) to [363,724](/explorer/363724#blockchain) use this version number.
  + Example: [000000000000024b89b42a942fe0d9fea3bb44ab7bd1b19115dd6a759c0808b8](/explorer/block/000000000000024b89b42a942fe0d9fea3bb44ab7bd1b19115dd6a759c0808b8) (Height [227,931](/explorer/227931#blockchain))
* `0x00000003` - The majority of blocks between [363,725](/explorer/363725#blockchain) to [388,380](/explorer/388380#blockchain) use this version number.
  + Example: [00000000000000000379eaa19dce8c9b722d46ae6a57c2f1a988119488b50931](/explorer/block/00000000000000000379eaa19dce8c9b722d46ae6a57c2f1a988119488b50931) (Height [363,725](/explorer/363725#blockchain))
* `0x00000004` - The majority of blocks between [388,381](/explorer/388381#blockchain) to around [411,000](/explorer/411000#blockchain) use this version number.
  + Example: [000000000000000004c2b624ed5d7756c508d90fd0da2c7c679febfa6c4735f0](/explorer/block/000000000000000004c2b624ed5d7756c508d90fd0da2c7c679febfa6c4735f0) (Height [388,381](/explorer/388381#blockchain))

After around the block height [411,000](/explorer/411000#blockchain) the version field starts being used as a bit field more frequently (as opposed to a simple number). This is why the version "numbers" look so much larger, because the first 3 bits now being set as `0b001`.

* `0x20000000` - Version bits being used, but not signaling for any upgrade in particular.
  + Version Bits: `0b00100000000000000000000000000000`
  + Example: [000000000000000005025d88492c54a51ac3bccaaa15c12a05aee16a28d6b294](/explorer/block/000000000000000005025d88492c54a51ac3bccaaa15c12a05aee16a28d6b294) (Height [410,370](/explorer/410370#blockchain))
* `0x20000001` - Version bits being used to signal for the CSV upgrade.
  + Version Bits: `0b00100000000000000000000000000001`
  + Example: [000000000000000004983f04183f2a6ae7f1cdf6ddb8f4b3f79e39e14392db4c](/explorer/block/000000000000000004983f04183f2a6ae7f1cdf6ddb8f4b3f79e39e14392db4c) (Height [416,498](/explorer/416498#blockchain))
* `0x20000002` - Version bits being used to signal for the [Segwit upgrade](/docs/technical/upgrades/segregated-witness.md).
  + Version Bits: `0b00100000000000000000000000000010`
  + Example: [0000000000000000001094a0145695e4228c21cbbc6be40507f728c6b7d6f16a](/explorer/block/0000000000000000001094a0145695e4228c21cbbc6be40507f728c6b7d6f16a) (Height [471,329](/explorer/471329#blockchain))
* `0x20000004` - Version bits being used to signal for the [Taproot upgrade](/docs/technical/upgrades/taproot.md).
  + Version Bits: `0b00100000000000000000000000000100`
  + Example: [00000000000000000004f065fae967b93540f321076684fe926d4e7bfbcd77ab](/explorer/block/00000000000000000004f065fae967b93540f321076684fe926d4e7bfbcd77ab) (Height [703,353](/explorer/703353#blockchain))

Here are some "non-standard" version numbers that pop up every now and then:

* `0x30000000` - I believe this may have been an unofficial bit used to signal support for 2 MB blocks. It appears 2,058 times between blocks [398,364](/explorer/398364#blockchain) and [476,482](/explorer/476482#blockchain).
  + Version Bits: `0b00110000000000000000000000000000`
  + Example: [0000000000000000018c393bb66dac52e1a2131ab2332b4d6e2caed463209892](/explorer/block/0000000000000000018c393bb66dac52e1a2131ab2332b4d6e2caed463209892) (Height [414,996](/explorer/414996#blockchain))
* `0x08000004` - This is another unofficial signal for [adaptive block sizes](https://github.com/bitpay/bips/blob/master/bip-adaptiveblocksize.mediawiki). It appears 39 times between blocks [416,832](/explorer/416832#blockchain) and [455,757](/explorer/455757#blockchain).
  + Version Bits: `0b00001000000000000000000000000100`
  + Example: [00000000000000000479bbbf51d485ddc7b161998b6f54049e576b09fd72e363](/explorer/block/00000000000000000479bbbf51d485ddc7b161998b6f54049e576b09fd72e363) (Height [416,832](/explorer/416832#blockchain))

## Current Default

The default version in the block header is currently:

```
0b00100000000000000000000000000000
```

Which in hex is

```
0x20000000
```

This indicates that you're using "version bits" (i.e. the first 3 bits are set to `0b001`), but without signaling for any proposed new features (all the other bits are set to zero).

The first *bit* in the version field can never be 1, as this would indicate a negative number, which would be invalid. This is because Bitcoin uses a custom encoding for [uint256](https://github.com/bitcoin/bitcoin/blob/master/src/arith_uint256.cpp) values.

```
This bit cannot be set to 1, or the version will be invalid:

00000000000000000000000000000000
↑
```

## Extra Nonce

There are no restrictions on what values you can put in the version field (other than it must be a minimum of `0x00000004`, and the first bit must not be `1`), so miners sometimes use it as an [extra nonce](/docs/technical/block/nonce.md#extranonce) when mining.

This is why since around block height [600,000](/explorer/600000#blockchain) (also before, but more so since then) you often see some "weird" version numbers in the block header that do not correspond to any proposed upgrades. For example:

* `0x2844a000` - Using *version bits* with some bits set, but none of them correspond to a proposed upgrade.
  + Version Bits: `0b00101000010001001010000000000000`
  + Example: [00000000000000000479bbbf51d485ddc7b161998b6f54049e576b09fd72e363](/explorer/block/00000000000000000479bbbf51d485ddc7b161998b6f54049e576b09fd72e363) (Height [791,617](/explorer/791617#blockchain))

Again, these version numbers are signaling for anything in particular; they've just been adjusted so the miner can continue [hashing](/docs/technical/cryptography/hash-function.md) their current block without having to rebuild it completely.

## Resources

* [Version bits FAQ for miners](https://bitcoincore.org/en/2016/06/08/version-bits-miners-faq/)
* [What restrictions does the version field in the block header have?](https://bitcoin.stackexchange.com/questions/117530/what-restrictions-does-the-version-field-in-the-block-header-have)
* [What are version bits?](https://bitcoin.stackexchange.com/questions/39216/what-are-version-bits)