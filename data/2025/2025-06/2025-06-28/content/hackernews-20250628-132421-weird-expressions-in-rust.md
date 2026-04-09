---
title: Weird expressions in rust
url: https://www.wakunguma.com/blog/rust-weird-expr
site_name: hackernews
fetched_at: '2025-06-28T13:24:21.531436'
original_url: https://www.wakunguma.com/blog/rust-weird-expr
author: lukastyrychtr
date: '2025-06-28'
description: Explore weird quirks of rusts type system
---

Rust has a very powerful type system, but as a result it has some quirks, some would say cursed expressions. There’s a test file,weird-expr.rs, in the rust repository that tests for some of these and makes sure there consistent between updates. So I wanted to go over each of these and explain how it’s valid rust.

Note that these are not bugs, but rather extreme cases of rust features like loops, expressions, coercion and so on.

## Strange

fn
 strange
()
 ->
 bool
 {
let
 _x
:
bool
 =
 return
 true
;}

The expressionreturn truehas the type!. The never type can coerce into any other type, so we can assign it to a boolean.

## Funny

fn
 funny
(){

	fn
 f
(_x
:
 ()){}

	f
(
return
);

}

The functionfhas a single parameter of()type, we can again passreturnbecause!will be coerced into().

## What

use
 std
::
cell
::
Cell
;

fn
 what
(){

	fn
 the
(x
:
 &
Cell
<
bool
>){

		return
 while
 !
x
.
get
() {x
.
set
(
true
);};

	}

	let
 i
=
 &
Cell
::
new
(
false
);

	let
 dont
=
 {
||
the
(i)};

	dont
();

	assert!
(i
.
get
());

}

Thethefunction takes a reference to aCell<bool>. Inside the function, we use a while loop

while
 !
x
.
get
() {x
.
set
(
true
);}

to set the cells contains totrueif its contents arefalseand we return that while loop which has the type().

Next we create a variableiwhich is a reference to aCell<bool>and bind a closure that callsthewithias the parameter, we then call that closure and assert thatiis true.

## Zombie jesus

fn
 zombiejesus
()
 {

 loop
 {

 while
 (
return
) {

 if
 (
return
) {

 match
 (
return
) {

 1
 =>
 {

 if
 (
return
) {

 return


 }
else
 {

 return


 }

 }

 _
=>
 {
return
 }

 };

 }
else
 if
 (
return
) {

 return
;

 }

 }

 if
 (
return
) {
break
; }

 }

}

The expression(return)has the type never, since the never type can coerce into any type we can use it in all these places.

Inifandwhilestatements it gets coerced into a boolean, in amatchstatement it gets coerced into anything.

let
 screaming
=
 match
(
return
){

	"
aahhh
"
 =>
 true
,

	_
=>
 false

};

## Not sure

use
 std
::
mem
::
swap;

fn
 notsure
()
 {

 let
 mut
 _x
:
 isize
;

 let
 mut
 _y
=
 (_x
=
 0
)
==
 (_x
=
 0
);

 let
 mut
 _z
=
 (_x
=
 0
)
<
 (_x
=
 0
);

 let
 _a
=
 (_x
+=
 0
)
==
 (_x
=
 0
);

 let
 _b
=
 swap
(
&mut
 _y,
 &mut
 _z)
==
 swap
(
&mut
 _y,
 &mut
 _z);

}

We have an uninitialised variable_x, we assign_yto(_x = 0) == (_x = 0).(_x = 0)evaluates to the unit type so_yis true. Similar thing with_zand_a, except_zis false since()is not less than itself._bis also true becauseswapreturns().

## Cant touch this

fn
 canttouchthis
()
 ->
 usize
 {

 fn
 p
()
 ->
 bool
 {
true
 }

 let
 _a
=
 (
assert!
(
true
)
==
 (
assert!
(
p
())));

 let
 _c
=
 (
assert!
(
p
())
==
 ());

 let
 _b
:
 bool
 =
 (
println!
(
"{}"
,
0
)
==
 (
return
 0
));

}

The functionp()function returns that a boolean, theassert!macro returns(), so_aand_care both true.

In the final line_bis assigned to the expression

(
println!
(
"{}"
),
0
)
==
 (
return
 0
))

Theprintln!returns macro returns(), and(return 0)is!which gets coerced into()so the expression is valid, this line also returns 0 which makes the function signature valid.

## Angry dome

fn
 angrydome
()
 {

 loop
 {
if
 break
 { } }

 let
 mut
 i
=
 0
;

 loop
 {

		i
+=
 1
;

		if
 i
==
 1
 {

			match
 (
continue
) {

				1
 =>
 { },

				_
=>
 panic!
(
"
wat
"
) }

			}

	 break
;

		}

}

In the first line we immediately exit the loop, becausebreakis a valid expression, which has the type!, we can use it in an if statement.

In the next part we assignito 0. We incrementiin the loop, the if statement will run in the first iteration becauseiis now 1. We match(continue)which is!, the loop skips to the next iteration, we incrementiagain so it’s now2. Theifstatement doesn’t run so the loop exits and the function returns.

## Union

fn
 union
()
 {

 union
 union
<'
union
> {
union
:
 &
'
union
 union
<'
union
>, }

}

Rust hasthree categoriesof keywords:

* Strict keywords, which can only be used in their correct contexts
* Reserved keywords, which have been reserved for future use, but have the same limitations as strict keywords
* Weak keywords, which only have special meaning in certain contexts

unionis a weak keyword and isonly a keyword when used in a union declaration, allowing us to it to be used in other contexts, such as function names.

## Punch card

fn
 punch_card
()
 ->
 impl
 std
::
fmt
::
Debug
 {

 ..=..=..
 ..
 ..
 ..
 ..
 ..
 ..
 ..
 ..
 ..
 ..
 ..
 ..
 ..

 ..=..
 ..=..
 ..
 ..
 ..
 ..
 ..
 ..
 ..
 ..
 ..
 ..=..
 ..

 ..=..
 ..=..
 ..=..
 ..=..
 ..
 ..=..=..
 ..=..=..=..

 ..=..=..
 ..
 ..=..
 ..=..
 ..=..
 ..
 ..
 ..
 ..=..
 ..

 ..=..
 ..=..
 ..=..
 ..=..
 ..
 ..=..
 ..
 ..
 ..=..
 ..

 ..=..
 ..=..
 ..=..
 ..=..
 ..
 ..
 ..=..
 ..
 ..=..
 ..

 ..=..
 ..=..
 ..
 ..=..=..
 ..=..=..
 ..
 ..
 ..=..=..

}

In rust..represents an unbounded range (std::ops::RangeFull) usually used in slices. Similarly..=represents a range up to and including a value (std::ops::RangeToInclusive). All the different ranges have types which you can see in thestd::opsmodule docs.

Ranges can be combined into whatever amalgamation you would like:

use
 std
::
ops
::
{
RangeFull
,
RangeTo
,
RangeToInclusive
};

let
 _a
:
 RangeToInclusive
<
RangeTo
<
RangeFull
>>
=
 ..=..
 ..
 ;

All of these range types implementDebug, which satisfies theimpl std::fmt::Debugreturn type.

## Monkey barrel

fn
 monkey_barrel
()
 {

 let
 val
:
 ()
=
 ()
=
()
=
()
=
()
=
()
=
()
=
()
=
()
=
()
=
()
=
()
=
()
=
()
=
()
=
()
=
()
=
()
=
()
=
()
=
()
=
()
=
()
=
()
=
()
=
();

 assert_eq!
(val, ());

}

In rust anassignment expressionconsists of a leftassignee expression, an equals sign (=) and a rightvalue expression. A tuple pattern can be used an assignee expression, which means it can appear on the left part of an assignment expression. Most of the times we use this to assign destructure values.

let
 (x,y)
=
 (
110
.
0
,
50
.
5
);

But the tuple can also be empty, which means we’re assigning it to the()type.

let
 ()
=
 ();

Because assignments return()we can chain them

let
 ()
=
 ()
=
()
=
();

## Semi’s

fn
 semisemisemisemisemi
()
 {

 ;;;;;;; ;;;;;;; ;;; ;;; ;;

 ;; ;; ;;;; ;;;; ;;

 ;;;;;;; ;;;;; ;; ;;;; ;; ;;

 ;; ;; ;; ;; ;; ;;

 ;;;;;;; ;;;;;;; ;; ;; ;;

}

You can add a semi-colon anywhere in a block, which creates an empty statement with an empty value(). So these semi-colons just create a bunch of empty statements.

## Useful syntax

fn
 useful_syntax
()
 {

 use
 {{
std
::
{{
collections
::
{{
HashMap
}}}}}};

 use
 ::
{{{{core}, {std}}}};

 use
 {{
::
{{core
as
 core2}}}};

}

Rust allows groupedusestatements to reduce boilerplate. These braces can also be used at the root of the statement, there’s also no limit to the number of braces you can use.

use
 {
std
::
sync
::
Arc
};

use
 core
::
{
mem
::
{{transmute}}};

## Infinite modules

fn
 infcx
()
 {

 pub
 mod
 cx {

 pub
 mod
 cx {

 pub
 use
 super
::
cx;

 pub
 struct
 Cx
;

 }

 }

 let
 _cx
:
 cx
::
cx
::
Cx
 =
 cx
::
cx
::
cx
::
cx
::
cx
::
Cx
;

}

We declare a modulecx, then we create another sub-module also namedcx. The line

pub
 use
 super
::
cx;

is re-exporting the module from itself, which means we can now call it recursively. It’s simpler to see if we change the names.

pub
 mod
 outer{

 pub
 mod
 inner{

 pub
 use
 super
::
inner;

 pub
 struct
 Item
;

 }

}



let
 _item
:
 outer
::
inner
::
Item
 =
 outer
::
inner
::
inner
::
inner
::
Item
;

## Fish fight

fn
 fish_fight
()
 {

 trait
 Rope
 {

 fn
 _____________
<
U
>(_
:
 Self
,
 _
:
 U
)
 where
 Self
:
 Sized
 {}

 }

 struct
 T
;

 impl
 Rope
 for
 T
 {}

 fn
 tug_o_war
(_
:
 impl
 Fn
(
T
,
 T
))
 {}

 tug_o_war
(<
T
>
::
_____________
::
<
T
>);

}

TheRopetrait has a provided method with one genericU, and it takes in two arguments, one of typeSelfand another of typeU. We make a structTand implementRopefor it. Thetug_of_warfunction accepts any function or closure that implementsFn(T,T).

The expression<T>::_____________::<T>is a fully qualified function pointer, withTas the generic type (fn(T,T)). Because both parameters are of the same type, we can pass this into thetug_of_war.

## Dots

fn
 dots
()
 {

 assert_eq!
(
String
::
from
(
"
..................................................
"
),

 format!
(
"{
:?
}"
,
..
 ..
 ..
 ..
 ..
 ..
 ..
 ..
 ..
 ..
 ..
 ..
 ..

 ..
 ..
 ..
 ..
 ..
 ..
 ..
 ..
 ..
 ..
 ..
 ..
));

}

The range syntax (std::ops::RangeFull) implementsDebugand gets formatted as"..". So we can chain them to get a string of dots.

## u8

fn
 u8
(
u8
:
 u8
)
 {

 if
 u8
 !=
 0
u8
 {

 assert_eq!
(
8
u8
, {

 macro_rules!
 u8
 {

 (
u8
)
=>
 {

 mod
 u8 {

 pub
 fn
 u8
<'
u8
:
 '
u8
 +
 '
u8
>(
u8
:
 &
'
u8
 u8
)
 ->
 &
'
u8
 u8
 {

 "
u8
"
;

 u8


 }

 }

 };

 }

 u8
!
(
u8
);

 let
 &
u8
:
 &
u8
 =
 u8
::
u8
(
&
8
u8
);

 crate
::
u8
(
0
u8
);

 u8


 });

 }

}

Let’s take this apart, we have a macrou8!, which declares a moduleu8which declares a functionu8which takes a parameter namedu8of typeu8and returns a reference to au8.

macro_rules!
 u8
 {

 (
u8
)
=>
 {

 mod
 u8 {

 pub
 fn
 u8
<'
u8
:
 '
u8
 +
 '
u8
>(
u8
:
 &
'
u8
 u8
)
 ->
 &
'
u8
 u8
 {

 "
u8
"
;

 u8


	 }

 }

 };

}

Next we callu8::u8(&8u8)and assign it to a variable (u8). The next line callscrate::u8(0u8), and finally we return theu8variable from the entire expression.

## Continue

fn
 𝚌𝚘𝚗𝚝𝚒𝚗𝚞𝚎() {

 type
 𝚕𝚘𝚘𝚙
=
 i32
;

 fn
 𝚋𝚛𝚎𝚊𝚔()
->
 𝚕𝚘𝚘𝚙 {

 let
 𝚛𝚎𝚝𝚞𝚛𝚗
=
 42
;

 return
 𝚛𝚎𝚝𝚞𝚛𝚗;

 }

 assert_eq!
(
loop
 {

 break
 𝚋𝚛𝚎𝚊𝚔 ();

 },
42
);

}

These use unicode monospace characters, instead of normal ASCII characters, for identifiers, which don’t break rust’s rules of using keywords as identifiers.

## Fishy

fn
 fishy
()
 {

 assert_eq!
(

	 String
::
from
(
"
><>
"
),

 String
::
<>
::
from
::
<>(
"
><>
"
)
.
chars
::
<>()
.
rev
::
<>()
.
collect
::
<
String
>()

 );

}

Rust uses the turbo fish syntax when adding generics and lifetimes. We can use empty angle brackets to explicitly specify empty generics.

## Special characters

fn
 special_characters
()
 {

 let
 val
=
 !
((
|
(
..
)
:
(_,_),(
|
__
@
_
|
__)
|
__)((
&*
"
\\
"
,
'
🤔
'
)
/**/
,{})
==
{
&
[
..=..
][
..
];})
//

 ;

 assert!
(
!
val);

}

Let’s decode the right expression:

let
 val
=
 &
[
..=..
][
..
];

We create a reference to a slice containing a range&[..=..], then we take a full slice of that.

Now for the left expression:

let
 val
=
 (
|
(
..
)
:
(_,_),(
|
__
@
_
|
__)
|
__)((
&*
"
\\
"
,
'
🤔
'
)
/**/
,{});

We have a closure with two arguments, the first argument is a tuple, with auto-inferred types.

let
 val
=
 |
(
..
)
:
(_,_)
|
{};

The second argument is a closure which has anat binding, the variable__is bound to a wildcard pattern (_), which will match anything.

let
 val
=
 |
(
..
)
:
(_,_),(
|
__
@
_
|
__)
|
{};

Then we immediately call that closure, passing in a tuple with a string and a char, and an empty block.

let
 val
=
 (
|
(
..
)
:
(_,_),(
|
__
@
_
|
__)
|
)((
&*
"
\\
"
,
'
🤔
'
),{})

## Match

fn
 r#match
()
 {

 let
 val
:
 ()
=
 match
 match
 match
 match
 match
 () {

 ()
=>
 ()

 } {

 ()
=>
 ()

 } {

 ()
=>
 ()

 } {

 ()
=>
 ()

 } {

 ()
=>
 ()

 };

 assert_eq!
(val, ());

}

This is just matching nestedmatchstatements.

## Match nested if

fn
 match_nested_if
()
 {

 let
 val
=
 match
 () {

 ()
if
 if
 if
 if
 true
 {
true
}
else
 {
false
} {
true
}
else
 {
false
} {
true
}
else
 {
false
}
=>
 true
,

 _
=>
 false
,

 };

 assert!
(val);

}

This is amatch guardwith nestedifstatements.

## Function

fn
 function
()
 {

 struct
 foo;

 impl
 Deref
 for
 foo {

 type
 Target
 =
 fn
()
->
 Self
;

 fn
 deref
(
&
self
)
 ->
 &
Self
::
Target
 {

 &
((
||
 foo)
as
 _)

 }

 }

 let
 foo
=
 foo () ()() ()()() ()()()() ()()()()();

}

TheDereftrait is used when a type can be implicitly coerced into another type, it’s usually used by smart pointers so they can be implicitly used at the underlying type.

We implementDereffor foo into a function pointer that returnsfoo, which means we can call that foo again recursively.

## Bathroom stall

fn
 bathroom_stall
()
 {

 let
 mut
 i
=
 1
;

 matches!
(
2
, _
|
_
|
_
|
_
|
_
|
_
if
 (i
+=
1
)
!=
 (i
+=
1
));

 assert_eq!
(i,
13
);

}

In a match arm multiple patterns can be matched in one arm, separated by|.

let
 foo
=
 '
a
'
;

match
 foo {

	'
a
'
..
'
c
'
|
'
x
'
..
'
z
'
 =>
 {}

 _
=>
 {}

}

Thematches!macro has the same syntax as a match statement so we can also chain multiple patterns, even if those are wildcard patterns.

matches!
((),_
|
_
|
_
|
_
|
_
|
_)

matches!
(
2
, _
|
_
|
_
|
_
|
_
|
_
if
 (i
+=
1
)
!=
 (i
+=
1
));

We have six different patterns here, which all do the same thing: we check ifi +=1 != i += 1, which increments it twice, so each iteration is incrementingiby 2.6 x 2 = 12plus 1 (the initial value) and the final value is 13 so the assertassert_eq!(i,13)is true. Thematch!(2,..)doesn’t panic because it’s a wildcard pattern so any value could have been used. The if statement is always going to be false because the right expression will always be one more than the left so it will run until all the patterns have been tried.

## Closure matching

fn
 closure_matching
()
 {

 let
 x
=
 |
_
|
 Some
(
1
);

 let
 (
|
x
|
 x)
=
 match
 x
(
..
) {

 |
_
|
 Some
(
2
)
=>
 |
_
|
 Some
(
3
),

 |
_
|
 _
=>
 unreachable!
(),

 };

 assert!
(
matches!
(
x
(
..
),
|
_
|
 Some
(
4
)));

}

xis a closure that takes in a parameter with an unspecified type, which will be inferred through its usage. Next wematch x(..)which makes the type of the closureRangeFull. It looks like we’re matching closures but it’s really just multiple wildcard patterns.

The numbers also don’t matter even though it seems as though the function is being incremented each time, since it’s a wildcard anything would match.

## Return already

fn
 return_already
()
 ->
 impl
 std
::
fmt
::
Debug
 {

 loop
 {

 return
 !!!!!!!

 break
 !!!!!!
1111

 }

}

Thebreakexpression is repeatedly applying anotoperation on an integer, while thereturn expressionis also repeatedly applying anotoperation on thebreakexpression.

## Fake macros

fn
 fake_macros
()
 ->
 impl
 std
::
fmt
::
Debug
 {

 loop
 {

 if
!
 {

 match
!
 (

 break
!
 {

 return
!
 {

 1337

 }

 }

 ) {

 }

 } {

 }

 }

}

Let’s isolate the return statement:

fn
 fake_macros
()
 ->
 impl
 std
::
fmt
::
Debug
{

	return
!
 {
1337
 }

}

This is doing anotoperation on the inner expression. Next we wrap that expression in a loop.

fn
 fake_macros
()
 ->
 impl
 std
::
fmt
::
Debug
{

	loop
 {

		break
!
 {

			return
!
 {

				1337

			}

		}

	}

}

Thebreak!{ }is also doing anotoperation on thereturn! { 1337 }, which has the type!. Now the functions return type is inferred from both the loop and the return statement. Divergent function?

Next we wrap everything inside the loop in a match statement

fn
 fake_macros
()
 ->
 impl
 std
::
fmt
::
Debug
{

	loop
 {

		match
!
(

			break
!
 {

				return
!
 {

					1337

				}

			}

		){



		}

	}

}

We don’t have to add any patterns to the match statement since we’re matchingnever. And finally we wrap this in anifstatement.

fn
 fake_macros
()
 ->
 impl
 std
::
fmt
::
Debug
{

	loop
 {

		if
!
 {

			match
!
 (

				break
!
 {

					return
!
 {

						1337

					}

				}

			)

		} {

		}

	}

}

So to sum it up:

* return! { 1337 }makes the return type of the function ani32, which implementsDebug
* break! { ... }makes the return type of the loop!, because of the innerreturn, which also implementsDebug
* We match the break statement and leave out the patterns since it is!
* Wrap the match statement in an if statement
