---
title: I Learned Go in 3 Weeks. Yesterday, My Code Merged into k9s. - DEV Community
url: https://dev.to/le_beltagy/i-learned-go-in-3-weeks-yesterday-my-code-merged-into-k9s-2dg4
site_name: devto
content_file: devto-i-learned-go-in-3-weeks-yesterday-my-code-merged-i
fetched_at: '2026-08-05T12:53:14.589914'
original_url: https://dev.to/le_beltagy/i-learned-go-in-3-weeks-yesterday-my-code-merged-into-k9s-2dg4
author: Le Beltagy
date: '2026-08-01'
description: I Learned Go in 3 Weeks. Yesterday, My Code Merged into k9s. From zero Go experience to a... Tagged with go, kubernetes, opensource, beginners.
tags: '#go, #kubernetes, #opensource, #beginners'
---

Fixing RBAC bugs in K8s 1.31

# I Learned Go in 3 Weeks. Yesterday, My Code Merged into k9s.

From zero Go experience to a merged PR in the most popular Kubernetes terminal UI — how I misread HTTP/1.1 upgrades, broke my own test suite, and learned thatcreateandgetare not the same verb when Kubernetes 1.31 changes the rules underneath you.

## The Setup

It started with a single function I didn't write.

I'd been contributing tok9sfor a week, trying to understand how a 58,000-star project structured its Go code. I was deep ininternal/dao/port_forwarder.go, staring at a block of code that checked whether a user was authorized to open a port-forward on a pod. The check was simple: does this service account havecreatepermission onpods/portforward?

I'd read the Kubernetes docs. Port-forward requirescreate. Everyone said so. The code worked. I moved on.

Then someone opened an issue:"Port-forward fails on k8s 1.31 with restricted RBAC."

Kubernetes 1.31 introduced thePortForwardWebsocketsfeature — a new code path that forwards ports over WebSockets instead of SPDY. And WebSockets, unlike SPDY, only require thegetverb on thepods/portforwardsubresource.

That was the bug. The code was checkingcreate. The new WebSocket path neededget. Users withget-only access couldn't port-forward in k9s, even thoughkubectlworked fine for them.

This is the story of how I tried to fix it, failed the first time, and learned more about Go, HTTP upgrades, and Kubernetes authorization in three days than in three weeks of tutorials.

This is not a tutorial. This is an autopsy of a two-line fix that took me forty-eight hours.

## Why Not Just Use kubectl?

I usekubectl port-forwardprofessionally. It works. It handles the WebSocket migration transparently. There's no bug report. No edge case. No problem.

But k9s is not kubectl. k9s is a terminal UI that wrapsclient-goand presents a unified interface for pod interaction. When k9s shows a pod and lets you pressShift-Fto forward a port, it first checks if you're allowed to do it. And that check was wrong.

The issue wasn't academic. A user with this RBAC role:

rules
:

-
 
apiGroups
:
 
[
"
"
]

 
resources
:
 
[
"
pods/portforward"
]

 
verbs
:
 
[
"
get"
]

Enter fullscreen mode

Exit fullscreen mode

could runkubectl port-forwardsuccessfully on Kubernetes 1.31+ (WebSocket path), but k9s would silently grey out the port-forward option, convinced they lacked permission.

That user was real. The issue had reproduction steps. A real cluster, a real role, a real workflow broken by a verb mismatch I would never have noticed without reading theclient-gosource.

## The k9s Architecture

┌─────────────────────────────────────────────────────────────┐
│ k9s TUI │
│ (tview / terminal UI) │
│ User presses Shift-F on a pod │
└──────────────────────┬──────────────────────────────────────┘
 │
 ▼
┌─────────────────────────────────────────────────────────────┐
│ internal/dao/port_forwarder.go │
│ │
│ 1. Check pod is Running ( readiness gate ) │
│ 2. Authorize: can user create pods/portforward? │
│ ▲ │
│ │ THIS WAS THE BUG │
│ 3. If yes → open port-forward session │
│ If no → grey out option / show error │
└──────────────────────┬──────────────────────────────────────┘
 │
 ┌────────┴────────┐
 │ │
 ▼ ▼
 ┌─────────────┐ ┌─────────────┐
 │ SPDY path │ │ WebSocket │
 │ (legacy) │ │ (k8s 1.31+) │
 │ needs │ │ needs │
 │ CREATE verb │ │ GET verb │
 └─────────────┘ └─────────────┘
 │ │
 └───────┬─────────┘
 ▼
 ┌─────────────────┐
 │ K8s API Server │
 │ /api/v1/.../ │
 │ portforward │
 └─────────────────┘

Enter fullscreen mode

Exit fullscreen mode

### The Decision I Missed

Path

Protocol

Required Verb

k9s Checked?

Legacy SPDY

SPDY/HTTP/1.1 upgrade

create
 on 
pods/portforward

✅ Yes

WebSocket

WebSocket (RFC 6455)

get
 on 
pods/portforward

❌ No

k9s only checked forcreate. It didn't know about the WebSocket path'sgetrequirement. Soget-only users were blocked even though they were authorized for the code path their cluster actually used.

## The Failures (And What Each One Taught Me)

### Failure 1: I Changed One Word and Called It a Day

My first fix was embarrassingly naive.

I found the function inport_forwarder.go. It built anSelfSubjectAccessReviewwith verb"create"and sent it to the API server. I changed it to"get". It compiled. I opened a draft PR.

Within an hour, a maintainer commented:"This breaks backward compatibility for clusters still on the SPDY path."

I had replaced one hardcoded verb with another. I didn't check SPDY. I didn't check both. I didn't even think about clusters running Kubernetes <1.31, or clusters where the WebSocket feature gate was disabled. I assumed "new = right."

Root cause:I treated a protocol negotiation problem like a string replacement problem.

The fix:The code needed to check BOTH verbs independently. Ifcreateis authorized, the user can port-forward via SPDY. Ifgetis authorized, they can port-forward via WebSocket. If either is authorized, k9s should allow the operation. The API server andclient-gohandle which protocol actually gets used at connect time.

// What I wrote first (WRONG — only checks get)

if
 
!
utils
.
CheckPodPortFwd
(
a
.
factory
.
Client
(),
 
a
.
factory
.
Config
(),
 
path
)
 
{

 
return
 
errors
.
New
(
"insufficient permission"
)

}

// What merged (RIGHT — checks create AND get independently)

if
 
!
utils
.
CheckPodPortFwd
(
a
.
factory
.
Client
(),
 
a
.
factory
.
Config
(),
 
path
)
 
{

 
if
 
!
utils
.
CheckPodPortFwdGet
(
a
.
factory
.
Client
(),
 
a
.
factory
.
Config
(),
 
path
)
 
{

 
return
 
errors
.
New
(
"insufficient permission"
)

 
}

}

Enter fullscreen mode

Exit fullscreen mode

Actually, the final merged code was cleaner — it added a newCheckPodPortFwdGethelper and called both from the port-forward check. The key insight:createandgetare not alternatives that replace each other. They're independent capabilities for independent protocol paths. Both can coexist. Neither can be dropped.

Lesson:When a platform supports multiple protocols, a fix for the new one cannot delete support for the old one. Test for coexistence, not replacement.

### Failure 2: I Blew Up the Test Suite Because I Didn't Understandt.Parallel()

k9s has a real test suite. Not toy tests — table-driven tests with ~50 test cases across multiple scenarios. I added a test that covered the new WebSocket path. It passed locally.

Then CI failed.

The error was a data race in the mock client. I'd instantiated a shared mockRestClientoutside the test loop to save setup code. Some tests ran witht.Parallel(). Two parallel tests mutated the same mock's response state simultaneously.

The race detector (go test -race) caught it and failed the build.

Root cause:I thought I was being efficient by sharing mock setup. I was actually creating a concurrency hazard in a test file I didn't fully understand.

The fix:I refactored each test case to build its ownRestClientmock inside the test closure. No shared state. The test file I added ended up being 223 lines — almost all of it test cases for every combination of permissions:

* Pod not running
* Nogetpermission, nocreatepermission → blocked
* create-only permission → allowed (legacy SPDY)
* get-only permission → allowed (WebSocket path, this was the fix)
* Both permissions → allowed

// Part of the 223 lines of tests I ended up writing

{

 
name
:
 
"get-only-portforward-allowed"
,

 
pod
:
 
runningPod
,

 
authorized
:
 
map
[
string
]
bool
{

 
"selfsubjectaccessreviews"
:
 
true
,

 
"pods"
:
 
true
,

 
"portforwardget"
:
 
true
,

 
},

 
want
:
 
true
,

},

Enter fullscreen mode

Exit fullscreen mode

Lesson:Parallel tests are not free. If you don't own the test infrastructure, assume shared state is forbidden until proven otherwise. Adata racein a test is a resume stain.

### Failure 3: I Didn't Know What an HTTP/1.1 Upgrade Was

The real bug was deeper than a verb string. I needed to understand WHYgetwas sufficient for WebSockets but not for SPDY.

SPDY (the legacy protocol) is initiated by an HTTPPOSTrequest to the port-forward endpoint. HTTPPOSTmaps to thecreateverb in Kubernetes authorization. So SPDY port-forwards requirecreate.

