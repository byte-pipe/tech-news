---
title: 'smnx/promethee: UEFI Bindings for JavaScript (Proof of Concept) - Codeberg.org'
url: https://codeberg.org/smnx/promethee
site_name: hnrss
content_file: hnrss-smnxpromethee-uefi-bindings-for-javascript-proof-o
fetched_at: '2026-02-10T11:23:55.271846'
original_url: https://codeberg.org/smnx/promethee
author: smnx
date: '2026-02-09'
description: promethee - UEFI Bindings for JavaScript (Proof of Concept)
tags:
- hackernews
- hnrss
---

smnx
/
promethee

Watch

			1


Star

			18


Fork

				You've already forked promethee


			2


UEFI Bindings for JavaScript (Proof of Concept)

* C69.7%
* Makefile21.4%
* TypeScript3.4%
* JavaScript2.9%
* Shell2.6%

trunk

Find a file

		HTTPS


sleepy-monax

3025d2b24f

Removed useless file.

2026-02-09 15:42:13 +01:00

src



Removed useless file.

2026-02-09 15:42:13 +01:00

.gitignore

Prometheus stole fire from the gods and gave it to man. For this he was chained to a rock and tortured for eternity.

2026-02-09 14:48:48 +01:00

get-deps

Prometheus stole fire from the gods and gave it to man. For this he was chained to a rock and tortured for eternity.

2026-02-09 14:48:48 +01:00

GNUmakefile

Prometheus stole fire from the gods and gave it to man. For this he was chained to a rock and tortured for eternity.

2026-02-09 14:48:48 +01:00

LICENSE

Update LICENSE copyright for 2026

2026-01-02 14:41:00 +01:00

promethee.jpeg

Prometheus stole fire from the gods and gave it to man. For this he was chained to a rock and tortured for eternity.

2026-02-09 14:48:48 +01:00

README.md

Update README.md

2026-02-09 14:56:28 +01:00

script.js

Prometheus stole fire from the gods and gave it to man. For this he was chained to a rock and tortured for eternity.

2026-02-09 14:48:48 +01:00

types.ts

Prometheus stole fire from the gods and gave it to man. For this he was chained to a rock and tortured for eternity.

2026-02-09 14:48:48 +01:00

#### README.md

# Promethee

## What this is

UEFI Bindings for JavaScript

## How it works

Promethee loads script.js from the boot volume and runs it. That script is your
bootloader. If you can do it with UEFI services, you can do it in JavaScript.

## Quick start

1. Fetch dependencies:
./get-deps
2. Build and run in QEMU:
make run

Your entrypoint isscript.js. The run target copies it to the UEFI
FAT volume as \script.js.

## Tiny example

Inscript.js:

var gop = efi.SystemTable.BootServices.LocateProtocol(efi.guid.GraphicsOutput);
if (gop) {
 var red = { r: 255, g: 0, b: 0 };
 gop.Blt(red, 'EfiBltVideoFill', 0, 0, 50, 50, 200, 120, 0);
}

## Notes

* Duktape tooling requires Node.js (used to generate sources).
* The build is freestanding; only minimal libc stubs are provided.
* If this makes you grin, you are probably holding the torch.
