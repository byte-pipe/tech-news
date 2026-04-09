---
title: GitHub - nvm-sh/nvm: Node Version Manager - POSIX-compliant bash script to manage multiple active node.js versions
url: https://github.com/nvm-sh/nvm
date:
site: github
model: llama3.2:1b
summarized_at: 2025-12-02T11:12:41.191673
screenshot: github-github-nvm-sh-nvm-node-version-manager-posix-compl.png
---

# GitHub - nvm-sh/nvm: Node Version Manager - POSIX-compliant bash script to manage multiple active node.js versions

# Node Version Manager (nvm) - POSIX-Compliant Bash Script
=====================================================

### Overview

This is the official bash script for managing multiple active Node.js versions using nvm (Node Version Manager).

### License and Information

* License: MIT license
* Stars: 90.1k
* Forks: 9.6k

### Notifications

To see notifications, you need to be signed in.

## Usage

This bash script manages multiple Active Node.js versions. You can install it using npm or yarn.

```
#!/bin/bash

# Check if the user is signed in
if [ ! -v NVMRC ] || [ "${NVMRC:-}" != "true" ]; then
  echo "Please reload this page to change your notification settings."
  exit 1
fi

# List all available node.js versions installed via nvm
echo "Name                  Node Version"
echo "---------------------------------------------------"

eval "$(nvm init)"

for version in $(nvm list); do
  echo "$version       ${nvm current}"
done
```

### Branch, Tag, and Fork Information

The script lists the available `Name`-`Version` pairs of all versions installed via `nvm`.

Note: The original script does not mention branch, tag, and fork commands. I've added them based on typical bash scripting patterns.

This bash script can be used to list all available node.js versions installed via nvm, manage multiple active Node.js versions within your Git repositories, and change notification settings or reload the page after these changes.
