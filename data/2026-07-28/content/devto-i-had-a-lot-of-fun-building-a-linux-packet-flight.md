---
title: I Had a Lot of Fun Building a Linux Packet Flight Recorder - DEV Community
url: https://dev.to/copyleftdev/i-had-a-lot-of-fun-building-a-linux-packet-flight-recorder-k44
site_name: devto
content_file: devto-i-had-a-lot-of-fun-building-a-linux-packet-flight
fetched_at: '2026-07-28T19:33:29.789554'
original_url: https://dev.to/copyleftdev/i-had-a-lot-of-fun-building-a-linux-packet-flight-recorder-k44
author: Don Johnson
date: '2026-07-28'
description: I built skbx to follow packets through the Linux kernel, preserve what it observed, and replay the evidence later without root. Tagged with linux, networking, ai, devops.
tags: '#linux, #networking, #ai, #devops'
---

Uses Rust and eBPF to replay kernel packet paths

Some projects begin with a roadmap.skbxbegan with me falling into a Linuxnetworking rabbit hole and enjoying it much more than I expected.

The question was simple:

Where did this packet actually go?

The answer was not.

A packet can pass through network namespaces, routing decisions, Netfilter,traffic control, XDP programs, tunnels, clones, copies, and drop paths. Apacket capture at one interface can be completely correct while still showingonly one part of that journey.

I wanted to see more of the journey. Then I wanted to save what I saw, replayit later without root, and know whether the capture itself had lostobservations.

That becameskbx.

## The short version

skbxis a Linux packet-path flight recorder built with Rust and CO-RE eBPF.

During a live capture, it observes kernel networking functions and writes anappend-only JSONL evidence stream. Afterward, that stream can be replayed andinspected without loading another eBPF program.

live traffic
 ↓
CO-RE eBPF observations
 ↓
bounded traceq JSONL
 ↓
replay → route patterns → explain an event

Enter fullscreen mode

Exit fullscreen mode

It can observe:

* kernel functions handling ansk_buff;
* packet clones, copies, copy-on-write, and XDP-to-SKB transitions;
* TC and XDP program entry and exit;
* tunnels and inner packet tuples;
* kernel-reported drop reasons;
* selected BPF helper and map activity;
* capture loss, decoding failures, and output failures.

This is not a replacement for tcpdump or Wireshark. Those tools are excellentwhen the question is about packet bytes and protocols at a capture point.skbxis for questions about the path through the local Linux kernel.

It is also not the first tool to follow packets through that path. The projectis explicitly inspired bypwru, which showed how useful broad eBPFpacket tracing can be.

The part I especially wanted to explore was the evidence after the liveterminal stopped scrolling.

## Why call it a flight recorder?

Live tracing is useful, but incident work often continues after the privilegedsession has ended.

Someone else may need to inspect the capture. We may want to compare it with asuccessful request. We may need to cite one exact event in a bug report. Anautomation or AI system may need structured input, but it should not be allowedto invent observations that were never captured.

So the nativeskbxstream, calledtraceq, has an envelope:

capture_start
event
event
...
capture_end

Enter fullscreen mode

Exit fullscreen mode

Every event receives a stable handle:

event:111111111111111111111111

Enter fullscreen mode

Exit fullscreen mode

Replay groups ordered events into bounded route patterns, which receive theirown handles:

route:1c0201e74424e253f8363577

Enter fullscreen mode

Exit fullscreen mode

The footer matters as much as the events. It records the stop reason andreliability counters for kernel reservation failures, tracer recursion misses,read failures, userspace decoding and enrichment failures, and outputfailures.

If the footer is absent, the artifact is incomplete. If the tracer lostobservations, that uncertainty stays attached to the result.

I like this property because tracing software is also software. It should notsilently act omniscient.

## Installing it

The live tracer currently supports Linux on x86_64 and arm64. It needs Rust1.85 or newer, Clang/LLVM with the BPF backend,bpftool, libelf, libpcap, anda kernel exposing/sys/kernel/btf/vmlinux.

On Ubuntu, the native packages are:

sudo 
apt-get 
install
 
"linux-tools-
$(
uname
 
-r
)
"
 
\

 clang llvm libelf-dev libpcap-dev pkg-config

Enter fullscreen mode

Exit fullscreen mode

On Debian:

sudo 
apt-get 
install
 
