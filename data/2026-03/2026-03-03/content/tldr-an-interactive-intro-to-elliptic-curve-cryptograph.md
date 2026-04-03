---
title: An interactive intro to Elliptic Curve Cryptography (ECC) | growingSWE
url: https://growingswe.com/blog/elliptic-curve-cryptography
site_name: tldr
content_file: tldr-an-interactive-intro-to-elliptic-curve-cryptograph
fetched_at: '2026-03-03T19:19:46.545506'
original_url: https://growingswe.com/blog/elliptic-curve-cryptography
date: '2026-03-03'
published_date: '2026-02-28'
description: A hands-on introduction to elliptic curve cryptography. Start with curve geometry, build point addition and scalar multiplication, see why ECDLP is hard, and then use that math in ECDH, ECDSA, and ECIES.
tags:
- tldr
---

# An interactive intro to Elliptic Curve Cryptography

For my Master's program, I recently took a course on Applied Cryptography which I really enjoyed. I will be writing several posts on various cryptography concepts to cement what I learned

Suppose two people want to communicate privately over the internet. They could encrypt their messages, scrambling them so that only someone with the right secret key can read them. But that raises an immediate problem: how do they agree on that secret key in the first place? They can't whisper it to each other. Every message between them passes through the open internet, where anyone could be listening.

One solution ispublic-key cryptography: each person has two linked keys, aprivate keythey keep secret and apublic keythey share openly. The keys are mathematically related, but computing the private key from the public key is so hard it's effectively impossible. That one-way relationship is what lets you encrypt messages, agree on shared secrets, and sign data to prove authorship.

The first widely used public-key systems were built on the difficulty of specific math problems.RSArelies on the fact that multiplying two large prime numbers is easy, but factoring the result back into those primes is extremely hard.Diffie-Hellmanrelies on a similar idea using exponents inmodular arithmetic(clock arithmetic where numbers wrap around at a fixed value).

Both systems work, and both are still in use. But they share a practical problem: the keys are enormous. A commonly recommended minimum for RSA today is 2048 bits (about 617 decimal digits), but for 128-bit security equivalence RSA needs 3072 bits. As we push for stronger security, the numbers grow fast: RSA key sizes grow much faster than security targets, because the underlying factoring attacks are sub-exponential.

What if a different mathematical structure could give us the same guarantees (easy in one direction, effectively impossible in reverse) but with much smaller numbers? That structure exists, and it comes from the geometry of curves.

## Drawing the curve

A mathematical equation can define a shape. Take the equationy=x2y = x^2y=x2, which says "y equals x squared." To draw it, you pick values ofxxx, computeyyy, and plot each resulting point on a grid. Step through the process below:

Plotting y = x²
x
y
(
-3
, 
9
)
-3
x = -3 → y = -3² = 9 → plot (-3, 9)
x = -2.5 → y = -2.5² = 6.25 → plot (-2.5, 6.25)
x = -2 → y = -2² = 4 → plot (-2, 4)
x = -1.5 → y = -1.5² = 2.25 → plot (-1.5, 2.25)
x = -1 → y = -1² = 1 → plot (-1, 1)
x = -0.5 → y = -0.5² = 0.25 → plot (-0.5, 0.25)
x = 0 → y = 0² = 0 → plot (0, 0)
x = 0.5 → y = 0.5² = 0.25 → plot (0.5, 0.25)
x = 1 → y = 1² = 1 → plot (1, 1)
x = 1.5 → y = 1.5² = 2.25 → plot (1.5, 2.25)
x = 2 → y = 2² = 4 → plot (2, 4)
x = 2.5 → y = 2.5² = 6.25 → plot (2.5, 6.25)
x = 3 → y = 3² = 9 → plot (3, 9)
1
 / 
13

Each step picks anxxxvalue, squares it to getyyy, and places a dot at that coordinate. As the points accumulate, a curve appears: the parabola. The equation defined the shape all along; we just needed enough points to see it.

