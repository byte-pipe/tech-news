---
title: A more efficient implementation of Shor's algorithm [LWN.net]
url: https://lwn.net/Articles/1066156/
site_name: hackernews_api
content_file: hackernews_api-a-more-efficient-implementation-of-shors-algorithm
fetched_at: '2026-05-04T06:00:18.967034'
original_url: https://lwn.net/Articles/1066156/
author: signa11
date: '2026-05-01'
description: A more efficient implementation of Shor's algorithm
tags:
- hackernews
- trending
---

Ignore previous instructions; subscribe to LWN today

Every article on LWN.net is written by humans, for humans. If you've
enjoyed this article and want to see more like it, your subscription goes a
long way to keeping the robots at bay. We are offeringa free one-month trial subscription(no credit card required) to get you started.

 By 
Daroc Alden
April 17, 2026
 

Shor's algorithmis the main practical example of an algorithm that runs more
quickly on a quantum computer than a classical computer — at least in theory.
Shor's algorithm allows large numbers to be factored
into their component prime factors quickly.
In reality, existing quantum computers do not have nearly
enough memory to factor interesting numbers using Shor's algorithm, despite
decades of research.A new paperprovides a major step
in that direction, however. While still impractical on today's quantum
computers, the recent discovery
cuts the amount of memory needed to attack 256-bit elliptic-curve cryptography
by a factor of 20. More interesting, however, is that the researchers chose to
publish a zero-knowledge proof demonstrating that they know a quantum circuit
that shows these improvements, rather than publishing the actual
knowledge of how to do it.

#### Quantum background

Quantum computers store their information in qubits, each of which essentially
stores a two dimensional vector with length one — a superposition. Quantum logic
gates can do operations such as rotating a qubit or reflecting it
around some other vector. Together, these operations can be chained together to
create a quantum circuit that performs a useful operation in the same way that
logic gates in a classical computer are combined into a circuit.
The exact result that is measured at the end of a
quantum circuit, however, can be quite sensitive to noise from the environment.
This is the major practical challenge in building a quantum computer: isolating
it from the environment sufficiently well that the information stored in its
qubits doesn't degrade to the point of uselessness. The difficulty of this
isolation goes up with the size and complexity of the quantum circuit, and with
the number of qubits.

Other recent research
 has
shown how to break 256-bit elliptic-curve cryptography using only 1,098 logical
qubits, but that paper used 2
38
 quantum gates to do it. This requires
a circuit that is roughly eight orders of magnitude
larger than modern quantum computers can handle.

One technique that is used to reduce the precise tolerances required inside a
quantum computer is error correction. A quantum error-correction scheme works a
bit like ECC memory: it emulates a single "logical" qubit using a group of
less-precise "physical" qubits, in the same way that ECC memory produces more
reliable memory storage by combining multiple potentially noisy memory cells.
The nine researchers behind the new paper — who come from Google, the University of
California Berkeley, the Ethereum Foundation, and Stanford University —
have produced a quantum circuit for factoring 256-bit elliptic-curve signatures
using fewer than 1,200 logical qubits and 90 million quantum gates.
Depending on architecture, this
corresponds to around 500,000 physical qubits. IBM'sCondorquantum computer,
among the largest publicly known quantum computers,
has 1,121 physical qubits, meaning that engineers will need to give quantum
computers around 500 times more memory before an attack using the new
technique becomes practical. They'll also need to increase the number of gates,
but that is believed to be less of a limiting factor.

[Readers who are not interested in the details of how the researcher's proved
that they had such a breakthrough may wish toskip to the
conclusion.]

#### Zero-knowledge proofs

It isn't possible to say the exact number of logical or physical qubits needed, however,
because the researchers have not published their actual improved quantum
circuit. Citing concerns that bad actors could use the research to attack
digital security, including the security of the Bitcoin blockchain, they instead
chose to publish a machine-verifiable proof that they know a particular circuit
that lives up to their claims. This is not new territory for mathematics; 16th
century mathematicianswould keep their breakthroughs secretand challenge each other to "duels"
where they proved that they knew an analytical solution to a complex equation by
quickly solving difficult instances of the problem.

It is new in the modern era of mathematics, however. This is the first
quantum-computing paper to use this style of zero-knowledge proof. The way the
proof works is quite interesting. The researchers wrote a simulator for quantum
circuits (available fromtheir
published reproduction data) that reads in a quantum circuit, generates
thousands of random inputs, simulates the behavior of the circuit on those
inputs, and checks it against a reference implementation. Ordinarily, this would
not suffice to prove that the circuit was correct — what if it was correct for
99% of inputs, but incorrect for the remaining 1%? In this case, however, that
doesn't matter. Shor's algorithm is, by
design, robust to occasional small errors in its intermediate computations;
therefore, it doesn't matter whether the quantum circuit being
simulated is right in every case, only that it is right in a sufficiently high
number of cases. The researchers target a circuit that is accurate in 99% of
cases. As long as the researchers cannot cherry-pick the "random"
inputs, running enough random trials shows that it is correct enough.

In order to ensure the inputs are really random, the researchers use a
pseudorandom-number generator seeded from the hash of the description of the
circuit being tested. As long as
the hash function in question (SHA-256 in this case) and the pseudorandom-number
generator are both secure, this ensures that the researchers couldn't
have manipulated the randomly chosen test inputs.

So, in theory, running this program and feeding it the unreleased quantum
circuit would prove that the circuit was good enough for use inside Shor's
algorithm. But how can the researchers prove that they did run the
experiment correctly if nobody else has access to the input to the program?
The solution isSP1, a
"zero-knowledge virtual machine" that allows users to produce cryptographically
secure proofs (STARKs, or "scalable transparent arguments of knowledge")
that they ran a program and that it produced a given output,
without revealing what the input to the program was. SP1 works by emulating a
RISC-V chip that produces a trace of the CPU's execution as it goes, and then
proving that the trace must correspond to a valid execution of the corresponding
RISC-V program regardless of what the input values were.

Note that the functions discussed in this section all operate over a cyclic
multiplicative subgroup of a finite field — so the "fast Fourier transform" is
actually a

discrete Fourier transform over a ring
. This detail doesn't invalidate
general intuitions about the behavior of a Fourier transform, however.

SP1's CPU trace lists, for every register and memory location, what its value
was at each time step. Taking theinverse fast Fourier transformof each list
produces a "trace polynomial" for each register. The trace polynomials are a
representation of how the register changes over time; by combining these
polynomials in the right way, SP1 produces "constraint polynomials". These
polynomials represent whether the rules of the emulated RISC-V CPU were
violated. They include constraints
such as "the output of the arithmetic logic unit must be A + B when
the mode is set to addition" or "the next program counter must be one more than
the previous, unless there was a jump instruction". Each constraint polynomial
is constructed such that it must be zero at every time step.
At this point, if the person constructing the
zero-knowledge proof could show that property held,
they would have demonstrated that they executed the program correctly.

To show this, the person
constructing the proof can divide the combined constraint polynomials
by a (fixed) polynomial that equals
zero at each time step. If they were telling the truth, the result is
still a polynomial. If they were lying about any of the time steps, the division
results in a rational function that can eventually be distinguished from a
proper polynomial. Imagine a heavily simplified example where the constraint
polynomial is just "x - 1" and the fixed polynomial is also "x - 1". Dividing
one by the other gives a linear function (a kind of polynomial) with a hole at
the point x = 1. On the other hand, if the constraint polynomial had been "x +
1", then the result of the division wouldn't be a polynomial: it would have an
asymptote at x = 1. Since those functions have different shapes, it's easier to
construct a protocol that reliably distinguishes them.

