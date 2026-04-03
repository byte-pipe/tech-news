---
title: Go 1.25 Release Notes - The Go Programming Language
url: https://go.dev/doc/go1.25
site_name: lobsters
fetched_at: '2025-08-13T23:06:34.661701'
original_url: https://go.dev/doc/go1.25
date: '2025-08-13'
tags: go, release
---

# Go 1.25 Release Notes

## Introduction to Go 1.25

The latest Go release, version 1.25, arrives inAugust 2025, six months afterGo 1.24.
Most of its changes are in the implementation of the toolchain, runtime, and libraries.
As always, the release maintains the Go 1 promise of compatibility.
We expect almost all Go programs to continue to compile and run as before.

## Changes to the language

There are no languages changes that affect Go programs in Go 1.25.
However, in thelanguage specificationthe notion of core types
has been removed in favor of dedicated prose.
See the respectiveblog postfor more information.

## Tools

### Go command

Thego build-asanoption now defaults to doing leak detection at
program exit.
This will report an error if memory allocated by C is not freed and is
not referenced by any other memory allocated by either C or Go.
These new error reports may be disabled by settingASAN_OPTIONS=detect_leaks=0in the environment when running the
program.

The Go distribution will include fewer prebuilt tool binaries. Core
toolchain binaries such as the compiler and linker will still be
included, but tools not invoked by build or test operations will be built
and run bygo toolas needed.

The newgo.modignoredirectivecan be used to
specify directories thegocommand should ignore. Files in these directories
and their subdirectories will be ignored by thegocommand when matching package
patterns, such asallor./..., but will still be included in module zip files.

The newgo doc-httpoption will start a documentation server showing
documentation for the requested object, and open the documentation in a browser
window.

The newgo version -m -jsonoption will print the JSON encodings of theruntime/debug.BuildInfostructures embedded in the given Go binary files.

Thegocommand now supports using a subdirectory of a repository as the
path for a module root, whenresolving a module pathusing the syntax<meta name="go-import" content="root-path vcs repo-url subdir">to indicate
that theroot-pathcorresponds to thesubdirof therepo-urlwith
version control systemvcs.

The newworkpackage pattern matches all packages in the work (formerly called main)
modules: either the single work module in module mode or the set of workspace modules
in workspace mode.

When the go command updates thegoline in ago.modorgo.workfile,
itno longeradds a toolchain line
specifying the command’s current version.

### Vet

Thego vetcommand includes new analyzers:

* waitgroup,
which reports misplaced calls tosync.WaitGroup.Add; and

* hostport,
which reports uses offmt.Sprintf("%s:%d", host, port)to
construct addresses fornet.Dial, as these will not work with
IPv6; instead it suggests usingnet.JoinHostPort.

## Runtime

### Container-awareGOMAXPROCS

The default behavior of theGOMAXPROCShas changed. In prior versions of Go,GOMAXPROCSdefaults to the number of logical CPUs available at startup
(runtime.NumCPU). Go 1.25 introduces two changes:

1. On Linux, the runtime considers the CPU bandwidth limit of the cgroup
containing the process, if any. If the CPU bandwidth limit is lower than the
number of logical CPUs available,GOMAXPROCSwill default to the lower
limit. In container runtime systems like Kubernetes, cgroup CPU bandwidth
limits generally correspond to the “CPU limit” option. The Go runtime does
not consider the “CPU requests” option.
2. On all OSes, the runtime periodically updatesGOMAXPROCSif the number
of logical CPUs available or the cgroup CPU bandwidth limit change.

Both of these behaviors are automatically disabled ifGOMAXPROCSis set
manually via theGOMAXPROCSenvironment variable or a call toruntime.GOMAXPROCS. They can also be disabled explicitly with theGODEBUG
settingscontainermaxprocs=0andupdatemaxprocs=0,
respectively.

In order to support reading updated cgroup limits, the runtime will keep cached
file descriptors for the cgroup files for the duration of the process lifetime.

### New experimental garbage collector

A new garbage collector is now available as an experiment. This garbage
collector’s design improves the performance of marking and scanning small objects
through better locality and CPU scalability. Benchmark result vary, but we expect
somewhere between a 10—40% reduction in garbage collection overhead in real-world
programs that heavily use the garbage collector.

The new garbage collector may be enabled by settingGOEXPERIMENT=greenteagcat build time. We expect the design to continue to evolve and improve. To that
end, we encourage Go developers to try it out and report back their experiences.
See theGitHub issuefor more details on the design and
instructions for sharing feedback.

