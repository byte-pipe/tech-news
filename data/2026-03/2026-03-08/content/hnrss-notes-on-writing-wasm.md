---
title: Notes on Writing Wasm
url: https://notes.brooklynzelenka.com/Blog/Notes-on-Writing-Wasm
site_name: hnrss
content_file: hnrss-notes-on-writing-wasm
fetched_at: '2026-03-08T19:10:31.483450'
original_url: https://notes.brooklynzelenka.com/Blog/Notes-on-Writing-Wasm
date: '2026-03-08'
description: I’ve been writing an increasing amount of Rust‑based Wasm over the past few years.
tags:
- hackernews
- hnrss
---

I’ve been writing an increasing amount ofRust‑basedWasmover the past few years. The internet has many opinions about Wasm, andwasm-bindgenis — let’s say — not universally beloved, but as I get more experience with it and learn how to work around its shortcomings, I’ve found some patterns that have dramatically improved my relationship with it.

I want to be clear up front about two things:

1. I deeply appreciate the work of thewasm-bindgenmaintainers.
2. It’s entirely possible that there are better ways to work with bindgen than presented here; this is just what’s worked for me in practice!

I’ve seen excellent programmers really fight with bindgen. I don’t claim to have all the answers, but this post documents a set of patterns that have made Rust+Wasm dramatically less painful for me.

# TL;DR

Unless you have a good reason not to:

1. Pass everything over the Wasm boundary by&reference
2. PreferRc<RefCell<T>>orArc<Mutex<T>>1over&mut
3. Do not deriveCopyon exported types
4. Usewasm_refgenfor any type that needs to cross the boundary in a collection (Vec, etc)
5. Prefix all Rust-exported types withWasm*and set thejs_name/js_classto the unprefixed name
6. Prefix all JS-imported types withJs*
7. ImplementFrom<YourError> for JsValueusingjs_sys::Errorfor all of Rust-exported error types

Some of these may seem strange without further explanation. Below give more of the rationale in detail.

# A Quick Refresher

wasm-bindgengenerates glue code that lets Rust structs, methods, and functions be called from JS/TS. Some Rust types have direct JS representations (those implementingIntoWasmAbi); others live entirely on the Wasm side and are accessed through opaque handles.

Wasm bindings often look something like this:

#[wasm_bindgen(js_name 
=
 Foo
)]

pub
 struct
 WasmFoo
(
RustFoo
)

 

#[wasm_bindgen(js_name 
=
 Bar
)]

pub
 struct
 WasmBar
(
RustBar
)

Conceptually, JS holds tiny objects that look like{ __wbg_ptr: 12345 }, which index into a table on the Wasm side that owns the real Rust values.

The tricky part is that you’re juggling two memory models at once:

* JavaScript: garbage‑collected, re‑entrant, async
* Rust: explicit ownership, borrowing, aliasing rules

Bindgen tries to help, but it both under‑ and over‑fits: some safe patterns are rejected, and some straight-up footguns are happily accepted. Ultimately, everything that crosses the boundary must have some JS representation, so it pays to be cognisant about what that representation is.

flowchart TD
 subgraph JavaScript
 subgraph Foo
 jsFoo["{ __wbg_ptr: 42817 }"]
 end

 subgraph Bar
 jsBar["{ __wbg_ptr: 71902 }"]
 end
 end

 subgraph Wasm
 subgraph table[Boundary Table]
 objID1((42817)) --> WasmFoo

 subgraph WasmFoo
 arc1[RustFoo]
 end

 objID2((71902)) --> WasmBar
 subgraph WasmBar
 arc2[RustBar]
 end
 end
 end

 jsFoo -.-> objID1
 jsBar -.-> objID2

## Should You Write Manual Bindings?

My take on most things is “you do you”, and this one is very much a matter of taste. I see a fair amount of code online that seems to prefer manual conversions withjs_sys. This is a reasonable strategy, but I have found it to be time consuming and brittle. If you change your Rust types, the compiler isn’t going to help you when you’re manually callingdyn_intoto do runtime checks. Bindgen is going to insert the same runtime checks either way, but if you lean into its glue (including with some of the patterns presented here), you can get much better compile-time feedback.

# Names Matter

It’s an old joke that the two hardest problems in computer science are naming, caching, and off-by-one-errors. Naming is extremely important for mental framing and keeping track of what’s happening, both of which can be a big source of pain when working with bindgen. As a rule, I use the current naming conventions:

## IntoWasmAbiTypes

QUOTE

TraitIntoWasmAbi[…] A trait for anything that can be converted into a type that can cross the Wasm ABI directly.—Source

These are the primitive types of Wasm, such asu32,String,Vec<u8>, and so on. They get converted to/from native JS and Rust types when they cross the boundary. We do not need to do anything to these types.

## Rust-Exported Structs GetWasm*

This is where you’ll usually spend most of your time. Wrapping Rust enums and structs in newtypes to re-expose them to JS is the bread and butter of Wasm. These wrappers get prefixed withWasm*to help distinguish them from JS-imported interfaces,IntoWasmAbitypes, and plain Rust objects. On the JS-side we can strip theWasm, since it will only get the one representation, and (if done correctly) the JS side generally doesn’t need to distinguish where a type comes from.

#[derive(
Debug
, 
Clone
, 
Copy
, 
PartialOrd
, 
Ord
, 
PartialEq
, 
Eq
)]

pub
 enum
 StreetLight
 {

 Red
,

 Yellow
,

 Gree
,

}

 

#[derive(
Debug
, 
Clone
, 
PartialOrd
, 
Ord
, 
PartialEq
, 
Eq
)]

#[wasm_bindgen(js_name 
=
 StreetLight
)]

pub
 struct
 WasmStreetLight
(
StreetLight
)

 

#[wasm_bindgen(js_class 
=
 StreetLight
)]

impl
 WasmStreetLight
 {

 #[wasm_bindgen(constructor)]

 pub
 fn
 new
() 
->
 Self
 {

 Self
(
StreetLight
::
Red
)

 }

 

 // ...

}

On the JS side, there’s only one StreetLight, so the prefix disappears. On the Rust side, the prefix keeps exported types visually distinct from:

* Plain Rust types
* JS‑imported interfaces
* IntoWasmAbivalues

## JS-Imported Interfaces GetJs*

Any interface brought into Rust viaextern "C"get aduck typedinterface (by default). These pass over the boundary without restriction, which makes them a very helpful escape hatch ___.

#[wasm_bindgen]

extern
 "C"
 {

 #[wasm_bindgen(js_name 
=
 logCurrentTime)]

 pub
 fn
 js_log_current_time
(
timestamp
:
 u32
);

}

 

#[wasm_bindgen]

extern
 "C"
 {

 #[wasm_bindgen(js_name 
=
 Hero
)]

 type
 JsCharacter
;

 

 #[wasm_bindgen(method, getter, js_name 
=
 hp)]

 pub
 fn
 js_hp
(
this
:
 &
JsCharacter
) 
->
 u32
;

}

 

// Elsewhere

const
 gonna_win
:
 bool
 =
 maelle
.
js_hp
() 
!=
 0

Duck typing is really helpful for cases where you want to expose a Rust trait to JS: as long as your Rust-exported type implements the interface, you can accept your Rust-exported type a JS-imported type, while retaining the ability to replace it with JS-imported types. A concrete example is if you’re exporting a storage interface, you likely have a default Rust implementation, but want extensibility if downstream devs want to give it an IndexedDB or S3 backend.

NOTE

We’re going to abuse this “duck typed JS-imports on a Rust-export” later forwasm_refgen.

The main gotchas with this approach are that 1. it’s brittle if the interface changes, and 2. if you don’t prefix your methods on the Rust-side withjs_*, you can run into namespace collisions (hence why I recommend prefixing these everywhere by convention). As an added bonus, this makes youveryaware of where you’re making method calls over the Wasm boundary.

# Don’t DeriveCopy

Copymakes it trivially easy to accidentally duplicate a Rust value that is actually a thin handle to a resource, resulting in null pointers. Just make a habit of avoiding it on exported wrappers. This can be a hard muscle memory to break since we usuallywantCopywherever possible in normal Rust code.

Copyis only acceptable when exporting wrapping around pure data that hasIntoWasmAbi, never for handles. I chalk this up as an optimisation; default to non-Copyunless you’rereallysure it’s okay.

# Avoiding Broken Handles

Try as it might,wasm-bindgenis unable to prevent handles breaking at runtime. A common culprit is passing an owned value to Rust:

#[wasm_bindgen(js_class 
=
 Foo
)]

impl
 WasmFoo
 {

 #[wasm_bindgen(js_name 
=
 "doSomething"
)]

 pub
 fn
 do_something
(
&
self
, 
bar
:
 Bar
) 
->
 Result
