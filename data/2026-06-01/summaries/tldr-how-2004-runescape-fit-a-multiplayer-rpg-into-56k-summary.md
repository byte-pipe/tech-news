---
title: How 2004 RuneScape fit a multiplayer RPG into 56k dial-up · jkm.dev
url: https://jkm.dev/posts/how-2004-runescape-fit-a-multiplayer-rpg-into-56k-dialup/
date: 2026-06-01
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-06-01T04:18:42.999663
---

# How 2004 RuneScape fit a multiplayer RPG into 56k dial-up · jkm.dev

# How 2004 RuneScape fit a multiplayer RPG into 56k dial‑up

## Constraints
- **Bandwidth** – 56 kbit/s modem gave roughly 5 KB/s downstream and even less upstream, with protocol overhead and line noise.
- **Java applet sandbox** – No native sockets or UDP; all traffic went over a single TCP connection, ordered and with per‑segment overhead.
- **Server cycle** – The game server advanced in ~600 ms ticks; each tick it had to compute every player’s visible world and send updates before the next tick.

## Cipher layer (ISAAC)
- After login, a tiny encryption layer protects only the packet *opcode*.
- Two ISAAC stream ciphers are used: one for client‑to‑server, one for server‑to‑client.
- Both streams are seeded from a shared four‑integer key; the inbound stream’s seed is offset by +50 to keep the keystreams distinct.
- Encryption is a single line: `putByte(opcode + outboundCipher.value())`; the body of the packet remains unencrypted.
- This minimal protection prevents easy third‑party packet parsing while adding virtually no byte overhead.

## Sending a walk request
- The client first runs a local breadth‑first search on its collision map to produce a path.
- Packet layout:
  1. **Opcode** (enciphered)
  2. **Length byte** – size of the variable‑length body.
  3. **Start position** – two shorts (x, z) = 4 bytes.
  4. **Way‑point deltas** – for each additional waypoint, one signed byte for x and one for z (2 bytes per waypoint).
  5. **Ctrl‑key byte** – indicates run mode toggle.
- **Delta encoding** saves bytes: each extra waypoint costs 2 bytes instead of 4, a 50 % reduction.
- Only corner tiles are transmitted; a straight‑line walk of ten tiles sends just the destination waypoint.
- Example: a single step north results in a 7‑byte packet (opcode + length + 2 bytes x + 2 bytes z + run‑toggle).

## Overall networking frugality
- Every packet is trimmed to the smallest viable size to stay within the 5 KB/s downstream limit.
- Decisions such as encrypting only the opcode, using delta encoding, and omitting intermediate tiles illustrate Jagex’s obsessive byte‑saving approach.
- The same core principles appear throughout RuneScape’s evolution, from the 2001 Classic version to modern RuneScape 3 and Old School RuneScape.