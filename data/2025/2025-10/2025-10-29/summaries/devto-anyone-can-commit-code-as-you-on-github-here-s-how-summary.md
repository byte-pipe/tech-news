---
title: "Anyone Can Commit Code as You on GitHub (Here's How to Stop Them) - DEV Community"
url: https://dev.to/nickytonline/anyone-can-commit-code-as-you-on-github-heres-how-to-stop-them-2in7
date: 2025-10-26
site: devto
model: llama3.2:1b
summarized_at: 2025-10-29T11:18:36.043734
screenshot: devto-anyone-can-commit-code-as-you-on-github-here-s-how.png
---

# Anyone Can Commit Code as You on GitHub (Here's How to Stop Them) - DEV Community

# Sign Your Git Commits with GPG for Enhanced Security
===========================================================

### Key Points

* Signing commits using GPG (GNU Privacy Guard) encrypts the commit, proving it came from yourself
* By default, your name and email are used in the commit authors on GitHub
* The "Verified" badge indicates a verified commit, but is not required for all platforms
* Signatures can help prevent impersonation, audit trails, regulated compliance, and supply chain attacks

### What is GPG?

GPG (GNU Privacy Guard) is an open-source implementation of the OpenPGP standard for encrypting and signing data. It's widely used for securing communication and authentication.

### Why Sign Your Commits?

Signing commits allows you to prove ownership and ensure your identity while using them in version control systems like Git.

* **Real-World Impersonation Examples**: Using a different identity can affect open source contributions, work environments, audit trails, security audits, and supply chain attacks.
* The "Verified" badge on GitHub is essential for maintaining the integrity of commits and preventing impersonation.

### Signatures in Practice

1.  **Git Configuration**: Set your commit authors to your name and email using `git config --global user.name <username>` and `git config --global user.email <email>`
2.  **Verification Badge**: Use the "Verified" badge on GitHub, but it's not always required or visible
3.  **Platform-Specific Tools**: Use tools like GPG Keychain for macOS (recommended) or Linux/Windows to manage your keys securely

**Conclusion**
----------

Regularly signing your Git commits with GPG provides an additional layer of security and authenticity, helping protect against impersonation and other potential issues in version control systems.
