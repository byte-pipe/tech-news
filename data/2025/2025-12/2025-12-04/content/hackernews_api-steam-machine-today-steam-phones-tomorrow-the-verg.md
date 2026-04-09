---
title: Steam Machine today, Steam Phones tomorrow | The Verge
url: https://www.theverge.com/report/820656/valve-interview-arm-gaming-steamos-pierre-loup-griffais
site_name: hackernews_api
fetched_at: '2025-12-04T19:09:41.557131'
original_url: https://www.theverge.com/report/820656/valve-interview-arm-gaming-steamos-pierre-loup-griffais
author: Sean Hollister
date: '2025-12-02'
published_date: '2025-12-02T19:42:08+00:00'
description: Valve tells The Verge it’s funding Fex, a key technology that’s letting Arm devices like phones play Windows games.
tags:
- hackernews
- trending
---

* Report
* Interview

# Steam Machine today, Steam Phones tomorrow

In an exclusive interview, Valve reveals it’s the architect behind a push to bring Windows games to Arm.

by


Sean Hollister
Dec 2, 2025, 7:42 PM UTC
* Link
* Share
The Steam Controller.

| Photo by Everything Time Studio / The Verge
* Report
* Interview

# Steam Machine today, Steam Phones tomorrow

In an exclusive interview, Valve reveals it’s the architect behind a push to bring Windows games to Arm.

by


Sean Hollister
Dec 2, 2025, 7:42 PM UTC
* Link
* Share
Sean Hollister

is a senior editor and founding member of The Verge who covers gadgets, games, and toys. He spent 15 years editing the likes of CNET, Gizmodo, and Engadget.

It’s a big deal thatValve is making a game console. But I’m beginning to think the Steam Machine may end up a footnote in gaming history. What if Valve could bring PC games not just to its own living room consoles, but also to the Arm chips that billions of people have in their phones? What if you no longer had to wait for game developers to do the hard work of porting PC games to your phone, Mac, or other Arm hardware, because games built for desktop PCs could just work?

If you wrote offthe Steam Frameas yet another VR headset few will want to wear, I guarantee you’re not alone. But the Steam Frame isn’t just a headset; it’s a Trojan horse that contains the tech gamers need to play Steam games on the next Samsung Galaxy, the next Google Pixel, perhapsArm gaming notebooksto come.

I know, because I’m already using that tech onmySamsung Galaxy. There is no official Android version ofHollow Knight: Silksong, one of the best games of 2025, but thatdoesn’t have to stop you anymore. Thanks to a stack of open-source technologies, including a compatibility layer called Proton and an emulator called Fex, games that were developed for x86-based Windows PCs can now run on Linux-based phones with the Arm processor architecture. With Proton, the Steam Deck could already do the Windows-to-Linux part; now, Fex is bridging x86 and Arm, too.

This stack is what powers the Steam Frame’s own ability to play Windows games, of course, and it was widely reported that Valve is using theopen-source Fex emulatorto make it happen.

What wasn’t widely reported: Valve is behind Fex itself.

In an interview, Valve’s Pierre-Loup Griffais, one of the architects behind SteamOS and the Steam Deck, tellsThe Vergethat Valve has been quietly funding almost all the open-source technologies required to play Windows games on Arm. And because they’re open-source, Valve is effectively shepherding a future where Arm phones, laptops, and desktops could freely do the same. He says the company believes game developers shouldn’t be wasting time porting games if there’s a better way.

Remember when the Steam Deck handheld showed that a decade of investment in Linux could make Windows gaming portable? Valve paidopen-source developers to follow their passionsto help achieve that result. Valve has been guiding the effort to bring games to Arm in much the same way: In 2016 and 2017, Griffais tells me, the company began recruiting and funding open-source developers to bring Windows games to Arm chips.

Fex lead developer Ryan Houdek tellsThe Vergehe chatted with Griffais himself at conferences those years and whipped up the first prototype in 2018. He tells me Valve pays enough that Fex is his full-time job. “I want to thank the people from Valve for being here from the start and allowing me to kickstart this project,” herecently wrote.

### Related

* Gabe Newell on closed and open systems in 2013: “we try to take the pieces where we’re going to add the best value and then encourage other people to do it.”

I didn’t realize it at the time, butwhen I showed offSilksongon my Samsung Galaxy S25using the GameHub app, I was running it on Fex, and Proton, and other Valve-backed open-source tech. Even if Valve never makes a Steam Phone, developers can take the tech and run.

So: Why Arm, how does any of this work, andmightValve make that Steam Phone? I asked Griffais, and here’s what he said — edited for brevity and clarity.

The Verge: Why Arm?

Pierre-Loup Griffais:In 2016, 2017, there was always an idea we would end up wanting to do that, and that’s when the Fex compatibility layer was started, because we knew there was close to a decade of work needed before it would be robust enough people could rely on it for their libraries. There’s a lot of work that went into that.

It all started with the same assumption that you’re going to get the same experience on Arm, you’re going to have the same set of games, and you’re going to be able to run them without having to worry about what architecture your computer is using. That was really our goal, to try to reduce barriers for users not having to worry about what games run and for developers to get a starting point for those new devices.

Because there’s a lot of price points and power consumption points where Arm-based chipsets are doing a better job of serving the market. When you get into lower power, anything lower than Steam Deck, I think you’ll find that there’s an Arm chip that maybe is competitive with x86 offerings in that segment.

We’re pretty excited to be able to expand PC gaming to include all those options instead of being arbitrarily restricted to a subset of the market.

When you say “include all those options,” you’re thinking there’ll be other Arm SteamOS devices, too?

Yeah, and I’m excited about that. I think that it paves the way for a bunch of different, maybe ultraportables, maybe more powerful laptops being Arm-based and using different offerings in that segment. Handhelds, there’s a lot of potential for Arm, of course, and one might see desktop chips as well at some point in the Arm world.

Desktops are not completely out of the question: Designs like, say,the Framework Desktopuse essentially a big SOC, right? And those big SOCs have existed in the Arm world for a while. Apple’s making very good-qualityexamples of that, so it’s not too crazy to imagine something like that in the PC space at some point.

When and how are you attracting companies to build those other kinds of devices?

I don’t think there’s a specific plan there. I think the first step is for us to ship what we have, and it will maybe show the way. Then it’s all based on the conversations we have after that.

If there are good opportunities, they will be made easier and easier over time because we’ll keep building the hardware support, we’ll keep greasing the wheels, so to speak, so that SteamOS can work on a wider variety of Arm devices, but also so that the catalog becomes more reliable there in terms of compatibility and performance.

We might have people reaching out, or we might reach out based on what we’re seeing OEMs build. Maybe they’ll build something with a different OS that we think would be a good fit with SteamOS or vice versa. In the handheld space, some collaborations were us reaching out, some were OEMs reaching out to us.

We’re seeing the same thing right now in the living room, where we’ve already had some good conversations with folks in the living room space that think SteamOS could be a good fit. As we work on SteamOS for Steam Machine, that’s closer to becoming a reality. We’re excited to partner with folks after that. I think the same will happen for SteamOS for Arm.

Is the Arm version of SteamOS a separate operating system?

It’s the same exact OS components, the same exact Arch Linux base, all the same updater, all the same technologies. Depending on form factors, you might have different pieces of software that you want to be running or not running — some of them make more sense on a handheld, some more sense on a headset, some in desktop form factor, but all of those options are always available and part of the core OS.

So when you’re looking at SteamOS on Arm, you’re really looking at the same thing. Instead of downloading the normal Proton that’s built for x86 and targets x86 games, it will also be able to download a Proton that’s Arm-aware, that has a bulk of its code compiled for Arm and can also include the Fex emulator.

Can you break down those layers for us? When I’m playing a Windows game on my Steam Deck, how does that work?

If you’re playing that game on your Steam Deck, you’re going to be playing it through Proton, which is essentially a distributionof Wine, bundled with everything you would need to run any sort of game made for Windows.

The game itself is a Windows executable, right? At a core level, the Linux operating system does not even know how to load the program, and so, instead of invoking it through the OS, you invoke it through Proton, which is going to do the first step of setting up the address space, loading the segments of code into memory. The code coming from the app is all x86, and so Proton is a facilitator. It puts the existing code of the app in a format and a layout that the Linux OS can understand and then starts executing that code.

