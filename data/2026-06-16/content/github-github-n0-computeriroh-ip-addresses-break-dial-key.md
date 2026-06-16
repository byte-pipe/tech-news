---
title: 'GitHub - n0-computer/iroh: IP addresses break, dial keys instead. Modular networking stack in Rust. · GitHub'
url: https://github.com/n0-computer/iroh
site_name: github
content_file: github-github-n0-computeriroh-ip-addresses-break-dial-key
fetched_at: '2026-06-16T12:37:07.445526'
original_url: https://github.com/n0-computer/iroh
author: n0-computer
description: IP addresses break, dial keys instead. Modular networking stack in Rust. - n0-computer/iroh
---

n0-computer

 

/

iroh

Public

* NotificationsYou must be signed in to change notification settings
* Fork429
* Star9.1k

 
 
 
 
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

2,513 Commits
2,513 Commits
.cargo
.cargo
 
 
.config
.config
 
 
.github
.github
 
 
.img
.img
 
 
docker
docker
 
 
iroh-base
iroh-base
 
 
iroh-dns-server
iroh-dns-server
 
 
iroh-dns
iroh-dns
 
 
iroh-relay
iroh-relay
 
 
iroh
iroh
 
 
.dockerignore
.dockerignore
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.typos.toml
.typos.toml
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CHANGELOG_old.md
CHANGELOG_old.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
LICENSE-APACHE
LICENSE-APACHE
 
 
LICENSE-MIT
LICENSE-MIT
 
 
Makefile.toml
Makefile.toml
 
 
README.md
README.md
 
 
TRANSPORTS.md
TRANSPORTS.md
 
 
cliff.toml
cliff.toml
 
 
code_of_conduct.md
code_of_conduct.md
 
 
deny.toml
deny.toml
 
 
example.config.toml
example.config.toml
 
 
release.toml
release.toml
 
 
View all files

## Repository files navigation

### less net work for networks

### Docs Site|Rust Docs

## What is iroh?

Iroh gives you an API for dialing by public key.
You say “connect to that phone”, iroh will find & maintain the fastest connection for you, regardless of where it is.

### Hole-punching

The fastest route is a direct connection, so if necessary, iroh tries to hole-punch.
Should this fail, it can fall back to an open ecosystem of public relay servers.
To ensure these connections are as fast as possible, wecontinuously measure iroh.

### Built onQUIC

Iroh usesnoqto establishQUICconnections between endpoints.
This way you get authenticated encryption, concurrent streams with stream priorities, a datagram transport and avoid head-of-line-blocking out of the box.

## Compose Protocols

Use pre-existing protocols built on iroh instead of writing your own:

* iroh-blobsforBLAKE3-based content-addressed blob transfer scaling from kilobytes to terabytes
* iroh-gossipfor establishing publish-subscribe overlay networks that scale, requiring only resources that your average phone can handle
* iroh-docsfor an eventually-consistent key-value store ofiroh-blobsblobs

## Getting Started

### Rust Library

It's easiest to use iroh from rust.
Install it usingcargo add iroh, then on the connecting side:

const
 
ALPN
:
 
&
[
u8
]
 = 
b"iroh-example/echo/0"
;

let
 endpoint = 
Endpoint
::
bind
(
)
.
await
?
;

// Open a connection to the accepting endpoint

let
 conn = endpoint
.
connect
(
addr
,
 
ALPN
)
.
await
?
;

// Open a bidirectional QUIC stream

let
 
(
mut
 send
,
 
mut
 recv
)
 = conn
.
open_bi
(
)
.
await
?
;

// Send some data to be echoed

send
.
write_all
(
b"Hello, world!"
)
.
await
?
;

send
.
finish
(
)
?
;

// Receive the echo

let
 response = recv
.
read_to_end
(
1000
)
.
await
?
;

assert_eq
!
(
&
response
,
 
b"Hello, world!"
)
;

// As the side receiving the last application data - say goodbye

conn
.
close
(
0u32
.
into
(
)
,
 
b"bye!"
)
;

// Close the endpoint and all its connections

endpoint
.
close
(
)
.
await
;

And on the accepting side:

let
 endpoint = 
Endpoint
::
bind
(
)
.
await
?
;

let
 router = 
Router
::
builder
(
endpoint
)

 
.
accept
(
ALPN
.
to_vec
(
)
,
 
Arc
::
new
(
Echo
)
)

 
.
spawn
(
)

 
.
await
?
;

// The protocol definition:

#
[
derive
(
Debug
,
 
Clone
)
]

struct
 
Echo
;

impl
 
ProtocolHandler
 
for
 
Echo
 
{

 
async
 
fn
 
accept
(
&
self
,
 
connection
:
 
Connection
)
 -> 
Result
<
(
)
>
 
{

 
let
 
(
mut
 send
,
 
mut
 recv
)
 = connection
.
accept_bi
(
)
.
await
?
;

 
// Echo any bytes received back directly.

 
let
 bytes_sent = tokio
::
io
::
copy
(
&
mut
 recv
,
 
&
mut
 send
)
.
await
?
;

 send
.
finish
(
)
?
;

 connection
.
closed
(
)
.
await
;

 
Ok
(
(
)
)

 
}

}

The full example code with more comments can be found atecho.rs.

Or use one of the pre-existing protocols, e.g.iroh-blobsoriroh-gossip.

### Other Languages

If you want to use iroh from other languages, make sure to check outiroh-ffi, the repository for FFI bindings.

### Links

* Introducing Iroh (video)
* Iroh Documentation
* Iroh Examples
* Iroh Experiments

## Repository Structure

This repository contains a workspace of crates:

* iroh: The core library for hole-punching & communicating with relays.
* iroh-relay: The relay client and server implementation. This is the code we run in production for the public relays (and you can, too!).
* iroh-base: Common types likeEndpointIdorRelayUrl.
* iroh-dns-server: DNS server implementation powering the DNS/Pkarr address lookup for EndpointIds, running at dns.iroh.link.

## License

Copyright 2025 N0, INC.

This project is licensed under either of

* Apache License, Version 2.0, (LICENSE-APACHEorhttp://www.apache.org/licenses/LICENSE-2.0)
* MIT license (LICENSE-MITorhttp://opensource.org/licenses/MIT)

at your option.

## Contribution

Unless you explicitly state otherwise, any contribution intentionally submitted for inclusion in this project by you, as defined in the Apache-2.0 license, shall be dual licensed as above, without any additional terms or conditions.

## About

IP addresses break, dial keys instead. Modular networking stack in Rust.

iroh.computer

### Topics

 rust

 tags

 realtime

 memes

 p2p

 quic

 multipath

 holepunching

 tagsoftags

 does-anyone-read-these

### Resources

 Readme

 

### License

 Apache-2.0, MIT licenses found
 

### Licenses found

Apache-2.0

LICENSE-APACHE

 

MIT

LICENSE-MIT

 

### Code of conduct

 Code of conduct
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

9.1k

 stars
 

### Watchers

62

 watching
 

### Forks

429

 forks
 

 Report repository

 

## Releases66

v1.0.0 - Dial keys, not IPs

 Latest

 

Jun 15, 2026

 

+ 65 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Rust99.6%
* Other0.4%