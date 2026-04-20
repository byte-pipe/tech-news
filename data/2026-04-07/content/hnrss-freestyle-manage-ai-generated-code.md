---
title: Freestyle - Manage AI-Generated Code
url: https://www.freestyle.sh/
site_name: hnrss
content_file: hnrss-freestyle-manage-ai-generated-code
fetched_at: '2026-04-07T11:23:36.621431'
original_url: https://www.freestyle.sh/
date: '2026-04-06'
description: Git, VMs, deployments, and execution — unified infrastructure for code you didn't write. The platform for AI app builders and workflow engines.
tags:
- hackernews
- hnrss
---

Freestyle
Products
Pricing
Docs
↗
Sign In

# Sandboxes forCoding Agents

Get Started
View Docs
App Builder
Background Agent
Review Bot
AI Assistant
1
// Like Lovable, Bolt, V0

2
import

{
 freestyle
,

VmSpec

}

from

"freestyle-sandboxes"
;

3
import

{

VmBun

}

from

"@freestyle-sh/with-bun"
;

4
import

{

VmDevServer

}

from

"@freestyle-sh/with-dev-server"
;

5

6
// Create repo from template

7
const

{
 repoId
}

=

await
 freestyle
.
git
.
repos
.
create
(
{

...

}
)
;

8

9
const

{
 vm
}

=

await
 freestyle
.
vms
.
create
(
{

10

with
:

{

11
 devServer
:

new

VmDevServer
(
{

12
 devCommand
:

"bun run dev"
,

13
 runtime
:

new

VmBun
(
)
,

14
 repo
:
 repoId

15

}
)
,

16

}
,

17
}
)
;
1
// Like Devin, Cursor Agent

2
import

{
 freestyle
,

VmSpec

}

from

"freestyle-sandboxes"
;

3
import

{

VmBun

}

from

"@freestyle-sh/with-bun"
;

4

5
const

{
 vm
}

=

await
 freestyle
.
vms
.
create
(
{

6
 git
:

{

7
 repos
:

[

8

{
 repo
:

"https://github.com/user/repo.git"

}
,

9

]

10

}

11
}
)
;

12

13
const

{
 forks
}

=

await
 vm
.
fork
(
{
 count
:

3

}
)
;

14

15
await

Promise
.
all
(
[

16

ai
(
forks
[
0
]
,

"Build the API endpoints"
)
,

17

ai
(
forks
[
1
]
,

"Build the frontend UI"
)
,

18

ai
(
forks
[
2
]
,

"Write the test suite"
)
,

19
]
)
;
1
// Like Code Rabbit, Greptile

2
import

{
 freestyle
}

from

"freestyle-sandboxes"
;

3
import

{

VmBun

}

from

"@freestyle-sh/with-bun"
;

4

5
const

{
 vm
}

=

await
 freestyle
.
vms
.
create
(
{

6
 git
:

{

7
 repos
:

[
{
 repo
:
 repoUrl
,
 rev
:
 branchRev
}
]
,

8

}
,

9
}
)
;

10

11
const

{
 stdout
:
 lint
}

=

await
 vm
.
exec
(
"bun run lint"
)
;

12
const

{
 stdout
:
 test
}

=

await
 vm
.
exec
(
"bun test"
)
;

13
const
 review
=

await

ai
(
vm
,

"Review the diff for bugs"
)
;

14

15
await
 github
.
pulls
.
createReview
(
{

16
 body
:
 review
,

17
 event
:
 test
.
includes
(
"FAIL"
)

?

"REQUEST_CHANGES"

:

"APPROVE"
,

18
}
)
;
1
// Like OpenClaw, Claude, Cowork

2
import

{
 freestyle
}

from

"freestyle-sandboxes"
;

3

4
const

{
 vm
}

=

await
 freestyle
.
vms
.
create
(
{

5
 persistence
:

{
 type
:

"persistent"

}
,

6

// Pauses after 60s idle — $0 cost, resumes on next exec

7
 idleTimeoutSeconds
:

60
,

8
}
)
;

9

10
while

(
true
)

{

11

const
 userMessage
=

await

getNextMessage
(
)
;

12

const
 result
=

await

ai
(
vm
,
 userMessage
)
;

13

await

respond
(
result
)
;

14
}
Trusted by
vly.ai
Rork
Vibeflow
vly.ai
Rork
Vibeflow

## Agent Scale Infrastructure

Sandboxes made for running tens of thousands of agents

### Instant Startup

VMs provision in under 700ms from API request to ready machine.

root@vm
$
 freestyle vms create
[ok]
 Restored memory snapshot
[ok]
 Mounted /dev/vda1
[ok]
 Reached target network
[ok]
 Started systemd-resolved
[ok]
 Started sshd.service
[ok]
 Reached target multi-user
VM ready in
0.7s
root@vm ~ #
█

### Live Forking

Clone a running VM without pausing it — get full copies in milliseconds.

### Pause & Resume

Hibernate VMs and resume exactly where you left off — pay nothing while paused.

ON
OFF

## Manage Agent Code

Git repos for your agents.

mission scaffold complete
mission scaffold complete
assign guidance computers
assign guidance computers
split nav and control APIs
split nav and control APIs
track every stage event
track every stage event
stream telemetry to ground
stream telemetry to ground
redact sensitive payload IDs
redact sensitive payload IDs
set retention by mission phase
set retention by mission phase
add launch-site policy rules
add launch-site policy rules
backfill logs from sim flights
backfill logs from sim flights
build telemetry rollup worker
build telemetry rollup worker
generate mission control digest
generate mission control digest
polish digest timing windows
polish digest timing windows
tune rollup thresholds
tune rollup thresholds
enable preflight checks in CI
enable preflight checks in CI
cache hot flight read paths
cache hot flight read paths
merge branch 'fuel-optimizer'
merge branch 'fuel-optimizer'
mission brief locked
mission brief locked
merge branch 'flight-telemetry'
merge branch 'flight-telemetry'
collect engine cycle metrics
collect engine cycle metrics
add trajectory snapshot reports
add trajectory snapshot reports
publish burn-rate indicators
publish burn-rate indicators
simulate alternate burn curve
simulate alternate burn curve
retry dropped comm packets
retry dropped comm packets
tune thrust profile model
tune thrust profile model
fix uplink queue deadlock
fix uplink queue deadlock
run final launch rehearsal
run final launch rehearsal
merge branch 'comms-hotfix'
merge branch 'comms-hotfix'
launch window approved at T-0
launch window approved at T-0
flight-telemetry
fuel-optimizer
safety-checklists
mission-rollups
engine-metrics
comms-hotfix
main
HEAD
Sandbox
Git Repo
acme
acme/app
zipline
zipline/api
nova
nova/app
⋮
⋮
sandbox-10k
10000/repo

### Granular Webhooks

Configure webhooks per repo, filter by branch, path, or event type.

git push
ci.internal/webhook

✓
hooks.slack.com/trigger

✓
freestyle deploy

✓

### Sync with GitHub

Bidirectional sync between Freestyle and GitHub repositories.

### Deploy from Git

Push to deploy with Freestyle Deployments or clone into a VM.

terminal

## The Most Powerful Sandboxes

Not containers. Full Linux VMs with real root access.

### Nested Virtualization

Run VMs inside VMs, Docker, or any virtualization stack your agents need. Full KVM support.

### Users, Groups, Services

Sealed Linux users, systemd services and groups; multi-user isolation inside every VM.

### Full Networking Stack

The full Linux networking stack with real root access.

## Ready to get started?

Free to start. No credit card required.

Start building
Read the docs

### What is a Freestyle sandbox?

### What do I pay for paused VMs?

### How is this different from other sandboxes?

### How secure is it?

### How are Freestyle Git repos different than GitHub?

Products
Freestyle Git
Freestyle VMs
Freestyle Deploys
Freestyle Runs
Documentation
Freestyle API Documentation
Freestyle API Reference
Open Source
Adorable (AI App Builder)
Freestyle CLI
Cloudstate (JavaScript Database)
Company
Careers
Status
Discord
Privacy Policy
©
2026
 Freestyle
