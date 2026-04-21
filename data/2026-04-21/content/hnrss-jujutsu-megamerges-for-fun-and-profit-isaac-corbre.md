---
title: Jujutsu megamerges for fun and profit - Isaac Corbrey
url: https://isaaccorbrey.com/notes/jujutsu-megamerges-for-fun-and-profit
site_name: hnrss
content_file: hnrss-jujutsu-megamerges-for-fun-and-profit-isaac-corbre
fetched_at: '2026-04-21T11:59:50.085924'
original_url: https://isaaccorbrey.com/notes/jujutsu-megamerges-for-fun-and-profit
date: '2026-04-20'
description: A practical guide to creating and maintaining powerful megamerge workflows in Jujutsu for faster, conflict-free development.
tags:
- hackernews
- hnrss
---

This article is written both for intermediate Jujutsu users and for Git users
who are curious about Jujutsu.

I’m a bigJujutsuuser, and I’ve found myself relying more and more on
what we in the JJ community colloquially call the “megamerge” workflow for my
daily development. It’s surprisingly under-discussed outside of a handful of
power users, so I wanted to share what that looks like and why it’s so handy,
especially if you’re in a complex dev environment or tend to ship lots of small
PRs.

In a hurry?Skip to the endfor some quick tips.

## Merge commits aren’t what you think they are

If you’re an average Git user (or even a Jujutsu user who hasn’t dug too deep
into more advanced workflows), you may be surprised to learn that there is
absolutely nothing special about a merge commit. It’s not some special case
that has its own rules. It’s just a normal commit that has multiple parents. It
doesn’t even have to be empty!1

@
 my
zpxsys
 Isaac Corbrey
 12 seconds ago
 6
34e82e2

│ 
(empty)
 (no description set)

○ 
ml
lmtkmv
 Isaac Corbrey
 12 seconds ago
 git_head()
 9
47a52fd

├─╮ 
(empty)
 Merge the things

│ ○ 
v
qsqmtlu
 Isaac Corbrey
 12 seconds ago
 f
41c796e

│ │ deps: Pin quantum manifold resolver

○ │ 
t
qqymrkn
 Isaac Corbrey
 19 seconds ago
 04
26baba

├─╯ storage: Align transient cache manifolds

◆
 z
zzzzzzz
 root()
 00
000000

Gotta put it all together!

You may be even more surprised to learn that merge commits are not limited
to having two parents. We unofficially call merge commits with three or more
parents “octopus merges”, and while you may be thinking to yourself “in what
world would I want to merge more than two branches?”, this is actually a really
powerful idea. Octopus merges power the entire megamerge workflow!

## So what the hell is a megamerge?

Basically, in the megamerge workflow you are rarely working directly off the
tips of your branches. Instead, you create an octopus merge commit (hereafter
referred to as “the megamerge”) as the child of every working branch you care
about. This means bugfixes, feature branches, branches you’re waiting on PRs
for, other peoples’ branches you need your code to work with, local environment
setup branches, even private commits that may not be or belong in any branch.Everythingyou care about goes in the megamerge. It’s important to remember
thatyou don’t push the megamerge, only the branches it composes.

@
 mn
rxpywt
 Isaac Corbrey
 25 seconds ago
 f
1eb374e

│ 
(empty)
 (no description set)

○ 
wu
xuwlox
 Isaac Corbrey
 25 seconds ago
 git_head()
 c
40c2d9c

├─┬─╮ 
(empty)
 megamerge

│ │ ○ 
tt
nyuntn
 Isaac Corbrey
 57 seconds ago
 7d
656676

│ │ │ storage: Align transient cache manifolds

│ ○ │ 
p
tpvnsnx
 Isaac Corbrey
 25 seconds ago
 8
97d21c7

│ │ │ parser: Deobfuscate fleem tokens

│ ○ │ 
zw
pzvxmv
 Isaac Corbrey
 37 seconds ago
 1
4971267

│ │ │ infra: Refactor blob allocator

│ ○ │ 
tq
xoxrwq
 Isaac Corbrey
 57 seconds ago
 9
