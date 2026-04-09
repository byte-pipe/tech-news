---
title: GitHub - nvm-sh/nvm: Node Version Manager - POSIX-compliant bash script to manage multiple active node.js versions
url: https://github.com/nvm-sh/nvm
date:
site: github
model: llama3.2:1b
summarized_at: 2025-10-16T11:14:43.562125
screenshot: github-github-nvm-sh-nvm-node-version-manager-posix-compl.png
---

# GitHub - nvm-sh/nvm: Node Version Manager - POSIX-compliant bash script to manage multiple active node.js versions

# Node Version Manager (nvm) - POSIX-compliant Bash Script
====================================================


Overview
--------

The `nvm-sh` project is a Node.js version manager that allows you to manage multiple active versions of your chosen JavaScript package. It provides a secure, easy-to-use way to manage different versions of popular Node.js packages.


Features
--------

### Key Features

*   **POSIX-compliant Bash script**: A modern and powerful scripting language for managing Node.js versions.
*   **User-friendly interface**: Users can easily view and manage their installed Node.js versions using a simple command-line interface (CLI).
*   **Secure authentication**: Required users to be signed in before making changes to their Node.js version manager settings.


License
--------

The `nvm-sh` project is released under the MIT license, allowing users to freely operate and share code for its use without any restrictions or charges.


History
------

### v1.12.0

The current major release of `nvm-sh` was made in 2022 with the version number `v1.12.0`. This release marks a significant improvement in performance and stability compared to previous versions.


Usage
-----

To get started, users must first install the `nvm-sh` package globally using npm by running the command:

```bash
npm install -g nvm-sh
```
Once installed, the user can then execute the following command to launch their Node.js version manager on a new terminal session. The CLI will guide them through the process of selecting an available Node.js version and making it active.


Example Use Cases
----------------


### Example 1

```bash
nvm sh --user npm install 8> /dev/null # Uninstall all versions except 8
```

This command demonstrates how to uninstall all previous versions of a package named `npm` (Node Package Manager) that is greater than the currently active version of 8.

### Example 2

```bash
nvm sh -s --user yarn install npm> /dev/null # Install and upgrade npm for version 7
```

This command uses the `nvm-sh` CLI to uninstall all previous versions of the `npm`, then updates it to a minimum of 7.0.


Conclusion
----------

In conclusion, `nvm-sh` is a powerful tool that simplifies the management of multiple active Node.js versions for developers and organizations alike. With its POSIX-compliant Bash script, user-friendly interface, and secure authentication process, `nvm-sh` is an essential package in modern JavaScript development workflows.
