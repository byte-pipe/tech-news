---
title: 'Asterinas: a new Linux-compatible kernel project [LWN.net]'
url: https://lwn.net/SubscriberLink/1022920/ad60263cd13c8a13/
site_name: hackernews
fetched_at: '2025-06-21T04:06:22.705070'
original_url: https://lwn.net/SubscriberLink/1022920/ad60263cd13c8a13/
author: howtofly
date: '2025-06-21'
---

LWN
.net

News from the source






User:


Password:



 |


 |


Subscribe
 /

Log in
 /

New account

# Asterinas: a new Linux-compatible kernel project

## [LWN subscriber-only content]

June 19, 2025

This article was contributed by Ronja Koistinen

Asterinas
 is a new
Linux-ABI-compatible kernel project written in Rust, based on what the
authors call a "framekernel architecture". The project overlaps somewhat
with the goals of the
Rust for Linux
project
, but approaches the problem space from a different direction by
trying to get the best from both monolithic and microkernel designs.

#### What's a framekernel?The framekernel concept is explained in the September 2024 paper "Framekernel: A Safe
and Efficient Kernel Architecture via Rust-based Intra-kernel Privilege
Separation" by Yuke Peng et al.A fuller version of the paperwas published in early June.Traditionally, monolithic kernels lump everything into one kernel-mode
address space, whereas microkernels only implement a minimaltrusted
computing base (TCB)in kernel space and rely on user-mode services for
much of the operating system's functionality. This separation implies the
use of interprocess communication (IPC) between the microkernel and those
services. This IPC often has a performance impact, which is a big part of
why microkernels have remained relatively unpopular.Stay on top of Linux kernel developmentwitha one-month free trial subscriptionto LWN, no credit card required.The core of Asterinas's "framekernel" design is the encapsulation of all
code that needs Rust'sunsafefeatures inside a library, enabling
the rest of the kernel (the services) to be developed using safe
abstractions. Those services remain within the kernel's address space, but
only have access to the resources that the core library gives to them.
This design is meant to improve the safety of the system while retaining
the simple and performant shared-memory architecture of monolithic
kernels. TheAsterinas bookon the project's website provides a nicearchitectural mission statement and overview.The aptness of the "framekernel" nomenclature can perhaps be debated. The
frame part refers to the development framework wrapping the unsafe
parts behind a memory-safe API. The concept of the TCB is, of
course, not exclusive to microkernel architectures but, because there are
strong incentives to strictly scrutinize and, in some contexts, evenformally
verifythe TCB of a system, keeping the TCB as small as possible is a
central aspect of microkernel designs.An update on the project is available on the Asterinas blog in the
June 4 post titled "Kernel
Memory Safety: Mission Accomplished". The post explains the team's
motivations and the need for the industry to address memory-safety
problems; it provides some illustrations that explain how the framekernel
is different from monolithic kernels and microkernels. It also takes a
moment to emphasize that the benefits of Rust don't stop with memory
safety; there are improvements tosoundnessas well.
Perhaps most importantly, the post highlights the upcoming Asterinas
presentation at the2025
USENIX Annual Technical Conference.#### Related workIn their paper, the authors compare Asterinas to some prior Rust-based
operating-system work, exploring the benefits of the language's
memory-safety features and explain how Asterinas differs from that previous
work. Specifically, the paper contrasts Asterinas withRedLeaf, an operating system written in Rust and presented at the 14th
USENIX Symposium on Operating Systems Design and Implementation (OSDI 20)
in 2020. Asterinas uses hardware isolation to permit running user-space
programs written in any programming language, aims to be general-purpose,
and provides a Linux-compatible ABI, while RedLeaf is a microkernel that is
designednotto use the hardware's isolation features, and the
project focuses on different things.Another project of interest isTock, an
embedded system that targets SoCs with limited hardware protection
functionality. Like Asterinas, Tock also divides the kernel into a
trusted core allowed to useunsafeand untrusted "capsules" that
are not. As mentioned, Asterinas does rely on hardware protection and
isn't intended for strictly embedded use, which differentiates it from
Tock.It bears mentioning that the Rust for Linux project, which is introducing
Rust code into the upstream Linux kernel, has similar goals as
Asterinas. It also aims to encapsulate kernel interfaces with safe
abstractions in such a way that drivers can be written in Rust without any
need forunsafe.#### Work toward formal verificationOne goal of shrinking the TCB of an operating system is to make it feasible
to have it formally verified. In February 2025, the Asterinas blog
featureda
post detailing plans to do just that. The best known formally verified
kernel isseL4, an L4-family
microkernel.Asterinas aims to use the framekernel approach to achieve a system that has
a small, formally verified TCB akin to a lean microkernel, but also a
simple shared-memory architecture with Linux ABI compatibility, all at the
same time. This is a radical departure from any previously formally
verified kernel; the blog post describes those kernels as deliberately
small and limited compared to "full-fledged, UNIX-style OSes".The Asterinas project is collaborating with a security-auditing company
calledCertiKto useVerusto formally verify the
kernel. There is an extensivereportavailable from CertiK on how Asterinas was audited and the
issues that were found.#### Libraries and toolsThe Asterinas kernel is only one result of the project. The other two areOSTD, described as "a Rust
OS framework that facilitates the development of and innovation in OS
kernels written in Rust", andOSDK, a
Cargo addon to assist with the development, building, and testing of
kernels based on OSTD.There are four stated goals for OSTD as a separate crate. One is to lower
the entry bar for operating-system innovation and to lay the groundwork for
newcomers to operating-system development. The second is to enhance memory
safety for operating systems written in Rust; other projects can benefit
from its encapsulation and abstraction of low-level operations. The third is
to promote code reuse across Rust-based operating-system projects. The
fourth is to boost productivity by enabling testing of new code in user
mode, allowing developers to iterate without having to reboot.It is worth emphasizing that the kernels that can be written with OSTD do
not have to be Linux-compatible or, in any way, Unix-like. The APIs
provided are more generic than that; they are memory-safe abstractions for
functionality like x86 hardware management, booting, virtual memory, SMP,
tasks, users, and timers. Like most Rust crates, OSTD isdocumented on
docs.rs.Asterinas reports Intel, among others, as a sponsor of the project.
Intel's interest is likely related to itsTrust
Domain Extensions (TDX)feature, which provides hardware modes and
features to facilitate isolation of virtual machines, and memory
encryption. The Asterinas book has a briefsection
on TDX, and the OSDK supports it.The OSTD, or at least the parts that Asterinas ends up using, seems to
essentially be the restricted TCB that allowsunsafe. For an
illustrative example, we could take a look at thenetworkkernel
component'ssource
codeand see that the buffer code uses DMA, locking, allocation, and
virtual-memory code from the OSTD through memory-safe APIs.#### Current stateAsterinas was first released under the Mozilla Public License in early
2024; it has undergone rapid development over the past year. GitHublists 45
individual committers, but the majority of the commits are from a
handful of PhD students from the Southern University of Science and
Technology, Peking University, and Fudan University, as well as a Chinese
company calledAnt Group, which
is a sponsor of Asterinas.At the time of writing, Asterinas supports two architectures, x86 and RISC-V.
In the January blog post linked above, it was reported that Asterinas
supported 180 Linux system calls, but the number has since grown to206
on x86. As of version 6.7, Linux has 368 system calls in total, so there is
some way to go yet.Overall, Asterinas is in early development. There have been no releases,
release announcements, changelogs, or much of anything other than Git tags
and a short installation guide in the documentation. TheDependents
tabof the OSTD crate on crates.io shows that no unrelated, published
crate yet uses OSTD.It does not seem like Asterinas is able to run any applications yet.Issue #1868in Asterinas's repository outlines preliminary plans toward a first
distribution. The initial focus on a custom initramfs and some rudimentary
user-space applications, followed by being able torun
Docker. There are initial plans to bootstrap a distribution based on
Nix. Notably (but unsurprisingly), this issue mentions that Asterinas
doesn't support loading Linux kernel modules, nor does it ever
plan to.#### Near-future goalsTheRoadmapsection of the Asterinas book says that the near-term goals are to expand
the support for CPU architectures and hardware, as well as to focus on
real-world usability in the cloud by providing a host OS for virtual
machines. Apparently, the support for Linux virtio devices is already
there, so a major hurdle has already been cleared. In particular, the
Chinese cloud market, in the form of Aliyun (also known as Alibaba Cloud)is a
focus. The primary plans involve creating a container host OS with a
tight, formally verified TCB and support for some trusted-computing
features in Intel hardware, for the Chinese cloud service.While both Rust for Linux and Asterinas have similar goals (providing a
safer kernel by relying on Rust's memory safety), their scopes and
approaches are different. Rust for Linux focuses on safe abstractions
strictly for new device drivers to be written in safe Rust, but this leaves
the rest of the kernel untouched.
Asterinas, on the other hand, aims to build a whole new kernel from the ground
up, restricting theunsafe-permitting core to the absolute minimum,
which can then be formally verified. Asterinas also focuses on
containers and cloud computing, at least for now, while Rust for Linux looks to
benefit the whole of the Linux ecosystem.Despite the stated cloud focus, there is more going on, for example building
support forX11andXfce.
Also, the OSTD could, of course, prove interesting for OS development
enthusiasts irrespective of the Asterinas project, but so far it remains unknown
and untested by a wider audience.Asterinas is certainly a refreshingly innovative take on principles for
operating-system development, leaning on the safety and soundness
foundations provided by the Rust language and compiler. So far it is at an
early exploratory stage driven by enthusiastic Chinese researchers and
doesn't see any serious practical use, but it is worth keeping an eye
on. It will be interesting to see the reception it will get from the
Rust for Linux team and the Linux community at large.Index entries for this articleGuestArticlesKoistinen, Ronjato post comments



### Singularity OS v2Posted Jun 19, 2025 17:49 UTC (Thu)
 byCyberax(✭ supporter ✭, #52523)
 [Link] (10 responses)> The core of Asterinas's "framekernel" design is the encapsulation of all code that needs Rust's unsafe features inside a library, enabling the rest of the kernel (the services) to be developed using safe abstractionsVery much like Singularity OS from Microsoft, but with the borrow checker for memory safety instead of a garbage collector.### Singularity OS v2Posted Jun 19, 2025 17:54 UTC (Thu)
 bykhim(subscriber, #9252)
 [Link] (9 responses)Haven't Singularity OS tried to use in-language safety as security boundary? Java have shown is it's terrible idea and I'm pretty sure Singularity OS would have had the same fate if it ever went beyond “demo” stage.But using that boundary to separate TCB from “non-malicious, but potentially buggy code” is an interesting twist: Rustusafeis entirely unsuitable against malicious actor (there are numerous soundness bugs in a compiler), but with non-malicious yet not entirely trusted actor… this may even actually work.### Singularity OS v2Posted Jun 19, 2025 18:06 UTC (Thu)
 byCyberax(✭ supporter ✭, #52523)
 [Link] (8 responses)> Haven't Singularity OS tried to use in-language safety as security boundary?Yep, and it worked well.> Java have shown is it's terrible idea and I'm pretty sure Singularity OS would have had the same fate if it ever went beyond “demo” stage.Java's security model was just designed badly. It essentially granted elevated privileges to _code_, kinda like the SUID bit in Unix. With obvious pitfals because the input data can be manipulated, and Java also had way too many ways around its own safeties.Modern sandboxing instead relies on capability passing. Just look at JavaScript/WASM for an example of a resilient language-level sandboxing.### Singularity OS v2Posted Jun 19, 2025 18:12 UTC (Thu)
 bykhim(subscriber, #9252)
 [Link] (7 responses)> Just look at JavaScript/WASM for an example of a resilient language-level sandboxing.Do you even know of any production use of JavaScript/WASM without non-language sandbox?I think the fact that none (or almost no one) does that spokes volumes about viability of such approach.> Yep, and it worked well.It's impossible to say whether it “worked well” if it was never tested in an environment where security breach means losses measured in billions, sorry.Java also “worked pretty well” till they deployed it in browsers.### Singularity OS v2Posted Jun 19, 2025 19:16 UTC (Thu)
 byCyberax(✭ supporter ✭, #52523)
 [Link] (4 responses)> Do you even know of any production use of JavaScript/WASM without non-language sandbox?Sure, modern browsers are an example. A JavaScript sandbox escape is easy to elevate because so many sharp objects have to be exposed to the scripting context (e.g. WebGPU).Docker also has WASM containers now.> It's impossible to say whether it “worked well” if it was never tested in an environment where security breach means losses measured in billions, sorry.Java is literally used for the most secure applications: hardware security modules and payment systems.### Singularity OS v2Posted Jun 19, 2025 19:30 UTC (Thu)
 bykhim(subscriber, #9252)
 [Link] (2 responses)> Sure, modern browsers are an example.What do you call “modern browser” here? Lynx? Coz all browsers that I know of put rendered in a OS-supported sandbox, precisely because they don't trust JavaScript.A JavaScript sandbox escape is easy to elevate because so many sharp objects have to be exposed to the scripting context (e.g. WebGPU).GPU is, usually, handled by separate GPU-talking process.> Docker also has WASM containers now.Docker also has WASM containers now.Does it have in-WASM-image security boundary? Last time I looked it was treating the whole WASM blob as an OS process, with one array imitating “untrusted memory” and without any fine-grained security checks similar to BPF or JVM – poor imitation of OS-level sandboxing, not fire-tuned language-level one.> Java is literally used for the most secure applications: hardware security modules and payment systems.Do they run untrust apples in these? Really? Again: saw some of them, none trust Java-language sandbox.The question is not whether Java or WASM or JavaScript are used in sensitive context but whether they trust language-level security management… I'm yet to see serious system that's built that way.### Singularity OS v2Posted Jun 19, 2025 19:43 UTC (Thu)
 byCyberax(✭ supporter ✭, #52523)
 [Link] (1 responses)> GPU is, usually, handled by separate GPU-talking process.Not with WebGPU. It works in the same address space as JS, and allows things like direct buffer manipulation (see:https://markaicode.com/webgpu-2-chrome-2025-performance/). The WebGPU library (Dawn/wgpu) make the underlying platform APIs safe, but if you escape the JS sandbox, you can access it directly.Browsers obviously try to make exploitation harder with OS-level sandboxes, but once you're out of the JS sandbox, it's game over for serious attackers.> Does it have in-WASM-image security boundary? Last time I looked it was treating the whole WASM blob as an OS process, with one array imitating “untrusted memory” and without any fine-grained security checks similar to BPF or JVM – poor imitation of OS-level sandboxing, not fire-tuned language-level one.Well, yes. That's the whole idea behind WASM.> Do they run untrust apples in these? Really? Again: saw some of them, none trust Java-language sandbox.They do. JavaCards allow third-party apps, and they use a similar capability-based security model.### Singularity OS v2Posted Jun 19, 2025 20:15 UTC (Thu)
 bykhim(subscriber, #9252)
 [Link]> Well, yes. That's the whole idea behind WASM.Then how is it relevant to the discussion about “in-language safety as security boundary”?> JavaCards allow third-party apps, and they use a similar capability-based security model.Since when? I admit that I haven't worked with cardlets for last ten years but when I did it was exact same “cardlet as whole is it's own world with no security boundaries inside”> Browsers obviously try to make exploitation harder with OS-level sandboxes, but once you're out of the JS sandbox, it's game over for serious attackers.This may be the one example where you are right and language-based is used as a security boundary… and only because of so much sunk cost that it's impossible to fix that design.All other examples that have brought don't use language-level sandbox as security boundary at all – and even browsers are not trusting it entirely.One half-example where language-level sandbox kinda-sorta-works if you squint just right vs dozens of examples where it's ditched for something simpler and thus more robust doesn't look like “it worked well” to me, sorry.### Singularity OS v2Posted Jun 19, 2025 21:40 UTC (Thu)
 byepa(subscriber, #39769)
 [Link]These hardware security modules and payment systems are not relying on Java’s security features to run arbitrary untrusted Java bytecode, as people once tried to in browser applets.The properties enforced by languages such as Rust don’t try to let you do that, but while they are less concerned with malicious attacks, they do a better job of preventing bugs in practice and letting you formally verify your system. I think that was the OP’s point.### Singularity OS v2Posted Jun 19, 2025 21:44 UTC (Thu)
 byroc(subscriber, #30627)
 [Link] (1 responses)> Do you even know of any production use of JavaScript/WASM without non-language sandbox?I think you're right that everyone who cares about security uses a hardware-backed (i.e. process) sandbox to protect the host platform from untrusted JS/WASM. At least I hope they do.But in lots of cases people are still relying on language/VM-level protection to protect mutually distrusting JS/WASM components from each other. While the state of the art in browsers today is full site isolation so that no process mixes code from mutually distrusting Web sites, Safari/Webkit doesn't do it, and on Android I don't think any browser commits to it.This is even true for systems designed without legacy constraints. Cloudflare Workers runs mutually distrusting workers in the same process using V8 isolates.### WASM security proofs.Posted Jun 20, 2025 6:22 UTC (Fri)
 bygmatht(subscriber, #58961)
 [Link]People who are interested in the research into WASM/WASI security may want to read:https://www.cs.cmu.edu/~csd-phd-blog/2023/provably-safe-s...### OS development getting more popular again?Posted Jun 19, 2025 18:24 UTC (Thu)
 byshironeko(subscriber, #159952)
 [Link] (15 responses)In the past few years we've seen so many new OS pop up, this is so cool.### OS development getting more popular again?Posted Jun 20, 2025 10:30 UTC (Fri)
 bypaulj(subscriber, #341)
 [Link] (14 responses)China is going to replace Linux. In large part cause of the stupidity of the US and its expanding sanctions.Already there are phones from major Chinese manufacturers that are now running non-Linux kernels. China is going to rewrite everything for itself, cause the US has shown you absolutely must not - in strategic terms - depend on any technology the US government can have influence over.### OS development getting more popular again?Posted Jun 20, 2025 11:33 UTC (Fri)
 bygeorgyo(guest, #121727)
 [Link] (13 responses)Does the US control Linux? How can the US even sanction a GPL international code base? Even if they could, what would that even mean? All the development is open, and the code is readily available.If you ship a product that modifies the Linux kernel, you must also share that code. While I personally think that is great, I can imagine that companies that want to build a bigger moat would want a proprietary kernel. Then they could have hardware or security features that they don't have to share.IE, anyone can pretty much make an Android phone, but only Apple has the sources for the iOS kernel. Some might want a similar wall.Personally, I hope that Linux stays the preferred choice. There is just a ton of value in everyone not reimplementing the wheel over and over again.### US sanctioning LinuxPosted Jun 20, 2025 11:46 UTC (Fri)
 byfarnz(subscriber, #17727)
 [Link] (9 responses)As an example, the US could require that versions of the Linux kernel in the USA (which includes Linus Torvalds' and Greg K-H's work) do not contain drivers for hardware produced by sanctioned entities, and that entities in the USA (Linus and Greg again) do not communicate with sanctioned entities.That prevents the Chinese manufacturers from upstreaming their code, forcing them to maintain a fork without even being allowed to tell Linus and Greg what changes make their lives harder, let alone upstreaming general infrastructure improvements that make all devices in their device class easier to drive.### US sanctioning LinuxPosted Jun 20, 2025 14:24 UTC (Fri)
 bypizza(subscriber, #46)
 [Link] (8 responses)> That prevents the Chinese manufacturers from upstreaming their code, forcing them to maintain a fork without even being allowed to tell Linus and Greg what changes make their lives harder, let alone upstreaming general infrastructure improvements that make all devices in their device class easier to drive....And how maintaining a fork harder than writing/maintaining their own independent kernel (and userspace)?### US sanctioning LinuxPosted Jun 20, 2025 14:34 UTC (Fri)
 byfarnz(subscriber, #17727)
 [Link] (1 responses)It's about the same difficulty level, since their code will diverge from the upstream version in significant ways.Given that you're not getting any long-term benefit from starting from Linux, however, why not dump the Linux legacy for future products? There's a decent chunk of code in there that you basically don't care about - x86 and x86-64 legacy stuff, SATA drivers etc - and you get a smaller codebase to maintain if you dump it all.### US sanctioning LinuxPosted Jun 20, 2025 16:31 UTC (Fri)
 bybluca(subscriber, #118303)
 [Link]> It's about the same difficulty level, since their code will diverge from the upstream version in significant ways.Come on now, that is not even remotely true. Adding some device drivers for some specific hardware is not nearly the same thing as reimplementing the entire kernel from scheduling, memory, control groups, events, netlink, network, namespaces, mounts, filesystems, and so on and so forth.ARM vendors have been doing exactly this since forever. They take a kernel version, and they add hundreds of thousands to millions of lines of code of device-specific stuff, freeze it and ship it. New device, new kernel version, rinse and repeat.### US sanctioning LinuxPosted Jun 20, 2025 15:01 UTC (Fri)
 bypaulj(subscriber, #341)
 [Link] (5 responses)Because part of the value of the code-base is the expertise you have in it, and the expertise you can access for it and via it.If you can no longer interact with a significant chunk of the external expertise for a code-base, because it resides in (or is otherwise subject to) a country that is playing silly geo-political games, then that value is lost. You can't ask for help. You can't submit patches and get them reviewed, thus streamlining their integration with other pending and future work.You must now rely on your own expertise. Your own internal expertise will much rather develop its own code, that it fully understands, than have to wade through tonnes of other people's code. Especially when there is a language barrier for any available documentation. If they start from scratch, then they can write their own documentation in their own language. As they develop a community around that new project, they will all share a language, making comms much easier, making further development easier, etc.There are many reasons, they could be good or bad. Regardless of how we might weigh those reasons up, China views it as worthwhile to develop replacements for Linux. And they have multiple efforts in progress. At least one of which is close to full-commercial-release.### US sanctioning LinuxPosted Jun 20, 2025 16:04 UTC (Fri)
 byWol(subscriber, #4433)
 [Link] (4 responses)> There are many reasons, they could be good or bad. Regardless of how we might weigh those reasons up, China views it as worthwhile to develop replacements for Linux. And they have multiple efforts in progress. At least one of which is close to full-commercial-release.And America seems to think everyone SHOULD share its "view on life". I make no bones that I place "Freedom of Speech" THIRD on a "Pick any two" list, so I certainly don't share America's view of what freedom is. I've seen it commented here that the majority of Chinese are on the whole very happy with their lot. Certainly they don't share "the American Dream". And one only has to look at the current geo-political situation to realise there is a lot of grass-roots (not politically manufactured) anti-Americanism in the Middle East.The Rest of the World should be developing replacements for American products. And if only Europe could get its act together AS EUROPE, and not a bunch of squabbling fiefdoms, America could easily find itself kow-towing to *our* economic might ...As pretty much every empire since before the Romans has proved, economic power leads to military power, and the Chinese appear to have taken that lesson to heart. So should we.(At least the Russians don't seem to have learnt it - not very well, at any rate. Selling raw materials isn't enough ...)Cheers,Wol### US sanctioning LinuxPosted Jun 20, 2025 16:26 UTC (Fri)
 bykhim(subscriber, #9252)
 [Link] (3 responses)> And if only Europe could get its act together AS EUROPE, and not a bunch of squabbling fiefdoms, America could easily find itself kow-towing to *our* economic might ...Europe is dead, there are no need to even talk about it. It's Zombie that's still moving, but couldn't survive.> (At least the Russians don't seem to have learnt it - not very well, at any rate. Selling raw materials isn't enough ...)Russians learned it better than everyone else. In the coming years the military might would be the deciding factor. And Russia prepared that before anyone else. China is still not ready, and Europe is only just talking about what needs to be done. While time have almost run out.> As pretty much every empire since before the Romans has proved, economic power leads to military power, and the Chinese appear to have taken that lesson to heart.I wonder where have you got that fantasy. Economic power and military power are, of course, interdependent, but if you have economic power and don't have military to protect you, then you are just food. US would rob Europe till it would collapse, then Russia would rip whatever it wants from the rotting carcass. UK would probably be able to grab some small parts of it, too, Portugal and Spain can survive if the Pope calls the people of Latin America to their protection, but the majority of European population have no future… in Europe, at least.### Stop this herePosted Jun 20, 2025 16:35 UTC (Fri)
 bycorbet(editor, #1)
 [Link] (2 responses)Seriously, you all know that this is far off-topic for LWN. Why do we have to keep asking you to stop it? Can everybody pushing this subthread please put an end to it now?### Stop this herePosted Jun 20, 2025 16:59 UTC (Fri)
 bykhim(subscriber, #9252)
 [Link] (1 responses)> Seriously, you all know that this is far off-topic for LWN.We don't know that if you don't tell us, actually. Lots of development in Linux and FOSS (that's on-topic for LWN, right?) is driven by that separation of the world into isolated clusters already – and it would be even more serious in the coming years.How would we know if LWN staff have decided to accept that and stopped ignoring it if we wouldn't discuss it?> Can everybody pushing this subthread please put an end to it now?That's fair: you want us to stop and wait few more years till you would accept the fact that even if you decide to ignore political games, it does not mean that political games will agree to ignore you… got it. Let's see where would it go after a year or two?> Why do we have to keep asking you to stop it?Because it is more difficult for people living closer to the chasm to ignore it, maybe… Or because there are more-and-more development driven by this “offtopic” in areas that LWN is supposed to cover, maybe…But let's discuss that year or two later… there would be more evidence why these things are very much on-topic for LWN by then.### Stop this herePosted Jun 20, 2025 18:00 UTC (Fri)
 bydaroc(editor, #160859)
 [Link]To be clear:Right above the comment box is a bullet point saying "Is the comment on-topic for the article and LWN?"The article in question here is about Asterinas. Were the first few comments on whether independent OS projects will become more common in the face of current politics on topic? Yes, just. But by the time the discussion got to the international balance of power and history of empire — without any reference to OS development — it stopped being on topic.I do think it's genuinely important to discuss these things, especially with people who don't share your views. But not every discussion has to happen here, specifically. There are lots of places to discuss these things on the internet, and if we don't all make some amount of effort to sort things by topicality, it gets much harder for people to find the discussions in which they are interested in participating.### OS development getting more popular again?Posted Jun 20, 2025 12:16 UTC (Fri)
 bypaulj(subscriber, #341)
 [Link] (2 responses)> How can the US even sanction a GPL international code base?Have you not kept abreast of the news here on LWN, where the "Linux Foundation" has a policy on removing/excluding people from Linux development if the US state orders, a policy which all the top US based kernels - particularly Linus - agree with?https://lwn.net/Articles/1007272/Have you not kept abreast of the news more widely in the tech industry, where the US threatens European companies with punitive measures if they do not follow its orders to stop selling their products to Chinese tech companies - indeed, they're not even allowed to give support for the equipment they already sold? (And needless to say, US tech companies are following those orders too - NVidia no longer allowed to sell higher-end "GPUs" to China).> Personally, I hope that Linux stays the preferred choice. There is just a ton of value in everyone not reimplementing the wheel over and over again.Too late. Chinese tech industry is already hard at work replacing Linux, as far as its own needs are concerned. It is a major strategic objective. There already are phones from the biggest makers coming to market, running their own Chinese developed kernel. This trend will continue. This story is due to that.### OS development getting more popular again?Posted Jun 20, 2025 15:04 UTC (Fri)
 byWol(subscriber, #4433)
 [Link] (1 responses)> Too late. Chinese tech industry is already hard at work replacing Linux, as far as its own needs are concerned. It is a major strategic objective. There already are phones from the biggest makers coming to market, running their own Chinese developed kernel. This trend will continue. This story is due to that.And Europe will be doing the same, if they have any sense. The American "Industrial / Defense" alliance was probably in large part behind their current political dominance in the world, they have the ability to make everything they need for themselves. Europe needs a "Europe first" policy for all defence production, which will probably have massive economic benefits. Which is also why America won't be happy if we do ...Let's hope Keir and crew have the guts to stand up and say "if we're spending so much more on defence, we need to spend it at home ..."Cheers,Wol### OS development getting more popular again?Posted Jun 20, 2025 16:35 UTC (Fri)
 bykhim(subscriber, #9252)
 [Link]> Let's hope Keir and crew have the guts to stand up and say "if we're spending so much more on defence, we need to spend it at home ..."Do you really believe they would be allowed to spend it in Europe? Why would US allow that and how can Europe oppose them if they have no military to protect their interests?For that matter, why do you think stuff that Europe would pay for would even ever reach the European soil?It would be a prudent decision for US to force Europe to pay for new shiny military toys and then use them in fight with China.P.S. And UK isnotEurope. It's closer to theTabaquiwho plans to feed on remnants of Europe afterShere Khanwould take its fill… it may even get some small pieces… not sure how big, though.### Counting system calls is not a good compatibility metricPosted Jun 19, 2025 21:58 UTC (Thu)
 byroc(subscriber, #30627)
 [Link] (2 responses)It's easy to evaluate, but it's pretty misleading. For example "ioctl" is one system call, and your OS might have an entry for it in its system-call table, but in reality it's a gateway to a whole universe of APIs. So is "io_uring" ... and even "open" (hello /proc, /sys)! And many other offenders sprouting myriad commands and options --- "ptrace", "perf_event_open", "madvise", ...For a better measure you need to run some kernel test suites.Building a Linux-compatible kernel is pretty much an infinite amount of work. You can "target a subset" but users will always want more. Microsoft tried that path and gave up pretty quickly. I guess gVisor has been modestly successful. It would be interesting for the various "Linux compatible" projects to try to converge on the API subset they support.I suppose if AGI is going to provide us with a huge number of cheap developers in the near future, projects like this will start to make more sense.### Counting system calls is not a good compatibility metricPosted Jun 20, 2025 9:00 UTC (Fri)
 bykris.shannon(subscriber, #45828)
 [Link]Another reasonable successful example is theLX Zones in SmartOSI do have to agree with "users will always want more" though.### Counting system calls is not a good compatibility metricPosted Jun 20, 2025 11:12 UTC (Fri)
 byKarellen(subscriber, #67644)
 [Link]On the other hand, when Linux was first getting going, Linux was the one implementing POSIX syscalls one at a time to the point where it just had enough to get bash/glibc running. And then enough more for the next program, and then the next.And a lot of "Linux" software isn't that closely tied to Linux, and will happily run on *BSD or other POSIXish OSs. If they can reimplement 99% of the most commonly used syscalls/features behind a Linux-compatible ABI, they'll probably have a lot software which will actually run on the system.### LicencingPosted Jun 20, 2025 6:52 UTC (Fri)
 bynim-nim(subscriber, #34454)
 [Link] (2 responses)MPL, OMG, people never learn.### LicencingPosted Jun 20, 2025 9:33 UTC (Fri)
 byxav(guest, #18536)
 [Link]Have corporate sponsors, use corporation-friendly licenses.### LicencingPosted Jun 20, 2025 13:35 UTC (Fri)
 byWol(subscriber, #4433)
 [Link]And why would they want the GPL? Which one, anyway? And is the GPL even *appropriate* for what they want to do? (Note my historic comments, that GPL is pretty useless when your system doesn't "link" in the conventional way!)Personally, I think MPL is actually a very good fit for Rust's crate system - the licence is modular in the same way crates are modular. It's not aggressively copyleft, but it stops you from taking other peoples' code private.Cheers,Wol### What about project depencencies ?Posted Jun 20, 2025 9:32 UTC (Fri)
 byacer(subscriber, #156526)
 [Link] (2 responses)Is it safe to include so many crates for an operating system implementation?https://github.com/asterinas/asterinas/blob/main/Cargo.lock### What about project depencencies ?Posted Jun 20, 2025 10:14 UTC (Fri)
 byfarnz(subscriber, #17727)
 [Link]Looking over that list, probably yes. There's a chunk of crates in there that are part of the Asterinas project, it's just that they're building as isolated dependencies instead of a big ball of spaghetti. Then there's a lot of single-purpose crates, which the OS needs (e.g. a printk implementation, some cryptographic primitives, CPU feature flag parsing), and can either share with others, or reimplement itself (with the additional risk of bugs that other people would see).There's about 10 crates or so in that set that I'd be unsure about, providing things like coloured log output to serial consoles.The things I would like to see in terms of trust are:Adeny.tomland a CI job to runcargo deny. This would be there to check for licensing, CVEs etc, and to allow them to restrict unwanted crates from getting in.Asupply-chaindirectory as set up bycargo vetand associated CI job to vet the full dependency set, so that I can see how well-audited their dependency chain is.### What about project depencencies ?Posted Jun 20, 2025 17:35 UTC (Fri)
 bythoughtpolice(subscriber, #87455)
 [Link]FWIW, it isn't really meaningfully useful to look at the lockfile for Rust projects to evaluate dependency footprint. Lockfiles contain "more" than you might expect because they also contain e.g. all possible transitive dependencies for everything (even if they are disabled by features), they contain cross platform dependencies (e.g. OS-specific libraries are included even if you don't use that OS), stuff like that. You have to look at the actual compiled crate graph if you want to actually eyeball the dependency footprint.For some reason they don't seem to use workspace-level dependencies, instead splitting specific deps between Cargo.toml files, so it's harder to see what the general "surface area" is.





Copyright © 2025, Eklektix, Inc.Comments and public postings are copyrighted by their creators.Linux is a registered trademark of Linus Torvalds
