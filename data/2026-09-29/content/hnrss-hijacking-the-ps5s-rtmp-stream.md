---
title: Hijacking the PS5's RTMP Stream
url: https://yashgarg.dev/posts/hijacking-ps5-rtmp-stream/
site_name: hnrss
content_file: hnrss-hijacking-the-ps5s-rtmp-stream
fetched_at: '2026-09-29T07:30:37.075729'
original_url: https://yashgarg.dev/posts/hijacking-ps5-rtmp-stream/
date: '2026-09-28'
description: The long way around to screen sharing.
tags:
- hackernews
- hnrss
---

Back to posts
 
 
Hijacking the PS5's RTMP Stream
 
 
 
 
Yash Garg
 
 

# Hijacking the PS5's RTMP Stream

 

The long way around to screen sharing.

 
 
 September 28, 2026 
 
·
 
5 min read
 
 
 
gaming
networking
 
 
 
 
 
 
 
 
 
 
 
 
 
Contents
 
* 1.The Problem
* 2.Remote Play
* 3.How PS5 Streaming Works
* 4.Finding the Right Hostname
* 5.DNS Trick
* 6.Receiving the Stream
* 7.Watching It
 
 

Sony has progressively locked down what you can do with the PS5’s hardware. Streaming is a good example: the console gives you a nice, convenient“Broadcast”button, but the moment you want to do anything outside the handful of services Sony supports, it gets annoying very fast.

Third-party Bluetooth devices are the same story! Sony locks the wireless stack to their own peripherals, so your headphones or controllers from other brands simply won’t pair :/

## #The Problem

I often stream games with friends onDiscordwho watch me play, but the PS5 doesn’t support screen sharing to Discord. The obvious fix is a capture card — plug the HDMI output into acapture card, feed it intoOBSon your Mac, stream from there. But decent ones aren’t cheap, and I didn’t want to spend upwards of $100 just for this.

## #Remote Play

Remote Playsomewhat worked for me. I could connect the PS5 to my MacBook, share the Mac’s screen to Discord and play from there.

The problem is that you need to connect everything to the Remote Play device: controller, earphones, etc. I also occasionally ran into input lag, and the stream quality is entirely controlled by the PS5. You can’t really configure anything.

I didn’t want to change my physical setup every time I wanted to stream.

## #How PS5 Streaming Works

The PS5 supports streaming toYouTubeandTwitchby default if you’re signed into those accounts. The protocol used for this isRTMP, or Real-Time Messaging Protocol, which is commonly used for live audio/video streaming.

So when you start a broadcast, the PS5 roughly does this:

 
 
 

What if we could make our own device act as Twitch and receive that RTMP stream instead?

 
 
 

That’s the idea. The PS5 doesn’t hardcode Twitch’s IP, it looks it up via DNS every time. If we control what DNS returns, we control where the stream goes.

## #Finding the Right Hostname

The obvious first attempt was to spoofingest.twitch.tvdirectly. That’s the hostname the PS5 resolves when you hit broadcast, so pointing it at the Mac should work, right?

Not quite.ingest.twitch.tv:443is actually adiscovery endpoint, not the RTMP server itself. PS5 makes an HTTPS call to it asking “which regional ingest server should I use?” and Twitch responds with something likeap-southeast-1.prod.fi.contribute.live-video.net. Then the PS5 pushes the actual stream there.

Spoofing that hostname ran into a different problem: the actual Twitch ingest usesRTMPS(RTMP over TLS on port 443), and PS5 validates the certificate against trustedCAs. A self-signed cert doesn’t work, and there’s no way to install custom CAs on a PS5.

I then tried YouTube as a workaround. Its RTMP ingest uses plain RTMP on port 1935, so there was no TLS certificate to deal with. The PS5 happily sent the stream to my Mac, so I knew the basic approach worked.

The problem was that PS5 periodically checks YouTube’s API to make sure the stream is actually live. Since YouTube never received the stream, that check failed and it stopped broadcasting after about 60 seconds.

That meant I needed to find a Twitch endpoint that used plain RTMP. The answer came from watching DNS logs while broadcasting:

sudo
 tail
 -f
 /tmp/dnsmasq.log

