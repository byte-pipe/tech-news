---
title: Cloudflare Workers and Containers now support inbound TCP connections and gRPC | The Cloudflare Blog
url: https://blog.cloudflare.com/grpc-workers/
site_name: tldr
content_file: tldr-cloudflare-workers-and-containers-now-support-inbo
fetched_at: '2026-08-06T12:55:16.354790'
original_url: https://blog.cloudflare.com/grpc-workers/
date: '2026-08-06'
published_date: '2026-08-03T13:00:00.000Z'
description: Cloudflare Workers now support inbound TCP connections via Spectrum, allowing direct socket forwarding to Durable Objects and Containers. Developers can run full-duplex gRPC applications or leverage automatic gRPC-to-gRPC-web translation directly within Workers.
tags:
- tldr
---

AI is changing how people interact with computers, and voice is becoming an increasingly important part of that shift. Real-time assistants, AI-powered dictation, and other voice interfaces need low-latency communication between clients, models, and supporting services. Many developers usegRPC, a Remote Procedure Call (RPC) framework built on HTTP/2 and TCP, for this infrastructure.

Ever since Workerslaunched in 2017, we’ve been expanding their capabilities, including adding the ability toopen outbound TCP connectionsand aJavaScript-native RPC systembuilt onCap’n Proto. And so as part of Agents Week, we’re extending Workers in the other direction, supporting inbound TCP connections and adding new ways to run gRPC applications on Cloudflare.

Today, we’re announcing:

* connect(socket)— a newhandlerin the Workers runtime that lets your Worker directly accept an inbound TCP socket provided bySpectrum(Cloudflare’s ingress proxy for non-HTTP traffic)
* Full-duplex, bi-directional gRPC from Cloudflare Containers— forward the socket from your Worker to your gRPC server running in a container
* Workers can serve unary and server-streaming gRPC APIs and call gRPC servers— you write your code usinggRPC-web, and Cloudflare automatically converts incoming and outgoing requests to gRPC

We’re introducing this in private beta — you can sign uphere.

Let’s dig into each of these below.

## connect(socket) from your Worker to Durable Objects and Containers

The Workers runtime now provides aconnect() handlerthat accepts a socket that you can read from and write to:

export
 default
 {

	async
 connect
(
socket
)
:
 Promise
<
void
> {

		const
 writer
 =
 socket.writable.
getWriter
();

		await
 writer.
write
(
new
 TextEncoder
().
encode
(
"Hello, world!
\n
"
));

		await
 writer.
close
();

	},

} 
satisfies
 ExportedHandler
;

You can pass this socket from one Worker to another Worker, or from a Worker to a Durable Object. This lets your Worker control where an incoming TCP connection is routed:

import
 { DurableObject } 
from
 "cloudflare:workers"
;

export
 class
 SocketDurableObject
 extends
 DurableObject
<
Env
> {

	async
 connect
(
socket
:
 Socket
)
:
 Promise
<
void
> {

		// Echo bytes from inside the Durable Object

		await
 socket.readable.
pipeTo
(socket.writable);

	}

}

export
 default
 {

	async
 connect
(
socket
, 
env
)
:
 Promise
<
void
> {

		const
 stub
 =
 env.
SOCKET_DO
.
getByName
(
"my-server"
);

		const
 durableObjectSocket
 =
 stub.
connect
(
"host:port"
);

		await
 Promise
.
all
([

			socket.readable.
pipeTo
(durableObjectSocket.writable),

			durableObjectSocket.readable.
pipeTo
(socket.writable),

		]);

	},

} 
satisfies
 ExportedHandler
<
Env
>;

You can pass a socket from a Durable Object toits Container:

import
 { DurableObject } 
from
 "cloudflare:workers"
;

export
 class
 SocketContainer
 extends
 DurableObject
<
Env
> {

	constructor
(
ctx
:
 DurableObjectState
, 
env
:
 Env
) {

		super
(ctx, env);

		this
.ctx.container
!
.
start
();

	}

	async
 connect
(
socket
:
 Socket
)
:
 Promise
<
void
> {

		const
 containerSocket
 =
 this
.ctx.container
!

			.
getTcpPort
(
8080
)

			.
connect
(
"10.0.0.1:8080"
);

		await
 containerSocket.opened;

		await
 Promise
.
all
([

			socket.readable.
pipeTo
(containerSocket.writable),

			containerSocket.readable.
pipeTo
(socket.writable),

		]);

	}

}

And then handle the socket in the container:

# server.py

import
 socketserver

class
 Handler
(
socketserver
.
BaseRequestHandler
):

 def
 handle
(self):

 while
 data 
:=
 self
.request.recv(
64
 *
 1024
):

 self
.request.sendall(
b
"Echo: "
 +
 data)

class
 Server
(
socketserver
.
ThreadingTCPServer
):

 allow_reuse_address 
=
 True

 daemon_threads 
=
 True

with
 Server((
"0.0.0.0"
, 
8080
), Handler) 
as
 server:

 server.serve_forever()

This gives you full control over the entire path from client to your server running in a container on Cloudflare, opening the door to full-duplex communication between client and server running any program, in any language, for any TCP-based protocol.

To expose the raw TCP socket to the client, we’re introducing a new type ofSpectrumapplication, where you specify a Worker that you want incoming TCP connections to be routed to.Spectrumis Cloudflare’s ingress proxy for non-HTTP traffic, and allows Cloudflare to sit in front of any TCP or UDP application.

## Bidirectional gRPC from Cloudflare Containers

gRPCis a well-established and popular Remote Procedure Call (RPC) framework that was initially released by Google almost 10 years ago, and is now used across mobile apps, distributed systems, and most recently — voice AI applications.

Real-time voice AI applications demand low-latency, and both client and server to be able to send messages to each other over a single, persistent connection. WebSockets and Durable Objects are excellent fits for this, and the Cloudflare Agents SDK provides@cloudflare/voiceto make this easy. But there is a ton of software out there that uses gRPC for real-time client-server communication.

Using the APIs described above, you can now deploy gRPC servers to Cloudflare, written in any language, with full support for bidirectional streaming between client and server. This lets you take advantage of Cloudflare’s network of330+ locationsand handle requests much closer to clients than is possible elsewhere. We’re excited about the doors this opens up for low-latency voice and colocated inference.

For example, here’s a minimal gRPC server that echoes messages it receives back to the client:

package
 main

import
 (

	"
io
"

	"
log
"

	"
net
"

	pb 
"
example/proto
"

	"
google.golang.org/grpc
"

)

type
 server
 struct
 {

	pb
.
UnimplementedByteStreamServer

}

func
 (
server
) 
Chat
(
stream
 pb
.
ByteStream_ChatServer
) 
error
 {

	if
 err 
:=
 stream.
Send
(
&
pb
.
ByteChunk
{

		Payload: []
byte
(
"connected
\n
"
),

	}); err 
!=
 nil
 {

		return
 err

	}

	for
 {

		message, err 
:=
 stream.
Recv
()

		if
 err 
==
 io.EOF {

			return
 stream.
Send
(
&
pb
.
ByteChunk
{

				Payload: []
byte
(
"goodbye
\n
"
),

			})

		}

		if
 err 
!=
 nil
 {

			return
 err

		}

		if
 err 
:=
 stream.
Send
(
&
pb
.
ByteChunk
{

			Payload: 
append
([]
byte
(
"echo: "
), message.Payload
...
),

		}); err 
!=
 nil
 {

			return
 err

		}

	}

}

func
 main
() {

	listener, err 
:=
 net.
Listen
(
"tcp"
, 
":50051"
)

	if
 err 
!=
 nil
 {

		log.
Fatal
(err)

	}

	grpcServer 
:=
 grpc.
NewServer
()

	pb.
RegisterByteStreamServer
(grpcServer, 
&
server
{})

	log.
Println
(
"gRPC server listening on :50051"
)

	log.
Fatal
(grpcServer.
Serve
(listener))

}

With this, there’s pretty much no gRPC-based application that you can’t deploy to Cloudflare, no matter what language it’s in or dependencies it relies on. But what if you need to do something simpler, and just serve a basic gRPC server or connect from a Worker to a gRPC server running somewhere else?

## Workers as gRPC servers and clients with gRPC to gRPC-web conversion — no container needed

gRPC-webis a browser-compatible version of gRPC. Web browsers don’t expose the lower-level HTTP/2 features that gRPC requires, and there is no raw TCP Socket API built into web browsers — this is why the WebSocket API exists, and why Workers have supported WebSocketssince 2021.

HTTP/2 splits each request and response into small binary messages calledframes. This is core to how a single HTTP/2 or HTTP/3 connection is able to multiplex — many requests can be interleaved over one connection. Each frame has a stream ID, allowing the receiver to reassemble it into the correct request or response. gRPC depends on this stream-level control for efficient streaming, cancellation, flow control, andtrailers.

Web platform APIs likefetch()don’t provide this control. So how can we make it simple and easy to use gRPC from Cloudflare Workers — without clients needing to make any changes? We translate incoming gRPC to gRPC-web, and translate outgoing gRPC-web to gRPC.

