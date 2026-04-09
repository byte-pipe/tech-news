---
title: 'cli/q: 🌱 A minimal programming language and compiler. - Git'
url: https://git.urbach.dev/cli/q
site_name: lobsters
fetched_at: '2025-08-04T23:07:01.159353'
original_url: https://git.urbach.dev/cli/q
author: cli
date: '2025-08-04'
description: q - 🌱 A minimal programming language and compiler.
tags: plt
---

cli
/
q

Watch

			1


Star

			2


Fork

				You've already forked q


			0


🌱
 A minimal programming language and compiler.

main

Find a file

		HTTPS


		Cite this repository


			Cancel


			Exact


Eduard Urbach

b2c5eb7d52


			All checks were successful





/ test (push)
Successful in 16s

Details

Implemented x86 encoding for the test instruction

2025-08-05 01:04:50 +02:00

docs



Updated documentation

2025-07-29 14:08:18 +02:00

examples



Updated existing code to use shorter forms

2025-08-03 18:01:37 +02:00

lib



Implemented constants

2025-07-21 16:31:30 +02:00

src



Implemented x86 encoding for the test instruction

2025-08-05 01:04:50 +02:00

tests



Added a test for prime number calculation

2025-08-04 20:37:17 +02:00

.gitignore

Updated documentation

2025-07-05 17:14:39 +02:00

go.mod

Updated dependencies

2025-07-24 11:29:28 +02:00

go.sum

Updated dependencies

2025-07-24 11:29:28 +02:00

main.go

Initial commit

2025-06-18 22:18:31 +02:00

#### docs/readme.mdUnescapeEscape

# The Q Programming Language

Q is a minimal, dependency-free programming language and compiler targeting x86-64 and arm64 with ultra-fast builds and tiny binaries.

## Features

* High performance (ssaandasmoptimizations)
* Fast compilation (<1 ms for simple programs)
* Tiny executables ("Hello World" is ~600 bytes)
* Multiple platforms (Linux, Mac and Windows)
* Zero dependencies (no llvm, no libc)

## Installation

Note

qis under heavy development and not ready for production yet.

Feel free tocontact meif you are interested in helping out.

Build from source:

git clone https://git.urbach.dev/cli/q

cd
 q
go build

Install via symlink:

ln -s
$PWD
/q ~/.local/bin/q

## Usage

Runhelloexample:

q examples/hello

Build an executable:

q build examples/hello

Build for another architecture:

q build examples/hello --arch arm
q build examples/hello --arch x86

Build for another operating system:

q build examples/hello --os linux
q build examples/hello --os mac
q build examples/hello --os windows

Build with verbose output:

q build examples/hello --verbose

## Source overview

This section is for contributors who want a high-level overview of the source code structure.

### Packages

* arm- arm64 architecture
* asm- Generic assembler
* ast- Abstract syntax tree
* cli- Command line interface
* codegen- SSA to assembly code generation
* compiler- Compiler frontend
* config- Build configuration
* core- DefinesFunctionand compiles tokens to SSA
* cpu- Types to represent a generic CPU
* data- Data container that can re-use existing data
* dll- DLL support for Windows systems
* elf- ELF format for Linux executables
* errors- Error handling that reports lines and columns
* exe- Generic executable format to calculate section offsets
* expression- Expression parser generating trees
* fs- File system access
* global- Global variables like the working directory
* linker- Frontend for generating executable files
* macho- Mach-O format for Mac executables
* memfile- Memory backed file descriptors
* pe- PE format for Windows executables
* scanner- Scanner that parses top-level instructions
* set- Generic set implementation
* sizeof- Calculates the byte size of numbers
* ssa- Static single assignment types
* token- Tokenizer
* types- Type system
* verbose- Verbose output
* x86- x86-64 architecture

### Typical flow

1. main
2. cli.Exec
3. compiler.Compile
4. scanner.Scan
5. core.Compile
6. linker.Write

## FAQ

### How tiny is a Hello World?

arm64

x86-64

🐧
 Linux

646 bytes

582 bytes

🍏
 Mac

33 KiB

8.2 KiB

🪟
 Windows

1.7 KiB

1.7 KiB

This table often raises the question why Mac builds are so huge compared to the rest. The answer is inthese few linesof their kernel code. None of the other operating systems force you to page-align sections on disk. In practice, however, it's not as bad as it sounds because the padding is a zero-filled area that barely consumes any disk space insparse files.

### Which platforms are supported?

arm64

x86-64

🐧
 Linux

✔️

✔️

🍏
 Mac

✔️
*

✔️

🪟
 Windows

✔️
*

✔️

Those marked with a star need testing. Please contact me if you have a machine with the marked architectures.

### How is the assembly code quality?

The backend uses an SSA based IR which is also used by well established compilers likegcc,goandllvm. SSA makes it trivial to apply lots of common optimization passes to it. As such, the quality of the generated assembly is fairly high despite the young age of the project.

### Which security features are supported?

#### PIE

All executables are built as position independent executables supporting a dynamic base address.

#### W^X

All memory pages are loaded with either execute or write permissions but never with both. Constant data is read-only.

Read

Execute

Write

Code

✔️

✔️

❌

Data

✔️

❌

❌

### How do I use it for scripting?

The compiler is actually so fast that it's possible to compile an entire script within microseconds.

#!/usr/bin/env q

import io

main() {
	io.write("Hello\n")
}

Create a file with the contents above and add permissions viachmod +x. Now you can execute it from anywhere. The generated machine code runs directly from RAM if the OS supports it.

### How do I run the test suite?

Run all tests:

go run gotest.tools/gotestsum@latest

Generate coverage:

go
test
 -coverpkg
=
./... -coverprofile
=
cover.out ./...

View coverage:

go tool cover -func cover.out
go tool cover -html cover.out

### How do I run the benchmarks?

Run compiler benchmarks:

go
test
 ./tests -run
=
'^$'
 -bench
=
. -benchmem

Run compiler benchmarks in single-threaded mode:

GOMAXPROCS
=
1
 go
test
 ./tests -run
'^$'
 -bench . -benchmem

Generate profiling data:

go
test
 ./tests -run
=
'^$'
 -bench
=
. -benchmem -cpuprofile cpu.out -memprofile mem.out

View profiling data:

go tool pprof --nodefraction
=
0.1 -http
=
:8080 ./cpu.out
go tool pprof --nodefraction
=
0.1 -http
=
:8080 ./mem.out

### Is there an IRC channel?

#qonirc.urbach.dev.

### How do I pronounce the name?

/ˈkjuː/ just likeqin the English alphabet.

## License

Please see thelicense documentation.

## Copyright

© 2025 Eduard Urbach