<(), 
Error
> {

 // ...

 }

 

 #[wasm_bindgen(js_name 
=
 "doSomethingElse"
)]

 pub
 fn
 do_something_else
(
&
self
, 
bars
:
 Vec
<
Bar
>) 
->
 Result
<(), 
Error
> {

 // ...

 }

}

If you do the above, it will of course consume yourBar(s), but since this goes over the boundary you get no help from the compiler about how you manage the JS side! The object will get freed on the Rust side, but you still have a JS handle that now points to nothing. You might say something like “so much for memory safety”, and you wouldn’t be wrong.

Why would you find yourself in this situation? There’s a couple reasons:

* Bindgen forbids&[T]unlessT: IntoWasmAbi
* Vec<&T>is not allowed
* You just want the compiler to stop yelling

Types that have areIntoWasmAbithat are notCopyget cloned over the boundary (no handle) so they behave differently from both non-IntoWasmAbiandCopytypes

## Prefer Passing By Refence (by Default)

If you take one thing from this post, take this:

INFO

Never consume exported values across the boundary unless you have a clear reason to do so and are going to manage the handle on the JS side.

This one if pretty straightforward: pass everything around by reference. Consuming a value is totally “legal” to the compiler since it will happily free the memory on Rust side,but the JS-side handle will not get cleaned up. The next time you go to use that handle, it willthrowan error. Unless you’re doing something specific with memory management, just outright avoid this situation: pass by&referenceand use interior mutability.

This is a pretty easy pattern to follow: default to wrapping non-IntoWasmAbitypes inRc<RefCell<T>>orArc<Mutex<T>>1depending on if and how you have your code structured for async. The cost of going over the Wasm boundary definitely eclipses anRcbump, so this is highly unlikely to be a performance bottleneck.

#[derive(
Debug
, 
Clone
)]

#[wasm_bindgen(js_name 
=
 Foo
)]

pub
 struct
 WasmFoo
(
pub
(
crate
) 
Rc
<
RefCell
<
Foo
>>)

 

#[derive(
Debug
, 
Clone
)]

#[wasm_bindgen(js_name 
=
 Bar
)]

pub
 struct
 WasmBar
(
pub
(
crate
) 
Rc
<
RefCell
<
Bar
>>)

 

#[wasm_bindgen(js_class 
=
 Foo
)]

impl
 WasmFoo
 {

 #[wasm_bindgen(js_name 
=
 "doSomething"
)]

 pub
 fn
 do_something
(
&
self
, 
bar
:
 WasmBar
) 
->
 Result
<(), 
Error
> {

 // ...

 }

}

## Avoid&mut

This one can be pretty frustrating when it happens: there are cases where taking&mut selfcan throw runtime errors due to re-entrancy. This pops up more frequently than I would have expected given that the default behaviour of JS is single threaded, but JS’sasyncdoesn’t have to respect Rust’s compile-time exclusivity2checks.

INFO

If you can’t prove exclusivity, don’t pretend you have it. Use the relevant interior‑mutability primitive for your concurrency model.

# Ducking Around Reference Restrictions

As mentioned earlier, you can useextern "C"JS-imports to model any duck typed interface,includingRust-exports. This means that we are able to work around several restrictions3inwasm-bindgen.

## Owned Collection Restriction

Bindgen restricts which types can be passed across the boundary. The one folks often run into first is that&[T]only works whenTisIntoWasmAbi(including JS-imported types4) — i.e. usually not your Rust-exported structs. This means that you are often forced to construct aVec<T>. This makes sense since JS is going to take control over the resulting JS array, and can mutate it as it pleases. It also means that when the type comes back in, you are unable to accept it as&[T]orVec<T>unless the earlierIntoWasmAbicaveat applies.

A classic example of this is returning an ownedVec<T>of instead of a slice whenTdoes not implement a JS-managed type. What’s returned to JS are not a bunch ofTs, but ratherhandles(e.g.{ __wbg_ptr: 12345 }) toTs that live on the Wasm side.4

On the other hand,we’reable to treat handles as duck typed objects that conform to some interface. Handles are far less restricted than Rust-exported types, and can be passed around more freely.

The workaround is fairly straightforward:

* Make your exported type cheap to clone
* Expose a namespaced clone method
* Import that method via a JS interface
* Convert with friendly ergonomics (.into)

// Step 1: make it inexpensive to `clone` (i.e. using `Rc` or `Arc` if not already cheap)

#[derive(
Debug
, 
Clone
)]

