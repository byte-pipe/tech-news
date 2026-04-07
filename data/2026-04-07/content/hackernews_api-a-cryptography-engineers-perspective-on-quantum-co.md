---
title: A Cryptography Engineer’s Perspective on Quantum Computing Timelines
url: https://words.filippo.io/crqc-timeline/
site_name: hackernews_api
content_file: hackernews_api-a-cryptography-engineers-perspective-on-quantum-co
fetched_at: '2026-04-07T11:23:29.858701'
original_url: https://words.filippo.io/crqc-timeline/
author: thadt
date: '2026-04-06'
published_date: '2026-04-06T15:00:00Z'
description: The risk that cryptographically-relevant quantum computers materialize within the next few years is now high enough to be dispositive, unfortunately.
tags:
- hackernews
- trending
---

6 Apr 2026

# A Cryptography Engineer’s Perspective on Quantum Computing Timelines

My position on the urgency of rolling out quantum-resistant cryptography has changed compared to just a few months ago. You might have heard this privately from me in the past weeks, but it’s time to signal and justify this change of mind publicly.

There had been rumors for a while of expected and unexpected progress towards cryptographically-relevant quantum computers, but over the last week we got two public instances of it.

First,Google published a paper revising down dramatically the estimated number of logical qubits and gates required to break 256-bit elliptic curveslike NIST P-256 and secp256k1, which makes the attack doable in minutes on fast-clock architectures like superconducting qubits. They weirdly1frame it around cryptocurrencies and mempools and salvaged goods or something, but the far more important implication are practical WebPKI MitM attacks.

Shortly after,a different paper came out from Oratomic showing 256-bit elliptic curves can be broken in as few as 10,000 physical qubits if you have non-local connectivity, like neutral atoms seem to offer, thanks to better error correction. This attack would be slower, but even a single broken key per month can be catastrophic.

They have this excellent graph on page 2 (Babbush et al.is the Google paper, which they presumably had preview access to):

Overall, it looks like everything is moving: the hardware is getting better, the algorithms are getting cheaper, the requirements for error correction are getting lower.

I’ll be honest, I don’t actually know what all the physics in those papers means. That’s not my job and not my expertise. My job includes risk assessment on behalf of the users that entrusted me with their safety. What I know is what at least some actual experts are telling us.

Heather Adkins and Sophie Schmiegare telling usthat “quantum frontiers may be closer than they appear” and that2029is their deadline. That’s in 33 months, and no one had set such an aggressive timeline until this month.

Scott Aaronsontells usthat the “clearest warning that [he] can offer in public right now about the urgency of migrating to post-quantum cryptosystems” is a vague parallel with how nuclear fission research stopped happening in public between 1939 and 1940.

The timelines presented at RWPQC 2026, just a few weeks ago, were much tighter than a couple years ago, and are already partially obsolete. The joke used to be that quantum computers have been 10 years out for 30 years now. Well, not true anymore, the timelines have started progressing.

If you are thinking “well, this could be bad, or it could be nothing!” I need you to recognize howimmediately dispositivethat is. The bet is not “are you 100% sure a CRQC will exist in 2030?”, the bet is “are you 100% sure a CRQC will NOT exist in 2030?” I simply don’t see how a non-expert can look at what the experts are saying, and decide “I know better, there is in fact < 1% chance.” Remember that you are betting with your users’ lives.2

Put another way, even if the most likely outcome was no CRQC in our lifetimes, that would be completely irrelevant, because our users don’t want just better-than-even odds3of being secure.

Sure, papers about an abacus and a dog are funny and can make you look smart and contrarian on forums. But that’s not the job, and those argumentsbetray a lack of expertise. As Scott Aaronsonsaid:

Once you understand quantum fault-tolerance, asking “so when are you going to factor 35 with Shor’s algorithm?” becomes sort of like asking the Manhattan Project physicists in 1943, “so when are you going to produce at least a small nuclear explosion?”

The job is not to be skeptical of things we’re not experts in, the job is to mitigate credible threats, and there are credible experts that are telling us about an imminent threat.

In summary, it might be that in 10 years the predictions will turn out to be wrong, but at this point they might also be right soon, and that risk is now unacceptable.

## Now what

Concretely, what does this mean? It means we need to ship.

Regrettably, we’ve got to roll out what we have.4That meanslarge ML-DSA signaturesshoved in places designed for small ECDSA signatures, like X.509, with the exception of Merkle Tree Certificates for the WebPKI, which is thankfullyfar enough along.

This isnotthe article I wanted to write. I’ve had a pending draft for months now explaining we should ship PQ key exchange now, but take the time we still have to adapt protocols to larger signatures, because they were all designed with the assumption that signatures are cheap. That other article is now wrong, alas: we don’t have the time if we need to be finished by 2029 instead of 2035.

For key exchange, the migration to ML-KEM is going well enough but:

1. Anynon-PQ key exchangeshould now be considered a potential active compromise, worthy of warning the userlike OpenSSH does, because it’s very hard to make sure all secrets transmitted over the connection or encrypted in the file have a shorter shelf life than three years.
2. We need to forget aboutnon-interactive key exchanges (NIKEs)for a while; we only have KEMs (which are only unidirectionally authenticated without interactivity) in the PQ toolkit.

It makes no more sense to deploynew schemes that are not post-quantum. I know, pairings were nice. I know, everything PQ is annoyingly large. I know, we had basicallyjustfigured out how to do ECDSA over P-256 safely. I know, there might not be practical PQ equivalents for threshold signatures or identity-based encryption. Trust me, I know it stings. But it is what it is.

Hybrid classic + post-quantum authentication makes no senseto me anymore and will only slow us down; we should go straight to pure ML-DSA-44.6Hybrid key exchange is reasonably easy, with ephemeral keys that don’t even need a type or wire format for the composite private key, and a couple years ago it made sense to take the hedge. Authentication is not like that, and even withdraft-ietf-lamps-pq-composite-sigs-15with its 18 composite key types nearing publication, we’d waste precious time collectively figuring out how to treat these composite keys and how to expose them to users. It’s also been two years since Kyber hybrids and we’ve gained significant confidence in the Module-Lattice schemes. Hybrid signatures cost time and complexity budget,5and the only benefit is protection if ML-DSA is classically brokenbefore the CRQCs come, which looks like the wrong tradeoff at this point.

Insymmetric encryption, we don’t need to do anything, thankfully. There is a common misconception that protection from Grover requires 256-bit keys, butthat is based on an exceedingly simplified understanding of the algorithm. A more accurate characterization is that with a circuit depth of 2⁶⁴ logical gates (the approximate number of gates that current classical computing architectures can perform serially in a decade) running Grover on a 128-bit key space would require a circuit size of 2¹⁰⁶. There’s been no progress on this that I am aware of, and indeed there are old proofs thatGrover is optimal and its quantum speedup doesn’t parallelize. Unnecessary 256-bit key requirements are harmful when bundled with the actually urgent PQ requirements, because they muddle the interoperability targets and they risk slowing down the rollout of asymmetric PQ cryptography.

In my corner of the world, we’ll have to start thinking about what it means for half thecryptography packages in the Go standard libraryto be suddenly insecure, and how to balance the risk of downgrade attacks and backwards compatibility. It’s the first time in our careers we’ve faced anything like this: SHA-1 to SHA-256 was not nearly this disruptive,7and even that took forever with the occasional unexpected downgrade attack.

Trusted Execution Environments (TEEs)like Intel SGX and AMD SEV-SNP and in general hardware attestation are just f***d. All their keys and roots are not PQ and I heard of no progress in rolling out PQ ones, which at hardware speeds means we are forced to accept they might not make it, and can’t be relied upon. I had to reassess a whole project because of this, and I will probably downgrade them to barely “defense in depth” in my toolkit.

Ecosystems with cryptographic identities(likeatprotoand, yes, cryptocurrencies) need to start migrating very soon, because if the CRQCs come before they aredone, they will have to make extremely hard decisions, picking between letting users be compromised and bricking them.

File encryption is especially vulnerable to store-now-decrypt-later attacks, so we’ll probably have to start warning and then erroring out on non-PQage recipient typessoon. It’s unfortunately only been a few months since we even added PQ recipients, inversion 1.3.0.8

Finally, this week I startedteachinga PhD course in cryptography at the University of Bologna, and I’m going to mention RSA, ECDSA, and ECDH only as legacy algorithms, because that’s how those students will encounter them in their careers. I know, it feels weird. But it is what it is.

For more willing-or-not PQ migration, follow me on Bluesky at@filippo.abyssdomain.expertor on Mastodon at@filippo@abyssdomain.expert.

## The picture

Traveling back from an excellentAtmosphereConf 2026, I saw my first aurora, from the north-facing window of a Boeing 747.

My work is made possible byGeomys, an organization of professional Go maintainers, which is funded byAva Labs,Teleport,Tailscale, andSentry. Through our retainer contracts they ensure the sustainability and reliability of our open source maintenance work and get a direct line to my expertise and that of the other Geomys maintainers. (Learn more in theGeomys announcement.)
Here are a few words from some of them!

Teleport — For the past five years, attacks and compromises have been shifting from traditional malware and security breaches to identifying and compromising valid user accounts and credentials with social engineering, credential theft, or phishing.Teleport Identityis designed to eliminate weak access patterns through access monitoring, minimize attack surface with access requests, and purge unused permissions via mandatory access reviews.

Ava Labs — We atAva Labs, maintainer ofAvalancheGo(the most widely used client for interacting with theAvalanche Network), believe the sustainable maintenance and development of open source cryptographic protocols is critical to the broad adoption of blockchain technology. We are proud to support this necessary and impactful work through our ongoing sponsorship of Filippo and his team.

1. The whole paper is a bit goofy: it has a zero-knowledge proof for a quantum circuit that will certainly be rederived and improved upon before the actual hardware to run it on will exist. They seem to believe this is about responsible disclosure, so I assume this is just physicists not being experts in our field in the same way we are not experts in theirs.↩
2. “You” is doing a lot of work in this sentence, but the audience for this post is a bit unusual for me: I’m addressing my colleagues and the decision-makers that gate action on deployment of post-quantum cryptography.↩
3. I had a reviewer object to an attacker probability of success of 1/536,870,912 (0.0000002%, 2⁻²⁹) after 2⁶⁴ work, correctly so, because in cryptography we usually target 2⁻³².↩
4. Why trust the new stuff, though? There are two parts to it: the math and the implementation. The math is also not my job, so I again defer to experts like Sophie Schmieg, whotells us that she is very confident in lattices, and the NSA, who approved ML-KEM and ML-DSA at the Top Secret level for all national security purposes. It is also older than elliptic curve cryptography was when it first got deployed. (“Doesn’t the NSA lie to break our encryption?” No, the NSA has never intentionally jeopardized US national security with a non-NOBUSbackdoor, andthere is no way for ML-KEM and ML-DSA to hide a NOBUS backdoor.) On the implementation side, I am actually very qualified to have an opinion, having made cryptography implementation and testing my niche. ML-KEM and ML-DSA are a lot easier to implement securely than their classical alternatives, and with thebetter testing infrastructurewe have now I expect to see exceedingly few bugs in their implementations.↩
5. One small exception in that if youalreadyhave the ability to convey multiple signatures from multiple public keys in your protocol, it can make sense to to “poor man’s hybrid signatures” by just requiring 2-of-2 signatures from one classical public key and one pure PQ key. Some of the tlog ecosystem might pick this route, but that’sonlybecause the cost is significantly lowered by the existing support for nested n-of-m signing groups.↩
6. Why ML-DSA-44 when we usually use ML-KEM-768 instead of ML-KEM-512? Because ML-KEM-512 is Level 1, while ML-DSA-44 is Level 2, so it already has a bit of margin against minor cryptanalytic improvements.↩
7. Because SHA-256 is a better plug-in replacement for SHA-1, because SHA-1 was a much smaller surface than all of RSA and ECC, and because SHA-1 was notthatbroken: it still retained preimage resistance and could still be used in HMAC and HKDF.↩
8. The delay was in large part due to my unfortunate decision of blocking on the availability of HPKE hybrid recipients, which blocked on the CFRG, which tookalmost two yearsto select a stable label string for X-Wing (January 2024) with ML-KEM (August 2024), despite making precisely no changes to the designs. The IETF should have an internal post-mortem on this, but I doubt we’ll see one.↩