---
title: AI Cryptanalysis Could Break Encryption Before Quantum
url: https://www.cybrsecmedia.com/ai-may-beat-quantum-to-the-first-cryptographic-surprise
site_name: tldr
content_file: tldr-ai-cryptanalysis-could-break-encryption-before-qua
fetched_at: '2026-10-17T14:04:10.755915'
original_url: https://www.cybrsecmedia.com/ai-may-beat-quantum-to-the-first-cryptographic-surprise
date: '2026-10-17'
published_date: '2026-10-16T17:58:15.000Z'
description: AI-assisted cryptanalysis may threaten encryption before quantum computers arrive. Experts urge crypto agility, inventories and post-quantum planning.
tags:
- tldr
---

AI and Quantum Computing
 — 
AI and crypto-agility
 — 
Article

# AI May Beat Quantum to the First Cryptographic Surprise

AI-assisted cryptanalysis may threaten encryption before quantum computers arrive. Experts urge crypto agility, inventories and post-quantum planning.

, 

 and 

George V. Hulme

 

 October 16, 2026

 
 . 12:58 PM

7 min read
 

* 𝕏
* Share on Facebook
* Share on LinkedIn
* Share via Email
 

"We might lose public key cryptography," the Johns Hopkins cryptographer Matthew Greenpostedon X on October 7, 2026. By the end of the day, the post had traveled far enough that Green spent much of the next week explaining what he *hadn't* said.

He hadn't said RSA was broken, that anyone should stop using encrypted messaging, or that Bitcoin was doomed. He said something more specific and, for enterprise security teams, perhaps even more consequential: AI-assisted research is finding cryptographic shortcuts faster than expected. That speed could make existing post-quantum migration plans too slow.

The AI newcomer to the cryptographic race comes after post-quantum cryptography readiness timelines had already been moved up considerably.

Subscribe to the CYBR.SEC.Media newsletter

Green's post landed one day after OpenAIpublishedhundreds of AI-assisted potential solutions to long-open math problems, and three months after researchers at Anthropicdisclosedthat their Claude Mythos model had found a key-recovery attack on HAWK, alattice-basedsignature scheme the National Institute of Standards and Technology is evaluating. HAWK's designers withdrew it from consideration within days. A separate study, CryptanalysisBench,reportednovel cryptanalysis from frontier AI models: a full key-recovery attack on the SpoC authenticated-encryption cipher and an error in KINDI's published proof of security against chosen-ciphertext attacks. Those results were previously unknown, at least publicly so.

"When does AI find a major exploit for RSA encryption or some other encryption standard? And does AI get there faster than quantum computing? I think it's an unknown, but definitely a concern," Rob Gregory, VP and CISO at Optiv, told CYBR.SEC.Media.

For enterprises, that means post-quantum cryptography migration, the planned replacement of RSA (The algorithm developed by Rivest, Shamir, and Adleman whose security depends on the difficulty of factoring large numbers) and elliptic-curve systems with algorithms believed to resist quantum computers, is no longer a one-time standards swap to finish by 2030 for many federal agencies, or a one-and-done exercise for anyone else. It is the first iteration of a recurring exercise: find every place the organization relies on public-key math, build the machinery to replace it, and be ready to do it again.

## What the withdrawn NIST candidate did and didn't touch

Until this year, quantum computers were the cryptographic concern. Shor'salgorithm, running on a sufficiently powerful quantum machine, can efficiently solve the mathematical problems underpinning most public-key cryptography today: RSA factoring and elliptic-curve discrete logarithms. That threat drove NIST tofinalizeits first post-quantum standards in 2024, including ML-KEM for key exchange and ML-DSA for digital signatures. Federal agencies must move their most sensitive systems toPQCfor key establishment by the end of 2030 andfor digital signaturesby the end of 2031.

AI-assisted cryptanalysis may work differently. It does not need a cryogenic quantum machine. It needs compute, training data, and the ability to find hidden patterns in mathematical structures. In July, Anthropic's Claude Mythos Preview found an attack on HAWK that effectively halved the scheme's expected security level, reducing the attack cost for HAWK-256 from roughly 2^64 operations to about 2^38. The CryptanalysisBench paper described models finding flaws in SpoC and KINDI. None of these were deployed standards, and NIST has said the HAWK finding does not affect its finalized schemes, which rest on different mathematical foundations. The takeaway: a model spotted a weakness in a NIST candidate before the candidate could be standardized.

That is why awarningfrom Justin Drake's October 7 landed so hard. Drake, a researcher at the Ethereum Foundation, wrote that it is now "reasonable to brace for the possibility that ECDSAbreaksbefore qday, in the worst case in months, not years." ECDSA, the Elliptic Curve Digital Signature Algorithm, secures Bitcoin, Ethereum, and much of the code-signing and certificate infrastructure. "Qday" is the shorthand cryptographers use for the moment a quantum computer can break current encryption at scale. By "break," Drake meant fast private-key recovery on existing hardware, a large GPU cluster, not a cryogenic quantum machine.

## What quantum and AI could each break

The two mathematical threats are different, which is part of what makes them hard to plan for together. Quantum computing, if it arrives, is expected to be a broad-spectrum break: RSA, ECDSA, and Diffie-Hellman fall more or less concurrently. AI-assisted cryptanalysis will be narrower and more opportunistic as researchers can now use it to find specific shortcuts in specific structures. But the practical consequence for enterprises is similar. Both shorten the assumed safe lifetime of encrypted data.

Google's quantum-AI team released awhite paperin March estimating that breakingsecp256k1, the elliptic curve used by Bitcoin and many other systems, would require fewer than 500,000 physical qubits, roughly a twenty-fold reduction from previous estimates. The realistic window experts now discuss for a capable quantum machine runs from 2030 to 2035. AI acceleration, if it materializes, would run concurrently.

The systems at risk are specific. Transport Layer Security certificates protect web traffic. Code-signing keys verify software updates. Public-key infrastructure anchors identity. Virtual private networks protect remote access. Then there is any data whose confidentiality must survive into the 2030s.

The immediate danger is not necessarily a break tomorrow but harvest-now-decrypt-later: adversaries recording encrypted traffic today to decrypt whenever the math falls, whether by qubit or by AI-discovered shortcut.

## How worried should you be? Cryptographers disagree on the odds

For Coinbase and the exchanges that custody billions in Bitcoin, the threat is, for now, theoretical. Yehuda Lindell, Coinbase's head of cryptography, cast serious doubt on the fear that AI advances threaten elliptic-curve cryptography. "There is no evidence whatsoever pointing to a break of decades-old hardness assumptions like elliptic curve cryptography," he wrote in an October 7 Xthread, and the idea that "AI is doing amazing math so elliptic curve hardness is in dangerhas no logical basis whatsoever." The best-known classical attacks on 256-bit curves still require about 2^128 operations, a figure that Rob Hamilton, ina red-team analysis of Bitcoin's secp256k1 curve, traced to the square-root cost of generic discrete-log algorithms—meaning the math protecting Bitcoin has not been improved upon by AI or human cryptanalysts.

Eddy Lazzarin, general partner at a16z crypto, made a similar point on the firm'spanel discussion: the recent results do not mean elliptic curves are newly vulnerable. "We didn't learn that elliptic curves are vulnerable in a way that they weren't before," he said. "We didn't learn that any specific cryptographic assumptions have less security than they did before." Dan Boneh, who leads Stanford's applied cryptography group, acknowledged on the same panel that the newly published AI math results contained "no questions here on cryptography," leaving open what models can actually do.

Drake himself labeled his "months, not years" timeline a worst-case conjecture, not a forecast. Green, after his "We might lose public key cryptography" post went viral,calibrated his own warningto roughly 15% odds that confidence is lost in existing public-key encryption systems and 1% odds of losing public-key cryptography entirely. Haseeb Qureshi, managing partner at Dragonfly, wrote in anessay, "Against Cryptographic Doomerism," that even if the chance of a fundamental break is low enough to leave a 95% probability that "everything is totally fine," the asymmetric costs—wasted preparation versus catastrophic surprise—favor preparing anyway.

Vitalik Buterin, the Ethereum co-founder,warnedthat the cryptographic risk exposure extends beyond elliptic curves. He added that AI-assisted research over the next two years could weaken the lattice constructions underpinning post-quantum replacements. That matters because lattices underpinML-KEMandML-DSA, the very standards enterprises are being asked to adopt. If AI finds weaknesses there too, migration deadlines get shorter and confidence erodes.

In his follow-up thread, Green redirected the conversation from panic to planning. Losing public-key cryptography does not mean encryption becomes impossible, he wrote. It means a wave of new cryptanalytic results that erode security margins, forcing standards bodies to deprecate smaller parameter sets and crank up parameter sizes. His one serious ask was not urgent migration but contingency planning: the speed of AI surprises and the speed of replacing standards "are just orders of magnitude different," so "you only recover from a surprise like this if you do the preparation in advance."

"All I want is for cryptographers and security engineers to have a plan in the event that something bad happens," Green said on October 9. "And yelling 'oh fuck’ isn't a plan."

## The four moves that mitigate AI, PQC risk

Take inventory.
 Most large organizations do not know everywhere they rely on RSA, ECDSA, or Diffie-Hellman. Certificates hide in forgotten subdomains. Firmware-signing keys sit in build pipelines. Vendor dependencies chain through layers of outsourced software. "This is the number one item on the agenda," Gregory said. "You have to understand where your encrypted data is, what keys it is encrypted with, and what options those platforms have for encryption standards." 
Rank by data lifespan.
 Data that must stay confidential into the 2030s, root certification authorities, and long-lived firmware-signing chains should move first. How long the data must stay secret is the best proxy for how fast it needs protection.
Use hybrid mode where possible
, running classical and post-quantum algorithms in parallel so security holds unless both fail. NIST's guidance permits 
hybrid solutions
 during the transition, and they hedge against both the quantum threat and the possibility that a freshly standardized 
PQC
 algorithm turns out to have an AI-discovered weakness. "I’ve started using a phrase called crypto agility, which means the ability to bring your own encryption. You need to be able to change the encryption standard on a whim,” Gregory said. 
Write cryptographic agility into contracts
, making it a contractual and architectural requirement. Betting on any single algorithm is not a strategy. Buying the ability to swap algorithms without re-architecting is.

The organizations that will handle this transition are not the ones that best predict whether quantum computing breaks crypto or AI does. They are the ones that can change algorithms faster than their adversaries can exploit what they're using. "Being 90% of the way ready does you nothing. If you're not 100% of the way ready to go, you're just as vulnerable as somebody that didn't do anything," Gregory said.

Related:

Crypto Agility: Preparing Encryption for Quantum Threats
As quantum computers become cryptographically relevant, agentic networks will have to keep one step ahead of the decryption storm.
CYBR.SEC.Media
Andy Ellis

## Latest

How to CISO

### Crypto Agility: Preparing Encryption for Quantum Threats

As quantum computers become cryptographically relevant, agentic networks will have to keep one step ahead of the decryption storm.

, 

 and 

Andy Ellis

 October 16, 2026

 

 

Cybersecurity Investment

### AI Gets the Billions. Cybersecurity Defenders Get the Burnout.

As AI's creators cash in on FUD, cybersecurity teams face growing threats and mounting exhaustion. Plus: overlooked startups and practical guardrails that deserve attention.

, 

 and 

Bill Brenner

 October 15, 2026

 

 

AI security certifications

### HITRUST Expands AI Security Certification and Risk Tools

HITRUST expands AI security certification, adds agentic AI controls and automates third-party risk assessments and report sharing.

, 

 and 

Bill Brenner

 October 15, 2026

 

 

Burnout

### Cybersecurity Burnout Doesn't Always Announce Itself. Sometimes It Starts With a Longer To-Do List.

CYBR.SEC.Community Co-Founder Sam Van Ryder shares his personal experience with burnout, the warning signs he nearly missed, and why cybersecurity professionals need to recognize exhaustion before it becomes a crisis.

, 

 and 

Bill Brenner

 October 15, 2026