---
title: How we ran a Unix-like OS (Xv6) on our home-built CPU with our home-built C compiler | Fueled by Coffee
url: https://fuel.edby.coffee/posts/how-we-ported-xv6-os-to-a-home-built-cpu-with-a-home-built-c-compiler/
site_name: hackernews
fetched_at: '2025-06-30T01:04:49.847467'
original_url: https://fuel.edby.coffee/posts/how-we-ported-xv6-os-to-a-home-built-cpu-with-a-home-built-c-compiler/
author: AlexeyBrin
date: '2025-06-30'
published_date: '2020-10-04T20:00:00+09:00'
---

Share

Takaya Saeki

 （☕, 🍣, 🍔) => 💻 / Likes web and system programming.

 Oct 4, 2020


 16 min read


# How we ran a Unix-like OS (Xv6) on our home-built CPU with our home-built C compiler

[Thanks for many comments and votes onHacker News!]

It’s been two years since I started working as a software engineer.
I sometimes tell my colleagues about a student project I did in my junior year of university,
and it’s so well-received that I’m writing this post.1

Now, let me ask you a question. Have you ever designed your own ISA, built a processor of that ISA on FPGA, and built a compiler for it?
Furthermore, have you run an operating system on that processor?
Actually, we have.

In this post, I’m going to talk about my undergraduate days in 2015,
our four months of building a home-built CPU of a home-built RISC ISA,
building a home-built C toolchain, and porting Xv6, a Unix-like OS, to that CPU.

## CPU Experiment at the University of Tokyo

It was all done as a student experiment project called CPU Experiment.
So, let’s start with what is CPU experiment.

CPU experiment is a little famous exercise held in the winter of the junior year in my department,
the Department of Information Science at the University of Tokyo.
In the experiment, students are divided into groups of four or five students.
Each group designs an own CPU architecture, implements it on an FPGA,
builds an OCaml subset compiler for that CPU, and then runs a given ray-tracing program on the CPU.
Typically, one or two people are responsible for each of the CPU, FPU, CPU simulator and compiler.
I was in charge of the CPU in my group, Group 6.

This exercise is well known for the high expectation of self learning.
The instructor only asks the students to “take this ray-tracing program written in OCaml and run it on your CPU implemented on an FPGA”, and the class ends.
He/she doesn’t tell much about the concrete steps of how to write CPU and compilers.
The students learn for themselves how to embody the general knowledge of CPUs and compilers learned in previous lectures to the level of real circuits and code.
Well, this is a very tough exercise, but very exciting and educational.

## Let’s run Operating System on our own CPU.

As some of you may have noticed, I didn’t talk about operating system at all.
I’ll add a little explanation.

Typically, the experiment proceeds as follows.
First, you make a CPU that works reliably, no matter how slow it is.
If you can make a working CPU and successfully run the ray-tracing program, you can earn the credit of the experiment.
After that, your team has a free time.
The traditional way to spend this free time is to further speed up their CPU.
In past experiments, students have made out-of-order CPU, VLIEW CPU, multi-core CPU, or even superscalar CPU, which is amazing.

However, some teams put more energy into doing fun such as running games or playing music by connecting a speaker with their CPU.
Group 6, to which I belonged, was a group of such people who loved entertainment,
and we decided to run an OS as our team goal.

As a result of other groups showing interest in this idea, a joint group of about 8 people, Group X,
was formed, and their goal was “Let’s run an OS on our own CPU!”

Although I was in charge of creating a CPU in Group 6,
this time I chose to be the leader of the OS team in the Group X.
So this post is written primarily from the perspective of the OS team,
but of course I also introduce the overall group’s results.

## Xv6

As the OS to be ported, we chose Xv6, a simple Unix v6-inspired OS created by MIT for educational purposes.
Xv6 is written in ANSI C, unlike Unix v6, and it runs on x86.
Xv6 is an educational OS, so its features are a bit poor, but it has sufficient features as a simple Unix-like OS.
You can find more information of Xv6 onWikipediaorthe GitHub repository.

## Challenges

In porting xv6, there are a lot of challenges on the software side alone because we were trying to create everything from scratch.

1. C Compiler and tool chain for Xv6

In the CPU experiment, we usually create an ML compiler. Naturally, you can’t compile C codes of Xv6.

2. What kind of CPU features required for operating system?

Privilege protections? Virtual address? Interrupt?
Yes, we had overall understanding of what operating system does by lectures,
but we didn’t have solid enough understanding to explain what specific CPU features could make that happen at that time.

3. What about the simulator?

We had a simulator made in the core part of CPU experiment,
but it was a simple one that executes one instruction by instruction,
and there was no interruption or no virtual address conversion.

4. Low portability of xv6

Xv6 was not very portable.
For example, it assumes thecharis 1 byte andintis 4 bytes, and manipulates the stack heavily.
Well, the name “Xv6” I guess comes from x86 and Unix “v6”, so it’s kind of natural.

We had a lot of concerns, but started the Group X’s OS porting project in December.From here I’m going to write about what we did in roughly chronological order.
It’s a little bit long, so if you want to look at our final products quickly,please jump to March.

## Late November - Starting the compiler

The first problem that we saw the answer to was the compiler and tool chain.
To be surprise, our decision was to build the C89 compiler from scratch.
To be honest, I hadn’t imagined that we would choose this way.
I remember I talked with Yuichi, who became in charge of CPU of Group X, about doing a gcc or llvm port at first.

However, one of the team members, Keiichi, suddenly said he had written a C compiler and showed us a prototype of a compiler with a simple parser and emitter.
It seemed more fun to write the toolchain from scratch, so we decided to write a compiler by ourselves.

Yuichi and Wataru from Group 3, who had already finished the core part of the experiment that year, joined Keiichi, and the Group X compiler team was born.
We later named our compiler Ucc.

## Mid-December - The OS team is up!

At the beginning of December, I completed my CPU, and Group 6 completed the core part of the CPU experiment.
So, we moved on to the fun part, Group X’s OS porting task.
At this time, myself and Shohei from Group 6 started working in Group X and became the OS team. Masayoshi joined it at the same time.

### Core part of the experiment: Writing a CPU

By the way, I guess not so many software engineers have ever written a CPU, so let me talk a little bit about making a CPU as well.

Nowadays, making a CPU doesn’t mean wiring every single jump wire on a breadboard; you write the circuitry in Hardware Description Language.
Then you synthesize that HDL into a real circuit using Vivado or Quartus.
This process is called logic synthesis, not compilation.

HDL and programming language are similar but different.
Think of it like writing a function that maps the signal state of registers to another signal state, triggered by a clock or input signal.
If you want to experience real reactive programming, I suggest you try writing an HDL.
Please also remember to write HDLs, always worrying about whether the signal propagation of the HDLs you write really ends up in one clock.
Otherwise, the behavior of your circuits would be incomprehensible to humans.

The hardest part of the actual development was that this logic synthesis took a ridiculous amount of time.
It was not uncommon for us to have to wait up to 30 minutes after starting the synthesis,
so once I started the synthesis,
I was often playing Smash Bros. Melee with the other CPU guys who were also waiting for the synthesis to finish.
FYI, my character was Sheik.

## Late December to mid-January - Learn by porting Xv6 to MIPS

We began to find the answer to “What kind of CPU features required for operating system?”

After the OS team was born, we started weekly rounds of Xv6 source code reading.

At the same time, I started porting Xv6 to MIPS.
This was partly to learn how an OS works at the implementation level, and partly because there appeared to be no Xv6 port to MIPS.
I completed the port until the process scheduler started in about a week.
I did a lot of research on MIPS during this porting process,
and on x86 to understand how xv6 works.
Thanks to that, I understood mechanisms around interrupts and MMU at the implementation level.
At this stage I got a solid understanding of the CPU functionality required for Xv6.

Also, in mid-January, we worked hard to compile the entire Xv6 code by commenting out the various parts.
As a result, Xv6 on the simulator of our homebrew architecture showed the first message of the boot sequence,

xv6...
cpu0: starting...

At the same time, this meant that by this time Ucc had already grown enough to compile most of xv6, which was awesome.2

## February - our CPU, GAIA was born!

In the MIPS port, I completed the initialization of the PIC, which was a real pain,
and also completed the implementation of the interrupt handler.
As a result, the porting of Xv6 to MIPS was completed until just before the first user program started.