Whenever that game code makes an API call for something it was built against in its original development environment, either just a core C runtime library or higher-level APIs like DirectX or DirectSound, or USB enumeration or input — whenever the game calls those functions, those functions exist in Proton’s code, and it’s going to be Proton implementing that and giving you results. Or giving the game a result based on the Linux OS, as opposed to the other environment that the game was designed for. So it’s just an alternate implementation for all those APIs.

At the end of the day, the code of the game is not changed, right? It’s the same code that’s loaded into memory and executed natively by the CPU.

How is Wine different from Proton?

It’s really the same thing. Proton includes Wine, and the bulk of development that’s happening Wine is actually driven by Proton; it’s all the same set of developers. But there’s a branch of Wine that is Wine plus a bunch of experimental gaming-focused stuff. That is what we’re currently working on at the moment, and when it gets tested enough, it’s no longer experimental and goes into Wine proper and then everyone has it.

Proton is just a preview of the latest and greatest Wine. Its goal is to provide the best game compatibility, so all the APIs the game might run are well supported and offered with good performance and has all the gaming stuff configured for you. It includes those extra layers like DXVK, which is a D3D11 driver that’s translating to Vulkan, and VKD3D, which is a D3D12 layer that translates to Vulkan as well. There’s also built-in support in Wine that targets OpenGL.

Proton is targeted towards the Steam runtime, so it’s using all the libraries that are provided by Steam, so you don’t need to install any extra components in your OS, and it’s also integrated with Steam and games in general to manage save data and so Steam can find games for cloud save purposes.

How does all of this change when we’re running Windows games on Arm?

First there’s an intermediate step. Anytime you’re setting up code segments, Wine is now going to try and see if it’s x86 or Arm code, because some Windows apps are targeted towards Arm or might include mixed segments, or a DLL might bundle both Arm and x86 code. If there’s x86 code, it will put it in the right spot with enough functionality to jump in and out of the Fex emulator.

The Fex emulator’s sole purpose is to provide compatibility with x86. So it takes the x86 code, and uses a just-in-time translator to emit Arm code that does the exact same thing. Proton built for Arm support will make sure that whenever it’s setting up code segments, any code segment that’s x86 will properly jump into Fex so it can be run through Fex instead of the native CPU.

All the game code is translated by Fex, so it has a bit of work to do. But when the game jumps into an API call, like, say, issuing a draw call to the graphics driver through the Vulkan or D3D12 API, it will immediately jump into Arm-native code. Because you’re running Arm-native code built as part of Proton, the area you have to emulate is only the code that’s owned by the game itself. So the performance hit of any emulation stops as soon as you cross that API boundary between Windows and Linux.

How does this compare to other Windows-on-Arm emulation, likePrism for Windows on Arm?

I don’t really know how the Windows one works and what its priorities are, so I’m not the best person to talk about that. I think what I would say about Fex is, it was designed for being able to attain the best performance possible for gaming stuff in a way that also guarantees the best correctness.

Some games do tricky things with a CPU when they’re trying to do anti-tamper and things like that, and so by making sure that we implement the emulation with 100 percent correctness, I think we have good support for that.

You’ve told me Valve is really funding a lot of this Proton development, this Wine development, and I’ve heard that the same thing is happening with Fex. How long has Valve supported Fex and to what degree?

That’s right, all the core developers have been funded by us since the beginning. We definitely started that project with the idea that it would be something that’s useful for the ecosystem at large, but also something that would be really useful for SteamOS and other applications in the future.

We identified that Arm compatibility was going to be really important so that folks can enjoy those new options in the market without having a whole bootstrapping problem of “where are the games going to come from.” The last thing that we want, and that’s been our philosophy since forever, is we don’t want game developers to have to spend a bunch of time porting things to different architecture if they can avoid it.

We would way rather have those game developers invest their time and energy into making their games better, or working on their next game. We think that porting work is essentially wasted work when it comes to the value of the library.

Valve started Fex?

