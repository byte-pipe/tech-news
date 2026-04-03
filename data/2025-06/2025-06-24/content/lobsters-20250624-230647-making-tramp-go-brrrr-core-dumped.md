---
title: Making TRAMP go Brrrr…. • Core Dumped
url: https://coredumped.dev/2025/06/18/making-tramp-go-brrrr./
site_name: lobsters
fetched_at: '2025-06-24T23:06:47.536000'
original_url: https://coredumped.dev/2025/06/18/making-tramp-go-brrrr./
date: '2025-06-24'
published_date: '2025-06-18T00:00:00+00:00'
tags: emacs, performance
---

I recently changed jobs and found myself in a position where I would need to do a lot of work on remote machines. Since I am Emacs user, the most common way to do this is usingTRAMP (Transparent Remote access, Multiple Protcol). TRAMP is an Emacs package that let’s you treat a remote host like a local system, similar toVSCode Remote Development Extension. I had used TRAMP before and it tended to be slow. Since I would be using it all day now I figured I should take some time to make it faster.

## TRAMP is great

TRAMP really is an amazing piece of technology. It supports a huge number of protocols and it lets you pretend that you are working on a local system. You can copy files around, run programs, run shells, and for the most part everything just works.

But TRAMP unfortunately has a propensity for being slow. Sometimes this is not TRAMPs fault and comes from how it is used. In my testing, each call through TRAMP takes about 50-100ms. Compare that to a normal external process call in Emacs which would take around 1 ms. Workflows that work fine on a local machine become unbearable when working remotely. However, this doesn’t mean that TRAMP has to be slow. If you runemacs -Qand use TRAMP you will normally find it quite snappy.

## Getting started

First, let’s set up some of the basic settings. Tramp alreadyhas a sectionon how to improve performance, so I am not going to reiterate those suggestions here. But these additional settings will prevent TRAMP from creating a bunch of extra files and use scp directly when moving files.

(
setq

remote-file-name-inhibit-locks

t


tramp-use-scp-direct-remote-copying

t


remote-file-name-inhibit-auto-save-visited

t
)

In order to open a file on a remote host, TRAMP needs to copy the file contents to your local machine. Most TRAMP methods have two ways to copy files; inline or out-of-band. Out-of-band will use external methods likersyncorscp, while inline will send compressed base64 encoded text over the SSH session and then decode it on the other side. This works best for small files where the overhead of creating a new connection is not worth it. This is by default set to 10KB. However, I found in my testing that the best value was much bigger than that.

You can see in the graph above that inline is faster all the way up until about 2MB. After that point inline continues to grow linearly (the x-axis is logarithmic) while the out-of-band copying is sub-linear. Generally the slower the connection, the bigger the gap between inline and out-of-band. In the graph above it is 250ms, but on some slower connections I have observed that gap to be closer to 750ms. Interestingly, the cutoff always seems to be around 2MB, at least on my machines.

(
setq

tramp-copy-size-limit

(
*

1024

1024
)

;; 1MB


tramp-verbose

2
)

I also found that usingrsyncas your method makes updating an existing file (i.e. making a small change to a file and saving it) about 3-4 times faster than usingscp. I don’t usersyncthough because it breaks remote shells.

## Use Direct Async

When creating a new process in Emacs, you have two options: synchronous or asynchronous. Async processes have historically been really slow over TRAMP, because it has to create a new connection for every async process. However recent version of TRAMP have added a feature calleddirect async processthat makes this significantly faster. This feature alone will take many packages (like magit or git-gutter) from completely unusable to bearable over TRAMP. Here is how you configure it with TRAMP2.7.

(
connection-local-set-profile-variables


'remote-direct-async-process


'
((
tramp-direct-async-process

.

t
)))

(
connection-local-set-profiles


'
(
:application

tramp

:protocol

"scp"
)


'remote-direct-async-process
)

(
setq

magit-tramp-pipe-stty-settings

'pty
)

We have to add that extra setting to get magit to work. Seethis issuefor more details. You can double check that this mode is working by callingM-: (tramp-direct-async-process-p)on a remote file.

## Fix remote compile

Newer versions of TRAMP will useSSH connection sharingfor much faster connections. These don’t require you to reenter your password each time you connect. Thecompilecommand disables this feature, so we want to turn it back on.

(
with-eval-after-load

'tramp


(
with-eval-after-load

'compile


(
remove-hook

'compilation-mode-hook

#'
tramp-compile-disable-ssh-controlmaster-options
)))

## How to debug perf issues

What can we do to make working over TRAMP faster? If you are like me and already have an existing config, it is more than likely that some packages you are using are not going to play nicely over TRAMP due to the extra overhead. There will be certain operations like changing modes, moving the cursor, or saving a buffer that has inexplicable delays.

When you encounter this, you should use the built-in profiler. useM-x profiler-startbefore behavior that is slow and thenM-x profiler-stopandM-x profiler-reportafterwards. This will give you a hierarchical list of where Emacs was spending its time. If this is an issue related to TRAMP you should seetramp-wait-for-outputbe a significant portion of the total time. But it is not always clear what is actually causing TRAMP to be called. In this case, you can usedebug-on-entryontramp-send-commandto get a backtrace when something calls TRAMP. This will let you see the exact commands that are calling out to TRAMP and causing the slow down. In my case, I found a couple of the features of doom modeline were causing a lot of delays.

(
remove-hook

'evil-insert-state-exit-hook

#'
doom-modeline-update-buffer-file-name
)

(
remove-hook

'find-file-hook

#'
doom-modeline-update-buffer-file-name
)

(
remove-hook

'find-file-hook

'forge-bug-reference-setup
)

## Magit

magit is one of Emacs super powers, consistently rated as one of the best packages. I use it for practically everything related to git. Unfortunately, it is quite slow over TRAMP. On my remote repo’s it can take 10-20 seconds just to runmagit-status. And every time you run a command it needs to refresh the whole status buffer, leading to more delays. Magit is designed to run on a local machine where shell commands are cheap. A simple magit command might run 30 individual shell commands. This can be a big overhead over TRAMP.

So here is my advice for working with magit over TRAMP.

1. Usemagit-dispatchandmagit-file-dispatchinstead of doing everything from the status buffer. This will let you quickly execute commands without waiting for the status buffer to load and refresh each time. Only use the status buffer when you need to get a high-level view of your repo or need to operate on large numbers of files.
2. Don’t be afraid to just run a shell command. RunningM-S-! git branch fooorM-S-! git commit -m "Update foo"will often be faster than waiting 8 seconds for magit to populate all branch targets over ssh, or load the git commit interface. Some things like cherry-picking or rebasing are still much easier in magit, despite the overhead.
3. Try and remove anything extra that magit might try and do. Here are some settings I am using.

;; don't show the diff by default in the commit buffer. Use `C-c C-d' to display it

(
setq

magit-commit-show-diff

nil
)

;; don't show git variables in magit branch

(
setq

magit-branch-direct-configure

nil
)

;; don't automatically refresh the status buffer after running a git command

(
setq

magit-refresh-status-buffer

nil
)

A lot of this slowness could be alleviated with some better caching. When I first started testing this I foundforge-dispatchto be extremely slow. Some profiling showed thatmagit was making 176 calls over TRAMP, even though it only needed 6 of them. This has since been fixed, but there is more performance to be gained. I tried toimplement a magit caching mechanismand it was a huge boost for performance (though it is still very rough). I stopped working on it because the magit maintainersaid that he is hoping 2025 will be the yearto add caching to the whole magit workflow! If you are interested in seeing that happen, consider sponsoringhere.

### Speed Git

Even with all the settings above, opening the status buffer and staging a few files is still quite slow. So I created a simple mode that just opens a status buffer and lets me easily stage some files. It doesn’t have any of the fancy features or folding headers of the magit status buffer, but it is nearly instantaneous. When I want to quickly stage or unstage some files, this is what I reach for. I am not interested in trying to maintain this as a proper package, buthereis the source if you are interested.

## LSP

LSP mode works over TRAMP, but unfortunately not with the direct async process feature. There is aworkaroundyou can use though. Another alternative islsp-bridge, but I was not able to test it because it requires the remote python to be built with FFI support, which my server does not have. Even though it is supported, LSP over TRAMP can be kind of slow, so I tend not to use it. Rather than addinglspto the major mode hook, I added this function that will not enable LSP by default on remote hosts. It also removes other functionality that can tend to cause a slowdown.

(
defun

$lsp-unless-remote

()


(
if

(
file-remote-p

buffer-file-name
)


(
progn

(
eldoc-mode

-1
)


(
setq-local

completion-at-point-functions

nil
))


(
lsp
)))

## Cache everything

If sending calls over TRAMP is so expensive, the best thing we can do is not run them. TRAMP already has some built-in caching for things like remote files, but it only keeps them for a short while. Anything that doesn’t go through TRAMP will be a win. I created this function for just that purpose:

(
defun

memoize-remote

(
key

cache

orig-fn

&rest

args
)


"Memoize a value if the key is a remote path."


(
if

(
and

key


(
file-remote-p

key
))


(
if-let

((
current

(
assoc

key

(
symbol-value

cache
))))


(
cdr

current
)


(
let

((
current

(
apply

orig-fn

args
)))


(
set

cache

(
cons

(
cons

key

current
)

(
symbol-value

cache
)))


current
))


(
apply

orig-fn

args
)))

I can then use it to cache things I don’t want TRAMP to be looking up all the time. Here are some things that get called very frequently and don’t really change. If I ever want to reset the cache, I can reset the variable tonil.

;; Memoize current project

(
defvar

project-current-cache

nil
)

(
defun

memoize-project-current

(
orig

&optional

prompt

directory
)


(
memoize-remote

(
or

directory


project-current-directory-override


default-directory
)


'project-current-cache

orig

prompt

directory
))

(
advice-add

'project-current

:around

#'
memoize-project-current
)

;; Memoize magit top level

(
defvar

magit-toplevel-cache

nil
)

(
defun

memoize-magit-toplevel

(
orig

&optional

directory
)


(
memoize-remote

(
or

directory

default-directory
)


'magit-toplevel-cache

orig

directory
))

(
advice-add

'magit-toplevel

:around

#'
memoize-magit-toplevel
)

;; memoize vc-git-root

(
defvar

vc-git-root-cache

nil
)

(
defun

memoize-vc-git-root

(
orig

file
)


(
let

((
value

(
memoize-remote

(
file-name-directory

file
)

'vc-git-root-cache

orig

file
)))


;; sometimes vc-git-root returns nil even when there is a root there


(
when

(
null

(
cdr

(
car

vc-git-root-cache
)))


(
setq

vc-git-root-cache

(
cdr

vc-git-root-cache
)))


value
))

(
advice-add

'vc-git-root

:around

#'
memoize-vc-git-root
)

;; memoize all git candidates in the current project

(
defvar

$counsel-git-cands-cache

nil
)

(
defun

$memoize-counsel-git-cands

(
orig

dir
)


(
$memoize-remote

(
magit-toplevel

dir
)

'$counsel-git-cands-cache

orig

dir
))

(
advice-add

'counsel-git-cands

:around

#'
$memoize-counsel-git-cands
)

## Future work

All this work has made TRAMP quite usable for me. There are still things that are slow, but almost nothing that just doesn’t work. For most of the work I do I hardly notice that I am working over a remote protocol. However, in writing all this, I kept thinking to myself “There has to be a better way to do this”. I have started to think of ways to fundamentally improve the performance of TRAMP that would involve changes to the package itself. I plan to write more on that soon, so stay tuned!

### Have a comment?

Join the discussion onHN,Lobsters,Reddit, or send me anemail.
