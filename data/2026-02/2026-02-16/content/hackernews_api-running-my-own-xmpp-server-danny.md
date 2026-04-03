---
title: Running My Own XMPP Server » Danny
url: https://blog.dmcc.io/journal/xmpp-turn-stun-coturn-prosody/
site_name: hackernews_api
content_file: hackernews_api-running-my-own-xmpp-server-danny
fetched_at: '2026-02-16T19:17:44.412863'
original_url: https://blog.dmcc.io/journal/xmpp-turn-stun-coturn-prosody/
author: Danny
date: '2026-02-16'
published_date: '2026-02-16T00:00:10Z'
description: Notes from setting up Prosody in Docker for federated messaging, with file sharing, voice calls, and end-to-end encryption.
tags:
- hackernews
- trending
---

Notes from setting up Prosody in Docker for federated messaging, with file sharing, voice calls, and end-to-end encryption.

About a year ago Imoved my personal messaging to Signalas part of a broader push to take ownership of my digital life. That went well. Most of my contacts made the switch, and I’m now at roughly 95% Signal for day-to-day conversations. But Signal is still one company running one service. If they shut down tomorrow or change direction, I’m back to square one.

XMPP fixes that. It’s federated, meaning your server talks to other XMPP servers automatically and you’re never locked into a single provider. Your messages live on your hardware. The protocol has been around since 1999 and it’s not going anywhere. I’d tried XMPP years ago and bounced off it, but the clients have come a long way since then.MonalandConversationsare genuinely nice to use now.

This post covers everything I did to get a fully working XMPP server running withProsodyin Docker, from DNS records through to voice calls.

## Prerequisites

* A server with Docker and Docker Compose
* A domain you control
* TLS certificates (Let’s Encrypt works well)

## DNS records

XMPP uses SRV records to let clients and other servers find yours. You’ll need these in your DNS:

_xmpp-client._tcp.xmpp.example.com SRV 0 5 5222 xmpp.example.com.
_xmpp-server._tcp.xmpp.example.com SRV 0 5 5269 xmpp.example.com.

Port 5222 is for client connections, 5269 is for server-to-server federation. You’ll also want an A record pointingxmpp.example.comto your server’s IP.

If you want HTTP file uploads (I’d recommend it), add a CNAME or A record forupload.xmpp.example.compointing to the same server. Same forconference.xmpp.example.comif you want group chats with a clean subdomain, though Prosody handles this internally either way.

## TLS certificates

Prosody won’t start without certificates. I use Let’s Encrypt with the Cloudflare DNS challenge so I don’t need to expose port 80:

docker run --rm
\

 -v ~/docker/xmpp/certs:/etc/letsencrypt
\

 -v ~/docker/xmpp/cloudflare.ini:/etc/cloudflare.ini:ro
\

 certbot/dns-cloudflare certonly
\

 --dns-cloudflare
\

 --dns-cloudflare-credentials /etc/cloudflare.ini
\

 -d xmpp.example.com

Thecloudflare.inifile contains your API token:

dns_cloudflare_api_token

=

your-cloudflare-api-token

After certbot runs, fix the permissions so Prosody can read the certs:

chmod -R
755
 ~/docker/xmpp/certs/live/ ~/docker/xmpp/certs/archive/
chmod
644
 ~/docker/xmpp/certs/archive/xmpp.example.com/*.pem

Set up a cron to renew monthly:

0

3

1
 * * docker run --rm -v ~/docker/xmpp/certs:/etc/letsencrypt
\

 -v ~/docker/xmpp/cloudflare.ini:/etc/cloudflare.ini:ro
\

 certbot/dns-cloudflare renew
\

 --dns-cloudflare-credentials /etc/cloudflare.ini
\


&&
 docker restart xmpp

## The Docker setup

Thedocker-compose.yml:

services
:


prosody
:


image
:

prosodyim/prosody:
13.0


container_name
:

xmpp


restart
:

unless-stopped


ports
:


-
"5222:5222"


-
"5269:5269"


volumes
:


- prosody-data:/var/lib/prosody


- ./prosody.cfg.lua:/etc/prosody/prosody.cfg.lua:ro


- ./certs/live/xmpp.example.com/fullchain.pem:/etc/prosody/certs/xmpp.example.com.crt:ro


- ./certs/live/xmpp.example.com/privkey.pem:/etc/prosody/certs/xmpp.example.com.key:ro

volumes
:


prosody-data
:

Two ports exposed: 5222 for clients, 5269 for federation. The data volume holds user accounts and message archives. Config and certs are mounted read-only.

## Prosody configuration

This is the core of it. I’ll walk through the key sections rather than dumping the whole file.

### Modules

Prosody is modular. My module list:

modules_enabled
=
 {

-- Core


"roster"
;
"saslauth"
;
"tls"
;
"dialback"
;
"disco"
;

"posix"
;
"ping"
;
"register"
;
"time"
;
"uptime"
;
"version"
;


-- Security


"blocklist"
;


-- Multi-device & mobile


"carbons"
;
"csi_simple"
;

"smacks"
;
-- Stream Management (reliable delivery)


"cloud_notify"
;
-- Push notifications for mobile


-- Message archive


"mam"
;


-- User profiles & presence


"vcard_legacy"
;
"pep"
;
"bookmarks"
;


-- Admin


"admin_shell"
;
}

The ones I found matter most for a good mobile experience:carbonssyncs messages across all your devices instead of delivering to whichever one happened to be online.smacks(Stream Management) handles flaky connections gracefully, so messages aren’t lost when your phone briefly drops signal.cloud_notifyenables push notifications so mobile clients don’t need a persistent connection, which is essential for battery life. Andmam(Message Archive Management) stores history server-side for search and cross-device sync.

### Security settings

c2s_require_encryption
=

true

s2s_require_encryption
=

true

s2s_secure_auth
=

true

authentication
=

"internal_hashed"

allow_registration
=

false

All connections are encrypted and registration is disabled since I create accounts manually withprosodyctl. I’ve enableds2s_secure_auth, which means Prosody will reject connections from servers with self-signed or misconfigured certificates. You’ll lose federation with some poorly configured servers, but if you’re self-hosting for privacy reasons it doesn’t make much sense to relax authentication for other people’s mistakes.

### OMEMO encryption

TLS encrypts connections in transit, but the server itself can still read your messages. If you’re self-hosting, that means you’re trusting yourself, which is fine. But if other people use your server, or if you just want the belt-and-braces approach, OMEMO adds end-to-end encryption so that not even the server operator can read message content.

OMEMO is built on the same encryption that Signal uses, so I’m comfortable trusting it. There’s nothing to configure on the server side either. OMEMO is handled entirely by the clients. Monal, Conversations, and Gajim all support it, and in most cases it’s enabled by default for new conversations. I’d recommend turning it on for everything and leaving it on.

### Message archive

archive_expires_after
=

"1y"

default_archive_policy
=

true

Messages are kept for a year and archiving is on by default. Clients can opt out per-conversation if they want.

### HTTP for file uploads

http_interfaces
=
 {
"*"
 }
http_ports
=
 {
5280
 }
https_ports
=
 { }
http_external_url
=

"https://xmpp.example.com"

Prosody serves HTTP on port 5280 internally. I leave HTTPS to my reverse proxy (Caddy), which handles TLS termination. Thehttp_external_urltells Prosody what URL to hand clients when they upload files.

### Virtual host and components

VirtualHost
"xmpp.example.com"

 ssl
=
 {
 key
=

"/etc/prosody/certs/xmpp.example.com.key"
;
 certificate
=

"/etc/prosody/certs/xmpp.example.com.crt"
;
 }

Component
"conference.xmpp.example.com"

"muc"

 modules_enabled
=
 {
"muc_mam"
 }
 restrict_room_creation
=

"local"

Component
"upload.xmpp.example.com"

"http_file_share"

 http_file_share_size_limit
=

10485760

-- 10 MB

 http_file_share_expires_after
=

2592000

-- 30 days

 http_external_url
=

"https://xmpp.example.com"

The MUC (Multi-User Chat) component gives you group chats with message history viamuc_mam. I restrict room creation to local users so random federated accounts can’t spin up rooms on my server.

The file share component handles image and file uploads. A 10 MB limit and 30-day expiry keeps disk usage under control.

## Reverse proxy for file uploads

Prosody’s HTTP port needs to be reachable from the internet for file uploads to work. I use Caddy:

xmpp.example.com {
 reverse_proxy xmpp:5280
}

When a client sends an image, Prosody hands it a URL likehttps://xmpp.example.com/upload/...and the receiving client fetches it over HTTPS.

## Creating accounts

With registration disabled, accounts are created from the command line:

docker
exec
 -it xmpp prosodyctl adduser danny@xmpp.example.com

It prompts for a password. Done. Log in from any XMPP client.

## Firewall

Open the XMPP ports:

sudo ufw allow
5222
 comment
'XMPP client'

sudo ufw allow
5269
 comment
'XMPP federation'

Port 80/443 for the reverse proxy if you haven’t already. If your server is behind a router, forward 5222 and 5269.

## Voice and video calls

Text and file sharing work at this point. Voice and video calls need one more piece: a TURN/STUN server. Without it, clients behind NAT can’t establish direct media connections.

I runcoturnalongside Prosody. The two share a secret, and Prosody generates temporary credentials for clients automatically.

Generate a shared secret:

openssl rand -hex
32

The coturndocker-compose.yml:

services
:


coturn
:


image
:

coturn/coturn:latest


container_name
:

coturn


restart
:

unless-stopped


network_mode
:

host


volumes
:


- ./turnserver.conf:/etc/coturn/turnserver.conf:ro


tmpfs
:


- /var/lib/coturn

It runs withnetwork_mode: hostbecause TURN needs real network interfaces to handle NAT traversal. Docker’s port mapping breaks this.

Theturnserver.conf:

listening-port=3478
tls-listening-port=5349
min-port=49152
max-port=49200
relay-threads=2
realm=xmpp.example.com
use-auth-secret
static-auth-secret=YOUR_SECRET_HERE
no-multicast-peers
no-cli
no-tlsv1
no-tlsv1_1
denied-peer-ip=10.0.0.0-10.255.255.255
denied-peer-ip=172.16.0.0-172.31.255.255
denied-peer-ip=192.168.0.0-192.168.255.255
log-file=stdout

If your server is behind NAT, add:

external-ip=YOUR_PUBLIC_IP/YOUR_PRIVATE_IP

Then tell Prosody about it. Add"turn_external"to your modules, and inside theVirtualHostblock:

 turn_external_host
=

"xmpp.example.com"

 turn_external_port
=

3478

 turn_external_secret
=

"YOUR_SECRET_HERE"

Open the firewall ports:

sudo ufw allow
3478
 comment
'STUN/TURN'

sudo ufw allow
5349
 comment
'TURNS'

sudo ufw allow 49152:49200/udp comment
'TURN relay'

Verify withdocker exec xmpp prosodyctl check turn.

## Clients

On iOS I went withMonal, which is open source and supports all the modern XEPs. Push notifications work well. On Android,Conversationsseems to be the go-to. On desktop,Gajimcovers Linux and Windows, and Monal has a macOS build.

All of them support OMEMO encryption, file sharing, group chats, and voice/video calls.

## Verifying your setup

Prosody has solid built-in diagnostics:

docker
exec
 xmpp prosodyctl check

This checks DNS records, TLS certificates, connectivity, and module configuration. Fix anything it flags. The error messages are genuinely helpful.

TheXMPP Compliance Testeris worth running too. Mine scored above 90% after getting the config right.

## Final thoughts

The whole setup runs in two small Docker containers and a reverse proxy entry. Prosody, file uploads, message archive, push notifications, group chats, voice calls.

I still use Signal for most day-to-day conversations and I’m not planning to stop. But having my own XMPP server means I’m not entirely dependent on any single service. I can message anyone on any XMPP server, not just people who signed up to the same one. It’s a nice fallback to have.

If you’re already running Docker on a server somewhere, it’s a good weekend project.

### Other posts

* Making My Blog Available on Tor
* Network-Wide Ad Blocking with Tailscale and AdGuard Home
* What Your Bluetooth Devices Reveal About You
* Leaving Spotify for Self-Hosted Audio
* ZeroNet: The Web Without Servers
