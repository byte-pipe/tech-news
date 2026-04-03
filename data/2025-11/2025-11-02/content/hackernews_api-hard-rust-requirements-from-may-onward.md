---
title: Hard Rust requirements from May onward
url: https://lists.debian.org/debian-devel/2025/10/msg00285.html
site_name: hackernews_api
fetched_at: '2025-11-02T11:08:16.436734'
original_url: https://lists.debian.org/debian-devel/2025/10/msg00285.html
author: rkta
date: '2025-11-01'
description: Hard Rust requirements from May onward
tags:
- hackernews
- trending
---

[
Date Prev
][
Date Next
]
[
Thread Prev
][
Thread Next
]
[
Date Index
]
[
Thread Index
]

# Hard Rust requirements from May onward

* To:debian-devel@lists.debian.org
* Cc:deity@lists.debian.org,debian-68k@lists.debian.org,debian-hppa@lists.debian.org,debian-superh@lists.debian.org,debian-alpha@lists.debian.org
* Subject: Hard Rust requirements from May onward
* From: Julian Andres Klode <jak@debian.org>
* Date: Fri, 31 Oct 2025 21:48:46 +0100
* Message-id: <[🔎]20251031213541.GA73786@debian.org>
* Mail-followup-to:debian-devel@lists.debian.org,deity@lists.debian.org,debian-68k@lists.debian.org,debian-hppa@lists.debian.org,debian-superh@lists.debian.org,debian-alpha@lists.debian.org

Hi all,

I plan to introduce hard Rust dependencies and Rust code into
APT, no earlier than May 2026. This extends at first to the
Rust compiler and standard library, and the Sequoia ecosystem.

In particular, our code to parse .deb, .ar, .tar, and the
HTTP signature verification code would strongly benefit
from memory safe languages and a stronger approach to
unit testing.

If you maintain a port without a working Rust toolchain,
please ensure it has one within the next 6 months, or
sunset the port.

It's important for the project as whole to be able to
move forward and rely on modern tools and technologies
and not be held back by trying to shoehorn modern software
on retro computing devices.

Thank you for your understanding.
--
debian developer - deb.li/jak | jak-linux.org - free software dev
ubuntu core developer i speak de, en

Attachment:signature.ascDescription:PGP signature

Reply to:

* debian-devel@lists.debian.org
* Julian Andres Klode (on-list)
* Julian Andres Klode (off-list)

* Follow-Ups:Re: Hard Rust requirements from May onwardFrom:John Paul Adrian Glaubitz <glaubitz@physik.fu-berlin.de>
* Re: Hard Rust requirements from May onwardFrom:John Paul Adrian Glaubitz <glaubitz@physik.fu-berlin.de>
* From:John Paul Adrian Glaubitz <glaubitz@physik.fu-berlin.de>

* Prev by Date:Bug#1119816: ITP: python-fairscale -- PyTorch extension library for high performance machine learning
* Next by Date:Re: Hard Rust requirements from May onward
* Previous by thread:Bug#1119816: ITP: python-fairscale -- PyTorch extension library for high performance machine learning
* Next by thread:Re: Hard Rust requirements from May onward
* Index(es):DateThread
* Date
* Thread
