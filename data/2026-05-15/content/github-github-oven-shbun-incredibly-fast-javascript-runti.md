---
title: 'GitHub - oven-sh/bun: Incredibly fast JavaScript runtime, bundler, test runner, and package manager – all in one · GitHub'
url: https://github.com/oven-sh/bun
site_name: github
content_file: github-github-oven-shbun-incredibly-fast-javascript-runti
fetched_at: '2026-05-15T11:42:13.367593'
original_url: https://github.com/oven-sh/bun
author: oven-sh
description: Incredibly fast JavaScript runtime, bundler, test runner, and package manager – all in one - oven-sh/bun
---

oven-sh

 

/

bun

Public

* NotificationsYou must be signed in to change notification settings
* Fork4.5k
* Star90.4k

 
 
 
 
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

15,360 Commits
15,360 Commits
.buildkite
.buildkite
 
 
.cargo
.cargo
 
 
.claude
.claude
 
 
.cursor
.cursor
 
 
.github
.github
 
 
.vscode
.vscode
 
 
bench
bench
 
 
completions
completions
 
 
dockerhub
dockerhub
 
 
docs
docs
 
 
misctools
misctools
 
 
packages
packages
 
 
patches
patches
 
 
scripts
scripts
 
 
src
src
 
 
test
test
 
 
.aikido
.aikido
 
 
.bk.yaml
.bk.yaml
 
 
.clang-tidy
.clang-tidy
 
 
.clangd
.clangd
 
 
.coderabbit.yaml
.coderabbit.yaml
 
 
.cursorignore
.cursorignore
 
 
.dockerignore
.dockerignore
 
 
.editorconfig
.editorconfig
 
 
.git-blame-ignore-revs
.git-blame-ignore-revs
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.lldbinit
.lldbinit
 
 
.mailmap
.mailmap
 
 
.prettierignore
.prettierignore
 
 
.prettierrc
.prettierrc
 
 
.typos.toml
.typos.toml
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
LATEST
LATEST
 
 
LICENSE.md
LICENSE.md
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
bun.lock
bun.lock
 
 
bunfig.node-test.toml
bunfig.node-test.toml
 
 
bunfig.toml
bunfig.toml
 
 
entitlements.debug.plist
entitlements.debug.plist
 
 
entitlements.plist
entitlements.plist
 
 
flake.lock
flake.lock
 
 
flake.nix
flake.nix
 
 
meta.json
meta.json
 
 
oxlint.json
oxlint.json
 
 
package.json
package.json
 
 
rust-toolchain.toml
rust-toolchain.toml
 
 
rustfmt.toml
rustfmt.toml
 
 
shell.nix
shell.nix
 
 
tsconfig.base.json
tsconfig.base.json
 
 
tsconfig.json
tsconfig.json
 
 
workspace.code-workspace
workspace.code-workspace
 
 
View all files

## Repository files navigation

# Bun

Documentation

  •  

Discord

  •  

Issues

  •  

Roadmap

### Read the docs →

## What is Bun?

Bun is an all-in-one toolkit for JavaScript and TypeScript apps. It ships as a single executable calledbun.

At its core is theBun runtime, a fast JavaScript runtime designed asa drop-in replacement for Node.js. It's written in Zig and powered by JavaScriptCore under the hood, dramatically reducing startup times and memory usage.

bun run index.tsx 
#
 TS and JSX supported out-of-the-box

Thebuncommand-line tool also implements a test runner, script runner, and Node.js-compatible package manager. Instead of 1,000 node_modules for development, you only needbun. Bun's built-in tools are significantly faster than existing options and usable in existing Node.js projects with little to no changes.

bun 
test
 
#
 run tests

bun run start 
#
 run the `start` script in `package.json`

bun install 
<
pkg
>
 
#
 install a package

bunx cowsay 
'
Hello, world!
'
 
#
 execute a package

## Install

Bun supports Linux (x64 & arm64), macOS (x64 & Apple Silicon), and Windows (x64 & arm64).

Linux users— Kernel version 5.6 or higher is strongly recommended, but the minimum is 5.1.

x64 users— if you see "illegal instruction" or similar errors, check ourCPU requirements

#
 with install script (recommended)

curl -fsSL https://bun.com/install 
|
 bash

#
 on windows

powershell -c 
"
irm bun.sh/install.ps1 | iex
"

#
 with npm

npm install -g bun

#
 with Homebrew

brew tap oven-sh/bun
brew install bun

#
 with Docker

docker pull oven/bun
docker run --rm --init --ulimit memlock=-1:-1 oven/bun

### Upgrade

To upgrade to the latest version of Bun, run:

bun upgrade

Bun automatically releases a canary build on every commit tomain. To upgrade to the latest canary build, run:

bun upgrade --canary

View canary build

## Quick links

* IntroWhat is Bun?InstallationQuickstartTypeScriptTypeScript 6
* What is Bun?
* Installation
* Quickstart
* TypeScript
* TypeScript 6
* Templatingbun initbun create
* bun init
* bun create
* Runtimebun runFile types (Loaders)JSXEnvironment variablesBun APIsWeb APIsNode.js compatibilityPluginsWatch mode / Hot ReloadingModule resolutionAuto-installbunfig.tomlDebuggerREPL$ Shell
* bun run
* File types (Loaders)
* JSX
* Environment variables
* Bun APIs
* Web APIs
* Node.js compatibility
* Plugins
* Watch mode / Hot Reloading
* Module resolution
* Auto-install
* bunfig.toml
* Debugger
* REPL
* $ Shell
* Package managerbun installbun addbun removebun updatebun linkbun pmbun outdatedbun publishbun patchbun whybun auditbun infoGlobal cacheGlobal storeIsolated installsWorkspacesCatalogsLifecycle scriptsFilterLockfileScopes and registriesOverrides and resolutionsSecurity scanner API.npmrc
* bun install
* bun add
* bun remove
* bun update
* bun link
* bun pm
* bun outdated
* bun publish
* bun patch
* bun why
* bun audit
* bun info
* Global cache
* Global store
* Isolated installs
* Workspaces
* Catalogs
* Lifecycle scripts
* Filter
* Lockfile
* Scopes and registries
* Overrides and resolutions
* Security scanner API
* .npmrc
* BundlerBun.buildLoadersPluginsMacrosvs esbuildSingle-file executableCSSHTML & static sitesHot Module Replacement (HMR)Full-stack with HTML importsStandalone HTMLBytecode cachingMinifier
* Bun.build
* Loaders
* Plugins
* Macros
* vs esbuild
* Single-file executable
* CSS
* HTML & static sites
* Hot Module Replacement (HMR)
* Full-stack with HTML imports
* Standalone HTML
* Bytecode caching
* Minifier
* Test runnerbun testWriting testsLifecycle hooksMocksSnapshotsDates and timesDOM testingCode coverageConfigurationDiscoveryReportersRuntime Behavior
* bun test
* Writing tests
* Lifecycle hooks
* Mocks
* Snapshots
* Dates and times
* DOM testing
* Code coverage
* Configuration
* Discovery
* Reporters
* Runtime Behavior
* Package runnerbunx
* bunx
* APIHTTP server (Bun.serve)HTTP routingHTTP error handlingHTTP metricsWebSocketsWorkersBinary dataStreamsFile I/O (Bun.file)Archive (tar)SQLite (bun:sqlite)PostgreSQL (Bun.sql)Redis (Bun.redis)S3 Client (Bun.s3)FileSystemRouterTCP socketsUDP socketsGlobalsChild processes (spawn)Cron (Bun.cron)WebViewTranspiler (Bun.Transpiler)HashingColors (Bun.color)ConsoleFFI (bun:ffi)C Compiler (bun:fficc)HTMLRewriterCookies (Bun.Cookie)CSRF (Bun.CSRF)Secrets (Bun.secrets)YAML (Bun.YAML)TOML (Bun.TOML)JSON5JSONLMarkdownImage processingUtilsNode-APIGlob (Bun.Glob)Semver (Bun.semver)DNSfetch API extensions
* HTTP server (Bun.serve)
* HTTP routing
* HTTP error handling
* HTTP metrics
* WebSockets
* Workers
* Binary data
* Streams
* File I/O (Bun.file)
* Archive (tar)
* SQLite (bun:sqlite)
* PostgreSQL (Bun.sql)
* Redis (Bun.redis)
* S3 Client (Bun.s3)
* FileSystemRouter
* TCP sockets
* UDP sockets
* Globals
* Child processes (spawn)
* Cron (Bun.cron)
* WebView
* Transpiler (Bun.Transpiler)
* Hashing
* Colors (Bun.color)
* Console
* FFI (bun:ffi)
* C Compiler (bun:fficc)
* HTMLRewriter
* Cookies (Bun.Cookie)
* CSRF (Bun.CSRF)
* Secrets (Bun.secrets)
* YAML (Bun.YAML)
* TOML (Bun.TOML)
* JSON5
* JSONL
* Markdown
* Image processing
* Utils
* Node-API
* Glob (Bun.Glob)
* Semver (Bun.semver)
* DNS
* fetch API extensions

## Guides

* DeploymentDeploy to VercelDeploy to RailwayDeploy to RenderDeploy to AWS LambdaDeploy to DigitalOceanDeploy to Google Cloud Run
* Deploy to Vercel
* Deploy to Railway
* Deploy to Render
* Deploy to AWS Lambda
* Deploy to DigitalOcean
* Deploy to Google Cloud Run
* BinaryConvert a Blob to a stringConvert a Buffer to a blobConvert a Blob to a DataViewConvert a Buffer to a stringConvert a Blob to a ReadableStreamConvert a Blob to a Uint8ArrayConvert a DataView to a stringConvert a Uint8Array to a BlobConvert a Blob to an ArrayBufferConvert an ArrayBuffer to a BlobConvert a Buffer to a Uint8ArrayConvert a Uint8Array to a BufferConvert a Uint8Array to a stringConvert a Buffer to an ArrayBufferConvert an ArrayBuffer to a BufferConvert an ArrayBuffer to a stringConvert a Uint8Array to a DataViewConvert a Buffer to a ReadableStreamConvert a Uint8Array to an ArrayBufferConvert an ArrayBuffer to a Uint8ArrayConvert an ArrayBuffer to an array of numbersConvert a Uint8Array to a ReadableStream
* Convert a Blob to a string
* Convert a Buffer to a blob
* Convert a Blob to a DataView
* Convert a Buffer to a string
* Convert a Blob to a ReadableStream
* Convert a Blob to a Uint8Array
* Convert a DataView to a string
* Convert a Uint8Array to a Blob
* Convert a Blob to an ArrayBuffer
* Convert an ArrayBuffer to a Blob
* Convert a Buffer to a Uint8Array
* Convert a Uint8Array to a Buffer
* Convert a Uint8Array to a string
* Convert a Buffer to an ArrayBuffer
* Convert an ArrayBuffer to a Buffer
* Convert an ArrayBuffer to a string
* Convert a Uint8Array to a DataView
* Convert a Buffer to a ReadableStream
* Convert a Uint8Array to an ArrayBuffer
* Convert an ArrayBuffer to a Uint8Array
* Convert an ArrayBuffer to an array of numbers
* Convert a Uint8Array to a ReadableStream
* EcosystemUse React and JSXUse Gel with BunUse Prisma with BunUse Prisma Postgres with BunAdd Sentry to a Bun appCreate a Discord botRun Bun as a daemon with PM2Use Drizzle ORM with BunUse Upstash Redis with BunBuild an app with Nuxt and BunBuild an app with Qwik and BunBuild an app with Astro and BunBuild an app with Remix and BunBuild a frontend using Vite and BunBuild an app with Next.js and BunRun Bun as a daemon with systemdBuild an HTTP server using Hono and BunBuild an app with SvelteKit and BunBuild an app with SolidStart and BunBuild an app with TanStack Start and BunBuild an HTTP server using Elysia and BunBuild an HTTP server using StricJS and BunContainerize a Bun application with DockerBuild an HTTP server using Express and BunUse Neon Postgres through Drizzle ORMServer-side render (SSR) a React componentRead and write data to MongoDB using Mongoose and BunUse Neon's Serverless Postgres with Bun
* Use React and JSX
* Use Gel with Bun
* Use Prisma with Bun
* Use Prisma Postgres with Bun
* Add Sentry to a Bun app
* Create a Discord bot
* Run Bun as a daemon with PM2
* Use Drizzle ORM with Bun
* Use Upstash Redis with Bun
* Build an app with Nuxt and Bun
* Build an app with Qwik and Bun
* Build an app with Astro and Bun
* Build an app with Remix and Bun
* Build a frontend using Vite and Bun
* Build an app with Next.js and Bun
* Run Bun as a daemon with systemd
* Build an HTTP server using Hono and Bun
* Build an app with SvelteKit and Bun
* Build an app with SolidStart and Bun
* Build an app with TanStack Start and Bun
* Build an HTTP server using Elysia and Bun
* Build an HTTP server using StricJS and Bun
* Containerize a Bun application with Docker
* Build an HTTP server using Express and Bun
* Use Neon Postgres through Drizzle ORM
* Server-side render (SSR) a React component
* Read and write data to MongoDB using Mongoose and Bun
* Use Neon's Serverless Postgres with Bun
* HTMLRewriterExtract links from a webpage using HTMLRewriterExtract social share images and Open Graph tags
* Extract links from a webpage using HTMLRewriter
* Extract social share images and Open Graph tags
* HTTPHot reload an HTTP serverCommon HTTP server usageWrite a simple HTTP serverConfigure TLS on an HTTP serverSend an HTTP request using fetchProxy HTTP requests using fetch()Start a cluster of HTTP serversStream a file as an HTTP Responsefetch with unix domain sockets in BunUpload files via HTTP using FormDataStreaming HTTP Server with Async IteratorsStreaming HTTP Server with Node.js StreamsServer-Sent Events (SSE) with Bun
* Hot reload an HTTP server
* Common HTTP server usage
* Write a simple HTTP server
* Configure TLS on an HTTP server
* Send an HTTP request using fetch
* Proxy HTTP requests using fetch()
* Start a cluster of HTTP servers
* Stream a file as an HTTP Response
* fetch with unix domain sockets in Bun
* Upload files via HTTP using FormData
* Streaming HTTP Server with Async Iterators
* Streaming HTTP Server with Node.js Streams
* Server-Sent Events (SSE) with Bun
* InstallAdd a dependencyAdd a Git dependencyAdd a peer dependencyAdd a trusted dependencyAdd a development dependencyAdd a tarball dependencyAdd an optional dependencyGenerate a yarn-compatible lockfileConfiguring a monorepo using workspacesInstall a package under a different nameInstall dependencies with Bun in GitHub ActionsUsing bun install with ArtifactoryConfigure git to diff Bun's lockb lockfileOverride the default npm registry for bun installUsing bun install with an Azure Artifacts npm registryMigrate from npm install to bun installConfigure a private registry for an organization scope with bun install
* Add a dependency
* Add a Git dependency
* Add a peer dependency
* Add a trusted dependency
* Add a development dependency
* Add a tarball dependency
* Add an optional dependency
* Generate a yarn-compatible lockfile
* Configuring a monorepo using workspaces
* Install a package under a different name
* Install dependencies with Bun in GitHub Actions
* Using bun install with Artifactory
* Configure git to diff Bun's lockb lockfile
* Override the default npm registry for bun install
* Using bun install with an Azure Artifacts npm registry
* Migrate from npm install to bun install
* Configure a private registry for an organization scope with bun install
* ProcessRead from stdinListen for CTRL+CSpawn a child processListen to OS signalsParse command-line argumentsRead stderr from a child processRead stdout from a child processGet the process uptime in nanosecondsSpawn a child process and communicate using IPC
* Read from stdin
* Listen for CTRL+C
* Spawn a child process
* Listen to OS signals
* Parse command-line arguments
* Read stderr from a child process
* Read stdout from a child process
* Get the process uptime in nanoseconds
* Spawn a child process and communicate using IPC
* Read fileRead a JSON fileCheck if a file existsRead a file as a stringRead a file to a BufferGet the MIME type of a fileWatch a directory for changesRead a file as a ReadableStreamRead a file to a Uint8ArrayRead a file to an ArrayBuffer
* Read a JSON file
* Check if a file exists
* Read a file as a string
* Read a file to a Buffer
* Get the MIME type of a file
* Watch a directory for changes
* Read a file as a ReadableStream
* Read a file to a Uint8Array
* Read a file to an ArrayBuffer
* RuntimeDelete filesRun a Shell CommandImport a JSON fileImport a TOML fileImport a YAML fileImport a JSON5 fileSet a time zone in BunSet environment variablesRe-map import pathsDelete directoriesRead environment variablesImport a HTML file as textInstall and run Bun in GitHub ActionsDebugging Bun with the web debuggerInstall TypeScript declarations for BunDebugging Bun with the VS Code extensionInspect memory usage using V8 heap snapshotsDefine and replace static globals & constantsBuild-time constants with --defineCodesign a single-file JavaScript executable on macOS
* Delete files
* Run a Shell Command
* Import a JSON file
* Import a TOML file
* Import a YAML file
* Import a JSON5 file
* Set a time zone in Bun
* Set environment variables
* Re-map import paths
* Delete directories
* Read environment variables
* Import a HTML file as text
* Install and run Bun in GitHub Actions
* Debugging Bun with the web debugger
* Install TypeScript declarations for Bun
* Debugging Bun with the VS Code extension
* Inspect memory usage using V8 heap snapshots
* Define and replace static globals & constants
* Build-time constants with --define
* Codesign a single-file JavaScript executable on macOS
* StreamsConvert a ReadableStream to JSONConvert a ReadableStream to a BlobConvert a ReadableStream to a BufferConvert a ReadableStream to a stringConvert a ReadableStream to a Uint8ArrayConvert a ReadableStream to an array of chunksConvert a Node.js Readable to JSONConvert a ReadableStream to an ArrayBufferConvert a Node.js Readable to a BlobConvert a Node.js Readable to a stringConvert a Node.js Readable to an Uint8ArrayConvert a Node.js Readable to an ArrayBuffer
* Convert a ReadableStream to JSON
* Convert a ReadableStream to a Blob
* Convert a ReadableStream to a Buffer
* Convert a ReadableStream to a string
* Convert a ReadableStream to a Uint8Array
* Convert a ReadableStream to an array of chunks
* Convert a Node.js Readable to JSON
* Convert a ReadableStream to an ArrayBuffer
* Convert a Node.js Readable to a Blob
* Convert a Node.js Readable to a string
* Convert a Node.js Readable to an Uint8Array
* Convert a Node.js Readable to an ArrayBuffer
* TestSpy on methods inbun testBail early with the Bun test runnerMock functions inbun testRun tests in watch mode with BunUse snapshot testing inbun testSkip tests with the Bun test runnerUsing Testing Library with BunUpdate snapshots inbun testRun your tests with the Bun test runnerSet the system time in Bun's test runnerSet a per-test timeout with the Bun test runnerMigrate from Jest to Bun's test runnerWrite browser DOM tests with Bun and happy-domMark a test as a "todo" with the Bun test runnerRe-run tests multiple times with the Bun test runnerGenerate code coverage reports with the Bun test runnerimport, require, and test Svelte components with bun testSet a code coverage threshold with the Bun test runnerSelectively run tests concurrently with glob patterns
* Spy on methods inbun test
* Bail early with the Bun test runner
* Mock functions inbun test
* Run tests in watch mode with Bun
* Use snapshot testing inbun test
* Skip tests with the Bun test runner
* Using Testing Library with Bun
* Update snapshots inbun test
* Run your tests with the Bun test runner
* Set the system time in Bun's test runner
* Set a per-test timeout with the Bun test runner
* Migrate from Jest to Bun's test runner
* Write browser DOM tests with Bun and happy-dom
* Mark a test as a "todo" with the Bun test runner
* Re-run tests multiple times with the Bun test runner
* Generate code coverage reports with the Bun test runner
* import, require, and test Svelte components with bun test
* Set a code coverage threshold with the Bun test runner
* Selectively run tests concurrently with glob patterns
* UtilGenerate a UUIDHash a passwordEscape an HTML stringGet the current Bun versionUpgrade Bun to the latest versionEncode and decode base64 stringsCompress and decompress data with gzipSleep for a fixed number of millisecondsDetect when code is executed with BunCheck if two objects are deeply equalCompress and decompress data with DEFLATEGet the absolute path to the current entrypointGet the directory of the current fileCheck if the current file is the entrypointGet the file name of the current fileConvert a file URL to an absolute pathConvert an absolute path to a file URLGet the absolute path of the current fileGet the path to an executable bin file
* Generate a UUID
* Hash a password
* Escape an HTML string
* Get the current Bun version
* Upgrade Bun to the latest version
* Encode and decode base64 strings
* Compress and decompress data with gzip
* Sleep for a fixed number of milliseconds
* Detect when code is executed with Bun
* Check if two objects are deeply equal
* Compress and decompress data with DEFLATE
* Get the absolute path to the current entrypoint
* Get the directory of the current file
* Check if the current file is the entrypoint
* Get the file name of the current file
* Convert a file URL to an absolute path
* Convert an absolute path to a file URL
* Get the absolute path of the current file
* Get the path to an executable bin file
* WebSocketBuild a publish-subscribe WebSocket serverBuild a simple WebSocket serverEnable compression for WebSocket messagesSet per-socket contextual data on a WebSocket
* Build a publish-subscribe WebSocket server
* Build a simple WebSocket server
* Enable compression for WebSocket messages
* Set per-socket contextual data on a WebSocket
* Write fileDelete a fileWrite to stdoutWrite a file to stdoutWrite a Blob to a fileWrite a string to a fileAppend content to a fileWrite a file incrementallyWrite a Response to a fileCopy a file to another locationWrite a ReadableStream to a file
* Delete a file
* Write to stdout
* Write a file to stdout
* Write a Blob to a file
* Write a string to a file
* Append content to a file
* Write a file incrementally
* Write a Response to a file
* Copy a file to another location
* Write a ReadableStream to a file

## Contributing

Refer to theProject > Contributingguide to start contributing to Bun.

## License

Refer to theProject > Licensepage for information about Bun's licensing.

## About

Incredibly fast JavaScript runtime, bundler, test runner, and package manager – all in one

bun.com

### Topics

 react

 nodejs

 javascript

 npm

 bundler

 typescript

 jsx

 zig

 transpiler

 javascriptcore

 bun

 ziglang

### Resources

 Readme

 

### License

 View license
 

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

90.4k

 stars
 

### Watchers

589

 watching
 

### Forks

4.5k

 forks
 

 Report repository

 

## Releases214

Bun v1.3.14

 Latest

 

May 13, 2026

 

+ 213 releases

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Rust46.6%
* Zig32.2%
* C++13.2%
* TypeScript5.1%
* C1.7%
* JavaScript0.8%
* Other0.4%