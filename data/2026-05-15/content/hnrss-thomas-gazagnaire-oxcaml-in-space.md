---
title: 'Thomas Gazagnaire :: O(x)Caml in Space'
url: https://gazagnaire.org/blog/2026-05-14-borealis.html
site_name: hnrss
content_file: hnrss-thomas-gazagnaire-oxcaml-in-space
fetched_at: '2026-05-15T19:34:10.888648'
original_url: https://gazagnaire.org/blog/2026-05-14-borealis.html
author: Thomas Gazagnaire
date: '2026-05-15'
description: 'On 23 April, Borealis booted in orbit on DPhi Space''s ClusterGate-2: a pure-OCaml CCSDS protocol stack with end-to-end-encrypted command and control and post-quantum key rotation. OxCaml is what comes next.'
tags:
- hackernews
- hnrss
---

# ThomasGazagnaire

Building Functional Systems from Cloud to Orbit.thomas@gazagnaire.org

## O(x)Caml in Space

2026-05-14 · Discuss onHacker News

#unikernels
#ocaml
#space

On 23 April, our pure-OCamlCCSDSprotocol
stack booted up in low Earth orbit! The project, codenameBorealis, is running insideDPhi Space's
ClusterGate-2payload moduleon the host satellite, with end-to-end-encrypted command and
control and post-quantum key rotation, all implemented in safe
OCaml.

Why does OCaml matter here? Untrusted code running on a satellite
is ahuge security risk,
and OCaml is an ideal safe language to run in space. In hisICFP 2022 keynote,KC Sivaramakrishnanlooked back on thedecade-long engineering effortthat produced OCaml 5, the release that put safe and performant
multi-threading into the OCaml runtime.

KC ended his talk speculating that OCaml 5.0 would go to the
moon, due to its language features that would deliver C/Rust-like
performance on demand while keeping the mathematical rigour of
classic ML. Here at Parsimoni, we took his words a bit too
literally :-)

Closing slide of KC Sivaramakrishnan's 
ICFP 2022 keynote
: the arrow from OCaml 5.0 to the moon, and the metaphor that gave this post its title.

Borealis's first boot on DPhi Space's mission-ops dashboard, 23 April 2026. The first time a pure-OCaml CCSDS stack ran in 
space
!

The host satellite circles the Earth every ninety minutes or so. A few
months afterVirgile Roblesand I hacked on
this over Christmas, we (virtually) jumped around when we saw
this:

2026-04-23 18:48:06 SpaceOS/Borealis (BPv7, BPSec, OTAR) by Parsimoni
2026-04-23 18:48:06 ClusterGate-2 proxy [single iteration]
2026-04-23 18:48:06 Config: scid=100, tm_vcid=0, tc_vcid=4, tm_spi=1, tc_spi=2, tm_frame_len=1115
2026-04-23 18:48:06 Session keys: EK=0x0100 AK=0x0101 active
2026-04-23 18:48:09 Telemetry health: { ... "status": "healthy" }

## What is actually running

Borealis is a daemon. On both the ground and the satellite it
speaks a normal client-server protocol (telemetry queries,
commands and responses, OTAR rekey requests), the same shape as
any production server. What is unusual is the wire underneath.

The protocol stack is a pure-OCaml implementation ofCCSDS, the protocol
family that links spacecraft to the ground. It covers every
layer from radio framing up through Bundle Protocol and the
security extensions on top; the binary formats are described asocaml-wirecodecs.

On ClusterGate-2, only the upper layers of that stack are
exercised. The satellite has no network connectivity from
outside. The only ground link is filesystem upload and download
via DPhi's API: a file written to the uplink directory is
forwarded by DPhi on the next pass, and downlink works the same
way. Borealis treats that filesystem as a delay-tolerant network.
Every command, response, telemetry sample and image chunk is
serialised into aBPv7bundle and
written to disk; DPhi forwards the file as opaque bytes.

BPSecwraps each
bundle in two extension blocks: one encrypts the payload, the
other authenticates it. Sequence numbers
reject replays, and the pre-shared keys (rotated by OTAR, below)
keep the routing path out of the trust path. The satellite operator sees only opaque bundle bytes; nothing in
the routing path can read, modify, forge or substitute the
contents.

This matters because we are tenants on someone else's hardware.
On ahosted-payload
satellitemultiple tenants
share a single bus, and container isolation alone would not
suffice. A shared Linux kernel means kernel-level CVEs regularly
break the tenant boundary, and the same primitives keep
resurfacing in new forms:Dirty
Frag(a universal Linux LPE published
this year),Fragnesia(a close cousin in the same family), and"Copy Fail",
a Linux kernel privilege escalation disclosed in late April that
hit every major distribution at once. Earlier rounds
(Dirty Pipein 2022, thenf_tables use-after-freeexploited for container escape in 2024) suggest there will be
more. On a ground server you can run
the package manager and reboot; in orbit, kernel patching is its
own delivery problem with its own delay, and is sometimes not
possible at all. The cryptographic
envelope around each bundle is the only durable guarantee.

Beyond confidentiality and authenticity, the long-mission threat
model needs key rotation. Borealis supports OTAR (Over-The-Air
Rekeying) for its post-quantum signing keys
(ML-DSA-65). Those keys live for the life of the satellite (ten
to fifteen years), which is why NASA'sSpace System Protection Standard (NASA-STD-1006A)treats post-quantum command authentication as a requirement
rather than a future option. OTAR lets us rotate the post-quantum
keys without re-flashing the satellite. To our knowledge this will bethe first public in-orbit demonstration of post-quantum OTAR;
we plan to exercise the rotation on a later pass.

Borealis runs as a guest on DPhi's hosted-payload module: an Arm
SoC (four Cortex-A53 cores, 4 GB RAM) running Linux. The
flight binary is 5-10 MB, statically linked, shipped as aFROM scratchDocker image. It polls the bus for telemetry
(angle, speed, position) and an onboard camera (a low-quality
fish-eye, good for demos only). The core of the satellite-side
loop looks like this:

let send_telemetry t ~prefix payload =
 let bundle =
 make_bundle t ~source:Eid.sat_telem
 ~destination:Eid.ground_telem ~payload
 in
 match protect_bundle t bundle with
 | Ok protected ->
 ignore (write_bundle t ~dir:(downlink_dir t.config) ~prefix protected)
 | Error _ -> log t "Failed to protect telemetry bundle"

protect_bundleapplies BPSec with keys from the SDLS Security
Association, the cryptographic parameters ground and satellite
agreed on at provisioning. If any of that fails, no bundle leaves
the satellite.

The uplink path mirrors the downlink path. The satellite reads
bundles from/data/uplink/, unprotects each with BPSec, and
routes by destination at the bundle layer:

if dest = Eid.sat_cmd then handle_command t payload
else if dest = Eid.sat_otar then handle_otar t payload
else log t "Unknown destination"

Text commands are short UTF-8 strings parsed into an ADT; the
typechecker enforces exhaustive dispatch:

type cmd = Ping | Check | Capture | Halt

let dispatch t = function
 | Ping -> send_response t ~prefix:"pong" "PONG"
 | Check -> run_self_check t
 | Capture -> capture_and_send t
 | Halt -> t.shutdown_requested <- true

Adding a new command means adding a constructor; the compiler
then flags every place it is not yet handled.

OTAR rekey messages take the other branch. The payload is binary
rather than text, encrypted under a master key that was loaded
onto the satellite at integration time and lives in process
memory on the module (the module has no TPM or secure element,
because building a radiation-tolerant one is still an open
hardware problem). The satellite decrypts the new keys, holds them in a
staging slot, and activates them. The current flight loop
activates on receipt; the protocol also supports a separate
ground-driven activation step where the operator verifies the
install before committing, and switching to that path is a
flight-loop change, not new code.