We’ve actually used gRPC-web within Cloudflare’s reverse proxy since 2020, when we wrote about theRoad to gRPCon the Cloudflare blog. We convert requests to HTTP/1.1 so that messages can be inspected and gRPC apps can benefit fromCloudflare’s security features, like WAF rules and Bot Management.

Now, in private beta and then rolling out to everyone, we’re extending this so that given a Protocol Buffer (protobuf) definition file like this:

syntax 
=
 "proto3"
;

package hello;

service 
Greeter
 {

 rpc 
SayHello
 (
HelloRequest
) returns (
HelloReply
);

}

message 
HelloRequest
 {

 string name 
=
 1
;

}

message 
HelloReply
 {

 string message 
=
 1
;

}

You can write a unary gRPC server in a Worker in just a few lines of code, using the@connectrpc/connectopen-source package:

import
 { createConnectRouter } 
from
 "@connectrpc/connect"
;

import
 {

 universalServerRequestFromFetch,

 universalServerResponseToFetch,

} 
from
 "@connectrpc/connect/protocol"
;

import
 { Greeter } 
from
 "./gen/hello_pb"
;

const
 router
 =
 createConnectRouter
();

router.
service
(Greeter, {

 sayHello
: ({ 
name
 }) 
=>
 ({ message: 
`Hello, ${
name
}!`
 }),

});

const
 handlers
 =
 new
 Map
(

 router.handlers.
map
((
handler
) 
=>
 [handler.requestPath, handler]),

);

export
 default
 {

 async
 fetch
(
request
:
 Request
)
:
 Promise
<
Response
> {

 const
 handler
 =
 handlers.
get
(
new
 URL
(request.url).pathname);

 return
 universalServerResponseToFetch
(

 await
 handler
(
universalServerRequestFromFetch
(request, {})),

 );

 },

} 
satisfies
 ExportedHandler
;

You can make outbound requests to external gRPC servers this way too, by using the client built into@connectrpc/connect:

import
 { createClient } 
from
 "@connectrpc/connect"
;

import
 { createGrpcWebTransport } 
from
 "@connectrpc/connect-web"
;

import
 { Greeter } 
from
 "./gen/hello_pb"
;

const
 client
 =
 createClient
(

 Greeter,

 createGrpcWebTransport
({

 baseUrl: 
"https://grpc.example.com"
,

 fetch
: (
input
, 
init
) 
=>

 fetch
(input, { 
...
init, redirect: 
"manual"
 }),

 }),

);

export
 default
 {

 async
 fetch
()
:
 Promise
<
Response
> {

 const
 reply
 =
 await
 client.
sayHello
({ name: 
"Workers"
 });

 return
 Response.
json
(reply);

 },

} 
satisfies
 ExportedHandler
;

Your code uses gRPC-web, but when it speaks to the outside world, it is automatically translated into gRPC. This means that clients and servers that you already depend on don’t need to change. For example, you can:

* Provide gRPC backends to mobile apps that speak gRPC— Many mobile apps already use gRPC to reduce network payloads, serialize data more efficiently, and generate strongly-typed client libraries. You can now build the backend server for mobile apps on Workers, while still using established gRPC native libraries likegrpc-swift-2andgrpc-kotlin.
* Put a Worker in front of an existing gRPC backend— So many developers already put Workers in front of existing REST APIs to move performance critical work closer to the user, or to incrementally move state intoDurable Objects. Now you can do this with existing gRPC backends as well, or build new APIs and services that fetch data from your existing gRPC backend.

## What’s next for Socket Workers and gRPC on Cloudflare

We’re introducing everything from this post in private beta — you can sign uphere.

At Cloudflare, we useCap’n ProtoandCap’n Weband theJavaScript-native RPC system that is built into Cloudflare Workersinstead of gRPC. And when we ship things, we always aim to be using them ourselves. So in this case, we want to first work closely with a smaller set of developers using gRPC, and make sure we’ve nailed it before turning this on for everyone.

More broadly, we’re excited to continue to push the bounds of what types of traffic the Workers platform can serve, going beyond TCP and into UDP-based protocols. Keeptelling us what you want to buildon Workers, and we’ll keep pushing the bounds of what is possible.

## Related tags

Agents Week
Cloudflare Workers
Containers
Developers
gRPC
Product News

Follow on Social Media

* Cloudflare

## Subscribe to receive notifications of new posts

Email address

We’ll never share your email address.

Subscribe

Thanks for subscribing! Check your inbox to confirm.