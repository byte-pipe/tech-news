---
title: '[Gluon][Tutorial] Persistent attention by Mogball · Pull Request #7298 · triton-lang/triton · GitHub'
url: https://github.com/triton-lang/triton/pull/7298
site_name: hackernews
fetched_at: '2025-10-03T19:09:00.043787'
original_url: https://github.com/triton-lang/triton/pull/7298
author: mmastrac
date: '2025-10-03'
description: Rewrite the attention kernel to be persistent. This gives better performance at low-contexts. However, fp16 at large context has suffered a bit due to a ptxas instruction scheduling issue in the so...
---

triton-lang



/

triton

Public

* NotificationsYou must be signed in to change notification settings
* Fork2.3k
* Star17.1k

# [Gluon][Tutorial] Persistent attention#7298


 New issue






Have a question about this project?Sign up for a free GitHub account to open an issue and contact its maintainers and the community.

 Sign up for GitHub

By clicking “Sign up for GitHub”, you agree to ourterms of serviceandprivacy statement. We’ll occasionally send you account related emails.

Already on GitHub?Sign into your account

Jump to bottom

 Merged

Mogball

 merged 93 commits into


main

from

mogball/persistent



Jul 9, 2025

 Merged

# [Gluon][Tutorial] Persistent attention#7298

Mogball

 merged 93 commits into


main

from

mogball/persistent



Jul 9, 2025

 +466


 −512


Add this suggestion to a batch that can be applied as a single commit.

This suggestion is invalid because no changes were made to the code.

Suggestions cannot be applied while the pull request is closed.

Suggestions cannot be applied while viewing a subset of changes.

Only one suggestion per line can be applied in a batch.

Add this suggestion to a batch that can be applied as a single commit.

Applying suggestions on deleted lines is not supported.

You must change the existing code in this line in order to create a valid suggestion.

Outdated suggestions cannot be applied.

This suggestion has been applied or marked resolved.

Suggestions cannot be applied from pending reviews.

Suggestions cannot be applied on multi-line comments.

Suggestions cannot be applied while the pull request is queued to merge.

Suggestion cannot be applied right now. Please check back later.
