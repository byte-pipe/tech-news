---
title: Jujutsu + Radicle = ❤️
url: https://radicle.xyz/2025/08/14/jujutsu-with-radicle
site_name: lobsters
fetched_at: '2025-08-15T23:06:59.294259'
original_url: https://radicle.xyz/2025/08/14/jujutsu-with-radicle
date: '2025-08-15'
description: Radicle is a decentralized platform for code collaboration, offering secure and sovereign infrastructure for developers.
tags: vcs
---

# Jujutsu + Radicle = ❤️

How I use Jujutsu in tandem with Radicle

Published by
fintohaps
 on 14.08.2025

* Radicle and GitMy.git/configgit fetch radandgit push rad
* My.git/config
* git fetch radandgit push rad
* Jujutsu and Gitjj newjj editjj squashjj rebaseMy.jj/configUser ConfigRepository Config
* jj new
* jj edit
* jj squash
* jj rebase
* My.jj/configUser ConfigRepository Config
* User Config
* Repository Config
* Radicle and JujutsuContributing PatchesCreating a New PatchUpdating a PatchMaintaining Patches
* Contributing PatchesCreating a New PatchUpdating a Patch
* Creating a New Patch
* Updating a Patch
* Maintaining Patches

Roughly a year ago at the first everLocal First Conference, a friend and
previous colleague –Alex Good– told me about this tool calledjj(Jujutsu). We did the usual thing and I sat down beside him as he
explained it to me. My brain did the usual thing and took in some of the
information but not enough of it, and so I didn’t touchjjfor quite some time
after that – but what’s good enough for Alex Good is good enough for me.

After that, I feel like I saw a post aboutjjonce every couple of months on
Hacker News – confirmation bias anyone? It was a constant talking point during
Git Merge 2024, and now it’s a third Git tool that uses the concept of change
identifiers, so it’s a talking point on theGit mailing list.

So, fast-forward a year or so, and I’ve been usingjjfor quite some time
while contributing to and maintaining theheartwoodrepository – the home of
the Radicle protocol – as well as some others. Did I have to convince my whole
team thatjjshould be used by all of us and we all switch to this new
workflow? No. The first piece of “magic” ofjjis that it is essentially a
version control system that has a transparent layer on top of Git itself. A
change injjwill always point to a Git commit. The beauty of its
implementation is that the underlying commit can change as much as it wants,
while thejjchange remains the same. This unlocks a lot of nice flows for
managing changes usingjj.

So, you must be wondering by now, “How do I blend Radicle withjj?” Well,
let’s dance between the three worlds ofjj, Git, and Radicle, to see how they
have melted together to form a beautiful (almost) branch-less workflow.

### Radicle and Git

I won’t spend too much time here, but if you don’t know by now, Radicle works on
top of Git to allow people to use this ubiquitous tool, while we benefit from
its storage and protocol. When you start a Radicle repository, it’s essentially
a Git repository where we use some special references and extension points of
Git to cryptographically secure your commits, and store all yoursocial, collaborative artifacts. If you haven’t yet, godownloadRadicle and try it yourself using ourguides.

Note that if you’re already familiar withjjthis might not be that
interesting for you, and you can skip toUser Config.

#### My.git/config

As a maintainer of a few repositories using Radicle, I naturally need to push to
and fetch from the repository in Radiclestorage. This means
that I’ll need a remote – this is set up for you when you runrad initorrad
clone. This looks like:

[remote "rad"]


url

=

rad://z371PVmDHdjJucejRoRYJcDEvD5pp


fetch

=

+refs/heads/*:refs/remotes/rad/*


fetch

=

+refs/tags/*:refs/remotes/rad/tags/*


pushurl

=

rad://z371PVmDHdjJucejRoRYJcDEvD5pp/z6MkireRatUThvd3qzfKht1S44wpm4FEWSSa4PRMTSQZ3voM

[branch "master"]


remote

=

rad


merge

=

refs/heads/master

Therad://URL tellsgitwhichremote helperto use
by trying to findgit-remote-rad. This will handle fetching/pushing from/to
the repository identified byz371PVmDHdjJucejRoRYJcDEvD5pp. The stringz6MkireRatUThvd3qzfKht1S44wpm4FEWSSa4PRMTSQZ3voMis my Node ID, and
identifies my machine
which makes sure that when I push, my references get stored under thatnamespace. Then when have the usual upstream branch setup
formasterfor theradremote – you may be familiar with this Git config entry
when you have youroriginset up for another Git forge.

There’s one last piece of the puzzle in config that is an alias for easily
creating a Radiclepatch.

[alias]


patch

=

push rad HEAD:refs/patches

When you push to the special referencerefs/patches, the remote helper will
catch this and create a new patch for you, and in this case it will use whateverHEADis for the head of the patch. Note that it will use whateverrad/masteris as the base of the patch – that is to say, whatever commits are betweenrad/masterandHEAD(includingHEAD) are the commits being proposed by the
patch. So, whenever I’m ready to make a patch, I usegit patchand my$EDITORpops open to make my well-crafted message describing what changes I’m
making.

#### git fetch radandgit push rad

This is going to be brief. All I do withgitnow isgit fetch rad(or my
peer’s remotes) to fetch any new work in Radicle storage. For pushing I will usegit push radto create or update patches (coming up), update my version ofmaster, and, on the rare occasion, push a branch. That’s it! No morecommit,
no morerebase, no moremerge– ok I still usegit log– but that’s pretty
much it. So how did I ditch all of these commands? Let’s take a lookjj.

### Jujutsu and Git

Let’s see how I’m usingjjby visiting several of its commands and seeing how
I can use them in different scenarios.

#### jj new

It’s only natural to start off withjj new. This command creates a new change
injj, as well as creating a new, empty commit for that change. Whenever I’m
going to make a new change that’s based on themasterbranch, I run:

$ jj new master@rad
Working copy (@) now at:
qx
uvyurn

8e
711a87

(empty)

(no description set)

Parent commit (@-) :
xsl
qmmsl

62
cdaf6d

master@rad
 |
deployment: Vercel → Cloudflare Workers
Added 0 files, modified 0 files, removed 1 files

You’ll notice thatjjspits out a Change ID and a Commit ID. You may also
notice that a prefix is highlighted – this is the unique prefix for the change
and the commit at this time! Which means that I can useqxor8eto refer to
this particular change or commit without any ambiguity; an amazing UX, if you
ask me.

At this point, I might know what I’m going to be working on so I usejj
describeto give this change a message.

$ jj describe -m
"blog: Radicle and JJ"

Working copy (@) now at:
qx
uvyurn

40
8133a5

(empty)
 blog: Radicle and JJ

Parent commit (@-) :
xsl
qmmsl

62
cdaf6d

master@rad
 |
deployment: Vercel → Cloudflare Workers

I’ve now changed the description so that it no longer says(no description
yet), and it now readsblog: Radicle and JJ.

So let’s see what we have here:

$ jj show qx
Commit ID:
408133a5e54c80d2398be0c78cccabbd6063902d

Change ID:
qxuvyurnqsvupzlpzsvzzpqlmlqvoxwq

Author :
Fintan Halpenny
 <
fintan.halpenny@radicle.xyz
> (
2025-06-10 07:52:34
)
Committer:
Fintan Halpenny
 <
fintan.halpenny@radicle.xyz
> (
2025-06-10 07:52:34
)

 blog: Radicle and JJ

We can see that it looks similar to a Git commit, which we can also inspect
using:

$ git show 408133a5e54c80d2398be0c78cccabbd6063902d

commit 408133a5e54c80d2398be0c78cccabbd6063902d

Author: Fintan Halpenny <fintan.halpenny@radicle.xyz>
Date: 2025-06-10 07:52:34 +0200

 blog: Radicle and JJ

This leaves us in a position to do our usual changes within our working copy of
the Git repository.

At any point where I’m looking to separate changes, I can usejj newagain,
specifying any change to make a new change after the given change:

$ jj new qx
Working copy (@) now at:
w
msmovxx

c5
0301c1

(empty)

(no description set)

Parent commit (@-) :
qx
uvyurn

40
8133a5
 blog: Radicle and JJ

$ jj describe -m
"blog: Radicle an JJ - add body"

Working copy (@) now at:
w
msmovxx

a3
d195ad

(empty)
 blog: Radicle and JJ – add body

Parent commit (@-) :
qx
uvyurn

40
8133a5
 blog: Radicle and JJ

If I ever think I’m about to make some changes before the change I’m on, then I
can use the-Boption:

$ jj new -B @
Rebased 1 descendant commits
Working copy (@) now at:
zv
rmpyox

f0
635336

(empty)

(no description set)

Parent commit (@-) :
xsl
qmmsl

62
cdaf6d

master@rad
 |
deployment: Vercel → Cloudflare Workers
Added 0 files, modified 0 files, removed 1 files

#### jj edit

At any point in time, I can also decide to go back to an old change and edit it,
specifying the change that I want to edit:

$ jj edit qx
Working copy (@) now at:
qx
uvyurn

40
8133a5
 blog: Radicle and JJ

Parent commit (@-) :
xsl
qmmsl

62
cdaf6d

master@rad
 |
deployment: Vercel → Cloudflare Workers

You can now forget about all thosefixup!commits you were making to add
changes into previous commits. No longer are you at the mercy of making a commit
that is ahead of some other changes and you need to reorder it usinggit
rebase. You taste that? It tastes like victory…

#### jj squash

Ok, so you’ve made some changes that are not related to the current change? This
happens, or at least it does to me – I’m not perfect, (un)fortunately. I can use
the power ofjj new, whether after or before the current change, and combine
it withjj squash:

$ jj squash -u --from w --to qx
Rebased 1 descendant commits
Working copy (@) now at:
qx
uvyurn

1e
2b0ccc

(empty)
 blog: Radicle and JJ

Parent commit (@-) :
xsl
qmmsl

62
cdaf6d

master@rad
 |
deployment: Vercel → Cloudflare Workers

This says that I’m squashing the changes from the change identified bywinto
the changeqx, and I want to keep the description ofqxand drop the
description ofw(the-uoption).

For extra points,jjeven includes the beautiful-ioption forchoosingwhich changes you’re taking from the source change – via a TUI. I cannot
begin to describe how useful this is for moving around file changes and keeping
my history clean and linear.

#### jj rebase

The final piece of the puzzle, at least for my workflow, isjj rebase. I can
move around changes and put them on top of a destination change:

$ jj rebase -d qx -r sm
Working copy (@) now at:
sm
vvuqzo

42
0180e8
 blog: relevant blog material
Parent commit (@-) :
qx
uvyurn

1e
2b0ccc
 blog: Radicle and JJ
Added 1 files, modified 0 files, removed 0 files

This rebases the changesmonto the changeqx. In fact, the-rcan take a
set of changes (seerevsets) and graft them all on top of the
destination.

#### My.jj/config

The final part I’ll touch on is myjjconfig, which can be split into the user
and repo config. Thanks to Bruno, who wrote a lot of this on Zulip, and I
cribbed it from him.

##### User Config

Here is my user config, and we’ll discuss a couple of the entries, and I’ll
leave the rest as homework.

[aliases]

dlog

=

[
"log"
,

"-r"
]

l

=

[
"log"
,

"-r"
,

"(trunk()..@):: | (trunk()..@)-"
]

fresh

=

[
"new"
,

"trunk()"
]

tug

=

[


"bookmark"
,


"move"
,


"--from"
,


"closest_bookmark(@)"
,


"--to"
,


"closest_pushable(@)"
,

]

[revset-aliases]

"closest_bookmark(to)"

=

"heads(::to & bookmarks())"

"closest_pushable(to)"

=

"heads(::to & mutable() & ~description(exact:
\"\"
) & (~empty() | merges()))"

"desc(x)"

=

"description(x)"

"pending()"

=

".. ~ ::tags() ~ ::remote_bookmarks() ~ @ ~ private()"

"private()"

=

"description(glob:'wip:*') |
\

 description(glob:'private:*') |
\

 description(glob:'WIP:*') |
\

 description(glob:'PRIVATE:*') |
\

 conflicts() |
\

 (empty() ~ merges()) |
\

 description('substring-i:
\"
DO NOT MAIL
\"
')"

* fresh: this allows me to have an alias forjj new master@radand usejj
fresh.
* tug: this allows me to tug the closestbookmarkto a change
that can be pushed – we’ll see an example of this later.

##### Repository Config

And here is my repository config, which we’ll discuss a bit more in detail.

[revset-aliases]

"trunk()"

=

"master@rad"

"immutable_heads()"

=

"present(trunk()) |
\

 tags() |
\

 (
\

 untracked_remote_bookmarks() ~
\

 untracked_remote_bookmarks(remote='rad') ~
\

 untracked_remote_bookmarks(regex:'^patch(es)/',remote='rad')
\

 )"

[git]

write-change-id-header

=

true

We want to change thetrunk()alias from its default injjso that it points
tomaster@rad, the default branch in this particular Radicle repository. Thetrunk()revset is used in a few place, for example, we saw it above infresh, but it is also in the next revset alias.

Some changes injjwill be marked asimmutable.jjwill prevent you from changing certain changes if they are marked as immutable,
and its default value for this can be very restrictive, so instead we change it
here. First we mark changes that arepresentintrunk()ortags()as
immutable. Then we have untracked remote bookmarks with the set difference
operator~. What are not marking as immutable are bookmarks that are inrador thatpatch/patches. That is, if the changes are ours or from patches,
then they’re safe to edit. You might think, “Why are patches safe?”” Well, let’s
finally get into Radicle and Jujutsu.

### Radicle and Jujutsu

So here we are, a lot of build up to get to the point where I can describe how I
can avoid using branches (as much as possible).

#### Contributing Patches

We will first dive into contributing a new patch using Radicle. As described inJujutsu and Git, I can start making a set of changes usingjj new, editing them just how I like usingjj edit, and ordering them just
the way I want withjj rebaseandjj squash. During this whole time, I’m in
that, initially scary,detached HEAD state. Here it comes,
we’re going to make a patch!

##### Creating a New Patch

git patch

That’s it. Well, the$EDITORopens and I write a title and a body describing
my wonderful changes, and when I’m done, the remote helper will create the patch
and announce it to the network.

✓
 Patch
e5f0a5a5adaa33c3b931235967e4930ece9bb617
 opened

✓
 Synced with
8
 node(s)

To rad://z3cyotNHuasWowQ2h4yF9c3tFFdvc/z6MkvZwzK64f3GuDcAs6dEcje89ddfHkBjS1v9Dkh7aCGq3C
 * [new reference] HEAD -> refs/patches

##### Updating a Patch

Let’s be honest though, my wonderful changes are rarely wonderful from the
get-go. They need some polishing, and my peers always have great suggestions
that I should integrate into the patch.

From here, I can find the patch usingrad patch:

$ rad patch

╭
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
╮

│
●
ID

Title

Author

Reviews

Head

+

-

Updated

 │

├
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
┤

│
●

18a71ad
 radicle-cli: Warn when using old names of nodes
self

(you)
 - - - - -
552f4af

+146

-3

4 days ago

 │

│
●

ed450c9
 node, profile, ssh: Make key location configurable
self

(you)
 - - - - -
d2f7b89

+376

-74

1 month ago

 │

│
●

12bc851
 node, cli: Refactor test environment
self

(you)
 - - - - -
d059957

+826

-1214

1 month ago

 │

│
●

3219ef8
 Remove predefined bootstrap nodes
istankovic

z6MkmiJ…mkTV5sS
 - - - - -
7322e3a

+138

-108

2 days ago

 │

│
●

058586b
 Suggest the git configured default branch during init
stemporus

z6MkqLa…jr8xo5K
 - - - - -
6a1147f

+16

-8

2 weeks ago

 │

│
●

1015e51
 build: Rewrite tagging script
fintohaps

z6Mkire…SQZ3voM
 - - - - -
149de0b

+24

-12

3 weeks ago

 │

│
●

e85ff9a
 node: clean up `UploadError`
fintohaps

z6Mkire…SQZ3voM
 - - - - -
b408e44

+15

-13

3 weeks ago

 │

│
●

c54883e
 Canonical References
fintohaps

z6Mkire…SQZ3voM
 - - - - -
34014a6

+4642

-1575

1 month ago

 │

│
●

e500399
 radicle: improve inline comments
fintohaps

z6Mkire…SQZ3voM
 - - - - -
e7cab63

+924

-244

1 month ago

 │

│
●

6080c3c
 Add issue instructions
yorgos-laptop

z6MkrnX…CPFSFS3
 - - - - -
1877285

+32

-15

1 month ago

 │

│
●

40a8d72
 radicle: introduce COB stream
fintohaps

z6Mkire…SQZ3voM
 - - - - -
ec00acb

+1178

-9

4 months ago
 │

│
●

8ab3f9c
 Add document on how to implement a new COB type
liw

z6MkgEM…1b2w2FV
 - - - - -
5a3b095

+314

-0

1 year ago

 │

╰
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
╯

Let’s say I received feedback on myCanonical Referencespatch, I can use itsID, the shortened version above, to inspect it:

$ rad patch show c54883e

╭
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
╮

│
Title

Canonical References

 │

│
Patch
 c54883e5ffb1f8a99f432e3ac79c0b728cd0dab3
 │

│
Author

fintohaps

z6Mkire…SQZ3voM

 │

│
Head

34014a67b0ddc859d95e17ffc71c1ae61aff5758

 │

│
Branches

patch/c54883e, sync-goal

 │

│
Commits
 ahead
6
, behind
49

 │

│
Status

open

 │

│

 │

│
See RIP-0004[^0] for the specification.
 │

│

 │

│
This patch is an implementation of RIP-0004. It implements the rules mechanism
 │

│
within the `rules` module. This is interplays with the existing `canonical`
 │

│
mechanisms, already defined (but slightly refactored).
 │

│

 │

│
The `rules` are then used in pushing and fetching references. A test is added to
 │

│
illustrate the canonical references in action via tags.
 │

│

 │

│
There were some incidental changes that were made to ensure the tags use case is
 │

│
easy for users. The first change was to add a tags refspec to remotes in order
 │

│
to easily fetch tags from peers -- as well ensuring those tags do not pollute
 │

│
the `refs/tags` namespace in the working copy.
 │

│

 │

│
This had a knock on change where there was a bug `libgit2` that didn't allow for
 │

│
deleting `multivar` entries, which the new remote setup fell under. This was
 │

│
fixed and so we update to `git2-0.19`.
 │

│

 │

│
As well this, the `rad id update` command would error if the payload identifier
 │

│
was not the project identifier. This would stop adding new payloads to extend
 │

│
the identity -- which was needed for introducing canonical references.
 │

│

 │

│
[^0]:
 │

│
https://app.radicle.xyz/nodes/seed.radicle.garden/rad:z3trNYnLWS11cJWC6BbxDs5niGo82/patches/1d1ce874f7c39ecdcd8c318bbae46ffd02fe1ea8?tab=changes
 │

├
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
┤

│
34014a6
 radicle: refactor rule matching
 │

│
0e0b77e
 radicle: add canonical refs to identity
 │

│
bbe019c
 radicle: canonical reference rules
 │

│
b3ad6f2
 radicle: refactor Canonical
 │

│
04277b4
 radicle: store threshold in Canonical
 │

│
312c6a4
 meta: relax radicle-git dependencies
 │

├
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
┤

│
●
 opened by
fintohaps

z6Mkire…SQZ3voM

(3e97837)
 10 months ago
 │

│
↑
 updated to c1a2cc5787f44c0a835c1deae375be04c399dd7e
(58e932c)
 9 months ago
 │

│
↑
 updated to c55494efc2e780cd6c91a1f90efdae8a3eb1c7ef
(1b07774)
 8 months ago
 │

│
↑
 updated to 583e6b3366c36cc7e67910c29a66750397a60484
(fdd5277)
 7 months ago
 │

│
↑
 updated to d54ddef216909bdd3e54e33e4f82c45df79c00d3
(f24f9d8)
 7 months ago
 │

│
↑
 updated to ac48ae6e75d4eaa13daed657eed24dfeabb9be94
(7d8e461)
 7 months ago
 │

│
↑
 updated to 2b31e460db7451376dc3e346ee02b5fd597fa5c6
(040cfb7)
 7 months ago
 │

│
↑
 updated to e1c360a1311a0a215bed6eb42e4b0c8c5c44e611
(f0dec88)
 6 months ago
 │

│
↑
 updated to 492cfbafd31e4bac85ee73af519ddc6254b47f82
(f9cb27f)
 4 months ago
 │

│
↑
 updated to fbdf18d7683bdac7a76149777eed5cf9bbbf5bd5
(2a64755)
 4 months ago
 │

│
↑
 updated to 4baf32afd65f2c4b374d8f21fed6877aa804a003
(0cecae6)
 4 months ago
 │

│
 └─ ⋄ reviewed by
self

(you)
 1 month ago
 │

│
↑
 updated to d2ebc70caca54a8ba508d72862c1e1c79d718129
(4515d45)
 1 month ago
 │

│
↑
 updated to 13e9ba641c624db26b6bfe85870daf064f90e9ab
(045e465)
 1 month ago
 │

│
↑
 updated to 47495c408ccf5eec49b61c7bdb339e5f2d695a30
(a6be355)
 1 month ago
 │

│
↑
 updated to e3bdb65d3adb94360dd3449744792f6ecb1f451f
(8d08215)
 1 month ago
 │

│
 └─ ⋄ reviewed by
erikli

z6MkgFq…FGAnBGz
 1 month ago
 │

│
↑
 updated to 9f779028704b4c022cbe25c0e4a9bb46dc8463ba
(49fcea7)
 1 month ago
 │

│
↑
 updated to 86ebfcaaf986edba5e77ede1be4d3c4ce33bd27c
(2df7cd9)
 1 month ago
 │

│
↑
 updated to fa9bdff35d76903f72cf24f1cccca812ae26e98c
(34014a6)
 1 month ago
 │

╰
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
╯

You can see here how non-perfect my changes are, I’m being vulnerable here.

I can now grab the valueHeadin the above table, and use it injj, by
runningjj new 34014a67b0ddc859d95e17ffc71c1ae61aff5758. This will drop me
onto a new change after34014a67b0ddc859d95e17ffc71c1ae61aff5758, and then I
can usejj log -r ::@to see all the previous changes.

Again, I use the wonderfuljj editcommand, or perhaps I make new changes that
I thenjj squashinto the relevant changes – it all depends on the scope of
the change!

Once I’m done, I pushHEADto another specialrefspec, using
the patch’s full identifier:

git push rad HEAD:patches/c54883e5ffb1f8a99f432e3ac79c0b728cd0dab3
-f

We use-fif we are editing the changes since this will change the underlying
commits andgitwill reject this. Once again, this will open my$EDITORand
I will add a message about the changes that were made in this update.

This creates a new “revision” for the patch, preserving the older revisions.
So essentially, patches in Radicle are append-only. This makes it safe for us to
make edits to changes, marking them as mutable – the Git history will be
preserved!

#### Maintaining Patches

From the maintaining perspective, the flow starts off similar to updating, where
I would look up the patch that I want to merge. If I made the patch, things are
a bit easier because the Git objects are easily accessible and I can dojj newusing the commit. If I attempt to do this with a patch that came from another
contributor, then I may run into this issue:

$ jj new 7322e3ac61669ba6dbde16bb0f7d30edf1ee85ce

Error:
Revision `7322e3ac61669ba6dbde16bb0f7d30edf1ee85ce` doesn't exist

The way to do this instead, is to use the remote syntax and the specialpatchesreference:

$ jj new patches/3219ef871dd44c7ef51693f4aeba4c2c5c0c5c7b@rad
Working copy (@) now at:
oo
xzsqoy

eb
9e0803

(empty)

(no description set)

Parent commit (@-) :
s
wpyssrk

73
22e3ac

patches/3219ef871dd44c7ef51693f4aeba4c2c5c0c5c7b patches/3219ef871dd44c7ef51693f4aeba4c2c5c0c5c7b@rad
 |
node, cli: remove predefined bootstrap nodes

At this point, I can also look at what commits are in the patch viarad patch
show, or by usingjj log -r ::@. If they’re already on topmaster@rad, then
to merge the patch I can simplygit push rad master– and the remote helper
marks the patch as merged if the canonical reference ofmasteris update (a
topic for another time).

If the patch isn’t on top ofmaster@radthen I can rebase the changes usingjj rebase -d master@rad -r <base>::<head>to get the series of changes on top
of our latest. It’s then necessary to push a new revision to the patch so that
the patch can know it is being merged with the new commits – remember that I
rebased, so this changes the underlying commits.

We should update ourmasterbookmark, and this is where thetugalias comes
in. When I runjj tug, it figures out thatmasteris the closest bookmark
and pulls it up to the latest change that can be pushed. I can then push to
update the patch:

git push rad master:patches/3219ef871dd44c7ef51693f4aeba4c2c5c0c5c7b
-f

Here I’m usingmasterinstead ofHEAD– this gets around a little issue I’ve
been seeing for patches that I do not own, where the remote helper rejects the
push because it cannot resolveHEAD(a mystery left for another day).

Once the patch has been rebased, I can do the usualgit push rad masterto
update the canonical reference and have the patch marked as merged.

## Conclusion

And our adventure ends here. We dived into how Radicle works with Git, how
Jujutsu works Git, and how I use Jujutsu to have a branch-less flow in Radicle.
This is has been a dream to work with. This type of tooling feels like it
enables me a lot more when managing my changes and keeping a clean history. I
wasableto do this withgit rebase, but it felt like it got in the way more
than it enabled me – and I haven’t even touched on howconflictsare easy in Jujutsu!

There is plenty of room for improvements here, some things on my list are:

* Keeping track of Jujutsu change IDs in Radicle data, which is already being
looked at!
* Not needing to userad patch showto get metadata for managing patches, and
perhaps even bookmarking patch identifiers automatically.

Come help in discussion on ourZulip, and enjoy being Radicle 🌱👾
