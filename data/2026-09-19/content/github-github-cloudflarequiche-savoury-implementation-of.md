---
title: 'GitHub - cloudflare/quiche: 🥧 Savoury implementation of the QUIC transport protocol and HTTP/3 · GitHub'
url: https://github.com/cloudflare/quiche
site_name: github
content_file: github-github-cloudflarequiche-savoury-implementation-of
fetched_at: '2026-09-19T14:10:37.127836'
original_url: https://github.com/cloudflare/quiche
author: cloudflare
description: 🥧 Savoury implementation of the QUIC transport protocol and HTTP/3 - cloudflare/quiche
---

cloudflare

 

/

quiche

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.1k
* Star11.9k

 
 
 
master
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

2,534 Commits
2,534 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.codex/
skills/
quiche-draft-release
.codex/
skills/
quiche-draft-release
 
 
.github
.github
 
 
.opencode
.opencode
 
 
apps
apps
 
 
buffer-pool
buffer-pool
 
 
datagram-socket
datagram-socket
 
 
fuzz
fuzz
 
 
h3i
h3i
 
 
netlog
netlog
 
 
octets
octets
 
 
qlog-dancer
qlog-dancer
 
 
qlog
qlog
 
 
quiche
quiche
 
 
task-killswitch
task-killswitch
 
 
tokio-quiche
tokio-quiche
 
 
tools
tools
 
 
.gitignore
.gitignore
 
 
.gitlab-ci.yml
.gitlab-ci.yml
 
 
.semgrepignore
.semgrepignore
 
 
AGENTS.md
AGENTS.md
 
 
CODEOWNERS
CODEOWNERS
 
 
COPYING
COPYING
 
 
Cargo.toml
Cargo.toml
 
 
Cross.toml
Cross.toml
 
 
Dockerfile
Dockerfile
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
RELEASING.md
RELEASING.md
 
 
catalog-info.yaml
catalog-info.yaml
 
 
clippy.toml
clippy.toml
 
 
quiche.svg
quiche.svg
 
 
rustfmt.toml
rustfmt.toml
 
 
View all files

## Repository files navigation

quicheis an implementation of the QUIC transport protocol and HTTP/3 as
specified by theIETF. It provides a low level API for processing QUIC packets
and handling connection state. The application is responsible for providing I/O
(e.g. sockets handling) as well as an event loop with support for timers.

For more information on how quiche came about and some insights into its design
you can read aposton Cloudflare's blog that goes into some more detail.

## Who uses quiche?

### Cloudflare

quiche powers Cloudflare edge network'sHTTP/3 support. Thecloudflare-quic.comwebsite can be used for
testing and experimentation.

### Android

Android's DNS resolver uses quiche toimplement DNS over HTTP/3.

### curl

quiche can beintegrated into curlto provide support for HTTP/3.

## Getting Started

### Command-line apps

Before diving into the quiche API, here are a few examples on how to use the
quiche tools provided as part of thequiche-appscrate. These are not
suitable for production environments; seedisclaimers and
notes.

After cloning the project according to the command mentioned in thebuildingsection, the client can be run as follows:

 $ cargo run --bin quiche-client -- https://cloudflare-quic.com/

while the server can be run as follows:

 $ cargo run --bin quiche-server -- --cert apps/src/bin/cert.crt --key apps/src/bin/cert.key

(note that the certificate provided is self-signed and should not be used in
production)

Use the--helpcommand-line flag to get a more detailed description of each
tool's options.

### Configuring connections

The first step in establishing a QUIC connection using quiche is creating aConfigobject:

let
 
mut
 config = quiche
::
Config
::
new
(
quiche
::
PROTOCOL_VERSION
)
?
;

config
.
set_application_protos
(
&
[
b"example-proto"
]
)
;

// Additional configuration specific to application and use case...

TheConfigobject controls important aspects of the QUIC connection such
as QUIC version, ALPN IDs, flow control, congestion control, idle timeout
and other properties or features.

QUIC is a general-purpose transport protocol and there are several
configuration properties where there is no reasonable default value. For
example, the permitted number of concurrent streams of any particular type
is dependent on the application running over QUIC, and other use-case
specific concerns.

quiche defaults several properties to zero, applications most likely need
to set these to something else to satisfy their needs using the following:

* set_initial_max_streams_bidi()
* set_initial_max_streams_uni()
* set_initial_max_data()
* set_initial_max_stream_data_bidi_local()
* set_initial_max_stream_data_bidi_remote()
* set_initial_max_stream_data_uni()

Configalso holds TLS configuration. This can be changed by mutators on
the an existing object, or by constructing a TLS context manually and
creating a configuration usingwith_boring_ssl_ctx_builder().

A configuration object can be shared among multiple connections.

### Connection setup

On the client-side theconnect()utility function can be used to create
a new connection, whileaccept()is for servers:

// Client connection.

let
 conn = quiche
::
connect
(
Some
(
&
server_name
)
,
 
&
scid
,
 local
,
 peer
,
 
&
mut
 config
)
?
;

// Server connection.

let
 conn = quiche
::
accept
(
&
scid
,
 
None
,
 local
,
 peer
,
 
&
mut
 config
)
?
;

### Handling incoming packets

Using the connection'srecv()method the application can process
incoming packets that belong to that connection from the network:

let
 to = socket
.
local_addr
(
)
.
unwrap
(
)
;

loop
 
{

 
let
 
(
read
,
 from
)
 = socket
.
recv_from
(
&
mut
 buf
)
.
unwrap
(
)
;

 
let
 recv_info = quiche
::
RecvInfo
 
{
 from
,
 to 
}
;

 
let
 read = 
match
 conn
.
recv
(
&
mut
 buf
[
..read
]
,
 recv_info
)
 
{

 
Ok
(
v
)
 => v
,

 
Err
(
e
)
 => 
{

 
// An error occurred, handle it.

 
break
;

 
}
,

 
}
;

}

### Generating outgoing packets

Outgoing packet are generated using the connection'ssend()method
instead:

loop
 
{

 
let
 
(
write
,
 send_info
)
 = 
match
 conn
.
send
(
&
mut
 out
)
 
{

 
Ok
(
v
)
 => v
,

 
Err
(
quiche
::
Error
::
Done
)
 => 
{

 
// Done writing.

 
break
;

 
}
,

 
Err
(
e
)
 => 
{

 
// An error occurred, handle it.

 
break
;

 
}
,

 
}
;

 socket
.
send_to
(
&
out
[
..write
]
,
 
&
send_info
.
to
)
.
unwrap
(
)
;

}

When packets are sent, the application is responsible for maintaining a
timer to react to time-based connection events. The timer expiration can be
obtained using the connection'stimeout()method.

let
 timeout = conn
.
timeout
(
)
;

The application is responsible for providing a timer implementation, which
can be specific to the operating system or networking framework used. When
a timer expires, the connection'son_timeout()method should be called,
after which additional packets might need to be sent on the network:

// Timeout expired, handle it.

conn
.
on_timeout
(
)
;

// Send more packets as needed after timeout.

loop
 
{

 
let
 
(
write
,
 send_info
)
 = 
match
 conn
.
send
(
&
mut
 out
)
 
{

 
Ok
(
v
)
 => v
,

 
Err
(
quiche
::
Error
::
Done
)
 => 
{

 
// Done writing.

 
break
;

 
}
,

 
Err
(
e
)
 => 
{

 
// An error occurred, handle it.

 
break
;

 
}
,

 
}
;

 socket
.
send_to
(
&
out
[
..write
]
,
 
&
send_info
.
to
)
.
unwrap
(
)
;

}

#### Pacing

It is recommended that applicationspacesending of outgoing packets to
avoid creating packet bursts that could cause short-term congestion and
losses in the network.

quiche exposes pacing hints for outgoing packets through the [at] field
of the [SendInfo] structure that is returned by thesend()method.
This field represents the time when a specific packet should be sent into
the network.

Applications can use these hints by artificially delaying the sending of
packets through platform-specific mechanisms (such as theSO_TXTIMEsocket option on Linux), or custom methods (for example by using user-space
timers).

### Sending and receiving stream data

After some back and forth, the connection will complete its handshake and
will be ready for sending or receiving application data.

Data can be sent on a stream by using thestream_send()method:

if
 conn
.
is_established
(
)
 
{

 
// Handshake completed, send some data on stream 0.

 conn
.
stream_send
(
0
,
 
b"hello"
,
 
true
)
?
;

}

The application can check whether there are any readable streams by using
the connection'sreadable()method, which returns an iterator over all
the streams that have outstanding data to read.

Thestream_recv()method can then be used to retrieve the application
data from the readable stream:

if
 conn
.
is_established
(
)
 
