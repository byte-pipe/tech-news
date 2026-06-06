---
title: Moving beyond fork() + exec() [LWN.net]
url: https://lwn.net/SubscriberLink/1076018/16f01bbbb8e0d1f0/
site_name: hackernews_api
content_file: hackernews_api-moving-beyond-fork-exec-lwnnet
fetched_at: '2026-06-06T19:33:14.228137'
original_url: https://lwn.net/SubscriberLink/1076018/16f01bbbb8e0d1f0/
author: jwilk
date: '2026-06-06'
description: Moving beyond fork() + exec()
tags:
- hackernews
- trending
---

### Welcome to LWN.netThe following subscription-only content has been made available to you 
by an LWN subscriber. Thousands of subscribers depend on LWN for the 
best news from the Linux and free software communities. If you enjoy this 
article, please considersubscribing to LWN. Thank you
for visiting LWN.net!ByJonathan CorbetJune 5, 2026Since the earliest days of Unix, two of the core process-oriented system
calls have beenfork(), which creates a child process as a copy of
the parent, andexec(), which runs a new program in the place of
the current one. In Linux kernels, those system calls are better known asclone()andexecve(),
but the core functionality remains the same. While there is elegance to
this process-creation model, there are shortcomings as well. A recentproposalfrom
Li Chen to add "spawn templates" to the kernel will not be accepted in its
current form, but it may point the way toward a new process-creation
primitive in the future.fork()is a relatively expensive system call; it must copy the
entire process state (including memory) for the child process. Many
optimizations have been made over the years, but a fork is still a
fundamentally costly operation. To make things worse, afork()call is often immediately followed by anexec(), which will
discard all of that memory that was so carefully copied for the child.
Attempts (such asvfork())
have been made over the years to optimize for this case, but the pattern
still is more expensive than it could be.#### Spawn templatesChen's patch set takes an interesting approach to optimize thefork()andexec()pattern. It is focused on applications
that repeatedly launch processes running the same executable; imagine, for
example, a program that must run Git repeatedly to obtain information about
the contents of a repository. In such cases, the program could establish a
template to accelerate those invocations, spreading the setup cost across
multiple operations. This template would be created with thespawn_template_create()system call:struct spawn_template_create_args {
	__aligned_u64 flags;
	__s32 execfd;
	__u32 exec_flags;
	__aligned_u64 filename;
	/* Some fields elided */
 };

 int spawn_template_create(struct spawn_template_create_args *args, size_t args_size);This call will return a file descriptor representing a template for the
executable file, which can be specified as either a file descriptor
(execfd) or an absolute path (filename), but not both.
To create the template, the kernel will open the indicated file and cache a
bunch of information that will allow a process to run that file more
quickly in the future.The application in question may run a given executable many times, but each
invocation is different in a number of ways. The details of a specific
invocation must be placed into an instance of this structure:struct spawn_template_spawn_args {
	__aligned_u64 flags;
	__aligned_u64 pidfd;
	__aligned_u64 argv;
	__aligned_u64 envp;
	__aligned_u64 actions;
	__aligned_u64 actions_len;
	__aligned_u64 reserved[4];
 };Theargvfield is a pointer to the argument list to be passed to
the program, whileenvppoints to its environment. Changes to
file descriptors and signal handling, instead, are passed throughactions, which is a pointer to an array of:struct spawn_template_action {
	__u32 type;
	__u32 flags;
	__s32 fd;
	__s32 newfd;
	__aligned_u64 arg;
 };If, for example, file descriptor four should be closed in the child, the
associatedspawn_template_actionstructure would havetypeset toSPAWN_TEMPLATE_ACTION_CLOSEandfdset to four. Other actions exist for duplicating file descriptors, opening
files, changing the working directory, and changing signal handling.Once thespawn_template_spawn_argsstructure has been filled in,
the new process can be run with:int spawn_template_spawn(int template_fd,
 			 struct spawn_template_spawn_args *args, int args_size);Internally, this system call follows something close to the normalfork()/exec()path. Chen is careful to point out that
all of the normal checks applied when executing a new file remain in place.
But the cached information in the template makes the whole process faster
than it was before.

How much faster? Benchmark results provided in the cover letter show an
improvement of about 2%, which may not seem like a lot, but it may
make a difference for applications that fit the expected pattern.#### Towardposix_spawn()The most detailed review of this work wasposted
by Mateusz Guzik, who said: "This problem is dear to my heart and I
have been pondering it on and off for some time now. The entire fork + exec
idiom is terrible and needs to be retired". He pointed out that the
focus of the patch set was a bit strange in that it left thefork()part of the problem untouched. That is where most of the
cost lies, he said, so optimization efforts should seek to remove it from
the picture. Rather than copying the current process, "creating a
pristine process is the way to go".Christian Braunerwas
favorabletoward the goal, saying: "The idea of having a builder api
for exec isn't all that crazy". His suggestion, though, was that a new
API should be built on top of the existingpidfdabstraction. Without getting into any
degree of detail, he said that the right approach would be to create an
option topidfd_open()to create an empty process. A series of calls to a newpidfd_config()system call would then configure this new process
as desired, setting up its environment, image to execute, and more.pidfd_config()would thus be analogous tofsconfig().An important objective for a new interface, Brauner said, would be the
ability to support an implementation ofposix_spawn()in user space.posix_spawn()is well suited as a replacement for
thefork()/exec()pattern; developers would likely
welcome a native implementation that isn't (unlike the current
implementation) hidingfork()andexec()under the covers.

Chenagreedthat the API as broadly sketched out by Brauner seemed better, and said
that future work would be in that direction. So there will be no spawn
templates in the Linux kernel but, if Chen's future work comes to fruition,
Linux may finally gain a properposix_spawn()implementation instead.Index entries for this articleKernelSystem calls/clone()KernelSystem calls/execve()to post comments### posix_spawn() does avoid the copy-on-write, at least sometimesPosted Jun 5, 2026 14:29 UTC (Fri)
 bysmcv(subscriber, #53363)
 [Link] (1 responses)> a native implementation that isn't (unlike the current implementation) hiding fork() and exec() under the coversposix_spawn() does at least *sometimes* avoid the copying problems of fork/exec - if there's no dedicated syscall for it, perhaps it uses vfork() and exec()? I know that recent GLib tries to use posix_spawn() as a backend for g_spawn_async() and similar functions if it can, and that was done to avoid real user-facing issues with fork/exec on low-memory systems, apparently successfully.(Unfortunately, the things you can do in posix_spawn() are rather limited, so libraries that want to run subprocesses in a somewhat predictable execution environment, while not 100% in control of their own host process's execution environment, can't always use it - for example you can posix_spawn_file_actions_addclose() to close individual fds, but you can't do the equivalent of close_range(). So GLib still needs to use fork/exec in many cases, depending on the options passed to GLib's own APIs by the library user.)### posix_spawn() does avoid the copy-on-write, at least sometimesPosted Jun 5, 2026 16:49 UTC (Fri)
 bybluca(subscriber, #118303)
 [Link]Yeah it uses CLONE_VM and CLONE_VFORK, so that the parent is frozen until the child is exec'ed, and that way the memory is fully shared with no COW, saving a ton of memory### io_uringPosted Jun 5, 2026 14:45 UTC (Fri)
 byjosh(subscriber, #17465)
 [Link] (10 responses)I've said this before (and have given a talk on it): I think the right mechanism for "actions" is an io_uring. Create a new empty process, run a ring in it to do things like receive/install file descriptors, end the ring with one or more attempts at exec, if you hit the end of the ring without an exec then the process gets SIGKILLed.I do think it makes sense to combine that with the "spawn template" mechanism somehow, insofar as one might want to load an ELF once and then repeatedly execute it (e.g. make invoking gcc).### io_uringPosted Jun 5, 2026 15:06 UTC (Fri)
 bykrisman(subscriber, #102057)
 [Link]Agreed. In fact,https://lwn.net/ml/all/87fr31xdz3.fsf@mailhost.krisman.be/### io_uringPosted Jun 5, 2026 15:32 UTC (Fri)
 bybluca(subscriber, #118303)
 [Link] (3 responses)One major difference is that there would be no seccomp support, which for something that allows spawning processes would be a pretty major shortcoming. I'm not up to date on the generic LSM story aside from that, but at some point it I think it basically boiled down to "block iouring" or "allow iouring" and that was it, maybe things have moved on that front though### io_uringPosted Jun 5, 2026 15:41 UTC (Fri)
 bykrisman(subscriber, #102057)
 [Link] (2 responses)Not true anymore. We now have per-operation bpf-based filtering in io_uring.### io_uringPosted Jun 5, 2026 15:55 UTC (Fri)
 bybluca(subscriber, #118303)
 [Link] (1 responses)So still no seccomp, and requires its own bespoke filtering? As a userspace developer making heavy use of pidfd_spawn I'd much rather have a normal syscall based approach, like fsconfig(). Much nicer, and integrates much better with the existing sandboxing ecosystem. fsconfig/opentree/movemount/etc are a really nice family of APIs, well designed and pleasant to use.### io_uringPosted Jun 5, 2026 16:09 UTC (Fri)
 byjosh(subscriber, #17465)
 [Link]No matter what filtering mechanism you use, operations in io_uring do not map 1:1 to syscalls. I think the BPF-based filtering in io_uring is a reasonable mapping of filtering to the concepts of io_uring. Using seccomp would still require substantially adapting seccomp; existing filters would not Just Work.### io_uringPosted Jun 5, 2026 17:49 UTC (Fri)
 bycalvin(subscriber, #168398)
 [Link] (2 responses)Why not go further? Be able to spawn a process with an empty set of FDs, address space, etc, then load an executable yourself. This would also allow for moving more exec() loader responsibilities into userspace.### io_uringPosted Jun 5, 2026 19:56 UTC (Fri)
 byjosh(subscriber, #17465)
 [Link]That would work in many cases, but you still need to handle exec in the kernel for suid or similar.That said, that does not need to be the high performance case; it would be fine to have a userspace mechanism for everything and have it just not work when escalating privileges.### io_uringPosted Jun 6, 2026 4:53 UTC (Sat)
 byIAmLiterallyABee(subscriber, #144892)
 [Link]That's basically how Fuchsia works### io_uringPosted Jun 5, 2026 19:36 UTC (Fri)
 bykhim(subscriber, #9252)
 [Link] (1 responses)You want to extend io_uring is some “special way”… Why? What would it buy you? Do you really spawn so many processes that normal syscalls are not enough?Just execute the code that would perform you damn template (and yes, this very much includes io_uring if you really need to)using existing mechanisms.No need to change anything in kernel at all, everything can be done from the userspace.### io_uringPosted Jun 5, 2026 19:58 UTC (Fri)
 byjosh(subscriber, #17465)
 [Link]I am suggesting adding a system call to load an executable for subsequent repeated reuse, and then separately providing bindings for that system call to io_uring. It would be available either way, it would just be faster via io_uring.### Cost vs benefit ?Posted Jun 5, 2026 18:01 UTC (Fri)
 byalkbyby(subscriber, #61687)
 [Link] (6 responses)>> but the pattern still is more expensive than it could be.I am curious if there is much evidence on that kind of statement. Sure, having vfork (or clone with CLONE_VFORK) plus a sequence of "spawn action" syscalls (such as closing fd-s, getting signal actions/masks etc) are not without overheads. E.g. crossing userspace/kernelspace boundary and copying some process structures. But we're talking possibly in the ballpark of (perhaps tens of) microseconds. Compared to "natural" exec overhead with process startup with dynamic linker, relocation and so on being likely in the ballpark order of magnitude larger.I do get people's frustration with exec. Clearly posix_spawn is the right user-space API. But for that API we already have everything that we need in kernel space. And user-space is at least mostly, right as well.There used to be a time when e.g. glibc did "regular" fork with all the dangers of pthread_atfork business and/or OOMing, but that has long been fixed.So then what is the point of more complexity/security risk and so on?### Cost vs benefit ?Posted Jun 5, 2026 18:36 UTC (Fri)
 byalkbyby(subscriber, #61687)
 [Link] (5 responses)Well, most likely the biggest issue with vfork+exec's overhead is that it is linear on number of file descriptors and VMAs of the parent's process. For larger processes this can add up to quite a bit. But having numbers-based discussion would be still better to have.### Cost vs benefit ?Posted Jun 5, 2026 19:14 UTC (Fri)
 byCyberax(✭ supporter ✭, #52523)
 [Link] (4 responses)[v]fork()+exec is terrible when you have a multithreaded app. You either end up COW-ing tons of pages just to be discarded a few milliseconds later, or you're stalling everything.### Cost vs benefit ?Posted Jun 5, 2026 20:25 UTC (Fri)
 byalkbyby(subscriber, #61687)
 [Link] (3 responses)vfork doesn't trigger any COWs and should scale okay in multi threaded processes (modulo VMA copy overheads; each thread is 1 or 2 vmas; but those should not be huge)### Cost vs benefit ?Posted Jun 5, 2026 20:44 UTC (Fri)
 byCyberax(✭ supporter ✭, #52523)
 [Link] (2 responses)vfork "freezes" the process instead, which might be even worse in case you have hundreds of threads that are now waiting for vfork() to finish.Either way, it's bad.### Cost vs benefit ?Posted Jun 5, 2026 22:03 UTC (Fri)
 byalkbyby(subscriber, #61687)
 [Link] (1 responses)No. vfork only halts calling thread. Only for the duration of posix_spawn. Which is likely helpful w.r.t. reducing cache line bouncings and contention.Also I made mistake above. VMAs are not copied by vfork/CLONE_VFORK. So looks like only "unscalable" part of vfork is duplicating file descriptors. Of which most are being closed either explicitly or via O_CLOEXEC, in a most typical uses. Some processes have millions of those. But in most cases it is not expensive.Again, I'd like to point out that people here (including myself) are speculating about costs. If costs are driving decision, then concrete numbers should be obtained.I have a sense: a) fork has real issues b) people tend to (incorrectly) attribute much of it's issues to vfork c) the entire vfork+small set of signal-safe actions+exec is very very foot-gun heavy d) so it is tempting to kernel folk to propose something nicerBut IMHO as long as libc handles the foot-gun aspect by delivering high quality posix_spawn implementation, what is the difference?### Cost vs benefit ?Posted Jun 6, 2026 19:22 UTC (Sat)
 byquotemstr(subscriber, #45331)
 [Link]> But IMHO as long as libc handles the foot-gun aspect by delivering high quality posix_spawn implementation, what is the difference?You're correct. You've identified one of many areas in which a bit of simple shared glue in user mode saves our having to add worse glue to the kernel.The possibility of such wins is one reason I'm so vigorously opposed to efforts by the Go people, the Zig people, and others to bypass the "bloated" libc and do "pure" system calls. Bypassing libc is a foolish false economy. It forces coordination points from cheap user mode code to expensive kernel code, because the Zigs of the world refuse to adopt any cooperative protocol that hardware privilege separation forces them to use.Go, for example, is happy enough using user32/kernel32/ntdll on Windows; it's happy enough using libc on macOS. But on Linux, it's somehow imperative for them to make direct system calls, therefore defeating attempts to form a cooperative commons that doesn't involve a CPU privilege transition. Why? libc system call wrappers aren't slow. They aren't bloated. Bypassing them doesn't grant a program superpowers. AFAICT, the impulse of some language runtime authors to bypass libc is based on vibes. Marginal individual benefits, large community costs.Vanity, thy name is static linking.### Fork() in the road paperPosted Jun 5, 2026 18:54 UTC (Fri)
 byjoib(subscriber, #8541)
 [Link] (4 responses)A famous (?) paper describing problems with the fork+exec approach to process creation:https://www.microsoft.com/en-us/research/wp-content/uploa...It suggests an alternative approach of creating an "empty" process and then various syscalls to be extended with variants taking a pid argument (or, if implemented today on Linux, presumably pidfd) that could be used for setting up the new process before launching it.### Fork() in the road paperPosted Jun 5, 2026 21:33 UTC (Fri)
 bygutschke(subscriber, #27910)
 [Link] (3 responses)The last time this conversation came up about two years ago, it was suggested that we can already do all of this with existing system calls. By creative combination of system calls, we can spawn an "empty process" that then configures itself as needed.I was skeptical but curious, andhttps://github.com/gutschke/safeexec/blob/main/safeexec.cis the result of my investigation.It's a bit ugly as the system calls weren't really designed with this goal in mind, but it's good enough to start experimenting. At the very least, we could validate the basic concept of starting from an empty process. It's much easier to experiment with different alternatives to traditional fork()/exec(), if we can do so from userspace instead of having to propose kernel additions.Once there is consensus on what we would like to do and what real-life applications actually require, we can identify specific issues that need to be added to the kernel.As is, we just run in circles. Every few years, there is a new proposal. It gains some traction. And then it peters out as it isn't really a full replacement for what applications already have, or it runs into some major roadblock with other kernel subsystems.I would love if somebody identified two or three major applications that suffer from measurable issues using today's fork()/exec() or using the various spawn() implementations, and then hacked in my code to see if the benchmark numbers that they care about change. Incidentally, if I correctly understand the new proposal for templates, I believe that could also be simulated with my POC userspace implementation.N.B.: I don't claim that my hack'ish code should ever be used for production. But I believe we need a lot more real-life examples of applications testing different process launching strategies to see if new API proposals make a difference or would largely go unused.### Fork() in the road paperPosted Jun 5, 2026 22:57 UTC (Fri)
 bymalmedal(subscriber, #56172)
 [Link] (2 responses)If you want hacky. Why not just CLONE_VM without CLONE_VFORK?It's somewhat annoying because you have to allocate a stack in the parent process and you can't reuse that area until you are sure the child has called exec but not insurmountable.### Fork() in the road paperPosted Jun 5, 2026 23:11 UTC (Fri)
 bygutschke(subscriber, #27910)
 [Link] (1 responses)It's been ages since I last experimented with CLONE_VM, so I probably don't remember all the details. But I think it had really awkward calling conventions that made it pretty much impossible to use from C code.If my cover ever was productized in some form, adding yet another assembly wrapper is obviously doable. But I intentionally tried to keep things as high level and portable as it's possible with this sort of low level code.And yes, it's ugly, and very far from portable without at least some effort. That's the nature of these APIs### Fork() in the road paperPosted Jun 5, 2026 23:35 UTC (Fri)
 bymalmedal(subscriber, #56172)
 [Link]I was curious as to what it would look like, so I coded it up. It's not too bad, unless I'm missing something.The stack for each process can be reused as soon at it has called exec. Not sure how to best detect that. Options include things like FD_CLOEXEC or when /proc/<pid>/exe of the child has changed.#include <fcntl.h>#include <linux/sched.h>#include <stdio.h>#include <stdlib.h>#include <string.h>#include <sys/time.h>#include <sys/wait.h>#include <unistd.h>int clone(int (*fn)(void *), void *stack, int flags, void *arg, .../* pid_t *parent_tid, void *tls, pid_t *child_tid */);int target(void *arg) {char fname[256];int i = *(int *)arg;snprintf(fname, sizeof(fname), "file%d.txt", i);int fd = open(fname, O_CREAT | O_RDWR, 0777);dup2(fd, 1);dup2(fd, 2);execl("/usr/bin/bash", "bash", "-c", "sleep 100 ; date", NULL);return -1;}double dtime() {struct timeval tv;gettimeofday(&tv, NULL);return (double)tv.tv_sec + tv.tv_usec / 1000000.0L;}int main(int argc, char **argv, char **envp) {const int STACK_SIZE = 65536;const int STACKS = 200;int pids[STACKS];int args[STACKS];char *stack = malloc(STACK_SIZE * STACKS);const long SIZE = 20 * 1024L * 1024 * 1024;char *buffer = malloc(SIZE);memset(buffer, 1, SIZE);double start = dtime();for (int i = 0; i < STACKS; i++) {args[i] = i + 1;pids[i] = clone(target, stack + STACK_SIZE * (i % STACKS + 1), CLONE_VM,&args[i]);}fprintf(stderr, "Avg %d %f\n", 0, (dtime() - start) / 200.0);for (int i = 0; i < STACKS; i++) {int status;int ret = waitpid(pids[i], &status, 0);if (status != 0 || ret < 0) {printf("status %d %d %d %d\n", i, pids[i], status, ret);}}printf("done\n");}### fork() + exec()Posted Jun 5, 2026 18:55 UTC (Fri)
 byclugstj(subscriber, #4020)
 [Link] (2 responses)If you are repeatedly creating large processes, you are already doing it wrong. The fix is in user space, not the kernel.### fork() + exec()Posted Jun 5, 2026 21:54 UTC (Fri)
 byroc(subscriber, #30627)
 [Link] (1 responses)I came here to say this!! If, as a userspace developer, you really care about performance there are many tools available to you today to mitigate the cost of fork+exec, some of which reach much higher levels of performance than creating new process ever can.Obviously the most efficient thing you can do is not use another process. Get the functionality into a library and call it in your current process.If you do need a separate process for some reason (e.g., resource management or sandboxing), create a persistent subprocess and reuse it many times.If for some reason you need lots of separate subprocesses, use the zygote pattern: fork+exec one zygote process, then every time you need a new subprocess, fork the zygote.There are edge cases where these don't apply, but adding complex new kernel interfaces that give tiny wins on edge cases does not seem like a good idea.### fork() + exec()Posted Jun 5, 2026 22:07 UTC (Fri)
 byCyberax(✭ supporter ✭, #52523)
 [Link]A lot of software might be _avoiding_ the subprocesses exactly because they are so horrible. In my case, we actually used a "process runner" server in one project to avoid forking in a large Java app. We needed it to do text extraction from Microsoft documents and for image parsing/resizing.### But won't someone think of the children?Posted Jun 5, 2026 23:49 UTC (Fri)
 byejr(subscriber, #51652)
 [Link]So many puns intended, and this is kinda-sorta horribly bitten tongue in horribly bitten cheek.For how many of us was our first OS class a lesson in "denial of service" by not checking fork()'s return value? Back in the day of shared resources, that was a very, very quick and socially enforced lesson. Later on, I was a sysadmin in academia, and we knew to be ready for it.Maybe we need "bad idea" emulation environments within which students (*cough* agents) must learn? Removing vfork+exec seems fantastic. But how do we train the N+4th generation on *why* that choice is fantastic? No programming language itself helps or else we'd all be using Pascal / Modula-{2,3,...} / Ada.Now that I'm a bit outside education, I really worry. We already had the problem of people knowing only Matlab, and then(?) only Python... There was one student who did not understand that a textual representation of an integer was different than the different encodings. I admit that I still have great difficulty in explaining the difference without courses in architecture, programming, and applications. If you *start* with the difference, sure, it's just there. If you've gone five+ years of college-level education without ever experiencing that difference, well, I've failed to put myself in their place sufficiently to explain it well.Sorry. Rambling.Otherwise, I'd assume that init would remain responsible for reaping zombie children. Perhaps we also could modify the terminology?