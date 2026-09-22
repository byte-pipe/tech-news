---
title: Adversarial examples for fast hash functions
url: https://thomasahle.com/blog/adversarial-examples-for-hashes
site_name: tldr
content_file: tldr-adversarial-examples-for-fast-hash-functions
fetched_at: '2026-09-22T15:26:03.394526'
original_url: https://thomasahle.com/blog/adversarial-examples-for-hashes
author: Thomas Dybdahl Ahle
date: '2026-09-22'
description: How often do chosen inputs collide? Reproducible examples, machine-checked collision bounds, and the speed of fast hash functions.
tags:
- tldr
---

Contents

Hash functionsmap data of arbitrary length to fixed-size values. The goal is to ensure thatdistinct inputsmap todistinct outputs, except with very small probability over the randomness of asecret keyused by the hash function.This propertyensures we can build fast hash tables where every data point doesn’tcollidein the same bucket.1

Hashing needs to be fast.xxHashboasts 60 GB/s, or basically as fast as you can read memory. Such bulk hashing is useful for file synchronisation or data integrity checking. Many popular hashes likekomihash, a5hash, HighwayHash, SpookyHash, aHash, andt1ha2are willing to trade quality, at least for adversarial inputs, for more speed.

This used to be fine. Many use cases of hashes are low risk, and it’s not worth it for attackers to do expensive cryptanalysis for inputs that make the hashes collide much more often than average. Still, most hashes try to besomewhatrobust, to prevent accidentally quadratic slowdowns in algorithms and DoS attacks.

The best hashes giveproofsthatanypair of inputs collide with low probability.This is something unique in a world of cryptography that nobody can prove is actually secure. Let’s say a hash isb-bit universal if inputs of lengthLcollide with probability at mostL · 2−bfor allL. Sometimes the dependency onLis worse, but it’s (provably) never better.2The question becomes: What is the fastest possible hash that’sb-bit universal for some desiredb?

I was able to use Claude Fable to analyse a broad selection of popular hashes fromSMhasher—a large project to empirically test statistical properties of hashes. It found that most of them have inputs on which they perform terribly—at least 20 bits below expectation. A few hashes have published proofs, and Fable was able to find mistakes in some and verify others in Lean. Click on any dot in the chart to read the full analysis.

Apple M2 Pro

Intel Xeon

Y-axis 
Linear
Square root (√y)
Quadratic (y²)
Logarithmic

Collision score bounds versus bulk speed. Speed is logarithmic. Score uses square-root spacing to give low scores more room; tick labels show the original bit values. Solid teal circles are proved lower guarantees; hollow circles are unresolved claims. Rust diamonds are witness upper caps; crosses mark every-seed pairs. Labels identify selected landmarks; every plotted variant is available in the hash selector.

Tab to a point and use arrow keys, Home or End to move between points. Enter or Space opens its profile. Escape closes it. Tap a point or its label on touch screens.

Inspect a hash
Choose a hash…

Select a hash, or tap a point or label.

×

Collision score
Bulk speed
Output width

#### Background

#### What this result means

How this was checked, and where it applies
How the key is chosen
What is covered
Benchmark host

Article discussion
Implementation studied
Benchmark record

Figure 1.Fast implementations can have very different collision guarantees. Solid dots show what a proof guarantees; rust marks show limits exposed by specific pairs. The guarantee and the speed measurement may use different key setups—open a profile for those assumptions.

Full data table·Data and provenance·Timing reproduction·Hash profiles

How to read the bounds and benchmarks

On the speed axis, equal distances represent equal ratios: moving from 1 to 2 bytes per cycle takes the same space as moving from 10 to 20. The vertical axis uses square-root spacing to give low collision scores more room. Zero stays visible, and all tick labels and profile values show the original scores in bits. The score is itself logarithmic in the collision bound; seeits definition.

Solid teal circles give proved minimum scores. Hollow circles show unproved claims. Rust diamonds cap the score using a specific pair of distinct messages that collide; crosses identify pairs that collide for every seed. An asterisk means the cap uses a sampled rate. Finding no worse pair does not prove that none exists, so these caps are not a ranking of safety. A cross can sit above zero because the score adjusts for message length. All plotted variants are available in the selector, including the four HalftimeHash styles, which each return 64 bits.

The separate historical32-byte pair Agave 9, 12, 11 and 11 collisions per 230keys in wyhash, rapidhash v1, rapidhash v3 and XXH3-64. The selected XXH3-64 pair has a different measured rate: about 527 of every 2^36 keys (sampled; 527 events, pooled). Search effort was unequal; these witness caps do not rank hashes.Current pair and count provenance.

Speed is measured on 256 KiB messages, regardless of the length of the colliding pair. “B/cycle” means bytes processed per reported timer cycle; larger is faster. The M2 and Xeon timers use different cycle conventions, so compare hashes on the same host. The separate short-input measurements use 1–31 bytes. Foldhash uses a verified port with control measurements. GHASH is timed through OpenSSL’s GMAC interface, including setup costs. The benchmark protocol records the timers, repeated runs and calibration details.

Both published UMASH headline bounds are now proved by different routes: the implemented mod-8p accumulator and the C fingerprint’s two independent multipliers. The solid points show 56.18 and 83.99 bits (about 84 on L ≤ 246words), for ideal full keys, a fixed seed and full C outputs. Key derivation, per-call seeds and masked outputs are outside these theorems; the paper’s 162/q projection step remains unvalidated. The four 64-bit HalftimeHash styles have a corrected 63-bit bound under the stated execution assumptions and length limits. The original advanced 24-byte function was refuted; its repaired version is plotted separately. ChainHash is one 64-bit function on both hosts: 28.31 B/cycle on Xeon and 26.26 on M2, with a machine-checked 63.0-bit guarantee from 64 uniformly random key bytes. ChainHash-128 is the 128-bit function, again one function on both hosts: 14.43 B/cycle on Xeon and 10.26 on M2, with a machine-checked 127-bit guarantee from 128 random key bytes. SipHash-1-3 and SipHash-2-4 are plotted as unresolved claims at their 64-bit output width. This audit supplies neither a proof nor a counterexample for these SipHash bounds. The cited 2014 analysis reports collision characteristics of 2-167for SipHash-1-x and 2-236.3for SipHash-2-4 (Dobraunig, Mendel and Schläffer, 2014), and our own search sees nothing above 2-26.4per pair. Some historical collision examples have no matching timing, so they are absent from the chart. See theproof notesfor the distinctions.

The main takeaways:

1. AI changes the threat model: Software that used to be secure mostly from obscurity is now easy to break. If you can get provably correct software, take it.
2. Provable hashes are just as fast as heuristic hashes. Our own hash, ChainHash, built on my work with Jakob Tejs onFast Polynomial Evaluation, had the highest throughput among all the hashes on Intel Xeon, second highest on Apple M2 Pro.
3. Proofs of correctness are good, but verified Lean proofs are better. Not everything published is audited equally well, and we found multiple gaps, some of which could be fixed, and others that required code changes.

All the findings were disclosed upstream to maintainers before the publication of this blog post.
You can read the maintainers’ replies in the discussions forxxHash,komihash,MuseAir, andfoldhash.
The consenus was that only truemulticollisionattacks, where a large set of inputs all collide with high probability are worth fixing.
Universal hashing protects against that, but in principle a hash could be robust to multicollisions and not be universal.

That's a fair position, in particular since changing the hash is hard to do backwards compatibly.
However, for this blog post we focus onprovable guarantees, and the discovered collisions prove that the heuristic hashes are not just universal hashes that haven't been proven correct yet.
And we also did find flooding-grade key-free multicollisions for many hashes.3

Hash robustness: colliding inputs and affected keys

Four categories of hash robustness issues, shown side by side: seed-independent pairs, few-way collisions, weak-key multicollisions, and seed-independent multicollisions. Each category has a short definition and its most directly relevant applications. All inputs discussed here are chosen without knowing the secret key.

Seed-independent pair

The same two distinct inputs

collide for every key.

Use for: Fingerprinting,

hash-based equality,

deduplication, approximate

membership filters.

Few-way collisions

A small set collides for

some keys.

Use for: Cuckoo hashing,

bounded-capacity buckets,

hash-indexed caches and

hardware tables.

Weak-key multicollision

A large fixed set collides

for a fraction of keys.

Use for: Randomized

dictionaries, long-lived

caches, hash-based

partitioning.

Multicollisions

A large fixed set collides

for every key.

Use for: Maps and sets,

hash-based database

operations, sharding,

distinct-count sketches.

Hash robustness: colliding inputs and affected keys

Four categories of hash robustness issues, shown side by side: seed-independent pairs, few-way collisions, weak-key multicollisions, and seed-independent multicollisions. Each category has a short definition and its most directly relevant applications. All inputs discussed here are chosen without knowing the secret key.

Seed-independent pair

The same two distinct inputs

collide for every key.

Use for: Fingerprinting,

hash-based equality,

deduplication, approximate

membership filters.

Few-way collisions

A small set collides for

some keys.

Use for: Cuckoo hashing,

bounded-capacity buckets,

hash-indexed caches and

hardware tables.

Weak-key multicollision

A large fixed set collides

for a fraction of keys.

Use for: Randomized

dictionaries, long-lived

caches, hash-based

partitioning.

Multicollisions

A large fixed set collides

for every key.

Use for: Maps and sets,

hash-based database

operations, sharding,

distinct-count sketches.

Hash robustness: colliding inputs and affected keys

Four categories of hash robustness issues, shown side by side: seed-independent pairs, few-way collisions, weak-key multicollisions, and seed-independent multicollisions. Each category has a short definition and its most directly relevant applications. All inputs discussed here are chosen without knowing the secret key.

Seed-independent pair

The same two distinct inputs

collide for every key.

Use for: Fingerprinting,

hash-based equality,

deduplication, approximate

membership filters.

Few-way collisions

A small set collides for

some keys.

Use for: Cuckoo hashing,

bounded-capacity buckets,

hash-indexed caches and

hardware tables.

Weak-key multicollision

A large fixed set collides

for a fraction of keys.

Use for: Randomized

dictionaries, long-lived

caches, hash-based

partitioning.

Multicollisions

A large fixed set collides

for every key.

Use for: Maps and sets,

hash-based database

operations, sharding,

distinct-count sketches.

Figure 2:
 Inputs are chosen without knowing the secret key. Applications indicate where each weakness is most directly relevant. 
Findings for individual hashes
.

Hopefully this work will inspire research into even faster provable hashes. Many of the “exploits” used similar bad patterns repeated across many hash families. Hopefully the knee-jerk reaction is not just switching everything to “cryptographically secure” hashes like SHA or using AES native instructions. As we have shown,provably securehashes are plentiful and fast.

If anyone has issues with the above presentation, or would like me to add/update/remove any particular hash, pleasecontact me on Twitter.

Below follows an appendix with the in-depth analysis of each hash. Be warned that itcontains AI slop, and I can’t guarantee everything is correct. I only trust the concrete examples found and measured.

## Appendix

A few terms used in the details

Message, collision and witness
A message is the input data. A collision is two different messages with the same complete hash. A witness is a specific pair demonstrating such a collision.

Seed and key
A seed is a small input used to initialize the hash. The key is all its secret material. Values calculated from one seed may be related; they are not automatically independent random values.

Word, block and lane
A word is a fixed-size integer, usually 64 bits or eight bytes here. A block is a chunk of the message. A lane is one of several calculations performed alongside each other.

State and finalizer
The state holds intermediate results as the hash processes data. A finalizer is the last mixing step that turns that state into the output.

API and wrapper
An API is the function a program can call. A wrapper is code around the core calculation, for example to encode the input length, expand a seed or shorten the output. Those steps can affect the guarantee.

Uniform and independent
Uniform means every allowed value is equally likely. Independent means learning one random choice tells you nothing about another.

XOR, AES and SIMD
XOR combines bits, producing 1 where they differ. AES is an encryption algorithm whose instructions some hashes reuse for mixing. SIMD instructions operate on several values at once for speed.

Field arithmetic
A finite field is a number system with a fixed set of values and well-defined addition, multiplication and division by nonzero values. GF(2
128
) names one with 2
128
 values. These rules make certain collision proofs possible.

Lean and proof scope
Lean is software that checks the steps of a mathematical proof. A proof about an algorithm does not automatically prove that a C implementation or compiler executes it correctly.

The appendix contains the individual hash analyses, their recurring collision patterns, and instructions for verifying and reproducing the results.

## Appendix A. The hard cases, hash by hash

Each entry below starts with the practical finding, then gives the exact code version, message bytes and derivation. The pattern labels link to shared explanations of the arithmetic. “Every seed” means changing the seed cannot separate that pair; a sampled rate describes only the tested random-key experiment.

### Recurring patterns

Most of these pairs exploit the same few identities. A secret added after information is lost cannot recover it; a second lane or a wider output cannot help if it repeats the same computation. The groups below describe the witnesses in these entries, not every path of each hash. A row can belong to more than one group. The generator examples are marked separately from the selected scoring pairs; “ungrouped” means the entry does not establish one of these mechanisms, not that the hash is safe.

#### P1. The folded multiply forgets complements

LetB = 264andF(a,b) = lo₆₄(ab) ⊕ hi₆₄(ab). Complementing a message word also complements its XOR-masked operand. The exact integer identity is:(~a)(~b) = ab + (264−1)(264−1−a−b)If the products have halves (lo, hi) and (lo′, hi′), the folds agree exactly whenlo ⊕ lo′ = hi ⊕ hi′: the carry and borrow patterns can erase the change. The entries report roughly 2−27for several pairs, not a common theorem or rate for all seed mappings; the rate is the same whether the operands are masked by the shipped constants or by uniform secret words, because the differential never uses the mask value. XXH3-64’s 32-byte NAF pair (2−10.47) needs the default-secret words and is recorded as a caveat, not as the scored pair. At eight bytes, foldhash reads the same word into both operands, so one complemented word suffices. XXH3-128 also preserves the raw sum by choosing w₁ = ~w₀. For the documented XXH3-64 32/128-byte pair, common tail folds change the output but not the colliding-seed set; quality’s extra fold likewise preserves every fast collision.

Rows:wyhash,rapidhash v1,rapidhash v3,foldhash-fast,foldhash-quality,XXH3-64,XXH3-128.

What a proof needs:an XOR-universality bound for the keyed fold under the actual joint distribution of its masks, including the zero output difference used here.

#### P2. Public arithmetic leaves the seed out of the difference

For a seed-last wrapperHₛ(m) = Gₛ(C(m)), the identityC(m) = C(m′) ⇒ Hₛ(m) = Hₛ(m′)holds for every seed, whether or not Gₛ is invertible. CityHash, FarmHash, gxhash and pengyhash lose the distinction in public compression. MUM and mir instead XOR an already-colliding public product term into their seeded state; their fold adds the product halves. MuseAir reacheshead ⊕ P(tail) ⊕ Kₛ, so a head change cancels any chosen public tail change at the same length. In mx3, h ← (h + g(w))C leaves a common seed coefficient after the same number of steps, and g is publicly invertible. Fasthash similarly lets an inverse word mix cancel the length term. MurmurHash3’s public word bijections let the attacker place, then cancel, the top-bit difference described in P7; the seed affects the state but does not hide that differential.

Rows:CityHash64,FarmHash64,gxhash,pengyhash,MUM v3,mir,MuseAir,mx3,fasthash-32/64,MurmurHash3.

What a proof needs:a collision bound for the message compression itself, with keys participating in the arithmetic that distinguishes messages; keying only the surrounding state or finalizer supplies no such bound.

#### P3. Zero absorbs the other operand

The identity is simply0 · x = 0 · x′ = 0. In a5hash-128, a public operand can be set to zero for every seed. In a5hash-64, the first message word matches one value of the expanded state, zeroing an operand on its exactly counted seed fibre of density 118 × 2−45. Half a word suffices in HighwayHash’s lo₃₂(v₁)·hi₃₂(v₀) product: fixing hi₃₂(key[0]) makes hi₃₂(v₀) zero. That class has density 2−32, but a further conditional event of probability 56165/240is required to merge the full state. HalftimeHash24’s equal-length Encode3 witness does collide throughout its high₃₂(core_key[6]) = 0 class, also of density 2−32; the encoding lets only one symbol change. These are different events, not a shared collision rate.

The shipped constants also admit this zero-operand pattern inwyhashandrapidhash v1/v3. Prior reports include wyhash issue #15 and rapidhash issues #10 and #25. Those rows are scored under the random-secret model, with the seed and every secret word uniform, which excludes these shipped-constant pairs; each row’s notes record them as default-secret caveats.

Rows:a5hash-128,a5hash-64,HighwayHash,HalftimeHash24 (equal-length witness).

What a proof needs:a bound on the actual key fibres that zero an operand, together with the conditional probability that the remaining state differences cancel.

#### P4. Related lanes repeat the same product

In komihash, a second lane inherits a public XOR offset: s₂ = s₁ ⊕ c. Choosing its message word as w₂ = w₁ ⊕ c givesw₂ ⊕ s₂ = (w₁ ⊕ c) ⊕ (s₁ ⊕ c) = w₁ ⊕ s₁. Compensating the other operand’s public offset makes both lane products identical within each message. Their low halves cancel in the lane XOR; the chosen bit flips leave a common high-product change of at most one, which often vanishes or cancels through the additions. This explains the measured 0.9106 rate at lengths 64 through 127 bytes, where the fold follows immediately. The entry does not extend that result past another bulk round.

Row:komihash.

What a proof needs:independent lane keys, or a joint differential bound for their actual dependence, so an attacker cannot equate lane operands merely by cancelling public offsets.

#### P5. Length encoding can be cancelled

A length field only helps if it distinguishes the encoded inputs. On gxhash’s short path,Cₙ(m)ᵢ = (pad(m)ᵢ + n) mod 256; fifteen zero bytes and sixteen ff bytes both become sixteen 0f bytes. HalftimeHash’s raw advanced core omits length, so empty and one zero byte coincide. Fasthash includes length, but one message step lets the attacker solvemix(w) = 7m ⊕ 8m, cancelling the difference between seven and eight bytes before the common multiply. For mx3’s one-byte/eight-byte pair, the corresponding equation isg(w) = g(0) + C(g(2) − g(9)). Both paths have the same seed coefficient. These are encoding or length-term aliases; t1ha2’s cross-length pair still requires the carry event in P7.

Rows:gxhash,HalftimeHash24 (raw core),fasthash-32/64,mx3.

What a proof needs:injective length framing before compression, or a keyed cross-length collision bound that accounts for how message words can cancel the length term.

#### P6. Equal-state blocks and public inverses generate families

A collision recipe can give more than a pair. MurmurHash3’s supporting 32-byte construction hasT_A(s) = T_B(s)for the incoming state s: it resets thedifferenceto zero, not the state to a fixed constant. Choosing A or B at each of n positions therefore gives 2nequal-length colliding messages. Separately, the CityHash README’s pair B solves a public word permutation for a chosen compressed value; three free words give 2192colliding 32-byte inputs. MuseAir’s invertible head encoding giveshead′ = head ⊕ P(T) ⊕ P(T′), one partner for every tail of the chosen length. These are the documented generators; the selected shorter CityHash and MurmurHash3 pairs keep their original scores.

Rows:MurmurHash3 (supporting two-block pair)·generator record;CityHash64 (supporting pair B)·inverse record;MuseAir·head–tail recipe.

What a proof needs:an injective encoding or a keyed collision bound for the joint message-to-state map; invertibility in one public input word makes these compensating words easy to solve and does not make the whole map injective.

#### P7. Top bits and carries carry a difference through

At word width w, let t = 2w−1. Modulo 2w,x ⊕ t = x + t, and (x ⊕ t)c = (xc) ⊕ t for odd c. Public rotations and XOR shifts can place a difference at that top bit; a later message word cancels it. MurmurHash3, fasthash’s supporting equal-length pair and nmhash32x use this deterministic identity. nmhash32 works in 16-bit multiplication lanes and additionally constrains an addition and a carry across bit 13. More generally,x ⊕ d = x + d − 2(x & d), so a fixed XOR change can become opposite signed additive changes. SpookyHash’s late injection and tail cancel for the favourable sign; exact half-seed balance is unproved. The selected t1ha2 pair instead uses a seed class of density 2−24, with measured success about 2−4.19within that class. Its cancellation depends on carries, not a zero operand.

Rows:MurmurHash3,fasthash-32/64 (supporting equal-length pair),nmhash32,nmhash32x,SpookyHash V2,t1ha2.

What a proof needs:a differential bound through the actual word widths and joint carry conditions, rather than an assumption that rotations, odd multipliers or individual state bits behave independently.

I leaveaHash’s AES pathungrouped: its entry needs an inverse-AES differential and simultaneous shuffled-addition cancellation under independent keys, which is not established by the identities above. The proof and comparison entries also receive no collision-pattern assignment. Neither a proof gap nor a shared multiplication instruction is enough to assign a row.

message word

state word

public constant

seed enters

secret

×

multiply

⊕

fold lo ⊕ hi

Δ: m → m′

orange ends at cancellation

Byte ranges are inclusive; arrows name operations.

Bare 8- or 16-digit word values are hexadecimal.

Δ = XOR difference; δ = addition difference.

Rounded words, double-bordered state words, dashed public constants, seed dots, and orange differences identify the same operations throughout these diagrams.

In the numbered excerpts, I specialize the supplied implementations to the selected message paths. Unless marked otherwise, words are unsigned 64-bit values;+,-and ordinary*wrap modulo264,^is XOR, androtlrotates a 64-bit word left.mul128(a,b) → (lo,hi)returns the full unsigned product, andfold(a,b) = lo ^ hi. Right-hand sides use the old values in tuple assignments.read32lezero-extends its result to 64 bits before shifts;read64lereads a little-endian word at a byte offset.words(lo,hi)is a 128-bit block. AES operations are single AES instruction rounds, with the named second operand XORed at the end;aesenclastomits MixColumns. Byte shuffles use little-endian memory order;pack_le(bytes, indices)packs the selected bytes in the listed order, least-significant byte first. Each comment marks the secret inputs, public constants and operation used by the example.

### CityHash64pattern:P2·P6

The messages collide before CityHash uses the seed. Once both inputs have become the same intermediate value, adding the same secret cannot distinguish them.

8-byte path · the two reads overlap

w0 · bytes 0..7

m ≠ m′

k2 · public

mul = k2 + 16

public

+ k2

read

a = w0 + k2

b = w0

rotl(b, 27)

rotl(a, 39) + b

b

a

×

×

hi

hi

×

×

mul

mul

lo + a → c

lo → d

⊕

hi discarded in both products

Public HashLen16(c, d, mul)

c ⊕ d

×

hi

×

mul · public

lo; ⊕ (lo ≫ 47) → a₁

×

hi

⊕ d; ×

mul · public

lo; ⊕ (lo ≫ 47) → b₁

×

hi

mul · public

hi discarded

lo · cancels here

equal public_hash

− k2 (public)

seed

seed enters

HashLen16(public_hash − k2,

seed, kMul)

kMul · public

×

Same wrapper arguments for every seed.

CityHash64 compresses the two eight-byte words to the same public value before the seed enters the final HashLen16 call.

01
// Input: M[8]; secret seed (64 bits). All constants below are public.

02
const k2 = 0x9ae16a3b2f90404f, kMul = 0x9ddfea08eb382d69;

03
u64 HashLen16(u64 u, u64 v, u64 mul) {

04
 a = (u ^ v) * mul; a ^= a >> 47;

05
 b = (v ^ a) * mul; b ^= b >> 47;

06
 return b * mul;

07
}

08
len = 8; mul = k2 + 2 * len;

09
a = read64le(M, 0) + k2;

10
b = read64le(M, len - 8); // Both reads use the same word.

11
c = rotl(b, 27) * mul + a; // Source rotr(b, 37).

12
d = (rotl(a, 39) + b) * mul; // Source rotr(a, 25).

13
public_hash = HashLen16(c, d, mul); // Exploit: collision before any seed.

14
return HashLen16(public_hash - k2, seed, kMul);

15
// WithSeeds: replace k2, seed on line 14 by secret seed0, seed1.

Code:cityhash;SMHasher3 hashes/cityhash.cpp, CityHash64WithSeed v1.1.1; tested at SMHasher3 commit7ad8939d; local copy:sources/cityhash.cpp. Excerpt: HashLen16, HashLen0to16 and CityHash64WithSeeds, source lines 236–259, 289–297 and 389–396. The existingCityHash source excerptshows the same seeded wrapper.

Original quoted wrapper

I transcribed this wrapper from theCityHash source excerptin the checked source record:

uint64 CityHash64WithSeed(const char *s, size_t len, uint64 seed) {
 return CityHash64WithSeeds(s, len, k2, seed);
}

uint64 CityHash64WithSeeds(const char *s, size_t len,
 uint64 seed0, uint64 seed1) {
 return HashLen16(CityHash64(s, len) - seed0, seed1);
}

Inlines 8–13, the entire message has already become one public hash value before either seed is used. If two messages have equalCityHash64values, this wrapper receives identical arguments for every choice of secrets. The final mixing inlines 14–15cannot separate them. For fixed seeds, the final operation is also bijective in the public value. The forward collision implication holds without needing that property.

CityHash64 — EXTENSION —Peters 2024;Aumasson, Bernstein and Boßlet 2012.These are eight-byte inputs for v1.1.1:

/* Hex encodes bytes in memory order, not hexadecimal integers. */
A = hex("a01109025ea76be1");
B = hex("020bd424b04ae555");

/* Example seed: */
0x6637c1ce6357a2c8
/* H(A) = H(B), selected 64-bit output: 0xd4d44b0c5f8bae0a */

Length and word difference.8 and 8 bytes;L = 1. Zero-based little-endian words are shown below; a final partial word is zero-extended only for displaying the difference, not for the hash input.

w[0]: 0xe16ba75e020911a0 -> 0x55e54ab024d40b02 (XOR 0xb48eedee26dd1aa2)

Collision probability: 1 for every seed; L = 1 and score 0. The all-seed statement is structural (the seed enters only through a bijection of the public value); the verifier additionally samples 224random 64-bit seeds and 224(seed0, seed1) pairs, all of which collide, and records/verify-check.log holds an earlier 220run. Re-run on 2026-09-18 against upstream google/cityhash master f5dc541 and SMHasher3 3b619371.

Reproduction.From the supplied Reproduction documentation, run inverify/cityhash-64/:

cc -O2 -std=c11 -o cityhash64_verify cityhash64_verify.c -lm
./cityhash64_verify # 2^24 random seeds (default), about 0.3 s single-threaded

Original: Orson Peters, “Breaking CityHash64, MurmurHash2/3, wyhash, and more”, orlp.net, 2 November 2024 (post); Jean-Philippe Aumasson, Daniel J. Bernstein and Martin Boßlet, “Hash-flooding DoS reloaded: attacks and defenses”, 29C3, December 2012 (slides). The seed-last collision mechanism is reproduced; Peters' published v1.0.3 strings do not collide on v1.1.1, and the eight-byte pair here is a new v1.1.1 construction; this pair in turn does not collide under v1.0.3 (the libc++ std::hash variant), which Peters' strings cover; the seed-last weakness is common to both versions. The supporting longer construction uses a reconstructed inversion argument.

Selected score (CityHash64 v1.1.1): 0 bits.8/8 bytes;L = 1. 1 (every seed). SeeThe collision score.

Try it in the browser
Load on view

Waiting to validate the verification program.

Run verify/cityhash-64 locally

The same verifier’s supporting pair B inverts the public 32-byte path in one word while leaving three words free, giving 2192messages with a chosen public hash. This is theP6 generator; the eight-byte pair above remains the selected scoring witness.

Records:Original project & code·Verifier package·Measurements

### FarmHash64pattern:P2

This FarmHash variant first computes a value without using the secret. The selected messages already agree at that step, so both seeded interfaces preserve the collision.

8-byte path · the two reads overlap

w0 · bytes 0..7

m ≠ m′

k2 · public

mul = k2 + 16

public

+ k2

read

a = w0 + k2

b = w0

rotl(b, 27)

rotl(a, 39) + b

b

a

×

×

hi

hi

×

×

mul

mul

lo + a → c

lo → d

⊕

hi discarded in both products

Public HashLen16(c, d, mul)

c ⊕ d

×

hi

×

mul · public

lo; ⊕ (lo ≫ 47) → a₁

×

hi

⊕ d; ×

mul · public

lo; ⊕ (lo ≫ 47) → b₁

×

hi

mul · public

hi discarded

lo · cancels here

equal public_hash

− k2 (public)

seed

seed enters

HashLen16(public_hash − k2,

seed, kMul)

kMul · public

×

Same wrapper arguments for every seed.

FarmHash64 NA compresses the two eight-byte words to the same public value before the seed enters the final HashLen16 call.

01
// Input: M[8]; secret seed (64 bits). All constants below are public.

02
const k2 = 0x9ae16a3b2f90404f, kMul = 0x9ddfea08eb382d69;

03
u64 HashLen16(u64 u, u64 v, u64 mul) {

04
 a = (u ^ v) * mul; a ^= a >> 47;

05
 b = (v ^ a) * mul; b ^= b >> 47;

06
 return b * mul;

07
}

08
len = 8; mul = k2 + 2 * len;

09
a = read64le(M, 0) + k2;

10
b = read64le(M, len - 8); // Both reads use the same word.

11
c = rotl(b, 27) * mul + a; // Source rotr(b, 37).

12
d = (rotl(a, 39) + b) * mul; // Source rotr(a, 25).

13
public_hash = HashLen16(c, d, mul); // Exploit: public NA compression collides.

14
return HashLen16(public_hash - k2, seed, kMul);

15
// Hash64WithSeeds: replace k2, seed on line 14 by secret seed0, seed1.

Code:farmhash;SMHasher3 hashes/farmhash.cpp, FarmHash-64.NA; tested at SMHasher3 commit7ad8939d; local copy:sources/farmhash.cpp. Excerpt: HashLen16 and farmhashna, source lines 169–195, 238–246 and 351–358. (byte-identical at SMHasher3 HEAD 3b619371; google/farmhash master 9d99331e has had no functional change to farmhashna since v1.1, March 2015)

The NA short path inlines 8–13compresses the message without a secret. At eight bytes its two reads overlap completely, and the selected pair gives the same public hash. The seed enters only inline 14, so every choice of seed receives identical final-mix arguments. The two-seed interface inline 15leaves the same implication intact.

FarmHash64 NA — EXTENSION —Peters 2024.Its seeded wrapper has the same structure. The new short pair is:

/* Hex encodes bytes in memory order, not hexadecimal integers. */
A = hex("574522e6dce98176");
B = hex("0df3b1f900d36296");

/* Example seed: */
0x82bdf567d8ebbf4f

Length and word difference.8 and 8 bytes;L = 1. Zero-based little-endian words are shown below; a final partial word is zero-extended only for displaying the difference, not for the hash input.

w[0]: 0x7681e9dce6224557 -> 0x9662d300f9b1f30d (XOR 0xe0e33adc1f93b65a)

At the displayed seed, h(A) = 0x49186432ae14e980 and h(B) = 0x49186432ae14e980 (evaluated locally from the supplied source). Collision probability: 1 for every seed; L = 1 and score 0. The record sampled 230seeds on both seed interfaces without a counterexample; the all-seed statement follows from the public collision (HashLen16 is a bijection of its first argument for every seed). libfarmhash's public wrapper returns the same value when built with NDEBUG, and a bijective DebugTweak of it otherwise.

Reproduction.From the supplied Reproduction documentation, run inverify/farmhash-64/:

cc -O2 -std=c11 -o farmhash64_pairs farmhash64_pairs.c -lm
./farmhash64_pairs # 2^24 seeds per pair (about 1.5 s single-threaded)

The supplied record documents aREPRODUCTION —Peters 2024of Peters’ separately published FarmHash strings on FarmHash NA. That reproduction does not transfer his CityHash strings to newer CityHash code. The displayed FarmHash witness is the verifier-confirmed eight-byte pair. For both families, switching to the interface with two seed words leaves the structural problem intact.

Original: Orson Peters, “Breaking CityHash64, MurmurHash2/3, wyhash, and more”, orlp.net, 2 November 2024 (post). Peters’ separately published FarmHash strings reproduce on FarmHash NA; the eight-byte NA witness here is a new, shorter construction using the same seed-last structure.

Selected score (FarmHash64 NA v1.1): 0 bits.8/8 bytes;L = 1. 1 (every seed). SeeThe collision score.

Try it in the browser
Load on view

Waiting to validate the verification program.

Run verify/farmhash-64 locally

Records:Original project & code·Verifier package·Measurements

### gxhashpattern:P2·P5

The short-input encoding turns a 15-byte message and a 16-byte message into the same block. The AES-based mixing starts too late to recover their difference.

m: 15 zero bytes

