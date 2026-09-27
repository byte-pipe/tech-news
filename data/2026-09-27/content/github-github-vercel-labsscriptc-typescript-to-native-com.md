---
title: 'GitHub - vercel-labs/scriptc: TypeScript-to-Native Compiler · GitHub'
url: https://github.com/vercel-labs/scriptc
site_name: github
content_file: github-github-vercel-labsscriptc-typescript-to-native-com
fetched_at: '2026-09-27T15:32:16.153430'
original_url: https://github.com/vercel-labs/scriptc
author: vercel-labs
description: TypeScript-to-Native Compiler. Contribute to vercel-labs/scriptc development by creating an account on GitHub.
---

vercel-labs

 

/

scriptc

Public

* NotificationsYou must be signed in to change notification settings
* Fork137
* Star5.3k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

735 Commits
735 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github/
workflows
.github/
workflows
 
 
docs
docs
 
 
examples/
native-object
examples/
native-object
 
 
internal/
compatibility
internal/
compatibility
 
 
native/
llvm-codegen
native/
llvm-codegen
 
 
packages
packages
 
 
scripts
scripts
 
 
tests
tests
 
 
.dockerignore
.dockerignore
 
 
.gitignore
.gitignore
 
 
.node-version
.node-version
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
Dockerfile.sandbox
Dockerfile.sandbox
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
RELEASING.md
RELEASING.md
 
 
eslint.config.mjs
eslint.config.mjs
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
tsconfig.base.json
tsconfig.base.json
 
 
vitest.config.ts
vitest.config.ts
 
 
View all files

## Repository files navigation

# scriptc

scriptc compiles TypeScript and JavaScript to typed IR, readable C, textual LLVM IR, native assembly and objects, native executables, and WebAssembly modules. It uses the TypeScript compiler for parsing and type checking. Source outputs require only Node. On macOS 15+ arm64, ordinary LLVM-tier executables use scriptc's bundled helper and precompiled runtime pack; clang is only the platform linker driver and does not compile program or runtime C.

Static builds include a small native runtime, but no Node or JavaScript engine. Code that cannot compile statically is reported as a diagnostic. For npm packages andany-typed code,--dynamicembedsquickjs-ngexplicitly.

scriptc is experimental and targets macOS, Linux, Windows, and WebAssembly via WASI Preview 1.

## Installation

The compiler requires Node.js 24 or newer.--emit=ir|c|llvmneeds only Node.--emit=asm|objuses the matching optional platform helper installed with scriptc on supported macOS, Linux, and Windows hosts (and for WASI), but needs no compiler, archiver, linker, or SDK. Ordinary LLVM-tier executable builds need a platform linker driver and SDK/sysroot, but use the bundled helper plus precompiled runtime pack rather than compiling generated or runtime C. SetSCRIPTC_LINKERto choose that driver. Explicit C builds, LLVM fallbacks,--sanitize, and the deprecatedSCRIPTC_CC=clang|zigcccompatibility route additionally need a C compiler. The executables it produces do not require Node.

$ 
npm install -g scriptc

## Build a program

Createhello.ts:

const
 
who
 
=
 
process
.
argv
.
length
 
>
 
2
 ? 
process
.
argv
[
2
]
 : 
"world"
;

console
.
log
(
`hello, 
${
who
}
`
)
;

Compile and run it in one step:

$ 
scriptc run hello.ts

hello, world

Or write a standalone executable:

$ 
scriptc build hello.ts -o hello

$ 
./hello ctate

hello, ctate

Or stop at a source-level compiler artifact without invoking clang, an archiver, or a linker:

$ 
scriptc build hello.ts --emit=ir 
>
/dev/null

$ 
ls .scriptc/

hello.ir.json

$ 
scriptc build hello.ts --emit=c 
>
/dev/null

$ 
ls .scriptc/

hello.c

hello.ir.json

$ 
scriptc build hello.ts --emit=llvm 
>
/dev/null

$ 
ls .scriptc/

hello.c

hello.ir.json

hello.ll

$ 
scriptc build hello.ts --emit=asm 
>
/dev/null

$ 
ls .scriptc/

hello.c

hello.ir.json

hello.ll

hello.s

$ 
scriptc build hello.ts --emit=obj 
>
/dev/null

$ 
ls .scriptc/

hello.c

hello.ir.json

hello.ll

hello.o

hello.s

Different output kinds accumulate in.scriptc/; rebuilding a kind updates its file.

--emit=objwrites a relocatable program object, not a standalone library. It
has undefinedscr_*runtime references and a requiredscr_runtime_abi_v1marker;scriptc build --lib --profile ...remains the
self-contained archive interface. The helper runs on macOS 15+ arm64 and emits
artifacts with anarm64-apple-macosx14.0.0deployment target. Sanitized
assembly/object
emission is rejected until the helper's AddressSanitizer pipeline matches the
executable path.

External object consumption is experimental. Use--print=native-link-infoto emit the object and print a versioned JSON recipe
containing its target,mainentry, exact@scriptc/runtimesource pack,
required system libraries, FFI inputs, and ABI marker. The recipe never uses
hidden scriptc cache paths. Seeexamples/native-objectfor C-driver and direct Apple-linker builds.

## Use Node APIs

Supported Node APIs compile to the native runtime. For example,server.ts:

import
 
{
 
createServer
 
}
 
from
 
"node:http"
;

const
 
server
 
=
 
createServer
(
(
req
,
 
res
)
 
=>
 
{

 
res
.
setHeader
(
"content-type"
,
 
"application/json"
)
;

 
res
.
end
(
JSON
.
stringify
(
{
 
path
: 
req
.
url
 
}
)
)
;

}
)
;

server
.
listen
(
8080
,
 
(
)
 
=>
 
{

 
console
.
log
(
"listening on http://localhost:8080"
)
;

}
)
;

$ 
scriptc build server.ts -o server

$ 
./server

listening on http://localhost:8080

## Check static coverage

scriptc coverageshows how much of a program can compile statically and gives a coded diagnostic for every dynamic or unsupported site.

$ 
scriptc coverage hello.ts

 statements analyzed 2

 compile statically 2 (100%)

 fully static — this program has no dynamic remainder.

## Build WebAssembly

WASI and other cross-target builds require Zig. Its bundled WASI libc produces a portable WASI Preview 1 module through the production LLVM backend:

Install Zig and make sure thezigexecutable is available on yourPATH.SCRIPTC_CC=zigccis scriptc's selector for invoking Zig'sccsubcommand;zigccis not a standalone executable.

$ 
SCRIPTC_CC=zigcc SCRIPTC_TARGET=wasm32-wasi scriptc build hello.ts --no-keep-c -o hello.wasm 
>
/dev/null

$ 
file hello.wasm

hello.wasm: WebAssembly (wasm) binary module version 0x1 (MVP)

$ 
SCRIPTC_CC=zigcc SCRIPTC_TARGET=wasm32-wasi scriptc run hello.ts

hello, world

The WASI target supports the same executable language tiers as the native targets, including async/await, promises, generators, timers, stdin/readline events, callback and promise filesystem APIs, and--dynamic. APIs that require capabilities absent from portable WASI Preview 1—network sockets/fetch, child processes, OS signals, and filesystem watching—fail before linking withSC3002; sanitizer builds, native FFI, and library-mode archive builds are target diagnostics too. Seeplatform supportfor the precise boundary.

## Use npm packages

Pass--dynamicto embed an npm package's JavaScript in the executable. The result does not readnode_modulesat runtime.

import
 
pc
 
from
 
"picocolors"
;

console
.
log
(
pc
.
green
(
"hello from scriptc"
)
)
;

$ 
npm install picocolors

$ 
scriptc build cli.ts --dynamic -o cli

$ 
./cli

hello from scriptc

## Documentation

See thequickstartandCLI referencefor the complete workflow. The docs also describenpm dependencies,native FFI,platform support, and the currentlimitations.

## Development

$ 
pnpm install 
&&
 pnpm -r build

$ 
vercel link 
&&
 vercel env pull 
#
 writes a project-scoped VERCEL_OIDC_TOKEN

$ 
pnpm test:sandbox

The normal workspace build needs no local LLVM installation. To rebuild a
native helper/runtime pack, install CMake, Ninja, and the pinned LLVM 22
development package on that target host, then run the matching@scriptc/llvm-<platform>and@scriptc/runtime-<platform>build:nativescripts. The macOS full test suite also uses those generated artifacts.

pnpm test:sandboxloads.env.local, preflights Vercel authentication and
project access, and uses the managedvercel/sandbox/universalimage by
default. It installs the repository-pinned Node, pnpm, and LLVM toolchain plus
ScriptC dependencies in each disposable Sandbox before building the uploaded
worktree. SetSCRIPTC_SANDBOX_IMAGEto a fully qualified VCR reference only to use the
optional prebuilt image frompnpm test:sandbox:image.
The prebuilt image keeps the roughly four-minute fast path; cold managed-image
runs take longer because they install the pinned toolchain in each Sandbox.

VERCEL_OIDC_TOKENis preferred. For access-token authentication, setVERCEL_TOKEN,VERCEL_TEAM_ID, andVERCEL_PROJECT_ID; team and project are
never inferred fromSCRIPTC_SANDBOX_IMAGE. The legacy VCR command used bypnpm test:sandbox:imagecannot authenticate with an OIDC JWT, so image builds
useVERCEL_TOKENwhen available or the existing Vercel CLI login; OIDC claims
still select the VCR team and project. The test corpus runs each program
under Node and as a compiled native binary, then compares stdout, stderr, and
exit codes byte for byte. The full gate also runs the corpus with
AddressSanitizer and the runtime reference-count audit.