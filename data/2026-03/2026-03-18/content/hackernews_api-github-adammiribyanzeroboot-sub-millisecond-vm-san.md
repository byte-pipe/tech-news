---
title: 'GitHub - adammiribyan/zeroboot: Sub-millisecond VM sandboxes for AI agents via copy-on-write forking · GitHub'
url: https://github.com/adammiribyan/zeroboot
site_name: hackernews_api
content_file: hackernews_api-github-adammiribyanzeroboot-sub-millisecond-vm-san
fetched_at: '2026-03-18T19:24:58.730565'
original_url: https://github.com/adammiribyan/zeroboot
author: adammiribyan
date: '2026-03-17'
description: Sub-millisecond VM sandboxes for AI agents via copy-on-write forking - adammiribyan/zeroboot
tags:
- hackernews
- trending
---

adammiribyan

 

/

zeroboot

Public

* NotificationsYou must be signed in to change notification settings
* Fork20
* Star516

 
 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

21 Commits
21 Commits
assets
assets
 
 
demo
demo
 
 
deploy
deploy
 
 
docs
docs
 
 
guest
guest
 
 
sdk
sdk
 
 
src
src
 
 
.gitignore
.gitignore
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
verify.sh
verify.sh
 
 
View all files

## Repository files navigation

Sub-millisecond VM sandboxes for AI agents via copy-on-write forking

## Try it

curl -X POST https://api.zeroboot.dev/v1/exec \
 -H 
'
Content-Type: application/json
'
 \
 -H 
'
Authorization: Bearer zb_demo_hn2026
'
 \
 -d 
'
{"code":"import numpy as np; print(np.random.rand(3))"}
'

## Benchmarks

Metric

Zeroboot

E2B

microsandbox

Daytona

Spawn latency p50

0.79ms

~150ms

~200ms

~27ms

Spawn latency p99

1.74ms

~300ms

~400ms

~90ms

Memory per sandbox

~265KB

~128MB

~50MB

~50MB

Fork + exec (Python)

~8ms

-

-

-

1000 concurrent forks

815ms

-

-

-

Each sandbox is a real KVM virtual machine with hardware-enforced memory isolation.

## How it works

 Firecracker snapshot ──► mmap(MAP_PRIVATE) ──► KVM VM + restored CPU state
 (copy-on-write) (~0.8ms)

1. Template(one-time): Firecracker boots a VM, pre-loads your runtime, and snapshots memory + CPU state
2. Fork(~0.8ms): Creates a new KVM VM, maps snapshot memory as CoW, restores all CPU state
3. Isolation: Each fork is a separate KVM VM with hardware-enforced memory isolation

## SDKs

Python—sdk/python

from
 
zeroboot
 
import
 
Sandbox

sb
 
=
 
Sandbox
(
"zb_live_your_key"
)

result
 
=
 
sb
.
run
(
"print(1 + 1)"
)

TypeScript—sdk/node

import
 
{
 
Sandbox
 
}
 
from
 
"@zeroboot/sdk"
;

const
 
result
 
=
 
await
 
new
 
Sandbox
(
"zb_live_your_key"
)
.
run
(
"console.log(1+1)"
)
;

## Docs

* API Reference
* Deployment Guide
* Architecture

## Status

Working prototype. The fork primitive, benchmarks, and API are real, but not production-hardened yet.Open an issueif you're interested.

## License

Apache-2.0

## About

Sub-millisecond VM sandboxes for AI agents via copy-on-write forking

zeroboot.dev

### Topics

 rust

 vm

 virtual-machine

 sandbox

 kvm

 code-execution

 ai-agents

 copy-on-write

 firecracker

### Resources

 Readme

 

### License

 Apache-2.0 license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

516

 stars
 

### Watchers

6

 watching
 

### Forks

20

 forks
 

 Report repository

 

## Contributors1

* adammiribyanAdam Miribyan

## Languages

* Rust80.7%
* Shell10.7%
* Python3.1%
* C3.0%
* TypeScript2.2%
* Makefile0.3%