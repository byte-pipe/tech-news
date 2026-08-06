---
title: 'GitHub - denoland/celld: self-hosted, distributed Durable Objects · GitHub'
url: https://github.com/denoland/celld
site_name: hnrss
content_file: hnrss-github-denolandcelld-self-hosted-distributed-durab
fetched_at: '2026-08-06T12:55:19.577192'
original_url: https://github.com/denoland/celld
date: '2026-08-05'
description: self-hosted, distributed Durable Objects. Contribute to denoland/celld development by creating an account on GitHub.
tags:
- hackernews
- hnrss
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 denoland

 

/

celld

Public

* NotificationsYou must be signed in to change notification settings
* Fork32
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

3 Commits
3 Commits
.github/
workflows
.github/
workflows
 
 
crates
crates
 
 
docs
docs
 
 
examples
examples
 
 
.gitignore
.gitignore
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
View all files

## Repository files navigation

# celld

Self-hosted, distributedDurable Objects.

celld is an open-source daemon that runs Cloudflare Workers and Durable
Objects on your own machines. Each object is its own SQLite database,
addressed by name and replicated to an
S3-compatible bucket you own; nodes coordinate through that bucket alone, with
no control plane or consensus. Because every object is its own small database,
applications shard by construction — the contention and blast-radius failures
of one shared database are designed out, not managed. Idle cells hibernate to
nearly nothing. Learn more atcelld.devor read thedocumentation.

## How it works

Everycelldnode embeds V8 and executes Wrangler bundles. The fleet shares an
S3-compatible bucket containing deployments, cell state, and small ownership
records. Object-storage compare-and-swap ensures that exactly one node owns a
cell at a time, without a membership protocol, failure detector, or consensus
service.

celld continuously replicates each cell's SQLite database to the bucket.
When a cell moves or wakes up, its new owner restores that database and resumes
execution. The bucket is the durable source of truth; nodes are replaceable.

## Install

The installer downloads thecelldbinary (provenance is verifiable withgh attestation verify):

curl -fsSL https://celld.dev/install.sh 
|
 sh

Put~/.local/binon yourPATHif the installer asks you to.

Worker projects deployed withcelld deployneedesbuildonPATH; asset-only projects do not.

The installer keeps verified releases under~/.local/lib/celld/releasesand
atomically switches onecurrentpointer. To remove celld, use the guarded
uninstaller:

curl -fsSL https://celld.dev/uninstall.sh 
|
 sh

## Container

The release image contains thecelldbinary and is published for Linux
x86-64 and ARM64:

docker run --rm ghcr.io/denoland/celld --version

Persist the runtime's local state and pass the standard AWS credential
environment through:

docker volume create celld-state
docker run --rm --network host \
 -e AWS_ACCESS_KEY_ID \
 -e AWS_SECRET_ACCESS_KEY \
 -e AWS_SESSION_TOKEN \
 -e CELLD_WATCH=/var/lib/celld/state \
 -v celld-state:/var/lib/celld \
 ghcr.io/denoland/celld \
 --bucket s3://my-cells-bucket \
 --endpoint https://ACCOUNT.r2.cloudflarestorage.com \
 --region auto \
 --listen 0.0.0.0:8080 \
 --advertise node-a.internal:8080

Drop--endpoint/--regionfor real AWS S3. Behind a load balancer,
give each node a distinct--advertiseits peers can reach.

## Run it

celld uses the standard AWS credential chain. Deploy to an S3-compatible
bucket, then start celld against the same bucket:

celld deploy 
.
 \
 --bucket s3://my-cells-bucket

celld \
 --bucket s3://my-cells-bucket \
 --listen 0.0.0.0:8080 \
 --advertise 10.0.0.12:8080

Use--endpointfor another S3-compatible service and--regionwhen it
cannot be inferred. A fleet runs one application, and every node loads its
latest successfully committed deployment fromdeploy/current.json. Runcelld --helpfor the complete command line.
Deployment objects use the documented types incrates/celld/protocol.rs.celld deployinvokesesbuildfromPATHfor Worker code, accepts the supported
Wrangler config subset—including co-deployed or asset-only static
assets—and writes those objects directly. Every node discovers owners and
peers from bucket leases; there is no account or join service.

Peer HTTP does not terminate TLS. Put every advertised address on a trusted
private network or an encrypted overlay such as WireGuard or Tailscale; do not
publish the peer port directly. A literal public IP is rejected unless--unsafe-public-advertiseis supplied explicitly. The first current node createsfleet/peer-auth.jsonin the bucket. All peer requests are protocol-versioned,
body-bound, HMAC-authenticated, clock-bounded, and replay-protected with that
fleet secret. Treat access to the bucket and its credentials as fleet
administrator access.

## Operate a fleet

celld diagnoseenumerates every node lease by default, then performs a signed
direct probe of each live peer:

celld diagnose --bucket s3://my-cells-bucket

The report keeps checking after an individual failure and distinguishes
expired records, malformed or unsafe advertise addresses, unreachable peers,
and incompatible protocols. It also prints each node's coarse resident-cell,
WebSocket, RSS, CPU, file-descriptor, pressure, and shedding sample. Pass one
or more--peer NODE_IDoptions to restrict the check.

Pressure shedding is opt-in while the first release's safe defaults are being
measured. Set a resident-cell high and low watermark on loaded nodes:

CELLD_MAX_RESIDENT_CELLS=1000 \
CELLD_RESIDENT_LOW_WATER=800 \
celld --bucket s3://my-cells-bucket --listen 0.0.0.0:8080 \
 --advertise node-a.internal:8080

On Linux,CELLD_MAX_RSS_MBandCELLD_MAX_CPU_PERCENTadd process-memory and
CPU triggers; the resident-cell watermark is portable. Under pressure, celld
durably replicates and fences least-recently used idle cells, publishes them as
unowned without resetting their epoch, and refuses to reacquire new unowned
cells until the low watermark is reached. A spare receives no assignment: it
acquires released cells through the same bucket protocol when normal traffic
reaches it. Cells with active work or live host WebSockets are not shed.

## Build from source

cargo build --locked
cargo 
test
 --locked
cargo clippy --all-targets --locked -- -D warnings

The workspace builds thecelldruntime. Its versioned object-storage
protocol lives incrates/celld/protocol.rs. Small Wrangler projects underexamples/exercise the supported Worker and Durable Object surface.

The runtime and compatibility surface are still evolving. Public tests cover
the standalone engine smoke path; conformance against the Workers and Durable
Objects reference behavior, and a deterministic simulation of the distributed
protocol under fault injection, run before each release.

## Contributions

Pull requests are disabled. Coding agents make it too easy to send a large,
low-context change that costs maintainers more time than it saves. Thoughtful
contributions are welcome; please understand the code, keep the patch focused,
and respect the review time you are asking for.

Send agit format-patchattachment tory@deno.com.

Contributor License Agreement: By emailing a patch, you certify that you have
the right to submit it and assign to Deno Land Inc. all rights in the patch
that you can assign. Where a right cannot be assigned, you grant Deno Land
Inc. a perpetual, irrevocable,
worldwide, royalty-free, transferable, sublicensable license to use, modify,
combine, relicense, redistribute, or publish the patch, in whole or in part,
with or without attribution.

## License

Apache-2.0

See thelimitationsandsecuritypages before operating a public fleet.