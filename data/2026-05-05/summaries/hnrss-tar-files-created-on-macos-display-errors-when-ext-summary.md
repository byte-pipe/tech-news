---
title: Tar Files Created on macOS Display Errors When Extracting on Linux
url: https://aruljohn.com/blog/macos-created-tar-files-linux-errors/
date: 2026-04-30
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-05-05T00:54:11.481595
---

# Tar Files Created on macOS Display Errors When Extracting on Linux

# Tar Files Created on macOS Display Errors When Extracting on Linux

## Creating tar files
- Standard command used: `tar -cvzf pix.tar.gz pix`
- Produces a gzipped tar archive of the `pix` directory.

## SCP to Linux server
- Archive transferred with `scp pix.tar.gz user@myserver.tld:/tmp/`

## Extract or untar on Linux
- Extraction command: `tar -xzvf pix.tar.gz`
- Output shows files prefixed with `._` and warnings such as  
  `tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.quarantine'`

## Warnings and errors when extracting
- Common warnings involve unknown extended header keywords for Apple metadata and quarantine attributes.
- Appear when macOS‑created archives are unpacked on Linux.

## Why does it have those extra files?
- macOS’s default `bsdtar` includes extended attributes and creates “AppleDouble” files (`._filename`) to store them.
- Linux `tar` does not understand these extended headers, leading to warnings.

## Solution 1: Use `--no-xattrs` when creating the tar
- Command: `tar -cvzf --no-xattrs pix.tar.gz pix`
- Prevents inclusion of extended attributes, eliminating extra files and warnings.

## Solution 2: Use `--disable-copyfile` when creating the tar
- Command: `tar -cvzf --disable-copyfile pix.tar.gz pix`
- Also suppresses creation of AppleDouble files.

## Solution 3: Install and use GNU tar instead of BSD tar
- Verify current tar: `tar --version` (shows bsdtar).
- Install GNU tar via Homebrew: `brew install gnu-tar`.
- Add GNU tar to PATH (Intel macOS):  
  `export PATH="/usr/local/opt/gnu-tar/libexec/gnubin:$PATH"`
- Add GNU tar to PATH (Apple Silicon):  
  `export PATH="/opt/homebrew/opt/gnu-tar/libexec/gnubin:$PATH"`
- After updating PATH, `tar --version` should show GNU tar.
- Create archives with the usual command; GNU tar does not add the problematic metadata.

## Conclusion
- macOS’s default tar adds Apple-specific extended attributes that cause warnings on Linux.
- Using `--no-xattrs` or `--disable-copyfile` removes the extra files.
- Switching to GNU tar provides a permanent fix without needing extra flags.