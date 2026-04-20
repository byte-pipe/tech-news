---
title: 'GitHub - cloudflare/workerd: The JavaScript / Wasm runtime that powers Cloudflare Workers · GitHub'
url: https://github.com/cloudflare/workerd
site_name: github
content_file: github-github-cloudflareworkerd-the-javascript-wasm-runti
fetched_at: '2026-03-17T11:21:37.653272'
original_url: https://github.com/cloudflare/workerd
author: cloudflare
description: The JavaScript / Wasm runtime that powers Cloudflare Workers - cloudflare/workerd
---

cloudflare



/

workerd

Public

* NotificationsYou must be signed in to change notification settings
* Fork565
* Star7.6k




 
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

8,530 Commits
8,530 Commits
.devcontainer
.devcontainer
 
 
.github
.github
 
 
.opencode
.opencode
 
 
.vscode
.vscode
 
 
.zed
.zed
 
 
build
build
 
 
deps/
rust
deps/
rust
 
 
docs
docs
 
 
empty
empty
 
 
fuzzilli
fuzzilli
 
 
githooks
githooks
 
 
images
images
 
 
npm
npm
 
 
patches
patches
 
 
samples
samples
 
 
src
src
 
 
tools
tools
 
 
types
types
 
 
.bazelignore
.bazelignore
 
 
.bazelrc
.bazelrc
 
 
.bazelversion
.bazelversion
 
 
.clang-format
.clang-format
 
 
.clang-tidy
.clang-tidy
 
 
.git-blame-ignore-revs
.git-blame-ignore-revs
 
 
.gitignore
.gitignore
 
 
.npmrc
.npmrc
 
 
.prettierignore
.prettierignore
 
 
.prettierrc.json
.prettierrc.json
 
 
AGENTS.md
AGENTS.md
 
 
BUILD.bazel
BUILD.bazel
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Dockerfile.release
Dockerfile.release
 
 
LICENSE
LICENSE
 
 
MODULE.bazel
MODULE.bazel
 
 
README.md
README.md
 
 
RELEASE.md
RELEASE.md
 
 
SECURITY.md
SECURITY.md
 
 
build-releases.sh
build-releases.sh
 
 
codecov.yml
codecov.yml
 
 
compile_flags.txt
compile_flags.txt
 
 
doxyfile
doxyfile
 
 
justfile
justfile
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
ruff.toml
ruff.toml
 
 
View all files

## Repository files navigation

# 👷workerd, Cloudflare's JavaScript/Wasm Runtime

workerd(pronounced: "worker-dee") is a JavaScript / Wasm server runtime based on the same code that powersCloudflare Workers.

You might use it:

* As an application server, to self-host applications designed for Cloudflare Workers.
* As a development tool, to develop and test such code locally.
* As a programmable HTTP proxy(forward or reverse), to efficiently intercept, modify, and
route network requests.

## Introduction

### Design Principles

* Server-first:Designed for servers, not CLIs nor GUIs.
* Standard-based:Built-in APIs are based on web platform standards, such asfetch().
* Nanoservices:Split your application into components that are decoupled and independently-deployable like microservices, but with performance of a local function call. When one nanoservice calls another, the callee runs in the same thread and process.
* Homogeneous deployment:Instead of deploying different microservices to different machines in your cluster, deploy all your nanoservices to every machine in the cluster, making load balancing much easier.
* Capability bindings:workerdconfiguration uses capabilities instead of global namespaces to connect nanoservices to each other and external resources. The result is code that is more composable -- and immune to SSRF attacks.
* Always backwards compatible:Updatingworkerdto a newer version will never break your JavaScript code.workerd's version number is simply a date, corresponding to the maximum"compatibility date"supported by that version. You can always configure your worker to a past date, andworkerdwill emulate the API as it existed on that date.

Read the blog post to learn more about these principles.

### WARNING:workerdis not a hardened sandbox

workerdtries to isolate each Worker so that it can only access the resources it is configured to access. However,workerdon its own does not contain suitable defense-in-depth against the possibility of implementation bugs. When usingworkerdto run possibly-malicious code, you must run it inside an appropriate secure sandbox, such as a virtual machine. The Cloudflare Workers hosting service in particularuses many additional layers of defense-in-depth.

With that said, if you discover a bug that allows malicious code to break out ofworkerd, please submit it toCloudflare's bug bounty programfor a reward.

## Getting Started

### Supported Platforms

In theory,workerdshould work on any POSIX system that is supported by V8 and Windows.

In practice,workerdis tested on:

* Linux and macOS (x86-64 and arm64 architectures)
* Windows (x86-64 architecture)

On other platforms, you may have to do tinkering to make things work.

### Buildingworkerd

To buildworkerd, you need:

* BazelIf you useBazelisk(recommended), it will automatically download and use the right version of Bazel for building workerd.
* If you useBazelisk(recommended), it will automatically download and use the right version of Bazel for building workerd.
* On Linux:We use the clang/LLVM toolchain to build workerd and support version 19 and higher. Earlier versions of clang may still work, but are not officially supported.Clang 19+ (e.g. packageclang-19on Debian Trixie). If clang is installed asclang-<version>please create a symlink to it in your PATH namedclang, or use--action_env=CC=clang-<version>onbazelcommand lines to specify the compiler name.libc++ 19+ (e.g. packageslibc++-19-devandlibc++abi-19-dev)LLD 19+ (e.g. packagelld-19).python3,python3-distutils, andtcl8.6
* We use the clang/LLVM toolchain to build workerd and support version 19 and higher. Earlier versions of clang may still work, but are not officially supported.
* Clang 19+ (e.g. packageclang-19on Debian Trixie). If clang is installed asclang-<version>please create a symlink to it in your PATH namedclang, or use--action_env=CC=clang-<version>onbazelcommand lines to specify the compiler name.
* libc++ 19+ (e.g. packageslibc++-19-devandlibc++abi-19-dev)
* LLD 19+ (e.g. packagelld-19).
* python3,python3-distutils, andtcl8.6
* On macOS:Xcode 16.3 installation (available on macOS 15 and higher). Building with just the Xcode Command Line Tools is not being tested, but should work too.Homebrew installedtcl-tkpackage (provides Tcl 8.6)
* Xcode 16.3 installation (available on macOS 15 and higher). Building with just the Xcode Command Line Tools is not being tested, but should work too.
* Homebrew installedtcl-tkpackage (provides Tcl 8.6)
* On Windows:InstallApp Installerfrom the Microsoft Store for thewingetpackage manager and then runinstall-deps.batfrom an administrator prompt to install
bazelisk, LLVM, and other dependencies required to build workerd on Windows.Addstartup --output_user_root=C:/tmpto the.bazelrcfile in your user directory.When developing at the command-line, runbazel-env.batin your shell first
to select tools and Windows SDK versions before running bazel.
* InstallApp Installerfrom the Microsoft Store for thewingetpackage manager and then runinstall-deps.batfrom an administrator prompt to install
bazelisk, LLVM, and other dependencies required to build workerd on Windows.
* Addstartup --output_user_root=C:/tmpto the.bazelrcfile in your user directory.
* When developing at the command-line, runbazel-env.batin your shell first
to select tools and Windows SDK versions before running bazel.

You may then buildworkerdat the command-line with:

bazel build //src/workerd/server:workerd

You can pass--config=releaseto compile in release mode:

bazel build //src/workerd/server:workerd --config=release

You can also build from within Visual Studio Code using the instructions indocs/vscode.md.

The compiled binary will be located atbazel-bin/src/workerd/server/workerd.

If you run a Bazel build before you've installed some dependencies (like clang or libc++), and then you install the dependencies, you must resync locally cached toolchains, or clean Bazel's cache, otherwise you might get strange errors:

bazel fetch --configure --force

If that fails, you can try:

bazel clean --expunge

The cache will now be cleaned and you can try building again.

If you have a fairly recent clang packages installed you can build a more performant release
version of workerd:

bazel build --config=thin-lto //src/workerd/server:workerd

### Configuringworkerd

workerdis configured using a config file written in Cap'n Proto text format.

A simple "Hello World!" config file might look like:

using
 Workerd =
import

"/workerd/workerd
.
capnp"
;

const
 config
:Workerd.Config
 = (
 services = [
 (name =
"main"
, worker = .mainWorker),
 ],

 sockets = [

#
 Serve HTTP on port 8080.

 ( name =
"http"
,
 address =
"*:8080"
,
 http = (),
 service =
"main"

 ),
 ]
);

const
 mainWorker
:Workerd.Worker
 = (
 serviceWorkerScript = embed
"hello
.
js"
,
 compatibilityDate =
"2023-02-28"
,

#
 Learn more about compatibility dates at:


#
 https://developers.cloudflare.com/workers/platform/compatibility-dates/

);

Wherehello.jscontains:

addEventListener
(
"fetch"
,

event

=>

{


event
.
respondWith
(
new

Response
(
"Hello World"
)
)
;

}
)
;

Complete reference documentation is provided by the comments in workerd.capnp.

There is also a library of sample config files.

### Runningworkerd

To serve your config, do:

workerd serve my-config.capnp

For more details about command-line usage, useworkerd --help.

Prebuilt binaries are distributed vianpm. Runnpx workerd ...to use these. If you're running a prebuilt binary, you'll need to make sure your system has the right dependencies installed:

* On Linux:glibc 2.35 or higher (already included on e.g. Ubuntu 22.04, Debian Bookworm)
* glibc 2.35 or higher (already included on e.g. Ubuntu 22.04, Debian Bookworm)
* On macOS:macOS 13.5 or higherThe Xcode command line tools, which can be installed withxcode-select --install
* macOS 13.5 or higher
* The Xcode command line tools, which can be installed withxcode-select --install
* x86_64 CPU with at least SSE4.2 and CLMUL ISA extensions, or arm64 CPU with CRC extension (enabled by default under armv8.1-a). These extensions are supported by all recent x86 and arm64 CPUs.

### Local Worker development withwrangler

You can useWrangler(v3.0 or greater) to develop Cloudflare Workers locally, usingworkerd. First, run the following command to configure Miniflare to use this build ofworkerd.

export MINIFLARE_WORKERD_PATH="<WORKERD_REPO_DIR>/bazel-bin/src/workerd/server/workerd"

Then, run:

wrangler dev

### Serving in production

workerdis designed to be unopinionated about how it runs.

One good way to manageworkerdin production is usingsystemd. Particularly useful issystemd's ability to open privileged sockets onworkerd's behalf while running the service itself under an unprivileged user account. To help with this,workerdsupports inheriting sockets from the parent process using the--socket-fdflag.

Here's an example system service file, assuming your config defines two sockets namedhttpandhttps:

#
 /etc/systemd/system/workerd.service

[Unit]
Description=workerd runtime
After=local-fs.target remote-fs.target network-online.target
Requires=local-fs.target remote-fs.target workerd.socket
Wants=network-online.target

[Service]
Type=exec
ExecStart=/usr/bin/workerd serve /etc/workerd/config.capnp --socket-fd http=3 --socket-fd https=4
Sockets=workerd.socket

#
 If workerd crashes, restart it.

Restart=always

#
 Run under an unprivileged user account.

User=nobody
Group=nogroup

#
 Hardening measure: Do not allow workerd to run suid-root programs.

NoNewPrivileges=true

[Install]
WantedBy=multi-user.target

And corresponding sockets file:

#
 /etc/systemd/system/workerd.socket

[Unit]
Description=sockets
for
 workerd
PartOf=workerd.service

[Socket]
ListenStream=0.0.0.0:80
ListenStream=0.0.0.0:443

[Install]
WantedBy=sockets.target

Once these files are in place you can enable the service -- see the systemd documentation or ask your favorite LLM for details.

## About

The JavaScript / Wasm runtime that powers Cloudflare Workers

blog.cloudflare.com/workerd-open-source-workers-runtime/

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

7.6k

 stars


### Watchers

62

 watching


### Forks

565

 forks


 Report repository



## Releases411

v1.20260317.1

 Latest



Mar 17, 2026



+ 410 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





## Used by90.4k

 + 90,372


## Contributors

### Uh oh!

There was an error while loading.Please reload this page.





## Languages

* C++52.4%
* JavaScript21.9%
* TypeScript18.9%
* Starlark1.9%
* Rust1.8%
* Python1.4%
* Other1.7%
