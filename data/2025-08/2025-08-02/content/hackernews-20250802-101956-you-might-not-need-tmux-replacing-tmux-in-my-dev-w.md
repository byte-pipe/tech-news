---
title: 'you might not need tmux: replacing tmux in my dev workflow'
url: https://bower.sh/you-might-not-need-tmux
site_name: hackernews
fetched_at: '2025-08-02T10:19:56.306166'
original_url: https://bower.sh/you-might-not-need-tmux
author: elashri
date: '2025-08-02'
description: replacing tmux in my dev workflow
---

Hear me out, I can already read the descenting opinions:

* But I need session persistence!
* But I need split windows!
* But I need to group windows per project!
* But I need lots of terminals inside of a remote server!

I had the exact same response whenever someone would argue against usingtmux.
For context, I've been a huge fan oftmuxand have been using it as a daily
part of my workflow for 7+ years. Whether I'm developing on my local machine or
in SSH, I was usingtmux.

However, a couple of years ago I stumbled across aGitHub issue in the kitty projectthat has stuck in my mind like an itch that I cannot scratch.

In summary: multiplexers add unnecessary overhead, suffer from a complexity
cascade, because they actually have totranslateescape codes, modifying
them in hackish ways to get them to work with their concepts of
windows/sessions.

And then a couple of weeks ago I watched this excellent interview fromlinkarzuand kovid (creator of kitty). In it, theydiscussedtmux.

I have to say, the arguments are convincing. Over the years, I have had a
handful of problems withtmuxthat were not necessarily deal breakers but very
annoying to deal with on a regular basis.

For example, if you do not setTERMwithtmuxproperly, your colors will
render incorrectly. Withouttmuxeverything looks good, but with it things can
look washed out or just wrong. So when debugging issues related to terminal
features, you need to consider both your terminal emulator andtmux. Now add
another layer likesshand you're really pulling your hair out.

Another example is buffer scrollback. It's one of those things where you have to
learn thetmuxway of scrolling a window. You get used to it, of course, but
it's just not great.

And what about mouse select to copy/paste? It works most of the time, but
sometimestmuxgets ignored and I'm selecting across splits which makes the
thing I'm copying impossible to grab without bailing.

Another issue I ran into a couple of times is the lack of experimental protocol
support. I use "experimental" loosely since some of them are gaining popularity
inside terminal emulators, like thekitty graphics protocol.
Even if your terminal emulator supports the kitty graphics protocol,tmuxdoes not.

This is why kovid argues that terminal multiplexers:

"[...] act as a drag on the ecosystem as a whole, making it very hard to get
any new features."

Okay, I get it, I'm sympathetic to the issue terminal multiplexers cause to the
wider terminal ecosystem, but what's the alternative?tmuxsolves problems
that are not easy to replace:

* session persistence (detach + attach process from terminal)
* window management (tabs, splits, moving them around)

Session persistence can be accomplished in a number of ways, with varying
degrees of feature overlap with whattmuxprovides:

* ctrl-z+fg
* nohup {cmd} &
* disown

These are discussed in thisstack exchangepost. None of them quite work the waytmuxworks. In particular, these
commands will either a) get killed when you close your terminal, or b) cannot
reattach easily.

For window management, the argument is we should use our window managers to
manipulate our windows. That works great for local development, but what happens
when you are SSH'd into a server? How do you let your window manager manipulate
windows within an SSH session?

Darn, built-in tools don't quite check all of our boxes, I wonder, are there anytmuxalternatives that could work?

I was desperate for a solution and I really did not want to build my own. I also
didn't want to replacetmuxwith something equally as large of a dependency.
Here's what I found:

* dtach
* abduco
* shpool

All of these tools embody the unix philosophy of doing one thing, well. So they
are targeting session persistence (detach and attach functionality). What's
exciting about this idea is since there are no virtual splits, I can get native
scrollback!

Most of them work bycreating a daemon1with some permutation offork()and communicating with a unix socket between the detached process and "client"
terminals. Some of them support buffer playback so when you reattach you can see
where you left off. Most of them haven't quite nailed this aspect of whattmuxdoes well, butshpooldoes a pretty good job.

I tried all of them with varying degrees of success. They could do what they
claim, but they are buggy. In particular, I could not get them to detach when
inside ofnvim, which is a deal breaker. I assumed it was because the
shortcuts I was using to detach were being captured bynvim. Who knows, it
might be something misconfigured on my end.

However, out of those tools I used,shpoolchecked the most boxes.
Specifically they have a commandshpool detachwhich allowed me to run a
command to detach the current process. So I was able to create a keymap that
sent the detach command toshpool:

1
-- https://github.com/shell-pool/shpool/issues/71#issuecomment-2632396805

2
vim.keymap
.
set
({

"n"
,

"v"
,

"i"
,

"t"

},

"<C-space><C-d>"
,

function
()

3

vim.cmd
(
"!shpool detach"
)

4
end
)

Nice, this is working well for session persistence. Let's move onto window
management. I'm usingghosttyon my work laptop andsway+footon my personal
machines. I can use both of them for window management, but as a note I employ a
client+server development workflow. This means my client (e.g. laptop, desktop)
connects to a headless VM on myproxmoxbox where I do all of my dev. So I am
always SSH'd during development. So how can I use my local window managers to
control all myshpoolsessions on a remote server?

shpoolhas some docs on how toautomatically connect toshpool

The idea is simple: use your window manager to create new terminal windows and
thensshinto eachshpoolsession. Here's thessh_configI use to make
this easier:

Host *
 # ping server to make sure it's still responding
 ServerAliveInterval 60
 ServerAliveCountMax 3

Host = d.*
 HostName 192.168.88.xxx
 User erock
 IdentityFile ~/.ssh/id_ed25519

 # attach to shpool session based on the name provided
 RemoteCommand shpool attach -f %k
 RequestTTY yes

 # share ssh connection with all terminals that try to connect to this host
 ControlPath ~/.ssh/cm-%r@%h:%p
 ControlMaster auto
 ControlPersist 10m

Now I can automatically create or attach to myshpoolsessions:

* ssh d.chat-> connect to IRC
* ssh d.dot-> connect to my dotfilesneovimclient
* ssh d.term-> connect to a running terminal
* ssh d.pico-> connect to my piconeovimclient

I can spin up as manyshpoolsessions as I want and connect to them as-needed.
Then when I combine this withautossh,
I can keep my terminal windows open on my client and reconnect automatically
when the client reconnects to my network!

1
autossh -M
0
 d.chat

So, did I finally replacetmux? For me, the answer is a resounding yes! Once I
got all of this setup on my dev machine, I haven't usedtmuxor feel like a
massive downgrade. I did have to adjust my normal workflow slightly, but that's
been fun. Further, I'm slowly noticing things thattmuxdidn't handle well,
but now, "just work": native scrollback, terminal notifications, and terminal
titles being the most notable changes.

It's not perfect, there are active issues withshpool, like it doesn't restore
terminal state properly when reattaching which can makeresizing broken while usingnvim.
But as noted in that issue, there is a work-around:

1
vim.keymap
.
set
(
"n"
,

"<leader>l"
,

function
()

2

io.stdout
:
write
(
"
\027
[?2048h"
)

3
end
,

opts
)

shpoolalsodoesn't support "multiplayer"which has caused some issues with usingautosshon multiple clients since they
will disconnect each other.

Could this workflow replacetmuxfor you? Let me know!

1. 1.7 How do I get my program to act like a
daemon?↩︎

 last updated:
2025-08-01

I have no idea what I'm doing. Subscribe to myrss feedto read more
posts.