w0 [0..7]

w1 [8..14] + pad

m′: 16 ff bytes

w0 [0..7]

w1 [8..15]

+ 15 per byte

+ 16 mod 256

00 + 0f = 0f

ff + 10 = 0f

copy

copy

cancels here: all 16 bytes are 0f

=

equal compressed block

AES round transform

⊕

seed

⊕ (seed, seed)

seed enters

equal state

K0, K1, K2 · public AES finalization

gxhash’s bytewise length addition makes the short messages identical before the seed is XORed into the AES round output.

01
// Input: M[len], 1 <= len <= 16; secret seed (64 bits).

02
const K0 = words(0xb09d3e21f2784542, 0xfc3bc28e89c222e5); // Public.

03
const K1 = words(0xcb6b2e9b03fce279, 0x39132bd9b361dc58); // Public.

04
const K2 = words(0x689d2b7dd0012e32, 0xc78b122b5544b1b7); // Public.

05
byte block[16] = {0};

06
copy(block, M, len); // Zero padding; no terminator in M.

07
for (i = 0; i < 16; ++i)

08
 block[i] = (block[i] + len) & 255; // Exploit: bytewise length addition.

09
state = words(read64le(block, 0), read64le(block, 8));

10
state = aesenc(state, words(seed, seed)); // First secret-dependent step.

11
state = aesenc(state, K0);

12
state = aesenc(state, K1);

13
state = aesenclast(state, K2);

14
return state.lo; // The 128-bit variant returns state.

Code:gxhash;SMHasher3 hashes/gxhash.cpp, v3.5.0; tested at SMHasher3 commit7ad8939d; local copy:sources/gxhash.cpp. Excerpt: KEYDATA, get_partial, compress_all and gxhash_x86, source lines 43–78 and 149–213. The SMHasher3 file is unchanged through 3b619371; it ports ogxd/gxhash 55bde47 (current main; output-identical to tag 3.5.0).

On this short path,lines 5–8zero-pad the message and add its length bytewise. Fifteen zero bytes and sixteenffbytes reach the same block. The source structure isfinalize(aes_encrypt(compress_all(input), seed)): the first secret-dependent operation isline 10. Identical compressed blocks remain identical through those rounds, so the collision survives both full output widths.

gxhash — EXTENSION —Peters 2024.The source record reduces its structure tofinalize(aes_encrypt(compress_all(input), seed)). The compression is public. The following pair gives a cross-length collision:

/* Hex encodes bytes in memory order, not hexadecimal integers. */
A = hex("000000000000000000000000000000");
B = hex("ffffffffffffffffffffffffffffffff");

/* Example seed: */
0xf556ecbfcbfee3ad

Length and word difference.15 and 16 bytes;L = 2. Zero-based little-endian words are shown below; a final partial word is zero-extended only for displaying the difference, not for the hash input.

w[0]: 0x0000000000000000 -> 0xffffffffffffffff (XOR 0xffffffffffffffff)
w[1]: 0x0000000000000000 -> 0xffffffffffffffff (XOR 0xffffffffffffffff)

At the displayed seed, h64(A) = h64(B) = 0x43ec3783791d0fb8; both full 128-bit outputs are 0x0d7dc5b336c1cdc543ec3783791d0fb8. The shipped logs in verify/gxhash-64/ report 67,108,864/67,108,864 seeds (226, NEON, run_2e26_neon.txt) and 16,777,216/16,777,216 portable seeds (run_2e24_portable.txt) colliding on both output widths; a 226AES-NI rerun of the same program on a Xeon 8375C (run_2e26_xeon_aesni.txt) gives the same 67,108,864/67,108,864, and the Rust crate built from ogxd/gxhash main (55bde47, unchanged since the port, checked 18 September 2026) returns the same 64- and 128-bit values for both messages (rust_check_head.txt). The structural rate is 1, L = 2, and the score is ≤ 1.

Reproduction.From the supplied Reproduction documentation, run inverify/gxhash-64/:

cc -O2 -o gxhash64_verify gxhash64_verify.c -lm # auto-detects ARMv8 AES; add -maes on x86 for AES-NI
./gxhash64_verify # 2^24 random seeds (default), about 1 s with hardware AES, 4 s portable

Original: Orson Peters, gxhash issue #83 “Hash has arbitrary seed-independent multicollisions, is not DoS resistant”, 2 June 2024 (open issue; later structural comment by purplesyringa; the pairs below were posted there on 18 September 2026). The seed-independent public-compression collision mechanism is reproduced; the new witnesses here include the 15-versus-16-byte pair and a verified equal-length 24-byte pair.

Selected score (gxhash-64 v3.5.0): ≤ 1 bits.15/16 bytes;L = 2. 1 (every seed). SeeThe collision score.

Try it in the browser
Load on view

Waiting to validate the verification program.

Run verify/gxhash-64 locally

Records:Original project & code·Verifier package·Measurements

### MurmurHash3 x64_128pattern:P2·P6·P7

The attacker introduces a controlled difference early in the hash and cancels it with later message data. The construction works without knowing the seed and makes both halves of the output agree.

c1 · public

87c37b91114253d5

c2 · public

4cf5ad432745937f

x

×

×

hi

hi

×

c1 · public

lo; rotl 31

c2 · public

lo

mix1(x); both high halves discarded

x

×

×

hi

hi

×

c2 · public

lo; rotl 33

c1 · public

lo

mix2(x); both high halves discarded

seed32

seed enters

seed enters

h1

h2

w0 · bytes 0..7

Δmix1 = 2³⁶

w1 · bytes 8..15

Δmix2 = 2³²

⊕ mix1

⊕ mix2

×

hi

rotl 27; + h2

5 public

lo; + K₁

h1: Δ = 2⁶³

+

rotl 31 → Δ2⁶³

+ h1

cancels here

×

hi

× 5

5 public

lo; + K₂

equal h2

w2 · bytes 16..23

Δmix1 = 2⁶³

⊕ mix1(w2)

cancels here

equal h1

×5 keeps lo; hi discarded in both lanes.

K₁ = 52dce729; K₂ = 38495ab5 · public

Equal (h1, h2) enters length/final mixing.

MurmurHash3’s public word bijections inject chosen bit differences that cancel in h2 during the block and in h1 at the tail for every seed.

01
// Input: M[24]; secret seed32 (32 bits, zero-extended into 64-bit words).

02
const c1 = 0x87c37b91114253d5, c2 = 0x4cf5ad432745937f; // Public.

03
u64 mix1(u64 x) { return rotl(x * c1, 31) * c2; }

04
u64 mix2(u64 x) { return rotl(x * c2, 33) * c1; }

05
u64 fmix(u64 x) { // Public finalizer constants.

06
 x ^= x >> 33; x *= 0xff51afd7ed558ccd;

07
 x ^= x >> 33; x *= 0xc4ceb9fe1a85ec53;

08
 return x ^ (x >> 33);

09
}

10
h1 = u64(seed32); h2 = u64(seed32);

11
h1 ^= mix1(read64le(M, 0)); // Exploit: choose injected difference.

12
h1 = rotl(h1, 27); h1 += h2; h1 = h1 * 5 + 0x52dce729;

13
h2 ^= mix2(read64le(M, 8));

14
h2 = rotl(h2, 31); h2 += h1; h2 = h2 * 5 + 0x38495ab5;

15
h1 ^= mix1(read64le(M, 16)); // Eight-byte tail cancels difference.

16
h1 ^= 24; h2 ^= 24; // Length injection, in bytes.

17
h1 += h2; h2 += h1;

18
h1 = fmix(h1); h2 = fmix(h2);

19
h1 += h2; h2 += h1;

20
return words(h1, h2);

Code:smhasher;SMHasher3 hashes/murmurhash3.cpp, MurmurHash3 x64_128; tested at SMHasher3 commit7ad8939d; local copy:sources/murmurhash3.cpp. Excerpt: fmix64 and MurmurHash3_128, source lines 43–52 and 221–299. The SMHasher3 file is unchanged through 3b619371 (2026-08-27) and last changed 2023-02-12.

The seed affects the running state inline 10. Message words pass through the public invertible functions inlines 3–4before being XORed into it. That lets an attacker choose the difference injected into the state, even without knowing the state itself. Modulo264, XORing the top bit is the same as adding263. That difference survives addition of a common value and multiplication by the odd constant used bylines 12–14. Public word transforms and rotations place the difference where it is needed; later message words cancel it. For this pair, one block leaves a difference in one state word and the tail inline 15removes it before finalization.

MurmurHash3 x64_128 — EXTENSION —Aumasson, Bernstein and Boßlet 2012.The selected pair is:

/* Hex encodes bytes in memory order, not hexadecimal integers. */
A = hex("000000000000000000000000000000000000000000000000");
B = hex("60a0fd219e0ef2cd42e098d38ee8728d000000007d4dce82");

/* Example seed: */
0x00000000

Length and word difference.24 and 24 bytes;L = 3. Zero-based little-endian words are shown below; a final partial word is zero-extended only for displaying the difference, not for the hash input.

w[0]: 0x0000000000000000 -> 0xcdf20e9e21fda060 (XOR 0xcdf20e9e21fda060)
w[1]: 0x0000000000000000 -> 0x8d72e88ed398e042 (XOR 0x8d72e88ed398e042)
w[2]: 0x0000000000000000 -> 0x82ce4d7d00000000 (XOR 0x82ce4d7d00000000)

At seed 0x00000000, both outputs, as two 64-bit words in API order, are (0x042b02a247843246, 0x2541774c612f4f96) (evaluated locally from the supplied source). All 232/232API seeds collide in the recorded enumeration: rate 1, L = 3, score ≤ 1.59. The verify program prints the same value as 16 little-endian bytes, 46328447a2022b04964f2f614c774125.

Reproduction.From the supplied Reproduction documentation, run inverify/murmurhash3-128/:

cc -std=c11 -O2 -o murmurhash3_128_verify murmurhash3_128_verify.c -lm
./murmurhash3_128_verify # 2^24 random seeds, rng seed 1

Original: Jean-Philippe Aumasson, Daniel J. Bernstein and Martin Boßlet, “Hash-flooding DoS reloaded: attacks and defenses”, 29C3, December 2012 (slides); Orson Peters, “Breaking CityHash64, MurmurHash2/3, wyhash, and more”, orlp.net, 2 November 2024 (post). The 2012 top-bit mechanism is reproduced and extended here to a new 24-byte x64_128 pair, checked over all232API seeds; Peters’ x86_32 example is a different variant and was separately reproduced. A 128-bit return type does not undo a collision in the state that produces it.

Selected score (MurmurHash3 x64_128): ≤ 1.59 bits.24/24 bytes;L = 3. 1 (every seed). SeeThe collision score.

Try it in the browser
Load on view

Waiting to validate the verification program.

Run verify/murmurhash3-128 locally

The supporting 32-byte two-block pair cancels the state difference for the incoming state, so n choices between its two 32-byte alternatives give 2ncolliding messages. It resets the difference, not the state; this is theP6 generator, separate from the selected 24-byte pair.

Records:Original project & code·Verifier package·Measurements

### MuseAirpattern:P2·P6

One part of the message can be changed to cancel a change elsewhere. In the historical version studied here, this leaves the same intermediate state for every seed.

seed

17 ⊕ C1 · public

×

⊕ C0 (public)

×

lo2 ⊕ 17

hi2 ⊕ seed

i_seed

j_seed

w0 [0..7], w1 [8..15]

head_i: bytes 0..3 ∥ 12..15

head_j: bytes 4..7 ∥ 8..11

Δhead_i = Δlo0; Δhead_j = Δhi0

⊕ head_i

⊕ head_j

w2 · byte 16

u = byte at bits 0,24,48

v = 0

public tail encoding

C2, C3 · public

C4, C5 · public

×

×

u ⊕ C3

× C2

v ⊕ C5

× C4

lo0; ⊕

hi0; ⊕

hi1; ⊕

lo1; ⊕

⊕

⊕

equal i

equal j

Head and tail differences cancel here for every seed.

Bulk context only · six products, updated in order

s0..5 start at C0+seed, C1−seed, C2⊕seed,

C3+seed, C4−seed, C5⊕seed; all C are public.

s0 ⊕ w0 [0..7]

s1 ⊕ w1 [8..15]

×

×

×

⊕

hi0

+ s0

lo0

s1 ⊕ w2 [16..23]

s2 ⊕ w3 [24..31]

×

×

×

⊕

hi1

+ s1

lo1

s2 ⊕ w4 [32..39]

s3 ⊕ w5 [40..47]

×

×

×

⊕

hi2

+ s2

lo2

s3 ⊕ w6 [48..55]

s4 ⊕ w7 [56..63]

×

×

×

⊕

hi3

+ s3

lo3

s4 ⊕ w8 [64..71]

s5 ⊕ w9 [72..79]

×

×

×

⊕

hi4

+ s4

lo4

s5 ⊕ w10 [80..87]

s0 ⊕ w11 [88..95]

×

×

×

⊕

hi5

+ s5

lo5 → next block

First block uses public C6 as the incoming lo5.

MuseAir’s 17-byte pair cancels the public tail-product difference with the head before finalization; the six-product bulk ring below is a separate path not used by this pair.

01
// Input: M[17]; secret seed (64 bits); ordinary MuseAir-64 v0.3 path.

02
const C[6] = {0x5ae31e589c56e17a, 0x96d7bb04e64f6da9, // Public.

03
 0x7ab1006b26f9eb64, 0x21233394220b8457,

04
 0x047cb9557c9f3b43, 0xd24f2590c0bcee28};

05
(lo2, hi2) = mul128(seed ^ C[0], 17 ^ C[1]);

06
i = (read32le(M, 0) << 32) | read32le(M, 12); // read_short(head, 16).

07
j = (read32le(M, 4) << 32) | read32le(M, 8);

08
i ^= 17 ^ lo2; j ^= seed ^ hi2;

09
u = (u64(M[16]) << 48) | (u64(M[16]) << 24) | M[16];

10
v = 0; // read_short(tail, 1): same byte thrice.

11
(lo0, hi0) = mul128(C[2], C[3] ^ u); // Public tail products.

12
(lo1, hi1) = mul128(C[4], C[5] ^ v);

13
i ^= lo0 ^ hi1; j ^= lo1 ^ hi0; // Exploit: head XOR cancels tail XOR.

14
// All four variants now have the same (i,j) for the two messages.

15
(lo2, hi2) = mul128(i ^ C[2], j ^ C[3]);

16
i ^= lo2; j ^= hi2;

17
(lo2, hi2) = mul128(i ^ C[4], j ^ C[5]);

18
return i ^ j ^ lo2 ^ hi2;

Code:museair;SMHasher3 hashes/museair.cpp, MuseAir v0.3; tested at SMHasher3 commit7ad8939d; local copy:sources/museair.cpp. Excerpt: museair_read_short and museair_hash_short, source lines 15–106.

Inlines 5–8, the head and seed contribute to a pair of state words, whilelines 9–13inject the tail through public multiplications. The head encoding is invertible, so a change to the tail can be compensated by a change to the head. In schematic notation, the state ishead XOR public_tail(tail) XOR seed_term(length, seed). For equal lengths, the seed term is common to both messages. Choose the new head so that its change cancels the public tail’s change atline 13, and the finalizer sees identical inputs. The whole state presented to finalization agrees.

MuseAir v0.3 — EXTENSION —Peters 2026.This pair collides in all four SMHasher3 variants, including their full 128-bit outputs:

/* Hex encodes bytes in memory order, not hexadecimal integers. */
A = hex("0000000000000000000000000000000000");
B = hex("8079763bb19a00001a9a1100642d3a3f01");

/* Example seed: */
0x2cb0f69f4abea221
/* H(A) = H(B), selected 64-bit output: 0xd4ed417ecc529ae4 */

Length and word difference.17 and 17 bytes;L = 3. Zero-based little-endian words are shown below; a final partial word is zero-extended only for displaying the difference, not for the hash input.

w[0]: 0x0000000000000000 -> 0x00009ab13b767980 (XOR 0x00009ab13b767980)
w[1]: 0x0000000000000000 -> 0x3f3a2d6400119a1a (XOR 0x3f3a2d6400119a1a)
w[2]: 0x0000000000000000 -> 0x0000000000000001 (XOR 0x0000000000000001)

The supplied measurement record reports 230/230collisions in each of the four variants, both for the original implementation and a separate verifier; the author's C re-implementation, validated against the four SMHasher3 verification values, also found 226/ 226in all four variants; SMHasher3's hashes/museair.cpp is byte-identical at 7ad8939d and 3b619371. The structural rate is 1, L = 3, and the score is ≤ 1.59. At the displayed seed the 64-bit Standard variant gives 0xd4ed417ecc529ae4 and BFast-64 gives 0x7643ae45a2e33e20; the 128-bit variants give 0x1596b59d9910a4ce917c745e7176a8cd (as u128).

Reproduction.From the supplied Reproduction documentation, run inverify/museair/:

cc -O2 -std=c11 -o museair_verify museair_verify.c -lm
./museair_verify # 2^24 uniformly random seeds

Original: Orson Peters, MuseAir issue #3 “Seed-independent trivial collisions”, 12 July 2026 (closed issue). Peters' cancellation construction for algorithm v1 (crate 0.5.1) is reproduced in mechanism and transferred here to v0.3 with a new 17-byte witness that collides in all four SMHasher3 variants, including their full 128-bit outputs. The same pairs collide for every seed on upstream v0.4 (crate 0.4.0, 24 July 2025), the last release before the v1 rewrite. Upstream moved to algorithm v2 (crate 0.6.0, 13 July 2026), whose tail products XOR in the seed, and its changelog deprecates every earlier version; against v2 the same pairs gave 0 collisions in 224seeds on all four APIs (a sample, not a bound; the v0.3 mechanism does not apply). v1 (crate 0.5.1, three days in July 2026) is also not affected by these particular pairs (0/224), although it has Peters' seed-free tail and its own pairs. This witness concerns the v0.3 code SMHasher3 still measures. Thecurrent README (3f0d8c8, line 82)states: “To keep a simple interface, MuseAir relies solely on an initial seed, without any additional secret; this makes it unsuitable for direct use on servers—it is more susceptible than other hashes in such environments.” It also claims “Not vulnerable to blinding multiplication attacks that hinder public use (which affect wyhash and rapidhash)” and “passed all SMHasher3 tests”. The historical claim quoted here was dropped in v0.4. The v0.3 score is version-bound; current v2 has a separate32-byte witness at 19.45 bits.

Selected score (MuseAir v0.3): ≤ 1.59 bits.17/17 bytes;L = 3. 1 (every seed). SeeThe collision score.

Try it in the browser
Load on view

Waiting to validate the verification program.

Run verify/museair locally

Records:Original project & code·Verifier package·Measurements

### MuseAir v2 (crate 0.6.0)

The current algorithm mixes the seed into the tail products, closing the earlier every-seed construction. A new 32-byte pair still collides when the multiplication carries match a fixed pattern.

Claim excerpt.Thecurrent README (3f0d8c8)says “Not vulnerable to blinding multiplication attacks that hinder public use (which affect wyhash and rapidhash)” and “passed all SMHasher3 tests”. Its single-seed interface has no additional secret; line 82 explicitly calls it unsuitable for direct use on servers. The key model here ismuseair::hash(bytes, seed)with a uniform 64-bit seed. The v0.3 row retains its separate 1.59-bit result.

/* Hex encodes bytes in memory order. */
M = hex("0000000000000000000000000000000000000000000000000000000000000000");
M' = hex("00000000000000404a048402a910048a00000000000000a80000000000000000");
/* API seed */
0x040963434fe5e368
/* H(M) = H(M') = 0xef46cda19c0bbc67 */

For 17–32 bytes the tail enters aswmul(C4 XOR seed XOR u, C5). Flip bits 59, 61 and 63 of u, and XOR4000000000000000and8a0410a90284044ainto the head words. The signed-digit change shifts the tail product by ±21·C5 (carry weight 16); when its XOR image matches the fixed head pattern, the changes cancel. The example seed040963434fe5e368givesef46cda19c0bbc67for both strings. Seed 0 does not collide.

The independent verifier linked to crate 0.6.0 found 23,869/232and 12,191/231hits. Their pooled rate is ε = 36,060/(1.5·232) ≈ 2−17.447. Thus log₂(4/ε) ≈19.45 bits, 95% interval [19.43, 19.46]. The searcher’s independent C port agrees. This is a measured cap, not a global optimality claim. Verifier package.

bfast::hashcollides on the same seeds. The 128-bit functions have the same measured rate under their separate two-seed model; that does not change the single-seed model scored here. The v0.3 every-seed pair yields 0/224on v2. The chart uses the separate MuseAir-v2 registration and timings, validated against the crate and this witness. The registration maps the uniform 64-bit seed directly to the standard v2 hash. The old MuseAir registration remains v0.3.

Selected score (MuseAir v2 (crate 0.6.0)): ≈ 19.45* bits.32/32 bytes; L = 4. about 2^-17.45 of keys (sampled; 36,060 events / 1.5×2^32 keys, upstream crate). SeeThe collision score.

Reproduction.Standalone C and upstream Rust package. Thev2 follow-up in issue #4, posted on 19 September 2026, reports this pair and its measured rate separately from the older v0.3 results.

Records:Original project & code·Verifier package·Measurements

### komihashpattern:P4

Two message changes exploit a known relationship between parallel calculations. They collide for about 91% of sampled seeds at the studied lengths, even though the attacker chooses the messages first.

IVAL1, E = 55…55

public

IVAL5, O = aa…aa

public

UseSeed

& E; ⊕ IVAL1

& O; ⊕ IVAL5

public

public

×

lo ⊕ B

hi + old s5

A = preseeded s1

B = preseeded s5

Four parallel message lanes · one 64-byte block

lane 0

w0 [0..7]

0 → 1

w4 [32..39]

×

⊕

⊕

A

B

lo

hi; + s5

lane 1

w1 [8..15]

w0 ⊕ IVAL2

w5 [40..47]

w4 ⊕ IVAL6

×

⊕

⊕

A ⊕ IVAL2 public

B ⊕ IVAL6 public

lo

hi; + s6

lane 2

w2 [16..23]

w6 [48..55]

×

⊕

⊕

A ⊕ IVAL3 public

B ⊕ IVAL7 public

lo

hi; + s7

lane 3

w3 [24..31]

w7 [56..63]

×

⊕

⊕

A ⊕ IVAL4 public

B ⊕ IVAL8 public

lo

hi; + s8

Within each message: P0 = P1, with high half H

⊕

⊕

lo0

lo1

s5

s6

lo0 ⊕ lo1 = 0

(B+H) ⊕ ((B⊕IVAL6)+H)

High-fold equality depends on H and addition carries.

On success, both folded s1 and s5 agree.

komihash’s public lane offsets let the first two products match, so their low halves cancel and only the related high-half additions can retain the pair’s difference.

01
// Input: M[64]; secret UseSeed (64 bits); public IVAL constants:

02
const I[8] = {0x243f6a8885a308d3, 0x13198a2e03707344,

03
 0xa4093822299f31d0, 0x082efa98ec4e6c89,

04
 0x452821e638d01377, 0xbe5466cf34e90c6c,

05
 0xc0ac29b7c97c50dd, 0x3f84d5b5b5470917};

06
s1 = I[0] ^ (UseSeed & 0x5555555555555555);

07
s5 = I[4] ^ (UseSeed & 0xaaaaaaaaaaaaaaaa);

08
(lo, hi) = mul128(s1, s5); s5 += hi; s1 = lo ^ s5; // Preseed.

09
s2 = I[1] ^ s1; s3 = I[2] ^ s1; s4 = I[3] ^ s1;

10
s6 = I[5] ^ s5; s7 = I[6] ^ s5; s8 = I[7] ^ s5;

11
(s1, hi) = mul128(read64le(M, 0) ^ s1, read64le(M, 32) ^ s5); s5 += hi;

12
(s2, hi) = mul128(read64le(M, 8) ^ s2, read64le(M, 40) ^ s6); s6 += hi;

13
// Exploit: the first two products are identical within each message.

14
(s3, hi) = mul128(read64le(M, 16) ^ s3, read64le(M, 48) ^ s7); s7 += hi;

15
(s4, hi) = mul128(read64le(M, 24) ^ s4, read64le(M, 56) ^ s8); s8 += hi;

16
s4 ^= s7; s1 ^= s8; s2 ^= s5; s3 ^= s6;

17
s5 ^= s6 ^ s7 ^ s8; s1 ^= s2 ^ s3 ^ s4; // Fold immediately after one block.

18
r1 = (((read64le(M, 56) >> 8) | (u64(1) << 56)) >> 56) ^ s1;

19
r2 = s5; // Empty tail: r1 = 1 ^ s1 (padding bit).

20
(lo, hi) = mul128(r1, r2); s5 += hi; s1 = lo ^ s5;

21
(lo, hi) = mul128(s1, s5); s5 += hi; s1 = lo ^ s5;

22
return s1;

Code:komihash/komihash.h, v5.34;SMHasher3 hashes/komihash.cpp, v5.27 core; tested at SMHasher3 commit7ad8939d; local copy:sources/komihash.h(v5.34). Excerpt: IVAL constants, kh_m128, HASHLOOP64, komihash_epi and preseeding, source lines 117–124, 646–710, 728–804 and 928–974. Rechecked against SMHasher3 3b619371 (hashes/komihash.cpp unchanged since 84f77218, 2025-08-28; results run 7ad8939d) and upstream komihash 50a15150 (tag 5.34, 2026-08-04, newest release as of 2026-09-18).

After preseeding inlines 6–8, the long-input path constructs additional lane states (lines 9–10) by XORing public constants into the resulting secret words. The message can compensate for those same constants. For the displayed pair, two lanes perform identical products (lines 11–12) within each message. Their low halves cancel in the XOR fold inlines 16–17. Flipping the selected bits changes the common high product by at most one; often it does not change at all, and many remaining cases cancel through the additions as well.

komihash — NEW.The selected pair differs in just the low bit of two words:

/* Hex encodes bytes in memory order, not hexadecimal integers. */
A = hex("0000000000000000447370032e8a191311111111111111112222222222222222"
 "f0f9dda4c1c0a15e9cf534900ea6f5e033333333333333334444444444444444");
B = hex("0100000000000000457370032e8a191311111111111111112222222222222222"
 "f0f9dda4c1c0a15e9cf534900ea6f5e033333333333333334444444444444444");

/* Example seed: */
0x27d1f77dc2a01269
/* H(A) = H(B), selected 64-bit output: 0x113c6b88bc913857 */

Length and word difference.64 and 64 bytes;L = 8. Zero-based little-endian words are shown below; a final partial word is zero-extended only for displaying the difference, not for the hash input.

w[0]: 0x0000000000000000 -> 0x0000000000000001 (XOR 0x0000000000000001)
w[1]: 0x13198a2e03707344 -> 0x13198a2e03707345 (XOR 0x0000000000000001)

I measured a rate of about 0.9106 over uniform 64-bit seeds. The large recorded run found 3,910,946,997 collisions in232trials; the second model family independently measured 0.9106. Randomizing the ordinary API seed leaves this result intact.

The second-family check found 15,277,062 collisions in 224seeds, about 91.06%. I report the integer count to make the measurement reproducible. An earlier independent check of the untuned variant (common word m4 = 0) measured 0.8990 over 230seeds, which is the rate before tuning m4 to the bias of the seeded state.

The ordinary seed expansion makes the relevant high state nonuniform. Tuning the common message word exploits that distribution and raises the rate. Seed-dependent operands still expose relations when lanes inherit public differences. An attacker can arrange related operands without calculating their secret values.

The 0.9106 result applies to this construction at lengths 64 through 127 bytes only, with identical suffixes. At those lengths, the lanes fold immediately after the first large block. At 128 bytes, another block processes the still-distinct lanes before that fold. I found no collisions there: 0 in 224seeds for this pair (one-sided 95% bound about 2-22.4), 0 in 220seeds for the same pair at 128, 192, 256 and 1000 bytes, and 0 in each of 816 generic single- and double-word differences at 128 bytes with 222seeds per cell (about 2-20per cell). This proves nothing beyond those bounds. This gives no proof of zero collision probability and no bound for arbitrary longer inputs. The SMHasher3 v5.27 core and the checked v5.34 implementation agree for this analysis.

Reproduction. Following verify/Reproduction documentation, run in verify/komihash/:

cc -O2 -std=c11 -o komihash_pair komihash_pair.c -lm
./komihash_pair # 2^24 seeds, 0.3-0.7 s on an Apple M2 Pro

New. I am not aware of an earlier published lane-tie construction for komihash: the komihash issue tracker (searched 2026-09-18) and the SMHasher3 results report no fixed-pair, hidden-seed collision; the pair was disclosed upstream as avaneev/komihash issue #23on 2026-09-18.

Selected score (komihash v5.27 / v5.34): ≈ 3.14* bits.64/64 bytes;L = 8. 0.9106 measured. SeeThe collision score.

Try it in the browser
Load on view

Waiting to validate the verification program.

Run verify/komihash locally

Records:Original project & code·Verifier package·Measurements

### SpookyHash V2pattern:P7

The hash adds the message tail just before final mixing. Carefully chosen tail changes can cancel an earlier difference for about half of sampled seeds; the exact one-half claim is not proved.

12-word state at initialization

same seed → native seed0

s0

seed

s3

seed

s6

seed

s9

seed

same seed → native seed1

s1

seed

s4

seed

s7

seed

s10

seed

C = deadbeefdeadbeef · public

s2

C

s5

C

s8

C

s11

C

Mix(M[0..95]); then Mix(M[96..191])

w23 · bytes 184..191

Δ = 2⁶³

+ into s11, late in Mix

s11 before rotl

⊕; + s0 → s10

rotl 46

s10: Δ = 2⁶³

s11: δ = ±2⁴⁵

w34 · bytes 272..279

tail change 2⁶³

w35 · bytes 280..285

tail change −2⁴⁵

End: + tail[10]

End: + tail[11]

cancels here

cancels if δ = +2⁴⁵

equal s10

equal s11

Other ten words and the length byte are common.

All twelve words agree before EndPartial × 3.

The sign condition is measured, not proved balanced.

SpookyHash V2’s unmixed End additions cancel the late block difference in s10 and s11 for the successful sign, merging all twelve state words.

01
// Input: M[286] (the earlier supporting pair; the scored 275-byte witness applies the same trail one Mix step earlier); secret seed; Hash64 uses it for both native seed words.

02
const C = 0xdeadbeefdeadbeef; // Public initialization constant.

03
void Mix(byte *p) { // s0..s11 alias state words s[0]..s[11].

04
 s0 += read64le(p,0); s2 ^= s10; s11 ^= s0; s0 = rotl(s0,11); s11 += s1;

05
 s1 += read64le(p,8); s3 ^= s11; s0 ^= s1; s1 = rotl(s1,32); s0 += s2;

06
 s2 += read64le(p,16); s4 ^= s0; s1 ^= s2; s2 = rotl(s2,43); s1 += s3;

07
 s3 += read64le(p,24); s5 ^= s1; s2 ^= s3; s3 = rotl(s3,31); s2 += s4;

08
 s4 += read64le(p,32); s6 ^= s2; s3 ^= s4; s4 = rotl(s4,17); s3 += s5;

09
 s5 += read64le(p,40); s7 ^= s3; s4 ^= s5; s5 = rotl(s5,28); s4 += s6;

10
 s6 += read64le(p,48); s8 ^= s4; s5 ^= s6; s6 = rotl(s6,39); s5 += s7;

11
 s7 += read64le(p,56); s9 ^= s5; s6 ^= s7; s7 = rotl(s7,57); s6 += s8;

12
 s8 += read64le(p,64); s10 ^= s6; s7 ^= s8; s8 = rotl(s8,55); s7 += s9;

13
 s9 += read64le(p,72); s11 ^= s7; s8 ^= s9; s9 = rotl(s9,54); s8 += s10;

14
 s10 += read64le(p,80); s0 ^= s8; s9 ^= s10; s10 = rotl(s10,22); s9 += s11;

15
 s11 += read64le(p,88); s1 ^= s9; s10 ^= s11; s11 = rotl(s11,46); s10 += s0;

16
} // Exploit: last word enters very late.

17
s0 = s3 = s6 = s9 = seed; s1 = s4 = s7 = s10 = seed;

18
s2 = s5 = s8 = s11 = C;

19
Mix(M); Mix(M + 96); // Two complete 96-byte blocks.

20
byte tail[96] = {0}; copy(tail, M + 192, 94); tail[95] = 94;

21
for (i = 0; i < 12; ++i) s[i] += read64le(tail, 8*i); // V2 tail cancellation.

22
// Complete states agree here for the successful seeds, before final mixing.

23
EndPartial(s); EndPartial(s); EndPartial(s); // Unchanged source finalizer.

24
return s0; // Native 128-bit output is words(s0,s1).

Code:SpookyHash;SMHasher3 hashes/spookyhash.cpp, V2; tested at SMHasher3 commit7ad8939d; local copy:sources/spookyhash.cpp. Excerpt: Mix, End, Hash128 and the seeded wrapper, source lines 88–159 and 307–347.

The late change in the last fully mixed block (line 15) becomes a top-bit difference in one state word and a signed difference in another. V2 then adds the tail directly (lines 20–21) before its final mixing. Two tail changes cancel those state differences for one sign. For the other sign, a related pair makes the complementary cancellation.

SpookyHash V2 — NEW.A longer literal input makes the mechanism easier to see. B is A with three specified byte changes:

/* A is the concatenation of these hex byte strings, without a NUL. */
A = hex(
 "a0ed1dcaeb2e421c17cf8516645510b61c1e80eb014c077fdbb3b3ab867298f2"
 "ccfb12c325d96dd09c3de65c247a0257a6d22a9da89710cfb724db191c748806"
 "e9d6b0272f125818a2c061b9e406999b788261dcd2487f7064e1bf4d00670a3d"
 "09230d92b37de4141a5e5d12e205c37e42c13193ab064833476cb9e5a22bd74c"
 "85073313646062ca36b300b4a62fa6797864ca181b97739bf4dd0567f5ce9a24"
 "398e0ddb544ee4926c6c033f6397e4790f51641c3d6dc04d5dcfe95ffe305426"
 "2ff9e5d8a8f17cce6b3c565acbecc693b77d90b1564fd1ddc71df2c56f2fd52f"
 "d6d8c9fb3b84612e5f83397bb5ac932651ce382aa90592ebb81d61c29ac53c2b"
 "ace0711020c947c1ce55f2cfd79f821e92ba90562ba05eeab1b8f0771534"
);
/* B starts as A. Offsets are zero-based bytes. */
memcpy(B, A, 286);
B[191] ^= 0x80;
B[279] ^= 0x80;
B[285] &= ~0x20;

/* Example seed: */
0x0000000000000004
/* H(A) = H(B), selected 64-bit output: 0xe3f63e3f415763ac */
Complete pair as literal hex bytes
A = hex(
 "a0ed1dcaeb2e421c17cf8516645510b61c1e80eb014c077fdbb3b3ab867298f2"
 "ccfb12c325d96dd09c3de65c247a0257a6d22a9da89710cfb724db191c748806"
 "e9d6b0272f125818a2c061b9e406999b788261dcd2487f7064e1bf4d00670a3d"
 "09230d92b37de4141a5e5d12e205c37e42c13193ab064833476cb9e5a22bd74c"
 "85073313646062ca36b300b4a62fa6797864ca181b97739bf4dd0567f5ce9a24"
 "398e0ddb544ee4926c6c033f6397e4790f51641c3d6dc04d5dcfe95ffe305426"
 "2ff9e5d8a8f17cce6b3c565acbecc693b77d90b1564fd1ddc71df2c56f2fd52f"
 "d6d8c9fb3b84612e5f83397bb5ac932651ce382aa90592ebb81d61c29ac53c2b"
 "ace0711020c947c1ce55f2cfd79f821e92ba90562ba05eeab1b8f0771534"
);
B = hex(
 "a0ed1dcaeb2e421c17cf8516645510b61c1e80eb014c077fdbb3b3ab867298f2"
 "ccfb12c325d96dd09c3de65c247a0257a6d22a9da89710cfb724db191c748806"
 "e9d6b0272f125818a2c061b9e406999b788261dcd2487f7064e1bf4d00670a3d"
 "09230d92b37de4141a5e5d12e205c37e42c13193ab064833476cb9e5a22bd74c"
 "85073313646062ca36b300b4a62fa6797864ca181b97739bf4dd0567f5ce9a24"
 "398e0ddb544ee4926c6c033f6397e4790f51641c3d6dc04d5dcfe95ffe3054a6"
 "2ff9e5d8a8f17cce6b3c565acbecc693b77d90b1564fd1ddc71df2c56f2fd52f"
 "d6d8c9fb3b84612e5f83397bb5ac932651ce382aa90592ebb81d61c29ac53c2b"
 "ace0711020c947c1ce55f2cfd79f821e92ba90562ba05e6ab1b8f0771514"
);

Length and word difference.286 and 286 bytes;L = 36. Zero-based little-endian words are shown below; a final partial word is zero-extended only for displaying the difference, not for the hash input.

w[23]: 0x265430fe5fe9cf5d -> 0xa65430fe5fe9cf5d (XOR 0x8000000000000000)
w[34]: 0xea5ea02b5690ba92 -> 0x6a5ea02b5690ba92 (XOR 0x8000000000000000)
w[35]: 0x0000341577f0b8b1 -> 0x0000141577f0b8b1 (XOR 0x0000200000000000)

I measured collisions for about half of seeds. The shipped run verify/spookyhash2-64/run_226.log gives 33,552,409/226= 0.49997 (and run_224.log 8,387,160/224); the independent verifier counted 536,879,630/1,073,741,823 at 230; an exact balance proof over the complete seed domain is missing. The second-family verifier confirmed the example and cancellation argument but marked the stronger exact-half claim INCONCLUSIVE. I cannot assume that an internal bit is balanced without analysing its dependence on the seed.

The collision occurs in the complete state entering finalization, so the full 128-bit result also agrees. Independent native seed-word runs have also been reproduced; their counts are given with the selected 275-byte pair below. Bob Jenkins alreadywarns against using SpookyHash when there is an opponent; this pair illustrates that warning. This earlier 286-byte pair hasL = 36and a score near 6.17; the selected shorter pair below gives 6.13.

Selected 275-byte witness.The same late-injection mechanism one Mix step earlier reduces L from 36 to 35. In block 2, word 10 gains263; End words 1 and 9 also gain263, and End word 10 loses221. These cancel the full 768-bit state difference for approximately half the duplicated 64-bit seeds. Exact balance is unproved.

M = hex("9d21a7fafac0e24f428e3c0124de5f8c54c1de8bef8535a636cfd97be5aad365055fb9bc0a26d493c5f21f4acbfade067eba007efbf79f8729cacdc39c584138336a77d8330a62803d3750884eb91b907e091a0ff547078c45198f347078fe21b0fa47014d7d1cd6142861dadfecd7fd0bf71f80b4e9112d36a8d91996608d73c49284098d900d7ef1f9c16471246346ca2277cbf87725a6d861b0db4924da8f5c5307034eb3933fcca647e8404e141afc956d0eb643e7ee9381dabba3c2d09e2dae44a4bda150f889d0704a2463cd7cb2b194ea3ccc9982ceae11e212336b6b3ad81125bd494e3f1b7291e3b0c73a74fa886a41f0fe25055b0f1fc96e8f7c0123002a69c35989a703b718ce8a1bfbddafb3e3")
M' = hex("9d21a7fafac0e24f428e3c0124de5f8c54c1de8bef8535a636cfd97be5aad365055fb9bc0a26d493c5f21f4acbfade067eba007efbf79f8729cacdc39c584138336a77d8330a62803d3750884eb91b907e091a0ff547078c45198f347078fe21b0fa47014d7d1cd6142861dadfecd7fd0bf71f80b4e9112d36a8d91996608d73c49284098d900d7ef1f9c16471246346ca2277cbf87725a6d861b0db4924da8f5c5307034eb3933fcca647e8404e141afc956d0eb643e76e9381dabba3c2d09e2dae44a4bda150f889d0704a2463cdfcb2b194ea3ccc9982ceae11e212336b6b3ad81125bd494e3f1b7291e3b0c73a74fa886a41f0fe25055b0f1fc96e8f7c0123002a69c35989a703b718ce8a1bfb5dafb3c3")
// 275 bytes each; h1 = h2 = seed = 0
H32(M) = H32(M') = 0x9ecef355
H64(M) = H64(M') = 0x6d1347279ecef355
// Second 64-bit output word: 0x147d4b759d34be02 on both sides.

The independent verifier found 536,875,475/1,073,741,823 collisions at all three widths, giving an estimated score cap of 6.13. The same pair collides on SpookyHash2-32 at the same measured rate. Native Hash32 uses a 32-bit seed; this measurement uses SMHasher3's duplicated 64-bit seed. The claimed 232run was not independently reproduced. The independent-seed-word rate (h1, h2 uniform) is reproduced for both pairs: 275-byte pair 134,213,174/228(shipped verify program) and 134,214,618/228and 134,222,222/228(two harnesses on the reference SpookyV2.cpp); 286-byte pair: 8,391,186/224(shipped run_2^24_mode1.log). The supplied package now checks this pair alongside the earlier 286-byte pairs. Record and caveats.

Reproduction.From the supplied Reproduction documentation, run inverify/spookyhash2-64/:

cc -O2 -std=c11 -o spookyhash2_64_pair spookyhash2_64_pair.c -lm
./spookyhash2_64_pair # 2^24 uniform seeds, h1 = h2 = seed (SMHasher3's seeding), ~4 s

New.The supplied record identifies this late-injection cancellation as new.

Selected score (SpookyHash V2-64): ≈ 6.13* bits.275/275 bytes;L = 35. about half the seeds; verifier 536875475/1073741823. SeeThe collision score.

Try it in the browser
Load on view

Waiting to validate the verification program.

Run verify/spookyhash2-64 locally

Records:Original project & code·Verifier package·Measurements

### aHashpattern:ungrouped

Claim excerpt.“designed to prevent an adversary that does not know the key from being able to create hash collisions or partial collisions.”The result below uses four independent uniform RandomState words and hashes a byte slice, including its length.

This example requires differences to cancel in two internal calculations at once. Its measured rate uses independently random internal key words in the checked reproduction, so transferring it to a Rust application requires checking the key setup too.

Two accumulators · independent RandomState keys

k0, k1

k2, k3

key enters

key enters

enc

sum

SHUF · public

byte permutation

see line 2

After common hash_in((56,0)) and enc.lo += 56

w0, w1

bytes 0..15

enc

sum

AESDEC

SHUF

⊕ v

+ v

w2, w3

bytes 16..31

enc

sum

AESDEC

SHUF

⊕ v

+ v

w3, w4

bytes 24..39

enc

sum

AESDEC

SHUF

⊕ v

+ v

w5, w6

bytes 40..55

enc

sum

AESDEC

SHUF

⊕ v

+ v

cancels here

w3 (bytes 24..31) enters twice, unchanged.

Both trails must cancel for the same key.

equal enc

equal sum

same finalizer input

aHash’s pair must cancel both the inverse-AES difference and the shuffled-addition difference, including the repeated read of bytes 24–31, before finalization.

01
// Input: M[56]; secret k[4] = four independent 64-bit RandomState words.

02
const SHUF[16] = {4,11,9,6,8,13,15,5,14,3,1,12,0,7,10,2}; // Public.

03
enc = words(k[0], k[1]); sum = words(k[2], k[3]); key = enc ^ sum;

04
void hash_in(block v) {

05
 enc = aesdec(enc, v); // Exploit: inverse-AES differential.

06
 sum = shuffle_bytes(sum, SHUF); // Output byte i = input byte SHUF[i].

07
 sum.lo += v.lo; sum.hi += v.hi; // Exploit also needs sum cancellation.

08
}

09
len = 56;

10
hash_in(words(len, 0)); enc.lo += len; // Both source length injections.

11
hash_in(words(read64le(M, 0), read64le(M, 8)));

12
hash_in(words(read64le(M, 16), read64le(M, 24)));

13
hash_in(words(read64le(M, len-32), read64le(M, len-24))); // Offsets 24,32.

14
hash_in(words(read64le(M, len-16), read64le(M, len-8))); // Offsets 40,48.

15
// Bytes 24..31 are read twice; both enc and sum must merge.

16
combined = aesenc(sum, enc); previous = combined;

17
combined = aesdec(combined, key);

18
combined = aesdec(combined, previous);

19
return combined.lo;

Code:aHash;SMHasher3 hashes/rust-ahash.cpp, aHash 0.8 AES + fallback (selected row: 0.8.12, AES path); tested at SMHasher3 commit7ad8939d; local copy:sources/rust-ahash.cpp. Excerpt: from_random_state, hash_in, add_data and finish, source lines 125–138, 202–231 and 310–361. The port is unchanged at SMHasher3 3b619371 (2026-08-27) and follows aHash master 4b73276 (2025-06-20, Cargo.toml 0.8.10), whose AES core is byte-for-byte the v0.8.12 core; native Rust v0.8.12 and master a9d649d runs confirm. Reported upstream astkaitchuck/aHash#292on 2026-09-18.

The construction combines a differential through the inverse-AES operations inline 5with cancellation in the shuffled-addition accumulator inlines 6–7. The four message blocks inlines 11–14include an overlapping read at bytes 24–31. Both accumulators must agree before finalization; success in only the AES component would not be enough. The key words inline 3are independent RandomState words, so this construction does not depend on SMHasher3’s correlated scalar-seed expansion.

aHash AES path — NEW.The selected 424-byte pair E is all zero bytes except ten:

byte 24 25 26 27 280 344 345 346 347 384
M 7c 06 7e 7b 08 80 08 82 80 03
M' 81 08 81 80 03 7d 06 7d 7b 08
/* Hex encodes bytes in memory order. */
M = hex("0000000000000000000000000000000000000000000000007c067e7b000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000080000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000008008828000000000000000000000000000000000000000000000000000000000000000000000000003000000000000000000000000000000000000000000000000000000000000000000000000000000");
M' = hex("00000000000000000000000000000000000000000000000081088180000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000007d067d7b00000000000000000000000000000000000000000000000000000000000000000000000008000000000000000000000000000000000000000000000000000000000000000000000000000000");
/* Internal RandomState words (API arguments = these XOR PI2) */
0x0e17425e994c2579 0x4e057e193aec29dc 0x665cc79160d3c675 0x3d80ed4ec94cfe49
/* H(M) = H(M') = 0x93ecf09ded4decc5 */

Length.424 and 424 bytes;L = 53. For inputs longer than 64 bytes aHash runs four AES lanes and two additive lanes: the last 64 bytes seed them, then each 64-byte block is folded in with oneaesdecper lane and one shuffle-and-add per additive lane. E is a two-S-box “lane echo” in lane 1. The tail (byte 384) puts a one-byte difference into the lane when the lanes are seeded; the first loop block (bytes 24–27, the InvMixColumns column of one inverse-S-box output) cancels it through a single S-box at difference-table entry 4/256; the fifth block (byte 280) injects a second one-byte difference and the sixth (bytes 344–347) cancels it the same way. The additive lane still carries the five byte differences of the first cancellation, but a byte difference survives the shuffle and an addition of zero, so they travel until they land on the five bytes of the second cancellation and cancel additively. Two S-boxes at 4/256 plus small carry terms give the measured rate. The independent upstream-crate verifier measured 967,503 collisions in 232keys: ε ≈ 2−12.116. Thus log₂(53/ε) ≈17.84 bits, with a 95% interval [17.84, 17.85]; the C reproduction gives 3,783/224. The pair needs the four key words to be independent: under SMHasher3’s correlated expansionwith_seeds(s,s,s,s)it did not collide in 224trials. A truncated-trail enumeration with a GF(28) feasibility filter finds no one-S-box trail and no two-S-box trail before six iterations, so within this family only about 0.2 bits of length remain.

The earlier selected pair, the 56-byte three-S-box A_2 whose trail the diagram above shows, is kept as the historical exhibit:

/* Hex encodes bytes in memory order. */
M = hex("22313233343536373839263b3c3d3e3f407b42404445464748494a4b4c4d4e4f0df97e025c5d5e5f606162636465666768696a6b6c6d6e6f");
M' = hex("1f313233343536373839343b3c3d3e3f406d422f4445464748494a4b4c4d4e4fff098d055c5d5e5f606162636465666768696a6b6c6d6e6f");
/* Internal RandomState words (API arguments = these XOR PI2) */
0xec6baf58f9a18793 0xb5e2ee792117d0ff 0x893c786e1e8196a8 0xa4edbe691f677fb2
/* H(M) = H(M') = 0x21a01e6ddf40c84a */

A_2 length and word difference.56 and 56 bytes;L = 7. Zero-based little-endian words are shown below; a final partial word is zero-extended only for displaying the difference, not for the hash input.

w[0]: 0x3736353433323122 -> 0x373635343332311f (XOR 0x000000000000003d)
w[1]: 0x3f3e3d3c3b263938 -> 0x3f3e3d3c3b343938 (XOR 0x0000000000120000)
w[2]: 0x4746454440427b40 -> 0x474645442f426d40 (XOR 0x000000006f001600)
w[4]: 0x5f5e5d5c027ef90d -> 0x5f5e5d5c058d09ff (XOR 0x0000000007f3f0f2)

Pair A_2 uses the same three-S-box inverse-AES trail as the earlier pair: active bytes {0,10} become {1,3}, then bytes 32–35 cancel the remaining difference. The additive-lane differences (3, −14, 14, 17) reduce the carry loss from about 0.69 to 0.38 bits. The two cancellations must succeed together. The independent upstream-crate verifier measured 12,627 collisions in 233keys: ε ≈ 2−19.376. Thus log₂(7/ε) ≈22.18 bits, with a 95% interval [22.16, 22.21]. A fresh native run found 3,124/231; the C searcher found 3,178/231.

Those experiments draw all four RandomState words independently. They do not rely on SMHasher3’s correlated expansion of one scalar seed. The package also reproduces collisions in aHash’s multiply-based fallback, but reports a rate discrepancy with the earlier record; that result remains outside the table.

Reproduction.From the supplied Reproduction documentation, run inverify/rust-ahash/:

cc -O2 -DAHASH_SOFT_AES -o ahash_pairs ahash_pairs.c -lm
./ahash_pairs # 2^24 secrets per model, rng seed 1

TheNEWlabel here concerns this fixed-pair AES differential: Peters’2023 side-channel key-recovery attackis earlier work under a different attack model, fixed in 0.8.4.

Selected score (aHash 0.8.12, AES path): ≈ 17.84* bits.424/424 bytes; L = 53. about 2^-12.12 of keys (sampled; 967,503 events / 2^32 keys, native Rust crate 0.8.12). SeeThe collision score.

Try it in the browser
Load on view

Waiting to validate the verification program.

Run verify/rust-ahash locally

Rust transfer.The native program uses crate 0.8.12 with the x86 AES feature andRandomState::hash_one(&[u8]):write_usize(len), thenwrite(bytes).RandomState::with_seedsXORs each argument with its corresponding public PI2 word, a bijection on four independent uniform words. For the displayed internal key, its public API arguments area9438ebec17194e4 0bb688b615fedc93 499051d9d7fdc675 9b696bdcaa2076a5. Both outputs are21a01e6ddf40c84a, as recorded in the upstream verifier log. Other key types, write sequences and backends require separate checks. In crate 0.8.12, ARM AES additionally requiresnightly-arm-aes.

Among the 56-byte three-S-box pairs, A_1 is statistically tied with A_2 and the 64-byte mirror B_0 has a similar rate at L = 8 (a 22.38-bit cap); the enumeration shows three S-boxes is the minimum below 65 bytes, which is why the lane echo above 64 bytes wins. The19 September update to issue #292reported A_2; the20 September updatereports E.

Records:Original project & code·Design & FAQ·Verifier package·Measurements

### t1ha2pattern:P7

Claim excerpt.“Great quality of hashing”; cryptographic suitability is disclaimed. The key model is one uniform 64-bit API seed, with the two byte strings fixed before the seed is drawn.

A 13-byte input and a 16-byte input can reach the same result when the arithmetic carries line up. The analysis counts the relevant kind of seed and measures how often the remaining cancellation succeeds.

w0 · bytes 0..7

operand: len + w0

P2 · public prime

×

+ len; ×

× P2

seed

seed enters

lo; ⊕

hi; + len

a = seed ⊕ lo

b = len + hi

w1 · bytes 8..15

or bytes 8..10

zero-extended

P1 · public prime

+ w1

×

a + w1

× P1

lo; b ⊕=

hi; a +=

b after second mix

a after second mix

cancels here when both carry conditions hold

The common finalizer starts from the same (a, b).

t1ha2’s public first product and seeded second product cancel in both state words for the successful carry patterns of the selected seed class.

01
// Input: M[len], 9 <= len <= 16; secret seed (64 bits).

02
const P0 = 0xec99bf0d8372caab, P1 = 0x82434fe90edcef39; // Public.

03
const P2 = 0xd4f06db99d67be4b, P5 = 0xc060724a8424f345;

04
const P6 = 0xcb5af53ae3aaac31;

05
a = seed; b = len; // Byte length enters the state.

06
w0 = read64le(M, 0);

07
w1 = read_le_zero_extended(M + 8, len - 8); // 5 or 8 bytes in this pair.

08
(lo, hi) = mul128(b + w0, P2); // First product is public.

09
a ^= lo; b += hi;

10
(lo, hi) = mul128(a + w1, P1); // Exploit: carries in this seeded product.

11
b ^= lo; a += hi; // mixup64(&b, &a, w1, P1).

12
x = (a + rotl(b, 23)) * P0; // Source rotr(b, 41).

13
y = (rotl(a, 41) + b) * P6; // Source rotr(a, 23).

14
return fold(x ^ y, P5);

Code:t1ha;SMHasher3 hashes/t1ha.cpp, t1ha2_atonce v2.1.4; tested at SMHasher3 commit7ad8939d; local copy:sources/t1ha.cpp. Excerpt: constants, mixup64, final64, T1HA2_TAIL and t1ha2, source lines 180–186, 748–760, 800–862 and 1144–1180. The upstream t1ha core is unchanged from tag v2.1.4 through commit 00eb779 (2025-02-15); the GitHub mirror is archived and the primary repository is now GitFlic.

Both messages take the short path in lines 5–11. The public first product and seeded tail product cancel for a signed-digit difference +260+ 254− 248− 29− 21. The selected F60 pair has 13 and 16 bytes, L = 2. Putl0 = lo((len + w0) · P2),t = tailandLseed = lo(((seed XOR l0) + t) · P1). The sufficient class is(Lseed & a5845081f808f44a) == 2080000118003408. Since this map is bijective and fixes 24 bits, its density is exactly 2−24.

t1ha2-64 — NEW.The following pair uses different lengths:

/* Hex encodes bytes in memory order. */
M = hex("c4c0cc2284cd239ede36a18fa6");
M' = hex("fbc31866049ec02dea0c4e2be580d3cf");
/* API seed */
0x4c240c2749cd4915
/* H(M) = H(M') = 0xc35b49165b1a4480 */

Length and word difference.13 and 16 bytes; L = 2. Little-endian words, with the partial word zero-extended only for displaying the difference:

w[0]: 0x9e23cd8422ccc0c4 -> 0x2dc09e046618c3fb (XOR 0xb3e3538044d4033f)
w[1]: 0x000000a68fa136de -> 0xcfd380e52b4e0cea (XOR 0xcfd38043a4ef3a34)

The independent upstream verifier found 58,715,203 collisions in 230class samples. The measured class contribution is 2−24× 58,715,203/230≈ 2−28.1928, hence log₂(2/ε) ≈29.19 bits(conditional-rate 95% uncertainty about ±0.0004 bits). This is a sampled sufficient contribution, not a proof of total equality. Two fresh uniform checks gave 226 and 258 hits per 236; the searcher found 217, all inside the class. The class-weighted estimate is the reported rate. This cross-length witness does not establish the same cap for an equal-length-only model.

Reproduction.From the supplied Reproduction documentation, run inverify/t1ha2-64/:

cc -O2 -std=c11 -o t1ha2_64_verify t1ha2_64_verify.c -lm
./t1ha2_64_verify # 2^24 seeds per experiment, rng seed 1 (about 1.3 s)

New.This carry-pattern construction is new in the supplied records.

Selected score (t1ha2_atonce-64 v2.1.4): ≈ 29.19* bits.13/16 bytes; L = 2. about 2^-28.19 of keys (sampled class contribution: 2^-24 × 58,715,203/2^30). SeeThe collision score.

Try it in the browser
Load on view

Waiting to validate the verification program.

Run verify/t1ha2-64 locally

Verifier package: all 224.9 million five-digit routes were enumerated; six-digit routes were not.

Records:Original project & code·Verifier package·Measurements

### a5hash-64pattern:P3

Some seeds turn one operand of a multiplication into zero. The other operand can then change without affecting the product, erasing the message difference.

Seed expansion · two 64-bit state words

K2 ⊕ 6615, O

public

K1 ⊕ 6615, E

public

UseSeed

⊕ (seed & O)

⊕ (seed & E)

public

public

×

lo

hi

s1

s2

v01 = E ⊕ s1; v10 = O ⊕ s2 (fixed)

w0 · bytes 0..7

32-bit halves swapped

matches s1 in class

w1 · bytes 8..15

32-bit halves swapped

changed in m′

⊕ w0

⊕ w1

×

w0 ⊕ s1 = 0

w1 ⊕ s2

difference dies at the zero product

lo = 0; + v01

hi = 0; + v10

equal s1 = v01

equal s2 = v10

The remaining 6599 message bytes are common.

a5hash-64 forgets the changed second message word when the nonuniform seed expansion makes the first message operand zero.

01
// Input: M[6615]; secret UseSeed (64 bits); all constants below public.

02
const K1 = 0x243f6a8885a308d3, K2 = 0x452821e638d01377;

03
const E = 0x5555555555555555, O = 0xaaaaaaaaaaaaaaaa;

04
len = 6615; p = M; n = len;

05
s1 = K1 ^ len; s2 = K2 ^ len; // Length injection before expansion.

06
(s1, s2) = mul128(s2 ^ (UseSeed & O), s1 ^ (UseSeed & E));

07
v01 = E ^ s1; v10 = O ^ s2; // Fixed through the input loop.

08
do {

09
 w0 = (read32le(p, 0) << 32) ^ read32le(p, 4);

10
 w1 = (read32le(p, 8) << 32) ^ read32le(p, 12);

11
 (s1, s2) = mul128(w0 ^ s1, w1 ^ s2); // Exploit: first w0 ^ s1 = 0.

12
 n -= 16; p += 16; s1 += v01; s2 += v10;

13
} while (n > 16);

14
// Here n = 7; source's >3-byte tail path, including overlapping reads:

15
mo = n >> 3;

16
s1 ^= (read32le(p, 0) << 32) | read32le(p, n - 4);

17
s2 ^= (read32le(p, mo*4) << 32) | read32le(p, n - 4 - mo*4);

18
(s1, s2) = mul128(s1, s2);

19
(s1, s2) = mul128(s1 ^ v01, s2);

20
return s1 ^ s2;

The “practically resistant” wording is from the main README at 10492db (19 December 2025), after tag 5.25. The tagged 5.21 and 5.25 READMEs instead say “practically secure against the "blinding multiplication" attack when the UseSeed is kept secret and hash outputs are not exposed”. Both conditions belong to the claim.

Code:a5hash;SMHasher3 hashes/a5hash.cpp, v5.21, 64-bit; tested at SMHasher3 commit7ad8939d; local copy:sources/a5hash.cpp. Excerpt: a5hash, source lines 33–34 and 64–130. The tested port is a5hash upstream commit b0ba799 (v5.21). The latest release, v5.25, changes only macros and comments; the pair, the class count (118 x 219seeds) and every class collision were re-checked against the v5.25 header, which reproduces SMHasher3's verification value; SMHasher3 HEAD (3b619371, 2026-08-27) still ships v5.21.

Inlines 5–6, the initial state is derived by multiplying two words that contain alternating bits of the seed and length-dependent constants. The low half of that product is not uniformly distributed. For this length, one particular state value has 118 ×219preimage seeds. Making the first input operand match that state value zeroes the first multiplication inline 11. The other operand’s message bytes are then forgotten, so the two differing heads reach the same state.

a5hash-64 v5.21 — NEW.The best verified score in the follow-up records comes from an awkward length: 6615 bytes. Here is an exact recipe; indices are absolute byte offsets:

/* Exactly 6615 bytes; zero-based indices. */
unsigned char A[6615], B[6615];
for (size_t i = 0; i < 6615; ++i) A[i] = B[i] = (7*i + 3) & 255;
/* Replace the first 16 bytes by these literal byte strings: */
A[0..15] = hex("e0aa5c8e000000008877665544332211");
B[0..15] = hex("e0aa5c8e000000001122334455667788");

/* Example seed: */
0xbdd730a20c451ba4
/* H(A) = H(B), selected 64-bit output: 0x9cda28706bf2e550 */
Complete pair as literal hex bytes
A = hex(
 "e0aa5c8e000000008877665544332211737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dd"
);
B = hex(
 "e0aa5c8e000000001122334455667788737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dde4ebf2f900070e151c"
 "232a31383f464d545b626970777e858c939aa1a8afb6bdc4cbd2d9e0e7eef5fc"
 "030a11181f262d343b424950575e656c737a81888f969da4abb2b9c0c7ced5dc"
 "e3eaf1f8ff060d141b222930373e454c535a61686f767d848b9299a0a7aeb5bc"
 "c3cad1d8dfe6edf4fb020910171e252c333a41484f565d646b727980878e959c"
 "a3aab1b8bfc6cdd4dbe2e9f0f7fe050c131a21282f363d444b525960676e757c"
 "838a91989fa6adb4bbc2c9d0d7dee5ecf3fa01080f161d242b323940474e555c"
 "636a71787f868d949ba2a9b0b7bec5ccd3dae1e8eff6fd040b121920272e353c"
 "434a51585f666d747b828990979ea5acb3bac1c8cfd6dd"
);

Length and word difference.6615 and 6615 bytes;L = 827. Zero-based little-endian words are shown below; a final partial word is zero-extended only for displaying the difference, not for the hash input.

w[1]: 0x1122334455667788 -> 0x8877665544332211 (XOR 0x9955551111555599)

The seed-class density is exactly 118 × 2-45, about 2-38.12. The follow-up record reports independent enumeration of the class and rehashing checks. With L = 827, that supplies a score cap of 47.81 bits, rounded upward. It is an upper bound on the score, not a proof that the worst pair has been found, and the sufficient class need not contain every colliding seed. The search over lengths and heavy state values was not exhaustive; the records name unexplored points (length 4567, heavy values of the second state word, lengths of at most 16 bytes), so a stronger pair may exist.

The supplied measurement record reports65,535/65,535class-sampled collisions for each of three tail fills. Sampling the exactly known2−19stratum gave1,821 collisions in230trials, or2−38.17after weighting, against the exact class contribution2−38.12.

This is a case where the obvious statistical experiment would be disappointing. Uniformly sampling a modest number of seeds would usually find nothing. Once the class is understood, counting its members and verifying the collision implication is much more informative. A well-mixed-looking output does not make a many-to-one seed expansion harmless. The same README section estimates that crafted inputs trigger a blinding multiplication with probability 2-62(optimistic) or 2-59(pessimistic) for a 64-bit secret seed, on the premise that the state is unbiased up to a 1- to 4-bit margin; for this length and this chosen first block the counted preimage class of the expanded seed puts the first-iteration cancellation at 2-38.12.

Reproduction.From the supplied Reproduction documentation, run inverify/a5hash/:

cc -O2 -std=c11 -o a5hash_verify a5hash_verify.c -lm
./a5hash_verify # 2^24 random seeds per pair, about 0.5 s

The command above runs the original supporting pairs. The supplement selected_pairs.c checks both selected witnesses. Build it from the archive parent withcc -O2 -std=c11 verify/a5hash/selected_pairs.c -lm -o a5-selected, then run./a5-selected. It checks the literal bytes, keys and outputs; it does not re-enumerate the 6615-byte class.

New.This counted seed-class construction is new in the follow-up records.

Selected score (a5hash v5.21, 64-bit): ≤ 47.81 bits.6615/6615 bytes;L = 827.≥ 118 × 2^-45 ≈ 2^-38.12. SeeThe collision score.

Try it in the browser
Load on view

Waiting to validate the verification program.

Run verify/a5hash locally

The selected long pair contributes about2−38.12over independently drawn API seeds; 47.81 is its length-normalized score cap, not that probability’s exponent. The older 23-byte supporting witness has a different contribution, about2−46.74. Neither is an attack-work estimate, and counting a class does not let an attacker force a victim into it.

The bounded length search exhausted 55 feasible (length, value) points. None improved the selected 47.81-bit cap; the closest alternative was 48.22 bits. The selected a5hash witness and score are unchanged.

Records:Original project & code·Verifier package·Measurements

### a5hash-128pattern:P3

Here the attacker can make a multiplication erase the message difference for every seed. The full 128-bit result collides, despite this variant’s passing test-suite result.

Seed expansion · two 64-bit state words

K2 ⊕ 17, O

public

K1 ⊕ 17, E

public

UseSeed

⊕ (seed & O)

⊕ (seed & E)

public

public

×

lo

hi

s1

s2

c · bytes 1..8

repacked from w0,w1

c = −s3

d · bytes 9..16

w1 + w2 [16..16]

only w2 changes

s3 = a4093822299f31d0

public

s4 = c0ac29b7c97c50dd

public

×

c + s3 = 0

d + s4

+ s3

+ s4

changed byte dies here: lo = hi = 0

lo; ⊕ s1

hi; ⊕ s2

same seeded s1

same seeded s2

s1

s2

a ← w0 [0..7]

unchanged

b ← w1 [8..15]

unchanged

+ a

+ b

×

a + s1

b + s2

lo

hi

Equal inputs to both output folds.

a5hash-128 erases the changed last byte in a public zero product before XORing its halves into the seeded two-word state.

01
// Input: M[17]; secret UseSeed (64 bits); all constants below public.

02
const K1 = 0x243f6a8885a308d3, K2 = 0x452821e638d01377;

03
const E = 0x5555555555555555, O = 0xaaaaaaaaaaaaaaaa;

04
s1 = K1 ^ 17; s2 = K2 ^ 17;

05
s3 = 0xa4093822299f31d0; s4 = 0xc0ac29b7c97c50dd; // No secret here.

06
(s1, s2) = mul128(s2 ^ (UseSeed & O), s1 ^ (UseSeed & E));

07
a = (read32le(M, 0) << 32) | read32le(M, 4);

08
b = (read32le(M, 8) << 32) | read32le(M, 12);

09
c = (read32le(M, 1) << 32) | read32le(M, 5); // len-16, len-12.

10
d = (read32le(M, 9) << 32) | read32le(M, 13); // len-8, len-4; overlap.

11
(s3, s4) = mul128(c + s3, d + s4); // Exploit: c + s3 = 0, d erased.

12
s1 ^= s3; s2 ^= s4;

13
(s1, s2) = mul128(a + s1, b + s2);

14
out_lo = fold(E ^ s1, s2);

15
out_hi = fold(s1 ^ s3, s2 ^ s4);

16
return words(out_lo, out_hi);

The “practically resistant” wording is from the main README at 10492db (19 December 2025), after tag 5.25. The tagged 5.21 and 5.25 READMEs instead say “practically secure against the "blinding multiplication" attack when the UseSeed is kept secret and hash outputs are not exposed”. Both conditions belong to the claim.

Code:a5hash;SMHasher3 hashes/a5hash.cpp, v5.21, 128-bit; tested at SMHasher3 commit7ad8939d; local copy:sources/a5hash.cpp. Excerpt: a5hash128, source lines 242–336. (a5hash v5.21 = upstream commit b0ba799). The newest upstream release, v5.25 (tag 5.25, 2025-12-12), changes only macros, version strings and comments in a5hash.h; the a5hash128 body is identical and the same pair collides on it for every seed (226/226sampled seeds, control pair 0/226).

Some message words enter through a product with public constants inline 11. Set one operand to zero and the partner word becomes irrelevant. The relevant constant is Seed3 = 0xA4093822299F31D0. The overlapping input reads inlines 7–10make the displayed bytes encode its additive inverse as one operand; changing the last byte changes only the other operand. This is a full 128-bit collision for every seed. The distinct 64-bit a5hash algorithm does not have this public-product path. The README's point that the seeded state recovers after a blinding multiplication (README lines 40 and 481-482) does not apply here: the line-11 product uses only the public constants Seed3 and Seed4, so the erased word never reaches the seeded state.

a5hash-128 v5.21 — NEW.Some of this variant’s message words likewise enter through a product with public constants. Set one operand to zero and the partner word becomes irrelevant:

/* Hex encodes bytes in memory order, not hexadecimal integers. */
A = hex("00ddc7f65b30ce60d60000000000000000");
B = hex("00ddc7f65b30ce60d600000000000000ff");

/* Example seed: */
0x5f642f87d5e23888

Length and word difference.17 and 17 bytes;L = 3. Zero-based little-endian words are shown below; a final partial word is zero-extended only for displaying the difference, not for the hash input.

w[2]: 0x0000000000000000 -> 0x00000000000000ff (XOR 0x00000000000000ff)

At the displayed seed, both complete outputs, as(low word, high word), are(0x754f558f576fdbdc, 0xe70d0e48e169dd4c)(evaluated locally from the supplied source). The independent confirmation retained indata.jsonrecords220/220collisions for this 17-byte pair. The structural rate is1,L = 3, and the score is≤ 1.59.

I use the follow-up verification of the mechanism and shorter witness for this row. The original investigation’s longer witness remains unverified.

Reproduction.From the supplied Reproduction documentation, run inverify/a5hash/:

cc -O2 -std=c11 -o a5hash_verify a5hash_verify.c -lm
./a5hash_verify # 2^24 random seeds per pair, about 0.5 s

The command above runs the original supporting pairs. The supplement selected_pairs.c checks both selected witnesses. Build it from the archive parent withcc -O2 -std=c11 verify/a5hash/selected_pairs.c -lm -o a5-selected, then run./a5-selected. It checks the literal bytes, keys and outputs; it does not re-enumerate the 6615-byte class.

New.This public-product construction is new in the follow-up records.

Selected score (a5hash v5.21, 128-bit): ≤ 1.59 bits.17/17 bytes;L = 3. 1 (every seed). SeeThe collision score.

Try it in the browser
Load on view

Waiting to validate the verification program.

Run verify/a5hash locally

Records:Original project & code·Verifier package·Measurements

### HighwayHashpattern:P3

The pair makes the entire internal state agree for a rare, counted set of keys. All three output sizes inherit that collision. The checked count is for one sufficient event, not every possible way the pair might collide.

Lean: ✓ checked.The trail algebra (M1, M2), exact 235·239 reduced count, and the bridge from uniform keys to that model are now machine-checked (M1–M4 complete), so 56165/272is a Lean theorem for the stated trail as well as an executed-and-verified count; the full status records the scope.

mul0[i], mul1[i] start at public constants

v0[i] = mul0[i] ⊕ k[i]; v1[i] uses rotl(k[i],32)

0

⊕ k0

rotl 32; ⊕

v0[0]

v1[0]

mul0[0]

mul1[0]

1

⊕ k1

rotl 32; ⊕

v0[1]

v1[1]

mul0[1]

mul1[1]

2

⊕ k2

rotl 32; ⊕

v0[2]

v1[2]

mul0[2]

mul1[2]

3

⊕ k3

rotl 32; ⊕

v0[3]

v1[3]

mul0[3]

mul1[3]

Lane 0 · first packet, before the zipper

w0 · bytes 0..7

δ = +256

+ mul0; lo32(v1)

×

hi32(v0[0]) = 0

lo64 = 0; ⊕ mul0[0]

hi = 0

dead when hi32(v0[0]) = 0

Key event: hi32(k0) = dbe6d5d5

×

lo32(v0 + mul1)

hi32(v1)

lo64; ⊕ mul1 (hi = 0)

hi = 0

Second product unchanged in the first packet.

v1[0,1]

v0[0,1]

δv1

zipper: byte permutation, +

zipper back to v1; +

Z low: 3,12,2,5,14,1,15,0 · public

Z high: 11,4,10,13,9,6,8,7 · public

w4 · bytes 32..39

second-packet correction

+; matched products

w8 · bytes 64..71

third-packet correction

+

cancels here on success

all 4 × {v0, v1, mul0, mul1} agree

HighwayHash’s lane-0 zero multiply lets the first packet difference pass through the zipper, and two later packets merge all sixteen state words on the sufficient key event.

01
// Input: M[96]; secret key[4], four independent 64-bit words.

02
mul0 = {0xdbe6d5d5fe4cce2f, 0xa4093822299f31d0, // Public constants.

03
 0x13198a2e03707344, 0x243f6a8885a308d3};

04
mul1 = {0x3bd39e10cb0ef593, 0xc0acf169b5f18a8c,

05
 0xbe5466cf34e90c6c, 0x452821e638d01377};

06
for (i = 0; i < 4; ++i) { v0[i] = mul0[i] ^ key[i]; v1[i] = mul1[i] ^ rotl(key[i],32); }

07
pair zipper(u64 a, u64 b) { // Public byte permutation, a = low lane.

08
 bytes = little_endian_bytes(words(a,b));

09
 return (pack_le(bytes, {3,12,2,5,14,1,15,0}),

10
 pack_le(bytes, {11,4,10,13,9,6,8,7}));

11
}

12
void Update(u64 P[4]) {

13
 for (i = 0; i < 4; ++i) {

14
 v1[i] += mul0[i] + P[i];

15
 mul0[i] ^= (v1[i] & 0xffffffff) * (v0[i] >> 32); // Exploit: zero, then equal products.

16
 v0[i] += mul1[i];

17
 mul1[i] ^= (v0[i] & 0xffffffff) * (v1[i] >> 32);

18
 }

19
 for (j = 0; j < 4; j += 2) (v0[j],v0[j+1]) += zipper(v1[j],v1[j+1]); // Wordwise addition.

20
 for (j = 0; j < 4; j += 2) (v1[j],v1[j+1]) += zipper(v0[j],v0[j+1]);

21
}

22
for (p = 0; p < 96; p += 32) { for (i = 0; i < 4; ++i) P[i] = read64le(M,p+8*i); Update(P); }

23
// No remainder or padding on this path; successful states have merged here.

24
for (r = 0; r < 4; ++r) Update({rotl(v0[2],32),rotl(v0[3],32),rotl(v0[0],32),rotl(v0[1],32)});

25
return v0[0] + v1[0] + mul0[0] + mul1[0];

Code:google/highwayhash/c/highwayhash.c, commit f8381f3 (2024-04-18);SMHasher3 hashes/highwayhash.cpp, SMHasher3 timing implementation; tested at SMHasher3 commit7ad8939d; local copy:sources/highwayhash.c. Excerpt: Reset, ZipperMergeAndAdd, Update and Finalize64, source lines 16–74 and 114–139. The frozen repository head remains f8381f3 as of 2026-09-18; the SMHasher3 timing implementation is unchanged from 7ad8939d to 3b619371.

First restrict the random 256-bit key to the classhi32(key[0]) = 0xdbe6d5d5. Its density is exactly2−32. One first-packet multiplication (line 15) then has a zero operand, allowing the message difference through without recording it in the multiplier state. The next packet, using the samelines 14–20, cancels the propagated difference when a further relation between multiplication operands holds. The final packet removes the remaining difference.

HighwayHash — EXTENSION. This pair extends the designers’ cancellation strategy. It merges the complete state during absorption, before finalization, using three complete packets:

/* Three packets: serialize each row as four little-endian uint64_t words. */
uint64_t A[3][4] = {
 {0x24192a2a01b331d1, 0, 0, 0},
 {0x24192a2ab4b332d1, 0, 0, 0},
 {0, 0, 0, 0}
};
uint64_t B[3][4] = {
 {0x24192a2a01b332d1, 0, 0, 0},
 {0x24192a2ab3b330d1, 0, 0, 0},
 {0x100, 0, 0, 0}
};

/* Example key words, in API order: */
0xdbe6d5d58afad71e 0xa0142b42de197939 0x5bd2b2861106bd66 0xb6c304527caad524
/* H(A) = H(B), selected 64-bit output: 0xf5eba26391be727f */
Complete pair as literal hex bytes
A = hex(
 "d131b3012a2a1924000000000000000000000000000000000000000000000000"
 "d132b3b42a2a1924000000000000000000000000000000000000000000000000"
 "0000000000000000000000000000000000000000000000000000000000000000"
);
B = hex(
 "d132b3012a2a1924000000000000000000000000000000000000000000000000"
 "d130b3b32a2a1924000000000000000000000000000000000000000000000000"
 "0001000000000000000000000000000000000000000000000000000000000000"
);

Length and word difference.96 and 96 bytes;L = 12. Zero-based little-endian words are shown below; a final partial word is zero-extended only for displaying the difference, not for the hash input.

w[0]: 0x24192a2a01b331d1 -> 0x24192a2a01b332d1 (XOR 0x0000000000000300)
w[4]: 0x24192a2ab4b332d1 -> 0x24192a2ab3b330d1 (XOR 0x0000000007000200)
w[8]: 0x0000000000000000 -> 0x0000000000000100 (XOR 0x0000000000000100)

The exact analysis counts the additional event with conditional probability56165/240= 235·239/240. Multiplying by the class density gives56165/272, about2−56.22. This is the exact contribution of a sufficient collision event, not the total collision probability. The byte-equation argument specifies the conditioned sample space, carry constraints, denominator and full-state implication; the exact counter, count log and recount record make that claim inspectable. A rounded exponent should not be turned into a strict inequality.

At that point all 1024 state bits agree. The 64-, 128-, and 256-bit finalizers necessarily produce identical outputs, regardless of their different numbers of rounds. Thus the known 96-byte witness gives the same score cap, about 59.81, at every output width. Longer output is helpful only when the wider output retains information that has not already been lost.

Independent class-key screens are consistent with the count: the verify package's own 11/228and 47/230(verify/highwayhash/run_2p24.txt, run_2p26.txt) and the count package's 51/230and 98/231(records/highwayhash-count/sample30_seed11.txt, sample31_seed12.txt), 207 hits where 233 are expected; every 95% interval contains 2-24.2226, and all hits collided at every width. These are not members of the older 19-run pool of 2,109 collisions in 4.35·10^10 class keys, whose rate was 2-24.30± 0.03 (1σ). That pool sits about 2.4σ below the count. The old runs shared a generator, so separate process executions should not be read as independent confirmation; the deficit is a shared-generator effect in that record, not evidence overturning the exact count. The 0/234unconditioned search had far below one expected hit at this rate and cannot validate it.

An independent computation(supplemental record)varied the number R of finalization rounds for 64-bit outputs: selected 32-byte pairs collide for every key at R = 0 (proved), at a measured rate of 0.996 at R = 1 with a proved lower bound of 247/256 ≈ 0.965, and at a measured rate of about2−19.7at R = 2. R = 3 has a reproduced distinguisher but no observed full collisions; R = 4 has no reproduced collision or distinguisher in the tested families, with collision searches reaching about234.5keys. These are results for particular message differences, separate from the absorption collision above, which survives any number of finalization rounds.

The later exact-count report(supplemental report)finds the optimum over A’s first two lane-0 packet words, keeping the other lanes zero and the differences fixed, atp1 = 0x241a0d29f0cb31d1,p2 = 0x24192a2ac586b59d: conditional trail probability about2−24.098, hence an absorption contribution about2−56.10for 96-byte messages (score ≤ 59.69). Its 72-byte version reports a separately proved score cap of 59.28; remainder wrap can prevent a collision, so the complete-packet probability does not transfer unchanged. I retain the original 96-byte pair and its exact contribution56165/272in thechart data table, where the supplied package directly reproduces the witness.

Reproduction.From the supplied Reproduction documentation, run inverify/highwayhash/:

cc -O2 -std=c11 -o highwayhash_verify highwayhash_verify.c -lm
./highwayhash_verify # 2^24 keys per experiment (2^28 for the E_2 screen)

Extension. The reported full-state collision is a theory-led extension of thedesigners’ cancellation strategy.

Thepaper’s abstractpromises “statistical analysis, speed measurements and preliminary cryptanalysis” and adds “Assuming it withstands further analysis”. In §6.2, p. 13, it assigns the combined event that both changes leave both multiplier values unaffected a probability “at most 1 in264”. The counted sufficient event contradicts that quantitative step by about27.8. This is the reason for the EXTENSION credit. The second-model sample checked the pair and found a compatible rate; the linked counting argument, not that sample, supports the exact numerator.

Selected score (HighwayHash-64, frozen): ≤ 59.81 bits.96/96 bytes;L = 12. class contribution56165/2^72 ≈ 2^-56.22. SeeThe collision score.

Try it in the browser
Load on view

Waiting to validate the verification program.

Run verify/highwayhash locally

For two fixed queries, testing full-output equality gives PRF distinguishing advantage at least56165/272− 2−ragainst a random r-bit function. At 64 bits the sufficient event is about 219.4 times the random-function rate, but its absolute advantage is still only about2−56. It is a structural distinguisher, not a constant-success two-query attack or a measured hash-table flood. Repeating the same queries under one key supplies no new independent key trial.

The reproduction README distinguishes the screens: the default./highwayhash_verifytests228class keys for E2, with 11 hits../highwayhash_verify 26tests230, with 47 hits, the run summarized by verify/README. Every hit is then checked at full state and all output widths. Neither screen rederives the numerator.

Records:Original project & code·Original paper·Verifier package·Measurements

### wyhash final v4.3pattern:P1

Flipping all the bits in two multiplication operands can leave the mixed product unchanged. With the compiled-in default secret the hash is also breakable for every seed, a property the author acknowledged in issue #15 (2019): any message whose final operand a reads as secret[1] = 0x8bb84b93962eacc9 has a zero final product, so its output depends only on the length. The 16-byte pair 934bb88b14151617c9ac2e961c1d1e1f / 934bb88b14151617c9ac2e96acadaeaf collides for every 64-bit seed (230random seeds and seeds 0, 1, 264-1 checked against upstream wyhash.h at e4764a0b). The score below is taken under the strongest key model the API supports, a uniform seed together with four uniform secret words, which excludes this shipped-constant pair; it is recorded here as the default-secret caveat. This is the same zero-operand pattern P3 used by a5hash-128.

s1 · public

8bb84b93962eacc9

prepared seed S

seed enters

L4

⊕

⊕

w0 · bytes 0..7

U = w0 ⊕ s1

m′ uses ~U

w1 · bytes 8..15

V = w1 ⊕ S

m′ uses ~V

×

U

V

lo

hi

⊕

128-bit U × V

cancels here if the two folds agree

lo ⊕ hi

equal running state

wyhash loses the complemented-word difference when the first message product has equal lo ⊕ hi folds.

01
// Selected 32-byte path; exact product, non-strict wyhash.

02
const s0 = 0x2d358dccaa6c78a5, s1 = 0x8bb84b93962eacc9;

03
fold(a,b) = lo64(a*b) ^ hi64(a*b); // Exact 128-bit product.

04
seed ^= fold(seed ^ s0, s1);

05
seed = fold(read64le(M,0) ^ s1, read64le(M,8) ^ seed);

06
// Exploit: complement both words on line 5; a successful fold merges seed.

07
a = read64le(M,16) ^ s1; b = read64le(M,24) ^ seed;

08
(a,b) = (lo64(a*b), hi64(a*b)); // Simultaneous assignment.

09
return fold(a ^ s0 ^ 32, b ^ s1);

Code:wyhash/wyhash.hat 2ac9a50 (2026-03-22, the commit that renamed the final-4.2 guard to final_version_4_3; the wyhash() body is unchanged since 2023-10-06 and unchanged at HEAD e4764a0b, 2026-03-23), measured through the paper harness's re-implementation and re-checked against the upstream header;SMHasher3 hashes/wyhash.cpp, registration "wyhash v4.2, 64-bit non-strict version" at SMHasher3 commit7ad8939d(import commit 202dada 'Update wyhash to 4.2 (commit 18a2515)', last touched ef3e615 NFC), whose verification value 0x9DAE7DD3 the upstream final v4.3 header reproduces, confirming function identity. The chart uses this matching registration’s timings: 8.75 B/cycle on M2 Pro and 8.47 B/cycle on Xeon. The benchmark uses the fixed secret; the collision experiment randomizes all four secret words. Local copy:sources/wyhash.cpp.

The common differential complements both message words entering the first multiply-fold. WriteU = u ^ s1andV = v ^ s2; complementinguandvalso complementsUandV. For the exact 128-bit product,

(~U)(~V) = UV - (U + V)(2^64 - 1) + (2^64 - 1)^2
fold(U,V) = lo64(U*V) ^ hi64(U*V)

For a roughly 2-26.4fraction of the sampled seeds, the differences in the folded halves cancel. The identity describes the mechanism; that approximate frequency is a measured property of these pairs and seed mappings, not a theorem for every mask distribution. Once this message fold agrees, the unchanged suffix starts from equal state. In the scored model the hidden key is the 64-bit API seed together with the four secret words (320 bits); the shipped public secret gives the same rate, because the differential never uses the value of the mask. The differential and harness results are prior work fromthe paper.

Inline 5the fold result becomes the next seed state. The remaining words are identical. The supplied claim record identifies this as the same non-strict function body used in SMHasher3’s v4.2 import; the measured row is final v4.3 with the seed and the four secret words sampled.

wyhash final v4.3 — REPRODUCTION —Ahle and Knudsen 2026.Independently reproduced paper-harness result, re-measured on 19 September 2026 with a uniform 64-bit seed and four uniform secret words per key (320 key bits) throughwyhash(key, len, seed, secret).

/* Pair A: literal bytes, in memory order; no NUL. */
A = hex("9bd4604137366abec688a63706aa4a2188d35499de169df633e0964e8c04600c");
B = hex("642b9fbec8c99541397759c8f955b5de88d35499de169df633e0964e8c04600c");
/* random-secret witness: seed, then secret[0..3] */
seed = 0x6c58e2bbe0b8c2ef;
secret = {0x2e87eccce404b9e7, 0x27807013cee858cb, 0x064c5e57e4a52845, 0xbda1eaa3841f1235};

Length and word difference.32 and 32 bytes;L = 4. Words are zero-based and little-endian.

w[0]: 0xbe6a36374160d49b -> 0x4195c9c8be9f2b64 (XOR 0xffffffffffffffff)
w[1]: 0x214aaa0637a688c6 -> 0xdeb555f9c8597739 (XOR 0xffffffffffffffff)

At the displayed key,h(A) = h(B) = 0xbf0d6eb792755aad; with the shipped secret, the recorded seed0x131b854bbd1f5b12gives0xa7dd61b404363777for both messages.

Under the random-secret model the pooled sample is 1088 collisions in 3·235keys (search harness 357/235; independent verifier 388 and 343 per 235on two RNG streams, all against the upstream header): rate 2−26.50, cap28.5bits, 95% interval [28.4, 28.6]. Default-secret controls give the same class: the supplied 9/230(28.8 [27.9, 30.0]), the search harness’s 28/231and the verifier’s 21/231pool to 58/(230+ 232) = 2−26.46(28.5 [28.1, 28.9]), and two earlier 235-seed reruns at e4764a0b observed 387 and 379. A secret produced bymake_secret(at most 64 bits of entropy) gives 21/231. The 24-byte single-word complement (L = 3) is statistically tied: 847/3·235= 2−26.86, 28.4 [28.3, 28.5].Measurement record.

Original: Thomas Ahle and Jakob Knudsen, “Fast Evaluation of Polynomials with Rational Preprocessing”, 2026 manuscript (paper); Orson Peters, “Breaking CityHash64, MurmurHash2/3, wyhash, and more”, orlp.net, 2 November 2024 (post). The paper harness's roughly 2-26.4multiply-fold differential (results_length.md, 32-byte default-secret/random-seed row, 25/231; its Table row uses a random secret array, 21/231) and the 32-byte pair are reproduced, now with the secret words sampled as well; this entry adds independent verification and a standalone reproduction program, with no new attack construction. Peters' 2024 search found fixed-seed multicollisions but no seed-independent attack; wangyi-fudan had already acknowledged the shipped-constant annihilation inwyhash issue #15in 2019; that result is distinct from the paper's random-seed fold differential.

Key model and default-secret caveat.Seed and all four secret words uniform per key, as passed towyhash(key, len, seed, secret)(a caller array ormake_secret). The witness mechanismfold(X, Y) = fold(~X, ~Y)never uses the secret value, so the shipped public secret gives the same rate. With the shipped secret wyhash additionally has seed-independent collisions: any message whose final operand reads as secret[1] annihilates the last product (12, 16 and 32 bytes; 1 bit at L = 2; acknowledged in issue #15), and the class w0= 0x5555555555555555 ⊕ secret[1] collides for one seed in three (3.59 bits at L = 4). Both need the shipped constants and are excluded by the scored model. The SMHasher3 row is non-strict v4.2: the upstream final v4.3 header reproduces the SMHasher3 v4.2 registration's verification value 0x9DAE7DD3, so the two are the same function.

The extended package now contains a standalone implementation, startup reference checks, the explicit pair and arandom-secretmode that draws the seed and four secret words per trial and asserts the witness above:Reproduction documentation. Its deterministic220-key check is separate from the larger pooled measurement.

Selected score (wyhash final v4.3): ≈ 28.5* bits.32/32 bytes;L = 4.1088/(3·2^35)measured with the seed and four secret words uniform. SeeThe collision score.

Try it in the browser
Load on view

Waiting to validate the verification program.

Runverify/wyhashlocally

The selected 32-byte witness gives an estimated cap of 28.5 bits from1088/(3·235)events. Its transformed exact Poisson 95% interval is [28.4, 28.6] bits. This is uncertainty in the witness-derived cap, not a confidence interval for the unknown worst pair.

### rapidhash v1pattern:P1

This historical variant inherits a multiplication-based mixing idea from wyhash. The pair changes both operands in a way that sometimes preserves the mixed product.

mask s1

at v1’s first fold

mask s2

at v1’s first fold

Seed setup absent from the supplied v1 excerpt.

⊕

⊕

w0 · bytes 0..7

U = w0 ⊕ s1

m′ uses ~U

w1 · bytes 8..15

V = w1 ⊕ s2

m′ uses ~V

×

U

V

lo

hi

⊕

128-bit U × V

cancels here if the two folds agree

lo ⊕ hi

equal running state

rapidhash v1 loses the complemented-word difference when the first message product has equal lo ⊕ hi folds.

01
// rapidhash v1.0 (tag rapidhash_v1.0), 32-byte path.

02
// s1 = secret[2]; s2 = prepared_seed ^ secret[1].

03
U = read64le(M,0) ^ s1; V = read64le(M,8) ^ s2;

04
P = exact128(U * V);

05
state = lo64(P) ^ hi64(P);

06
// Complementing both input words gives operands ~U and ~V.

07
// If their fold agrees, continue v1 with equal state and unchanged suffix.

08
// No unavailable v1 seed-preparation or finalizer is transcribed here.

Code: rapidhash v1.0, tag rapidhash_v1.0 = commit 5889784 (tag commit 2024-07-07, GitHub release 2024-08-06), measured through the paper harness’s transcription and reproduced in verify/rapidhash-v1/rapidhash_v1_verify.c. No SMHasher3 v1 registration exists. At 32 bytes the prepared seed is seed xor rapid_mix(seed xor secret[0], secret[1]) xor 32; s1 = secret[2] = 0x4b33a62ed433d4a3 and s2 = prepared_seed xor secret[1], where secret[1] = 0x8bb84b93962eacc9.

The v1 reproduction exercises thesame complemented-operand fold differential. The v1.0 header (tag rapidhash_v1.0, commit 5889784) is transcribed in full in verify/rapidhash-v1; at 32 bytes seed ^= rapid_mix(seed ^ secret[0], secret[1]) ^ 32 (header line 245), the first fold is rapid_mix(w0 ⊕ secret[2], w1 ⊕ seed ⊕ secret[1]) (line 286) and the finalizer folds (w2 ⊕ secret[1])·(w3 ⊕ seed) before the last mix (lines 292-293). The explicit v1 pair, seed and full output below come from the independent reproduction record. Its SMHasher3 result and speeds are unavailable; the supplied suite record tests v3. The quoted maintainer reply closes N-R-K's issue #10 (2024-11-23), which reported a seed-independent collision from w[len-16] = secret[1]. hoxxep's issue #25 (2025-05-24) discusses trivial collisions and randomising secrets. In January 2026 the author added that random seeds are not recommended and most users use seed 0. The selected pair and key model are stated below.

rapidhash v1 — REPRODUCTION —Ahle and Knudsen 2026.Independently reproduced paper-harness result, re-measured on 19 September 2026 with a uniform 64-bit seed and three uniform secret words per key (256 key bits) throughrapidhash_internal(key, len, seed, secret).

/* Pair A: literal bytes, in memory order; no NUL. */
A = hex("9bd4604137366abec688a63706aa4a2188d35499de169df633e0964e8c04600c");
B = hex("642b9fbec8c99541397759c8f955b5de88d35499de169df633e0964e8c04600c");
/* random-secret witness: seed, then secret[0..2] */
seed = 0x3879cdfddc782ad3;
secret = {0xd0d81d65fd961dff, 0xa9132a2f5b5d4f54, 0xd72e7f4d4f7270f5};

Length and word difference.32 and 32 bytes;L = 4. Words are zero-based and little-endian.

w[0]: 0xbe6a36374160d49b -> 0x4195c9c8be9f2b64 (XOR 0xffffffffffffffff)
w[1]: 0x214aaa0637a688c6 -> 0xdeb555f9c8597739 (XOR 0xffffffffffffffff)

At the displayed key,h(A) = h(B) = 0x4329ec0defb7f826; with the compiled-in secret, the recorded seed0x3788f2419a81e2d6gives0x8f7a71ffebd4a14bfor both messages.

Under the random-secret model the pooled sample is160/234collisions (search harness 38/232; independent verifier 40/232and 82/233, all through the upstream v1.0 header): rate 2−26.68, cap28.7bits fromlog2(L) − log2(count/2^34), 95% interval [28.5, 28.9]. Default-secret controls give the same class: the supplied 12/230(28.4 [27.6, 29.4]), two upstream reruns of 76 and 89 per 233and the verifier’s 47/232pool to 224/234.39= 2−26.59(28.6 [28.4, 28.8]); odd secret words give 49/232. The 24-byte word-0 complement (L = 3) is statistically tied: 125/234= 2−27.03, 28.6 [28.4, 28.9].Measurement record; the historical default-secret record israpid1_32.

Original: Thomas Ahle and Jakob Knudsen, “Fast Evaluation of Polynomials with Rational Preprocessing”, 2026 manuscript (paper). The paper’s roughly2−27multiply-fold differential and 32-byte rapidhash v1 pair are reproduced; this entry adds independent verification and a standalone reproduction program, with no new attack construction.

Key model and default-secret caveat.Seed and the three secret words uniform per key, passed throughrapidhash_internal; the publicrapidhash()andrapidhash_withSeed()wrappers use the compiled-inrapid_secret. The witness is a pure fold differential and does not use the secret value, so the compiled-in secret gives the same rate. With the compiled-in secret rapidhash v1 additionally has the seed-independent annihilation reported by N-R-K in issue #10 (the word at offset len−16 equal to secret[1]; 16 bytes, 1 bit at L = 2), which needs the shipped constant and is excluded by the scored model. SMHasher3 results and speeds in the supplied record apply to v3, not v1. No v1 SMHasher3 speed is supplied. The author quotation is from the v1-era issue #10; the full claim record also contains later v3 wording.

The extended package now contains a standalone implementation, startup reference checks, the explicit pair and arandom-secretmode that draws the seed and three secret words per trial and asserts the witness above:Reproduction documentation. Its deterministic220-key check is separate from the larger pooled measurement.

Selected score (rapidhash v1): ≈ 28.7* bits.32/32 bytes;L = 4.160/2^34measured with the seed and three secret words uniform. SeeThe collision score.

Try it in the browser
Load on view

Waiting to validate the verification program.

Runverify/rapidhash-v1locally

The selected 32-byte witness gives an estimated cap of 28.7 bits from160/234events. Its transformed exact Poisson 95% interval is [28.5, 28.9] bits. This is uncertainty in the witness-derived cap, not a confidence interval for the unknown worst pair.

### rapidhash v3pattern:P1

The same general multiplication pattern gives a collision pair for the standard, -micro and -nano v3 variants, at the same rate whether the eight secret words are the shipped constants or fresh random values. The reported rate is a sampled estimate, not an exact probability.

s2 · public

4b33a62ed433d4a3

prepared seed S

seed enters

L5

⊕

⊕

w0 · bytes 0..7

U = w0 ⊕ s2

m′ uses ~U

w1 · bytes 8..15

V = w1 ⊕ S

m′ uses ~V

×

U

V

lo

hi

⊕

128-bit U × V

cancels here if the two folds agree

lo ⊕ hi

equal running state

rapidhash v3 loses the complemented-word difference when the first message product has equal lo ⊕ hi folds.

01
// Selected 32- or 48-byte path, shared by standard/micro/nano.

02
const s1 = 0x8bb84b93962eacc9, s2 = 0x4b33a62ed433d4a3;

03
const s7 = 0xaaaaaaaaaaaaaaaa;

04
fold(a,b) = lo64(a*b) ^ hi64(a*b); // Exact product; unprotected.

05
seed ^= fold(seed ^ s2, s1);

06
seed = fold(read64le(M,0) ^ s2, read64le(M,8) ^ seed);

07
// Exploit: both operands on line 6 are complemented.

08
if (len > 32) seed = fold(read64le(M,16) ^ s2, read64le(M,24) ^ seed);

09
a = read64le(M,len-16) ^ len ^ s1;

10
b = read64le(M,len-8) ^ seed;

11
(a,b) = (lo64(a*b), hi64(a*b)); // Simultaneous assignment.

12
return fold(a ^ s7, b ^ s1 ^ len);

Code:rapidhash;SMHasher3 hashes/rapidhash.cpp, v3, at SMHasher3 commit7ad8939d(body imported at SMHasher3 commit 29e3090, 2025-09-07, from rapidhash commit 34f4515, 2025-08-30; identical to master 1ae7842f, 2026-08-19, apart from #pragma once); Local copies:sources/rapidhash.cppandsources/rapid_v3_port.h. Excerpt: rapid_mix and the selected short paths.

SMHasher3 testsrapidhash v3. The first-fold flaw persists:line 6is the same selected path in standard, -micro and -nano for these lengths. If it merges, the optional fold in line 8 sees equal seed states and identical words; the length-dependent tail does not separate them. This is thepaper’s fold differential.

rapidhash v3 — REPRODUCTION —Ahle and Knudsen 2026.Independently reproduced paper-harness result, re-measured on 19 September 2026 with a uniform 64-bit seed and eight uniform secret words per key (576 key bits) throughrapidhash_internal(key, len, seed, secret)of the unmodified upstream header.

/* Pair A: literal bytes, in memory order; no NUL. */
A = hex("9bd4604137366abec688a63706aa4a2188d35499de169df633e0964e8c04600c");
B = hex("642b9fbec8c99541397759c8f955b5de88d35499de169df633e0964e8c04600c");
/* random-secret witness: seed, then secret[0..7] */
seed = 0x27d3b5addafed424;
secret = {0x8201394795b91ef9, 0xbc80d672c2c377f6, 0x5afd557e26c19903, 0xa3a9fab4fc0d80e2,
 0x5108fe3feb9bd088, 0x6742ee43cec628a4, 0x2267c78c10996237, 0xd96b61ed51f62b33};

Length and word difference.32 and 32 bytes;L = 4. Words are zero-based and little-endian.

w[0]: 0xbe6a36374160d49b -> 0x4195c9c8be9f2b64 (XOR 0xffffffffffffffff)
w[1]: 0x214aaa0637a688c6 -> 0xdeb555f9c8597739 (XOR 0xffffffffffffffff)

At the displayed key,h(A) = h(B) = 0xd832bac31b8fda6c; with the shipped secret, the recorded seed0x3187ae8a8617e034gives0xa7ee6375a78a86f0for both messages.

Under the random-secret model the pooled sample is2386/237.83collisions (search harness 13/230, 161/234and 358/235on an SMHasher3-validated port; independent verifier 10/230, 5/230with ChaCha20 keys, 155/234, 311/235and 1373/237on the unmodified upstream tag): rate 2−26.61, cap28.6bits fromlog2(L) − log2(count/2^37.83), 95% interval [28.5, 28.7]. Default-secret controls give the same class: the supplied 11/230, the fairness pass’s 174/234, the study’s 12/230and 184/234and the verifier’s 158/234pool to 539/235.64= 2−26.57(28.6 [28.4, 28.7]). The 24-byte word-0 complement (L = 3) is statistically tied: 1906/237.83= 2−26.93, 28.5 [28.45, 28.6].Measurement record; the historical default-secret record is rapid3_32.

Second length and smaller variants.The 48-byte pair D also has11/230collisions with the shipped secret, withL = 6, and 191/234.17= 2−26.59under the random secret (29.2 bits [29.0, 29.4]). The random-secret estimate gives a 29.2-bit cap; the earlier default-secret sample gives 29.1 bits. Thecharted capof 28.6 uses the 32-byte pair. The same counts, example seed and outputs occur for standard, -micro and -nano at each of these two lengths, as retained in all six measurement records.

/* Pair D: literal bytes, in memory order; no NUL. */
A = hex("9bd4604137366abec688a63706aa4a2188d35499de169df633e0964e8c04600c48c651edae76208e840fc51f1cccbb02");
B = hex("642b9fbec8c99541397759c8f955b5de88d35499de169df633e0964e8c04600c48c651edae76208e840fc51f1cccbb02");
seed = 0x3187ae8a8617e034;

Length and word difference.48 and 48 bytes;L = 6. Words are zero-based and little-endian.

w[0]: 0xbe6a36374160d49b -> 0x4195c9c8be9f2b64 (XOR 0xffffffffffffffff)
w[1]: 0x214aaa0637a688c6 -> 0xdeb555f9c8597739 (XOR 0xffffffffffffffff)

At the displayed seed,h(A) = h(B) = 0xb52b5b5759f1d08a.

The supplied independent run with the shipped secret observed11/230collisions, an estimated cap of29.13bits fromlog2(L) − log2(count/2^30)(default-secret control; measurement record rapid3_48). Under the random secret the same pair gives 191/234.17, 29.2 bits.

For the separate 16-byte pair C, standard, -micro and -nano each observed zero collisions in230trials. That null result is not a collision estimate and is not used for this row.

Original: Thomas Ahle and Jakob Knudsen, “Fast Evaluation of Polynomials with Rational Preprocessing”, 2026 manuscript (paper). The paper’s multiply-fold differential is reproduced for the 32- and 48-byte rapidhash v3 pairs in standard, -micro and -nano; this entry adds independent measurements and a standalone reproduction program, with no new attack construction.

Key model and default-secret caveat.Seed and all eight secret words uniform per key, passed throughrapidhash_internal(the header’s doc comment still says “triplet”; the code indexes secret[0..7]); the public wrappers use the shipped array. The witness never uses a secret value, so the shipped secret gives the same rate. With the shipped secret rapidhash v3 additionally has the every-seed annihilation reported by N-R-K in issue #10 (v3 moved the condition to the word at offset len−16 equal to secret[1] ⊕ len; 16 and 32 bytes; 1 bit at L = 2), which needs the shipped array and is excluded by the scored model. SMHasher3 tests v3. The first-fold flaw persists in standard, -micro and -nano: each has 11/230at both 32 B and 48 B with the shipped secret. The 28.6-bit plotted cap uses L=4 at 32 B; the 48-byte random-secret estimate is 29.2 (29.1 in the earlier default-secret sample). Timings shown are for standard v3. Built with RAPIDHASH_PROTECTED at master 1ae7842f, the shipped-constant annihilation pairs differ on every one of 226seeds, but the fold pairs A and D still collide (4/228each, about 2-26); protected mode removes the key-free pair, not the fold differential. Independent 234and 233default-secret samples against upstream master 1ae7842f gave 174 and 98 events (pooled 28.5 bits, 95% interval [28.3, 28.7]).

Reproduction.From Reproduction documentation, run inverify/rapidhash-v3/:

cc -O2 -std=c11 -o rapidhash_v3_verify rapidhash_v3_verify.c -lm
./rapidhash_v3_verify 20
./rapidhash_v3_verify 20 1 random-secret

The program checks the SMHasher3 verification values and the recorded colliding seed before taking a new220-seed sample; therandom-secretmode draws the seed and eight secret words per trial for all six cases and asserts the random-model witness above. For the rare fold differentials, zero new hits at this scale does not reproduce or refute the separate230-seed rate. See the README for expected output and variant coverage.

Selected score (rapidhash v3): ≈ 28.6* bits.32/32 bytes;L = 4.2386/2^37.83measured with the seed and eight secret words uniform. SeeThe collision score.

Try it in the browser
Load on view

Waiting to validate the verification program.

Run verify/rapidhash-v3 locally

The selected 32-byte witness gives an estimated cap of 28.6 bits from2386/237.83events. Its transformed exact Poisson 95% interval is [28.5, 28.7] bits. This is uncertainty in the witness-derived cap, not a confidence interval for the unknown worst pair.

Records:Original project & code·Verifier package·Measurements

### XXH3-64 0.8.3pattern:P1

Complementing one keyed word of a 16-byte block leaves the folded product unchanged for about one key in 227, whatever the secret bytes are. The scored pair is a 24-byte word complement under a uniform 192-byte secret. A 32-byte pair built from the default-secret words collides far more often (one seed in about 1,423) when the library's built-in secret is in use; it is recorded below as the default-secret caveat.

Claim excerpt.“not meant to avoid intentional collisions”. The scored result is a fixed-pair rate forXXH3_64bits_withSecretv0.8.3 with 192 uniform secret bytes (1536 key bits; the API minimum is 136 bytes), the strongest key model the API supports.XXH3_64bits_withSeed, andXXH3_64bits_withSecretandSeedand the streamingreset_withSecretandSeedfor inputs of at most 240 bytes, hash with the default secret and only the 64-bit seed hidden; they are covered by the caveat below. Neither is a violated cryptographic guarantee.

/* Pair W0. Hex encodes bytes in memory order. */
M = hex("000000000000000000000000000000000000000000000000");
M' = hex("ffffffffffffffff00000000000000000000000000000000");
/* 192-byte secret (XXH3_64bits_withSecret has no seed) */
c9eb2c4bbc54b9cd6ddfbb86d6dfffae5f96e2b9ba49bafeda316c65e62f6d099798b895b8cfaa0a65497109bd7bb4a1
1b6e08792a6222604c44afeb83ab8d9fbc49fa6bd7eeb2a8886a0cbf50060b759a7d3f801597002d68fc5fab9f4144e6
aaf3c9a2ddac70e35114db1307ef0d0ce23e5a947218d6217f45612f0987f9f59e68c918342362f7e9984e9f4cd86e51
ece391ffcb3ac35fa080b04dbb776cfb6f539ca0049bd1d89db1a130daf6a5121292121c90af684d0a9dad3752ee254a
/* H(M) = H(M') = 0x24453ecc9793506c */

Bytes 0..7 are complemented and everything else is zero. At 24 bytes those bytes feed only block 0 (bytes 0..15), while the tail block (bytes 8..23) is unchanged, so under a uniform secret the pair collides exactly when the two uniform keyed words of block 0 satisfyfold(x, y) = fold(~x, y), the (M, 0) XOR differential of lo ⊕ hi of a 64×64-bit product; the seed-and-secret model gives the same rate, since S2i+ seed and S2i+1− seed are uniform whenever S is. Lengths 17..23 would re-read the changed bytes in the tail block. The example key above is the verifier's first witness.

A = w0 XOR S0; B = w1 XOR S1; // S0, S1: the secret words of block 0 (uniform)
fold(A, B) = low64(A * B) XOR high64(A * B);
// M' gives (~A, B); the tail block is unchanged.
collision iff fold(A, B) == fold(~A, B);
// The final avalanche is bijective.

The independent verifier observed 260/235throughXXH3_64bits_withSecretand 267/235with seed and secret both uniform: ε = 527/236≈ 2−26.96. With L = 3, log₂(3/ε) ≈28.5 bits, 95% interval [28.4, 28.7]. Under the same model the 32-byte NAF pair below is an ordinary (M, M) block complement, 764/236.17≈ 2−26.59, 28.6 bits [28.5, 28.7], statistically tied. Inputs of 1..16 bytes are injective per length under a uniform secret, and the stripe swap on the > 240-byte path is about 2−32.6at L ≥ 31 (cap ≈ 37.5). This sampled cap leaves room for stronger pairs.Measurement record.

Selected score (XXH3-64 0.8.3): ≈ 28.5* bits.24/24 bytes; L = 3. about 527 of every 2^36 keys (sampled; 527 events, pooled). SeeThe collision score.

Default-secret caveat.WithXXH3_64bits_withSeed(default kSecret, uniform 64-bit seed), withXXH3_64bits_withSecretandSeedfor inputs of at most 240 bytes (xxhash.h v0.8.3 hashes with kSecret and the seed there and ignores the custom secret) and with the streamingreset_withSecretandSeed, the 32-byte pair below collides for 2−10.47of seeds: three fresh upstream streams found 755,087, 754,660 and 754,334 hits per 230seeds throughwithSeed, ε = 2,264,081/(3·230) ≈ 2−10.4745, and 188,643/228throughwithSecretandSeedand 11,864/224streaming, hit for hit with the one-shot call. With L = 4 the cap is 12.47 bits, 95% interval [12.473, 12.476].

/* NAF pair (default secret). Hex encodes bytes in memory order. */
M = hex("0000000000000000000000000000000051151210404400000000008204000105");
M' = hex("00000000000000000000000000000000aeeaedefbfbbffffffffff7dfbfffefa");
/* API seed */
0x2468b3bc26a44073
/* H(M) = H(M') = 0xdd686b61e2f6dc69 */

Both strings begin with 16 zero bytes. In block 1, the little-endian words (P, N) are the positive and negative digit sums of the non-adjacent signed-digit representation of D = K₂ + K₃ + 1 =faff443b8e121551, where K₂ and K₃ are the default-secret words used by this block; the second message complements this block, and the seed-shifted carry masks of the two multiplicands then agree except at the signed-digit positions. The example seed is2468b3bc26a44073(= P − K₂), givingdd686b61e2f6dc69for both messages.Seed 0 does not collide.The construction uses the values of K₂ and K₃ and does not transfer to an independently random secret (0/232in the XXH3-128 control; the 2−26.6class above).XXH3_generateSecret_fromSeedyields only 64 bits of entropy (kSecret ± seed) and stays in this model. The bounded search that found it checked 192 single moves and 18,336 two-move neighbours; that local search is not a global bound.

Reproduction.Package README, standalone C verifier, smoke counts and length checks; therandom-secretmode samples the W0 pair throughXXH3_64bits_withSecretwith a fresh 192-byte secret per trial, keeps the NAF/withSeedcheck as the default-secret control and asserts trial by trial thatwithSecretandSeedreturns thewithSeedoutputs at 32 bytes.

cc -O3 -std=c11 xxh3_64_pair_check.c -lm -o check
./check 20
./check random-secret 20

Historical controls remain separate. The base-1143 zero-tail pair had 483 and 535 hits per 230fresh seeds and a 23.01-bit cap with the default secret; the older pair A supplied the 9/12/11/11 cross-hash comparison. Neither supplies the current score.Issue #1127and the ensuing#1146/#1150comment changes quote default-secret figures forXXH3_64bits_withSeed(about 2−27and 2−21for the 128-byte pairs, and the 2−10.47pair above); the random-secret rate scored here is the figure for the custom-secret interface.

Try it in the browser
Load on view

Waiting to validate the verification program.

Run verify/xxh3-64 locally

Records:Original project & code·Algorithm specification·Verifier package·Measurements

### XXH3-128 0.8.3pattern:P1

Producing a full 128-bit collision requires preserving both a product-related value and a sum. The pair is chosen to do both, and its rate is the same with a fresh random 192-byte secret as with the library’s default secret; the score is taken under the random secret.

S0 · public

be4ba423396cfeb8

S1 · public

1cad21f72c81017c

seed

+ seed

− seed

public

public

w0 · bytes 0..7

U = w0 ⊕ (S0 + seed)

m′ uses ~U

w1 · bytes 8..15

V = w1 ⊕ (S1 − seed)

m′ uses ~V

×

U

V

lo

hi

⊕

128-bit U × V

cancels here if the two folds agree

lo ⊕ hi

equal first mix16B term F

The second accumulator also reads the raw sum.

w1 = ~w0; complementing swaps the words

+ : w0 + w1 = 2⁶⁴ − 1

equal lo and hi before both finalizers

XXH3-128 loses the complemented-word difference when the first message product has equal lo ⊕ hi folds, while w0 + w1 also stays unchanged for Pair F.

01
// Selected 32-byte path; S0..S3 are the secret words (kSecret for withSeed, caller bytes for withSecret).

02
const S = {0xbe4ba423396cfeb8, 0x1cad21f72c81017c,

03
 0xdb979083e96dd4de, 0x1f67b3b7a4a44072};

04
const P1 = 0x9e3779b185ebca87;

05
fold(a,b) = lo64(a*b) ^ hi64(a*b); // Exact 128-bit product.

06
mix(j) = fold(read64le(M,8*j) ^ (S[j] + seed),

07
 read64le(M,8*j+8) ^ (S[j+1] - seed));

08
avalanche(x) { x ^= x >> 37; x *= 0x165667919e3779f9; return x ^ (x >> 32); }

09
const P2 = 0xc2b2ae3d27d4eb4f, P4 = 0x85ebca77c2b2ae63;

10
lo = 32 * P1; hi = 0;

11
lo += mix(0); lo ^= read64le(M,16) + read64le(M,24);

12
hi += mix(2); hi ^= read64le(M,0) + read64le(M,8);

13
// Pair F has w1 = ~w0: the sum on line 12 stays 2^64-1.

14
out_lo = avalanche(lo + hi);

15
out_hi = -avalanche(lo * P1 + hi * P4 + (32 - seed) * P2);

16
return (out_lo, out_hi); // Both output words must agree.

Code:xxHash/xxhash.h, v0.8.3;SMHasher3 hashes/xxhash.cpp, 0.8.3, XXH3-128; tested at SMHasher3 commit7ad8939d; local copy:sources/xxhash.cpp. Excerpt: the same mix16B plus XXH128_mix32B and the 128-bit finalizer, source lines 881–917. Arithmetic is modulo264except for the exact 128-bit products.

Thesame fold differentialmust also preserve the raw word sum entering the other accumulator inline 12. Pair F first setsw1 = ~w0; complementing both words swaps them and keepsw0 + w1 = 2^64 − 1. The unchanged tail and both finalizers therefore agree whenever the first fold cancels. The stored observations compare both output words.

XXH3-128 0.8.3 — REPRODUCTION —Ahle and Knudsen 2026.Independently reproduced paper-harness result, re-measured on 19 September 2026 with a uniform 192-byte secret per key (1536 key bits) throughXXH3_128bits_withSecret.

/* Pair F: literal bytes, in memory order; no NUL. */
A = hex("9bd4604137366abe642b9fbec8c9954188d35499de169df633e0964e8c04600c");
B = hex("642b9fbec8c995419bd4604137366abe88d35499de169df633e0964e8c04600c");
/* random-secret witness: 192-byte secret (XXH3_128bits_withSecret has no seed) */
f55eeab0159e547f711592ac35d621071d0717aa7711f16dfa734583e3cd2b0bc8858c2486e8ee0602aec0ee2442e847
66d18cd32f3848391113dd2f09bd80ae2ae4caf1d6c14c97ec2b84e675d93834168d3521ce6792cb17447baff00d291a
8e27646d7b1b34ddccf7e5836819c8009baa94225f7c5f4d8dfad13146531fe00a74042b9f7536a8570de8b36903cc98
a3e30e15e0c5cfe797ddab09244f7ff55b6a75163d16f5860bfbea0dd4030c420b3fe642b7358944e8d568313cc9a5e7

Length and word difference.32 and 32 bytes;L = 4. Words are zero-based and little-endian.

w[0]: 0xbe6a36374160d49b -> 0x4195c9c8be9f2b64 (XOR 0xffffffffffffffff)
w[1]: 0x4195c9c8be9f2b64 -> 0xbe6a36374160d49b (XOR 0xffffffffffffffff)

Under the displayed secret both complete outputs agree:high64 = 0xced3d509b74eee89andlow64 = 0x033e7fcc84653051(0xced3d509b74eee89033e7fcc84653051in high/low order), re-checked through the non-inlined library. With the default secret the recorded seed0xe130d569418d2efegives0x77aee7ca6253510cff9994fe21ab989afor both messages.

Under the random-secret model the pooled sample is 479 full 128-bit collisions in 235.46keys (independent verifier: 156/234throughwithSecret, 84/233with seed and secret both uniform, 60/232on a second stream; search harness 179/234): rate 2−26.56, cap 28.6 bits from log2(L) − log2(count/235.46), 95% interval [28.4, 28.7]. The default-secret control gives the same class: sixteen 230-seed runs of the reproduction program (RNG seeds 1–16; eight against xxHash dev 6cc7b4b, eight against the embedded 0.8.3 header, whose XXH3 core is functionally identical) observed 165/234, and the verifier 44/232, pooled 209/234.32= 2−26.62(28.6 [28.4, 28.8]). The paper harness's original 5/230run gave 29.7 bits with a wide interval [28.5, 31.3] that contains both estimates.Measurement record.

Original: Thomas Ahle and Jakob Knudsen, “Fast Evaluation of Polynomials with Rational Preprocessing”, 2026 manuscript (paper); Thomas Ahle, xxHash issue #1127 (XXH3 differential reported upstream), 2 September 2026 (issue). The paper’s multiply-fold differential and 32-byte XXH3-128 pair are reproduced, preserving the raw word sum and comparing both output words; this entry adds independent verification and a standalone reproduction program, with no new attack construction.

Key model.Pair F sets w1=~w0 before complementing both words, preserving their sum, so the collision is the pair-independent event fold(A, B) = fold(~A, ~B) on both 64-bit halves; both low64 and high64 are compared, and this is a full 128-bit collision. The event does not use the secret value, and the seed is redundant for inputs of at most 240 bytes (S0+ seed and S1− seed are uniform whenever S is), so the seed-and-secret model gives the same rate. The rate is block- and length-independent (64 B: 43/232; 160 B: 34/232). The XXH3-64 NAF pair does not transfer (0/232).XXH3_128bits_withSecretandSeedignores the custom secret for every length up to 240 (confirmed over 54,400 checks), so callers of that function with short inputs are in the 64-bit-seed model, where the same pair collides at the same rate.

The extended package now contains a standalone implementation, startup reference checks, the explicit pair and arandom-secretmode that draws a fresh 192-byte secret per trial, asserts the witness above and checks trial by trial thatwithSecretandSeedreturns thewithSeedoutputs at 32 bytes:Reproduction documentation. Its deterministic220-key check is separate from the larger pooled measurement.

Selected score (XXH3-128 0.8.3): ≈ 28.6* bits.32/32 bytes;L = 4.479/2^35.46measured with a uniform 192-byte secret. SeeThe collision score.

Try it in the browser
Load on view

Waiting to validate the verification program.

Run verify/xxh3-128 locally

The selected 32-byte witness gives an estimated cap of 28.6 bits from 479/235.46events. Its transformed exact Poisson 95% interval is [28.4, 28.7] bits. This is uncertainty in the witness-derived cap, not a confidence interval for the unknown worst pair.

Records:Original project & code·Algorithm specification·Verifier package·Measurements

### MUM v3pattern:P2

In the historical implementation studied here, two message words produce the same public mixing value. Combining that value with the seed preserves their collision.

w0 · bytes 0..7

two distinct words

p0 · public

9ebdcae10d981691

×

w0

× p0

+

lo

hi

lo + hi modulo 2⁶⁴ · cancels here

same public term

term = 23c79412f8129524

seed

seed enters (L4)

seeded state

⊕

term

⊕

equal state

common MUM finalization

MUM v3’s two message words give the same public lo + hi term, so XORing that term into the seeded state collides for every seed.

01
// MUM v3, exact multiplication, 8-byte input; either unroll factor.

02
const p0 = 0x9ebdcae10d981691, start = 0xc42b5e2e6480b23b;

03
mum(a,b) = (lo64(a*b) + hi64(a*b)) mod 2^64;

04
state = mum((seed + 8) mod 2^64, start);

05
term = mum(read64le(M,0), p0); // Public: no seed enters this term.

06
state ^= term; // Exploit: the two words give the same term.

07
return mum(state, state); // MUM v3 finalization.

Code:mum-hash/mum.h, v3, measured through the paper harness's re-implementation (which already carries the November 2025 zero-operand guard in its bulk loop; an eight-byte input never reaches it);SMHasher3 hashes/mum_mir.cpp, MUM v3; SMHasher3 timings: mum3.exact.unroll3; the SMHasher3 tree used for the two-host benchmark (mum_mir.cpp unchanged since ad6f3443, 2023); local copy:sources/mum_mir.cpp. Excerpt: _mum, the public primes, the remainder-word loop, v3 finalizer and wrapper, source lines 44–88, 103–140 and 173–194. Arithmetic is modulo 264except for the exact 128-bit products.

MUM uses addition of product halves here. Its public term inline 5is equal for the two words: _mum(w, 0x9ebdcae10d981691) = 0x23c79412f8129524. XORing the same term into the seeded state proves collision for every seed. An eight-byte input never enters the bulk unroll loop, so the result holds for both 8-word and 16-word unroll variants. The November 2025 collision-prevention change (commit 52c7d6c) only guards the paired-word loop for inputs longer than 8×unroll bytes; the eight-byte path is unchanged, so the pair still collides for every seed in the current default build (mum.h at 595c091, 2026-06-02) and under MUM_V3, MUM_V1 and MUM_V2. Only the opt-in MUM_QUALITY build, which adds the prime to each remainder word before multiplying, escapes this particular pair, and a short rho search yields an every-seed eight-byte pair for it as well.

MUM v3 — REPRODUCTION —Ahle and Knudsen 2026.Independently reproduced paper-harness result; default public constants and a random 64-bit API seed.

/* Pair G: literal bytes, in memory order; no NUL. */
A = hex("7954a998719b89b0");
B = hex("2d69169b259feb08");
seed = 0x0000000000000000;

Length and word difference.8 and 8 bytes;L = 1. Words are zero-based and little-endian.

w[0]: 0xb0899b7198a95479 -> 0x08eb9f259b16692d (XOR 0xb862045403bf3d54)

At the displayed seed,h(A) = h(B) = 0xb341726e9ea37186.

The supplied independent run observed220/220collisions. The public-term identity proves probability 1 for every seed and score≤ 0. Measurement record: mum8.

The second unroll variant's record, mum16, has the same pair, example seed and output and independently records 220/220. SMHasher3 names the 8-word and 16-word versions mum3.exact.unroll3 and mum3.exact.unroll4; both are FAIL 214/250. SMHasher3's own published table (results/README.md at 7ad8939d, the maintainer's machine) lists them at 27.39 and 28.06 in its 'Avg. cycles (1-32 bytes)' column and 5.97 and 5.86 bytes per cycle in bulk; the Xeon and M2 numbers in thechart data tableare this post's measurements.

Original: Thomas Ahle and Jakob Knudsen, “Fast Evaluation of Polynomials with Rational Preprocessing”, 2026 manuscript (paper). The paper’s key-free eight-byte MUM v3 pair is reproduced for both the 8-word and 16-word unroll variants; this entry adds independent verification and a standalone reproduction program, with no new attack construction.

Exact multiplication, fixed public constants, default MUM v3 configuration (including the November 2025 bulk-loop guard). The fixed, seed-independent 8-byte pair collides for every API seed in both the 8-word and 16-word unroll variants. Herekey_freemeans that all-seed identity, with the stated public constants; every experiment’s pair is chosen independently of the deployed secret, whether or not it has that identity.

Reproduction.From Reproduction documentation, run inverify/mum/:

cc -O2 -std=c11 -o mum_verify mum_verify.c -lm
./mum_verify 20

The program checks the SMHasher3 verification value and the recorded colliding seed before taking a new220-seed sample. For the rare fold differentials, zero new hits at this scale does not reproduce or refute the separate230-seed rate. MUM’s all-seed cases must collide on every sampled seed. See the README for expected output and variant coverage.

Selected score (MUM v3): 0 bits.8/8 bytes;L = 1. 1 (every seed);2^20/2^20in both unroll variants. SeeThe collision score.

Try it in the browser
Load on view

Waiting to validate the verification program.

Run verify/mum locally

Records:Original project & code·Verifier package·Measurements

### pengyhash v0.3pattern:P2

The main loop does not use the secret. Two messages that leave it in the same state remain indistinguishable when the secret is added later.

w0 · bytes 0..7

changed

w1 · bytes 8..15

changed

w2 [16..23] = w3 [24..31] = 0

Both pairs satisfy w1 + w0 + w0 = 0.

a = 32 + w1 + w0

+ w0

+ w1

32 public

+

⊕

a

rotl(w1,14)

+ w1 → u

u = 3ad679fa2cd9554d

Public u collides: the difference cancels here.

s0 = 32

s1 = u ⊕ rotl(u,40)

s2 = u

s3 = 32

+ w0 again

⊕ rotl 40

u → s2

+; ⊕ rotl 11 (L6)

Both tails are empty: f0 = f1 = f2 = f3 = 0.

seed

+ s1 only

Six final rounds

seed enters here (line 10)

equal state

+ s0 + s1 + s2 + s3

Equal result for every seed.

pengyhash’s selected word pairs give the same seed-free four-word bulk state, and the seed enters only after that merge in finalization.

01
// 64-bit arithmetic; R(x,k) rotates left. Input words are little-endian.

02
s = (len(M), 0, 0, 0);

03
for each full 32-byte block (w0,w1,w2,w3): // NO seed here.

04
 s1 += w1; s0 += s1+w0; s1 = s0 ^ R(s1,14);

05
 s3 += w3; s2 += s3+w2; s3 = s2 ^ R(s3,23);

06
 s3 += w3; s0 += s3+w0; s3 = s0 ^ R(s3,11);

07
 s1 += w1; s2 += s1+w2; s1 = s2 ^ R(s1,40);

08
(f0,f1,f2,f3) = little-endian words of zero-padded remaining 0..31 bytes;

09
repeat 6 times:

10
 s1 += seed; // The only seed entry, repeated in finalization.

11
 s1 += f1; s0 += s1+f0; s1 = s0 ^ R(s1,14);

12
 s3 += f3; s2 += s3+f2; s3 = s2 ^ R(s3,23);

13
 s3 += f3; s0 += s3+f0; s3 = s0 ^ R(s3,9);

14
 s1 += f1; s2 += s1+f2; s1 = s2 ^ R(s1,40);

15
return s0+s1+s2+s3;

Code:pengyhash;SMHasher3 hashes/pengyhash.cpp, v0.3; tested at SMHasher3 commit7ad8939d; local copy:sources/pengyhash.cpp. Excerpt: the complete bulk loop and finalizer. Arithmetic wraps at the stated word width. The file is unchanged at 3b619371 and ports upstream master 9b70a18e (2022-11-30, newest commit; no tags or releases).

Lines 3–7 compress each block before the seed enters on line 10. For the selected pair, w2 = w3 = 0 and w1 + 2w0 = 0 on both sides. The remaining public word-pair function has the same value,u1 = 0x3ad679fa2cd9554d, on both inputs. A Brent-rho search found this equality. Both bulk states are(0x20, 0xe38334c0faa0af61, 0x3ad679fa2cd9554d, 0x20)and both tails are empty. Identical inputs to lines 9–15 prove equal outputs for every seed.

pengyhash v0.3 — NEW.Fixed messages and a uniformly hidden API seed; No prior literature identified in the supplied checked record.

M = hex("7d664c02e4863788063367fb37f290ef00000000000000000000000000000000") // 32 bytes
M' = hex("2bbb99a5513852e1aa89ccb45c8f5b3d00000000000000000000000000000000") // 32 bytes
seed = 0x3a34ce6380fc0bc5
H(M,seed) = H(M',seed) = 0x90f2edac34d9a4d5

Examples and output variants.0x3a34ce6380fc0bc5 -> both 90f2edac34d9a4d5; seed 0 -> both 76a337c4b9d61cf9; seed 1 -> both 938d2f6beab2457f; seed 0xffffffffffffffff -> both 9936086fe57a4f5c (all four reproduced by the verifier). Second pair: 0x3a34ce6380fc0bc5 -> both cd93fc86a39c2c20; seed 0 -> both 937af7f4b9c00694; seed 1 -> both 88c04971182dae4e.

The independent verifier measured 1,073,741,824/1,073,741,824 collisions. State equality proves ε = 1, so L = 4 gives score ≤ 2. The separately verified 32-byte-versus-one-byte pair has the same cap (L counts the longer message, so the one-byte side does not lower it); the package includes it too.

Version and seed model. The attacked function is SMHasher3's sequenced pengyhash v0.3, verification 0x861A1254, with a 64-bit seed. rurban's SMHasher tests the older v0.2 (32-bit seed, verification 0x1FC2217B), not v0.3. Upstream v0.3 has a reported unsequenced modification; this result is pinned to the sequenced SMHasher3 form. v0.3 uses GPLv3; earlier versions used BSD 2-Clause. Upstream pengyhash.c has unsequenced combined assignments (issue #2, open; gcc -Wsequence-point flags all eight bulk and finalization lines). On every compiler we tried, gcc 11.5 and clang 21.1 at -O0 and -O2, the upstream source computes the same function as the SMHasher3 sequenced form (verification 0x861A1254) and both pairs collide for every seed sampled; fwojcik reports the same for gcc 12.2 -O3 in issue #2.

NEW: we found no prior publication of this pair or of the seed-free bulk-loop collision. The SeedBlockLen failures in SMHasher3 are related-seed collisions, not the same-seed event scored here.

* Not independently re-run: the 2,000-cell x 226-seed differential scan (zero hits, resolution about 2-26per cell), the sub-32-byte argument, and the other z3 targets. They do not affect the score.

Verbatim official wording and checked source record

Fast 64-bit non-cryptographic hash algorithm | ## v0.3 changes
- remove usage of memcpy()
- 64-bit seed
- tweaked hash with new rotation constants
- faster
- switched to GNU GPLv3 license | Version 0.3 passes these tests.

README.md line 2 (the entire official description; also the GitHub repository description) and lines 4-9 (the remainder of the 199-byte README), https://github.com/tinypeng/pengyhash; author's reply on issue #1 'Fail Avalanche, Seed Tests from demerphq/smhasher' (tinypeng, 2022-11-30T04:38:57Z, issue still open), https://github.com/tinypeng/pengyhash/issues/1. Implied quality claim: the author-bundled SMhasher_results.txt (first added 2020-08-21, updated -- not added -- in the v0.3 commit 036dab53: line 2 '--- Testing pengyhash "pengyhash" GOOD', 'Verification value 0x861A1254 ....... PASS', zero FAIL lines) and SMhasher_demerphq_results.txt ('# All Tests Passed. pengyhash passed all 195 tests run.'). No paper, design doc, security statement or collision claim of any kind exists.

pengyhash v0.3 (upstream master commit 9b70a18e, 2022-11-30; no tags or releases; GPLv3 since v0.3, BSD 2-Clause before, confirmed from LICENSE at 70a23e40). Author Alberto Fajardo (GitHub tinypeng). SMHasher3 'pengyhash' = v0.3, hashes/pengyhash.cpp, SRC_STABLEISH, verification_LE = verification_BE = 0x861A1254 (SMHasher3 commit 45557df3 'Update pengyhash to v0.3 (commit 9b70a18)', authored 2023-09-12, committed 2023-11-17). rurban tests v0.2 (uint32_t seed, verification 0x1FC2217B, 2020-09-04), not v0.3. Upstream v0.3 has an unsequenced modification (issue #2, open); the SMHasher3 sequenced form is what was attacked, pinned by reproducing 0x861A1254.

Reproduction.From Reproduction documentation, run inverify/pengyhash/:

cc -O2 -std=c11 -o pengyhash_verify pengyhash_verify.c -lm
./pengyhash_verify 20

This checks the SMHasher3 value, asserts the recorded outputs, prints the literal pair and samples exactly220seeds per case. Expected output and the distinction from the larger historical runs are in the README.

Selected score (pengyhash v0.3): ≤ 2 bits.32/32 bytes;L = 4. 1 (every seed). SeeThe collision score.

Try it in the browser
Load on view

Waiting to validate the verification program.

Run verify/pengyhash locally

Records:Original project & code·Verifier package·Measurements

### nmhash32 v2pattern:P7

The chosen difference cancels for roughly one in four seeds. Every possible 32-bit seed was checked, giving an exact count for this pair.

P0 = 9e3779b1 · public; only lane j = 0 changes

w0 · bytes 0..3

Δ = 80400000

w4 · bytes 16..19

Δ = 80400000

seed + 64; ⊕

⊕ P0 public

w4

x = P0 ⊕ w0

y = (seed+64) ⊕ w4

+

+

+ y

x differences cancel if bit22(seed+64) = 1.

×

×

hi16

hi16

C1

public

lo16(x)

hi16(x)

lo16

hi16

lo16

lo16; ≪16

x

×

×

hi16

hi16

C2

public

lo16(x)

hi16(x)

lo16

hi16

lo16

lo16; ≪16

x

×

×

hi16

hi16

C3

public

lo16(x)

hi16(x)

lo16

hi16

lo16

lo16; ≪16

x

split x

⊕ (x ≪ 5) ⊕ (x ≫ 13)

⊕

x

⊕ retained y

⊕ (x ≪ 11) ⊕ (x ≫ 9)

Each product keeps lo16; hi16 is discarded.

C3 low-half multiply: no carry across bit 13.

Then ⊕ (x ≫ 10) ⊕ (x ≫ 20).

x: Δ = 80202808

y: Δ = 80400000

⊕ shifts

retained y

w8 · bytes 32..35

Δ = 80202808

w12 · bytes 48..51

Δ = 80400000

⊕; cancels here

⊕; cancels here

All four lanes enter the final round identically.

nmhash32’s lane-0 difference returns through the retained y word and is cancelled by the next two message words when the seed-bit and carry conditions hold.

01
// All registers are 32 bits; shifts/XORs in each assignment use the old x.

02
mul16(x,c) = ((lo16(x)*lo16(c)) mod 2^16)

03
 | (((hi16(x)*hi16(c)) mod 2^16) << 16);

04
P = [0x9e3779b1,0x85ebca77,0xc2b2ae3d,0x27d4eb2f];

05
C1=0xf0d9649b; C2=0x29a7935d; C3=0x55d35831;

06
mix(x,y,final):

07
 x += y; if final: y ^= (y<<17) ^ (y>>6);

08
 x = mul16(x,C1); x ^= (x<<5) ^ (x>>13);

09
 x = mul16(x,C2); x ^= y; x ^= (x<<11) ^ (x>>9);

10
 x = mul16(x,C3); x ^= (x>>10) ^ (x>>20); return x;

11
sl = seed + 64;

12
for j = 0..3:

13
 x[j] = P[j] ^ read32le(M,4*j);

14
 y[j] = sl ^ read32le(M,16+4*j);

15
 x[j] = mix(x[j], y[j], false); // Loop round; y[j] is retained.

16
 x[j] ^= read32le(M,32+4*j); y[j] ^= read32le(M,48+4*j);

17
 x[j] = mix(x[j], y[j], true); // Final round uses remixed local y.

18
x = sum_j (x[j] ^ P[j]);

19
x ^= sl + (sl>>5); x = mul16(x,C3);

20
return x ^ (x>>10) ^ (x>>20);

Code:hash-garage;SMHasher3 hashes/nmhash.cpp, nmhash32 v2; tested at SMHasher3 commit7ad8939d; local copy:sources/nmhash.cpp. Excerpt: NMHASH32_9to255 and its four-lane fold, specialized to 64 bytes. Arithmetic wraps at the stated word width.

The changed lane is j = 0. XORing0x80400000into both words on lines 13–14 leaves the addition on line 7 unchanged precisely when bit 22 ofseed + 64is set. The difference passes through the lane multiplications and XOR shifts on lines 8–10; the low 16-bit C3 multiplication additionally requires no carry across bit 13. The resulting x difference is0x80202808and the retained y difference is0x80400000. The fresh words on line 16 cancel them, leaving the entire final round and fold equal.

nmhash32 v2 — NEW.Fixed messages and a uniformly hidden API seed; No prior literature identified in the supplied checked record.

M = hex("00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000") // 64 bytes
M' = hex("00004080000000000000000000000000000040800000000000000000000000000828208000000000000000000000000000004080000000000000000000000000") // 64 bytes
seed = 0xb54cda26
H(M,seed) = H(M',seed) = 0xe00f99e0

Examples and output variants.0xb54cda26 -> both 0xe00f99e0 (seed 0 differs: f238703d vs cc7f7e62); verifier's further colliding seed 0xe142fddf -> both 0427babe.

The search program's scalar transcription, an independent scalar verifier, and the upstream nmhash.h itself (hash-garage e022156ca8, AVX-512 and NMH_SCALAR builds) each enumerated all 232seeds and counted 1,078,944,392 collisions. Thus ε for this fixed pair is exactly 1078944392/232≈ 0.251211; L = 8 gives score ≤ 4.994 (the unrounded value is log2(8·232/1078944392) = 4.9930266347…). The verifier's separate sampled run found 269,753,620/1,073,741,823. The package's smaller sample is reported separately and does not replace that exhaustive count.

Version and seed model. NMHASH32 v2 uses a 32-bit seed and returns 32 bits. Verification is 0x12A30553. The last algorithmic change was 2021-06-08; the 2021-06-09 commit changed the version label, and the December 2024 undefined-behaviour fix preserved verification values. The new timings use scalar code on M2 Pro and Advanced Vector Extensions 512 (AVX-512) on Xeon; the reproduction is scalar. The M2 Pro SMHasher3 binary fails NMHASH's built-in verification (0x4B575DFB, expected 0x12A30553; speed-table footnote ‡), so its M2 figures time a mis-built variant and are indicative only; the shipped reproduction and a scalar build of the upstream header both reproduce 0x12A30553, so the pair result is unaffected.

Prior work.NEW: no prior literature is identified in the supplied checked record. Statistical failures in SMHasher3 and rurban are recorded separately from this fixed same-seed pair.

* Not verified (search program only): the proposed exclusion of L ≤ 7, the 8-byte fold histogram, the 24-byte null search (0/232; resolution 2-32), and the 1,251-cell generic scan at 226seeds per cell (resolution about 2-26). No optimality claim is made.

Verbatim official wording and checked source record

32bit hash, the core loop is constructed of invertible operations, and the multiplications are limited to `16x16->16`. For better speed on short keys, the limitation is loosen to `32x32->32` multiplication in the `NMHASH32X` variant when hashing the short keys or avalanching the final result of the core loop. | Both hashes are the same high quality, and pass the checking:

- [rurban/smhasher](https://github.com/rurban/smhasher), including LongNeighbors and BadSeeds
- [demerphq/smhasher](https://github.com/demerphq/smhasher/)
- [massive collision tester](https://github.com/Cyan4973/xxHash/tree/dev/tests/collisions), 1G, len=8,16,256

README.md, section `NMHASH32`/`NMHASH32X` first paragraph and section '### Quality' (the only quality/collision statement in the repository), https://github.com/gzm55/hash-garage/blob/master/README.md (raw: https://raw.githubusercontent.com/gzm55/hash-garage/master/README.md). Design statement in rurban/smhasher issue #190 'Add NMHASH32' (gzm55, 2021-04-10): 'friendly to low profile hardware, using only narrow multiplications (16 x 16 -> 16), and 32bit addition, shift and xor'. The supplied audit found no statement about cryptographic strength, seeded security or adversarial inputs in the inspected files (README, nmhash.h, LICENSE, issue #2, rurban issues #190/#194).

NMHASH32 v2 (`#define NMH_VERSION 2`, nmhash.h line 18, set by commit bb223145cc 2021-06-09 which only changes '2-dev' to '2'; the last algorithmic change is 8dbdc6f9c5 2021-06-08 'improve speed for long keys', which set the verification values 0x12A30553/0xA8580227; the 2024-12-15 undefined behaviour (UB) fix by Reini Urban (7712708e68, merged e022156ca8) leaves them unchanged). Author James Z.M. Gao (gzm55/hash-garage, BSD 2-Clause). SMHasher3 'NMHASH' = 'nmhash32 v2', hashes/nmhash.cpp (ported 2022-03-26, dbd38eff), SRC_STABLEISH, FLAG_HASH_SMALL_SEED, verification_LE 0x12A30553; rurban nmhash32 0x12A30553 (same values in the nmhash.h header). Companion NMHASH32X is a separate row.

Reproduction.From Reproduction documentation, run inverify/nmhash32/:

cc -O2 -std=c11 -o nmhash32_verify nmhash32_verify.c -lm
./nmhash32_verify 20

This checks the SMHasher3 value, asserts the recorded outputs, prints the literal pair and samples exactly220seeds per case. Expected output and the distinction from the larger historical runs are in the README.

Selected score (nmhash32 v2): ≤ 4.994 bits.64/64 bytes;L = 8.1078944392/2^32(exhaustive). SeeThe collision score.

Try it in the browser
Load on view

Waiting to validate the verification program.

Run verify/nmhash32 locally

Records:Original project & code·Verifier package·Measurements

### nmhash32x v2pattern:P7

This variant has a separate pair whose changes cancel for every seed. The result concerns NMHASH32X’s own computation, rather than borrowing the count from NMHASH32.

w0 · bytes 0..3

Δ = 08008008

w1 · bytes 4..7

Δ = 08008008

seed

seed enters; ⊕ w1

w1

⊕ c2b2ae3d public

x

y

⊕

⊕

⊕ y

cancels in x

×

hi

C1 · public

×

×

hi

C2 · public

×

x

lo; ⊕ (x ≫ 23)

⊕

lo

⊕ rotl(y,4): Δ = 80080080

⊕ (x ≫ 12): Δ = 80000000

×

hi

C3 · public, odd

×

lo; ⊕ (x ≫ 12)

x: Δ = 80080000

y: Δ = 80080080

rotl 4

w5 · bytes 20..23

Δ = 80080000

w6 · bytes 24..27

Δ = 80080080

⊕; cancels here

⊕; cancels here

All products keep lo32; hi32 is discarded.

The independent (a,b) stream is unchanged.

Both x and y agree before the remaining fold.

nmhash32x’s controlled XOR trail becomes a top-bit difference through an odd public multiplier, then two tail words cancel both state differences for every seed.

01
// All arithmetic is 32-bit; R rotates left; every read is little-endian.

02
C1=0x11049a7d; C2=0xbcccdc7b; C3=0x065e9dad;

03
round(x,y,w0,w1,r):

04
 x ^= w0; y ^= w1; x ^= y;

05
 x *= C1; x ^= x>>23; x *= C2;

06
 y = R(y,r); x ^= y; x ^= x>>12;

07
 x *= C3; x ^= x>>12; return (x,y);

08
x=0xc2b2ae3d; y=seed; a=0x27d4eb2f; b=seed;

09
(x,y)=round(x,y,read32le(M,0),read32le(M,4),4);

10
(a,b)=round(a,b,read32le(M,8),read32le(M,12),3);

11
// len=28: ((len-1)&8) != 0 and ((len-1)&4) == 0.

12
a ^= read32le(M,16)+b; a ^= a>>16; a *= 0xa52fb2cd;

13
a ^= a>>15; a *= 0x551e4d49;

14
x ^= read32le(M,20); y ^= read32le(M,24);

15
x ^= y; x *= C1; x ^= x>>23; x *= C2;

16
x ^= R(y,3); x ^= x>>12; x *= C3;

17
x ^= 28; x ^= R(a,27); x ^= x>>14;

18
return x * 0x141cc535;

Code:hash-garage(nmhash.h, NMH_VERSION 2, HEAD e022156, 2024-12-15);SMHasher3 hashes/nmhash.cpp, nmhash32x v2, at SMHasher3 commit7ad8939d(file unchanged at 3b619371); local copy:sources/nmhash.cpp. Excerpt: NMHASH32X_9to255, specialized to the selected 28-byte path.

The first two words differ byΔ = 0x08008008. Their changes cancel inx ^= yon line 4, then re-enter on line 6 asR(Δ,4) = 0x80080080. The next XOR shift maps that to exactly0x80000000. Multiplication by odd C3 preserves this top-bit XOR difference for every value, and line 7 leaves x differing by0x80080000. The tail words on line 14 cancel x and y before the remaining fold; the independent a,b stream is unchanged. The trail therefore holds for every seed.

nmhash32x v2 — NEW.Fixed messages and a uniformly hidden API seed; No prior literature identified in the supplied checked record.

M = hex("00000000000000000000000000000000000000000000000000000000") // 28 bytes
M' = hex("08800008088000080000000000000000000000000000088080000880") // 28 bytes
seed = 0x00000000
H(M,seed) = H(M',seed) = 0xdc5952ce

Examples and output variants.0x00000000 -> both dc5952ce; 0x00000001 -> both b4e64737; 0xdeadbeef -> both e79bc644; 0xffffffff -> both a0a1d8b2 (all reproduced by the verifier); verifier's own 0xc78b9a30 -> both 73b04a67.

The independent verifier re-derived the trail, sampled2^20and2^30seeds without a counterexample, and exhaustively counted 4,294,967,296/4,294,967,296 collisions. With 28 bytes,L = 4andε = 1give score ≤ 2. Confirmed 32- and 33-byte variants are retained in the source record; the 28-byte pair is selected here.

Version and seed model.NMHASH32X v2 is a separate function from NMHASH32, with 32×32 short-key multiplication, a 32-bit seed, 32-bit output and verification 0xA8580227. It has its own row and witness. Its statistical failures and host-specific timings must not be merged with NMHASH32’s. The new timings use scalar code on M2 Pro and AVX-512 on Xeon.

Prior work.NEW: the supplied checked record identifies no prior literature for this deterministic short-path trail.

* Not verified (original implementation only): the proposedL ≤ 3impossibility argument and the 1,251-cell generic scan at2^26seeds per cell (resolution about2^-26). The score is a witnessed cap, not a proof of optimality.

Verbatim official wording and checked source record

Both hashes are the same high quality, and pass the checking:

- [rurban/smhasher](https://github.com/rurban/smhasher), including LongNeighbors and BadSeeds
- [demerphq/smhasher](https://github.com/demerphq/smhasher/)
- [massive collision tester](https://github.com/Cyan4973/xxHash/tree/dev/tests/collisions), 1G, len=8,16,256 | `NMHASH32X` is a variant of `NMHASH32`, which mixes short keys with 32x32->32 `MUL`, and improve the speed of short keys.

README.md section '### Quality', https://github.com/gzm55/hash-garage/blob/master/README.md; rurban/smhasher issue #194 'Add NMHASH32X variant of NMHASH32', opening post by gzm55, 2021-04-22, https://github.com/rurban/smhasher/issues/194. The supplied audit found no security statement in the inspected sources.

NMHASH32X v2, additional variant of NMHASH32 from the same nmhash.h (32x32->32 multiplies for short keys and the final avalanche); SMHasher3 'NMHASHX' = 'nmhash32x v2', hashes/nmhash.cpp, SRC_STABLEISH, FLAG_HASH_SMALL_SEED, verification_LE 0xA8580227; rurban nmhash32x 0xA8580227 (added via rurban/smhasher issue #194, 2021-04-22). This variant has its own pair and row.

Reproduction.From Reproduction documentation, run inverify/nmhash32x/:

cc -O2 -std=c11 -o nmhash32x_verify nmhash32x_verify.c -lm
./nmhash32x_verify 20

This checks the SMHasher3 value, asserts the recorded outputs, prints the literal pair and samples exactly220seeds per case. Expected output and the distinction from the larger historical runs are in the README.

Selected score (nmhash32x v2): ≤ 2 bits.28/28 bytes;L = 4. 1 (every seed). SeeThe collision score.

Try it in the browser
Load on view

Waiting to validate the verification program.

Run verify/nmhash32x locally

Records:Original project & code·Verifier package·Measurements

### mx3 v3pattern:P2·P5

Two messages of different lengths are chosen so that their data cancels the length difference inside the hash. They then collide regardless of the seed.

w0 · byte 0 (padded)

or bytes 0..7

C · public

bea225f9eb34556d

×

hi

w0

× C

×

hi

lo; ⊕ (x ≫ 39)

× C

lo = g(w0)

g(len + 1) · public

×

hi

× C

C public

+

+ g(w0)

+ lo

Q = g(w0) + C·g(len+1): cancels here

×

hi

Q

C · public

seed

× C²

×

hi

C² public

+

lo

lo; +

equal state

All high halves discarded; the final mix is common.

mx3’s one-byte and eight-byte inputs cancel their public length and word terms, leaving the same seed·C² contribution and hence the same state for every seed.

01
// Arithmetic modulo 2^64; words and a partial tail are read little-endian.

02
C = 0xbea225f9eb34556d;

03
g(w): w *= C; w ^= w>>39; return w*C;

04
stream(h,w) = (h+g(w))*C;

05
mix(h):

06
 h ^= h>>32; h *= C; h ^= h>>29; h *= C;

07
 h ^= h>>32; h *= C; return h ^ (h>>29);

08
h = stream(seed, len(M)+1);

09
for each full 8-byte word w: h = stream(h,w);

10
if a partial word remains: h = stream(h, zero_pad_le(tail));

11
return mix(h);

12
// For 1..8 bytes, exactly one message step follows line 8:

13
// h_before_mix = seed*C^2 + g(len+1)*C^2 + g(word)*C.

Code:mx3v3.0.0 (upstream tag 48924ee7, still master HEAD); pseudo-code fromSMHasher3 hashes/mx3.cppat SMHasher3 commit7ad8939d(unchanged through main 3b619371); local copy:sources/mx3.cpp. Excerpt: revision 3 mix_stream, initialization and finalizer; the unrolled loop is four sequential stream steps.

Every message term in lines 8–10 goes through the public bijection g. The one-byte and eight-byte paths each perform exactly one message step, so their seed terms in line 13 are identical. Setw = g⁻¹(g(0) + C·(g(2) − g(9))) = 0x5c26a409b8e3cbb6; the remaining public terms are then equal too. The bijective finalizer cannot separate equal states. The verifier independently reconstructed partners for all 256 one-byte messages.

mx3 v3 — NEW.Fixed messages and a uniformly hidden API seed; No prior literature identified in the supplied checked record.

M = hex("00") // 1 bytes
M' = hex("b6cbe3b809a4265c") // 8 bytes
seed = 0x2cb0f69f4abea221
H(M,seed) = H(M',seed) = 0x730d2d8dbe4d729e

Examples and output variants.0x2cb0f69f4abea221 -> both 730d2d8dbe4d729e; seed 0 -> both 424c78f4f12f7ff4; seed 1 -> both 01144efd26493619; seed 0xffffffffffffffff -> both d8c06c982066af91 (all reproduced by the verifier's own implementation and by the linked SMHasher3 reference library). 7-byte pair: 0x3bb548a553e612ba -> both eebfade252d2c35f; seed 0 -> both 35dd1592d75f49c2.

The verifier measured 1,073,741,823/1,073,741,823 collisions for the selected pair (three threads, floor(230/3) seeds each, so 230- 1 trials), reproduced verification 0x7B287B65, and compared 200,000 inputs against the SMHasher3 reference without mismatches; a 2026-09-18 rerun of verify/mx3 and of a driver including the upstream mx3.h gave 1,073,741,824/1,073,741,824 for both pairs. Algebra proves ε = 1 and L = 1, hence score 0, the metric floor. Its separately verified seven-byte-versus-eight-byte pair also has score 0.

Version and seed model.This is mx3 v3.0.0, tag 48924ee7, with a 64-bit seed. rurban’s mx3 entry tests v1.0.0 (0x4DB51E5B) with a 32-bit seed cast to 64 bits; its GOOD label and older bad-seed result do not describe the attacked v3.

Prior work.NEW: the supplied checked record identifies no prior literature. The known seed-equals-length zero-hash case concerns v1/v2. The v3 pair here does not depend on learning or choosing the seed.

No generic scan was run because the selected confirmed pair already reaches the metric floor. The equal-length 16-byte pair was re-checked against the upstream header in a separate driver, not part of verify/mx3; it collides for every seed and has a 1-bit cap at L = 2. The broader word-count characterization remains a report of the original implementation. Neither is used for scoring.

Verbatim official wording and checked source record

Repo with non-cryptographic bit mixer, pseudo random number generator and a hash function. The functions were found semi-algorithmically as detailed in those posts: | * mx3::hash passes all [SMHasher](https://github.com/rurban/smhasher) tests | [Version 3](https://github.com/jonmaiga/mx3/releases/tag/v3.0.0) improves mx3::hash with better seeding and speed while maintaining the same good quality. | This work is to a large degree empirical without much theoretical attention. It would be interesting to know more of what properties and weaknesses mx3 has, so please don't hesitate to let me know!

README.md first paragraph (raw line 2), section 'Quality' third bullet, section 'Version 3', section 'Feedback', https://github.com/jonmaiga/mx3 (raw: https://raw.githubusercontent.com/jonmaiga/mx3/master/README.md); release v3.0.0 body 'Improves mx3::hash in terms of speed and seeding.'; pull request (PR) #1 'Better seeding and faster stream mixer' (jonmaiga, 2022-04-13): '- Avoid obvious bad seeds when data length == seed'; blog http://jonkagstrom.com/mx3/index.html (2020-08-10): 'For hashing pass all SMHasher tests' (section 'Goals'); the quotes 'At first, the idea I outlined above...' and 'With this it passed all the SMHasher tests' sit inside the 'mx3::hash outline' section. No collision-probability, universality or security claim anywhere; the Rust port mx3-rs (chfoo) says 'The crate is *not* intended for cryptographically secure purposes.'

mx3 v3.0.0 (tag 48924ee7 = master HEAD, released 2022-04-19T12:33:59Z; repo last pushed 2022-04-19; v1.0.0 = 3368253, tag commit dated 2020-08-11 while the mx3.h header says 2020-08-13 -- clarified; v2.0.0 = d34470f 2020-10-22). Author Jon Maiga, CC0. SMHasher3 'mx3.v3', hashes/mx3.cpp (SRC_ACTIVE; v3 added 2022-08-18 commit 09beb3f2), verification_LE 0x7B287B65 (mx3.v2 0x527399AD, mx3.v1 0x4DB51E5B). rurban 'mx3' pins the submodule at 3368253 = v1.0.0 (0x4DB51E5B) and passes a uint32_t seed cast to uint64_t.

Reproduction.From Reproduction documentation, run inverify/mx3/:

cc -O2 -std=c11 -o mx3_verify mx3_verify.c -lm
./mx3_verify 20

This checks the SMHasher3 value, asserts the recorded outputs, prints the literal pair and samples exactly220seeds per case. Expected output and the distinction from the larger historical runs are in the README.

Selected score (mx3 v3): 0 bits.1/8 bytes;L = 1. 1 (every seed). SeeThe collision score.

Try it in the browser
Load on view

Waiting to validate the verification program.

Run verify/mx3 locally

Records:Original project & code·Verifier package·Measurements

### mir (exact and inexact)pattern:P2

Both selected messages contribute the same zero value to the seeded state. That makes them collide for every seed in both studied implementations.

w0 · bytes 0..7

0 ↔ 3cc02a2b092b150b

p1 · public

65862b62bdf5ef4d

×

w0

× p1

+

lo

hi

Exact: lo + hi is 0 or 2⁶⁴, hence term = 0.

Inexact: split w0 = (vH,vL), p1 = (pH,pL)

×

hi = 0

vL

pH public

lo64 → LH

×

hi = 0

vH

pL public

lo64 → HL

×

hi = 0

vH

pH public

lo64 → HH

×

hi = 0

vL

pL public

lo64 → LL

+

+ LH

+ HL

rm = LH + HL mod 2⁶⁴

HH + (rm ≫ 32) + LL + (rm ≪ 32)

mod 2⁶⁴ also gives term = 0: cancels here

All four 32×32 products have hi64 = 0.

seed

+ 8

r = seed + 8

⊕

r

⊕ public term = 0

equal r

The remaining keyed-state updates are common.

mir’s eight-byte words give the same zero public term in both exact and inexact multiplication, so the seeded state is identical for every seed.

01
// Arithmetic modulo 2^64. Exact products themselves have 128 bits.

02
p1=0x65862b62bdf5ef4d; p2=0x288eea216831e6a7;

03
mum_exact(v,p) = lo64(v*p) + hi64(v*p);

04
mum_inexact(v,p):

05
 (v1,v2)=(hi32(v),lo32(v)); (p1,p2)=(hi32(p),lo32(p));

06
 rm = v2*p1 + v1*p2; // 64-bit sum: its top carry is dropped.

07
 return v1*p1 + (rm>>32) + v2*p2 + (rm<<32);

08
r = seed + len(M); // Only seed entry; choose one mum variant throughout.

09
for each full 16-byte block (w0,w1):

10
 r ^= mum(w0,p1); r ^= mum(w1,p2); r ^= mum(r,p1);

11
if at least 8 bytes remain: r ^= mum(read64le(next8),p1); consume 8;

12
if 1..7 bytes remain:

13
 tail=0; start=0;

14
 if tail_len>=4: tail=uint64(read32le(tail_bytes))<<32; start=4;

15
 for i=start..tail_len-1: tail=(tail>>8) | (uint64(tail_bytes[i])<<56);

16
 r ^= mum(tail,p2);

17
r ^= mum(r,p1); r ^= mum(r,p2);

18
return r;

Code:mir;SMHasher3 hashes/mum_mir.cpp, mir.exact / mir.inexact; arithmetic since 2019-04-09; tested at SMHasher3 commit7ad8939d; local copy:sources/mum_mir.cpp. Excerpt: mir_hash and mir_round, with both forms of the multiply-and-add fold. Arithmetic wraps at the stated word width.

For eight-byte messages, the only message term is the publicmum(w,p1)on line 11. The second word isp1⁻¹ mod (2^64−1) = 0x3cc02a2b092b150b. Its exact product halves sum to2^64, hence the folded term is zero, just as for w = 0. Direct evaluation of lines 4–7 also gives zero for this word in the inexact variant. The states after line 11 are therefore equal for every seed in both variants. This extends the paper’s MUM public-term collision to the MUM-derived mir function.

mir (exact and inexact) — EXTENSION —Ahle and Knudsen 2026.Fixed messages and a uniformly hidden API seed; Extension of the paper’s MUM public-term result to the MUM-derived mir_hash.

M = hex("0000000000000000") // 8 bytes
M' = hex("0b152b092b2ac03c") // 8 bytes
seed = 0x910a2dec89025cc1
H(M,seed) = H(M',seed) = 0x5e900c9f273619d2

Examples and output variants.0x910a2dec89025cc1 -> both 5e900c9f273619d2 (exact and inexact); seed 0 -> both 1e30aaaa9235e65a (exact) / both 1e30aaaa9235e65b (inexact); seed 1 -> both 38d782429014d4bf (both variants); seed 0xfffffffffffffff8 (seed+len = 0) -> both 0 (all reproduced bit-for-bit by the verifier). 16-byte pair: 0x22118258a9d111a0 -> both 4d337930c595fdd0 (exact) / both 66c4631e3e47d736 (inexact); seed 0 -> both fd26864d6d50b5b1 (exact).

The independent verifier measured 1,073,741,824/1,073,741,824 collisions per variant, with checks against both SMHasher3 verification values. Public-term equality provesε = 1. The eight-byte pair hasL = 1and score 0. The independently verified 16-byte pair at the p2 site also collides for every seed and has score 1; it is included in the program.

Version and seed model.mir has no algorithm version number; its arithmetic is unchanged since April 2019. SMHasher3 mir.exact (0x00A393C8) and mir.inexact (0x422A66FC) are output-equivalent to upstream mir_hash and mir_hash_strict on little-endian hosts. The strict fold drops one cross-product carry; it does not drop every carry. The 64-bit seed is passed verbatim, including seed+len = 0; SMHasher3’s inexact seed-fixup is a harness option, not the API model here. The chart uses only mir.exact timings from the two-host benchmark.

Original: Thomas Ahle and Jakob Knudsen, “Fast Evaluation of Polynomials with Rational Preprocessing”, 2026 manuscript (paper). The paper’s MUM public-term collision mechanism is reproduced in the MUM-derived mir function; the new eight-byte and 16-byte pairs here collide for every seed in both the exact and inexact variants. The supplied record finds no earlier mir_hash-specific literature; that does not make the underlying MUM mechanism new. The VMUM/MUM-V3 issue and later collision-prevention default concern other functions.

* Not verified (original implementation only): the 24-byte variant and the seven-byte-versus-eight-byte half-seed pair. Neither is used in the table, chart or score. No generic scan was run after reaching the metric floor.

Verbatim official wording and checked source record

Simple high-quality multiplicative hash passing demerphq-smhasher,
 faster than spooky, city, or xxhash for strings less 100 bytes.
 Hash for the same key can be different on different architectures.
 To get machine-independent hash, use mir_hash_strict which is about
 1.5 times slower than mir_hash. | File `mir-hash.h` is a general, simple,
 high quality hash function used by hashtables

mir-hash.h lines 6-10 (file header comment), https://github.com/vnmakarov/mir/blob/master/mir-hash.h; README.md section 'Structure of the project code', lines 310-311, https://github.com/vnmakarov/mir/blob/master/README.md. No security, DoS, hash-flooding or cryptographic claim or disclaimer for mir_hash anywhere (the words crypt/secur/attack/collision/flood do not occur in mir-hash.h or the mir README). The parent MUM's README says 'MUM hash is a **fast non-cryptographic hash function**' (line 25), '[V]MUM is not designed to be a crypto-hash' (lines 237-238) and, at lines 1-2, '# **Update (Nov. 28, 2025): Implemented collision attack prevention in VMUM and MUM-V3**' (Issue #18), which did not touch mir_hash.

mir_hash from vnmakarov/mir mir-hash.h (no version number; arithmetic unchanged since commit 334c14e78b 2019-04-09 'Speedup mir hash. Impelement strict hash.', after 6ad0fc6784 2019-04-08 'Rename mir-mum.h to mir-hash.h. Rename mum to mir. Use simpler hash function.'; later commits change platform detection (baab39e9f1 2019-11-01, 71364bf3d1 2020-09-29), constant names (86d5234268 2023-05-02) and copyright, last bd0e9d7a72 2024-05-15, header 'Copyright (C) 2018-2024 Vladimir Makarov' from 'cosmetic only'). MIR releases v0.1.0 2021-08-12 ... v1.0.0 2024-05-27 (latest); repo HEAD a8ab7c31cd 2026-06-19. SMHasher3 hashes/mum_mir.cpp (imported 2022-01-18, 7087ce7a; family SRC_FROZEN, src_url mum-hash): 'mir.exact' = relaxed mir_hash (__int128 hi+lo fold, verification 0x00A393C8) and 'mir.inexact' = mir_hash_strict (32x32 partial products with one dropped carry from 'no carries', 0x422A66FC); output-equivalent to mir-hash.h on little-endian hosts, not line-for-line. rurban 'mirhash' (MIR_VERIF conditional: 0x00A393C8 under __GNUC__ && UINT_MAX != ULONG_MAX, else 0x422A66FC) and 'mirhashstrict'. One pair breaks both variants.

Reproduction.From Reproduction documentation, run inverify/mir/:

cc -O2 -std=c11 -o mir_verify mir_verify.c -lm
./mir_verify 20

This checks the SMHasher3 value, asserts the recorded outputs, prints the literal pair and samples exactly220seeds per case. Expected output and the distinction from the larger historical runs are in the README.

Selected score (mir.exact / mir.inexact): 0 bits.8/8 bytes;L = 1. 1 (every seed). SeeThe collision score.

Try it in the browser
Load on view

Waiting to validate the verification program.

Run verify/mir locally

Records:Original project & code·Verifier package·Measurements

### fasthash (32- and 64-bit)pattern:P2·P5·P7

Including the input length does not help if a message change can cancel it. The seven- and eight-byte inputs below do exactly that, affecting both output widths.

w0 · bytes 0..6

or bytes 0..7

zero-pad the 7-byte tail

C · public

2127599bf4325c37

×

hi

⊕ (w0 ≫ 23)

× C

lo; ⊕ (x ≫ 47)

mix(w0)

m · public

880355f21e6d1965

×

hi

× m

len = 7 / 8

seed

⊕ seed

lo

h = seed ⊕ len·m

⊕

mix(w0)

⊕ h

7m ⊕ mix(0) = 8m ⊕ mix(w0′)

The difference cancels here, including length.

×

hi

equal word

m · public

lo

equal h → common 64-bit mix / 32-bit fold

fasthash’s public word mix cancels the different length terms before the common multiplication, merging the seeded state for both output widths.

01
// Arithmetic modulo 2^64, except the final uint32 conversion.

02
m=0x880355f21e6d1965; C=0x2127599bf4325c37;

03
mix(x): x ^= x>>23; x *= C; return x ^ (x>>47);

04
h = seed ^ (len(M)*m);

05
for each full little-endian word w: h = (h ^ mix(w))*m;

06
if 1..7 bytes remain: h = (h ^ mix(zero_pad_le(tail)))*m;

07
h = mix(h);

08
return h; // fasthash64

09
// fasthash32 instead returns uint32(h - (h>>32)).

10
// Lengths 1..8 all take exactly one of lines 5 and 6.

Code:fast-hash;SMHasher3 hashes/fasthash.cpp, 32- and 64-bit, 08a25db2; tested at SMHasher3 commit7ad8939dand re-checked against SMHasher3 HEAD 3b619371 (2026-08-27; hashes/fasthash.cpp unchanged since db13e8c1, 2023-11-02) and upstream HEAD ae4eca64 (fasthash.c unchanged since 08a25db2; all later commits are README-only; an open, unmerged portability PR #4, 2026-06-05, keeps the same constants and seed injection); local copy:sources/fasthash.cpp.

The seed enters on line 4, but every message word first passes through the public bijection mix. Seven zero bytes and an eight-byte word both take one message step. Choosingw = mix⁻¹(7m XOR 8m) = 0xf375d1d1e77b175ecancels their length terms before multiplication. Both states entering line 7 are identical for every seed; the 32-bit fold on line 9 preserves equality. For equal lengths, two words with mix difference2^63cancel across the odd multiplier m, giving a separately verified 16-byte pair.

fasthash (32- and 64-bit) — NEW.Fixed messages and a uniformly hidden API seed; No prior literature identified in the supplied checked record.

M = hex("00000000000000") // 7 bytes
M' = hex("5e177be7d1d175f3") // 8 bytes
seed = 0x0123456789abcdef
H(M,seed) = H(M',seed) = 0x3f624b9140899669

Examples and output variants. 0x0123456789abcdef -> fasthash64 3f624b9140899669 for both (SMHasher3 fasthash-32 with the same 64-bit seed: 01274ad8 for both; upstream fasthash32 truncates the seed to 0x89abcdef and returns 1188bc14 for both); seed 0xc05a677850dc981a -> both 875005bd11563f7a; seed 0 -> both 78ef6597ace64ee2 (all reproduced by the verifier). Equal-length pair: 0x0123456789abcdef -> both 1ac53b33e0d7dd39; seed 0 -> both 52b6455608a72a7f; 0xc05a677850dc981a -> both f1c750f15e01b5a6.

The independent verifier measured 1,073,741,824/1,073,741,824 collisions at both output widths for the selected seven-byte-versus-eight-byte pair, and a 2026-09-18 re-run linked against the upstream fasthash.c at HEAD gave 1,073,741,824/1,073,741,824 for each of the three pairs (7/8-byte, 16-byte, 1/8-byte) at both output widths, fasthash64 under a uniform 64-bit seed and fasthash32 under a uniform 32-bit seed. The one-step identity proves eps = 1, L = 1, score 0. The equal-length 16-byte pair was independently checked on 4,294,967,296 seeds and has score 1. A later check linked directly against the unmodified upstream fasthash.c (ztanml/fast-hash HEAD ae4eca64) enumerated all 232seeds of the upstream uint32_t fasthash32 API: 4,294,967,296/4,294,967,296 collisions for both pairs; the 64-bit-seed model remains proven plus sampled (230splitmix64 seeds: 1,073,741,824/1,073,741,824).

Version and seed model.The unversioned fast-hash code is pinned to upstream commit 08a25db2 (2018-10-22). SMHasher3 verification is 0xA16231A7 at 64 bits and 0xE9481AFC at 32 bits. Its wrappers pass a 64-bit seed to both widths; upstream fasthash32 takes a 32-bit seed. The every-seed identity covers both models, which the reproduction program measures separately.

Prior work. NEW: we are not aware of any prior publication of fixed-pair, seed-independent collisions for fast-hash; the closest remark is the comment at line 37 of rurban/smhasher's fasthash.cpp that an empty key exposes the seed through the mix inverse (a seed-recovery observation, not a collision).

No generic scan was run after reaching the metric floor. A shorter pair of the same kind, one byte 00 versus eight bytes 2cb6512f74662d63, also collides for every seed (230/230uniform 64-bit seeds for fasthash64 and 230/230uniform 32-bit seeds for fasthash32, linked against the upstream fasthash.c at HEAD, 2026-09-18) and does not change the score.

Verbatim official wording and checked source record

The fast-hash is a simple, robust, and efficient general-purpose hash function. | Robust - Passes all tests of SMHasher(http://code.google.com/p/smhasher). | The fast-hash was tested using the SMHasher(http://code.google.com/p/smhasher), which is known as the "DieHarder" hash testing. The test results show that the fast-hash is a better choice than Google MurmurHash2 (slightly biased and slower than the fast-hash), Jenkins hash function (moderately biased and notably slower than the fast-hash), and a few other popular ones such as Bernstein, CRC, SDBM, FNV, and etc. | Yes, you can use any hardcoded integer number like 0xdeadbeef as the seed.

README.md lines 3, 6 and 67 ('## Results', 2012 original SMHasher; the embedded FastHash64 log has no FAIL lines), https://github.com/ztanml/fast-hash/blob/master/README.md; issue #1 'how do I seed fasthash ?' (lucasart, 2019-12-22), author reply by ztanml 2020-01-17 (the only seed guidance; no secrecy requirement), https://github.com/ztanml/fast-hash/issues/1. README line 20 cites O'Neill's PCG paper ('one of the best general-purpose integer hash functions', a pseudorandom number generator (PRNG)-quality remark, Section 9). No statement about collision resistance, seed secrecy, hash flooding or cryptographic strength anywhere (README, headers, comments, issues #1-#3, PR #4). Third-party: rurban's harness comment fasthash.cpp line 37 '// security: if the system allows empty keys (len=3) the seed is exposed, the reverse of mix.'

fast-hash (ztanml/fast-hash; 'Copyright (C) 2012 Zilong Tan', originally Ulib's FastHash at code.google.com/p/fast-hash; unversioned: 0 tags, 0 releases, single code commit 08a25db2 'init' 2018-10-22, six README-only commits, last ae4eca64 2023-04-23; MIT text in the sources, GitHub license field null; repository description 'Fast hash function learned using genetic programming'). SMHasher3 hashes/fasthash.cpp 'fasthash-64' (verification_LE 0xA16231A7) and 'fasthash-32' (0xE9481AFC; = h - (h>>32) of the same 64-bit value, so every 64-bit collision is a 32-bit collision), SRC_STABLEISH, last touched db13e8c1 (authored 2023-11-02, committed 2023-11-17). rurban fasthash64 / fasthash32.

Reproduction.From Reproduction documentation, run inverify/fasthash/:

cc -O2 -std=c11 -o fasthash_verify fasthash_verify.c -lm
./fasthash_verify 20

This checks the SMHasher3 value, asserts the recorded outputs, prints the literal pair and samples exactly220seeds per case. Expected output and the distinction from the larger historical runs are in the README.

Selected score (fasthash-64): 0 bits.7/8 bytes;L = 1. 1 (every seed). SeeThe collision score.

Selected score (fasthash-32): 0 bits.7/8 bytes;L = 1. 1 (every seed). SeeThe collision score.

Try it in the browser
Load on view

Waiting to validate the verification program.

Run verify/fasthash locally

Records:Original project & code·Verifier package·Measurements

### UMASH-64/128: both headline bounds provedpattern:ungrouped

Records:Original project and code·Collision bounds (PDF)·Measurements

Both published UMASH headline bounds are proved for ideal full keys, a fixed seed and the C architecture. The new proofs give a 56.18-bit score for UMASH-64 and 83.99 bits for UMASH-128 on L ≤ 246words. They use different routes from the paper; its intermediate projection step remains unvalidated.

The published gap remains.With q = 264and p = 261−1, the paper’s 162/q projected-identity step does not follow from its raw collision bound and reduction fibre sizes. An XOR-differential bound cannot be transferred to a different additive group that way. The finite counterexample in the compiled paper invalidates that inference, without refuting the headline bounds.

The 64-bit route: keep the implemented accumulator.The primary hash retains its accumulator modulo8p = 264−8, preserving three bits beyond reduction modulo p; this follows fromumash_reference.pyandumash.cfor every length ≥ 9 bytes. In the exceptional one-chunk final-block case, projected identities leave an accumulator difference fjp modulo 8p, so a full collision additionally requires8 | fj. A plain final reduction modulo p would lose this condition and would not give the bound by this route. The ≤8-byte branch is handled separately; distinct short inputs of equal length never collide.

The primary envelope.Measure L in eight-byte words. Set A = 205/(264−561), S = 435/(264−561) + 2/(261−3), and ρ(L) = min(1, 2⌈L/32⌉/(261−3)). Then ε(1) = 1/(264−561) andε(L ≥ 2) = max{A + (1−A)ρ(L), S}. In particular, Pr[collision] <58·⌈L/512⌉/261, proving the published headline 64·⌈L/512⌉/261= ⌈s/4096⌉·2−55for byte length s = 8L. The fine envelope scores56.18 bits at L = 2under both fixed-length and at-most-length conventions.

The fingerprint route: two independent multipliers.The C architecture shares 34 OH words between its two compressors but uses two independent polynomial multipliers. Conditional on the shared OH key, the comparison polynomials are fixed, so their root probabilities multiply; the compressors themselves are never assumed independent. Marginal and joint identity bounds givePr[collision] < (81/128)·⌈L/223⌉²·2−83, proving the published fingerprint headline independently of the primary-hash proof.

The finer fingerprint envelope.Put a = 732757/(q−561), b = 1416246956032/(q(q−561)), and use ρ above. Then E(1) = 1/(q(q−561)) andE(L ≥ 2) = b(1−ρ)² + aρ(1−ρ) + ρ². This gives a score of83.99 bits on L ≤ 246(the display “84” is rounded),88.63 bits through 64 MiB, and approximately69.0 bits on L ≤ 261−1(strictly between 68.99 and 69). The published formula scores approximately 83 on the row’s domain and 68 on the full byte-length domain. The coarse 81/128 refinement scores 83.66 on the row’s domain; the plotted score comes from E.

Bounds at representative lengths.UMASH-64 gives −log₂ ε =55.18 / 47.995 / 38.000at 1 KB / 1 MB / 1 GB (210/ 220/ 230bytes), compared with the published 55 / 47 / 37. The C fingerprint gives75.98 bits at 1 GB, compared with the published 75. These are collision-probability bounds without the score’s length adjustment. Both chart markers are solid proven guarantees.

Both open joint cases are now closed.The corrected ENH-only proof closesOpenENHOnly, including two-word changes at every valuation: 4721784/2128under IID OH words, still <2−105after distinct-word conditioning (exact certificates). The joint projection proof closesOpenPHENH: equal chunk counts and checksums, exactly one differing nonfinal PH chunk, both final ENH words differing, minimum valuation r = 1,…,63. Its bound is 170906186782/2128under IID words, still <2−90after distinct-word conditioning (exact certificates). Neither proof assumes independence of the completed compressors.

The Python single-multiplier fingerprint is refuted.ItsUmashKeycarries one polynomial multiplier, reused for the secondary output. Let A be 256 zero bytes and B be 256 bytes of 0x01. Atf = p−1 or f = 1, A‖B and B‖A collide in both outputs for every OH key and fixed seed. The f = p−1 fibre alone has probability 1/(p−2) ≈ 2−61in the reference multiplier model, refuting that variant’s 83-bit headline. The C architecture’s two independent multipliers are essential to its proved fingerprint bound. Proposition 11.1 and model checks.

Scope.Both theorems use theideal full-key distribution: 34 OH words sampled uniformly without replacement (IID also proved), a fixed seed, and independent uniform polynomial multipliers on {2,…,p−1}, one for the primary hash and two for the C fingerprint. The C library accepts f in {1,…,p−1}; the bounds hold a fortiori for uniform sampling on that range. Salsa20 expansion /umash_params_derive, its nonuniform OH-repair sampler, comparisons with different per-call seeds, and masked outputs are outside these theorems. Execution checks compared the C accumulator, finalizer, dispatch paths and incremental API against models on thousands of inputs; these checks are not a formal proof of every machine-code path.

Proof scope and machine-checked statements.The earlier Collision bounds (PDF) gave a 53.38-bit paper bound with primary marginal 3125/q (exact arithmetic); it is superseded for the plotted primary score, but that marginal remains an input to the independent fingerprint proof. The Lean completion record covers the46.52-bit envelope and ENH-only closure. The 53.38- and 56.18-bit refinements, approximately 84-bit fingerprint score and PH+ENH joint closure are verified paper proofs with exact certificates;the headline bounds are not yet machine-checked.

Disclosure.I openedUMASH issue #40on 18 September 2026 about the projection gap. Both headlines are now proved in the stated ideal-key C model, while the 162/q step remains unvalidated. The compiled paper gives both proofs and the Python reference discrepancy.

### HalftimeHash: corrected wrapper proofpattern:ungrouped

Records:Original project and code·Corrected bounds and repair (PDF)·Measurements·Verifier package

The public 64-bit functions have a corrected guarantee. Establishing it requires analyzing the surrounding length and output handling as well as the central calculation, under the listed execution assumptions.

The gap and its repair.Lemma 3 treats different encoded vectors as though every coordinate must differ: (0,0) and (1,0) show the problem. The corrected proof tracks joint events for coordinate subsets, with matrix-fibre bounds from 2-adic minors. The corrected proof gives the replacement bound 2−96(h+2)²(h+5), giving 83.27 bits at h=16 for the intended distance-3 construction, checked all 441 maximal minors of the four displayed matrices, and recorded paper errata.

The shipped Style wrappers.They use Encode2, whose distance is two. Their key overlap reaches the length tables but not the sixteen output-byte tables: the maximum core key index is 1834 and output tables start at 2048. Conditioning on that layout closes the independence gap under a flat-address, unsigned/modular-arithmetic execution contract. The compiled paper states the execution assumptions; the independent execution search found no overlap pair. This does not certify the literal header under every ISO-C++ optimization: its undersized array view and unmodified NEON dispatch have separate defects.

Bounds and domain.Let δ=2−64. The corrected proof bounds the equal-length core by (h+2)(h+3)·2−64, with h(N)=⌊log₈(7N+1)⌋−1 for complete groups; the wrapper adds its independent tabulation term δ+(1−δ)Pr[core collision]. Unequal lengths have probability at most 2−63−2−128. The normalized coefficient 2−2−64is optimal: 0x00 versus 0x01 attains it, giving my conservative 63-bit certificate.

The stack-safe domain is N<19,173,961 complete groups. The Style64/128/256/512 caps are respectively length <2,761,050,384 / 5,522,100,768 / 11,044,201,536 / 22,088,403,072 bytes. The compiled paper and execution harness specify the contract and caps. Lean M1–M5 compile for the corrected abstract scalar Style model, including flat key addresses and overlap; this gives partial implementation assurance. It does not prove the shipped C++/SIMD binary.

### HalftimeHash24 (advanced 24-byte API, Encode3)pattern:P3·P5

Records:Original project and code·Corrected bounds and repair (PDF)·Measurements·Verifier package

The original advanced function has an equal-length counterexample to its claimed guarantee: at most 36.4 bits, from a fixed 168-byte pair that collides whenever the top 32 bits of one key word are zero. Its raw core is fixed-length by design; the unequal-length identity that gives 0 bits is recorded in a note below.

NEW: an advertised bound refuted.The paper says,“For HalftimeHash24, and for strings less than an exabyte in length, this is more than 83 bits of entropy”, for same-length strings. The callableadvanced::V1<3>throughV4<3>produce 24 bytes; they are distinct from the public Style wrappers.

// b = 1: equal-length witness, L = 21 words
M = 168 zero bytes;
M' = M with little-endian word 6 = 1; // byte 48 = 0x01
// Full 24-byte outputs agree whenever high32(core_key[6]) = 0.
// Unequal-length witness, L = 1:
X = empty byte string; Y = hex("00"); // every key

Encode3’s parity generation fails to spread this word change: only one encoded symbol differs. The favourable key event has probability 2−32; at equal length, L=21 gives a score cap of 32+log₂21≈36.4 bits. Independent execution measured 76 collisions in 316,053,236,830 sampled key arrays across four scalar entry points, about 2−31.95, with central exact-Poisson 95% interval [2−32.30,2−31.63]; forcing the high word to zero yielded 268,435,456/268,435,456 collisions at every b. Counts, streams and interval · verification program.

Note on unequal lengths.The raw advanced core does not encode length: empty and one zero byte collide for every key (1,000/1,000 random key arrays checked; Style64 separated them 1,000/1,000). Used across lengths it would therefore be key-free at L=1, score 0. The core is fixed-length by design, so the row’s headline is the equal-length pair above; this identity is kept as a note only.

### ChainHash: one function, 64 random key bytes

Records:Project and code·Specification·Theorem and proof·Lean proofs·Measurements·Test suites

ChainHash is my 64-bit construction for hashing long messages with a collision guarantee: one function on every host, with a machine-checked 63.0-bit score from 64 independently random key bytes.

Three levels.Level 1 is reduced carry-less NH (CLNH) over logical 256-byte blocks, with comb pairs (wi, wi+8); four blocks interleave across each 1 KiB region rather than forming contiguous 256-byte slices. Level 2 evaluates the block values by Horner in an independent key word y, with the byte length as leading coefficient: P0=ℓ, Pt=yPt−1+ctin GF(264). Level 3 is an integer-add twist followed by a quintic finalizer. The flat long-input product loop follows Orson Peters’s PolymurHash lineage. Thespecificationdefines the comb, presence masks and key layout exactly.

One function, several evaluation strategies.The digest is independent of Horner stride k, SIMD width, lazy or eager reduction, streaming chunking and valid thread splits. The partial API joins region-aligned partitions; a split inside a region must preserve the comb’s block assembly. These are ways to evaluate the same polynomial, not host-specific hash definitions. The implementation’s property tests cover the portable, x86 and NEON paths, strides, reductions, streaming and two-thread joins; they do not replace a proof of all compiled code.

Key and bound.The key is 64 uniformly random bytes, read as eight field words s, y, c0…c4, τ; the block keys are the powers κm=sm+1. For two distinct messages fixed independently of the key, each at most 8L bytes long, ε ≤ min(1,(p(L)+d(L))/264). Here p(L) is the comb-block count: for Q=⌊(L−1)/128⌋ and u=1+((L−1) mod 128), p(L)=4Q+min(4,⌈u/2⌉). The term d(L) ≤ 32 bounds the number of keys s that can cancel one changed block: d(1)=1, d(L)=2 for L ≤ 8, and thetheoremgives the full envelope. It is smaller than the formal degree of the block difference because squaring is a bijection of the field. Since p(1)=d(1)=1, the score is63.0 bits at L=1, for fixed-length and at-most-length messages, including empty, partial-word and unequal-length inputs, for 1 ≤ L ≤ 261−1. The resident implementation caches 56 expanded words (448 bytes); this is distinct from the 64 random bytes. The benchmark’s SplitMix64 seed constructor is a different key distribution and is outside the theorem.

Machine-checked.The collision bound, the equality of the serial, k-lane and lazy evaluations for every stride, and the exact 63.0-bit minimum are proved inLean(89 theorems; standard axioms only). 464 test vectors agree between the C header and an independent Lean reference. Compiler correctness and the benchmark’s seed expansion are outside these theorems.

Measured.Under the post’s SMHasher3 protocol, ChainHash reaches28.31 B/cycle on Xeon 8375C(higher of two passes) and26.26 on M2 Pro(median of three). At 1–31 bytes it costs 155.14 cycles/hash on Xeon and 87.49 on M2, against 29.44 and 25.05 for XXH3-64 in the same binaries; the per-call setup and the three serial multiplications of the finalizer are not amortized on short inputs. It passes thecomplete SMHasher3 suite(200/200 on x86 and arm64) and the complete rurban SMHasher suite (All+BIC, 17/17 sections); the verification value is 0x66672BD6.

### ChainHash-128

Records:Project and code·Specification·Theorem and proof·Lean proofs·Measurements

ChainHash-128 is the 128-bit function: the same three levels over GF(2128), one function on every host, with a machine-checked 127-bit score from 128 independently random key bytes.

Construction.Level 1 is reduced CLNH over logical 512-byte comb blocks in GF(2128), the GCM field, with comb pairs (wi, wi+8) of 128-bit words; eight blocks interleave across each 4 KiB region. Level 2 evaluates the block values by Horner in an independent 128-bit key word y, with the byte length as leading coefficient, on k chains whose exact-count schedule returns the serial value. Level 3 is the integer twist modulo 2128and the quintic finalizer. Horner stride, SIMD width, schoolbook or Karatsuba products, lazy or eager reduction, streaming chunks and region-aligned thread splits leave the digest unchanged.

Key and bound.The key is 128 uniformly random bytes, read as eight field words s, y, c0…c4, τ, with κa=sa+1. For two distinct messages fixed independently of the key, each at most 8L bytes, ε ≤ min(1,(pB(L)+dB(L))/2128), where pB(L) is the logical 512-byte block count (eight blocks per 4 KiB region; thespecificationgives the exact count) and dB(L)=1 for L ≤ 16 and min(32, 2⌈L/32⌉) beyond: through 128 bytes a block difference is δ·s2, which has a single root. Both terms are 1 at L=1, so the score is127 bits, for fixed-length and at-most-length messages, including empty, partial-word and unequal-length inputs, for 1 ≤ L ≤ 261−1. At 1 GB, pB=221and the bound is about 2−107. The benchmark’s 64-bit seed expansion does not supply the 128 random bytes.

Machine-checked.The collision bound, evaluation independence for every stride and the exact 127-bit minimum are proved inLean(116 theorems; standard axioms only), and 625 test vectors agree between the C header and an independent Lean reference across the portable, XMM, YMM and ZMM backends, strides 1–8, eager and lazy reduction, and schoolbook and Karatsuba products.

Measured.SMHasher3 bulk on the Xeon 8375C is 14.43 B/cycle (higher of two passes) and 10.26 on the M2 Pro (median of three; no run more than 15% from its median). Controls in the same binaries, Xeon / M2: XXH3-128 19.82 / 12.53 and UMASH-128 6.02 / 7.52. Four-lane VPCLMULQDQ on ZMM carries the Xeon figure; the NEON loop is issue-bound rather than multiplier-bound. Short 1–31 B inputs cost 175.9 cycles/hash on Xeon and 167.9 on M2. Full SMHasher3 suite:188 of 188 tests pass(Xeon).

### HalftimeHash24: our fixed 24-byte core

Records:Original project and code·Corrected bounds and repair (PDF)·Measurements·Verifier package

This repair changes the message encoding and includes the input length explicitly. It has its own proof and measurements and should not be confused with either the original advanced function or the public 64-bit wrappers.

The fixed code implements the distance-3 encoder and appends the total byte length as the last scalar tail word under fresh terminal Toeplitz keys; it returns 192 bits. The construction theorem is machine-checked in Lean (M1–M4). We display the requested conservative 6804·2−96collision-bound label, 83.27 bits; this is not the exact normalized score (the source derives 96 bits), and the retained stack-safe domain actually has the stronger 972·2−96uniform bound. The old 2−32witness producedzero collisions in 236keys at each of four widths. The shipped 24-byte refutation remains in thechart data table.

This fix is ours, on branchfixed-24byte-coreingithub.com/thomasahle/HalftimeHash, and isnot yet upstream; the patch and verification report identify the exact code. Three-run median bulk/small results are Xeon 14.12 B/cycle / 79.42 cycles and M2 5.55 / 48.63. Relative to komihash, rapidhash and HalftimeHash-512 controls, respectively, the bulk ratios are Xeon 1.924× / 1.322× / 0.736× and M2 0.683× / 0.358× / 0.744×; small-key cost ratios are Xeon 2.951× / 2.872× / 0.940× and M2 1.963× / 2.371× / 0.770×. All runs and control ratios.

### Poly1305 and GHASHpattern:ungrouped

Poly1305 and GHASH show how polynomial hashing is used inside authentication systems. Here we compare their collision bounds and implementation speeds, while keeping the full protocols and benchmark key generators outside those mathematical claims.

The new Poly1305 and GHASH audit certifies the ideal-key bounds: Poly1305 retains the conservative 103-bit score from 8⌈bytes/16⌉/2106, and GHASH uses thesingle-stream, AAD-only127-bit bound (⌈bytes/16⌉+1)/2128, with byte lengths below 261. The cited two-stream envelope instead gives 126.4 bits. Both ideal byte-string families are machine-checked in Lean; their 64-bit-seeded benchmark wrappers do not inherit those bounds, and the audit exhibits a GHASH pair colliding for seed zero. GHASH timing remains an OpenSSL GMAC proxy including setup.

### SipHash-1-3 and SipHash-2-4pattern:ungrouped

SipHash targets a stronger problem: an attacker may learn from earlier results while choosing new inputs. Both variants are plotted at their 64-bit output width with hollow markers. These positions show unresolved claims, not proved collision guarantees.

Both use an add–rotate–xor permutation keyed by 128 bits. I include them as PRFs. I have no universality theorem or pair to score in this comparison. Their 1–31-byte and bulk timings are in thechart data table; both are shown as hollow, unresolved claims in the chart.

### Go runtime map hash / hash/maphash (go1.27.1, amd64 AES)pattern:P2

A fixed 15-byte string and a fixed 16-byte string collide for about one process key in 16.8 million. In those processes, changing the map seed does not help. The exact sufficient trail gives a 25-bit cap on this post’s score.

Claim and version.Thehash/maphash documentationsays hashes are “intended to be collision-resistant, even for situations where an adversary controls the byte sequences”; the package also disclaims cryptographic security. The 25-bit cap directly contradicts that adversarial-input intent, rather than a numerical guarantee: Go states none. This entry studiesgo1.27.1’s amd64 AES path.

Key model.The runtime draws a 128-byte AES key schedule once per process and a 64-bit seed per map;maphash.MakeSeedalso supplies a 64-bit seed. The experiment redraws both layers independently. Inputs up to 16 bytes use only the first 16 process-key bytes. The trail event depends on bytes 8, 10, 12 and 14 of that process key, so it holds for every map seed when those bytes satisfy the condition.

Relevant path.For 1–16 bytes, write F for an AES encryption round whose round key is its own input. The byte layout below is little-endian:

F(x) = AESENC(x, x)
X = LE64(map_seed) || LE16(length) repeated 4 times
S = F(X XOR process_key[0:16])
v = zero_pad_to_16(message) XOR S
return low64(F(F(F(v))))

Fixed pair, in hex.The lengths are 15 and 16 bytes, so L = 2:

m = 000000000000000000000000000000
m′ = a3fe5da3a3fe5da342a3bcfe42a3bcfe

Mechanism and score.Changing the length from 15 to 16 changes four bytes entering the single seed-state round. Each active AES substitution has four of 256 inputs giving the chosen output difference. These independent events have probability (4/256)4= 2−24. On that trail the state difference is exactly the displayed 16-byte message, so the message XOR cancels it and all later states agree. This is an exact sufficient collision event; it need not count every possible collision. Consequently log₂(L/ε) ≤ log₂(2/2−24) =25.0 bits.

Measurements.The independent AES-NI transcription found66 / 230collisions, giving a sampled score of 24.96 bits and central 95% Poisson interval[24.61, 25.33]. The real go1.27.1 runtime, with its global AES key redrawn inside the test, found20 / 228. The interval describes sampling uncertainty; it does not weaken the exact sufficient-trail cap. The 66-count run is the independent transcription, not a second real-runtime run.

Scope and qualifications.This covers string map keys andmaphash.String,maphash.Bytesand the corresponding byte-sequenceHashpath. Go byte slices are accepted bymaphash.Bytesbut cannot themselves be map keys. Integer map keys usememhash32/memhash64, different paths that are not scored here. The ARM64 AES path has a different differential: two observations in 233trials suggest about 2−32, but only under qemu, without ARM hardware confirmation. The no-AES fallback has no finding here. Neither receives the amd64 25-bit score or a timing paired with it.

Reproduction.The Go maphash verification package supplies the independent implementation, witness checks and runtime evidence. The timing record identifies the measured backend; absent host timings remain blank.

Records:Documentation and claim·Implementation studied·Verifier package·Measurements

### Abseil Hash (20260817.0)pattern:P2

The empty string and one fixed eight-byte string collide for every seed, giving a zero-bit cap. A same-length pair also exists. Abseil promises statistical mixing and changing hash values, and explicitly disclaims a security role for its seed.

Claim and version.TheSeed() commentsays: “It is not meant as a security feature right now”. Thepublic headerdescribes per-process variation and an avalanche target. The result contradicts no security promise. The audited 20260817.0 hash files agree with commit73d2688.

Key model.The process seed derives from an address, using address-space randomization rather than an independently sampled secret key; a non-PIE Linux build can make that address constant. SwissTable uses a five-bit per-table seed through its seeded hashing hook. The pair below is independent of both, so their actual distributions do not affect it. Separately, 32 possible table seeds provide at most five bits of table randomization: any nonzero collision probability over a uniform table seed is at least 1/32. This does not assert that every arbitrary pair collides, and the length-normalized score still includes log₂ L.

Relevant default short-input path.Let D(n) be the 64-bit little-endian load at byte offset n in the public constant array. The defaults share this path for these short strings:

kMul = 0x79d5f9e0de1e8cf5
Mix(a, b) = low64(a * b) XOR high64(a * b)
D(n) = load64(public_constant_bytes + n)
if n == 0: v = 0x57
if 1 <= n <= 3: v = (m[0] << 16) | (m[n/2] << 8) | m[n-1]
if 4 <= n <= 8: v = (load32(m) << 32) | load32(m + n - 4)
if n <= 8: return Mix(seed XOR D(n) XOR v, kMul)
if 9 <= n <= 16:
 return Mix(seed XOR D(n) XOR load64(m),
 kMul XOR load64(m + n - 8))

Fixed pair, in hex.The first message is empty; lengths 0 and 8 bytes give L = 1:

m = "" (zero bytes)
m′ = a6e02637c07bd386

Nonempty alternative (1 / 8 bytes, also L = 1):
m = 61
m′ = 44b53d572db1948b

Same-length pair (16 / 16 bytes, L = 2):
m = 6162636465666768f58c1edee0f9d579
m′ = 4142434445464748f58c1edee0f9d579

Mechanism and score.For the headline pair, D(0) XOR 0x57 = D(8) XOR v(m′), so both calls pass the same first operand to Mix for every seed. Thus ε = 1 and log₂(1/1) =0 bits. In the 16-byte pair, the last eight bytes encode kMul. The second operand becomes zero and Mix(x,0) = 0 for every first operand, giving ε = 1 and log₂(2/1) =1 bit. Reseeding cannot separate either pair.

Verification and scope.Real-library checks found equality for all 32 table seeds, for 228additional seeds and across 2,800 actualflat_hash_settables. The short-input identity applies on the audited 64-bit scalar default, x86 AES-NI and ARM-crypto defaults, since their long-input backend differences do not affect these strings. The ARM conclusion follows the common source structure; the independent verifier did not rerun it on ARM hardware. Non-default CRC32C and longer-input families require separate analysis.

Reproduction.The Abseil verification package includes the empty-input pair, nonempty alternative, same-length pair and checks against the real library. See the timing record for the exact backend measured on each available host.

Records:Documentation and claim·Implementation studied·Verifier package·Measurements

### .NET 10 Marvin32pattern:ungrouped

Two fixed six-character strings collide for about one random seed in 480. The measured rate gives a 9.91-bit cap. The result concerns Marvin’s 32-bit string hash, including ordinal hashing and the randomized comparer used after a dictionary switches away from its initial nonrandomized comparer.

Claim and version.Microsoft’sruntime security design notesays “the 64-bit Marvin32 seed is chosen at app start and remains static for the life of the app”, and distinguishes per-dictionary seeds. TheString.GetHashCode documentationwarns that it cannot substitute for a cryptographically strong hash. Neither gives a numerical collision bound for Marvin. The separate System.HashCode algorithm is not Marvin. This result uses.NET 10.0.12’s Marvin.cs.

Key model.Treat the per-process seed as a uniform 64-bit value, split into two 32-bit words. It stays fixed forstring.GetHashCodeand ordinal string hashing. Each randomized dictionary comparer draws its own seed. A process whose string hashes collide therefore does not force collisions in all its dictionaries; each independent dictionary seed has the same roughly one-in-480 odds.

Relevant path.All additions wrap modulo 232. The 12-byte pair is three complete little-endian words, followed by the common terminator and finalization:

Block(p0, p1):
 p1 ^= p0; p0 = rotl32(p0, 20)
 p0 += p1; p1 = rotl32(p1, 9)
 p1 ^= p0; p0 = rotl32(p0, 27)
 p0 += p1; p1 = rotl32(p1, 19)
 return p0, p1

p0, p1 = low32(seed), high32(seed)
for each 32-bit little-endian word w in the 12-byte message:
 p0 += w
 p0, p1 = Block(p0, p1)
p0 += 0x80
p0, p1 = Block(p0, p1)
p0, p1 = Block(p0, p1)
return p0 XOR p1 // 32-bit hash code

Fixed pair, UTF-16LE bytes.Each string has six valid, nonsurrogate BMP code units; 12 bytes gives L = 2:

m = 610061002f546d1662006200
 "aa" U+542F U+166D "bb"
m′ = 610061802f9579a262fc6100
 "a" U+8061 U+952F U+A279 U+FC62 "a"

Additive word differences: 0x80000000, 0x8c0c4100, -0x400

Mechanism and score.Only one Block separates consecutive word injections. The three-word additive difference cancels through the second Block and the next injection for a substantial fraction of initial states; once the full state agrees, the common remaining steps preserve equality. The independent implementation counted8,945,794 / 232, or ε ≈ 2−8.9072. Hence log₂(2/ε) = 9.9072, displayed as9.91 bits, with central 95% Poisson interval [9.9063, 9.9082]. A real-runtime check found 34,855 / 224, consistent with this rate.

Scope and qualifications.The output is 32 bits. The scored APIs includestring.GetHashCode,StringComparer.Ordinaland dictionary/hash-set comparers after they switch to randomized string hashing. The initial nonrandomized comparer,OrdinalIgnoreCaseandSystem.HashCodeare outside this result. The scalar algorithm is shared by x86-64 and ARM64. The smaller eight-byte pair6100610061006100versus7211721150ef4fefhas L = 1 and a measured cap about 22.53 bits; it does not improve the headline cap.

Reproduction.The Marvin verification package supplies the independent C program, upstream source, runtime vectors and C# checker. The timing record distinguishes timing from the collision samples and from a full statistical-suite result.

Records:Documentation and claim·Implementation studied·Verifier package·Measurements

### foldhash-fast 0.2.0pattern:P1

For an eight-byte input, both multiplication operands reuse the same message word. Complementing that word sometimes preserves the mixed result. The measured rate assumes independently random key material, rather than the default Rust key generator.

EXTENSION.The differential reproduces thepaper’s wyhash/rapidhash complement-both-operands mechanism; foldhash’s overlapping reads make it apply to one word, L = 1.Orson Peters (2024)supplied earlier known/fixed-seed attacks on the folded-multiply family, including zero absorption; that post does not analyze this hidden-seed differential or foldhash.

Code and scope. Native 64-bit little-endian path at tagv0.2.0, commit 8f878c636fda9c9e93384824ea45e06d03f009f5. The pseudocode followssrc/lib.rs, lines 143–159 (fold),240–259 (short)and279–350 (long), plussrc/fast.rs, lines 35–122 (writes and finish).Local source. All word additions wrap modulo 264; multiplication in F is exact to 128 bits. v0.2.0 is still the newest release (crates.io, 2025-08-23); master at 77d8e3d (2026-06-30) differs only in a no_std cfg guard in src/seed.rs. Reruns on that source reproduce the rate: the same verifier gave 2761 / 238and 699 / 236(uniform model), and the upstream crate at that commit through its public API with SharedSeed::from_u64 seeds gave 642 / 236and 674 / 236.

F(x, y) = low64(x * y) XOR high64(x * y)
write(bytes):
 a = rotate_right(accumulator, len(bytes) mod 64)
 accumulator = short(bytes, a) if len(bytes) ≤ 16 else long(bytes, a)

short(v, a):
 n = len(v); x = a; y = seeds[1]
 if n ≥ 8: x ^= load64(v, 0); y ^= load64(v, n-8)
 elif n ≥ 4: x ^= load32(v, 0); y ^= load32(v, n-4)
 elif n > 0: x ^= v[0]; y ^= (v[n-1] << 8) | v[n/2]
 return F(x, y)

long(v, a):
 s0 = a; s1 = a + seeds[1]
 if len(v) > 128:
 s2 = a + seeds[2]; s3 = a + seeds[3]
 if len(v) > 256:
 s4 = a + seeds[4]; s5 = a + seeds[5]
 repeat:
 for j = 0..5:
 sj = F(load64(v, 8*j) XOR sj,
 load64(v, 48+8*j) XOR seeds[0])
 v = v[96:]
 until len(v) ≤ 256
 s0 ^= s4; s1 ^= s5
 repeat:
 for j = 0..3:
 sj = F(load64(v, 8*j) XOR sj,
 load64(v, 32+8*j) XOR seeds[0])
 v = v[64:]
 until len(v) ≤ 128
 s0 ^= s2; s1 ^= s3
 n = len(v)
 for t in [0, 1, 2, 3]:
 if t == 0 or n ≥ 32*t:
 s0 = F(load64(v, 16*t) XOR s0,
 load64(v, n-16*(t+1)) XOR seeds[0])
 s1 = F(load64(v, 16*t+8) XOR s1,
 load64(v, n-16*(t+1)+8) XOR seeds[0])
 return s0 XOR s1

finish_fast():
 if sponge_len > 0:
 return F(low64(sponge) XOR accumulator,
 high64(sponge) XOR seeds[0])
 return accumulator

A folded multiply of two xor-keyed words
At length eight the same word w enters both operands. Each is XORed with a secret, their 128-bit product is split, and its high and low halves are XORed to give the hash.

u = w XOR rotr(seed, 8)
v = w XOR seeds[1]
p = u × v (128 bits)
lo64(p)
hi64(p)
⊕
64-bit fold

At eight bytes both reads alias the same word. Replacing w with its bitwise complement complements both keyed operands; the low/high XOR can stay unchanged.

Fixed pair, in hex.Both inputs are eight bytes, L = 1:

m = 0000000000000000
m′ = ffffffffffffffff

Verified UTF-8 alternative, also 8 / 8 bytes:
m = 2141214121412141 ("!A!A!A!A")
m′ = debedebedebedebe

Mechanism.At length eight, the short path reads the same word w from both ends, so its hash is F(rotr(seed, 8) XOR w, seeds[1] XOR w). Replacing w by its complement complements both operands, reducing the attack to F(u,v) = F(~u,~v). In the 128-bit product the complementary transformation moves the two halves in opposite directions, and the XOR fold survives when the associated carry and borrow patterns match. This is the paper’s differential at L = 1 instead of L = 2, with no output queries or seed knowledge. Equal accumulators remain equal after the common length prefix or string-terminator sponge fold, so the byte pair works throughVec<u8>/&[u8], and the UTF-8 pair works throughString/&str.

Verified measurements.Under independent uniform per-hasher and shared seed words, the selected fast run found2757 / 238collisions: ε ≈ 2−26.5711, with the central exact Poisson 95% interval [2−26.6255, 2−26.5173]. Thus log₂(L/ε) ≈26.5711 bits, interval [26.5173, 26.6255]. All five counters (accumulator, raw fast, vector, string framing and quality) were exactly 2757. The separate verified UTF-8 pair gave 2677 / 238, ε ≈ 2−26.6136, interval [2−26.6688, 2−26.5589], and score 26.6136 bits. These witness-derived caps include sampling uncertainty and give no proved worst-pair guarantee; source: VERIFIED rows in the synthesis.

Interval convention.For k observed collisions in N draws, the central exact Poisson (Garwood) endpoints are χ²2k,0.025/(2N) and χ²2(k+1),0.975/(2N); score endpoints reverse under log₂(L/ε). “Exact” names the Poisson construction; displayed endpoints are rounded and this is a rare-event sampling model.

No every-seed pair found within a fixed byte-slice key type.I searched unread bytes, length-extension signatures, lane/round symmetries, structured and random message corpora, and XOR differences. The independent verifiers confirmed the seed-dependent pair above; they did not independently verify the exhaustive-search or no-pair proof claims. I therefore have no proof excluding such pairs at every input length. The separate cross-type finding below is outside the row’s domain.

Default seed entropy. RandomState::default() obtains a per-hasher seed and a cached global SharedSeed (fast.rs, lines 125–148). On the default std path, the per-hasher generator mixes a stack address with evolving thread-local state; global initialization mixes stack, function and static addresses, wall-clock seconds/nanoseconds when available, and a heap address (seed.rs, lines 22–70,140–174). It does not draw seven independent words from an OS random-number API. The global result is a single u64 expanded into six words, with bits 0, 31 and 63 forced on (lines 97–131), so the shared material has at most 64 bits of entropy rather than 384; I have not quantified the environment-dependent default entropy. For the scored experiment, I use independent uniform secret words. A verified check with uniform per-hasher seed and SharedSeed::from_u64(uniform u64) found 688 / 236for the same pair, consistent with that rate; this checks seed expansion while leaving the complete default generator untested. Upstream has an open issue (#47, 2026-07-03, RandomState with the std feature on new threads) and the maintainer's own pull request #48 (2026-07-03) improving that seeding; neither is released.

Suite and speed scope.My verified C++ port matches 52,080 Rust oracle outputs on each host, with Xeon sanitizer checks. SMHasher3 callsFoldHasher::with_seed(S, &SharedSeed::from_u64(S)), then one raw byte write and finish; initialization is outside the timed region. The full default suite is79 of 200 tests passedfor fast and117 of 200 tests passedfor quality; I report my run here. It differs from the maintainer’s results directory and does not measure default RustRandomState. I did not request--extracases. A passing implementation verification value does not mean the statistical suite passed. The direct seed-zero raw-byte path explains the recorded basic sanity failure; I kept it in the results without patching it.

Bulk B/cycle and 1–31 B cycles/hash are respectively14.24 / 14.94(fast, M2 Pro),14.42 / 18.92(quality, M2 Pro),9.07 / 20.09(fast, Xeon) and9.07 / 25.28(quality, Xeon). The backend token is blank (generic 64-bit multiply-fold). These select the better bulk and small-key results independently from two runs. M2 cycle estimates use a calibrated monotonic clock; Xeon uses TSC ticks; printed GiB/s assumes 3.5 GHz. The control ratios, new/baseline (bulk, small cycles), are M2 komihash (0.9443, 1.0967), M2 rapidhash (0.9950, 1.0030), Xeon komihash (0.9986, 0.9734), and Xeon rapidhash (1.0019, 1.0007). They refer to the baselines recorded with this port, not a later table rerun. Timings and controls · port and suite report · Rust oracle vectors.

Reproduction.Reproduction documentation and the independent C11 verifier include reference-vector checks and the original sample log. Fromverify/foldhash-fast/:

cc -O2 -std=c11 -pthread -o foldhash_verify foldhash_verify.c
./foldhash_verify 20 1 0xc0ffee1234567890

A 220-seed smoke run normally sees zero of these rare collisions; it checks implementation consistency, not the historical rate. The README gives the original large-run parameters.

Selected score: ≈ 26.5711* bits.8/8 bytes; L = 1; 2757/238measured.

### foldhash-quality 0.2.0pattern:P1

The quality variant adds a mixing step after the fast calculation. If the earlier calculation has already collided, that extra step receives identical inputs and cannot separate them.

EXTENSION. Same paper differential and Peters 2024 family credit asfoldhash-fast; same short/long paths and 0000000000000000 / ffffffffffffffff pair, 8/8 bytes, L = 1.src/quality.rs, lines 72–75, tag v0.2.0adds only this final step: v0.2.0 is the newest release (crates.io, 2025-08-23). Upstream master (77d8e3d, 2026-06-30) differs from v0.2.0 only by a no-std cfg guard in src/seed.rs; an oracle built on master reproduces the verifier's nine reference vectors, and the real crate at master gives 171 / 234for the scored pair (26.58 bits, [26.37, 26.81]).

finish_quality():
 return F(finish_fast(), 0x243f6a8885a308d3)

Mechanism.Quality applies a deterministic, seed-independent folded multiply to the fast output. Every fast collision survives this final map, which may add collisions of its own. The verified four-counter run observed no quality-only collisions, and the extra avalanche step does not improve the selected fixed-pair score.

Verified measurement. The selected quality counter found 696 / 236, ε ≈ 2-26.5571; the central exact Poisson 95% interval is [2-26.6663, 2-26.4499]. The score is 26.5571 bits, interval [26.4499, 26.6663]. This combines four independent 234chunks with 168, 198, 170 and 160 hits; fast/quality and raw/vector counters agreed in every chunk. No every-seed pair was found within a fixed byte-slice key type; the exploratory search and seed-entropy qualifications above apply unchanged. A fresh 8-thread rerun of the same four commands on 2026-09-18 gave 176+190+189+177 = 732 / 236(26.48 bits, [26.38, 26.59]); the real crate at master gave 171 / 234(scored model) and 83 / 233(from_u64 model). The count differs from 696 because the thread count changes the deterministic stream, not because the rate changed.

Reproduction.Reproduction documentation · C11 verifier ·complete verification archive. Fromverify/foldhash-quality/:

cc -O2 -std=c11 -pthread -o foldhash_verify foldhash_verify.c
./foldhash_verify verify
./foldhash_verify measure 0000000000000000 ffffffffffffffff 20 1 0 0xa11ce001

Selected score: ≈ 26.5571* bits.8/8 bytes; L = 1; 696/236measured. Samedefault seed caveatand direct-seeded benchmark scope as fast.

Official wording. Three consecutive README sentences are quoted below, including “quadratric” (README.md, lines 263–272 at v0.2.0, unchanged on master as of 2026-09-18). The paragraph continues: “For a student of cryptography it should be trivial to derive the secret values from direct observation of hash outputs…”.

This (plus other careful design throughout the hash function) ensures that it is not possible to create a list of inputs that collide for every instance of foldhash, and also prevents certain access patterns on hash tables going quadratric by ensuring that each hash table uses a different seed and thus a different access pattern.
It is these two properties that we refer to when we claim foldhash is “minimally DoS-resistant”: it does the bare minimum to defeat very simple attacks. However, to be crystal clear, foldhash does not claim to provide HashDoS resistance against interactive attackers.

Disclosure: reported asorlp/foldhash#50on 2026-09-18. The maintainer replied the same day that the fixed-pair result was “not too surprised given the ad-hoc nature of folded multiply” and that collisions across key types are out of scope. The issue remains open.

Records:Original project & code· Verifier package · Measurements

Records:Original project & code·Verifier package·Measurements

## How these results were produced

I provide29 C11 collision-reproduction packagesthat check the implementation’s published verification constant or reference vectors, then the explicit collision witness. The19 September smoke runreproduced the reference counts for all 27 Makefile targets; the two foldhash packages passed their separately documented checks. A separateC++ audit packagecovers HalftimeHash. They check consistency and the printed witnesses. They do not prove full equivalence to upstream on every input or a rare-event probability theorem.

I checked every selected witness in a separate verification program. Some programs reimplement the algorithm; others embed upstream code, including komihash, HighwayHash and XXH3. Several headline mechanisms also received independent checks at limited sampling scale. Those samples did not certify SpookyHash’s exact-half claim or HighwayHash’s exact numerator.

The initial investigation took about one day, followed by further searches, independent checks and proof work. It traced where message words meet keys, proposed pairs and measured full-output collisions. The record does not count every rejected mechanism or provide a full compute ledger. I report the scope of each standalone program, exact count, prose proof and Lean status file.

The one-day account covers the investigation I directed. Large parallel searches and later verification runs followed; the records do not provide a complete hardware-cost ledger. I do not treat agreement between reviews alone as evidence of historical novelty or correctness. Appendix B separates deterministic smoke counts, fresh confirmation streams, exhaustive enumerations and analytical event counts.

## Appendix B. Reproducing the numbers

Show as table

Figure 1 data: all displayed rows. See 
The collision score
 for bound direction. Missing or mismatched speeds are omitted from that axis; claimed bounds with a proof gap found use open circles. SMHasher3 values come from 
the two-host benchmark
 and the linked 
new-hash timing records
.
Hash
Family
Evidence / proof status
Collision score: cap or guarantee
M2 Pro bulk B/cycle
Xeon 8375C bulk B/cycle
M2 Pro 1–31 B, cycles/hash
Xeon 8375C 1–31 B, cycles/hash
Lean
Paper M2 Pro GB/s at 16 KB
CityHash64 v1.1.1
constant-multiplier lanes
every key
0 bits
6.10
†
5.43
42.30
†
46.68
—
—
FarmHash64 NA v1.1
constant-multiplier lanes
every key
0 bits
5.96
†
5.43
43.15
†
45.11
—
—
MurmurHash3 x64_128
constant-multiplier lanes
every key
at most 1.59 bits (cap)
1.92
†
2.73
40.31
†
41.30
—
—
mx3 v3
constant-multiplier lanes
every key
0 bits
4.32
†
4.82
43.23
†
41.59
—
—
fasthash-64
constant-multiplier lanes
every key
0 bits
1.39
†
2.30
34.96
†
34.00
—
—
fasthash-32
constant-multiplier lanes
every key
0 bits
1.40
†
2.30
36.81
†
36.20
—
—
MuseAir v0.3 (SMHasher3)
keyed multiply-fold
every key
at most 1.59 bits (cap); version-bound to v0.3
10.21
†
7.82
24.65
†
19.91
—
—

MuseAir v2 (crate 0.6.0)
keyed multiply-fold
about 2^-17.45 of keys (sampled; 36,060 events / 1.5×2^32 keys, upstream crate)
at most 19.45 bits (cap; sampled; 95% interval 19.43–19.46)
10.42
7.53
22.32
29.27
—
—
komihash v5.27 / v5.34
keyed multiply-fold
about 0.9106 of keys (sampled; 3,910,946,997 events / 2^32 keys)
at most 3.14 bits (cap; sampled)
7.96
†
7.35
25.05
†
27.49
—
—
t1ha2_atonce-64 v2.1.4
keyed multiply-fold
about 2^-28.19 of keys (sampled class contribution: 2^-24 × 58,715,203/2^30)
at most 29.19 bits (cap; sampled); conditional-rate 95% ≈ ±0.0004 bits
6.19
†
5.82
39.30
†
39.16
—
—
a5hash v5.21, 64-bit
keyed multiply-fold
collides for at least 118 of every 2^45 keys (counted)
at most 47.81 bits (cap)
3.20
†
3.17
22.36
†
19.32
—
—
a5hash v5.21, 128-bit
keyed multiply-fold
every key
at most 1.59 bits (cap)
12.22
†
7.93
21.47
†
22.23
—
—
wyhash final v4.3
keyed multiply-fold
about 1088 of every 2^36.58 keys (sampled; 1088 events, pooled)
at most 28.5 bits (cap; sampled); 95% Poisson interval [28.4, 28.6]
8.75
8.47
21.20
26.66
—
—
rapidhash v1
keyed multiply-fold
about 160 of every 2^34 keys (sampled; 160 events, pooled)
at most 28.7 bits (cap; sampled); 95% Poisson interval [28.5, 28.9]
—
—
—
—
—
—
rapidhash v3
keyed multiply-fold
about 2386 of every 2^37.83 keys (sampled; 2386 events, pooled)
at most 28.6 bits (cap; sampled); 95% Poisson interval [28.5, 28.7]
15.03
†
10.67
21.08
†
27.58
—
—
foldhash-fast 0.2.0
keyed multiply-fold (mum)
EXTENSION; 2757 / 2^38 seeds; no same-type every-seed pair found
at most 26.5711 bits (cap; sampled); 95% Poisson [26.5173, 26.6255]
14.24
9.07
14.94
20.09
—
—
foldhash-quality 0.2.0
keyed multiply-fold (mum)
EXTENSION; 696 / 2^36 seeds; no same-type every-seed pair found
at most 26.5571 bits (cap; sampled); 95% Poisson [26.4499, 26.6663]
14.42
9.07
18.92
25.28
—
—
MUM v3
keyed multiply-fold
every key
0 bits
Plotted: 14.12 (mum3.exact.unroll4)
mum3.exact.unroll1: 2.38
mum3.exact.unroll2: 4.29
mum3.exact.unroll3: 7.54
mum3.exact.unroll4: 14.12
Plotted: 6.65 (mum3.exact.unroll4)
mum3.exact.unroll1: 3.17
mum3.exact.unroll2: 6.04
mum3.exact.unroll3: 6.57
mum3.exact.unroll4: 6.65
23.42
†
23.92
—
—
mir.exact / mir.inexact
mir.inexact: no matching timing on either host.
keyed multiply-fold
every key
0 bits
1.86
†
2.59
34.63
†
32.18
—
—
XXH3-64 0.8.3
NH-like accumulators
about 527 of every 2^36 keys (sampled; 527 events, pooled)
at most 28.5 bits (cap; sampled); 95% Poisson interval [28.4, 28.7]
13.16
19.69
24.51
30.16
—
—
XXH3-128 0.8.3
NH-like accumulators
about 479 of every 2^35.46 keys (sampled; 479 events, pooled)
at most 28.6 bits (cap; sampled); 95% Poisson interval [28.4, 28.7]
13.37
19.82
29.76
34.92
—
—
HighwayHash-64, frozen
keyed-state lane products
collides for at least 56,165 of every 2^72 keys (counted class contribution)
at most 59.81 bits (cap)
1.48
3.24
90.16
61.88
✓ checked
—
SpookyHash V2-64
ARX lanes
about half of keys (sampled; 536875475/1073741823)
at most 6.13 bits (cap; sampled)
5.81
†
5.08
37.74
†
45.59
—
—
pengyhash v0.3
ARX lanes
every key
at most 2 bits (cap)
3.68
†
4.41
74.39
†
72.62
—
—
nmhash32 v2
narrow 16-bit multiplies
collides for 1,078,944,392 of every 2^32 keys (exhaustively counted)
at most 4.994 bits (cap)
1.99
†
‡
6.88
59.96
†
‡
49.21
—
—
nmhash32x v2
32-bit lane multiplies
every key
at most 2 bits (cap)
1.94
†
‡
6.88
37.18
†
‡
30.62
—
—
gxhash-64 v3.5.0
keyed AES rounds
every key
at most 1 bits (cap)
31.81
18.28
40.02
31.35
—
—
aHash 0.8.12, AES path
keyed AES rounds
about 2^-12.12 of keys (sampled; 967,503 events / 2^32 keys, native Rust crate 0.8.12)
at most 17.84 bits (cap; sampled); 95% interval 17.84–17.85
1.12
0.81
39.30
79.77
—
—
SipHash-1-3
ARX PRF
no pair found
no theorem, no pair found: no score
1.13
†
1.01
50.39
†
70.58
—
—
SipHash-2-4
ARX PRF
no pair found
no theorem, no pair found: no score
0.59
†
0.53
73.41
†
95.55
—
—
HalftimeHash24 (advanced 24-byte API, Encode3)
NH trees
at least 1 of every 2^32 keys (counted; equal-length 168-byte Encode3 pair); sampled 76/316053236830 ≈ 2^-31.95, 95% interval [2^-32.30, 2^-31.63]
at most 36.4 bits (cap; counted 2^-32 key class for a fixed equal-length pair, sampled 2^-31.95)
—
—
—
—
—
—
PolymurHash 2.0
prime-field polynomial
proved with correction: D(8L)/K0
≥ 54.2267 bits (proved)
5.59
†
4.97
32.86
†
39.16
✓ checked
19.70
Poly1305
prime-field polynomial
proved (audited)
≥ 103 bits (proved)
2.20
4.48
156.96
250.51
✓ checked (ideal key)
—
Horner / unrolled, GF(2^64)
GF(2^k) polynomial
proved (audited)
≥ 64 bits (proved)
—
—
—
—
✓ checked
—
BRW, GF(2^64)
GF(2^k) polynomial
proved (audited)
≥ 63 bits (proved)
—
—
—
—
✓ checked
—
Injective recurrence, one chain
GF(2^k) polynomial
proved (audited)
≥ 64 bits (proved)
—
—
—
—
✓ checked
—
Injective recurrence, eight lanes
GF(2^k) polynomial
proved (audited)
≥ 61 bits (proved)
—
—
—
—
✓ checked
—
GHASH
GF(2^k) polynomial
proved (audited)
≥ 127 bits (proved)
2.48
7.02
1382.75
1912.96
✓ checked (ideal key)
—
NH with 64-bit words
NH
proved (audited)
≥ 64 bits (proved)
—
—
—
—
partial: executable refinement remains unproved
—
HalftimeHash (Style wrappers)
NH + tabulation
proved ≥ 63 (audited; corrected proof with an execution contract and finite length caps; see records)
≥ 63 bits (proved)
Fastest style: 10.49 (Style256)
Style64: 
4.63
Style128: 
9.49
Style256: 
10.49
Style512: 
7.49
Fastest style: 19.29 (Style512)
Style64: 
2.50
Style128: 
8.07
Style256: 
15.70
Style512: 
19.29
Style64: 
48.06
Style128: 
58.62
Style256: 
59.12
Style512: 
63.38
Style64: 
90.11
Style128: 
82.97
Style256: 
77.66
Style512: 
85.74
partial: executable refinement remains unproved
—
UMASH-64
PH/NH + prime-field polynomial
Proved:
 Pr[collision] < 58·⌈L/512⌉/2
61
; fine envelope scores 56.18 bits.
Ideal full keys, fixed seed, full C output
.
≥ 56.18 bits
14.21
11.33
34.19
38.76
partial: 46.52-bit envelope + ENH-only closure machine-checked; 56.18 / 84 are verified paper proofs, not yet machine-checked
40.70
UMASH-128 fingerprint
PH/NH + prime-field polynomial
Proved:
 Pr[collision] < (81/128)·⌈L/2
23
⌉²·2
−83
; finer envelope scores 83.99 on L ≤ 2
46
.
Ideal full keys, fixed seed, full C output
.
≥ 84 bits on L ≤ 2^46 
Rounded; plotted at 83.99
7.82
6.02
41.84
40.23
partial: 46.52-bit envelope + ENH-only closure machine-checked; 56.18 / 84 are verified paper proofs, not yet machine-checked
23.90
CLHASH
PH + GF(2^127) polynomial
proved (audited)
≥ 64 bits (proved)
15.15
11.56
40.53
43.03
✓ checked
—
Carryless NH (CLNH)
PH (carry-less NH)
proved (audited)
≥ 64 bits (proved)
—
—
—
—
✓ checked (field theorem)
—
ChainHash (ours)
64 random key bytes
CLNH + Horner + quintic
proved (machine-checked)
≥ 63 bits
26.26
28.31
87.49
155.14
✓ checked
89 theorems, standard axioms; 464 C/Lean vectors
—
Simple tabulation
tabulation
proved (audited)
≥ 64 bits (proved)
—
—
—
—
✓ checked
—
Vector multiply-shift
multiply-shift
proved (audited)
≥ 64 bits (proved)
—
—
—
—
✓ checked
—
HalftimeHash24, repaired encoder (not shipped)
Our fix; not yet upstream
NH: keyed pair products summed
proved (audited)
≥ 83.27 bits (proved)
5.55
14.12
48.63
79.42
✓ construction (M1–M4)
—

ChainHash-128 (ours)
128 random key bytes
CLNH + Horner + quintic, GF(2^128)
proved (machine-checked)
≥ 127 bits
10.26
Same binaries: XXH3-128 12.53, UMASH-128 7.52
14.43
Same binaries: XXH3-128 19.82, UMASH-128 6.02
167.89
175.93
✓ checked
116 theorems, standard axioms; 625 C/Lean vectors
—

Go maphash
keyless AES rounds on a secret lane state
2
−24
 exact sufficient trail; 66 / 2
30
 sampled; runtime 20 / 2
28
≤ 25.0 bits
sample interval [24.61, 25.33]
—
17.66
—
64.32
—
—

absl::Hash
keyed multiply-fold (mum)
1 (every seed)
0 bits
—
8.22
—
20.67
—
—

Marvin32 (.NET)
ARX (SipHash-like half rounds)
8,945,794 / 2
32
 ≈ 2
−8.91
≈ 9.91 bits
95% [9.9063, 9.9082]
—
0.95
—
31.07
—
—

† No dedicated ARM hash backend exists in this SMHasher3 tree; generic code may still use shared ARM arithmetic helpers. I retain the backend tokens verbatim. A blank means no named token; UMASH/CLHASH’shwclmultoken runs PMULL on ARM, and aHash’sportablenames its shuffle while its AES rounds use ARM instructions. Hover a speed for its token and run spread.

The corrected pass retains pre-existing verification-code failures for NMHASH/NMHASHX on M2 Pro only: SMHasher3's scalar build there computes different functions (NMHASHX 0x9CF42B2D instead of 0xA8580227), so the M2 numbers for these two rows time implementations whose output is not the registered hash. The Xeon (AVX-512) builds verify (NMHASHX 0xA8580227 PASS); on x86 the upstream nmhash.h scalar path (NMH_VECTOR=0) also gives 0xA8580227. Four poly-mersenne registrations also retain their separately recorded verification-code failures; the structural Sanity checks passed. Timing alone is not a correctness certificate.

Public records index: papers, specifications, measurements, and exact certificates.

Theverification packagecontains29 C11 collision-reproduction packages, including MuseAir v2, Go’s map hash, Abseil Hash, Marvin32, both foldhash variants, wyhash, rapidhash v1 and XXH3-64/128. Each checks reference outputs and explicit witnesses, then samples deterministic pseudorandom seeds. The checks support implementation consistency; they do not prove equivalence on every input.

# From the page/archive parent directory:
make -C verify -j2
make -C verify -j1 check

The27 Makefile checksreproduced their README counts on 19 September 2026. The two foldhash packages are built separately, using the commands in their READMEs; both passed their reference checks and gave zero hits in their deterministic 220-seed smoke runs (fast instructions,quality instructions). These small samples do not replace the historical large measurements or exhaustive counts. Statistical interpretations assume that the sampled streams behave like independent uniform draws; a zero count is not a hard population bound.

The a5hash supplement checks the selected 6615-byte and 17-byte witnesses. The MuseAir supplement checks the C–E witnesses, samples the BFast constructions, and counts its masked seed class exactly. Their READMEs give the commands. The per-hash packages record which selected and supporting pairs they check; a single package can cover several output variants. These checks do not re-establish the historical large counts or HighwayHash’s analytical numerator.verify.tar.gzcontains the deployed source package. The interactive chart and downloadable figures are generated from the samedata.jsonrecord; the static figure remains available without JavaScript.