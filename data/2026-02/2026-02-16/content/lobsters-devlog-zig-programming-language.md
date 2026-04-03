---
title: Devlog ⚡ Zig Programming Language
url: https://ziglang.org/devlog/2026/?20260213#2026-02-13
site_name: lobsters
content_file: lobsters-devlog-zig-programming-language
fetched_at: '2026-02-16T06:00:25.260650'
original_url: https://ziglang.org/devlog/2026/?20260213#2026-02-13
date: '2026-02-16'
tags: zig
---

# Devlog

This page contains a curated list of recent changes to main branch Zig.

Also available as anRSS feed.

This page contains entries for the year2026. Other years are available inthe Devlog archive page.

February 13, 2026

# io_uring and Grand Central Dispatch std.Io implementations landed

Author: Andrew Kelley

As we approach the end of the 0.16.0 release cycle, Jacob has been hard at work, bringingstd.Io.Eventedup to speed with all the latest API changes:

* io_uring implementation
* Grand Central Dispatch implementation

Both of these are based on userspace stack switching, sometimes called “fibers”, “stackful coroutines”, or “green threads”.

They are nowavailable to tinker with, by constructing one’s application usingstd.Io.Evented. They should be consideredexperimentalbecause there is important followup work to be done before they can be used reliably and robustly:

* better error handling
* remove the logging
* diagnose the unexpected performance degradation when usingIoMode.eventedfor the compiler
* a couple functions still unimplemented
* more test coverage is needed
* builtin function to tell you the maximum stack size of a given functionto make these implementations practical to use when overcommit is off.

With those caveats in mind, it seems we are indeed reaching the Promised Land, where Zig code can have Io implementations effortlessly swapped out:

const

std

=

@import
(
"std"
)
;

pub

fn

main
(
init
:

std
.
process
.
Init
.
Minimal
)

!
void

{


var

debug_allocator
:

std
.
heap
.
DebugAllocator
(
.
{
}
)

=

.
init
;


const

gpa

=

debug_allocator
.
allocator
(
)
;


var

threaded
:

std
.
Io
.
Threaded

=

.
init
(
gpa
,

.
{


.
argv0

=

.
init
(
init
.
args
)
,


.
environ

=

init
.
environ
,


}
)
;


defer

threaded
.
deinit
(
)
;


const

io

=

threaded
.
io
(
)
;


return

app
(
io
)
;

}

fn

app
(
io
:

std
.
Io
)

!
void

{


try

std
.
Io
.
File
.
stdout
(
)
.
writeStreamingAll
(
io
,

"Hello, World!
\n
"
)
;

}

$ strace ./hello_threaded
execve("./hello_threaded", ["./hello_threaded"], 0x7ffc1da88b20 /* 98 vars */) = 0
mmap(NULL, 262207, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f583f338000
arch_prctl(ARCH_SET_FS, 0x7f583f378018) = 0
prlimit64(0, RLIMIT_STACK, NULL, {rlim_cur=8192*1024, rlim_max=RLIM64_INFINITY}) = 0
prlimit64(0, RLIMIT_STACK, {rlim_cur=16384*1024, rlim_max=RLIM64_INFINITY}, NULL) = 0
sigaltstack({ss_sp=0x7f583f338000, ss_flags=0, ss_size=262144}, NULL) = 0
sched_getaffinity(0, 128, [0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31]) = 8
rt_sigaction(SIGIO, {sa_handler=0x1019d90, sa_mask=[], sa_flags=SA_RESTORER, sa_restorer=0x10328c0}, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGPIPE, {sa_handler=0x1019d90, sa_mask=[], sa_flags=SA_RESTORER, sa_restorer=0x10328c0}, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
writev(1, [{iov_base="Hello, World!\n", iov_len=14}], 1Hello, World!
) = 14
rt_sigaction(SIGIO, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=SA_RESTORER, sa_restorer=0x10328c0}, NULL, 8) = 0
rt_sigaction(SIGPIPE, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=SA_RESTORER, sa_restorer=0x10328c0}, NULL, 8) = 0
exit_group(0) = ?
+++ exited with 0 +++

Swapping out only the I/O implementation:

const

std

=

@import
(
"std"
)
;

pub

fn

main
(
init
:

std
.
process
.
Init
.
Minimal
)

!
void

{


var

debug_allocator
:

std
.
heap
.
DebugAllocator
(
.
{
}
)

=

.
init
;


const

gpa

=

debug_allocator
.
allocator
(
)
;


var

evented
:

std
.
Io
.
Evented

=

undefined
;


try

evented
.
init
(
gpa
,

.
{


.
argv0

=

.
init
(
init
.
args
)
,


.
environ

=

init
.
environ
,


.
backing_allocator_needs_mutex

=

false
,


}
)
;


defer

evented
.
deinit
(
)
;


const

io

=

evented
.
io
(
)
;


return

app
(
io
)
;

}

fn

app
(
io
:

std
.
Io
)

!
void

{


try

std
.
Io
.
File
.
stdout
(
)
.
writeStreamingAll
(
io
,

"Hello, World!
\n
"
)
;

}

execve("./hello_evented", ["./hello_evented"], 0x7fff368894f0 /* 98 vars */) = 0
mmap(NULL, 262215, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f70a4c28000
arch_prctl(ARCH_SET_FS, 0x7f70a4c68020) = 0
prlimit64(0, RLIMIT_STACK, NULL, {rlim_cur=8192*1024, rlim_max=RLIM64_INFINITY}) = 0
prlimit64(0, RLIMIT_STACK, {rlim_cur=16384*1024, rlim_max=RLIM64_INFINITY}, NULL) = 0
sigaltstack({ss_sp=0x7f70a4c28008, ss_flags=0, ss_size=262144}, NULL) = 0
sched_getaffinity(0, 128, [0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31]) = 8
mmap(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f70a4c27000
mmap(0x7f70a4c28000, 548864, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f70a4ba1000
io_uring_setup(64, {flags=IORING_SETUP_COOP_TASKRUN|IORING_SETUP_SINGLE_ISSUER, sq_thread_cpu=0, sq_thread_idle=1000, sq_entries=64, cq_entries=128, features=IORING_FEAT_SINGLE_MMAP|IORING_FEAT_NODROP|IORING_FEAT_SUBMIT_STABLE|IORING_FEAT_RW_CUR_POS|IORING_FEAT_CUR_PERSONALITY|IORING_FEAT_FAST_POLL|IORING_FEAT_POLL_32BITS|IORING_FEAT_SQPOLL_NONFIXED|IORING_FEAT_EXT_ARG|IORING_FEAT_NATIVE_WORKERS|IORING_FEAT_RSRC_TAGS|IORING_FEAT_CQE_SKIP|IORING_FEAT_LINKED_FILE|IORING_FEAT_REG_REG_RING|IORING_FEAT_RECVSEND_BUNDLE|IORING_FEAT_MIN_TIMEOUT|IORING_FEAT_RW_ATTR|IORING_FEAT_NO_IOWAIT, sq_off={head=0, tail=4, ring_mask=16, ring_entries=24, flags=36, dropped=32, array=2112, user_addr=0}, cq_off={head=8, tail=12, ring_mask=20, ring_entries=28, overflow=44, cqes=64, flags=40, user_addr=0}}) = 3
mmap(NULL, 2368, PROT_READ|PROT_WRITE, MAP_SHARED|MAP_POPULATE, 3, 0) = 0x7f70a4ba0000
mmap(NULL, 4096, PROT_READ|PROT_WRITE, MAP_SHARED|MAP_POPULATE, 3, 0x10000000) = 0x7f70a4b9f000
io_uring_enter(3, 1, 1, IORING_ENTER_GETEVENTS, NULL, 8Hello, World!
) = 1
io_uring_enter(3, 1, 1, IORING_ENTER_GETEVENTS, NULL, 8) = 1
munmap(0x7f70a4b9f000, 4096) = 0
munmap(0x7f70a4ba0000, 2368) = 0
close(3) = 0
munmap(0x7f70a4ba1000, 548864) = 0
exit_group(0) = ?
+++ exited with 0 +++

Key point here being that theappfunction is identical between those two snippets.

Moving beyond Hello World, the Zig compiler itself works fine usingstd.Io.Evented, both with io_uring and with GCD, but as mentioned above, there is a not-yet-diagnosed performance degradation when doing so.

Happy hacking,

Andrew

February 06, 2026

# Two Package Management Workflow Enhancements

Author: Andrew Kelley

If you have a Zig project with dependencies, two big changes just landed which I think you will be interested to learn about.

Fetched packages are now storedlocallyin thezig-pkgdirectory of the project root (next to yourbuild.zigfile).

For example here are a few results fromaweboafter runningzig build:

$ du -sh zig-pkg/*
13M freetype-2.14.1-alzUkTyBqgBwke4Jsot997WYSpl207Ij9oO-2QOvGrOi
20K opus-0.0.2-vuF-cMAkAADVsm707MYCtPmqmRs0gzg84Sz0qGbb5E3w
4.3M pulseaudio-16.1.1-9-mk_62MZkNwBaFwiZ7ZVrYRIf_3dTqqJR5PbMRCJzSuLw
5.2M uucode-0.1.0-ZZjBPvtWUACf5dqD_f9I37VGFsN24436CuceC5pTJ25n
728K vaxis-0.5.1-BWNV_AxECQCj3p4Hcv4U3Yo1WMUJ7Z2FUj0UkpuJGxQQ

It is highly recommended to add this directory to the project-local source control ignore file (e.g..gitignore). However, by being outside of.zig-cache, it provides the possibility of distributing self-contained source tarballs, which contain all dependencies and therefore can be used to build offline, or for archival purposes.

Meanwhile, anadditionalcopy of the dependency is cached globally. After filtering out all the unused files based on thepathsfilter, the contents are recompressed:

$ du -sh ~/.cache/zig/p/*
2.4M freetype-2.14.1-alzUkTyBqgBwke4Jsot997WYSpl207Ij9oO-2QOvGrOi.tar.gz
4.0K opus-0.0.2-vuF-cMAkAADVsm707MYCtPmqmRs0gzg84Sz0qGbb5E3w.tar.gz
636K pulseaudio-16.1.1-9-mk_62MZkNwBaFwiZ7ZVrYRIf_3dTqqJR5PbMRCJzSuLw.tar.gz
880K uucode-0.1.0-ZZjBPvtWUACf5dqD_f9I37VGFsN24436CuceC5pTJ25n.tar.gz
120K vaxis-0.5.1-BWNV_BFECQBbXeTeFd48uTJRjD5a-KD6kPuKanzzVB01.tar.gz

The motivation for this change is to make it easier to tinker. Go ahead and edit those files, see what happens. Swap out your package directory with a git clone. Grep your dependencies all together. Configure your IDE to auto-complete based on thezig-pkgdirectory.Run baobab on your dependency tree. Furthermore, by having the global cache have compressed files instead makes it easier to share that cached data between computers. In the future,it is planned to support peer-to-peer torrenting of dependency trees. By recompressing packages into a canonical form, this will allow peers to share Zig packages with minimal bandwidth. I love this idea because it simultaneously provides resilience to network outages, as well as a popularity contest. Find out which open source packages are popular based on number of seeders!

The second change here is the addition of the--forkflag tozig build.

In retrospect, it seems so obvious, I don’t know why I didn’t think of it since the beginning. It looks like this:

zig build --fork=[path]

This is aproject overrideoption. Given a path to a source checkout of a project, all packages matching that project across the entire dependency tree will be overridden.

Thanks to the fact that package content hashes include name and fingerprint,this resolves before the package is potentially fetched.

This is an easy way to temporarily use one or more forks which are in entirely separate directories. You can iterate on your entire dependency tree until everything is working, while using comfortably the development environment and source control of the dependency projects.

The fact that it is a CLI flag makes it appropriately ephemeral. The moment you drop the flags, you’re back to using your pristine, fetched dependency tree.

If the project does not match, an error occurs, preventing confusion:

$ zig build --fork=/home/andy/dev/mime
error: fork /home/andy/dev/mime matched no mime packages
$

If the project does match, you get a reminder that you are using a fork, preventing confusion:

$ zig build --fork=/home/andy/dev/dvui
info: fork /home/andy/dev/dvui matched 1 (dvui) packages
...

This functionality is intended to enhance the workflow of dealing with ecosystem breakage. I already tried it a bit and found it to be quite pleasant to work with. The new workflow goes like this:

1. Fail to build from source due to ecosystem breakage.
2. Tinker with--forkuntil your project works again. During this time you can use the actual upstream source control, test suite,zig build test --watch -fincremental, etc.
3. Now you have a new option: be selfish and just keep working on your own stuff, or you can proceed to submit your patches upstream.

…and you can probably skip the step where you switch yourbuild.zig.zonto your fork unless you expect upstream to take a long time to merge your fixes.

February 03, 2026

# Bypassing Kernel32.dll for Fun and Nonprofit

Author: Andrew Kelley

The Windows operating system provides a large ABI surface area for doing things in the kernel. However, not all ABIs are created equally. As Casey Muratori points out in his lecture,The Only Unbreakable Law, the organizational structure of software development teams has a direct impact on the structure of the software they produce.

The DLLs on Windows are organized into a heirarchy, with some of the APIs being high-level wrappers around lower-level ones. For example, whenever you call functions ofkernel32.dll, ultimately, the actual work is done byntdll.dll. You can observe this directly by using ProcMon.exe and examining stack traces.

What we’ve learned empirically is that the ntdll APIs are generally well-engineered, reasonable, and powerful, but the kernel32 wrappers introduce unnecessary heap allocations, additional failure modes, unintentional CPU usage, and bloat.

This is why the Zig standard library policy is toPrefer the Native API over Win32. We’re not quite there yet - we have plenty of calls into kernel32 remaining - but we’ve taken great strides recently. I’ll give you two examples.

## Example 1: Entropy

According to the official documentation, Windows does not have a straightforward way to get random bytes.

Many projects including Chromium, boringssl, Firefox, and RustcallSystemFunction036fromadvapi32.dllbecause it worked on versions older than Windows 8.

Unfortunately, starting with Windows 8, the first time you call this function, it dynamically loadsbcryptprimitives.dlland callsProcessPrng. If loading the DLL fails (for example due to an overloaded system, which we have observed on Zig CI several times), it returns error 38 (from a function that hasvoidreturn type and is documented to never fail).

The first thingProcessPrngdoes is heap allocate a small, constant number of bytes. If this fails it returnsNO_MEMORYin aBOOL(documented behavior is to never fail, and always returnTRUE).

bcryptprimitives.dllapparently also runs a test suite every time you load it.

All thatProcessPrngisreallydoing isNtOpenFileon"\\Device\\CNG"and reading 48 bytes withNtDeviceIoControlFileto get a seed, and then initializing a per-CPU AES-based CSPRNG.

So the dependency onbcryptprimitives.dllandadvapi32.dllcan both be avoided, and the nondeterministic failure and latencies on first RNG read can also be avoided.

## Example 2: NtReadFile and NtWriteFile

ReadFilelooks like this:

pub

extern

"kernel32"

fn

ReadFile
(


hFile
:

HANDLE
,


lpBuffer
:

LPVOID
,


nNumberOfBytesToRead
:

DWORD
,


lpNumberOfBytesRead
:

?
*
DWORD
,


lpOverlapped
:

?
*
OVERLAPPED
,

)

callconv
(
.
winapi
)

BOOL
;

NtReadFilelooks like this:

pub

extern

"ntdll"

fn

NtReadFile
(


FileHandle
:

HANDLE
,


Event
:

?
HANDLE
,


ApcRoutine
:

?
*
const

IO_APC_ROUTINE
,


ApcContext
:

?
*
anyopaque
,


IoStatusBlock
:

*
IO_STATUS_BLOCK
,


Buffer
:

*
anyopaque
,


Length
:

ULONG
,


ByteOffset
:

?
*
const

LARGE_INTEGER
,


Key
:

?
*
const

ULONG
,

)

callconv
(
.
winapi
)

NTSTATUS
;

As a reminder,the above function is implemented by calling the below function.

Already we can see some nice things about using the lower level API. For instance, therealAPI simply gives us the error code as the return value, while the kernel32 wrapper hides the status code somewhere, returns aBOOLand then requires you to callGetLastErrorto find out what went wrong. Imagine! Returning a value from a function 🌈

Furthermore,OVERLAPPEDis a fake type. The Windows kernel doesn’t actually know or care about it at all! The actual primitives here are events, APCs, andIO_STATUS_BLOCK.

If you have a synchronous file handle, thenEventandApcRoutinemust benull. You get the answer in theIO_STATUS_BLOCKimmediately. If you pass an APC routine here then some old bitrotted 32-bit code runs and you get garbage results.

On the other hand if you have an asynchronous file handle, then you need to either use anEventor anApcRoutine.kernel32.dlluses events, which means that it’s doing extra, unnecessary resource allocation and management just to read from a file. Instead, Zig now passes an APC routine and then callsNtDelayExecution. This integrates seamlessly with cancelation, making it possible to cancel tasks while they perform file I/O, regardless of whether the file was opened in synchronous mode or asynchronous mode.

For a deeper dive into this topic, please refer to this issue:

Windows: Prefer the Native API over Win32

January 31, 2026

# zig libc

Author: Andrew Kelley

Over the past month or so, several enterprising contributors have taken an interest in thezig libc subproject. The idea here is to incrementally delete redundant code, by providing libc functions as Zig standard library wrappers rather than as vendored C source files. In many cases, these functions are one-to-one mappings, such asmemcpyoratan2, or trivially wrap a generic function, likestrnlen:

fn

strnlen
(
str
:

[
*
:
0
]
const

c_char
,

max
:

usize
)

callconv
(
.
c
)

usize

{


return

std
.
mem
.
findScalar
(
u8
,

@ptrCast
(
str
[
0
..
max
]
)
,

0
)

orelse

max
;

}

So far, roughly 250 C source files have been deleted from the Zig repository, with 2032 remaining.

With each function that makes the transition, Zig gains independence from third party projects and from the C programming language, compilation speed improves, Zig’s installation size is simplified and reduced, and user applications which statically link libc enjoy reduced binary size.

Additionally, arecent enhancementnow makes zig libc share the Zig Compilation Unit with other Zig code rather than being a separate static archive, linked together later. This is one of the advantages of Zig having an integrated compiler and linker. When the exported libc functions share the ZCU, redundant code is eliminated because functions can be optimized together. It’s kind of like enabling LTO (Link-Time Optimization) across the libc boundary, except it’s done properly in the frontend instead of too late, in the linker.

Furthermore, when this work is combined with the recentstd.Io changes, there is potential for users to seamlessly control how libc performs I/O - for example forcing all calls toreadandwriteto participate in an io_uring event loop, even though that code was not written with such use case in mind. Or,resource leak detectioncould be enabled for third-party C code. For now this is only a vaporware idea which has not been experimented with, but the idea intrigues me.

Big thanks to Szabolcs Nagy forlibc-test. This project has been a huge help in making sure that we don’t regress any math functions.

As a reminder to our users, now that Zig is transitioning to being the static libc provider, if you encounter issues with the musl, mingw-w64, or wasi-libc libc functionality provided by Zig,please file bug reports in Zig firstso we don’t annoy maintainers for bugs that are in Zig, and no longer vendored by independent libc implementation projects.

The very same day I sat at home writing this devlog like a coward, less than five miles away,armed forces who are in my city against the will of our elected officials shot tear gas, unprovoked, at peaceful protestors. Next time I hope to have the courage to join my neighbors, and I hope to not get shot likeAlex PrettiandRenée Good.
