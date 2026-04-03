---
title: NVIDIA is full of shit - Sebin's Blog
url: https://blog.sebin-nyshkim.net/posts/nvidia-is-full-of-shit/
site_name: lobsters
fetched_at: '2025-07-05T23:06:50.206454'
original_url: https://blog.sebin-nyshkim.net/posts/nvidia-is-full-of-shit/
author: Sebin Nyshkim
date: '2025-07-05'
description: 'Since the disastrous launch of the RTX 50 series, NVIDIA has been unable to escape negative headlines: scalper bots are snatching GPUs away from consumers before official sales even begin, power connectors continue to melt, with no fix in sight, marketing is becoming increasingly deceptive, GPUs are missing processing units when they leave the factory, and the drivers, for which NVIDIA has always been praised, are currently falling apart. And to top it all off, NVIDIA is becoming increasingly insistent that media push a certain narrative when reporting on their hardware.'
tags: hardware, rant
---

Since the disastrous launch of the RTX 50 series, NVIDIA has been unable to escape negative headlines: scalper bots are snatching GPUs away from consumers before official sales even begin, power connectors continue to melt, with no fix in sight, marketing is becoming increasingly deceptive, GPUs are missing processing units when they leave the factory, and the drivers, for which NVIDIA has always been praised, are currently falling apart. And to top it all off, NVIDIA is becoming increasingly insistent that media push a certain narrative when reporting on their hardware.

## What’s an MSRP anyway?

Just like with every other GPU launch in recent memory, this one has also been ripe with scalper bots snatching up stock before any real person could get any for themselves. Retailers have reported that they’ve receivedvery little stock to begin with. This in turn sparked rumors about NVIDIA purposefully keeping stock low to make it look like the cards are in high demand to drive prices. And sure enough, on secondary markets, the cards goway aboveMSRP and some retailers have started tobundle the cards with other inventory(PSUs, monitors, keyboards and mice, etc.) to inflate the price even further and get rid of stuff in their warehouse people wouldn’t buy otherwise—and you don’t even get a working computer out of spending over twice as much as a GPU alone would cost you.

Newegg selling the ASUS ROG Astral GeForce RTX 5090 for $3,359 (MSRP: $1,999)
eBay Germany offering the same ASUS ROG Astral RTX 5090 for €3,349,95 (MSRP: €2,229)

I had a look at GPU prices for previous generation models for both AMD and NVIDIA as recently as May 2025 and I wasn’t surprised to find even RTX 40 series are still very much overpriced, with the GeForce RTX 4070 (lower mid-tier) starting at $800 (MSRP: $599), whereas the same money can get you a Radeon RX 7900 XT (the second best GPU in AMD’s last generation lineup). The discrepancy in bang for buck couldn’t be more jarring. And that’s before considering that NVIDIA gave out defective chips to board partners that weremissing ROPs(Raster Operations Pipelines) from the factory, thus reducing their performance. Or, how NVIDIA put it in a statement toThe Verge:

We have identified a rare issue affecting less than 0.5% (half a percent) of GeForce RTX 5090 / 5090D and 5070 Ti GPUs which have one fewer ROP than specified. The average graphical performance impact is 4%, with no impact on AI and Compute workloads. Affected consumers can contact the board manufacturer for a replacement. The production anomaly has been corrected.

Those 4% can make an RTX 5070 Ti perform at the levels of an RTX 4070 Ti Super, completely eradicating the reason you’d get an RTX 5070 Ti in the first place. Not to mention that the generational performance uplift over the RTX 40 series was already received quite poorly in general. NVIDIA also had to later amend their statement to The Verge and admit the RTX 5080 was also missing ROPs.

It’s adding insult to injury with the cards’ generalunobtainiumand it becomes even more ridiculous when you compare NVIDIA to another trillion dollar company that is also in the business of selling hardware to consumers: Apple.

