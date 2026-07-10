---
title: 'GitHub - tailscale/tailscale: The easiest, most secure way to use WireGuard and 2FA. · GitHub'
url: https://github.com/tailscale/tailscale
site_name: github
content_file: github-github-tailscaletailscale-the-easiest-most-secure
fetched_at: '2026-07-10T12:02:04.346234'
original_url: https://github.com/tailscale/tailscale
author: tailscale
description: The easiest, most secure way to use WireGuard and 2FA. - tailscale/tailscale
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 tailscale

 

/

tailscale

Public

* NotificationsYou must be signed in to change notification settings
* Fork2.9k
* Star33.5k

 
 
 
 
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

10,918 Commits
10,918 Commits
.bencher
.bencher
 
 
.github
.github
 
 
appc
appc
 
 
atomicfile
atomicfile
 
 
chirp
chirp
 
 
client
client
 
 
clientupdate
clientupdate
 
 
cmd
cmd
 
 
control
control
 
 
derp
derp
 
 
disco
disco
 
 
docs
docs
 
 
doctor
doctor
 
 
drive
drive
 
 
envknob
envknob
 
 
feature
feature
 
 
gokrazy
gokrazy
 
 
health
health
 
 
hostinfo
hostinfo
 
 
internal
internal
 
 
ipn
ipn
 
 
jsondb
jsondb
 
 
k8s-operator
k8s-operator
 
 
kube
kube
 
 
licenses
licenses
 
 
log
log
 
 
logpolicy
logpolicy
 
 
logtail
logtail
 
 
metrics
metrics
 
 
misc
misc
 
 
net
net
 
 
omit
omit
 
 
packages/
deb
packages/
deb
 
 
paths
paths
 
 
portlist
portlist
 
 
posture
posture
 
 
prober
prober
 
 
proxymap
proxymap
 
 
release
release
 
 
safesocket
safesocket
 
 
safeweb
safeweb
 
 
scripts
scripts
 
 
sessionrecording
sessionrecording
 
 
ssh/
tailssh
ssh/
tailssh
 
 
syncs
syncs
 
 
tailcfg
tailcfg
 
 
tempfork
tempfork
 
 
tka
tka
 
 
tool
tool
 
 
tsconsensus
tsconsensus
 
 
tsconst
tsconst
 
 
tsd
tsd
 
 
tsnet
tsnet
 
 
tstest
tstest
 
 
tstime
tstime
 
 
tsweb
tsweb
 
 
types
types
 
 
util
util
 
 
version
version
 
 
wf
wf
 
 
wgengine
wgengine
 
 
wif
wif
 
 
words
words
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.golangci.yml
.golangci.yml
 
 
.policy-tests.yml
.policy-tests.yml
 
 
.policy.yml
.policy.yml
 
 
.stignore
.stignore
 
 
ALPINE.txt
ALPINE.txt
 
 
CODEOWNERS
CODEOWNERS
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
Dockerfile
Dockerfile
 
 
Dockerfile.base
Dockerfile.base
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
PATENTS
PATENTS
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
VERSION.txt
VERSION.txt
 
 
api.md
api.md
 
 
assert_ts_toolchain_match.go
assert_ts_toolchain_match.go
 
 
build_dist.sh
build_dist.sh
 
 
build_docker.sh
build_docker.sh
 
 
cache_key_test.go
cache_key_test.go
 
 
flake.lock
flake.lock
 
 
flake.nix
flake.nix
 
 
flakehashes.json
flakehashes.json
 
 
go.mod
go.mod
 
 
go.sum
go.sum
 
 
go.toolchain.branch
go.toolchain.branch
 
 
go.toolchain.next.branch
go.toolchain.next.branch
 
 
go.toolchain.next.rev
go.toolchain.next.rev
 
 
go.toolchain.rev
go.toolchain.rev
 
 
go.toolchain.version
go.toolchain.version
 
 
gomod_test.go
gomod_test.go
 
 
header.txt
header.txt
 
 
license_test.go
license_test.go
 
 
pkgdoc_test.go
pkgdoc_test.go
 
 
pull-toolchain.sh
pull-toolchain.sh
 
 
View all files

## Repository files navigation

# Tailscale

https://tailscale.com

Private WireGuard® networks made easy

## Overview

This repository contains the majority of Tailscale's open source code.
Notably, it includes thetailscaleddaemon and
thetailscaleCLI tool. Thetailscaleddaemon runs on Linux, Windows,macOS, and to varying degrees
on FreeBSD and OpenBSD. The Tailscale iOS and Android apps use this repo's
code, but this repo doesn't contain the mobile GUI code.

OtherTailscale reposof note:

* the Android app is athttps://github.com/tailscale/tailscale-android
* the Synology package is athttps://github.com/tailscale/tailscale-synology
* the QNAP package is athttps://github.com/tailscale/tailscale-qpkg
* the Chocolatey packaging is athttps://github.com/tailscale/tailscale-chocolatey

For background on which parts of Tailscale are open source and why,
seehttps://tailscale.com/opensource/.

## Using

We serve packages for a variety of distros and platforms athttps://pkgs.tailscale.com.

## Other clients

ThemacOS, iOS, and Windows clientsuse the code in this repository but additionally include small GUI
wrappers. The GUI wrappers on non-open source platforms are themselves
not open source.

## Building

We always require the latest Go release, currently Go 1.26. (While we build
releases with ourGo fork, its use is not
required.)

go install tailscale.com/cmd/tailscale{,d}

If you're packaging Tailscale for distribution, usebuild_dist.shinstead, to burn commit IDs and version info into the binaries:

./build_dist.sh tailscale.com/cmd/tailscale
./build_dist.sh tailscale.com/cmd/tailscaled

If your distro has conventions that preclude the use ofbuild_dist.sh, please do the equivalent of what it does in your
distro's way, so that bug reports contain useful version information.

## Bugs

Please file any issues about this code or the hosted service onthe issue tracker.

## Contributing

PRs welcome! But please file bugs. Commit messages shouldreference
bugs.

We requireDeveloper Certificate of
OriginSigned-off-bylines in commits.

Seecommit-messages.md(or skimgit log) for our commit message style.

## About Us

Tailscaleis primarily developed by the
people athttps://github.com/orgs/tailscale/people. For other contributors,
see:

* https://github.com/tailscale/tailscale/graphs/contributors
* https://github.com/tailscale/tailscale-android/graphs/contributors

## Legal

WireGuard is a registered trademark of Jason A. Donenfeld.

## About

The easiest, most secure way to use WireGuard and 2FA.

tailscale.com

### Topics

 oauth

 vpn

 sso

 2fa

 wireguard

 tailscale

### Resources

 Readme

 

### License

 BSD-3-Clause license
 

### Code of conduct

 Code of conduct
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

33.5k

 stars
 

### Watchers

266

 watching
 

### Forks

2.9k

 forks
 

 Report repository

 

## Releases155

v1.98.8

 Latest

 

Jun 30, 2026

 

+ 154 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Go95.8%
* C1.5%
* TypeScript1.0%
* Shell0.5%
* Swift0.3%
* HTML0.2%
* Other0.7%