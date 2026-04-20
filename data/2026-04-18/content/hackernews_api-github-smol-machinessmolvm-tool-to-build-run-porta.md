---
title: 'GitHub - smol-machines/smolvm: Tool to build & run portable, lightweight, self-contained virtual machines. · GitHub'
url: https://github.com/smol-machines/smolvm
site_name: hackernews_api
content_file: hackernews_api-github-smol-machinessmolvm-tool-to-build-run-porta
fetched_at: '2026-04-18T11:33:53.021816'
original_url: https://github.com/smol-machines/smolvm
author: binsquare
date: '2026-04-17'
description: Tool to build & run portable, lightweight, self-contained virtual machines. - smol-machines/smolvm
tags:
- hackernews
- trending
---

smol-machines



/

smolvm

Public

* NotificationsYou must be signed in to change notification settings
* Fork51
* Star1.4k




 
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

487 Commits
487 Commits
.github/
workflows
.github/
workflows
 
 
assets
assets
 
 
crates
crates
 
 
docs
docs
 
 
examples
examples
 
 
lib
lib
 
 
libkrun @ 7931903
libkrun @ 7931903
 
 
libkrunfw @ 351d354
libkrunfw @ 351d354
 
 
scripts
scripts
 
 
sdks
sdks
 
 
smolvm-sdk @ d6535e1
smolvm-sdk @ d6535e1
 
 
src
src
 
 
tests
tests
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
AGENTS.md
AGENTS.md
 
 
Cargo.toml
Cargo.toml
 
 
LICENSE
LICENSE
 
 
Licenses.md
Licenses.md
 
 
Makefile.toml
Makefile.toml
 
 
README.md
README.md
 
 
build.rs
build.rs
 
 
rust-toolchain.toml
rust-toolchain.toml
 
 
rustfmt.toml
rustfmt.toml
 
 
smolvm.entitlements
smolvm.entitlements
 
 
View all files

## Repository files navigation

# smolvm

Ship and run software with isolation by default.

This is a CLI tool that lets you:

1. Manage and run custom Linux virtual machines locally with: sub-second cold start, cross-platform (macOS, Linux), elastic memory usage.
2. Pack a stateful virtual machine into a single file (.smolmachine) to rehydrate on any supported platform.

## Install

#
 install (macOS + Linux)

curl -sSL https://smolmachines.com/install.sh
|
 bash

#
 for coding agents — install + discover all commands

curl -sSL https://smolmachines.com/install.sh
|
 bash
&&
 smolvm --help

Or download fromGitHub Releases.

## Quick Start

#
 run a command in an ephemeral VM (cleaned up after exit)

smolvm machine run --net --image alpine -- sh -c
"
echo 'Hello world from a microVM' && uname -a
"

#
 interactive shell

smolvm machine run --net -it --image alpine -- /bin/sh

#
 inside the VM: apk add sl && sl && exit

## Use This For

Sandbox untrusted code— run untrusted programs in a hardware-isolated VM. Host filesystem, network, and credentials are separated by a hypervisor boundary.

#
 network is off by default — untrusted code can't phone home

smolvm machine run --image alpine -- ping -c 1 1.1.1.1

#
 fails — no network access

#
 lock down egress — only allow specific hosts

smolvm machine run --net --image alpine --allow-host registry.npmjs.org -- wget -q -O /dev/null https://registry.npmjs.org

#
 works — allowed host

smolvm machine run --net --image alpine --allow-host registry.npmjs.org -- wget -q -O /dev/null https://google.com

#
 fails — not in allow list

Pack into portable executables— turn any workload into a self-contained binary. All dependencies are pre-baked — no install step, no runtime downloads, boots in <200ms.

smolvm pack create --image python:3.12-alpine -o ./python312
./python312 run -- python3 --version

#
 Python 3.12.x — isolated, no pyenv/venv/conda needed

Persistent machines for development— create, stop, start. Installed packages survive restarts.

smolvm machine create --net myvm
smolvm machine start --name myvm
smolvm machine
exec
 --name myvm -- apk add sl
smolvm machine
exec
 --name myvm -it -- /bin/sh

#
 inside: sl, ls, uname -a — type 'exit' to leave

smolvm machine stop --name myvm

Use git and SSH without exposing keys— forward your host SSH agent into the VM. Private keys never enter the guest — the hypervisor enforces this. Requires an SSH agent running on your host (ssh-add -lto check).

smolvm machine run --ssh-agent --net --image alpine -- sh -c
"
apk add -q openssh-client && ssh-add -l
"

#
 lists your host keys, but they can't be extracted from inside the VM

smolvm machine
exec
 --name myvm -- git clone git@github.com:org/private-repo.git

Declare environments with a Smolfile— reproducible VM config in a simple TOML file.

image
 =
"
python:3.12-alpine
"

net
 =
true

[
network
]

allow_hosts
 = [
"
api.stripe.com
"
,
"
db.example.com
"
]

[
dev
]

init
 = [
"
pip install -r requirements.txt
"
]

volumes
 = [
"
./src:/app
"
]

[
auth
]

ssh_agent
 =
true

smolvm machine create myvm -s Smolfile
smolvm machine start --name myvm

More examples:python·node·doom

## How It Works

Each workload gets real hardware isolation — its own kernel onHypervisor.framework(macOS) or KVM (Linux).libkrunVMM with custom kernel:libkrunfw. Pack it into a.smolmachineand it runs anywhere the host architecture matches, with zero dependencies.

Images use theOCIformat — the same open standard Docker uses. Any image on Docker Hub, ghcr.io, or other OCI registries can be pulled and booted as a microVM. No Docker daemon required.

Defaults: 4 vCPUs, 8 GiB RAM. Memory is elastic via virtio balloon — the host only commits what the guest actually uses and reclaims the rest automatically. vCPU threads sleep in the hypervisor when idle, so over-provisioning has near-zero cost. Override with--cpusand--mem.

## Comparison

smolvm

Containers

Colima

QEMU

Firecracker

Kata

Isolation

VM per workload

Namespace (shared kernel)

Namespace (1 VM)

Separate VM

Separate VM

VM per container

Boot time

<200ms

~100ms

~seconds

~15-30s

<125ms

~500ms

Architecture

Library (libkrun)

Daemon

Daemon (in VM)

Process

Process

Runtime stack

Per-workload VMs

Yes

No

No (shared)

Yes

Yes

Yes

macOS native

Yes

Via Docker VM

Yes (krunkit)

Yes

No

No

Embeddable SDK

Yes

No

No

No

No

No

Portable artifacts

.smolmachine

Images (need daemon)

No

No

No

No

## Platform Support

Host

Guest

Requirements

macOS Apple Silicon

arm64 Linux

macOS 11+

macOS Intel

x86_64 Linux

macOS 11+ (untested)

Linux x86_64

x86_64 Linux

KVM (
/dev/kvm
)

Linux aarch64

aarch64 Linux

KVM (
/dev/kvm
)

## Known Limitations

* Network is opt-in (--netonmachine create). TCP/UDP only, no ICMP.
* Volume mounts: directories only (no single files).
* macOS: binary must be signed with Hypervisor.framework entitlements.
* --ssh-agentrequires an SSH agent running on the host (SSH_AUTH_SOCKmust be set).

## Development

Seedocs/DEVELOPMENT.md.

Apache-2.0· made by@binsquare·twitter·github

## About

Tool to build & run portable, lightweight, self-contained virtual machines.

smolmachines.com

### Topics

 rust

 containers

 virtual-machine

 microvm

 crun

 libkrun

### Resources

 Readme



### License

 Apache-2.0 license


### Uh oh!

There was an error while loading.Please reload this page.





Activity


Custom properties


### Stars

1.4k

 stars


### Watchers

5

 watching


### Forks

51

 forks


 Report repository



## Releases41

smolvm v0.5.19

 Latest



Apr 18, 2026



+ 40 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





### Uh oh!

There was an error while loading.Please reload this page.





## Contributors7

## Languages

* Rust82.3%
* Shell15.3%
* TypeScript2.4%