Proton is also something where you could say we started it, but because it’s a derivative of Wine, it’s less clear-cut. Whereas Fex, we were talking with a few developers that we knew were the right fit for an undertaking like that, a long-term thing that needed a very specific set of experts. We worked hard on trying to convince these guys to start the project, and have been funding them ever since.

The Steam Frameruns Android apps, but it’s not Android running on the headset. How?

It’s a similar compatibility layer as Proton, just targeted at Android. There’s not a whole Android API and implementation there, just a subset mostly targeted towards games, providing the right libraries on our side, so that things typically contained in an Android executable can run. They’re already targeting Arm, so you don’t need to do emulation on the code that’s contained there. You just need to set up the libraries and executable in such a way that it can run in the first place.

Will there be SteamOS phones? Will you bring non-gaming apps into the store in a big way?

We have done things around phones withthe Steam Link app. I don’t know if that’s going to be a big focus for us to develop local content or try to develop SteamOS for devices like that. I mean, I’m not discounting any possibility, but I think with just living room, handheld, and desktop, trying to have a good outcome for gaming applications and everything else you’d want to do in a desktop, we have a ton of work to do.

Is Arm the future of handheld gaming, or is it just something for headsets?

I don’t know. I think Arm devices are definitely a good fit for lower performance, like anything lower than Steam Deck. But it’s possible it’ll be a good option for something on the order of the Steam Deck performance envelope. We don’t really try to steer the market one direction or another; we just want to make sure that good options are always supported.

Follow topics and authors
 from this story to see more like this in your personalized homepage feed and to receive email updates.
* Sean Hollister
* Interview
* Report

## More in:Steam Machines have returned: all the news about Valve’s new hardware universe

Valve’s Android compatibility layer now has its official name, Lepton, and a cute frog logo.
Stevie Bonifield
Dec 3
Valve signals it won’t subsidize the Steam Machine.
Sean Hollister
Nov 25
Here come the third-party Steam Machine accessories.
Cameron Faulkner
Nov 19

## Most Popular

Most Popular
1. Crucial is shutting down — because Micron wants to sell its RAM and SSDs to AI companies instead
2. Steam Machine today, Steam Phones tomorrow
3. Apple’s head of UI design is leaving for Meta
4. Antigravity’s 360-degree drone is here to help you forget DJI
5. BMW iX3 first drive: a ‘New Class’ is in session

## The Verge Daily

A free daily digest of the news that matters most.

Email (required)
Sign Up
By submitting your email, you agree to our

Terms
 and
Privacy Notice
.
This site is protected by reCAPTCHA and the Google

Privacy Policy

and

Terms of Service

apply.
Advertiser Content From

This is the title for the native ad

## More inReport

AI chatbots can be wooed into crimes with poetry
The future of country music is here, and it’s AI
Anyone can try to edit Grokipedia 0.2 but Grok is running the show
An unsettling indie game about horses keeps getting banned from stores
A leading kids safety bill has been poison pilled, supporters say
Sony is slowly improving the ergonomics of its cameras, but it’s still not enough
AI chatbots can be wooed into crimes with poetry
Robert Hart
Two hours ago
The future of country music is here, and it’s AI
Charlie Harding
12:00 PM UTC
Anyone can try to edit Grokipedia 0.2 but Grok is running the show
Robert Hart
Dec 3
An unsettling indie game about horses keeps getting banned from stores
Ash Parrish
Dec 3
A leading kids safety bill has been poison pilled, supporters say
Lauren Feiner
Dec 3
Sony is slowly improving the ergonomics of its cameras, but it’s still not enough
Antonio G. Di Benedetto
Dec 3
Advertiser Content From

This is the title for the native ad

## Top Stories

12:00 PM UTC
The future of country music is here, and it’s AI
3:00 PM UTC
Anthropic’s quest to study the negative effects of AI is under pressure
﻿
Video
Dec 3
BMW iX3 first drive: a ‘New Class’ is in session
Dec 3
One day, AI might be better than you at surfing the web. That day isn’t today.
Dec 3
Crucial is shutting down — because Micron wants to sell its RAM and SSDs to AI companies instead
Two hours ago
AI chatbots can be wooed into crimes with poetry
