---
title: dev.to's Dashboard Can't Count Its Own Posts - DEV Community
url: https://dev.to/dannwaneri/devtos-dashboard-cant-count-its-own-posts-3fci
site_name: devto
content_file: devto-devtos-dashboard-cant-count-its-own-posts-dev-comm
fetched_at: '2026-08-05T12:53:14.879204'
original_url: https://dev.to/dannwaneri/devtos-dashboard-cant-count-its-own-posts-3fci
author: Daniel Nwaneri
date: '2026-08-03'
description: 'This is a submission for DEV''s Summer Bug Smash: Clear the Lineup powered by Sentry. ... Tagged with bugsmash, devchallenge, ai.'
tags: '#bugsmash, #devchallenge, #ai'
---

Summer Bug Smash: Clear the Lineup 🐛🛹

This is a submission forDEV's Summer Bug Smash: Clear the Lineuppowered bySentry.

## Project Overview

forem is the open source platform behind dev.to itself. I've had it starred and cloned for months and never opened the codebase — it's Rails, and I don't write Ruby. Jess's post was the reason that finally changed.

github.com/forem/forem

## Bug Fix or Performance Improvement

#23687is a one-line report: a user published exactly one post, and the dashboard's "Posts" counter said 2.

Not writing Ruby meant I couldn't guess my way to the fix from vibes. I had to actually trace it — readingDashboardsController, the sidebar partials, and theArticlemodel until the shape of the bug was undeniable, not assumed.

The "Posts" badge in the dashboard sidebar renders@user.articles_count— acounter_culturecache onUserthat increments for everyArticlerow belonging to that user, full stop. No filter on type, no filter on state:

# app/models/article.rb

counter_culture
 
:user

Enter fullscreen mode

Exit fullscreen mode

But the link that badge sits on always opens the same default view:DashboardsController#showwith no params. That view only listsnon-archived, full-post-typearticles:

# app/controllers/dashboards_controller.rb

@articles
 
=
 
target
.
articles
.
from_subforem
.
includes
(
:organization
)

@articles
 
=
 
params
[
:state
]
 
==
 
"status"
 
?
 
@articles
.
statuses
 
:
 
@articles
.
full_posts

@show_archived
 
=
 
params
[
:filter
].
to_s
.
casecmp
(
"archived"
).
zero?

Enter fullscreen mode

Exit fullscreen mode

Forem has three article types —full_post,status(a short "Boost" update), andfullscreen_embed— and the counter doesn't distinguish between them, or between archived and active. The badge counts everything. The list under it shows a strict subset. Anyone who's ever posted a status update, or archived a post, sees a number that doesn't match what they can actually click into and see — exactly what got reported in #23687.

I couldn't verify that in Ruby, but I recognized the shape of it instantly once it was laid out: a cached count drifting from what a filtered view actually renders. I've shipped that exact bug in JavaScript. Same failure, different syntax.

## Code

github.com/forem/forem/pull/23690

The fix doesn't touch the sharedarticles_countcounter — that cache is read elsewhere for badges and spam heuristics, where "every article this user has ever made" is the correct meaning. Instead,DashboardsControllergets a helper scoped to match what the Posts tab actually renders, and both the full-page and AJAX sidebar actions use it instead of the raw cache:

# The "Posts" nav item always links to the default (non-archived, full posts

# only) view of the user's own dashboard, so its indicator should reflect

# that same scope rather than the user's raw articles_count, which also

# includes statuses and archived posts that never show up in that list.

def
 
posts_count_for
(
user
)

 
user
.
articles
.
from_subforem
.
full_posts
.
where
(
archived: 
false
).
count

end

Enter fullscreen mode

Exit fullscreen mode

## My Improvements

There was no way for me to eyeball this and trust it — I can't read Ruby well enough for that, and there's no Ruby or Postgres on the machine I was working from, so I couldn't run the spec suite locally either. Verification had to happen somewhere else: I wrote regression specs asserting a user with one full post, one status, and one archived post should see a count of exactly 1, pushed the branch, and let Forem's own CI be the judge instead of my own confidence.

CI caught something real on the first run — not in the fix, in my test.create(:article, type_of: "status")failed its own model validation, because status-type articles in Forem aren't allowed to have body markdown, and the factory's default does. I found the pattern already used elsewhere in the suite (body_markdown: "", main_image: nil), fixed the two specs, and pushed again.

That failure is the actual proof this wasn't guesswork dressed up as a fix. If I'd been able to run specs locally I might have caught it before pushing; instead the project's own CI did the job a local run would have.

Same lesson my other two entries kept landing on:The Cloudflare Worker That Ran Perfectly and Still Failed TwiceandI Was Filming a Demo of My Monitoring Tool. The Monitor Wasn't Monitoring.— "it compiled" and "it's correct" are different claims, and only one of them is worth trusting.

Everything's green now — 19 successful checks, 1 skipped, 0 failures, including the shard that runsdashboard_spec.rb. The PR is open against forem/forem and waiting on a maintainer review, since third-party fork PRs need one before merge. Not merged yet as of writing this — I'd rather say that plainly than imply otherwise.

Different from my other two entries in one way: I don't write Ruby. Claude found the bug and wrote the fix. I picked the issue and gated everything that left my machine — the fork, the push, the PR, the CLA. Full delegation on the code, not on whether it shipped.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (25 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse