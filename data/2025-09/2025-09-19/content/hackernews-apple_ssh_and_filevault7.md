---
title: apple_ssh_and_filevault(7)
url: https://keith.github.io/xcode-man-pages/apple_ssh_and_filevault.7.html
site_name: hackernews
fetched_at: '2025-09-19T11:06:46.692284'
original_url: https://keith.github.io/xcode-man-pages/apple_ssh_and_filevault.7.html
author: ingve
date: '2025-09-19'
---

apple_ssh_and_filevault(7)

Miscellaneous Information Manual

apple_ssh_and_filevault(7)

# NAME

apple_ssh_and_filevault—SSH and FileVault

# DESCRIPTION

When FileVault is enabled, the data volume is locked and
 unavailable during and after booting, until an account has been
 authenticated using a password. The macOS version of OpenSSH stores all of
 its configuration files, both system-wide and per-account, in the data
 volume. Therefore, the usually configured authentication methods and shell
 access are not available during this time. However, when Remote Login is
 enabled, it is possible to perform password authentication using SSH even in
 this situation. This can be used to unlock the data volume remotely over the
 network. However, it does not immediately permit an SSH session. Instead,
 once the data volume has been unlocked using this method, macOS will
 disconnect SSH briefly while it completes mounting the data volume and
 starting the remaining services dependent on it. Thereafter, SSH (and other
 enabled services) are fully available.

# HISTORY

The capability to unlock the data volume over SSH appeared in
 macOS 26 Tahoe.

# SEE
 ALSO

sshd(8)

1 July, 2025

Darwin