### Trace flight recorder

Runtime execution traceshave long provided a powerful,
but expensive way to understand and debug the low-level behavior of an
application. Unfortunately, because of their size and the cost of continuously
writing an execution trace, they were generally impractical for debugging rare
events.

The newruntime/trace.FlightRecorderAPI
provides a lightweight way to capture a runtime execution trace by continuously
recording the trace into an in-memory ring buffer. When a significant event
occurs, a program can callFlightRecorder.WriteToto
snapshot the last few seconds of the trace to a file. This approach produces a
much smaller trace by enabling applications to capture only the traces that
matter.

The length of time and amount of data captured by aFlightRecordermay be configured within
theFlightRecorderConfig.

### Change to unhandled panic output

The message printed when a program exits due to an unhandled panic
that was recovered and repanicked no longer repeats the text of
the panic value.

Previously, a program which panicked withpanic("PANIC"),
recovered the panic, and then repanicked with the original
value would print:

panic: PANIC [recovered]
 panic: PANIC

This program will now print:

panic: PANIC [recovered, repanicked]

### VMA names on Linux

On Linux systems with kernel support for anonymous virtual memory area (VMA) names
(CONFIG_ANON_VMA_NAME), the Go runtime will annotate anonymous memory
mappings with context about their purpose. e.g.,[anon: Go: heap]for heap
memory. This can be disabled with theGODEBUG settingdecoratemappings=0.

## Compiler

### nilpointer bug

This release fixes acompiler bug, introduced in Go 1.21, that
could incorrectly delay nil pointer checks. Programs like the following, which
used to execute successfully (incorrectly), will now (correctly) panic with a
nil-pointer exception:

package main

import "os"

func main() {
 f, err := os.Open("nonExistentFile")
 name := f.Name()
 if err != nil {
 return
 }
 println(name)
}

This program is incorrect because it uses the result ofos.Openbefore
checking the error. Iferris non-nil, then thefresult may be nil, in
which casef.Name()should panic. However, in Go versions 1.21 through 1.24,
the compiler incorrectly delayed the nil check untilafterthe error check,
causing the program to execute successfully, in violation of the Go spec. In Go
1.25, it will no longer run successfully. If this change is affecting your code,
the solution is to put the non-nil error check earlier in your code, preferably
immediately after the error-generating statement.

### DWARF5 support

The compiler and linker in Go 1.25 now generate debug information
usingDWARF version 5. The
newer DWARF version reduces the space required for debugging
information in Go binaries, and reduces the time for linking,
especially for large Go binaries.
DWARF 5 generation can be disabled by setting the environment
variableGOEXPERIMENT=nodwarf5at build time
(this fallback may be removed in a future Go release).

### Faster slices

The compiler can now allocate the backing store for slices on the
stack in more situations, which improves performance. This change has
the potential to amplify the effects of incorrectunsafe.Pointerusage, see for exampleissue
73199. In order to track down these problems, thebisect toolcan be
used to find the allocation causing trouble using the-compile=variablemakeflag. All such new stack allocations can also
be turned off using-gcflags=all=-d=variablemakehash=n.

## Linker

The linker now accepts a-funcalign=Ncommand line option, which
specifies the alignment of function entries.
The default value is platform-dependent, and is unchanged in this
release.

## Standard library

### New testing/synctest package

The newtesting/synctestpackage
provides support for testing concurrent code.

TheTestfunction runs a test function in an isolated
“bubble”. Within the bubble, time is virtualized:timepackage
functions operate on a fake clock and the clock moves forward instantaneously if
all goroutines in the bubble are blocked.

TheWaitfunction waits for all goroutines in the
current bubble to block.

This package was first available in Go 1.24 underGOEXPERIMENT=synctest, with
a slightly different API. The experiment has now graduated to general
availability. The old API is still present ifGOEXPERIMENT=synctestis set,
but will be removed in Go 1.26.

### New experimental encoding/json/v2 package

Go 1.25 includes a new, experimental JSON implementation,
which can be enabled by setting the environment variableGOEXPERIMENT=jsonv2at build time.

When enabled, two new packages are available:

* Theencoding/json/v2package is
a major revision of theencoding/jsonpackage.
* Theencoding/json/jsontextpackage
provides lower-level processing of JSON syntax.

In addition, when the “jsonv2” GOEXPERIMENT is enabled:

* Theencoding/jsonpackage
uses the new JSON implementation.
Marshaling and unmarshaling behavior is unaffected,
but the text of errors returned by package function may change.
* Theencoding/jsonpackage contains
a number of new options which may be used
to configure the marshaler and unmarshaler.

The new implementation performs substantially better than
the existing one under many scenarios. In general,
encoding performance is at parity between the implementations
and decoding is substantially faster in the new one.
See thegithub.com/go-json-experiment/jsonbenchrepository for more detailed analysis.

See theproposal issuefor more details.

We encourage users ofencoding/jsonto test
their programs withGOEXPERIMENT=jsonv2enabled to help detect
any compatibility issues with the new implementation.

We expect the design ofencoding/json/v2to continue to evolve. We encourage developers to try out the new
API and provide feedback on theproposal issue.

### Minor changes to the library

#### archive/tar

TheWriter.AddFSimplementation now supports symbolic links
for filesystems that implementio/fs.ReadLinkFS.

#### encoding/asn1

UnmarshalandUnmarshalWithParamsnow parse the ASN.1 types T61String and BMPString more consistently. This may
result in some previously accepted malformed encodings now being rejected.

#### crypto

MessageSigneris a new signing interface that can
be implemented by signers that wish to hash the message to be signed themselves.
A new function is also introduced,SignMessage,
which attempts to upgrade aSignerinterface toMessageSigner, using theMessageSigner.SignMessagemethod if
successful, andSigner.Signif not. This can be
used when code wishes to support bothSignerandMessageSigner.

Changing thefips140GODEBUG settingafter the program has started is now a no-op.
Previously, it was documented as not allowed, and could cause a panic if changed.

SHA-1, SHA-256, and SHA-512 are now slower on amd64 when AVX2 instructions are not available.
All server processors (and most others) produced since 2015 support AVX2.

#### crypto/ecdsa

The newParseRawPrivateKey,ParseUncompressedPublicKey,PrivateKey.Bytes, andPublicKey.Bytesfunctions and methods
implement low-level encodings, replacing the need to usecrypto/ellipticormath/bigfunctions and methods.

When FIPS 140-3 mode is enabled, signing is now four times faster, matching the
performance of non-FIPS mode.

#### crypto/ed25519

When FIPS 140-3 mode is enabled, signing is now four times faster, matching the
performance of non-FIPS mode.

#### crypto/elliptic

The hidden and undocumentedInverseandCombinedMultmethods on someCurveimplementations have been removed.

#### crypto/rsa

PublicKeyno longer claims that the modulus value
is treated as secret.VerifyPKCS1v15andVerifyPSSalready warned that all inputs are
public and could be leaked, and there are mathematical attacks that can recover
the modulus from other public values.

Key generation is now three times faster.

#### crypto/sha1

Hashing is now two times faster on amd64 when SHA-NI instructions are available.

#### crypto/sha3

The newSHA3.Clonemethod implementshash.Cloner.

Hashing is now two times faster on Apple M processors.

#### crypto/tls

The newConnectionState.CurveIDfield exposes the key exchange mechanism used to establish the connection.

The newConfig.GetEncryptedClientHelloKeyscallback can be used to set theEncryptedClientHelloKeys
for a server to use when a client sends an Encrypted Client Hello extension.

SHA-1 signature algorithms are now disallowed in TLS 1.2 handshakes, perRFC 9155.
They can be re-enabled with theGODEBUG settingtlssha1=1.

WhenFIPS 140-3 modeis enabled, Extended Master Secret
is now required in TLS 1.2, and Ed25519 and X25519MLKEM768 are now allowed.

TLS servers now prefer the highest supported protocol version, even if it isn’t
the client’s most preferred protocol version.

Both TLS clients and servers are now stricter in following the specifications
and in rejecting off-spec behavior. Connections with compliant peers should be
unaffected.

#### crypto/x509

CreateCertificate,CreateCertificateRequest, andCreateRevocationListcan now accept acrypto.MessageSignersigning interface as well ascrypto.Signer. This allows these functions to use
signers which implement “one-shot” signing interfaces, where hashing is done as
part of the signing operation, instead of by the caller.

CreateCertificatenow uses truncated
SHA-256 to populate theSubjectKeyIdif it is missing.
TheGODEBUG settingx509sha256skid=0reverts to SHA-1.

ParseCertificatenow rejects certificates
which contain a BasicConstraints extension that contains a negative pathLenConstraint.

ParseCertificatenow handles strings encoded
with the ASN.1 T61String and BMPString types more consistently. This may result in
some previously accepted malformed encodings now being rejected.

#### debug/elf

Thedebug/elfpackage adds two new constants:

* PT_RISCV_ATTRIBUTES
* SHT_RISCV_ATTRIBUTESfor RISC-V ELF parsing.

#### go/ast

TheFilterPackage,PackageExports, andMergePackageFilesfunctions, and theMergeModetype and its
constants, are all deprecated, as they are for use only with the
long-deprecatedObjectandPackagemachinery.

The newPreorderStackfunction, likeInspect, traverses a syntax
tree and provides control over descent into subtrees, but as a
convenience it also provides the stack of enclosing nodes at each
point.

#### go/parser

TheParseDirfunction is deprecated.

#### go/token

The newFileSet.AddExistingFilesmethod enables existingFiles to be added to aFileSet,
or aFileSetto be constructed for an arbitrary
set ofFiles, alleviating the problems associated with a single globalFileSetin long-lived applications.

#### go/types

Varnow has aVar.Kindmethod that classifies the variable as one
of: package-level, receiver, parameter, result, local variable, or
a struct field.

The newLookupSelectionfunction looks up the field or method of a
given name and receiver type, like the existingLookupFieldOrMethodfunction, but returns the result in the form of aSelection.

#### hash

The newXOFinterface can be implemented by “extendable output
functions”, which are hash functions with arbitrary or unlimited output length
such asSHAKE.

Hashes implementing the newClonerinterface can return a copy of their state.
All standard libraryHashimplementations now implementCloner.

#### hash/maphash

The newHash.Clonemethod implementshash.Cloner.

#### io/fs

A newReadLinkFSinterface provides the ability to read symbolic links in a filesystem.

#### log/slog

GroupAttrscreates a groupAttrfrom a slice ofAttrvalues.

Recordnow has aSourcemethod,
returning its source location or nil if unavailable.

#### mime/multipart

The new helper functionFileContentDispositionbuilds multipart
Content-Disposition header fields.

#### net

LookupMXandResolver.LookupMXnow return DNS names that look
like valid IP address, as well as valid domain names.
Previously if a name server returned an IP address as a DNS name,LookupMXwould discard it, as required by the RFCs.
However, name servers in practice do sometimes return IP addresses.

On Windows,ListenMulticastUDPnow supports IPv6 addresses.

On Windows, it is now possible to convert between anos.Fileand a network connection. Specifcally, theFileConn,FilePacketConn, andFileListenerfunctions are now implemented, and
return a network connection or listener corresponding to an open file.
Similarly, theFilemethods ofTCPConn,UDPConn,UnixConn,IPConn,TCPListener,
andUnixListenerare now implemented, and return
the underlyingos.Fileof a network connection.

#### net/http

The newCrossOriginProtectionimplements protections againstCross-Site
Request Forgery (CSRF)by rejecting non-safe cross-origin browser requests.
It usesmodern browser Fetch metadata, doesn’t require tokens
or cookies, and supports origin-based and pattern-based bypasses.

#### os

On Windows,NewFilenow supports handles opened for asynchronous I/O (that is,syscall.FILE_FLAG_OVERLAPPEDis specified in thesyscall.CreateFilecall).
These handles are associated with the Go runtime’s I/O completion port,
which provides the following benefits for the resultingFile:

* I/O methods (File.Read,File.Write,File.ReadAt, andFile.WriteAt) do not block an OS thread.
* Deadline methods (File.SetDeadline,File.SetReadDeadline, andFile.SetWriteDeadline) are supported.

This enhancement is especially beneficial for applications that communicate via named pipes on Windows.

Note that a handle can only be associated with one completion port at a time.
If the handle provided toNewFileis already associated with a completion port,
the returnedFileis downgraded to synchronous I/O mode.
In this case, I/O methods will block an OS thread, and the deadline methods have no effect.

The filesystems returned byDirFSandRoot.FSimplement the newio/fs.ReadLinkFSinterface.CopyFSsupports symlinks when copying filesystems that implementio/fs.ReadLinkFS.

TheRoottype supports the following additional methods:

* Root.Chmod
* Root.Chown
* Root.Chtimes
* Root.Lchown
* Root.Link
* Root.MkdirAll
* Root.ReadFile
* Root.Readlink
* Root.RemoveAll
* Root.Rename
* Root.Symlink
* Root.WriteFile