Based on this experience, I made the draft specifications of the interrupt and virtual address translation for our homebrew CPU.
In order to keep it simple, we decided to omit hardware privilege mechanisms like Ring protection.
For virtual address translation, we decided to use a hardware page-walking method, just like x86.
It may seem difficult to implement in hardware, but we thought it was cheaper if we sacrificed the speed and omit TLB implementation.
After all, Yuichi made an excellent CPU core later, and it installed TLB from the beginning though.

Yuichi completed the overall design of the ISA of our CPU.
He named our CPU GAIA.
In typical CPU experiment projects, we don’t implement interrupt nor MMU.
However, Yuichi started to implement them for Xv6, based on the refactored version of the CPU of Group 3.

I’ll note the weekly records as the rapid progress begins from then on!

## 1st Week

Instead of just commenting boot sequences out, Masayoshi started implementing actual initialization of our CPU,
and Shohei rewrote the x86 assembly of Xv6 into our homebrew architecture’s.
I added interrupt simulation capability to our simulator which Wataru had made in the core part of CPU experiments,
and also completed support for virtual address translation.
This gave the simulator enough functionality to run the OS.

## 2nd Week

I made a primitive linker for our architecture to assemble Xv6 and its binary blobs.
Shohei was working on implementation of the interrupt handler, which was a tough part.
Interrupts are hard to understand, hard to figure out the flow, hard to debug, and hard to develop.

When I ported Xv6 to MIPS, I had GDB, so it was rather OK, but our own simulator didn’t have any debug features, so it must have been very difficult to debug.
Shohei couldn’t bear the difficulty of debugging, so he added a disassembler and a debug dump function to the simulator.
After this, the simulator’s debugging features were rapidly upgraded by the OS team, and finally the simulator grew to look like the following picture.

## 3rd Week

Overcoming various difficulties, the porting of Xv6 was advanced, but Xv6 still did not work.

Especially, the specification of Ucc thatcharandintare both 32 bits caused a lot of troubles.
That was not Ucc’s fault.
Actually, the C specification only requiressizeof(char) == 1andsizeof(char) <= sizeof(int), so this was legal.

However, xv6 is written for x86,
so it assumessizeof(int) == 4and adds constants to the value of the pointer, which caused a lot of inconsistencies.
Because the bug created by this was so hard to find and the amount was also large,
it was decided to ask Ucc to makechar8 bits after all.

After delegating the char 32-bit problem to the Ucc team,
I wrote the initialization of paging of the first entry stage, and tried to get the interrupts to work properly by trial and error.

The bottom line is that we worked hard to fix the challenge #4, “Low portability of Xv6”.

## February 27,28

When I reread the slack, I can see that a lot of progress was made on this day.
After the Ucc team very quickly finished the change to makechar8-bit,
we worked hard on a lot of debugging.
Finally, our first user programinitworked!

After that, we made more and more progress in porting the user process applications that I hadn’t yet gotten to in the port to MIPS.
On the way, many bugs that were hard to reproduce or inadequacies in the interrupt specification were found and fixed,
, but we got over it somehow.

One interesting errata we fixed is the cache alias issue.
GAIA CPU chose a virtual address instead of a physical address as the cache index.
This is because it allows you to skip the virtual address translation to look up caches.
However, due to that, we found that inconsistency happened between caches, because multiple caches of virtual addresses could point to the same single physical address.
When the cache of one virtual address was updated, the caches of other virtual addresses pointing to the same physical address were not updated.

This bug was hard to fix on the hardware side at low cost, so we fixed it by introducing “Page Coloring” in our Xv6.
This introduces “color” for each cache line, and allocates pages so that virtual addresses pointing to the same physical address will always get the same color.
This means virtual addresses pointing to the same physical address will always have only one cache.
This allowed Xv6 to ensure that GAIA never had multiple caches which shared the same physical address.

## March - Xv6 Runs!

On 1st, the xv6 port is complete. xv6 was now running on the simulator…!

### There should be no shortage of entertainment

Originally, the Xv6 port was meant to be fun, and since Xv6 started working on the simulator, we worked hard to add a lot more fun.

First of all, a mini curses is created by Masayoshi in about 4 hours and theslcommand run on our Xv6.

Shohei kind of wanted to do a Minesweeper.

During this period, Yuichi completed the implementation of the CPU of the Group X.
The real CPU ran much faster than the simulator, which made the game easier to play and develop.
At this time, a very high quality application, 2048, was created.

This 2048 was very high quality.
Yuichi played with it all the time.
Incidentally, the 2048 uses non-line buffering input, but xv6 originally did not have this feature.
To support this feature,ioctlwas added as adevswaction in addition toreadandwrite,
and newtermios-related features to controlICANONandechowere added.
So the only Xv6 that can play 2048 with such a high degree of completeness is the one on GAIA.

By the way, for a V6-inspired Xv6, I guess addinggttyandsttysystem calls is a more Unix V6-like approach.
However, I adoptedioctlbecause Xv6 doesn’t have the concept of tty, and becauseioctlwas introduced in the next version, V7, which is close in history.

Now, as something a little cooler, Xv6-GAIA has a small assembler made by Keiichi.
Also it has a mini vi that Shohei made.
Guess what you can do with these two.

It’s interactive programming on an FPGA!
This is a pretty impressive demo for a CPU experiment, which usually doesn’t include any interactive program.

## The greatest demo

The original task of the CPU experiment was “Run the given ray-tracing program on your homebrew CPU”.
Now that you’ve got an operating system running on your CPU, you know what you’re supposed to do, right?
We decided to run the ray-tracing program “on the OS “on our own CPU.
We had a few bugs, but we managed to finish it an hour before the final presentation.

So, we did what every student in the history of our department has probably joked at least once:
Run an operating system on a CPU, and ran the ray-tracing program on top of it.

## Looking back from 2020

What I’ve written so far is essentially a rewrite of my own blog post I wrote in 2015.
While reading it now, I can see a lot of my technical inexperience at the time, what we did then is definitely exciting.

By the way, you can see what our Xv6 looked like at that time on your browser right now fromhere!
After the CPU experiment, I ported our GAIA simulator to JavaScript by Emscripten.
Let’s try oursl,minesweeper, and2048.

xv6...

cpu0: starting

init: starting sh

$

 

 

 

 

Let me also tell you that the porting of Xv6 to MIPS,
which wasn’t finished at the time of the CPU experiment,
was finished a month after the experiment.
TheGitHub repository is here.

After we posted a blog post about the Group X challenge in 2015, later generations of students continued to take on new challenges around OS.

In 2018, some students ran their own OS on top of a home-built CPU,
and in 2019, a group of students ran their own OS while adopting RISC-V for their home-built CPU ISA.
In addition, the group in 2020 finally ran Linux on top of a homebrew CPU that also adopted RISC-V as its ISA.3

I’m sure there will be many more stories in the future,
so everyone please look forward to them.
Personally, I look forward to someone running Linux on their own ISA someday, or running a VM on it.

Reinventing the wheel is generally said to be something to be avoided, but there’s quite a bit to learn from actually doing it.
It made me realize that I didn’t understand it as well as I could implement it from scratch.
Plus, I recommend it to you because, above all, it’s fun to die for!

That’s the end of the story of our CPU experiment. If you’re interested in reinventing the exciting wheel, please try building a CPU or porting an OS to it.

Lastly, I would like to summarize the members of the Group X.

* Takaya Saeki- It’s me. Xv6 (Xv6 GAIAandXv6 MIPS)
* Shohei Kobayashi-Xv6
* Masayoshi Hayashi-Xv6
* Keiichi Watanabe-Ucc
* Wataru Inariba-Ucc,CPU simulator
* Yuichi Nishiwaki-GAIA,Ucc
* Masaki Waga-FPU
* Ryuichi Kiryo- Random tasks

1. If you can read Japanese, you can read my past posthere.
I’m working at Microsoft, and not all colleagues read Japanse. So, I’m writing this English post.↩︎
2. Keiichi once told that one of the reasons they could grow Ucc so rapidly was that they wrote Ucc by OCaml.
OCaml allows you to manipulate tree structure so easily without any pointer bugs.
In addition, of course that’s because they are awesome.
BTW, for those who’re interested in the preprocessor part, we used Clang’s CPP.
Did you know Clang’s CPP can be used as a standalone command?Keiichi has written his article about the compiler team in Japanese.↩︎
3. The all articles are written in Japanse.
The articlesof the group who ran their own OS on top of a home-built CPU in 2018,The group ran their own OS with their RISC-V CPU in 2019,
andthe group in 2020 who ran Linux on their RISC-V CPU.↩︎