Different equations produce different shapes. The equationx2+y2=1x^2 + y^2 = 1x2+y2=1gives a circle (every point at distance 1 from the center). Toggle between these below:

Equations draw shapes
y = x²
x
y
y = x²
x² + y² = 1
y² = x³ − x + 1

Anelliptic curveis another equation of this kind:

y
2
=
x
3
+
a
x
+
b
y^2 = x^3 + ax + b
y
2
=
x
3
+
a
x
+
b

Selecty2=x3−x+1y^2 = x^3 - x + 1y2=x3−x+1in the demo above to see one. Thex3x^3x3term makes the right side grow much faster than the left, giving the curve its distinctive looping shape, different from the smooth symmetry of a circle or the open bowl of a parabola.

Despite the name, elliptic curves have nothing to do with ellipses. The name comes from elliptic integrals, which arose historically when computing the arc length of an ellipse. The connection is purely mathematical and not worth worrying about.

The constantsaaaandbbbdetermine the curve's shape. Adjust the sliders below and watch the curve change. Click anywhere on the curve to place a point:

Elliptic curve explorer
y² = x³ 
−
 
1.0
x 
+
 
1.0
x
y
Click on the curve to place a point
a = 
-1.0
b = 
1.0

Click a few different spots. Every point you place has a mirror: if(x,y)(x, y)(x,y)is on the curve, then(x,−y)(x, -y)(x,−y)is too, because squaring a negative number gives the same result as squaring its positive counterpart ((−y)2=y2(-y)^2 = y^2(−y)2=y2). The curve is always symmetric across the x-axis. This symmetry will matter when we define addition.

One constraint on the parameters: certain combinations ofaaaandbbbproduce a curve with a cusp or a self-intersection (a sharp point where the curve crosses itself). These are calledsingular curves, and they break the algebraic structure we need. Toggle between the three cases below to see what goes wrong:

Singular vs non-singular curves
y² = x³ − x + 1
x
y
Smooth curve with no sharp points or crossings. The algebraic structure works.
Non-singular
Cusp
Self-intersection

At a cusp, the curve comes to a sharp point where the tangent line is undefined. At a self-intersection, two branches of the curve cross, giving two tangent lines at one point. Both situations break the point addition we're about to define, which depends on there being exactly one tangent line at every point. The mathematical condition for avoiding singularities is that the discriminant4a3+27b2≠04a^3 + 27b^2 \neq 04a3+27b2=0. Cryptographic curves always satisfy this.

We have a curve. Now what? The idea that turned this into cryptography was to define anarithmeticon the points of the curve: a way to "add" two points together and get a third point, also on the curve.

## Adding points on a curve

The geometric construction goes like this. Take two pointsPPPandQQQon the curve. Draw a straight line through them. Because the equation is cubic (thex3x^3x3term), this line will generally intersect the curve at exactly one more point, call itR′R'R′(special cases like vertical lines or tangencies are handled by the point at infinity and the doubling rule). Now reflectR′R'R′over the x-axis, which means flipping its y-coordinate from positive to negative or vice versa. The reflected pointRRRis the result. We defineP+Q=RP + Q = RP+Q=R.

Move the sliders below to slidePPPandQQQalong the curve and watch the addition happen:

Point addition on an elliptic curve
R'
P
Q
P+Q
P = (
-1.50
, 
1.90
)
Q = (
1.80
, 
2.50
)
P+Q = (
-0.27
, 
-2.13
)
P.x = 
-1.5
Q.x = 
1.8

The dashed line goes throughPPPandQQQ. It hits the curve atR′R'R′(the unfilled circle). ReflectingR′R'R′over the x-axis gives usP+QP + QP+Q(the red point).

This "addition" isn't ordinary addition. We're not adding the coordinates together. We're using a geometric recipe (draw a line, find the intersection, reflect) to produce a new point from two existing ones. But mathematicians call it addition because it behaves like addition in the ways that matter.

It'sassociative, meaning thatP+(Q+R)=(P+Q)+RP + (Q + R) = (P + Q) + RP+(Q+R)=(P+Q)+R. There's anidentity elementcalled the "point at infinity"OOO, which acts like zero:P+O=PP + O = PP+O=Pfor any pointPPP. And every point has aninverse: the point directly below (or above) it, the reflection, sinceP+(−P)P + (-P)P+(−P)gives the point at infinity. These properties make the curve's points a mathematicalgroup. That's the algebraic structure the rest of this article depends on.

The algebra behind this construction uses the line's slope. For two distinct pointsP=(x1,y1)P = (x_1, y_1)P=(x1​,y1​)andQ=(x2,y2)Q = (x_2, y_2)Q=(x2​,y2​), the slope of the line through them is:

m
=
y
2
−
y
1
x
2
−
x
1
m = \frac{y_2 - y_1}{x_2 - x_1}
m
=
x
2
​
−
x
1
​
y
2
​
−
y
1
​
​

And the result point(x3,y3)(x_3, y_3)(x3​,y3​)is:

x
3
=
m
2
−
x
1
−
x
2
,
y
3
=
m
(
x
1
−
x
3
)
−
y
1
x_3 = m^2 - x_1 - x_2, \quad y_3 = m(x_1 - x_3) - y_1
x
3
​
=
m
2
−
x
1
​
−
x
2
​
,
y
3
​
=
m
(
x
1
​
−
x
3
​
)
−
y
1
​

But what happens whenPPPandQQQare the same point? You can't draw a line through a single point. Instead, you use the tangent line, the line that just touches the curve atPPP. Its slope comes from calculus (implicit differentiation of the curve equation):

m
=
3
x
1
2
+
a
2
y
1
m = \frac{3x_1^2 + a}{2y_1}
m
=
2
y
1
​
3
x
1
2
​
+
a
​

The rest of the formula is the same. This operation, adding a point to itself, is calledpoint doubling, and it's the building block for everything that follows.

## Climbing the curve

With point doubling, we can compute2P=P+P2P = P + P2P=P+P. Then3P=2P+P3P = 2P + P3P=2P+P. Then4P4P4P,5P5P5P, and so on. ComputingnPnPnPfor some integernnnis calledscalar multiplication: we're multiplying a point by a number to get another point.

The naive approach takesn−1n - 1n−1additions: addPPPto itselfnnntimes. But there's a much faster method. To compute100P100P100P, observe that100=64+32+4100 = 64 + 32 + 4100=64+32+4in binary. So compute2P2P2P,4P4P4P,8P8P8P,16P16P16P,32P32P32P,64P64P64Pby repeated doubling (six doublings), then add64P+32P+4P64P + 32P + 4P64P+32P+4P(two additions). That's eight operations instead of 99. In general, computingnPnPnPtakes roughlylog⁡2(n)\log_2(n)log2​(n)operations using thisdouble-and-addalgorithm. Even for a 256-bit number (roughly107710^{77}1077), that's only about 256 doublings and additions, which a computer does in a fraction of a second.

Step through the computation ofnGnGnGon a small curve:

Scalar multiplication
y² = x³ − 2x + 4,   G = (
-1.5
, 
1.9
)
G
x
y
n = 
8
1G = (-1.50, 1.90)
2G = (4.56, -9.46)
3G = (0.46, 1.78)
4G = (1.04, -1.74)
5G = (2.52, 3.88)
6G = (-0.78, -2.26)
7G = (35.99, 215.73)
8G = (-1.95, 0.68)
1
 / 
8

Watch the points hop around in what looks like a random pattern. Even on this small curve, there's no visible relationship betweennnnand the position ofnGnGnG. The points don't march along the curve in any recognizable order. They scatter unpredictably.

Elliptic curve cryptography depends on that apparent randomness.

## The trapdoor

Going forward is easy: givenPPPandnnn, computingQ=nPQ = nPQ=nPtakes roughlylog⁡2(n)\log_2(n)log2​(n)steps using double-and-add. Going backward is hard: givenPPPandQQQ, findingnnnsuch thatQ=nPQ = nPQ=nPhas no known shortcut on a well-chosen curve.

This is aone-way function(sometimes called a trapdoor): easy to compute forward, practically impossible to reverse. Every public-key system has one. For RSA, multiplying two large primes is easy but factoring their product is hard. For elliptic curves, scalar multiplication is easy but recovering the scalar is hard.

The problem of recoveringnnnis called theElliptic Curve Discrete Logarithm Problem(ECDLP). The name "discrete logarithm" comes from an analogy with regular logarithms: in regular math, ifbn=xb^n = xbn=x, thenn=log⁡b(x)n = \log_b(x)n=logb​(x). Here, ifnP=QnP = QnP=Q, we're looking for a kind of "logarithm" in the world of elliptic curve points. "Discrete" means we're working with integers, not continuous numbers.

Step through a brute-force search to see what "going backward" looks like:

Brute-force ECDLP search
Given G
:
 
(-1.5, 1.9)
Given Q = nG
:
 
(1.57, 2.17)
Find
:
 
n = ?
Q
G
1
G
x
y
Tried 
1
 of 
12
 values. No match yet
1G = (-1.50, 1.90). No match
2G = (4.56, -9.46). No match
3G = (0.46, 1.78). No match
4G = (1.04, -1.74). No match
5G = (2.52, 3.88). No match
6G = (-0.78, -2.26). No match
7G = (35.99, 215.73). No match
8G = (-1.95, 0.68). No match
9G = (10.79, -35.17). No match
10G = (-0.18, 2.09). No match
11G = (1.70, -2.34). No match
12G = (1.57, 2.17). Match!
1
 / 
12

On the small curve in this demo, the search finishes quickly becausennnis small. In real cryptography,nnnis roughly22562^{256}2256(a number with 77 digits). Even the best known algorithms would need about21282^{128}2128operations. If every computer on Earth worked on the problem, it would take longer than the age of the universe.

## From smooth curves to scattered dots

Everything so far used real-number coordinates like smooth curves, infinite precision and irrational slopes. Real cryptography can't work this way. Computers represent real numbers with floating-point arithmetic, which introduces tiny rounding errors. In cryptography, a single wrong bit means the wrong answer. We need exact arithmetic.

The fix is to work over afinite field. Instead of using all real numbers, we use only the integers from000top−1p - 1p−1, wherepppis a prime number. All arithmetic wraps around atppp, the same way a clock wraps around at 12.

This is calledmodular arithmetic(writtenmodp\bmod pmodp). For example, ifp=7p = 7p=7, then5+4=9≡2(mod7)5 + 4 = 9 \equiv 2 \pmod{7}5+4=9≡2(mod7)because 9 divided by 7 has remainder 2.

The curve equation becomes:

y
2
≡
x
3
+
a
x
+
b
(
m
o
d
p
)
y^2 \equiv x^3 + ax + b \pmod{p}
y
2
≡
x
3
+
a
x
+
b
(
mod
p
)

Nowxxxandyyyare integers from000top−1p - 1p−1. Division is replaced bymodular inverse, a number that, when multiplied, gives 1 moduloppp. (For example, the inverse of 3 modulo 7 is 5, because3×5=15≡1(mod7)3 \times 5 = 15 \equiv 1 \pmod{7}3×5=15≡1(mod7).) The point addition formulas stay exactly the same, just computed modppp.

The visual result is completely different. The smooth curve becomes a scattered cloud of dots:

Elliptic curve over a finite field
Curve
:
 
y² ≡ x³ + 1x + 6 (mod 23)
Points
:
 
20
Field size:
p = 23
p = 29
p = 37
p = 97

Click any point to see its inverse (the point with the same x-coordinate but negated y-coordinate, modppp). Despite looking random, these points satisfy the same equation and obey the same addition rules. The algebraic structure is fully preserved even though the geometry is gone. It's this version of the curve (over a finite field with a very large prime) that real cryptographic systems use.

The number of points on the curve is close toppp(more preciselyp+1−tp + 1 - tp+1−t, where∣t∣≤2p|t| \le 2\sqrt{p}∣t∣≤2p​by Hasse's theorem, so the count is close topppin relative terms). Cryptographic systems typically use a large prime-order subgroup of sizennnclose toppp. For curves using 256-bit primes, this gives roughly22562^{256}2256points to work in.

The trapdoor still applies. Scalar multiplication over a finite field is just as fast (log⁡2(n)\log_2(n)log2​(n)steps via double-and-add), and the ECDLP is at least as hard as it was over real numbers. It is harder, in fact, because the scattered-dot structure removes geometric intuition an attacker might exploit. All the constructions that follow (key exchange, signatures, encryption) work over this finite field.

## Exchanging secrets on a curve

With a set of points, an addition operation, and a one-way function (scalar multiplication that's easy to compute but hard to reverse), we can build a protocol for two people to agree on a shared secret over an open channel, without ever sending the secret itself.

This protocol is calledECDH(Elliptic Curve Diffie-Hellman). Alice and Bob agree publicly on a curve and a starting pointGGGcalled thegenerator. If you computeG,2G,3G,…G, 2G, 3G, \ldotsG,2G,3G,…, the points eventually cycle back to the start.

The number of steps before the points cycle is called theorderofGGG, writtennnn. For cryptographic curves,nnnis roughly22562^{256}2256, so the generator produces an enormous set of distinct points before repeating. Private keys are random scalars in the range[1,n−1][1, n-1][1,n−1]. (Some curves like X25519 accept 32 random bytes and deterministically "clamp" the bits into a safe scalar, simplifying key validation.)

1. Alice picks a random secret integeraaaas her private key. She computesaGaGaG(her public key) and sends it to Bob.
2. Bob picks a random secret integerbbbas his private key. He computesbGbGbG(his public key) and sends it to Alice.
3. Alice takes Bob's public keybGbGbGand multiplies it by her private key:a(bG)=abGa(bG) = abGa(bG)=abG.
4. Bob takes Alice's public keyaGaGaGand multiplies it by his private key:b(aG)=baGb(aG) = baGb(aG)=baG.

Since scalar multiplication is associative,abG=baGabG = baGabG=baG. Both arrive at the same point, the shared secret. An eavesdropper seesGGG,aGaGaG, andbGbGbG(all sent over the public channel), but computingabGabGabGfrom those values requires solving the ECDLP: findingaaafromGGGandaGaGaG, orbbbfromGGGandbGbGbG.

Adjust the private keys below and watch the shared secret update:

ECDH key exchange
Curve
:
 
y² = x³ + 1x + 6 (mod 23)
G
:
 
(7, 3)
Order
:
 
29
Alice
Private key: 
a = 
7
Public key: 
aG = 
(9, 12)
Computes: a(bG) = 
(4, 7)
Bob
Private key: 
b = 
13
Public key: 
bG = 
(15, 17)
Computes: b(aG) = 
(4, 7)
Alice a = 
7
Bob b = 
13

Both sides always arrive at the same point. In practice, the shared secret (usually just the x-coordinate of this point) is fed through a key derivation function to produce a symmetric encryption key, which is then used to encrypt the actual conversation.

## Signing with curves

Key exchange lets two people establish a shared secret. But cryptography also needsdigital signatures: a way to prove that a message came from a specific person and hasn't been tampered with. This is what you use when you sign a software update, authenticate a TLS certificate, or authorize a cryptocurrency transaction.

ECDSA(Elliptic Curve Digital Signature Algorithm) works like this. The signer has a private keyddd(a secret integer) and a public keyQ=dGQ = dGQ=dG(a point on the curve, published for anyone to see).

To sign a message:

1. Hash the message to get a numbermmm(ahash function, like SHA-256, turns any input into a fixed-size number)
2. Pick a random secretnoncekkk(a one-time random number, never reused)
3. Compute the pointR=kGR = kGR=kGon the curve
4. Setr=Rxmodnr = R_x \bmod nr=Rx​modn(the x-coordinate ofRRR, taken modulo the group ordernnn)
5. Computes=k−1(m+r⋅d)modns = k^{-1}(m + r \cdot d) \bmod ns=k−1(m+r⋅d)modn(using the modular inverse ofkkk)
6. Ifr=0r = 0r=0ors=0s = 0s=0, a newkkkmust be generated and the process repeated
7. The signature is the pair(r,s)(r, s)(r,s)

To verify the signature against the signer's public keyQQQ:

1. Computeu1=m⋅s−1modnu_1 = m \cdot s^{-1} \bmod nu1​=m⋅s−1modnandu2=r⋅s−1modnu_2 = r \cdot s^{-1} \bmod nu2​=r⋅s−1modn
2. Compute the pointR′=u1G+u2QR' = u_1 G + u_2 QR′=u1​G+u2​Q
3. If the x-coordinate ofR′R'R′modulonnnequalsrrr, the signature is valid

The math works out so that only someone who knowsdddcan produce a valid(r,s)(r, s)(r,s)for a given message, but anyone who knows the public keyQQQcan verify it. Adjust the parameters below to see signing and verification with small numbers:

ECDSA sign and verify
G
:
 
(7, 3)
n (order)
:
 
29
Public key Q
:
 
(14, 5)
Signing
1. Pick random k = 
5
2. R = kG = 
(1, 12)
3. r = R.x mod n = 
1
4. s = k⁻¹(m + r·d) mod n = 
16
Signature: 
(r=1, s=16)
Verification
1. u₁ = m·s⁻¹ mod n = 
8
2. u₂ = r·s⁻¹ mod n = 
20
3. R' = u₁G + u₂Q = 
(1, 12)
4. v = R'.x mod n = 
1
v 
==
 r → 
VALID
d=
10
m=
12
k=
5

There are two security requirements: the noncekkkmust never be reused across different messages, andkkkand its inverse must be protected like the private key itself. If an attacker sees two signatures that used the samekkkwith different messages, the two equations leak enough information to compute the private keyddddirectly. In 2010, Sony's PlayStation 3 code signing key was extracted because they used the same nonce for every signature.

## Encrypting with curves

ECDH gives us key agreement and ECDSA gives us signatures. But what about encryption? If Alice wants to send an encrypted message to Bob using his public key, she needs ECIES (Elliptic Curve Integrated Encryption Scheme).

ECIES is a hybrid encryption scheme that combines elliptic curve cryptography with symmetric encryption:

1. Alice generates a randomephemeral keypair: a private keyrrrand public keyR=rGR = rGR=rG
2. Alice computes the shared secret:S=r⋅QBS = r \cdot Q_BS=r⋅QB​(whereQBQ_BQB​is Bob's public key)
3. Alice derives a symmetric key fromSSS(usually from the x-coordinate, often through a key derivation function)
4. Alice encrypts the message using the symmetric key (with AES or similar)
5. Alice sends(R,ciphertext)(R, \text{ciphertext})(R,ciphertext)to Bob (the ephemeral public key and the encrypted message)

Bob decrypts by computing the same shared secret:

1. Bob receives(R,ciphertext)(R, \text{ciphertext})(R,ciphertext)
2. Bob computes the shared secret:S=dB⋅RS = d_B \cdot RS=dB​⋅R(wheredBd_BdB​is his private key)
3. Bob derives the same symmetric key fromSSS
4. Bob decrypts the ciphertext

The math ensures both arrive at the same shared secret becauser⋅QB=r⋅(dBG)=(r⋅dB)G=(dB⋅r)G=dB⋅(rG)=dB⋅Rr \cdot Q_B = r \cdot (d_B G) = (r \cdot d_B) G = (d_B \cdot r) G = d_B \cdot (rG) = d_B \cdot Rr⋅QB​=r⋅(dB​G)=(r⋅dB​)G=(dB​⋅r)G=dB​⋅(rG)=dB​⋅R.

The ephemeral keyrrris generated fresh for every message, which means the same plaintext encrypted twice produces different ciphertexts. An eavesdropper seesRRRand the ciphertext, but computingrrrfromR=rGR = rGR=rGrequires solving the ECDLP.

Try the demo below (using simplifiedXORencryption instead of AES to keep the demonstration clear):

ECIES hybrid encryption
Curve
:
 
y² = x³ + 1x + 6 (mod 23)
G
:
 
(7, 3)
Bob's public key Q_B
:
 
(11, 9)
Message
Encryption (Alice)
1. Random ephemeral r = 
7
2. Ephemeral public R = rG = 
(9, 12)
3. Shared secret S = r·Q_B = 
(14, 18)
4. Symmetric key k = S.x = 
14
5. Ciphertext = encrypt(msg, k)
Send (R, 
46672e4c616c
...
) to Bob
Decryption (Bob)
1. Receive (R, ciphertext)
2. Shared secret S = d_B·R = 
(14, 18)
3. Symmetric key k = S.x = 
14
4. Plaintext = decrypt(ciphertext, k)
Decrypted: 
"
Hi Bob
"
Bob d_B = 
11
Alice r = 
7

ECIES lets you encrypt a message directly to someone's public key without a prior key exchange. Full ECIES specifications also include a key derivation function (KDF) and a MAC or AEAD scheme for integrity. Ethereum's devp2p/RLPx protocol uses ECIES during the handshake to establish shared session keys; the ongoing transport then uses symmetric encryption. Signal Protocol uses a variant called the X3DH key agreement protocol that builds on similar elliptic curve principles.

## Why curves win

The practical advantage of elliptic curve cryptography comes down to key size. For the same level of security, ECC keys are much smaller than RSA or Diffie-Hellman keys:

Security level
ECC key
RSA key
DH key
80 bits
160 bits
1,024 bits
1,024 bits
112 bits
224 bits
2,048 bits
2,048 bits
128 bits
256 bits
3,072 bits
3,072 bits
192 bits
384 bits
7,680 bits
7,680 bits
256 bits
512+ bits (e.g., P-521)
15,360 bits
15,360 bits

"Security level" means the number of operations an attacker would need to break the system. At 128-bit security (the standard for most applications today, meaning an attacker would need21282^{128}2128operations), an ECC key is 256 bits while an RSA key is 3,072 bits. That's a 12x difference. At higher security levels the gap grows: 256-bit security needs 512+-bit ECC keys (e.g., P-521) versus 15,360-bit RSA keys.

Smaller keys are faster to compute and cheaper to transmit, which matters especially on constrained devices like smart cards. This is why TLS 1.3, Signal, SSH, and Bitcoin all use ECC.

TLS 1.3dropped static RSA key transport and uses only ephemeral (EC)DHE forforward secrecy. Signal and WhatsApp use Curve25519 for all key agreement. SSH supports ECDSA and Ed25519 keys. Bitcoin and Ethereum both use secp256k1, though Bitcoin now uses Schnorr signatures (BIP340) for Taproot outputs alongside ECDSA for legacy and SegWit transactions.

The two most common curves are NIST P-256 (from FIPS 186-2, published in 2000) and Curve25519 (designed by Daniel Bernstein in 2006). X25519, the Diffie-Hellman function on Curve25519, was designed to resist implementation mistakes: it accepts any 32 bytes of secret material and deterministically clamps the bits into a valid scalar, so there are fewer ways to mishandle keys.

Elliptic curves give us key exchange and digital signatures with keys that fit comfortably in a text message. There is a caveat, though. All public-key cryptography, including ECC, is theoretically vulnerable to quantum computing: an algorithm called Shor's algorithm can solve the ECDLP efficiently on a sufficiently powerful quantum computer. No such computer exists yet, but the threat has motivated work on post-quantum cryptography, which uses different mathematical structures (lattices, error-correcting codes, hash trees) that quantum computers can't efficiently break.