How is it that one can supply customers with enough stock on launch consistently for decades, and the other can’t? The only reason I can think of is, that NVIDIA just doesn’t care. They’re making the big bucks with data center GPUs now, selling the shovels that drive the “AI” bullshit gold rush, to the point that selling to consumers isincreasingly becominga rounding error on their balance sheets.

## These cards are 🔥🔥🔥 (and not the good kind)

The RTX 50 series are the second generation of NVIDIA cards to use the 12VHPWR connector. The RTX 40 series became infamous as the GPU series with melting power connectors. So did they fix that?

No. The cables can still melt, both on the GPU and PSU. It’s a design flaw in the board of the GPU itself which cannot be fixed unless the circuitry of the cards is replaced with a new design.

With the RTX 30 cards, each power input (i.e. the cables from the power supply) had its own shunt resistor[1]. If one pin in a power input had not been connected properly, another pin would have had to take over in its stead. If both pins were not carrying any current, there would have been no phase on the shunt resistor and the card would not have started up. You’d get a black screen, but the hardware would still be fine.

NVIDIA, in its infinite wisdom, changed this design starting with the RTX 40 series.

Instead of individual shunt resistors for each power input, the shunt resistors are now connected in parallel to all pins of the power input from a single 12VHPWR connector. Additionally, the lines are recombined behind the resistors. This mind-boggling design flaw makes it impossible for the card to detect if pins are unevenly loaded, since as much as the card is concerned, everything comes in through the same single line.

Connecting the shunt resistors in parallel also makes them pretty much useless since if one fails, the other will still have a phase and the card will happily keep drawing power and not be any the wiser. If the card is supplied with 100W on each pin and 5 of the 6 pins don’t supply a current, then a single pin has to supply the entire 600W the card demands. No wire is designed for this amount of power draw. As a result, excessive friction occurs from too many electrons traveling through the cable all at once and it melts (see:Joule heating).

NVIDIA realized that the design around the shunt resistors in the RTX 40 series was kinda stupid, so they revised it: by eliminating the redundant shunt resistor, but changing nothing else about the flawed design.

There’s something to be said about the fact NVIDIA introduced the 12VHPWR connector to the ATX standard to allow for only a single connector to supply their cards with up to 600W of power but making it way less safe to operate at these loads. Worse yet, NVIDIA says the four “sensing pins” on top of the load bearing 12 pins aresupposedto prevent the GPU from pulling too much power. The fact of the matter is, however, that the “sensing pins” only tell the GPU how much it’s allowed to pull when the systemturns on, but theydo notcontinuously monitor the power draw—that would be for the shunt resistors on the GPU board, which we established, NVIDIA kept taking out.

If I had to guess, NVIDIA must’ve beenvery confidentthat the “sensing pins” are a suitable substitution for those shunt resistors in theory, but practice showed that they were not at all accounting for user error. That was their main excuse after after it blew up in their face and they investigated. And indeed, if the 12VHPWR connector isn’t properly inserted, pins could not make proper contact, causing the remaining wires to carry more load. This is something that the “sensing pins”cannotdetect, despite their name and NVIDIA selling it as some sort of safety measure.

Size comparison between the RTX 5090 FE (right) and its predecessor, the RTX 4090 FE (left) ©
ZMASLO
 (
CC BY 3.0
) via
Wikimedia

NVIDIA also clearly did not factor in the computer cases on the market that people would pair these cards with. The RTX 4090 wasmassive,a real heccin chonker. It was so huge in fact, that it kicked off the trend of needingsupport bracketsto keep the GPU from sagging and straining the PCIe slot. It also had its power connector sticking out to the side of the card and computer cases were not providing enough clearance to not bend the plug. As wasclarifiedafter the first reports of molten cables came up, bending a 12VHPWR cable without at least 35mm (1.38in) clearance could loosen the connection of the pins and create the problem of the melting connectors—something that wasn’t a problem with the battle tested 6- and 8-pin PCIe connectors we’ve been using up to this point[2].

Board partners like ASUS try to work around that design flaw by introducing intermediate shunt resistors for each individual load bearing pin before the ones according to NVIDIA’s designs, but these don’t solve the underlying issue, that the card won’t shut itself down if any of the lines aren’t drawing enough or any power. What you get at most is an indicator LED lighting up and some software telling you “Hey, uh, something seems off, maybe take a look?”

The fact NVIDIA insists on keeping the 12VHPWR connector around and not do jack shit about the design flaws in their cards to prevent it from destroying itself from the slightest misuse should deter you from considering any card from them that uses it.

## A carefully constructed moat

Over the years NVIDIA has released a number of proprietary technologies to market that only work on their hardware—DLSS, CUDA, NVENC and G-Sync to just name a few. The tight coupling with with NVIDIA’s hardware guarantees compatibility and performance.

However, this comes at a considerable price these days, as mentioned earlier. If you’re thinking about an upgrade you’re either looking at a down-payment on a house or an uprooting of your entire hardware and software stack if you switch vendors.

If you’re a creator, CUDA and NVENC are pretty much indispensable, or editing and exporting videos in Adobe Premiere or DaVinci Resolve will take you a lot longer[3]. Same for live streaming, as using NVENC in OBS offloads video rendering to the GPU for smooth frame rates while streaming high-quality video.

Speaking of games: G-Sync in gaming monitors also requires a lock-in with NVIDIA hardware, both on the GPU side and the monitor itself. G-Sync monitors have a special chip inside that NVIDIA GPUs can talk to in order to align frame timings. This chip is expensive and monitor manufacturers have to get certified by NVIDIA. Therefore monitor manufacturers charge a premium for such monitors.

The competing open standard is FreeSync, spearheaded by AMD. Since 2019, NVIDIA also supports FreeSync, but under their “G-Sync Compatible” branding. Personally, I wouldn’t bother with G-Sync when a competing, open standard exists and differences are negligible[4].

### NVIDIA giveth, NVIDIA taketh away

The PC, as gaming platform, has long been held in high regards for its backwards compatibility. With the RTX 50 series, NVIDIA broke that going forward.

PhysX, which NVIDIA introduced into their GPU lineup with the acquisition of Ageia in 2008, is a technology that allows a game to calculate game world physics on an NVIDIA GPU. After the launch of the RTX 50 series cards it was revealed that they lack support for the 32-bit variant of the tech. This causes games like Mirror’s Edge (2009) and Borderlands 2 (2012) that still run on today’s computers to take ungodly dips into single digit frame rates, because the physics calculations are forcibly performed on the CPU instead of the GPU[5].

Even though the first 64-bit consumer CPUs hit the market as early as 2003 (AMD Opteron, Athlon 64), 32-bit games were still very common around these times, as Microsoft would not release 64-bit versions of Windows to consumers until Vista in 2006[6]. NVIDIA later released the source code for the GPU simulation kernel onGitHub. The pessimist in me thinks they did this because they can’t be bothered to maintain this themselves and offload that maintenance burden to the public.

### DLSS is, and always was, snake oil

Back in 2018 when the RTX 20 series launched as the first GPUs with hardware accelerated ray tracing, it sure was impressive and novel to have this tech in consumer graphics cards. However, NVIDIA also introduced upscaling tech alongside it to counterbalance the insane computational expense it introduced. From the beginning, the two were closely interlinked. If you wanted ray tracing in Cyberpunk 2077 (the only game at the time that really made use of the tech), you also had to enable upscaling if you didn’t want your gameplay experience to become a (ridiculously pretty) PowerPoint slide show.

That upscaling tech is the now ubiquitous DLSS, orDeep Learning Super Sampling[7]. It renders a game at a lower resolution internally and then upscales it to the target resolution with specialized accelerator chips on the GPU die. The only issue back then was that because the tech was so new, barely any game made use of it.

What always rubbed me the wrong way about how DLSS was marketed is that it wasn’t only for the less powerful GPUs in NVIDIA’s line-up. No, it was marketed for the top of the line $1,000+ RTX 20 series flagship models to achieve the graphical fidelity with all the bells and whistles. That, to me, was a warning sign that maybe, just maybe, ray tracing was introduced prematurely and half-baked. Back then I theorized, that by tightly coupling this sort of upscaling tech to high-end cards and ray traced graphics, it sets a bad precedent. The kind of graphics NVIDIA was selling us on were beyond the cards’ actual capabilities.

Needing to upscale to keep frame rates smooth already seemed “fake” to me. If that amount of money for a single PC component still can’t produce those graphics without using software trickery to achieve acceptable frame rates, then what am I spending that money for to begin with exactly?

Fast-forward to today and nothing has really changed, besides NVIDIA now charging double the amount for the flagship RTX 5090. And guess what? It still doesn’t do Cyberpunk 2077—theflagship ray tracing game—with full ray tracing at a playable framerate in native 4K, only with DLSS enabled.

From the RTX 4090 website:

From the RTX 5090 website:

GPU
MSRP
CP2077 4K native RT Overdrive FPS
RTX 4090
$1,599
~20 FPS
RTX 5090
$1,999
~27 FPS

So 7 years into ray traced real-time computer graphics and we’re still nowhere near 4K gaming at 60 FPS, even at $1,999. Sure, you could argue to simply turn RT off and performance improves. But then, that’s not why you spent all that money for, right? Pure generational uplift in performance of the hardware itself is miniscule. They’re selling us a solution to a problem they themselves introduced and co-opted every developer to include the tech into their games. Now they’re doing an even more computationally expensive version of ray tracing: path tracing. So all the generational improvements we could’ve had are nullified again.

And even if you didn’t spend a lot of money on a GPU, what you get isn’t going to be powerful enough to make those ray traced graphics pop and still run well. So most peoples’ experience with ray tracing is: turn it on to see how it looks, realize it eats almost all your FPS and never turn it on ever again, thinking ray tracing is a waste. So whatever benefits in realistic lighting was to be achieved is also nullified, because developers will still need to do lighting the old-fashioned way for the people who don’t or can’t use ray tracing[8].

Making the use of upscaling tech a requirement, at every GPU price point, for every AAA game, to achieve acceptable levels of performance gives the impression that the games we’re sold are targeting hardware that either doesn’t even exist yet or nobody can afford, and we need constant band-aids to make it work. Pretty much all upscalers force TAA[9]for anti-aliasing and it makes the entire image on the screen look blurry as fuck the lower the resolution is.

Take for example thisRed Dead Redemption 2footage showing TAA “in action”, your $1,000+ at work:

Frame generation exacerbates this problem further by adding to the ghosting of TAA because it guesstimates where pixels willprobablygo in an “AI” generated frame in between actually rendered frames. And when it’s off it reallylooks off.Both in tandem look like someone smeared your screen with vaseline. And this is what they expect us to pay a premium for? For the hardwareandthe games?!

Combine that with GPU prices being absolutely ridiculous in recent years and it all takes on the form of a scam.

As useful or impressive a technology as DLSS might be, game studios relying as heavily on it as they do, is turning out to be detrimental to the visual quality of their games and incentivizes aiming for a level of graphical fidelity and complexity with diminishing returns. Games from 2025 don’t look that dramatically different or better than games 10 years prior, yet they run way worse despite more modern and powerful hardware. Games these days demand such a high amount of compute that the use of upscaling tech like DLSS is becomingmandatory.The most egregious example of this beingMonster Hunter Wilds, which states in its system requirements, that itneedsframe generation to run at acceptable levels.

Recommended system requirements for Monster Hunter Wilds noting 1080p on medium settings reaches 60 fps only with frame generation enabled

Meanwhile, Jensen Huang came up on stage during the keynote for the RTX 50 series cards andproudly proclaimed:

RTX 5070, 4090 performance at $549, impossible without artificial intelligence.

What he meant by that, as it turns out, is the RTX 5070 only getting there with every trick DLSS has to offer, including new DLSS 4 Multi-Frame Generation only available on RTX 50 cards at the lowest quality setting and all DLSS trickery turned up to the max.

You cannot tell me this is anywhere near acceptable levels of image quality for thousands of bucks (video time-stamped):

Not only does that entail rendering games at a lower internal resolution, you also have to tell your GPU to pull 3 additional made up frames out of its ass so NVIDIA can waltz around claiming “Runs [insanely demanding game here] as 5,000 FPS!!!” for thehigher number = bettermasturbator crowd. All the while the image gets smeared to shit, because NVIDIA just reinvented the motion smoothing option from your TV’s settings menu, but badly and also it’s “AI” now. Else what would all those Tensor-cores be doing than waste space on the GPU die that could’ve gone to actual render units? NVIDIA likes you to believe DLSS can create FPS out of thin air and they’re trying to prove it withdubious statistics—only disclosing in barely readable fine print, that it’s a deliberately chosen very small sample size, so the numbers look more impressive.

The resolution is fake, the frames are fake, too, and so is the marketed performance. Never mind that frame generation introduces input lag that NVIDIA needs to counter-balance with their “Reflex” technology, lest what you see on your screen isn’t actually where you think it is because, again, the frames faked in by Frame Generation didn’t originate from the game logic. They create problems for themselves, that they then create “solutions” for in an endless cycle of trying to keep up the smoke screen that these cards do more than they’re actually equipped to do, so a 20% premium for a 10% uplift in performance has the faintest resemblance of justification[10].

I was afraid DLSS would get used to fake improvements where there are barely any back then and I feel nothing if not vindicated for how NVIDIA is playing it up, while jacking up prices further and further with each generation. None of that is raw performance of their cards. This is downright deceitful bullshit.

## The intimidations will continue until morale improves

NVIDIA lying on their own presentations about the real performance of their cards is one thing. It’s another thing entirely, when they start bribing and threatening reviewers, to steer the editorial direction in NVIDIA’s favor.

In December 2020, hardware review channelHardware Unboxedreceived an emailfrom NVIDIA Senior PR Manager Bryan Del Rizzo, after they reviewed NVIDIA cards on pure rasterization performance without DLSS or ray tracing, saying that performance did not live up to their expectations:

Hi Steve,

We have reached a critical juncture in the adoption of ray tracing, and it has gained industry wide support from top titles, developers, game engines, APIs, consoles and GPUs.

As you know, NVIDIA is all in for ray tracing. RT is important and core to the future of gaming. But it’s also only one part of our focused R&D efforts on revolutionizing video games and creating a better experience for gamers. This philosophy is also reflected in developing technologies such as DLSS, Reflex and Broadcast that offer immense value to consumers who are purchasing a GPU. They don’t get free GPUs—they work hard for their money and they keep their GPUs for multiple years.

Despite all of this progress, your GPU reviews and recommendations continue to focus singularly on rasterization performance and you have largely discounted all of the other technologies we offer to gamers. It is very clear from your community commentary that you do not see things the same way that we, gamers, and the rest of the industry do.

Our Founders Edition boards and other NVIDIA products are being allocated to media outlets that recognize the changing landscape of gaming and the features that are important to gamers and anyone buying a GPU today—be it for gaming, content creation or studio and streaming.

Hardware Unboxed should continue to work with out add-in card partners to secure GPUs to review. Of course, you will still have access to obtain pre-release drivers and press materials. That won’t change.

We are open to revisiting this in the future should your editorial direction change.

Hardware Unboxed was thus banned from receiving review samples of NVIDIA’s Founder Edition cards. It didn’t take long for NVIDIA to back-paddle after the heavily publicized outcry blew up in their face.

Which makes it all the more surprising, that a couple years later, they’re trying to pull this again. WithGamers Nexusof all outlets.

As Steve Burke explains in the video, NVIDIA approached him from the angle, that in order to still be given access to NVIDIA engineers for interviews and specials for their channel, Gamers Nexus needs to include Multi-Frame Generation metrics into their benchmark charts during reviews. Steve rightfully claims that this tactic of intimidating media by taking away access until they review NVIDIA cards in a way that agrees with the narrative NVIDIA wants to uphold, tarnishes the legitimacy ofeveryreview of every NVIDIA card ever made, past and present. It creates an environment of distrust that is not at all conductive when you’re trying to be a tech reviewer right now.

This also coincided with the launch of the RTX 5060, a supposedly more budget friendly offering. Interestingly, NVIDIA did not provide reviewers with the necessary drivers to test the GPU prior to launch. Instead, the card and the drivers launched at the same time all of these reviewers were off at Computex, a computer expo in Taipei, Taiwan. The only outlets that did get to talk about the card prior to release were cherry-picked by NVIDIA, and even then it was merelypreviewsof details NVIDIA allowed them to talk about,notindependentreviews.Because if they would’ve been properly reviewed, they’d all come to the same conclusions: that the 8 GB of VRAM would make this $299[11]“budget card” age very poorly because that is not enough VRAM to last long in today’s gaming landscape.

But it probably doesn’t matter anyways, because NVIDIA is also busy tarnishing the reputation of their drivers,releasing hotfix after hotfixin an attempt to stop their cards, old and new, from crashing seemingly randomly, when encountering certain combinations of games, DLSS and Multi-Frame Generation settings. Users of older generation NVIDIA cards can simply roll back to a previous version of the driver to alleviate these issues, but RTX 50 series owners don’t get this luxury, because older drivers won’t make their shiny new cards go.

## NVIDIA won, we all lost

With over 90% of the PC market running on NVIDIA tech, they’re the clear winner of the GPU race. The losers are every single one of us.

Ever since NVIDIA realized there is tons of more money to be made on everything that isnotpart of putting moving pixels on a screen, they’ve taken that opportunity head on. When the gold rush for crypto-mining started, they were among the first to sell heavily price-inflated, GPU-shaped shovels to anybody with more money than brains. Same now with the “AI” gold rush. PC gamers were hung out to dry.

NVIDIA knows we’re stuck with them and it’s infuriating. They keep pulling their shenanigans and they will keep doing it until someone cuts them down a couple notches. But the only ones who could step up to the task won’t do it.

AMD didn’t even attempt at facing NVIDIA at the high-end segment this generation, instead trying to compete on merely the value propositions for the mid-range. Intel is seemingly still on the fence if they really wanna sell dedicated GPUs while shuffling their C-suite and generally being in disarray. Both of them could be compelling options when you’re on a budget, if it just wasn’t for the fact that NVIDIA has a longstanding habit of producing proprietary tech that only runs well on their hardware. Now they’ve poisoned the well with convincing everybody that ray tracing is something every game needs now and games that incorporate it do so on an NVIDIA tech-stack which runs like shit on anything that is not NVIDIA. That is not a level playing field.

When “The way it’s meant to be played” slowly turns into “The only way it doesn’t run like ass” it creates a moat around NVIDIA that’s obviously hard to compete with. And gamers aren’t concerned about this because at the end of the day, all they care about is that the game runs well and looks pretty.

But I want you to consider this: Games imbued with such tech creates a vendor lock-in effect. It gives NVIDIA considerable leverage in terms of how games are made, which GPUs you consider buying to run these games and how well they will eventually, actually run on your system. If all games that include NVIDIA’s tech are made in a way that make it so youhaveto reach for the more expensive models, you can be sure that’s a soft power move NVIDIA is gonna pull.

And as we established, it looks like they’re already doing that. Tests show that the lower-end NVIDIA graphics cards cannot (and probably were never intended to) perform well enough, even with DLSS, because in order to get anything out of DLSS you need more VRAM, which these lower-end cards don’t have enough of. So they’re already upselling you on more expensive models by cutting corners in ways that make it a “no-brainer” to spend more money on more expensive cards, when you otherwise wouldn’t have.

And they’re using their market dominance to control the narrative in the media, to make sure you keep giving them money and keep you un- or at the very least misinformed. When you don’t have to compete, but don’t have any improvements to sell either (or have no incentive for actual, real R&D) you do what every monopolist does and wring out your consumer base until you’ve bled them dry.

A few years back I would’ve argued that that’s their prerogative if they provide the better technical solutions to problems in graphics development. Today, I believe that they are marauding monopolists, who are too high on their own supply and they’re ruining it for everybody. If NVIDIA had real generational improvements to sell, they wouldn’t do it by selling usoutright lies.

And I hate that they’re getting away with it, time and time again, for over seven years.

1. A shunt resistor is a small electrical component in a circuit that measures how much current is flowing through a connection (typically from the PCIe power connectors from the power supply and optionally from the PCIe port). A graphics card uses this information to manage its power consumption, detect if that consumption is within safe operating parameters and, if not, perform an emergency shutdown to prevent damages.↩︎
2. Which NVIDIA’s main rival AMDis not getting tiredof pointing out.↩︎
3. AMD also has accelerated video transcoding tech but for some reason nobody seems to be willing to implement it into their products. I read that this might be because for the longest time AMD’s AMF has been missing a crucial feature (namely b-frames) causing a significant drop in image quality compared to NVIDIA’s NVENC. But still, the option would be nice, if only for people to not be artificially stuck on NVIDIA.↩︎
4. Also, I would expect my display to not draw any power after I’ve physically powered it off—not stand-by,off.G-Sync displays were shown to still draw as much as14W when turned off, while a FreeSync display drew none, like you would expect.↩︎
5. Obviously, this is bad for game preservation and backwards compatibility that the PC platform is known and lauded for. Another case of this is 3dfx’sGlide 3D graphics API, which was exclusive to their Voodoo graphics cards. It was superseded by general purpose technologies like Direct3D and OpenGL after 3dfx became defunct. NVIDIA’s proprietary tech isn’t becoming general purpose, as to allow competitors to compete on equal footing and on their own merits.↩︎
6. The 64-bit version of Windows XP doesn’t count, because it wasn’t available to consumers.↩︎
7. The “Super Sampling” part of DLSS is already a misnomer. Super sampling in the traditional sense means rendering at a higher resolution and then downsampling the rendered images to the target resolution (e.g. render at 4K, downsample to 1440p). The point of this is to achieve better anti-aliasing results. Starting with DLSS 2.0 the NVIDIA tech does theexact opposite—rendering at alowerresolution andupscalingto the target resolution. The term might have had the correct meaning in DLSS 1.0, but not anymore with DLSS 2.0 onwards. Also, in DLSS 1.0 game devs needed to train the models themselves with high resolution footage of their game from every conceivable angle, light setting, environments, etc. which was probably prohibitively time consuming and hurt the tech’s adoption. Later versions of DLSS changed this for a more generally trained model and uses information from the rendered frames of the game itself.↩︎
8. Unless you’reDoom: The Dark Agesand don’t allow people to turn it off.↩︎
9. TAA, or Temporal Anti-Aliasing, is an anti-aliasing technique that uses past rendered frames to estimate where to apply smoothing to jagged edges of rendered graphics, especially with moving objects. TAA is very fast with minimal performance impact. The downside, however, is that using past frames causes ghosting artifacts and blurs motion much more visibly than FXAA (Fast Approximate Anti-Aliasing) or MSAA (Multi-Sampling Anti-Aliasing). The issue is, however, that rendering pipelines shifted to deferred rendering and heavy use of shaders that anti-aliasing techniques like MSAA don’t work with, so TAA is the only viable option left, as outlined in thisDigitalFoundry deep-dive.↩︎
10. And people just gobble it up because tech literacy and common sense are fucking dead!↩︎
11. That’s the MSRP of course, but as we already established, MSRPs are a complete wash with graphics cards, and JayzTwoCents demonstrates this in hisreviewof the RTX 5060, with 3rd party offerings of the card adding as much as an $80 premium on top for diminishing little extra performance. Because, again, this card’s Achilles’ heel is the low amount of VRAM, and charging $80 over MSRP for only double-digit increases in MHz and call it “overclocked” is honestly insulting.↩︎
