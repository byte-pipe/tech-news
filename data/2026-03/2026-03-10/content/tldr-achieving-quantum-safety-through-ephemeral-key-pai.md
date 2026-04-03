---
title: Achieving Quantum Safety Through Ephemeral Key Pairs and Account Abstraction - Cryptography - Ethereum Research
url: https://ethresear.ch/t/achieving-quantum-safety-through-ephemeral-key-pairs-and-account-abstraction/24273
site_name: tldr
content_file: tldr-achieving-quantum-safety-through-ephemeral-key-pai
fetched_at: '2026-03-10T11:15:50.518788'
original_url: https://ethresear.ch/t/achieving-quantum-safety-through-ephemeral-key-pairs-and-account-abstraction/24273
date: '2026-03-10'
published_date: '2026-03-04T10:24:40+00:00'
description: Achieving Quantum Safety Through Ephemeral Key Pairs and Account Abstraction Thanks to @abaiocchi for his contributions and to @asanso for his feedback Abstract We propose a quantum-safe wallet design that requires no c&hellip;
tags:
- tldr
---

# Achieving Quantum Safety Through Ephemeral Key Pairs and Account Abstraction

Cryptography

account-abstraction
, 
 
post-quantum

mvicari

 March 4, 2026, 10:24am
 

1

# Achieving Quantum Safety Through Ephemeral Key Pairs and Account Abstraction

Thanks to@abaiocchifor his contributions and to@asansofor his feedback

## Abstract

We propose a quantum-safe wallet design that requires no changes to Ethereum’s signature schemes or protocol rules. By leveraging account abstraction, we make each ECDSA key pair single-use: every transaction rotates the signer while the smart contract wallet address remains constant. This eliminates long-term public key exposure, the core vulnerability that Shor’s algorithm would exploit, using only today’s infrastructure. This aims to solve, at least in the short term, quantum security on the execution layer.

## Introduction

The quantum threat to elliptic curve cryptography is no longer a distant concern. Shor’s algorithm efficiently solves the discrete logarithm problem and, as a result, ECDSA. While a cryptographically relevant quantum computer doesn’t exist yet, the timeline is shrinking. The Ethereum Foundation has established dedicated post-quantum research efforts, and Vitalik has recently outlined abroader PQ roadmap.

On Ethereum, an EOA that has never transacted is effectively quantum-safe, since its public key is hidden behind a hash. But the moment it signs a transaction, the public key is permanently exposed onchain, making that address effectively burned from a quantum-resistance standpoint.

Significant work is being done to bring post-quantum signature schemes directly to the EVM, most notably Falcon (1,2,3,ETHFALCON) andPoqeth. These efforts are essential for the long term, but onchain verification still costs upwards of 1M gas for Falcon, while hash-based signatures are currently in the ~200k gas range. These costs could be further reduced byEIP-8051andEIP-8052, once they get added to the EVM.

Gas cost is not the only challenge in the way of post-quantum signatures: standardization, hardware wallet compatibility and proven resistance to classical attacks are significant obstacles that a new standard for ETH signatures will need to overcome. Even if such a signature was ready, standardization needs time, and fully replacing ECDSA requires protocol-level changes (EIP-7701,RIP-7560). Our approach is complementary: rather than replacing ECDSA, we make it disposable.

## Proposed Design

We can leverage Account Abstraction to maintain a static identity towards the rest of the blockchain (the smart account), while switching the signer’s identity after every transaction. This does not prevent quantum computers from recovering the user’s private key, rather makes the private key that was used to sign the previous transaction useless to sign any future transaction.

The scheme is really simple:

1. User appends an address to the calldata of his userOp
2. The Smart Contract Wallet validates the transaction
3. The userOp is executed
4. The authorized signer on the Smart Contract Wallet is changed to the new address

After the transaction is executed, the old private key, even if recovered, is completely useless. Only the address has been communicated to the Smart Contract Wallet, so only part of the hash of the public key has been revealed, making the new private key quantum-safe until the next transaction.

A few practical considerations can be done to ease the process: for instance the user, instead of choosing an arbitrary new address, can generate the addresses to send following a BIP44 derivation path, which is also widely available on currently employed wallets.

scheme1466×712 53.3 KB

## Practical Implementation

This design can be implemented by making some minor tweaks to the baseSimpleWallet. All we need is a way to extract the next caller from the calldata and change the owner of the Smart Contract Wallet. We implemented a proof of concept at thisrepo.

This implementation also aims to solve a key issue we identified: we need to rotate the signer even if the userOp reverts. Otherwise a failed transaction would mean that the current signer of the Smart Contract Wallet is currently exposed. We instead emit an event if a userOp fails, but we still finalize the transaction and execute the rotation part.

With this implementation we recorded some transactions (example) and we measured ~136k gas units for an ERC20 transfer, a gas overhead of less than 100k with respect to the same token transfer on the same chain (example). This overhead, which is already significantly lower than post quantum signature verifications as of today, comes with the added benefits of Account Abstraction. The gas cost of the user rotation itself, if added to a pre-existing Account Abstraction based wallet is even lower and almost negligible in the greater picture.

### Social Recovery Repurposing

Another way of achieving the same procedure is by exploiting existing social recovery features of Smart Contract Wallets. Unless some ad-hoc limitation forbids this, we can set the recovery guardian for our account to our own address, requesting an identity recovery after every transaction. This comes with a slightly higher gas cost, since we’re abusing a feature meant for a different purpose, but has the upside of being able to start using this quantum-safe wallet design without deploying custom architectures onchain.

Our experiments with this method show that the gas cost overhead that can be expected for this operation is ~30k, while the whole gas overhead of the architecture we were using (without recovery) was around ~110k.[1]

## Known Vulnerabilities

There is a vulnerability to this design that we are aware of: themempool waiting period. In this period the user’s public key is visible and a quantum-capable attacker could retrieve his private key and frontrun him.

This issue is not that deeply concerning at the moment, given that the restricted timeframe the attacker would have to recover the private key would make this exploit extremely harder to exploit if not impossible. If one wants to be completely safe though, the use ofprivate mempoolscan completely eliminate the issue. Furthermore, the vulnerability would be mitigated in the context of L2s due to shorter waiting periods.

## Conclusion

We presented a scheme that achieves quantum safety on the execution layer by rotating ECDSA key pairs after every transaction, using account abstraction to preserve a stable on-chain identity. The approach requires no protocol changes and introduces minimal gas overhead (~100k over a standard transfer). It does not replace post-quantum signature schemes, which remain necessary for a complete long-term solution, but it eliminates long-term public key exposure using only current infrastructure. The main open question is mempool-level exposure: while a transaction is pending, the current signer’s public key is visible, and private mempools are the most immediate mitigation.

1. ERC20 transferfrom EOA,with simple AA,with AA and rotation.↩︎

6 Likes