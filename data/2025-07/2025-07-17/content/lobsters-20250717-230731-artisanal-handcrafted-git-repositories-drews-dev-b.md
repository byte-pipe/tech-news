---
title: Artisanal Handcrafted Git Repositories | drew's dev blog
url: https://drew.silcock.dev/blog/artisanal-git/
site_name: lobsters
fetched_at: '2025-07-17T23:07:31.859394'
original_url: https://drew.silcock.dev/blog/artisanal-git/
date: '2025-07-17'
description: How to lovingly handcraft your own git repositories
tags: vcs
---

Back to blog






 July 16, 2025


•

 27 min read



# Artisanal Handcrafted Git Repositories




Table of Contents




There’s no love and care put into crafting our git repositories nowadays.

Let’s change that.

I’m going to talk about how to handmake your git repositories without using these silly git commands.

You might also learn a bit more about how git works under the hood during the process, or whatever.

If you’re so inclined, you might also take it as an opportunity to appreciate how the power of git comes not from the complexity of its code but from the simplicity and elegance of its design. I mean, if that’s your thing.

Git refers to the user-friendly commands as “porcelain” and to the internals as “plumbing”, so you can think of this as an introductory lesson in git plumbing. In fact, git has “plumbing” commands which we’re not even using, so this is more like an introductory course in git fluid dynamics. In other words, it’s pretty silly.

#

## Pre-requisites

I’m going to assume you are familiar with git and are comfortable in a shell environment, otherwise this probably won’t make much sense to you.

#

## Let’s get started

The first thing we’d do normally is rungit init, but where’s the care and attention in that? We’re going to do it the old-fashioned way, like the pilgrims of yore would’ve done.

Terminal window
1
$

mkdir

artisanal-git
2
$

cd

artisanal-git
3

4
# This is where git stores all the information for a repository, from branches to
5
# commits to objects.
6
$

mkdir

.git
7

8
# Git expects these folders to exist, but we don't need to add anything into them yet.
9
$

mkdir

-p

.git/hooks

.git/info

.git/objects/info

.git/objects/pack

.git/refs/heads

.git/refs/remotes

.git/refs/tags

.git/logs
10

11
# This is just a standard repo-specific config file – these are the default values on my
12
# machine.
13
$

cat

<<
EOF

>

.git/config
14
[core]
15

repositoryformatversion = 0
16

filemode = true
17

bare = false
18

logallrefupdates = true
19

ignorecase = true
20

precomposeunicode = true
21
EOF

Now we only have to add one more file before we’ve got a valid git repository, and that’s theHEAD. You might’ve come across this before –HEADjust means “what is your repository pointing to right now?”. It’s a text file and it’s either got a reference in (the normal state of a repository) or just a plain commit hash – this is what’s referred to as a “detached head” (sounds painful, I know).

We’re going to point git to our default branch, calledmain.

Terminal window
1
$

echo

"ref: refs/heads/main"

>

.git/HEAD

You might be thinking – wait a minute, where is thismainbranch? I’ve not created any branches yet. And you haven’t, but that’s fine because we don’t have any commits yet. We can rungit statusto check whether git is happy with our handiwork so far.

Terminal window
1
$

git

status
2
On

branch

main
3

4
No

commits

yet
5

6
nothing

to

commit
 (create/copy
files

and

use

"git add"

to

track
)

If you get the error “fatal: This operation must be run in a work tree”, it’s probably just because you’re running it from inside the.gitfolder, which won’t work. Just cd one level up and you should be good to go.

Nice! Now, let’s get committing.

#

## Content Addressable Storage

Before we start hand-crafting our commits, we need to spend a bit of time refining our craftwork by studying the lore.

First, we need to understand what an“object”is in git, what they are and how git stores them.

Git needs to store lots of things. If you create a commit in git, git then needs to store everything about the commit itself, including the commit description, which files it includes, who committed it, the timestamp, and the contents of the files.

All of these things are stored as “objects”. But what do these look like? Let’s take another repository which already has a bunch of data in it.

Terminal window
1
$

git

log

-1
2
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
3
commit

84eae65b6780129486768e6497736c38bfdf9b3d
 (HEAD -
>

main,

origin/main,

origin/HEAD
) ┃
4
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
5
Author:

Drew

Silcock

<redacted>
6
Date:

Mon

Sep

30

21:39:55

2024

+0100
7

8

Improve

py

3.13

graphs

and

add

extra

section

on

scaling.

This is the last commit in the repo for this blog, at the time of writing. We can see that the commit is identified by its SHA-1 hash,84eae65b(I can’t be bothered to type out the whole thing).

This is where things start to get clever – the way git stores all these things like commits, files, etc.1is not based on some location separate from the data itself like a filename or a key (which would require knowing this filename/key outside of the data itself, e.g. by querying a central listing) but based on the contents of the thing itself. Do a SHA-1 hash of the object and that is the “key” that you use to find the object on disk.

This is called Content Addressable Storage (CAS) or sometimes fixed-content storage and once you recognise it, you startseeing it all over the place. CAS and content addressing in general are used by, among other things:

* Docker layers
* InterPlanetary File System (IPFS)
* BitTorrent via Distributed Hash Tables (DHTs)
* Nix

A side bonus of using content addressable storage is that if you ever have duplicate files, you don’t need to store them twice – they’ll have the same hash so they’ll be stored in the same location.

#

### Commit objects

To find commit84eae65bwe need to look in.git/objects/84/eae65b6780129486768e6497736c38bfdf9b3d. The data is compressed using zlib so we have to pipe it into a decompressor (I’m usingpigzhere):

Terminal window
1
$

cat

.git/objects/84/eae65b6780129486768e6497736c38bfdf9b3d

|

pigz

-d
2
commit

1136tree

5a0be7720e65417e08034a64bc257bc56a60b4b3
3
parent

e345662c7d53408eb2638cf0fdbae442fe6b68f4
4
author

Drew

Silcock

<redacted>

1727728795

+0100
5
committer

Drew

Silcock

<redacted>

1727728795

+0100
6
gpgsig

-----BEGIN

PGP

SIGNATURE-----
7

8

iQIzBAABCAAdFiEEaZwozZ5d++BpkqZmtEW8+mMmNyAFAmb7DJsACgkQtEW8+mMm
9

NyAZeBAAs2I1rodxTBpOnFUgNnl5Slf2o03VZlc7kvbw2miCUP5CkO40REHzGXXE
10

K3sJSUhObttTrKr0GjUChcvzBZBKoigawP+h3IeY07whhhTcnNaBXjQqzpcl+G5A
11

ryEVkQXdCqVRWAk3I/6Z3hFlfUogzbxihGoEKvjyMZtmfy0di0WAOJ+PLlTIEwJJ
12

SQYcUaA7l01ocIWy85MezGJHZEpurcBjzu5nkYCMGRw85u9tXXqjzaYh6Fu7WVEH
13

rHmBO8tEFF/WcQC1FonVggrOQOAsssuaMxwxKV/p4HRxP9lHGmzFCGfbKAY1bQ82
14

2dWgROwMAp6jtvLSX6OLu6i0O3+m6NAwTtKcOFDU+Jae4h2m1GC3/8qDukhK7o+e
15

5LJCLAZPtTvpai43COLRnF9iteV15H267WOxpIvXqbMBwIFcaaHepFMLA0Y39Kr3
16

FHd1JAaaE6fiUe4rjNP5Wx6ZVLKdEYznjbxgxiRkr9dcemR5SUQtreHjaaLTo0E9
17

m6bEE1huZp+gu/dy9e7hgNORiwmkUP49r4/WPbNwwKrMxr5lD1ZwQk6DKEi6jAyq
18

BduJ4fdtamFlngnbJtoW0LHsdxROMwHkqs1Pz4zxpmeOZZEv0p0pzFhM30ta+YjQ
19

ogBAyoRGHAZG2cze5uI8Cg7fr1A+uTqGmBAXexYN+/ok4+Bf/5g
=
20

=gvSk
21

-----END

PGP

SIGNATURE-----
22

23
Improve

py

3.13

graphs

and

add

extra

section

on

scaling.

If we pipe this intohexylwe can see the hidden null byte:

Terminal window
1
$

cat

.git/objects/84/eae65b6780129486768e6497736c38bfdf9b3d

|

pigz

-d

|

hexyl
2
┌────────┬─────────────────────────┬─────────────────────────┬────────┬────────┐
3
│00000000│

63

6f

6d

6d

69

74

20

31

┊

31

33

36

00

74

72

65

65

│commit

1┊136⋄tree│
4
│00000010│

20

35

61

30

62

65

37

37

┊

32

30

65

36

35

34

31

37

│

5a0be77┊20e65417│
5
│00000020│

65

30

38

30

33

34

61

36

┊

34

62

63

32

35

37

62

63

│e08034a6┊4bc257bc│
6
│00000030│

35

36

61

36

30

62

34

62

┊

33

0a

70

61

72

65

6e

74

│56a60b4b┊3_parent│
7
│00000040│

20

65

33

34

35

36

36

32

┊

63

37

64

35

33

34

30

38

│

e345662┊c7d53408│
8
│00000050│

65

62

32

36

33

38

63

66

┊

30

66

64

62

61

65

34

34

│eb2638cf┊0fdbae44│
9
...

So this follows the formatcommit (content length)\x00(commit contents)which is the format used by all the other types of objects too.

#

### Tree objects

We can see the hash of another object here by looking at the first info after the null byte:tree 5a0be7720e65417e08034a64bc257bc56a60b4b3. This tells us that the “tree” object with hash5a0be772contains the files included in the commit.

Terminal window
1
$

cat

.git/objects/5a/0be7720e65417e08034a64bc257bc56a60b4b3

|

pigz

-d
2
tree

678100644

.gitignore�

H@�L�������BO��p�100644

.prettierignore�Y��Vt
$
��n!]-

]�100644

.prettierrc.mjs�2iY��n�
$3Q
%�w��40000

.vscode
3