The master key itself has no rotation path. It was installed on
the payload before the satellite was mated to the launcher, and
there is no more-trusted channel to deliver a new one once the
spacecraft is in orbit. If the master key is lost, this stack is
unreachable. That is the honest failure mode for a long mission
with no hardware-backed key storage.

## What is coming next: OxCaml

OxCamlis Jane Street's compiler branch on
top of OCaml. Its mode system matters on the satellite hot path.
Locality lets us mark allocations stack-bound, so they never
reach the heap and never reach the GC. Uniqueness and
capabilities track shared mutable state in the type system,
turning data races into compile-time errors on the parallel parts
of the stack.

The hot path on the hosted-payload module is CCSDS dispatch:
every CFDP segment, every COP-1 frame, every camera packet flows
through a Space Packet header decode and an APID-based routing
step before the payload reaches the application logic.
Real-time on-board dispatch with hard scheduling deadlines on
every pass is exactly the workload the EUORCHIDEHorizon Europe project was
set up to address (the consortium where this on-board work first
started insideTarides, and which
eventually led us to spinParsimoniout
as a dedicated space-software company).

 Per-packet latency on the CCSDS dispatch hot path:
 decoding a Space Packet primary header into a 3-field record
 and routing by APID. Stock OCaml versus OxCaml with the same
 code annotated 
exclave_ stack_
. Measured on a
 laptop, not the flight module.
 

Switching to OxCaml withexclave_ stack_annotations drops
p99.9 latency from29 ns to 9 ns per packeton the dispatch
hot path, and removes GC pressure entirely (394 minor GCs to
zeroover 25 million packets). Throughput is comparable; the
win is jitter, and on a hosted-payload module with hundreds of
microseconds of jitter budget, that is the whole game.

The recipe is mechanical: turn a per-iteration heap allocation
({ apid; seq_count; data_len }) into a stack-allocated one
(exclave_ stack_ { apid; seq_count; data_len }), and require
the consumer to take it@ local. The type system proves the
record cannot escape the dispatch scope; the compiler emits no
heap traffic; the GC has nothing to collect.

Setup.Apple M5 Max, macOS 25.4. Stock OCaml 5.3.0 versus
5.2.0+ox (Jane Street's OxCaml fork). Workload: 100 000 batches
of 256 CCSDS Space Packet header dispatches each (about 25.6 M
packets total), each routed through an[@inline never]handler
so the record genuinely escapes. Median of 10 runs.

## Why OCaml

Around 70% of severe CVEs in C/C++ codebases trace to memory
corruption (buffer overflows, use-after-free, integer overflows),
based onMicrosoft's MSRC analysis (2019)andChromium's 2020 study.
Our security extensions (SDLS, BPSec, and OTAR) all handle
ciphertexts and key material, which is exactly where memory bugs
hurt most. The C-based incumbent in this domain,NASA CryptoLib, has had its
own such bugs: for instance,a heap buffer overflow in the TC frame parser,
triggered by an integer underflow on a crafted frame. An OCaml
implementation removes that class of attack surface from the
application logic by construction. The runtime, the kernel
underneath, and the bootloader are still C and still in the TCB:
memory safety helps where it helps, and is not a substitute for a
trusted compute base audit.

Beyond what OCaml gives us today, the language itself keeps
advancing.Jane Streetmaintains OxCaml, an
experimental branch of OCaml. Its design goal is safe,
predictable control over the performance-critical parts of a
program, opt-in only where you need it, and still in OCaml:
every valid OCaml program is also a valid OxCaml program.OxCaml Labs(Anil
Madhavapeddy's group at Cambridge) andFP Launchpad(KC Sivaramakrishnan's
lab at IIT Madras) are pushingOCamlforward;Tarides upstreams the pieces that are readyinto the mainline.

I somehow focused on the moon :-) Going to orbit first meant
prioritising correctness over performance, because protocol bugs
in orbit are expensive to fix. The defence runs through every
layer of the stack: type checking, formally verified
cryptographic primitives
(libcrux,fiat-crypto), interop
testing, anddependency audits.

