---
title: can an email go 500 miles in 2025?
url: https://flak.tedunangst.com/post/can-an-email-go-500-miles-in-2025
site_name: hackernews
fetched_at: '2025-07-09T16:07:09.799872'
original_url: https://flak.tedunangst.com/post/can-an-email-go-500-miles-in-2025
author: zdw
date: '2025-07-09'
---

## can an email go 500 miles in 2025?

Once upon a time, there was a university president who couldn’t send an email more than 500 miles, and the wise sysadmin said that’s not possible, so the president said come to my office, and lo and behold, the emails stopped before going 500 miles. Has technology improved? Can we send an email farther than 500 miles in 2025?There’s a lot to the story that’s obviously made up, but if we fix the details so that it can happen, we can reproduce it.### connectWe need some code to do a nonblocking connect that will timeout quickly. This is mostly copied from the examples ingetaddrinfofor lookups and connect, andconnectfor the nonblocking check, adapted slightly to have a very short timeout and report errors.Thepolltimeout is 3ms, as specified by the lore. I think this is nonsense, why would an invalid or incomplete sendmail configuration default tothreemilliseconds? But that’s the time you get backing a lightspeed delay out of 500 miles. We’ll see if it matters.code#include <sys/types.h>#include <sys/socket.h>#include <sys/select.h>#include <poll.h>#include <netdb.h>#include <err.h>#include <unistd.h>#include <string.h>#include <errno.h>#include <stdio.h>intconnect_wait(ints){structpollfd pfd[1];interror=0;
 socklen_t len=sizeof(error);

 pfd[0].fd=s;
 pfd[0].events=POLLOUT;

 error=poll(pfd,1,3);if(error==-1)return-1;if(error==0){errno=ETIMEDOUT;return-1;}if(getsockopt(s,SOL_SOCKET,SO_ERROR,&error,&len)==-1)return-1;if(error!=0){errno=error;return-1;}return0;}intmain(intargc,char**argv){structaddrinfo hints,*res,*res0;interror;intsave_errno;ints;

 memset(&hints,0,sizeof(hints));
 hints.ai_family=AF_UNSPEC;
 hints.ai_socktype=SOCK_STREAM;
 error=getaddrinfo(argv[1]?:"www.openbsd.org","www",&hints,&res0);if(error)errx(1,"%s",gai_strerror(error));
 s=-1;for(res=res0; res; res=res->ai_next){s=socket(res->ai_family,res->ai_socktype | SOCK_NONBLOCK,res->ai_protocol);if(s==-1)continue;

 error=connect(s,res->ai_addr,res->ai_addrlen);if(error==-1&& errno==EINPROGRESS)error=connect_wait(s);if(error==-1){warn("connect failure");
 close(s);
 s=-1;continue;}break;/* okay we got one */}if(s==-1)return-1;
 printf("it's a live one!\n");
 freeaddrinfo(res0);}The secret here is the kernel will always round 3ms up to at least one whole tick, 10ms. And maybe we get a bit extra from the current tick. So the actual timeout will be 10ms to 19ms. Enough time to make a quick roundtrip even at halfc.pollorselectwith a zero timeout returns immediately, so not much chance of finishing the connection before that happens.We’re not going to try sending an email with sendmail because I don’t want to wait three days while the message sits in the retry queue before failing. I hope they had some sandwiches delivered to the president’s office while the demonstration was in progress.### successLet’s try connecting to a few schools, working our way across the country.ix$ ./connect upenn.edu
it's a live one!
ix$ ./connect uchicago.edu
it's a live one!
ix$ ./connect ucla.edu
it's a live one!Now I’m getting suspicious, we appear to be bending spacetime.ix$ ping ucla.edu
ping: Warning: ucla.edu has multiple addresses; using 3.33.167.235
PING ucla.edu (3.33.167.235): 56 data bytes
64 bytes from 3.33.167.235: icmp_seq=0 ttl=245 time=1.162 ms
64 bytes from 3.33.167.235: icmp_seq=1 ttl=245 time=1.189 msOkay, so we have a problem where indeed the schools are not located in spacetime the way we were expecting. Everybody is using cloud whatsit for hosting, and they may well be hosted in the same data center. We haven’t gone 500 miles. For all I know, we haven’t gone 500 feet.At this point I realized I’m also pinging web servers, not email servers, which we’ll get back to. There’s no reason the story can’t be about a failure to load a web page farther than 500 miles. But the story is funnier if it’s an email, haha, he thought it was strapped to a pigeon leg and the bird got tired.### redoIn search of success (failure), I switch to running the experiment backwards, looking for schools with ping times that are more realistic. After a while, I found a few.ix$ ping rutgers.edu
PING rutgers.edu (128.6.46.111): 56 data bytes
64 bytes from 128.6.46.111: icmp_seq=0 ttl=241 time=8.896 ms
64 bytes from 128.6.46.111: icmp_seq=1 ttl=241 time=5.768 ms
ix$ ./connect rutgers.edu
it's a live one!Rutgers is pretty close, and indeed I can connect. Stretching out a bit farther, we start having some trouble.ix$ ping cmu.edu
PING cmu.edu (128.2.42.10): 56 data bytes
64 bytes from 128.2.42.10: icmp_seq=0 ttl=242 time=13.764 ms
64 bytes from 128.2.42.10: icmp_seq=1 ttl=242 time=13.721 ms
ix$ ./connect cmu.edu
it's a live one!
ix$ ./connect cmu.edu
connect: connect failure: Operation timed out
ix$ ping www.maine.edu
PING lv-o-wpc-prod.its.maine.edu (130.111.28.163): 56 data bytes
64 bytes from 130.111.28.163: icmp_seq=0 ttl=51 time=15.255 ms
64 bytes from 130.111.28.163: icmp_seq=1 ttl=51 time=15.310 ms
ix$ ./connect maine.edu
it's a live one!
ix$ ./connect maine.edu
connect: connect failure: Operation timed outMaine is about 500 miles from here, so it seems we’re right on the edge again.Dayton is 500 miles in the other direction, but the tubes are just a bit fuller.ix$ ping udayton.edu
PING udayton.edu (131.238.73.184): 56 data bytes
64 bytes from 131.238.73.184: icmp_seq=0 ttl=235 time=25.429 ms
64 bytes from 131.238.73.184: icmp_seq=1 ttl=235 time=25.437 ms
ix$ ./connect udayton.edu
connect: connect failure: Operation timed out
ix$ ./connect udayton.edu
connect: connect failure: Operation timed outThat’ll never work. As we might have predicted, the speed of light is not significantly different in 2025.### mxAnd now to make it biblically accurate, let’s consider some MX servers. This would require switching the lookup code tores_query, or we can just use some existing tools to make observations.First, get some records for schools.host -t mx upenn.edu
upenn.edu mail is handled by 10 mxa-00390e01.gslb.pphosted.com.
host -t mx stanford.edu
stanford.edu mail is handled by 10 mxa-00000d07.gslb.pphosted.com.Okay, so not really much different than www servers. There’s a ton of outsourcing. The ping times are interested however.ix$ ping mxa-00390e01.gslb.pphosted.com
PING mxa-00390e01.gslb.pphosted.com (148.163.133.158): 56 data bytes
64 bytes from 148.163.133.158: icmp_seq=0 ttl=242 time=62.538 ms
64 bytes from 148.163.133.158: icmp_seq=1 ttl=242 time=62.443 ms
ix$ ping mxa-00000d07.gslb.pphosted.com
PING mxa-00000d07.gslb.pphosted.com (67.231.157.125): 56 data bytes
64 bytes from 67.231.157.125: icmp_seq=0 ttl=246 time=23.796 ms
64 bytes from 67.231.157.125: icmp_seq=1 ttl=246 time=23.564 msI can walk across town and hand deliver a postcard to Penn, but I can’t send them an email. Stanford, across the country, is almost but not quite within email range.ix$ host -t mx ucla.edu
ucla.edu mail is handled by 1 smtp.google.com.
ix$ ping smtp.google.com
ping: Warning: smtp.google.com has multiple addresses; using 142.251.167.27
PING smtp.google.com (142.251.167.27): 56 data bytes
64 bytes from 142.251.167.27: icmp_seq=0 ttl=109 time=6.533 ms
64 bytes from 142.251.167.27: icmp_seq=1 ttl=109 time=6.556 msHa, there we go. I can send an email 3000 miles to UCLA without fear of timeout.### conclusionThe 500 mile limit for perfectly misconfigured servers is still in place, but good luck trying to determine which domains are accessible using a roadmap.

Posted 04 Jul 2025 15:49 by tedu Updated: 04 Jul 2025 15:49

Tagged:
software

web
