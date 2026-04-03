---
title: IPv6 Adoption in 2026
url: https://www.netmeister.org/blog/ipv6-adoption.html
site_name: lobsters
content_file: lobsters-ipv6-adoption-in-2026
fetched_at: '2026-02-22T06:00:38.104925'
original_url: https://www.netmeister.org/blog/ipv6-adoption.html
date: '2026-02-22'
tags: networking
---

# Signs of Triviality

Opinions, mostly my own, on the importance of being and other things.

 [
homepage
] 
 [
blog
] 
 [
jschauma@netmeister.org
] 
 [
@jschauma
] 
 [
RSS
]


## IPv6 Adoption in 2026

February 19th, 2026

IPv6 was defined inRFC1883in December of 1995. That's right, IPv6 is now30frickin' years old, and we're still
 nowhere near universal adoption. What's worse, Istillhave to argue with people about why
 they should treat IPv6 as a first-class requirement,
 not a "nice to have" optional feature.Akamai,Cloudflare,
 andGoogleall show similar adoption rates of around 40% - 45% of
 HTTP traffic to the sites they each serve:

IPv6 Adoption in the USA from 2013 until 2026

These companies provide the server-side view, with
 the ability to assess which networks or countries
 support IPv6, and one interesting observation there is
 that it looks like IPv6 traffic rises and falls
 following workday pattern, suggesting possibly higher
 availability of IPv6 on mobile or residential networks
 compared to business or perhaps off-hour usage
 patterns that favor services with higher IPv6
 availability (e.g., streaming) compared to "business
 traffic":

 IPv6 Adoption in the USA from February 2025
 - February 2026


But that peculiarity aside, this traffic is all HTTP as
 observed by the big service providers. What kind of
 IPv6 traffic adoption did I see on my puny little
 domain? Well, the answer was disappointing: only
 about 20% of HTTP traffic, 3.43% of SMTP traffic, and
 2.34% of DNS traffic to this server is IPv6. Abysmal.

But this got me to wondering wondering just about
 serviceavailabilityin general. Rather than
 focusing on clients, I was looking to answer the
 question: what percentage of serversoffersIPv6? For that, I once again scanned theTranco Top 1M
 domainsand checked each for the availability ofAandAAAArecords for theirwwwservice names, theirMXrecords, as well as theirNSglue records.

### NSrecords / DNS

Let's start at the DNS. The use ofNSrecords and the concentration
 of DNS providers is is a topic I've exploredpreviously, but not
 from an IPv6 angle. Theroot
 zoneis, of course, fully dual stack, but what
 about the top-level domains (TLDs)? As of February 2026, there
 are 1,436 TLDs in the root zone. Looking only at theNSglue records in the root
 zone:

 

Total

% of TLDs

Only IPv4-only glue records

18

1.25

Only IPv6-only glue records

0

0

At least one IPv4-only glue record

240

16.71

At least one IPv6-only glue record

22

1.53

Ok, so that's fairly good:98.75% of all TLDs
 use IPv6for their name servers.

Now for the Top 1M Domains, I looked up theNSrecords and used theiradditional dataif provided by the name
 server and otherwise manually looked up theNS'sAorAAAArecords.1

 

Total

% of TLDs

All NS IPv4 only

260,739

27.99

All NS IPv6 only

10

0.001

All NS dual-stack

645,560

69.30

At least one dual-stack NS

670,054

71.93

At least one NS IPv4-only

281,475

30.22

At least one NS IPv6-only

834

0.09

Dual-stack + at least one IPv4-only NS

24,170

2.59

Dual-stack + at least one IPv6-only NS

104

0.01

Dual-stack + IPv6-only + IPv4-only

36

0.003

Dual-stack + only IPv4-only

24,134

2.59

Dual-stack + only IPv6-only

68

0.007

At least one NS IPv6-enabled

670,784

72.01

So in summary, for the Top 1M Domains, slightly
 over70% of name servershave IPv6 addresses.
 That's a far cry from near universal availability as
 for the TLDs, but still not terrible.

### WWWrecords / HTTP

Now on to HTTP traffic. As noted above, large
 content delivery networks obviouslysupportIPv6, and as I notedpreviously,
 the majority of the Top 1M Domains are served by just
 a few large service providers, so you would expect
 pretty much all of them to likewise speak IPv6. But
 it turns out that even on those CDNs thatofferIPv6, customers do indeed choose toactively disableit.

 

Total

% of Top 1M
2

IPv4 only

557,996

55.80

Dual-Stack

353,223

35.32

IPv6 only

157

0.2

That is: onlyslightly more than a thirdof
 the Top 1M Domains are IPv6 enabled!

Now "Happy
 Eyeballs" has been around since "World
 IPv6 Day" 15 years ago (!), andRFC8305dates back to 2017, but this doesn't assuage many
 conservative and change-averse industry verticals who,
 perhaps years ago, observed a minor performance
 penalty during early IPv6 testing and since then have
 left their "Disable IPv6" code, configs, and convictions
 in place unchanged.

### MXrecords / SMTP

But of course the internet is more than just the
 web, and HTTP is not the only protocol we care about.
 I've covered email before (e.g., with respect toPQC supportor the
 distribution ofemail
 service providers), so it made sense to take a
 look at IPv6 support across the Top 1M Domains'MXrecords as well. For each
 domain'sMXrecords, I
 checked theirAandAAAArecords to see how many mail
 servers are, in theory at least3, reachable via
 IPv6 and IPv4 on all, some, or none of their named
 mail exchanges.

Looking at the Top 1M Domains, 643,241
 domains have explicitMXrecords4; for those, I've
 found:

 

Total

% of MX records

All MX IPv4 only

334,696

52.03

All MX IPv6 only

74

0.01

All MX dual-stack

288,849

44.91

At least one MX dual-stack

301,273

46.84

At least one MX IPv4-only

347,119

53.96

At least one MX IPv6-only

271

0.04

Only IPv4-only and IPv6-only MXs

89

0.01

Dual-stack with at least one IPv4-only MX

12,334

1.92

Dual-stack with at least one IPv6-only MX

108

0.01

Dual-stack + IPv4-only + IPv6-only MX

18

0.002

Dual-stack + only IPv4-only MX

12,316

1.91

Dual-stack + only IPv6-only MX

90

0.01

At least one MX IPv6 enabled (dual-stack or IPv6-only)

301,436

46.86

This comparison does not take into account the mail
 exchange's priority, but in summary:fewer than
 halfof all of the Top 1M Domains' mail servers
 support IPv6!

There are many reasons why mail servers might
 conservatively favor IPv4-only configurations. "Happy
 Eyeballs" has always seemed to me primarily an HTTP
 focused approach, even though the RFC is protocol
 agnostic. I just haven't seen many SMTP servers
 implement it, which, in turn, means that any IPv6
 misconfiguration leads to performance impact or even
 lost mail.

Additionally, a large number of SMTP abuse
 prevention mechanisms -- requiring matching reverse
 DNS records, IP block reputation scoring,
 SPF/DKIM/DMARC configuration -- see challenges with IPv6
 adoption. But while I'm sympathetic to such concerns,
 they can be overcome: Google and Microsoft offer IPv6
 for Gmail and Outlook respectively, so I'm going to
 have to give Yahoo, GoDaddy, and Namecheap (to name
 just a few of the big providers) some
 serious side-eye for remaining IPv4 only here.

### Conclusion

The lack of IPv6 adoption is frustrating. For the
 two most widely used protocols, SMTP and HTTP,
 organizations choose to consciouslydisableIPv6, in part, I'm certain, based on decisions made
 ten, fifteen, or more years ago.

None of the problems service providers might
 encounter are impossible to overcome, but all of them
 suffer from the lack of critical mass adoption
 problem. As long as IPv6 is not seen as a
 fundamental requirement to do business, people will
 continue to disable it; as long as large businesses
 disable IPv6, it will not be seen as a fundamental
 requirement.

This is exacerbated by our educators failing our
 next generation: even today, in 2026, there are many
 engineering schools and universities thatdo not
 have IPv6on campus! Computer Science and
 Engineering students are not exposed in their
 homework, projects, labs, and even routine use to
 IPv6, so when they enter the industry, they will
 continue to favor what's been "working" for them so
 far: NAT and RFC1918 overuse. Why bother with something
 they've never engaged with?

<Insert inspirational "let's roll up our sleeves
 and enable IPv6 everywhere" message here>, but
 I suspect we'll still not be there in
 another ten years, either. Universal IPv6 seems as elusive
 as Linux on the Desktop -- onlythatis
 actually an entirely viable alternative at this
 point. And people are clearly being overly hopeful
 about IPv6 adoption when I asked onMastodon,
 at least in comparison, I suppose:

Wish I was so optimistic...

February 19th, 2026

Footnotes:

[1] Some DNS lookups simply failed
 due to a server side failure or yielded no results, so
 I ended up with a total of 931,515 domains instead of
 an even one million.↩

[2] Around 8.86% of top 1M domains
 do not have anyA/AAAArecords for their
 second-level or theirwww.<domain>name. This
 includes domains such as, e.g.,akamai.netorakadns.net, which are used by
 Akamai for customer subdomains but don't themselves
 serve as HTTP endpoints.↩

[3] I say "in theory", because I have observed some
 widely used mail services tohaveAAAArecords that are not
 actually reachable. This is, of course,worsethan not having anyAAAArecords at all, because now
 IPv6 enabled mail servers will attempt and then time
 out on trying these addresses before hopefully failing
 over to IPv4.↩

[4] For this exercise, I'm ignoringNULL
 MX recordsas well as noMXrecords. That is, I'mnotlooking at what the raw domain resolves
 to.↩

Links:

* Discussion on HackerNews
* Akamai IPv6 Statistics
* APNIC labs IPv6 stats
* Cloudflare IPv6 Statistics
* Google IPv6 Statistics

Related:

* Who reads your email?
* Who controls the internet?

 ← [
Use of PQC in SMTP STARTTLS
]

 [
homepage
] 
 [
blog
] 
 [
jschauma@netmeister.org
] 
 [
@jschauma
] 
 [
RSS
]
