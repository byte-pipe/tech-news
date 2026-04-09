---
title: "Anyone Can Commit Code as You on GitHub (Here's How to Stop Them) - DEV Community"
url: https://dev.to/nickytonline/anyone-can-commit-code-as-you-on-github-heres-how-to-stop-them-2in7
date: 2025-10-26
site: devto
model: llama3.2:1b
summarized_at: 2025-11-02T11:20:48.410184
screenshot: devto-anyone-can-commit-code-as-you-on-github-here-s-how.png
---

# Anyone Can Commit Code as You on GitHub (Here's How to Stop Them) - DEV Community

**Signing Git Commits Using GPG on GitHub**

GPG (GNU Privacy Guard) is a cryptographic system that ensures the integrity of data by authenticating the sender and encrypting the message. When signed with GPG, you can prove that you, alone, made the commit.

### What is GPG?

GPG uses open-source implementation of the OpenPGP standard for encrypting and signing data. This provides a secure way to sign commits, ensuring only someone with access to your private key can make the signature.

**Why Sign Your Commits?**

Sign your commits to prevent impersonation:

* Stop malicious contributors from pretending under your identity
* Ensure audit trails are accurate by proving who committed what code
* Comply with regulated industries through signed commits
* Protect against supply chain attacks by verifying repository integrity

### Key Benefits of Signed Commits

1.  **Real-world Impersonation Examples**: Sign your commits to prevent being impersonated in scenarios like open-source contributions, work environments, and audit trails.
2.  **Compliance**: Regulated industries require signed commits for proof of origin, increasing security when working with them.
3.  **Supply Chain Attacks**: Signed commits are the only way to detect malicious code injected into widely-used libraries without detection.

### Who Should Care About Signed Commits?

1.  **Systems**: Organizations consider signed commits through branch protection rules and require them for compliance.
2.  **Regulated Industries**: Security tools flag repositories withoutsigned commits, making GPG required for legitimate uses.
3.  **Security Risks**: Unverified commits present security risks when dealing with supply chain attacks.

**A Quick Guide for macOS**

To set up GPG signing on macOS, follow these steps:

1.  Install the `gpg` command-line tools: `brew install gpg`
2.  Configure your code editor to use your email address as the GPG key repository
3.  Set your GitHub repository's GPG settings

**Additional Tools for Windows Users**

For users on Windows, you can use:

*   GPG4win: A standalone GUI tool for managing GPG keys and encrypting data in windows
    *   Install it via the Microsoft Store or Chocolatey.
*   Git with a proper installation of gpg command-line tools

**Final Step: Sign Your Commits**

To sign your commits, follow these steps:

1.  Log into GitHub using SSH (Secure Shell)
2.  Navigate to your repository settings.
3.  Update your `git config` entry for adding the relevant key.
4.  Push your updated commit with GPG added.

By following this guide and configuring your Git workflow correctly, you'll increase an organization's security by securely signing commits.
