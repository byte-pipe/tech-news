---
title: Claude Code Can Debug Low-level Cryptography
url: https://words.filippo.io/claude-debugging/
date: 2025-11-02
site: hackernews
model: llama3.2:1b
summarized_at: 2025-11-02T11:09:25.872709
screenshot: hackernews-claude-code-can-debug-low-level-cryptography.png
---

# Claude Code Can Debug Low-level Cryptography

## Claude Code Can Debug Low-level Cryptography

After four days of writing a new Go implementation of ML-DSA, my code was rejected by Verify because it doesn't verify signatures correctly.

### Identifying the Bug

I found that Verify was rejecting valid signatures because I had merged HighBits and w1Encode into a single function for using them in Sign. However, this merge also causes incorrect behavior later on when checking the high bits in Verify.

### Analyzing the Code

Upon analyzing my code with Claude Code, it quickly pointed out the issue: merging HighBits and w1Encode incorrectly.

### Conclusion

 Claude Code significantly improved my verification tests for ML-DSA, identifying a complex low-level bug that was causing incorrect signature verification. This highlights the importance of using AI tools to help debug seemingly intractable issues when working on novel cryptographic algorithms.

## Key Points

*   Claude Code helped identify and fix a key bug in the verification process.
*   The issue was caused by merging HighBits and w1Encode together, leading to incorrect high-bit processing after Sign.
*   Verification was rejecting valid signatures due to this error.
*   Analyzing my code with Claude Code revealed the root cause of the problem.
