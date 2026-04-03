---
title: update README.md format and clarify state of the project · minio/minio@7aac2a2 · GitHub
url: https://github.com/minio/minio/commit/7aac2a2c5b7c882e68c1ce017d8256be2feea27f
site_name: hackernews_api
content_file: hackernews_api-update-readmemd-format-and-clarify-state-of-the-pr
fetched_at: '2026-02-14T06:00:13.304455'
original_url: https://github.com/minio/minio/commit/7aac2a2c5b7c882e68c1ce017d8256be2feea27f
author: psvmcc
date: '2026-02-13'
description: MinIO is a high-performance, S3 compatible object store, open sourced under GNU AGPLv3 license. - update README.md format and clarify state of the project · minio/minio@7aac2a2
tags:
- hackernews
- trending
---

This repository was archived by the owner on Feb 13, 2026. It is now read-only.


 minio



/

minio

Public archive

* NotificationsYou must be signed in to change notification settings
* Fork7k
* Star60.2k




## File tree

Expand file tree
Collapse file tree

## 1filechanged

+
10
-
13
lines changed
Open diff view settings
Filter options
* README.md
Expand file tree
Collapse file tree

## 1filechanged

+
10
-
13
lines changed
Open diff view settings
Collapse file

### ‎README.md‎

Copy file name to clipboard
Expand all lines: README.md
+
10
-
13
Lines changed: 10 additions & 13 deletions
* Display the source diff
* Display the rich diff
Original file line number
Diff line number
Diff line change
@@ -1,13 +1,9 @@
1
-
#
Maintenance Mode
2
-
3
-
**
This project is currently under maintenance and is not accepting new changes.
**
4
-
5
-
**
Alternate Options:
**
6
-
7
-
-

**
AIStor Free
**
: Fully featured, standalone version of AIStor for community use. Download a free license key from
[
Free license download
]
(
https://min.io/download
)
8
-
-

**
AIStor Enterprise
**
: Fully featured, Distributed version of AIStor for commercial enterprise use.
[
Subscription
]
(
https://www.min.io/pricing
)
9
-
10
-
Learn more about
[
subscription tiers
]
(
https://blog.min.io/introducing-new-subscription-tiers-for-minio-aistor-free-enterprise-lite-and-enterprise/
)
1
+
>
[
!NOTE
]
2
+
>
**
THIS REPOSITORY IS NO LONGER MAINTAINED.
**
3
+
>
4
+
>
**
Alternatives:
**
5
+
>
-

**
[
AIStor Free
]
(
https://min.io/download
)
**
 — Full-featured, standalone edition for community use (free license)
6
+
>
-

**
[
AIStor Enterprise
]
(
https://min.io/pricing
)
**
 — Distributed edition with commercial support
11
7
12
8
---
13
9
@@ -34,7 +30,7 @@ We designed MinIO as Open Source software for the Open Source software community
34
30
All usage of MinIO in your application stack requires validation against AGPLv3 obligations, which include but are not limited to the release of modified code to the community from which you have benefited. Any commercial/proprietary usage of the AGPLv3 software, including repackaging or reselling services/features, is done at your own risk.
35
31
36
32
The AGPLv3 provides no obligation by any party to support, maintain, or warranty the original or any modified work.
37
-
All support is provided on a best-effort basis through Github and our
[
Slack
]
(
https//slack.min.io
)
 channel, and any member of the community is welcome to contribute and assist others in their usage of the software.
33
+
All support is provided on a best-effort basis through Github and our
[
Slack
]
(
https
:
//slack.min.io
)
 channel, and any member of the community is welcome to contribute and assist others in their usage of the software.
38
34
39
35
MinIO
[
AIStor
]
(
https://www.min.io/product/aistor
)
 includes enterprise-grade support and licensing for workloads which require commercial or proprietary usage and production-level SLA/SLO-backed support. For more information,
[
reach out for a quote
]
(
https://min.io/pricing
)
.
40
36
@@ -54,6 +50,7 @@ See the sections below for detailed instructions on each method.
54
50
###
Legacy Binary Releases
55
51
56
52
Historical pre-compiled binary releases remain available for reference but are no longer maintained:
53
+
57
54
-
 GitHub Releases:
https://github.com/minio/minio/releases
58
55
-
 Direct downloads:
https://dl.min.io/server/minio/release/
59
56
@@ -72,7 +69,7 @@ You can alternatively run `go build` and use the `GOOS` and `GOARCH` environment
72
69
For example:
73
70
74
71
```
75
-
env GOOS=linux
GOARCh
=arm64 go build
72
+
env GOOS=linux
GOARCH
=arm64 go build
76
73
```
77
74
78
75
Start MinIO by running
`
minio server PATH
`
 where
`
PATH
`
 is any empty folder on your local filesystem.
@@ -94,7 +91,7 @@ For application developers, see <https://docs.min.io/enterprise/aistor-object-st
94
91
95
92
>
[
!NOTE
]
96
93
>
Production environments using compiled-from-source MinIO binaries do so at their own risk.
97
-
>
The AGPLv3 license provides no warranties nor
liabilites
 for any such usage.
94
+
>
The AGPLv3 license provides no warranties nor
liabilities
 for any such usage.
98
95
99
96
##
Build Docker Image
100
97