0bf43e4

│ ├─╯ io: Unjam polarity valves

○ │ 
mo
slkvzr
 Isaac Corbrey
 50 seconds ago
 75
3ef2e7

│ │ deps: Pin quantum manifold resolver

○ │ 
q
upprxtz
 Isaac Corbrey
 57 seconds ago
 53
32c1fd

├─╯ ui: Defrobnicate layout heuristics

○ 
ww
tmlyss
 Isaac Corbrey
 57 seconds ago
 58
04d1fd

│ test: Add hyperfrobnication suite

◆
 zz
zzzzzz
 root()
 0
0000000

Scary! Too much merge!

It’s okay if this sounds like a lot. After all, you know how much effort you
put into switching contexts if you have to revisit an old PR to get it reviewed,
among other things. However, this enables a few really valuable things for you:

1. You are always working on the combined sum of all of your work.This
means that if your working copy compiles and runs without issue, you know
that your work will all interact without issue.
2. You rarely have to worry about merge conflicts.You already don’t need to
worry about merge conflicts a ton since conflicts are a first-class concept
in Jujutsu, but since you’re literally always merging your changes together
you’ll never be struck with surprise merge conflicts on the forge side.
There might be the occasional issue with contributors’ changes, but in my
experience this hasn’t been a major problem.
3. There’s way less friction when switching between tasks.Since you’re
always working on top of the megamerge, you never need to go to your VCS to
switch tasks. You can just go edit what you need to. This also means it’s way
easier to make small PRs for drive-by refactors and bugfixes.
4. It’s easier to keep your branches up to date.With a little magic, you
can keep your entire megamerge up to date with your trunk branch with a
single rebase command. I’ll show you how to do that later on.

## How do I make one?

Starting a megamerge is super simple: just make a new commit with each branch
you want in the megamerge as a parent. I like to give that commit a name and
leave it empty, like so:

jj
 new
 x
 y
 z

jj
 commit
 --message
 "megamerge"

 Making megamerges. It's not so hard after all!
 

You’re then left with an empty commit on top of this whole thing. This is where
you do your work! Anything above the megamerge commit is considered WIP. You’re
free to split things out as you need to, make multiple branches based on that
megamerge commit, whatever you want to do. Everything you write will be based on
the sum of everything within the megamerge, just like we wanted!

Of course, at some point you’ll be happy with what you have, and you’ll be left
wondering:

## How do I actually submit my changes?

How you get your WIP changes into your megamerge depends on where they need to
land. If you’re making changes that should land in existing changes, you can
use thesquashcommand with the--toflag to shuffle them into the right
downstream commits. If your commit contains multiple commits’ worth of changes,
you can eithersplitit out into multiple commits before squashing them or
(what I prefer) interactively squash withsquash --interactiveto just pick
out the specific pieces to move.

# Squash an entire WIP commit (defaults to `--from @`)

jj
 squash
 --to
 x
 --from
 y

# Interactively squash part of a WIP commit (defaults to `--from @`)

jj
 squash
 --to
 x
 --from
 y
 --interactive

 Hunk, I choose you!
 

Of course, Jujutsu is a beautiful piece of software and has some automation for
this! Theabsorbcommand will do a lot of this for you by identifying which
downstream mutable commit each line or hunk of your current commit belong in andautomatically squashing them down for you. This feels like magic every time
I use it (and not the evil black box black magic kind of magic where nothing can
be understood), and it’s one of the core pieces of Jujutsu’s functionality that
make the megamerge workflow so seamless.

# Automagically autosquash your changes (defaults to `--from @`)

jj
 absorb
 --from
 x

 Ope, that was fast.
 

Absorbing won’t always catch everything in your commit, but it’ll usually get at
least 90% of your changes. The rest are either easily squashable downstream or
unrelated to any previous commit.

Conveniently, things aren’t much more complicated if I have changes that belong
in a new commit. If the commit belongs in one of the branches I’m working on, I
can just rebase it myself and move the bookmark accordingly.

jj
 commit

jj
 rebase
 --revision
 x
 --after
 y
 --before
 megamerge

jj
 bookmark
 move
 --from
 y
 --to
 x

Let’s break that rebase down to better understand how it works:

# We're gonna move some commits around!

jj rebase

 # Let's move our WIP commit(s) x...

 --revision x

 # so that they come after y (e.g. trunk())...

 --after y

 # and become a parent of the megamerge.

 --before megamerge

 A little bit of rocket surgery, as a treat.
 

If I’ve started work on an entirely new feature or found an unrelated bug to
fix, then it’s even simpler! Using a few aliases, I can super easily include new
changes in my megamerge:2

There are also template aliases which let you change how Jujutsu logs to
the terminal using thetemplating language, and fileset aliases, which act
similarly to revset aliases but act on files instead of revisions using thefileset language.

[
revset-aliases
]

# Returns the closest merge commit to `to`

"closest_merge(to)" = 
"heads(::to & merges())"

[
aliases
]

# Inserts the given revset as a new branch under the megamerge.

stack = [
"rebase"
, 
"--after"
, 
"trunk()"
, 
"--before"
, 
"closest_merge(@)"
, 
"--revision"
]

Here’s a quick explanation of whatclosest_merge(to)is actually doing:

heads( 
# Return only the topologically tip-most commit within...

 ::to 
# the set of all commits that are ancestors of `to`...

 & merges()) 
# ...that are also merge commits.

Using that revset alias,stacklets us target any revset we want and insert it
betweentrunk()(your main development branch) and our megamerge commit:

jj
 stack
 x::y

 Whoa, that was neat!
 

This is more useful if I havemultiplestacks of changes I want to include in
parallel; if it’s just one, I have another alias that just gets the entire stack
of changes after the megamerge:

[
aliases
]

stage = [
"stack"
, 
"closest_merge(@).. ~ empty()"
]

closest_merge(@).. 
# Return the descendants of the closest merge

 # commit to the working copy...

 ~ empty() 
# ...without any empty commits.

This one doesn’t require any input! Just have your commits ready and stage ‘em:

jj
 stage

 Wait, what? You can do that?
 

The last missing piece of this megamerge puzzle is (unfortunately) dealing with
the reality that isother people:

## How do I keep all this crap up to date?

That’s a great question, and one I spent a couple months trying to answer in
a general sense. Jujutsu has a really easy way of rebasing your entire working
tree onto your main branch:

jj
 rebase
 --onto
 trunk
()

 Nice.
 

However, this only works if your entire worktree isyourchanges. When you try
to reference commits you don’t own (like untracked bookmarks or other people’s
branches) Jujutsu will stop early to protect them from being rewritten.3

 Wait, not so nice. How do I do this?
 

Let’s fix that by rebasing only the commits we actually control. I struggled
with this one for a while, but thankfully the Jujutsu community is awesome.
Kudos toStephen Jenningsfor coming up with this awesome revset:

[
aliases
]

restack = [
"rebase"
, 
"--onto"
, 
"trunk()"
, 
"--source"
, 
"roots(trunk()..) & mutable()"
]

roots( 
# Get the furthest upstream commits...

 trunk()..) 
# ...in the set of all descendants of ::trunk()...

 & mutable() 
# ...and only return ones we're allowed to modify.

Rather than trying to rebase our entire working tree (likejj rebase --onto trunk()tries to do), this alias only targets commits we’re actually allowed to
move. This leaves behind branches that we don’t control as well as work that’s
stacked on top of other people’s branches. It has yet to fail me, even with
monster ninefold mixed-contributor megamerges! (Say that five times fast.)

 There we go, that's better!
 

## TL;DR

Jujutsu megamerges are super cool and let you work on many different streams of
work simultaneously. Read the whole article for an in-depth explanation of how
they work. For a super ergonomic setup, add these to your config withjj config edit --user:

[
revset-aliases
]

"closest_merge(to)" = 
"heads(::to & merges())"

[
aliases
]

# `jj stack <revset>` to include specific revs

stack = [
"rebase"
, 
"--after"
, 
"trunk()"
, 
"--before"
, 
"closest_merge(@)"
, 
"--revision"
]

# `jj stage` to include the whole stack after the megamerge

stage = [
"stack"
, 
"closest_merge(@).. ~ empty()"
]

# `jj restack` to rebase your changes onto `trunk()`

restack = [
"rebase"
, 
"--onto"
, 
"trunk()"
, 
"--source"
, 
"roots(trunk()..) & mutable()"
]

Useabsorband/orsquash --interactiveto get new changes into existing
commits,commitandrebaseto make new commits under your megamerge,
andcommitwithstackorstageto move entire branches into your
megamerge.4

# Changes that belong in existing commits

jj
 absorb

jj
 squash
 --to
 x
 --interactive

# Changes that belong in new commits

jj
 rebase
 --revision
 y
 --after
 x

# Stack anything on top of the megamerge into it

jj
 stage

# Stack specific revsets into the megamerge

jj
 stack
 w::z

Remember that megamerges aren’t really meant to be pushed to your remote;
they’re just a convenient way of showing yourself the whole picture. You’ll
still want to publish branches individually as usual.

 I live in this constantly, and you can too.
 

Megamerges may not be everyone’s cup of tea – I’ve certainly gotten a few
horrified looks after showing my working tree – but once you try them, you’ll
likely find they let you bounce between tasks with almost no effort. Give them
a try!

## Footnotes

1. In Git, merge commits that contain new changes outside of conflict
resolution are called an “evil merge”. Evil mergesaren’t really “evil” in
Jujutsusince it has a more consistent model than Git.5Commit ID:b976b2a9c6ebbaada7fcd9d112a8390f2cb75b54Change ID:tqxoxrwqqqtmxvywmzmspstupqqkskqkAuthor :Isaac Corbrey<isaac@isaaccorbrey.com> (28 minutes ago)Committer:Isaac Corbrey<isaac@isaaccorbrey.com> (24 minutes ago)Parent :ttnyuntnstorage: Align transient cache manifoldsParent :qupprxtzui: Defrobnicate layout heuristicsio: Unjam polarity valvesAdded regular file two.txt:1:# Sphinx of black quartz, judge my vowBubble, bubble, toil and trouble.Definitely tangential, but I felt it necessary to mention.↩
2. Aliases are a super powerful part of Jujutsu. There are two types you should
look into:revset aliases, which allow you to create custom functions which
return one or more commits with therevset language, andcommand aliases,
which let you extend Jujutsu’s default functionality and add your own.↩
3. Jujutsu has a concept ofmutableandimmutablecommits, which basically
dictates what commits you’re allowed to modify on a normal basis. It’s
largely just a lint since you can override this with--ignore-immutable,
but it’s good at keeping you out of trouble. You can use themutable()andimmutable()aliasesto select only mutable and immutable commits
respectively.↩
4. Ifrestackdoesn’t quite work the way you like, try incorporatingthis
config from Austin Seipp. My default setup restacks every mutable commit in
your repo, which behaves poorly when you have lots of mutable branches from
the past you haven’t had time to clean up yet.[revset-aliases]'stack()' ='stack(@)''stack(x)' ='stack(x, 2)''stack(x, n)' ='ancestors(reachable(x, mutable()), n)'[aliases]restack = ["rebase","--onto","trunk()","--source","roots(trunk()..) & stack()"]Thanks for the tip Cole!↩
5. Thanks toAndrew Hoogfor helping me figure out footnotes in Astro. Did
you know that you can reference footnotes from other footnotes?↩

 
 
 
 

Special thanks tomsmetko,Cole Helbling,Hardy Jones,Alpha Chen, Jeremy Brown,Luke Randall, 789.ha, andPhilip Metzgerfor reading early drafts and sharing their feedback! We all see further
 by standing on the shoulders of giants.

I like building tools, breaking workflows, and putting them back together
 better. If you enjoy my work and want to support it, you canbuy me a coffee ☕orsupport me on Liberapay 💛.