---
title: Vinyl Cache has left github — Varnish HTTP Cache
url: https://vinyl-cache.org/organization/moving.html
site_name: lobsters
content_file: lobsters-vinyl-cache-has-left-github-varnish-http-cache
fetched_at: '2026-02-19T06:00:31.266260'
original_url: https://vinyl-cache.org/organization/moving.html
date: '2026-02-19'
tags: vcs
---

# Vinyl Cache has left github¶

## … what you need to do¶

If you are interested in continued collaboration with the Vinyl Cache project,
please register an account on our self hostedforgejoinstance followingthis link.

This invitation link expires 2026-03-20T00:22:08+01:00 and is good for up to 100
registrations.

When it becomes invalid, anyone who already has an account should be able to help out,
unless we still get abused by spammers and need to close registrations again.

If you have registered and do not receive the email confirmation, please check
your SPAM folder.

## About the new forge¶

Our forge is special in some ways. Read about it and/or report issues:
<https://code.vinyl-cache.org/vinyl-cache/code.vinyl-cache.org>

## Location mapping old/new¶

The translation rules from old to new URL are:

* the prefix changes fromhttps://github.com/varnishcache/tohttps://code.vinyl-cache.org/vinyl-cache/.
* in the project name,varnishis replaced withvinyl.

The main/trunk branch is going to bemain.

Or expressed as asedcommand:

sed

-
e

's:github.com/varnish:code.vinyl-cache.org/vinyl-:; s:varnish:vinyl:'

old

new

https://github.com/varnishcache/varnish-cache

https://code.vinyl-cache.org/vinyl-cache/vinyl-cache

https://github.com/varnishcache/homepage

https://code.vinyl-cache.org/vinyl-cache/homepage

https://github.com/varnishcache/pkg-varnish-cache

https://code.vinyl-cache.org/vinyl-cache/pkg-vinyl-cache

https://github.com/varnishcache/varnish-devicedetect

https://code.vinyl-cache.org/vinyl-cache/vinyl-devicedetect

https://github.com/varnishcache/libvmod-example

https://code.vinyl-cache.org/vinyl-cache/libvmod-example

https://github.com/varnishcache/fuzzdata

https://code.vinyl-cache.org/vinyl-cache/fuzzdata

https://github.com/varnishcache/vc-commit-event

https://code.vinyl-cache.org/vinyl-cache/vc-commit-event

https://github.com/varnishcache/pkg-debian

https://code.vinyl-cache.org/vinyl-cache/pkg-debian

https://github.com/varnishcache/varnish-release-rpm

https://code.vinyl-cache.org/vinyl-cache/vinyl-release-rpm

These are the web frontend URLs. The git clone URLs change accordingly,
optionally with.gitappended. Ssh access changes fromgit@github.com:___.gittogit@code.vinyl-cache.org/___.git(optionally
without.git) with paths substituted as per the table above. The main/trunk
branch changes tomain.

Note that some repositories have not been in use for some time. We will possibly
decide to then also archive them on our own forge.

## Changing your git settings¶

The followingbashscript automates changing the origin and main branch. Use
it from within a git-directory. If your “main origin” is not calledorigin,
adjust theorigin=originline accordingly:

#!/bin/bash

## call this from a varnish-cache git directory

set -eux
top=$(git rev-parse --show-toplevel)
cd "${top}"

# determine the new origin and use it
origin=origin
newurl=$(git remote get-url "${origin}" | sed -e 's:github.com\([\:/]\)varnishcache:code.vinyl-cache.org\1vinyl-cache:;s:varnish:vinyl:')
git remote set-url "${origin}" "${newurl}"
git fetch

# rename main to master
git checkout -b main master
git branch -u origin/main main
git branch -d master
if [[ "${top}" == *varnish* ]] ; then
 new="${top/varnish/vinyl}"
 mv "${top}" "${new}"
 echo NOW CALL: cd "${new}"
fi

## What is happening after the forge migration¶

Now that the important first step is done, we are very busy getting our tooling
back, which is mainlyvtestand other CI as
well as the automatic website update.

When the dust has settled, we will add mirrors, which will provide read only
access tocode only. They will get announced onhttps://vinyl-cache.org

## Mini-Retro: What we did¶

One by one, we migrated our repositories from github tohttps://code.vinyl-cache.org.

The following was done for each in turn:

* Alasttag was pushed for important repositories.
* A note will was added to the README to inform about the migration, new
repository location and, optionally,lasttag.
* If applicable, the central script/tool called for code builds was changed to
fail and point to the README. This was usuallyconfigureor a primarymaketarget.
* The github repository was set toarchived. This means that no changes to
the code, pull requests, issues, the wiki or whatever were possible from this
point on.
* The repository was migrated to the new location.
* Once the migration was complete and manual sanity checks looked OK, the
repository was opened at the new location.

### What went wrong¶

On one or two occasions, the README change was accidentally wrong, so we had to
un-archive, fix and archive github again.

For the migration to our most important repo
<https://code.vinyl-cache.org/vinyl-cache/vinyl-cache>, we did not consider that
renaming the master branch to main by pushing a new main branch and then
deleting the master branch would render all migrated pull requests with master
as the base invalid. Forgejo automatically closed them.

Thanks to the fantastic superpowers of self hosting, fixing this issue directly
on the SQL level was straight forward, so all accidentally closed pull requests
are available again, except for aminor detailwhich we
did not bother fixing.
