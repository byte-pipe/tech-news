---
title: 'GitHub - swoole/typephp: Compile PHP to Native Binaries · GitHub'
url: https://github.com/swoole/typephp
site_name: github
content_file: github-github-swooletypephp-compile-php-to-native-binarie
fetched_at: '2026-08-28T21:20:54.532308'
original_url: https://github.com/swoole/typephp
author: swoole
description: Compile PHP to Native Binaries. Contribute to swoole/typephp development by creating an account on GitHub.
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 swoole

 

/

typephp

Public

* NotificationsYou must be signed in to change notification settings
* Fork38
* Star794

 
 
 
master
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

1,541 Commits
1,541 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
benchmark
benchmark
 
 
bin
bin
 
 
completions
completions
 
 
docs
docs
 
 
examples
examples
 
 
phpunit
phpunit
 
 
src
src
 
 
tests
tests
 
 
wasm
wasm
 
 
.clang-format
.clang-format
 
 
.gitignore
.gitignore
 
 
.php-cs-fixer.dist.php
.php-cs-fixer.dist.php
 
 
LICENSE
LICENSE
 
 
README-CN.md
README-CN.md
 
 
README.md
README.md
 
 
cli.php
cli.php
 
 
composer.json
composer.json
 
 
package.php
package.php
 
 
phpstan-bootstrap.php
phpstan-bootstrap.php
 
 
phpstan.neon
phpstan.neon
 
 
phpunit.xml
phpunit.xml
 
 
project.yml
project.yml
 
 
run-tests.php
run-tests.php
 
 
swoole-logo.ico
swoole-logo.ico
 
 
swoole-logo.svg
swoole-logo.svg
 
 
View all files

## Repository files navigation

English|简体中文

# TypePHP

A native AOT compiler for PHP

Compile PHP source code into native machine code ahead of time — producing
native executables, PHP extensions, and shared libraries — while keeping
the PHP syntax you already know.

## What is TypePHP?

TypePHP is an Ahead-Of-Time (AOT) compiler that translates PHP source code into
C++ and then into native machine code. Unlike a bytecode cache or a VM, it does
not interpret opcodes at runtime: it generates optimized native binaries that
run directly on the CPU.

It keeps familiar PHP syntax and adds compile-time type information, so the
compiler can emit fast, statically-typed C++ for hot paths. Dynamic PHP values,
internal functions, reflection, and object metadata continue to interoperate
with the Zend runtime through PHPX; user functions are not executed as Zend
opcodes after they have been compiled.

TypePHP iswritten entirely in PHPand isfully self-hosting: thetpccompiler binary is built by compiling the compiler's own PHP source code with
TypePHP. The bootstrap chain is pure PHP — no C or C++ glue in the compiler
itself.

TypePHP is under active development. It intentionally supports a defined,
testable subset of PHP rather than claiming drop-in compatibility with every
dynamic PHP program. ReadCompatibility modeland theincompatible-feature listbefore adopting
it for an existing application.

## How it works

PHP source + .stub.php declarations + optional C/C++ sources
 │
 ▼
 parse, validate, and collect declarations
 │
 ▼
 lower function bodies and constants to C++17
 │
 ▼
 native compiler + reusable object/PCH caches
 │
 ▼
 executable | PHP extension | shared library | WASI component

The prepare phase builds the complete symbol model without allocating runtime
cache IDs. Constants and declaration defaults retain their AST until the
convert phase, where they are lowered after all project symbols are known.
This two-phase design keeps multi-file and self-hosted builds deterministic.

## Features

* Self-hosting, written in PHP— the TypePHP compiler is implemented
entirely in PHP and bootstraps itself:tpccompiles the compiler's own
source into a native binary.
* True AOT compilation— PHP is lowered to C++17, then to native machine
code. No interpreter, no opcode cache, no JIT warm-up.
* Three native build modes— build a nativebinexecutable, a loadable
PHPextextension, or a reusablelibshared library from the same codebase.
* Native type system—int,float, andboolmap directly to C++
scalar types (int64_t,double,bool) for orders-of-magnitude speedups
on numeric code.
* High-precision numerics—bigInt(GMP),decimal(libmpdec), andbigFloat(MPFR), with typed operators and method APIs.
* Strongly-typed containers—std::array,std::vector,std::map, andstd::ordered_mapwith compile-time element types; up to10×faster than
PHP arrays and on par with C++std::vector.
* Universal methods— call methods directly on primitives
($s->upper(),$arr->contains(),$big->mul(2)); statically-known calls
are resolved directly at compile time.
* Mixed C++ / PHP— call C++ functions from PHP (and vice versa) for
performance-critical kernels.
* Compile-time functions & keywords—any(),refval(),objval(),expected(),unexpected(), plustoInt(),toString(),toArray()and
friends.
* Compile-time safety—#[Immutable]read-only contracts and#[ArrayDef]array-shape metadata, checked at compile time with zero runtime cost.
* Compile-time code generation—#[Getter],#[Setter],#[With],#[Constructor],#[Printer], and#[Arrayable]generate type-safe methods
from property declarations.
* Modern PHP support— PHP 8.4 property hooks, asymmetric visibility,
PHP 8.5clone()-with, and(void)discard expressions.
* Cross-platform & WASM— Linux, Windows, and macOS targets for x64 and
ARM64, plus WASI 0.2 and browser (Jco) output.
* Python bridge— generate IDE helpers for Python modules and convert
Python scripts to TypePHP.

## Why TypePHP?

TypePHP AOT

Opcode cache (OPcache)

JIT (PHP 8+)

Compilation target

Native machine code

Bytecode

Machine code (trace)

Startup / warm-up

None (already compiled)

Per-process warm-up

JIT warm-up

Type-driven optimization

Compile-time, full-program

None

Limited, trace-based

Native executable output

Yes

No

No

Source code protection

Compiled to machine code

Bytecode (reversible)

Bytecode (reversible)

Deterministic performance

Yes

No

No

Strengths over plain PHP:

* Near-native performance.Numeric and container-heavy hot paths compile
down to the same machine code a C++ program would produce. See thebenchmarkbelow.
* Source protection.Your source is compiled away — shipped artifacts are
native binaries, not readable PHP files.
* Native process entry.Binary mode starts directly from a native
executable and does not require the PHP CLI or a separate interpreter
process. The executable still embeds/links PHPX,libphp, and any configured
native libraries, which must be available in the deployment package.
* Gradual typing that actually pays off.Adduse native_types,std::containers, and type declarations only where performance matters; the rest
stays ordinary PHP.
* Zend ecosystem interop.Extension mode loads as a standard PHP extension,
and projects can call supported internal functions and require other Zend
extensions explicitly.

## Requirements

* PHP 8.4 – 8.5CLI, development headers, andphp-config
* The matchingPHP embed library(libphp.soorlibphp.dylib) for binary/shared-library
builds on Unix-like systems
* GCC 9+(or Clang) withC++17
* CMake 3.24+
* Composer 2
* High-precision math libraries:GMP,MPFR(libmpdec is bundled with PHPX)

#
 Ubuntu/Debian

sudo apt install build-essential cmake pkg-config libgmp-dev libmpfr-dev

#
 RHEL/CentOS/Fedora

sudo dnf install gcc gcc-c++ cmake pkgconf-pkg-config gmp-devel mpfr-devel

#
 Arch Linux

sudo pacman -S base-devel cmake pkgconf gmp mpfr

GMP powersbigIntand MPFR powersbigFloat. Thedecimaltype is backed
by libmpdec, which is bundled with PHPX — no separate install required.

Linux x64 is the primary development and full-test CI platform. The compiler
also has Windows, macOS, ARM64, and WASI backends; availability of PHP embed,
toolchain, and third-party libraries still determines which target can be
built on a given host.

Native release assets are built with the latest PHP 8.5 ZTS release. TypePHP
publishes Linux x64, Linux ARM64, macOS ARM64, and Windows x64 packages. Native
NTS and 32-bit x86 packages are not provided. Linux and macOS archives contain
the compiler and production Composer dependencies, while the Windows archive
contains the complete matching PHP/PHPX runtime and SDK.

## Installation

### Via Composer

composer require --dev swoole/typephp

Then compile your project:

vendor/bin/tpc.php project.yml

When working inside the TypePHP source repository, use the local entry point
instead:

bin/tpc.php project.yml

### From source

git clone https://github.com/swoole/typephp.git

cd
 typephp
composer install
php bin/tpc.php --help

PHPX_HOMEmay point to a separate PHPX checkout or installation.PHP_HOMEmay point to the PHP embed prefix; it must containbin/php-config, PHP headers,
andlib/libphp.soon Unix-like systems.

### Buildinglibphp.so

Binary and shared-library builds require PHP'sembedSAPI. Iflibphp.sois
missing on Linux,tpc.phpcan interactively download the PHP source and build
it for you. A PHP extension build resolves Zend symbols from the host SAPI and
must not load a secondlibphp. SeeAutomatic libphp.so build.

## Quick Start

Createhello.php:

<?php

function
 
main
(): 
void

{
 
echo
 
"
Hello World!
\n"
;
 
var_dump
(
PHP_VERSION
);
 
var_dump
(
php_uname
());
}

Compile and run it:

bin/tpc.php hello.php
./hello

Example output (the exact PHP version and platform strings depend on the linked
runtime):

Hello World!
string(5) "8.x.x"
string(16) "Linux ..."

Binary mode requires a globalmain()function. It may be declared with no
parameters, or asmain(int $argc, array $argv)to receive command-line
arguments, and must returnvoid. Top-level executable statements are not
allowed; executable code belongs in a function or method.

## Compilation Modes

TypePHP supports three build modes, selected with-m/--mode:

Mode

Flag

Output

Needs 
main()

Typical use

Binary

-m bin
 (default)

Executable

Yes

CLI tools, long-running services, standalone apps

Extension

-m ext

PHP 
.so
 / 
.dll

No

Loading compiled functions/classes into a PHP SAPI

Library

-m lib

Shared library plus generated 
.stub.php

No

Reusing a compiled TypePHP API from another project

#
 Binary (default)

bin/tpc.php app.php -o myapp

#
 PHP extension

bin/tpc.php extension/ -m ext -o my_extension

#
 Shared library; also generates mylib.stub.php

bin/tpc.php lib/ -m lib -o mylib

SeeCompilation modesfor details.

## Project configuration

For multi-file projects, keep repeatable build settings inproject.yml:

name
: 
myapp

mode
: 
bin

php-version
: 
"
8.5
"

optimize
: 
2

job
: 
8

build-dir
: 
build

cxx-std
: 
c++17

sources
:
 - 
src

 - 
cpp-src

 - 
path
: 
src/php85

 
if
: 
PHP_VERSION_ID >= 80500

 - 
path
: 
src/windows

 
if
: 
PHP_OS_FAMILY == "Windows"

ignore
:
 - 
src/experimental

include-paths
:
 - 
native/include

defines
:
 - 
FEATURE_FAST_PATH=1

link-paths
:
 - 
native/lib

link-libs
:
 - 
curl

#
 Zend extension requirements, not native linker libraries.

#
 `extension-dependencies` is the equivalent long name; do not use both.

ext-deps
:
 - 
pdo_mysql

 - 
curl

Paths are resolved relative to the YAML file. A source entry may be a file or
directory; conditional entries supportPHP_VERSION,PHP_VERSION_ID, andPHP_OS_FAMILY. CLI arguments override their YAML counterparts. Native linker
dependencies belong inlink-libs;ext-depswritesZEND_MOD_REQUIREDentries so Zend can reject loading when a required PHP extension is missing.

The build directory contains generated C++, dependency objects, and the
precompiled-header cache. Reusing it makes incremental builds much faster;
use--forceonly when the reusable PHPX objects must be rebuilt.

SeeCompiler CLIfor all project keys and command-line
precedence rules.

## Compatibility model

TypePHP follows PHP syntax and runtime behavior where they are compatible with
ahead-of-time compilation, but it also makes several deliberate restrictions:

* global scope is declaration-only; executable statements must be inside a
function or method;
* binary mode has a strictmain()signature;
* use native_typesopts scalar declarations into fixed native storage, so a
value cannot later change to an incompatible type;
* statically-known calls and properties are compiled directly, while supported
dynamic operations use PHPX/Zend runtime fallbacks;
* .stub.phpfiles declare C++ or imported-library APIs and must contain empty
bodies;#[Native]classes are not permitted in stub files;
* some highly dynamic reference, declaration, closure, and reflection patterns
remain intentionally unsupported.

The compatibility boundary is part of the public contract and has both
positive and negative tests. ConsultIncompatible PHP featuresfor the current,
specific list instead of assuming that absence from this README means support.

## Compile-time attributes and code generation

TypePHP consumes its built-in code-generation attributes while lowering the
class. The generated methods retain the declared property types and take part
in the same conflict, inheritance, and final-method checks as explicitly
declared methods.

Attribute

Target

Generated API

#[Getter]

Instance property, including a promoted property

public function getName(): T

#[Setter]

Mutable instance property, including a promoted property

public function setName(T $name): void

#[With]

Mutable instance property, including a promoted property

public function withName(T $name): static
; clones the object, updates the clone, and returns it

#[Constructor]

Declared instance property

Adds the property to a generated public 
__construct()

#[Printer]

Named class

public function __toString(): string

#[Arrayable]

Named class

public function toArray(): array

<?php

#[Printer(fields: [
'
id
'
, 
'
name
'
])]
#[Arrayable(fields: [
'
id
'
, 
'
name
'
])]

final
 
class
 User
{
 #[Constructor, Getter, With]
 
public
 
int
 
$
id
;

 #[Constructor, Getter, Setter]
 
public
 
string
 
$
name
 = 
'
guest
'
;
}

function
 
main
(): 
void

{
 
$
user
 = 
new
 
User
(
7
);
 
$
user
->
setName
(
'
Alice
'
);

 
$
copy
 = 
$
user
->
withId
(
8
);
 
echo
 
$
user
->
getId
(); 
// 7

 
echo
 
$
copy
->
getId
(); 
// 8

 
echo
 
$
user
; 
// User(id=7, name=Alice)

 
echo
 
$
user
->
toArray
()[
'
name
'
];
}

Withoutfields,#[Printer]and#[Arrayable]use the class's own public
instance properties. The positional form, such as#[Arrayable(['id'])], is
equivalent to#[Arrayable(fields: ['id'])].

#[Getter],#[Setter], and#[With]cannot target static properties or
properties with hooks.#[Setter]and#[With]additionally reject readonly
properties.#[Constructor]cannot be used when the class already declares__construct(), and required constructor properties must precede properties
with defaults. A generated method name that conflicts with a declared or
inherited final method is a compile-time error.

## Examples

### 1. Native types — compile-time numeric speedup

<?php

use
 
native_types
;

function
 
fib
(
int
 
$
n
): 
int

{
 
if
 (
$
n
 == 
1
 || 
$
n
 == 
2
) {
 
return
 
1
;
 }
 
return
 
fib
(
$
n
 - 
1
) + 
fib
(
$
n
 - 
2
);
}

function
 
main
(
int
 
$
argc
, 
array
 
$
argv
): 
void

{
 
$
n
 = (
int
)
$
argv
[
1
];
 
$
begin
 = 
microtime
(
true
);
 
echo
 
fib
(
$
n
) . 
"\n"
;
 
echo
 
"
Time: 
"
 . (
microtime
(
true
) - 
$
begin
) . 
"\n"
;
}

bin/tpc.php fib.php -O3 -o fib
./fib 30

Withuse native_types,intvariables become C++int64_tand arithmetic
compiles to plain CPU instructions instead of ZendVM calls.

### 2. High-precision numerics

<?php

declare
(strict_types=
1
);

use
 
native_types
;

function
 
main
(): 
void

{
 
// 54-digit integer — automatically detected and stored as bigInt

 
$
a
 = std::
bigInt
(
"
123456789012345678901234567890123456789012345678901234
"
);
 
$
b
 = std::
bigInt
(
"
987654321098765432109876543210987654321098765432109876
"
);

 
echo
 
$
a
->
add
(
$
b
)->
toString
() . 
"\n"
; 
// exact, no overflow

 
// Exact decimal arithmetic — no binary floating-point error

 
$
c
 = std::
decimal
(
"
0.1
"
)->
add
(std::
decimal
(
"
0.2
"
));
 
echo
 
$
c
->
toString
() . 
"\n"
; 
// "0.3"

 
// 256-bit floating point

 
$
pi
 = std::
bigFloat
(
"
3.14159265358979323846264338327950288419716939937510
"
);
 
echo
 
$
pi
->
mul
(
2
)->
toString
() . 
"\n"
;
}

SeeHigh-precision typesandNative types.

### 3. Strongly-typed containers

<?php

use
 
native_types
;

function
 
main
(): 
void

{
 
$
vector
 = std::
vector
(Type::Int);

 
$
vector
[] = 
1
;
 
$
vector
[] = 
2
;
 
$
vector
[] = 
3
;

 
$
sum
 = 
0
;
 
foreach
 (
$
vector
 
as
 
$
value
) {
 
$
sum
 += 
$
value
;
 }

 
echo
 
$
sum
 . 
"\n"
; 
// 6

 
echo
 
$
vector
[
1
] . 
"\n"
; 
// 2

 
// key-value map with fixed key/value types

 
$
map
 = std::
ordered_map
(Type::String, Type::Int);
 
$
map
[
"
a
"
] = 
1
;
 
$
map
[
"
b
"
] = 
2
;
}

SeeStd containers.

### 4. Universal methods

<?php

function
 
main
(): 
void

{
 
$
s
 = 
"
hello world
"
;
 
echo
 
$
s
->
length
() . 
"\n"
; 
// strlen()

 
echo
 
$
s
->
upper
() . 
"\n"
; 
// strtoupper()

 
echo
 
$
s
->
substr
(
0
, 
5
) . 
"\n"
; 
// substr()

 
$
arr
 = [
1
, 
3
, 
5
, 
7
, 
9
];
 
echo
 
$
arr
->
count
() . 
"\n"
; 
// count()

 
var_dump
(
$
arr
->
contains
(
3
)); 
// in_array()

 
$
big
 = std::
bigInt
(
"
12345678901234567890
"
);
 
echo
 
$
big
->
mul
(
2
)->
toString
() . 
"\n"
;
}

Method calls on primitives are resolved at compile time into direct C/C++
function calls — no vtable lookup, no reflection, no runtime dispatch. SeeUniversal methods.

### 5. Mixed C++ / PHP

Write performance-critical kernels in C++ and call them from PHP:

//
 math.cpp

#
include
 
<
phpx.h
>

using
 
namespace
 
php
;

Int 
php_fast_sum
(Int a, Int b) {
 
return
 a + b;
}

<?php

// math.stub.php — declares the C++ function signature

function
 
fast_sum
(
int
 
$
a
, 
int
 
$
b
): 
int
 {}

<?php

function
 
main
(): 
void

{
 
echo
 
fast_sum
(
3
, 
4
) . 
"\n"
; 
// 7

}

Addmath.cpp,math.stub.php, and the calling PHP source to the same project
configuration. Thephp_C++ symbol prefix is the TypePHP callable ABI; stub
functions provide type metadata only and must not contain an implementation.

SeeMixed C++/PHP.

## Benchmark

### PHP language benchmarks (from php-src)

TypePHP runs the officialbench.phpandmicro_bench.phplanguage
benchmarks that ship with the PHP source tree, compiled with-O3:

Benchmark

Interpreted PHP

TypePHP AOT (
-O3
)

Speedup

bench.php
 (total)

5.034 s

0.603 s

~8×

micro_bench.php
 (total)

13.045 s

2.021 s

~6.5×

Both benchmarks measure core PHP language performance — function calls, object
property access, array/hash access, string handling, control flow, and more.
The checked-in workloads arebenchmark/bench.phpandbenchmark/micro_bench.php. Additional focused
performance regressions live in the samebenchmark/directory.

These numbers are a project measurement snapshot, not a performance guarantee.
PHP version, compiler, CPU, optimization flags, and enabled extensions can all
change the result; compare on the same machine with the same workload before
making deployment decisions.

### std::array vs PHP array

A 10000×100000 element update loop, comparing PHP arrays against TypePHP'sstd::arrayand native C++:

Implementation

Time

PHP array (JIT)

67.6 s

std::array
 (TypePHP AOT)

6.4 s

C++ 
std::vector

6.2 s

std::arrayis roughly10× fasterthan PHP arrays and performs
close to the hand-written C++ result in this workload. See the benchmark inStd containers.

## Command Line

bin/tpc.php 
<
file
|
dir
|
project.yml
>
 [options] [-- program-args...]

Common usage:

#
 Compile a single file

bin/tpc.php app.php

#
 Optimize and run, passing args to the program after `--`

bin/tpc.php app.php -O3 -r -- --flag value

#
 Compile a project defined in project.yml

bin/tpc.php project.yml -O2 -j 8

#
 Build a PHP extension

bin/tpc.php extension/ -m ext -o my_extension

#
 Only generate C++ (skip compile & link)

bin/tpc.php app.php --dry --build-dir /tmp/typephp-build

#
 Compile to WASI 0.2

bin/tpc.php --wasm app.php

#
 Compile for the browser (requires jco)

bin/tpc.php --wasm=browser app.php

Key options:

Option

Description

-O <0-3>

Optimization level (default 
0
)

-d
, 
--debug

Debug build with symbols and source tracking

-o
, 
--output <file>

Output file name

-m
, 
--mode <bin|lib|ext>

Build mode (default 
bin
)

-r
, 
--run

Run after a successful build

-j
, 
--job <num>

Parallel compile jobs (default 
4
)

-f
, 
--force

Rebuild reusable PHPX objects instead of using the cache

--build-dir <dir>

Directory for generated C++ and intermediates

--dry

Generate C++ only, skip compile and link

--php-version <8.4|8.5>

PHP syntax version to accept

--cxx-std <ver>

C++ standard (e.g. 
c++17
, 
c++20
)

--march <arch>

Target instruction set (e.g. 
native
)

--target-platform <triple>

Cross-compilation target triple

--lto

Enable link-time optimization

--sanitize <type>

Enable a sanitizer (e.g. 
address
)

--profile

Enable Linux gperftools profiling

--format

Format generated C++ with clang-format

--no-literal-strings

Disable the literal-string table optimization

--no-progress
, 
--no-color

CI-friendly output controls

-I
, 
-D
, 
-L
, 
-l

Repeatable native include, define, library path, and library options

Runbin/tpc.php --helpfor the authoritative, up-to-date list. SeeCompiler CLIfor details, including Bash completion:

source
 
<(
./tpc --generate-completion=bash
)

## Troubleshooting

* libphp.so/libphp.dylibis missing:install/build the matching PHP embed SAPI, setPHP_HOME, or letbin/tpc.phpoffer the interactive Linux installer.
* PHPX cannot be found:setPHPX_HOMEto a PHPX installation containinginclude/andlib/libphpx.so(or the platform equivalent), then build PHPX
before compiling the project.
* Startup crashes or ABI errors:the PHP headers,php-config,libphp,
and loaded extension ABI must agree on the PHP version and ZTS/NTS mode. Do
not mix artifacts from different PHP builds.
* Incremental builds are unexpectedly slow:keep a stable--build-dirso
object and PCH caches can be reused. When an external test runner already
runs several tests concurrently, avoid multiplying that concurrency by an
unnecessarily largetpc -jvalue.
* A project compiles withbin/tpc.phpbut fails withtpc:reproduce with
the self-hosted compiler. Bootstrap execution can expose dynamic-call or ABI
paths that the PHP-hosted compiler does not exercise.

## Python bridge

TypePHP ships a Python tool submodule that shares thetpcentry point:

#
 Generate IDE helpers for Python modules

./tpc --gen-python-helper math
./tpc --gen-python-helper numpy --output-dir .ide-helper

#
 Convert a Python script to TypePHP

./tpc --convert-python-to-php script.py 
>
 script.php

SeePython tool submodule.

## Development and testing

Install development dependencies and run the compiler unit suite:

composer install
PHPX_HOME=/path/to/phpx vendor/bin/phpunit

PHPT is the end-to-end suite. Build the self-hosted compiler first and pass it
explicitly to the test runner; using the Zend PHP executable as--compilerdoes not test the deployed compiler:

PHPX_HOME=/path/to/phpx php bin/tpc.php project.yml --job 2 --no-progress
php run-tests.php -q -j8 --compiler ./tpc tests/compiler

Static analysis and the source-derived coverage matrix are separate checks:

composer analyse
php bin/analyze-test-coverage.php
php bin/analyze-test-coverage.php \
 --format=markdown --output=build/test-coverage.md --strict

The coverage tool reports PHP version × feature × positive compilation ×
runtime semantics × negative diagnostics, plus concrete PHP-parser AST nodes.
It intentionally does not publish a single percentage without an explicit
denominator. SeeTest coverage analyzer.

GitHub Actions runs PHPUnit and self-hosted PHPT on PHP 8.4 and 8.5. Changes to
compiler behavior should add a focused PHPUnit test for internal/code-generation
rules and a PHPT whenever runtime output or diagnostics are observable.

## Documentation

* Quick Start— minimal compilation flow
* Compilation modes—bin,ext,lib
* Compiler CLI— CLI arguments and project config
* Incompatible PHP features— current limits
* Native types— native scalar types
* High-precision types— BigInt / Decimal / BigFloat
* Std containers— strongly-typed containers
* Universal methods— compile-time method resolution
* Compile-time functions—any(),refval(),objval(), …
* Mixed C++/PHP— C++/PHP interop
* #[Immutable]— compile-time read-only contracts
* #[ArrayDef]— typed array-property contracts
* Property hooks— PHP 8.4 hook lowering and runtime metadata
* Object storage models— Zend object, Box, and Native class boundaries
* Generators— generator lowering and lifecycle
* Test coverage analyzer— AST and feature evidence matrix
* WASI build— WASI targets

## License

TypePHP is licensed under theGNU General Public License v3.0.

## Community

* Repository:https://github.com/swoole/typephp
* Copyright © 2026 上海识沃网络科技有限公司 (Swoole)