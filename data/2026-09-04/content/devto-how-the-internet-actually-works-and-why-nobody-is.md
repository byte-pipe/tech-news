---
title: How the internet actually works, and why nobody is in charge of it - DEV Community
url: https://dev.to/lovestaco/how-the-internet-actually-works-and-why-nobody-is-in-charge-of-it-3im8
site_name: devto
content_file: devto-how-the-internet-actually-works-and-why-nobody-is
fetched_at: '2026-09-04T21:14:44.304248'
original_url: https://dev.to/lovestaco/how-the-internet-actually-works-and-why-nobody-is-in-charge-of-it-3im8
author: Athreya aka Maneshwar
date: '2026-09-01'
description: Hello, I'm Maneshwar, and I'm building LiveReview — a blast-radius aware AI code review built for... Tagged with networking, webdev, programming, beginners.
tags: '#networking, #webdev, #programming, #beginners'
---

Hello, I'm Maneshwar, and I'm building LiveReview — a blast-radius aware AI code review built for your business-critical systems.Star usto help devs discover the project, give it a try, and share your feedback to help improve the product.

You open a video and it starts playing in about a second.

Somewhere between your thumb and that first frame, your request crossed maybe fifteen different companies' equipment, possibly an ocean, and came back. Nobody coordinated it.

That is the part I find genuinely strange about the internet, and it is the part most explanations skip.

They tell you the internet is "a global network of networks", which is true and tells you nothing. So let's actually take it apart.

## There is no internet. There are 75,000 of them.

The single most useful thing to understand up front:the internet is not a thing anyone built.

It is roughly 75,000 independent networks that agreed on how to hand traffic to each other.

Your ISP is one. Your university is one. Cloudflare is one.

They own their own cables and routers, they answer to nobody in particular, and they interconnect voluntarily.

Once you see it that way, every weird thing about the internet starts making sense.

The whole arrangement has three parts:

The edgeis everything that actually wants to say something. Your phone, a laptop, a server in a rack, and increasingly a doorbell.These are calledhostsorend systems, and they split roughly into clients that ask and servers that answer.

The access networkis your on-ramp. Fibre or cable at home, the office network, 5G from your pocket.Its only job is getting you to the first router.It is also, almost always, the slowest part of the entire journey, which is worth remembering next time you blame a website for being slow.

The coreis the mesh in the middle.Routers and the links between them, and nothing else.No control room, no master server, no company that owns it.

## Nobody reserved you a line

Here is where the design gets clever.

Before the internet, connecting two things meant acircuit.

Make a phone call and the network reserved a physical path end to end for you, for the whole call, whether you were talking or breathing.

The internet threw that out. Your data gets chopped intopackets, each one stamped with where it came from and where it is going, and each one is then thrown into the network to fend for itself.

Packet three might go via Frankfurt while packet four goes via Amsterdam. They can arrive out of order. Some might not arrive at all.

This sounds worse than a reserved line, and for a single conversation it kind of is. What you get in exchange is enormous:

* The network is shared efficiently.Nobody is holding a lane open while they think about what to type.
* It routes around damage.A cut cable is a detour, not an outage. That was literally the design goal.
* It scales absurdly.Routers do not track your conversation. They just look at each packet and pass it on.

The reassembly, the retries, the putting-things-back-in-order, all of that happens at the two ends.

The middle stays gloriously dumb. That principle has a name, theend-to-end argument, and it is arguably why the internet could grow the way it did.

## Every layer adds an envelope

So how does one blob of bytes know how to get anywhere?

It gets wrapped. Four times.

Your browser makes a request at theapplication layer. HTTP, or SMTP for mail, or DNS for lookups.

Thetransport layerwraps it with ports and sequence numbers.TCP if you want it reliable and in order, UDP if you would rather have it fast and are willing to lose some.

Thenetwork layerwraps that with IP addresses.Source and destination, like a postal address.

Thelink layerwrapsthatwith the hardware address of the next hop, which is usually your router, sitting a few metres away.

At the other end, each layer peels off its own envelope and passes the rest up. That is encapsulation on the way down and decapsulation on the way up.

Here is why this matters rather than just being trivia:each layer only knows about the one below it.Walk from wifi to ethernet mid-download and only the bottom envelope changes. TCP does not notice.

Your browser certainly does not. You can swap out an entire generation of physical network technology without touching a single line of application code, which is exactly what happened when the world moved to fibre, and again to 5G.

You can watch the envelopes for yourself:

# every router between you and a host, one line each

traceroute 
-q1
 dev.to

Enter fullscreen mode

Exit fullscreen mode

# or watch a single request get wrapped, live

sudo 
tcpdump 
-n
 
-i
 any 
