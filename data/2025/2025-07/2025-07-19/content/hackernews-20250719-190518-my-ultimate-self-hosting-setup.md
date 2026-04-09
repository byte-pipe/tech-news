---
title: My Ultimate Self-hosting Setup
url: https://codecaptured.com/blog/my-ultimate-self-hosting-setup/
site_name: hackernews
fetched_at: '2025-07-19T19:05:18.374556'
original_url: https://codecaptured.com/blog/my-ultimate-self-hosting-setup/
author: mirdaki
date: '2025-07-19'
---

# My Ultimate Self-hosting Setup

Jul 7, 2025

“The circle is now complete. When I left you, I was but the learner, now I am the master (of this setup anyway)."

I’ve spent a few years trying different approaches forself-hosting, such as using multiple Docker compose files or Ansible. I’ve done some neat things (such as setting upPi-Hole with Docker and Traefik), but I never really committed to any approach. I wanted to find something that was “perfect” and that meant I spent a lot of time tinkering and received little actually benefit from self-hosting.

So I did some self-reflection and decided it was time for “good enough”. I laid out my goals and requirements to stay focused. I put together a step by step plan. And then after quite a bit of work, I’ve actually achieved my goal and been running this setup without major issue for over six months!

I’ve written this to share a little about the process I went through as well as some specific problems I solved along the way. I’ve really benefited from the content and software folks have freely shared, and hope I can continue that and help others.

Table of Contents

* Goals
* Requirements
* Important Tech Choices
* Layout Design
* Specific Problems and Solution
* Next Steps

## Goals

There are a lot of reasons folks get into self-hosting. Some to learn skills they can use in their career. Others to create an autonomous smart home. And yet others just love to tinker.

I primarily want control of my data and the services that use it. It’s better for privacy and can reduce the ability for companies to pull a Darth Vader and shut down services I depend on or drastically change them. Having that control makes me feel comfortable actually incorporating those services into my life. And I want to offer the same benefit to my family and friends.

## Requirements

To actually achieve that goal, I put together some requirements that balance various factors (security, usability, and complexity). Here is what I came up with in roughly priority order:

* Keep as much as I can off the public facing internetI don’t want to be the lowest hanging fruit for a malicious actor. Literally preventing connecting to a service helps to achieve that. It also gives me room to make mistakes and not severely endanger myself
* I don’t want to be the lowest hanging fruit for a malicious actor. Literally preventing connecting to a service helps to achieve that. It also gives me room to make mistakes and not severely endanger myself
* Reduce the likelihood that me misconfiguring something would bring down the core “infrastructure” of my setup for an extended period of timeI’m human, I’m going to make mistakes. So I should build something that accounts for itThis means I avoid circular dependencies, make it easy to revert changes, treat certain things as appliances, and may not even host something myself
* I’m human, I’m going to make mistakes. So I should build something that accounts for it
* This means I avoid circular dependencies, make it easy to revert changes, treat certain things as appliances, and may not even host something myself
* I fully own the core components, no Darth Vader altering the deal should break thatIn this case it means things like authentication, networking, and domain namesLimiting this to open source options means that in the worst case where a project dies or is bought out, the code is still there for me to use. That gives me time to plan next steps instead of scrambling to something else or just losing the ability to use something
* In this case it means things like authentication, networking, and domain names
* Limiting this to open source options means that in the worst case where a project dies or is bought out, the code is still there for me to use. That gives me time to plan next steps instead of scrambling to something else or just losing the ability to use something
* Relatively easy for family and friends to useThis means keep one login per person, ideally with SSO, for as many services as I canMe working with someone to setup things once is fine. But my users shouldn’t need me to regularly fix things for themIn certain cases, this might mean I do make something public facing on the internet for usability sake
* This means keep one login per person, ideally with SSO, for as many services as I can
* Me working with someone to setup things once is fine. But my users shouldn’t need me to regularly fix things for them
* In certain cases, this might mean I do make something public facing on the internet for usability sake
* Configuration should be declarative when possibleGreat for putting into version control and getting all the benefits from it like backups and reverting changesIt makes it easier to understand what I’ve doneIt’s also easier to find other people’s config and adapt it (which I’ve done a lot of)
* Great for putting into version control and getting all the benefits from it like backups and reverting changes
* It makes it easier to understand what I’ve done
* It’s also easier to find other people’s config and adapt it (which I’ve done a lot of)
* Updates should be easy and safe enough that I actually do themToo many manual steps or too precarious an update and I might delay things longer than I should
* Too many manual steps or too precarious an update and I might delay things longer than I should

And some anti-requirements:

* Things do not need to be super modular or cleanThe desire to make it perfect is strong, but for this case, often just adds complexity and uses time without benefit
* The desire to make it perfect is strong, but for this case, often just adds complexity and uses time without benefit
* Not everything needs to be open sourceTo be clear, I certainly prefer open source software, but if there is something that is just better for my use case (and still meets my other requirements), then I should allow myself that
* To be clear, I certainly prefer open source software, but if there is something that is just better for my use case (and still meets my other requirements), then I should allow myself that

## General Approach

### Important Tech Choices

Before going to far, let’s go over some specific technology that are at the core of my setup.

#### NixOS

NixOSis a Linux distribution that uses the Nix language and package manager to configure everything about the OS. It certainly has a learning curve (and it’s error messages leave much to be desired), but it’s very powerful. I can set everything from my preferred shell to firewall rules with just few lines of nix.

It has a ton ofpackagesavailable. In most cases, configuring a new service is as simple as setting a few properties like what port number to use and marking the service as enabled. And if a package isn’t available, you can always use Podman or Docker to run it. Here is a snippet of nix setting upSilverBullet(a note taking service):

silverbullet
=
 {
 enable
=

true
;
 listenPort
=

3003
;
 spaceDir
=
 cfg
.
dataDir;
 envFile
=

"/etc/silverbullet.env"
;
};

environment
.
etc
.
"silverbullet.env"

=
 {
 user
=

"silverbullet"
;
 text
=

''

 SB_SYNC_ONLY=true

 ''
;
};

I put everything into a singleGit repoto gain the benefits of version control. It also lets me share “modules” (units of configuration) across multiple of my machines.

I’ve also had a lot of luck looking up other people’s config on GitHub byfiltering for the nix languagewhen searching. That’s given me great insight how others organize and leverage nix files.

#### ZFS

ZFSis a file system that has excellent data protection features. It also allows you to create space efficient snapshots of your drives. Making it really easy to rollback if something has gone wrong (which came in really handy when I accidentally blocked SSH on one of my VMs, whoops).

You do need to set it up correctly for your use case, which took a bit of research on my part (speaking of, I’m putting a lot of helpful links at the end of this post). It’s worth understanding the pros and cons of different configuration options, as they will result in different performance and data protection.

My main storage setup is pretty simple. It a ZFS pool with four 10TB hard drives in a RAIDZ2 data vdev with an additional 256GB SDD as a cache vdev. That means two hard drives can die without me loosing that data. That gives me ~19TB of usable storage, which I’m currently using less than 10% of. Leaving plenty of room to grow.

#### Tailscale

Tailscaleis a mesh VPN that is really approachable. It allows you to connect multiple devices to each other without exposing them to the public internet (among many other features). To connect to a service I run at home, it’s as simple as installing an open source client and logging in.

Tailscale, the company, offers a free tier with a limited number of users and devices. But, because I want to own the core infrastructure of my setup, I opted to useheadscale, an open source version of the Tailscale backend. It doesn’t have all the features, but I don’t need to worry about the company changing how their tiers work or going out of business all together (though I wish them the best, it’s an awesome product I do recommend).

By putting services behind my Tailscale network, I improve my security posture. But it does have the usability con that anyone who wants to use my services, does need to run a Tailscale client on their device. This is probably the biggest pain point for family and friend usage.

#### Authelia & LLDAP

Autheliaprovides authentication and authorization for services in a couple of ways. For services that support OpenID Connect it provides a very simple single sign on experience. If not, Authelia can integrate with my reverse proxy (nginx) and require the user login before the reverse proxy allows access to a service.

LLDAPis LDAP service that provides user and group management for Authelia. It also provides LDAP auth as a backup option in case OpenID Connect is not supported by a service I want to use.

I really appreciate that both Authelia and LLDAP are very lightweight and that they work well together. But I’m not going to lie, understanding how auth works and getting it setup took a lot of time. But between the official docs, other people’s configs, and experimentation, I have it working nicely.

### Layout Design

Here is a diagram of where I’ve ended up:

In case folks are curious, each computer is named after a Star Wars planet (and has some loose meaning connecting it to that planet).

#### Primary Public Server

