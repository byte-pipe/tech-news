---
title: Quantum Computers Are Not a Threat to 128-bit Symmetric Keys
url: https://words.filippo.io/128-bits/
date: 2026-04-20
site: hnrss
model: llama3.2:1b
summarized_at: 2026-04-21T12:01:46.430222
---

# Quantum Computers Are Not a Threat to 128-bit Symmetric Keys

## Quantum Computers and Symmetric Keys: A Summary

Quantum computers pose a threat to various cryptographic algorithms, but replacing existing asymmetric cryptography with post-quantum primitives may not be necessary as it does not affect the security of symmetric key algorithms. There's a common misconception that quantum computers can halve the available cryptographic keys, making 128-bit keys unsafe.

## The Misunderstanding

Instead, researchers like Shor have shown that certain quantum algorithms, such as Grover's, can efficiently find keys for 128-bit symmetric encryption keys. These algorithms often imply the use of a different quantum algorithm, not Grover's specifically.

### What Actually Happens with Grover's

Grover's algorithm can efficiently search an input space for a specific function in O(N^(1/4) \* √N), where N is the number of bits. However, this speedup comes with significant limitations:

*   The "search time" claimed by Grover's to find an AES-128 key is approximately 2^64 seconds or about 3,000 years.
*   Even running it in parallel across multiple CPU cores would take well over a day.

### Is 128-bit Symmetric Keys Safe?

Currently, existing symmetric algorithms like AES and SHA-256 are safe against quantum computers. The focus of the post-quantum transition should be on addressing the performance concerns rather than reducing key sizes.

## In Conclusion

Quantum computers have raised intriguing questions about the threat they pose to encryption methods. However, the current understanding suggests that even symmetric algorithms for 128-bit keys are still securely available and do not need to change as part of a post-quantum transition.

This summary highlights the importance of accurately interpreting quantum algorithm speedsup claims and their implications on existing cryptographic practices. It also emphasizes the focus on improving key management rather than making changes based solely on reduced key sizes or theoretical improvements in computational power.