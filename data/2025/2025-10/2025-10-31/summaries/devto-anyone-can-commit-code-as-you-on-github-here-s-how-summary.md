---
title: "Anyone Can Commit Code as You on GitHub (Here's How to Stop Them) - DEV Community"
url: https://dev.to/nickytonline/anyone-can-commit-code-as-you-on-github-heres-how-to-stop-them-2in7
date: 2025-10-26
site: devto
model: llama3.2:1b
summarized_at: 2025-10-31T11:53:09.505101
screenshot: devto-anyone-can-commit-code-as-you-on-github-here-s-how.png
---

# Anyone Can Commit Code as You on GitHub (Here's How to Stop Them) - DEV Community

**Git Commit Signing with GPG**

* **Why sign your commits?**: Commit impersonation, open source contributions, work environments, audit trails, and supply chain attacks are just a few scenarios where signing commits matters.
* **Does anyone care about verification badges?**: Most developers don't check them, but systems do. Organizations require signed commits through branch protection rules, regulated industries need them for compliance, security tools flag repositories without them, and supply chain attacks make signed commits necessary.

**Key Points**

* GPG (GNU Privacy Guard) is an open-source implementation of the OpenPGP standard for encrypting and signing data
* Signing a commit with GPG proves it came from someone with access to your private key, not just someone who knows your name and email address

**Signatures and Verification**

* Signed commits show the commit hash, message hash (calculated with GPG), and SHA-1 sum (calcualted with Git)
* The "Verified" badge indicates that only you can create these signatures
* Anyone impersonating you could use a compromised account to sign your commits

**GPG Tools for macOS**

* Install gpg (`$brew install gpg` or `sudo apt-get install gnupg`)
* Use the command line tool (-e, -u) and add your key to GPG Keychain.
