---
title: 'Ingo Blechschmidt: "So. For the past few days I''ve been deep in a fun…" - Mathstodon'
url: https://mathstodon.xyz/@iblech/116769502749142438
site_name: hnrss
content_file: hnrss-ingo-blechschmidt-so-for-the-past-few-days-ive-bee
fetched_at: '2026-07-03T11:50:08.066602'
original_url: https://mathstodon.xyz/@iblech/116769502749142438
date: '2026-07-02'
description: 'So. For the past few days I''ve been deep in a fun and very rewarding, but also extremely scary debugging saga. To cut a long git-bisecting story short: Since Linux 6.9 (May 2024), the tool that locks the laptop''s drive on suspend had been silently failing. Like many of my friends, I use full-disk encryption (LUKS) to protect my data if my laptop is lost, seized or stolen. Highly recommended to everyone; in combination with tested and automated backups, it contributes greatly to peace of mind. (Under Windows, the canonical software to do that is VeraCrypt.) Except that, for more than two years, the encryption key remained resident in memory across suspend, leaving it there for the taking by anyone who seized the still-powered laptop. (It still worked on a full shutdown, but a full shutdown is rare these days.) There is something uniquely unsettling about trusting a security mechanism for years and learning it was never doing the thing. "A technical argument by a trusted author,
  which is hard to check and looks similar to arguments known to be correct, is hardly ever checked in detail." The same, it seems, is true for computer code. The culprit was a sensible and useful refactoring, https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=a28d893eb3270cf62c10dd8777af0d8452cdc072. But it had an unexpected long-range interaction with the encryption code. The fix is exactly one line long: https://lore.kernel.org/all/ajKwRtP8izwRsMmv@quasitopos/ And no, without formal proofs I cannot say whether my patch is correct and free of its own long-range interactions... At the very least, we now have an automated test to detect future regressions (https://github.com/NixOS/nixpkgs/pull/532499) and a patch to emit a warning instead of failing silently (https://gitlab.com/cryptsetup/cryptsetup/-/merge_requests/936).'
tags:
- hackernews
- hnrss
---

To use the Mastodon web application, please enable JavaScript. Alternatively, try one of the 
native apps
 for Mastodon for your platform.