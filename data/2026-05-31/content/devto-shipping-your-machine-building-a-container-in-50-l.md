---
title: 'Shipping Your Machine: Building a Container in 50 Lines of Code (Part 2) - DEV Community'
url: https://dev.to/yechielk/shipping-your-machine-building-a-container-in-50-lines-of-code-part-2-4cm4
site_name: devto
content_file: devto-shipping-your-machine-building-a-container-in-50-l
fetched_at: '2026-05-31T19:32:45.626203'
original_url: https://dev.to/yechielk/shipping-your-machine-building-a-container-in-50-lines-of-code-part-2-4cm4
author: Yechiel Kalmenson
date: '2026-05-26'
description: Welcome Back to the Jailhouse In Part 1 of this series, we built the foundation of our... Tagged with go, containers, beginners, docker.
tags: '#go, #containers, #beginners, #docker'
---

## Welcome Back to the Jailhouse

InPart 1 of this series, we built the foundation of our container using Go. We successfully used theCLONE_NEWUTSnamespace and process forking to isolate our container's hostname from the host machine.

But we still have a massive security flaw. Right now, if we drop into our container's bash shell, we can still see all of the host's files. We could easilycdstraight out of our "isolated" environment and mess with the host machine.

Let's lock it down.

### chrootto Jail

Linux has a wonderful system call calledchroot(short for "change root"). It lets us change the root directory (/) for a given process. As far as the process is concerned, the directory we pointchroottois the entire universe. Anything outside of it simply doesn't exist.

Let's update ourchild()function to set the root directory to our current working directory:

func
 
child
()
 
{

 
fmt
.
Printf
(
"Running in new child process %v 
\n
"
,
 
os
.
Args
[
2
:
])

 
must
(
syscall
.
Sethostname
([]
byte
(
"container"
)))

 
// Get current directory and lock the process inside it

 
pwd
,
 
err
 
:=
 
os
.
Getwd
()

 
must
(
err
)

 
must
(
syscall
.
Chroot
(
pwd
))

 
// chroot changes the root, but doesn't automatically move us there. 

 
// We must explicitly change our working directory to the new root!

 
must
(
os
.
Chdir
(
"/"
))

 
cmd
 
:=
 
exec
.
Command
(
os
.
Args
[
2
],
 
os
.
Args
[
3
:
]
...
)

 
cmd
.
Stdin
 
=
 
os
.
Stdin

 
cmd
.
Stdout
 
=
 
os
.
Stdout

 
cmd
.
Stderr
 
=
 
os
.
Stderr

 
must
(
cmd
.
Run
())

}

Enter fullscreen mode

Exit fullscreen mode

Runsudo go run main.go run /bin/bash.

Crash!

panic: fork/exec /bin/bash: no such file or directory

Enter fullscreen mode

Exit fullscreen mode

What happened?

We just told our process that our current directory is the entire universe. So, when we askexec.Commandto run/bin/bash, it isn't looking at your computer's actual hard drive anymore. It is looking inside your project folder for a directory calledbincontaining an executable calledbash.

Because our current directory doesn't have those, it fails! We need an actual root filesystem to provide the basic binaries our shell expects.

(Note: Production container runtimes like runC actually use a more advanced system call calledpivot_rootfor better security, butchrootis perfect for understanding the core concept!).

### The Image

To fix this, we need to provide an actual root filesystem that contains the basic folders and binaries (like /bin/bash) that our shell expects.

You can grab a basic Ubuntu root filesystem yourself using Docker. Open a new terminal tab and run these exact commands in your project directory:

# Use docker to start a Ubuntu container and then export its filesystem to a compressed file called ubuntu.tar

docker 
export
 
$(
docker create ubuntu
)
 
>
 ubuntu.tar

# Create a directory called ubuntu-rootfs and unzip your tar file into it

mkdir 
ubuntu-rootfs

tar
 
-xf
 ubuntu.tar 
-C
 ubuntu-rootfs

Enter fullscreen mode

Exit fullscreen mode

This creates a folder calledubuntu-rootfscontaining a complete, brand-new Ubuntu file system.

Assuming you have that folder in your project directory, let's change ourchrootcall to point to it as follows:

 
must
(
syscall
.
Chroot
(
filepath
.
Join
(
pwd
,
 
"ubuntu-rootfs"
)))

 
must
(
os
.
Chdir
(
"/"
))

Enter fullscreen mode

Exit fullscreen mode

Now, when we runsudo go run main.go run /bin/bash, everything works perfectly!

You can runls /and you will only see the files inside yourubuntu-rootfsdirectory. Try runningcd ..to escape, and you will find yourself in the exact same directory as before. You cannot access the host machine at all.

### PIDs and /proc

We're ready for the next step. If you remember, when we randocker run -it ubuntu /bin/bashback in the beginning of Part 1, one of the ways we could tell we were in an isolated container was by runningps auxand observing only two processes running with very low PIDs.

Let's try to replicate that. While inside our new container, try runningps auxto view the running processes.

It breaks with an error:

Error, 
do 
this: mount 
-t
 proc proc /proc

Enter fullscreen mode

Exit fullscreen mode

Thepscommand works by reading the/procdirectory, which is a special virtual filesystem in Linux that contains live data about running processes. Our isolated root filesystem has an empty/procfolder, and the operating system hasn't been told to attach the live process data to it. Because it's empty,psfails!

To fix this, we need to do two things:

1. Give our container its own isolated Process IDs (PIDs) using namespaces.
2. Mount theprocfilesystem so commands likepscan read it.

First, update theSysProcAttrin therun()function to include the PID and Mount namespaces. (Note:CLONE_NEWNSstands for "New Namespace", but it specifically refers to the Mount namespace! It just happens to be the first namespace added to the Linux kernel and back then no one thought they might end up needing more so they just called it "namespace" 🤷).

 
cmd
.
SysProcAttr
 
=
 
&
syscall
.
SysProcAttr
{

 
Cloneflags
:
 
syscall
.
CLONE_NEWUTS
 
|
 
syscall
.
CLONE_NEWPID
 
|
 
syscall
.
CLONE_NEWNS
,

 
}

Enter fullscreen mode

Exit fullscreen mode

Next, mount theprocdirectory inside ourchild()function, right after wechroot. We will also use Go'sdeferkeyword to ensure we unmount it and clean up after ourselves when the function exits:

 
must
(
syscall
.
Chroot
(
filepath
.
Join
(
pwd
,
 
"ubuntu-rootfs"
)))

 
must
(
os
.
Chdir
(
"/"
))

 
// Mount the proc filesystem

 
must
(
syscall
.
Mount
(
"proc"
,
 
"proc"
,
 
"proc"
,
 
0
,
 
""
))

 
// Clean up after ourselves when the function exits

 
defer
 
syscall
.
Unmount
(
"proc"
,
 
0
)

Enter fullscreen mode

Exit fullscreen mode

Now, run your container and typeps aux. You'll see only three processes running:exe(our Go program) running as PID 1,bashrunning as PID 2, and thepscommand we just ran!

### Cgroups (Keeping it Civil)

We have our invisibility cloak (Namespaces) and our isolated universe (chroot). But what happens if we write an infinitewhileloop inside our container that eats up all the CPU and memory?

It would completely crash the host machine!

To prevent our container from using up all of our resources, Linux usescgroups(Control Groups). Cgroups act as the bouncer, ensuring no single container uses more than its fair share of resources.

To set up a cgroup, we can lean on a famous Linux philosophy: "Everything is a file." This means we can configure the kernel's resource limits by creating specific directories and writing text into special files.

Let's add a quick helper function to ourmain.gofile to limit the maximum number of processes our container is allowed to spawn to 20:

func
 
cg
()
 
{

 
cgroups
 
:=
 
"/sys/fs/cgroup/"

 
pids
 
:=
 
filepath
.
Join
(
cgroups
,
 
"pids"
)

 
// 1. Create a new cgroup for our container

 
containerCgroup
 
:=
 
filepath
.
Join
(
pids
,
 
"my-container"
)

 
os
.
Mkdir
(
containerCgroup
,
 
0755
)

 
// 2. Write the limit into the cgroup file (max 20 processes)

 
must
(
os
.
WriteFile
(
filepath
.
Join
(
containerCgroup
,
 
"pids.max"
),
 
[]
byte
(
"20"
),
 
0700
))

 
// 3. Add our current process to this cgroup

 
must
(
os
.
WriteFile
(
filepath
.
Join
(
containerCgroup
,
 
"cgroup.procs"
),
 
[]
byte
(
strconv
.
Itoa
(
os
.
Getpid
())),
 
0700
))

}

Enter fullscreen mode

Exit fullscreen mode

Let's break down what this function is doing:

1. Create the group:By making a new directory inside/sys/fs/cgroup/pids, the Linux kernel automatically creates a new Control Group for us.
2. Set the rule:Inside that new directory, Linux automatically generates a file calledpids.max. We open that file and write the text"20"into it. This establishes a rule that our process will only be allowed to run 20 sub-processes.
3. Enforce the rule:Linux also generates a file calledcgroup.procs. We get our Go program's current Process ID (os.Getpid()) and write it into this file. This tells the kernel,"Hey, apply the rules of this folder to me!"

Finally, let's call this function inside ourrun()function, right before we execute our child process:

func
 
run
()
 
{

 
fmt
.
Printf
(
"Running %v 
\n
"
,
 
os
.
Args
[
2
:
])

 
args
 
:=
 
append
([]
string
{
"child"
},
 
os
.
Args
[
2
:
]
...
)

 
cmd
 
:=
 
exec
.
Command
(
"/proc/self/exe"
,
 
args
...
)

 
cmd
.
Stdin
 
=
 
os
.
Stdin

 
cmd
.
Stdout
 
=
 
os
.
Stdout

 
cmd
.
Stderr
 
=
 
os
.
Stderr

 
cmd
.
SysProcAttr
 
=
 
&
syscall
.
SysProcAttr
{

 
Cloneflags
:
 
syscall
.
CLONE_NEWUTS
 
|
 
syscall
.
CLONE_NEWPID
 
|
 
syscall
.
CLONE_NEWNS
,

 
}

 
// Set up our resource limits!

 
cg
()

 
must
(
cmd
.
Run
())

}

Enter fullscreen mode

Exit fullscreen mode

And just like that, our container is officially resource-limited! Because cgroups inherit down to child processes, everything that runs inside our container is bound by this rule. If a malicious script inside tries to execute a "fork-bomb" (a script that endlessly copies itself to freeze the computer), the kernel will step in and aggressively kill it the second it hits 20 processes.

### The Reveal

If you put all of this together, we just built Docker from scratch in about 50 lines of code.

Containers aren't magic. They aren't heavyweight VMs. They are simply standard Linux processes wrapped in namespaces, jailed in a specific directory, and policed by cgroups.

In fact, you don't even need Go to do this. You can trigger the exact same isolation using a single line of bash:

sudo 
unshare 
--uts
 
--pid
 
--mount
 
--fork
 
--root
=
/home/ubuntu-rootfs 
--mount-proc
 /bin/bash

Enter fullscreen mode

Exit fullscreen mode

And there you have it! The next time someone says "it works on my machine," you know exactly what it takes to ship their machine to production.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse