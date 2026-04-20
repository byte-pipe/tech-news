---
title: Reverse-engineering the UniFi inform protocol — Tamarack
url: https://tamarack.cloud/blog/reverse-engineering-unifi-inform-protocol
site_name: hnrss
content_file: hnrss-reverse-engineering-the-unifi-inform-protocol-tama
fetched_at: '2026-03-09T19:20:16.028188'
original_url: https://tamarack.cloud/blog/reverse-engineering-unifi-inform-protocol
date: '2026-03-09'
description: Every UniFi device phones home to its controller on port 8080. The payload is AES-encrypted, but the header is plaintext, and that's enough to build multi-tenant routing.
tags:
- hackernews
- hnrss
---

February 24, 2026

# Reverse-engineering the UniFi inform protocol

Every UniFi device phones home to its controller on port 8080. The payload is AES-encrypted, but the header is plaintext, and that's enough to build multi-tenant routing.

A few years ago I ran a small UniFi hosting service. Managed cloud controllers for MSPs and IT shops who didn't want to run their own. Every customer got their own VPS running a dedicated controller.

The product worked. People wanted hosted controllers, mostly so they didn't have to deal with hardware, port forwarding, backups. The problem was the economics.

Each customer needed their own VPS. DigitalOcean droplets ran $4-6/month. I was charging $7-8. That's $1-2 of margin per customer, and any support request at all wiped it out. I was essentially volunteering.

The obvious fix is multi-tenancy: put multiple controllers on shared infrastructure instead of giving every customer their own VM. But UniFi controllers aren't multi-tenant. Each one is its own isolated instance with its own database and port bindings. You need a routing layer, something in front that can look at incoming traffic and figure out which customer it belongs to.

For the web UI on port 8443, that's easy. Subdomain per customer behind a reverse proxy, nothing special. But the inform protocol on port 8080 is where things get interesting.

## What inform does

Every UniFi device (access points, switches, gateways) phones home to its controller. An HTTP POST to port 8080 every 10 seconds. This is how the controller keeps track of everything: device stats, config sync, firmware versions, client counts.

The payload is AES-128-CBC encrypted. So I assumed you'd need per-device encryption keys to do anything useful with the traffic, which would mean you'd need the controller's database, which would mean you're back to one instance per customer.

Then I looked at the raw bytes.

## The packet

The first 40 bytes of every inform packet are unencrypted:

Offset Size Field
────── ───── ──────────────────────────
0 4B Magic: "TNBU" (0x544E4255)
4 4B Packet version (currently 0)
8 6B Device MAC address
14 2B Flags (encrypted, compressed, etc.)
16 2B AES IV length
18 16B AES IV
34 4B Data version
38 4B Payload length
42+ var Encrypted payload (AES-128-CBC)

Byte offset 8 is the device's MAC address, completely unencrypted.

On the wire it looks like this:

54 4E 42 55 # Magic: "TNBU"
00 00 00 00 # Version: 0
FC EC DA A1 # MAC: fc:ec:da:a1:b2:c3
B2 C3
01 00 # Flags
...

"TNBU" is just "UBNT" backwards, Ubiquiti's ticker symbol and the default SSH credentials on their devices.

The MAC is in the header because the controller needs to identify the devicebeforedecrypting. Encryption keys are per-device, assigned during adoption, so the controller has to know which device is talking before it can look up the right key. Not a security oversight, just a practical requirement. But it means you can route inform traffic without touching the encryption at all.

## Reading the MAC

Extracting it is almost nothing:

header
:=
 make
([]
byte
,
40
)

if
 _, err
:=
 io.
ReadFull
(conn, header); err
!=
 nil
 {

 return
 err

}



if
 string
(header[
0
:
4
])
!=
 "TNBU"
 {

 return
 fmt.
Errorf
(
"not an inform packet"
)

}



mac
:=
 fmt.
Sprintf
(
"
%02x
:
%02x
:
%02x
:
%02x
:
%02x
:
%02x
"
,

 header[
8
], header[
9
], header[
10
],

 header[
11
], header[
12
], header[
13
])

Read 14 bytes and you know which device is talking. No decryption needed.

## Building the proxy

With the MAC in hand, routing is simple. Keep a table of which MAC belongs to which tenant, forward the whole packet (header and encrypted payload, untouched) to the right backend.

Device (MAC: aa:bb:cc:dd:ee:ff)
 |
 v
+-----------------------------------+
| |
| Inform Proxy |
| |
| Read MAC from bytes 8-13 |
| |
| Lookup: |
| aa:bb:cc:... -> tenant-7 |
| 11:22:33:... -> tenant-3 |
| fe:dc:ba:... -> tenant-12 |
| |
| Forward to correct backend |
| |
+-----------------------------------+
 | | |
 v v v
 Tenant 7 Tenant 3 Tenant 12

The whole proxy is maybe 200 lines of Go with an in-memory MAC-to-tenant lookup table.

In practice, the proxy is mostly a fallback. Once a device is adopted, you point it at its tenant's subdomain (set-inform http://acme.tamarack.cloud:8080/inform) and after that, standard Host header routing handles it through normal ingress. The MAC-based routing catches edge cases like devices that haven't been reconfigured yet, or factory-reset devices re-adopting.

## The other ports

Inform is the hard one. The rest of the controller's ports are more straightforward:

Port
Protocol
Purpose
8080
TCP/HTTP
Inform (device phone-home)
8443
TCP/HTTPS
Web UI and API
3478
UDP
STUN
6789
TCP
Speed test (internal)
27117
TCP
MongoDB (internal)
10001
UDP
L2 discovery (local only)

Once I figured out inform, the rest was almost anticlimactic. 8443 is the web UI, so that's just subdomain-per-tenant with standard HTTPS ingress. 3478 (STUN) is stateless so a single shared coturn instance covers every tenant. The rest are either internal to the container or L2-only, so they never leave the host.

## Inside the encrypted payload

For the curious: the payload after byte 42 is AES-128-CBC. Freshly adopted devices use a default key (ba86f2bbe107c7c57eb5f2690775c712) which is publicly documented by Ubiquiti and ships in the controller source code. After adoption, the controller assigns a unique per-device key.

The decrypted payload contains device stats and configuration data. Interesting if you're building controller software, but irrelevant for routing.

## So what does this get you

Every tenant still gets their own dedicated controller, but you're not paying for a whole VM per customer anymore. What was a volunteering operation at $1-2 margin becomes something you can actually make money on.

None of it works if the MAC is inside the encrypted payload. You'd need per-device keys at the proxy layer, which means you'd need access to every controller's database, which puts you right back at one instance per customer. Six plaintext bytes in a packet header make the whole thing possible.

I don't think Ubiquiti designed it this way for third parties to build on. The MAC is there because the controller genuinely needs it before decryption. But the happy side effect is that the inform protocol is routable by anyone who can read 14 bytes off a TCP connection.

If you've poked at the inform protocol yourself, I'd like to hear about it.[email protected]
