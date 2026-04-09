---
title: Fully Homomorphic Encryption and the Dawn of A Truly Private Internet
url: https://bozmen.io/fhe
site_name: hackernews_api
fetched_at: '2025-07-18T23:07:22.064398'
original_url: https://bozmen.io/fhe
author: Barış Özmen
date: '2025-07-18'
description: Barış Özmen Blog
tags:
- hackernews
- trending
---

# Fully Homomorphic Encryption and the Dawn of A Truly Private Internet

2025-07-16fheprogrammingessay

This article is archived atmirror.xyz

gene-spafford"Using encryption on the Internet is the equivalent of arranging an armored car to deliver credit card information from someone living in a cardboard box to someone living on a park bench." -- Gene Spafford

Imagine sending Google an encrypted question and getting back the exact results you wanted — without them having any way of knowing what your question was or what result they returned. The technique to do that is calledFully Homomorphic Encryption (FHE).

The first time I heard about what FHE does, I didn't believe it was possible. But it is — an it works inreal-world systemstoday.

It allows arbitrary computations on ciphertext (encrypted data) — without needing to decrypt it first. The result of the computation, once decrypted, matches the result as if it had been performed on plaintext (unencrypted data).

* From Craig Gentry'sslides

### Moore's Law of FHE

As FHE allows encrypted computation, users can keep their data encrypted all the time on the internet (sending, server computing, receiving back). This prevents any chance of data breach. Full Privacy.

But then, why isn't it the default like HTTPS? Why isn't everyone using it? And why haven't most people even heard of?

Because it is still not practical for most applications, as it is very slow. Butthis is changing fastas I'll explain below.

Current FHE has 1,000x to 10,000x computational overhead compared to plaintext operations. On the storage side, ciphertexts can be40 to 1,000 times largerthan the original. It's like the internet in 1990—technically awesome, but limited in practice.

Here's where it gets interesting:FHE algorithms are getting 8x faster each year.Operations that took 30 minutes per bit in 2011 now take milliseconds. See the graph below showing its dramatic speed improvement.

ref

The graph shows 10^12 times improvement until 2014. The pace of improvement continued over the last decade too. I will go deeper on that later in this article.

### The Inflection Point

If this dramatic improvement continues, we're approaching a computational inflection point. In not too distant future, FHE could be fast enough for:

* Encrypted cloud computing
* Encrypted LLM inference
* Confidential blockchain smart contracts

The implications are big. The entire business model built on harvesting user data could become obsolete. Why send your plaintext when another service can compute on your ciphertext?

Internet's "Spy by default" can become "Privacy by default".

ref

### Dive Deeper

Below sections go deeper into each aspect of the claim of this article. You can jump into any if you are particularly curious about those sections. You can also read them in order, as they are in a logical sequence:

* The problem:Achilles' Heel of Security
* The solution:Defining Full-Privacy Computing
* Technical Deep dive:How FHE Actually Works
* More on performance improvements:The Moore's Law of FHE: 8x Faster Every Year
* Connecting the dots:Future of computation is encrypted

## Achilles' Heel of Security

All data exists in one of three states:

1. At Rest(stored on disk)
2. In Transit(moving over a network)
3. In Use(being processed in memory)

We have robust solutions for the first two:

* At Rest:Disk encryption, file system encryption.
* In Transit:TLS/SSL, VPNs, end-to-end encryption.

Butin use—when data is loaded into RAM and processed by CPUs—it is decrypted. This is the Achilles’ heel of modern security. Cloud providers, insiders, attackers, or compromised CPUs can read your plaintext data.

Think about every major data breach you've heard of:

* The2014 celebrity photo leak(Apple iCloud)
* The23andMe genetic data theft
* TheCapital One hack

They were failures of encryption-in-use or at rest. The moment data gets loaded into memory for processing, it becomes vulnerable.

FHE fixes this. Data can stay encrypted through its entire lifecycle on the cloud, which we can call "Full-Privacy Computing".

## Defining Full-Privacy Computing

Picture an internet where your data is always encrypted:

* Encrypted at rest
* Encrypted in transit
* Encrypted in use

This means:

* Your device never sends plaintext to any server
* Servers process only encrypted data
* Only you can decrypt the results

Here's what a private ChatGPT session might look like:

# Your device
pk, sk = keygen() # pk: public key, sk: secret (private) key
enc_prompt = encrypt("Why did the dev go to therapy?", pk)
server.send(enc_prompt, pk)

# OpenAI's servers (they can never decrypt and see your prompt)
enc_prompt, pk = client.receive()
enc_llm = encrypt(LLM_MODEL, pk)
enc_answer = enc_llm.run(enc_prompt)
client.send(enc_answer)

# Your device again
enc_answer = server.receive()
answer = decrypt(enc_answer, sk)
print(answer)
"""Because of too many unresolved dependencies!"""

OpenAI computes the correct response, but can never see your question or their answer in plaintext.

Privacy as a computational invariant.

## How FHE Works

The term "homomorphic" comes from Greek: "homo" (same) + "morphe" (form). It means having a structure-preserving map between two algebraic structures. FHE ishomomorphicbecause operations on encrypted data can be mapped (i.e. mirrored) onto those on the original data.

The homomorphism incategory theoryis often shown by a commutative diagram, where you can go from a point to another by interchanging the order of operations. In the below diagram for FHE, you can go from (a, b) to E(a*b) in two separate ways.

ref

Let's look at an equivalent diagram with client/server perspective andf(x)function.

ref

One helpful analogy to FHE is theFourier transform, which converts a signal from the time domain into the frequency domain. Computations performed on the frequency domain are equivalent to those in the time domain and vice versa. Meaning that you can compute in either domain and still get the same result. In a similar way, FHE operates between plaintext and ciphertext domains. Transformations done in plaintext domain are equivalent to those in the ciphertext domain, and vice versa.

bidirectional transformation

Fourier Transform

time domain <--> frequency domain

FHE

plaintext domain <--> ciphertext domain

### The Lattice-Based Cryptography

To do the above mentioned transformation, FHE useslattice-based cryptography—imagine a multidimensional grid of points extending infinitely in all directions.

* [ref](lattice-based cryptography)

At the heart of lattice-based cryptography are problems that are believed to be extremely hard to solve—even for quantum computers. Two of the most well-known examples are1::

* Shortest Vector Problem (SVP):Find the shortest path between lattice points
* Closest Vector Problem (CVP):Find the lattice point nearest to any given point

In 2D, these look trivial. But add 1,000,000 dimensions? Then it becomes extremely hard, so that it is believed thateven quantum computers can't crack them efficiently. This makes FHE inherently quantum-resistant. A very important property to prepare for the possible quantum computing future.

Bonus: Lattice operations are highly parallelizable, which means they benefit enormously from modern GPUs and specialized hardware acceleration.

#### Learning With Errors (LWE)

Lattice-based FHE schemes rely on theLearning With Errors (LWE)orRing-LWE problem. At a high level, LWE looks like this:

A-> a known matrix

s-> secret key

e-> random small noise

Calculateb = A*s + e(i.e.bis a noisy linear combination)

Generate public key =(A, b)

The hard problem:Given the public key(A, b), find the secret keys

ref

Notice thatA*sis linear, so visually forms a lattice. In other words,A*sis on a lattice point. The addition of noiseemakes the resultingA*s + e = bdrifting from the lattice point (Note that the noise is sampled from a narrow random distribution so thatbdoesn't drift too much from the lattice point so that it is closer to another lattice point).

So the problem becomes that: If an attacker wants to find secret keysfrom the public key(A, b), he needs to solve the problem of finding the closest lattice point = closest vector problem (CVP). And closest vector problem is believed to be NP-hard and evenquantum-resistant.

To sum up, encryption works because of noise. And encryption remains secure because decoding a lattice point with noise is hard.

#### Noise management & Bootstrapping

While the noise is the trick here, it also causes the following problem during addition and multiplication operations. During homomorphic addition, the noises of each ciphertext is also added to each other, while during multiplications they are multiplied. This results in:

* Addition --> noise grows linearly (manageable)
* Multiplication --> noise grows multiplicatively (un-manageable)

If the noise gets too big, decryption fails — you get garbage instead of the result.

Since noise growth unmanageable with multiplication, the noise-based HE schemes beforeCraig Gentry 2009allowed only a limited number of multiplications (hence not Turing-complete). For that reason, they were calledSomewhat Homomorphic Encryption.

Craig Gentryinvented in 2009the first HE scheme that allows infinite number of additions and multiplications combined. Hence it isTuring Complete. Hence it is called Fully Homomorphic Encryption. Note that any kind of computation can be represented as additions and multiplications. Indeed, all computations are reduced to additions and multiplications on the CPU/GPU level.

The main piece that makes FHE work was the method called "bootstrapping". Bootstrapping reduces the noise whenever it gets too big. In that way, it guarantees that noise doesn't disrupt decryption, no matter how many multiplications are performed.

The way how bootstrapping work is very clever. It's probably called "bootstrapping", because it "refreshes" the cipher text under another public key. It cleverly switches the ciphertext from one public key to another, as follows:

1. Take the original public keypk_orig
2. Take the ciphertextctxwhich was originally encrypted underpk_orig
3. Generate a whole new key pairpk_new,sk_new
4. Encryptpk_origunderpk_new, obtainingpk_bootstrap(Yes! Encrypt the key with another key. Creative!)
5. Encrypt the ciphertextctxunderpk_new, obtainingctx_new
6. Run (homomorphically) the decrypt operation onctx_newwithsk_new, obtainingctx_bootstrap

Notice that, the decryption procedure of FHE is itself a computation. So it can be used for homomorphic computations too!

The newctx_bootstrapis another new ciphertext, whose noise is reset. Note that, it gained some fixed noise as it went through additions and multiplications during the decryption computation. But this noise is bounded.

Another thing to keep in mind is, bootstrapping is the performance bottleneck of modern FHE schemes. Though its computational overhead gets better every year by new algorithms.

* From Craig Gentry'sslides

There are many more details to that. I listed some resources going through atFHE Bootstrapping, though they also don't cover everything. One needs to read throughFHE Reference Library. Other topics around bootstrapping are quite complicated, and as far as I understood, it is the focal point of FHE algorithmic innovations. It's really important to understand it conceptually at least, because it's the root of FHE slowness, while also the reason why FHE works.

Other topics around FHE you need to be aware arerelinearizationandmodulus switching.I'll explain them only by intuition here. For deeper math, I suggestVitalik's postas a starter.

#### Relinearization

A ciphertext is linear in the secret key ->a + b​⋅s

After multiplication, the result become quadratic in secret key. To show that:

Let's multiply below ciphertexts:

* ct1 = (a1, b1), whose decrypted form isa1 + b1*s
* ct2 = (a2, b2), whose decrypted form isa2 + b2*s

After multiplication:

* ct_mul = (a₁a₂, a₁b₂ + a₂b₁, b₁b₂), whose decrypted form isa₁a₂ + (a₁b₂ + a₂b₁)·s + b₁b₂·s²
* Notice thes²term, which makesct_mulquadratic in the secret key.

Relinearization uses additional public key material called "relinearization keys" to eliminate the higher-degree terms. The process:

1. Takes the quadratic termb₁b₂·s²
2. Uses relinearization keys to "convert" this back into linear terms
3. Produces a new linear ciphertext(c₀', c₁')that decrypts to the same value

#### Modulus Switching

It's used to manage noise growth. It's a trick to reduce the noise by decreasing the modulus of the ciphertext.

I did couple of conversations with ChatGPT to understand some mathematical details of FHE better, and wrote down what I learned from themhere.

### Classification of HE Schemes

What do we mean by a Homomorphic Encryption (HE) Scheme?

A HE scheme is a cryptographic construction that defines how encryption, decryption, and homomorphic operations are performed (e.g. BGV, CKKS, TFHE).

Homomorphic Encryption schemes are classified by the types and number of operations they support.

Partial Homomorphic Encryption

Supports only one operation (e.g., addition in Paillier, multiplication in RSA).

(I will build a toy Pailler example below, whose code is short and intuitive)

Somewhat Homomorphic Encryption

Supports both addition and multiplication, but number of multiplications allowed is limited.

(I explained in previous section how noise growth limits number of multiplications possible)

Fully Homomorphic Encryption

Supports unlimited additions and multiplications. Turing Complete. Manages noise by periodically reducing via bootstrapping.

### A toy example

One of the best ways to really understand a computational concept isbuilding it from scratch,minimally.

For the purposes of this blog post, creating a Fully Homomorphic Encryption scheme would be very lengthy. Instead, we will writePaillier HE, which is shorter and easier to understand for getting an intuition. Paillier is a Partial HE, meaning that it doesn't support all operations (hence not Fully HE). It only supports additions (hence additive homomorphism). We'll follow a typical HE flow:

1. Key Generation(public-key + private-key)
2. Encryptionof data (using public-key)
3. Computation(homomorphic operations)
4. Decryptionof result (using private-key)

fhe-toy-implementations## Partial HE (Paillier) - additive homomorphismimport sympy, random

def generate_keypair(bit_length=512):
 p = sympy.nextprime(random.getrandbits(bit_length))
 q = sympy.nextprime(random.getrandbits(bit_length))
 n = p * q
 g = n + 1
 lambda_ = (p - 1) * (q - 1)
 mu = sympy.mod_inverse(lambda_, n)
 return (n, g), (lambda_, mu)

def encrypt(m, public_key):
 n, g = public_key
 r = random.randint(1, n - 1)
 return (pow(g, m, n**2) * pow(r, n, n**2)) % (n**2)

def decrypt(c, private_key, public_key):
 lambda_, mu = private_key
 n, _ = public_key
 l = (pow(c, lambda_, n**2) - 1) // n
 return (l * mu) % n

def homomorphic_sum(a, b, public_key):
 return (a * b) % (public_key[0]**2)

public_key, private_key = generate_keypair(128)

enc1 = encrypt(5, public_key)
print(enc1) # 75042696080311881003721105285833023546234037256871189406054603593273414107194675808782154359890875636008219678257354647151456750847402457204123856890

enc2 = encrypt(3, public_key)
print(enc2) # 269297253929306291153284608946414491483346738328838888044406160105950588673820650688249910373352597049965491330298818622410901670587359945691000319758

enc_sum = homomorphic_sum(enc1, enc2, public_key)
print(enc_sum) # 232817745404365921249916946617154013580946738803385878188677616867767489473531493655408124901849935882016399498283109322848069064027287561237823608127

dec_sum = decrypt(enc_sum, private_key, public_key)
print(dec_sum) # 8Here is thecolab notebook linkfor you to run and play with yourself.I highly recommend. It will give valuable intuitionNote that ciphertexts will be different at each run, as encryption process is non-deterministic (notice therandommethods). Above commented print outputs are from a single run, for showing how a ciphertext looks like under Paillier.

If we were to build a Fully HE, it could use a similar API withgenerate_keypair,encrypt,decrypt, andhomomorphic_sumwith an addition ofhomomorphic_multiply. But the code would be much longer. For such a code, see Vitalik'shomomorphic_encryption.pyandmatrix_fhe.py. Also readhis awesome deep dive.

Further reading:

* FHE time complexity
* Exploring Fully Homomorphic Encryption by Vitalik
* Build from scratchFHE toy implementationsSee Bit-wise FHE section ofFHE toy implementations#Bit-wise Fully Homomorphic EncryptionBuilding Safe AI - A Tutorial for Encrypted Deep Learning - i am traskFully Homomorphic Encryption from Scratch - daniellowebgrubHN - Explained from scratch private information retrieval and homomorphic encryption (blintzbase.com)TFHE toy implementation
* FHE toy implementationsSee Bit-wise FHE section ofFHE toy implementations#Bit-wise Fully Homomorphic Encryption
* See Bit-wise FHE section ofFHE toy implementations#Bit-wise Fully Homomorphic Encryption
* Building Safe AI - A Tutorial for Encrypted Deep Learning - i am trask
* Fully Homomorphic Encryption from Scratch - daniellowebgrub
* HN - Explained from scratch private information retrieval and homomorphic encryption (blintzbase.com)
* TFHE toy implementation
* From the pioneers:Craig Gentry (FHE inventor)2025, April.FHE inside out2024, June.FHE past, present, future2021, Oct.A decade (or so) of FHEJung-hee Cheon (CKKS inventor)2019, March.HE and blockchain
* Craig Gentry (FHE inventor)2025, April.FHE inside out2024, June.FHE past, present, future2021, Oct.A decade (or so) of FHE
* 2025, April.FHE inside out
* 2024, June.FHE past, present, future
* 2021, Oct.A decade (or so) of FHE
* Jung-hee Cheon (CKKS inventor)2019, March.HE and blockchain
* 2019, March.HE and blockchain

## The Moore's Law of FHE: 8x Faster Every Year

ref

The Four Generations:

* 1978 (Pre-history):Rivest, Adleman, Dertouzos envisioned FHE by the name "privacy homomorphisms"
* 2009 (Gen 1):Gentry's 2009 PhD thesis constructing the first ever FHE scheme
* 2011 (Gen 1):First implementation of FHE–bootstrapping took 30 minutes per bit2
* 2011-2012 (Gen 2):BGV/BFV schemes, lattice-based, still slow.
* 2013+ (Gen 3):Faster bootstrapping in milliseconds.
* 2017 (Gen 4):CKKS for approximate floats, enabling ML/AI.

For more, seeFHE History.

Since 2011, FHE performance has improved 8× every year—from 10¹⁰× overhead down to ~10³× ~10^4× today.

* From Craig Gentry'sslides

Recent breakthroughs are accelerating the timeline:

* A June 2025paperby Dan Boneh & Jaehyung Kim claims 1,000× higher multiplication throughput and 10× lower latency (for large-integer ops)
* Hardware acceleration could add another10³× speedup

Alongside with algorithm improvements, hardware improvements are also happening, compounding the effect. More on that inFHE Hardware

Here is Vitalik's thoughts on pace of progress:

exploring-fully-homomorphic-encryption-by-vitalik--archivedWe are quickly getting to the point where many of the applications of homomorphic encryption in privacy-preserving computation are starting to become practical. Additionally, research in the more advanced applications of the lattice-based cryptography used in homomorphic encryption is rapidly progressing. So this is a space where some things can already be done today, but we can hopefully look forward to much more becoming possible over the next decade.

## Future of computation is encrypted

Let's connect the dots.

Data breaches are almost unavoidable.

The only way to protect data is to keep it always encrypted on servers, without the servers having the ability to decrypt.

This means data should be encrypted even when computations are performed on it.

FHE enables computation on encrypted data.

FHE is not practical yet for many applications because of its high computational overhead. But it's practical for some.

FHE algorithms are getting better each year, by 8x per year. The result is that feasible real-world applications are on the increase. FHE is eating computation, but it is still small.

If the trend continues, FHE will conquer many more real-world use cases to the point that most cloud computations can be done with FHE.

Privacy awareness of users is increasing. Privacy regulations are increasing.

If FHE is a possible option, people and institutions will demand it.

If people are demanding it, and the trends have made FHE practical for most computations, then most internet computations will be on FHE.

The future of internet computations will be encrypted. It is not if, it is when.

HTTPS by default --> 2010s
FHE by default --> ?

## Key References

Key Papers & Resources:

* FHE Reference Library- Comprehensive academic papers
* Craig Gentry's 2009 PhD Thesis- The foundational work

From the Pioneers:

* Craig Gentry:FHE inside out,FHE past, present, future,A decade (or so) of FHE
* Jung-hee Cheon (CKKS inventor):HE and blockchain
* Pascal Paillier:Introduction to FHE
* Daniele Micciancio:Fully Homomorphic Encryption from the Ground Up

Good reads:

* Vitalik Buterin:Exploring FHE

Improvements:

* Fully Homomorphic Encryption Just Became Practical

Implementation Examples:

* FHE for Genomics
* Encrypted Sentiment Analysis
* Encrypted Deep Learning
* Private Wikipedia
* More Production Examples

Community:

* FHE.org- The central hub for FHE development

Other:

* https://github.com/jonaschn/awesome-he

1. Cryptographic systems rely onhard problems—those with no known polynomial-time solutions (NP-hard). To be useful, these problems must be easy to compute in one direction but hard to reverse. Such problems are calledone-way functions, and all cryptography depends on them. A classic example ismultiplying large primes—easy forward, hard to factor back.↩
2. The inefficiency caused by overhead of bootstrapping, which is part of computation on encrypted data. 30 minutes per bit in bootstrapping. https://x.com/i/grok/share/jhND3efXK7or24rdkFgcxpbZz↩

											Incoming Internal References (0)


											Outgoing Internal References (13)


1. ![[Gene Spafford#^05f1d8]]Imagine sending Google an encrypted question and getting back the exact results you wanted — without them having any way of knowing what your question was or what result they returned. The technique to do that is called **Fully Homomorphic Encryption (FHE)**.
2. The first time I heard about what FHE does, I didn't believe it was possible. But it is — an it works in[[FHE Real-world Applications|real-world systems]]today.
3. There are many more details to that. I listed some resources going through at[[FHE Bootstrapping|FHE Bootstrapping]], though they also don't cover everything. One needs to read through [FHE Reference Library](https://people.csail.mit.edu/vinodv/FHE/FHE-refs.html). Other topics around bootstrapping are quite complicated, and as far as I understood, it is the focal point of FHE algorithmic innovations. It's really important to understand it conceptually at least, because it's the root of FHE slowness, while also the reason why FHE works.
4. I did couple of conversations with ChatGPT to understand some mathematical details of FHE better, and wrote down what I learned from them[[FHE math chatgpt discussions|here]].### Classification of HE Schemes
5. ### A toy exampleOne of the best ways to really understand a computational concept is[[Build from scratch|building it from scratch]], [[Minimalism|minimally]].
6. ### A toy exampleOne of the best ways to really understand a computational concept is [[Build from scratch|building it from scratch]],[[Minimalism|minimally]].
7. ![[FHE toy implementations#Partial HE (Paillier) - additive homomorphism]]
8. Further reading:-[[FHE time complexity]]- [Exploring Fully Homomorphic Encryption by Vitalik](https://vitalik.eth.limo/general/2020/07/20/homomorphic.html)
9. - Build from scratch-[[FHE toy implementations]]- See Bit-wise FHE section of [[FHE toy implementations#Bit-wise Fully Homomorphic Encryption]]
10. - [[FHE toy implementations]]- See Bit-wise FHE section of[[FHE toy implementations#Bit-wise Fully Homomorphic Encryption]]- [Building Safe AI - A Tutorial for Encrypted Deep Learning - i am trask](https://iamtrask.github.io/2017/03/17/safe-ai/)
11. For more, see[[FHE History]].
12. Alongside with algorithm improvements, hardware improvements are also happening, compounding the effect. More on that in[[FHE Hardware]]
13. Here is Vitalik's thoughts on pace of progress:![[Exploring Fully Homomorphic Encryption by Vitalik (archived)#^end]]## Future of computation is encrypted

											Outgoing Web References (59)


1. mirror.xyz/0x7a8dEd001067D6f98296df0E9dA2aEE6d75B9494/zwAyC5midnsbwXN-yMg0ykVkJar-OR3zwz2w8xQoMbM* mirror.xyz
2. eurocrypt.iacr.org/2021/slides/gentry.pdf* slides
3. youtu.be/PfSZL9LsMCg* 40 to 1,000 times larger
4. youtu.be/487AjvFW1lk?t=668* ref
5. x.com/VitalikButerin/status/1248704356758753281* ref
6. en.wikipedia.org/wiki/2014_celebrity_nude_photo_leak* 2014 celebrity photo leak
7. echcrunch.com/2023/12/04/23andme-confirms-hackers-stole-ancestry-data-on-6-9-million-users* 23andMe genetic data theft
8. en.wikipedia.org/wiki/Capital_One#July_2019_security_breach* Capital One hack
9. en.wikipedia.org/wiki/Homomorphism* homomorphic
10. en.wikipedia.org/wiki/Category_theory* category theory
11. vitalik.eth.limo/general/2020/07/20/homomorphic.html* ref
12. en.wikipedia.org/wiki/Fourier_transform* Fourier transform
13. www.esat.kuleuven.be/cosic/blog/introduction-to-lattices* lattice-based cryptography
14. www.zama.ai/post/fully-homomorphic-encryption-and-post-quantum-cryptography* ref]([lattice-based cryptography
15. en.wikipedia.org/wiki/Post-quantum_cryptography#Lattice-based_cryptography* even quantum computers can't crack them efficiently
16. en.wikipedia.org/wiki/Learning_with_errors* Learning With Errors (LWE)
17. en.wikipedia.org/wiki/Ring_learning_with_errors* Ring-LWE problem
18. blintzbase.com/posts/pir-and-fhe-from-scratch* ref
19. en.wikipedia.org/wiki/Post-quantum_cryptography#Lattice-based_cryptography* quantum-resistant
20. www.cs.cmu.edu/~odonnell/hits09/gentry-homomorphic-encryption.pdf* Craig Gentry 2009
21. digitalprivacy.ieee.org/publications/topics/types-of-homomorphic-encryption* Somewhat Homomorphic Encryption
22. www.cs.cmu.edu/~odonnell/hits09/gentry-homomorphic-encryption.pdf* invented in 2009
23. en.wikipedia.org/wiki/Turing_completeness* Turing Complete
24. eople.csail.mit.edu/vinodv/FHE/FHE-refs.html* [FHE Bootstrapping|FHE Bootstrapping]], though they also don't cover everything. One needs to read through [FHE Reference Library
25. vitalik.eth.limo/general/2020/07/20/homomorphic.html* Vitalik's post
26. en.wikipedia.org/wiki/Paillier_cryptosystem* Paillier HE
27. github.com/vbuterin/research/blob/master/tensor_fhe/homomorphic_encryption.py* homomorphic_encryption.py
28. github.com/vbuterin/research/blob/master/matrix_fhe/matrix_fhe.py* matrix_fhe.py
29. vitalik.eth.limo/general/2020/07/20/homomorphic.html* his awesome deep dive
30. vitalik.eth.limo/general/2020/07/20/homomorphic.html* Exploring Fully Homomorphic Encryption by Vitalik
31. iamtrask.github.io/2017/03/17/safe-ai* Building Safe AI - A Tutorial for Encrypted Deep Learning - i am trask
32. www.daniellowengrub.com/blog/2024/01/03/fully-homomorphic-encryption#lwe-to-rlwe-keys* Fully Homomorphic Encryption from Scratch - daniellowebgrub
33. news.ycombinator.com/item?id=32987155* HN - Explained from scratch private information retrieval and homomorphic encryption (blintzbase.com)
34. github.com/barisozmen/tfhe* TFHE toy implementation
35. www.youtube.com/watch?v=V3FcM1B4mcg&list=PLnbmMskCVh1cCnWbmgxI0BM0UD2JHH9fz&index=14* FHE inside out
36. www.youtube.com/watch?v=184NHhE3Kq0* FHE past, present, future
37. www.youtube.com/watch?v=487AjvFW1lk* A decade (or so) of FHE
38. medium.com/hashed-official/homomorphic-blockchain-1f7db66ac2f7* HE and blockchain
39. www.zama.ai/post/homomorphic-encryption-101* ref
40. eprint.iacr.org/2025/346.pdf* paper
41. www.youtube.com/watch?v=V3FcM1B4mcg&list=PLnbmMskCVh1cCnWbmgxI0BM0UD2JHH9fz&index=14* 10³× speedup
42. eople.csail.mit.edu/vinodv/FHE/FHE-refs.html* FHE Reference Library
43. crypto.stanford.edu/craig/craig-thesis.pdf* Craig Gentry's 2009 PhD Thesis
44. www.youtube.com/watch?v=V3FcM1B4mcg&list=PLnbmMskCVh1cCnWbmgxI0BM0UD2JHH9fz&index=14* FHE inside out
45. www.youtube.com/watch?v=184NHhE3Kq0* FHE past, present, future
46. www.youtube.com/watch?v=487AjvFW1lk* A decade (or so) of FHE
47. medium.com/hashed-official/homomorphic-blockchain-1f7db66ac2f7* HE and blockchain
48. www.youtube.com/watch?v=aruz58RarVA&t=3082s* Introduction to FHE
49. www.youtube.com/watch?v=TySXpV86958* Fully Homomorphic Encryption from the Ground Up
50. vitalik.eth.limo/general/2020/07/20/homomorphic.html* Exploring FHE
51. bowtieditaliano.substack.com/p/fully-homomorphic-encryption-just* Fully Homomorphic Encryption Just Became Practical
52. github.com/barisozmen/securegenomics* FHE for Genomics
53. uggingface.co/spaces/zama-fhe/encrypted_sentiment_analysis* Encrypted Sentiment Analysis
54. iamtrask.github.io/2017/03/17/safe-ai* Encrypted Deep Learning
55. iralwiki.com* Private Wikipedia
56. www.jeremykun.com/fhe-in-production* More Production Examples
57. fhe.org* FHE.org
58. www.lesswrong.com/posts/PxMSnEPFG34o9zkq4/what-is-cryptographically-possible* ^1]: Cryptographic systems rely on _hard problems_—those with no known polynomial-time solutions (NP-hard). To be useful, these problems must be easy to compute in one direction but hard to reverse. Such problems are called [one-way functions
59. en.wikipedia.org/wiki/One-way_function#Multiplication_and_factoring* multiplying large primes
