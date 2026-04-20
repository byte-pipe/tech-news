---
title: 'GitHub - teamchong/turboquant-wasm: TurboQuant WASM SIMD vector compression — 3 bits/dim with fast dot product. Requires relaxed SIMD (Chrome 114+, Firefox 128+, Safari 18+, Node 20+) · GitHub'
url: https://github.com/teamchong/turboquant-wasm
site_name: hnrss
content_file: hnrss-github-teamchongturboquant-wasm-turboquant-wasm-si
fetched_at: '2026-04-05T11:12:51.352161'
original_url: https://github.com/teamchong/turboquant-wasm
date: '2026-04-04'
description: TurboQuant WASM SIMD vector compression — 3 bits/dim with fast dot product. Requires relaxed SIMD (Chrome 114+, Firefox 128+, Safari 18+, Node 20+) - teamchong/turboquant-wasm
tags:
- hackernews
- hnrss
---

teamchong



/

turboquant-wasm

Public

* NotificationsYou must be signed in to change notification settings
* Fork5
* Star159




 
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

82 Commits
82 Commits
.github/
workflows
.github/
workflows
 
 
benchmarks
benchmarks
 
 
demo
demo
 
 
docs/
assets
docs/
assets
 
 
scripts
scripts
 
 
src
src
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.npmignore
.npmignore
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
build.zig
build.zig
 
 
build.zig.zon
build.zig.zon
 
 
package.json
package.json
 
 
tsconfig.json
tsconfig.json
 
 
View all files

## Repository files navigation

# TurboQuant WASM

Experimental WASM + relaxed SIMD build ofbotirk38/turboquantfor browsers and Node.js.

Based on the paper"TurboQuant: Online Vector Quantization with Near-optimal Distortion Rate"(Google Research, ICLR 2026).

Live Demo— vector search, image similarity, and 3D Gaussian Splatting compression running in the browser.

## Why TurboQuant?

Float32 embedding indexes are large — 1M vectors × 384-dim = 1.5GB. They don't fit in mobile RAM, take minutes to download, and gzip only saves ~7% because float32 has high entropy.

TurboQuant compresses them 6x (1.5GB → 240MB) and searches directly on compressed data without decompressing. No training step — unlike PQ/OPQ, justinit({ dim, seed })and encode any vector immediately.

## What this adds

* npm packagewith embedded WASM —npm install turboquant-wasm
* Relaxed SIMD—@mulAddFMA maps tof32x4.relaxed_madd
* SIMD-vectorizedQJL sign packing/unpacking and scaling
* TypeScript API—TurboQuant.init()/encode()/decode()/dot()
* Golden-value tests— byte-identical output with the reference Zig implementation

## Browser Requirements

The WASM binary uses relaxed SIMD instructions:

Runtime

Minimum Version

Chrome

114+

Firefox

128+

Safari

18+

Node.js

20+

## Quick Start

import

{

TurboQuant

}

from

"turboquant-wasm"
;

const

tq

=

await

TurboQuant
.
init
(
{

dim
:
1024
,

seed
:
42

}
)
;

// Compress a vector (~4.5 bits/dim, ~6x compression)

const

compressed

=

tq
.
encode
(
myFloat32Array
)
;

// Decode back

const

decoded

=

tq
.
decode
(
compressed
)
;

// Fast dot product without decoding

const

score

=

tq
.
dot
(
queryVector
,

compressed
)
;

// Batch search: one WASM call for all vectors (83x faster than looping dot())

const

allCompressed

=

new

Uint8Array
(
/* concatenated compressed vectors */
)
;

const

scores

=

tq
.
dotBatch
(
queryVector
,

allCompressed
,

bytesPerVector
)
;

tq
.
destroy
(
)
;

## API

class

TurboQuant

{


static

async

init
(
config
:
{

dim
:
number
;

seed
:
number

}
)
:
Promise
<
TurboQuant
>
;


encode
(
vector
:
Float32Array
)
:
Uint8Array
;


decode
(
compressed
:
Uint8Array
)
:
Float32Array
;


dot
(
query
:
Float32Array
,

compressed
:
Uint8Array
)
:
number
;


dotBatch
(
query
:
Float32Array
,

compressedConcat
:
Uint8Array
,

bytesPerVector
:
number
)
:
Float32Array
;


destroy
(
)
:
void
;

}

## Building

#
 Run tests

zig
test
 -target aarch64-macos src/turboquant.zig

#
 Full npm build (zig -> wasm-opt -> base64 embed -> bun + tsc)

bun run build

#
 Build WASM only

bun run build:zig

Requires Zig 0.15.2 and Bun.

## Quality

Encoding preserves inner products — verified by golden-value tests and distortion bounds:

* MSEdecreases with dimension (unit vectors)
* Bits/dimis ~4.5 (payload only, excluding 22-byte header)
* Dot product preservation— mean absolute error < 1.0 for unit vectors at dim=128
* Bit-identicaloutput withbotirk38/turboquantfor same input + seed

## Credits

* botirk38/turboquant— original Zig implementation
* TurboQuant paper(Google Research, ICLR 2026) — algorithm design

## License

MIT

## About

TurboQuant WASM SIMD vector compression — 3 bits/dim with fast dot product. Requires relaxed SIMD (Chrome 114+, Firefox 128+, Safari 18+, Node 20+)

teamchong.github.io/turboquant-wasm/

### Resources

 Readme



### License

 MIT license


### Uh oh!

There was an error while loading.Please reload this page.





Activity


### Stars

159

 stars


### Watchers

1

 watching


### Forks

5

 forks


 Report repository



## Releases10

v0.2.9

 Latest



Apr 5, 2026



+ 9 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





### Uh oh!

There was an error while loading.Please reload this page.





## Contributors

### Uh oh!

There was an error while loading.Please reload this page.





## Languages

* Zig85.4%
* TypeScript8.9%
* Python4.5%
* JavaScript1.2%
