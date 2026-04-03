---
title: Home - D Programming Language
url: https://dlang.org/
site_name: hackernews_api
content_file: hackernews_api-home-d-programming-language
fetched_at: '2026-02-13T19:20:30.643924'
original_url: https://dlang.org/
author: arcadia_leak
date: '2026-02-12'
description: D is a general-purpose programming language with static typing, systems-level access, and C-like syntax.
tags:
- hackernews
- trending
---

Report a bug

			If you spot a problem with this page, click here to create a Bugzilla issue.



Improve this page

			Quickly fork, edit online, and submit a pull request for this page.
			Requires a signed-in GitHub account. This works well for small changes.
			If you'd like to make larger changes you may want to consider using
			a local clone.





Dis a general-purpose programming language with
 static typing, systems-level access, and C-like syntax.
 With theD Programming Language, write fast,
 read fast, and run fast.Fast code, fast.



Downloads

Latest version: 2.112.0
 –
Changelog




your code here



Got a brief example illustrating D?

Submit your code to the digitalmars.D forum specifying
 "[your code here]" in the subject.

Upon approval it will be showcased here on a random schedule.

Compute average line length for stdin

The D programming language
Modern convenience.
Modeling power.
Native efficiency.

void
 main()
{

import
 std.range, std.stdio;


auto
 sum = 0.0;

auto
 count = stdin

//Get an input range set up to read one line at a time

 .byLine

//Perform a transparent operation (as in the shell command tee)

 .tee!(l => sum += l.length)
 .walkLength;

 writeln(
"Average line length: "
,
 count ? sum / count : 0);
}

Round floating point numbers

2.4 plus 2.4 equals 5 for sufficiently large values of 2.

import
 std.algorithm, std.conv, std.functional,
 std.math, std.regex, std.stdio;


alias
 round = pipe!(to!
real
, std.math.round, to!string);

static
 reFloatingPoint = ctRegex!
`[0-9]+\.[0-9]+`
;


void
 main()
{

// Replace anything that looks like a real


// number with the rounded equivalent.

 stdin
 .byLine
 .map!(l => l.replaceAll!(c => c.hit.round)
 (reFloatingPoint))
 .each!writeln;
}

Sort lines

Mercury
Venus
Earth
Mars
Jupiter
Saturn
Uranus
Neptune

import
 std.stdio, std.array, std.algorithm;


void
 main()
{
 stdin
 .byLineCopy
 .array
 .sort!((a, b) => a > b)
// descending order

 .each!writeln;
}

Sort an Array at Compile-Time

void
 main()
{

import
 std.algorithm, std.stdio;


"Starting program"
.writeln;


enum
 a = [ 3, 1, 2, 4, 0 ];

// Sort data at compile-time


static

immutable
 b = sort(a);


// Print the result _during_ compilation


pragma
(msg,
"Finished compilation: "
, b);
}

Invoke external programs

void
 main()
{

import
 std.exception, std.stdio, std.process;


auto
 result = [
"whoami"
].execute;
 enforce(result.status == 0);
 result.output.write;
}

Print hex dump

void
 main()
{

import
 std.algorithm, std.stdio, std.file, std.range;

enum
 cols = 14;

// Split file into 14-byte chunks per row

 thisExePath.File(
"rb"
).byChunk(cols).take(20).each!(chunk =>

// Use range formatting to format the


// hexadecimal part and align the text part

 writefln!
"%(%02X %)%*s %s"
(
 chunk,
 3 * (cols - chunk.length),
""
,
// Padding

 chunk.map!(c =>
// Replace non-printable

 c < 0x20 || c > 0x7E ? '.' :
char
(c))));
}

Start a minimal web server

#!/usr/bin/env dub

/+ dub.sdl:
dependency "vibe-d" version="~>0.9.0"
+/


void
 main()
{

import
 vibe.d;
 listenHTTP(
":8080"
, (req, res) {
 res.writeBody(
"Hello, World: "
 ~ req.path);
 });
 runApplication();
}

Initialize an Array in parallel

void
 main()
{

import
 std.datetime.stopwatch : benchmark;

import
 std.math, std.parallelism, std.stdio;


auto
 logs =
new

double
[100_000];

auto
 bm = benchmark!({

foreach
 (i,
ref
 elem; logs)
 elem = log(1.0 + i);
 }, {

foreach
 (i,
ref
 elem; logs.parallel)
 elem = log(1.0 + i);
 })(100);
// number of executions of each tested function

 writefln(
"Linear init: %s msecs"
, bm[0].total!
"msecs"
);
 writefln(
"Parallel init: %s msecs"
, bm[1].total!
"msecs"
);
}

Sort in-place across multiple arrays

void
 main()
{

import
 std.stdio : writefln;

import
 std.algorithm.sorting : sort;

import
 std.range : chain;


int
[] arr1 = [4, 9, 7];

int
[] arr2 = [5, 2, 1, 10];

int
[] arr3 = [6, 8, 3];

// @nogc functions are guaranteed by the compiler


// to be without any GC allocation

 () @nogc {
 sort(chain(arr1, arr2, arr3));
 }();
 writefln(
"%s\n%s\n%s\n"
, arr1, arr2, arr3);
}

Count frequencies of character pairs

void
 main()
{

import
 std.stdio : writefln;

// An associative array mapping pairs of characters to integers


int
[
char
[2]] aa;

auto
 arr =
"ABBBA"
;


// Iterate over all pairs in the string


// ['A', 'B'], ['B', 'B'], ..., ['B', 'A']


foreach
 (i; 0 .. arr.length - 1)
 {

// String slicing doesn't allocate a copy


char
[2] pair = arr[i .. i + 2];

// count occurrences

 aa[pair]++;
 }

foreach
 (key, value; aa)
 writefln(
"key: %s, value: %d"
, key, value);
}

Tiny RPN calculator

2 3 3 4 + * *

void
 main()
{

import
 std.stdio, std.string, std.algorithm, std.conv;


// arr is real[] and sym is the current symbol

 readln.split.fold!((arr, sym)
 {

static

foreach
 (c;
"+-*/"
)

if
 (sym == [c])

// replace the last 2 elements with the binary op


return
 arr[0 .. $-2] ~

mixin
(
"arr[$-2] "
 ~ c ~
" arr[$-1]"
);


// sym must be a number


return
 arr ~ sym.to!
real
;
 })((
real
[]).init).writeln;
}

Subtyping with alias this

struct
 Point
{

private

double
[2] p;

// Forward all undefined symbols to p


alias
 p
this
;

double
 dot(Point rhs)
 {

return
 p[0] * rhs.p[0] + p[1] * rhs.p[1];
 }
}

void
 main()
{

import
 std.stdio : writeln;

// Point behaves like a `double[2]` ...

 Point p1, p2; p1 = [2, 1], p2 = [1, 1];

assert
(p1[$ - 1] == 1);

// ... but with extended functionality

 writeln(
"p1 dot p2 = "
, p1.dot(p2));
}



## Support the D language

D is made possible through the hard work and dedication of many volunteers,
 with the coordination and outreach of the D Language Foundation, a 501(c)(3) non-profit organization.
 You can help further the development of the D language and help grow our
 community by supporting the Foundation.

DonateLearn More About The FoundationLots ofto oursponsorsandcontributors.



### Industry Proven





 D shines from low-level control
 to high-level abstraction



Success stories


What is D used for?





#### News



Stay updated with the latest posts in theOfficial D Blogfrom February 22, 2024:DMD Compiler as a Library: A Call to Armsby
 Razvan Nitu.

From October 2, 2023:Crafting Self-Evident Code with Dby
 Walter Bright.

#### Learn



Take theTour, exploremajor featuresin D,
 browse thequick overview,
 start withCorC++background,
 and ask questions in theLearn forum.

For a deeper dive into D
 check outbooksorvideossuch as Ali Çehreli's free bookProgramming in D.



#### Community



Discuss D on theforums, join
 theIRC channel, read ourofficial Blog, or follow us
 onTwitter.
 Browse thewiki, where among
 other things you can find thehigh-level visionof theD Language Foundation.

#### Documentation



Refer to thelanguage specificationand
 the documentation ofPhobos, D's standard
 library. TheDMD manualtells you how
 to use the compiler. Readvarious articlesto deepen
 your understanding.



#### Contribute



Report any bugs you find to ourbug tracker. If you can fix an issue, make a pull request onGitHub.
 There aremany other waysto help, too!

#### Packages



DUB is the package manager for D.Get started with DUB, and check out theavailable packages.



#### Run



Configure linting,
 formatting or
 completion for
 your favoriteIDE,editoror
 userun.dlang.ioto play and experiment
 with D code.

#### Explore



Learn aboutpragmatic D,
 theDStyle,common D idiomsandtemplates,

 See what's coming upcoming withnext version,
 exploreD Improvement Proposals,
 and don't fearD's garbage collection.

## Fast code, fast.

### Write Fast

D allows writing large code fragments without redundantly specifying types,
like dynamic languages do. On the other hand, static inference deduces types and other
code properties, giving the best of both the static and the
dynamic worlds.voidmain()
{// Define an array of numbers, double[].// Compiler recognizes the common// type of all initializers.autoarr = [ 1, 2, 3.14, 5.1, 6 ];// Dictionary that maps string to int,// type is spelled int[string]autodictionary = ["one": 1,"two": 2,"three": 3 ];// Calls the min function defined belowautox = min(arr[0], dictionary["two"]);
}// Type deduction works for function results.// This is important for generic functions,// such as min below, which works correctly// for all comparable types.automin(T1, T2)(T1 lhs, T2 rhs)
{returnrhs < lhs ? rhs : lhs;
}

Automatic memory management makes for safe, simple, and robust code.
D also supports scoped resource management (aka theRAIIidiom)
andscopestatementsfor
deterministic transactional code that is easy to write and read.importstd.stdio;classWidget { }voidmain()
{// Automatically managed.autow =newWidget;// Code is executed in any case upon scope exit.scope(exit) { writeln("Exiting main."); }// File is closed deterministically at scope's end.foreach(line; File(__FILE_FULL_PATH__).byLine())
 {
 writeln(line);
 }
 writeln();
}

Built-in linear and associative arrays, slices, and ranges make daily
programming simple and pleasant for tasks, both small and large.The D programming language
Modern convenience.
Modeling power.
Native efficiency.// Compute average line length for stdinvoidmain()
{importstd.range, std.stdio;autosum = 0.0;autocount = stdin.byLine
 .tee!(l => sum += l.length).walkLength;

 writeln("Average line length: ",
 count ? sum / count : 0);
}

### Read Fast

The best paradigm is to not impose something at the expense of others.
D offers classic polymorphism, value semantics, functional
style, generics, generative programming, contract programming,
and more—all harmoniously integrated.// Interfaces and classesinterfacePrintable
{voidprint(uintlevel)// contract is part of the interfacein{assert(level > 0); }
}// Interface implementationclassWidget : Printable
{voidprint(uintlevel)in{ }do{ }
}// Single inheritance of stateclassExtendedWidget : Widget
{overridevoidprint(uintlevel)in{/* weakening precondition is okay */}do{//... level may be 0 here ...}
}// Immutable data shared across threadsimmutablestring programName ="demo";// Mutable data is thread-localintperThread = 42;// Explicitly shared datasharedintperApp = 5;// Structs have value semanticsstructBigNum
{// intercept copyingthis(this) { }// intercept destructor~this() { }
}voidmain()
{// ...}

D offers an innovative approach to concurrency, featuring true
immutable data, message passing, no sharing by default, and
controlled mutable sharing across threads.Read more.

From simple scripts to large projects, D has the breadth
to scale with any application's needs: unit testing,
information hiding, refined modularity, fast compilation, precise
interfaces.Read more.

### Run Fast

D compiles naturally to efficient native code.

D is designed such that most "obvious" code is fastandsafe. On occasion a function might need to escape the confines of type
safety for ultimate speed and control. For such rare cases D offers
native pointers, type casts, access to any C function without any
intervening translation, manual memory management, custom allocators
and even inline assembly code.importcore.stdc.stdlib;voidlivingDangerously()
{// Access to C's malloc and free primitivesenumbytes =float.sizeof * 1024 * 1024;autobuf = malloc(bytes);// free automatically upon scope exitscope(exit) free(buf);// Interprets memory as an array of floatsautofloats =cast(float[]) buf[0 .. bytes];// Even stack allocation is possibleautomoreBuf = alloca(4096 * 100);//...}// Using inline asm for extra speed on x86uintchecked_multiply(uintx,uinty)
{uintresult;version(D_InlineAsm_X86)
 {// Inline assembler "sees" D variables and labels.asm{
 mov EAX,x ;
 mul EAX,y ;
 mov result,EAX ;
 jc Loverflow ;
 }returnresult;
 }else{
 result = x * y;if(!y || x <=uint.max / y)returnresult;
 }
Loverflow:thrownewException("multiply overflow");
}voidmain()
{// ...}

The@safe,@trusted, and@systemfunction
attributes allow the programmer to best decide the safety-efficiency
tradeoffs of an application, and have the compiler check for
consistency.Read more.

Copyright © 1999-2026 by the
D Language Foundation
 | Page generated by

Ddoc
 on Thu Jan 15 22:48:15 2026
 
