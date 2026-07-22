---
title: 'Tutorial: Introduction to Formal Verification with Lean (Part 1) - HashCloak'
url: https://hashcloak.com/blog/tutorial-introduction-to-formal-verification-with-lean-(part-1)
site_name: hnrss
content_file: hnrss-tutorial-introduction-to-formal-verification-with
fetched_at: '2026-07-22T19:32:31.176440'
original_url: https://hashcloak.com/blog/tutorial-introduction-to-formal-verification-with-lean-(part-1)
date: '2026-07-19'
description: A tutorial Formal Verification using Lean for cryptographic engineers. Implement and prove correctness of the One-Time pad following a cryptography book.
tags:
- hackernews
- hnrss
---

Back to insights

Back to insights

# Tutorial: Introduction to Formal Verification with Lean (Part 1)

Elena

Cryptography Engineer

Jul 15, 2026

Formal verification is a tool to verify correctness of (mathematical) statements. Where we use pen and paper to write a math proof, we could actually use a formal verification tool to write down the proof in code and get it machine-checked, to know for sure the proof is correct. Examples of these tools areRocq(formally Coq),Isabelleand, the topic for this tutorial,Lean.

In this tutorial we'll write some simple statements about cryptography and their proofs in Lean. So this aims to be fun for cryptographic engineers who are new to formal verification or want to refresh their knowledge of the basics of formal verification.

Specifically, we'll do a walkthrough the very basics of Lean and then formally verify the One-Time Pad (OTP) protocol, first popularized byClaude Shannonbut described earlier byFrank MillerandGilbert Vernam.

The goal for this tutorial is to take formal definitions and proofs about simpler cryptography protocols, such the One-Time Pad, and port them to Lean. We use Dan Boneh and Victor Shoup's"A Graduate Course in Applied Cryptography"as the main source for definitions and proofs.

By the end of this tutorial, you should be able to go through other formalized cryptography Lean proofs such as those fromVCV-io

Disclaimer: this is by no means intended to give best practices in Lean, but rather an introduction that might make sense to and be fun for cryptography people.

## The Lean programming language & proof assistant

Leanwas created in 2013 byLeonardo de Moura, then at Microsoft Research. It is a functional programming language and theorem prover.

It can be used by mathematicians to write down their axioms, lemma’s and theorems and add proofs where needed. If the proof gets compiled by Lean, that means it’s correct (assuming trust in the Lean compiler). The benefit, apart from checkeable proofs, is that it is easier to break up proofs into sub-proofs and collaborate. Furthermore, Lean can help you complete proofs by automatically searching and applying missing pieces.

However, Lean is also “just” a programming language. Specifically, it is a pure functional programming language, meaning its programs don’t have side effects and functions are treated as first class values. We’ll see more about the latter in the tutorial.

There are many great resources in order to get started with Lean. Here are a few:

* Book & exercises for beginners:The Hitchhiker’s Guide to Logical Verification
* Introductory books on the Lean website:Functional Programming in Lean. Great if you already know functional programming.Theorem Proving in Lean 4. A more mathematical aim.
* Functional Programming in Lean. Great if you already know functional programming.
* Theorem Proving in Lean 4. A more mathematical aim.
* Natural Numbers Game. Interactive game to learn proving in Lean directly in the browser.

(The reason I created this specific exercise even though so many great resources already exist, is the specific overlap with cryptography; VCV-io has amazing proofs for cryptography but is too advanced for beginners and doesn’t have tutorials.)

# Tutorial

Let’s get started. The tutorial has 4 parts after we do a quick “Hello World!” (part 2 is the longest). Everything is in Lean 4 and the idea is for you to code along.

All code shown with line numbers is code that is needed for the final result. Code that has no line numbers is not yet completed or is just to check something and can be safely removed.

Finally, at the beginning of the subsections there is a small comment containing the new concepts shared in that section.

## Hello world in Lean

* the Lean InfoView
* eval

You can download Lean locally, or use an online editor such ashttps://live.lean-lang.org/which will look something like this (below). On the left side you’ll write Lean and on the right side is the Lean Infoview with useful information and tips.

To make sure everything works fine, write something like

⧉
#
eval
 
1
+
1

And verify that the outcome is shown in the InfoView on the right-hand side.

For the traditional “Hello World!”, we can do either of the following:

⧉
#
eval
 
"Hello World!"
#
eval
 
String
.
append
 
"Hello "
 
"World!"
#
eval
 
String
.
append
 
"Hello "
 
(
if
 
1
 
>
 
2
 
then
 
"Lean!"
 
else
 
"World!"
)

Some properties of Lean:

* Follows standard mathematical conventions: e.g.#eval 4 + 5 * 6evaluates to 4+(5*6)=34
* No parenthesis to hold function arguments, i.e in Lean you writef xinstead off(x)
* Functions are first-class values in Lean, they get treated just like any value such as a number or a string

But let’s not get ahead of ourselves; we’ll learn each necessary Lean topic as we go.

## What does the book say? I.e. what do we want to port to Lean?

We know more or less what we want to define, but the crux is that for using Lean we need clarity and precision. What exactly do we want to define and how exactly are we going to define it? This is why we use theBoneh & Shoup book, so the math we need is already written out and we only need to worry about translating it to Lean.

First, there is the definition of a Shannon cipher (2.1.1), which has 3 properties. The first two tell us what the encryption and decryption functions are and the last one is the correctness property, which says that decryption after encryption should return the original message.

The specific example we are interested in is the one-time pad, where encryption and decryption are simply XOR-ing:

A significant part of the tutorial will be dedicated to proving the properties of bit-wise exclusive-OR (XOR):

And finally, we can show one-time pad is a Shannon Cipher by proving it adheres to the correctness property:

For this first tutorial we’ll do the following simple steps:

1. Define bitstrings and the XOR function
2. Prove necessary properties for XOR* commutativity
* associativity
* the identity element
* self-inverse
3. Define a Shannon Cipher, which has* an encryption function
* a decryption function
* the property that decryption “reverses” encryption (correctness)
4. Show that a OTP, where encryption and decryption is XOR, is a Shannon Cipher

Ready for some fun? Let’s begin.

## Tutorial Part 1: Define a BitString and XOR

The one-time pad will be defined over keys K, messages M and ciphertexts C which are all bit strings of the same length L; K:= M := C := {0,1}ᴸ.

In the definition of XOR we need addition modulo 2. So it will be helpful for us to see {0,1}ᴸ as ℤ₂ᴸ and use arithmetics over ℤ₂ in Lean.

### Finite Fields

* import libraries
* Zmod n

First, import the finite field libraryZModfrom the mathematics library in Lean:

⧉
1
import
 
Mathlib
.
Data
.
ZMod
.
Basic

In this predefined libraryZMod ndefines the integers modulon, which comes with modular arithmetic pre-implemented. (You can read more about already implemented types by holding Cmd/Ctrl + clicking on them, e.g. checkoutZMod n.)

Tryout some simple modular arithmetic to get familiar withZMod, for example 5 + 6 mod 7:

⧉
#
eval
 
(
5
:
 
ZMod
 
7
)
 
+
 
(
6
:
 
ZMod
 
7
)

Now we can define the domain of K, M, L by creating a new type that is a vector of elements fromZMod 2.

### BitString definition

* Vector
* dependent type
* check

A nice thing about Lean is that we don’t have to fix bit string lengthL; we can just sayLin ℕ, like we would in math. (Type “\N” to write ℕ in Lean.)

The predefined typeVector α ncreates a vector of lengthnwith elements of typeα. So we can useVector (ZMod 2) Lfor defining our custom type ℤ₂ᴸ:

⧉
1
def
 
BitString
 
(
L
:
 
ℕ
)
:
 
Type
 
:=
 
Vector
 
(
ZMod
 
2
)
 
L

This is a dependent type, which gives a different instantiation for different valuesLin ℕ. We can check it: (prefix a comment in Lean with--)

⧉
#
check
 
BitString
 
5
 
--BitString 5 : Type

Note that#evalwon’t work because there is nothing to evaluate, but#checkdisplays the type of the expression, which in this case works fine.

### XOR definition

* implicit parameters
* currying
* lambda function

Now we define the functionxoron input bit strings x = [x_1, …, x_L] and y = [y_1, …, y_L] to be [x_1 +₂ y_1, …, x_L +₂ y_L] if +₂ is addition modulo 2.

How can we define this in Lean? Think about the function signature in math: ℤ₂ᴸ × ℤ₂ᴸ → ℤ₂ᴸ. There are several options of how to do this (there are always many ways to achieve the same thing in Lean), we’ll go with:

⧉
def
 
xor
 
{
L
:
 
ℕ
}
 
(
x
 
y
:
 
BitString
 
L
)
:
 
(
BitString
 
L
)

Here, parameterLisimplicit. Now we need the “function body”.

To easily iterate over the two input vectors and add them component-wise, we can use the predefined functionzipWithavailable on vectors. Let’s understand the type ofzipWith:

⧉
def
 
zipWith
 
(
f
 
:
 
α
 
→
 
β
 
→
 
φ
)
 
(
as
 
:
 
Vector
 
α
 
n
)
 
(
bs
 
:
 
Vector
 
β
 
n
)
 
:
 
Vector
 
φ
 
n

It takes as arguments a functionfand two vectorsasandbs, and returns a vector of the same length asasandbs. Note that the types of the vector elements can be distinct (although it’s not the case forxor).

The function typef : α → β → φmeans: it takes an element of typeαand an element of typeβand it returns an element of typeφ. In math we would write α × β → φ. The approach Lean uses is calledcurrying; a function with multiple arguments is represented as a sequence of functions, each taking a single argument. This means you can do partial application and makes the code very flexible. So we can readf : α → β → φasf : α → (β → φ), which shows that when you give it the first element of typeα, you end up with a functionβ → φto which you then give an element of typeβand end up with an output of typeφ.

So whatzipWithdoes is walk over two vectors in parallel and performs operationfon the two current elements. In the case ofxorwe want it to walk overxandyand add them modulo 2.

⧉
def
 
xor
 
{
L
:
 
ℕ
}
 
(
x
 
y
:
 
BitString
 
L
)
:
 
(
BitString
 
L
)
 
:=
 
 
-- TODO define f
 
 
Vector
.
zipWith
 
f
 
x
 
y

The final piece of the puzzle is how to define the functionfwe want to pass tozipWith, knowing it needs to perform addition on the elements. We can use alambda function, which can be written in a compact way like this:fun x => x + 1(e.g. return the successor of a natural number).

Putting it together:

⧉
1
def
 
xor
 
{
L
:
 
ℕ
}
 
(
x
 
y
:
 
BitString
 
L
)
:
 
(
BitString
 
L
)
 
:=
2
 
 
Vector
.
zipWith
 
(
fun
 
a
 
b
 
=
>
 
a
 
+
 
b
)
 
x
 
y

Note that this will work correctly, because the type ofBitStringhas elements in ℤ₂ and thus addition will automatically be addition mod 2.

## Tutorial Part 2: Prove properties of XOR

Okay now the real fun begins!

Just for clarity, the content you should at least have now is:

⧉
1
import
 
Mathlib
.
Data
.
ZMod
.
Basic
2
 
3
def
 
BitString
 
(
L
:
 
ℕ
)
:
 
Type
 
:=
 
Vector
 
(
ZMod
 
2
)
 
L
4
 
5
def
 
xor
 
{
L
:
 
ℕ
}
 
(
x
 
y
:
 
BitString
 
L
)
:
 
(
BitString
 
L
)
 
:=
6
 
 
Vector
.
zipWith
 
(
fun
 
a
 
b
 
=
>
 
a
 
+
 
b
)
 
x
 
y

Or whatever equivalent version works for you! We’ll add one more line;beforethexordefinition:

⧉
1
namespace
 
BitString

This will make sure Lean does not get confused with a different already existingxordefinition when we start proving things 😅

Continuing to follow the Boneh & Shoup book, we’ll now prove the properties as mentioned in the definition of xor (Example 2.1), starting with commutativity:

### Prove commutativity of XOR;x ⊕ y = y ⊕ x

We start by proving commutativity for XOR, meaningx ⊕ y = y ⊕ x. This first property will take the most time to prove since it contains the first Lean proof of the tutorial. It’s split up into 3 steps.

#### Define lemma for commutativity

* goals in Lean
* lemma definition
* sorry

We’ll define the commutativity property as a lemma and then prove it. As soon as you’ve written down the lemma, Lean will call it the “goal” of what is yet to be proven. Your task is to reduce the current goal into one or more smaller subgoals, which are closer to something you already know is true. Proving your statement then becomes a chain of reduction, similar to breaking up a programming problem into smaller subproblems.

The elements a lemma (or theorem) exist of in Lean:

⧉
lemma
 
<
name_lemma
>
 
<
arguments_lemma
>
 
:
 
<
statement_lemma
>
 
:=
 
<
proof
>

In this case, the<arguments_lemma>consist of two BitStrings;xandy.

The<statement_lemma>should express the commutativity property we want to prove forxandy:xor x y = xor y x.

The name of the lemma depends on preference; I picked the elegantly shortxor_comm_property. Note that for the BitStrings we need the implicit parameterL:

⧉
1
lemma
 
xor_comm_property
 
{
L
:
 
ℕ
}
 
(
x
 
y
 
:
 
BitString
 
L
)
 
:
 
xor
 
x
 
y
 
=
 
xor
 
y
 
x
 
:=
2
 
 
 
 
sorry
 
-- This is the placeholder until you add the proof

Thesorryplaceholder is not a crazy invention of mine, this is really the Lean placeholder, which you could read as “sorry I haven’t proven it yet”.

#### Prove lemma commutativity: step 1

* tactics,by
* ⊢
* Vector.ext

We’ll build our proofs usingtactics: instructions that help reduce the current goal. You’ll have many different options of steps you can apply, for example:

* rewrite goal into an equivalent form
* split goal into several subgoals
* close a goal when it matches something you already know to be true

We start by removingsorryand replacing it withby, which indicates we’re going to prove this using tactics. This is useful, because Lean will help us by showing what our goal is and what progress we’re making. It looks something like this:

In the InfoView, Lean says: the goal is to show that forL ∈ ℕandx,yof typeBitString L:x.xor y = y.xor x. (The goal is always preceded by⊢.)

Onto the proof. What do we know? For every indexi, if we calculate the corresponding element on both sides, they will be equal:(x.xor y)[i] = (y.xor x)[i]since(x[i] + y[i]) = (y[i] + x[i])due to commutativity for addition in ℤ₂.

So if we can split up our goal intoLsubgoals, ranging overi, then the remaining goal becomes proving a single equality of the single element on both sides.

To achieve this splitting intoLsubgoals, we can use an extensionality lemma, which says: “2 things are the same if they are made up of the same things”. This is a general type of lemma which applies for many types and for a vector it is accessible viaVector.ext(reference). We can use it as follows:

⧉
1
lemma
 
xor_comm_property
 
{
L
:
 
ℕ
}
 
(
x
 
y
 
:
 
BitString
 
L
)
 
:
 
xor
 
x
 
y
 
=
 
xor
 
y
 
x
 
:=
2
 
 
 
 
by
3
 
 
 
 
 
 
apply
 
Vector
.
ext

Now in the editor you can see the goal has changed to:

⧉
L
 
:
 
ℕ
x
 
y
 
:
 
BitString
 
L
⊢
 
∀
 
(
i
 
:
 
ℕ
)
 
(
x_1
 
:
 
i
 
<
 
L
)
,
 
(
x
.
xor
 
y
)
[
i
]
 
=
 
(
y
.
xor
 
x
)
[
i
]

So still we haveL ∈ ℕandx,yof typeBitString L, but the goal has changed to: for alli ∈ ℕwithi < L:(x.xor y)[i] = (y.xor x)[i]. See the next step for what this really means and how we can continue the proof.

#### Prove lemma commutativity: step 2

* intro
* simp

In the pen-and-paper proof we could continue the proof by fixing an arbitrary i and prove equality for it. We might start by saying “let i ∈ with i < L”, to then proceed proving the equality for that fixed i. In Lean this can be expressed as follows:

1. First, fix the free variablei ∈ ℕwithintro i
2. Then, make the assumptioni < Lwithintro h_i_lt_L(“hypothesis i less than L”)

introstrips the front of the goal and puts it into the local “context” of the proof. It either fixes a variable (as in 1) or assumes an additional hypothesis (as in 2).

You can write them consequently in a single line:

⧉
1
lemma
 
xor_comm_property
 
{
L
:
 
ℕ
}
 
(
x
 
y
 
:
 
BitString
 
L
)
 
:
 
xor
 
x
 
y
 
=
 
xor
 
y
 
x
 
:=
2
 
 
 
 
by
3
 
 
 
 
 
 
apply
 
Vector
.
ext
4
 
 
 
 
 
 
intro
 
i
 
h_i_lt_L

Now the goal is:

⧉
L
 
:
 
ℕ
x
 
y
 
:
 
BitString
 
L
i
 
:
 
ℕ
h_i_lt_L
 
:
 
i
 
<
 
L
⊢
 
(
x
.
xor
 
y
)
[
i
]
 
=
 
(
y
.
xor
 
x
)
[
i
]

The part before the goal⊢is everything that is in context; the variables we have fixed and the assumptions we have made. The goal is what we now have left to prove.

To finish the proof we’ll use the tacticsimp(“simplifier”) to replace equal expressions. First, we can expand the definition ofxorinx.xor yandy.xor x:

⧉
1
lemma
 
xor_comm_property
 
{
L
:
 
ℕ
}
 
(
x
 
y
 
:
 
BitString
 
L
)
 
:
 
xor
 
x
 
y
 
=
 
xor
 
y
 
x
 
:=
2
 
 
 
 
by
3
 
 
 
 
 
 
apply
 
Vector
.
ext
4
 
 
 
 
 
 
intro
 
i
 
h_i_lt_L
5
 
 
 
 
 
 
simp
[
xor
]

Now the goal is:

⧉
L
 
:
 
ℕ
x
 
y
 
:
 
BitString
 
L
i
 
:
 
ℕ
h_i_lt_L
 
:
 
i
 
<
 
L
⊢
 
x
[
i
]
 
+
 
y
[
i
]
 
=
 
y
[
i
]
 
+
 
x
[
i
]

And at this point we know this is true due to commutativity of addition in ℤ₂. This is an already proven property fromZModwhich is calledadd_comm.

Addsimp[add_comm]and voilà, we are done with our first proof!

⧉
1
lemma
 
xor_comm_property
 
{
L
:
 
ℕ
}
 
(
x
 
y
 
:
 
BitString
 
L
)
 
:
 
xor
 
x
 
y
 
=
 
xor
 
y
 
x
 
:=
2
 
 
 
 
by
3
 
 
 
 
 
 
apply
 
Vector
.
ext
4
 
 
 
 
 
 
intro
 
i
 
h_i_lt_L
5
 
 
 
 
 
 
simp
[
xor
]
6
 
 
 
 
 
 
simp
[
add_comm
]

Confirm on the right in the InfoView that there are no goals left 🫡

Just a few disclaimers before we move on. Is this the fastest, shortest, most elegant way of proving this property? No, no and probably no.

The goal here is to precisely understand every step we are doing. In practice, Lean solves many things automagically for us. However, for educational purposes, I think it is helpful to see and understand every substep, which is why I’m approaching it lengthy and mechanically. In addition, my goal is to understand how a pen-and-paper proof would translate to Lean, before I continue on to the auto-stuff. But feel free to make the proofs as short or as different as you like!

### Prove associativity of XOR;x ⊕ (y ⊕ z) = (x ⊕ y) ⊕ z

* auto-applying insimp
* merging expressions insimp

Now that we know the general idea, the following proving steps will be much faster. In this step we showxoris associative, i.e.x ⊕ (y ⊕ z) = (x ⊕ y) ⊕ z. First, the lemma definition:

⧉
1
lemma
 
xor_assoc_property
 
{
L
:
 
ℕ
}
 
(
x
 
y
 
z
:
 
BitString
 
L
)
 
:
 
xor
 
x
 
(
xor
 
y
 
z
)
 
=
 
xor
 
(
xor
 
x
 
y
)
 
z
 
:=
 
2
 
 
sorry

Once again, we’ll prove this equality at the level of a random single entry for the left and right side, usingVector.ext:

⧉
1
lemma
 
xor_assoc_property
 
{
L
:
 
ℕ
}
 
(
x
 
y
 
z
:
 
BitString
 
L
)
 
:
 
xor
 
x
 
(
xor
 
y
 
z
)
 
=
 
xor
 
(
xor
 
x
 
y
)
 
z
 
:=
 
2
 
 
by
3
 
 
 
 
apply
 
Vector
.
ext

The InfoView shows:

⧉
L
 
:
 
ℕ
x
 
y
 
z
 
:
 
BitString
 
L
⊢
 
∀
 
(
i
 
:
 
ℕ
)
 
(
x_1
 
:
 
i
 
<
 
L
)
,
 
(
x
.
xor
 
(
y
.
xor
 
z
)
)
[
i
]
 
=
 
(
(
x
.
xor
 
y
)
.
xor
 
z
)
[
i
]

In the previous step we fixed variable i and introduced the hypothesis that i < L. However, here Lean can apply some magic and figure those parts out insimp. It doesn’t only apply the rewrite you are passing it; it will browse through all available proven properties and tactics that might be applicable and automatically figure out what works.

So we can move on immediately to proving this equality:

⧉
(
x
.
xor
 
(
y
.
xor
 
z
)
)
[
i
]
 
=
 
(
(
x
.
xor
 
y
)
.
xor
 
z
)
[
i
]

Once again, expanding the definition ofxorwill bring us a step closer, writesimp[xor]and confirm that the expansion intoLsubgoals is also automatically applied:

⧉
1
lemma
 
xor_assoc_property
 
{
L
:
 
ℕ
}
 
(
x
 
y
 
z
:
 
BitString
 
L
)
 
:
 
xor
 
x
 