{

 
// Iterate over readable streams.

 
for
 stream_id 
in
 conn
.
readable
(
)
 
{

 
// Stream is readable, read until there's no more data.

 
while
 
let
 
Ok
(
(
read
,
 fin
)
)
 = conn
.
stream_recv
(
stream_id
,
 
&
mut
 buf
)
 
{

 
println
!
(
"Got {} bytes on stream {}"
,
 read
,
 stream_id
)
;

 
}

 
}

}

### HTTP/3

The quicheHTTP/3 moduleprovides a high level API for sending and
receiving HTTP requests and responses on top of the QUIC transport protocol.

Have a look at the [quiche/examples/] directory for more complete examples on
how to use the quiche API, including examples on how to use quiche in C/C++
applications (see below for more information).

## Calling quiche from C/C++

quiche exposes athin C APIon top of the Rust API that can be used to more
easily integrate quiche into C/C++ applications (as well as in other languages
that allow calling C APIs via some form of FFI). The C API follows the same
design of the Rust one, modulo the constraints imposed by the C language itself.

When runningcargo build, a static library calledlibquiche.awill be
built automatically alongside the Rust one. This is fully stand-alone and can
be linked directly into C/C++ applications.

Note that in order to enable the FFI API, theffifeature must be enabled (it
is disabled by default), by passing--features ffitocargo.

## Building

quiche requires Rust 1.88 or later to build. The latest stable Rust release can
be installed usingrustup.

Once the Rust build environment is setup, the quiche source code can be fetched
using git:

 $ git clone https://github.com/cloudflare/quiche

and then built using cargo:

 $ cargo build --examples

cargo can also be used to run the testsuite:

 $ cargo 
test

Note thatBoringSSL, which is used to implement QUIC's cryptographic handshake
based on TLS, needs to be built and linked to quiche. This is done automatically
by theboring-syscrate when building with cargo, but requires thecmakecommand to be available during the build process.

On WindowsNASMis also required. Theofficial BoringSSL
documentationhas
more details.

In alternative you can use your own custom build of BoringSSL by configuring
the BoringSSL directory with theBORING_BSSL_PATHenvironment variable:

 $ BORING_BSSL_PATH=
"
/path/to/boringssl
"
 cargo build --examples

### Building for Android

Building quiche for Android (NDK version 19 or higher, 21 recommended), can be
done usingcargo-ndk(v2.0 or later).

First theAndroid NDKneeds to be installed, either using Android Studio or
directly, and theANDROID_NDK_HOMEenvironment variable needs to be set to the
NDK installation path, e.g.:

 $ 
export
 ANDROID_NDK_HOME=/usr/local/share/android-ndk

Then the Rust toolchain for the Android architectures needed can be installed as
follows:

 $ rustup target add aarch64-linux-android armv7-linux-androideabi i686-linux-android x86_64-linux-android

Note that the minimum API level is 21 for all target architectures.

cargo-ndk(v2.0 or later) also needs to be installed:

 $ cargo install cargo-ndk

Finally the quiche library can be built using the following procedure. Note that
the-t <architecture>and-p <NDK version>options are mandatory.

 $ cargo ndk -t arm64-v8a -p 21 -- build --features ffi

Seebuild_android_ndk19.shfor more information.

### Building for iOS

To build quiche for iOS, you need the following:

* Install Xcode command-line tools. You can install them with Xcode or with the
following command:

 $ xcode-select --install

* Install the Rust toolchain for iOS architectures:

 $ rustup target add aarch64-apple-ios x86_64-apple-ios

* Installcargo-lipo:

 $ cargo install cargo-lipo

To build libquiche, run the following command:

 $ cargo lipo --features ffi

or

 $ cargo lipo --features ffi --release

iOS build is tested in Xcode 10.1 and Xcode 11.2.

### Building Docker images

In order to build the Docker images, simply run the following command:

 $ make docker-build

You can find the quiche Docker images on the following Docker Hub repositories:

* cloudflare/quiche
* cloudflare/quiche-qns

Thelatesttag will be updated whenever quiche master branch updates.

cloudflare/quiche

Provides a server and client installed in /usr/local/bin.

cloudflare/quiche-qns

Provides the script to test quiche within thequic-interop-runner.

## Disclaimers and Notes

⚠️This repository includes a number of client and server example
applications that are provided to demonstrate simple usage of the quiche library
API. They are not intended to be used in production environments; no
performance, security or reliability guarantees are provided.

## Copyright

Copyright (C) 2018-2019, Cloudflare, Inc.

SeeCOPYINGfor the license.