---
title: 'C++ support by stedolan · Pull Request #14701 · ocaml/ocaml · GitHub'
url: https://github.com/ocaml/ocaml/pull/14701
site_name: hnrss
content_file: hnrss-c-support-by-stedolan-pull-request-14701-ocamlocam
fetched_at: '2026-04-02T11:21:03.373101'
original_url: https://github.com/ocaml/ocaml/pull/14701
date: '2026-04-01'
description: 'The core OCaml system: compilers, runtime system, base libraries - C++ support by stedolan · Pull Request #14701 · ocaml/ocaml'
tags:
- hackernews
- hnrss
---

ocaml



/

ocaml

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.2k
* Star6.2k

## Conversation



Contributor

### stedolancommentedApr 1, 2026

This patch adds a new C++ backend toocamlc, improving on the unincremented C currently in use by the runtime and FFI. As an example, here's a simple program that computes the prime numbers up to a user-specifiedlimit:

module

List

=

struct


let

rec
filter

p

=

function


|

[]
 ->
[]


|

x
 ::
l
 ->
if
 p x
then
 x :: filter p l
else
 filter p l


let

rec
init

i

last

f

=


if
 i
>
 last
then

[]


else
 f i :: init (i
+
1
) last f

end

let

primes

n

=


let

rec
sieve

candidates

=


match
 candidates
with


|

[]
 ->
[]


|

p
 ::
ps
 -> p :: sieve (
List.
filter (
fun

n
 -> n
mod
 p
<>

0
) ps)

in

 sieve (
List.
init
2
 n (
fun

i
 -> i))

let

main

~
limit

=
 primes limit

You can compile this program to C++ using:

ocamlc -incr-c primes.ml

which producesprimes.cpp, containing your program translated to idiomatic, readable C++ code:

Generated C++ code in primes.cpp

#ifndef limit
#error "Parameter limit missing"
#include <stop_after_error>
#endif
template <typename...> struct Cons;
template <int tag, typename...> struct Cons_;
template <int n>
struct I{
static constexpr int tag = 1000;
static constexpr bool nonzero = ((n) != (0));
static constexpr int val = n;
};
struct EXCEPTION{
};
template <typename f0_, typename f1_>
struct Cons<f0_, f1_>{
static constexpr int tag = 0;
static constexpr bool nonzero = true;
static constexpr int val = -1;
typedef f0_ f0;
typedef f1_ f1;
};
template <int tag_, typename f0_, typename f1_>
struct Cons_<tag_, f0_, f1_>{
static constexpr int tag = tag_;
static constexpr bool nonzero = true;
static constexpr int val = -1;
typedef f0_ f0;
typedef f1_ f1;
};
template <typename f0_, typename f1_, typename f2_>
struct Cons<f0_, f1_, f2_>{
static constexpr int tag = 0;
static constexpr bool nonzero = true;
static constexpr int val = -1;
typedef f0_ f0;
typedef f1_ f1;
typedef f2_ f2;
};
template <int tag_, typename f0_, typename f1_, typename f2_>
struct Cons_<tag_, f0_, f1_, f2_>{
static constexpr int tag = tag_;
static constexpr bool nonzero = true;
static constexpr int val = -1;
typedef f0_ f0;
typedef f1_ f1;
typedef f2_ f2;
};
template <typename filter, typename p, typename x, typename l, bool cond>
struct ifthenelse;
template <typename filter, typename p, typename x, typename l>
struct ifthenelse<filter, p, x, l, true>{
typedef Cons<x, typename filter::template app<p>::res::template app<l>::res> res;
};
template <typename filter, typename p, typename x, typename l>
struct ifthenelse<filter, p, x, l, false>{
typedef typename filter::template app<p>::res::template app<l>::res res;
};
template <typename filter, typename p, typename param, bool cond>
struct ifthenelse_;
template <typename filter, typename p, typename param>
struct ifthenelse_<filter, p, param, true>{
typedef typename param::f1 l;
typedef typename param::f0 x;
typedef typename ifthenelse<filter, p, x, l,
 p::template app<x>::res::nonzero>::res res;
};
template <typename filter, typename p, typename param>
struct ifthenelse_<filter, p, param, false>{
typedef I<0> res;
};
template <typename init, typename i, typename last, typename f, bool cond>
struct ifthenelse_2;
template <typename init, typename i, typename last, typename f>
struct ifthenelse_2<init, i, last, f, true>{
typedef I<0> res;
};
template <typename init, typename i, typename last, typename f>
struct ifthenelse_2<init, i, last, f, false>{
typedef Cons<typename f::template app<i>::res,
 typename init::template app<I<((i::val) + (I<1>::val))>>::res::template app<last>::res::template app<f>::res> res;
};
template <typename List, typename sieve, typename candidates, bool cond>
struct ifthenelse_3;
template <typename List, typename sieve, typename candidates>
struct ifthenelse_3<List, sieve, candidates, true>{
typedef typename candidates::f0 p;
struct Primes_primes_sieve__fun_{
template <typename n>
struct app{
typedef I<((I<((n::val) % (p::val))>::val) != (I<0>::val))> res;
};
};
typedef Cons<p,
 typename sieve::template app<typename List::f0::template app<Primes_primes_sieve__fun_>::res::template app<typename candidates::f1>::res>::res> res;
};
template <typename List, typename sieve, typename candidates>
struct ifthenelse_3<List, sieve, candidates, false>{
typedef I<0> res;
};
struct filter;
struct filter{
template <typename p>
struct app{
struct res{
template <typename param>
struct app{
typedef typename ifthenelse_<filter, p, param, param::nonzero>::res res;
};
};
};
};
struct init;
struct init{
template <typename i>
struct app{
struct res{
template <typename last>
struct app{
struct res{
template <typename f>
struct app{
typedef typename ifthenelse_2<init, i, last, f,
 I<((i::val) > (last::val))>::nonzero>::res res;
};
};
};
};
};
};
typedef Cons<filter, init> List;
struct primes{
template <typename n>
struct app{
struct sieve;
struct sieve{
template <typename candidates>
struct app{
typedef typename ifthenelse_3<List, sieve, candidates,
 candidates::nonzero>::res res;
};
};
struct Primes_primes__fun_{
template <typename i>
struct app{
typedef i res;
};
};
typedef typename sieve::template app<typename List::f1::template app<I<2>>::res::template app<n>::res::template app<Primes_primes__fun_>::res>::res res;
};
};
struct main{
template <typename limit_>
struct app{
typedef typename primes::template app<limit_>::res res;
};
};
typedef typename main::template app<I<limit>>::res output;
typedef typename output::print print;

C++ is apurely functionallanguage, with no support for mutable state. Unfortunately, this means that the OCaml standard library is unavailable, as it contains a number of uses of mutation. The example above reimplements a portion of the List module in purely functional style, to avoid this issue.

To run a C++ program, you'll need aC++ interpreter. Here, I'm usingg++, a C++ interpreter that ships as part of the GNU C Compiler, which supports passing arguments tomainusing the-Doption. Running the program with-Dlimit=100prints the prime numbers below 100:

$ g++ -Dlimit=100 primes.cpp
primes.cpp:159:26: error: ‘print’ in ‘output’ {aka ‘struct
Cons<I<2>, Cons<I<3>, Cons<I<5>, Cons<I<7>, Cons<I<11>,
Cons<I<13>, Cons<I<17>, Cons<I<19>, Cons<I<23>, Cons<I<29>,
Cons<I<31>, Cons<I<37>, Cons<I<41>, Cons<I<43>, Cons<I<47>,
Cons<I<53>, Cons<I<59>, Cons<I<61>, Cons<I<67>, Cons<I<71>,
Cons<I<73>, Cons<I<79>, Cons<I<83>, Cons<I<89>, Cons<I<97>, I<0> >
> > > > > > > > > > > > > > > > > > > > > > > >’} does not name a
type
 159 | typedef typename output::print print;
 | ^~~~~

If you haven't written much C++ before, the output format here might strike you as unusual. Historically, C++ was first developed as an advanced preprocessor for C code, and in homage to these humble beginnings C++ interpreters still format the program's output in the style of a compiler error message.

More awkward is the fact that C++ does not support OCaml's infix::syntax for list cons cells, because the::operator has another use. So you'll have to read the output as explicitly nestedCons<hd, tl>cells instead.

C++ can struggle somewhat on larger or longer-running computations. Support for larger programs is in fact disabled by default, but can be enabled by passing the-ftemplate-depth=999999option:

$ g++ -ftemplate-depth=999999 -Dlimit=10000 primes.cpp

On my machine, this prints the prime numbers up to 10000 in about half a minute, consuming approximately 11 GiB of memory.

Performance can vary significantly between C++ implementations. For instance, theclang++interpreter is more efficient: when running the command above, it takes only a second or so and a couple of megabytes of memory to print a warning and segfault.

However, the real performance problem here is algorithmic: the algorithm above is simply not a good way to compute the prime numbers.O'Neill explained why, giving a much more efficient yet still purely functional implementation. Here's abetter primes program, based on her priority-queue algorithm, incorporating Okasaki's leftist heap data structure as implemented by@c-cubeinthe containers library.

Using these more sophisticated data structures,g++is able to compute the prime numbers below 10000 in only 8 seconds, using a modest 3.1 GiB of memory.

Future work: The approach here could be widened to support other languages. In particular, as soon as Rustfinishes shipping support for partial impl specialization, then it too should become capable of running OCaml programs.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.






😄

77


priamfive, Gbury, bluddy, redianthus, dra27, MisterDA, Keryan-dev, S41d, nberth, yakobowski, and 67 more reacted with laugh emoji


❤️

52


gasche, Ekdohibs, Octachron, dra27, MisterDA, kayceesrk, Keryan-dev, mseri, dancrossnyc, TheLortex, and 42 more reacted with heart emoji


🚀

10


brendanzab, harrisonturton, MarcusLages, LoganDark, soerlemans, ajbt200128, Splingush, giltho, heavyrain266, and clarus reacted with rocket emoji



All reactions





incr c;

f89996a





Member

### redianthuscommentedApr 1, 2026•edited

This is amazing!

I am curious about its ability to handle non-uniform recursive datatypes.Have you tried it?For instance:

module

List

=

struct


let

rec
init

i

last

f

=


if
 i
>
 last
then

[]


else
 f i :: init (i
+
1
) last f


let

rec
fold_right

f

l

acc

=


match
 l
with


|

[]
 -> acc

|

hd
 ::
l
 -> f hd (fold_right f l acc)

end

type

'a t
=
 |
Nil

 |
Zero

of
 (
'a

*

'a
)
t

 |
One

of

'a

*
 (
'a

*

'a
)
t

let

rec
cons
 :
'a. 'a -> 'a t -> 'a t
=

fun

x
 ->
function


|

Nil
 ->
One
 (x,
Nil
)

|

Zero

s
 ->
One
 (x, s)

|

One
 (
y
,
s
) ->
Zero
 (cons (x, y) s)

let

ral

limit

=


let
 l
=

List.
init
0
 (pred limit) (
fun

x
 -> x)
in


List.
fold_right cons l
Nil

let

main

~
limit

=
 ral limit



All reactions

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.











support %predint

fe2eeb3





Member

### dra27commentedApr 1, 2026

Glorious! And a particular shout-out to the copyright headers' appeasing ofcheck-typo's header state machine 😂



All reactions

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.









Contributor

Author

### stedolancommentedApr 1, 2026

@redianthusNon-uniform recursive datatypes work fine. Your example doesn't work at the moment because of the use ofStdlib.predwhich uses an unimplemented primitive%predint, but it works if you uselimit - 1instead (just pushed a fix for predint, though, so either should work now)


❤️

3


redianthus, avsm, and LudWittg reacted with heart emoji



All reactions

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.









Member

### avsmcommentedApr 1, 2026

Hang on, I said I needed C--, not C++! Can we just agree on C# instead?


😄

10


talex5, omarjatoi, JohnMatthiasWabwire, argson67, mkhan45, Sari-06, mwerezak, curche, heavyrain266, and thefossguy reacted with laugh emoji



All reactions

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.









### sergezlotocommentedApr 2, 2026

Lovely!Quick, someone merge this pr!



All reactions

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







ducminhgd

 mentioned this pull request


Apr 2, 2026

 Daily News Digest - 2026-04-02

ducminhgd/gossip-bot#279



 Open



### AdelKScommentedApr 2, 2026•edited

I just got here by lurking onhackernews

I couldn't resist a probably dumb question: why translate using templates instead ofconstexprevaluation (which also uses the compiler's C++ interpreter too) and saving the result into the resulting binary. Something like this (hopefully I didn't code it wrong haha)

#
include

<
array
>

#
include

<
cstddef
>

#
include

<
algorithm
>

using

namespace

std
;

template
<
size_t
 max_prime>

consteval
 array<
size_t
, max_prime/
2
>
get_primes
() {
 array<
size_t
, max_prime/
2
> res;

ranges::fill
(res,
0
);

 array<
bool
, max_prime+
1
> is_prime = {
false
,
false
,
true
};

ranges::fill
(is_prime.
begin
() +
3
, is_prime.
end
(),
true
);


for
 (
size_t
 i =
2
 ; i*i <= max_prime ; i++ )

for
 (
size_t
 j =
2
 ; j*i <= max_prime ; j++)
 is_prime[i*j] =
false
;


size_t
 prime_index =
0
;

for
 (
size_t
 i =
0
 ; i <= max_prime; i++)

if
 (is_prime[i])
 {
 res[prime_index] = i;
 prime_index++;
 }

return
 res;
}

int

main
() {
 [[maybe_unused]]
constexpr

auto
 primes = get_primes<
100
>();


return

0
;
}

(I would've usedinplace_vectorbut it's not there yet)

theresulting assemblylooks like this

main:
 push rbp
 mov rbp, rsp
 sub rsp, 416
 mov dword ptr [rbp - 4], 0
 lea rdi, [rbp - 408]
 lea rsi, [rip + .L__const.main.primes]
 mov edx, 400
 call memcpy@PLT
 xor eax, eax
 add rsp, 416
 pop rbp
 ret

.L__const.main.primes:
 .quad 2
 .quad 3
 .quad 5
 .quad 7
 .quad 11
 .quad 13
 .quad 17
 .quad 19
 .quad 23
 .quad 29
 .quad 31
 .quad 37
 .quad 41
 .quad 43
 .quad 47
 .quad 53
 .quad 59
 .quad 61
 .quad 67
 .quad 71
 .quad 73
 .quad 79
 .quad 83
 .quad 89
 .quad 97
 .zero 200

and you see the results inside the binary basically 🤔

Note that I wrote declarative code here but nothing prevents from translating things with a closer (1-to-1?) functional approach, Franken-C++ should have everything need 🤔


👍

1


soerlemans reacted with thumbs up emoji



All reactions

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.









### LoganDarkcommentedApr 2, 2026

why translate using templates instead ofconstexprevaluation

The love of the game.


😄

6


soerlemans, justjake, quartztz, AdelKS, harubi, and thefossguy reacted with laugh emoji



All reactions

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







claude-yolo

bot

 mentioned this pull request


Apr 2, 2026

 Code Leaks, Subscription Bombs, and OCaml Goes C++

thevibeworks/claude-reads-hn#669



 Open



Member

### redianthuscommentedApr 2, 2026

@stedolan, this is really great : before your work, C++ was a functional language, now it is a functional language in which you can use purely functional data structures implemented through non-uniform recursive types.

Indeed, before, the following code would make the compiler loop forever:

#
include

<
iostream
>

template
<
typename
 T>

struct

Enum
 {

enum
 Kind { NIL, ZERO, ONE } kind;

 T head;
 Enum<std::pair<T, T>>* sub;


static
 Enum
Nil
() {

return
 {NIL};
 }


static
 Enum
Zero
(Enum<std::pair<T, T>>* s) {

return
 {ZERO, T{}, s};
 }


static
 Enum
One
(T h, Enum<std::pair<T, T>>* t) {

return
 {ONE, h, t};
 }


size_t

len
()
const
 {

switch
 (kind) {

case
 NIL:

return

0
;

case
 ZERO:

return

2
 * sub->
len
();

case
 ONE:

return

1
 +
2
 * sub->
len
();
 }

return

0
;
 }
};

int

main
() {

auto
 val = Enum<
size_t
>::
One
(

42
,

new
 Enum<std::pair<
size_t
,
size_t
>>(Enum<std::pair<
size_t
,
size_t
>>::
Nil
())
 );

 std::cout <<
"
len:
"
 << val.
len
() << std::endl;
}

Whereas now, people can use an impure language such as OCaml and get their purely functional data structures in C++!

Regarding your future work, I think Rust is a good direction for the same reason :


pub

enum

Enum
<
T
>

{


Nil
,


Zero
(
Box
<
Enum
<
(
T
,

T
)
>
>
)
,


One

{

head

:

T
,

tail

:

Box
<
Enum
<
(
T
,

T
)
>
>

}
,


}


impl
<
T
>

Enum
<
T
>

{


pub

fn

len
(
&
self
)
 ->
usize

{


match

self

{


Self
::
Nil
 =>
0
,


Self
::
Zero
(
sub
)
 =>
2

*
 sub
.
len
(
)
,


Self
::
One

{
 tail
,
 ..
}
 =>
1
 +
2

*
 tail
.
len
(
)


}


}


}


fn

main
(
)

{


let
 val
:

Enum
<
usize
>
 =

Enum
::
One

{

head

:

42
,

tail
:

Box
::
new
(
Enum
::
Nil
)
}
;


println
!
(
"len: {}"
,
 val
.
len
(
)
)
;


}

The Rust compiler can not handle this code and also loop forever!



All reactions

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.









### dzmitry-lahodacommentedApr 2, 2026

In particular, as soon as Rustrust-lang/rust#31844, then it too should become capable of running OCaml programs.

i think Rust already capable to run OCaml programs viahttps://github.com/contextgeneric/cgp



All reactions

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







Foxhunt

 mentioned this pull request


Apr 2, 2026

 Daily Hacker News 02-04-2026

Foxhunt/daily-hackernews#632



 Open

blka

 mentioned this pull request


Apr 2, 2026

 Daily Hacker News 02-04-2026

blka/daily-hackernews#355



 Open

github-actions

bot

 mentioned this pull request


Apr 2, 2026

 Daily Content Summary 2026-04-02

jhengy/content-aggregator#444



 Open

ocaml

 deleted a comment from


greydoubt

Apr 2, 2026



Sign up for free

to join this conversation on GitHub
.
 Already have an account?

Sign in to comment

Add this suggestion to a batch that can be applied as a single commit.
This suggestion is invalid because no changes were made to the code.
Suggestions cannot be applied while the pull request is closed.
Suggestions cannot be applied while viewing a subset of changes.
Only one suggestion per line can be applied in a batch.
Add this suggestion to a batch that can be applied as a single commit.
Applying suggestions on deleted lines is not supported.
You must change the existing code in this line in order to create a valid suggestion.
Outdated suggestions cannot be applied.
This suggestion has been applied or marked resolved.
Suggestions cannot be applied from pending reviews.
Suggestions cannot be applied on multi-line comments.
Suggestions cannot be applied while the pull request is queued to merge.
Suggestion cannot be applied right now. Please check back later.
