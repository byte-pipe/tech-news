---
title: This Website is Served from Nine Neovim Buffers on My Old ThinkPad
url: https://vim.gabornyeki.com/
site_name: lobsters
fetched_at: '2025-08-19T23:06:43.938710'
original_url: https://vim.gabornyeki.com/
date: '2025-08-19'
description: This Website is Served from Nine Neovim Buffers on My Old ThinkPad, a blog post by Gábor Nyéki
tags: lua, vim
---

# This Website is Served from Nine Neovim Buffers on My Old ThinkPad

August 18, 2025

TL;DR:I wrote a Neovim plugin in Lua that serves HTTP requests from open buffers.
It has no external dependencies, it has first-class support for serving content inDjot, and it is faster than Nginx so it won’t be a performance bottleneck behind a reverse proxy.
What’s not to like?

There is thatfamous storyfrom the 1990s about the man who was a Lisper but could not afford any of the commercial Lisps, so he deployed message routing for a German air traffic control system in a headless instance of Emacs.
This, of course, is horrific.
But it does remind us: our editors are capable of more, if we just let them out of the little nook that they occupy in our imagination.

Like Emacs, Vim is also fairly well-regarded for its versatility, although not in the typical systems programming sense.
Yet part of the origin story of Neovim specifically is a desire for an editor that can handle asynchronous IO.1The result of the efforts that that desire spurred is an API that can be put to good use in networking.

Fig. 1.A running instance of nvim-web-server.

I’ve written a plugin callednvim-web-serverthat serves HTTP requests in pure Lua.
It doesn’t require Node.js, a Python interpreter, or any other external tools.
Only Neovim’s Lua API.

Benefits (tongue-in-cheek):

* Instant deployment of new content.2
* The lowest-overhead content management system in existence.3
* Seamless Git integration.4
* Native support for Vim keybindings.

Downsides:

* Are there any?

Of course there are but we will ignore them.

## Contents

1. This must be slow
2. Deploying on an old ThinkPad
3. Is this even safe?

## This must be slow

I had expected nvim-web-server to be slow, given that Lua is a dynamically typed, interpreted language.
But it’s not.
It is faster than Nginx.

How can that be?
Well, for one thing, it is purposefully built for serving a static website and nothing more.
Nginx can do a lot more than that (even though in this benchmark it doesn’t).
Then, nvim-web-server also leverages Neovim’s bindings to libuv, a library that provides an efficient event loop.

But asynchronous IO does not seem to be the only reason for nvim-web-server’s speed.
The asyncio-based Python libraryaiohttpisslowerthan Nginx, at least on Python 3.10.
Historically, libuv (viauvloop’sbindings) was faster than asyncio, and this still seems to be the case as of Python 3.12.
But asyncio’s speed disadvantage appears to beno more than10-to-20 percent, which would not account for aiohttp’s underperformance compared with Nginx.

Table 1.
 Concurrency and Web Server Performance

Server

Concurrent Requests
5

Response Rate

Average

95%

99%

nvim-web-server

1

3,980.63/s

0.3 ms

0.3 ms

0.5 ms

nvim-web-server

50

15,284.43/s

3.2 ms

5.6 ms

7.3 ms

nvim-web-server

100

15,124.05/s

6.4 ms

11.4 ms

16.9 ms

nvim-web-server

200

14,475.55/s

13.5 ms

20.2 ms

36.3 ms

nvim-web-server

400

14,445.56/s

26.7 ms

43.6 ms

77.0 ms

Nginx

1

4,450.65/s

0.2 ms

0.4 ms

0.5 ms

Nginx

50

11,305.71/s

4.8 ms

10.1 ms

15.9 ms

Nginx

100

11,575.76/s

8.2 ms

21.8 ms

34.5 ms

Nginx

200

10,010.94/s

18.5 ms

53.6 ms

95.7 ms

Nginx

400

10,461.02/s

33.9 ms

96.4 ms

139.4 ms

aiohttp
6

1

6,391.33/s

0.2 ms

0.2 ms

0.3 ms

aiohttp

50

8,477.42/s

5.9 ms

7.0 ms

9.3 ms

aiohttp

100

8,447.58/s

11.7 ms

15.2 ms

18.4 ms

aiohttp

200

7,696.38/s

25.7 ms

35.0 ms

56.9 ms

aiohttp

400

7,132.18/s

55.0 ms

62.7 ms

114.9 ms

So the other reason may just be that LuaJIT is extremely fast.
If the conclusion ofthis 2016 benchmarkstill holds, then even though uvloop is a little faster than asyncio, aiohttp is not bottlenecked by asyncio but by itsHTTP parser.7That HTTP parser is written in pure Python, using re to process strings with regular expressions.

There is more than one reason that Python is slow.
But one is that CPython has to box every integer, float, boolean, etc., which means more time spent allocating and deallocating memory rather than serving HTTP requests.
This penalty also affects code that performs FFI to offload computation to a compiled library, since data that crosses the FFI boundary has to be boxed, too.

LuaJIT spends less time managing allocations.
First, it does not box numbers, booleans, nil values, and raw pointers.
Instead, it embeds all such values into 64-bit double-precision floatsusing NaN tagging.
Not only does this make pure Lua code faster but it also reduces FFI overhead.

Second, LuaJIT implementsallocation sinkingthrough which it can avoid allocating temporary values.
Traditional escape analysis can turn a heap allocation into a stack allocation if the compiler can prove that the allocated value doesn’t escape the local scope.
Allocation sinking is more aggressive, and in certain cases it can even eliminate stack allocations.
Importantly, this makes many uses of tables, Lua’s do-it-all data structure, more memory efficient and thus faster.

Third, LuaJIT has a very low memory footprint overall, between1-to-2xof standard Lua in popular benchmarks.
This is very good for a JIT compiler.
Ruby’s YJIT also does well, with only a0-to-5-percentoverhead.
But PyPy typically uses2-to-6xas much memory as CPython, and TruffleRuby often uses 15-to-25x as much memory as vanilla Ruby.

The result is that nvim-web-server doesn’t only use a very fast event loop.
It also has a fast (albeit thoroughly rudimentary) HTTP parser, and a fast mechanism for resolving requested paths and serving content.

In practical terms, what all this means is that if nvim-web-server is hosted behind an Nginx reverse proxy, then it won’t be the throughput bottleneck.
And even less so if Nginx accepts HTTPS connections because thenSSL terminationwill constrain Nginx’s throughput further.
(Although it has to be said that nvim-web-server will necessarily increaselatencysince we are replacing a web server with a reverse proxyanda web server.)

## Deploying on an old ThinkPad

Fig. 2.ThinkPad E430 as a stand-in for a private cloud.

It has become normalized to change our phones, computers, and cars every two to five years.
But were it not for planned obsolescence (and, to be fair, the enormous improvements in car safety in the last couple decades), old hardware with minimal maintenance could still perform many tasks effectively.

The ThinkPad that serves this website, an Edge E430 from 2012, was my only computer throughout grad school.
Now it is old by some measures, barely middle-aged by others.
It runs a Core i3-2350M with two physical cores.
Although this CPU is 14 years old, it has the same L1/L2 cache per physical core (64 KB/256 KB) as my i7-8565U which is eight years its junior.
But, for example, it doesn’t supportthe AVX2 instruction set, unlike 95 percent of computers inthe June 2025 Steam Survey.

This poor laptop also shows signs of wear.
The speaker cover is gone.
The battery is all but dead.
The original CPU fan died and the aftermarket fan I replaced it with now constantly spins.
Also, from some point on, the OS failed to boot if the room was below 18°C (65°F).
It was probably an issue with the old SSD which I have replaced.
Aside from all of this, it still works and doesn’t complain.

Its abundance of ports is a showcase of an earlier era.
VGA, HDMI, two USB2 ports, two USB3 ports, a headphone jack, ethernet, an SD card slot, a DVD drive, and a fingerprint reader.

And a WiFi adapter that supports 802.11n, for a maximum speed of a whopping 300 Mb/s.

And it only has 8 GB of RAM.
That is not a problem though, Neovim barely consumes 80 MB.

Speaking of Neovim, the web server is started with a straightforward Vim script.
The script initializes the server, opens the files to serve, and adds them to the routing table.

setup.vim

" Run this with `nvim -c 'source %' setup.vim`.
"

lua require("web-server").init()

split template.html
WSSetBufferAsTemplate

edit index.dj
WSAddBuffer /

edit screenshot.png
WSAddBuffer /screenshot.png image/png

edit laptop.jpg
WSAddBuffer /laptop.jpg image/jpg

edit arch_mix.png
WSAddBuffer /arch_mix.png image/png

edit arch_mix_dark.png
WSAddBuffer /arch_mix_dark.png image/png

edit favicon.ico
WSAddBuffer /favicon.ico image/x-icon

edit github-mark.svg
WSAddBuffer /github-mark.svg image/svg+xml

edit github-mark-white.svg
WSAddBuffer /github-mark-white.svg image/svg+xml

close

And that’s all there is to it.8Almost.

## Is this even safe?

Fig. 3.Neovim is deployed in a confined Docker container behind an Nginx reverse proxy.

nvim-web-server itself is implemented in a memory-safe language, Lua.
It never evaluates code and it never accesses the file system in response to requests, only content that has previously been loaded into its routing table.

However, the underlying LuaJIT runtime, as well as Neovim and libuv (which nvim-web-server relies on for core functionality), are largely written in C, and LuaJIT also includes a significant amount of hand-written assembly.
While LuaJIT is deployed as part ofOpenResty, Neovim is not typically used as a web server in production, so it has not been subject to the kind of security-minded scrutiny that a web server gets.

It is only reasonable then to take some precautions.
To mitigate these risks, I have deployed Neovim

1. in a Docker container,
2. running as an unprivileged user.

Furthermore, the container is confined by

1. an AppArmor profile that restricts file system access,
2. a seccomp profile that restricts access to system calls, and
3. a netfilter ruleset that blocks outgoing network connections.

I’ve also considered replacing 3, 4, and 5 withgVisorwhich is a container runtime that reimplements a commonly used subset of Linux’s system calls in Go.
It has a feature thatallows an external monitoring processto trace the system calls made by the containerized process.
This looks like a very neat alternative.
But it is left for a future hobby project.

1. This concern was so central thatIssue #3back in 2014 was about using libuv for OS calls.↩︎︎
2. No need for build systems, scp, rsync, or anything else.
Content is updated when the buffer is saved.
Djot buffers are converted to HTML automatically.↩︎︎
3. No need to set up and maintain WordPress, MariaDB, etc.↩︎︎
4. SeeFugitive.↩︎︎
5. For 50 concurrent requests, I ranhey -c 50 -n 10000 ...(simulating 50 concurrent users making 200 requests each).
For the other scenarios, I only changed-cand kept the total number of requests as-n 10000.↩︎︎
6. I ran http.server and aiohttp with Python 3.10.12.
The speed improvements of Python3.11and3.12may improve the numbers in the table.The aiohttp app, like nvim-web-server, preloaded the content into memory:from aiohttp import web

with open("index.html", "r") as handle:
 INDEX = handle.read()

app = web.Application()
routes = web.RouteTableDef()

@routes.get("/")
async def index(request):
 return web.Response(text=INDEX, content_type="text/html")

app.add_routes(routes)
web.run_app(app)↩︎︎
7. The aiohttp library benefits a lot from using asyncio, which is illustrated by how the Python standard library’s http.server fares by comparison.
Instead of asyncio, http.server uses threading, and this strategy does not scale well.
Each HTTP request starts a new thread, so http.server is slow even when serving non-concurrent requests, and its performance deteriorates as the number of concurrent requests increases.
Both throughput and latency suffer:ServerConcurrent RequestsResponse RateAverage95%99%http.server12,096.12/s0.5 ms0.5 ms2.3 mshttp.server501,275.15/s16.8 ms7.5 ms17.3 mshttp.server100491.20/s41.9 ms12.0 ms1,031.8 mshttp.server200360.43/s72.5 ms15.6 ms2,292.9 mshttp.server400243.11/s225.6 ms1,022.2 ms7,227.2 mshttp.server logs every request to stderr which slows down execution, so for the benchmark I ran it withpython3 -m http.server 2>/dev/null.↩︎︎
8. The script that producesFig. 1is just a little more complex.
To keep every buffer visible in a separate window, the script usessplitandvsplitinstead ofedit, and it doesn’t callcloseat the end.
This strategy would fail with too many splits because Neovim refuses to split windows that are too small.
To prevent this, before each split, the script also maximizes the available space in the active window.
Then once every buffer is open and everything is set up, it equalizes the space given to each window.So opening every buffer and setting up the routing table looks like this:" ...

command MaximizeWindow normal <C-w><C-_><C-w><C-|>
command EqualizeWindows normal <C-w>=

MaximizeWindow
split index.dj
WSAddBuffer /

MaximizeWindow
vsplit screenshot.png
WSAddBuffer /screenshot.png image/png

" ...

EqualizeWindows↩︎︎
