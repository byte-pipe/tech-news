---
title: Free Software hasn't won
url: https://dorotac.eu/posts/fosswon/
site_name: hackernews_api
fetched_at: '2025-10-13T11:07:19.538848'
original_url: https://dorotac.eu/posts/fosswon/
author: LorenDB
date: '2025-10-12'
description: Free software hasn't won
tags:
- hackernews
- trending
---

This is a translated version of a talk I gave atP.I.W.Oin June, with cleanups and adjustments for the blog form.

# # Free Software hasn't won

…that doesn't sound right. I made the slides inInkscape, on a computer runningKDEand Linux, I useFirefoxregularly. But maybe that's just me. What about you, are you using Free Software? Hands up! [hands go up in the audience] Of course! What nonsense, "Free Software hasn't won". Someone replaced my slides, hey conference staff!

**Staff:** *The other folder.*

[Browsing to a directory named "other folder", opening file called "your slides dimwit.pdf"]

Now, those are finally my slides.

Hello audience, my name is Dorota, and I'm going to talk about how

# # Open Source has won.

And that's not recent, the news has been out in 2008, and has been regularly repeated since by reputable press:ZDNET,Linux Journal,Wired, and so on.

Those press articles list a multitude of examples to prove it.

Linux, Ruby, Red Hat, uh, GitHub? Does that mean I can download GitHub and run it on my own server? Microsoft? Come on, that's some kind of a joke. Those slides are manipulated! So what else do they contain? Oh,this quoteis all right:

> Open source won. It’s not that an enemy has been vanquished or that proprietary software is dead, there’s not much regarding adopting open source to argue about anymore. After more than a decade of the low-cost, lean startup culture successfully developing on open source tools, it’s clearly a legitimate, mainstream option for technology tools and innovation.

Oh, the name of the quoted person is wrong. Looks like an attack on my reputation! Anyways.

The point is, if we want to build something new, using Free Software is not a hindrance. And thats super important, becausesoftware is eating the world. What does it mean? It means software keeps appearing in areas where there used to be no software before. That, in turn, means that we're slowly giving up control over more and more areas of life to those who made the software. After all, their software controls those areas of life from now on.

That's why it's great that there's always an alternative available, that we can select software that is free which grants control to us, and not just its manufacturer. So we have alternateoperating systemsmade withLinux. There areverymanyprogramminglanguagestochoosefrom. We can choose one of theopengames, orgraphicsoraudio creationsoftware without resorting to closed software.

Similarly, we don't need closed software toprint in 3D, or to build amobile computer(also known as smartphone) or asmart watch. There are graphics cards which runcompletely free of closed firmware(Upon asking nouveau devs, they confirmed they wrote some firmware. Nvidia Kepler from 2012 is the last model where free firmware is allowed). There are such bicycles! Pretty much everyone owns one that rides without closed software. There are also sewing machines:

There are comms systems:

There are cars, and have been for a long time:



There are hard drives:

[the slides go blank]

There are wireless headphones, TVs... [slides remain blank] wait, something's wrong. There are phones! [Slides stay mockingly blank, noise of frantic clicking.]

[…]

[…]

[…]

Crap. This isn't right.

Oh, now I get it! The only kind of a phone that grants us openness is an analog phone. That reminds me of the time we were building the aforementioned Librem 5. There was a problem finding the modem for it. The reason is, one company controls the necessary patents necessary to connect to cellular networks. That company can and does impose arbitrary conditions on anyone using their integrated circuits. That made it very difficult to find modems that match our needs, and at the same time any reseller is willing to sell us. The resellers worried that by passing them on to us, they could break some distribution rule and not be able to get any modems in the future.

So that's a no. But I know what will be open for sure.

Richard Stallman started an important project calledGNUin 1983. In one of hisinterviews, as he describes how he started the project, he mentions a certain device that his university bought, but which didn't work very well. He wanted to improve it, but no one wanted to share the device's sources with him. That was an offense! Why wouldn't anyone share the code?

What was that device?

That was a printer. Considering that the GNU project started in 1983 and that the story's from 1981, it works out to over 40 years of fighting for printer freedom. So let's reveal our open alternative.

Oh come on. This cannot be. Have you ever used a printer? If you even manage to find a driver, if you even manage to connect to the printer, then it's still going to print single-sided black-and-white when you asked double-sided color. And despite having to put up with that, Free Software people still haven't gotten frustrated enough to solve the problem once and for all? Unbelievable.

I have a theory. People who say "Open Source has won" are only taking into account a small part of what software is out there. Take a look at this list: it's a map showing which kinds of software force you into running something closed (bold) and which have open options available (italics).

* Applications: *Blender, Firefox, KiCAD* – **Twitter, YouTube**
* Operating System: *GCC, Apache, OpenSSL*
* Kernel: *Linux, Zephyr, FreeRTOS*
* Firmware: *Coreboot* – **modem, GPU**
* Appliances: *Prusa 3D,Airgradient* – **washing machine, TV**

What picture does this paint? Things programmers care about directly, like the OS and the kernel, are quite well covered. Whatever we need, there's an open version. Applications are also more or less fine. There's a Web browser, there's creativity software. The problem appears when you try to participate in social media. Sure, there are alternatives. ButMastodon, orPeerTubeare separate networks from the closed ones, so they won't help much when trying to reach people who aren't yet using them.

Looking at the lower layers, like appliances or firmware, there seem to be options. But those options are limited to a couple niches, and with most things we buy, like a TV or a PC component – sorry, pal, there's simply no choice at all.

## ## All the firmwares in the average laptop

How many processors are there in a typical laptop? By "processor" I mean something that needs its own software. For example, a GPU has its own processor that needs software, or a hard drive, or a keyboard. Here's a diagram of my personal estimate of what separate components need software:

I estimate there are 10 to 15 separate processors on a typical laptop. Just the graphics card may host five of them.

What does that mean for free software? Normally, all that's open – Linux, drivers, applications – all of this is confined to the main CPU. Now imagine you want to use this operating system through some human-friendly interface, like the touch screen or the keyboard. Those are running closed software, so if you want to enter any sort of data on your average laptop, it's game over: you can't make a move without dependence on closed software.

Same story with the graphics card. You won't display anything without closed software. What a fail. Okay, let's ditch keyboards and displays because this is a server. But that's a fail, too: to communicate over a network card, you still need software that it's running and that hasn't been opened. Suppose that we managed to somehow solve this problem. We hit the wall anyway when we try to store data: SSDs as well as HDDs are running their own closed software. I haven't heard of a single case of open software ever running on a storage device!

But that's not even the worst. The peak of lameness isthe processor inside the processor. Have you already heard of Secure Boot? It's a piece of BIOS that is loaded onto the processor inside the main processor before the main operating system. Secure Boot allows the manufacturer choose which software the user can run. A similar system exists on Android phones to lock them to a particular system. Manufacturers of Android-based phones are not shy about restricting what the user can run on their devices.

## ## That runs against user's freedom!

User freedom exists only when theFour Freedoms of Softwareare upheld:

* 0: freedom to run the program for any purpose,
* 1: to study and change it,
* 2: to share copies of it,
* 3: to improve it and share the improvements.

…but those are just words. Who cares about that? This theory is only ever going to be relevant to us computer experts, right?

Except… could it be that you're the family's tech support expert? Does your uncle/mum/grandma come to you carrying their malfunctioning Android phone, hoping for you to make everything right again?

And have you ever disappointed them? Has it already happened that their phone was simply too old and unsupported to be useful any more? Have you already told someone they need to pay up to replace a phone that seems perfectly functional?

Sadly, that's what the Android manufacturersupporttimelinessay: typically after 4, exceptionally after 8 years, they will no longer release security updates. That makes devices too insecure to use, and turns them into e-waste.

What does Free Software have to do with it? I don't know, but my Lenovo laptop, 13 years since release of the hardware, the operating system is still receiving regular security updates. I suspect this has something to do with the lack of a boot loader lock and the openness of all the drivers. That's unlike Android. Even if there's no explicit lock, the drivers are so rarely open that the community rarely has the manpower to create a custom ROM for a given device.

## ## Rug pulls

The couple hundred bucks that your aunt might need to pony up to get a new phone pale in comparison to how much you need to pay for some cloud-only devices. Some cloud-enabled gadgets don't let the user choose an alternative provider for services the device requires. What happens when the companyshuts downtheonline service? Of course, the devicebecomes an expensive brick. Imagine someone setting your 2300 bucks on fire just like that.

That's still nothing compared to what some other people have to deal with. Imagine you're a farmer, and your harvest is on the field, ready to get cut and brought in. T here's a storm brewing, so you jump into the combine harvester, and start the work. Oh no! The machine broke down! Not to worry, you're a resourceful farmer and you have the necessary spare part. You install it and start the machine, except… it tells you: "Unauthorized component. Please contact customer service". Now you're in real trouble because it could take9 monthsfor the customer service to solve the problem. You can't harvest the food worth tens of thousands of dollars, you're that much in the red. Game over, your farm is bankrupt. But that's not the end of the world, is it?

This is what a pacemaker looks like. Why would I mention those in a talk about software freedom? You see, a pacemaker is a complex device which must examine and diagnose the patient continuously, in real time, in order to perform its function. Its task is to detect a dangerous condition and perform a medical procedure in response to it. It needs software to do this complicated task. But if the device isn't perfect at diagnosing, that's a big problem. I'm not a medical expert, but getting your heart shocked when it's not necessary sounds dangerous in its own right. When it runs closed software that does not grant us the freedom to modify it, we have to resort to begging the manufacturer to fix it. And when we get no freedom to study it, we can't even avoid the circumstances that make it misfire!

But don't take my word for it. I only know of this problem because ofKaren Sandler, whoseinvolvement with Free Softwareis intertwined with this problem since the beginning.

The bottom line is, if we have people who have no other choice but to trust their own body to apiece of closed software and a single manufacturer, how could we possibly say that Open Source had won?

## ## Appliances and copyleft

Are you responsible for building an appliance? I bet you're using Open Source software in it, aren't you? Then licenses like the MIT require you to include a notice about the authors of the source code together with the software you distribute. There's a wholegalleryof those on the curl website, ranging from cars to food processors. Are you feeling proud for releasing a device with Free Software in it? Not so quick! Can the user of your device study and modify the software you gave them? Have you actually granted them the Four Freedoms?

Permissive licenseslike the MIT license are Free Software, so they let you do all that the Four Freedoms promise. But they also allow you to do another thing: to close the software again by never granting those freedoms regarding your own modifications. If that's what happened, then freedom for me, not for thee. You, the manufacturer, reaped the benefits, the user can't, sucks to be the user.

The responsibility to prevent this falls on us, computer experts. When we create software, we have the choice of license we want to release it under. And we should be using what's called "copyleft": it's a term that applies to licenses which prevent code once released under that license from being closed again. The most widespread copyleft license is theGnu General Public License(GPL), and I recommend that you all use that one.

## ## Licenses and more

Licenses are not the only thing relevant for Free Software. There are other things to fight:

* patents, like in the case of cellular modems,
* hardware locks, like Android's,
* project management.

As for the last point, recently Google gavean amazing exampleby restricting access to sources in development to select manufacturers. Everyone else will not get continuous updates, but only once per major release. This illustrates how much influence over the practical usability of a project management decisions have. This is not a change in licensing, and it's also not a technical change, so it's not immediately visible under those lenses.

Instead, it's a consequence of who's in charge. In this case, it's not a community who controls the Android project, but a for-profit corporation. At the same time, it's regular people who are on the user side of the project. Is it any wonder that the goals of a corporation and those of regular people differ? Is it any wonder that the corporation is making changes that suit it even when they don't suit the community of users? When those are the conditions under which a project is developed, it can have deep consequences, even on an architectural level.

TakeDebianas a point of comparison. The first statement on the web page already says "Debian is a Community of People!". The software is being developed and used by the same people. They won't make it harder to use. They provide a complete operating system, publish all the sources, andpurge anything that isn't open enough. On the other hand, Android has long beenreplacingopen components by closed ones, making AOSP (the open part of android) all butunuseable on its own.

## ## Why?

I suspect this situation has something to do with how computers and appliances have been developed historically. Computers have their roots in academia. When they were sold, they were always advertised as blank slates, general purpose devices, as opportunities to do what you choose to do with them. Not so much for appliances. Those have always had a single purpose. Except they kept getting complicated, until they entered a level of complexity where they needed to incorporate computers in order to perform their function. But they kept being manufactured as appliances, with only a handful of people being expected or allowed to exercise control over them. Incorporating computers didn't change the culture around them.

This is just a guess and I don't know how correct it is. For example Apple was always a computer manufacturer, but they are making computers now as if those were appliances.

## ## What now?

The responsibility is ours – computer nerds' – to make Free Software win. When we build a hardware device, we must publish the firmware sources. We must publish technical documentation – it often so happens that the device documentation needed to make open firmware is missing or incomplete (another war story from the Librem 5, camera sensors this time).

As users, or institutional customers, we should demand that the manufacturer provides open sources for any firmware they are shipping with their devices.

But there's one more way: political pressure. I expect this to be a more effective method than individual action. After all, EU managed to convince phone manufacturers tostandardize on USB-C ports for charging, as well as toextend the warranty period. Perhaps they could also force computer manufacturers to not install boot loader locks. It would fit nicely into theInformation Society Directive. It says things like:

> Member States must provide legal protection against any person knowingly performing without authority any of the following acts:

* > the removal or alteration of any electronic rights-management information;

…oh. So instead of jailing people who put locks on devices they no longer own, it enforces the jailing of those who remove them from their own devices. Great.

Dear European Comission, please always have someone with a clue in the room who can explain the consequences of your ideas in a way you can understand. You can do it, already did a couple times, like above. But work on consistency, okay? Pinky promise?

Here are some people with a clue:Free Software Foundation Europewith theirPublic Money Public Codeopen letter, theRight to Repairmovement, as well as theEuropean Pirate Party.

I recommend anyone who cares to join forces with them. But if you don't want to engage politically, there are also financial way of support. And I don't even mean (although I do encourage) donating. I mean supporting Free Software friendly manufacturers! Buy the Librem 5 fromPurism, or a 3D printer fromPrusa, or a smartwatch runningEspruino. You see, it's expensive to manufacture any sort of hardware. It doesn't help that the markets are already saturated with closed products. Even if open source, hackable products are superior, it will take people at large a long time to realize that this is a superpower. Free Software thrived in culture of repair and modification. But this culture has been suffocated in the wider society with closed, throwaway items, so few people recognize its benefits. That unsustainable crowding out makes another obstacle for Open Source friendly products in the current markets.

There's a noble exception here. What makes it even more unusual is that it comes from Google. It's Chromebooks. Google has a set of requirements that all Chromebook manufacturers must fulfill, and one of them is having a completely open BIOS, together with the Embedded Controller firmware. All Chromebooks I'm aware of run Coreboot. They still contain some closed software, notably the RAM startup software, which, I believe, is present in all laptops, but! ARM-base Chromebooks are able to run with a completely open BIOS apart from that. So if anyone wants to take care of this together with me, I have thisNLNet projectto make it as easy as possible to run regular, mainline Linux on them. So please, contact me, if you're that person.

## ## The world

A short quiz: how many devices can you count around you which contain processors?

Some hints: TV, camera, toothbrush, oscilloscope, e-book reader, radio receiver, dishwasher, router, washing machine, vacuum cleaner, bathroom scales.

Now think wider. When I went to the supermarket, the vegetable section had a scales that printed labels with barcodes. They were equipped with touch screens. You bet there's a processor and a load of firmware in those. But shops are chock-full of processors in my part of the world. There are thousands of price labels in each of those stores, and they are all e-paper screens. I'm fairly sure you need software to drive those and receive wireless updates.

Keep going and you might realize that the software running in your car allowsremote control. Orin your train. That snafu wouldn't have occured if the railways had access to sources of the train software.

What about other business uses? Car diagnostic stations? Medical equipment? Accounting software?

Software is really eating the world, and it's closed software which is *everywhere* around us, without free options. What's the regular person's role in this? They give up control over entire areas of their lives to others, others who often can't be supervised or replaced.

You know, we messed up. There's no other way to put it. We even let closed software sneak into our own home field: computers. Sure, the interfaces are open. There's SATA, there's PCI. We can swap parts if we want to, we can run Linux there, all is fine. Except it's not, because peripherals are as important as the core, and we, software people, lost control of the peripherals of our darlings already.

## ## Wasted potential

In theory, it's possible that someone opens a piece of software regardless of the wishes of the original authors. The whole game modding scene is about that. Here's an example of someone running Tetris on a pocket camera:

ZX3 running Tetris with hacked firmware

But going against the manufacturer is just wasted work. Imagine the difference between hacking it in and modifying the official sources. The potential, things we could achieve if we didn't have to break doors that are open! So here's a silly example: I have an action camera. Due to somestupid law, the camera breaks off every recording as soon as it reaches the 30 minutes mark. Now I have 20 years of coding experience. Having source code, I could have fixed the problem and went on with my life. Another example, another camera: I am making a time lapse from my window. Every day at 10:00, I take a picture from a camera that just sits there. But this camera has no time lapse feature, so I must go there in person every time. Why can't I fix this? Of course, no source code.

## ## Epilogue

There's now anew printerproject that advertises itself as open source. But if you look at the details, it's actually not. Instead, it uses asource-available licensewhich does not grant you Freedom 0 – you must not use the sources for commercial purposes. Better than nothing, I guess.

Comments
