---
title: Bytecode Alliance — WASI 0.3 Launched
url: https://bytecodealliance.org/articles/WASI-0.3
site_name: hnrss
content_file: hnrss-bytecode-alliance-wasi-03-launched
fetched_at: '2026-06-12T19:42:05.239850'
original_url: https://bytecodealliance.org/articles/WASI-0.3
date: '2026-06-12'
published_date: '2026-06-11T00:00:00+00:00'
description: WASI 0.3
tags:
- hackernews
- hnrss
---

WASI 0.3 is official, and async is now native to WebAssembly Components.The WASI Subgroup voted to ratify WASI 0.3.0, rebasing WASI onto the WebAssembly Component Model’s async primitives. The 0.3.0 specification is now stable, and runtime and toolchain support is landing now.

The work thatwasi:ioin WASI 0.2 used to do (pollables, input-streams, output-streams) is now part ofthe canonical ABI, where the Component Model now offers these primitives natively. As a concequence of that, most of the changes from WASI 0.2 to 0.3 are entirelymechanicaland significantly simplify the signatures we had before. The new async
primitives are part of the Component Model’scanonical ABI,
enabling bindings generators to emit idiomatic async bindings for their given
language.

## The Component Model Async ABI

In WASI 0.2 each component needed its own event loop/async runtime. That meant that individual components could be run on a host, but there was no way for those event loops to coordinate with one another. If a component used streaming or async APIs, it couldn’t be composed with any other components.

WASI 0.3 makes it so the host is now the one in charge of managing the one event loop that is shared by all components. This is enabled by addingstream<T>,future<T>, andasyncas first-class constructs to the canonical ABI:

* stream<T>andfuture<T>function like resource types: each is an owned handle, passing one across a component boundary transfers ownership from caller to callee. Unlike resource types, they can’t be borrowed.
* The runtime, not each component, drives the scheduling. When a value has been delivered to afuture, the runtime schedules whichever task is awaiting it, even if it was passed through multiple component boundaries. The writer that delivers that value might be the host, another component, or even the same component that holds the read end.
* The async model iscompletion-based, notreadiness-based. This is similar to the ultra-efficient Linuxio_uringand Windows’ IOCP/IoRingAPIs. Anepoll/kqueue-style readiness API can be emulated on top of this for programs which need the compatibility.
* Components export and importasync funcs directly. Gone is the three-stepstart-foo/finish-foo/subscribedance from WASI 0.2.

## Changes to the WASI interfaces

Most of the changes in the 0.3 interfaces are entirely mechanical. WASI 0.2 had to perform some acrobatics to make async work, but now that async is native to the component model we can write the same things we did before but much more ergonomically. Here is an overview of the patterns we were encoding in WASI 0.2 with thewasi:iopackage, and what those patterns now look like in 0.3 with Component Model async:

WASI 0.2 (
wasi:io
)

WASI 0.3 (Component Model)

resource pollable

future<T>

resource input-stream

stream<u8>

resource output-stream

stream<u8>
 (written-to direction)

poll(list<pollable>)

await
 on a future (runtime-handled)

subscribe()
 on resource

return a 
future<...>
 from the call

start-foo
 / 
finish-foo

foo: async func(...)

A problem with WASI 0.2 was that it surfaced terminal errors inline on each read call on the stream. That meant callers only learned the outcome if they kept reading. If readers stopped early they could not distinguish between a stream close and an error.
In WASI 0.3 streams now return an additional future which resolves independently of how much of the stream is consumed, solving the stream status problem of WASI 0.2:

// WASI 0.2
read-via-stream: func() -> result<input-stream, error-code>;
// WASI 0.3
read-via-stream: func() -> tuple<stream<u8>, future<result<_, error-code>>>;

## Changes to language bindings

One of the super powers of the component model is that it makes it trivial to
create bindings to and from other languages. With the addition of first-class
async it means guest binding generators can leverage that to create async
bindings that feel native to that language. Take for example thewasi:http/handlerinterface. This interface exposes one function,handle, which is marked async:

interface handler {
 handle: async func(request: request) -> result<response, error-code>;
}

To implement an HTTP server in Rust with this, we can use thewit-bindgencrate. This maps theinterface handlerto atrait Guest, and maps thehandle: async functo anasync fn handle:

use
 
wasi
::
http
::
types
::{
ErrorCode
,
 
Request
,
 
Response
};

impl
 
Guest
 
for
 
Component
 
{

 
async
 
fn
 
handle
(
request
:
 
Request
)
 
->
 
Result
<
Response
,
 
ErrorCode
>
 
{

 
// ...

 
}

}

Async support for guest binding generators is also in-progress for many languages includingPython,JavaScript,C#, andC. All of these languages rely onstackless coroutines. But the Component Model’s async ABI was designed from the ground up to accomodate bothstackfulandstacklesscoroutines side-by-side. An example of a language with those is Go. Instead of exposing async and non-async functions, Go’s runtime is able to convert synchronous-looking calls to async calls, and provides concurrent execution via virtual threads called “goroutines”.

Usingcomponentize-gowe can implement an HTTP server by exporting afunc Handle. This enables streaming bodies via goroutines that do blocking calls. The runtime then parks the goroutine at the ABI boundary and resumes it when the stream is ready, without blocking the rest of the program:

package
 
export_wasi_http_handler

import
 
(

	
.
 
"wit_component/wasi_http_types"

	
.
 
"go.bytecodealliance.org/pkg/wit/types"

)

func
 
Handle
(
request
 
*
Request
)
 
Result
[
*
Response
,
 
ErrorCode
]
 
{

	
tx
,
 
rx
 
:=
 
MakeStreamU8
()
 
// ← 1. Create a channel pair

	
go
 
func
()
 
{
 
// ← 2. Spawn a virtual thread

		
defer
 
tx
.
Drop
()

		
tx
.
WriteAll
([]
uint8
(
"Hello, world!"
))
 
// ← 3. Write into the channel

	
}()

	
response
,
 
send
 
:=
 
ResponseNew
(
 
// ← 4. Create an HTTP response

		
FieldsFromList
([]
Tuple2
[
string
,
 
[]
byte
]{

			
{
F0
:
 
"content-type"
,
 
F1
:
 
[]
byte
(
"text/plain"
)},

		
})
.
Ok
(),

		
Some
(
rx
),
 
// ← 5. Pass the receiver as the HTTP body

		
trailersFuture
(),

	
)

	
send
.
Drop
()

	
return
 
Ok
[
*
Response
,
 
ErrorCode
](
response
)
 
// ← 6. Return the HTTP response

}

Now that WASI 0.3 has been launched with support for component model async,
guest toolchains and host runtimes will be unblocked to begin stabilizing all of
these. Over the coming weeks and months you can expect individual projects to
begin announcing support for WASI 0.3.

## Changes towasi:http

The interface that has seen the most change iswasi:http. We haven’t just
mechanically converted poll-based interfaces to native async ones, but actually
reorganized the worlds and changed some of the core abstractions.wasi:httpnow exposes two worlds:wasi:http/serviceandwasi:http/middleware:

interface client { /* ... */ }
interface handler { /* ... */ }

// When used by guest bindings generators, grant the
// ability to make HTTP calls through the `client` import, and
// handle incoming HTTP requests through the `handler` export.
world service {
 import client;
 export handler;
}

// The middleware world is a super-set of the service world.
world middleware {
 include service; // ← Do everything that `service` can do.
 import handler; // ← But also pass incoming requests down to another handler.
}

Themiddlewareworld replaces the 0.2-eraproxyworld, and is used to define
HTTP handlers which can forward requests to other handlers. What’s new in WASI
0.3 is that this can now performservice
chaining:
a pattern where components can be directly composed with one another. This means
components acting as microservices that frequently interop with other
microservices, do not need to go over the network. Instead a runtime can choose
to directly compose them with each other inside the same process. For most
microservices this will reduce the time for calling other microservices from milliseconds to nanoseconds: six orders of magnitude.

## Conclusion

We’re happy to share that WASI 0.3 has been released. That means that:

* Spec ratified: WASI 0.3 has passed the WASI Subgroup vote. This is a stable release, which means programs you compile for it today are guaranteed to keep working in the future. Even as we continue to release patch release every two months, e.g. 0.3.x.
* Wasmtime: Wasmtime 45 runs the latest release candidate today, and Wasmtime 46 will ship WASI 0.3.0 with Component Model Async enabled by default.
* Jco close behind: jco, the JavaScript Component Model toolchain, also supports all of WASI 0.3. A release that has support enabled by default will be going out soon.
* Guest toolchains next.In parallel, work is in progress to enable WASI 0.3 in guest toolchains. As these release, you’ll be able to write WASI 0.3 components in Rust, Go, JavaScript, Python, and more.

The best place to get started with WebAssembly Components is theWasm Component Model book.
For a comprehensive list of changes, see theWASI 0.3.0 release notes. If you’re wondering what’s next for WebAssembly Components and WASI, seeThe Road to Component Model 1.0.

WASI 0.3 is the work of a community. Thank you to everyone in the WASI Subgroup who designed, debated, and refined this release, to the runtime and toolchain maintainers who built the implementations that make it real, and to every contributor who filed an issue, reviewed a PR, or asked the hard question that made the spec better. And thank you to the users building on WASI; your components, your feedback, and your willingness to try release candidates shaped what shipped.

Component Model’s native async was years in the making, and it opens a new chapter: one where async and composability are first-class, and where the same primitives serve every language. We can’t wait to see what you build on it. Welcome to WASI 0.3.