\

 bpftool clang llvm libelf-dev libpcap-dev pkg-config

Enter fullscreen mode

Exit fullscreen mode

Then install the CLI directly from GitHub:

cargo 
install
 
--git
 https://github.com/copyleftdev/skbx 
--locked
 skbx-cli

Enter fullscreen mode

Exit fullscreen mode

Before attaching anything,doctorchecks the host:

skbx doctor 
--json

Enter fullscreen mode

Exit fullscreen mode

plangoes one step further. It shows exactly which functions would beattached without performing the attachment:

skbx plan 
--filter-func
 
'ip.*'
 
--json

Enter fullscreen mode

Exit fullscreen mode

That separation turned out to be useful while building the project. A missingkernel capability should be visible before a privileged capture begins, notsilently approximated afterward.

## Capturing a first packet

Here is a small ICMP capture:

sudo 
skbx capture 
--probe
 ip_rcv 
\

 
--duration
 10 
\

 
--output
 trace.jsonl 
\

 icmp

Enter fullscreen mode

Exit fullscreen mode

While it runs, create some traffic in another terminal:

ping 
-c
 3 1.1.1.1

Enter fullscreen mode

Exit fullscreen mode

The capture is deliberately bounded. It has a finite duration and event limitinstead of assuming that an unbounded trace is safe.

After it finishes, replay does not require root:

skbx replay trace.jsonl

Enter fullscreen mode

Exit fullscreen mode

Replay summarizes the functions, processes, packet identities, route patterns,consensus, outliers, and reliability state. Given the same valid JSONL input,it produces a byte-identical summary.

If an event looks interesting, retrieve it with its surrounding same-packetevidence:

skbx explain trace.jsonl event:<handle>

Enter fullscreen mode

Exit fullscreen mode

The repository includes a small contract fixture containing anip_rcveventfollowed bykfree_skb_reason. Replaying that fixture produces a route shapedlike this:

{

 
"handle"
:
 
"route:1c0201e74424e253f8363577"
,

 
"functions"
:
 
[

 
"ip_rcv"
,

 
"kfree_skb_reason"

 
],

 
"routes"
:
 
1
,

 
"truncated"
:
 
false
,

 
"outlier"
:
 
false

}

Enter fullscreen mode

Exit fullscreen mode

That output was generated by the current CLI from the checked-in test fixture;it is not illustrative pseudodata.

## Use case: what happened to a website request?

This is the use case I keep returning to.

Supposecurlstarts an HTTPS request and eventually times out. A capture onthe client can answer questions such as:

* Did the request enter the local TCP and IP output paths?
* Which interfaces and namespaces were associated with it?
* Was its mark changed?
* Did a TC or XDP program handle it?
* Was it transformed or placed into a tunnel?
* Did the local kernel report a drop?

That evidence can clear or implicate the client host.

It cannot prove what happened inside the ISP or on the target server. To provethose parts, we need observations from those vantage points. That limitationis important: the absence of a local drop is not proof that a remote hostreceived the packet.

The useful result is a smaller, evidence-backed search area:

client host evidence
 ↓
observed departure boundary
 ↓
ISP / transit inference
 ↓
target-host evidence, if available

Enter fullscreen mode

Exit fullscreen mode

I would rather know exactly where my evidence ends than have a tool produce aconfident story about systems it could not observe.

## Use case: a packet disappears inside the host

“The network dropped it” can hide several very different failures.

A host may reject a packet through a normal kernel path. A TC classifier orXDP program may return a drop action. A packet may be consumed during teardown.A transformation may cause the packet we were following to continue under adifferent kernel object.

For focused TCP drop questions, a small bpftrace program may be the fastestanswer. For packet contents, I still reach for tcpdump or Wireshark.

I reach forskbxwhen I do not yet know which local subsystem owns thefailure, or when I want to preserve the ordered path rather than one dropevent.

## Use case: follow transformations instead of losing the trail

Linux does not promise that one logical packet corresponds to onestruct sk_buffaddress for its entire lifetime.

Packets can be cloned, copied, or changed through copy-on-write. XDP frames canlater become SKBs. Tunnels introduce outer and inner packet identities.

skbxuses bounded, capture-local lineage state to connect those transitions.The provenance remains explicit: an event records whether it matched theoriginal filter or was included because it belonged to a packet already beingtracked.

For example, a marked packet can be followed with:

sudo 
skbx capture 
\

 
--filter-mark
 0x2a 
\

 
--filter-track-skb
 
\

 
--output
 trace.jsonl

Enter fullscreen mode

Exit fullscreen mode

The important word here iscapture-local. A lineage identifier is not adistributed trace ID, and it should not be presented as one.

## Use case: capture once, investigate without root

Loading and attaching eBPF programs is privileged work. Reading a JSONL filedoes not need to be.

That makes a simple handoff possible:

1. An operator checks the plan and performs a bounded capture.
2. The capture ends and writes its reliability footer.
3. The artifact is copied to a normal development or analysis environment.
4. Another person replays it and cites exactevent:orroute:handles.

This is useful for incident handoffs and bug reports, but it is also useful forlearning. I can capture a small experiment once and inspect it repeatedlywithout keeping probes attached while I try to understand the result.

## Use case: give an AI evidence instead of a mystery

One of my stranger motivations was making the CLI friendly to both operatorsand software agents.

Before touching the host, an agent can ask the executable what it supports:

skbx describe 
--format
 json
skbx schema
skbx doctor 
--json

skbx plan 
--json

Enter fullscreen mode

Exit fullscreen mode

The native engine remains the source of truth. An AI system may summarize aroute or explain a captured event, but the event must already exist in thetrace. Machine output stays on standard output, diagnostics stay on standarderror, and unsupported capabilities remain explicit.

This does not make an AI explanation automatically correct. It gives theexplanation something concrete to cite and gives a human a way to check it.

## The engineering parts I enjoyed

The obvious fun was seeing packets move through functions I had previouslytreated as boxes in a diagram.

The less obvious fun was designing the boundaries:

* discovering validstruct sk_buff *arguments from the target kernel's BTF
instead of guessing from function names;
* keeping kernel-side state and work bounded;
* moving JSON encoding, symbolization, and filesystem work out of the eBPF hot
path;
* making probe planning inspectable before attachment;
* separating raw observation from later explanation;
* treating partial output as incomplete instead of “probably good enough”;
* making replay deterministic enough to use in tests and automation.

Those constraints made the tool more interesting to build. They also gave me abetter mental model of what an observability tool can honestly claim.

## What it does not know

skbxonly observes what the running kernel and selected probes expose.

It does not see inside an ISP. It does not see a remote host unless it runsthere too. It is not a packet-content replacement for Wireshark. Kernelconfiguration, BTF availability, permissions, hidden addresses, unsupportedsignatures, and capture loss can all limit the evidence.

Those limitations are part of the interface rather than footnotes.

I am still exploring where this project is most useful. The best next input isnot “looks cool,” although I will happily take that. It is a packet path thetool cannot explain yet, together with the kernel version, exact command,doctor --jsonoutput, and reliability footer.

The source, installation instructions, architecture notes, and field guidesare in the repository:

## copyleftdev/skbx

### Agent-first Linux packet-path tracing with Rust/eBPF: bounded evidence, deterministic replay, and packet routes with receipts.

# skbx

skbxshows where a packet went inside Linux—and keeps the receipts.

Follow a packet through the flight recorder →

Field guides:

* Trace a website request across your Linux host, ISP, and target
* Debug a Linux packet drop with replayable eBPF evidence

It observes kernel networking functions, TC/XDP programs, packet
transformations, tunnels, drops, and selected BPF helper activity with
Rust and CO-RE eBPF. Every observation lands in a bounded, replayable evidence
stream with stable handles and explicit loss telemetry.

Use it when “the packet disappeared” is not a sufficient incident report.

capture → event:8c6f… → replay → route:21b4… → explain
 evidence pattern context

Inspired bypwru, rebuilt around an
agent-first contract: deterministic observations, machine-readable
capabilities, bounded state, and no invented evidence.

## The short version

You need to…

skbx gives you…

See the kernel path of an SKB

BTF-discovered kprobes with exact function evidence

Follow clones, copies, COW, and XDP-to-SKB

…

View on GitHub

If you try it, I would love to know which networking question you used it toanswer—and where its evidence stopped.

AI-assistance disclosure: I built and testedskbx. I used OpenAI Codex toresearch adjacent writing, challenge the article's positioning, edit thisdraft, verify its commands and example output against the repository, andgenerate the cover illustration. I reviewed the technical claims and remainresponsible for their accuracy.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse