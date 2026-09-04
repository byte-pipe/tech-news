---
title: On solving the Jane Street Reverse Engineering Challenge | jestoph’s tech blog
url: https://jestoph.com/2026/09/04/jane-street-challenge.html
site_name: hnrss
content_file: hnrss-on-solving-the-jane-street-reverse-engineering-cha
fetched_at: '2026-09-04T14:48:04.286764'
original_url: https://jestoph.com/2026/09/04/jane-street-challenge.html
author: Jestoph
date: '2026-09-04'
published_date: '2026-09-04T00:00:00+00:00'
description: 'Or: Why do I always do things the hard way?'
tags:
- hackernews
- hnrss
---

Share on: 

Or: Why do I always do things the hard way?

Jane Street periodically puts out challenges, and this one thoroughly nerd-sniped me and sent me down a month-long rabbit
hole that I’m only now emerging from. This post is an overview of how I solved it with a combination of hard-headedness
and sleep deprivation. It’s going to be decently technical, but in future posts I’ll go over the specifics of each
step if people are interested.

For some background I’d recommend looking at the original post on the Jane Street blog here -Can you reverse Engineer an ASIC?

And if you ever want to read the (terrible) code I used for this challenge, you can find it at my github pagehere

## Challenge Accepted

I have an engineering degree rotting away somewhere in my brain, so a lot of the words of the challenge
are familiar. The challenge is to take an ASIC and work out what it does. For those unfamiliar, an ‘ASIC’ is an
Application-Specific Integrated-Circuit, which is a fancy word for what we’d usually call a ‘Computer Chip’.
Firms like Jane Street presumably design these to get extra performance relative to the equipment you can buy from
a normal manufacturer.

In any case, the challenge is to take a ‘GDS’ file describing a chip, and work backwards to understand what it does,
and then I guess maybe there’s a password in there or something. I didn’t, and still don’t, know what ‘GDS’ stand for.

There’s two parts to the challenge - one is a warmup where you’re given a lot more information (like the actual design of
the chip), and the real puzzle where you’re given a firm handshake and a ‘good luck’ as you face the increasing prospect
of not sleeping for the next three weeks.

### What’s in the files?

For some reason, I like to do things the hard way so rather than doing any research I just started poking around in the files.
I can see there’s some familiar words in them like like ‘clk’ (clock), ‘rst’ (reset) and ‘VGND’ (Ground Voltage) and ‘VPWR’ (Power Voltage).

And there’s a bunch of …. something with a prefix ofsky130_fd_sc_hd__followed by things that sound like logic element, like
‘or’ and ‘not’ and things like that. I guess that’s what I’ll need to pull out of the file?

I found there’s a really nice library ‘gdstk’ in python that seems to be able to read them. It tell me that there’s 27
elements on the warmup puzzle. A good start!

% python3 -c 'print(len(__import__("gdstk").read_gds("warmup/04_final.gds").cells))'
27

There’s also a ‘vcd’ file for the main puzzle, which is a text file, and I guess is a simulation input or output or something.
I didn’t, and still don’t, know what ‘vcd’ stands for. I can see some suspicious entries in it that look like ASCII characters.
I play around with it, writing a small C program, and get the output ‘TRY AGAIN’. Ah, so the circuit has messages in it somehow!

$ gcc what-is-this-thing.c && ./a.out
T R Y A G A I N T R Y A G A I N

Ok we’re on to something

## Getting Distracted and wasting my time. And my life.

Here we need to do a huge digression and of course build our own circuit simulator. For reasons.

You can skip this section. I sure wish I did.

### Several days later

Ok so I built a circuit sim using sqlite3 as a driver. Quite neat really. But it’s quite hard to design circuits in Python!
If only there was a language for describing hardware.

### Several days later

Ok so I built a parser for my new language and now I can design circuits. But I need to test them! If only there was some
way of scriptings inputs and validating outputs.

### Several days later

Ok so I built a harness for my circuit simulator. But it’s really hard to visualise what it’s doing! If only there was…
well you see where this is going

### Several days later

Ok so I gave up on writing a wave form viewer and decided to just use ‘surfer’. But these gds files are hard to
work with, how can I make that easier?

### Several days later

Ok so I wrote a basic GDS viewer in raylib but I can’t get the blocks to sit quite the way I want to. So anyway,
I realised I’m down too many tangents and it’s time to drop all of the custom software.

Ok we’re done with that section. Aren’t you glad you skipped it?

## Focus, Chris, Focus.

The Jane Street blog actually points to quite a handyGDS Viewer, so I spent
some time just looking at it real hard and hoping something would come to me. I was able to roughly annotate what
I though were which inputs, and I could later confirm that by looking through the approximate locations of wires
in the files. Because this was the warmup I could compare what I knew about the circuit against what I could see.

### What do these files represent?

These files seem to have some sense of ‘layers’ of different types of material or something, I imagine it’s a bit like a
big 3d-printer that has to be told where to move the print head, and at what depth it needs to put a new material.
Maybe these files are close to the instructions to the machine? But rather than having arbitrary positions in vertical
space they seem to have standard layers of standard widths so that simplifies things.

I wanted to prove that I could at least operate on these files, so I tried to extract the Jane Street logo on the
upper right corner. Somehow this was way harder than I thought and I ended up extracting everythingexceptthe
Jane Street logo? But whatever good enough, lets move on.

I also at some point work out that the library I’m using can extract the elements to SVG file formats, and it includes
a bunch of text describing the parts of the elements. This will be key to actually understanding the challenge because
I can maybe use that information to work out which parts are inputs and outputs.

### Time to actually read about these elements

I’ve gotten as far as I can with guessing. Time to actually read some proper documentation.
Looks like this is their official home, despite the ‘unofficial’ in the name -sky130-unofficial

The docs had the answers to many of my questions. Why do I always do things the hard way?

It turns out that this ‘sky130’ thing is like a … standard? Or something for making chips. I guess making chips is hard,
and so it makes sense for there to be common design elements. Crucially it also contains the descriptions of what the
elements do, which is easy for elements like ‘and’ that are probably an ‘and gate’ but less clear for a ‘o21bai’ which is a
…. well don’t worry too much about that.

Using the information from the docs and the labels from the SVG I can now theoretically map specific geometry to the I/O of
the circuit elements, which I guess will be the first step to turning it into a ‘real circuit’. I get really lucky here,
in that my library has the ability to check if two elements overlap in 2d space (remember these gds files are actually a
description of a 3d geometry).

I wasn’t sure how reasonable the assumption of the labels overlapping the correct locations, but it worked way better than
I expected! I guess labels are already referenced on their centerpoint! It even picked up some geometry that isn’t visually
connected so a visual inspection would never have revealed their connections. And looking at the total design’s
IO ports, it’s so much less visually noisey.

## I think I can make a graph now?

I think I have what I need now to extract a circuit from this gds file. This isn’t going to be easy. This thing has 1k
paths and almost 17k polygons even after ignoring everything I don’t care about.

I need to find a way of finding things that are ‘touching’, which means that they are on adjacent layers and also overlapping.

My algorithm is pretty terrible, but it does the job for now. I also introduce a simplification step where I take
all of the ‘wire segments’ and …. compress? or coalesce? them into a single wire. The logic is, that if two wires are
touching then they’re actually the same wire from my perspective.

Luckily I spent several weeks grinding leetcode last year while unemployed so a few graph algorithms weren’t going
to slow me down.

### Many days later

The next few days of work were not easy. In my working log I have recorded that “By beating my bloodied face against
the keyboard for several hours and cursing how long I’ve already spent on this, I’ve managed to nail down a tricky bug”.
I’m not exactly sure what that bug was now, but I’m sure it deserved it.

I’ve started to be able to turn my network in to real descriptions of hardware in a language called ‘Verilog’,
which also allows me to run basic simulations like checking that ‘turning this pin high makes that one go low’. I’m
eventually able to extract all the components into a handful of spaghetti, and I spend time manually drawing out
the connections.

I don’t use any tooling (other than excalidraw, my drawing program). I mostly just look at it real hard until things
make sense. Again, I do things the hard way

Not pictured: Sanity

But in any case I now had an understanding of the major components of the warmup puzzle - two shift registers (that shift
things), an adder (that adds things) and a comparitor (that compares things) and I work on trying to simulate the outputs.
I know that the input needs to sum to be 496 as the comparitor is namedcomparitor496so I just need to put in the
correct sequence of bits to achieve that. That’s just simple maths, the hard part was trying to get all the various parts
all working together in a single simulation.

If only there were some way of doing this that didn’t involve trading off my sanity for progress.

A few hour later and it’s done! I finally got this thing to work!

It’s at this point I knew I had a chance of solving this thing, but it was a race against the clock, and my immune
system was starting to give out.

## On to the real puzzle

The real puzzle has many more component types (81 vs 20 or so) and many more of them (almost 10k vs 1k) so this
won’t be easy. I was able to quickly get most aspects of my scripts working from the warmup steps, so long as I
dropped all validation. Which is not ideal but it was only temporary. More annoying is that the process of extracting
the circuit takes almost a whole minute instead of two seconds.

### Initial work

I was able to get a little win by rearranging my wire segment gathering step so it is now 100x faster (3.4 second
down to .03 seconds). It has byte-for-byte compatible behaviour so I’m pretty confident it hasn’t introduced any
bugs. However the major slow step still swamp this improvement - finding all connected components takes almost a
whole minute. Luckily I have a lot of confidence in that step after the nightmare of the warmup puzzle, so I don’t
have to run it too often

### Extracting the real puzzle

It took a long time, but I added implementations of all of the 40 or so new components that I need in the real puzzle
by just manually copying them from the documentation site. In retrospect I’m sure I could have copy-pasted it from
somehwere, but (in case you haven’t been paying attention) I like to do things the hard way.

After that, and some quality-of-life improvements around being able to add names or aliases to wires, I was able to
build and run a simulation of the real puzzle. It didn’t work, but still, I think that means I’m in with a shot of
solving this thing.

### Is there a bug?

One annoyance I had is that I had to disable my validations, but it’s hard to make progress without validations
as it’s easy to introduce bugs without noticing until hours or days later. So I went back to trying to turn them
back on. For example I had a validation step that checked that all wires are actually connected to something.

I found in one section of my simulation that I had an undriven wire, meaning that its value was completely unknown
to my simulator. That’s a bit strange really, because even if you don’t care about the value of a wire you’d
typically just drive it to some known value rather than not connecting it at all. I assumed it was a bug in
my pin-detection logic, but by visual inspection I could see that my code was correctly picking up a wire that’s
only connected to two input pins.

Even stranger, the circuit has a connection on a neighboring pin that isn’t even an input or an output! Maybe
there’s a bug here and it should be connected to one of the inputs? Given how little I understand, I sheepishly
reported it to Jane Street.

The next day I had an email confirming that I was right! But luckily it shouldn’t have an impact on the actual results of
the challenge. I quite sincerely think this bug report might be one of my coolest technical achievements.

### Looking from a bird’s eye view

I spent a long time mapping out sections of subcircuits and the wires connecting them, and things started to
fall in to place. I worked out that the section that feeds the ‘success’ wire has 6 wires, so now the challenge
is slightly reduced to ‘how do I make those 6 wires go high?’, and luckily it seems like two of them do it
after a certain number of clock cycles, so really it’s only 4 wires.

I can see other patterns too. The left-most subcircuits seem to act like a signal generator which then feeds in
to other sections of the circuit. So maybe the ‘password’ is hidden inside the structure of these elements?

Combining the three, I can see it gives 121 or 120 clock transitions before the output goes high. That matches
the waveform in the provided example, so maybe you need to have the password correct in 120/121 clocks otherwise
you get the message?

This section seems to feed the rest of the circuit, so this might be the start of a clue.

I was now able to get each sub-section to run in a simulation but not really do anything useful. I then started
working on connecting all the sub-components into one large circuit.

### It turns out I’m an idiot.

I wasn’t able to get my overall sim working at all for 2 or 3 days, even though I’d quite thoroughly tested
each sub component. Well, it turns out that I had forgotten to set the ‘reset’ pin, so the whole thing was effectively
disabled, kind of like forgetting to turn the car on and wondering why you’re not going anywhere.

I fixed that and immediately saw ‘TRY AGAIN’ as expected. Success!

Even more interesting is, I deleted the input I was feeding to the circuit and I found it had other messages too:

Input

Output

Wrong Answer

TRY AGAIN

All 0’s

EMPTY SKY

All 1’s

BIG BANG

Correct Answer

TBD

## The doldrums

I’ve now reached the hardest part of this challenge. I’ve found that the input to this circuit is 120 bits, and I have
no idea how to progress. I considered exhaustively checking every input but that would unfortunately take more time
than any of us have on this planet.

### Wire-by-Wire

I follow the output wire back directly, but the complexity of the inputs are too much for me. I need some new
approach. At some point in my notes I ask the question ‘what if I run the simulation in reverse?’, and I start
mulling on this idea.

The thing is, I know where I want a signal to be and I know what the inputs need to be at that point.

So then if I take one step back in time I can re-write the desired output as a functions of the previous step.

This is like a recurrance relation, but I actually know what I want the output to be on step 120, and I know
that the circuit starts with all outputs at zero. So theoretically this is solvable in some mathematical sense.

Hopefully the picture below explains a bit better what I mean

I focus on a shift register component as it’s closest to the one I solved in the warmup puzzle (which is a nice touch
of pedagogy, so thank you Ben and Anish!). There’s some tricky constraints actually, I can tell it depends on previous
values in the shift register, this probably needs some constraint solver to solve. Constraint solvers are notoriously
complicated to understand, but luckily I know the perfect tool

### On using a spreadsheet to write verilog

I’m sorry for the abomination that I’m about to show you.

Yes, that’s a spreadsheet that I used to write verilog that I then fed in to my simulated circuit. Surprisingly,
under the hood spreadsheets are actually incredibly sophisticated constraint solvers. I dumped the output into a
Verilog file, and ….. it worked! At least for two wires. It does look like this approach will be
underpowered in general because it relies on me eyeballing the output and toggling bits here and there until all my
checks go green. But it did prove that this approach of solving it backwards has legs.

It’s time to bring out the big guns and learn to use a constraint solver.

### This …. isn’t as hard as I expected?

I remembered reading about constraint solvers onHillel Waynes blog(who has a new book out you should go buy! I’ve got my copy), but I’d always been intimidated because they
use big words like ‘constraint’ and ‘solver’ and I just need a thing to solve the constraints in my - ooooh I get it!

I ended up using a tool called ‘z3’. It’s kind of magical? Every time it finds a solution I get a surge of joy. You
tell it things like ‘This wire can never be low’ or ‘This wire has to be high at step 120’ and it either finds how
it can do that, or tells you it can’t be done. I was able to give it thousands of constraints in the end and it
would find solutions in the blink of an eye.

Debugging it is a bit of a nightmare though, and mostly seems to involve me thinking real hard and deleting lines
until it starts working again. I did get a bit of a sense for the sort of outputs it liked to produce - in particular
if I didn’t specify starting points it would just choose whatever was convenient for it (and inconvenient for me)

Annoyingly I did a lot of the translation work from my circuit in to z3 by hand. I’m not quite sure why I did it that
way other than I had gotten sick by this point and I didn’t trust myself to write a transformation script.

I went one-by-one on the wires I cared about. There are about 24 that I need to be high at the same time and I was able to
get 22 of them relatively easily in isolation by a combination of using the solver and sometimes just guessing a bit and
validating them in isolation.

### It turns out I’ve done this the hard way, as is characteristic.

It turns out the structure of the inputs to many of the element appears to just need two pulses at a multiple of
11, determined by the value of a counter. If I’d just looked at the inputs a bit longer instead I might have worked it
out, but I was in too deep looking at the lower layers rather than looking around at what I could see right in
front of me.

### The Answer. It’s done

I now combined all of my constraints in to a single giant script and set about squashing the bugs. There were a few,
but by 10pm instead of an error I got the following output -

% python3 solver.py
Solution!
verilog saved to 'out.txt'

My hands started shaking because by this point the only way it could have a solution is if it had the answer.

I loaded it in to my simulator, run it, and there it is. The answer -(* TWO STARS *)

I emailed Jane Street, and the next morning I had my confirmation so I can now add it to my table of outputs -

Input

Output

Wrong Answer

TRY AGAIN

All 0’s

EMPTY SKY

All 1’s

BIG BANG

Correct Answer

~TBD~ 
(* TWO STARS *)

## What next?

Well I don’t really know what to work on next, I really enjoyed this challenge but I also have other hobbys such as
‘getting to bed before 3am’. But Jane Street did mention they might have a new challenge coming out in a couple of months,
so stay tuned!

If you have any suggestions for fun projects, let me know either on Hacker News or by email.

And if you’re in Sydney and found this interesting, get in touch and we can grab a coffee.

<
Blog Archive
Archive of all previous blog posts

>
Blog Archive
Archive of all previous blog posts