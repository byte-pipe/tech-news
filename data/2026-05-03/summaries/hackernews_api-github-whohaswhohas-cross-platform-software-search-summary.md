---
title: GitHub - whohas/whohas: Cross-platform software search · GitHub
url: https://github.com/whohas/whohas
date: 2026-05-02
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-05-03T06:01:29.297318
---

# GitHub - whohas/whohas: Cross-platform software search · GitHub

# whohas – Cross‑platform Package Search Tool

## Overview
- **whohas** is a Perl command‑line utility that queries multiple Linux/Unix package repositories simultaneously.  
- Designed for package maintainers to locate ebuilds, PKGBUILDs, etc., but also useful for regular users.

## Supported Distributions
- Arch, Debian, Fedora, Gentoo, Mageia, Mandriva, openSUSE, Slackware, Source Mage, Ubuntu  
- BSD families: FreeBSD, NetBSD, OpenBSD  
- macOS ports: Fink, MacPorts, Cygwin  

## Primary Use Cases
- Identify which distributions provide a specific application or library.  
- Retrieve version information for a package across distributions (currently implemented for Debian).  
- Obtain URLs linking to detailed package pages.

## Typical Workflow
1. Run `whohas <package>` to list matching packages across all supported repos.  
2. Pipe output through `grep` to refine results, e.g.:  
   - `whohas gimp | grep "gimp "` – exact package name.  
   - `whohas gimp | grep -i arch` – only Arch Linux entries.  
   - `whohas arch | grep "^Arch"` – results for the term “arch” limited to Arch Linux.  

## Example Output (searching for “gaim”)
- Shows entries per distribution with columns: distribution, package name, version, release/date, repository status, and URL.  
- Sample lines:  
  - `Arch gaim 1.4.0-1 10-07-2005 Current http://www.archlinux.org/packages.php?id=4226`  
  - `Debian gaim 1 stable http://packages.debian.org/stable/net/gaim`  
  - `Gentoo gaim-encryption 2.38 12-07-2005 http://packages.gentoo.org/ebuilds/?gaim-encryption-2.38`  

## Additional Information
- The tool works best in terminals that support clickable hyperlinks.  
- Full documentation and project page: http://www.philippwesche.org/200811/whohas/intro.html  
- Repository includes source files, installation instructions, license, and changelog.