WebSockets are initiated differently. They start with an HTTPGETrequest that includes anUpgrade: websocketheader. The server responds with101 Switching Protocols, and the connection becomes a WebSocket.

Because the initial request isGET, Kubernetes authorization maps it to thegetverb on thepods/portforwardsubresource.

I didn't know any of this when I opened the issue. I spent an evening reading:

* RFC 6455 (The WebSocket Protocol)
* Kubernetesclient-gosource forStreamWithContext
* The KEP forPortForwardWebsockets(KEP-4006)
* k9sown issue history for how it handlesclient-godeprecation

Root cause:I thought port-forward was "one API call." It's actually a protocol negotiation dance betweenclient-go, the API server, and the kubelet. The authorization model is protocol-dependent.

The fix:I didn't change the fix. The code was correct once I checked both verbs. But I did update the error message to indicate both acceptable verbs, so users who were blocked would know exactly which permissions they needed:

return
 
fmt
.
Errorf
(
"user is not authorized to create or get portforward %q"
,
 
path
)

Enter fullscreen mode

Exit fullscreen mode

Lesson:Before you fix a bug in a distributed system, understand the protocol it's built on. The symptom was a missing verb. The cause was a protocol upgrade. The fix that didn't understand the protocol would have broken the legacy path.

## The PR

Stat

Value

Changed files

2

Lines added

240

Lines deleted

3

Files touched

internal/dao/port_forwarder.go
, 
internal/dao/port_forwarder_test.go

Tests added

6 test cases covering every permission combination

Review rounds

2

Time from first draft to merge

48 hours

The diff is small. The logic is simple. The effort was in understanding why the logic needed to exist at all — and proving it with tests that would catch someone else making my first-draft mistake.

PR title:fix(dao): allow port-forward with 'get' verb on pods/portforward for K8s 1.31+ WebSocket path

It merged cleanly. No follow-up fixes needed.

## What I Learned About Contributing to Big Projects

### 1. Start with the issue, not the code

I read the original issue (#4144) three times before I touched a file. The reporter included their Kubernetes version, their RBAC role, and the exact error message. Without that reproduction, I would have never understood the WebSocket migration context.

### 2. Read the test file before the source file

port_forwarder_test.gotaught me more about how k9s handles authorization thanport_forwarder.go. Tests are documentation that can't lie.

### 3.go test -raceis not optional

The race detector caught my bug before a maintainer did. It turned an embarrassing review comment into a private CI failure. Run it locally. Always.

### 4. Two-line fixes need two-hundred-line tests

The production change was ~20 lines. The tests were 223 lines. That's the ratio in production Go. If your fix doesn't have a test that would have failed before the fix, your fix isn't done.

### 5. Backward compatibility is a constraint, not a suggestion

My first draft worked on Kubernetes 1.31. It would have broken k9s for half the user base still on 1.30 or older. A real fix supports both paths simultaneously. This is what separates "it works on my machine" from "it merged into k9s."

## Why This Matters (And Why It Doesn't)

### It matters because:

* k9s has ~58,000 GitHub stars and thousands of daily users. My fix affects real people with real clusters.
* I learned Go by readingclient-gosource and writing table-driven tests, not by building TodoMVC.
* I now understand Kubernetes authorization, HTTP upgrades, and protocol negotiation at a level I didn't before.

### It doesn't matter because:

* It's a 20-line fix. Senior engineers at Google write diffs like this before coffee.
* I didn't architect a new subsystem. I didn't refactor the codebase. I fixed a verb check.
* The value isn't in the code. The value is in the proof that I can read an issue, understand the context, write a correct fix, survive review, and ship.

That's the signal I'm building.

## What's Next?

I'm continuing to contribute to k9s. The codebase is complex enough to keep teaching me things — howtviewrenders terminal UIs, howk9swatchers avoid polling the API server, how thedaolayer abstractsclient-gooperations.

I also contributed to Checkov today — adding missing GCP taggable resources for Cloud SQL and GKE clusters. Small PR. Two lines. Merged in 20 minutes. That's what happens when you build the muscle: the second contribution is faster than the first.

## TL;DR

I started learning Go three weeks ago. I found a bug in k9s where port-forward authorization only checked thecreateverb, missing thegetverb needed by Kubernetes 1.31's new WebSocket path.

My first fix was wrong — I replacedcreatewithgetand nearly broke backward compatibility for legacy SPDY clusters. The final fix checks both verbs independently.

I wrote 223 lines of table-driven tests to cover every permission combination. The PR merged in 48 hours. Adata racein my test taught me that parallel tests don't share mock state.

If you're learning a language, don't build tutorial projects. Find a real bug in a real project and fix it. The test suite will teach you more than any course.

What's your first open-source contribution story? Drop it in the comments — especially if you also broke a test suite and lived to tell about it.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse