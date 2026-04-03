---
title: GitHub - nvm-sh/nvm: Node Version Manager - POSIX-compliant bash script to manage multiple active node.js versions
url: https://github.com/nvm-sh/nvm
date:
site: github
model: llama3.2:1b
summarized_at: 2025-11-01T11:16:06.925905
screenshot: github-github-nvm-sh-nvm-node-version-manager-posix-compl.png
---

# GitHub - nvm-sh/nvm: Node Version Manager - POSIX-compliant bash script to manage multiple active node.js versions

# Node Version Manager for Git - a POSIX-compliant bash script
==============================================

### Overview
----------

The `nvm-sh` is a Node.js version manager that enables multiple active node.js versions on the same machine. It provides tools for installing, upgrading, and managing different versions of node.js.

### Key Features
--------------

*   POSIX-compliant
*   Sign-in required to change notification settings
*   Forks: Node.js with commit history available as a GitHub repository

### Usage
-----

To use `nvm-sh`, you can follow these steps:

1.  Install the `nvm` package globally and create a configuration file named `.nvmrc`.
2.  Run `nvm install lts`. This will add a new `node-lts`. You can upgrade later by running `sudo nvm install <versionnumber>`.
3.  Navigate to a project directory: `cd project-directory`
4.  Initialize the shell with the current branch' commit history as a Git repository. Run `nvm use lts@latest --force` and authenticate.
5.  To use an older version of node.js (e.g., `node-lts 12.20.0`), run `nvm use node-lts`.

### Branches
---------

*   To manage different branches of the same repository, ensure that you are signed in as a fork on [GitHub](https://github.com/). The `--force` option is used to force re-cloning and re-authorization.

### Security Notice
--------------

Please be aware of the security considerations when managing multiple versions of node.js:

*   Never commit your current version or any part of it to source control. It's recommended to keep all Git repositories isolated.
*   Always verify signatures on each commit by checking timestamps and digital certificates in your Git repository settings.

### License
-------

The `nvm-sh` package is released under the MIT license.