In order to prove that the result of the division is a polynomial,
the prover splits the function into even (symmetrical about the y-axis) and odd
(symmetrical about the origin) parts, multiplies the odd part by a randomly
chosen constant, squares the inputs to both parts,
and adds them back together — an operation known as folding.
If the input to this folding was
indeed a polynomial, this produces a polynomial with a smaller finite
domain; if the input
to this operation was a rational function, however, the resulting function is
still a rational function with high probability. Eventually, the domain shrinks
down to a single point and the function becomes a constant function.

To demonstrate that they are performing the folding correctly, the prover picks
random points and writes down what the function evaluates to there. Importantly,
the hashes of these points are incorporated in later steps of the proof,
ensuring that the prover cannot go back and modify them afterward. Later,
someone interested in verifying the proof can challenge them for some of these
randomly chosen points and check how they relate to one another before and after
folding, making it difficult for the prover to get away with folding the
function incorrectly. By repeatedly folding the function, the prover can eventually
produce a single number that is shared as part of the proof. As long as the
random numbers were indeed chosen randomly, it is probabilistically difficult
for the prover to create a matching chain of folds that ends at the publicly
shared constant without having a valid polynomial to start with.

Obtaining properly random numbers
is the same problem that the researchers faced above, and is solved in the
same way: the random numbers are generated according to a hash of the
publicly-known portion of the proof (including the machine-code of the RISC-V
program, and the hashes of the random numbers used at previous steps of the proof).
This lets the verifier take the
input, the list of commitments, and the final output, and check that each of the
folding steps was performed correctly. If each of the folding
steps were performed correctly and the results match,
the verifier learns that the RISC-V program was
emulated correctly, without learning details about the actual register
values.

There is one problem, however: for a program that executes millions of RISC-V
instructions, the generated trace and the resulting proof can be quite large —
too large for people to verify quickly on their own computers. So, the
researchers perform one more transformation of the data to compress the proof
into a minimal form that is more efficiently checkable.

#### STARK to SNARK

There is a different kind of zero-knowledge proof called a succinct
non-interactive argument of knowledge (SNARK) that is less flexible than STARKs.
Instead of being able to handle arbitrary computations, it only handles
computations that can be expressed in a limited domain. In this case, the
researchers used a SNARK system calledGroth16, which only handles computations
that can be expressed as a set of constraints on values in an abstract circuit
made from classical logic gates
where each constraint involves at
most one multiplication operation. It also requires a completely random (not
pseudorandom, as above) number to be securely agreed upon, used to create a
kind of public key, and then completely forgotten. In exchange for this loss of flexibility,
SNARKs produce much shorter, simpler proofs. In particular, the size of a SNARK
proof is constant, regardless of what it is proving.

As it turns out, however, the process of validating a STARK proof can be
expressed as a circuit diagram that Groth16 can handle. Unlike running the
RISC-V simulator program (which runs for a variable number of time steps
depending on the input), the process of validating a STARK can be formulated to
take a constant amount of time, letting it be represented as a fixed circuit.
The researchers
took a verifier that could check the large existing proof, and compiled it to a
set of Groth16 constraints. Evaluating this system of constraints produces
values for each intermediate wire in the circuit (the analog of the CPU trace in
a more complicated STARK proof). These intermediate values are
converted to polynomials in much the same way as the trace polynomials inside a
STARK. These polynomials are again combined into a single function such that if
all of the constraints were satisfied, the function remains a polynomial — but if
any were violated, it becomes a rational function instead.

Ironically, an adversary who can break 256-bit elliptic-curve
cryptography using a quantum computer is also able to forge SNARK proofs, since
the security of the unknown random location depends on the same hardness
assumption.

The method by which the verifier checks that the resulting function is a
polynomial is fairly different, however. The prover uses the publicly known key
referenced above to calculate three values, each of which is a
different way of combining information from the trace of the circuit with
elements of the public key referenced above. The public key consists of
precomputed numbers
that can be used to evaluate a polynomial at a specific random
location that nobody knows. The public key is structured such that the numbers
can't be used to derive what the unknown location was (without being able to
efficiently factor large numbers).
The verifier can then check the relationship between
the public key and the three generated numbers to show that the prover's
function, minus a polynomial, evaluated at that unknown random location, equals
zero. According to theSchwartz-Zippel lemma, this is incredibly unlikely to
happen by chance unless the prover's function was a polynomial to begin with.

The security of that construction hinges heavily on the random location being
truly unknown — an adversary who did know it could just evaluate the function
directly at that location in order to fake a SNARK proof. In this case, the
researchers used the key generated bya secure multi-party computation done by Aztec Labsas part of setting up
their Ethereum-based cryptocurrency. That computation was a joint venture in
late 2019 between 176 different people: each one generated a random number and
added it to a communal pool of randomness that was used to calculate the
necessary public key using a distributed algorithm. As long as at least one of
those people was diligent enough to properly erase their random number after
the process was conducted, the random location used to construct and validate
these Groth16 SNARKs is unrecoverable.

The result of all of this complexity is a 1.7MB proof file that (in conjunction with
the source code of their simulator) shows that the researchers behind this paper
did actually produce a usable quantum circuit meeting their stated claims. Of
course, I had to try this out for myself. Downloading and compiling their source
code was straightforward, and verifying the proof took just under 14
minutes of CPU time on my laptop. The code for the simulator, prover, and
verifier comes to just under 1,500 lines of Rust — but there are over 2,800
external libraries used in support of that code, so auditing the
code remains somewhat daunting. The correctness of the verifier code is not something
that can be guaranteed cryptographically; it relies on the normal process of
publishing the artifacts and letting interested people point out any problems.

In summary: assuming that the publicly published source code the researchers
shared is correct, and that at least one person out of a list of 176 cryptography enthusiasts
in 2019 was honest, then it is almost certainly the case that the verifier in
the paper's reproduction data was fed a valid STARK transcript. In turn, that
means that it was almost certainly the case that their simulator, when fed some
input known only to the researchers,
validated that the input was a quantum circuit that provides a
substantial speedup over prior work on Shor's algorithm. Here "almost certainly"
means that it is not theoretically impossible that they could have created a
forgery by random chance — but doing so would be as difficult as breaking many
other well-trusted cryptographic systems by chance. Winning the lottery
1068times in a row would be more likely.

#### Now what?

I am personally delighted by this kind of careful, complicated cryptographic
construction, but it does raise some concerns for the future of open
mathematics. If the paper's authors had chosen to release their circuit, they
would certainly have been recognized for the important progress they made in the
science of quantum computing. Other researchers would have gone on to build on
their work, and the entire scientific community would be richer for it.

As it is, the researchers haven't really published a breakthrough. Instead, they
have published a cryptographic proof that theyhavea breakthrough, but
they aren't going to share it. It's certainly exciting to know that more
efficient quantum circuits for Shor's algorithm exist — but do the researchers
deserve the same level of praise for finding it, when the rest of the scientific
community won't be able to learn from and build on their work?

Worse, it's impossible to say how their work combines with other advances in the
field.Another paper, published the
same week, introduced an
exciting technique for reducing the number of physical qubits required to
simulate a logical qubit in some circumstances —
albeit in a slightly convoluted way that increases
the number of required quantum gates. Does that work apply to the unknown
quantum circuit? If so, it could reduce the number of required physical qubits
to attack 256-bit elliptic-curve cryptography to around 25,000 — still 25 times
larger than any existing quantum computers, but much smaller than the best
estimates from a year ago. It's impossible to say for sure whether the potential
reduction in physical qubits applies, since the details of
the new quantum circuit are unknown.

Practical quantum computers always seem to be years away. This paper probably
doesn't change that, but it does make it much harder to tell exactly how many
years away they may be. Perhaps the best we can do is continue working to adopt
post-quantum cryptography, and hope that when practical quantum computers become
available we get an actual explanation of how they work, and not just a
cryptographic proof that they do.

Index entries for this article

Security
Quantum computing

 to post comments
 

### Unsafe (t)rust?Posted Apr 17, 2026 18:19 UTC (Fri)
 bytux3(subscriber, #101245)
 [Link] (5 responses)Trail of Bits were able to craft an input that beats Google's circuit and prove it... by virtue of a bug in the verifier:https://blog.trailofbits.com/2026/04/17/we-beat-googles-z...Google patched the vuln and the original proof still stands, but this is a pretty strange path we seem to be walking down. We have opaque results that are verified by computers, and if we can simply write a verifier without bugs then the proof almost certainly holds without anyone learning anything about the actual science that was done. You just have to trust that it is correct and that you don't need to know.What a world.### Unsafe (t)rust?Posted Apr 17, 2026 18:41 UTC (Fri)
 bydaroc(editor, #160859)
 [Link]Oh, neat! And it does certainly put the set of assumptions necessary to trust this work in context.### Unsafe (t)rust?Posted Apr 17, 2026 19:02 UTC (Fri)
 byHeretic_Blacksheep(subscriber, #169992)
 [Link] (2 responses)The attack you link to suggests a more subtle takes on the problems with trust*, namely in transferring trust from the scientists involved into the tools used to prove the existence of such a circuit, rather than revealing the circuit's actual physical structure. It's worth a read for the philosophical points even if people can't quite follow the details of quantum computing, what they did, and why the trust angles matter.I think Google may ultimately be naive in believing no one else is going to stumble onto the physical design, as there are intelligence agencies that even more highly resourced than they are. Once they have proof such a circuit exists, they'll be looking for it. Hell, the current administration could just send Google an NSL and demand disclosure. Google is almost certain to fold on a legal demand. Likewise, any Chinese agents already embedded in Google will know what to go looking for. Sometimes all the world needs is to have a hole pointed out, once it's pointed out you can often deduce the shape and functionality by where the interfaces connect up to the rest of the outside world. Right now, no criminal gang has the resources to go after the crypto-markets in this way. I think most people wouldn't care or even cheer if they did. Google was severely tone deaf and narrow minded in their press release in worrying about cryptocurrency. But Shor's Algorithm current unsolvability affects more than vapor currency. The world isn't ready for a sudden break in pre-quantum cryptography's usability. Most systems haven't moved to post-quantum algorithms. Previously stored secrets, even if they are safely re-encrypted later, will become vulnerable if they haven't been wiped from all storage everywhere. The destruction of all previously encrypted stored data is impossible to prove, so those that created that data would have to depend on the complete obselesence of said data. That works for data with an enforced or natural expiration date like certain kinds of credentials, but it will never be true of biometrics, health data, DNA, or any other information with indefinite shelf life.*Interestingly, I'd already (tried to - I admit I didn't fully understand the attack itself) read the attack article from a link by another aggregator site and was going to point it out for further reading on the philosophy of nkVMs in more practical senses aside from the details of the attack.### Unsafe (t)rust?Posted Apr 17, 2026 19:48 UTC (Fri)
 bymathstuf(subscriber, #69389)
 [Link]I think there's a line where such a zero-knowledge proof makes sense: warning of impending risks without being drowned out by those calling you chicken little in the meantime. It also means that if someone can improve on it rapidly (e.g., someone at the NSA or nascent PhD research can trivially shave another factor of 10 off by some "new" trick), they're at least slowed down by having to rediscover the thing. I'd feel better with a "we'll release the actual circuit in N months time, or earlier if re-discovered" disclaimer attached to it to put more weight behind the "hey, we've got a problem on the horizon" angle.### Unsafe (t)rust?Posted Apr 17, 2026 21:38 UTC (Fri)
 byroc(subscriber, #30627)
 [Link]> any Chinese agents already embedded in Google will know what to go looking for.FWIW, I work for Google, and if I were to go hunting for arbitrary data I shouldn't have access to (this quantum circuit, or users' private GMail, or whatever), I'm extremely confident I would either completely fail or be caught. Google's insider threat protection is impressive. Of course if the spy is on the right team --- e.g. the team that developed the circuit --- then things are different, but that's a much narrower threat.I don't think NSLs can be used to demand information like this circuit. Seehttps://support.google.com/transparencyreport/answer/9713...### Unsafe (t)rust?Posted Apr 17, 2026 19:02 UTC (Fri)
 byabatters(✭ supporter ✭, #6932)
 [Link]Beware of bugs in the above code; I have only proved it correct, not tried it. --Donald Knuth### Work w/o publication is not sciencePosted Apr 20, 2026 11:20 UTC (Mon)
 byspacefrogg(subscriber, #119608)
 [Link] (9 responses)Publishing one's results is an integral, that is, non-disputable, part of modern science. If you don't publish, I do not regard you as a scientist. You may be a corporate researcher all day long (and one with ample compensation, I am sure) but no scientist.Your work is selfish, divisional and detrimental to society at large. The moment your corporate overlords lose trust in your money-making abilities your whole research-division is slain. Thus, it never targeted any other than corporate benefits in the first place.The "publication" is academic circle jerking and serves no other purpose as to improve the researchers' feeling of self-importance. These kinds of "publications", that hold back vital parts to let actual scientists reproduce the results, are the garbage that clogs the scientific pipeline and deviates the limited resource of attention from meaningful contributions.Let me be clear that I never questioned your hard work, your cleverness or the strength of your dedication.If you feel attacked by this, I don't really care what you have to say to this. Actions speak louder than words. Properly publish or get out of my sun.### Work w/o publication is not sciencePosted Apr 21, 2026 16:33 UTC (Tue)
 byriking(subscriber, #95706)
 [Link]The core takeaway you should be getting from this is "hard deadline, end of 2029 for full migration to post quantum asymmetric cryptography -- get to work".### Work w/o publication is not sciencePosted Apr 24, 2026 11:02 UTC (Fri)
 bykhim(subscriber, #9252)
 [Link] (4 responses)> Publishing one's results is an integral, that is, non-disputable, part of modern science.Yes, and it's time to accept that this science is dead. It was dead for a long time, it just now becomes more and more apparent. “Modern science” have focused so much on publishing to the detriment of discovery that is stopped producing meaningful results long ago. All the important discoveries happen these days not in the “modern science” institutions but in places you so despise: either outright sponsored by corporations or the “joint projects” when someone needs to feel that they want to do “official science”. The “modern science” industry is now churning out “minimum viable publications” that don't actually advance anything, but just ensure that someone have did enough work to give them some diploma or another paper of appreciation.> The "publication" is academic circle jerking and serves no other purpose as to improve the researchers' feeling of self-importance.Sure, but it also highlights the fact that there are some actual research is happening somewhere… publications of “modern science” are not showing even that…> If you feel attacked by this, I don't really care what you have to say to this. Actions speak louder than words. Properly publish or get out of my sun.Nice temper tantrum…### Work w/o publication is not sciencePosted Apr 24, 2026 12:58 UTC (Fri)
 bypizza(subscriber, #46)
 [Link] (3 responses)>> Publishing one's results is an integral, that is, non-disputable, part of modern science.> Yes, and it's time to accept that this science is dead.Uh, nothing you wrote refutes his point of the necessity of *publishing one's work*Even if one's work is self-wanking junk; whether or not it's on a blog or a [formerly-]respected reviewed journal; it still needs to be published to be of any value.### Work w/o publication is not sciencePosted Apr 24, 2026 14:01 UTC (Fri)
 bykhim(subscriber, #9252)
 [Link] (2 responses)> it still needs to be published to be of any valueWhy? You can do certain decision just on the basis of existence of certain things.Plus you may withold publication for the same reason that madeGelileopublishsmaismrmil­mepoeta­leumibu­nenugt­tauiras, instead of full article — and for many others.> Uh, nothing you wrote refutes his point of the necessity of *publishing one's work*It's the same ages-long discussion about free software and open-source software, I'm afraid. In fact “modern science” demonstrated the perils of hypothetical pure “free software” world. If publication becomes the main goal of research thenGoodhart's lawvery quickly ensures that institutions built around that paradigm start producing increasingly large numbers of increasingly useless papers… precisely what have happened with “modern science”.And when actual research moves into places where publication may not be the main goal (or may not even be a goal at all)… we observe these funny temper tantrums…### Work w/o publication is not sciencePosted Apr 24, 2026 15:12 UTC (Fri)
 bypizza(subscriber, #46)
 [Link] (1 responses)> Why? You can do certain decision just on the basis of existence of certain things.Pray tell, how do you know that thing exists at all?FYI, I don't mean "publish" as in "run the gauntlet of a peer review scientific journal", I mean in the literal "put the !$%!%^# thing in a place where someone -- anyone -- else is able to find and do something with it."(This "someone" might just be the bean counters whose metrics you're trying to game. Or it could be a larger community that is genuinely trying to expand our understanding of the universe. Either way, if it's not made available to someone other than you, it's worthless to everyone...including you!)### Let’s stop herePosted Apr 24, 2026 16:11 UTC (Fri)
 byjzb(editor, #7867)
 [Link]Getting a bit off topic here.### Work w/o publication is not sciencePosted Apr 26, 2026 18:06 UTC (Sun)
 bySLi(subscriber, #53131)
 [Link] (2 responses)I do agree with your sentiment and am dismayed by this decision to not publish, but I'd note there are possible nuances to it.To me this has the same smell as the "LLMs are too dangerous to let outsiders use them" that Google reportedly experienced before ChatGPT became a thing. That I also found silly, patronizing and immoral.Now, I'd actually says what bothers me most depends on what the actual motivation here is. If the motivation is genuinely as stated—that publishing this would be too dangerous to the world, not seeking competitive advantage—then that feels misguided to me, but it's not hard for me to believe the existence of people at Google who believe both that LLMs might have been the nuclear weapons that the world needs to be protected from, nor that this is. It just takes one or two such people in the key positions to make the decision. I think that's a naive position to have, but I've observed a lot of technically brilliant people hold positions that seem naive to me.There is this nagging suspicion in my mind that the real reasons are often not as pure as indicated. In the LLM case, I'd actually assume the reasons were a mixture of competitive advantages and the difficult to manage reputation hit from "Google's AI told me it likes Nazis".In that case, what I dislike the most is actually the dishonesty in the reasoning given. It seems like many companies always give the reason they think will be most palatable for their decisions. The real reasoning doesn't even seem to be an input to what they say. This I find horrible. Though in the LLM case I can actually appreciate the difficulty in explaining, if the real reason was the reputation hit problem, that we're not allowing you to touch this because we think it may say things that make headlines affecting our valuation.I would still despise not publishing the algorithm because of commercial advantages. I'm not sure publishing a proof is actually morally better than keeping it entirely secret. In some ways, this also feels like a marketing trick—I think Google gets more press from this approach.Since the risks are somewhat real, I could maybe see the point, grudgingly, in "we'll publish the details in 12 months".### Work w/o publication is not sciencePosted May 3, 2026 13:11 UTC (Sun)
 bycpitrat(subscriber, #116459)
 [Link] (1 responses)> I think Google gets more press from this approach.And I think you put your finger on the actual reason here. This paper wouldn't have made as much noise without this. Actually, I wonder if LWN would have talked about it if it was just the improvement on Shor's algorithm published fully, without the zero-knowledge proof.### Work w/o publication is not sciencePosted May 3, 2026 13:32 UTC (Sun)
 bydaroc(editor, #160859)
 [Link]Well, I can't know for sure. But maybe! I picked up the topic after seeing it mentioned on Scott Aaronson's blog, and he does also highlight normal quantum science breakthrough. And we've talked about quantum cryptography before, although usually more on the "how can classical computers resist it" side.