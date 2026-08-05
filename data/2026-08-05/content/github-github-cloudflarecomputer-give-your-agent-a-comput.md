---
title: 'GitHub - cloudflare/computer: Give your agent a computer 👾 · GitHub'
url: https://github.com/cloudflare/computer
site_name: github
content_file: github-github-cloudflarecomputer-give-your-agent-a-comput
fetched_at: '2026-08-05T20:40:01.560150'
original_url: https://github.com/cloudflare/computer
author: cloudflare
description: Give your agent a computer 👾. Contribute to cloudflare/computer development by creating an account on GitHub.
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 cloudflare

 

/

computer

Public

* NotificationsYou must be signed in to change notification settings
* Fork119
* Star2.6k

 
 
 
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

591 Commits
591 Commits
.agents/
skills
.agents/
skills
 
 
.changeset
.changeset
 
 
.github
.github
 
 
docs
docs
 
 
examples
examples
 
 
packages
packages
 
 
script
script
 
 
.editorconfig
.editorconfig
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
COLLABORATORS.md
COLLABORATORS.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
biome.jsonc
biome.jsonc
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
View all files

## Repository files navigation

# Cloudflare Computer

Cloudflare Computer is a virtual filesystem that lives inside a
Durable Object. The Durable Object holds the authoritative state in
SQLite and exposes one pluggable execution surface throughworkspace.runtime. Three backends ship today:

* Containerprojects the SQLite state into a sandbox container as
a real FUSE mount. A sandbox-side daemon (computerd) mounts the state
as a filesystem and syncs changes back over a capnweb RPC channel.
Full Linux userland, real binaries, real network.
* Isolate shellrunsjust-bashin a Dynamic Worker. It reaches the authoritative Workspace over
Workers RPC, so there is no second store or sync round trip.
* Isolate JavaScriptruns an ECMAScript module in a fresh Dynamic
Worker with structured input/results, durable relative imports,
configured libraries, Workspace-backednode:fs/promises, and trustedws:gitandws:artifactsmodules.

A Workspace may register multiple backends under stable IDs.workspace.runtime.exec(source, { backend })is the single execution
entry point; the selected backend defines whethersourceis a shell
command or an ECMAScript module. Backends connect lazily on first use.

Workspace can also be constructed without a backend at all, giving
callers the filesystem on its own.

Important

PREVIEW ONLYThis package is provided as a preview for feedback only.
APIs are unstable and the design is subject to change.

Suitable for experiments, exploration and prototypes. It is NOT suitable
for production use at this time.

The specification underdocs/is forward-looking — read it for
intent, not as description of the code today.

## Using it

If you want to build on Cloudflare Computer, install@cloudflare/computerand follow that
package's README — it has the installation steps, the entrypoint map,
and worked examples of thefsandruntimesurfaces.

To contribute feedback, seeCONTRIBUTING.md.
Approved collaborators should followCOLLABORATORS.mdfor setup, build, and test instructions.

## Examples

Theexamples/directory holds runnable consumers of the
public surface. Each is a Worker workspace with its own README.

* examples/container— runscomputerdinside a
container, mounts a workspace, and talks to a Durable Object over
capnweb. Awrite/read/execHTTP surface.
* examples/worker-shell— same HTTP surface as the
container example, but the shell runsjust-bashin a Dynamic Worker loaded throughenv.LOADER. No container.
* examples/worker-javascript— mirrorsworker-shell, butexecevaluates an ECMAScript module in a Dynamic
Worker instead of running a shell command.
* examples/think— a@cloudflare/thinkchat agent that uses the workspace as its working directory, reachable
from a terminal.
* examples/think-compare-runtimes—
a web UI that runs the same agent task against the container and
worker runtimes side by side.
* examples/tutorial— a step-by-step build: one
endpoint, one agent that writes a markdown recipe card on the host and
runspandocon it in the container to produce a PDF.
* examples/artifacts— generates a Worker project
in a workspace and publishes it to Cloudflare Artifacts as a
clone-ready repo.
* examples/assets— turns a prompt into an image with
Workers AI, writes it to the workspace, and returns a shareable link
through@cloudflare/computer/assets.

## Repository layout

The repo is a small monorepo. Each package has its own README with
package-specific status and usage notes.

* packages/dofs(@cloudflare/dofs) —
Durable Object SQLite-backed virtual filesystem, sync protocol
building blocks, and a@platformatic/vfsprovider for Node.
* packages/rpc(@cloudflare/computer-rpc) — capnweb wire types and
server/client helpers shared between the Durable Object andcomputerd.
* packages/computerd(@cloudflare/computerd) — thecomputerddaemon: a FUSE mount plus
HTTP/WebSocket RPC server that runs inside the sandbox container.
* packages/computer(@cloudflare/computer) — the top-level Computer package
consumed by Durable Objects. Work in progress.
* packages/computer-computerd-linux-x64— private Docker image context for the prebuiltcomputerdlinux-x64
binary. The image, not an npm package, is the release artifact.

## Performance

computerd's FUSE mount beats real disk on metadata-heavy work and
trails it on large sequential I/O. Seedocs/19_performance.mdfor the fullfs-benchnumbers, acloudflare/sandbox-sdknpm installcomparison, and how
to reproduce them.

## Documentation

* docs/— design specification. Forward-looking;
treat as intent.
* docs/19_performance.md— filesystem benchmarks.

## Contributing

We accept bug reports, fix proposals, feature requests, and design
proposals through issues and discussions. We do not accept unsolicited
pull requests. SeeCONTRIBUTING.mdfor the public
contribution paths.

Approved collaborators should followCOLLABORATORS.mdfor setup, formatting, testing,
commit message, and pull request conventions.

If you're working in this repo as an agent, start withAGENTS.mdand the skills under.agents/skills/.

## License

MIT. SeeLICENSE.