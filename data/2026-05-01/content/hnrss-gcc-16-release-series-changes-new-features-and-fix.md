---
title: GCC 16 Release Series — Changes, New Features, and Fixes - GNU Project
url: https://gcc.gnu.org/gcc-16/changes.html
site_name: hnrss
content_file: hnrss-gcc-16-release-series-changes-new-features-and-fix
fetched_at: '2026-05-01T03:52:57.430914'
original_url: https://gcc.gnu.org/gcc-16/changes.html
date: '2026-04-30'
description: GCC 16 has been released
tags:
- hackernews
- hnrss
---

# GCC 16 Release SeriesChanges, New Features, and Fixes

This page is a "brief" summary of some of the huge number of improvements
in GCC 16.
You may also want to check out ourPorting to GCC 16page and thefull GCC documentation.

## Caveats

* int8_tetc. are nowsigned charon Solaris
 for conformance with the C99 standard. However, this is an
 incompatible change. Seethe
 porting notesfor more information.
* The-pthreadoption no longer
 predefines_REENTRANTon Solaris.
 Seethe porting notesfor more
 information.
* The so-called "json" format for-fdiagnostics-format=has been removed in this release.
 Users seeking machine-readable diagnostics from GCC should useSARIF.

## General Improvements

* Link-Time Optimization now supports better handling of toplevel asm
 statements with-flto-toplevel-asm-heuristics.
* Speculative devirtualization now handles general indirect function
 calls and supports speculating of more than one target.
* The vectorizer is now more flexible in identifying in-loop parallelism
 of reductions.
* The vectorizer now supports vectorizing uncounted loops or loops for
 which the number of iterations could not be determined.
* The vectorizer now supports peeling for alignment for vector length
 agnostic loops using masking.
* The vectorizer now supports mutual peeling for alignment.
* The vectorizer now generates more efficient code for loops with early
 breaks by eliminating the vector induction computations.

### Documentation

* The documentation forGCC Command Optionsand theoption indexhave been corrected to include many previously
 missing options.
* The documentation forGCC-specific attributeshas been modernized to put more emphasis
 on the standard attribute syntax, which GCC accepts in all supported
 dialects of C and C++. The material has also been reorganized to be
 less repetitive, and there is a newindexfor attributes.
* Documentation for parameters and option spec files has been moved
 from the main GCC manual to theGCC internals manual.
 These features are intended for use by GCC developers and those
 who need to build custom GCC configurations.

## New Languages and Language specific improvements

### OpenMP

See theGNU Offloading and Multi-Processing Project (GOMP)page for general information.

* Thememory allocationsupport has been enhanced: for allocators with thepinnedtrait, includingompx_gnu_pinned_mem_alloc,
 theCUDA
 API (if available)is used; this improves the performance when accessing
 this memory on Nvidia GPUs. The newly addedompx_gnu_managed_mem_allocallocator and theompx_gnu_managed_mem_space(both GNU
 extensions) allocate device-accessible memory on the host. Such memory is
 device accessible even when unified-shared memory is not supported and
 might have different page-migration behavior than other memory on systems
 even if all host memory is device accessible.
* OpenMP 5.0: Limited support fordeclare mapperhas been added
 for C and C++, only. Theuses_allocatorsclause is now
 supported, including the OpenMP 5.2 syntax changes and supporting
 semicolons (OpenMP 6.0); for now, only predefined allocators are supported.OpenMP 5.1: Initial support for theiteratormodifier in map
 clauses and thetarget updateconstruct has been added for C
 and C++.OpenMP 5.2: Thebegin declare variantdirective for C
 and C++ is now supported.OpenMP 6.0: Theomp_target_memsetandomp_target_memset_asyncAPI routines have been
 added. Theno_openmp_constructsassumptions clause can now
 be used.OpenMP Technical Report 14 (TR14): The namedomp_default_deviceconstant has been added to denote the default-device number.For OpenMP directives and clauses that have been deprecated in OpenMP 5.0,
 5.1, or 5.2, a deprecation warning is shown, hinting at the to-be-used
 syntax; the warning is on by default and can be silenced using-Wno-deprecated-openmp. Additionally, a deprecation warning is
 shown when using a deprecated named constant or API routine; this warning
 can be silenced using-Wno-deprecated-declarations.