# Sep 22 23:20:28 dnsmasq: query[A] ingest.global-contribute.live-video.net from 192.168.8.171

# Sep 22 23:20:28 dnsmasq: reply aps30.contribute.live-video.net is 35.55.13.0

The PS5 was resolvingingest.global-contribute.live-video.net, which chains down toaps30.contribute.live-video.net. That’s the real RTMP server. Spoofingcontribute.live-video.netcovers all subdomains and redirects the actual stream to the Mac without any certificate issues.

## #DNS Trick

The setup has two main parts:dnsmasqandnginx-rtmp. I built a small macOS menu bar app that bundles both and manages them.

I rundnsmasqon my Mac and configure it to resolve Twitch’s ingest domains to my Mac’s LAN address:

server
=
1.1.1.1

server
=
8.8.8.8

# Redirect Twitch ingest traffic to the Mac

address
=
/contribute.live-video.net/192.168.8.175

address
=
/ingest.global-contribute.live-video.net/192.168.8.175

address
=
/live.twitch.tv/192.168.8.175

address
=
/live-sin.twitch.tv/192.168.8.175

address
=
/live-nrt.twitch.tv/192.168.8.175

address
=
/live-syd.twitch.tv/192.168.8.175

address
=
/live-fra.twitch.tv/192.168.8.175

address
=
/live-ams.twitch.tv/192.168.8.175

address
=
/live-lhr.twitch.tv/192.168.8.175

address
=
/live-jfk.twitch.tv/192.168.8.175

address
=
/live-lax.twitch.tv/192.168.8.175

address
=
/live-sea.twitch.tv/192.168.8.175

log-queries

log-facility
=
/tmp/dnsmasq.log

no-hosts

listen-address
=
0.0.0.0

192.168.8.175is my Mac’s IP. When the PS5 asks DNS for one of these Twitch endpoints,dnsmasqreturns my Mac’s IP instead. The PS5 connects to my Mac thinking it’s Twitch.

The last piece is pointing the PS5 at this DNS server. I have aGL.iNet routerrunningOpenWRT, so I configured it to hand my Mac’s IP as the DNS server specifically for the PS5’sDHCPlease.

# SSH into the router and run:

uci
 add_list
 dhcp.lan.dhcp_option=
"
tag:PS5,6,192.168.8.175
"

uci
 commit
 dhcp

/etc/init.d/dnsmasq
 restart

Thetag:PS5part works because the PS5’s static lease already has that tag set in/etc/config/dhcp. Option6is the DHCP option for DNS server. The PS5 picks this up on its next DHCP renewal, no manual DNS configuration is required on the console!

## #Receiving the Stream

For that, I’m usingnginx-rtmp:

worker_processes
 1
;

error_log
 /tmp/nginx-error.log
 warn
;

pid
 /tmp/nginx.pid
;

events
 {

 worker_connections
 512
;

}

rtmp
 {

 server
 {

 listen
 1935
;

 chunk_size
 4096
;

 application
 ps5
 {

 live
 on
;

 record
 off
;

 sync
 10ms
;

 # Notify our app when a stream starts

 on_publish
 http://127.0.0.1:9988/on_publish
;

 }

 }

}

http
 {

 server
 {

 listen
 8080
;

 location
 /stat
 {

 rtmp_stat
 all
;

 }

 }

}

Theon_publishcallback is how the menu bar app detects when the PS5 starts broadcasting. nginx fires a POST tolocalhost:9988with the stream name, and the app surfaces the full RTMP URL ready to copy.

At this point, the PS5 is pushing its stream (1080p60, H.264, AAC stereo) directly to my Mac instead of Twitch.

 
 
 

From here I can pull the stream into anything: OBS to re-stream it, record it locally, or just play it directly.

## #Watching It

Instead of going through OBS, I usedmpvto pull the stream and shared the window to Discord. The low-latency profile keeps the delay less than a second:

mpv
 --profile=low-latency
 --audio-buffer=0.3
 rtmp://127.0.0.1/ps5/stream-key

This has been quite reliable surprisingly. I’ve been using it for a few weeks now and haven’t had any issues. You can find the complete source codehere.

Until next time! 👋

 
 
 
 
 
 
 
-
 
 
Mentioned this post? Send a webmention:
Send