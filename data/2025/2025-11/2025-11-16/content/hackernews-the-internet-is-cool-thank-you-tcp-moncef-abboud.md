---
title: The Internet is Cool. Thank you, TCP | Moncef Abboud
url: https://cefboud.com/posts/tcp-deep-dive-internals/
site_name: hackernews
fetched_at: '2025-11-16T11:07:01.487220'
original_url: https://cefboud.com/posts/tcp-deep-dive-internals/
author: Moncef Abboud
date: '2025-11-16'
published_date: '2025-11-14T00:00:00+00:00'
description: An exploration of TCP, the workhorse of the internet. This deep dive includes detailed examples and a step-by-step walkthrough.
---

The Internet is Cool. Thank you, TCP




Contents



The Internet is Cool. Thank you, TCP



The internet is incredible. It’s nearly impossible to keep people away from. But it can also be unreliable: packets drop, links congest, bits mangle, and data corrupts.Oh, it’s dangerous out there!(I’m writing this in Kramer’s tone)

So how is it possible that our apps just work? If you’ve networked your app before, you know the drill:socket()/bind()here,accept()there, maybe aconnect()over there, and it just works. Reliable, orderly, uncorrupted data flows to and fro.

Websites (HTTP), email (SMTP) or remote access (SSH) are all built on top of TCP and just work.

## Why TCP

Why do we need TCP? Why can’t we just use the layer below, IP?

Remember, the network stack goes: Physical –> Data Link (Ethernet/Wi-Fi, etc) –> Network (IP) –> Transport (TCP/UDP).

IP (Layer 3) operates at the host level, while the transport layer (TCP/UDP) works at the application level using ports. IP can deliver packets to the correct host via its IP address, but once the data reaches the machine, it still needs to be handed off to the correct process. Each process “binds” to a port: its address within the machine. A common analogy is: the IP address is the building, and the port is the apartment. Processes or apps live in those apartments.

Another reason we need TCP is that if a router (a piece of infra your average user does not control) drops packets or becomes overloaded, TCP at the edges (on the users’ machines) can recover without requiring routers to participate. The routers stay simple, the reliability happens at the endpoints.

Packets get lost, corrupted, duplicated, and reordered. That’s just how the internet works. TCP shields developers from these issues. It handles retransmission, checksums, and a gazillion other reliability mechanisms. If every developer had to implement those themselves, they’d never have time to properly align their flexboxes, a truly horrendous alternate universe.

Jokes aside, the guarantee that data sent and received over a socket isn’t corrupted, duplicated, or out of order, despite the underlying network being unreliable, is exactly why TCP is awesome.

## Flow and Congestion Control

When you step back and think about network communication, here’s what we’re really trying to do: machine A sends data to machine B. Machine B has a finite amount of space and must store the incoming data somewhere before passing it to the application, which might be asleep or busy. This temporary storage takes the name of areceive bufferand is managed by the kernel:

sysctl net.ipv4.tcp_rmem=>net.ipv4.tcp_rmem = 4096 131072 6291456, a min of 4k, default of 128k and max of 8M.

The problem is that space is finite. If you’re transferring a large file (hundreds of MBs or even GBs), you could easily overwhelm the destination. The receiver therefore needs a way to tell the sender how much more data it can handle. This mechanism is calledflow control, and TCP segments include a field called thewindow, which specifies how much data the receiver is currently willing to accept.

Another issue is overwhelming the network itself, even if the receiving machine has plenty of buffer space. You’re only as strong as your weakest link: some links carry gigabits, others only megabits. If you don’t tune for the slowest link, congestion is inevitable.

Fun fact: in 1986, the Internet’s bandwidth dropped from a few dozen KB/s to as low as40 bps(yes, bits per second! yes, those numbers are wild!), in what became known ascongestion collapse. When packets were lost and systems retried sending them, they made congestion even worse: a doom loop. To fix this, TCP incorporated ‘play nice’ and ‘back off’ behaviors known ascongestion control, which help prevent the Internet from clogging itself to death.

## Some Code: A Plain TCP Server

With all low-level things like TCP, C examples are the way to go. Just show it like it is.



1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38

#include

<stdio.h>

#include

<stdlib.h>

#include

<string.h>

#include

<unistd.h>

#include

<arpa/inet.h>

#include

<signal.h>

int

sockfd

=

-
1
,

clientfd

=

-
1
;

void

handle_sigint
(
int

sig
)

{


printf
(
"
\n
Ctrl+C caught, shutting down...
\n
"
);


if

(
clientfd

!=

-
1
)

close
(
clientfd
);


if

(
sockfd

!=

-
1
)

close
(
sockfd
);


exit
(
0
);

}

int

main
()

{


signal
(
SIGINT
,

handle_sigint
);


sockfd

=

socket
(
AF_INET
,

SOCK_STREAM
,

0
);


int

opt

=

1
;


// SO_REUSEADDR to force bind to the port even if an older socket is still terminating (TIME_WAIT)


setsockopt
(
sockfd
,

SOL_SOCKET
,

SO_REUSEADDR
,

&
opt
,

sizeof
(
opt
));


struct

sockaddr_in

addr

=

{

.
sin_family

=

AF_INET
,

.
sin_port

=

htons
(
8080
),

.
sin_addr
.
s_addr

=

INADDR_ANY

};


bind
(
sockfd
,

(
struct

sockaddr
*
)
&
addr
,

sizeof
(
addr
));


listen
(
sockfd
,

5
);


printf
(
"Listening on 8080...
\n
"
);


clientfd

=

accept
(
sockfd
,

NULL
,

NULL
);


char

buf
[
1024
],

out
[
2048
];


int

n
;


while

((
n

=

recv
(
clientfd
,

buf
,

sizeof
(
buf
)

-

1
,

0
))

>

0
)

{


buf
[
n
]

=

'\0'
;


int

m

=

snprintf
(
out
,

sizeof
(
out
),

"you sent: %s"
,

buf
);


printf
(
"response %s %d
\n
"
,

out
,

m
);


send
(
clientfd
,

out
,

m
,

0
);


}


close
(
clientfd
);

close
(
sockfd
);

}

This create a TCP server that echoes what the client sends prefixed with ‘You sent:’.



1
2
3
4
5
6

# compile and run server

gcc
-o
 server server.c
&&
 ./server

# connect client

telnet 127.0.0.1 8080

# hi

# you sent: hi

127.0.0.1(localhost) could be replace with a remote IP and it should work all the same.

We used the following primitives/functions follow the Berkley Socket way of doing things (released with BDS 4.2):

* SOCKET: create an endpoint (structure in the kernel).BIND: associate to a port.LISTEN: get ready to accept connection and a specify queue size of pending connection (beyond that size, drop!)ACCEPT: accept an incoming connection (TCP Server)CONNECT: attempt connection (TCP client)SEND: send dataRECEIVE: receive dataCLOSE: release the connection
* BIND: associate to a port.LISTEN: get ready to accept connection and a specify queue size of pending connection (beyond that size, drop!)ACCEPT: accept an incoming connection (TCP Server)CONNECT: attempt connection (TCP client)SEND: send dataRECEIVE: receive dataCLOSE: release the connection
* LISTEN: get ready to accept connection and a specify queue size of pending connection (beyond that size, drop!)ACCEPT: accept an incoming connection (TCP Server)CONNECT: attempt connection (TCP client)SEND: send dataRECEIVE: receive dataCLOSE: release the connection
* ACCEPT: accept an incoming connection (TCP Server)CONNECT: attempt connection (TCP client)SEND: send dataRECEIVE: receive dataCLOSE: release the connection
* CONNECT: attempt connection (TCP client)SEND: send dataRECEIVE: receive dataCLOSE: release the connection
* SEND: send dataRECEIVE: receive dataCLOSE: release the connection
* RECEIVE: receive dataCLOSE: release the connection
* CLOSE: release the connection

In the example above, we’re using client/server dynamics in a request/response pattern. But I can add the following aftersend:



1
2
3
4

send
(
clientfd
,

out
,

m
,

0
);

sleep
(
5
);

const

char

*
msg

=

"not a response, just doing my thing
\n
"
;

send
(
clientfd
,

msg
,

strlen
(
msg
),

0
);

Compile, run, and telnet:



1
2
3
4
5

client here
you sent: client here
client again
not a response, just doing my thing
you sent: client again

I typed in the telnet terminal:client here, thenclient again. I only gotyou sent: client here, then the server was sleeping. My second line,client again, was patiently waiting in the receive buffer. The server sentnot a response, just doing my thing, then picked up my second TCP packet and replied withyou sent: client again.

This is very much a duplex bidirectional link. Each side sends what it wishes, it just happens that at the beginning, one listens and the other connects. The dynamics afterwards don’t have to follow a request/response pattern.

## Catfishing Curl: A Dead Simple HTTP Server

Let’s create a very simple HTTP/1.1 server (later versions are trickier).



1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29


// same as before


printf
(
"Listening on 8080...
\n
"
);


int

i

=

1
;


while

(
1
)

{


clientfd

=

accept
(
sockfd
,

NULL
,

NULL
);


char

buf
[
1024
],

out
[
2048
];


int

n
;


while

((
n

=

recv
(
clientfd
,

buf
,

sizeof
(
buf
)

-

1
,

0
))

>

0
)

{


buf
[
n
]

=

'\0'
;


int

body_len

=

snprintf
(
out
,

sizeof
(
out
),

"[%d] Yo, I am a legit web server
\n
"
,

i
++
);


char

header
[
256
];


int

header_len

=

snprintf
(


header
,

sizeof
(
header
),


"HTTP/1.1 200 OK
\r\n
"


"Content-Type: text/plain
\r\n
"


"Content-Length: %d
\r\n
"


"Connection: close
\r\n
"


"
\r\n
"
,


body_len


);


printf
(
"header: %s
\n
"
,

header
);


printf
(
"out: %s
\n
"
,

out
);


send
(
clientfd
,

header
,

header_len
,

0
);


send
(
clientfd
,

out
,

body_len
,

0
);


break
;

// one request per connection


}


close
(
clientfd
);


}



1
2
3
4

~ curl localhost:8080

[
1] Yo, I am a legit web server
~ curl localhost:8080

[
2] Yo, I am a legit web server

We’re usingito keep count of requests. We’re establishing a TCP connection and returning the HTTP headers expected by the HTTP client (the TCP peer, really). A real HTTP server would return proper HTML, CSS, and JS, and handle a whole lot of other options and headers. But underneath, it’s simply a process making use of our reliable, dependable TCP.

## The Actual Bytes



1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18

 0 <----- 32 bits ------>
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
 | Source Port | Destination Port |
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
 | Sequence Number |
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
 | Acknowledgment Number |
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
 | Header|Rese-| Flags | Window Size |
 | Len |rved | | |
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
 | Checksum | Urgent Pointer |
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
 | Options (if any) |
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
 | Data (Payload) |
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

Each TCP segment has the header above. And each TCP segment is contained within a IP packet. We have a source and destination ports. Each 16 bits, and that’s where the 64k port limit comes from!

Each transport-layer connection is5-tuple (TCP/UDP, src IP, src port, dst IP, dst port).

### Sequence and Acknowledgment Numbers

TCP reliability depends on two key fields: theSequence number, indicating which bytes a segment carries, and theAcknowledgment number, indicating which bytes have been received. Sequence numbers let the receiver interpret data order, detect and reorder out-of-order segments, and identify losses. TCP usescumulative acknowledgments—an ACK of 100 means bytes 0-99 were received. If bytes 100-120 are lost but later bytes arrive, the ACK remains 100 until the missing data is received.



1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26

1. A --> B: Send [Seq=0-99]
2. B --> A: Send [Seq=0-49]

3. B --> A: Receives A's [0-99] --> sends ACK=100
4. A --> B: Receives B's [0-49] --> sends ACK=50

5. A --> B: Send [Seq=100-199] --- lost ---
6. B --> A: Send [Seq=50-99] --- lost ---

7. A --> B: Send [Seq=200-299]
 B receives --> notices gap (100-199 missing) --> sends ACK=100

8. B --> A: Send [Seq=100-149]
 A receives --> notices gap (50-99 missing) --> sends ACK=50

9. A --> B: Send [Seq=300-399]
 B still missing 100-199 --> sends ACK=100

10. B --> A: Send [Seq=150-199]
 A still missing 50-99 --> sends ACK=50

11. A --> B: Retransmit [Seq=100-199]
 B receives --> now has 0-399 --> sends ACK=400

12. B --> A: Retransmit [Seq=50-99]
 A receives --> now has 0-199 --> sends ACK=200

Header Length shows how many 4-byte words are in the header, needed because the Options field is variable length, and thus so is the header.

### TCP Flags

Next are 8 flags (1 bit each). A few important ones:

SYN: used to establish a connection.ACK: indicates the Acknowledgment number is valid.

These two flags are central to connection setup. Why establish a connection? To detect out-of-order or duplicate segments you must track what has been sent and received i.e., maintain a state or a connection.

SYNandACKparticipate in the famous 3-way handshake:

* A –> B:SYN(I want to connect)B –> A:SYN+ACK(I got your SYN, I want to connect too!)A –> B:ACK(got it, connection established!)
* B –> A:SYN+ACK(I got your SYN, I want to connect too!)A –> B:ACK(got it, connection established!)
* A –> B:ACK(got it, connection established!)

TheFINflag signals teardown and also uses a handshake:

* X –> Y:FIN(I want to disconnect)Y –> X:ACK(got your FIN, whatever!)Y –> X:FIN(I want to disconnect too - sometimes sent with the previous ACK)X –> Y:ACK(got it!)
* Y –> X:ACK(got your FIN, whatever!)Y –> X:FIN(I want to disconnect too - sometimes sent with the previous ACK)X –> Y:ACK(got it!)
* Y –> X:FIN(I want to disconnect too - sometimes sent with the previous ACK)X –> Y:ACK(got it!)
* X –> Y:ACK(got it!)

This is normally a 4-way (sometimes 3-way) goodbye handshake.

RSTis the reset flag. It indicates an error or forced shutdown — drop the connection immediately. An OS sendsRSTif no process is listening or if the listening process crashed. There’s also a known TCP reset attack where intermediaries injectRSTto terminate connections (used by some firewalls).

### Window

We talked about this field in flow control. As mentionned above, this indicates how many bytes the receiver is willing to receive after the acknowledged number.

With the example above, runningss(Socket Statistics) provides info about the TCP connection.



1
2
3
4

ss
-tlpmi

// State Recv-Q Send-Q Local Address:Port Peer Address:Port Process
// LISTEN 0 5 0.0.0.0:http-alt 0.0.0.0:
*

users
:
((
"server"
,pid
=
1113,fd
=
3
))

// 	 skmem:
(
r0,rb131072,t0,tb16384,f0,w0,o0,bl0,d0
)
 cubic cwnd:10

rb131072(128KB) is the receive buffer size, whiletb16384(16KB) is the transmit buffer size, where data waits before being sent over the network.Send-Qindicates bytes not yet acknowledged by the remote host, andRecv-Qshows bytes received but not yet read by the application (e.g., data waiting in from the second line in telnet session above, while the server was sleeping).

### Checksum

Checksum is used for reliability. All 16-bit words in the TCP segment are added together, and the result is compared to the checksum. If they don’t match, it means some bits were likely corrupted, and retransmission is needed.

## Conclusion

It always amazes me how all this works. The network, the internet. Reliably and continuously. Just a few decades ago, sending a few KB was quite the feat. And today, streaming 4k is banal. God bless all those hardworking people that made and make it all possible!



Technical Writing
,
Open Source


QEMU

Docker

Go

Linux
 This post is licensed under
 CC BY 4.0
 by the author.

Share
