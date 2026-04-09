---
title: I'm a laptop weirdo and that's why I like my new Framework 13
url: https://blog.matthewbrunelle.com/im-a-laptop-weirdo-and-thats-why-i-like-my-new-framework-13/
site_name: hackernews
fetched_at: '2025-12-26T19:06:40.899786'
original_url: https://blog.matthewbrunelle.com/im-a-laptop-weirdo-and-thats-why-i-like-my-new-framework-13/
author: todsacerdoti
date: '2025-12-26'
published_date: '2025-08-29T17:11:30.000Z'
description: It turns out I've always done weird things to my laptops.
---

This month I sold my 2021 M1 Max Macbook Pro and bought a Framework 13 DIY Edition laptop. After I got everything setup I sat down to write about the experience. Some ~4500 words later I realized I needed to break my thoughts into multiple posts.

See also:

* Framework 13 DIY Edition Hardware Thoughts
* Setting up my new Framework Laptop 13 DIY Edition with NixOS

My new Framework 13 laptop just arrived. After I finally set everything up I started writing a post about the experience. I thought I'd write alittle bitabout my previous laptops, but a lot of fond memories I had forgotten about came flooding back. The tinkerings and many openings of laptops past. If you will indulge me, I've been feeling nostalgic. This is for the other laptop weirdos out there that that feel the same.

### I have a history of doing terrible acts to laptops

The only image I could find of my NC10 was this blurry, 2021 flip phone photo of me removing the windows sticker.

In 2008, I managed to get my hands on a Samsung NC10 Netbook in a fancy metallic blue color. [^ Back when netbooks where a thing circle 2007-2013] Prior to this I only had desktops. The specs were pretty humble (from wikipedia):

* A single core 1.6 GHz Intel Atom N270
* Integrated Intel GMA 950 graphics
* 1 GB DDR2 RAM
* 10.2 inch 1024x600 screen and aVGA connectorof all things.
* 83-key keyboard rather than the usual 87 or 88 keys on a laptop.
* A 160 GB HDD

Something could be done about that though! You couldupgradethe RAM to a powerful 2GB. You could replace the slow HDD with an SSD. You couldadd a touch screen. You couldmake a Hackintoshout of it if you replaced the wifi card. If you wanted to, you could do those things and I was a weirdo, so I did!

I found a lot of fun in trying to get as much as I could out of that hardware. In fact I'd say the act of doing all that was far more enjoyable than actually using the laptop once the tinkering was done. After the novelty and slowness of a Hackintosh wore off I put Linux on the Netbook. I still sought the thrill of the hunt.

I installed a lite weight distroCrunchBang[^ or just #!] and messed around. I read more about different minimalist distros and came across two others I could hop to: Arch and Gentoo. This feels like an inflection point in my life, I choose to try Arch since I wouldn't have to compile everything on a single core. [^ Who know what would have happened if I picked Gentoo. I might have a beard now.] The screen was small and I wanted to maximize its usefulness so I started trying tiling WMs. Why notXMonad?

It turns out the GMA950 was undervolted on the NC10. Someone made a shareware tool called the GMABooster that could restore the max clock rate. The original websitehttp://www.gmabooster.com/home.htmis long toast and not on wayback. ThisArch forum threadhas details though:

It allows a user, not a manufacturer to choose the desired GMA speed. It combines a sophisticated assembler-level technology and the user-friendly graphic user interface, offering You to near double the GMA core perfomance without even a need to restart a computer..

The package was on AUR so I could squeeze out a little more performance. I could finally watch 480 YouTube videos instead of 360. At some point, long after I had stopped using the netbook, the AUR package became abandoned. Iadopted it as maintainerandmirroredthe binary in GitHub. This was the first time I ever was a package maintainer. [^ I am on a couple random packages in nixpkgs now.] Nowadays the package is memorialized in the theAUR archive.

I had a device that I could repeatedly break and remake. Did I do anything productive or meaningful with it? Absolutely not. Did I learn a lot in the process? I'd say so!

### In the past you could do terrible things to Macbooks too

When I went to College I got a 2011 Macbook Pro. The kind that would overheat and desolder the GPU. [^ Some clever people have found hardware hacks to repair the problemhttps://www.jeffgeerling.com/blog/2017/fixing-2011-macbook-pro-booting-grey-screen-amd-radeon-video-glitch] Mine managed to last a long time and didn't need replacing until 2019. The RAM was not built-in yet on Macbooks. Apple said the model could only support up to 8GB total RAM, but youcould actuallyget 16GB to work. Also, this was back when Macbooks had CD drives. I replaced the my drive with anOther World Computing DIY Optical Drive to HDD Upgrade Kit. [^ And you could put the drive into an "OWC SuperSlim" enclosure to turn it into a USB CD drive.] and installed SSDs in both slots. With two drives I was able to install rEFInd as a boot manager and triple boot:

* OSX as a stable install for my course work
* Windows for games
* Linux so I could break my install repeatedly

I iterated on my Arch install so many times that I started to keep a checklist about my setup process to help me remember everything. Certain stylistic choices were set and still used to this day. [^ This is when I started using Inconsolata for a monospace font and Zenburn for a color scheme.] I couldn't change quite as many things about this laptop, but I still made an effort to change what I could.

### As laptops grew thinner they grew more boring

When it came time for a new laptop I was not looking at Macbook Pros anymore. Apple had made changes, like the touch bar and removing magsafe, that felt like they were targeting a different audience. So instead I had been eyeing a ThinkPad.[^ It's almost cliche to buy one and install Linux.] The prices on the Lenovo store are mostly made up and constantly discounted. My housemate had access to a corpo portal for Lenovo that let me get one at a heavily reduced price. The cost of 3 year service coverage was also discounted so I got some figuring it could help to cover cost of parts if if something failed.

So I bought a Gen 7 X1 Carbon and... I just used it. No mods were possible on this laptop. When I had an SSD failure I asked Lenovo if they could mail me the drive so I could do the install. They said they had to send someone to confirm the issue. So a technician came out and replaced the drive.

### The gift and curse of a free Macbook Pro

Finally in 2023 I waslaid off by HubSpot. Part of severance was the following:

Laptops & WFH Set-Up: Impacted employees may keep their HubSpot laptops (it will be cleaned of any company data remotely), as well as any work from home gear like monitors and keyboards.

Thus a pretty high spec 2021 M1 Max Macbook Pro fell into my lap. I gave my X1 Carbon to a friend to avoid creating yet more ewaste that sits in my closet.

The 2021 version was a bit of return to form: touch bar was gone, magsafe was back, etc. However even theiFixit reviewsaid the "design represents a major move in the right direction" but still only rated the laptop a 4/10 for repairability. [^ The score was eventually updated to a 5/10 when Apple later released a service manual and access to parts.]

I felt some dissonance though. If I was looking to buy a laptop, I wouldn't have picked this one. macOS was getting less enjoyable to use with each update. Likewise the Linux Desktop experience was really coming into its own. [^ By 2023 essentially all my games were playable!] However I felt bad about buying a new laptop when I now had a perfectly good one. So I held onto it and once again, no mods were done or could be done with this laptop.

### Finally buying a Framework 13

I had waited on getting a Framework laptop because I wanted to see them go through a couple iterations. I wanted to see if the promise of repairing, replacing and upgrading actually came true. From what I read it mostly has! [^ People with Framework 15 do seem to be waiting though.]

What changed the decision for me was the following:

* Lugging around a powerful 16 inch laptop was a drag. Having a laptop when traveling is nice if I need to hurriedly rebook something. Mobile sites and apps tend to restrict you in weird ways.
* Despite being a couple years old, the laptop was still worth a lot. People probably want Macbooks for local LLM inference. So I felt pretty good a buyer will actually use the laptop.
* The Framework release a refresh of the 13 with the new AMD chips.

Then I had a friend get Laptop 13 and attest to liking it. That was the last push I needed to finally buy one. Now I can be a laptop weirdo again.

You can't change the RAM on laptops now.You can't change the SSD on laptops now.You can't easily repair the screen on laptops now.

You can do all that and more with a Framework laptop.You can be a laptop weirdo with a Framework laptop.

Weirdo typically has two interpretations:

A possibly dangerous person.A strange, odd, eccentric person.

To both of those I say: all us laptop weirdos can now put asnack drawerin our laptops.You cannot stop us.

### Similar topics

## Setting up my new Framework Laptop 13 DIY Edition with NixOS

Declarative partitioning with Disko, hibernate with LUKS, and Lanzeboote, oh my!



 26 Aug






## Framework 13 DIY Edition Hardware Thoughts

Framework did a really great job with the 13 and I'm excited to do terrible things with the laptop.



 26 Aug