The entry point for my services is “taris”, which runs the services that everything else needs (Authelia and headscale) or things that just need to be publicly available (like this blog). I want to keep it limited. Both because that means their is less that can go wrong and also because it’s running on a relatively cheapVPS.

Headscale needs to be publicly available, as it acts kinda like a lighthouse for all the Tailscale clients to find before they can connect to each other. Because logging into the Tailscale network uses Authelia and LLDAP, those also need to be publicly available. I also run a secondary status monitoring service on taris so I can be notified if my primary status monitoring service on my private server goes down.

I also use taris to proxy out my Foundry VTT service (used to play games like Dungeons and Dragons remotely). I can’t run it on taris itself, since Foundry is heavy to run. I also didn’t want everyone I play with to need to setup Tailscale. It just adds too much friction. More info on how I proxy ithere.

#### Primary Private Server

My main physical server is “kuat”. It’s runningTrueNAS, which makes creating and managing the NixOS VMs and ZFS pool pretty pleasant.

Within my ZFS pool I have two datasets, which I’ve organized by backup needs. My “files” dataset holds data I created (like photos, documents, associated databases, etc) and that I would be very sad to loose. My “media” dataset contains data from other sources (like ripped blu-rays and purchased ebooks), which I could replace if necessary. Each is an NFS share that my VMs can mount (though enabling that required someextra steps).

My primary VM is “bespin”. It leverages NixOS to runs the bulk of my services. It points my services to use the appropriate dataset to store it’s data (e.g. Nextcloud with my photos uses my “files” dataset and Jellyfin with my movies uses my “media” dataset). I also have a test VM called “alderaan” that I sometimes use to test services before I blow it away.

#### Other Services

I have a couple of machines I treat as appliances. They only serve one purpose, because I consider them so mission critical. This way, me misconfiguring something elsewhere shouldn’t break them.

I runHome Assistant OSon “tython” for my smart home needs. I considered running it with NixOS, but Home Assistant really pushes to use add-ons managed by Home Assistant OS itself. I decided to just go with the default approach. Some things aren’t worth fighting against the tide for.

“coruscant” runs myMatrixserver andElementchat client (Matrix is a really neat open source protocol that can connect all your chat platforms into one place). There is a greatprojectthat provides an Ansible playbook for managing all the various components used with Matrix, so I rely on them instead of doing it all over again myself.

I also fully outsource my email and password management toProtonMailandBitwardenrespectively. I need both to always work. Email is a critical communication platform and very tricky to get right. And I need secrets in my password manager to setup my services. If I ran it myself, I could have a dependency problem where my infrastructure needs the password manager to run, but my password manager couldn’t run without my infrastructure.

## Specific Problems and Solution

Any project like this is going to encounter countless little problems and solutions along the way. Here are some of the standouts.

### Service Awareness for Others

My family and friends aren’t likely to remember a bunch of different URLs to access the services I make available to them. To simplify that, I have a “start page” they bookmark for easy access. It list the services they can use so they can easily navigate to them.

I’m usingFlame, which is a dashboard management project, to create this start page. Flame hasn’t been updated in a while, but it’s not doing a whole lot and looks pretty. I just manually add the common services folks can use and it works well enough. I may eventually look for alternatives, but this is perfectly serviceable for now.

### Using Tailscale and Another VPN

Unfortunately many operating systems (Android and Windows for instance) don’t support running multiple VPNs at the same time. Since Tailscale is a VPN, this creates some issues if you want to use another VPN (for privacy reasons) to route the non-Tailscale network traffic (such as your internet searches).

Tailscale does have a feature called “exit nodes” that allows you to route all your client’s traffic to another a device on the Tailscale network.

We can combine exit nodes withGluetun, which is a containerized OpenVPN and Wireguard client. It allows you to connect to a another VPN service, such as ProtonVPN.

With some container network fiddling, we can have a containerized Tailscale exit node send it’s outgoing traffic to a ProtonVPN endpoint. Here is myNix configfor all that.

This does mean an Android user could connect to Tailscale and select that ProtonVPN endpoint as an exit note. Which is great!

But with the major caveats that it does use a lot more battery than a normal VPN and I’ve noticed irregular slow downs when using the exit node (my current guess is higher processor load on my server causes these latency spikes). So I sometimes use it, for instance if I’m connecting to public WiFi, but it’s not an always on thing for me.

I’ve not had issues on Linux using Tailscale alongside ProtonVPN (not through an exit node), so for my personal desktop/laptop, I don’t bother connecting to the exit node.

### Important Auth Notes

Auth is a pretty confusing space. There are a lot of different protocols and terminology that come into play to set things up. So I wanted to include a few useful points.

From my experience, the main protocols you’ll find self-hosted services supporting are OpenID Connect (OIDC), OAuth (which OIDC builds on, but services may only support specific auth providers like Google) and LDAP. If you have the option, choose OIDC, it’s more modern and has a better sign in experience with Authelia than the others.

Each service will need it’s own configuration both on the service side and on Authelia’s side to support logging in. Here is an example of myAuthelia config for Nextcloudand ahere are the steps for setting up Nextcloud’s portion of it.

I recommend always having an admin account that doesn’t use Authelia/LLDAP with each service. You probably need one anyway to get auth setup. But keeping it around and separate afterwards means you can fix auth configuration issues if something goes wrong.

For services that don’t use Authelia/LLDAP to sign in, I use this customenableAuthelia optionto easily connect nginx to Authelia and require sign in. It’s simple onceconfiguredand adds extra security.

Finally, Authelia does support access control, limiting users to specific domains. Which is great. But the nginx proxy access control and the OIDC access controlare configured separately. I didn’t realize that at first and had a more open policy than I intended. It’s easy enough to work with, just requires knowing about it.

### DNS and SSL

My public service domain names are configured like normal where you map the name to the public IP.

For my private services, I use the “internal” sub-domain of my primary domain. It provides an obvious indicator that a service is not publicly available. In my domain registrar, the DNS record of the “internal” domain point to the Tailscale IP address of that server. This is fine, as Tailscale uses anIP range that isn’t used by the public internet. So there isn’t a chance of accidentally pointing to someone else’s server.

NixOS has someconvenient optionsfor getting SSL certs via Lets Encrypt. For my publicly accessible services, I use traditional HTTP-01 validation (which has Lets Encrypt ping my server to confirm it is who says it is). For my internal services, I need to useDNS-01 validation. It has different steps depending on your domain registrar, but usually requires using some kind of secret your registrar gives you and saving it on your server for your server to prove it is yours.

### NixOS on a VPS

Simple note that most VPS providers don’t have NixOS as an install option. You can consultthis tableto find out what steps are needed to get it running with many of the popular providers.

### Mounting a TrueNAS Dataset on a VM

By default, TrueNAS blocks traffic from it’s VMs to the host. ThisLevel1Tech guideprovided a solution for me, though I later found anofficial guideas well. You’ll need to create a bridge network between the VM and host. After following those steps, I was able to mount my NFS datasets using thenormal steps.

### Proxying a Private Service Publicly

It’s pretty straightforward to expose a private service on the public internet. If you’re using the official Tailscale service, they have something calledTailscale Funnel. But if you’re like me and running headscale, it’s not much more complicated.

On an public server, you just use nginx’sproxyPasswhile pointing at the Tailscale domain name of the private server and the port number the service is using. Here is theconfigandexample valuesto do it.

## Next Steps

Now any project like this is never done. But I can mostly keep it on autopilot now, and just slowly tweak or add things as time and need arise. Here are a few things I’m thinking of:

* I need a dedicated backup server (or two) to backup my important data to. I do already have a lot of it in Nextcloud, which syncs to my desktop and laptop. So I’m not in a terrible place, but it should be better. This will also involve making sure I can actually restore everything too, since a backup doesn’t do anything if you can’t use it.
* I should also take advantage of the access control features of headscale/Tailscale. I don’t have any users I don’t trust on the Tailscale network, but that’s not a good reason to not lock it down some.
* In general I want to do another pass and see what other security improvements I could make (such as make SSH visible only over Tailscale, at least for my public servers).
* I want to look again at something likePi-holeorAdGuard Hometo provide a local DNS encryption and cache. I likely wouldn’t use it to provide the DNS for my local services, as that’d turn it into another piece of core infrastructure that everything would depend on.
* And of course, I have an ever growing list of services that sound interesting I want to add, such asForgejo(a Git server),Manyfold(a 3D print catalog), andRomM(a game rom manager)

## Resources

Here are a few useful links to help you learn more:

* My self-hosted config
* Perfect Media Server
* LinuxServer.io
* Understanding ZFS concepts
* Choosing the Right ZFS Pool Layout
* How Nix Works
* Configuring NixOS
* NixOS Security Steps

Till next time,- Matthew Booe

## Related Posts
