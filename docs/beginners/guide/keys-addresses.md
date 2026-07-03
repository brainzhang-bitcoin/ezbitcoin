![Loading Tool](../../images/icons_loader-2.svg)

To send and receive bitcoins you need some sort of "account number" and "password".

In Bitcoin, we call these a [public key](/docs/beginners/guide/public-keys.md) and a [private key](/docs/beginners/guide/private-keys.md).

[![Diagram showing a public key as an account number and a private key as the password.](../../images/beginners_guide_keys-addresses_01-private-public.png)](https://static.learnmeabitcoin.com/beginners/guide/keys-addresses/01-private-public.png)

Here are your account details. Welcome to Bitcoin.

However, this "account number" is an awkwardly long *number*. So to make life easier we create a *shortened* version of this public key, which we call an address.

[![Diagram showing an address another version of the account number.](../../images/beginners_guide_keys-addresses_01-private-public-address.png)](https://static.learnmeabitcoin.com/beginners/guide/keys-addresses/01-private-public-address.png)

You'll see how hideous the public key is in a moment.

So to summarize:

* **Public Key** – Your *account number*.
  + **Address** –Also your *account number*, but a shorter version that people use when sending you bitcoins.
* **Private Key** – Your *password*. This prevents other people from sending bitcoins from your address.

## Where do keys and addresses come from?

All the keys used in Bitcoin are randomly generated on your computer.

### [Private Key](/docs/beginners/guide/private-keys.md)

It all starts with the private key, which is just a **randomly generated number**:

[![Illustration showing a private key being produced by a random number generator.](../../images/beginners_guide_keys-addresses_02-random-private.png)](https://static.learnmeabitcoin.com/beginners/guide/keys-addresses/02-random-private.png)

But because this number is so large, we usually display it in [hexadecimal](/docs/technical/general/hexadecimal.md) format:

[![Diagram showing a private key converted to hexadecimal format.](../../images/beginners_guide_keys-addresses_02-random-private-hex.png)](https://static.learnmeabitcoin.com/beginners/guide/keys-addresses/02-random-private-hex.png)

Hexadecimal numbers are shorter than decimal numbers because they also use the letters a, b, c, d, e and f.

And there we have a private key; just a big random number.

For example:

|  |  |
| --- | --- |
| Private Key | ef235aacf90d9f4aadd8c92e4b2562e1d9eb97f0df9ba3b508258739cb013db2 |

**Do not use the example private key (or address) on this page.** I'm just showing these as examples of what they look like. All of your private keys should be generated securely on your own computer/device and kept secret.

A private key can be any number between **1** and **115792089237316195423570985008687907852837564279074904382605163141518161494336**.

### [Public Key](/docs/beginners/guide/public-keys.md)

You use your private key to calculate your public key.

But first, this public key is going to be seen by other people. Therefore, when we use the private key to create our public key, **we don't want it to be possible for anyone to figure out what our private key was**.

Because after all, the private key protects our bitcoins.

[![Diagram showing how a private key is used to calculate the public key, but you cannot calculate the private key from the public key.](../../images/beginners_guide_keys-addresses_03-public-private-one-way.png)](https://static.learnmeabitcoin.com/beginners/guide/keys-addresses/03-public-private-one-way.png)

We don't want anyone to be able to work backwards from the public key to the private key.

Fortunately, we can use a special type of **mathematical function** to achieve this.

We just shove the private key (which is a number after all) in to this function, and the function spits out a public key (which is another number again).

[![Diagram showing a private key being put through a mathematical function to produce a public key.](../../images/beginners_guide_keys-addresses_03-public-private-one-way-function.png)](https://static.learnmeabitcoin.com/beginners/guide/keys-addresses/03-public-private-one-way-function.png)

Now, there are two benefits of using this particular function:

1. **There is a mathematical connection between the private key and public key.** This will come in handy later on when we want to spend our bitcoins in a [transaction](/docs/beginners/guide/transactions.md).  
   ![Illustration showing how the private key fits the public key like a traditional key and lock.](../../images/beginners_guide_keys-addresses_03-public-private-mathematical-fit.png)
2. **It's not possible to figure out the private key from the public key**. Even though the public key is calculated *from* the private key, we're using what's known as a "one-way" function, so you can't work backwards from the public key to calculate the private key.

And ta-da, thanks to our random number and this function, we now have a *pair of keys* that we can use to send and receive bitcoins:

|  |  |
| --- | --- |
| Private Key | ef235aacf90d9f4aadd8c92e4b2562e1d9eb97f0df9ba3b508258739cb013db2 |
| Public Key | 02b4632d08485ff1df2db55b9dafd23347d1c47a457072a1e87be26896549a8737 |

### Address

That public key is hideous isn't it. Nobody is going to enjoy typing that out.

So let's make it a bit prettier and call it an address.

[![Diagram showing a public key being converted to a shorter address format.](../../images/beginners_guide_keys-addresses_04-public-address-pretty.png)](https://static.learnmeabitcoin.com/beginners/guide/keys-addresses/04-public-address-pretty.png)

Thank goodness.

All we've done here is *compress* the public key (using [hash functions](/docs/technical/cryptography/hash-function.md)), and convert it to a format that doesn't use any characters that look similar to each other when written down (called [Base58](/docs/technical/keys/base58.md)).

So it's still not the shortest and sweetest piece of data you've ever seen, but it *is* an improvement.

And that's all an address is; a shorter version of the public key:

|  |  |
| --- | --- |
| Private Key | ef235aacf90d9f4aadd8c92e4b2562e1d9eb97f0df9ba3b508258739cb013db2 |
| Public Key | 02b4632d08485ff1df2db55b9dafd23347d1c47a457072a1e87be26896549a8737 |
| Address | 1EUXSxuUVy2PC5enGXR1a3yxbEjNWMHuem |

**It's not possible to work backwards from the address to the public key either.** This is due to the use of hash functions when compressing the public key.

## Do I have to remember all 3 keys?

Because your public key and address are worked out *from* your private key, **you can get away with just saving your private key**.

[![Diagram showing the private key as the source of the public key and address.](../../images/beginners_guide_keys-addresses_05-private-source.png)](https://static.learnmeabitcoin.com/beginners/guide/keys-addresses/05-private-source.png)

So if worse comes to worst, if you ever need to send your address to someone, you can just work it out from your private key.

You're most likely going to be using a [wallet](/docs/beginners/wallets.md), so managing your individual private keys and addresses isn't really an issue. The only thing you need to keep safe when using a wallet is your [seed](/docs/technical/keys/hd-wallets/mnemonic-seed.md).

## What happens if I lose my private key?

Well then you're fu…*lly out of luck*.

**It's impossible to work out your private key from either your public key or address**, so if you lose your private key, it's gone.

[![Diagram showing how you can't work backwards from an address or public key to the private key.](../../images/beginners_guide_keys-addresses_05-private-lost.png)](https://static.learnmeabitcoin.com/beginners/guide/keys-addresses/05-private-lost.png)

You can't calculate your private key from your address or public key.

And if you haven't got the private key for an address, any bitcoins located at that address will be locked there forever.

How's that for security?

This may seem like an unforgiving system, and that's because it is.

On the other hand, it's refreshing to know that there are no backdoors to your money. There is only one key to your bitcoins, and you're in charge of it.

[![Illustration of someone trying to call Bitcoin for support after losing their private key.](../../images/beginners_guide_keys-addresses_lol-customer-support.png)](https://static.learnmeabitcoin.com/beginners/guide/keys-addresses/lol-customer-support.png)