---
title: 'GitHub - rustfs/rustfs: 🚀2.3x faster than MinIO for 4KB object payloads. RustFS is an open-source, S3-compatible high-performance object storage system supporting migration and coexistence with other S3-compatible platforms such as MinIO and Ceph. · GitHub'
url: https://github.com/rustfs/rustfs
site_name: github
content_file: github-github-rustfsrustfs-23x-faster-than-minio-for-4kb
fetched_at: '2026-04-12T11:34:10.169149'
original_url: https://github.com/rustfs/rustfs
author: rustfs
description: 🚀2.3x faster than MinIO for 4KB object payloads. RustFS is an open-source, S3-compatible high-performance object storage system supporting migration and coexistence with other S3-compatible platforms such as MinIO and Ceph. - rustfs/rustfs
---

rustfs



/

rustfs

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.1k
* Star24.9k




 
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

2,730 Commits
2,730 Commits
.agents/
skills
.agents/
skills
 
 
.cargo
.cargo
 
 
.config/
make
.config/
make
 
 
.docker
.docker
 
 
.github
.github
 
 
.vscode
.vscode
 
 
crates
crates
 
 
deploy
deploy
 
 
helm
helm
 
 
rustfs
rustfs
 
 
scripts
scripts
 
 
.dockerignore
.dockerignore
 
 
.envrc
.envrc
 
 
.gitignore
.gitignore
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLA.md
CLA.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
Dockerfile
Dockerfile
 
 
Dockerfile.decommission-local
Dockerfile.decommission-local
 
 
Dockerfile.glibc
Dockerfile.glibc
 
 
Dockerfile.source
Dockerfile.source
 
 
Justfile
Justfile
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
README_ZH.md
README_ZH.md
 
 
SECURITY.md
SECURITY.md
 
 
_typos.toml
_typos.toml
 
 
build-rustfs.sh
build-rustfs.sh
 
 
docker-buildx.sh
docker-buildx.sh
 
 
docker-compose-simple.yml
docker-compose-simple.yml
 
 
docker-compose.decommission.yml
docker-compose.decommission.yml
 
 
docker-compose.yml
docker-compose.yml
 
 
entrypoint.sh
entrypoint.sh
 
 
flake.lock
flake.lock
 
 
flake.nix
flake.nix
 
 
rust-toolchain.toml
rust-toolchain.toml
 
 
rustfmt.toml
rustfmt.toml
 
 
rustfs.spec
rustfs.spec
 
 
View all files

## Repository files navigation

RustFS is a high-performance, distributed object storage system built in Rust.

Getting Started·Docs·Bug reports·Discussions

English |简体中文|Deutsch|Español|français|日本語|한국어|Portuguese|Русский

RustFS is a high-performance, distributed object storage system built in Rust—one of the most loved programming languages worldwide. RustFS combines the simplicity of MinIO with the memory safety and raw performance of Rust. It offers full S3 compatibility, is completely open-source, and is optimized for data lakes, AI, and big data workloads.

Unlike other storage systems, RustFS is released under the permissible Apache 2.0 license, avoiding the restrictions of AGPL. With Rust as its foundation, RustFS delivers superior speed and secure distributed features for next-generation object storage.

## Feature & Status

* High Performance: Built with Rust to ensure maximum speed and resource efficiency.
* Distributed Architecture: Scalable and fault-tolerant design suitable for large-scale deployments.
* S3 Compatibility: Seamless integration with existing S3-compatible applications and tools.
* OpenStack Swift API: Native support for Swift protocol with Keystone authentication.
* OpenStack Keystone Integration: Native support for OpenStack Keystone authentication with X-Auth-Token headers.
* Data Lake Support: Optimized for high-throughput big data and AI workloads.
* Open Source: Licensed under Apache 2.0, encouraging unrestricted community contributions and commercial usage.
* User-Friendly: Designed with simplicity in mind for easy deployment and management.

Feature

Status

Feature

Status

S3 Core Features

✅ Available

Bitrot Protection

✅ Available

Upload / Download

✅ Available

