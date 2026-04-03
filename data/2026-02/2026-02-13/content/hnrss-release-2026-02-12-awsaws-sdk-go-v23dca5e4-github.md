---
title: Release 2026-02-12 · aws/aws-sdk-go-v2@3dca5e4 · GitHub
url: https://github.com/aws/aws-sdk-go-v2/commit/3dca5e45d5ad05460b93410087833cbaa624754e
site_name: hnrss
content_file: hnrss-release-2026-02-12-awsaws-sdk-go-v23dca5e4-github
fetched_at: '2026-02-13T11:16:00.408677'
original_url: https://github.com/aws/aws-sdk-go-v2/commit/3dca5e45d5ad05460b93410087833cbaa624754e
date: '2026-02-13'
description: AWS SDK for the Go programming language. . Contribute to aws/aws-sdk-go-v2 development by creating an account on GitHub.
tags:
- hackernews
- hnrss
---

aws



/

aws-sdk-go-v2

Public

* NotificationsYou must be signed in to change notification settings
* Fork752
* Star3.5k




## File tree

Expand file tree
Collapse file tree

## 6fileschanged

+
12
-
22
lines changed
Open diff view settings
Filter options
* .changelog41575353444b40ffbf474f4155544f00.jsonb69903abaa7b45808c95754997de8be5.json
* 41575353444b40ffbf474f4155544f00.json
* b69903abaa7b45808c95754997de8be5.json
* CHANGELOG.md
* serviceec2CHANGELOG.mdgo_module_metadata.gointernal/integrationtestgo.mod
* ec2CHANGELOG.mdgo_module_metadata.go
* CHANGELOG.md
* go_module_metadata.go
* internal/integrationtestgo.mod
* go.mod
Expand file tree
Collapse file tree

## 6fileschanged

+
12
-
22
lines changed
Open diff view settings
Collapse file

### ‎.changelog/41575353444b40ffbf474f4155544f00.json‎

Copy file name to clipboard
Expand all lines: .changelog/41575353444b40ffbf474f4155544f00.json
-
12
Lines changed: 0 additions & 12 deletions

Load Diff
This file was deleted.
Collapse file

### ‎.changelog/b69903abaa7b45808c95754997de8be5.json‎

Copy file name to clipboard
Expand all lines: .changelog/b69903abaa7b45808c95754997de8be5.json
-
8
Lines changed: 0 additions & 8 deletions

Load Diff
This file was deleted.
Collapse file

### ‎CHANGELOG.md‎

Copy file name to clipboard
Expand all lines: CHANGELOG.md
+
6
Lines changed: 6 additions & 0 deletions
* Display the source diff
* Display the rich diff
Original file line number
Diff line number
Diff line change
@@ -1,3 +1,9 @@
1
+
# Release (2026-02-12)
2
+
3
+
## Module Highlights
4
+
* `github.com/aws/aws-sdk-go-v2/service/ec2`: [v1.288.0](service/ec2/CHANGELOG.md#v12880-2026-02-12)
5
+
 * **Feature**: Launching nested virtualization. This feature allows you to run nested VMs inside virtual (non-bare metal) EC2 instances.
6
+
1
7
# Release (2026-02-11)
2
8
3
9
## Module Highlights
Collapse file

### ‎service/ec2/CHANGELOG.md‎

Copy file name to clipboard
Expand all lines: service/ec2/CHANGELOG.md
+
4
Lines changed: 4 additions & 0 deletions
* Display the source diff
* Display the rich diff
Original file line number
Diff line number
Diff line change
@@ -1,3 +1,7 @@
1
+
#
v1.288.0 (2026-02-12)
2
+
3
+
*

**
Feature
**
: Launching nested virtualization. This feature allows you to run nested VMs inside virtual (non-bare metal) EC2 instances.
4
+
1
5
#
v1.287.0 (2026-02-11)
2
6
3
7
*

**
Feature
**
: R8i instances powered by custom Intel Xeon 6 processors available only on AWS with sustained all-core 3.9 GHz turbo frequency
Collapse file

### ‎service/ec2/go_module_metadata.go‎

Copy file name to clipboard
Expand all lines: service/ec2/go_module_metadata.go
+
1
-
1
Lines changed: 1 addition & 1 deletion

Load Diff
Some generated files are not rendered by default. Learn more about

customizing how changed files appear on GitHub.
Collapse file

### ‎service/internal/integrationtest/go.mod‎

Copy file name to clipboard
Expand all lines: service/internal/integrationtest/go.mod
+
1
-
1
Lines changed: 1 addition & 1 deletion
Original file line number
Diff line number
Diff line change
@@ -5,7 +5,7 @@ require (
5
5

github.com/aws/aws-sdk-go-v2/config

v1.32.7
6
6

github.com/aws/aws-sdk-go-v2/feature/s3/manager

v1.22.0
7
7

github.com/aws/aws-sdk-go-v2/service/dynamodb

v1.55.0
8
-

github.com/aws/aws-sdk-go-v2/service/ec2

v1.
287
.0
8
+

github.com/aws/aws-sdk-go-v2/service/ec2

v1.
288
.0
9
9

github.com/aws/aws-sdk-go-v2/service/lambda

v1.88.0
10
10

github.com/aws/aws-sdk-go-v2/service/s3

v1.96.0
11
11

github.com/aws/aws-sdk-go-v2/service/s3control

v1.68.0