#### reflect

The newTypeAssertfunction permits converting aValuedirectly to a Go value
of the given type. This is like using a type assertion on the result ofValue.Interface,
but avoids unnecessary memory allocations.

#### regexp/syntax

The\p{name}and\P{name}character class syntaxes now accept the names
Any, ASCII, Assigned, Cn, and LC, as well as Unicode category aliases like\p{Letter}for\pL.
FollowingUnicode TR18, they also now use
case-insensitive name lookups, ignoring spaces, underscores, and hyphens.

#### runtime

Cleanup functions scheduled byAddCleanupare now executed
concurrently and in parallel, making cleanups more viable for heavy
use like theuniquepackage. Note that individual cleanups should
still shunt their work to a new goroutine if they must execute or
block for a long time to avoid blocking the cleanup queue.

A newGODEBUG=checkfinalizers=1setting helps find common issues with
finalizers and cleanups, such as those describedin the GC
guide.
In this mode, the runtime runs diagnostics on each garbage collection cycle,
and will also regularly report the finalizer and
cleanup queue lengths to stderr to help identify issues with
long-running finalizers and/or cleanups.
See theGODEBUG documentationfor more details.

The newSetDefaultGOMAXPROCSfunction setsGOMAXPROCSto the runtime
default value, as if theGOMAXPROCSenvironment variable is not set. This is
useful for enabling thenewGOMAXPROCSdefaultif it has been
disabled by theGOMAXPROCSenvironment variable or a prior call toGOMAXPROCS.

#### runtime/pprof

The mutex profile for contention on runtime-internal locks now correctly points
to the end of the critical section that caused the delay. This matches the
profile’s behavior for contention onsync.Mutexvalues. Theruntimecontentionstackssetting forGODEBUG, which allowed opting in to the
unusual behavior of Go 1.22 through 1.24 for this part of the profile, is now
gone.

#### sync

The newWaitGroup.Gomethod
makes the common pattern of creating and counting goroutines more convenient.

#### testing

The new methodsT.Attr,B.Attr, andF.Attremit an
attribute to the test log. An attribute is an arbitrary
key and value associated with a test.

For example, in a test namedTestF,t.Attr("key", "value")emits:

=== ATTR TestF key value

With the-jsonflag, attributes appear as a new “attr” action.

The newOutputmethod ofT,BandFprovides anio.Writerthat writes to the same test output stream asTB.Log.
LikeTB.Log, the output is indented, but it does not include the file and line number.

TheAllocsPerRunfunction now panics
if parallel tests are running.
The result ofAllocsPerRunis inherently
flaky if other tests are running.
The new panicking behavior helps catch such bugs.

#### testing/fstest

MapFSimplements the newio/fs.ReadLinkFSinterface.TestFSwill verify the functionality of theio/fs.ReadLinkFSinterface if implemented.TestFSwill no longer follow symlinks to avoid unbounded recursion.

#### unicode

The newCategoryAliasesmap provides access to category alias names, such as “Letter” for “L”.

The new categoriesCnandLCdefine unassigned codepoints and cased letters, respectively.
These have always been defined by Unicode but were inadvertently omitted in earlier versions of Go.
TheCcategory now includesCn, meaning it has added all unassigned code points.

#### unique

Theuniquepackage now reclaims interned values more eagerly,
more efficiently, and in parallel. As a consequence, applications usingMakeare now less likely to experience memory blow-up when lots of
truly unique values are interned.

Values passed toMakecontainingHandles previously required multiple
garbage collection cycles to collect, proportional to the depth of the chain
ofHandlevalues. Now, once
unused, they are collected promptly in a single cycle.

## Ports

### Darwin

Asannouncedin the Go 1.24 release notes, Go 1.25 requires macOS 12 Monterey or later.
Support for previous versions has been discontinued.

### Windows

Go 1.25 is the last release that contains thebroken32-bit windows/arm port (GOOS=windowsGOARCH=arm). It will be removed in Go 1.26.

### Loong64

The linux/loong64 port now supports the race detector, gathering traceback information from C code
usingruntime.SetCgoTraceback, and linking cgo programs with the
internal link mode.

### RISC-V

The linux/riscv64 port now supports thepluginbuild mode.

TheGORISCV64environment variable now accepts a new valuerva23u64,
which selects the RVA23U64 user-mode application profile.
