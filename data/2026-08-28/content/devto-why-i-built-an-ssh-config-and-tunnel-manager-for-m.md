---
title: Why I Built an SSH Config and Tunnel Manager for macOS - DEV Community
url: https://dev.to/malusev998/why-i-built-an-ssh-config-and-tunnel-manager-for-macos-58n8
site_name: devto
content_file: devto-why-i-built-an-ssh-config-and-tunnel-manager-for-m
fetched_at: '2026-08-28T12:25:21.775585'
original_url: https://dev.to/malusev998/why-i-built-an-ssh-config-and-tunnel-manager-for-macos-58n8
author: Dusan Malusev
date: '2026-08-26'
description: Every internal tool I need sits behind SSH. Grafana, Prometheus, the staging clusters, internal AI... Tagged with ssh, macos, swift, tunneling.
tags: '#ssh, #macos, #swift, #tunneling'
---

Every internal tool I need sits behind SSH. Grafana, Prometheus, the staging clusters, internal AI tooling—none of it answers on a public address, and the only door is a bastion I have a key for. That is the right setup for anything with real data behind it, and I wouldn't change it. What Ididchange is typingssh -N -L 3000:localhost:3000 -J bastion prod-1from memory four times a day across three different machines.

So one weekend, I started writingSSH Config Manager. It is a native macOS app that edits~/.ssh/configwithout wrecking formatting, saves tunnels as presets, and opens those tunnels in-process instead of shelling out tossh. I wrote it for my own workflow first. Putting it on the App Store came later, once it was genuinely useful to me and I figured others were struggling with the exact same friction.

## The VPN Question

The first thing people ask is:why not run a VPN and be done with it?Fair question, but the honest answer is that SSH is the tool I already understand inside and out.

I have configuredsshdenough times to know whatPermitRootLogin noandPasswordAuthentication noactually change. When a connection stops working, I can usually name the exact line that broke it. A VPN introduces a whole second network layer underneath, complete with its own credentials, its own background daemon to keep patched, and its own unique failure modes to debug at 2:00 AM when production is down. SSH is already on every Linux server I touch and every developer machine I own — there is nothing new to roll out and nothing new to secure.

The tradeoff is real, and I would rather acknowledge it up front. Operating without a VPN means no transparent network routing: every internal service I want to reach must be explicitly forwarded to a local port in advance, and a colleague without my config reaches none of them. Still, I would far rather maintain a clean list of port forwards than maintain another background daemon.

## Shell Aliases Do Not Survive Three Machines

The obvious fix for long commands is a set of shell functions. In practice, that fell apart for me.

I use a MacBook Pro for most daily tasks, but ScyllaDB work happens on Linux because every team member uses Linux and the tooling assumes it. Those environments don't agree on much—different shells, different key paths, and a different set of inventory hosts. I never got dotfile synchronization into a state where SSH aliases were cleanly shared rather than messily merged. The failure mode was predictable: an alias written on the laptop was missing on the remote machine where I needed it, or worse, pointed to a port that moved months ago.

The configuration file itself is the piece that is already portable and universally standardized. Everything reads it out of the box:ssh,scp,rsync -e ssh, and my editor's remote development plugins. Building a tool around~/.ssh/configrather than shell scripts is the core design decision everything else flows from.

## Nothing Tells You What Config Keys Mean

Another friction point is that standard text editors treat~/.ssh/configas an arbitrary blob of text. A misspelled directive isn't auto-completed or flagged—you find out at connect time when the setting you thought you configured was silently ignored. The actual definition of what a keyword does lives inside thessh_config(5)man page in a separate terminal window, which is exactly where you don't want to be toggling back and forth while editing.

To fix this, the app embeds a comprehensive keyword catalog.KeywordRegistry.swiftcurrently contains 95 entries, each specifying its canonical spelling, expected value type (string, integer, boolean, fixed enum, path, or list), category section, and a concise help string pulled directly fromssh_config(5):

.
init
(

 
canonical
:
 
"IdentityFile"
,
 
field
:
 
.
path
,
 
category
:
 
.
identity
,

 
help
:
 
"Private key file for public-key authentication. May be repeated."
),

.
init
(

 
canonical
:
 
"ProxyJump"
,
 
field
:
 
.
string
,
 
category
:
 
.
connection
,

 
help
:
 
"Connect through one or more jump hosts, e.g. user@bastion:22."
),

Enter fullscreen mode

Exit fullscreen mode

That registry powers real-time auto-completion, a searchable "Add Setting" picker, and inline field documentation—eliminating second-guessing over whether it'sIdentityFileorIdentityKey, or whetherIdentitiesOnlyaccepts a file path.

The editor engine is completely lossless. Comments, blank lines, and custom indentation formatting stay untouched. Only the modified directive gets rewritten on save. This proved vital: my SSH configuration contains years of inline comments explaining obscure host settings, and a tool that reformats or strips comments on save is a tool I would use exactly once.

## The Tunnel Engine Never Runsssh

The most interesting architectural constraint came from Apple's App Store guidelines. Sandboxed macOS applications cannot arbitrarily spawn the system/usr/bin/sshbinary. As a result, all SSH tunnels are opened in-process viaswift-nio-sshinsideNIOTunnelEngine.swift—there is nosshsubprocess anywhere in the execution path.

Implementing this required more effort than the rest of the app combined. All three forwarding modes operate over the same connection model:

* -Lspawns a local listener bound to adirect-tcpipchannel at a fixed target.
* -Ddrives that same channel type via a dynamic SOCKS5 proxy listener.
* -Roperates in reverse: the engine requeststcpip-forwardfrom the server, mapping each returnedforwarded-tcpipchannel to a local port.

ProxyJumpdirectives are recursively resolved into an ordered chain of hops prior to connecting. Each jump host inherits its explicit configuration (User,IdentityFile, nestedProxyJump) exactly as OpenSSH would evaluate it. Host keys are verified againstknown_hosts, utilizing trust-on-first-use (TOFU) for previously unseen hosts.

To achieve complete parity, two missing capabilities had to be added toswift-nio-ssh:

1. RSA Support:swift-nio-sshdoes not ship with RSA key support by default.NIOSSHRSAis registered as a custom key handler at startup sossh-rsaidentities from files or SSH agents can be offered during handshakes.
2. Post-Quantum KEX:On systems prior to macOS 15, native ML-KEM support is missing from CryptoKit. A fallback ML-KEM-768 backend is installed on startup to ensure modern post-quantum key exchange functions across all supported macOS releases.

Reconnection logic relies on a deterministic exponential backoff implementation inTunnelBackoff.swift(1s, 2s, 5s, 15s, capped with ±20% jitter). Keeping this logic in a standalone pure type allows the backoff schedule to be fully unit-tested without needing a live network server.

There are explicit trade-offs worth noting:

* ProxyCommandis rejected outright because executing arbitrary subprocesses is restricted inside the app sandbox.
* ControlMastermultiplexing directives are parsed and validated but not executed, as there is no local subprocess to multiplex across.
* Active tunnels terminate if you quit the app.

For edge cases where running the native binary is necessary, the app generates and copies the exact command string to your clipboard:

ssh 
-N
 
-T
 
-o
 
ControlPath
=
none 
-L
 3000:localhost:3000 prod-1

Enter fullscreen mode

Exit fullscreen mode

By passing the host alias rather than the resolved IP address,sshperforms its own resolution, guaranteeing identical behavior to running the command manually in your shell.

## Seeing Connection State Is Most of the Value

A visual interface provides clear operational advantages. Having a clear dashboard showing active tunnels, flapping connections, resolved identity keys, and exact error diagnostics is well worth the screen real estate compared to querying terminal commands individually.

One of the most useful features turned out to be the built-inknown_hostsauditor. Operating via static analysis without network side-effects, it flags key issues automatically:

* Malformed entries:Unparseable syntax or corrupted lines.
* Duplicates:Repeating host definitions with conflicting or redundant keys.
* Orphans:Host keys that don't match any host entry configured in~/.ssh/config.

Hashed entries are ignored during orphan checks since hostnames cannot be reversed, and revoked key entries are preserved intentionally. While these findings aren't dramatic individually, together they transformknown_hostsfrom an ever-growing junk drawer into a file you actually understand and maintain.

## What the App Store Cost

Building this was my first experience submitting to the Mac App Store. The process was equal parts rewarding and tedious. Sandboxing constraints forced the creation of a custom in-process tunnel engine—a case where platform limitations ultimately led to a cleaner, more robust architecture than shelling out to binaries.

The one-time Apple Developer fee is small, and I preferred pricing the app simply so it sustains its own maintenance cost without needing a subscription model. It is a tool built out of personal necessity, and it remains valuable regardless of how many people use it.

If you deal with locked-down server architecture and a fragile SSH config, the easiest piece to adopt right away is theknown_hostsaudit pattern. Spotting malformed, duplicate, or orphaned lines is simple to implement, and it immediately cleans up technical debt most developers overlook.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse