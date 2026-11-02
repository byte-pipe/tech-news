---
title: 13. BSD Unix, Part 3 - The Beginning of BSD Unix
url: https://fosscomics.com/posts/13.%20BSD%20Unix%20Part%203%20-%20The%20Beginning%20of%20BSD%20Unix/
date: 2026-11-02
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-11-03T06:08:41.482119
---

# 13. BSD Unix, Part 3 - The Beginning of BSD Unix

# 13. BSD Unix, Part 3 – The Beginning of BSD Unix

## Background
- In 1976 Ken Thompson returned to Bell Labs; Bill Joy and Chuck Haley began experimenting with the Unix kernel.
- Berkeley had a culture of sharing research software, influenced by the Free Speech Movement and anti‑war activism.

## First BSD (1BSD)
- Early 1977 Bill Joy assembled the Berkeley Software Distribution (BSD) by bundling a Pascal system with **ex**, a line editor derived from **em**.
- 1BSD was not a standalone OS; it was a collection of software to be installed on an existing Unix system.
- About 30 tapes were distributed in the following year; a separate AT&T Unix source license was required, but Berkeley charged only for tape and postage.

## Second BSD (2BSD)
- Joy improved the Pascal system, added **vi** (visual mode of ex), the C shell, and other tools, creating 2BSD.
- Roughly 75 tapes were shipped over the next year; Joy personally handled copying and mailing.
- The distribution emphasized kernel tuning and bug fixing.

## VAX Adoption and 3BSD
- In 1978 a VAX‑32 machine arrived at Berkeley, offering 32‑bit architecture and 1 MiB memory.
- Existing Bell Labs VAX Unix (32/V) lacked virtual‑memory support; graduate student Ozalp Babaoglu, advised by Domenico Ferrari, sought to add it for the Macsyma computer‑algebra system.
- Joy helped integrate and debug the virtual‑memory code; by January 1979 most bugs were resolved.
- Joy ported ex, vi, the C shell, etc., while Peter Kessler and Marshall Kirk McKusick ported the Pascal system.
- The combined package—virtual‑memory kernel, 2BSD tools, and 32/V utilities—became **3BSD**, shipped starting December 1979.

## Wider Impact
- ARPANET linked DARPA‑funded research institutions but suffered from heterogeneous hardware and OSes.
- DARPA recognized Unix’s portability and took note of Berkeley’s successful 3BSD distribution to research sites.

## References
- Marshall Kirk McKusick, *Twenty Years of Berkeley Unix* (1999)
- Andrew Leonard, “BSD Unix: Power to the people,” Salon (2000)
- SRI International, *ARPANET* (origins, 1969)
- Ozalp Babaoglu, biographical note on Unix virtual‑memory research
- The Unix Heritage Society (TUHS), 2BSD distribution archive
- Warren Toomey, “The Strange Birth and Long Life of Unix,” IEEE Spectrum (2011)