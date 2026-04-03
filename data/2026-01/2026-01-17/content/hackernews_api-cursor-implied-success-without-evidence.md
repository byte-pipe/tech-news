---
title: Cursor Implied Success Without Evidence
url: https://embedding-shapes.github.io/cursor-implied-success-without-evidence/
site_name: hackernews_api
fetched_at: '2026-01-17T11:06:33.263285'
original_url: https://embedding-shapes.github.io/cursor-implied-success-without-evidence/
author: embedding-shape
date: '2026-01-16'
description: Cursor's latest “browser experiment” implied success without evidence
tags:
- hackernews
- trending
---

2026-01-16

# Cursor's
latest "browser experiment" implied success without evidence

On January 14th 2026, Cursor published a blog post titled "Scaling
long-running autonomous coding" (https://cursor.com/blog/scaling-agents)

In the blog post, they talk about their experiments with running
"coding agents autonomously for weeks" with the explicit goal of

understand[ing] how far we can push the frontier of agentic coding
for projects that typically take human teams months to complete

They talk about some approaches they tried, why they think those
failed, and how to address the difficulties.

Finally they arrived at a point where something "solved most of our
coordination problems and let us scale to very large projects without
any single agent", which then led to this:

To test this system, we pointed it at an ambitious goal: building a
web browser from scratch. The agents ran for close to a week, writing
over 1 million lines of code across 1,000 files. You can explore the
source code on GitHub (https://github.com/wilsonzlin/fastrender)

This is where things get a bit murky and unclear. They claim "Despite
the codebase size, new agents can still understand it and make
meaningful progress" and "Hundreds of workers run concurrently, pushing
to the same branch with minimal conflicts", but they never actually say
if this is successful or not, is it actually working? Can you run this
browser yourself? We don't know and they never say explicitly.

After this, they embed the following video:

Video

And below it, they say "While it might seem like a simple screenshot,
building a browser from scratch is extremely difficult.".

### They
never actually claim this browser is working and functional

error: could not compile 'fastrender' (lib) due to 34 previous
errors; 94 warnings emitted

And if you try to compile it yourself, you'll see that it's very far
away from being a functional browser at all, and seemingly, it never
actually was able to build.

Multiple recent GitHub Actions runs onmainshow
failures (including workflow-file errors), and independent build
attempts report dozens of compiler errors, recent PRs were all merged
with failing CI, and going back in the Git history from most recent
commit back 100 commits,I
couldn't find a single commit that compiled cleanly.

I'm not sure what the "agents" they unleashed on this codebase
actually did, but they seemingly never ran "cargo build" or even less
"cargo check", because both of those commands surface 10s of errors
(which surely would balloon should we solve them) and about 100
warnings. There is an open GitHub issue in their repository about this
right now:https://github.com/wilsonzlin/fastrender/issues/98

And diving into the codebase, if the compilation errors didn't make
that clear already, makes it very clear to any software developer that
none of this is actually engineered code. It is what is typically known
as "AI slop", low qualitysomethingthat surely representssomething, but it doesn't have intention behind it, and it
doesn't even compile at this point.

They later start to talk about what's next, but not a single word
about how to run it, what to expect, how it's working or anything else.
Cursor's blog post provides no reproducible demo and no known-good
revision (tag/release/commit) to verify the screenshots, beyond linking
the repo.

Regardless of intent, Cursor's blog post creates the impression of a
functioning prototype while leaving out the basic reproducibility
markers one would expect from such claim. They never explicitly claim
it's actually working, so no one can say they lied at least.

They finish off the article saying:

But the core question, can we scale autonomous coding by throwing
more agents at a problem, has a more optimistic answer than we
expected.

Which seems like a really strange conclusion to arrive at, when all
they've proved so far, is that agents can output millions of tokens and
still not end up with something that actually works.

A "browser experiment" doesn't need to rival Chrome. A reasonable
minimum bar is: it compiles on a supported toolchain and can render a
trivial HTML file. Cursor's post doesn’t demonstrate that bar, and
current public build attempts fail at this too.

## Conclusion

Cursor never says "this browser is production-ready", but they do
frame it as "building a web browser from scratch" and "meaningful
progress" and then use a screenshot and "extremely difficult" language,
wanting to give the impression that this experiment actually was a
success.

The closest they get to implying that this was a success, is this
part:

Hundreds of agents can work together on a single codebase for weeks,
making real progress on ambitious projects.

But this extraordinary claim isn't backed up by any evidence. In the
blog post they never provide a working commit, build instructions or
even a demo that can be reproduced.

I don't think anyone expects this browser to be the next Chrome, but
I do think that if you claim you've built a browser, it should at least
be able to demonstrate being able to be compiled + loading a basic HTML
file at the very least.

Versions

2026-01-16
db6064b
 Add link to tested commits

@@ -33 +33 @@ And if you try to compile it yourself, you'll see that it's very far away from b

 Multiple recent GitHub Actions runs on `main` show failures (including workflow-file errors), and independent build attempts report dozens of compiler errors, recent PRs were all merged with failing CI, and going back in the Git history from most recent commit back

-about

 100

-commits, I

+commits,<br/>[I

 couldn't find a single commit that compiled

-cleanly.

+cleanly](https://gist.github.com/embedding-shapes/f5d096dd10be44ff82b6e5ccdaf00b29).

2026-01-16
3dcd6e7
 Fix linebreak typo

@@ -9,3 +9 @@ On January 14th 2026, Cursor published a blog post titled "Scaling long-running

-In the blog post, they talk about their experiments with running "coding agents autonomously for weeks"

-

-with the explicit goal of

+In the blog post, they talk about their experiments with running "coding agents autonomously for weeks" with the explicit goal of

2026-01-16
c74ab74
 Fix favicon, fix typos, made better simply

@@ -33 +33,3 @@ And below it, they say "While it might seem like a simple screenshot, building a

 And if you try to compile it yourself, you'll see that it's very far away from being a functional browser at all, and seemingly, it never actually was able to build.

 Multiple recent GitHub Actions runs on `main` show failures (including workflow-file errors), and independent build attempts report dozens of compiler errors, recent PRs were all merged with failing CI, and going back in the Git history from most recent

-commit,

+commit back about 100 commits,

 I couldn't find a single commit that compiled cleanly.

@@ -37 +39 @@ I'm not sure what the "agents" they unleashed on this codebase actually did, but

 And diving into the codebase, if the compilation errors didn't make that

-sure,

+clear already,

 makes it very clear to any software developer that none of this is actually engineered code. It is what is typically known as "AI slop", low quality *something* that surely represents *something*, but it doesn't have intention behind it, and it doesn't even compile at this point.

@@ -59 +61 @@ The closest they get to implying that this was a success, is this part:

 But this extraordinary claim isn't backed up by any evidence. In the blog post they never provide a working commit, build instructions or even a demo that can

+be

 reproduced.

2026-01-16
bafc54f
 Favicon + changes + cursor video

@@ -21 +21 @@ Finally they arrived at a point where something "solved most of our coordination

 This is where things get a bit murky and unclear. They claim "Despite the codebase size, new agents can still understand it and make meaningful progress" and "Hundreds of workers run concurrently, pushing to the same branch with minimal conflicts", but they never actually say if this is successful or not, is it actually working? Can you run this browser yourself? We don't know and they never

-say.

+say explicitly.

@@ -25 +25 @@ After this, they embed the following video:

-[video]

+![](/content/cursor-screenshots.webm)

@@ -33 +33 @@ And below it, they say "While it might seem like a simple screenshot, building a

 And if you try to compile it yourself, you'll see that it's very far away from being a functional browser at all, and seemingly, it never actually was able to build. Multiple recent

-CI workflow

+GitHub Actions

 runs on `main`

-are failing, all the

+show failures (including workflow-file errors), and independent build attempts report dozens of compiler errors, recent

 PRs were

+all

 merged with failing CI, and going back in the Git history from most recent commit, I couldn't find a single commit that compiled cleanly.

@@ -39 +39,3 @@ And diving into the codebase, if the compilation errors didn't make that sure, m

 They later start to talk about what's next, but not a single word about how to run it, what to expect, how it's working or anything else. Cursor's blog post provides no reproducible

-demo/build instructions or

+demo and no

 known-good

-commit,

+revision (tag/release/commit) to verify the screenshots,

 beyond linking the repo.

 Regardless of intent, Cursor's blog post creates the impression of a functioning prototype while leaving out the basic reproducibility markers one would expect from such claim. They never explicitly claim it's actually working, so no one can say they lied at least.

@@ -46,0 +49,2 @@ Which seems like a really strange conclusion to arrive at, when all they've prov

+A "browser experiment" doesn't need to rival Chrome. A reasonable minimum bar is: it compiles on a supported toolchain and can render a trivial HTML file. Cursor's post doesn’t demonstrate that bar, and current public build attempts fail at this too.

@@ -55 +59 @@ The closest they get to implying that this was a success, is this part:

 But this extraordinary claim isn't backed up by any evidence.

-They

+In the blog post they

 never provide a working commit, build instructions or even a demo that can reproduced.

2026-01-16
d664475
 Move

@@ -0,0 +1,57 @@

+---

+date: 2026-01-16

+---

+

+# Cursor's latest "browser experiment" implied success without evidence

+

+On January 14th 2026, Cursor published a blog post titled "Scaling long-running autonomous coding" (https://cursor.com/blog/scaling-agents)

+

+In the blog post, they talk about their experiments with running "coding agents autonomously for weeks"

+

+with the explicit goal of

+

+> understand[ing] how far we can push the frontier of agentic coding for projects that typically take human teams months to complete

+

+They talk about some approaches they tried, why they think those failed, and how to address the difficulties.

+

+Finally they arrived at a point where something "solved most of our coordination problems and let us scale to very large projects without any single agent", which then led to this:

+

+> To test this system, we pointed it at an ambitious goal: building a web browser from scratch. The agents ran for close to a week, writing over 1 million lines of code across 1,000 files. You can explore the source code on GitHub (https://github.com/wilsonzlin/fastrender)

+

+This is where things get a bit murky and unclear. They claim "Despite the codebase size, new agents can still understand it and make meaningful progress" and "Hundreds of workers run concurrently, pushing to the same branch with minimal conflicts", but they never actually say if this is successful or not, is it actually working? Can you run this browser yourself? We don't know and they never say.

+

+After this, they embed the following video:

+

+[video]

+

+And below it, they say "While it might seem like a simple screenshot, building a browser from scratch is extremely difficult.".

+

+### They never actually claim this browser is working and functional

+

+> error: could not compile 'fastrender' (lib) due to 34 previous errors; 94 warnings emitted

+

+And if you try to compile it yourself, you'll see that it's very far away from being a functional browser at all, and seemingly, it never actually was able to build. Multiple recent CI workflow runs on `main` are failing, all the PRs were merged with failing CI, and going back in the Git history from most recent commit, I couldn't find a single commit that compiled cleanly.

+

+I'm not sure what the "agents" they unleashed on this codebase actually did, but they seemingly never ran "cargo build" or even less "cargo check", because both of those commands surface 10s of errors (which surely would balloon should we solve them) and about 100 warnings. There is an open GitHub issue in their repository about this right now: https://github.com/wilsonzlin/fastrender/issues/98

+

+And diving into the codebase, if the compilation errors didn't make that sure, makes it very clear to any software developer that none of this is actually engineered code. It is what is typically known as "AI slop", low quality *something* that surely represents *something*, but it doesn't have intention behind it, and it doesn't even compile at this point.

+

+They later start to talk about what's next, but not a single word about how to run it, what to expect, how it's working or anything else. Cursor's blog post provides no reproducible demo/build instructions or known-good commit, beyond linking the repo. Regardless of intent, Cursor's blog post creates the impression of a functioning prototype while leaving out the basic reproducibility markers one would expect from such claim. They never explicitly claim it's actually working, so no one can say they lied at least.

+

+They finish off the article saying:

+

+> But the core question, can we scale autonomous coding by throwing more agents at a problem, has a more optimistic answer than we expected.

+

+Which seems like a really strange conclusion to arrive at, when all they've proved so far, is that agents can output millions of tokens and still not end up with something that actually works.

+

+## Conclusion

+

+Cursor never says "this browser is production-ready", but they do frame it as "building a web browser from scratch" and "meaningful progress" and then use a screenshot and "extremely difficult" language, wanting to give the impression that this experiment actually was a success.

+

+The closest they get to implying that this was a success, is this part:

+

+> Hundreds of agents can work together on a single codebase for weeks, making real progress on ambitious projects.

+

+But this extraordinary claim isn't backed up by any evidence. They never provide a working commit, build instructions or even a demo that can reproduced.

+

+I don't think anyone expects this browser to be the next Chrome, but I do think that if you claim you've built a browser, it should at least be able to demonstrate being able to be compiled + loading a basic HTML file at the very least.
