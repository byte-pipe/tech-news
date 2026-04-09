---
title: io_uring, kTLS and Rust for zero syscall HTTPS server
url: https://blog.habets.se/2025/04/io-uring-ktls-and-rust-for-zero-syscall-https-server.html
site_name: hackernews_api
fetched_at: '2025-08-23T22:01:38.537703'
original_url: https://blog.habets.se/2025/04/io-uring-ktls-and-rust-for-zero-syscall-https-server.html
author: guntars
date: '2025-08-22'
description: Around the turn of the century we started to get a bigger need for high capacity web servers. For example there was the C10k problem paper.
tags:
- hackernews
- trending
---

Around the turn of the century we started to get a bigger need for high
capacity web servers. For example there wasthe C10k problempaper.

At the time, the kinds of things done to reduce work done per request was
pre-forking the web server. This means a request could be handled without an
expensive process creation.

Because yes, creating a new process for every request used to be something
perfectly normal.

Things did get better. People learned how to create threads, making things more
light weight. Then they switched to usingpoll()/select(), in order to not
just spare the process/thread creation, but the whole context switch.

I remember a comment onKuro5hinfrom anakata, the creator of both The
Pirate Bay and the web server that powered it, along the lines of “I am select()
of borg, resistance is futile”, mocking someone for not understanding how to
write a scalable web server.

Butselect()/poll()also doesn’t scale. If you have ten thousand
connections, that’s an array of ten thousand integers that need to be sent to
the kernel for every single iteration of your request handling loop.

Enterepoll(kqueueon other operating systems, but I’m focusing on Linux
here). Now that’s better. The main loop is now:

 set_up_epoll()
 while True:
 new, read, write = epoll()
 epoll_add_connections(new)
 for con in read:
 process(con.read())
 if con.read_all_we_need:
 epoll_remove_read_op(con)
 for con in write:
 con.write_buffer()
 if con.buffer_empty:
 epoll_remove_write_op(con)

All the syscalls are pretty cheap.epoll()only deals in deltas, and it
doesn’t have to be re-told the thousands of active connections.

But they’re not without cost. Once we’ve gotten this far, the cost of a syscall
is actually a significant part of the total remaining cost.

We’re here going to ignore improvements likesendfile()andsplice(), and
instead jump to…

## io_uring

Instead of performing a syscall for everything we want to do, commanding the
kernel to do this or that, io_uring lets us just keep writing orders to a
queue, and letting the kernel consume that queue asynchronously.

For example, we can putaccept()into the queue. The kernel will pick that
up, wait for an incoming connection, and when it arrives it’ll put a
“completion” into the completion queue.

The web server can then check the completion queue. If there’s a completion
there, it can act on it.

This way the web server can queue up all kinds of operations that were
previously “expensive” syscalls by simply writing them to memory. That’s it.
And then it’ll read the results from another part of memory. That’s it.

In order to avoid busy looping, both the kernel and the web server will only
busy-loop checking the queue for a little bit (configurable, but think
milliseconds), and if there’s nothing new, the web server will do a syscall to
“go to sleep” until something gets added to the queue.

Similarly on the kernel side, the kernel will stop busy-looping if there’s
nothing new, and needs a syscall to start busylooping again.

This sounds like it would be tricky to optimize, but it’s not. In the end the
web server just puts stuff on the queue, and calls a library function that only
does that syscall if the kernel actually has stopped busylooping.

This means that a busy web server can serve all of its queries without even once
(after setup is done) needing to do a syscall. As long as queues keep getting
added to,stracewill shownothing.

## One thread per core

Since CPUs today have many cores, ideally you want to run exactly one thread
per core, bind it to that core, and not share any read-write data structure.

ForNUMAhardware, you also want to make sure that a thread only
accesses memory on the local NUMA node.This netflix talkhas some
interesting stuff on NUMA and high volume HTTP delivery.

The request load will still not be perfectly balanced between the threads (and
therefore cores), but I guess fixing that would have to be the topic of a
future post.

## Memory allocations

We will still have memory allocations though, both on the kernel and web server
side. Memory allocations in user space will eventually need syscalls.

For the web server side, you can pre-allocate a fixed chunk for every
connection, and then have everything about that connection live there. That way
new connections don’t need syscalls, memory doesn’t get fragmented, and you
don’t run the risk of running out of memory.

On the kernel side each connection will still need buffers for incoming and
outgoing bytes. This may be somewhat controllable via socket options, but again
it’ll have to be the subject of a future post.

Try to not run out of RAM. Bad things tend to happen.

## kTLS

kTLSis a feature of the Linux kernel where an application can hand off
the job of encryption/decryption to the kernel. The application still has to
perform the TLS handshake, but after that it can enable kTLS and pretend that
it’s all sent in plaintext.

You may say that this doesn’t actually speed anything up, it just moveswhereencryption was done. But there are gains:

1. This means thatsendfile()can be used, removing the need to copy a bunch
of data between user space and kernel space.
2. If the network card has hardware support for it, the crypto operation may
actually be offloaded from the CPU onto the network card, leaving the CPU to
do better things.

## Descriptorless files

Another optimization is to avoid passing file descriptors back and forth
between user space and kernel space. The mapping between file descriptors and
io_uring apparently has overhead.

So in comesdescriptorless filesviaregister_files.

Now the supposed file descriptor numbers that user space sees are just
integers. They don’t show up in/proc/pid/fd, and can only be used with
io_uring. They’re still capped by theulimitfile descriptor limit, though.

## tarweb

In order to learn these technologies better, I builta web server
incorporating all these things.

It’s namedtarwebbecause it’s a web server that serves the content of a
single tar file.

Rust, io_uring, and kTLS. Not exactly the most common combination. I found that
io_uring and kTLS didn’t play super well together. Enabling kTLS requires threesetsockopt()calls, and io_uring doesn’t supportsetsockopt(until they
mergemy PR, that is).

And thektlscrate, part ofrustls, only allows you to call the synchronoussetsockopt(), not export the needed struct for me to pass to my new
io_uringsetsockopt.Another pr sent.

So with those two PRs merged, it’s working great.

tarweb is far from perfect. The code needs a lot of work, and there’s no
guarantee that the TLS library (rustls) doesn’t do memory allocations during
handshakes. But it does serve https without even one syscall on a per request
basis. And that’s pretty cool.

## Benchmarks

I have not done any benchmarks yet. I want to clean the code up first.

## io-uring and safety

One thing making io_uring more complex than synchronous syscalls is that any
buffer needs to stay in memory until the operation is marked completed by
showing up in the completion queue.

For example when submitting awriteoperation, the memory location of those
bytes must not be deallocated or overwritten.

Theio-uringcrate doesn’t help much with this. The API doesn’t allow the
borrow checker to protect you at compile time, and I don’t see it doing any
runtime checks either.

I feel like I’m back in C++, where any mistake can blow your whole leg off.
It’s a miracle that I’ve not seen a segfault.

Someone should make asafer-ringcrate or similar, using the powers ofpinningand/or borrows or something, to achieve Rust’s normal “if it
compiles, then it’s correct”.

Edit: I’mnot the first to point it
out.

This post wasdiscussed on HackerNews on
2025-08-22.

View the comments.
