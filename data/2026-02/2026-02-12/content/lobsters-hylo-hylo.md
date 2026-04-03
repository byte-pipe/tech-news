---
title: Hylo | Hylo
url: https://hylo-lang.org/
site_name: lobsters
content_file: lobsters-hylo-hylo
fetched_at: '2026-02-12T06:00:25.877826'
original_url: https://hylo-lang.org/
date: '2026-02-12'
description: All in on Value Semantics and Generic Programming
tags: plt
---

# Hylo


A Systems Programming Language
All in on Value Semantics and Generic Programming



 Read Our Introduction


 Watch Dave's Talk at C++ On Sea











## Join the Hylo Community



Connect with developers and contributors






Slack



GitHub Discussions





## Achievements

Section titled “Achievements”



MVS & Theory


* Extending Swift’s subscripts with inout projections
* Method bundles
* Structured concurrency made easy: thread hopping, no function coloring
* Expressingdouble linked lists with value semanticsis safe and faster than doing it with reference semantics.




Compiler


* Compilationusing LLVM
* Novel techniques for compiling generics with coherence
* Caching and serialization of the compiler’s program state
* C interopresearch




Standard Library


* See the documentationof the current implementation with some fundamental traits and data structures.
* Positionless Collection Algorithms
* rs-stl: A Rust port of the C++ STL algorithms for improved generic programming




Developer Experience


* VSCode extensionwith syntax highlighting and code execution
* Documentation compiler
* Language Serverprototype




Compiler DevOps


* Development Containerssupport - easy to get started
* Support SPM/CMake, Ninja/Xcode, Windows/Linux/macOS
* Test generation compiler plugin
* Pre-builtHylo development toolchainDocker images
* Compiler written in Swift 6.2



## Research Around Hylo

Section titled “Research Around Hylo”




Who Owns the Contents of a Doubly-Linked List?


PDF


Dimi Racordon

2025-09


High-Fidelity C Interoperability in Hylo


PDF


Ambrus Tóth

2025-06


Debugging Hylo


PDF


Tudor-Stefan Magirescu

2025-06


On the State of Coherence in the Land of Type Classes


PDF


Dimi Racordon, Eugene Flessele, Cao Nguyen Pham

2025-02


Type Checking with Rewriting Rules



Dimi Racordon

2024-10


Use Site Checking Considered Harmful



Dimi Racordon, Benjamin Chung

2024-10


Method Bundles



Dimi Racordon, Dave Abrahams

2024-10


Borrow checking Hylo


PDF


Dimi Racordon, Dave Abrahams

2023-10


The Val Object Model


PDF


Dave Abrahams, Sean Parent, Dimi Racordon, David Sankel

2022-10


Existentialize Your Generics


PDF


Dimi Racordon, Matt Bovel, Hamza Remmal

2022-06


Implementation Strategies for Mutable Value Semantics


PDF


Dimi Racordon, Denys Shabalin, Daniel Zheng, Dave Abrahams, Brennan Saeta

2022


Toward a Lingua Franca for Memory Safety


PDF


Dimi Racordon, Aurélien Coet, Didier Buchs

2022


Native Implementation of Mutable Value Semantics


PDF


Dimi Racordon, Denys Shabalin, Daniel Zheng, Dave Abrahams, Brennan Saeta

2021-06


A Formal Definition of Swift's Value Semantics


PDF


Dimi Racordon

2020-11




Are you interested in research collaboration — as a student, professor, or independent contributor?
Learn about ouropen research topics, or suggest a new topic!

## Talks

Section titled “Talks”






Concurrency Hylomorphism


Lucian Radu Teodorescu

ACCU

2024-07




Keynote

Hylo: The Safe Systems and Generic-programming Language Built on Value Semantics


Dave Abrahams

C++ on Sea

2024-07




⚡

HyloDoc: A Documentation Compiler for Hylo


Ambrus Tóth

C++ on Sea

2024-06




Borrow checking Hylo


Dimi Racordon

IWACO

2023-05




Concurrency Approaches: Past, Present, and Future


Lucian Radu Teodorescu

ACCU

2023-04




Val: A Safe Language to Interoperate with C++


Dimi Racordon

CppCon

2022-09




Value Semantics: Safety, Independence, Projection, & Future of Programming


Dave Abrahams

CppCon

2022-09




⚡

An Object Model for Safety and Efficiency by Definition


Dave Abrahams

CppNorth

2022-07




Keynote

A Future of Value Semantics and Generic Programming Part 1


Dave Abrahams

C++Now

2022-05




Keynote

A Future of Value Semantics and Generic Programming Part 2


Dave Abrahams, Dimi Racordon

C++Now

2022-05




Structured Concurrency


Lucian Radu Teodorescu

ACCU

2022-04




## Podcasts

Section titled “Podcasts”






 Rust & Safety at Adobe with Sean Parent


Sean Parent

ADSP #160

2023-12-15




 Sean Parent on Hylo! (Part 2)


Sean Parent

ADSP #138

2023-07-14




 Sean Parent on Hylo (vs Rust)!


Sean Parent

ADSP #137

2023-07-07




 Val and Mutable Value Semantics


Dimi Racordon

CppCast #352

2023-01-20




# Working Examples

Section titled “Working Examples”

Even though the compiler and standard library are still in their early stages, we can already show some advanced examples
of Hylo code that you can try out onCompiler Explorer.

#### Subscripts - A Safe Projection Mechanism

Section titled “Subscripts - A Safe Projection Mechanism”

https://godbolt.org/z/Mzz17c5z1

Geometry.hylo
/// The orientation of a 2D vector.
public

type
Angle: Deinitializable {


/// The value of `self` in radians.

public

var
 radians: Float64


/// Creates an instance with its value in radians.

public
 memberwise init


/// Creates an instance with its value in degrees.

public
 init(degrees: Float64) {

&
self
.radians = degrees * Float64.pi() /
180
.
0

}


/// The value of `self` in degrees.

public

property
 degrees: Float64 {

let
 { radians *
180
.
0
 / Float64.pi() }

inout
 {

var
 d = radians *
180
.
0
 / Float64.pi()

yield
 &d

&
self
.radians = d * Float64.pi() /
180
.
0

}

}
}

public

fun

main
() {

var
 a = Angle(radians: .pi())


inout
 d = &a.degrees

precondition(d ==
180
.
0
)

&d =
0
.
0

precondition(a.radians ==
0
.
0
)
}

#### Sink Methods - Capability for Deinitializing

Section titled “Sink Methods - Capability for Deinitializing”

https://godbolt.org/z/cY7T5jPEc

SinkMethods.hylo
/// A computer that must be explicitly shut down using a sink method.
type
Computer {

public

var
 ram: String

public
 memberwise init


public

fun

shutdown
()
sink
 -> Void {

print(
"Key received, shutting down... Memory contents was: "
)

print(
self
.ram)


/// Sinking all parts

_ =
self
.ram

}
}

fun

test1
() {

var
 computer = Computer(ram:
"Important data"
)
}

Cannot deinit `computer`

fun

test2
() {

var
 computer = Computer(ram:
"Important data"
)

if
 random_bool() {

computer.shutdown()

}
}

Cannot deinit `computer` [when `if` not entered]

fun

test3
() {

var
 computer = Computer(ram:
"Important data"
)

while
 random_bool() {

computer.
shutdown()

Use of consumed object [after first iteration]

}
}

Cannot deinit `computer` [when `while` not entered]

fun

random_bool
() -> Bool {

return

false

// Generated using a fair dice roll % 2.
}

CustomMove.hylo
type
A: Deinitializable {

public

var
 witness: Int

public

var
 x: Int

public
 init(x:
sink
 Int) {

&
self
.x = x

&
self
.witness =
0

}
}

conformance
 A: Movable {

public

fun

take_value
(from source:
sink

Self
) {

set
 {

&
self
.x = source.x

&
self
.witness =
0

}

inout
 {

&
self
.x = source.x

&
self
.witness +=
1

}

}
}

public

fun

main
() {

var
 s = A(x:
1
)

&s = A(x:
2
)

&s = A(x:
2
)


precondition(s.x ==
2
)

precondition(s.witness ==
2
)
}

See more examples in thecompiler test suite.
