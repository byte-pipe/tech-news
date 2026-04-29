---
title: Bugs Rust Won't Catch | corrode Rust Consulting
url: https://corrode.dev/blog/bugs-rust-wont-catch/
site_name: hackernews_api
content_file: hackernews_api-bugs-rust-wont-catch-corrode-rust-consulting
fetched_at: '2026-04-29T20:09:24.492020'
original_url: https://corrode.dev/blog/bugs-rust-wont-catch/
author: Corrode Rust Consulting
date: '2026-04-29'
description: In April 2026, Canonical disclosed 44 CVEs in uutils, the Rust reimplementation of GNU coreutil…
tags:
- hackernews
- trending
---

## Idiomatic Rust

# Bugs Rust Won't Catch

by Matthias Endler

 
 Published: 2026-04-29
 
 

In April 2026, Canonicaldisclosed 44 CVEsin uutils, the Rust reimplementation of GNU coreutils that ships by default since 25.10. Most of them came out of an external audit commissioned ahead of the 26.04 LTS.

I read through the list and thought there’s a lot to learn from it.

What’s notable is that all of these bugs landed in a production Rust codebase, written by people who knew what they were doing, and none of them were caught by the borrow checker,clippy lints, orcargo audit.

I’m not writing this to criticize the uutils team. Quite the contrary; I actually want to thank them for sharing the audit results in such detail so that we can all learn from them.

We also hadJon Seager, VP Engineering for Ubuntu, on our ‘Rust in Production’ podcast recentlyand a lot of listeners appreciated his honesty about the state of Rust at Canonical.

If you write systems code in Rust, this is the most concentrated look at where Rust’s safety ends that you’ll likely find anywhere right now.

## Don’t Trust a Path Across Two Syscalls

This is the largest cluster of bugs in the audit. It’s also the reasoncp,mv, andrmarestillGNU in Ubuntu 26.04 LTS. :(

The pattern is always the same. You do one syscall tochecksomething about a path, then another syscall toacton the same path. Between those two calls, an attacker with write access to a parent directory can swap the path component for a symbolic link. The kernel re-resolves the path from scratch on the second call, and the privileged action lands on the attacker’s chosen target.

Rust’s standard library makes this easy to get wrong. The ergonomic APIs you reach for first (fs::metadata,File::create,fs::remove_file,fs::set_permissions) all take a path and re-resolve it every time, rather than taking a file descriptor and operating relative to that.
That’s fine for a normal program, but if you’re writing a privileged tool that needs to be secure against local attackers, you have to be careful.

### Case Study: CVE-2026-35355

Here’s the bug, simplified fromsrc/uu/install/src/install.rs.

// 1. Clear the destination

fs
::
remove_file
(to)
?
;

// ...

// 2. Create the destination. The path is re-resolved here!

let mut
 dest
 =
 File
::
create
(to)
?
;
 // follows symlinks, truncates

copy
(from,
 &mut
 dest)
?
;

Between step 1 and step 2, anyone with write access to the parent directory can planttoas a symlink to, say,/etc/shadow. ThenFile::createfollows the symlink and the privileged process happily overwrites/etc/shadowwith whateverfromhappened to contain.

The fix usesOpenOptions::create_new(true):

fs
::
remove_file
(to)
?
;

let mut
 dest
 =
 OpenOptions
::
new
()

 .
write
(
true
)

 .
create_new
(
true
)

 .
open
(to)
?
;

copy
(from,
 &mut
 dest)
?
;

The docs forcreate_newsay (emphasis mine):

No file is allowed to exist at the target location,also no (dangling) symlink. In this way, if the call succeeds, the file returned is guaranteed to be new.

### Rule: Anchor on a File Descriptor Instead

A&Pathin Rustlookslike a value, but remember that to the kernel it’s just a name. That name can point to different things from one syscall to the next.
Anchor your operations on a file descriptor instead.

create_new()only helps with that when you’re creating a new file. For everything else, open the parent directory once and workrelative to that handle.

If you act on the same path twice, assume it’s a TOCTOU (Time Of Check To Time Of Use) bug until you’ve proven otherwise.

## Set Permissions at Creation Time, Not After

This is a close relative of TOCTOU. You want a directory with restrictive permissions, so you write something like this.

// Create with default permissions

fs
::
create_dir
(
&
path)
?
;

// Fix up permissions

fs
::
set_permissions
(
&
path, Permissions
::
from_mode
(
0o700
))
?
;

For a brief moment,pathexists with the default permissions. Any other user on the system canopen()it during that window. Once they have a file descriptor, the laterchmoddoesn’t take it away from them.

### Rule: Set Permissions at Creation, Never After

Reach forOpenOptions::mode()andDirBuilderExt::mode()so the file or directory is born with the permissions you want. The kernel will apply yourumaskon top, so set that explicitly too if you really care.

## String Equality on Paths Is Not the Same as Filesystem Identity

The original--preserve-rootcheck inchmodwas literally this:

if
 recursive
 &&
 preserve_root
 &&
 file
 ==
 Path
::
new
(
"/"
) {

 return
 Err
(
PreserveRoot
);

}

That comparison is bypassed by anything thatresolvesto/but isn’t spelled/. So/../,/./,/usr/.., or a symlink that points to/. Runchmod -R 000 /../and see it rip right past your check and lock down the whole system.

Here’sthe fix:

fn
 is_root
(file
: &
Path
)
 ->
 bool
 {

 matches!
(fs
::
canonicalize
(file),
 Ok
(p)
 if
 p
 ==
 Path
::
new
(
"/"
))

}

if
 recursive
 &&
 preserve_root
 &&
 is_root
(file) {

 return
 Err
(
PreserveRoot
);

}

### Rule: Resolve Paths Before Comparing Them

canonicalizeresolves..,., and symlinks into a real absolute path. That’s a lot better than string comparison.

Oh and if you were wondering about this line:

matches!
(fs
::
canonicalize
(file),
 Ok
(p)
 if
 p
 ==
 Path
::
new
(
"/"
))

I think that’s just a fancy way of saying

// First, resolve the path to its canonical form

if let
 Ok
(p)
 =
 fs
::
canonicalize
(file) {

 // If that succeeded, check if the canonical path is "/"

 p
 ==
 Path
::
new
(
"/"
)

}
 else
 {

 false

}

In the specific case of--preserve-root, this works because/has no parent directory, so there’s nothing for an attacker to swap from underneath you. In the more general case of comparing two arbitrary paths for filesystem identity, however, you’d want to open both and compare their(dev, inode)pairs, the way GNU coreutils does. (Think identity, not string equality.)

By the way, my favorite bug in this group is CVE-2026-35363:

rm
 .
 # ❌

rm
 ..
 # ❌

rm
 ./
 # ✅ 

rm
 .///
 # ✅ 

It refused.and..but happily accepted./and.///, then deleted the current directory while printingInvalid input. 😅

## Stay in Bytes at Unix Boundaries

Rust’sStringand&strare always UTF-8.
That’s a great choice in 99% of all cases, but Unix paths, environment variables, arguments, and the inputs flowing through tools likecut,comm, andtrlive in the messy world of bytes.

Every time a Rust program bridges that gap, it has three options.

1. 🫩Lossy conversionwithfrom_utf8_lossysilently rewrites invalid bytes to U+FFFD. That’s just fancy data corruption.
2. 🫤Strict conversionwithunwrapor?crashes or refuses to operate.
3. 😚Staying in byteswithOsStror&[u8]is what you should usually do.

The audit found bugs in both of the first two categories. Here’s an example.

### Case Study:comm(CVE-2026-35346)

This is the original code, fromsrc/uu/comm/src/comm.rs.

// ra, rb are &[u8], raw bytes from the input files.

print!
(
"{}"
,
 String
::
from_utf8_lossy
(ra));

print!
(
"{delim}{}"
,
 String
::
from_utf8_lossy
(rb));

GNUcommworks on binary files because it just shuffles bytes around. The uutils version replaced anything that wasn’t valid UTF-8 withU+FFFD, which silently corrupted the output.

Here’s the fix: stay in bytes.

let mut
 out
 =
 BufWriter
::
new
(io
::
stdout
()
.
lock
());

out
.
write_all
(ra)
?
;

out
.
write_all
(delim)
?
;

out
.
write_all
(rb)
?
;

print!forces a UTF-8 round-trip throughDisplay.Write::write_alldoes not.
It writes the raw bytes directly tostdout.

### Rule: Pick the Right Type for the Situation

For Unix-flavored systems code, usePathandPathBuffor filesystem paths,OsStringfor environment variables, andVec<u8>or&[u8]for stream contents. It’s tempting to round-trip them throughStringfor easier formatting, but that’s where the corruption creeps in.

UTF-8 is a great default for application strings, but it’s absolutely, positively the wrong default for the raw byte stuff Unix tools work with.

## Treat Everypanic!as a Denial of Service

In a CLI, everyunwrap, everyexpect, every slice index, every unchecked arithmetic operation, everyfrom_utf8is a potential denial of service if an attacker can shape the input.
That’s because apanic!unwinds the stack and aborts the process. If your tool is running in a cron job, a CI pipeline, or a shell script, that means the whole thing just stops working. Even worse, you could find yourself in a crash loop that paralyzes the entire system.

A canonical case from the audit wassort --files0-from(CVE-2026-35348). The flag reads a NUL-separated list of filenames from a file, but the parser calledexpect()on a UTF-8 conversion of each name:

// Inside sort.rs, simplified

let
 path
 =
 std
::
str
::
from_utf8
(bytes)

 .
expect
(
"Could not parse string from zero terminated input."
);

GNUsorttreats filenames as raw bytes, the way the kernel does. The uutils version required UTF-8 and aborted the whole process on the first non-UTF-8 path:

$ python3 -c "open('list0','wb').write(b'weird\xffname\0')"

$ coreutils sort --files0-from=list0

thread 'main' panicked at uu_sort-0.2.2/src/sort.rs:1076:18:

Could not parse string from zero terminated input.: Utf8Error { valid_up_to: 5, error_len: Some(1) }

note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

(I reproduced this againstcoreutils 0.2.2on macOS. The Python one-liner is there because most modern shells refuse to create a non-UTF-8 filename for you.)

Your nightly cron job is dead and there goes your weekend.

### Rule: Turn Bad Input Into Errors, Not Panics

In code that processes untrusted input, treat everyunwrap,expect, indexing, orascast as a CVE waiting to be filed. Use?,get,checked_*,try_from, and surface a real error. Push back on the boundary of your application and let the caller deal with the fallout.

A good lint baseline to catch this in CI:

[
lints
.
clippy
]

unwrap_used
 =
 "
warn
"

expect_used
 =
 "
warn
"

panic
 =
 "
warn
"

indexing_slicing
 =
 "
warn
"

arithmetic_side_effects
 =
 "
warn
"

These are noisy in test code where panicking on bad data is exactly what you want. The cleanest way to scope them to non-test code is to put#![cfg_attr(test, allow(clippy::unwrap_used, clippy::expect_used, clippy::panic, clippy::indexing_slicing, clippy::arithmetic_side_effects))]at the top of each crate root, or to gate#[allow(...)]on the individual#[cfg(test)]modules.

## Propagate Errors, Don’t Discard Them

Closely related to the previous point, a few CVEs come from ignoring or losing error information.

chmod -Randchown -Rreturned the exit code of thelastfile processed instead of the worst one. Sochmod -R 600 /etc/secrets/*could fail on half the files and still exit0. Your script thinks everything is fine.

ddcalledResult::ok()on itsset_len()call to mimic GNU’s behavior on/dev/null. The intent was reasonable, but that same code ran for regular files too, so a full disk silently produced a half-written destination.

The reason was that someone wanted to throw away aResultand reached for.ok(),.unwrap_or_default(), orlet _ =.

### Rule: Don’t Throw Away Meaningful Error Information

Here’s a very simple pattern to avoid that:

// Don't bail on the first error, but remember the worst one.

let mut
 worst
 =
 0
;

for
 file
 in
 files {

 if let
 Err
(e)
 =
 chmod_one
(file) {

 worst
 =
 worst
.
max
(e
.
exit_code
());

 }

}

process
::
exit
(worst);

Also, if you write.ok()to discard aResult, leave a comment that explainswhythis specific failure is safe to ignore.

## Match the Original Tool’s Behavior Exactly

A surprising number of these CVEs aren’t “the code does something unsafe” but “the code does somethingdifferentfrom GNU, and a shell script somewhere relied on the GNU behavior.”

The clearest example iskill -1(CVE-2026-35369). GNU reads-1as “signal 1” and asks for a PID. uutils read it as “send the default signal to PID -1”, which on Linux meansevery process you can see. Yikes!

A typo becomes a system-wide kill switch.

### Rule: Bug-for-Bug Compatibility Is A Safety Feature

If you reimplement a battle-tested tool, bug-for-bug compatibility on exit codes, error messages, edge cases, and option semantics is a security feature. (Hello,Hyrum’s Law– and obligatoryXKCD 1172!)

Anywhere your behavior diverges from the original, somebody’s shell script is making a wrong decision.

uutils now runs the upstream GNU coreutils test suite against itself in CI. That’s the right scale of defense for this class of bug.

## Resolve Inputs Before Crossing a Trust Boundary

CVE-2026-35368is the worst single bug in the audit. It’s local root code execution inchroot. The bug is visible if you know what to look for (achrootfollowed by a function call that loads a dynamic library), but it’s the kind of thing that doesn’t jump out on a first read.

Here’s the pattern, simplified from thechrootutility.

chroot
(new_root)
?
;

// Still uid 0, but now inside the attacker-controlled filesystem.

let
 user
 =
 get_user_by_name
(name)
?
;

setgid
(user
.
gid
())
?
;

setuid
(user
.
uid
())
?
;

exec
(cmd)
?
;

Huh. Looks innocent.

The trap is thatget_user_by_nameends up loading shared libraries from thenewroot filesystem to resolve the username. An attacker who can plant a file in the chroot gets to run code as uid 0.

GNUchrootresolves the userbeforecallingchroot. Same fix here.

let
 user
 =
 get_user_by_name
(name)
?
;

chroot
(new_root)
?
;

setgid
(user
.
gid
())
?
;

setuid
(user
.
uid
())
?
;

exec
(cmd)
?
;

### Rule: Resolve Before You Cross

Once you’re across, every library call might run the attacker’s code. And no, static compilation doesn’t help here, becauseget_user_by_namegoes through NSS, whichdlopenslibnss_*modules at runtime regardless of whether your binary is statically linked.

## What RustDidPrevent

You might have made it this far and thought “Wow, that’s a lot of bugs! Maybe Rust isn’t as safe as I thought?”

That would be the wrong conclusion.

Keep in mind that none of the following bad things happened:

* No buffer overflows.
* No use-after-free.
* No double-free.
* No data races on shared mutable state.
* No null-pointer dereferences.
* No uninitialized memory reads.

That means, even if the tools were (and probably still are) buggy, they never had a bug that could be exploited to read arbitrary memory.

GNU coreutils has shipped CVEs in every single one of those categories. Take a peek at the last few years of the GNUNEWSfile:

* pwdbuffer overflow on deep paths longer than2 * PATH_MAX(9.11, 2026)
* numfmtout-of-bounds read on trailing blanks (9.9, 2025)
* unexpand --tabsheap buffer overflow (9.9, 2025)
* od --strings -Nwrites a NUL byte past a heap buffer (9.8, 2025)
* sort1-byte read before a heap buffer with aSIZE_MAXkey offset (9.8, 2025)
* ls -Zandls -lcrashes with SELinux but no xattr support (9.7, 2025)
* split --line-bytesheap overwrite (CVE-2024-0684, 9.5, 2024)
* b2sum --checkreads unallocated memory on malformed input (9.4, 2023)
* tail -fstack buffer overrun with many files and a highulimit -n(9.0, 2021)

…the list goes on and on. The Rust rewrite has shipped zero of these, over a comparable window of activity.1That’smostof what historically goes wrong in a C codebase.

What’s left is, frankly, a more interesting class of bug. It lives at the boundary between our controlled Rust environment and the messy, chaotic outside world, where paths, bytes, strings, and syscalls are all tangled up in one eternal ball of sadness.
That’s the new security boundary of modern systems code.2

If you write systems code in Rust, treat this CVE list as a checklist. Grep your own codebase forfrom_utf8_lossy, strayunwrap()calls, discardedResults,File::create, and string comparisons against"/".

I also wrote a companion post, titledPatterns for Defensive Programming in Rust.

## Correct Rust Is Idiomatic Rust

When I think of “idiomatic Rust”, correctness is not the first thing that comes to mind.
After all, isn’t that the compiler’s job?
Instead, I think of elegantiterator patterns, ergonomic method signatures,immutability, or clever use ofexpressions.
But none of that matters if the code doesn’t do the right thing, and the compiler is far from perfect at enforcing correctness.
That’s why we don’t only have idioms for writing more elegant code; we also have idioms for writing correct code.
They are the distilled experience of a community that has learned, often painfully, which shapes of code survive contact with reality and which ones do not.

Reality is rarely as tidy as the abstractions we would like to impose on it. The mark of robust systems, in any language, is the willingness to reflect that untidiness rather than paper over it. Rust gives us extraordinary tools to do so, and the compiler will hold a great deal for us. But the part it cannot hold, the boundary between our program and everything else, is still ours to get right.
The type system can encode many things, but it cannot encode conditions outside of its control, such as the passage of time between two syscalls.

Idiomatic Rust, then, is not just code that the borrow checker accepts or thatclippyleaves alone. It is code whose types, names, and control flow tell thetruthabout the system they run in. And that truth is sometimes ugly. It could mean using file descriptors instead of paths,OsStrinstead ofString,?instead ofunwrap, and bug-for-bug compatibility over clean semantics. None of it is as pretty as the version you would write on a whiteboard. But it is more honest.

#### Need Help Hardening Your Rust Codebase?

Is your team shipping Rust into production and want to make sure you’re not falling into the same traps?
I offer Rust consulting services, from code reviews and security-focused audits to training your team on the patterns that the compiler won’t enforce for you.Get in touchto learn more.

1. To be fair to GNU: GNU coreutils is 40 years old and has had a very long time to surface and fix this class of bug. And we don’tknowthere are no memory-safety bugs in the Rust rewrite, only that the audit didn’t find any. Still, the difference is noticeable when comparing the same duration of development activity.↩
2. It’s worth noting that thePath/PathBufTOCTOU class of bug is in some wayseasierto avoid in C than in Rust. C code naturally reaches for an open file descriptor and the*atfamily of syscalls (openat,fstatat,unlinkat,mkdirat), and most creation syscalls take amodeargument directly. Rust’s high-levelstd::fsAPIs abstract over the file descriptor and operate on&Pathvalues, which makes the path-based, re-resolving call the path of least resistance. The handle-based APIs exist on every Unix platform; Rust just doesn’t put them front and center.↩

## Additional Resources

* An update on rust-coreutils: Canonical’s announcement of the audit results
* Patterns for Defensive Programming in Rust: companion post on writing more robust Rust code
* Pitfalls of Safe Rust: common mistakes even safe Rust code can make
* Sharp Edges In The Rust Standard Library: surprising behaviors instd
* uutils/coreutils on GitHub: the Rust reimplementation of GNU coreutils

 Published: 2026-04-29
 

Revision history

Author:

Matthias Endler

Editor:

 Simon Brüggen
 

## Idiomatic Rust content. Straight to your inbox.

I regularly write new articles on idiomatic Rust. If you want to be notified
 when I publish them, you should sign up to my newsletter here. No spam.
 Unsubscribe at any time.

Subscribe

 Subscribing...
 

↑ 
Back to top