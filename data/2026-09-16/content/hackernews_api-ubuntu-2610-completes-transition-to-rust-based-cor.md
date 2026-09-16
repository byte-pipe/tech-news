---
title: Ubuntu 26.10 completes transition to Rust-based coreutils - OMG! Ubuntu
url: https://www.omgubuntu.co.uk/2026/09/ubuntu-2610-rust-coreutils-complete
site_name: hackernews_api
content_file: hackernews_api-ubuntu-2610-completes-transition-to-rust-based-cor
fetched_at: '2026-09-16T10:38:11.459445'
original_url: https://www.omgubuntu.co.uk/2026/09/ubuntu-2610-rust-coreutils-complete
author: Joey Sneddon
date: '2026-09-14'
published_date: '2026-09-13T16:39:11+00:00'
description: Ubuntu 26.10 completes the distro's move to Rust-based core utilities, with the commands previously held back due to security issues now migrated to
tags:
- hackernews
- trending
---

Ubuntu 26.10 completes the distro’s move to Rust-based core utilities, with the commands previously held back due to security issues now migrated to memory-safe versions.

cp,mvandrmwere held back on their GNU versions in Ubuntu 26.04 LTS due to a crop of TOCTOU (time-of-check to time-of-use) issues that needed to be fixed in theuutilsversions.

With those issues resolved upstream, Ubuntu 26.10 finishes the job. The‘Stonking Stingray’ships a full set of Rust core utilities, which encompasses common command-line tools likels,cat,chmodanddu.

Canonical donates €40k a year to help fund work on Rust software

Canonical’s engineers began ‘oxidising’ the distro – replacing foundational software with Rust alternatives – in 2025. Itsees security benefitsin doing so, since Rust catches memory bugs at compile time, whereas C compilers don’t.

Ubuntu 25.10 was the first release to ship with Rust-based utilities and madeRust-based sudo the default.

Migratinghasn’t been without hiccups, but Canonical has been studious.

Itcommissioned a security auditofuutilsahead of 26.04, which found the issues that kept the three commands back on their GNU versions. It’s also a gold sponsor of theTrifecta Tech Foundation, giving €40,000 a year to fund its work on Rust software.

The non-profit foundation is undertaking a Rust-basedrewrite of the Network Time Protocol (NTP), and Ubuntu plans to use it as the default time sync client by 27.10.

Here, the completion of the coreutils migration offers no functional difference to end users. The Rust-baseduutilsaims for drop-in compatibility with GNU versions, and treats any deviances as a bug. That’s by designed; the point is one of improved security.

Ubuntu 26.10 ‘Stonking Stingray’ beta arrives later this month, before the stable release on 15 October, 2026.

 coreutils 

 rust 

 Ubuntu 26.10