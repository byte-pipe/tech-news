---
title: Quantum Computers Are Not a Threat to 128-bit Symmetric Keys
url: https://words.filippo.io/128-bits/
site_name: hnrss
content_file: hnrss-quantum-computers-are-not-a-threat-to-128-bit-symm
fetched_at: '2026-04-21T11:59:48.625092'
original_url: https://words.filippo.io/128-bits/
date: '2026-04-20'
published_date: '2026-04-20T15:21:12.540462Z'
description: There is no need to update symmetric key sizes as part of the post-quantum transition, due to the details of how Grover's algorithm scales. Most authorities agree.
tags:
- hackernews
- hnrss
---

20 Apr 2026

# Quantum Computers Are Not a Threat to 128-bit Symmetric Keys

Theadvancing threat of cryptographically-relevant quantum computershas made it urgent to replace currently-deployed asymmetric cryptography primitives—key exchange (ECDH) and digital signatures (RSA, ECDSA, EdDSA)—which are vulnerable toShor’s quantum algorithm. It does not, however, impact existing symmetric cryptography algorithms (AES, SHA-2, SHA-3) or their key sizes.

There’s a common misconception that quantum computers will “halve” the security of symmetric keys, requiring 256-bit keys for 128 bits of security. That is not an accurate interpretation of the speedup offered by quantum algorithms, it’s not reflected in any compliance mandate, and risks diverting energy and attention from actually necessary post-quantum transition work. The misconception is usually based on a misunderstanding of the applicability of a different quantum algorithm,Grover’s.

AES-128 is safe against quantum computers. SHA-256 is safe against quantum computers. No symmetric key sizes have to change as part of the post-quantum transition.This is a near-consensus opinion amongst experts and standardization bodies and it needs to propagate to the rest of the IT community. The rest of this article backs up this claim both technically and with references to relevant authorities.

## The Grover speedup

Grover’s is a quantum algorithm that allows searching an input space of sizeNof an unstructured functionffor the “right answer” inπ/4×N\pi / 4 \times \sqrt{N}invocations off.

This is commonly interpreted to mean that Grover’s algorithm can find an AES-128 key in2642^{64}“time.” That is not the case in practice, because running such an attack as a single sequential thread would take hundreds of thousands of years, and parallelizing it makes its total cost grow.

A few important things to understand about Grover’s algorithm:

* the function oraclefmust be implemented as part of the quantum circuit;
* the oracle invocations have to happen one after the other in series;
* importantly, there is no better way to parallelize the attack than to partition the search space (Zalka, 1997).

Why does the last point matter? Because unlike regular bruteforce attacks, which are “embarrassingly parallel,” partitioning the search space degrades the Grover quadratic speedup.

Consider a classical bruteforce of a 64-bit key, where each attempt takes 5 ns (~ 16 cycles at 3 GHz). Running that on a single CPU would take nearly

2
64
×
5
 ns
≈
3,000
 years.

2^{64} \times 5 \text{ ns} \approx 3{,}000 \text{ years}.

So we parallelize it across

2
16
=
65,536
 CPUs

2^{16} = 65{,}536 \text{ CPUs}

each exploring

2
(
64
−
16
)
=
2
48
 keys

2^{(64 - 16)} = 2^{48} \text{ keys}

in a little over

2
48
×
5
 ns
≈
16
 days.

2^{48} \times 5 \text{ ns} \approx 16 \text{ days}.

Note how the total amount of work done across the system

2
16
×
2
48
=
2
64

2^{16} \times 2^{48} = 2^{64}

has not changed.

This is why we consider 64-bit keys weak: because they can be searched in parallel efficiently. If the attack had to be sequential, there would be no risk.1

Let’s try the same with a Grover attack on 128-bit keys. Again, running

2
128
=
2
64

\sqrt{2^{128}} = 2^{64}

operations in a row is infeasible, so we again parallelize the attack across2162^{16}quantum computers, each exploring

2
(
128
−
16
)
=
2
112
 keys.

2^{(128 - 16)} = 2^{112} \text{ keys}.

Each instance will need to do

2
128
/
2
16
=
2
56
 work.

\sqrt{2^{128} / 2^{16}} = 2^{56} \text{ work}.

Notice how that’s not2482^{48}!

A2162^{16}search space reduction factor inside a square root only saves282^{8}of work per instance, whereas classically it saves the full2162^{16}.

The total amount of work across the system wentupfrom2642^{64}to

2
56
×
2
16
=
2
72

2^{56} \times 2^{16} = 2^{72}

because we parallelized the attack, diluting the quadratic speedup in the process.

### Running the numbers

That gives us the intuition for why Grover’s algorithm doesn’t parallelize. To decide if it’s still a threat we need to run the numbers with concrete orders of magnitude.

First, we need to establish how many operations, or gates, in a row we can perform. To be conservative, let’s say that we have a fast-clock quantum architecture like superconducting qubits, and that a gate takes 1 µs.2If we are willing to keep the attack running (with no power outage or loss of fidelity!) for a decade, that gives us a maximum sequence of gates or “depth” of

10
 years
/
1
 µs
≈
2
48

10 \text{ years} / 1 \text{ µs} \approx 2^{48}

Next, we need to know how many sequential gates it takes to compute AES-128 inside the quantum circuit.Liao and Luo (2025)provide a highly optimized Grover oracle for AES-128 with a depth of 232 T-gates (and a circuit “width” of 724, which is roughly speaking the number of logical qubits operating in parallel).

Now we can solve for the lowest parallelization factor that will keep each instance within a maximum depth of2482^{48}(i.e. completing in a decade on these hypothetical fast and perfect quantum computers).

π
/
4
×
2
128
/
x
×
232
=
2
48

\pi / 4 \times \sqrt{2^{128} / x} \times 232 = 2^{48}

x
≈
2
47

x \approx 2^{47}

This means we’ll need 140 trillion quantum circuits of 724 logical qubits each operating in parallel for 10 years to break AES-128 with Grover’s.

Another way to measure the cost of that attack is itsDWcost, the depth × width product, roughly equivalent to discussing the product of cycles and cores for classical computation.

π
/
4
×
2
128
/
2
47
×
232
×
724
×
2
47
≈
2
104.5

\pi / 4 \times \sqrt{2^{128} / 2^{47}} \times 232 \times 724 \times 2^{47} \approx 2^{104.5}

Note that unlike Shor’s algorithm instantiations (and quantum error correction) which have been getting drastically better over the years, there aren’t many terms in that formula that can improve. The only two that are open to optimization are the AES-128 Grover oracle depth (232) and width (724), but they contribute only 17 bits to the total cost, and there is probably little space left for improvement.Liao and Luo (2025)shaved 7.5 bits off the very first estimate byGrassl et al. (2015)and 1.5 bits off the earliest Grover-specific estimate ofJaques et al. (2019).

## A comparison with Shor’s

Speaking of Shor’s, how does this compare with the recently discussed quantum attacks against 256-bit elliptic curves? After all, there are people who believe or believed those to be infeasible, too, butI’ve been arguing to take them seriously.

Babbush et al. (2026)claim a Shor’s execution in

70M
≈
2
26
 gates

70\text{M} \approx 2^{26} \text{ gates}

which would take minutes on an architecture with “fast” gate time of 10 µs (which is 10 times slower than what we conservatively assumed above).

2
104.5
/
2
26
=
2
78.5

2^{104.5} / 2^{26} = 2^{78.5}

Breaking AES-128 with Grover is 430,000,000,000,000,000,000,000 times more expensive than breaking 256-bit elliptic curves with Shor’s.

## NIST agrees

The U.S. National Institute of Standards and Technology (NIST) is the standardization body that ran the international competition for post-quantum cryptography and wrote the ML-KEM and ML-DSA specification documents.

NIST not only considers AES-128 to be safe, butmade itthe benchmarkfor the security of post-quantum primitives. AES-128 is by definition a Category 13post-quantum algorithm.

In justifying the use of AES-128, NIST refers to the same observations we explained above, and introduces the concept ofMAXDEPTHwhich is exactly the maximum serial computation that forces parallelization and limits Grover’s quadratic speedup.

It is worth noting that the security categories based on these reference primitives provide substantially more quantum security than a naïve analysis might suggest. For example, categories 1, 3 and 5 are defined in terms of block ciphers, which can be broken using Grover’s algorithm, with a quadratic quantum speedup. But Grover’s algorithm requires a long-running serial computation, which is difficult to implement in practice. In a realistic attack, one has to run many smaller instances of the algorithm in parallel, which makes the quantum speedup less dramati[c].

NIST’s calculation uses less optimized (and hence less conservative) AES quantum circuits (fromGrassl et al. (2015)instead ofLiao and Luo (2025)), but faster (and hence more conservative) logical gate speed. Nonetheless, it lands in the same ballpark and comes to the same conclusion.

Further proof,NIST IR 8547 ipd,Transition to Post-Quantum Cryptography Standards, disallows all quantum-vulnerable algorithms from 2035. However, it reiterates that all AES key sizes remain allowed in Section 4.1.3.

NIST’s existing standards in symmetric cryptography — including hash functions, XOFs, block ciphers, KDFs, and DRBGs — are significantly less vulnerable to known quantum attacks than the public-key cryptography standards in SP 800-56A, SP 800-56B, and FIPS 186. In particular, all NIST-approved symmetric primitives that provide at least 128 bits of classical security are believed to meet the requirements of at least Category 1 security within the system of five security strength categories for evaluating parameter sets in the NIST PQC standardization process (see Table 1).

Finally, in thePost-Quantum Cryptography FAQs, there is an explicit answer to “should we double AES key sizes.” (Emphasis mine.)

To protect against the threat of quantum computers, should we double the key length for AES now? (added 11/18/18)

Grover’s algorithm allows a quantum computer to perform a brute force key search using quadratically fewer steps than would be required classically. Taken at face value, this suggests that an attacker with access to a quantum computer might be able to attack a symmetric cipher with a key up to twice as long as could be attacked by an attacker with access only to classical computers. However there are a number of mitigating factors suggesting that Grover’s algorithm will not speed up brute force key search as dramatically as one might suspect from this result. First of all, quantum computing hardware will likely be more expensive to build and use than classical hardware. Additionally, it was proven by Zalka in 1997 that in order to obtain the full quadratic speedup, all the steps of Grover’s algorithm must be performed in series. In the real world, where attacks on cryptography use massively parallel processing, the advantage of Grover’s algorithm will be smaller.

Taking these mitigating factors into account,it is quite likely that Grover’s algorithm will provide little or no advantage in attacking AES, and AES 128 will remain secure for decades to come. Furthermore, even if quantum computers turn out to be much less expensive than anticipated, the known difficulty of parallelizing Grover’s algorithm suggests that both AES 192 and AES 256 will still be safe for a very long time. This of course assumes that no new cryptographic weaknesses, either with respect to classical or quantum cryptanalysis, are found in AES.

Based on such understanding,current applications can continue to use AES with key sizes 128, 192, or 256 bits. NIST will issue guidance regarding any transitions of symmetric key algorithms and hash functions to protect against threats from quantum computers when we can foresee a transition need. Until then, users should follow the recommendations and guidelines NIST has already issued. In particular, anything with less than 112 bits of classical security should not be used.

NIST is not equivocating about this at all: 128-bit keys are fine.

## BSI agrees

What about other standards bodies? The German Federal Office for Information Security recently publishedBSI TR-02102-1Cryptographic Mechanisms: Recommendations and Key Lengthswith “updates in the area of PQ cryptography.”

In it, they mention Grover’s in passing and with less conclusiveness than NIST, but come to the same conclusion:

The following block ciphers are recommended for use in new cryptographic systems:

AES-128, AES-192, AES-256

In the same publication, they recommend transitioning off quantum-vulnerable primitives (which notably does not include AES-128) even sooner than NIST:

The sole use of classic key agreement mechanisms is only recommended until the end of 2031, see also Section 2.3.

## Samuel Jaques agrees

Samuel Jaques is an assistant professor in the Department of Combinatorics and Optimization at the University of Waterloo, specializing in cryptography and quantum computing. You might be familiar with hisLandscape of Quantum Computing.

I foundthis 2024 slide deckafter having run all the numbers above, and I felt a bit silly having essentially re-done the same work two years later and with less domain expertise, but it’s actually encouraging how closely the conclusions match: the margin is wide enough and the relevance of guessing and optimization small enough, that we’re all repeatedly coming to equivalent conclusions.

He talks about how hard it is to build even a single logical qubit, which I am ignoring above because we are assuming a world where scalable quantum error correctiondoeshappen, or we wouldn’t be worried about asymmetric cryptography either.

He also talks about decoherence, which I only hinted at by mentioning how unlikely it is that a quantum computer canactuallyoperate for a decade uninterrupted, like we are conservatively assuming.

He makes the excellent point that the right metric to optimize Grover oracle circuits against is depth² × width, because depth contributes both to cost and to hitting the maximum depth. This suggests theLiao and Luo (2025)circuit might not be optimal, and he uses one fromJang et al. (2022)instead, but again comes to a very similar result.

Finally, he points out that each logical T-gate in a surface code architecture requires2162^{16}physical operations, so there are still terms missing in the formula before reaching a practical resource estimate.

## Why not switch anyway, you know, to be safe?

The whole post-quantum transition is about mitigating speculative risk, so why not be “safe” with symmetric keys, too? Because resources are finite, churn has a cost, and coordination is important.

The field is rushing to deploy post-quantum cryptography because experts are telling usthere is a concrete dangerto asymmetric cryptography. Conversely,the same expertsare telling us that there isnotany danger to symmetric cryptography.

Symmetric encryption is separate enough from asymmetric encryption that we usually don’t get to switch both at the same time for minimal marginal cost. For example, changing the negotiated TLS key exchange and PKI signature algorithms has little to do with changing supported cipher suites.

Conflating necessary and unnecessary changes will cause needless churn and take resources away from the urgent updates.We’re lucky we can leave the symmetric cryptography (sub-)systems untouched; we should take that blessing and focus on the work that actually needs doing,which is plenty.

There is also a complexity and coordination angle: transitioning any open ecosystem like TLS or anything that’s implemented across different libraries and programming languages requires agreeing on the target. It’s a lot easier to agree on something that’s technically accurate: we can either converge spontaneously or convince each other with technical arguments. Aiming for unnecessary and underspecified targets, instead, breeds interoperability issues and requires supporting multiple different idiosyncratic opinions, which introduces complexity.

## What about CNSA 2.0?

There is admittedly one compliance regime which requires 256-bit symmetric keys:CNSA 2.0.

That’s not a quantum computing adjustment, though: CNSA 2.0 requires a 256-bit “security level” for everything, like its predecessor Suite B always did for the Top Secret classification, and indeed mandates ML-KEM-1024 and ML-DSA-87. As far as I can tell, its intention is to avoid the very same fragmentation introduced by “security levels” by picking one oversized primitive for all settings.

By accepting AES-256 (instead of a non-existing AES-512) at the 256-bit security level, CNSA 2.0 also acknowledges that Grover’s algorithm doesn’t halve the security of AES.

It’s likely Go will implement CNSA 2.0 profiles, if nothing else because “256-bit everything” is a well-defined target that’s unlikely to move. It’s not the “secure and reasonable” target I tend to prefer, but it’s something we can commit to, unlike “secure and reasonable but with a partial misunderstanding of the security of some primitives” which can mean different things to different people.

## Are 256-bit keys always useless?

I generally believe that 256-bit “security levels” are somewhere between a comfort blanket and numerology, because as a colleague put it recently “we don’t believe in counting to21282^{128},” but that doesn’t mean 256-bit keys (or block sizes) are always useless to achieve the 128-bit security level.

When collisions are a concern andbirthday boundsare in play, the security in bits really is halved, so you need e.g. a 256-bit hash output for 128 bits of collision security. (This is why SHA-128 doesn’t exist.) Similarly, multi-target attacks, where the adversary’s advantage is measured as the chance of breaking one of many messages/keys, can require additional margin depending on how nonces are used.

These are concerns that are deep within the purview of the cryptography engineers designing the protocols, though, and not in scope for the policy-making or system administration choices. Well-designed protocols already account for all this. For example, TLS with AES-128 meets the 128-bit security level with large multi-target margins, thanks to its nonce design.

As a cryptography engineer, Idowish all ciphers took 256-bit keys, as it would make my life easier, but

1. we’ve already done the work of handling the 128-bit keys properly and switching now is going to be wasted effort we could instead put toward the actually urgent post-quantum transition; and
2. AES-256 was unfortunately defined to perform more rounds than AES-128, making it needlessly slower.

For more wishful-vs-real PQ migration, follow me on Bluesky at@filippo.abyssdomain.expertor on Mastodon at@filippo@abyssdomain.expert.

## The picture

Last month I attendedAtmosphereConf 2026, which was held atUBC. The campus is so beautiful, and there’s a spectacular path through the forest to the beach, where you can watch the sun setting over the water.

My work is made possible byGeomys, an organization of professional Go maintainers, which is funded byAva Labs,Teleport,Tailscale, andSentry. Through our retainer contracts they ensure the sustainability and reliability of our open source maintenance work and get a direct line to my expertise and that of the other Geomys maintainers. (Learn more in theGeomys announcement.)
Here are a few words from some of them!

Teleport — For the past five years, attacks and compromises have been shifting from traditional malware and security breaches to identifying and compromising valid user accounts and credentials with social engineering, credential theft, or phishing.Teleport Identityis designed to eliminate weak access patterns through access monitoring, minimize attack surface with access requests, and purge unused permissions via mandatory access reviews.

Ava Labs — We atAva Labs, maintainer ofAvalancheGo(the most widely used client for interacting with theAvalanche Network), believe the sustainable maintenance and development of open source cryptographic protocols is critical to the broad adoption of blockchain technology. We are proud to support this necessary and impactful work through our ongoing sponsorship of Filippo and his team.

1. There are sequential attacks which indeed were misinterpreted as more practical than they are. For example, astatic Diffie-Hellman oracle attack against Curve25519 or ristretto255 requires263.52^{63.5}oracle invocations, which sound practical, except they need to be sequential,making the attack take two centuries in extremely optimal circumstances.↩
2. “Gate” here meanslogicalT-gate, not physical gate. Superconducting qubits execute physical gates in ~100 ns, but a logical T-gate on an error-corrected surface-code machine is much slower. Published estimates for logical T-gate latency fall in the single-to-tens-of-microseconds range, so 1 µs sits at the conservative (for us) end.↩
3. Is Category 1 enough? Don’t we use ML-KEM-768 and ML-DSA-44 because they are Category 3 and Category 2, respectively? We do that not because Category 1 is insufficient, but because there’s concern that lattice cryptanalysis might advance slightly, and move ML-KEM-768 or ML-DSA-44 down to Category 1. There is no equivalent worry around AES, which indeed was picked as the verybarfor Category 1.↩