Take three of those layers as concrete examples. The wire-format
codecs are generated from a typed schema, reject malformed bytes
at decode time, and feed Microsoft'sEverParseparser
generator, which produces C validators formally verified inF*. The protocol state machines are
encoded asGADTs, so
the typechecker rejects invalid transitions at compile time. An
interop pipeline runs against existing reference implementations,
catching what the type system cannot express and surfacing
defects in upstream libraries along the way.

Beyond what these layers catch, the functional core lets us ship
the same code as flight software, ground software, and test
oracle. Theprotect_bundleabove is the same function in all
three roles. We feed recorded traffic from one role to the
others and compare outputs byte-for-byte. The OCaml code is also
the reference implementation that other implementations are
validated against. This is thenqsb-TLSapproach (Kaloper-Mersinjak, Mehnert, Madhavapeddy and Sewell,
USENIX Security 2015), and it has held up in TLS for a decade.Nitrokey's NetHSMruns the same OCaml TLS stack in shipping hardware security
modules today.

Borealis is no exception. It might look like we wrote a full
CCSDS protocol stack from zero to in-orbit demonstration in a
couple of months. That is not what happened. The core libraries
come fromMirageOS, and have been
running in production on the ground for the last decade. A library operating system is, by
definition, a large toolset where you pick the pieces you need.

TheASPLOS 2013 unikernels paperasked whether sealed, single-purpose images could improve cloud
infrastructure. A decade later, the same librariesrun in Docker Desktopon hundreds
of millions of laptops. Now they run in space, on ClusterGate-2,
doing the system-level plumbing as a Linux process rather than a
unikernel, in places I did not predict when we first designed
them.

Borealis is one binary in orbit.The next problem is scale:deploying and managing a fleet of specialised payload binaries
across many satellites with the same one-command ease that Docker
brought to Linux on the ground. The harder half is doing that
safely: signed updates from the ground, isolation between
payloads, and attestation of what is actually running. Getting hardware to orbit
is becoming routine; the interesting problems are increasingly in
the software that runs on it, a familiar shift from cloud
computing, where the stack on top of the servers ended up
mattering more than the servers.
That is what we are building next atParsimoni, with collaborators atCambridgeand beyond. I sketched the
wider question inIs Running Untrusted Code on a Satellite a
Good Idea?.

If you are building payload software, considering hosted payloads
on your bus, or want to compare notes on OCaml in flight,talk to meor write to theParsimoni team.

References

* Madhavapeddy et al.,Functional Networking for Millions of Docker Desktops(ICFP 2025).doi:10.1145/3747525
* Madhavapeddy et al.,Unikernels: Library Operating Systems for the Cloud(ASPLOS 2013).doi:10.1145/2451116.2451167
* MirageOS: a library operating system written in OCaml.
* Kaloper-Mersinjak et al.,Not-Quite-So-Broken TLS: Lessons in Re-Engineering a Security Protocol Specification and Implementation(USENIX Security 2015).
* EverParse(Project Everest).
* F*: A Proof-Oriented Programming Language(Microsoft Research).
* CryptoLib: CCSDS Space Data Link Security library(NASA, GitHub).
* OCaml: Memory Safety and Beyond(Tarides blog, December 2023).
* Oxidizing OCaml: Locality(Jane Street Tech Blog).

Related Posts

* From ASPLOS to Orbit: Unikernels Twelve Years Later
* Is Running Untrusted Code on a Satellite a Good Idea?
* Describing Binary Formats in OCaml
* Reimplementing the Space Protocol Stack from Scratch
* Library Operating Systems for the Desktop
* The Journey to OCaml Multicore: Bringing Big Ideas to Life
* Introducing Jane Street's OxCaml Branch