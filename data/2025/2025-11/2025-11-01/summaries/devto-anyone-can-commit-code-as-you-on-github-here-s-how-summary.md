---
title: "Anyone Can Commit Code as You on GitHub (Here's How to Stop Them) - DEV Community"
url: https://dev.to/nickytonline/anyone-can-commit-code-as-you-on-github-heres-how-to-stop-them-2in7
date: 2025-10-26
site: devto
model: llama3.2:1b
summarized_at: 2025-11-01T11:45:47.385825
screenshot: devto-anyone-can-commit-code-as-you-on-github-here-s-how.png
---

# Anyone Can Commit Code as You on GitHub (Here's How to Stop Them) - DEV Community

**Signing On GitHub with Git Commit Signing using GPG**

**What is GPG?**
GPG (GNU Privacy Guard) is an open-source implementation of the OpenPGP standard for encrypting and signing data. It's used to prove that you, and only you, made a commit on a Git repository.

**Why Sign Your Commits?**

1.  **Prevent Real-World Impersonation**: Commit impersonation isn't just theoretical; it can actually happen in real-world scenarios like open source contributions, work environments, and supply chain attacks.
2.  **Audit Trails**: Being able to cryptographically prove who committed what code is critical for compliance and regulatory industries.
3.  **Security**: Signed commits are essential for security tools to verify whether a repository has been compromised.

**Does Anyone Care?**
While it's not mandatory, most developers don't check the verification badges on every commit, but organizations that require signed commits through branch protection rules need them. Additionally, regulated industries use signed commits to ensure code is legitimate throughout supply chain audits.

**Why This Matters**
Signing your Git commits using GPG provides a secure way to prove you're the developer who made changes to a repository's codebase.

**Getting Started**

1.  **Install GPG Tools**: On macOS, follow the installation steps provided.
2.  **Configure GPG**: Set up your GPG key management for Git repositories on any platform.
3.  **Push Signed Commits**: Ensure your commits are signed before pushing them to GitHub.

For more information and detailed instructions, refer to the official OpenPGP specification or try the included tools (`git config --global user.name <account-name>` and `git config --global user.email <account-email>`) on Linux or Windows.
