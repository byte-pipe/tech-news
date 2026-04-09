---
title: I'm too dumb for Zig's new IO interface
url: https://www.openmymind.net/Im-Too-Dumb-For-Zigs-New-IO-Interface/
site_name: lobsters
fetched_at: '2025-08-23T23:07:53.866919'
original_url: https://www.openmymind.net/Im-Too-Dumb-For-Zigs-New-IO-Interface/
date: '2025-08-23'
description: Karl Seguin's Blog - A mix of coding and creative writing
tags: zig
---

# I'm too dumb for Zig's new IO interface

Aug 22, 2025

You might have heard that Zig 0.15 introduces a new IO interface, with the focus for this release being the new std.Io.Reader and std.Io.Writer types. The old "interfaces" had problems. Likethis performance issuethat I opened. And it relied on amix of types, which always confused me, and a lot ofanytype- which is generally great, but a poor foundation to build an interface on.

I've been slowly upgrading my libraries, and I ran into changes to thetls.Clientclient used by my smtp library. For the life of me, I just don't understand how it works.

Zig has never been known for its documentation, but if we look at the documentation fortls.Client.init, we'll find:

pub

fn

init
(
input
:

*
std
.
Io
.
Reader
,
 output
:

*
std
.
Io
.
Writer
,
 options
:

Options
)
 InitError
!
Client
Initiates a TLS handshake
and
 establishes a TLSv1
.
2

or
 TLSv1
.
3
 session
.

So it takes one of these new Readers and a new Writer, along with some options (sneak peak, which aren't all optional). It doesn't look like you can just give it anet.Stream, butnet.Streamdoes expose areader()andwriter()method, so that's probably a good place to start:

const
 stream
=

try
 std
.
net
.
tcpConnectToHost
(
allocator
,

"www.openmymind.net"
,

443
)
;

defer
 stream
.
close
(
)
;

var
 writer
=
 stream
.
writer
(
&
.
{
}
)
;

var
 reader
=
 stream
.
reader
(
&
.
{
}
)
;

var
 tls_client
=

try
 std
.
crypto
.
tls
.
Client
.
init
(

 reader
.
interface
(
)
,


&
writer
.
interface
,


.
{
}
,

// options TODO

)
;

Note thatstream.writer()returns aStream.Writerandstream.reader()returns aStream.Reader- those aren't the types ourtls.Clientexpects. To convert theStream.Readerto an*std.Io.Reader, we need to call itsinterface()method. To get a*std.io.Writerfrom anStream.Writer, we need the address of its&interfacefield. This doesn't seem particularly consistent. Don't forget that thewriterandreaderneed a stable address. Because I'm trying to get the simplest example working, this isn't an issue - everything will live on the stack ofmain. In a real word example, I think it means that I'll always have to wrap thetls.Clientinto my own heap-allocated type; giving the writer and reader have a cozy stable home.

Speaking of allocations, you might have noticed thatstream.writerandstream.readertake a parameter. It's the buffer they should use. Buffering is a first class citizen of the new Io interface - who needs composition? The documentationdoestell me these need to be at leaststd.crypto.tls.max_ciphertext_record_lenlarge, so we need to fix things a bit:

var
 write_buf
:

[
std
.
crypto
.
tls
.
max_ciphertext_record_len
]
u8

=

undefined
;

var
 writer
=
 stream
.
writer
(
&
write_buf
)
;

var
 read_buf
:

[
std
.
crypto
.
tls
.
max_ciphertext_record_len
]
u8

=

undefined
;

var
 reader
=
 stream
.
reader
(
&
read_buf
)
;

Here's where the code stands:

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
)

!
void

{


var
 gpa
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
 allocator
=
 gpa
.
allocator
(
)
;


const
 stream
=

try
 std
.
net
.
tcpConnectToHost
(
allocator
,

"www.openmymind.net"
,

443
)
;


defer
 stream
.
close
(
)
;


var
 write_buf
:

[
std
.
crypto
.
tls
.
max_ciphertext_record_len
]
u8

=

undefined
;


var
 writer
=
 stream
.
writer
(
&
write_buf
)
;


var
 read_buf
:

[
std
.
crypto
.
tls
.
max_ciphertext_record_len
]
u8

=

undefined
;


var
 reader
=
 stream
.
reader
(
&
read_buf
)
;


var
 tls_client
=

try
 std
.
crypto
.
tls
.
Client
.
init
(

 reader
.
interface
(
)
,


&
writer
.
interface
,


.
{


}
,


)
;


defer
 tls_client
.
end
(
)

catch

{
}
;

}

But if you try to run it, you'll get a compilation error. Turns out we have to provide 4 options: the ca_bundle, a host, awrite_bufferand aread_buffer. Normally I'd expect the options parameter to be for optional parameters, I don't understand why some parameters (input and output) are passed one way whilewriter_bufferandread_bufferare passed another.

Let's give it what it wants AND send some data:

// existing setup...

var
 bundle
=

std
.
crypto
.
Certificate
.
Bundle
{
}
;

try
 bundle
.
rescan
(
allocator
)
;

defer
 bundle
.
deinit
(
allocator
)
;

var
 tls_client
=

try
 std
.
crypto
.
tls
.
Client
.
init
(

 reader
.
interface
(
)
,


&
writer
.
interface
,


.
{


.
ca
=

.
{
.
bundle
=
 bundle
}
,


.
host
=

.
{

.
explicit
=

"www.openmymind.net"

}

,


.
read_buffer
=

&
.
{
}
,


.
write_buffer
=

&
.
{
}
,


}
,

)
;

defer
 tls_client
.
end
(
)

catch

{
}
;

try
 tls_client
.
writer
.
writeAll
(
"GET / HTTP/1.1\r\n\r\n"
)
;

Now, if I try to run it, the program just hangs. I don't know whatwrite_bufferis, but I know Zig now loves buffers, so let's try to give it something:

// existing setup...

// I don't know what size this should/has to be??

var
 write_buf2
:

[
std
.
crypto
.
tls
.
max_ciphertext_record_len
]
u8

=

undefined
;

var
 tls_client
=

try
 std
.
crypto
.
tls
.
Client
.
init
(

 reader
.
interface
(
)
,


&
writer
.
interface
,


.
{


.
ca
=

.
{
.
bundle
=
 bundle
}
,


.
host
=

.
{

.
explicit
=

"www.openmymind.net"

}

,


.
read_buffer
=

&
.
{
}
,


.
write_buffer
=

&
write_buf2
,


}
,

)
;

defer
 tls_client
.
end
(
)

catch

{
}
;

try
 tls_client
.
writer
.
writeAll
(
"GET / HTTP/1.1\r\n\r\n"
)
;

Great, now the code doesn't hang, all we need to do is read the response.tls.Clientexposes areader: *std.Io.Readerfield which is "Decrypted stream from the server to the client." That sounds like what we want, but believe it or notstd.Io.Readerdoesn't have areadmethod. It has apeakatakeByteSigned, areadSliceShort(which seems close, but it blocks until the provided buffer is full), apeekArrayand a lot more, but nothing like thereadI'd expect. The closest I can find, which I think does what I want, is to stream it to a writer:

var
 buf
:

[
1024
]
u8

=

undefined
;

var
 w
:

std
.
Io
.
Writer

=

.
fixed
(
&
buf
)
;

const
 n
=

try
 tls_client
.
reader
.
stream
(
&
w
,

.
limited
(
buf
.
len
)
)
;

std
.
debug
.
print
(
"read: {d} - {s}\n"
,

.
{
n
,
 buf
[
0
..
n
]
}
)
;

If we try to run the code now, it crashes. We've apparently failed an assertion regarding the length of a buffer. So it seems like we alsohaveto provide aread_buffer.

Here's my current version (it doesn't work, but it doesn't crash!):

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
)

!
void

{


var
 gpa
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
 allocator
=
 gpa
.
allocator
(
)
;


const
 stream
=

try
 std
.
net
.
tcpConnectToHost
(
allocator
,

"www.openmymind.net"
,

443
)
;


defer
 stream
.
close
(
)
;


var
 write_buf
:

[
std
.
crypto
.
tls
.
max_ciphertext_record_len
]
u8

=

undefined
;


var
 writer
=
 stream
.
writer
(
&
write_buf
)
;


var
 read_buf
:

[
std
.
crypto
.
tls
.
max_ciphertext_record_len
]
u8

=

undefined
;


var
 reader
=
 stream
.
reader
(
&
read_buf
)
;


var
 bundle
=

std
.
crypto
.
Certificate
.
Bundle
{
}
;


try
 bundle
.
rescan
(
allocator
)
;


defer
 bundle
.
deinit
(
allocator
)
;


var
 write_buf2
:

[
std
.
crypto
.
tls
.
max_ciphertext_record_len
]
u8

=

undefined
;


var
 read_buf2
:

[
std
.
crypto
.
tls
.
max_ciphertext_record_len
]
u8

=

undefined
;


var
 tls_client
=

try
 std
.
crypto
.
tls
.
Client
.
init
(

 reader
.
interface
(
)
,


&
writer
.
interface
,


.
{


.
ca
=

.
{
.
bundle
=
 bundle
}
,


.
host
=

.
{

.
explicit
=

"www.openmymind.net"

}

,


.
read_buffer
=

&
read_buf2
,


.
write_buffer
=

&
write_buf2
,


}
,


)
;


defer
 tls_client
.
end
(
)

catch

{
}
;


try
 tls_client
.
writer
.
writeAll
(
"GET / HTTP/1.1\r\n\r\n"
)
;


var
 buf
:

[
std
.
crypto
.
tls
.
max_ciphertext_record_len
]
u8

=

undefined
;


var
 w
:

std
.
Io
.
Writer

=

.
fixed
(
&
buf
)
;


const
 n
=

try
 tls_client
.
reader
.
stream
(
&
w
,

.
limited
(
buf
.
len
)
)
;

 std
.
debug
.
print
(
"read: {d} - {s}\n"
,

.
{
n
,
 buf
[
0
..
n
]
}
)
;

}

When I looked through Zig's source code, there'sonly one placeusingtls.Client. It helped to get me where where I am. I couldn't find any tests.

I'll admit that during this migration, I've missed some basic things. For example, someone had to help me findstd.fmt.printInt- the renamed version ofstd.fmt.formatIntBuf. Maybe there's a helper like:tls.Client.init(allocator, stream)somewhere. And maybe it makes sense that we doreader.interface()but&writer.interface- I'm reminded of Go's*http.Requestandhttp.ResponseWrite. And maybe Zig has some consistent rule for what parameters belong in options. And I know nothing about TLS, so maybe it makes complete sense to need 4 buffers. I feel a bit more confident about the weirdness of not having aread(buf: []u8) !usizefunction onReader, but at this point I wouldn't bet on me.
