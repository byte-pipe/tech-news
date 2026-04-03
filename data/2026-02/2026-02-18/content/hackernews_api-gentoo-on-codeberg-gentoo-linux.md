---
title: Gentoo on Codeberg – Gentoo Linux
url: https://www.gentoo.org/news/2026/02/16/codeberg.html
site_name: hackernews_api
content_file: hackernews_api-gentoo-on-codeberg-gentoo-linux
fetched_at: '2026-02-18T11:19:47.266758'
original_url: https://www.gentoo.org/news/2026/02/16/codeberg.html
author: todsacerdoti
date: '2026-02-17'
description: Gentoo on Codeberg
tags:
- hackernews
- trending
---

# Gentoo on CodebergFeb 16, 2026

Gentoo now has a presence onCodeberg, and contributions can be submitted for the Gentoo
repository mirror athttps://codeberg.org/gentoo/gentooas an alternative to GitHub.
Eventually also other git repositories will become available under the Codeberg Gentoo organization.
This is part of the gradual mirror migration away from GitHub, as already mentioned in the2025 end-of-year review.
Codeberg is a site based onForgejo, maintained by a dedicatednon-profit organization,
and located in Berlin, Germany. Thanks to everyone who has helped make this move possible!

These mirrors are for convenience for contribution and we continue to host our own
repositories, just like we did while using GitHub mirrors for ease of
contribution too.

## Submitting pull requests

If you wish to submit pull requests on Codeberg, it is recommended to
use theAGit approachas it is more space efficient and does not
require you to maintain a fork of gentoo.git on your own Codeberg
profile. To set it up, clone the upstream URL and check out a branch
locally:

git clone git@git.gentoo.org:repo/gentoo.git
cd gentoo
git remote add codeberg ssh://git@codeberg.org/gentoo/gentoo
git checkout -b my-new-fixes

Once you’re ready to create your PR:

git push codeberg HEAD:refs/for/master -o topic="$title"

and the PR should be created automatically. To push additional
commits, repeat the above command - be sure that the same topic is
used. If you wish to force-push updates (because you’re amending
commits), add “-o force-push=true” to the above command.

More documentation can be foundon our wiki.
