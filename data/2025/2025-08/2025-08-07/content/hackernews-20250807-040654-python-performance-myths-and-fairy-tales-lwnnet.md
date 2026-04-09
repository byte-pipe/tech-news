---
title: Python performance myths and fairy tales [LWN.net]
url: https://lwn.net/SubscriberLink/1031707/73cb0cf917307a93/
site_name: hackernews
fetched_at: '2025-08-07T04:06:54.600468'
original_url: https://lwn.net/SubscriberLink/1031707/73cb0cf917307a93/
author: todsacerdoti
date: '2025-08-07'
---

LWN
.net

News from the source






User:


Password:



 |


 |


Subscribe
 /

Log in
 /

New account

# Python performance myths and fairy tales

## [LWN subscriber-only content]

### Welcome to LWN.netThe following subscription-only content has been made available to you
by an LWN subscriber. Thousands of subscribers depend on LWN for the
best news from the Linux and free software communities. If you enjoy this
article, please considersubscribing to LWN. Thank you
for visiting LWN.net!ByJake EdgeAugust 5, 2025EuroPythonAntonio Cuni, who
is a longtime Python performance engineer andPyPydeveloper, gave a presentation atEuroPython
2025about "Myths and fairy tales around Python performance" on
the first day of the conference in Prague. As might be guessed from the
title, he thinks that much of the conventional wisdom about Python
performance is misleading at best. With lots of examples, he showed where
the real problems that he sees lie. He has come to the conclusion that memory
management will ultimately limit what can be done about Python performance,
but he has an
early-stage project calledSPythat
might be a way toward a super-fast Python.He started by asking the audience to raise their hands if they thought
"Python is slow or not fast enough"; lots of hands went up, which
was rather different than when he gave the presentation at PyCon Italy,
where almost no one raised their hand. "Very different audience", he
said with a smile. He has been working on Python performance for many
years, has talked with many Python developers, and heard some persistent
myths, which he would like to try to dispel.#### MythsThe first is that "Python is not slow"; based on the raised hands,
though, he thought that most attendees already knew that was a myth. These
days, he hears developers say that Python speed doesn't really matter,
because it is a glue language; "nowadays only the GPU matters", so
Python is fast enough. Pythonisfast enough for some tasks, he
said, which is why there are so many people using it and attending
conferences like EuroPython.There is a set of programs where Python is fast enough, but that set does
not hold all of the Python programs in use—it is only a subset. The
programs that need more Python performance are what is driving all of the
different efforts to optimize the interpreter, but are also causing
developers to constantly work to improve the performance of their programs, often by usingCython,Numba, and the like.In hisslides,
he represented the two sets as circles, with "programs where Python is fast
enough" fully inside "Python programs"; he then added the set of "all
possible programs" fully encompassing the other two. In his ideal world,
all possible programs would be able to be written with Python; currently,
programs that need all of the performance of the processor cannot use
Python. He would like to see the inner circles grow so that Python can
be used in more programs.The corollary of the "it's just a glue language" statement is that you
"just need to rewrite the hot parts inC/C++", though that is a little out
of date; "nowadays they say that we should rewrite it in Rust".
That is "not completely false", it is a good technique to speed up
your code, but soon enough it will "hit a wall". ThePareto
principle—described with a slide created by ChatGPT for unclear
reasons—says that 80% of the time will be spent in 20% of the code. So
optimizing that 20% will help.But the program will then run intoAmdahl's law, which
says that the improvement for optimizing one part of the code is limited by
the time spent in the now-optimized code;
"what was the hot part now is very very fast and then you need to
optimize everything else". He showed a diagram where someinner()function was taking 80% of the time; if that gets reduced
to, say, 10% of what it was, the rest of the program now dominates the run
time.Another "myth" is that Python is slow because it is interpreted; again,
there is some truth to that, but interpretation is only a small part of
what makes Python slow. He gave the example of a simple Python
expression:p.x * 2A compiler for C/C++/Rust could turn that kind of expression into three
operations: load the value ofx, multiply it by two, and then
store the result. In Python, however, there is a long list of operations
that have to be performed, starting with finding the type ofp,
calling its__getattribute__()method, throughunboxingp.xand2, to finally boxing the result, which requires
memory allocation. None of that is dependent on whether Python is
interpreted or not, those steps are required based on the language
semantics.#### Static typesNow people are using static types in Python, so he hears people say that
compilers for the language can now skip past all of those steps and
simply do the operation directly. He put up an example:def add(x: int, y: int) -> int:
 return x + y

 print(add(2, 3))But static typing is not enforced at run time, so there are various ways to
calladd()with non-integers, for example:print(add('hello ', 'world')) # type: ignoreThat is perfectly valid code and the type-checker is happy because of the
comment, but string addition is not the same as for integers. The
static types "are completely useless from the point of view of
optimization and performance". Beyond that, the following is legal
Python too:class MyClass:
 def __add__(self, other):
 ...

 def foo(x: MyClass, y: MyClass) -> MyClass:
 return x + y

 del MyClass.__add__"Static compilation of Python is problematic because everything can
change", he said.So, maybe, "a JIT compiler can solve all of your problems"; they can
go a long way toward making Python, or any dynamic language, faster, Cuni
said. But that leads to "a more subtle problem". He put up a slide
with atrilemmatriangle: a dynamic language, speed, or a simple implementation.
You can have two of those, but not all three.Python has historically favored a dynamic, simply implemented language, but
it is moving toward a dynamic, fast language with projects like theCPython JIT compiler. That loses the simple
implementation, but he does not have to care "because there are people
in the front row doing it for me", he said with a grin.In practice, though, it becomes hard to predict performance with a JIT.
Based on his experience with PyPy, and as a consultant improving Python
performance for customers, it is necessary to think about what the JIT will
do in order to get the best performance. That is a complex and error-prone
process; he found situations where he was "unable to trigger
optimizations in PyPy's compiler because the code was too complicated".All of this leads to what he calls "optimization chasing". It
starts with a slow program that gets its fast path optimized, which results
in a faster program and everyone is happy. Then they start to rely on that
extra speed, which can suddenly disappear with a seemingly unrelated change
somewhere in the program. His favorite example is a program that was
running on PyPy (using Python 2) and suddenly got 10x slower; it turned out
that a Unicode key was being used in a dictionary of strings
that led the JIT to de-optimize the code so that everything got much
slower.#### DynamicHe put up some code that did not really do anything exciting or useful, he
said, but did demonstrate some of the problems that Python compilers
encounter:import numpy as np

 N = 10

 def calc(v: np.ndarray[float], k: float) -> float:
 return (v * k).sum() + NThe compiler really can assume nothing from that code. Seemingly, it
importsNumPyin the usual way, thecalc()function multiplies each element of thevarray byk, adds them all up withsum()and then adds the constantNto that. First off, theimportmay not bring in NumPy
at all; there could be some import hook somewhere that does something
completely unexpected.Ncannot be assumed to be ten, because
that could be changed elsewhere in the code; as with the earlieradd()function, the type declarations oncalc()are not
ironclad either.But, in almost all cases, that code would do exactly what it looks like it
does. Developers rarely do these kinds of things that the language would
allow, but the
gap between the way programmers normally write Python and the definition of
the language is what "makes life complicated for the interpreter".
In practice, a lot of what Python allows does not actually happen.It is the extremely dynamic nature of the language that makes it slow,
"but at the same time it's what makes Python very nice". The
dynamic features are not needed 99% of the time, Cuni said, but "in that
1% are what you need to make Python awesome". Libraries often use
patterns that rely on the dynamic nature of the language in order to make
APIs "that end users can use nicely" so those features cannot simply
be removed.#### GameThe "compiler game" was up next; he progressively showed some code snippets
to point out how little a compiler can actually "know" about the code.
This code might seem like it should give an error of some sort:class Point:
 def __init__(self, x, y):
 self.x = x
 self.y = y

 def foo(p: Point):
 assert isinstance(p, Point)
 print(p.name) # ???Insidefoo(), the compiler knows thatpis aPoint, which has nonameattribute. But, of course,
Python is a dynamic language:def bar():
 p = Point(1, 2)
 p.name = 'P0'
 foo(p)Meanwhile, here is an example where the compiler cannot even assume that
the method exists:import random

 class Evil:
 if random.random() > 0.5:
 def hello(self):
 print('hello world')

 Evil().hello() # 🤷🏻‍♂️Legal Python, but "this is not something to define in production, I
hope", he said with a laugh. "Half of the time it still works, half
of the time
it raises an exception. Good luck compiling it."In another example, he showed a function:def foo():
 p = Person('Alice', 16)
 print(p.name, p.age)
 assert isinstance(p, Person) # <<<ThePersonclass was not shown (yet), but there was an empty class
(just "pass") calledStudent. In this case, theassertwill fail, because of the definition ofPerson:class Person:
 def __new__(cls, name, age):
 if age < 18:
 p = object.__new__(Student)
 else:
 p = object.__new__(Person)
 p.name = name
 p.age = age
 return p"You can have a class with a dunder-new [i.e.__new__()], which
returns something which is unrelated and is not an instance of the class.
Good luck optimizing that."The final entrant in the game was the following:N = 10

 @magic
 def foo():
 return NHe "de-sugared" the@magicdecorator and added some assertions:def foo():
 return N

 bar = magic(foo)

 assert foo.__code__ == bar.__code__
 assert bar.__module__ == '__main__'
 assert bar.__closure__ is None

 assert foo() == 10
 assert bar() == 20 # 🤯😱The code object forfoo()andbar()are the same, but
they give different results. As might be guessed, the value ofNhas been changed bymagic(); the code is as follows:def rebind_globals(func, newglobals):
 newfunc = types.FunctionType(
 func.__code__,
 newglobals,
 func.__name__,
 func.__defaults__,
 func.__closure__)
 newfunc.__module__ = func.__module__
 return newfunc

 def magic(fn):
 return rebind_globals(fn, {'N': 20})That returns a version of the function (foo()was passed) that has
a different view of the values of the global variables. That may seem like
a far-fetched example, but he wrotecode
much like thatfor thepdb++
Python debuggermany years ago. "I claim I had good reason to do
that", he said with a chuckle.#### AbstractionSo there are parts of the language that need to be accounted for, as he
showed in the game, but there is a more fundamental problem: "in Python,
abstractions are not free". When code is written, developers want
performance, but they also want the code to be understandable and
maintainable. That comes at a cost. He started with a simple function:def algo(points: list[tuple[float, float]]):
 res = 0
 for x, y in points:
 res += x**2 * y + 10
 returnIt takes a list of points, each represented as a tuple of floating-point
numbers, and performs a calculation using them.
Then he factored out the calculation into its own function:def fn(x, y):
 return x**2 * y + 10That is already slower than the original, because there
is overhead for calling a function: the function has to be looked up, a
frame object has to be created, and so on. A JIT compiler can help, but it
will still have more overhead. He took things one step further by
switching to aPointdata class:@dataclass
 class Point:
 x: float
 y: float

 def fn(p):
 return p.x**2 * p.y + 10

 def algo(items: list[Point]):
 res = 0
 for p in items:
 res += fn(p)
 returnThat, of course, slows it down even further. This is a contrived example,
Cuni said, but the idea is that every abstraction has a cost, "and then
you end up with a program that is very slow". It was an example of
what he calls "Python to Python" abstraction, where the code is being
refactored strictly within the language.A "Python to C" abstraction, where the hot parts of the code are factored
out into C or some other compiled language, also suffers from added costs.
One could imagine that Python implementations get more and more
optimizations such that the list ofPointobjects is represented
in a simple linear array of floating-point numbers, without boxing, but iffn()is written for Python's C API, those numbers will need to be
boxed and unboxed (in both directions), which is completely wasted work.
It is "unavoidable with the current C API". One of the ways to
speed up programs that were running under PyPy was to remove the C code and
perform the calculations directly in Python, which PyPy could optimize
well.#### An elephantThere is an elephant in the room, however, with regard to Python
performance, though it is one he rarely hears about: memory management. In
today's hardware, "computation is very cheap", but memory is the
bottleneck. If the data is in a cache at any level, accessing it is
inexpensive, but RAM accesses are quite slow. "Generally speaking, if
you want to have very very good performance, we should avoid cache misses
as much as possible."But Python is prone to having a memory layout that is cache-unfriendly. He
showed a simple example:class Person:
 def __init__(self, name, age):
 self.name = name
 self.age = age

 p = [Person('Alice', 16), Person('Bob', 21)]EachPersonhas two fields, which ideally would be placed together
in memory, and the two objects in the list would also be placed together,
for a cache-friendly layout. In practice, though, those objects are all
scattered throughout memory; he showed avisualization from
Python Tutor. Each arrow represented a pointer that needed to be
followed, thus a potential cache miss; there were nearly a dozen arrows for
this simple data structure."This is something you cannot just solve with a JIT compiler; it's
impossible to solve it without changing semantics." Python is
inherently cache-unfriendly, he said, "and I honestly don't know how to
solve this problem". His "sad truth" conclusion is that "Python
cannot be super-fast" without breaking compatibility. Some of the
dynamic features ("let's call it
craziness") he had described in the talk will eventually hamper performance improvements. "If we
want to keep this craziness, well, we have to leave some performance on the
table."His next slide was "The end", complete with emojis of sadness ("😢💔🥹"),
which is where he ended the talk when he gave it at PyCon Italy a year
earlier. This time, though, he wanted to "give a little hope" so he
added a question mark, then reiterated that without breaking
compatibility Python could not get super-fast.He has a proposal for the community if it decides that Python should try to
reach top-level performance, which he hopes the community does, but
"it's fine to say 'no'". He suggests tweaking the language
semantics by keeping the dynamic features where they are actually useful,
perhaps by limiting the kinds of dynamic changes that can be made to
specific points in time, so that compilers can depend on certain behavior
and structure. "Not to allow the world to change at any point in
time as it is now."Meanwhile, the type system should be revamped with an eye on performance.
Currently, the types are optional and not enforced, so they cannot be
used for optimizations. The intent would be that performance-oriented code
could be written in Python, not in some other language called from Python.
But, for cases where calling another language is still desirable, the
extra cost (e.g. boxing) of doing so should be removed. "Most
importantly, we want something which stays Pythonic, because we like this
language or we wouldn't be here."Cuni said that he has a potential solution, "which is not to make Python
faster", because he claims that is not possible. SPy, which stands for
"Static Python", is a project he started a few years ago to address the
performance problems. All of the standard disclaimers apply to SPy, it is
"a work in progress, research and development, [and] we don't know where it
will go". The best information can be found on the GitHub page linked
above or in histalk on SPy at PyCon
Italyin late May.He showed a quickdemoof doing
realtime edge detection from a camera; it ran in the browser usingPyScript. The demo shows the raw camera
feed on the left
and, at first, edge detection being run in NumPy on the right; NumPy
achieves fewer than two frames per second (fps). Switching to a SPy-based
edge-detection algorithm makes the right-hand image keep up with the
camera, running at around 60fps. Thecode for the
demois available on GitHub as well.He recommended the SPy repository and its issue tracker in particular for
interested attendees; some issues have been tagged as "good first issue"
and "help wanted". There is also aDiscord serverfor
chatting about the project. Before too long, a video of the talk should
appear on theEuroPython YouTube channel.[I would like to thank the Linux Foundation, LWN's travel sponsor, for
travel assistance to Prague for EuroPython.]Index entries for this articleConferenceEuroPython/2025PythonPerformanceto post comments



### Dynamism or performance: pick twoPosted Aug 5, 2025 17:43 UTC (Tue)
 byq3cpma(subscriber, #120859)
 [Link] (5 responses)Please bear with the smug Lisp weenie talk for a second: there seems to be a head-in-sand stance that you can't have both extreme dynamism and good performance.I think Common Lisp is one of the languages that tried the hardest to crack that dilemma and partly succeeded (Julia may be joining it).The key is not to have a language designed to be particularly fast, but one that is designed not to be slow (e.g. can't influence the standard library or language) from the start and most importantly, giving tools to manually optimize the hot parts; even if that means a lot of elbow grease.This means that you must be able to make _localized_ tradeoffs between speed and dynamism:* Gradual typing* CLOS vs structures (would be dataclasses in Python)* Inlining a single function call* Type, lifetime (allocate on stack) and compiler optimization level declarations can be restricted to any scope with `locally`Of course, having such an introspectable compilation process allows many user extensions to try and improve the status quo (e.g.https://github.com/marcoheisig/fast-generic-functionshttps://github.com/numcl/specialized-function), but that's only a very large bonus.### Dynamism or performance: pick twoPosted Aug 5, 2025 18:01 UTC (Tue)
 byq3cpma(subscriber, #120859)
 [Link] (2 responses)Though, about the Python conundrum at hand where it obviously can't redesign itself right now, I think doing it like CL optimizing compilers do might be a good idea: if you toggle a flag, type declarations change from assertions to "trusted blindly by the compiler", so that the usual static typing optimizer can do its job (https://www.sbcl.org/manual/#Declarations-as-Assertions).If Python coupled that mechanism (again, should be able to only enable at scope level or at least function level) with a way to declare that a specific function/variable is frozen (thus inlinable) and that change is an UB, it may work without upheaving the ecosystem.Perl got a strict mode, I think Python could get a "fast" one.### Dynamism or performance: pick twoPosted Aug 6, 2025 14:32 UTC (Wed)
 byDemiMarie(subscriber, #164188)
 [Link]UB is not a good idea unless you want to gain C’s insecurity as well. Exact type checks (“is this exactly of this type?”) are cheap.### The "guard" trick from JITs (including PyPy)Posted Aug 6, 2025 17:20 UTC (Wed)
 byfarnz(subscriber, #17727)
 [Link]There's a trick you can use, called a "guard", that would avoid it being UB.A guard is a cheap to evaluate runtime test, that returns either "true" or "false". If you're testing something that can get expensive, you handle that by returning a safe approximation to the result quickly; so, for example, your guard might look at type hints and return "yes, the runtime types match the hints" or "no, the runtime types might not match". In the case of depending on the type of a global variable, you might approximate by saying "no, the runtime types might not match" if any global variable has changed since the guard was created; this is OK, because it'll push you down the slow path even when you could go down the fast path.You then generate one or more guards as you generate an optimized function; the essential guard is one that tells you to go down the slow path if runtime types don't match the type hints you depended on. You can then add other guards to tell you if you need to regenerate the optimized path, or to take you down a very fast path in limited circumstances (e.g. a guard that says that if all the input values are less than 2**28, then you can use 32 bit registers throughout).Finally, you put a conditional at the top of every optimized function; "if the guard is true, call the optimized form. Else, go down the slow path".From here, there's a whole bunch of research you can draw upon (some of it incorporated into PyPy) that helps you minimise the number of guard checks you actually run at runtime; for example, you can know that if the guard of function bar returns "true" on the first loop iteration, it will continue to return "true" on all future iterations, and hoist the guard outside the loop, or that if you combine the guards for foo and bar, then foo can directly call the optimized form of bar, bypassing its guard check.The result of this is teaching people that "high performance" Python needs you to write code such that the guards are simple and never false (no touching globals outside of top-level functions, for example, or make sure that your code type checks). People who ignore that (for debugging, or because they don't care) still get working Python; people who pay attention get fast Python.### Accessors vs attributesPosted Aug 6, 2025 2:30 UTC (Wed)
 byDemiMarie(subscriber, #164188)
 [Link] (1 responses)My understanding is that Common Lisp defstruct produces accessors that only work on something that is exactly an instance of the strict. This means that the accssesors only need go check that the tag (in the pointer) and type (stored in the object header) are correct before loading the value from a fixed offset. That is going to be quite a bit faster than a dictionary lookup.### Accessors vs attributesPosted Aug 6, 2025 10:54 UTC (Wed)
 byunya(guest, #102269)
 [Link]DEFSTRUCT is pretty old and explicitly tuned for speed in design. One of the big issues in developing something with is that that not only are the accessors very simple, they are also inlined by default (which is part of why they are very simple)### OptimisationPosted Aug 5, 2025 23:55 UTC (Tue)
 bytialaramex(subscriber, #21167)
 [Link]> A compiler for C/C++/Rust could turn that kind of expression into three operations: load the value of x, multiply it by two, and then store the result.Perhaps even more importantly, the compiler might well eventually emit some entirely different operations or none at all by the "As if" rule during optimisation. Idiom recognition is an extreme example of this, compilers for many decades have been able to spot idiomatic ways to express in a compiled language an idea that is not efficiently realised the way it's expressed. e.g. in C you'd write a loop to walk the bits in an integer and count how many are set, but the target CPU may have a POPCOUNT instruction which just does all of that. So the compiler doesn't emit a loop at all, just a single instruction.I disagree with the dynamism / speed / simplicity trilemma. I think if you want speed you must give up dynamism AND simplicity. Of the two I mourn simplicity, but speed is hard to say "No" to.### Subtyping and mutable reference types considered slowPosted Aug 6, 2025 14:41 UTC (Wed)
 byDemiMarie(subscriber, #164188)
 [Link]One of the reasons you can’t have packed arrays (as in the last example) is that Python allows a List[T] to hold any subclass of T, which means the size of T is not known at compile-time. A packed array can only hold T, not subclasses of T. This is the reason for the infamous slicing problem in C++. Also, virtual functions are not fast. Performance needs non-virtual functions.The other problem is that Python types have reference semantics, rather than value semantics. You need value semantics (C#/D structs) or immutable types to make this work.### mypyc?Posted Aug 6, 2025 15:24 UTC (Wed)
 bytaymon(subscriber, #112650)
 [Link]Doesn't mypyc exist, and compile Python to static machine code based on type hints? I admit I would also have assumed that using type hints for optimization was impossible because of unsoundness, but there exists a project that does it. I'm also curious how SPy is different.





Copyright © 2025, Eklektix, Inc.Comments and public postings are copyrighted by their creators.Linux is a registered trademark of Linus Torvalds