Single Node Mode

✅ Available

Versioning

✅ Available

Bucket Replication

✅ Available

Logging

✅ Available

Lifecycle Management

🚧 Under Testing

Event Notifications

✅ Available

Distributed Mode

🚧 Under Testing

K8s Helm Charts

✅ Available

RustFS KMS

🚧 Under Testing

Keystone Auth

✅ Available

Multi-Tenancy

✅ Available

Swift API

✅ Available

Swift Metadata Ops

🚧 Partial

## RustFS vs MinIO Performance

Stress Test Environment:

Type

Parameter

Remark

CPU

2 Core

Intel Xeon (Sapphire Rapids) Platinum 8475B, 2.7/3.2 GHz

Memory

4GB

Network

15Gbps

Drive

40GB x 4

IOPS 3800 / Drive

rustfs.mp4

### RustFS vs Other Object Storage

Feature

RustFS

Other Object Storage

Console Experience

Powerful Console
Comprehensive management interface.

Basic / Limited Console
Often overly simple or lacking critical features.

Language & Safety

Rust-based
Memory safety by design.

Go or C-based
Potential for memory GC pauses or leaks.

Data Sovereignty

No Telemetry / Full Compliance
Guards against unauthorized cross-border data egress. Compliant with GDPR (EU/UK), CCPA (US), and APPI (Japan).

Potential Risk
Possible legal exposure and unwanted data telemetry.

Licensing

Permissive Apache 2.0
Business-friendly, no "poison pill" clauses.

Restrictive AGPL v3
Risk of license traps and intellectual property pollution.

Compatibility

100% S3 Compatible
Works with any cloud provider or client, anywhere.

Variable Compatibility
May lack support for local cloud vendors or specific APIs.

Edge & IoT

Strong Edge Support
Ideal for secure, innovative edge devices.

Weak Edge Support
Often too heavy for edge gateways.

Risk Profile

Enterprise Risk Mitigation
Clear IP rights and safe for commercial use.

Legal Risks
Intellectual property ambiguity and usage restrictions.

## Staying ahead

Star RustFS on GitHub and be instantly notified of new releases.

## Quickstart

To get started with RustFS, follow these steps:

### 1. One-click Installation (Option 1)

curl -O https://rustfs.com/install_rustfs.sh
&&
 bash install_rustfs.sh

### 2. Docker Quick Start (Option 2)

The RustFS container runs as a non-root userrustfs(UID10001). If you run Docker with-vto mount a host directory, please ensure the host directory owner is set to10001, otherwise you will encounter permission denied errors.


#
 Create data and logs directories

 mkdir -p data logs


#
 Change the owner of these directories

 chown -R 10001:10001 data logs


#
 Using latest version

 docker run -d -p 9000:9000 -p 9001:9001 -v
$(
pwd
)
/data:/data -v
$(
pwd
)
/logs:/logs rustfs/rustfs:latest


#
 Using specific version

 docker run -d -p 9000:9000 -p 9001:9001 -v
$(
pwd
)
/data:/data -v
$(
pwd
)
/logs:/logs rustfs/rustfs:1.0.0-alpha.76

If you usepodmaninstead of docker, you can install the RustFS with the below command

 podman run -d -p 9000:9000 -p 9001:9001 -v
$(
pwd
)
/data:/data -v
$(
pwd
)
/logs:/logs rustfs/rustfs:latest

You can also use Docker Compose. Using thedocker-compose.ymlfile in the root directory:

docker compose --profile observability up -d

Similarly, you can run the command with podman

podman compose --profile observability up -d

NOTE: We recommend reviewing thedocker-compose.ymlfile before running. It defines several services including Grafana, Prometheus, and Jaeger, which are helpful for RustFS observability. If you wish to start Redis or Nginx containers, you can specify the corresponding profiles.

### 3. Build from Source (Option 3) - Advanced Users

For developers who want to build RustFS Docker images from source with multi-architecture support:

#
 Build multi-architecture images locally

./docker-buildx.sh --build-arg RELEASE=latest

#
 Build and push to registry

./docker-buildx.sh --push

#
 Build specific version

./docker-buildx.sh --release v1.0.0 --push

#
 Build for custom registry

./docker-buildx.sh --registry your-registry.com --namespace yourname --push

Thedocker-buildx.shscript supports:

* Multi-architecture builds:linux/amd64,linux/arm64
* Automatic version detection: Uses git tags or commit hashes
* Registry flexibility: Supports Docker Hub, GitHub Container Registry, etc.
* Build optimization: Includes caching and parallel builds

You can also use Make targets for convenience:

make docker-buildx
#
 Build locally

make docker-buildx-push
#
 Build and push

make docker-buildx-version VERSION=v1.0.0
#
 Build specific version

make help-docker
#
 Show all Docker-related commands

Heads-up (macOS cross-compilation): macOS keeps the defaultulimit -nat 256, socargo zigbuildor./build-rustfs.sh --platform ...may fail withProcessFdQuotaExceededwhen targeting Linux. The build script attempts to raise the limit automatically, but if you still see the warning, runulimit -n 4096(or higher) in your shell before building.

### 4. Build with Helm Chart (Option 4) - Cloud Native

Follow the instructions in theHelm Chart READMEto install RustFS on a Kubernetes cluster.

### 5. Nix Flake (Option 5)

If you haveNix with flakes enabled:

#
 Run directly without installing

nix run github:rustfs/rustfs

#
 Build the binary

nix build github:rustfs/rustfs
./result/bin/rustfs --help

#
 Or from a local checkout

nix build
nix run

### 6. X-CMD (Option 6)

If you are anx-cmduser:

#
 Run directly without installing

x rustfs

#
 Download the binary and install it to the global environment

x env use rustfs
rustfs --help

### Accessing RustFS

1. Access the Console: Open your web browser and navigate tohttp://localhost:9001to access the RustFS console.* Default credentials:rustfsadmin/rustfsadmin
2. Create a Bucket: Use the console to create a new bucket for your objects.
3. Upload Objects: You can upload files directly through the console or use S3-compatible APIs/clients to interact with your RustFS instance.

NOTE: To access the RustFS instance viahttps, please refer to theTLS Configuration Docs.

## Documentation

For detailed documentation, including configuration options, API references, and advanced usage, please visit ourDocumentation.

## Getting Help

If you have any questions or need assistance:

* Check theFAQfor common issues and solutions.
* Join ourGitHub Discussionsto ask questions and share your experiences.
* Open an issue on ourGitHub Issuespage for bug reports or feature requests.

## Links

* Documentation- The manual you should read
* Changelog- What we broke and fixed
* GitHub Discussions- Where the community lives

## Contact

* Bugs:GitHub Issues
* Business:hello@rustfs.com
* Jobs:jobs@rustfs.com
* General Discussion:GitHub Discussions
* Contributing:CONTRIBUTING.md

## Contributors

RustFS is a community-driven project, and we appreciate all contributions. Check out theContributorspage to see the amazing people who have helped make RustFS better.

## Star History

## License

Apache 2.0

RustFSis a trademark of RustFS, Inc. All other trademarks are the property of their respective owners.

## About

🚀2.3x faster than MinIO for 4KB object payloads. RustFS is an open-source, S3-compatible high-performance object storage system supporting migration and coexistence with other S3-compatible platforms such as MinIO and Ceph.

rustfs.com/download/

### Topics

 rust

 filesystem

 bigdata

 s3

 minio

 cloud-native

 objectstorage

 object-storage

 multi-cloud

 amazon-s3

 ai-storage

 ai-native

### Resources

 Readme



### License

 Apache-2.0 license


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

24.9k

 stars


### Watchers

64

 watching


### Forks

1.1k

 forks


 Report repository



## Releases

93

tags

### Uh oh!

There was an error while loading.Please reload this page.





## Contributors

### Uh oh!

There was an error while loading.Please reload this page.





## Languages

* Rust98.3%
* Shell1.3%
* Makefile0.1%
* Python0.1%
* Just0.1%
* PowerShell0.1%