* OpenMP 5.1: Initial support for theiteratormodifier in map
 clauses and thetarget updateconstruct has been added for C
 and C++.
* OpenMP 5.2: Thebegin declare variantdirective for C
 and C++ is now supported.
* OpenMP 6.0: Theomp_target_memsetandomp_target_memset_asyncAPI routines have been
 added. Theno_openmp_constructsassumptions clause can now
 be used.
* OpenMP Technical Report 14 (TR14): The namedomp_default_deviceconstant has been added to denote the default-device number.
* For OpenMP directives and clauses that have been deprecated in OpenMP 5.0,
 5.1, or 5.2, a deprecation warning is shown, hinting at the to-be-used
 syntax; the warning is on by default and can be silenced using-Wno-deprecated-openmp. Additionally, a deprecation warning is
 shown when using a deprecated named constant or API routine; this warning
 can be silenced using-Wno-deprecated-declarations.

### OpenACC

See the GCCOpenACCwiki page
for general information.

* Theacc_memcpy_deviceandacc_memcpy_device_asyncAPI routines have been added for C, C++ and Fortran.
* OpenACC 3.0: Thewaitdirective now accepts theifclause.
* OpenACC 3.3: The Fortran API routinesacc_attachandacc_detachnow augment their OpenACC 2.6 C/C++ counterparts.
* OpenACC 3.4: In Fortran, named constants (PARAMETER) used asvarin data clauses are now permitted by the specification and
 GCC for better compatibility with existing code; however, with GCC,
 specifying them in data clauses affects neither compile-time nor runtime
 behavior.

### Ada

#### GNAT Extensions

* TheConstructor[RFC]andDestructor[RFC]extensions add new construction/finalization mechanisms that differ
 significantly from standard Ada. Those features are inspired by
 object-oriented programming in other widely used languages (such as C++).
* Implicit
 withallows a stand-alone use clause in the context clause of a
 compilation unit to imply an implicit with of the same library unit where
 an equivalent with clause would be allowed.
* Structural
 Generic
 instantiation[RFC]allows reference to an implicit instance of a generic unit, that is
 denoted directly by the unit’s name and actual parameters, rather than by
 a separately declared name.
* TheExtended_Accessaspect can be specified on a general access type declaration designating an
 unconstrained array subtype. It changes the pointer representation and
 allows easier interfacing with foreign languages when memory for the
 designated object is not allocated by Ada. In particular, it allows the
 creation
 ofaccess
 to an array
 slice[RFC].

#### Other

* VAST (Verifier for the Ada Semantic Tree), enabled
 with-gnatd_V(or-gnatd_Wfor verbose mode), can
 be used to debug the compiler. It checks various properties of the produced
 Ada Semantic Tree and reports detected violations.
* The semantic analysis of Ada 2022’s Reduction Expressions has been
 enhanced.
* The Ada.Containers.Bounded_Indefinite_Holders unit has been added.
* Various loopholes in the implementation of accessibility rules have been
 plugged.
* Android support has been improved.

### C++

* C++20 by default: GCC 16 changes the default language version
 for C++ compilation from-std=gnu++17to-std=gnu++20.
 If your code relies on older versions of the C++ standard, you will need to
 either add-std=to your build flags, or port your code; seethe porting notes.
 N.B. C++20 modules support is still experimental and must be enabled by-fmodules.
* Several C++26 features have been implemented:P2996R13, Reflection
 (PR120775, enabled by-std=c++26 -freflection)P3394R4, Annotations for
 ReflectionP3293R3, Splicing a base
 class subobjectP3096R12, Function Parameter
 ReflectionP3491R3,define_static_{string,object,array}
 (PR120783)P3560R2, Error Handling in
 ReflectionP1306R5, Expansion
 statements (PR120776)P2900R14, Contracts
 (PR119061)P2795R5, Erroneous behavior
 for uninitialized reads (PR114457)P1061R10, Structured bindings
 can introduce a pack (PR117783)P3068R5,constexprexceptions (PR117785)P3533R2,constexprvirtual inheritance (PR120777)P1494R5, Partial program
 correctness (PR119060)P3618R0, Allow attaching main
 to the global module (PR120773)P2843R3, Preprocessing is
 never undefined (PR120778)P2686R4,constexprstructured bindings and references toconstexprvariables (PR117784, only partially,
 structured bindings can beconstexprbut references toconstexprautomatic variables still not allowed)
* P2996R13, Reflection
 (PR120775, enabled by-std=c++26 -freflection)
* P3394R4, Annotations for
 Reflection
* P3293R3, Splicing a base
 class subobject
* P3096R12, Function Parameter
 Reflection
* P3491R3,define_static_{string,object,array}
 (PR120783)
* P3560R2, Error Handling in
 Reflection
* P1306R5, Expansion
 statements (PR120776)
* P2900R14, Contracts
 (PR119061)
* P2795R5, Erroneous behavior
 for uninitialized reads (PR114457)
* P1061R10, Structured bindings
 can introduce a pack (PR117783)
* P3068R5,constexprexceptions (PR117785)
* P3533R2,constexprvirtual inheritance (PR120777)
* P1494R5, Partial program
 correctness (PR119060)
* P3618R0, Allow attaching main
 to the global module (PR120773)
* P2843R3, Preprocessing is
 never undefined (PR120778)
* P2686R4,constexprstructured bindings and references toconstexprvariables (PR117784, only partially,
 structured bindings can beconstexprbut references toconstexprautomatic variables still not allowed)
* Several C++23 features have been implemented:P2036R3, Change scope of
 lambda trailing-return-type (PR102610)P2590R2, Explicit lifetime
 management (PR106658)P2246R1, Character encoding
 of diagnostic text (PR102613)
* P2036R3, Change scope of
 lambda trailing-return-type (PR102610)
* P2590R2, Explicit lifetime
 management (PR106658)
* P2246R1, Character encoding
 of diagnostic text (PR102613)
* Various C++ error messages (such as for problems involving templates)
 now have a hierarchical structure. This nesting of messages is presented
 using indentation and bullet points. The old behavior can be restored via-fno-diagnostics-show-nestingor-fdiagnostics-plain-output.
* Improved experimental C++20 modules support:New command line option--compile-std-modulethat
 conveniently builds the<bits/stdc++.h>header unit
 and thestdandstd.compatmodules before
 compiling any source files explicitly specified on the command line.Whenever the<bits/stdc++.h>header unit has been
 built, GCC now transparently translates an#includeof
 any importable standard library header into animportof<bits/stdc++.h>.Many reported bugs have been fixed, thanks to Nathaniel Shead.
* New command line option--compile-std-modulethat
 conveniently builds the<bits/stdc++.h>header unit
 and thestdandstd.compatmodules before
 compiling any source files explicitly specified on the command line.
* Whenever the<bits/stdc++.h>header unit has been
 built, GCC now transparently translates an#includeof
 any importable standard library header into animportof<bits/stdc++.h>.
* Many reported bugs have been fixed, thanks to Nathaniel Shead.
* Constraint failure diagnostics for standard library type traits such asis_constructible_vandis_invocable_vare
 improved to further elaborate why the trait isfalseinstead
 of just reportingexpression is_foo_v<...> evaluated to false,
 thanks to Nathaniel Shead.

#### Runtime Library (libstdc++)

* For targets that support128-bit
 integers,std::is_integral<__int128>and similar
 traits are always true. Previously this was only the case when compiling
 with GNU dialects (-std=gnu++17,-std=gnu++14,
 etc.) and not with strict dialects (-std=c++17, etc.)
* The proposalP0952R2: A new specification forstd::generate_canonicalwas implemented in all affected modes (since C++11), impacting the observed
 output. The previous behavior can be restored by defining_GLIBCXX_USE_OLD_GENERATE_CANONICAL.
* Thestd::variantABI was updated to make it conforming
 and consistent with C++20 and later modes. This impacts the layout
 of classes which have astd::variantas the first member
 and a base class of the same type as one of thevariant'salternatives, if that type is an empty class and has a non-trivial
 destructor:struct E { ~E(); };
struct Affected : E
{
 std::variant<E, int> mem; // previously stored at offset zero,
			 // uses non-zero offset now
};The previous behavior can be restored by defining_GLIBCXX_USE_VARIANT_CXX17_OLD_ABI. This impacts only
 C++17 mode.
* std::regexexecution has been rewritten to use a heap-based
 stack instead of the system stack, avoiding stack overflows when matching
 larger strings.
* Improved support for C++20, including:The C++20 implementation is no longer experimental.Workingstd::chrono::current_zone()on Windows
 (thanks to Björn Schäpers).
* The C++20 implementation is no longer experimental.
* Workingstd::chrono::current_zone()on Windows
 (thanks to Björn Schäpers).
* There are several changes to C++20 components which are incompatible with
 the experimental C++20 support in previous releases. The following C++20
 components have ABI changes in GCC 16:Atomic waiting/notifying functions in<atomic>and
 semaphore types in<semaphore>.
 Synchronization for<syncstream>.The representation ofstd::formatargs andstd::formatterspecializations.The representation of thestd::partial_orderingtype in<compare>.Semantics ofstd::variantwithstd::jthread,std::stop_token, andstd::stop_sourcealternatives.Representation of some range adaptors in<ranges>.This list is not necessarily complete. As C++20 support was experimental
 before GCC 16, programs using C++20 components should assume that those
 components are not compatible with older releases.
* Atomic waiting/notifying functions in<atomic>and
 semaphore types in<semaphore>.
 Synchronization for<syncstream>.
* The representation ofstd::formatargs andstd::formatterspecializations.
* The representation of thestd::partial_orderingtype in<compare>.
* Semantics ofstd::variantwithstd::jthread,std::stop_token, andstd::stop_sourcealternatives.
* Representation of some range adaptors in<ranges>.
* Improved experimental support for C++23, including:std::mdspan, thanks to Luc Grosheintz.ranges::starts_withandranges::ends_with.ranges::shift_leftandranges::shift_right.std::allocator_traits::allocate_at_least.
* std::mdspan, thanks to Luc Grosheintz.
* ranges::starts_withandranges::ends_with.
* ranges::shift_leftandranges::shift_right.
* std::allocator_traits::allocate_at_least.
* Improved experimental support for C++26, including:std::simd.std::inplace_vector.std::optional<T&>.std::copyable_functionandstd::function_ref.std::indirectandstd::polymorphic.std::owner_equalfor shared pointers, thanks to Paul Keir.<debugging>header and contents.Newstd::stringstreamandstd::bitsetmember functions acceptingstd::string_viewarguments,
 thanks to Nathan Myers.Padded mdspan layouts, aligned accessor,std::dims,std::constant_wrapper, andstd::submdspanthanks to Luc Grosheintz.std::philox_engine, thanks to 1nfocalypse.std::atomic_ref::address(), thanks to Yuao Ma.
* std::simd.
* std::inplace_vector.
* std::optional<T&>.
* std::copyable_functionandstd::function_ref.
* std::indirectandstd::polymorphic.
* std::owner_equalfor shared pointers, thanks to Paul Keir.
* <debugging>header and contents.
* Newstd::stringstreamandstd::bitsetmember functions acceptingstd::string_viewarguments,
 thanks to Nathan Myers.
* Padded mdspan layouts, aligned accessor,std::dims,std::constant_wrapper, andstd::submdspanthanks to Luc Grosheintz.
* std::philox_engine, thanks to 1nfocalypse.
* std::atomic_ref::address(), thanks to Yuao Ma.

### Fortran

* Coarrays using native shared memory mulithreading on single node
 machines and handling Fortran 2018'sTEAMfeature.
* Fortran 2003: Parameterized Derived Types support is improved.
 Handling of LEN parameters works but still requires a future 
 change of representation (see PR82649).
* Fortran 2018: Support the extensions to theIMPORTstatement, theREDUCEintrinsic and 
 the newGENERICstatement.
* The Fortran 2023 additions to the trigonometric functions are now
 supported (such as thesinpiintrinsic).
* Fortran 2023: Thesplitintrinsic subroutine is now
 supported andc_f_pointernow accepts an optional
 lower bound as a argument.
* The-fexternal-blas64option has been added to call
 external BLAS routines with 64-bit integer arguments forMATMUL. This option is only valid for
 64-bit systems and when-ffrontend-optimizeis
 in effect.

### Modula-2

* Spelling hints have been implemented. Currently spelling hints
 are issued when processing: import lists, module names and all
 symbols within nested scopes.
* A new implementation of wide set is used and this is
 accompanied with a library moduleM2WIDESET.
 This has changed the ABI and may lead to link-time
 errors with object files generated with a previous GCC version.
* A binary dictionary moduleBinDicthas been
 added to the base libraries.
* The proceduresWriteandWriteLnare available in the modules:ARRAYOFCHAR,CFileSysOp,CHAR,FileSysOp,StringandStringFileSysOp.
* The-fm2-pathname-root=option has been added to
 improve access to external library modules.

### Algol 68

* GCC now includes an experimental Algol 68 compiler, ga68. It aims to
 implement the language described by the Revised Report, including all
 errata approved by the Algol 68 Support subcommittee of IFIP WG2.1.
 Some GNU extensions and a POSIX prelude are also implemented.More information about the language can be found
 onthe Algol 68 website.More information about the front end can be found
 onthe wiki.

## New Targets and Target Specific Improvements

### IA-32/x86-64

* GCC now supports AMD CPUs based on the Zen6 core via-march=znver6. This switch enables the
 AVX512_BMM, AVX_NE_CONVERT, AVX_IFMA, AVX_VNNI_INT8 and
 AVX512_FP16 ISA extensions on top of ISA extensions enabled
 for Zen5.
* Auto-vectorization will now try to use a masked vector epilog when
 AVX512 support is enabled and tuning forznver4,znver5orznver6, saving code size
 and improving performance.
* GCC now supports the Intel CPU named Wildcat Lake through-march=wildcatlake.
 Wildcat Lake is based on Panther Lake.
* GCC now supports the Intel CPU named Nova Lake through-march=novalake.
 Based on ISA extensions enabled on Panther Lake, the switch in addition
 enables the APX_F, AVX10.1, AVX10.2 and PREFETCHI ISA extensions.
* Since GCC 16, AMX-TRANSPOSE and USER_MSR are not enabled through
 the compiler switch-march=diamondrapidsany longer. CLDEMOTE
 is not enabled through the compiler switches-march=alderlake,-march=arrowlake,-march=arrowlake-s,-march=gracemont,-march=lunarlake,-march=meteorlake,-march=pantherlakeand-march=raptorlakeany longer. KL and WIDEKL are not enabled
 through the compiler switches-march=clearwaterforestand-march=pantherlakeany longer. PREFETCHI is not enabled
 through the compiler switch-march=pantherlakeany longer.
* -mavx10.1-256,-mavx10.1-512, and-mevex512were removed together with the warning for the
 behavior change on-mavx10.1.-mavx10.1has
 enabled AVX10.1 intrinsics with 512-bit vector support since GCC 15.
* Support for AMX-TRANSPOSE was removed in GCC 16. GCC will no longer accept-mamx-transpose,
* The new--enable-x86-64-mfentryconfigure option
 enables-mfentrywhich uses__fentry__,
 instead ofmcountfor profiling on x86-64. This
 option is enabled by default for glibc targets.
* --enable-tls=DIALECTis now supported to control the
 default TLS dialect. The default remainsgnu.
 The accepted values aregnuandgnu2(for
 TLS descriptors).

### AMD GPU (GCN)

* For offloading to AMD GPUs: The launch overhead of OpenMP target regions
 and OpenACC compute regions has been drastically reduced.
* Experimental support for AMD Instinct MI300 (gfx942) devices
 has been added, including the genericgfx9-4-genericand
 mostly compatiblegfx950.
* By default, the following multilibs are now built:gfx908,gfx90a,gfx9-generic,gfx9-4-generic,gfx10-3-generic, andgfx11-generic. Multilibs for specific devices are no longer
 built by default if a generic arch exists. Note:When compiling for a specific arch and the multilib only exists
 for the associated generic arch, GCC's error message suggests
 the command-line option to do so.Generic architectures require ROCm 6.4.0 or newer.The new default-built set of multilibs now requires the assembler
 and linker of LLVM 20 or newer.Consult GCC'sAMD installation notesandconfiguration notesfor setting the multilibs to be build.
* When compiling for a specific arch and the multilib only exists
 for the associated generic arch, GCC's error message suggests
 the command-line option to do so.
* Generic architectures require ROCm 6.4.0 or newer.
* The new default-built set of multilibs now requires the assembler
 and linker of LLVM 20 or newer.
* Consult GCC'sAMD installation notesandconfiguration notesfor setting the multilibs to be build.

### LoongArch

* Bit-precise integer types (_BitInt (N)andunsigned _BitInt (N)) are supported.
* Added FunctionMulti-Versioning (FMV) support. Thetarget_clonesattribute can be used to generate multiple function versions for
 different LoongArch CPU features
 (e.g.,lsx,lasx), with automatic
 runtime selection of the optimal version based on CPU capabilities.
* Added support for the LoongArch32 architecture, including theilp32d(default),ilp32f,
 andilp32sABIs.This covers both the standard 32-bit version (LA32) and the
 reduced 32-bit version (LA32R), enabling GCC to generate 32-bit target
 code for a wider range of embedded applications.(Note: This feature depends on corresponding Binutils and glibc support.)

### S/390, System z, IBM z Systems

* Bit-precise integer types (_BitInt (N)andunsigned _BitInt (N)) are supported, now.
* Floating-point type_Float16is supported. All operations
 are carried out in software or byfloatinstructions.
* Global stack protector support has been added and exported via-mstack-protector-guard=global. Option-mstack-protector-guard-recordwas added, too. The primary
 use is for the Linux kernel in order to support run-time patching of the
 address loading of the canary.
* Support for-m31is deprecated and will be removed in a
 future release.

## Operating Systems

### Solaris

* GCC now supports the easy generation of Solaris CTF (Compact C Type
 Format) with the-gsctfoption. More information can be
 found in thectf(5)manual page.

### Windows

* GCC now supports native TLS (Thread-Local Storage) on Windows. In order
 to enable it,--enable-tlsmust be specified at configure
 time and recent GNU binutils must be used (version 2.44 or later).

## Improvements to GCC Diagnostics

* GCC can now output diagnostics in HTML form via-fdiagnostics-add-output=experimental-html
* GCC's SARIF output now respects thedump directory.
 For example, givengcc \
 -o build-dir/foo.o \
 -fdiagnostics-add-output=sarif
 foo.cGCC 15 would write the SARIF tofoo.c.sarif, whereas
 GCC 16 now writes it tobuild-dir/foo.c.sarif.
* GCC's SARIF output now captures the nesting of logical locations.
* In GCC's SARIF output,fixobjects now containdescriptionproperties in many cases.
* GCC's SARIF output has gained 5 new values for the§3.38.8kindsproperty ofthreadFlowLocation,
 for expressing non-standard control flow:throwfor throwing an exceptioncatchfor catching an exceptionunwindfor unwinding stack frame(s) during
	exception-handlingsetjmpfor calls to setjmplongjmpfor calls to longjmp that rewind the
	program counter/stack to the location of a previous setjmp call
* throwfor throwing an exception
* catchfor catching an exception
* unwindfor unwinding stack frame(s) during
	exception-handling
* setjmpfor calls to setjmp
* longjmpfor calls to longjmp that rewind the
	program counter/stack to the location of a previous setjmp call
* GCC diagnostics can now have directed graphs associated with them, and
 can also report "global" directed graphs. Graphs are ignored by text sinks,
 but are captured by SARIF sinks, and the "experimental-html" renders any
 such graphs in SVG-based form using dot. For example, settingcfgs=yeson a SARIF or HTML diagnostic sink will enable
 capturing GCC's intermediate representation of every function at every
 optimization pass.
* GCC diagnostics can now refer to logical locations inside XML and JSON
 files (such as via libgdiagnostics). Thesarif-replaytool
 now uses this to provide JSON pointers when it reports on issues in its
 SARIF input.
* IfGCC_DIAGNOSTICS_LOGis set in the environment, GCC's diagnostic subsystem will emit a
 text log to stderr (or a named file) to track what it's doing and the
 decisions it's making (e.g. exactly when and why a diagnostic is being
 rejected).
* IfEXPERIMENTAL_SARIF_SOCKETis set in the environment, GCC will attempt to connect to that socket on
 startup and send JSON-RPC notifications to it for every diagnostic emitted.

## Improvements for plugin authors

* GCC has gained a "publish/subscribe" framework, allowing for
 loosely-coupled senders and receivers, with strongly-typed messages
 passing between them. In this release the only topics for plugins
 to subscribe to are:events relating to optimization passes starting/stopping on particular
	functionsevents relating to the static analyzer
* events relating to optimization passes starting/stopping on particular
	functions
* events relating to the static analyzer
* GCC diagnostic sinks can now haveextensionobjects
 associated with them, with afinalizerhook. Plugins can
 use this to capture additional information in SARIF output files.
* GCC's diagnostic machinery has been substantially cleaned up in GCC 16.
 This should not affect plugins that use just thediagnostic-core.hheader, but maintainers of plugins making
 more sophisticated uses of diagnostics may need to refer to theporting guide.

## Improvements to Static Analyzer

* The analyzer is now usable on simple C++ examples, as it now handles
 C++'s Named Return Value Optimization and has some initial support for
 exceptions. However due to scaling issues it is not likely to be usable
 on production C++ code in this release.
* With the added support for exception-handling,-fanalyzerassumes that a call to an external function not marked with attributenothrowcould throw an exception if-fexceptionsis enabled. GCC 16 adds a new option-fanalyzer-assume-nothrow,
 for disabling this assumption. This is intended as a workaround for
 projects where the exception-handling generates large numbers of new
 warnings, such as C code where-fexceptionsis used for
 interoperability with C++ but where the C APIs in use are unlikely to
 throw exceptions.
* The data structure used by-fanalyzerfor representing
 the user's code has been rewritten in a way that makes it easier to
 understand and debug, and slightly improves locations used when reporting
 diagnostics. This comes at the cost of increasing the memory usage of
 the analyzer.
* The data structure used by-fanalyzerfor simulating the
 contents of memory in the user's program has been reimplemented. The new
 implementation is faster and easier to maintain.
* The analyzer has started to make use of GCC'svalue_rangemachinery, eliminating some false positives.

## Improvements to libgdiagnostics

libgdiagnostics
 has gained 37 entrypoints:

* 5 new entrypoints for working with logical locationsdiagnostic_logical_location_get_kind()diagnostic_logical_location_get_parent()diagnostic_logical_location_get_short_name()diagnostic_logical_location_get_fully_qualified_name()diagnostic_logical_location_get_decorated_name()
* diagnostic_logical_location_get_kind()
* diagnostic_logical_location_get_parent()
* diagnostic_logical_location_get_short_name()
* diagnostic_logical_location_get_fully_qualified_name()
* diagnostic_logical_location_get_decorated_name()
* 2 new entrypoints for supporting command-line options and SARIF playbackdiagnostic_manager_add_sink_from_spec()diagnostic_manager_set_analysis_target()
* diagnostic_manager_add_sink_from_spec()
* diagnostic_manager_set_analysis_target()
* 12 new entrypoints for working with directed graphs:diagnostic_manager_new_graph()diagnostic_manager_take_global_graph()diagnostic_take_graph()diagnostic_graph_release()diagnostic_graph_set_description()diagnostic_graph_add_node()diagnostic_graph_add_edge()diagnostic_graph_get_node_by_id()diagnostic_graph_get_edge_by_id()diagnostic_node_set_label()diagnostic_node_set_location()diagnostic_node_set_logical_location()
* diagnostic_manager_new_graph()
* diagnostic_manager_take_global_graph()
* diagnostic_take_graph()
* diagnostic_graph_release()
* diagnostic_graph_set_description()
* diagnostic_graph_add_node()
* diagnostic_graph_add_edge()
* diagnostic_graph_get_node_by_id()
* diagnostic_graph_get_edge_by_id()
* diagnostic_node_set_label()
* diagnostic_node_set_location()
* diagnostic_node_set_logical_location()
* 17 new entrypoints for building up text for a diagnostic via a buffer:diagnostic_message_buffer_new()diagnostic_message_buffer_release()diagnostic_message_buffer_append_str()diagnostic_message_buffer_append_text()diagnostic_message_buffer_append_byte()diagnostic_message_buffer_append_printf()diagnostic_message_buffer_append_event_id()diagnostic_message_buffer_begin_url()diagnostic_message_buffer_end_url()diagnostic_message_buffer_begin_quote()diagnostic_message_buffer_end_quote()diagnostic_message_buffer_begin_color()diagnostic_message_buffer_end_color()diagnostic_message_buffer_dump()diagnostic_finish_via_msg_buf()diagnostic_add_location_with_label_via_msg_buf()diagnostic_execution_path_add_event_via_msg_buf()
* diagnostic_message_buffer_new()
* diagnostic_message_buffer_release()
* diagnostic_message_buffer_append_str()
* diagnostic_message_buffer_append_text()
* diagnostic_message_buffer_append_byte()
* diagnostic_message_buffer_append_printf()
* diagnostic_message_buffer_append_event_id()
* diagnostic_message_buffer_begin_url()
* diagnostic_message_buffer_end_url()
* diagnostic_message_buffer_begin_quote()
* diagnostic_message_buffer_end_quote()
* diagnostic_message_buffer_begin_color()
* diagnostic_message_buffer_end_color()
* diagnostic_message_buffer_dump()
* diagnostic_finish_via_msg_buf()
* diagnostic_add_location_with_label_via_msg_buf()
* diagnostic_execution_path_add_event_via_msg_buf()
* diagnostic_manager_set_debug_physical_locations()

## Other significant improvements

## GCC 16.1

This is thelist
of problem reports (PRs)from GCC's bug tracking system that are
known to be fixed in the 16.1 release. This list might not be
complete (that is, it is possible that some PRs that have been fixed
are not listed here).

For questions related to the use of GCC,
please consult these web pages and the

GCC manuals
. If that fails,
the 
gcc-help@gcc.gnu.org

mailing list might help.
Comments on these web pages and the development of GCC are welcome on our
developer list at 
gcc@gcc.gnu.org
.
All of 
our lists

have public archives.

Copyright (C)Free Software Foundation, Inc.Verbatim copying and distribution of this entire article is
permitted in any medium, provided this notice is preserved.

These pages aremaintained by the GCC team.
Last modified 2026-04-30.