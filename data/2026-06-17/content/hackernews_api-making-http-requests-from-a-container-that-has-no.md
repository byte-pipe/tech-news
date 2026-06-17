---
title: Making HTTP requests from a container that has no curl, using bash /dev/tcp · Marek Šuppa
url: https://mareksuppa.com/til/bash-dev-tcp-http-without-curl/
site_name: hackernews_api
content_file: hackernews_api-making-http-requests-from-a-container-that-has-no
fetched_at: '2026-06-17T12:27:16.538613'
original_url: https://mareksuppa.com/til/bash-dev-tcp-http-without-curl/
author: Marek Šuppa
date: '2026-06-16'
published_date: '2026-06-16T00:00:00Z'
description: Minimal container images often ship without curl, wget, or any HTTP client at all. Bash can open a TCP socket through /dev/tcp, which is enough to write a tiny HTTP/1.1 request by hand for quick checks.
tags:
- hackernews
- trending
---

I needed to check that one container could reach another over an internal Docker network: a plainGET /healthagainst a service on a shared network. The obvious move iscurl http://service:8642/health. But this app image was stripped right down, with nocurlorwgetand nothing else around that I could use to open a socket.

As it turns out,bashcan speak HTTP by itselfbashcan open a TCP socket, and you can write a small HTTP request to it by hand. Opening a connection to a host and port and writing the request needs nothing beyond the shell that’s already there:

bash
Copy
exec
 3<>/dev/tcp/service/8642

printf
 
'GET /health HTTP/1.1\r\nHost: service\r\nConnection: close\r\n\r\n'
 >
&
3

cat <
&
3

servicehere is just the hostname of whatever you’re talking to. It has to resolve and be reachable from wherever you run this, so it needs to be set up first: a container or service name on a Docker network you’ve configured, or any DNS name that resolves. Swap in your own host and port.

That prints the whole response: the status line, the headers, the blank line, and the body. To add a header, such as anAuthorization: Bearertoken, put another\r\n-terminated line before the blank line that ends the request:

bash
Copy
exec
 3<>/dev/tcp/service/8642

printf
 
'GET /v1/models HTTP/1.1\r\nHost: service\r\nAuthorization: Bearer %s\r\nConnection: close\r\n\r\n'
 
"
$API_KEY
"
 >
&
3

cat <
&
3

What caught me out the first time is that/dev/tcpisn’t a real device file. There’s no such path on disk;ls /dev/tcpfinds nothing, andcat /dev/tcp/...from another shell just errors. It’s a redirection thatbashhandles internally. From theBash manual:

/dev/tcp/host/port– If host is a valid hostname or Internet address, and port is an integer port number or service name, bash attempts to open the corresponding TCP socket.

The names werepicked becauseno real Unix has a/dev/tcpor/dev/udphierarchy, so there’s nothing to collide with. Bash does the DNS lookup and theconnect(2)for you, andexec 3<>hands the socket a file descriptor (3) you read from and write to like any other.

A few things worth knowing:

* This is not a real HTTP client. It does not parse HTTP properly, handle redirects, chunked responses, compression, retries, TLS, or any of the other thingscurlquietly does for you. It’s a quick connectivity and debugging trick.
* TheConnection: closeheader matters. Without it the server keeps the connection open after it responds, which is the HTTP/1.1 default, andcat <&3then waits forever for bytes that never arrive. Asking the server to close meanscatreaches EOF and returns. Wrapping the call intimeout 6 bash -c '...'covers you either way.
* There’s no TLS./dev/tcpopens a raw socket, so this only works for plaintext HTTP. Forhttpsyou’d needopenssl s_client, and by then you may as well have the proper tools.
* This is abashfeature, not POSIX.dash(Debian’s/bin/sh) andzshdon’t have it, so a#!/bin/shscript can’t use it. Callbashdirectly.
* It’s a compile-time option, switched on whenbashis built with--enable-net-redirections. Most mainstream builds enable it, and it worked without any fuss in the Debian-based image I was in, but Debianshipped it disabled for years, so on an old or very minimal system it’s worth checking first.

For day-to-day workcurlis still the right tool. But inside a deliberately small container where you can’t install anything, this gets a quick check done without adding a package.