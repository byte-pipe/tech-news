---
title: Parse, don't Validate and Type-Driven Design in Rust — ramblings of @harudagondi
url: https://www.harudagondi.space/blog/parse-dont-validate-and-type-driven-design-in-rust/
site_name: hnrss
content_file: hnrss-parse-dont-validate-and-type-driven-design-in-rust
fetched_at: '2026-02-22T11:08:28.626931'
original_url: https://www.harudagondi.space/blog/parse-dont-validate-and-type-driven-design-in-rust/
date: '2026-02-21'
description: Applying the type-driven mindset to rust via the "Parse, don't Validate" pattern
tags:
- hackernews
- hnrss
---

# Parse, don't Validate and Type-Driven Design in Rust


Reading time:
 17 min read




## Table of Contents


1.1
 Dividing by zero
1.2
 Examples in the wild
1.3
 Maxims of Type Driven Design
1.4
 What can we do?
1.5
 Conclusion










Photo by theTingley Injury Law Firm.




In the Rust Programming Language Community Server, there’s tag named-parse-dont-validatewhich links to anarticleabout the concept of avoiding validation functions and encoding invariants in the type level instead. I usually recommend it to beginners/intermediates to Rust who are struggling with designing APIs.

The only problem is that it uses Haskell to explain its concepts.

Yeah, it’sfine, but for beginners unfamiliar with the functional paradigm, it might not be so approachable. And so I wanted so write a blog post about this pattern but in a rather Rust-centric way. So let’s start!

## Dividing by zero#

One basic example I can give is a function that divides a number by another number.

fn

divide
(
a
:

i32
,

b
:

i32
)

->

i32

{

a

/

b
}

This is fine, but unfortunately it can panic whenbhas the value of zero:

fn

main
()

{

let

a

=

5
;

let

b

=

0
;

dbg!
(
divide
(
a
,

b
));
}

This gives anerror:


Compiling

playground

v0
.
0
.
1

(
/
playground
)

Finished
 `
dev
`
profile

[
unoptimized

+

debuginfo
]

target
(
s
)

in

1
.
28s

Running
 `
target
/
debug
/
playground
`

thread

'
main
'

(
41
)

panicked

at

src
/
main
.
rs
:
2
:
5
:
attempt

to

divide

by

zero
note
:

run

with
 `
RUST_BACKTRACE=
1
`
environment

variable

to

display

a

backtrace

That’s fine and dandy if we want erroneous values to fail loudly at runtime, but what if we want stronger guarantees? This is especially important when some operations don’t fail loudly, like the following:

fn

divide_floats
(
a
:

f32
,

b
:

f32
)

->

f32

{

a

/

b
}

fn

main
()

{

let

a

=

5
.
0
;

let

b

=

0
.
0
;

dbg!
(
divide_floats
(
a
,

b
));
}

Compiling

playground

v0
.
0
.
1

(
/
playground
)

Finished
 `
dev
`
profile

[
unoptimized

+

debuginfo
]

target
(
s
)

in

0
.
62s

Running
 `
target
/
debug
/
playground
`
[
src
/
main
.
rs
:
8
:
2
]

divide_floats
(
a
,

b
)

=

inf

There’s no error! But do we want that?

We could add anassert!in thedivide_floatsfunction to emulate typical integer division behavior.

fn

divide_floats
(
a
:

f32
,

b
:

f32
)

->

f32

{

assert_ne!
(
b
,

0
.
0
,

"Division by zero is not allowed."
);

a

/

b
}

Compiling

playground

v0
.
0
.
1

(
/
playground
)

Finished
 `
dev
`
profile

[
unoptimized

+

debuginfo
]

target
(
s
)

in

0
.
65s

Running
 `
target
/
debug
/
playground
`

thread

'
main
'

(
32
)

panicked

at

src
/
main
.
rs
:
2
:
5
:
assertion
 `
left

!=

right
`
failed
:

Division

by

zero

is

not

allowed
.

left
:

0
.
0

right
:

0
.
0

Cute! But there’s still a problem of running into panics only at runtime. My beef with Python (or any other dynamic language for that matter) is that a lot of errors only arises when you run the program. That’s why they’re adding typechecking to these languages: people want to bubble some mistakes to compile-time (or typecheck-time, whatever). We can use Rust’s rich type system to communicate these errors at build time.

One way, which I think is the more common way as people are more familiar with it is the idea of fallible functions, which return either anOptionor aResult.

fn

divide_floats
(
a
:

f32
,

b
:

f32
)

->

Option
<
f32
>

{

if

b

==

0

{

return

None
;

}

Some
(
a

/

b
)
}

This is a fine way to do things, as it communicates that (1) the function can fail, and (2) you can handle the failing case after.††Of course,catch_unwindexists, but I’m pretending that it doesn’t.To me, the function’s invariants (bmust not be zero) is encoded after-the-fact, aka in the return typeOption<T>. This implies to me that the invariants could be encoded before-the-fact, aka in the function parameters. But what would that look like?

Enter the newtype pattern.

Say, let’s have a type that is something likef32, but it’s guaranteed to never be zero. We’ll name itNonZeroF32:

struct

NonZeroF32
(
f32
);

This struct only contains a single fieldf32. The semantics of the type understood from the name is that it’s just like a normalf32, but does not allow the value of zero. How do we guarantee this? Since rust does encapsulation at the module level, we make this type public while have its field private.

mod

nonzero

{

pub

struct

NonZeroF32
(
f32
);
}

Then, the only way to construct this type is via a fallible constructor function:

impl

NonZeroF32

{

fn

new
(
n
:

f32
)

->

Option
<
NonZeroF32
>

{

if

n

==

0

{

return

None
;

}


Some
(
NonZeroF32
(
n
))

}
}

Remember to add some convenience traits.

impl

Add

for

NonZeroF32

{

...

}
impl

Add
<
f32
>

for

NonZeroF32

{

...

}
impl

Add
<
NonZeroF32
>

for

f32

{

...

}
//
 and a bunch of other operators...

We can then use this in ourdivide_floatsfunction.

fn

divide_floats
(
a
:

f32
,

b
:

NonZeroF32
)

->

f32

{

a

/

b
}

There is an interesting implication in this pattern.

In the second version ofdivide_floats, we changed the return type fromf32toOption<f32>just to avoid the panics. As described in the original article by Alexis King, this is aweakeningof the return type, and the function’s promise. We temper the caller’s expectation by saying that yes, this function can fail in some way, and you have to account for that. And that weakening is described in the type system via theOptionenum.

In the third iteration ofdivide_floats, we change our perspective and ask ourselves “instead of weakening the return type, what if westrengthenthe function parameters?” We communicated that via accepting aNonZeroF32. Instead of having the validation code in our functions, we instead push that responsibility to the caller. The validation now happens before the function execution.

To see the advantage of pushing the validation forward to the user, let’s say we have another function like so:

//
 The quadratic formula!
fn

roots
(
a
:

f32
,

b
:

f32
,

c
:

f32
)

->

[
f32
;

2
]

{

//
 For the sake of demonstration we will be ignoring complex roots

let

discriminant

=

b

*

b

-

4

*

a

*

c
;

[

-
b

+

discriminant
.
sqrt
()

/

(
2

*

a
),

-
b

-

discriminant
.
sqrt
()

/

(
2

*

a
),

]
}

This function can fail if the discriminant is negative (which we will be ignoring in this contrived example), and ifais zero. The two ways of going about this can be written as follows:

fn

try_roots
(
a
:

f32
,

b
:

f32
,

c
:

f32
)

->

Option
<[
f32
;

2
]>

{

if

a

==

0

{

return

None
;

}

//
 ...
}

fn

newtyped_roots
(
a
:

NonZeroF32
,

b
:

f32
,

c
:

f32
)

->

[
f32
;

2
]

{

//
 unchanged
}

TheOptionversion has me duplicating the conditional for at least two different functions, which might be icky if you are a DRY-hard. Also, not only the function has to validate if the float can be zero, thecallermust then validate again by matching on the returnedOption. That seems redundant. It would be ideal if we only need to check only once.

let

roots

=

try_roots
(
5
,

4
,

7
);

//
 `try_roots` does a validation check
//
 and then we validate it again by matching on the result
match

roots

{

Some
(
result
)

=>

do_something
(),

None

=>

{

handle_error
();

return

},
}

TheNonZeroF32version can help with that as validation happens before, and happens once, instead of twice.

//
 Handle the special case once
let

Some
(
a
)

=

NonZeroF32
::
new
(
5
)

else

{

handle_error
();

return
;
}

//
 `newtyped_roots` does not need to handle it again,
//
 indicated by the function not needing to return
//
 an `Option` and us handling the result.
let

[
root1
,

root2
]

=

newtyped_roots
(
a
,

4
,

7
);

Moving away from thedivide_floats, let’s now use an example from the original blog post, converted to Rust:

fn

get_cfg_dirs
()

->

Result
<
Vec
<
PathBuf
>,

Box
<
dyn

Error
>>

{

let

cfg_dirs_string

=

std
::
env
::
var
(
"CONFIG_DIRS"
)
?
;


let

cfg_dirs_list

=

cfg_dirs_string
.
split
(
'
,
'
)

.
map
(
PathBuf
::
from
)

.
collect
::
<
Vec
<
PathBuf
>>();


if

cfg_dirs_list
.
is_empty
()

{

return

Err
(
"CONFIG_DIRS cannot be empty"
.
into
());

}


Ok
(
cfg_dirs_list
)
}

fn

main
()

->

Result
<(),

Box
<
dyn

Error
>>

{

let

cfg_dirs

=

get_cfg_dirs
()
?
;

match

cfg_dirs
.
first
()

{

Some
(
cache_dir
)

=>

init_cache
(
cache_dir
),

None

=>

unreachable!
(
"should never happen; already checked configDirs is non-empty"
),

}
}

Notice the following:

1. We checked ifcfg_dirs_listis empty in theget_cfg_dirsfunction. Then, we still had to “check” it again in themainfunction by matching oncfg_dirs.first(). TheVecwas known to be nonempty, do we have to check it again? Consequently, doesn’t this have an impact on performance, especially if we have to check it again and again and again?
2. The original post raised a good point about resilience to refactors. If for some reason theis_emptygets refactored out for some reason, and the programmer forgot to updatemain, then theunreachable!branch might actually get reached and explode your computer or whatever.

If we instead had a specialNonEmptyVec<T>newtype (well, not exactly special) where its existence guarantees that the Vec is never empty, we could do

struct

NonEmptyVec
<
T
>(
T
,

Vec
<
T
>);

impl
<
T
>

NonEmptyVec
<
T
>

{

//
 Notice that we don't need to return an `Option`

fn

first
(
&
self
)

->

&
T

{

...

}
}

fn

get_cfg_dirs
()

->

Result
<
NonEmptyVec
<
PathBuf
>,

Box
<
dyn

Error
>>

{

let

cfg_dirs_string

=

std
::
env
::
var
(
"CONFIG_DIRS"
)
?
;


let

cfg_dirs_list

=

cfg_dirs_string
.
split
(
'
,
'
)

.
map
(
PathBuf
::
from
)

.
collect
::
<
Vec
<
PathBuf
>>();


//
 We parse the `Vec` into a more structured type

let

cfg_dirs_list

=

NonEmptyVec
::
try_from
(
cfg_dirs_list
)
?
;


Ok
(
cfg_dirs_list
)
}

fn

main
()

->

Result
<(),

Box
<
dyn

Error
>>

{

let

cfg_dirs

=

get_cfg_dirs
()
?
;

//
 Notice that we don't have to check again if the `Vec`

//
 was empty, since we guarantee that via the `NonEmptyVec` type

init_cache
(
cfg_dirs
.
first
());
}

In this context, we can callNonZeroF32::newandNonEmptyVec::try_fromparsingfunctions, since they validate and convert the less semantic type to a type with more meaning imbued into it. That is, nonzeroness of a float and nonemptiness of aVecis now encoded into a type. You can just see the wordNonZeroF32and therefore understand that going forward it is always be anf32that is never zero.

Validation and checking functions on the other hand, well, just validate the value and leave the type as that. If I have ais_nonzero(f32) -> boolfunction, then there’s not really much of a readable difference between anf32that hasis_nonzerocalled on it versus and anf32that hasn’t.

fn

is_nonzero
(
n
:

f32
)

->

bool
;
fn

to_nonzero
(
n
:

f32
)

->

Option
<
NonZeroF32
>;

By taking advantage of the existence of a nominative type system, we can communicate that thisf32is not zero byparsingit to a new type, as opposed to justvalidatingit. If you only validate it, then you still can’t tell iff32was nonzero unless you dig through the code. However, if you parsed it, you can say it’s always be nonzero if you seeNonZeroF32in your code.

## Examples in the wild#

Of course, the above examples are very much contrived, but is there an instance where creating newtypes is helpful? Yes. In fact, most people have used it. It’s called aString.

If we dig into the internals,Stringis just a newtype over theVec<u8>type:

#[
derive
(
PartialEq
,

PartialOrd
,

Eq
,

Ord
)]
#[
stable
(
feature
=

"rust1"
,
 since
=

"1.0.0"
)]
#[
lang
=

"String"
]
pub

struct

String

{

vec
:

Vec
<
u8
>,
}

It’s parsing function isString::from_utf8, which contains the validation code for checking if the byte vector is valid UTF-8.


#[
inline
]

#[
stable
(
feature
=

"rust1"
,
 since
=

"1.0.0"
)]

#[
rustc_diagnostic_item
=

"string_from_utf8"
]

pub

fn

from_utf8
(
vec
:

Vec
<
u8
>)

->

Result
<
String
,

FromUtf8Error
>

{

match

str
::
from_utf8
(
&
vec
)

{

Ok
(
..
)

=>

Ok
(
String

{

vec

}),

Err
(
e
)

=>

Err
(
FromUtf8Error

{

bytes
:

vec
,

error
:

e

}),

}

}

So instead of passing around aVec<u8>around and validating all over the place, just parse into aStringand you can be assured with having a type-safeStringwith all the convenience functions you can get.

Another example isserde_json. In Python,json.loadssimply give you a dictionary. This is fine, especially if the data is sufficiently arbitrary, but if you have a schema and a type system, it’s better to let the type system do the work of parsingjson.

In our terminology, validation looks like this:

use

serde_json
::
{
from_str
,

Value
};

const

SAMPLE_JSON:

&
str

=

r#"{ "foo": 1, "bar": [1, 2, 3] }"#
;

let

json

=

from_str
::
<
Value
>(
SAMPLE_JSON
)

.
unwrap
();

let

first_elem

=

json
.
get
(
"bar"
)

.
and_then
(
|
bar
|

bar
.
get
(
0
))

.
unwrap
();

//
 do stuff with `first_elem`

That’s twounwraps! One for checking if the string is valid json and the other is for checking if thebarfield exists. Now consider this example where we use the parsing mechanic instead via types and theDeserializederive macro.

struct

Sample

{

foo
:

i32
,

bar
:

[
i32
;

3
]
}

impl

Sample

{

fn

first_elem
(
&
self
)

->

i32

{

self
.
bar
[
0
]

//
 does not panic, by definition

}
}

let

json

=

from_str
::
<
Sample
>(
SAMPLE_JSON
)
.
unwrap
();
let

first_elem

=

json
.
first_elem
();

//
 do stuff with `first_elem`

Since we deserialized thejsonfile into an actual type, we can safely make these guarantees:

1. Thefooandbaralways exist in thejsonstring we parse.
2. fooalways has an integer value.
3. baris always an array of three integers.
4. first_elemwill never panic since all elements of an array is always initialized, and indexing into the first the element of a nonzero-length array will always be successful.

The only point of failure here is pushed upfront, where thefrom_strhappens. After that point, there’s not really much error handling to be done here, since the validation is now represented at the type level instead of at the function level.

## Maxims of Type Driven Design#

With that said, what lessons can we learn from here? Turns out, most functional language programmers already have learned several lessons, and Rust is not much different in terms of applying such FP concepts to the language.

First lesson we can learn is thatwe should make illegal states unrepresentable.

What do we mean by that?

To refer back to theNonZeroF32andNonEmptyVecexamples, we say the state of being zero is illegal forNonZeroF32and the state of being empty is illegal forNonEmptyVec. And as illegal states, they cannot be represented in such types. That’s why the only constructors available for these types are fallible; the value either parsed successfully, or it failed and does not return the new types.

If we only do validation, like checking iff32is nonzero for example, then the illegal state can still be represented. There’s a small possible that the value is zero, especially after some refactors when the conditional checks are accidentally or intentionally removed in some places.



This reminds me of how other languages use integers as sentinel values. Given this code snippet fromWikipedia:

int

find
(
int

arr
[]
,

size_t

len
,

int

val
)

{

for

(
int
 i
=

0
;
 i
<
 len
;
 i
++
)

{

if

(
arr
[
i
]

==
 val
)

{

return
 i
;

}

}

return

-
1
;

//
 not found
}

The error is returned as-1, since indexing arrays is only valid for nonnegative integers. Seems weird as (1) the numbers -2 and belowcanexist, but not actually valid, and (2) treating certain values as special seems too error-prone, as in the future it could be that negative number can become semantically valid.



Second lesson we can learn is thatproving invariants should be done as early as possible.

There’s this concept calledshotgun parsingwhere the linked paper describes it as follows:

Shotgun Parsing: Shotgun parsing is a programming antipattern whereby parsing and input-validating code is mixed with and spread across processing code—throwing a cloud of checks at the input, and hoping, without any systematic justification, that one or another would catch all the “bad” cases.

Essentially, it describes the problem of usage of data without previous validation of its entirety of data. You could act on a part of the data that is validated beforehand, but discover that another part of the data is invalid.

The paper mentionsCVE-2016-0752, which is a bug that allows attackers to read arbitrary files because you can use..in the input. The paper argues that treating validation as emergent and not deliberate can lead to security bugs like these.

If we treat validation as deliberate, then it should happen as early as possible and as comprehensive as possible. By parsing first, every invariant can be proven first before executing on said data.



I remember thisvideoabout lambda calculus. It concludes that types can be represented as propositions in logic, and terms as proofs. I recommend watching the video, as it is eye-opening to me and maybe it can help you realize some things too.

Fundamentally, if your program typechecks properly, then you can say that the proof is correct. Thank you Curry-Howard Correspondence. There are proof assistant programming languages that can help with this likeLeanandAgda, but you can emulate this in Rust anyway. That’s how some weird libraries like thetypenumcrate work.

use

std
::
ops
::
Add
;
use

typenum
::*
;

//
 1.19.0

type

Lhs

=

<
P3

as

Add
<
P4
>>
::
Output
;
type

Rhs

=

P8
;

type

Result

=

<
Lhs

as

Same
<
Rhs
>>
::
Output
;

pub

fn

is_proof_correct
()
where

Result
:
{}

This is a simpleprogramin Rust where I check if3 + 4is equal to8. Obviously this is not correct, and so it will appropriately give you a compile error.


Compiling

playground

v0
.
0
.
1

(
/
playground
)
error
[
E0277
]
:

the

trait

bound
 `
PInt
<
UInt
<
UInt
<
UInt
<
UTerm
,

B1
>,

B1
>,

B1
>>
:

Same
<
PInt
<
UInt
<
...
,

...
>>>
`
is

not

satisfied

-->

src
/
lib
.
rs
:
11
:
5

|
11

|

Result
:

|

^^^^^^

unsatisfied

trait

bound

|

=

help
:

the

trait
 `
typenum
::
Same
<
PInt
<
UInt
<
UInt
<
UInt
<
UInt
<
UTerm
,

B1
>,

B0
>,

B0
>,

B0
>>>
`
is

not

implemented

for
 `
PInt
<
UInt
<
UInt
<
UInt
<
UTerm
,

B1
>,

B1
>,

B1
>>
`

=

note
:

the

full

name

for

the

type

has

been

written

to

'
/playground/target/debug/deps/playground-e4f34f6f1769e3b6.long-type-6323804316620900.txt
'

=

note
:

consider

using
 `
--
verbose
`
to

print

the

full

type

name

to

the

console

For

more

information

about

this

error
,

try
 `
rustc

--
explain

E0277
`
.
error
:

could

not

compile
 `
playground
`
(
lib
)

due

to

1

previous

error

So sad that the error message is dogshit. Such is life.



## What can we do?#

There are some recommendations I usually say to people on the RPLCS discord server, adapted from the original blog post.

First, just because a function accepts a type doesn’t mean you have to use it in your structs, nor have to perpetually represent it as that type. For example, let’s say we have a third party library function that looks like this.

fn

set_lightbulb_state
(
is_on
:

bool
)

{}

Youdon’thave to storeboolin yourApp/Contextstruct likeApp { lightbulb_state: bool }. That’s confusing. I’d rather have you define a separate enum with more semantics imbued into it, like:

enum

LightBulbState

{

Off
,

On
,
}

impl

From
<
LightBulbState
>

for

bool

{

...

}

struct

App

{

lightbulb_state
:

LightBulbState
}

//
 ...

fn

main
()

{

let

app

=

App

{

...

}

set_lightbulb_state
(
app
.
lightbulb_state
.
into
());
}

Yeah, people can say it gets more verbose, but I rather care more about correctness instead. Sorry.

Second, I sometimes get suspicious about these kind of APIs:

fn

do_something_fallible
(
data
:

&
Thing
)

->

Result
<(),

MyError
>

{}

//
 or worse,

fn

verify
(
data
:

&
Thing
)

->

bool

{}

If I see the function body does not do anything side-effectful, then it’s probable that parsing can help here turningThinginto a more structured datatype. And even for side-effectful stuff, there are some types that better represent certain situations, like infinite loop function representing their return types asResult<!, MyError>orResult<Infallible, MyError>.

## Conclusion#

I love creating more types. Five million types for everyone please.

I think it’s interesting that there’s a lot of instances where types drive the design of Rust programs. Like howVechas four layers of newtypes plus an additional field.sqlxgenerate anonymous structs in theirquery!macros.bonis a macro crate that converts functions into compile-time builders via types.

Of course, not everything is solvable via types. But personally I think pushing your verification code to types can help your code become clearer and more robust. Let the type system handle the validation for you. It exists, so might as well use it to its fullest extent.

I’d like to thank Alexis King for thisarticlewhere I first encountered this idea. I’d love to follow up on this topic with an extension on thissequel, and maybe recontextualizing in Rust via theunsafekeyword would be helpful.

Of course, newtyping is not the answer to all problems. Due to lack of ergonomic features to allow newtyping—likedelegation—many people are somewhat averse to using the pattern. Nevertheless, if someone made a good enough RFC I’d be happy to see it happen.

Using the type system as a compile-time checker because I want the compiler to help me write my programs is very nice. You should take advantage of the type system too, not many languages have it as good as Rust :)




Saturday, February 21st, 2026
 —

#design pattern
#rust
#type system
#type-driven design





### Liked this blog post and want some more? Consider donating to support the author!
