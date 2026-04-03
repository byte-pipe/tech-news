---
title: 'You already have a git server: (Maurycy''s blog)'
url: https://maurycyz.com/misc/easy_git/
site_name: hackernews
fetched_at: '2025-10-26T19:12:06.187715'
original_url: https://maurycyz.com/misc/easy_git/
author: chmaynard
date: '2025-10-26'
---

# You already have a git server:

Oct 24, 2025

(
Programming
)

If you have a git repository on a server with ssh access, you can just clone it:

# This works.

git clone ssh://username@hostname/path/to/repo

You can then work on it locally and push your changes back to the origin server.
By default, git won’t let you push to the branch that is currently checked out, but this is easy to change:

# Run this on the remote server.

git config receive.denyCurrentBranch updateInstead

This is a great way to sync code between multiple computers or to work on server-side files without laggy typing or manual copying.
If you want to publish your code, just point your web server at the git repo:

git clone https://hostname/path/to/repo/.git

# You can get rid of the .git part of the command by either setting the

# server to remap it to a nicer URL or by just renaming the .git directory

# (although this stops you from running git server side)

… although you will have to run this command server-side to make it cloneable:

# Create some files used by git-over-http:

# Should be repeated after making changes.

git update-server-info

That’s a lot of work, so let’s set up a hook to do that automatically:

# Automatically run git update-server-info.

# Should be run server-side

cp .git/hooks/post-update.sample .git/hooks/post-update

chmod a+x .git/hooks/post-update

Git hooks are just shell scripts, so they can do things like running a static site generator:

cat > .git/hooks/post-update
<<EOF

#!/bin/sh

set -euo pipefail

cd /path/to/site

/path/to/generator

EOF

chmod a+x .git/hooks/post-update

This is how I’ve been doing this blog for a while now:
It’s very nice to be able to type up posts locally (no network lag), and then push them to the server and have the rest handled automatically.

It’s also backed up by default:
If the server breaks, I’ve still got the copy on my laptop, and if my laptop breaks, I can download everything from the server.
Git’s version tracking also prevents accidental deletions, and if something breaks, it’s easy to figure out what caused it.
