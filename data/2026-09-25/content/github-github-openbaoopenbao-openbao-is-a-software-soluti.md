---
title: 'GitHub - openbao/openbao: OpenBao is a software solution to manage, store, and distribute sensitive data including secrets, certificates, and keys. · GitHub'
url: https://github.com/openbao/openbao
site_name: github
content_file: github-github-openbaoopenbao-openbao-is-a-software-soluti
fetched_at: '2026-09-25T15:44:40.353180'
original_url: https://github.com/openbao/openbao
author: openbao
description: OpenBao is a software solution to manage, store, and distribute sensitive data including secrets, certificates, and keys. - openbao/openbao
---

openbao

 

/

openbao

Public

* NotificationsYou must be signed in to change notification settings
* Fork581
* Star7.6k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

21,150 Commits
21,150 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
.hooks
.hooks
 
 
.release
.release
 
 
api
api
 
 
changelog
changelog
 
 
internal
internal
 
 
scripts
scripts
 
 
sdk
sdk
 
 
tools
tools
 
 
ui
ui
 
 
website
website
 
 
.git-blame-ignore-revs
.git-blame-ignore-revs
 
 
.gitignore
.gitignore
 
 
.go-version
.go-version
 
 
.golangci.deprecations.yml
.golangci.deprecations.yml
 
 
.golangci.yml
.golangci.yml
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CHARTER.md
CHARTER.md
 
 
CNAME
CNAME
 
 
CODEOWNERS
CODEOWNERS
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Dockerfile
Dockerfile
 
 
GOVERNANCE.md
GOVERNANCE.md
 
 
LICENSE
LICENSE
 
 
MAINTAINERS.md
MAINTAINERS.md
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
go.mod
go.mod
 
 
go.sum
go.sum
 
 
main.go
main.go
 
 
publiccode.yml
publiccode.yml
 
 
View all files

## Repository files navigation

# OpenBao

Please note: We take OpenBao's security and our users' trust
very seriously. If you believe you have found a security issue
in OpenBao,please responsibly discloseby contacting us atopenbao-security@lists.openssf.org.

 

* Website
* Mailing List
* GitHub Discussions
* Chat Server#openssf-openbao-discussion#openssf-openbao-support#openssf-openbao-tscWorking Groups:#openssf-openbao-wg#openssf-openbao-wg-namespaces#openssf-openbao-wg-pkcs11#openssf-openbao-wg-scalability#openssf-openbao-wg-supply#openssf-openbao-wg-ui
* #openssf-openbao-discussion
* #openssf-openbao-support
* #openssf-openbao-tsc
* Working Groups:#openssf-openbao-wg#openssf-openbao-wg-namespaces#openssf-openbao-wg-pkcs11#openssf-openbao-wg-scalability#openssf-openbao-wg-supply#openssf-openbao-wg-ui
* #openssf-openbao-wg
* #openssf-openbao-wg-namespaces
* #openssf-openbao-wg-pkcs11
* #openssf-openbao-wg-scalability
* #openssf-openbao-wg-supply
* #openssf-openbao-wg-ui

OpenBao is a software solution to manage, store, and distribute sensitive
data including secrets, certificates, and keys. The OpenBao community intends
to provide this software under an OSI-approved open-source license, led by a
community run under open-governance principles.

A modern system requires access to a multitude of secrets: database credentials,
API keys for external services, credentials for service-oriented architecture
communication, etc. Understanding who is accessing what secrets is already very
difficult and platform-specific. Adding on key rolling, secure storage, and
detailed audit logs is almost impossible without a custom solution. This is
where OpenBao steps in.

The key features of OpenBao are:

* Secure Secret Storage: Arbitrary key/value secrets can be stored in
OpenBao. OpenBao encrypts these secrets prior to writing them to persistent
storage, so gaining access to the raw storage isn't enough to access your
secrets. OpenBao can write to disk,PostgreSQL,
and more.
* Dynamic Secrets: OpenBao can generate secrets on-demand for some systems,
such as AWS or SQL databases. For example, when an application needs to access
an S3 bucket, it asks OpenBao for credentials, and OpenBao will generate an
AWS keypair with valid permissions on demand. After creating these dynamic
secrets, OpenBao will also automatically revoke them after the lease is up.
* Data Encryption: OpenBao can encrypt and decrypt data without storing it.
This allows security teams to define encryption parameters and developers to
store encrypted data in a location such as a SQL database without having to
design their own encryption methods.
* Leasing and Renewal: All secrets in OpenBao have aleaseassociated with
them. At the end of the lease, OpenBao will automatically revoke that secret.
Clients are able to renew leases via built-in renew APIs.
* Revocation: OpenBao has built-in support for secret revocation. OpenBao
can revoke not only single secrets, but a tree of secrets, for example,
all secrets read by a specific user, or all secrets of a particular type.
Revocation assists in key rolling as well as locking down systems in the case
of an intrusion.

## Documentation and Getting Started

Documentation is available on theOpenBao website.

## Developing OpenBao

Warning

Before submitting pull requests to OpenBao, ensure that you have
read and understood our contribution guidelines described inCONTRIBUTING.md. A failure to do so will likely result
in your pull request being rejected.

If you wish to work on OpenBao itself or any of its built-in systems,
you'll first needGoinstalled on your
machine. The Go toolchain version used in CI and releases is pinned at.go-version, but using the latest toolchain available for
local development is typically fine.

OpenBao usesGo Modules, so it is
recommended that you clone the repositoryoutsideof the GOPATH.

To build abaobinary:

$ mkdir -p bin
$ go build -o bin/bao 
.

To run the OpenBao server in development mode:

$ go run 
.
 server -dev 
#
 Or `./bin/bao server -dev` if you've built the binary already.

Since OpenBao is a large codebase that takes a short while to compile from a
cold cache, it is useful to attach the-vflag to build commands to get a
better sense of compilation progress.

To test a package:

$ go 
test
 ./some/package

Some additional notes on development:

* There is also aMakefileavailable for advanced build
configurations and maintenance tasks. It is not required to build, run & debug
OpenBao in most cases, but is worth a look.
* This repository also houses OpenBao's website and documentation page
just as OpenBao's web UI application under thewebsiteanduisubtrees respectively. Development instructions
are available atwebsite/README.mdandui/README.md.

### Importing OpenBao

This repository publishes two libraries that may be imported by other projects:github.com/openbao/openbao/api/v2andgithub.com/openbao/openbao/sdk/v2.

Note that this repository also contains OpenBao (the application), and as
with most Go projects, OpenBao uses Go modules to manage its dependencies.
The mechanism to do that is thego.modfile. As it happens, the
presence of that file also makes it theoretically possible to import OpenBao
as a dependency into other projects. Some other projects have made a practice
of doing so in order to take advantage of testing tooling that was developed
for testing OpenBao itself. This is NOT, and has NEVER been, a supported way
to use the OpenBao project. We will not fix bugs relating to failure to importgithub.com/openbao/openbaointo your project or refactor internal code to make
this easier to do.