-c
 5 
'host dev.to and port 443'

Enter fullscreen mode

Exit fullscreen mode

tracerouteis the more fun one. Each line is a real machine, in a real building, owned by a real company, that agreed to pass your packet along.

## Forwarding is not routing

These two words get used interchangeably, including by people who should know better. They are completely different jobs.

Forwardingis local and fast. A packet lands on a router, the router looks at the destination address, checks its forwarding table for the longest matching prefix, and shoves it out the right port. That is it. Nanoseconds, in dedicated hardware, millions of times a second. The router has no idea about the rest of the journey and does not care.

Routingis global and slow. It is the process of building those tables in the first place, which means every network on earth continuously telling its neighbours what it can reach.

One is reading the map. The other is the argument about what the map should say.

## The argument is called BGP

Networks announce their reachability using theBorder Gateway Protocol.

Your ISP says "you can reach these addresses through me", its neighbours repeat it, and within minutes the whole planet has updated.

Now here is the bit that should alarm you slightly.

BGP has no built-in way to check whether an announcement is true.

It is a protocol built on the assumption that network operators are honest and competent.

If a network announces address space it does not own, and its neighbours believe it, the world's traffic for those addresses starts flowing to the wrong place.

This is not hypothetical. In 2008, Pakistan Telecom tried to block YouTube domestically, announced YouTube's address range to its upstream provider by mistake, andtook YouTube off the internet for most of the planet for about two hours.

In 2018 a similar hijack was used to steal cryptocurrency by redirecting traffic to a DNS service.

Efforts likeRPKIare gradually adding cryptographic checks, so a network can prove it owns what it announces.

Adoption is still partial, andisbgpsafeyet.comwill tell you whether your own ISP has bothered.

One more thing that surprises people: routing is not really about finding thefastestpath.

BGP picks paths largely on business relationships, because carrying traffic costs money and networks prefer routes they get paid for over routes they pay for.

Your packets are not taking the shortest road. They are taking the cheapest road that somebody agreed to.

## What actually happens when you press Enter

Let's put the whole thing together on one request.

flowchart TD
 A[You press Enter] --> B{Address in a cache?}
 B -->|Yes| IP[IP address in hand]
 B -->|No| DNS[Ask a DNS resolver]
 DNS --> ROOT[Root, then .com, then the domain]
 ROOT --> IP
 IP --> TCP[TCP handshake: SYN, SYN-ACK, ACK]
 TCP --> TLS{Using HTTPS?}
 TLS -->|Yes| HS[TLS handshake, keys agreed]
 TLS -->|No| REQ
 HS --> REQ[Send the HTTP request]
 REQ --> HOP[Packets hop router to router]
 HOP --> SRV[Server answers]
 SRV --> PAINT[Browser paints the page]

Worth noticing how much of that is preamble. Before a single byte of the actual page moves, you have done a name lookup, a three-way handshake, and usually a TLS negotiation on top.

That is why latency hurts so much more than bandwidth for normal browsing. A fatter pipe does not make a round trip shorter, and you are paying for several round trips before anything renders.

Upgrading your connection speed does approximately nothing for a site whose server is far away.

## The floor you cannot get under

One last thing worth internalising, because it explains a lot of architecture decisions.

Light in fibre travels at roughly two thirds of the speed of light in a vacuum. London to New York is about 5,500km.

That is around 28 milliseconds each way if the cable ran perfectly straight, which it does not, so call it 35 to 40.

A single HTTPS request needs several round trips before the first byte comes back.

You are looking at 150ms or so before anything happens, and no amount of money moves that number, because it is a physics problem rather than an engineering one.

This is the entire reason CDNs exist. You cannot make the packet faster, so you move the content closer.

Every "edge computing" pitch you have ever heard is fundamentally a workaround for the speed of light.

## So what is the internet, really

It is not the cables. Those are just glass.

It is not the web either, which is one application riding on top of it, and one that arrived twenty years late to the party.

The internet is an agreement.

A set of protocols that let tens of thousands of independently owned, mutually distrustful networks hand packets to each other without any of them needing permission, a contract, or even a phone call.

It works because the middle was kept stupid and the edges were allowed to get clever.

That is a design decision made in the 1970s by people who could not have imagined video calls, and it held.

Your team's attention is limited, and the deluge of AI-generated code is making it harder to keep production code safe without slowing you down.

I'm buildingLiveReview, a blast-radius aware AI code review built for your business-critical systems.

Instead of presenting every diff with equal emphasis,LiveReview scores each change by blast radius — how far its impact reaches through your call graph — so you can focus attention where it actually matters.

Spend code review effort where business risk is highest — not spread evenly across every diff.

Try LiveReview on your codebase:

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse