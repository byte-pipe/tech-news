---
title: Monitoring my Homelab, Simply
url: https://b.tuxes.uk/simple-homelab-monitoring.html
site_name: lobsters
fetched_at: '2025-07-11T23:06:40.773389'
original_url: https://b.tuxes.uk/simple-homelab-monitoring.html
date: '2025-07-11'
tags: distributed, go, networking
---

# Monitoring my Homelab, Simply

Date:2025-07-09

I have a middling self-hosted/homelab setup, and it
 occasionally breaks.

Alas, no monitoring tool has ever sparked joy in me.

Don’t get me wrong, I understand that they’re essential for
 large fleets of services with fast-changing software and teams of
 oncallers working around the clock to understand the complex ways
 that complex systems fail… but my stuff doesn’t change that
 often, failures are mundane and low-scope, and I’m the only
 person coming to rescue this poor stopped systemd unit that
 failed to restart, or open the port that I accidentally blocked
 in an overzealous attempt to stop the barbarians.

So between no monitoring and Prometheus, I’ll choose no
 monitoring every day.

But there’s a spectrum.

## What I want from a
 monitoring setup

* Pages me when my stuff is aggregiously broken.
* Pages me if things are still broken.
* Pages me when my stuff is fixed.
* Stops pages me when I want.
* Can see into my Wireguard mesh network.
* Easy to add probers.

Simple, by which I mean:

* Easy to understand, e.g. avoid state.
* Easy to maintain: deploy, updates, blah, blah.
* Few moving pieces.

Out-of-scope:

* Historical data: I’m not chasing down grand mysteries that
 require fleet-wide aggregate metrics.
* Dashboards: I’m okay with logs.
* Perfection: a bit of jank is fine.
* False positives are okay: I don’t mind being pinged of a
 false problem, as long as I get told when things recover.
* False negatives are okay: it’s okay to miss things. My goal
 is to add a little monitoring, to catch agregious issues.

## Design

tl;dr I wrote a tiny program, that regularly checks
 HTTP/DNS/etc., and pages me via https://ntfy.sh

I’ve been running this for 2-3 years now.

### Show me the code

A prober probes at an interval, and has a description.

type prober interface {
 probe(context.Context) error
 interval() time.Duration
 String() string
}

Here’s an example prober for checking TLS connectivity and
 cert expiration:

type tlsProber struct {
 host string
 port int
 duration time.Duration
}

func (p *tlsProber) probe(ctx context.Context) error {
 target := fmt.Sprintf("%s:%d", p.host, p.port)
 conn, err := tls.Dial("tcp", target, &tls.Config{})
 if err != nil {
 return err
 }
 defer conn.Close()
 cs := conn.ConnectionState()
 if len(cs.PeerCertificates) == 0 {
 return fmt.Errorf("want >0 certs, got 0")
 }

 cert := cs.PeerCertificates[0]
 expiration := cert.NotAfter
 if diff := expiration.Sub(time.Now()); diff < 14*24*time.Hour {
 return fmt.Errorf("cert expires in %v at %v", diff, expiration)
 }
 return nil
}

func (p *tlsProber) interval() time.Duration {
 return p.duration
}

func (p *tlsProber) String() string {
 return fmt.Sprintf("TLS %s:%d", p.host, p.port)
}

I have similar things for HTTP, TCP, DNS and domain
 expiration. I have a decorator-styleretryProberfor
 if things are flaky.

I run each prober in a loop, notifying once for failures, with
 reminder notifications every hour. When the probe proceeds, it
 notifies too.

const reminderInterval = 1*time.Hour

type state int
const (
 good state = iota
 bad
)

func run(ctx context.Context, p prober, n notifier) {
 defer panic("Unreachable. Don't stop ticking. Never return!")
 log.Printf("Runner started for prober %q with interval %v.", p.String(), p.interval())
 ticker := time.NewTicker(p.interval())
 reminderTicker := time.NewTicker(reminderInterval)

 s := good
 var lastErr error
 for {
 select {
 case _ = <-ticker.C:
 // Jitter. Also, prevent crash loops from causing damage.
 time.Sleep(time.Duration(rand.Intn(5000))*time.Millisecond)
 log.Printf("Probing %s", p.String())
 err := p.probe(ctx)
 if err != nil {
 // bad
 if s == good {
 if err := n.notify(ctx, fmt.Sprintf("%s: %v", p.String(), err)); err != nil {
 log.Printf("Notify failed: %v", err)
 }
 } else {
 log.Printf("%s failed but not re-notifying: %v", p.String(), err)
 }
 s = bad
 lastErr = err
 continue
 }

 // good
 if s == bad {
 if err := n.notify(ctx, fmt.Sprintf("%s: now passing", p.String())); err != nil {
 log.Printf("Notify failed: %v", err)
 }
 s = good
 lastErr = nil
 }
 case _ = <-reminderTicker.C:
 log.Printf("Checking whether to ping a reminder for %s", p.String())
 if s != good {
 if err := n.notify(ctx, fmt.Sprintf("%s still failing: %v", p.String(), lastErr)); err != nil {
 log.Printf("Notify failed: %v", err)
 }
 }
 }
 }
}

If I was to review my own code I’d saysshould
 be namedprevState, and// badneeds
 more clarification. But this is my code and my blog, so LGTM!

I’ve left some boring bits out likemain,notifier, but I will mention that probers are
 defined in code:

var mythicBeastsNS = []string{
 "ns1.mythic-beasts.com",
 "ns2.mythic-beasts.com",
}

var probers = []prober{
 &tlsProber{host: "b.tuxes.uk", port: 443, duration: 5*time.Minute},
 &tcpProber{host: "my-vps.example.com", port: 22, duration: 5*time.Minute},
 &domainProber{domain: "tuxes.uk", rdapURL: "https://rdap.nominet.uk/uk/domain/tuxes.uk", expectedNS: mythicBeastsNS},
}

This saves me dealing with parsing, config files, and offers
 the flexibility of code.

### Deployment

This can run ~anywhere. It doesn’t listen, so no need to put
 it somewhere that can be scraped.

This happens to run as aDynamicUserdaemon on my
 router: my most reliable machine; a dependency to me fixing
 things anyway; and something I’ll notice if down.

### Receiving pages

I have https://ntfy.sh installed on my phone to receive pages.
 It’s respectful of battery, and can silence for n hours.

I can’t silence particular pages, so every silence is
 “global”. This is fine, I just need to know “I should fix a
 thing”. A global silence could mask growing problems. Meh. It’ll
 do.

### How to monitor the
 monitor?

If my daemon crashes, or I accidentally drop my computer in a
 stew, how long will it be until I notice I have no
 visibility?

To avoid this, I ping https://healthchecks.io as a dead man’s
 switch. If that doesn’t get a ping in the last 10 minutes it
 notifies me via https://ntfy.sh and email.

There’s a subtlety here. If my program reliably crashes after
 6 mins of runtime (e.g. due to memory leak, or a panic that
 happens on 2nd probe), but I manage to ping healthchecks.io every
 5 minutes, then my dead man’s switch will be happy, but my less
 frequent probers won’t ever be called.

So I have two dead man switch’s:

* One which expects pings every 5 mins
* One which expects pings every 2 hours

Those are also just HTTP probers:

var probers = []prober{
 // ...

 // Shortwave ping that is meant to quickly detect if this server is down.
 &httpProber{url: "https://hc-ping.com/79bfdda2-b162-451c-bc33-58d925240434", expected: 200, duration: 5*time.Minute},

 // Longwave ping that is meant to detect if this binary is crash looping.
 &httpProber{url: "https://hc-ping.com/05bdb3cc-4a2f-48dd-9a24-b08977e7f6a9", expected: 200, duration: 2*reminderInterval},
}

I can’t remember why I decided that the longwave probe should
 have a period of 2*reminderInterval, but I remember thinking hard
 about it, and thinking I was quite the scholar for thinking hard
 about this. If you figure it out and I’m correct, then please let
 me know.

## What I like about it

* Every part of this program fits inside my head.
 Mostly.
* Its only dependency is the Go standard library. Go is okay,
 but APIs that don’t break on me are great.
* Its only state is whether the last probe succeeded, and
 what the error message was.
* Adding probers or prober types is just normal code. No
 having to constrain my program with serialisation matters.

## Limitations

* No whitebox monitoring. Sometimes I’d like to check things
 like whether OS-level auto upgrades are working. Prometheus
 exporters can do this, and I miss out on those. It might not be
 too much code to parse some simple metrics from/metrics, or expose this via/health,
 but I’ve not needed it to bother.

## Alternatives

Probing is nothing new. There are tons of alternatives.

### No monitoring

I could just wait for me or my family to notice stuff is
 broken. It’s a reliable way to learn of stuff that actually needs
 fixing. But I’d like to spare that inconvenience, and have notice
 to fix things. Besides, I’m usually the cause of breakages, and
 if I can learn shortly after breaking it, I’m usually in a good
 spot to fix it.

### updown.io

A great site. Sadly it doesn’t have that many probers, and
 can’t see within my mesh network.

### Uptime Kuma

Pro: Looks nice. Off-the-shelf.

Con: Difficult to extend. Persistent state.

### Prometheus and Blackbox
 exporter

Nooooo