3���i(�[�Ə��D��100644

LICENCE���+�����rW4�^�
;
��r100644

README.md]%��h�
4
~
n�
*
Q�w
5

�+�100644

TODO.txt��E+1�n�[��

��ڏ�100644

astro.config.mjs
(
6

��c�Xp����jl�5A40000

fonts�0�A�����'���y�}40000 images��[z��CY��9������100644 logo.svg���
7

i:L��6��
8
100644 package-lock.json�����,!���ԥ��1��100644 package.jsonH�jCi��� i�za�c;�b�40000 public�D�PD0en/�%1��0ư��40000 src�OF;�0� ���)
9
�a�100644 tsconfig.jso?�s����V�v 4ice>y⏎

We can clearly see that this contains some useful information like filenames and some 644s which smells of unix permissions/file modes, but it looks like a mixed binary-text format. If we look at the hex, we can see a bit clearer what’s going on:

Terminal window
1
$

cat

.git/objects/5a/0be7720e65417e08034a64bc257bc56a60b4b3

|

pigz

-d

|

hexyl
2
┌────────┬─────────────────────────┬─────────────────────────┬────────┬────────┐
3
│00000000│

74

72

65

65

20

36

37

38

┊

00

31

30

30

36

34

34

20

│tree

678┊⋄100644

│
4
│00000010│

2e

67

69

74

69

67

6e

6f

┊

72

65

00

d6

20

48

19

40

│.gitigno┊re⋄×

H•@│
5
│00000020│

d7

4c

de

f6

ff

ba

be

c0

┊

d2

42

4f

a7

b5

70

f6

31

│×L××××××┊×BO××p×1│
6
│00000030│

30

30

36

34

34

20

2e

70

┊

72

65

74

74

69

65

72

69

│00644

.p┊rettieri│
7
│00000040│

67

6e

6f

72

65

00

dd

59

┊

c0

f4

8e

56

74

24

ef

9b

│gnore⋄×Y┊×××Vt
$
××│
8
│00000050│

e7

6e

21

1d

5d

2d

20

5d

┊

e2

80

31

30

30

36

34

34

│×n!•]-

]┊××100644│
9
│00000060│

20

2e

70

72

65

74

74

69

┊

65

72

72

63

2e

6d

6a

73

│

.pretti┊errc.mjs│
10
│00000070│

00

b8

32

69

59

18

96

10

┊

b9

6e

eb

24

33

51

25

89

│⋄×2iY•×•┊×n×
$3Q
%×│
11
│00000080│

77

04

02

b4

eb

34

30

30

┊

30

30

20

2e

76

73

63

6f

│w••××400┊00

.vsco│
12
│00000090│

64

65

00

0c

33

c7

c3

c0

┊

69

28

c9

5b

e8

c6

8f

9f

│de⋄_3×××┊i
(
×[××××│
13
│000000a0│

15

a5

08

c8

44

a3

dc

31

┊

30

30

36

34

34

20

4c

49

│•×•×D××1┊00644

LI│
14
│000000b0│

43

45

4e

43

45

00

e2

18

┊

cd

e0

2b

a8

bf

d9

ea

c7

│CENCE⋄×•┊××+×××××│
15
│000000c0│

72

57

34

f4

5e

95

3b

b7

┊

87

72

31

30

30

36

34

34

│rW4×^×
;
×┊×r100644│
16
│000000d0│

20

52

45

41

44

4d

45

2e

┊

6d

64

00

5d

25

dd

e9

68

│

README.┊md⋄]%××h│
17
│000000e0│

b1

0a

7e

6e

a3

2a

51

a7

┊

14

77

0c

c8

2b

06

b0

31

│×_~n×
*
Q×┊•w_×+•×1│
18
│000000f0│

30

30

36

34

34

20

54

4f

┊

44

4f

2e

74

78

74

00

be

│00644

TO┊DO.txt⋄×│
19
│00000100│

1c

e0

45

2b

31

bd

6e

fd

┊

5b

a2

e3

9f

14

09

e9

e8

│•×E+1×n×┊[×××•_××│
20
│00000110│

da

8f

a0

31

30

30

36

34

┊

34

20

61

73

74

72

6f

2e

│×××10064┊4

astro.│
21
│00000120│

63

6f

6e

66

69

67

2e

6d

┊

6a

73

00

28

0c

93

c5

63

│config.m┊js⋄
(
_××c│
22
│00000130│

bd

58

70

16

16

b0

e6

1e

┊

f9

ab

6a

6c

ef

35

41

34

│×Xp••××•┊××jl×5A4│
23
│00000140│

30

30

30

30

20

66

6f

6e

┊

74

73

00

ef

30

1e

e8

41

│0000

fon┊ts⋄×0•×A│
24
│00000150│

8d

c7

18

d7

c1

16

ed

27

┊

1c

8d

b6

a4

79

d0

7d

34

│××•××•×'┊•×××y×}4│
25
│00000160│ 30 30 30 30 20 69 6d 61 ┊ 67 65 73 00 1c 10 b7 b5 │0000 ima┊ges⋄••××│
26
│00000170│ 5b 7a 99 9c 43 59 18 e7 ┊ d9 39 fa 8f c8 ff d2 ca │[z××CY•×┊×9××××××│
27
│00000180│ 31 30 30 36 34 34 20 6c ┊ 6f 67 6f 2e 73 76 67 00 │100644 l┊ogo.svg⋄│
28
│00000190│ 95 07 b5 d8 0b 69 3a 4c ┊ 96 eb 06 36 b6 a7 0b be │×•××•i:L┊××•6××•×│
29
│000001a0│ a6 83 29 0d 31 30 30 36 ┊ 34 34 20 70 61 63 6b 61 │××)_1006┊44 packa│
30
│000001b0│ 67 65 2d 6c 6f 63 6b 2e ┊ 6a 73 6f 6e 00 9e 8f bc │ge-lock.┊json⋄×××│
31
│000001c0│ b0 d9 7f 11 2c 21 f7 a9 ┊ 8e d4 a5 be d8 31 10 86 │××••,!××┊×××××1•×│
32
│000001d0│ e4 31 30 30 36 34 34 20 ┊ 70 61 63 6b 61 67 65 2e │×100644 ┊package.│
33
│000001e0│ 6a 73 6f 6e 00 48 97 6a ┊ 43 69 f1 f4 e4 20 69 91 │json⋄H×j┊Ci××× i×│
34
│000001f0│ 02 7a 61 ec 63 3b 80 62 ┊ b9 34 30 30 30 30 20 70 │•za×c;×b┊×40000 p│
35
│00000200│ 75 62 6c 69 63 00 b0 44 ┊ d0 50 44 17 30 65 6e 2f │ublic⋄×D┊×PD•0en/│
36
│00000210│ 90 25 31 97 d1 30 c6 b0 ┊ 90 a8 34 30 30 30 30 20 │×%1××0××┊××40000 │
37
│00000220│ 73 72 63 00 cb 4f 46 3b ┊ b9 02 30 0e 8d 0a aa d6 │src⋄×OF;┊×•0•×_××│
38
│00000230│ 84 03 44 c6 40 2d b9 5d ┊ 31 30 30 36 34 34 20 74 │×•D×@-×]┊100644 t│
39
│00000240│ 61 69 6c 77 69 6e 64 2e ┊ 63 6f 6e 66 69 67 2e 6d │ailwind.┊config.m│
40
│00000250│ 6a 73 00 6b 3c 62 76 4e ┊ 97 2a f4 50 e1 e4 3d d8 │js⋄k<bvN┊×*×P××=×│
41
│00000260│ d6 b9 35 5f b8 07 f2 34 ┊ 30 30 30 30 20 74 69 6e │××5_×•×4┊0000 tin│
42
│00000270│ 61 00 60 6f b2 72 1f d5 ┊ df 74 c9 81 c1 f6 36 42 │a⋄`o×r•×┊×t××××6B│
43
│00000280│ 38 23 0d d0 61 ae 31 30 ┊ 30 36 34 34 20 74 73 63 │8#_×a×10┊0644 tsc│
44
│00000290│ 6f 6e 66 69 67 2e 6a 73 ┊ 6f 6e 00 08 3f fe 73 de │onfig.js┊on⋄•?×s×│
45
│000002a0│ c8 f0 8b 56 e3 76 20 00 ┊ 05 34 69 63 65 3e 79 │×××V×v ⋄┊•4ice>y │
46
└────────┴─────────────────────────┴─────────────────────────┴────────┴────────┘

Ok maybe it’s not that much clearer, but it’s obvious once I explain it:

1
(file mode) (file name)\x00(binary hash)(file mode) (file name)\x00(binary hash)...

The file mode is in plaintext so here we see that the file.gitignorehas mode100644which (according to Greg Bacon on StackOverflow) means a regular file with permissions 644. (Side note: I don’t know what git does on Windows where unix file modes and stat don’t exist, leave a comment below if you do!)

This also tells us that the hash of the.gitignorefile isd6 20 48 19 40 d7 4c de f6 ff ba be c0 d2 42 4f a7 b5 70 f6– we don’t need a null terminator at the end of this because SHA-1 hashes are always precisely 20 bytes, so we can go straight into the file mode of the next file in the tree without any bytes separating the two files in the tree.

Because git uses this content-addressing system, we can then look up the file itself using this hash:

Terminal window
1
$

cat

.git/objects/d6/20481940d74cdef6ffbabec0d2424fa7b570f6
|
pigz

-d
2
blob

274.vscode
3

4
# build output
5
dist/
6

7
# generated types
8
.astro/
9

10
# dependencies
11
node_modules/
12

13
# logs
14
npm-debug.log*
15
yarn-debug.log*
16
yarn-error.log*
17
pnpm-debug.log*
18

19

20
# environment variables
21
.env
22
.env.production
23

24
# macOS-specific files
25
.DS_Store
26

27
# jetbrains setting folder
28
.idea/

Again, we see the object type, in this case “blob” indicating file contents, followed by the length of the file contents, followed by a null byte (not shown by terminal here), followed by the file contents (and a very exciting example it is).

There’s actually some helper commands, which git calls “plumbing” commands, for printing out object info:git cat-file -p (sha-1 hash)will pretty print the object contents (the-tflag will display the object type and-swill display the size). We haven’t covered annotated tags, which are also objects, but they’re quite similar to commits and not massively interesting for our discussion. Lightweight tags (without messages) are just references to commits hashes, not objects, so are stored in therefs/folder alongside branches.

Neat!

#

### But wait, there’s no diffs/delta here! I thought commits were showing changes to files?

Commits do not store deltas or differences between files but rather store the whole before and the whole after. This was actually one of the big selling points of git compared to competing version control systems, back before git became the de-facto standard2.

What git does when you dogit diffis get the before contents, get the after contents, then run a differ on these two versions to display to the user. You can even change the differ that git uses. Personally, I usedelta, but I’ve heard good things aboutdifftasticanddiff-so-fancy.

You might be thinking that this will surely make repositories mahoosive, right? We’ll get onto that in just a second.

#

### What’s up with the first two letters of the hash being the folder?

Good question. Apparently, there are some filesystems which don’t allow you to have more than a certain n# files in any particular directory, and others which use a sequential scan to find a file within a directory, which wouldn’t be good if you were trying to commit to the Linux kernel, which has some~4.5 million objectsor so.

SHA-1 hashes are well distributed so you can expect as many hashes starting with00as1eas8fand every other possible combination. Git takes advantage of this by checking whether there are 27 or more files in any of these subdirectories3. If so, it would indicate that there are more than 6,700 objects in total, which tells git that it’s time to “pack” those “loose” objects up into packfiles, to save on space.

#

### Time to pack it up

If you look in the.git/objectsfolder, there are a couple of non-hex folders that you might be wondering about. One is calledinfo/and one is calledpack/.

The “info” folder is super interesting and not something I encountered before researching for this blog post – turns out multiple git repositories can share a single object database to reduce on storage size which is pretty neat. I think the “info” folder is only used for very specific, niche use cases to be honest.

The “pack” folder is very commonly used, and it’s where git puts its packfiles. What’s a packfile, I hear you ask? Well, as I said above, when git decides that there are too many “loose” objects in the.git/objectsfolder (apparently,6,700 by default), it pulls multiple objects together into a single packfile. This allows multiple objects to be compressed together within the same file, improving compression ratios.

This does introduce the problem of how to find objects once they’ve been packed up. Git supports per-pack index files and also multi-index files, which is a more recent introduction that allows using a single index for all your packs. If you’re using multiple pack index files, you can try some tactics like looking at the most recently changed packfiles first as potential speedups, but ultimately you do have to search through all the packfile index files to find your object.

At this point you might have a couple of questions:

* How does this stop repositories from getting mahoosive? Sure, it’s a bit better compressed, but that won’t make that much of a difference.
* If git stores the complete version of every file, why does git say “resolving deltas…” when I clone a repository?

The answer is that git does store deltas in the packfiles. In fact, git usesvarious strange heuristicsto determine how to pack objects as efficiently as possible, both in terms of the deltas and in terms of the compression (which is done after the delta creation).

In particular, git does not store the chronologically “first” version of a file as the base and then add deltas on top of that. It doesn’t even care whether two objects represent the same or not – git looks at which objects are similar and determines which would be the most optimal base for the deltas, regardless of whether the similar objects even represent the same file.

It is this clever but slightly magical heuristic-based packfile creation system that keeps the size of git repositories down. It also helps that git throws out “unreachable” objects so that your repository only has what you need it to have.

#

## Taking the trash out

It’s worth talking a bit more about git’s garbage collection, i.e. the removal of unreachable objects, because this is a bit of knowledge that may actually save your proverbial bacon one day.

If you accidentally delete a branch that has a bunch of important commits in, you might be thinking “Egad, I’ve lost all my precious files! Woe!”, but don’t worry – git does not in fact delete all your commits and files when you delete the branch.

In fact, git keeps a log of all the actions you do on each branch and HEAD in the folder.git/logs/. All the actions you do on HEAD are in.git/logs/HEADwhile changes to references like branches are in e.g..git/logs/refs/heads/main. Each log file contains one line per “action”, e.g. making a commit, pulling from a remote, merging a branch, checking out another branch (checkouts will only be in HEAD log, not individual branches), etc.

Because these logs contain information about actions performed on each reference, they’re called reference logs or just reflogs for short.

Reflog entries are kept for90 days(configurable asgc.reflogExpire) and while a commit is referenced from the reflog, it is still considered “reachable” by git. Even once an item is truly unreachable, i.e. it’s been removed from the reflog, git still gives it2 weeks(configurable asgc.pruneExpire) before it garbage collects it as a grace period. This means that you can often still recover your work using either the manual methods we describe here or by using thegit reflogcommands followed bygit checkoutorgit reset --hard.

For more details on reflog and more, check out theOh Shit, Git! zine from Julia Evans.

Beware, however! Logref files are local to your individual repository – if you delete your.gitfolder or clone afresh, it will not contain your deleted branch.

#

## Creating our first commit

Now that we understand git objects, we can make our first commit.

Terminal window
1
$

echo

-e

"Has spring come indeed?\nOn that nameless mountain lie\nThin layers of mist.\n\n - Matsuo Bashō"

>

haiku.txt
2

3
$

git

status
4
On

branch

main
5

6
No

commits

yet
7

8
Untracked

files:
9

(
use

"git add <file>..."

to

include

in

what

will

be

committed
)
10

haiku.txt
11

12
nothing

added

to

commit

but

untracked

files

present
 (use
"git add"

to

track
)

Okay, so normally we would need to add the file to our staging area before we can commit it. But we don’t really need to do that because we’re handcrafting our artisanal repository. Plus, the index is a binary file located in.git/indexwhich makes it a) not massively interesting and b) not particularly easy to manipulate using just command line tools.

If you’re interested in learning more about the index file format and enjoy sitting down with a cup of hot mocha and an internal documentation page describing binary file formats, take a look over at the git docs reference page on the index format:https://git-scm.com/docs/index-format[^me-disclaimer].

#

### Creating our file blob

Okay, so we need to construct the commit object from scratch. Let’s start with the blob, then use that to construct the tree, then we can build the commit object from that tree.

Terminal window
1
$

cat

haiku.txt

|

wc

-c
2

94
3

4
# Note: SHA-1 is done before applying zlib compression.
5
$

echo

-e

"blob 94\x00$(
cat
 haiku.txt)"

|

sha1sum
6
e5d59773e77daf9f9b9129781ca77d475a451831

-
7

8
$

mkdir

-p

.git/objects/e5
9

10
$

echo

-e

"blob 94\x00$(
cat
 haiku.txt)"

|

pigz

-z

>

.git/objects/e5/d59773e77daf9f9b9129781ca77d475a451831
11

12
# Check whether we messed it up yet
13
$

git

cat-file

-p

e5d59773e77daf9f9b9129781ca77d475a451831
14
Has

spring

come

indeed?
15
On

that

nameless

mountain

lie
16
Thin

layers

of

mist.
17

18

-

Matsuo

Bashō
19

20
# Nice!

#

### Creating our tree blob

Phew, so now let’s use that file blob object to create a tree blob with just that file in it, using file mode 100644 again:

Terminal window
1
# Let's make a helper function for the hex to bytes conversion.
2
# Note: I use fish, where this works but you need to add another `\\` before the `x&` in
3
# the sed command.
4
$

function

hex-to-bytes
()
{

printf

"$(
printf
 "
$1
"
|

sed
 's/../\\x&/g')"
; }

Note for Fish shell users: yourhex-to-bytes()function will look like this:

Terminal window
1
function

hex-to-bytes;
 printf
"$(
printf
 "
$argv
[1]"
|

sed
 's/../\\\\x&/g')"
;
end

Back to creating our tree object:

Terminal window
1
$

printf

"100644 haiku.txt\x00$(
hex-to-bytes
 e5d59773e77daf9f9b9129781ca77d475a451831)"

|

hexyl
2
┌────────┬─────────────────────────┬─────────────────────────┬────────┬────────┐
3
│00000000│

31

30

30

36

34

34

20

68

┊

61

69

6b

75

2e

74

78

74

│100644

h┊aiku.txt│
4
│00000010│

00

e5

d5

97

73

e7

7d

af

┊

9f

9b

91

29

78

1c

a7

7d

│⋄×××s×}×┊×××
)x•×}│
5
│00000020│

47

5a

45

18

31

0a

┊

│GZE•1_

┊

│
6
└────────┴─────────────────────────┴─────────────────────────┴────────┴────────┘
7

8
# Looks good so far.
9
$

printf

"100644 haiku.txt\x00$(
hex-to-bytes
 e5d59773e77daf9f9b9129781ca77d475a451831)"

|

wc

-c
10

37
11

12
$

printf

"tree 37\x00100644 haiku.txt\x00$(
hex-to-bytes
 e5d59773e77daf9f9b9129781ca77d475a451831)"

|

sha1sum
13
4aff48f6390a65b88d343ea5d23c03007646b5c2

-
14

15
$

mkdir

-p

.git/objects/4a
16

17
$

printf

"tree 37\x00100644 haiku.txt\x00$(
hex-to-bytes
 e5d59773e77daf9f9b9129781ca77d475a451831)"

|

pigz

-z

>

.git/objects/4a/ff48f6390a65b88d343ea5d23c03007646b5c2

#

### Creating our commit

Now that we have our tree, we can create the commit! (Finally…)

Terminal window
1
# This will vary on your machine, obviously
2
$

date

+'%s %z'
3
1752659127

+0100
4

5
# Feel free to replace with your name/email and timestamp/timezone – just bear in mind
6
# that the SHA-1 hash will be different.
7
# Note: Commits usually have a "parent" field but as this is our first commit, it has no
8
# parent.
9
$

cat

<<
EOF

>

/tmp/my-commit
10
tree 4aff48f6390a65b88d343ea5d23c03007646b5c2
11
author Drew Silcock <redacted> 1752659127 +0100
12
committer Drew Silcock <redacted> 1752659127 +0100
13

14
Initial artisanal commit.
15
EOF
16

17
# Optional – I like to sign my commits.
18
$

cat

/tmp/my-commit

|

gpg

--armor

--detach-sign
19
-----BEGIN

PGP

SIGNATURE-----
20

21
iQIzBAABCAAdFiEEaZwozZ5d++BpkqZmtEW8+mMmNyAFAmh3diEACgkQtEW8+mMm
22
NyDomRAAvWYhK9Eg+ZjmChFR2ZX9bB/KZH+H3ksziy2UHp8LiaHgOb3Ira02rpSm
23
LvVQjxmgurzYBd3nl1e/8E+V3TH1kGOzmvaoCcjJkSUj6togvD7+eImulc1/xkri
24
q/qqPXxvj2UoRMbSc4cVy/8SZ/MTxNWtCJsuFRe6iKLRiqk67h3PY+gvebCuJteC
25
TevKxWV/ra+NRX2Q0w52SEUpGTVcnnxYPyMEi28Kmd9VZUsOvuC43RMm/p7u/eiC
26
kAzJ3GKN4oQvN/3Xz8akb09VX66M/xbMYNv/J0pbSdeIGofMDfLA3oKeZzhrvUVf
27
zsrpiJ9kq2CTGIuZMJZQvPc8aEEMbr/PAHgSnSTicayon7JLoi5aaoyhZLCD+pgK
28
Sd6OMMjrKs61UL2qxelVVde2tZumfOL4GmILrhxQgqZbZsdfDUvPMee9yFkEZVam
29
re8ekkUlYmlmckTqJ0yQ7VTLYhdxPN+0DRynuiKKQaQlsCHhQi2MTYEn9l+mfbrO
30
7gUAe697+kDwo2VECs4Z7wtPG9F+kGNFpsC0CnGMWjKRR8ZBV9BBiLyc/SZgNd9Q
31
MZLQWPPvnMw0YlS59rHbUk3VwebxBKx8vX2WBt1NPFtmzkFRr73yL+e69JczspoM
32
t6FRuXH0bTtF+uVf7qD0saFXCC9lphLYFe5PuyzpIKwWbazGDFA
=
33
=rE6v
34
-----END

PGP

SIGNATURE-----
35

36
# We need to insert this signature into the commit in the format `gpgsig <signature>`.
37
# The single space at the start of each line is important.
38
# NOTE: My auto-formatter is removing the whitespace on the line after "BEGIN PGP
39
# SIGNATURE" – it should have a single space. You need that single space.
40
$

cat

<<
EOF

>

/tmp/my-commit-signed
41
tree 4aff48f6390a65b88d343ea5d23c03007646b5c2
42
author Drew Silcock <redacted> 1752659127 +0100
43
committer Drew Silcock <redacted> 1752659127 +0100
44
gpgsig -----BEGIN PGP SIGNATURE-----
45

46

iQIzBAABCAAdFiEEaZwozZ5d++BpkqZmtEW8+mMmNyAFAmh3diEACgkQtEW8+mMm
47

NyDomRAAvWYhK9Eg+ZjmChFR2ZX9bB/KZH+H3ksziy2UHp8LiaHgOb3Ira02rpSm
48

LvVQjxmgurzYBd3nl1e/8E+V3TH1kGOzmvaoCcjJkSUj6togvD7+eImulc1/xkri
49

q/qqPXxvj2UoRMbSc4cVy/8SZ/MTxNWtCJsuFRe6iKLRiqk67h3PY+gvebCuJteC
50

TevKxWV/ra+NRX2Q0w52SEUpGTVcnnxYPyMEi28Kmd9VZUsOvuC43RMm/p7u/eiC
51

kAzJ3GKN4oQvN/3Xz8akb09VX66M/xbMYNv/J0pbSdeIGofMDfLA3oKeZzhrvUVf
52

zsrpiJ9kq2CTGIuZMJZQvPc8aEEMbr/PAHgSnSTicayon7JLoi5aaoyhZLCD+pgK
53

Sd6OMMjrKs61UL2qxelVVde2tZumfOL4GmILrhxQgqZbZsdfDUvPMee9yFkEZVam
54

re8ekkUlYmlmckTqJ0yQ7VTLYhdxPN+0DRynuiKKQaQlsCHhQi2MTYEn9l+mfbrO
55

7gUAe697+kDwo2VECs4Z7wtPG9F+kGNFpsC0CnGMWjKRR8ZBV9BBiLyc/SZgNd9Q
56

MZLQWPPvnMw0YlS59rHbUk3VwebxBKx8vX2WBt1NPFtmzkFRr73yL+e69JczspoM
57

t6FRuXH0bTtF+uVf7qD0saFXCC9lphLYFe5PuyzpIKwWbazGDFA=
58

=rE6v
59

-----END PGP SIGNATURE-----
60

61
Initial artisanal commit.
62
EOF
63

64
# Now we're ready to add the commit as an object into git's loose object storage.
65
$

cat

/tmp/my-commit-signed

|

wc

-c
66

1027
67

68
$

echo

-e

"commit 1027\x00$(
cat
 /tmp/my-commit-signed)"

|

sha1sum
69
d62016426c1b7b4125d47bad267aeaaa78bb817c

-
70

71
$

mkdir

-p

.git/objects/d6
72

73
$

echo

-e

"commit 1027\x00$(
cat
 /tmp/my-commit-signed)"

|

pigz

-z

>

.git/objects/d6/2016426c1b7b4125d47bad267aeaaa78bb817c

Okay, so now we’ve created our commit, but we haven’t told git that our main branch points to this commit yet. That’s fine, we just need to create the main branch reference file.

#

### Okay, but what is a reference?

Well, an object is something that has data within it – it has a type and size and gets stored in.git/objectsas either loose or packed files. A reference is just a hash – no contents. References live in.git/refsand there are 3 common types:

* local branches, that live in.git/refs/heads/, e.g..git/refs/heads/mainfor the “main” branch
* remote branches, that live in.git/refs/remotes, e.g..git/refs/remotes/origin/mainfor the “main” branch in the remote called “origin”
* lightweight tags, that live in.git/refs/tags, e.g..git/refs/tags/v1.2.3for the “v1.2.3” tag (as mentioned before, annotated tags are objects because they contain messages).

When you dogit fetch, git checks the refs on the server to see whether they match the ones you’ve got in your.git/refs/remotesfolder, and updates your local folder accordingly. When git saysYour branch is up to date with 'origin/main'., it’s just saying that your local branch has the same reference in it than the remote branch, i.e..git/refs/heads/mainis identical to.git/refs/remotes/origin/main.

So what’s in one of these reference files? It’s just a commit hash! We already know our commit hash so let’s make ourmainbranch and point it to our artisanally created commit:

Terminal window
1
echo

"d62016426c1b7b4125d47bad267aeaaa78bb817c"

>

.git/refs/heads/main

#

### Checking our work

We can use our good-old porcelain commands to check our handiwork:

Terminal window
1
$

git

status
2
On

branch

main
3
nothing

to

commit,

working

tree

clean
4

5
$

git

branch
6
*
 main
7

8
$

git

log

--show-signature
9
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
10
commit

d62016426c1b7b4125d47bad267aeaaa78bb817c
 (HEAD -
>

main
) ┃
11
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
12
gpg:

Signature

made

Wed

16

Jul

10:51:29

2025

BST
13
gpg:

using

RSA

key

699C28CD9E5DFBE06992A666B445BCFA63263720
14
gpg:

Good

signature

from

"Drew Silcock <redacted>"
 [unknown]
15
gpg:

WARNING:

This

key

is

not

certified

with

a

trusted

signature!
16
gpg:

There

is

no

indication

that

the

signature

belongs

to

the

owner.
17
Primary

key

fingerprint:

699C

28CD

9E5D

FBE0

6992

A666

B445

BCFA

6326

3720
18
Author:

Drew

Silcock

<redacted>
19
Date:

Wed

Jul

16

10:45:27

2025

+0100
20

21

Initial

artisanal

commit.

Nice! We did it 🎉🎊

#

## Troubleshooting

If you get stuck with any of these points or get an error likeerror: bad tree object HEAD, try runninggit fsck --fulland it’s likely to tell you what’s gone wrong.

#

## Future Topics

It’s taken long enough to get to this point, but there’s a bunch of really interesting stuff that we didn’t have a chance to talk about – leave a comment, send me an email or shout into the wind which of the following you’d like to hear in a follow-up post:

* Stashes – how do they work? (Spoiler: they’re basically just commits)
* Reflog – I want to know more about how I can use the hidden power of the reflog to bring my precious files back from the dead.
* Packfile format and indices – I want to hear more about these packfiles and how git looks through them.
* Index file format – I am deeply upset that you skipped over this and demand a full blog post covering the binary format in full detail bit-by-bit, otherwise I will be seeking legal action.
* Networking – how does git communicate with the server? What’s the actual on-the-wire difference between usinghttps://github.com/...vs.[email protected]:/...vs.[email protected]:.... I actually have no idea about this so it’d be interesting to explore.

#

## Conclusion

While it was fun to learn how all these internals work, it’s not a good idea to do this in an actual repository – you will break things, and it will make you sad.

Hopefully, you found this interesting. To be honest, if you make it this far, you either a) skipped over the rest to see whether the conclusion said anything interesting (sorry to disappoint) or b) are the kind of person who reads all the way through highly technical articles about artisanal hand-crafted git repositories. Either way, I hope you enjoyed the read and maybe even learned something.

If there’s one thing to take away from this, it is the elegance of the design of git, and how it’s actually not that complicated once you understand the underlying file formats. Yes, I know there’s rebases and reflogs and all these more complicated things but git is not magic, and implementing a git clone (pun intended) from scratch in a language of your choice actually wouldn’t be that hard! At least, if you ignore the more complex things.

#

## Updates

* 2025-07-17:Added more details about packfiles, garbage collection and reflog.

#

## Further reading

The main inspiration for this was reading Julia Evans’ blog posts about git, so if you found this interesting, check our her posts about git. Then check out all the others too, they’re all good.

* Julia Evans – Inside .git –https://jvns.ca/blog/2024/01/26/inside-git
* Julia Evans – In a git repository, where do your files live? –https://jvns.ca/blog/2023/09/14/in-a-git-repository—where-do-your-files-live-/
* Git Reference Documentation – The Git index file has the following format –https://git-scm.com/docs/index-format
* Unpacking Git packfiles –https://codewords.recurse.com/issues/three/unpacking-git-packfiles
* Abin Simon (@meain) – What is in that .git directory? –https://blog.meain.io/2023/what-is-in-dot-git/
* Dulwich Project Documentation – Git File format –https://www.samba.org/~jelmer/dulwich/docs/tutorial/file-format.html

#

## Footnotes

1. But not everything.↩
2. Some people still use Perforce and Mercurial and whatnot, I know. Perforce was still popular in game dev last time I was there (which was a while ago now).↩
3. Given SHA-1 is well distributed, git just picks one folder to check to determine how many loose objects are in it.Junio Hamano chose folder17/. Don’t ask me why. Maybe it’s his favourite hexadecimal number?↩









Everything you need to know about Python 3.13 – JIT and GIL went up the hill
