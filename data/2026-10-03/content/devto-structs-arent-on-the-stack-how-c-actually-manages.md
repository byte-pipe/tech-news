---
title: Structs Aren't on the Stack. How C# Actually Manages Memory. - DEV Community
url: https://dev.to/smtahosin/structs-arent-on-the-stack-how-c-actually-manages-memory-128p
site_name: devto
content_file: devto-structs-arent-on-the-stack-how-c-actually-manages
fetched_at: '2026-10-03T03:06:56.529032'
original_url: https://dev.to/smtahosin/structs-arent-on-the-stack-how-c-actually-manages-memory-128p
author: S M Tahosin
date: '2026-10-01'
description: The biggest myth in C# is that structs live on the stack and classes live on the heap. Here is what the CLR actually does with your data. Tagged with csharp, dotnet, programming, beginners.
tags: '#csharp, #dotnet, #programming, #beginners'
---

Ask almost any developer what the difference is between aclassand astructin C#, and you will hear the exact same rehearsed answer:

"Classes live on the heap. Structs live on the stack."

It is in university slides. It is in popular YouTube tutorials. It is repeated in technical job interviews every single day.

And it is dead wrong.

If you write C# while holding onto that mental model, you are flying blind. You will be mystified when your application triggers unexpected Garbage Collection pauses, you will introduce subtle mutability bugs that take days to isolate, and you will miss out on the greatest performance features modern .NET has to offer.

Let us pull back the curtain on what the Common Language Runtime (CLR) is actually doing with your data in memory.

## The Textbook Myth That Refuses to Die

Where did the idea that "structs live on the stack" come from?

Early programming courses tried to simplify memory concepts: the stack is fast and self-cleaning, while the heap requires a garbage collector. Teachers told students: "Small things likeintandstructgo to the fast stack, big things likeclassgo to the slow heap."

It sounds tidy. But it completely confuseswhata type is withwhereit lives.

In C#, the distinction between aclassand astructis not about stack vs heap. It is aboutvalue semantics versus reference semantics.

Here is the fundamental rule of the CLR memory model:

Value types live wherever their declaring container is allocated.

The stack is merely an implementation detail of method execution. A struct does not demand a spot on the stack. A struct simply demands that its raw data is stored directly inside its storage location, without an extra pointer indirection.

## Where Do Structs Actually Live?

Let us test the textbook rule against four everyday scenarios.

### 1. Local Variables Inside a Method

void
 
Calculate
()

{

 
int
 
count
 
=
 
42
;

 
Point
 
origin
 
=
 
new
 
Point
(
0
,
 
0
);

}

Enter fullscreen mode

Exit fullscreen mode

In this specific case, yes.countandoriginare local variables declared inside a standard method. They are stored inside the thread stack frame forCalculate. When the method exits, the stack pointer unwinds, and that memory is instantly reclaimed without touching the Garbage Collector.

This is the only scenario where the textbook rule happens to be true.

### 2. A Struct Inside a Class

Now consider what happens when a struct is a field inside a class:

public
 
struct
 
Health

{

 
public
 
int
 
Current
;

 
public
 
int
 
Max
;

}

public
 
class
 
Player

{

 
public
 
string
 
Name
;

 
public
 
Health
 
PlayerHealth
;

}

Enter fullscreen mode

Exit fullscreen mode

When you writevar player = new Player();,Playeris a reference type, so the CLR allocates a block of memory on theManaged Heap.

Where doesPlayerHealthlive? Does it somehow detach and float over to the stack?

No. The thread stack frame vanishes when your setup method finishes, but theplayerobject must survive.PlayerHealthlives100% on the Managed Heap, embedded directly inside the byte payload of thePlayerobject.

### 3. A Struct Inside an Array

What about an array of structs?

Point
[]
 
points
 
=
 
new
 
Point
[
1000
];

Enter fullscreen mode

Exit fullscreen mode

In .NET, all arrays are reference types (System.Array), which means arraysalways live on the Managed Heap.

BecausePointis a struct, the CLR does not allocate 1,000 separate objects or create 1,000 pointers. Instead, it allocates a single, contiguous block of memory on the heap large enough to hold all 1,000 points back to back.

All 1,000 structs are on the heap. Not a single one is on the stack.

### 4. Variables Captured in Lambdas or Async Methods

This is where developers get caught completely off guard:

public
 
async
 
Task
 
ProcessOrderAsync
()

{

 
int
 
retryCount
 
=
 
0
;
 
// Value type, right?

 
await
 
Task
.
Delay
(
100
);

 
retryCount
++;

 
Console
.
WriteLine
(
retryCount
);

}

Enter fullscreen mode

Exit fullscreen mode

BecauseProcessOrderAsyncis anasyncmethod, the C# compiler generates a hidden state machine class behind the scenes. That local variableretryCountis hoisted into a field on a compiler-generated heap class so its value survives across thread switches and task suspensions.

Thatintis living on the Managed Heap. The exact same hoisting happens whenever a local variable is captured inside a lambda expression or LINQ query.

## Memory Anatomy: Class vs Struct on 64-bit CLR

To understand why C# gives us bothclassandstruct, let us look at raw memory layouts on a 64-bit machine.

public
 
class
 
ClassPoint

{

 
public
 
int
 
X
;

 
public
 
int
 
Y
;

}

public
 
struct
 
StructPoint

{

 
public
 
int
 
X
;

 
public
 
int
 
Y
;

}

Enter fullscreen mode

Exit fullscreen mode

Both contain two 32-bit integers (XandY), which is 8 bytes of actual data (4 bytes each).

Look at what the CLR actually allocates:

### The Anatomy ofClassPoint

When you instantiatenew ClassPoint(), you pay for three distinct components:

1. The Reference Pointer (8 bytes): Stored in your local variable, holding the 64-bit memory address of the heap object.
2. The SyncBlockIndex (8 bytes): An object header word used by the CLR for thread synchronization locks and default hash codes.
3. The MethodTable Pointer (8 bytes): A pointer pointing to the runtime type descriptor forClassPoint(used for virtual method dispatch and type checking).
4. The Fields (8 bytes): 4 bytes forX, 4 bytes forY.

Total memory allocated:32 bytes.

To store 8 bytes of payload, the class requires 32 bytes of memory. That is a300% overhead. Furthermore, accessingpoint.Xrequires dereferencing an 8-byte pointer across memory.

### The Anatomy ofStructPoint

When you declareStructPoint point, there is:

* No SyncBlockIndex.
* No MethodTable Pointer.
* No reference pointer indirection.

Total memory allocated:Exactly 8 bytes.

The data IS the variable. When your CPU needspoint.X, it reads the value directly from the memory location. There is zero pointer chasing, zero metadata overhead, and zero Garbage Collector work needed to track it.

## The Boxing Trap: The Silent GC Killer

Because C# unifies its type system underSystem.Object, any value type can masquerade as a reference type.

That convenience comes with a hidden performance tax calledboxing.

int
 
value
 
=
 
42
;

object
 
boxed
 
=
 
value
;
 
// Silent boxing allocation

Enter fullscreen mode

Exit fullscreen mode

What just happened behind the scenes?

When you assignvalueto anobject(or pass it to an interface likeIComparable), the CLR cannot simply provide a stack pointer, because stack frames are temporary.

Instead, the CLR performs three hidden steps:

1. It allocates a brand new 24-byte object on the Managed Heap.
2. It writes theSystem.Int32MethodTable pointer and SyncBlockIndex into the header.
3. It copies the raw bits of42into the payload section of that heap object.

When you cast it back withint back = (int)boxed;, the CLR verifies the type and copies the bytes back out.

### Why You Should Care

If you box a number once during application startup, it does not matter. But if boxing happens inside a loop or hot path, your application will crawl:

var
 
list
 
=
 
new
 
System
.
Collections
.
ArrayList
();

for
 
(
int
 
i
 
=
 
0
;
 
i
 
<
 
1_000_000
;
 
i
++)

{

 
list
.
Add
(
i
);
 
// Every single add boxes an int!

}

Enter fullscreen mode

Exit fullscreen mode

That loop does not just store numbers. It createsone million distinct heap objects, burning roughly 24 Megabytes of heap memory and triggering Generation 0 garbage collections.

This is why C# 2.0 introduced Generics (List<T>). When you useList<int>, the CLR generates specialized machine code forint, storing raw 4-byte integers in a contiguous buffer without a single boxing allocation.

### The Interface Trap

Boxing can also occur quietly when invoking interface methods on structs:

public
 
struct
 
Counter
 
:
 
IIncrementable

{

 
public
 
int
 
Value
;

 
public
 
void
 
Increment
()
 
=>
 
Value
++;

}

void
 
Run
(
IIncrementable
 
item
)
 
// Passing Counter here BOXES it!

{

 
item
.
Increment
();

}

Enter fullscreen mode

Exit fullscreen mode

The moment you passCounterto a parameter typed asIIncrementable, the runtime boxes it on the heap. Even worse:item.Increment()modifies the boxed heap copy, leaving your originalCounteron the stack unchanged!

## Hardware Sympathy: Why C# Struct Arrays Outperform Pointer Chasing

Modern CPUs are incredibly fast, but reading from system RAM is comparatively slow. To bridge this latency gap, CPUs rely on multi-level hardware caches (L1, L2, L3).

When the CPU reads a byte from memory, it fetches an entire64-byte Cache Lineof adjacent memory, anticipating that your code will need neighboring data next.

Look at what happens when you iterate through an array of objects versus an array of structs:

### The Reference Model (Java, Python, C# Classes)

In languages like Java or Python (or when using an array of C# classes:Point[]), the array holds references. The actual objects are scattered across memory wherever the heap allocator placed them.

As your loop iterates:

1. You read pointer 1 and jump to heap address0x410. The CPU suffers acache missand halts for 100 to 200 clock cycles waiting for RAM.
2. You read pointer 2 and jump to heap address0x890. Another cache miss. Another 150 cycles wasted.
3. Every step is an unpredictable jump across memory. This is calledpointer chasing.

### The Value Type Model (C++, C# Structs)

Now look atStructPoint[]:

BecauseStructPointis a value type, the array holds the raw data inline:

[X0, Y0, X1, Y1, X2, Y2, X3, Y3, ...]

When the CPU loads the first point, the 64-byte hardware cache line automatically brings the next 7 points directly into L1 cache!

When your loop accesses points 2, 3, and 4, the data is already waiting in L1 cache memory, accessible in roughly 1 nanosecond. The CPU hardware prefetcher detects the sequential pattern and streams upcoming data into cache ahead of time.

Iterating over an array of structs is often5x to 10x fasterthan iterating over an array of classes, with zero garbage collection pressure.

## Modern C# Superpowers:Span<T>andref struct

Historically, structs gave great performance, but passing around slices of arrays or substrings forced developers to either allocate new objects or writeunsafepointer code.

That changed with the arrival ofSpan<T>andref struct.

### What IsSpan<T>?

Span<T>is a value type that acts as a safe, uniform window over any contiguous block of memory.

Under the hood,Span<T>contains just two fields:

public
 
readonly
 
ref
 
struct
 
Span
<
T
>

{

 
internal
 
readonly
 
ref
 
T
 
_reference
;
 
// Managed interior pointer

 
private
 
readonly
 
int
 
_length
;
 
// Element count

}

Enter fullscreen mode

Exit fullscreen mode

On a 64-bit machine,Span<T>is only 16 bytes. Yet it can point to:

* A slice of a standard managed array (byte[]on the heap).
* A chunk of stack-allocated memory (stackalloc byte[256]).
* Native unmanaged memory allocated viaMarshal.AllocHGlobal.

### Slicing Without Allocations

Consider parsing a date string like"2026-09-24":

// Classic approach: 3 new string allocations on the heap

string
 
date
 
=
 
"2026-09-24"
;

string
 
year
 
=
 
date
.
Substring
(
0
,
 
4
);
 
// Allocates new string

string
 
month
 
=
 
date
.
Substring
(
5
,
 
2
);
 
// Allocates new string

string
 
day
 
=
 
date
.
Substring
(
8
,
 
2
);
 
// Allocates new string

Enter fullscreen mode

Exit fullscreen mode

EverySubstringcall allocates a brand newstringon the Managed Heap.

Now look at how you do it with modern C#:

ReadOnlySpan
<
char
>
 
dateSpan
 
=
 
"2026-09-24"
;

ReadOnlySpan
<
char
>
 
yearSpan
 
=
 
dateSpan
.
Slice
(
0
,
 
4
);

ReadOnlySpan
<
char
>
 
monthSpan
 
=
 
dateSpan
.
Slice
(
5
,
 
2
);

ReadOnlySpan
<
char
>
 
daySpan
 
=
 
dateSpan
.
Slice
(
8
,
 
2
);

int
 
year
 
=
 
int
.
Parse
(
yearSpan
);

int
 
month
 
=
 
int
.
Parse
(
monthSpan
);

int
 
day
 
=
 
int
.
Parse
(
daySpan
);

Enter fullscreen mode

Exit fullscreen mode

Slicedoes not allocate memory on the heap. It simply creates a 16-byte window pointing to an offset within the existing string buffer.

Zero allocations. Zero GC pauses.

### Theref structGuarantee

How does C# make this safe? How does it ensure aSpan<T>never outlives the stack frame it points to?

The compiler enforces theref structrules:

* Aref structcanonly ever live on the stack.
* It cannot be boxed into anobject.
* It cannot be a field of a regularclassor regularstruct.
* It cannot be used acrossawaitpoints in async methods.
* It cannot be captured in a lambda expression.

The C# compiler acts as a static lifetime verifier, ensuring the reference can never outlive its memory. You get C++ pointer speed with complete memory safety.

## Practical Rules for Production Code

How should you design your types in everyday development? Here are four practical guidelines:

### 1. Default toclass, Usestructfor Atomic Values

Do not blindly make everything a struct. Passing a 64-byte struct by value copies all 64 bytes on every method call, which is far more expensive than copying an 8-byte reference pointer.

Use astructwhen:

* The type represents a single atomic value (coordinates, currency, vectors).
* The total size is small (generally 16 to 24 bytes or fewer).
* The instances are short-lived or stored in large contiguous arrays.
* You do not require inheritance.

### 2. Always Make Structs Immutable (readonly struct)

Mutable structs cause notorious bugs. When you pass a struct to a method or access it through a property, C# creates a defensive copy:

// BAD: Mutable struct

public
 
struct
 
MutableVector

{

 
public
 
int
 
X
;

 
public
 
void
 
SetX
(
int
 
newX
)
 
=>
 
X
 
=
 
newX
;

}

public
 
MutableVector
 
Position
 
{
 
get
;
 
set
;
 
}

// Calling this modifies a temporary copy!

Position
.
SetX
(
100
);
 

// Position.X is STILL 0!

Enter fullscreen mode

Exit fullscreen mode

Always declare structs asreadonly struct:

public
 
readonly
 
struct
 
Vector2

{

 
public
 
int
 
X
 
{
 
get
;
 
}

 
public
 
int
 
Y
 
{
 
get
;
 
}

 
public
 
Vector2
(
int
 
x
,
 
int
 
y
)
 
=>
 
(
X
,
 
Y
)
 
=
 
(
x
,
 
y
);

}

Enter fullscreen mode

Exit fullscreen mode

Thereadonlykeyword prevents accidental mutation and eliminates defensive copying.

### 3. UseinParameters for Larger Readonly Structs

If a readonly struct is somewhat larger (for example, 32 or 48 bytes), avoid copying overhead by passing it with theinmodifier:

public
 
static
 
double
 
CalculateDistance
(
in
 
Matrix4x4
 
a
,
 
in
 
Matrix4x4
 
b
)

{

 
// Passed by readonly reference: 8-byte pointer passed under the hood,

 
// with compiler-enforced immutability!

}

Enter fullscreen mode

Exit fullscreen mode

### 4. ImplementIEquatable<T>on Custom Structs

Default struct equality (point1.Equals(point2)) uses reflection insideValueType.Equalsto compare fields, which is slow and triggers boxing.

ImplementingIEquatable<T>provides fast, zero-allocation equality:

public
 
readonly
 
struct
 
Point
 
:
 
IEquatable
<
Point
>

{

 
public
 
int
 
X
 
{
 
get
;
 
}

 
public
 
int
 
Y
 
{
 
get
;
 
}

 
public
 
Point
(
int
 
x
,
 
int
 
y
)
 
=>
 
(
X
,
 
Y
)
 
=
 
(
x
,
 
y
);

 
public
 
bool
 
Equals
(
Point
 
other
)
 
=>
 
X
 
==
 
other
.
X
 
&&
 
Y
 
==
 
other
.
Y
;

 
public
 
override
 
bool
 
Equals
(
object
?
 
obj
)
 
=>
 
 
obj
 
is
 
Point
 
other
 
&&
 
Equals
(
other
);

 
public
 
override
 
int
 
GetHashCode
()
 
=>
 
HashCode
.
Combine
(
X
,
 
Y
);

}

Enter fullscreen mode

Exit fullscreen mode

## Quick Reference: Value Types vs Reference Types

Characteristic

struct
 (Value Type)

class
 (Reference Type)

Where it lives

Wherever its container lives (Stack, Heap, or Inlined)

Always allocated on Managed Heap

Variable content

The raw data itself

An 8-byte memory pointer

Assignment behavior

Copies the entire value

Copies only the pointer reference

Object Header Overhead

Zero bytes

16 bytes (SyncBlockIndex + MethodTable)

Garbage Collector Burden

Zero (unless boxed or inside a class)

Tracked by GC, collected during GC cycles

Array Memory Layout

Contiguous block of raw values

Array of pointers pointing to scattered objects

Inheritance Support

Interfaces only

Full class inheritance hierarchy

Default Equality

Compares fields (via reflection unless overridden)

Compares reference identity

## Putting It Into Perspective

When you step back and look at modern C#, one design philosophy shines through:giving developers high-level productivity without taking away hardware efficiency.

Languages like Python and JavaScript abstract memory away entirely, trading throughput for developer convenience. Languages like C and C++ give you raw hardware control, but demand manual memory management.

C# proves you do not have to choose between memory safety and speed. By pairing value types with reified generics and stack-only types likeSpan<T>, you can write elegant, readable code that runs with hardware sympathy.

The next time someone in an interview or pull request review says that "structs live on the stack," you will know exactly how the Common Language Runtime actually lays out those bytes.

Have you ever tracked down a subtle bug caused by a mutable struct or unexpected boxing in your application logs? Or have you refactored a critical loop withSpan<T>and watched your memory allocations drop to zero? I would love to hear your experiences and war stories in the comments below.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse