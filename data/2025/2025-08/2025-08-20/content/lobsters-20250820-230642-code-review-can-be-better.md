---
title: Code Review Can Be Better
url: https://tigerbeetle.com/blog/2025-08-04-code-review-can-be-better/
site_name: lobsters
fetched_at: '2025-08-20T23:06:42.532086'
original_url: https://tigerbeetle.com/blog/2025-08-04-code-review-can-be-better/
author: matklad
date: '2025-08-20'
description: Insights, updates, and technical deep dives on building a high-performance financial transactions database.
tags: practices, vcs
---

# Code Review Can Be Better

Aug 4, 2025

matklad

Slightly unusual genre today: anegative
resultabout ourgit-reviewtool for a different take on code review process, which we decided to
shelve, at least for the time being.

A lot of people are unsatisfied with GitHub’s code review process.
One of the primary issues is that GitHub poorly supports stacked pull
requests andinterdiff
reviews. While I also see interdiff as valuable, it’s not the reason
why I decided to experiment withgit-review. I have two
other problems with GitHub, and with every single other code review
system, with the exception ofthe
thing that Jane Street uses internally:

* review state is not stored as a part of repository itself,
* review is done via remote-first web-interface.

## Optimal Workflow

Let’s start with the second one.

By the way of analogy, I don’t use GitHub’s web editor to write code.
I clone a repository locally, and work in my editor, which is:

* fully local, memory/nvme latencies, no HTTP round-trips,
* tailored to my specific odd workflow.

When I review code, I like to pull the source branch locally. Then I
soft-reset the code to mere base, so that the code looks as if it was
written by me. Then I fire up magit, which allows me to effectively
navigate both through the diff, and through the actual code. And I even
use git staging area to mark files I’ve already reviewed:

Reviewingcoderather than diff is so powerful: I can run
the tests, I can go to definition to get the context, I can try out my
refactoring suggestions in-place, with code completion and the other
affordances of my highly sophisticated code editor.

Alas, when I want to actually leave feedback on the PR, I have to
open the browser, navigate to the relevant line in the diff, and (after
waiting for several HTTP round-trips) type my suggestion into a text
area. For some reason, the text area also regularly lags for me,
especially on larger diffs.

Two things are wrong here. On the interface side, review feedback is
text related to the code. The most natural interface is to just leave
review comments as inline comments in the code, or even to fix the code
directly:

// CR(matklad): Hm, this check seems imprecise to me.

// Shouldn't we compare `replica.view` instead of `header.view` here?

if
 (header
.
view
!=
 view)
return
;

And on the implementation side, because the data is stored in a
remote database, rather than in a local git repository, we get all those
latency-inducing round-trips (not to mention vendor lock in).

Thus,git-reviewwas born. The idea is simple:

* Code review is a single commit which sits on top of the PR
branch.
* That commit adds a bunch of code comments with specific
markers.
* Review process involves both the author and the reviewer modifying
this top commit (so, there’s a fair amount ofgit push --force-with-leaseinvolved).
* The review concludes when all threads were marked as//? resolvedand an explicit revert commit is added on top
(such that review is preserved in the history).

## The Devil in The Detail

It didn’t exactly fail, but wasn’t a spectacular success. When it
comes to writing tools, I am a huge fan of getting-rich-quick schemes,
of writing 500 lines ofhacky,
use-case specific codewhich works better forthatuse-case
thansomething serious. A
simple script for convertingyour.mdto.htmlcan
be cheaper to maintainthan a general purpose solution.

I had a hope that “code review is just a commit” would be the secret
to keep implementation complexity low. Sadly, the devil is in the
details in this particular case.

The basic idea, that reviewing is leaving comments in code, works as
well as I had expected (that is, it’s really, really awesome). But
modifying code under review turned out to be tricky. If a reviewer
requests a change, and you apply it to some deep commit, or even add a
new commit on top, you now have to solve mere conflicts with the review
comments themselves, as they are often added at thehunkboundaries. And then, while--force-with-leaseis workable,
it also adds friction. There is an impedance mismatch here, where, for
code, we want very strong, hash-chained intentional sequence of
state-transitions, while for review we would be more happy with more lax
conflict-free merging rules. Itmightbe solved with more
tooling to “push” and “pop” review comments on top of pristine review
branch, but that seems to push well beyond my 500 line limit.

Then, there’s a second change. It seems likeupstream
git might be getting a Gerrit-style Change-Idfor tracking revisions
of a single commit over rebases. If that happens, we might actually get
first class support for per-commit interdiff review! But that would be
somewhat incompatible withgit-reviewapproach, which adds
an entire separate commit to the branch. But, perhaps, in theChange-Idworld, we could be adding review comments to the
commits themselves, and, rather that adding a revert at the conclusion
of review, instruct git to store all revisions of a particularChange-Id.

Anyway, we are begrudgingly back to web-interface based code reviews
for now. Hopefully someone is inspired enough to fix this properly one
day!

If you’ve been thinking along similar lines, the following links are
worth checking out:

* Fossilis an SCM system which stores everything in the repository.
* NoteDbbackend for Gerrit. Gerrit started with tracking review state in a
separate database, but then moved storage into git.
* git-buguses git to
store information about issues.
* git-appraiseuses git to store information about reviews.
* prrwhich
implements in-editor review interface on top of GitHub’s Web API
* How
Jane Street Does Code Reviewshows that a better world is possible,
and that it is already here, just not everywhere.

Enjoyed this post?Add our RSS feed.