#[wasm_bindgen(js_name 
=
 Character
)]

pub
 struct
 WasmCharacter
(
Rc
<
RefCell
<
Character
>>)

 

#[wasm_bindgen(js_class 
=
 Character
)]

impl
 WasmCharacter
 {

 // ...

 

 // Step 2: expose a *namespaced* (important!) `clone` function on the Wasm export

 #[doc(hidden)]

 pub
 fn
 __myapp_character_clone
(
&
self
) 
->
 Self
 {

 self
.
clone
()

 }

}

 

#[wasm_bindgen]

extern
 "C"
 {

 type
 JsCharacter

 

 // Step 3: create a JS-imported interface with that namespaced `clone`

 pub
 fn
 __myapp_character_clone
(
this
:
 &
JsCharacter
) 
->
 WasmCharacter
;

}

 

// Step 4: for convenience, wrap the namespaced clone in a `.from`

impl
 From
<
JsChcaracter
> 
for
 WasmCharacter
 {

 fn
 from
(
js
:
 JsCharacter
) 
->
 Self
 {

 js
.
__myapp_character_clone
()

 }

}

 

// Nicely typed Vec

// Step 5: use it! vvvvv

pub
 fn
 do_many_things
(
js_foos
:
 Vec
<
JsFoo
>) {

 let
 rust_foos
:
 Vec
<
WasmFoo
> 
=
 js_foos
.
iter
()
.
map
(Into
::
into
)
.
collect
();

 // ... ^^^^^^^

 // Converted

}

This still requires that you to manually track which parts bindgen thinks are JS-imports and which it thinks are Rust-exports, but with ournaming conventionit’s pretty clear what’s happening. The conversion isn’tfree, but (IMO) it makes your interfaces significantly more flexible and legible.

### Usewasm_refgen

The above pattern can be a bit brittle — even while writing the boilerplate — since all of the names have to line upjust so, and you don’t get compiler help when crossing the boundary like this. To help make this more solid, I’ve wrapped this pattern up as a macro exported fromwasm_refgen.

use
 std
::
{rc
::
Rc
, cell
::
RefCell
};

use
 wasm_bindgen
::
prelude
::*
;

use
 wasm_refgen
::
wasm_refgen;

 

#[derive(
Clone
)]

#[wasm_bindgen(js_name 
=
 "Foo"
)]

pub
 struct
 WasmFoo
 {

 map
:
 Rc
<
RefCell
<
HashMap
<
String
, 
u8
>>>, 
// Cheap to clone

 id
:
 u32
 // Cheap to clone

}

 

#[wasm_refgen(js_ref 
=
 JsFoo
)]
 // <-- THIS

#[wasm_bindgen(js_class 
=
 "Foo"
)]

impl
 WasmFoo
 {

 // ... your normal methods

}

Here’s a diagram from the README about how it works:

 ┌───────────────────────────┐

 │ │

 │ JS Foo instance │

 │ Class: Foo │

 │ Object { wbg_ptr: 12345 } │

 │ │

 └─┬──────────────────────┬──┘

 │ │

 │ │

 Implements │

 │ │

 │ │

 ┌───────────▼───────────────┐ │

 │ │ │

 │ TS Interface: Foo │ Pointer

 │ only method: │ │

 │ __wasm_refgen_to_Foo │ │

 │ │ │

 └───────────┬───────────────┘ │

JS/TS │ │

─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─│─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┼ ─ ─ ─ ─ ─ 

 Wasm │ │

 │ │

 ┌───────────┼──────────────────────┼───────────┐

 │ ▼ ▼ │

 │ ┌────────────────┐ ┌────────────────┐ │

 │ │ │ │ │ │

 │ │ &JsFoo ◀────────▶ WasmFoo │ │

 │ │ Opaque Wrapper │ │ Instance #1 │ │

 │ │ │ │ │ │

 │ └────────────────┘ └────────────────┘ │

 └──────────────────────┬───────────────────────┘

 │

 │

 Into::into

 (uses `__wasm_refgen_to_Foo`) 

 (which is a wrapper for `clone`)

 │

 │

 ▼

 ┌────────────────┐

 │ │

 │ WasmFoo │

 │ Instance #2 │

 │ │

 └────────────────┘

References passed over the boundary are already passed by ownership by bindgen — but these handles grab the reference off the boundary table. Recall that ourInto::intocallscloneunder the hood, so these are always safe to consume without breaking the JS handle!

pub
 fn
 do_many_things
(
js_foos
:
 Vec
<
JsFoo
>) {

 let
 rust_foos
:
 Vec
<
WasmFoo
> 
=
 js_foos
.
iter
()
.
map
(Into
::
into
)
.
collect
();

 // ...

}

# Automatically Convert To JS Errors

There are a few ways to handle errors coming from Wasm, but IMO the best balance of detail and convenience is to turn them intojs_sys::Errors on their way toJsValue. This lets us returnResult<T, MyError>instead ofResult<T, JsValue>.

For example, let’s say we have this type:

#[derive(
Debug
, 
Clone
, thiserror
::
Error
)]

pub
 enum
 RwError
 {

 #[error(
"cannot read {0}"
)]

 CannotRead
(
String
),

 

 #[error(
"cannot write"
)]

 CannotWrite

}

The fact that this is an enum is actually not a problem (the rest of the technique would work), but if you’re wrapping a different crate you’ll need a newtype wrapper:

// Important: no #[wasm_bindgen]

#[derive(
Debug
, 
Clone
, thiserror
::
Error
)]

#[error(transparent)]
 

pub
 struct
 WasmRwError
(
#[from]
 RwError
) 
// #[from] gets us `?` notation to lift into the newtype

We “could” slap a#[wasm_bindgen]on this and call it a day, but then we wouldn’t get nice error info on the JS side. Instead, we convert toJsValueourselves with this final bit of glue:

impl
 From
<
WasmRwError
> 
for
 JsValue
 {

 fn
 from
(
wasm
:
 WasmRwError
) 
->
 Self
 {

 let
 err
 =
 js_sys
::
Error
::
new
(
&
wasm
.
to_string
()); 
// Error message

 err
.
set_name
(
"RwError"
); 
// Nice JS error type

 err
.
into
() 
// Convert to `JsValue`

 }

}

Now you can returnResult<T, WasmRwError>, including if you want to call the Wasm-wrapped function elsewhere in your code. It retains the nice error on the Rust side (at minimum types-as-documentation). You also get?notation without needing to do in-placeJsValueconversion everywhere this error occurs; bindgen will helpfully do the conversion for you.

* Typed Rust errors
* ?propagation
* Real JSErrorobjects
* Zero boilerplate at call sites

This works as a copy-paste template; I’ve considered wrapping it as a macro but it’s less than 10 LOC. I was actually surprised that something like#[wasm_bindgen(error)]wasn’t available (maybe it is and I just can’t find it; heck maybe it’s worth contributing upstream).

# Print Build Info

This is a quality of life improvement that has saved me many hours of grief: print the exact build version, dirty status, and Git hash to theconsoleon startup. If you’re working on your Wasm project at the same time as developing a pure-JS library that consumes it, getting a JS bundler likeViteto pick up changes can be flaky at best.

This takes a bit of setup, especially if you’re in a Cargo workspace, but pays off. Here’s my current setup:

$WORKSPACE/Cargo.toml
[
workspace
]

resolver
 =
 "
3
"

members
 =
 [

 "
build_info
"
,

 # ...

]

$WORKSPACE/build_info/Cargo.toml
[
package
]

name
 =
 "
build_info
"

publish
 =
 false

# ...

$WORKSPACE/build_info/build.rs
use
 std
::
{

 env, fs,

 path
::
{
Path
, 
PathBuf
},

 process
::
Command
,

 time
::
{
SystemTime
, 
UNIX_EPOCH
},

};

 

#[allow(clippy
::
unwrap_used)]

fn
 main
() {

 let
 ws
 =
 env
::
var
(
"CARGO_WORKSPACE_DIR"
)
.
map_or_else
(

 |
_
|
 PathBuf
::
from
(env
::
var
(
"CARGO_MANIFEST_DIR"
)
.
unwrap
()),

 PathBuf
::
from
,

 );

 

 let
 repo_root
 =
 find_repo_root
(
&
ws
)
.
unwrap_or
(
ws
.
clone
());

 let
 git_dir
 =
 repo_root
.
join
(
".git"
);

 

 watch_git
(
&
git_dir
);

 

 let
 git_hash
 =
 cmd_out
(

 "git"
,

 &
[

 "-C"
,

 #[allow(clippy
::
unwrap_used)]

 repo_root
.
to_str
()
.
unwrap
(),

 "rev-parse"
,

 "--short"
,

 "HEAD"
,

 ],

 )

 .
unwrap_or_else
(
||
 "unknown"
.
to_string
());

 

 let
 dirty
 =
 cmd_out
(

 "git"
,

 &
[
"-C"
, 
repo_root
.
to_str
()
.
unwrap
(), 
"status"
, 
"--porcelain"
],

 )

 .
is_some_and
(
|
s
|
 !
s
.
is_empty
());

 

 let
 git_hash
 =
 if
 dirty
 {

 let
 secs
 =
 SystemTime
::
now
()

 .
duration_since
(
UNIX_EPOCH
)

 .
unwrap
()

 .
as_secs
();

 format!
(
"{git_hash}-dirty-{secs}"
)

 } 
else
 {

 git_hash

 };

 

 println!
(
"cargo:rustc-env=GIT_HASH={git_hash}"
);

}

 

fn
 cmd_out
(
cmd
:
 &
str
, 
args
:
 &
[
&
str
]) 
->
 Option
<
String
> {

 Command
::
new
(
cmd
)
.
args
(
args
)
.
output
()
.
ok
()
.
and_then
(
|
o
|
 {

 if
 o
.
status
.
success
() {

 Some
(String
::
from_utf8_lossy
(
&
o
.
stdout)
.
trim
()
.
to_string
())

 } 
else
 {

 None

 }

 })

}

 

fn
 find_repo_root
(
start
:
 &
Path
) 
->
 Option
<
PathBuf
> {

 let
 mut
 cur
 =
 Some
(
start
);

 while
 let
 Some
(
dir
) 
=
 cur
 {

 if
 dir
.
join
(
".git"
)
.
exists
() {

 return
 Some
(
dir
.
to_path_buf
());

 }

 cur
 =
 dir
.
parent
();

 }

 None

}

 

fn
 watch_git
(
git_dir
:
 &
Path
) {

 println!
(
"cargo:rerun-if-changed={}"
, 
git_dir
.
join
(
"HEAD"
)
.
display
());

 

 if
 let
 Ok
(
head
) 
=
 fs
::
read_to_string
(
git_dir
.
join
(
"HEAD"
)) {

 if
 let
 Some
(
rest
) 
=
 head
.
strip_prefix
(
"ref: "
)
.
map
(str
::
trim
) {

 println!
(
"cargo:rerun-if-changed={}"
, 
git_dir
.
join
(
rest
)
.
display
());

 println!
(

 "cargo:rerun-if-changed={}"
,

 git_dir
.
join
(
"packed-refs"
)
.
display
()

 );

 }

 }

 

 println!
(
"cargo:rerun-if-changed={}"
, 
git_dir
.
join
(
"index"
)
.
display
());

 

 let
 fetch_head
 =
 git_dir
.
join
(
"FETCH_HEAD"
);

 if
 fetch_head
.
exists
() {

 println!
(
"cargo:rerun-if-changed={}"
, 
fetch_head
.
display
());

 }

}

$WORKSPACE/build_info/src/lib.rs
#![no_std]

pub
 const
 GIT_HASH
:
 &
str
 =
 env!
(
"GIT_HASH"
);

…and finally where to get it to print in Wasm:

use
 wasm_bindgen
::
prelude
::*
;

 

// ...

 

#[wasm_bindgen(start)]

pub
 fn
 start
() {

 set_panic_hook
();

 

 // I actually use `tracing::info!` here,

 // but that's out of scope for this article

 web_sys
::
console
.
info1
(
format!
(

 "️your_package_wasm v{} ({})"
,

 env!
(
"CARGO_PKG_VERSION"
),

 build_info
::
GIT_HASH

 ));

}

# Wrap Up

Rust+Wasm is powerful—but unforgiving if you pretend the boundary isn’t there. Be explicit, name things clearly, pass by reference, and duck typing around any (unreasonable) limitations bindgen places on you.

With any luck, that’s helpful to others! I may update this over time as I find myself using more patterns.

## Footnotes

1. FWIW I preferfutures::lock::Mutexonstd, orasync_lock::Mutexunderno_std.↩↩2
2. I’m actually more annoyed by Rust on this one (see earlier comment about naming being important).&mutisn’t “just” a mutable reference; it’s anexclusivereference, which happens to make direct mutability viable, but the semantics are more about exclusivity.↩
3. I sometimes wonder if it’s my lot in life to import features between langauges.Witchcraftwas my first real library of note, and I can’t seem to stop abusing languages this way 😅↩
4. This simple example is already more nuance than would be ideal to juggle when writing code.↩↩2