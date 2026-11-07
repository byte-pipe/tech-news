---
title: 'GitHub - prometheus/prometheus: The Prometheus monitoring system and time series database. · GitHub'
url: https://github.com/prometheus/prometheus
site_name: github
content_file: github-github-prometheusprometheus-the-prometheus-monitor
fetched_at: '2026-11-08T09:02:52.953607'
original_url: https://github.com/prometheus/prometheus
author: prometheus
description: The Prometheus monitoring system and time series database. - prometheus/prometheus
---

main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

19,220 Commits
19,220 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.agents/
skills
.agents/
skills
 
 
.github
.github
 
 
cmd
cmd
 
 
compliance
compliance
 
 
config
config
 
 
discovery
discovery
 
 
docs
docs
 
 
documentation
documentation
 
 
internal/
tools
internal/
tools
 
 
model
model
 
 
notifier
notifier
 
 
plugins
plugins
 
 
prompb
prompb
 
 
promql
promql
 
 
rules
rules
 
 
schema
schema
 
 
scrape
scrape
 
 
scripts
scripts
 
 
storage
storage
 
 
template
template
 
 
tracing
tracing
 
 
tsdb
tsdb
 
 
util
util
 
 
web
web
 
 
.dockerignore
.dockerignore
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.golangci.yml
.golangci.yml
 
 
.promu.yml
.promu.yml
 
 
.yamllint
.yamllint
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CODEOWNERS
CODEOWNERS
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Dockerfile
Dockerfile
 
 
Dockerfile.distroless
Dockerfile.distroless
 
 
LICENSE
LICENSE
 
 
MAINTAINERS.md
MAINTAINERS.md
 
 
Makefile
Makefile
 
 
Makefile.common
Makefile.common
 
 
NOTICE
NOTICE
 
 
README.md
README.md
 
 
RELEASE.md
RELEASE.md
 
 
SECURITY-INSIGHTS.yml
SECURITY-INSIGHTS.yml
 
 
SECURITY.md
SECURITY.md
 
 
VERSION
VERSION
 
 
go.mod
go.mod
 
 
go.sum
go.sum
 
 
go.work
go.work
 
 
renovate.json
renovate.json
 
 
View all files

## Repository files navigation

# Prometheus

Visitprometheus.iofor the full documentation,
examples and guides.

Prometheus, aCloud Native Computing Foundationproject, is a systems and service monitoring system. It collects metrics
from configured targets at given intervals, evaluates rule expressions,
displays the results, and can trigger alerts when specified conditions are observed.

The features that distinguish Prometheus from other metrics and monitoring systems are:

* Amulti-dimensionaldata model (time series defined by metric name and set of key/value dimensions)
* PromQL, apowerful and flexible query languageto leverage this dimensionality
* No dependency on distributed storage;single server nodes are autonomous
* An HTTPpull modelfor time series collection
* Pushing time seriesis supported via an intermediary gateway for batch jobs
* Targets are discovered viaservice discoveryorstatic configuration
* Multiple modes ofgraphing and dashboarding support
* Support for hierarchical and horizontalfederation

## Architecture overview

## Install

There are various ways to install Prometheus.

### Precompiled binaries

Precompiled binaries for released versions are available in thedownloadsectiononprometheus.io. Using the latest production release binary
is the recommended way to install Prometheus.
See theInstallingchapter in the documentation for all the details.

### Docker images

Docker images are available onQuay.ioorDocker Hub.

You can launch a Prometheus container for trying it out with

docker run --name prometheus -d -p 127.0.0.1:9090:9090 prom/prometheus

Prometheus will now be reachable athttp://localhost:9090/.

### Building from source

To build Prometheus from source code, you need:

* Go: Version specified ingo.modor greater.
* NodeJS: Version specified in.nvmrcor greater.
* npm: Version 10 or greater (check withnpm --versionandhere).

Start by cloning the repository:

git clone https://github.com/prometheus/prometheus.git

cd
 prometheus

You can use thegotool to build and install theprometheusandpromtoolbinaries into yourGOPATH:

go install github.com/prometheus/prometheus/cmd/...
prometheus --config.file=your_config.yml

However, when usinggo installto build Prometheus, Prometheus will expect to be able to
read its web assets from local filesystem directories underweb/ui/static. In order for
these assets to be found, you will have to run Prometheus from the root of the cloned
repository. Note also that this directory does not include the React UI unless it has been
built explicitly usingmake assetsormake build.

An example of the above configuration file can be foundhere.

You can also build usingmake build, which will compile in the web assets so that
Prometheus can be run from anywhere:

make build
./prometheus --config.file=your_config.yml

The Makefile provides several targets:

* build: build theprometheusandpromtoolbinaries (includes building and compiling in web assets)
* test: run the tests
* test-short: run the short tests
* format: format the source code
* vet: check the source code for common errors
* assets: build the React UI

### Service discovery plugins

Prometheus is bundled with many service discovery plugins. You can customize
which service discoveries are included in your build using Go build tags.

To exclude service discoveries when building withmake build, add the desired
tags to the.promu.ymlfile underbuild.tags.all:

build
:
 
tags
:
 
all
:
 - 
netgo

 - 
builtinassets

 - 
remove_all_sd 
#
 Exclude all optional SDs

 - 
enable_kubernetes_sd 
#
 Re-enable only kubernetes

Then runmake buildas usual. Alternatively, when usinggo builddirectly:

go build -tags 
"
remove_all_sd,enable_kubernetes_sd
"
 ./cmd/prometheus

Available build tags:

* remove_all_sd- Exclude all optional service discoveries (keeps file_sd, static_sd, and http_sd)
* enable_<name>_sd- Re-enable a specific SD when usingremove_all_sd

If you add out-of-tree plugins, which we do not endorse at the moment,
additional steps might be needed to adjust thego.modandgo.sumfiles. As
always, be extra careful when loading third party code.

### Building the Docker image

You can build a docker image locally with the following commands:

make promu
promu crossbuild -p linux/
$(
go env GOHOSTARCH
)

make common-docker-current-arch

To build for a different architecture, replace$(go env GOHOSTARCH)with one
of the architectures inDOCKER_ARCHSfrom Makefile.common, such asamd64, and run the correspondingmake common-docker-<architecture>target.

Themake dockertarget is intended only for use in our CI system and will not
produce a fully working image when run locally.

## Using Prometheus as a Go Library

Within the Prometheus project, repositories such asprometheus/commonandprometheus/client_golangare designed as reusable libraries.

Theprometheus/prometheusrepository builds a stand-alone program and is not
designed for use as a library. We are aware that people do use parts as such,
and we do not put any deliberate inconvenience in the way, but we want you to be
aware that no care has been taken to make it work well as a library. For instance,
you may encounter errors that only surface when used as a library.

### Remote Write

We are publishing our Remote Write protobuf independently atbuf.build.

You can use that as a library:

go get buf.build/gen/go/prometheus/prometheus/protocolbuffers/go@latest

This is experimental.

### Prometheus code base

In order to comply withgo modrules,
Prometheus release number do not exactly match Go module releases.

For the
Prometheus v3.y.z releases, we are publishing equivalent v0.3y.z tags. The y in v0.3y.z is always padded to two digits, with a leading zero if needed.

Therefore, a user that would want to use Prometheus v3.0.0 as a library could do:

go get github.com/prometheus/prometheus@v0.300.0

For the
Prometheus v2.y.z releases, we published the equivalent v0.y.z tags.

Therefore, a user that would want to use Prometheus v2.35.0 as a library could do:

go get github.com/prometheus/prometheus@v0.35.0

This solution makes it clear that we might break our internal Go APIs between
minor user-facing releases, asbreaking changes are allowed in major version
zero.

## React UI Development

For more information on building, running, and developing on the React-based UI, see the React app'sREADME.md.

## More information

* Godoc documentation is available viapkg.go.dev. Due to peculiarities of Go Modules, v3.y.z will be displayed as v0.3y.z (the y in v0.3y.z is always padded to two digits, with a leading zero if needed), while v2.y.z will be displayed as v0.y.z.
* See theCommunity pagefor how to reach the Prometheus developers and users on various communication channels.

## Contributing

Refer toCONTRIBUTING.md

## License

Apache License 2.0, seeLICENSE.