(
xor
 
y
 
z
)
 
=
 
xor
 
(
xor
 
x
 
y
)
 
z
 
:=
 
2
 
 
by
3
 
 
 
 
apply
 
Vector
.
ext
4
 
 
 
 
simp
[
xor
]

The goal perihas turned into:

⧉
x
[
i
]
 
+
 
(
y
[
i
]
 
+
 
z
[
i
]
)
 
=
 
x
[
i
]
 
+
 
y
[
i
]
 
+
 
z
[
i
]

At this point we can close the goal using the associativity for addition in ℤ₂ withadd_assoc. Instead of writing a new linesimp[add_assoc], we can merge it in the previoussimp:

⧉
1
lemma
 
xor_assoc_property
 
{
L
:
 
ℕ
}
 
(
x
 
y
 
z
:
 
BitString
 
L
)
 
:
 
xor
 
x
 
(
xor
 
y
 
z
)
 
=
 
xor
 
(
xor
 
x
 
y
)
 
z
 
:=
2
 
 
by
3
 
 
 
 
apply
 
Vector
.
ext
4
 
 
 
 
simp
[
xor
,
 
add_assoc
]

This closes the goal and therefore the associativity property forxoris proven.

Note that there is still a certain amount of Lean magic automatically being applied. Strictly speaking,x[i] + (y[i] + z[i]) = x[i] + y[i] + z[i]does not have the forma + b + c = a + (b + c)that is expected foradd_assoc(notice the difference in parenthesis). Of course, we know that in this case it does mean the same, and I think we can accept Lean’s magic, but further down we’ll see that it means someone has defined this somewhere in a library we are depending on and that for our own definitions/proofs more strictness might be required.

### Define identity elementIDfor XOR and prove correctness

* Vector.replicate
* Vector.extusage with lambda function

The next thing we need is an identity element forxor. For such an elementIDit should hold that for allx:x ⊕ ID = x.

Sincexorequals addition in ℤ₂, the identity element should be a bit string with all0, as addition with 0 mod 2 is identity as well.

How to make aBitStringof zeroes of a length, for example L=5? We create a vector of length 5 filled with zeroes and cast it to aBitString(which is a vector with elements in ℤ₂):

⧉
#
eval
 
(
Vector
.
replicate
 
5
 
0
:
 
BitString
 
5
)

In the InfoView you can see this gives aBitStringof length 5 filled with zeroes. Now we can generalize this idea forID:

⧉
1
def
 
BitString_ID
 
{
L
:
 
ℕ
}
 
:
 
BitString
 
L
 
:=
 
Vector
.
replicate
 
L
 
0

And we want to show the following property holds: for allx:x ⊕ ID = x.

⧉
1
lemma
 
xor_show_identity
 
{
L
:
 
ℕ
}
 
(
x
:
 
BitString
 
L
)
:
 
xor
 
x
 
BitString_ID
 
=
 
x
 
:=
2
 
 
 
 
sorry

From the previous steps, we already know that this strategy will work:

⧉
 
 
-- by
 
 
-- apply Vector.ext
 
 
-- intro i
 
 
-- simp[xor, BitString_ID]

So let’s tryout something slightly different. Once again we useVector.ext, but calling it differently. This time we first look at the signature ofVector.extitself (refhere, but I replacednbyLfor clarity):

⧉
protected
 
theorem
 
ext
 
{
xs
 
ys
 
:
 
Vector
 
α
 
L
}
 
(
h
 
:
 
(
i
 
:
 
Nat
)
 
→
 
(
_
 
:
 
i
 
<
 
L
)
 
→
 
xs
[
i
]
 
=
 
ys
[
i
]
)
 
:
 
xs
 
=
 
ys
 
:=
 
sorry
* {xs ys : Vector α L}means thatxsandysare implicit types; Lean will deduce them.
* (h : (i : Nat) → (_ : i < L) → xs[i] = ys[i])is the argument we need to pass.
* xs = ysis what holds.

Let’s think about how we can passh : (i : Nat) → (_ : i < L) → xs[i] = ys[i]. It takes two arguments;iand the proof thati < Lfor lengthL. The output should be the proof thatxs[i] = ys[i]. We know that this proof can be given usingsimp[xor, BitString_ID].

To write the argument we can use a lambda function as we saw before. Putting it together, we can prove this property for identity as follows:

⧉
1
lemma
 
xor_show_identity
 
{
L
:
 
ℕ
}
 
(
x
:
 
BitString
 
L
)
:
 
xor
 
x
 
BitString_ID
 
=
 
x
 
:=
2
 
 
Vector
.
ext
 
fun
 
i
 
i_less_than_L
 
=
>
 
by
 
simp
 
[
xor
,
 
BitString_ID
]

Actually, because of Lean’s magic we could also just useVector.ext fun _ => by simp [xor, BitString_ID]and it will be figured out correctly as well.

### Prove self-inverse of XOR;x ⊕ xgivesID

* exact?,exact
* mpr
* rfl

The final property we prove forxoris that each element is its own inverse: for allx:x ⊕ x = ID.

To get started, create the lemma signature and apply the techniques we saw above:

⧉
1
lemma
 
xor_self_inverse
 
{
L
:
 
ℕ
}
 
(
x
:
 
BitString
 
L
)
:
 
xor
 
x
 
x
 
=
 
BitString_ID
 
:=
2
 
 
by
3
 
 
 
 
apply
 
Vector
.
ext
4
 
 
 
 
intro
 
i
 
i_less_than_L
5
 
 
 
 
simp
[
xor
,
 
BitString_ID
]

This leaves us at the following point:

By expanding the definitions ofxorandBitString_IDusingsimp[xor, BitString_ID]and narrowing down the goal to a subgoal periusingintro iandintro i_less_than_L, we now only need to show that for alli:x[i] + x[i] = 0.In ℤ₂ we know this holds - but how do we write this down in Lean?

It turns out Lean is very helpful and apart from solving things automatically, it can also give us suggestions. Type on the next line of the proof:exact?and check the suggestion in the InfoView:

Let’s first follow the advice and then understand what it does. Replaceexact?byexact CharTwo.add_eq_zero.mpr rfland confirm that it closes the goal 🎉

Now let’s go through it step by step. From the nameCharTwo.add_eq_zerowe can guess that this applies the property of addition to itself equals zero in a ring of characteristic 2. You can always check the details by pressingCmd/Ctrland clicking on the name in the code. In this case the theorem says the following (ref):

⧉
theorem
 
CharTwo
.
add_eq_zero
 
{
R
 
:
 
Type
 
u_1
}
 
[
Ring
 
R
]
 
[
CharP
 
R
 
2
]
 
{
a
 
b
 
:
 
R
}
 
:
 
 
 
 
a
 
+
 
b
 
=
 
0
 
↔
 
a
 
=
 
b

Theiff(↔) gives us 2 functions:

* mp: from left to right(a + b = 0) → (a = b)
* mpr: from right to left(a = b) → (a + b = 0)

Applied to the lemma we’re working on,CharTwo.add_eq_zero.mprsays: given a proof thatx[i] = x[i], it follows thatx[i] + x[i] = 0.

The final thing we need isrflwhich deems two things equal if they are equal by computation. In this case we can use it as a proof thatx[i] = x[i]and together they prove the full goal:

⧉
1
lemma
 
xor_self_inverse
 
{
L
:
 
ℕ
}
 
(
x
:
 
BitString
 
L
)
:
 
xor
 
x
 
x
 
=
 
BitString_ID
 
:=
 
2
 
 
by
3
 
 
 
 
apply
 
Vector
.
ext
4
 
 
 
 
intro
 
i
 
i_less_than_L
5
 
 
 
 
simp
[
xor
,
 
BitString_ID
]
6
 
 
 
 
exact
 
CharTwo
.
add_eq_zero
.
mpr
 
rfl

## Tutorial Part 3: Define a Shannon cipher

* Create a new type usingstructure

We’re getting closer to the end of this tutorial. The final pieces are to define the Shannon cipher as per the book and then show that a One-Time pad is indeed a Shannon cipher.

First, let’s recall the definition from thebookwe’re following:

We need to introduce a new type which has:

* an encryption function
* a decryption function
* a correctness property

For this, we’ll be using astructurein Lean. This is just like astructin other languages. For example, if we want to define a point with an x and y, both Floats:

⧉
structure
 
Point
 
where
 
 
x
 
:
 
Float
 
 
y
 
:
 
Float

How can we apply this to our case for aShannonCipher? First of all, we need the definition to be for a certain message space M, key space K and ciphertext space C.

To make a structure generic for a type you can do:

⧉
structure
 
Point
 
(
T
:
 
Type
)
 
where
 
 
x
 
:
 
T
 
 
y
 
:
 
T

So let’s make a skeleton to fill out:

⧉
1
structure
 
ShannonCipher
 
(
K
 
M
 
C
:
 
Type
)
 
where
2
 
 
enc
:
 
sorry
3
 
 
dec
:
 
sorry
4
 
 
correctness
:
 
sorry

Note that this doesn’t requireK,MandCto have the same type. Writing(K M C: Type)is equivalent to(K: Type) (M: Type) (C: Type)which might indicate more clearly these are separate generic types.

Now we define what types the fields ofShannonCipherhave. Encryption takes a key and a message and gives an output in the ciphertext space. The function signature in math is K × M → C. In Lean, this is expressed as K → M → C (recall the currying explanation from earlier).

The decryption function takes a key and a ciphertext and the output is in the message space. Let’s add these pieces to the definition (write “\r” to get → in Lean):

⧉
1
structure
 
ShannonCipher
 
(
K
 
M
 
C
:
 
Type
)
 
where
2
 
 
enc
:
 
K
 
→
 
M
 
→
 
C
3
 
 
dec
:
 
K
 
→
 
C
 
→
 
M
4
 
 
correctness
:
 
sorry

Finally there is the definition of correctness. The book says this property is:

∀ k ∈ K, m ∈ M: dec(k, enc(k,m)) = m

In Lean we can write this as (type “\forall” to get ∀ in Lean):

⧉
correctness
:
 
∀
 
(
k
:
 
K
)
 
(
m
:
 
M
)
,
 
dec
 
k
 
(
enc
 
k
 
m
)
 
=
 
m

Lean can also derive the types forkandm. Thus the final definition can be:

⧉
1
structure
 
ShannonCipher
 
(
K
 
M
 
C
:
 
Type
)
 
where
2
 
 
enc
:
 
K
 
→
 
M
 
→
 
C
3
 
 
dec
:
 
K
 
→
 
C
 
→
 
M
4
 
 
correctness
:
 
∀
 
k
 
m
,
 
dec
 
k
 
(
enc
 
k
 
m
)
 
=
 
m

Double check we can instantiate ShannonCipher with 3 different types:

⧉
#
check
 
ShannonCipher
 
Nat
 
String
 
Bool

Onto the final step!

## Tutorial Part 4: Prove that One-Time pad is a ShannonCipher

* create a value of a structure type
* syntactic sugar forfun args =>

Finally, we are instantiating a One-Time pad as a ShannonCipher. To do this we need to:

1. Pass the correct values for(K M C: Type).
2. Define theenc/decas applyingxor.
3. Prove the correctness property holds. We’ll follow the proof as it’s given in the book.

To create a value of a type defined with a structure, provide values for all of its fields. Following thestructureexample of the previous subsectionPoint; the point (0,0) can be defined as a value as follows (example from Functional Programming in Lean,ref):

⧉
structure
 
Point
 
where
 
 
x
 
:
 
Float
 
 
y
 
:
 
Float
 
 
def
 
origin
 
:
 
Point
 
:=
 
{
 
x
 
:=
 
0.0
,
 
y
 
:=
 
0.0
 
}

In addition, if we used the generic version of Point (structure Point (T: Type) where ...) we need to add the type explicitly:

⧉
def
 
origin
 
:
 
Point
 
Float
 
:=
 
{
 
x
 
:=
 
0.0
,
 
y
 
:=
 
0.0
 
}

For the OTP we set K := M := C := {0,1}ᴸ, which is the typeBitString (L: ℕ)that we defined earlier, so we can start the OTP like this:

⧉
1
def
 
OneTimePad
 
(
L
 
:
 
ℕ
)
 
:
 
ShannonCipher
 
(
BitString
 
L
)
 
(
BitString
 
L
)
 
(
BitString
 
L
)
 
:=
2
 
 
{
 
3
 
 
 
 
enc
 
:=
 
sorry
,
4
 
 
 
 
dec
 
:=
 
sorry
,
5
 
 
 
 
correctness
 
:=
 
sorry
 
6
 
 
}

For the definition ofencanddecwe can use lambda functions again:

⧉
enc
 
:=
 
fun
 
k
 
m
 
=
>
 
xor
 
k
 
m
dec
 
:=
 
fun
 
k
 
c
 
=
>
 
xor
 
k
 
c

In Lean you can express things in different ways, so we can use some syntactic sugar to express the above code slightly differently.fun args =>can be replaced by bringing the argumentsargsto the left of:=:

⧉
1
enc
 
k
 
m
 
:=
 
xor
 
k
 
m
2
dec
 
k
 
c
 
:=
 
xor
 
k
 
c

The final step is the value ofcorrectness, which should be a proof. We write the proof as stated in the book, recall from Example 2.1:

In order the following properties are applied:

1. substitution of actual encryption function byxor
2. substitution of actual decryption function byxor
3. associativity ofxor
4. self inverse ofxor
5. addition withIDgives self

Start with the proof by replacingsorrywithbyand check what the Lean InfoView says the goal is:

⧉
1
def
 
OneTimePad
 
(
L
:
 
ℕ
 
)
:
 
ShannonCipher
 
(
BitString
 
L
)
 
(
BitString
 
L
)
 
(
BitString
 
L
)
 
:=
 
2
{
3
 
 
enc
 
k
 
m
 
:=
 
xor
 
k
 
m
4
 
 
dec
 
k
 
c
 
:=
 
xor
 
k
 
c
5
 
 
correctness
 
:=
 
6
 
 
 
 
by
7
}

It shows the goal⊢ ∀ (k m : BitString L), k.xor (k.xor m) = mforL : ℕ:

This means Lean already did step 1 and 2. So we can directly apply associativity forxorby referencing the lemma that we proved for that property:

⧉
1
correctness
 
:=
 
2
 
 
 
 
by
3
 
 
 
 
 
 
simp
[
xor_assoc_property
]

This changes the goal to∀ (k m : BitString L), (k.xor k).xor m = m. Now, apply step 4 using the lemmaxor_self_inverse:

⧉
1
correctness
 
:=
 
2
 
 
 
 
by
3
 
 
 
 
 
 
simp
[
xor_assoc_property
]
4
 
 
 
 
 
 
simp
[
xor_self_inverse
]

The goal is now∀ (k m : BitString L), BitString_ID.xor m = m. To apply step 5 of the proof we’d like to use the lemmaxor_show_identity, but if you try that directly you’ll see:

“simp made no progress” - Why? Well, we defined the property asxor x BitString_ID = x, while the current goal isBitString_ID.xor m = m. So while we know this is the same, strictly speaking we haven’t shown this is the same. However, we have shown thatxor x y = xor y xin the commutativity property with lemmaxor_comm_property, so it will work fine if we apply that first.

Verify that the correctness property is proven:

⧉
1
correctness
 
:=
 
2
 
 
 
 
by
3
 
 
 
 
 
 
simp
[
xor_assoc_property
]
4
 
 
 
 
 
 
simp
[
xor_self_inverse
]
5
 
 
 
 
 
 
simp
[
xor_comm_property
]
6
 
 
 
 
 
 
simp
[
xor_show_identity
]

And this completes the definition of the One-Time Pad as a Shannon Cipher, following the book! Now we know (a little bit of) how to grab a cryptography book and implement the content in Lean. Isn’t that super cool?

Okay we’ll add one final thing to make it slightly cleaner and ready for part 2 of the tutorial where we will prove OTP is perfectly secure. (I’ll start working on this soon™)

Recall that we addednamespace BitStringbefore definingxor. This was to ensure Lean wouldn’t interpretxoras the already implemented function and magically start solving things for us. The namespace creates a collection of whatever we defined in it. In this case, it makes sense for the BitString “collection” to containsxor, but not to containShannonCipherand the definition ofOneTimePad.

Leaving it like this would mean that if we add a new file and want to reference the OTP definition, it’d be asBitString.OneTimePad. Not clean!

To solve it, add after thexorlemma’s:

⧉
1
end
 
BitString

Then, in order to use the previously defined functionality, add right before theOneTimePaddefinition:

⧉
1
open
 
BitString

The full code then becomes:

⧉
1
import
 
Mathlib
.
Data
.
ZMod
.
Basic
2
 
3
def
 
BitString
 
(
L
:
 
ℕ
)
:
 
Type
 
:=
 
Vector
 
(
ZMod
 
2
)
 
L
4
 
5
namespace
 
BitString
6
 
7
def
 
xor
 
{
L
:
 
ℕ
}
 
(
x
 
y
:
 
BitString
 
L
)
:
 
(
BitString
 
L
)
 
:=
8
 
 
Vector
.
zipWith
 
(
fun
 
a
 
b
 
=
>
 
a
 
+
 
b
)
 
x
 
y
9
 
10
-- commutativity
11
lemma
 
xor_comm_property
 
{
L
:
 
ℕ
}
 
(
x
 
y
 
:
 
BitString
 
L
)
 
:
 
xor
 
x
 
y
 
=
 
xor
 
y
 
x
 
:=
12
 
 
 
 
by
13
 
 
 
 
 
 
apply
 
Vector
.
ext
14
 
 
 
 
 
 
intro
 
i
 
h_i_lt_L
15
 
 
 
 
 
 
simp
[
xor
]
16
 
 
 
 
 
 
simp
[
add_comm
]
17
 
18
-- associativity
19
lemma
 
xor_assoc_property
 
{
L
:
 
ℕ
}
 
(
x
 
y
 
z
:
 
BitString
 
L
)
 
:
 
xor
 
x
 
(
xor
 
y
 
z
)
 
=
 
xor
 
(
xor
 
x
 
y
)
 
z
 
:=
20
 
 
by
21
 
 
 
 
apply
 
Vector
.
ext
22
 
 
 
 
simp
[
xor
,
 
add_assoc
]
23
 
24
def
 
BitString_ID
 
{
L
:
 
ℕ
}
 
:
 
BitString
 
L
 
:=
 
Vector
.
replicate
 
L
 
0
25
 
26
-- identity
27
lemma
 
xor_show_identity
 
{
L
:
 
ℕ
}
 
(
x
:
 
BitString
 
L
)
:
 
xor
 
x
 
BitString_ID
 
=
 
x
 
:=
28
 
 
Vector
.
ext
 
fun
 
i
 
i_less_than_L
 
=
>
 
by
 
simp
 
[
xor
,
 
BitString_ID
]
29
 
30
-- self-inverse
31
lemma
 
xor_self_inverse
 
{
L
:
 
ℕ
}
 
(
x
:
 
BitString
 
L
)
:
 
xor
 
x
 
x
 
=
 
BitString_ID
 
:=
32
 
 
by
33
 
 
 
 
apply
 
Vector
.
ext
34
 
 
 
 
intro
 
i
 
i_less_than_L
35
 
 
 
 
simp
[
xor
,
 
BitString_ID
]
36
 
 
 
 
exact
 
CharTwo
.
add_eq_zero
.
mpr
 
rfl
37
 
38
end
 
BitString
39
 
40
structure
 
ShannonCipher
 
(
K
 
M
 
C
:
 
Type
)
 
where
41
 
 
enc
:
 
K
 
→
 
M
 
→
 
C
42
 
 
dec
:
 
K
 
→
 
C
 
→
 
M
43
 
 
correctness
:
 
∀
 
k
 
m
,
 
dec
 
k
 
(
enc
 
k
 
m
)
 
=
 
m
44
 
45
open
 
BitString
46
 
47
def
 
OneTimePad
 
(
L
:
 
ℕ
 
)
:
 
ShannonCipher
 
(
BitString
 
L
)
 
(
BitString
 
L
)
 
(
BitString
 
L
)
 
:=
48
{
49
 
 
enc
 
k
 
m
 
:=
 
xor
 
k
 
m
50
 
 
dec
 
k
 
c
 
:=
 
xor
 
k
 
c
51
 
 
correctness
 
:=
52
 
 
 
 
by
53
 
 
 
 
 
 
simp
[
xor_assoc_property
]
54
 
 
 
 
 
 
simp
[
xor_self_inverse
]
55
 
 
 
 
 
 
simp
[
xor_comm_property
]
56
 
 
 
 
 
 
simp
[
xor_show_identity
]
57
}

If you followed the tutorial, please let me know what you think and nudge me for part 2 viaLinkedInorTwitter.

## Epilogue: About Formal Verification in blockchain

You might have heard about formal verification efforts in the blockchain world recently, e.g.Zcashannounced their development team Shielded Labs is aiming to formally verify the Orchard circuits after a critical bug was discovered. Thelean Ethereumteam that is working on the next set of proposed upgrades for Ethereum (a different "lean") aims to formally verify the zkVM they are building.Nethermindformally verified one of the chips in SP1 of Succinct with Lean last year.

In recent months, Vitalik and zkSecurity both published excellent blog posts about the topic."The Final Form of Software Development"byYoichi Hirai(zkSecurity) describes the workflow of having AI agents writing RISC-V assembly code accompanied by proofs in Lean for correctness of the code. AndVitalik's blog posttalks about what formal verification is and how we can really use it to improve software and Ethereum specifically.

Formal verification can help us have more trust in the systems we use. However, it is not a "perfect" solution either; when writing proofs about systems, there is always a step in between the actual code written and the theorems we are proving. For example, the original code gets compiled and we don't know the exact implications, or we have to model the code that was written (which we can do incorrectly).

To learn more about the conext and pitfalls of formal verification for code and why it is still very valuable, I recommendthis eposide of zkPodcastwith Alexander Hicks, who leads the formal verification effort in lean Ethereum.