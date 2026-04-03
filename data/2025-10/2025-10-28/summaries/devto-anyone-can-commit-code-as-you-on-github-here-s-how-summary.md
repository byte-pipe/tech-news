---
title: "Anyone Can Commit Code as You on GitHub (Here's How to Stop Them) - DEV Community"
url: https://dev.to/nickytonline/anyone-can-commit-code-as-you-on-github-heres-how-to-stop-them-2in7
date: 2025-10-26
site: devto
model: llama3.2:1b
summarized_at: 2025-10-28T11:16:53.337232
screenshot: devto-anyone-can-commit-code-as-you-on-github-here-s-how.png
---

# Anyone Can Commit Code as You on GitHub (Here's How to Stop Them) - DEV Community

**Git Commit Signing with GPG (GNU Privacy Guard)**

### Introduction to GPG Encryption and Signing

GPG (GNU Privacy Guard) is an open-source implementation of the OpenPGP standard for encrypting and signing data. In this context, GPG is used to sign Git commits, verifying that the commit was made by the actual owner of the repository.

**Key Features of GPG**

* **Secure Signatures**: GPG creates cryptographic signatures that prove the commit came from someone with access to the private key.
* **Authenticity**: The "Verified" badge indicates that the commit actually came from the key holder, not just a named impersonator.
* **Compliance**: In regulated industries, signed commits are critical for compliance and auditing.

**Why Sign Your Commits?**

Signing Git commits provides three main benefits:

1.  **Protection against impersonation**: GPG ensures that only the actual owner of the repository can commit changes.
2.  **Audit trail control**: Signed commits create a secure audit trail, allowing organizations to verify who made changes and when they were committed.
3.  **Supply chain security**: Signed commits make it difficult for attackers to inject malicious code into widely-used libraries.

**Benefits of Implementing GPG in Git Repitories**

*   Systems care: Organizations require signed commits through branch protection rules.
*   Compliance industries need them: Regulated sectors demand proof of legitimate changes.
*   Security tools flag suspicious repositories without GPG setup.

This guide is tailored for macOS, using the built-in `gpg` command-line tools. If you're on Linux or Windows, similar approaches apply but utilize different tools.

**Step-by-Step Guide to Setting Up Git Commit Signing with GPG**

1.  Install GPG tools:
    *   On macOS: Open Terminal and run `brew install gnuPG` (or `gitgpg` for more advanced options).
2.  Configure Git to use your name and email as the identity:
    *   Run `git config --global user.name "Your Name"` and `git config --global user.email "youremail@example.com"`.
3.  Sign commits using GPG:
    *   When committing, use the `-s` flag with git: `git add . && git commit -s -m "commit message"`.
4.  Verify the signing badge: Open your repository on GitHub and review the "Verified" badge under the login page.
