---
title: 'struct''s lifetime requirements can be bypassed via covariant field assignment · Issue #164250 · rust-lang/rust · GitHub'
url: https://github.com/rust-lang/rust/issues/164250
site_name: hackernews_api
content_file: hackernews_api-structs-lifetime-requirements-can-be-bypassed-via
fetched_at: '2026-10-13T17:57:49.048835'
original_url: https://github.com/rust-lang/rust/issues/164250
author: formerly_proven
date: '2026-10-13'
description: NoteGiven that this issue has been shared online and is currently getting quite a few visitors, here's some additional context. Rust's type system is intended to prevent memory unsafety. Upholding this promise is something we take very s...
tags:
- hackernews
- trending
---

# struct's lifetime requirements can be bypassed via covariant field assignment#164250

Open
Open
struct's lifetime requirements can be bypassed via covariant field assignment
#164250
Labels
A-borrow-checker
Area: The borrow checker
Area: The borrow checker
A-destructors
Area: Destructors (`Drop`, …)
Area: Destructors (`Drop`, …)
A-lifetimes
Area: Lifetimes / regions
Area: Lifetimes / regions
A-variance
Area: Variance (https://doc.rust-lang.org/nomicon/subtyping.html)
Area: Variance (https://doc.rust-lang.org/nomicon/subtyping.html)
C-bug
Category: This is a bug.
Category: This is a bug.
I-unsound
Issue: A soundness hole (worst kind of bug), see: https://en.wikipedia.org/wiki/Soundness
Issue: A soundness hole (worst kind of bug), see: https://en.wikipedia.org/wiki/Soundness
P-high
High priority
High priority
T-types
Relevant to the types team, which will review and decide on the PR/issue.
Relevant to the types team, which will review and decide on the PR/issue.

## Description

jsnell
opened 
on Oct 13, 2026
Issue body actions

Note

Given that this issue has been shared online and is currently getting quite a few visitors, here's some additional context.

Rust's type system is intended to prevent memory unsafety. Upholding this promise is something we take very seriously, which is why we've been working on things likethe next-generation trait solver,the region constraint rework, and more generallyProject Zero. It is a large priority of the Types Team to fix all type system unsoundnesses and to work towards there being a solid foundation to minimize the risk of unknown ones.

This bug is aP-highissue and would have beenP-criticalregardless of whether people encountered it in the wild. The reason that it is "onlyP-high" is that it's 11 years old. A bug like this which has not been found during the last 11 years cannot actually be that easy to hit.

Looking at the bug itself, it is also very likely that this unsoundness has not caused memory unsafety by accident. While it looks easy to trigger, to exploit this you need an intentionally maliciousDropimplementation.

~@lcnr

In the following code:

use
 std
::
sync
::
Mutex
;

static
 
KEPT
:
 
Mutex
<
Vec
<
Box
<
dyn
 std
::
any
::
Any
 + 
Send
>
>
>
 = 
Mutex
::
new
(
Vec
::
new
(
)
)
;

struct
 
Q
<
T
:
 
'
static
 + 
Send
>
(
Option
<
T
>
)
;

impl
<
T
:
 
'
static
 + 
Send
>
 
Drop
 
for
 
Q
<
T
>
 
{

 
fn
 
drop
(
&
mut
 
self
)
 
{
 
if
 
let
 
Some
(
t
)
 = 
self
.
0
.
take
(
)
 
{
 
KEPT
.
lock
(
)
.
unwrap
(
)
.
push
(
Box
::
new
(
t
)
)
;
 
}
 
}

}

fn
 
main
(
)
 
{

 
{

 
let
 l = 
String
::
from
(
"hello world, this is long enough"
)
;

 
let
 
mut
 q = 
Q
(
None
)
;

 q
.
0
 = 
Some
(
&
l
)
;

 
}

 
let
 _z = 
String
::
from
(
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
)
;

 
let
 k = 
KEPT
.
lock
(
)
.
unwrap
(
)
;

 
println
!
(
"{}"
,
 k
[
0
]
.
downcast_ref
::
<
&
'
static
 
String
>
(
)
.
unwrap
(
)
)
;

}

I expected to see this happen: program is not accepted

Instead, this happened: program compiles and printsXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX. With asan, the program will crash with aAddressSanitizer: stack-use-after-scope

### Meta

Issue on current nightly, and stables at least down to 1.85.0

Godbolt with asan:https://rust.godbolt.org/z/83MvfbKdeGodbolt without asan:https://rust.godbolt.org/z/GsGdqqMWe

Reactions are currently unavailable

## Metadata

## Metadata