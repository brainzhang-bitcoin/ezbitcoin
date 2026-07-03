![Loading Tool](../../images/icons_loader-2.svg)

A public key is the counterpart to a [private key](/technical/keys/private-key/).

And similar to a private key, it's displayed as a [hexadecimal](/technical/general/hexadecimal/) string.

For example:

```
0322406f1fe31f7179a85dedde622fe492ec37448a22d11bc122d16bd2f8576e10
```

If we didn't end up shortening this public key to an [address](/technical/keys/address/), this would be the "account number" that you send bitcoins to when making a [transaction](/beginners/guide/transactions/).

Anyway, here's the interesting part: **your public key is calculated *from* your private key**.

## How do you get a public key from a private key?

You insert a private key into a special *mathematical function*, and the result is a public key.

### What is this function?

It's called **[elliptic curve multiplication](/technical/cryptography/elliptic-curve/#multiply)**.

This basically involves "bouncing" around the graph of an elliptic curve until you end up at a final set of co-ordinates on the graph, and these resulting co-ordinates are your public key.

It'll be easier if I show you...

### What does an elliptic curve look like?

Like this:

[![A simple graph showing the shape of an elliptic curve.](../../images/beginners_guide_public-keys_01-elliptic-curve.png)](https://static.learnmeabitcoin.com/beginners/guide/public-keys/01-elliptic-curve.png)

Furthermore, the [elliptic curve used in Bitcoin](/technical/cryptography/elliptic-curve/) comes with a specific *starting point*.

[![A simple graph showing the generator point on an elliptic curve.](../../images/beginners_guide_public-keys_01-elliptic-curve-g.png)](https://static.learnmeabitcoin.com/beginners/guide/public-keys/01-elliptic-curve-g.png)

We call this starting point the *generator point* (G).

And if we were to do some "multiplication" on this curve (e.g. "multiplying" the starting point by 2), we would move around the curve like this.

[![Diagram showing elliptic curve multiplication.](../../images/beginners_guide_public-keys_01-elliptic-curve-g-multiplication.png)](https://static.learnmeabitcoin.com/beginners/guide/public-keys/01-elliptic-curve-g-multiplication.png)

The fact that we can draw a tangent anywhere on the curve and it intersects *one* other point on the curve is a special feature of elliptic curves.

And there we have it. We have just "multiplied" the starting co-ordinate **G** by 2, and found the position of the final co-ordinate **2G**.

This is *one round* of elliptic curve multiplication.

#### Elliptic curve multiplication

I keep putting "multiplication" inside quotes, because multiplication on elliptic curves is **not standard multiplication**. For example, if you were to multiply the co-ordinates of G by 2, it would not give you the co-ordinates of 2G (as shown on the graph).

You see, the geniuses who found out that you can move around the curve in this specific way had to call it something, so they to decided refer to this operation as "multiplication". Because, you know, mathematics can never be confusing enough.

So when I say "multiplication" from now on, I mean "elliptic curve multiplication".

### How do you create a public key?

In the above example we multiplied `G` by 2 to get `2G`.

To get a public key, we multiply `G` by our private key.

```
private key = f18f3c944012871ad7b90a4aaf457b8e679b3021349edc5bad7b1753e857001f
private key = 109260473740431031271649203294974511900235291483950379992408167175706784497695

public key  = 109260473740431031271649203294974511900235291483950379992408167175706784497695 * G
```

![Tool Icon](../../images/icons_tool.svg) EC Multiply

Generator Point

Random Point


Point 1

x:

0d

y:

0d


Multiplier

0d



+1

Random


Point 1 x Multiplier

x:

0d

y:

0d



Steps
 



0 secs

Or in other words, "bounce around the elliptic curve private key number of times".

[![Diagram showing multiplication on an elliptic curve.](../../images/beginners_guide_public-keys_02-public-key-multiplication.png)](https://static.learnmeabitcoin.com/beginners/guide/public-keys/02-public-key-multiplication.png)

The final resting point on the elliptic curve will give you a set of co-ordinates, and these co-ordinates form the public key.

So if these are the coordinates we end up with after multiplying `G` by our private key:

```
x = 15492482017498539452774967995455736955834329920153210634105963099022205349392
y = 66484543299854344167676653054794377465478015196270132341507299112734572147511
```

Then all we have to do is convert both to hexadecimal and smush them together...

```
public key (x) = 22406f1fe31f7179a85dedde622fe492ec37448a22d11bc122d16bd2f8576e10
public key (y) = 92fceb0155aaeadfe714c2c71aedaa1745f4c904675bdf29e24081e34623f337

public key (x,y) = 22406f1fe31f7179a85dedde622fe492ec37448a22d11bc122d16bd2f8576e1092fceb0155aaeadfe714c2c71aedaa1745f4c904675bdf29e24081e34623f337
```

![Tool Icon](../../images/icons_tool.svg) Public Key

Generate Random

Private Key

`0 bytes`

Public Key


Coordinates

x:

0d

y:

0d

parity:

A public key is just a point on an elliptic curve. The final public key is these coordinates in hexadecimal.

Compression
 Compressed (02 or 03 prefix)
 Uncompressed (04 prefix)
 x-only (no prefix)

The elliptic curve is symmetrical along the x-axis, so a *compressed* public key only needs to store the full x-coordinate and whether the y-coordinate is even or odd.

An x-only public key is used in [Taproot](/technical/upgrades/taproot/) outputs. The corresponding y-coordinate is assumed to be even.

`0 bytes`



**Never enter your private key into a website, or use a private key generated by a website.** Websites can easily save the private key and use it to steal your bitcoins.

0 secs

And ta da! A public key!

#### Public key format

This is the *old* (long) format of public key, which means I've got to put an `04` at the start. Like this:

```
public key = 0422406f1fe31f7179a85dedde622fe492ec37448a22d11bc122d16bd2f8576e1092fceb0155aaeadfe714c2c71aedaa1745f4c904675bdf29e24081e34623f337
```

To find out why this is the case, I'm afraid you're going to have to read through the section about [compressed public keys](#compressed-public-keys).

### Compressed Public Keys

To save space, public keys (these days) use the full `x` coordinate only.

This is because the elliptic curve is an *equation* (`y^2 = x^3 + 7`), which means that if you have the `x` co-ordinate, you can work out the corresponding `y` co-ordinate.

However, due to the `y^2` part of the equation, the `y` could be a *positive* or *negative* number:

[![Diagram showing two possible y-coordinates for a given x coordinate on the elliptic curve.](../../images/beginners_guide_public-keys_03-y-polarity.png)](https://static.learnmeabitcoin.com/beginners/guide/public-keys/03-y-polarity.png)

So the only extra information you need to find the correct `y` co-ordinate is to know whether the `y` co-ordinate is *above* or *below* the x-axis. And due to the way elliptic curves work:

* If `y` is **even**, it's *above* the x-axis.
* If `y` is **odd**, it's *below* the x-axis.

So instead of having to store both the full `x` and `y` co-ordinates, you can just store the full `x` co-ordinate, and whether the `y` co-ordinate is *even* or *odd*.

In Bitcoin, the polarity of the `y` co-ordinate is represented by a prefix:

* `02` = even
* `03` = odd

[![Diagram showing how a prefix is used to represent one of two possible y-coordinates on the elliptic curve.](../../images/beginners_guide_public-keys_03-y-polarity-prefix.png)](https://static.learnmeabitcoin.com/beginners/guide/public-keys/03-y-polarity-prefix.png)

So whereas an old-school uncompressed public key will begin with `04`, a **compressed public key** will begin with either `02` or `03`:

```
public key (uncompressed) = 0422406f1fe31f7179a85dedde622fe492ec37448a22d11bc122d16bd2f8576e1092fceb0155aaeadfe714c2c71aedaa1745f4c904675bdf29e24081e34623f337
public key (compressed)   = 0322406f1fe31f7179a85dedde622fe492ec37448a22d11bc122d16bd2f8576e10
```

Much shorter.

This seems like a lot of effort to save on a small amount of data, but because public keys are used within almost all transactions, it does end up saving a lot of space in the [blockchain](/beginners/guide/blockchain/) over time.

## Why do we use elliptic curve multiplication to make public keys?

Because elliptic curves have two useful properties when creating a private/public key pair.

1. **Elliptic curve multiplication is a "trapdoor function"**. In other words, you can't go backwards from public key to find out what the private key was.  

   > A trapdoor function is a function that is easy to compute in one direction, yet difficult to compute in the opposite direction (finding its inverse) without special information, called the "trapdoor".
2. **The public key has a *mathematical connection* to the private key.** As a result, it's possible to prove this connection (with a little more mathematics) without having to reveal your private key.

   So if I give you my public key (or [address](/technical/keys/address/)), I can prove to you that I "own" it without having to show you my private key.

   This feature is especially handy when making bitcoin [transactions](/beginners/guide/transactions/). Your public key can be placed into a transaction when you want to receive bitcoins, and you do not have to reveal the private key directly when you want to spend them later on (see [digital signatures](/beginners/guide/digital-signatures/)). As a result, this means that nobody can acquire the private key and use it to spend bitcoins that have been locked to the same public key.

   When I say *prove* that I own a public key, I mean "show that I possess the private key that the public key was created from".

### How can you prove you own a public key?

This is a whole topic (or two) in itself. But seeing as this is such an annoyingly relevant question, I'll try my best to cover the basics.

As mentioned, there's a mathematical connection between the private key and public key.

As a result:

1. I can put my private key through some more elliptic curve mathematics to get ***a new value*** (called a digital signature).
2. I can put my public key through some other elliptic curve mathematics to get ***a new value***.

[![Diagram showing two separate values being calculated from the private key and public key independently.](../../images/beginners_guide_public-keys_04-keys-ec-math.png)](https://static.learnmeabitcoin.com/beginners/guide/public-keys/04-keys-ec-math.png)

Now, there will be some small *overlap* between these new values:

[![Diagram showing and overlap between the two separate values calculated from the private key and public key independently.](../../images/beginners_guide_public-keys_04-keys-ec-math-verification.png)](https://static.learnmeabitcoin.com/beginners/guide/public-keys/04-keys-ec-math-verification.png)

And this overlap is enough to prove that there is a *mathematical connection* between the public key and private key.

And because nobody is able to recreate this digital signature without the private key, my digital signature it's enough to prove that I "own" the public key.

As a result, I can show you that I own a public key with a digital signature, and you never need to see my private key.

### Conclusion

All hail the elliptic curve.