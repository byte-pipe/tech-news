---
title: Firefox 147 Will Support The XDG Base Directory Specification - Phoronix
url: https://www.phoronix.com/news/Firefox-147-XDG-Base-Directory
site_name: hackernews
fetched_at: '2025-11-20T19:07:31.352781'
original_url: https://www.phoronix.com/news/Firefox-147-XDG-Base-Directory
author: bradrn
date: '2025-11-20'
---

# Firefox 147 Will Support The XDG Base Directory Specification

Written by
Michael Larabel
 in
Mozilla
 on 20 November 2025 at 08:19 AM EST.
19 Comments

A 21 year old bug report requesting support of the XDG Base Directory specification is finally being addressed by Firefox. The Firefox 147 release should respect this XDG specification around where files should be positioned within Linux users' home directory.

The XDG Base Directory
specification
 lays out where application data files, configuration files, cached assets, and other files and file formats should be positioned within a user's home directory and the XDG environment variables for accessing those locations. To date Firefox has just positioned all files under
~/.mozilla
 rather than the likes of
~/.config
 and
~/.local/share
.

Back in September 2004
this bug report
 was opened to support the FreeDesktop.org XDG Base Directory specification.

Merged this morning was the
support
 for this specification and associated commits.

In turn this long-open bug is now closed and Firefox 147 should be the version to finally support the XDG Base Directory specification for jiving more nicely with other Linux apps.
