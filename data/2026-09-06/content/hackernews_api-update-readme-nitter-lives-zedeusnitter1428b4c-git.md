---
title: Update README - Nitter lives · zedeus/nitter@1428b4c · GitHub
url: https://github.com/zedeus/nitter/commit/1428b4c2b4246f92a7e5b2673438e5fb39fcc4a3
site_name: hackernews_api
content_file: hackernews_api-update-readme-nitter-lives-zedeusnitter1428b4c-git
fetched_at: '2026-09-06T21:03:27.859205'
original_url: https://github.com/zedeus/nitter/commit/1428b4c2b4246f92a7e5b2673438e5fb39fcc4a3
author: zImPatrick
date: '2026-09-06'
description: Alternative Twitter front-end. Contribute to zedeus/nitter development by creating an account on GitHub.
tags:
- hackernews
- trending
---

zedeus

 

/

nitter

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork1.3k
* Star14.2k

 
 

## File tree

Expand file tree
Collapse file tree
Open diff view settings
Filter options
* .githubFUNDING.yml
* FUNDING.yml
* README.md
Expand file tree
Collapse file tree
Open diff view settings
Collapse file

### ‎.github/FUNDING.yml‎

Copy file name to clipboard
+
1
Lines changed: 1 addition & 0 deletions
Original file line number
Diff line number
Diff line change
@@ -1,3 +1,4 @@
1
1
github
: 
zedeus
2
2
liberapay
: 
zedeus
3
3
patreon
: 
nitter
4
+
ko_fi
: 
zedeus
Collapse file

### ‎README.md‎

Copy file name to clipboard
Expand all lines: README.md
+
24
-
17
Lines changed: 24 additions & 17 deletions
* Display the source diff
* Display the rich diff
Original file line number
Diff line number
Diff line change
@@ -1,42 +1,49 @@
1
1
# 
Nitter
2
2
3
3
> 
[
!NOTE
]
4
-
> 
On 24 August 2026 cease and desist letters were sent by X Corp. demanding a permanent takedown of Nitter instances and the project's repository.
4
+
> 
On 24 August 2026, cease and desist letters were sent by X Corp. demanding a permanent takedown of Nitter instances and the project's repository. 
\
5
+
> 
**
UPDATE:
**
 Following legal advice, the Nitter project will continue. More details will be announced soon.
5
6
6
7
A free and open source alternative Twitter front-end focused on privacy and
7
8
performance. 
\
8
9
Inspired by the 
[
Invidious
]
(
https://github.com/iv-org/invidious
)
 project.
9
10
10
-
## 
Donations
11
-
12
-
**
Liberapay
**
: 
https://liberapay.com/zedeus
<
br
>
13
-
**
Patreon
**
: 
https://patreon.com/nitter
<
br
>
14
-
**
Ko-fi
**
: 
https://ko-fi.com/zedeus
<
br
>
15
-
**
BTC
**
: bc1qpqpzjkcpgluhzf7x9yqe7jfe8gpfm5v08mdr55<
br
>
16
-
**
ETH
**
: 0x24a0DB59A923B588c7A5EBd0dBDFDD1bCe9c4460<
br
>
17
-
**
XMR
**
: 42hKayRoEAw4D6G6t8mQHPJHQcXqofjFuVfavqKeNMNUZfeJLJAcNU19i1bGdDvcdN6romiSscWGWJCczFLe9RFhM3d1zpL<
br
>
18
-
**
SOL
**
: FF5bheiD5AqPEdc3eyjymJ8AoMRF1hS78Ht6FiSZZF1t<
br
>
19
-
**
$Nitter
**
: 4fSxCKc91ELQYVdv3tmHW8R15KoALPwEngyoQe1Xpump<
br
>
20
-
**
ZEC
**
: u1vndfqtzyy6qkzhkapxelel7ams38wmfeccu3fdpy2wkuc4erxyjm8ncjhnyg747x6t0kf0faqhh2hxyplgaum08d2wnj4n7cyu9s6zhxkqw2aef4hgd4s6vh5hpqvfken98rg80kgtgn64ff70djy7s8f839z00hwhuzlcggvefhdlyszkvwy3c7yw623vw3rvar6q6evd3xcvveypt
11
+
[
![
Test Matrix
]
(
https://github.com/zedeus/nitter/workflows/Tests/badge.svg
)]
(
https://github.com/zedeus/nitter/actions/workflows/run-tests.yml
)
12
+
[
![
Test Matrix
]
(
https://github.com/zedeus/nitter/workflows/Docker/badge.svg
)]
(
https://github.com/zedeus/nitter/actions/workflows/build-docker.yml
)
13
+
[
![
License
]
(
https://img.shields.io/github/license/zedeus/nitter?style=flat
)]
(
#license
)
21
14
22
15
## 
Features
23
16
24
-
-
 No JavaScript or ads
17
+
-
 No JavaScript required
18
+
-
 Zero ads
25
19
-
 All requests go through the backend, client never talks to Twitter
26
20
-
 Prevents Twitter from tracking your IP or JavaScript fingerprint
27
21
-
 Uses Twitter's unofficial API (no developer account required)
28
22
-
 Lightweight (for 
[
@nim_lang
]
(
https://nitter.net/nim_lang
)
, 60KB vs 784KB from twitter.com)
29
-
-
 RSS feeds
23
+
-
 RSS feeds
 (instance-specific, often disabled due to abuse)
30
24
-
 Themes
31
25
-
 Mobile support (responsive design)
32
26
-
 AGPLv3 licensed, no proprietary instances permitted
33
27
34
28
## 
Roadmap
35
29
36
-
-
 Embeds
30
+
-
 
~~
Embeds
~~
 (see 
https://github.com/zedeus/nitter/wiki/Embeds-guide
)
37
31
-
 Account system with timeline support
38
32
-
 Archiving tweets/profiles
39
-
-
 Developer API
33
+
34
+
## 
Donations
35
+
36
+
[
![
GitHub Sponsors
]
(
https://img.shields.io/badge/GitHub%20Sponsors-EA4AAA?style=for-the-badge&logo=githubsponsors&logoColor=white
)]
(
https://github.com/sponsors/zedeus
)
37
+
[
![
Patreon
]
(
https://img.shields.io/badge/Patreon-FF424D?style=for-the-badge&logo=patreon&logoColor=white
)]
(
https://patreon.com/nitter
)
38
+
[
![
Liberapay
]
(
https://img.shields.io/badge/Liberapay-F6C915?style=for-the-badge&logo=liberapay&logoColor=black
)]
(
https://liberapay.com/zedeus
)
39
+
[
![
Ko-fi
]
(
https://img.shields.io/badge/Ko--fi-FF5E5B?style=for-the-badge&logo=kofi&logoColor=white
)]
(
https://ko-fi.com/zedeus
)
40
+
41
+
**
BTC
**
: bc1qpqpzjkcpgluhzf7x9yqe7jfe8gpfm5v08mdr55<
br
>
42
+
**
ETH
**
: 0x24a0DB59A923B588c7A5EBd0dBDFDD1bCe9c4460<
br
>
43
+
**
XMR
**
: 42hKayRoEAw4D6G6t8mQHPJHQcXqofjFuVfavqKeNMNUZfeJLJAcNU19i1bGdDvcdN6romiSscWGWJCczFLe9RFhM3d1zpL<
br
>
44
+
**
SOL
**
: FF5bheiD5AqPEdc3eyjymJ8AoMRF1hS78Ht6FiSZZF1t<
br
>
45
+
**
$Nitter
**
: 4fSxCKc91ELQYVdv3tmHW8R15KoALPwEngyoQe1Xpump<
br
>
46
+
**
ZEC
**
: u1vndfqtzyy6qkzhkapxelel7ams38wmfeccu3fdpy2wkuc4erxyjm8ncjhnyg747x6t0kf0faqhh2hxyplgaum08d2wnj4n7cyu9s6zhxkqw2aef4hgd4s6vh5hpqvfken98rg80kgtgn64ff70djy7s8f839z00hwhuzlcggvefhdlyszkvwy3c7yw623vw3rvar6q6evd3xcvveypt
40
47
41
48
## 
Resources
42
49
@@ -207,4 +214,4 @@ lines). If you're running the Docker image, you can do this:
207
214
Feel free to join our 
[
Matrix channel
]
(
https://matrix.to/#/#nitter:matrix.org
)
.
208
215
You can email me at 
zedeus@pm.me
 if you wish to contact me personally.
209
216
210
-
For legal inquiries, contact 
legal@poast.org
217
+
For legal inquiries
 and DMCA requests
, contact 
legal@poast.org