---
title: Evolving Git for the next decade [LWN.net]
url: https://lwn.net/SubscriberLink/1057561/bddc1e61152fadf6/
site_name: lobsters
content_file: lobsters-evolving-git-for-the-next-decade-lwnnet
fetched_at: '2026-02-15T06:00:31.217695'
original_url: https://lwn.net/SubscriberLink/1057561/bddc1e61152fadf6/
date: '2026-02-15'
tags: vcs
---

LWN
.net

News from the source






User:


Password:



 |


 |


Log in
 /

Subscribe
 /

Register

# Evolving Git for the next decade

## [LWN subscriber-only content]

 By
Joe Brockmeier
February 11, 2026


FOSDEM

Git is ubiquitous; in the last two decades, the version-control
system has truly achieved world domination. Almost every developer
uses it and the vast majority of open-source projects are hosted in
Git repositories. That does not mean, however, that it is
perfect. Patrick Steinhardt used his main-track session at FOSDEM 2026
to discuss some of its shortcomings and how they are being
addressed to prepare Git for the next decade.

Steinhardt said that he began to be interested in open-source
software around 2002, when he was 11 years old. He bought his first
book on programming when he was 12, and made his first contribution to
an open-source project in 2011. He became a Git and libgit2
contributor in 2015, has been a backend engineer at GitLab since 2020,
and became the manager of the Git team there in 2024.

#### Git must evolve

Git turned 20 last year; there are millions of Git repositories
and even more scripts depending on Git. "The success of Git is
indeed quite staggering." However, the world has changed
quite a bit since Git was first released in 2005; it was designed for
a different era. When Git was released, SHA-1 was considered to be a
secure hash function; that has changed, he said, with theSHAtteredattack that was announced in 2017 byCentrum Wiskunde & Informatica(CWI) and Google. In 2005, the Linux kernel repository was considered
big; now it is dwarfed byChromiumand other massivemonorepos. Continuous-integration
(CI) pipelines were the exception, he said, in 2005—but now
projects have pipelines with lots of jobs that are kicked off every
time there's a new commit.

Also, Steinhardt said to general laughter: "Git was very hard to
use back then; but to be quite honest, Git's still hard to use
nowadays." So, the world has changed and Git needs to change with
it. But, he said, the unique position of Git means that it can't have
a revolution; too many projects and developers rely on it. Instead, it
needs to evolve, and he wanted to highlight some of the important
transitions that Git is going through.

#### SHA-256

The most user-visible change that Git is going through today, he
said, is theSHA-256 transition. SHA-1 is a central part of the
project's design; every single object stored in Git, such as files
(blobs), directory trees, and commits, has an identity
that is computed by hashing the contents of the object. Objects arecontent
addressable, "given the contents, you know the name of the
object". That name, of course, is computed using the
no-longer-secure SHA-1.

The work by CWI and Google proved that attacks on SHA-1 are
viable. It requires a lot of compute, about 110 years
worth of single-GPU computations, but it is possible. He noted that
with all the hype around artificial intelligence, data centers have
greatly increased their GPU capacity. "It is very much in reach of
a large player to compute hash collisions".

No AI slop, all substance: subscribe to LWN today

LWN has always been about quality over quantity; we need your help
to continue publishing in-depth, reader-focused articles about Linux
and the free-software community. Please subscribe today to support our work
and keep LWN on the air; we are offeringa free one-month trial subscriptionto get you started.

SHAttered kicked off quite a few conversations on the Git mailing
lists. During these conversations, he said, it has been asserted that
the use of SHA-1 is not primarily for security and a number of
arguments have been made to back that up. The SHA-1 object hash
is primarily used as an integrity check to detect transmission errors
or bit flips. Also, source code is transparent, "if you see a merge
request where somebody enters random collision data into your code,
then you might probably ask some questions". Additionally, there
are other security measures such as GPG signatures, HTTPS transport,
and a web of trust among developers that means Git does not rely on
SHA-1 alone.

"But the reality is that things are a little bit more
complicated", Steinhardt said. Git may not rely on SHA-1 for
security, but everyone else does. When developers sign a commit with
Git, for example, it is the SHA-1 hash that is signed. It might be
noticeable if source code is changed to cause a collision, but
binary blobs such as firmware are not human-readable, so there is no
way to easily see that there is a malicious file. Tooling around Git
also assumes collision resistance, so CI systems, scripts, and such all
trust the SHA-1 hash.

Finally, various governments and enterprise requirements have
mandated removal of SHA-1 by 2030, so Git needs to move on. And it
has: SHA-256 support was added in October 2020, withversion 2.29. "But
nobody is using it", Steinhardt said, because ecosystem support is
lacking. "Unfortunately, this situation looks somewhat grim".
There is full support in Git itself,DulwichPython implementation, andForgejocollaboration platform. There is experimental support
for SHA-256 in GitLab,go-git, andlibgit2. Other popular Git tools
and forges, including GitHub, have no support for SHA-256 at all. That
creates a chicken-and-egg problem, he said. Nobody is moving to
SHA-256 because it is not supported by large forges, and large forges
are not implementing support because there's no demand.

The problem, Steinhardt said, is that we cannot wait forever. It
will become more and more feasible to break SHA-1, and the next
cryptographic weakness may be just around the corner. Even if there
were full support for SHA-256 today, projects still need time to
migrate. Git will make SHA-256 the default for newly created
repositories in 3.0, he said. The hope is to force forges and
third-party implementations to adapt. "The transition will likely
not be an easy one, and it may result in a few hiccups along the
road." When 3.0 will be released is still up in the air; adiscussionabout its release date in October 2025 on the Git mailing list did not
result in a firm decision.

He said that the audience could help to move things along. "You
can show your favorite code forges that you care about SHA-256 so they
bump the priority." He also encouraged people to help by testing
SHA-256 with new projects and adding support to third-party tools
that depend on Git. "Together, we can hopefully get the ecosystem
to move before the next vulnerability".

#### Reftables

Another significant shift for Git, which he declared his favorite
topic for discussion, is the move toreftables. By default,
Git stores references as "loose" references, where each is
stored as a separate file such as "refs/heads/main". The
format for these files is straightforward to understand, he noted, but
storing every single reference as a file does not scale well. It is
fine for a project with a handful of references, but if there
are hundreds or thousands then it becomes really inefficient.

To deal with that inefficiency today, Git will create apacked-refsfile; this can be done manually with "git pack-refs
--all", but Git will also do it automatically. However,
Steinhardt said, Git still needs to change the way it deals with
references.

The first reason he gave is that "filesystems are simply
weird". Many filesystems, for example, are case-insensitive by
default. That means that Git cannot have two branches whose names only differ
in case, as just one example. It is also an inefficient design, he
said: to create 20 different references, Git has to create 20
different files. That may not take long from a performance
perspective, but each reference requires 4KB of storage for typical
filesystems. That begins to add up quickly.

Packed references are computationally expensive, he said, which is
not a problem if a project only has a few references. "But,
Git users are not always reasonable." He said that GitLab hosts
one repository with about 20-million references; each time a reference
is deleted, thepacked-refsfile has to be completely
rewritten which means rewriting 2GB of data. "To add insult to
injury, this repository typically deletes references every couple
seconds."

The third problem Steinhardt described is that concurrency is an
afterthought. It is impossible to get a consistent view of all
references when there are multiple readers and writers in a repository
at the same time. When a user writes to a repository while another
user is reading the references, it is impossible to know if they are
getting a consistent result or a mixture of the old and new state.

Those problems have been known for a long time, he said, and that
is where the reftable backend comes into the picture. Users can create
a new repository with a reftable today. The tables are now stored in a
binary format rather than the text-based, which is more
efficient—though it does mean that the files are no longer
human-readable. The new data structure also allows Git to perform
atomic updates when writing references to the reference table, and Git
is no longer subject to filesystem limitations when it comes to naming
references.

As with SHA-256, reftables will become the default in Git
3.0. "So if you use Git in scripts or on the server side, you
should make sure you don't play weird games by accessing references
directly on the filesystem". Instead, Git users should always
access references with thegitcommand.

#### Large files

Steinhardt said that, for most of the people in the room, the
scalability problems related to references were mostly theoretical and
rarely encountered in practice. When it comes to scalability
bottlenecks, "the more important problem tends to be large
files". Storing large binary files in Git is, unfortunately, not a
use case that is well-supported today. There are third-party
workarounds, such asGit LFSandgit-annex, but
the Git project would like to solve the problem directly.

Large files are a problem for Git because of the way that it
compresses objects, he said. It works extremely well when working with
text files, such as source code, because that is what Git was designed
for. But Git's compression does not work well for binary files, and
even small edits to such files means creating entirely new
objects.

Another problem is that when cloning a repository, the user gets a
full copy of all of its history by default. That's desirable, he said,
for normal repositories; but for large monorepos with binary files,
"you probably don't want to download hundreds of gigabytes of
data". In addition, there is no support for resuming a cloning
operation: if it fails, the user has to start over. "So if you have
downloaded 400GB out of a 500GB repository and your network
disconnects, then you will have to redownload everything."

Code forges also struggle with large files. Users can resort to
partial clones to avoid downloading an entire repository, but forges
do not have that luxury. The consequence of that is significant
storage costs. He said that an analysis of GitLab's hosted
repositories has shown that 75% of the site's storage space is
consumed by binary files larger than 1MB. Huge repository sizes also
cause repository maintenance to become computationally
expensive. Other types of web sites might offload large files to
content-delivery networks (CDNs), but that is not an option for Git
forges, he said. "All data needs to be served by the Git server,
and that makes it become a significant bottleneck." Large objects
are a significant cost factor for any large Git provider.

Git LFS and partial clones can help users, but those are just
band-aids, Steinhardt said. Even though partial clones have been a
feature in Git for quite a while, "I bet many of you have never
used them before". And even when users do use partial clones,
servers still cannot offload the files to a CDN.

The solution islarge-object
promisors, a remote that is used only to store large blobs and is
separate from the main remote that stores other Git objects and the
rest of the repository. The functionality is now built directly into Git,
and is transparent to the client, he said.

In addition, large-object promisors could be served over protocols
other than HTTPS and SSH. That would allow, for example, serving large
objects via theS3
API. "This allows us to offload objects to a CDN and store
large blobs in a format that is much better suited for them".

Even with promisors, though, Steinhardt said that Git still does
not handle binary files efficiently on the client side. "This is
where pluggable object databases come into play, which will allow us
to introduce a new storage format for a large binary file
specifically." Git needs a format designed for binaries, he said,
where incremental changes to a binary file only lead to a small
storage increase. It needs to be efficient for any file size.

In addition, a new format would need to be compatible with Git's
existing storage format so that users could mix and match the old
format for text files and use the new format for large binaries. Git's
storage format is "deeply baked in" he said, but alternate
implementations like libgit2 and go-git already have pluggable
storage backends. "So there is no fundamental reason why Git can't
do this too. It requires a lot of plumbing and refactoring, but it's
certainly a feasible thing."

The two efforts to handle large objects, promisors and
pluggable object databases, are progressing in parallel. The promisors
effort is farther along, with the initial protocol implementation
shipped in Git 2.50, and additional features in Git 2.52,
both released in 2025. He
said that it is quite close to being usable on the client side, though
when support for promisors will arrive in Git forges is still
undetermined.

The pluggable object database work is not that far along, he
said. Over the past few Git releases the project has spent significant
time refactoring how Git accesses objects. In2.53,
which was released a few days after his talk, Git shipped a unified
object-database interface that will make it easier to change the
format in the future. He said that he expected a proof of concept in
Git 2.54, though implementing a viable format for binary files
"will probably take a little bit longer".

#### User-interface improvements

One area of Git that tends to draw plenty of complaints is its user
interface, he said. Many of Git's commands are extremely confusing,
and some workflows "are significantly harder than they have any
right to be". Recently, Git has had competition in the form of theJujutsuversion-control
project that has made the Git project take a hard look at what it is
doing. (LWNcoveredJujutsu in January 2024.)

Jujutsu is a Git-compatible, Rust-based project started byMartin von Zweigbergk. It has a growing
community and Steinhardt said that "many people seem to prefer the
Jujutsu experience way more" than using Git. That is not much of a
surprise, he said; Git's user interface has grown organically over two
decades. It has "inconsistencies and commands that just don't feel
modern". On the other hand, Jujutsu started from scratch and
learned from Git's mistakes.

Early on, Steinhardt said he had looked at Jujutsu and found it
confusing. "It just didn't make sense to me at all, so I simply
discarded it." However, after noticing that there was a steady
influx of people who did like it, he opted for another look. That
time, something clicked. "That moment when you realize that a tool
simply fixes all the UI issues that you had and that you have been
developing for the last 20 years was not exactly great." He had
two options: despair or learn from the competition. He chose to learn
from it.

There are a number of things that Jujutsu got right, he said. For
example, history is malleable by default. "It's almost as if you
were permanently in an interactive rebase mode, but without all the
confusing parts." When history is rewritten in Jujutsu all
dependents update automatically "so if you added a commit, all
children are rebased automatically". Conflicts are data, not
emergencies. "You can commit them and resolve them at any later
point in time." These features are nice to have, he said, and
fundamentally change how users think about commits. "You stop
treating them as precious artifacts and rather start treating them as
drafts that you can freely edit".

But, he said, Git is old: the project cannot simply completely
revamp its UI and break users' workflows. There are some things
that Git can steal from Jujutsu, though. He discussed the workflow for
splitting a Git commit, which involves seven separate commands with
Git's current UI. Most users do not know how to do this, he
said. The goal is to add several "opinionated subcommands" that
make more modern styles of working with merge requests, such asstacked
branches, much easier.

This includes two new commands, planned for Git
2.54,"git history split"and
"git history reword". Future
releases will have more history-editing subcommands and learn more
from Jujutsu.

Steinhardt did not have time for questions; he closed the talk by
saying that it had been a "whirlwind tour" through what is
cooking in Git right now, and hoped that it had provided a clear
picture of what the project was up to.

The video for the talk isnow
availableon the FOSDEM 2026 web site. Slides have not yet been
published.

[I would like to thank the Linux Foundation, LWN's travel sponsor,
for funding my travel to Brussels to attend FOSDEM.]

Index entries for this article

Conference
FOSDEM/2026

 to post comments


### Jujutsu and GitPosted Feb 11, 2026 17:51 UTC (Wed)
 byPoliorcetics(subscriber, #165001)
 [Link] (11 responses)I’ve been using Jujutsu almost since the first public appearance and I’m very happy Git is looking to take ideas from it (and the inspirations that influenced JJ of course, no software is built in a vacuum), it will make very powerful ideas and tools available to a wider audience### Jujutsu and GitPosted Feb 11, 2026 18:58 UTC (Wed)
 byquotemstr(subscriber, #45331)
 [Link] (9 responses)Perhaps Jujutsu is just one of those technologies whose time has come. Mercurial's Changeset Evolution (https://wiki.mercurial-scm.org/ChangesetEvolution) has provided a similar conflict-as-data experience for over a decade now, but it never really caught it. Maybe JJ will. It's spooky why sometimes N-1 iterations of an idea will languish but for mysterious reasons iteration N finally clicks### Jujutsu and GitPosted Feb 11, 2026 22:31 UTC (Wed)
 byNYKevin(subscriber, #129325)
 [Link]Changeset evolution has had a rough time of it, but there are some valid reasons for this:* It has been publicly labeled as "not ready" for ages, despite large numbers of Google and Facebook engineers using it as a daily driver.* It is yoked to Mercurial, and was only introduced after they had already lost the format war to Git.* It changed a bunch of its own terminology around for no clear reason ("unstable" was renamed to "orphaned," "troubled" was renamed to "unstable," etc.).* It blocks push (by default, overridable with --force) when you have unstable changesets in your repository, so it still treats conflicts as problems rather than data. They're just problems you can defer for a bit instead of problems you have to deal with right now.Disclaimer: I'm one of those Google engineers who use changeset evolution in Mercurial as a daily driver.### Jujutsu and GitPosted Feb 12, 2026 21:56 UTC (Thu)
 byparametricpoly(subscriber, #143903)
 [Link]I used mercurial before Git and the main reason I switched was that everyone else started using git and also git had much better performance with large projects. It's just a fact that C programs perform better than Python. Of course the couple of latest version of Python have been somewhat faster, but Python used to be one of the slowest general purpose language.### Jujutsu and GitPosted Feb 13, 2026 21:52 UTC (Fri)
 byjc2026(subscriber, #182142)
 [Link] (6 responses)Looking at the friction of even using a bigger hash for git, I don't think Jujitsu is going to take over git's market share. There may be some minor UI benefits to using jj but I contend that the technical merits of jj vs git are marginal and subjective, and in some cases worse. People who don't like git usually just don't know it well enough.### Jujutsu and GitPosted Feb 13, 2026 22:01 UTC (Fri)
 byquotemstr(subscriber, #45331)
 [Link] (5 responses)A bigger hash requires global cooperation. Someone using jj locally requires nobody's permission, yes?### Jujutsu and GitPosted Feb 13, 2026 22:29 UTC (Fri)
 byjc2026(subscriber, #182142)
 [Link] (4 responses)True, but using jj locally does not replace git in a true sense. I don't think jj is worth using locally either, even on a green field project. If you think git is hard, you just need to use it a bit more. Relatedly, I used to think git was weird and preferred other systems like Mercurial. But now I realize that was just a surface-level, naive analysis. Most of what git does is providing useful features and its complexity is exaggerated and all basically necessary. The actual concepts and format of git are simple. The features range from simple to sophisticated, and it is rare to be forced to use sophisticated features to just checkpoint or update your code. The command terminology and names are slightly strange, such as all the types of reset you can perform, but there are only a few so you can easily memorize them or make a cheat sheet. I think the model git uses, including its sharper edges, were thoughtfully added by people with experience using other tools and working on large codebases.### Jujutsu and GitPosted Feb 13, 2026 22:42 UTC (Fri)
 bysunshowers(guest, #170655)
 [Link] (1 responses)> But now I realize that was just a surface-level, naive analysis.The lack of universal undo in Git is not a surface-level analysis. It is a fundamental limitation in essentially every pre-jj VCS. (No. the reflog is not universal undo.)Having universal undo like in jj completely changes your level of confidence with source control operations. Screw up somehow? Make a bad edit? Simply run jj undo. People become experts much quicker when they can make mistakes and easily undo them.Based on jj's experience I've started building an operation log and universal undo into basically any project where it's a good fit.### Jujutsu and GitPosted Feb 14, 2026 4:28 UTC (Sat)
 byjc2026(subscriber, #182142)
 [Link]The "universal undo" of jj is achieved by removing some state concepts from git. That may be an improvement in some people's eyes but it makes certain commit history manipulations and constructions more difficult. I'm not the only person to think this.https://github.com/jj-vcs/jj/discussions/1905I think git was built the way it is, as opposed to the way jj is, to solve a particular problem.>Based on jj's experience I've started building an operation log and universal undo into basically any project where it's a good fit.jj did not invent the concept of undo or anything. Different tools have different levels of sophistication in their staging and undo features. Vim for example has an undo tree. SQL databases have transactions. Git has the reflog and the ability to search and go back to any recent commit, tagged or not, and start over (outside of some bizarre circumstances that you must explicitly walk into).### Jujutsu and GitPosted Feb 14, 2026 0:49 UTC (Sat)
 bymarcH(subscriber, #57642)
 [Link] (1 responses)> Most of what git does is providing useful features and its complexity is exaggerated and all basically necessary.Try doing something like this with git:https://v5.chriskrycho.com/journal/jujutsu-megamerges-and...I tried to do more or less that with git for years. No matter what I tried, it was incredibly manual, slow and generally painful. Search "stacked diffs" and find a gazillion of git extensions/variants trying to achieve something similar. None of them does it with out-of-the-box gitBefore jj, the least awful approach I eventually settled on was magit + linear branch + constant re-ordering.I'm afraid you missed that quote in the article and more importantly _whom it came from_:> "That moment when you realize that a tool simply fixes all the UI issues that you had and that you have been developing for the last 20 years was not exactly great."### Jujutsu and GitPosted Feb 14, 2026 4:45 UTC (Sat)
 byjc2026(subscriber, #182142)
 [Link]You know, I skimmed that article and I don't see much of a point to working that way. I stack things up all the time and always rebase and reorder, and it's fine for the uncommon occasions when I have to do it. I prefer completely linear history too by the way. The only time it is ever actually a problem is when creating a PR on a branch with unrelated stuff outstanding, and I don't want to create a bunch of dependencies on things just because I happened to put them first in the commit sequence. For example, let's say I fixed a bug while adding a feature, but the feature commits are first. I have to either create a branch for the bug fix or else rotate the commit stack so that the bug fix one is first, so I can push it by itself. Then rotate again to update the other stuff. This is mainly necessary because the repos I work in are large and slow to manipulate and test. The ideal of making a new branch or new working copy doesn't make sense there.I don't think it would be hard to solve this merge or stack problem in general. If you can figure out a way to correlate the commits, I'm sure ChatGPT can spit out a script to break this dependency thing easily. I never tried using a tool to solve this problem. Maybe Magit is what I should look for. But I'm not so bothered with my current methods either lol...### Jujutsu and GitPosted Feb 11, 2026 19:00 UTC (Wed)
 byjosh(subscriber, #17465)
 [Link]Likewise. Not least of which because jj still has a CLA, and git doesn't, so seeing inspiration from jj added to git feels like a positive step.### Resuming clonesPosted Feb 11, 2026 21:55 UTC (Wed)
 byjengelh(subscriber, #33263)
 [Link] (4 responses)In addition, there is no support for resuming a cloning operationBut there is! clone is just init+fetch+checkout, and "all that's left to do"™ is pick suitable checkpoints. Like so:git init; git remote add origin https://..../linux.git
for i in v2.6.12-rc2 v2.6.12-rc3 ... v6.19; do
 git fetch origin refs/tags/$i:refs/tags/$i
done
git fetch origin
#git gc
git checkout -b master origin/HEAD### Resuming clonesPosted Feb 12, 2026 2:14 UTC (Thu)
 byNahor(subscriber, #51583)
 [Link] (3 responses)sooo... what you're saying, is that the clone operation does not support resuming, right? That if you want to be able to do that, you have to do it yourself instead.But even when trying to do it manually, can you resume a fetch operation? *Lots* of *big* stuff can happen between two tags, making each tag very heavy to download.And how do you get the list of tags in the first place when you don't have the repo on your drive yet?And what of repos with tons of tags (see the whole "reftables" section in the article)? Creating a new connection to the git server for each tag will likely cost you more than trying to clone from scratch.### Resuming clonesPosted Feb 12, 2026 15:11 UTC (Thu)
 bymathstuf(subscriber, #69389)
 [Link]> And how do you get the list of tags in the first place when you don't have the repo on your drive yet?`git ls-remote` works with a local empty repo.### Resuming clonesPosted Feb 12, 2026 16:06 UTC (Thu)
 byjengelh(subscriber, #33263)
 [Link] (1 responses)>*Lots* of *big* stuff can happen between two tags, making each tag very heavy to download.You can go as fine-grained as blobs. Yeah, you can still have gigabitely-sized blobs (not that I think you should).Wait... y'all remember the time when Git repos could be accessed by Dumb HTTP, i.e. without /usr/libexec/git/git-http-backend? There's the resume support you were looking for :-p### Resuming clonesPosted Feb 12, 2026 18:28 UTC (Thu)
 bybrunowolff(guest, #71160)
 [Link]> Wait... y'all remember the time when Git repos could be accessed by Dumb HTTP, i.e. without /usr/libexec/git/git-http-backend?I think that still works. I recently put some git repos for openscad sources for 3d prints up on a server. I currently do pulls to get updates from the source repos I work in. I found out you need run update-server-info to update the refs or cloning won't work. I used post-update.sample as a post-merge hook to do that automatically when I do pulls. I tested cloning using http and it seems to work properly.### splitting git commitsPosted Feb 12, 2026 0:31 UTC (Thu)
 byAdamW(subscriber, #48457)
 [Link] (5 responses)"He discussed the workflow for splitting a Git commit, which involves seven separate commands with Git's current UI. Most users do not know how to do this, he said."Sure I know how to do it!cp bigfilewithlotsofchanges.py /tmpgit reset --hardgit checkout -b letstrythatagaingedit bigfilewithlotsofchanges.py /tmp/bigfilewithlotsofchanges.pycopy/paste chunkgit commit -a -scopy/paste chunk 2git commit -a -srinse, repeatwhat do you mean, that's not the right way?! Crazy talk.### splitting git commitsPosted Feb 12, 2026 13:30 UTC (Thu)
 byalx.manpages(subscriber, #145117)
 [Link] (2 responses)> git checkout -b letstrythatagainThese days, 'git switch -c letstrythatagain' seems to be preferred, I think.> cp bigfilewithlotsofchanges.py /tmp> git reset --hardI would do it differently. I'd first commit to a throw-away branch, so that I can then cherry-pick from it.Also, most often, 'git add -p' (and then 's' for split) would allow committing the changes separately without needing that dance.It's only when the changes are too close together that you'll need such a dance.And when you need it, I'd do it as:$ git add bigfilewithlotsofchanges.py$ git commit -m "WIP; let's split this"$ git tag tmp$ git switch -c tryagain$ git reset HEAD^ --h## loop:$ git checkout tmp -- bigfilewithlotsofchanges.py$ git restore --staged .$ vi bigfilewithlotsofchanges.py ## select the parts you want to keep for this commit$ git add .$ git commit -m "part 1"## goto loop or finish.## now we've finished, make sure that we're exactly like we started:$ git diff tmp$ git tag -d tmpIt's a long procedure, but that gives us a lot of control.### splitting git commitsPosted Feb 12, 2026 17:47 UTC (Thu)
 byjosh(subscriber, #17465)
 [Link] (1 responses)> These days, 'git switch -c letstrythatagain' seems to be preferred, I think.I genuinely find that confusing. `git checkout branchname` makes sense to me as the mechanism for "I want to check out this branch", and adding an option to create the branch makes sense to me as well. I could imagine wanting to change the option from `-b` to `-c`, but I personally feel like "switch" is not any clearer than "checkout".### splitting git commitsPosted Feb 12, 2026 17:58 UTC (Thu)
 byalx.manpages(subscriber, #145117)
 [Link]The problem with git-checkout(1) is that it has too much functionality, and thus is somewhat dangerous.That's why they split its functionality into separate commands git-switch(1) and git-restore(1).See <https://git.kernel.org/pub/scm/git/git.git/tree/Documenta...>.At first, I was a bit confused, but I'm now accustomed to git-switch(1), and it feels natural.### splitting git commitsPosted Feb 12, 2026 14:11 UTC (Thu)
 byiabervon(subscriber, #722)
 [Link]That is... a... way. I'm not sure there is a right way, though, just different ways that different people do use successfully. My personal method is actually for taking a branch that has a bunch of commits with mistakes I fix later, accidental whitespace changes, parts of false starts, etc. and making a clean branch where each commit does things I can describe and justify and eventually reaches almost the same tree.git checkout origin -b refinegit diff HEAD messy | git apply(edit, sometimes)git add -p (say yes to what you want to do in this step)git checkout .make checkgit commit(repeat)There are some snags around handling new files that "messy" added, but it's otherwise a pretty nice workflow (and fewer than seven git commands?). On the other hand, I've never taught someone else to do it, so I don't know how easy it is to learn.### splitting git commitsPosted Feb 12, 2026 16:00 UTC (Thu)
 byeaswarh(subscriber, #131924)
 [Link]In case you weren't joking, git add --interactive is your friend### Data modelPosted Feb 12, 2026 2:41 UTC (Thu)
 bypabs(subscriber, #43278)
 [Link] (3 responses)IIRC another issue is large directories, changes to them store the entire directory for each commit, rather than just the changed file entries.### Data modelPosted Feb 12, 2026 15:07 UTC (Thu)
 bymathstuf(subscriber, #69389)
 [Link] (1 responses)`restic` has a similar problem. The plan there, IIUC, is to split directory blobs using a rolling hash just list data blobs are, but progress is stalled.### Data modelPosted Feb 12, 2026 15:38 UTC (Thu)
 byjohill(subscriber, #25196)
 [Link]We solved this in `bup` recently, which actually stores data in git packfiles, but of course the split tree layout is no longer really compatible with git (it looks like a directory with nested subdirs to git.)### Data modelPosted Feb 13, 2026 11:44 UTC (Fri)
 bygrawity(subscriber, #80596)
 [Link]How does that differ from the way Git stores files? (Which also are stored in full rather than just the differences – but the "packfile" structure delta-compresses the resulting objects.)### Large text filesPosted Feb 12, 2026 2:45 UTC (Thu)
 bypabs(subscriber, #43278)
 [Link]Large text files are problematic in git too I think, is there any work on that?For example, my 51M .bash_history file that just adds more lines to the end at each commit, blows up to a 2.2GB git repo, and the Debian security tracker data repo is enormous.### Flexibility is also a featurePosted Feb 12, 2026 4:48 UTC (Thu)
 bywtarreau(subscriber, #51152)
 [Link] (5 responses)Evolutions need to be careful about not losing flexibility because flexibility is one extremely important Git feature.For example, while it's understandable that reftables can certainly speed up certain operations and/or solve naming problems (BTW aside FAT/NTFS, how many other FS are case insensitive by default to call that "most" ?), being able to grep/edit/add references directly in the refs/ directory *is* a useful feature. Granted it's not used every day, but when you have to do it, it's because you have no other solution. I'm a bit worried about the wording like "users need to make sure they're not doing tricks such as...". Because it's not necessarily "tricks", it's just regular operations that correspond to their legitimate workflow, and when they do it because they need it, they're left without any option left once the feature is removed (except staying on an old version forever of course).I think instead the speaker should rather say "those who rely on this flexibility should contact us and explain what they're doing and why they need it so that we can see if some new features are needed to ease the manipulation of refs".### Flexibility is also a featurePosted Feb 12, 2026 7:03 UTC (Thu)
 bybof(subscriber, #110741)
 [Link] (2 responses)> aside FAT/NTFS, how many other FS are case insensitive by default to call that "most"MacOS. And you know what all fashionable coders use locally, nowadays...### Flexibility is also a featurePosted Feb 12, 2026 7:38 UTC (Thu)
 bymarcH(subscriber, #57642)
 [Link] (1 responses)Note both HFS+ and APFS support case-sensitivity too.Since APFS has volume management built-in (like any other modern FS), it's very quick to carve space for a new case-sensitive partition.### Flexibility is also a featurePosted Feb 12, 2026 9:26 UTC (Thu)
 bydottedmag(subscriber, #18590)
 [Link]Remind me, when did Apple change macOS installations to create $HOME is on a case-sensitive partition?### Flexibility is also a featurePosted Feb 12, 2026 15:09 UTC (Thu)
 bymathstuf(subscriber, #69389)
 [Link] (1 responses)One can also make Linux filesystems per-directory case-insensitive (ext4).Many tools do "if windows or macos, then case-insensitive" when it is really a per-directory query :/ .### Flexibility is also a featurePosted Feb 13, 2026 11:45 UTC (Fri)
 bygrawity(subscriber, #80596)
 [Link]And vice versa, one can make NTFS case-sensitive per-directory (new feature in Windows 10).### git rebase / history rewritePosted Feb 12, 2026 7:55 UTC (Thu)
 bymarcH(subscriber, #57642)
 [Link] (4 responses)> There are a number of things that Jujutsu got right, he said. For example, history is malleable by default. "It's almost as if you were permanently in an interactive rebase mode, but without all the confusing parts." [...] These features are nice to have, he said, and fundamentally change how users think about commits. "You stop treating them as precious artifacts and rather start treating them as drafts that you can freely edit".Rewriting history relies on (at least) two key concepts 1. Change-Ids (as in Gerrit and others) and 2. The distinction between mutable ("rebasable", yuck) versus immutable commits.Funny enough, most GitHub projects don't care much "clean" git histories and do not need these concepts:https://blog.buenzli.dev/announcing-development-on-flirt/...https://zachholman.com/posts/git-commit-history/"Utter Disregard for Git Commit History"So these key concepts are needed only by "traditional" git users like for instance kernel developers who... spent years ignoring and/or dismissing them?!?https://lwn.net/Articles/1037069/"A policy for Link: tags"Very strange.Other relevant references:https://fossil-scm.org/home/doc/tip/www/rebaseharm.mdhttps://gitlab.com/gitlab-org/gitlab/-/issues/24096### git rebase / history rewritePosted Feb 12, 2026 8:51 UTC (Thu)
 bykleptog(subscriber, #1183)
 [Link] (2 responses)I see Jujitsu has the concept of "Change-Id" as a first-class feature, and that it can manage it so it lines up with Gerrit's Change-Id for a seamless experience. No more configuring the commit-hook for example. Very nice! Definitely putting jj on the list of things to try.Unfortunately, standard Git will strip the header out during cherry-pick/rebase, and it doesn't survive format-patch/apply-mail. But if Jujitsu can catch on, perhaps we will finally have a global unique patch identifier that can work cross repo.BTW, I also lament the lack of attention for clean commit histories. It's the main reason we use Gerrit rather than something like GitLab.### git rebase / history rewritePosted Feb 12, 2026 15:11 UTC (Thu)
 bymathstuf(subscriber, #69389)
 [Link]FWIW, we use GitLab and do care about clean histories. GitLab is nowhere near as hostile to rebase workflows as Github.### git rebase / history rewritePosted Feb 12, 2026 15:12 UTC (Thu)
 bymarcH(subscriber, #57642)
 [Link]> Definitely putting jj on the list of things to try.Warning: there is no way back :-)You know something is worth learning when the problem is not finding a good, free tutorial but _choosing_ which one to pick!> But if Jujitsu can catch on, perhaps we will finally have a global unique patch identifier that can work cross repo.In June 2025 there was a very discussion on the git mailing-list about adding Change-Ids to git:https://lore.kernel.org/git/CAESOdVAspxUJKGAA58i0tvks4ZOf...There may have been other ones but this one definitely stands out.> BTW, I also lament the lack of attention for clean commit histories. It's the main reason we use Gerrit rather than something like GitLab.Bisectable histories[*] will never go away but yeah, they seem to be less and less "mainstream" :-(Note appearances can be deceiving. As a coincidence, I was bisecting some really weird regression in cpython yesterday and it worked thanks to a "clean" history despite contributors apparently _not_ force-pushing to Github during review. That's because maintainers seem to always squash before merge, which Github supports just fine. You lose the ability to review more than one final commit per PR but for some GH projects that loss may be an acceptable price to pay.Technically, nothing would stop GH projects from alternating between the force-push review model and not depending on the PR at hand but that would surely confuse the hell out of most people - many of them don't even realize that two different usage models exist in the first place![*] on second thought, "bisectable" is less subjective than "clean" and still generic enough.### git rebase / history rewritePosted Feb 14, 2026 0:38 UTC (Sat)
 bymarcH(subscriber, #57642)
 [Link]> Rewriting history relies on (at least) two key concepts...... and a third, very important one is this:> "so if you added a commit, all children are rebased automatically". Conflicts are data, not emergencies. "You can commit them and resolve them at any later point in time."With git, you have to choose between merges or rewrites. With jj, you can combine both all the time:https://v5.chriskrycho.com/journal/jujutsu-megamerges-and...The first time one does something useful with "jj absorb" is a point of no return. No one in their sane mind would ever use git again to achieve the same thing. It would feel like coding in assembly.### Packfiles as efficient storagePosted Feb 12, 2026 9:39 UTC (Thu)
 byMrWim(subscriber, #47432)
 [Link] (1 responses)> Git's compression does not work well for binary files, and even small edits to such files means creating entirely new objects.I’d have thought that pack files would be efficient at storing small changes to large files. As I understand it the format allows referring to ranges of content from existing objects (not in the same pack).You still need to hash the whole file to name the new object, but you need to read the whole file either way to see if there are changes.Can ‘git add’ write a pack file directly?### Packfiles as efficient storagePosted Feb 13, 2026 0:23 UTC (Fri)
 bypabs(subscriber, #43278)
 [Link]They aren't very efficient even for small edits to large text files. I store my shell history in git. The text file is 51MB but the pack file is 2.2GB.







Copyright © 2026, Eklektix, Inc.Comments and public postings are copyrighted by their creators.Linux is a registered trademark of Linus Torvalds
