---
title: 'FastCGI: 30 Years Old and Still the Better Protocol for Reverse Proxies'
url: https://www.agwa.name/blog/post/fastcgi_is_the_better_protocol_for_reverse_proxies
site_name: hackernews_api
content_file: hackernews_api-fastcgi-30-years-old-and-still-the-better-protocol
fetched_at: '2026-04-30T12:31:14.177083'
original_url: https://www.agwa.name/blog/post/fastcgi_is_the_better_protocol_for_reverse_proxies
author: Andrew Ayer
date: '2026-04-30'
description: 'FastCGI: 30 years old and still the better protocol for reverse proxies'
tags:
- hackernews
- trending
---

HTTP reverse proxying is a minefield.
Just the other week, a researcher disclosed adesync
vulnerability in Discord's media proxythat allowed spying on private
attachments. This is not unusual; these vulnerabilities just keep coming.

The problem is the widespread use of HTTP as the protocol between reverse proxies
and backends, even though it's unfit for the job.
But we don't have to use HTTP here.
There's a 30-year-old protocol for proxy-to-backend communication
that avoids HTTP's pitfalls. It's called FastCGI,
and itsspecificationwas released 30 years ago today.

#### FastCGI is a Wire Protocol, not a Process Model

It's true that some web servers can automatically spawn FastCGI processes
to handle requests for files with the.fcgiextension, much like they
would for.cgifiles. But you don't have to use FastCGI this way - you
can also use the FastCGI protocol just like HTTP, with requests sent
over a TCP or UNIX socket to a long-running daemon that handles them as if they
were HTTP requests.

For example, in Go all you have to do is import thenet/http/fcgistandard library package and replacehttp.Servewithfcgi.Serve:

##### Go HTTP

l, _ := net.Listen("tcp", "127.0.0.1:8080")
http.Serve(l, handler)

##### Go FastCGI

l, _ := net.Listen("tcp", "127.0.0.1:8080")
fcgi.Serve(l, handler)

Everything else about your app stays the same - even your handler, which continues to use the standardhttp.ResponseWriterandhttp.Requesttypes.

Popular proxies like Apache, Caddy, nginx, and HAProxy support FastCGI backends, and the configuration is simple:

##### nginx HTTP

proxy_pass http://localhost:8080;

##### nginx FastCGI

fastcgi_pass localhost:8080;
include fastcgi_params;

Show more config examples

##### Apache HTTP

ProxyPass / http://localhost:8080/

##### Apache FastCGI

ProxyPass / fcgi://localhost:8080/

##### Caddy HTTP

reverse_proxy localhost:8080 {
	transport http {
	}
}

##### Caddy FastCGI

reverse_proxy localhost:8080 {
	transport fastcgi {
	}
}

##### HAProxy HTTP

backend app_backend
	server s1 localhost:8080

##### HAProxy FastCGI

fcgi-app fcgi_app
	docroot /

backend app_backend
	use-fcgi-app fcgi_app
	server s1 localhost:8080 proto fcgi

#### Why HTTP Sucks for Reverse Proxies: Desync Attacks / Request Smuggling

HTTP/1.1 has the tragic property of looking simple on the surface
(it's just text!) but actually being a nightmare to parse robustly.
There are so many different ways to format the same HTTP message,
and there are too many edge cases and ambiguities for implementations to handle consistently.
As a result, no two HTTP/1.1 implementations
are exactly the same, and the same message can be parsed differently by different parsers.

The most serious problem is that there is no explicit framing of HTTP
messages - the message itself describes where it ends, and there are
multiple ways for a message to do that, all with their own edge cases.
Implementations can disagree about where a message ends,
and consequently, where the next message begins. This is the foundation ofHTTP desync attacks,
also known as request smuggling, wherein a reverse proxy and a backend disagree about
the boundaries between HTTP messages, causing all sorts of nightmare
security issues, such as the Discord vulnerability I linked above.

A lot of people seem to think you can just patch the parser divergences,
but this is a losing strategy.James Kettlejust keeps finding new ones. Afterfinding another batch last year,
he declared"HTTP/1.1 must die".

HTTP/2,when consistently used between the proxy and backend, fixes desync by putting clear boundaries around messages, but FastCGI
has been doing that since 1996 with a simpler protocol.
For context, nginx has supported FastCGI backends since its first release,
but only got support for HTTP/2 backends in late 2025. Apache's support for HTTP/2 backends is still"experimental".

#### Why HTTP Sucks for Reverse Proxies: Untrusted Headers

If desync attacks were the only problem, you could just use HTTP/2 and call it
a day. Unfortunately, there's another problem: HTTP has no robust way
for the proxy to convey trusted information about the request, such as the real client IP address,
authenticated username (if the proxy handles authentication), or client certificate details
(if mTLS is used).

The only option is to stick this information in HTTP headers, alongside
the headers proxied from the client, without a clear structural distinction between trusted
headers from the proxy and untrusted headers from a potential attacker.
For example, theX-Real-IPheader is often used
to convey the client's real IP address. In theory, if your proxy correctly deletes all instances
of theX-Real-IPheader (not just the first, and including case variations likex-REaL-ip) before adding its own, you're safe.

In practice,this is a minefieldand there are an awful lot of ways your backend can end up trusting attacker-controlled data.
Your proxy really needs to delete not justX-Real-IP, butanyheader that's used for this sort of thing,
just in case some part of your stack relies on it without your knowledge.
For example, the Chi middlewaredetermines the client's real IP addressby looking at theTrue-Client-IPheader first. Only ifTrue-Client-IPdoesn't exist does it useX-Real-IP.
So even if your proxy does the right thing withX-Real-IP, you can still be pwned by an attacker
sending aTrue-Client-IPheader.

FastCGI completely avoids this class of problem by providing domain separation between headers from the client
and information added by the proxy. Though trusted data from the proxy and HTTP request headers are
transmitted to the backend in the same key/value parameter list, HTTP header names are prefixed with the string
"HTTP_", making it structurally impossible for clients to send a header that would be interpreted as trusted
data.

FastCGI defines some standard parameters such asREMOTE_ADDRto convey the real client IP address.
Go'snet/http/fcgipackage automatically uses this parameter to populate theRemoteAddrfield ofhttp.Request,
rendering middleware unnecessary. It Just Works. Proxies can also use non-standard parameters to report whether HTTPS was used,
what TLS ciphersuite was negotiated, and what client certificate was presented, if any.
Go automatically sets theRequest'sTLSfield to a non-nil (but empty) value if the request used HTTPS,
which is very handy for enforcing the use of HTTPS. Thefcgi.ProcessEnvfunction can be used to access the full set of
trusted parameters sent by the proxy.

#### Closing Thoughts

If FastCGI is the better protocol, why isn't it more popular? Maybe it's the name - while capitalizing
on CGI's popularity made sense in 1996, CGI feels dated in 2026. There's also an enduring lack of
awareness of the security problems with HTTP reverse proxying.Watchfire described desync attacksin 2005, and gave a prescient warning of their intractability,
but the attacks were inexplicably ignored for over a decade. In an alternate timeline, Watchfire's research was taken
seriously and people went looking for other protocols for reverse proxies.

FastCGI is very usable today, and has been in production use atSSLMatefor over 10
years. That said, using a vintage technology has some downsides.
It was never updated to support WebSockets. The tooling is not as good.
For example, curl has no way to make requests to a FastCGI server. It
supports FTP, Gopher, and even SMTP (however that works), but not
FastCGI. When I benchmarked Go's FastCGI server behind a variety
of reverse proxies, some workloads had worse throughput compared to HTTP/1.1 or HTTP/2.
I don't think that's inherent to the protocol, but a reflection that FastCGI code paths have not been
optimized as much as HTTP.

Despite these shortcomings, I still think FastCGI is worth using. I don't
use WebSockets, and it's fast enough for my use case (and maybe yours
too). If it ever became the bottleneck, I'd rather buy more hardware
than deal with the nightmare of HTTP reverse proxying.

Happy 30th birthday, FastCGI!