---
title: 'Bug Report: macOS 26 breaks /etc/resolver/ supplemental DNS for custom TLDs · GitHub'
url: https://gist.github.com/adamamyl/81b78eced40feae50eae7c4f3bec1f5a
site_name: hnrss
content_file: hnrss-bug-report-macos-26-breaks-etcresolver-supplementa
fetched_at: '2026-03-19T19:23:40.437005'
original_url: https://gist.github.com/adamamyl/81b78eced40feae50eae7c4f3bec1f5a
date: '2026-03-19'
description: 'Bug Report: macOS 26 breaks /etc/resolver/ supplemental DNS for custom TLDs - macos26-breaks-custom-dns.md'
tags:
- hackernews
- hnrss
---

Instantly share code, notes, and snippets.

# adamamyl/macos26-breaks-custom-dns.md

 Last active

March 19, 2026 18:53



Show Gist options



* Download ZIP





* Star10(10)You must be signed in to star a gist
* Fork0(0)You must be signed in to fork a gist

* Embed# Select an optionEmbedEmbed this gist in your website.ShareCopy sharable link for this gist.Clone via HTTPSClone using the web URL.## No results foundLearn more about clone URLsClone this repository at &lt;script src=&quot;https://gist.github.com/adamamyl/81b78eced40feae50eae7c4f3bec1f5a.js&quot;&gt;&lt;/script&gt;
* EmbedEmbed this gist in your website.
* ShareCopy sharable link for this gist.
* Clone via HTTPSClone using the web URL.
* Save adamamyl/81b78eced40feae50eae7c4f3bec1f5a to your computer and use it in GitHub Desktop.



Embed

# Select an option



* EmbedEmbed this gist in your website.
* ShareCopy sharable link for this gist.
* Clone via HTTPSClone using the web URL.

## No results found





Learn more about clone URLs





 Clone this repository at &lt;script src=&quot;https://gist.github.com/adamamyl/81b78eced40feae50eae7c4f3bec1f5a.js&quot;&gt;&lt;/script&gt;





Save adamamyl/81b78eced40feae50eae7c4f3bec1f5a to your computer and use it in GitHub Desktop.

Download ZIP

 Bug Report: macOS 26 breaks /etc/resolver/ supplemental DNS for custom TLDs




Raw

 macos26-breaks-custom-dns.md


Ah, the joys of waking up to find the Mac's done an overnight upgrade… and erm, suddenly things stop working. Thankfully, me and Claude managed to work out what the fuck is going on… I'm sharing here, as well as having raised in onhttps://feedbackassistant.apple.com/feedback/22280434(that seems to need a login?).

# Bug Report: macOS 26 breaks /etc/resolver/ supplemental DNS for custom TLDs

Product:macOS 26.3.1 (Darwin 25.3.0, Build 25D771280a)Component:Networking → DNS / mDNSResponderRegression from:macOS25.x26.3.0 (working immediately prior to overnight update)

## Summary

The/etc/resolver/per-domain DNS resolver mechanism — an Apple-documented, long-standing macOS feature — is silently broken in macOS 26 for any TLD that is not present in the IANA root zone.mDNSResponderintercepts queries for custom/private TLDs and handles them as mDNS (multicast DNS), never consulting the unicast nameserver specified in the resolver file. This breaks an entire class of local development and private network DNS workflows that previously worked correctly on macOS 25 and earlier.

## Background

macOS supports per-domain DNS resolver configuration via files placed in/etc/resolver/. A file named/etc/resolver/internalcontainingnameserver 127.0.0.1instructs the DNS stack to send all*.internalqueries to the local nameserver at 127.0.0.1. This mechanism is documented inman 5 resolverand has worked reliably since at least macOS 10.6. It is widely used by developers running local DNS servers (dnsmasq, bind, unbound) to resolve private domain suffixes.

This machine runsdnsmasq(via Homebrew) as a local DNS resolver, configured to answer queries for*.internaldomains (static entries for a local web application) and forward everything else upstream. The/etc/resolver/internalfile routes these queries to dnsmasq. This setup worked correctly on macOS 25.x.

## Steps to Reproduce

1. Install dnsmasq and configure it to answer a custom domain:# /opt/homebrew/etc/dnsmasq.d/test.conf
address=/probe.example-private/127.0.0.1
2. Start dnsmasq:brew services start dnsmasq
3. Verify dnsmasq answers directly:dig @127.0.0.1 probe.example-private A +short
# Returns: 127.0.0.1 ✓
4. Create a resolver file:sudo sh -c 'echo "nameserver 127.0.0.1" > /etc/resolver/example-private'
5. Flush DNS cache and restart mDNSResponder:sudo dscacheutil -flushcache && sudo killall -HUP mDNSResponder
6. Verifyscutil --dnsshows the resolver is registered:scutil --dns | grep -A4 "example-private"
# Shows: domain: example-private, nameserver: 127.0.0.1 ✓
7. Attempt to resolve via the system resolver:ping -c1 probe.example-private
# ping: cannot resolve probe.example-private: Unknown host ✗

python3 -c "import socket; print(socket.getaddrinfo('probe.example-private', 80))"
# socket.gaierror: [Errno 8] nodename nor servname provided, or not known ✗

## Expected Behaviour

ping,curl, and any application usinggetaddrinfo()should resolveprobe.example-privateto127.0.0.1, as specified by the dnsmasqaddress=directive, reached via the/etc/resolver/example-privateunicast nameserver entry. This is exactly what happened on macOS 25.x.

## Actual Behaviour

All resolution viagetaddrinfo()(i.e. every real application — browsers, curl, ping) fails with "Unknown host". No DNS traffic reaches dnsmasq. Instead,mDNSResponderintercepts the query and immediately returns a cached "No Such Record" mDNS response with an anomalously large TTL (~108002 seconds).

Evidence fromdns-sd -G v4 probe.example-private:

Timestamp A/R Flags IF Hostname Address TTL
11:42:03.617 Add 40000002 0 probe.example-private. 0.0.0.0 108002 No Such Record

Evidence fromtcpdump -i lo0 -n port 53captured during agetaddrinfo()call:

0 packets captured

No packets reach dnsmasq on 127.0.0.1:53 at all. mDNSResponder handles the query entirely internally via mDNS and never consults the unicast nameserver.

## Scope

Tested TLDs that fail:

TLD

Status

Notes

.internal

Broken

IETF draft special-use TLD; worked on macOS 25

.test

Broken

RFC 6761 §6.2 — explicitly reserved for local testing

.home.arpa

Broken

RFC 8375 — IANA reserved for residential private networks

.lan

Broken

Widely used convention (not IANA reserved, but irrelevant)

Arbitrary (e.g.
.emflocal
)

Broken

Any TLD not in the IANA root zone

.testis particularly egregious: RFC 6761 Section 6.2 explicitly reserves.testfor exactly this use case — local/private DNS testing — and specifies that resolvers SHOULD resolve it via normal DNS mechanisms. macOS 26 silently overrides this by treating it as mDNS-only.

google.com,bbc.co.ukand other standard IANA-registered TLDs continue to work correctly via the default unicast resolver. Only custom/unregistered/special-use TLDs are affected.

## Workaround

The only reliable workaround is to add entries manually to/etc/hosts, which bypasses mDNSResponder entirely. This is impractical for dynamic use cases (e.g. Docker container DNS, where host entries change frequently) and requires sudo for every change.

## Impact

This breaks the standard local development DNS workflow that has been documented and recommended by the macOS developer community for over a decade:

* Any developer using dnsmasq +/etc/resolver/for*.test,*.local,*.internal, or other private TLDs
* Docker Desktop's (and similar tools') container name resolution via custom TLDs
* Any tool that generates/etc/resolver/entries as part of its macOS integration (e.g. Vagrant, Tailscale, various VPN clients)
* Kubernetes local development tools (minikube, kind, k3d) that use*.cluster.localor similar

The failure is silent:scutil --dnscorrectly shows the resolver configuration is registered, leading users to believe the setup is correct while resolution silently fails. There is no log output, no error, and no indication that mDNS interception is occurring.

## Environment

* macOS version:26.3.1 (ProductVersionExtra: (a))
* Build:25D771280a
* Hardware:Apple Silicon (arm64)
* Regression:Working on macOS 25.x immediately before overnight system update
* dnsmasq version:Homebrew, listening on 127.0.0.1:53
* Verified via:dig @127.0.0.1(works),host(works — uses own resolver),ping/curl/python3 socket.getaddrinfo(all fail)

## References

* man 5 resolver(macOS) — documents the/etc/resolver/mechanism
* RFC 6761 — Special-Use Domain Names (reserves.test,.localhost,.invalid,.example)
* RFC 8375 — Special-Use Domainhome.arpa
* IETF draft-ietf-dnsop-interneti-mdn —.internalspecial-use proposal



### tinyappscommentedMar 19, 2026

Thanks for tracking this down and sharing it. There are a number of references to "macOS 25" like "Regression from: macOS 25.x" and "previously worked correctly on macOS 25 and earlier" - shouldn't that be "macOS 15" instead?

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### peterccommentedMar 19, 2026

Ah, I wonder if that explains why I had to turn the fancy DNS features of Tailscale off and on again a few times to get them to work again (which they did!)

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### FrizlabcommentedMar 19, 2026•edited

You’re supposed to usescutilnowsince a long time ago actually.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







Author

### adamamylcommentedMar 19, 2026

Ah, I wonder if that explains why I had to turn the fancy DNS features of Tailscale off and on again a few times to get them to work again (which they did!)

Tailscale's been OK for me…

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







Author

### adamamylcommentedMar 19, 2026

You’re supposed to usescutilnowsince a long time ago actually.

For diagnostics, I'm aware (as is my pal, Claude). It doesn't however, allow running an equivalent of dnsmasq, does it? (If it does, that could be interesting)

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







Author

### adamamylcommentedMar 19, 2026

Thanks for tracking this down and sharing it. There are a number of references to "macOS 25" like "Regression from: macOS 25.x" and "previously worked correctly on macOS 25 and earlier" - shouldn't that be "macOS 15" instead?

unameincludes the version, but I guess for most people they think of it by name (although tbf, I can never remember the order of any of them…). My Sequoia (Intel) Mac givesDarwin Kernel Version 24.6.0.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### ralgozinocommentedMar 19, 2026•edited

I am using this with Tahoe 26.3.1; the only difference with my setup is that my local dns server (coredns instead of dnsmasq but this should be irrelevant) is listening on the5300port instead of53.

I had to configure it to listen on that port because otherwise it will conflict with macos internet sharing dns IIRC.

I'd suggest you try configuring dnsmasq to listen on port 5300 (or any other free port) and add aport 5300line to the file in/etc/resolver/<domain>.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### tinyappscommentedMar 19, 2026

Thanks for tracking this down and sharing it. There are a number of references to "macOS 25" like "Regression from: macOS 25.x" and "previously worked correctly on macOS 25 and earlier" - shouldn't that be "macOS 15" instead?

unameincludes the version, but I guess for most people they think of it by name (although tbf, I can never remember the order of any of them…). My Sequoia (Intel) Mac givesDarwin Kernel Version 24.6.0.

Yes, but that still doesn't work, since Tahoe/macOS 26.3.1 is running Darwin 25.3.0 as reported byuname -r.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### vsviridovcommentedMar 19, 2026

Can you set the file type to markdown so it's rendered?

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







Author

### adamamylcommentedMar 19, 2026•edited

Can you set the file type to markdown so it's rendered?

Done. Thanks for mentioning — I thought it had auto-detected it was Markdown.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### nightpoolcommentedMar 19, 2026

This setup worked correctly on macOS 25.x.

😭

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### per-allanssoncommentedMar 19, 2026

Try using a non-loopback IP and see if it works then.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### BeauSlimcommentedMar 19, 2026

My setup is a little different, so this is just a data point for you. I use a ".home" TLD via dnsmasq on a couple OpenWRT APs for local resolution. I have a "home" file and a "10.in-addr.arpa" file in /etc/resolver on my three macs.pings from the command line or accessinghttp://whatever.homein Firefox, so /etc/resolver is working fine for me even after yesterday's security patch.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### zlogiccommentedMar 19, 2026

I've seen similar issues as well, at least with Safari.

1. The "Limit IP address tracking" option in the network adapter settings seems to mess with macOS' DNS resolver. Even without a paid or enabled iCloud Private Relay. It seems like "Limit IP address tracking" might be forcing macOS to use a fixed DoH or DoT DNS server (this article mentions CloudFlare/Akamai:https://basila.medium.com/ios-15-2-now-uses-cloudflares-akamai-s-dns-by-default-for-your-device-s-traffic-95d0f805a827)
2. It's not ideal but completely overriding the DNS on the network interface helped.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.





Sign up for free

to join this conversation on GitHub
.
 Already have an account?

Sign in to comment
