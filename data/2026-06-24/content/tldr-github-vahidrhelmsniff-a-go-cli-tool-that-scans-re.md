---
title: 'GitHub - VahidR/helmsniff: A Go CLI tool that scans rendered Kubernetes/Helm manifests and produces a CSV & JSON report of security misconfigurations. · GitHub'
url: https://github.com/VahidR/helmsniff
site_name: tldr
content_file: tldr-github-vahidrhelmsniff-a-go-cli-tool-that-scans-re
fetched_at: '2026-06-24T19:35:53.007861'
original_url: https://github.com/VahidR/helmsniff
date: '2026-06-24'
description: A Go CLI tool that scans rendered Kubernetes/Helm manifests and produces a CSV & JSON report of security misconfigurations. - VahidR/helmsniff
tags:
- tldr
---

VahidR

 

/

helmsniff

Public

* NotificationsYou must be signed in to change notification settings
* Fork0
* Star6

 
 
 
 
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

12 Commits
12 Commits
cmd
cmd
 
 
internal
internal
 
 
.gitignore
.gitignore
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
go.mod
go.mod
 
 
go.sum
go.sum
 
 
View all files

## Repository files navigation

# helmsniff

A Go CLI tool that scans rendered Kubernetes/Helm manifests and produces a CSV or JSON report of security misconfigurations.

## Security Checks

Every output row begins with two context columns, followed by one column per
check. Check columns are binary integers (1= violation/detected,0= ok),
whileK8S_STATUSandHELM_STATUSare booleans (true/false).

Column

Type

Description

DIR

string

Parent directory (chart) path, or input label for stdin mode

YAML_FULL_PATH

string

Full path to the analyzed YAML file, or input label for stdin mode

WITHIN_MANIFEST_SECRET

int

Document is a 
Secret
 with non-empty 
data
/
stringData

VALID_TAINT_SECRET

int

Reserved for taint-based secret detection (always 
0
; not yet implemented)

SEC_CONT_OVER_PRIVIL

int

Container running in privileged mode

INSECURE_HTTP

int

A plaintext 
http://
 URL found anywhere in the document

NO_SECU_CONTEXT

int

No 
securityContext
 at pod level or on any container

NO_DEFAULT_NSPACE

int

No namespace specified in resource metadata

NO_RESO

int

A container is missing both resource requests and limits

NO_ROLLING_UPDATE

int

Deployment uses 
Recreate
 or lacks a 
rollingUpdate
 strategy

NO_NETWORK_POLICY

int

Chart contains no 
NetworkPolicy
 resource

TRUE_HOST_PID

int

hostPID: true

TRUE_HOST_IPC

int

hostIPC: true

DOCKERSOCK_PATH

int

/var/run/docker.sock
 mounted via 
hostPath

TRUE_HOST_NET

int

hostNetwork: true

CAP_SYS_ADMIN

int

SYS_ADMIN
 capability added to a container

HOST_ALIAS

int

hostAliases
 present in the pod spec

ALLOW_PRIVI

int

allowPrivilegeEscalation: true

SECCOMP_UNCONFINED

int

seccompProfile.type
 set to 
Unconfined

CAP_SYS_MODULE

int

SYS_MODULE
 capability added to a container

K8S_STATUS

bool

Document is a valid Kubernetes resource (has 
apiVersion
 and 
kind
)

HELM_STATUS

bool

Document is managed by Helm (
managed-by: Helm
 label or 
helm.sh/chart
 label)

## Prerequisites

* Go 1.22+
* GNU Make

## Build

make build

The binary is compiled tobin/helmsniff.

## Usage

./bin/helmsniff --root 
<
rendered_dir
|
-
>
 --out 
<
output_path
|
-
>
 [--format csv
|
json]

Flags:

Flag

Description

--root

Path to directory containing rendered Kubernetes manifests, or 
-
 to read from stdin

--out

Path to output file, or 
-
 to write to stdout

--format

Output format: 
csv
 (default) or 
json

### Batch processing

Scan multiple charts in parallel using GNUparallel:

parallel ./bin/helmsniff --root {} --out reports/{/}.csv ::: datasets/rendered/
*
/

### JSON output

Generate a JSON report instead of CSV:

./bin/helmsniff --root datasets/rendered/mychart --out report.json --format json

### Stdin pipe

Pipehelm templateoutput directly without writing intermediate files:

helm template mychart ./charts/mychart 
|
 ./bin/helmsniff --root - --out - --format json

Or save to a file:

helm template mychart ./charts/mychart 
|
 ./bin/helmsniff --root - --out report.csv

## Makefile Targets

Target

Description

make build

Compile the binary

make clean

Remove 
bin/
 directory

make tidy

Run 
go mod tidy

make vet

Run 
go vet ./...

make lint

Run 
golangci-lint
 (must be installed)

make test

Run tests with race detector

## Project Structure

helmsniff/
├── cmd/main.go # CLI entry point (flags, walking, CSV/JSON output)
├── internal/
│ ├── config/constants.go # CSV header definition
│ ├── parser/
│ │ ├── parser.go # YAML document loader (file & reader)
│ │ └── parser_test.go
│ └── scanner/
│ ├── scanner.go # File walking & analysis orchestration
│ ├── security_checks.go # Individual check implementations
│ ├── row.go # Row data structure
│ ├── scanner_test.go
│ └── security_checks_test.go
├── ARCHITECTURE.md # Design notes & detailed check reference
├── Makefile
├── go.mod
└── go.sum

## License

MIT

## About

A Go CLI tool that scans rendered Kubernetes/Helm manifests and produces a CSV & JSON report of security misconfigurations.

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

6

 stars
 

### Watchers

0

 watching
 

### Forks

0

 forks
 

 Report repository

 

## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Go99.2%
* Makefile0.8%