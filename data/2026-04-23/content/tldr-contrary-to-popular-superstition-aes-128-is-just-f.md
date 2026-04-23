---
title: Contrary to popular superstition, AES 128 is just fine in a post-quantum world - Ars Technica
url: https://arstechnica.com/security/2026/04/contrary-to-popular-superstition-aes-128-is-just-fine-in-a-post-quantum-world/
site_name: tldr
content_file: tldr-contrary-to-popular-superstition-aes-128-is-just-f
fetched_at: '2026-04-23T11:59:26.559244'
original_url: https://arstechnica.com/security/2026/04/contrary-to-popular-superstition-aes-128-is-just-fine-in-a-post-quantum-world/
date: '2026-04-23'
published_date: '2026-04-21T12:35:20+00:00'
description: A stubborn misconception is hampering the already hard work of quantum readiness.
tags:
- tldr
---

Text
 settings

With growing focus on the existential threat quantum computing poses to some of the most crucial and widely used forms of encryption, cryptography engineer Filippo Valsorda wants to make one thing absolutely clear: Contrary to popular mythology that refuses to die, AES 128 is perfectly fine in a post-quantum world.

AES 128 is the most widely used variety of theAdvanced Encryption Standard, a block cipher suite formally adopted by NIST in 2001. While the specification allows 192- and 256-bit key sizes, AES 128 was widely considered to be the preferred one because it meets the sweet spot between computational resources required to use it and the security it offers. With no known vulnerabilities in its 30-year history, a brute-force attack is the only known way to break it. With 2128or 3.4 x 1038possible key combinations, such an attack would take about 9 billion years using the entire bitcoin mining resources as of 2026.

## It boils down to parallelization

Over the past decade, something interesting happened to all that public confidence. Amateur cryptographers and mathematicians twisted a series of equations known asGrover’s algorithmto declare the death of AES 128 once a cryptographically relevant quantum computer (CRQC) came into being. They said a CRQC would halve the effective strength to just 264, a small enough supply that—if true—would allow the same bitcoin mining resources to brute force it in less than a second (the comparison is purely for illustration purposes; a CRQC almost certainly couldn’t run like clusters of bitcoin ASICs and more importantly couldn’t parallelize the workload as the amateurs assume).

On Monday, Valsorda finally channeled years’ worth of frustration, fueled by the widely held misunderstanding, into ablog posttitled “Quantum Computers Are Not a Threat to 128-bit Symmetric Keys.”

“There’s a common misconception that quantum computers will ‘halve’ the security of symmetric keys, requiring 256-bit keys for 128 bits of security,” he wrote. “That is not an accurate interpretation of the speedup offered by quantum algorithms, it’s not reflected in any compliance mandate, and risks diverting energy and attention from actually necessary post-quantum transition work.”

That’s the easy part of the argument. The much harder part is the math and physics that explain it. At its highest level, it comes down to a fundamental difference in the way a brute-force search works on classical computers versus the way it works using Grover’s algorithm. Classical computers can perform multiple searches simultaneously, a capability that allows large tasks to be broken into smaller pieces to complete the overall job faster. Grover’s algorithm, by contrast, requires a long-running serial computation, where each search is done one at a time.

“What makes Grover special is that as you parallelize it, its advantage over non-quantum algorithms gets smaller,” Valsorda said in an interview. He continued:

Imagine it with small numbers, let’s say there are 256 possible combinations to a lock, A normal attack would take 256 tries. You decide it’s too long, so you get three friends and you each do 64 tries. “That’s the classical parallelization. With Grover you could in theory do √256)=16 tries in a row, but if that’s still too long and you again look for help from three friends. Each has to do √256/4)=8 tries.

So in total you do 8*4=32 tries, which is more than the 16 you would have done alone! Asking for help to parallelize the attack made the attack slower overall. Which is not the case for classical attacks.

Of course the numbers are way larger, but if we apply any reasonable constraint on the attacker (like having to finish a run in 10 years), the total work becomes so much more than 264.

Also, 264was never the right number, because that pretends you can do AES as a single operation on a single qubit. This is somewhat orthogonal. The combination of these two observations turn the actual cost into 2104give or take, which is well beyond the threshold for security.

Sophie Schmieg, a senior cryptography engineer at Google, explained it this way:

With a normal brute force search, if I interrupt it halfway through, I have roughly a 50% chance of it already being successful. So I can have two computers doing the search, each over 50% of the keys, and be done in half the time. But with Grover’s, if I interrupt halfway through, the probability of getting the correct answer is only 25%. So instead of using two computers on half of the search space, I now need four.

So if you look at coreseconds, the classical algorithms cost what they cost, independent of how many computers you use in parallel. You can increase cores and your time goes down by the corresponding amount. But with the quantum algorithm, coreseconds are not independent of the parallelization strategy. Having more cores does not reduce the time by the same amount, to the point that if you went to the maximally parallel instance where each QC has to check only a single key, you need 2128QCs, and not 264, i.e. you’re no better than classical.

Valsorda’s post provides a more mathematically detailed explanation, as doesthis video.

Valsorda listed a litany of sources that support the assertion that AES is perfectly acceptable in a post-quantum world, including from the National Institute of Standards and Technology (here,here, andhere), the German Federal Office for Information Security (here), and Samuel Jaques, an assistant professor in the Department of Combinatorics and Optimization at the University of Waterloo (here).

The exception to these recommendations is spelled out in the NSA’s version 2 of the Commercial National Security Algorithm Suite, which mandates AES 256. Valsorda said requirements for 256-level security were in place even in the predecessor algorithm suite, and weren’t specific to quantum readiness. “As far as I can tell, its intention is to avoid the very same fragmentation introduced by security levels by picking one oversized primitive for all settings.”

He further said 256-bit AES is also warranted in certain cases, such as to avoid the possibility of collisions, in which two keys randomly end up equal because of thebirthday paradox.

So the next time you hear someone say quantum computing reduces the security of AES by a factor of two, kindly remind them that’s a superstition that’s distracting engineers from the real and considerable work in preparing the world for the advent of CRQC. It’s a tall enough order updating asymmetric algorithms known to be vulnerable toShor’s algorithm, which breaks them in polynomial time, specificallycubic time, a massive advantage compared with the exponential time provided by today’s classical computers.

“Conflating necessary and unnecessary changes will cause needless churn and take resources away from the urgent updates,” Valsorda argued. “We’re lucky we can leave the symmetric cryptography (sub-)systems untouched; we should take that blessing and focus on the work that actually needs doing, which is plenty.”

 Dan Goodin
 

Senior Security Editor

 Dan Goodin
 

Senior Security Editor

 Dan Goodin is Senior Security Editor at Ars Technica, where he oversees coverage of malware, computer espionage, botnets, hardware hacking, encryption, and passwords. In his spare time, he enjoys gardening, cooking, and following the independent music scene. Dan is based in San Francisco. Follow him at 
here
 on Mastodon and 
here
 on Bluesky. Contact him on Signal at DanArs.82.
 

1. 1.Anthropic tested removing Claude Code from the Pro plan
2. 2.Mozilla: Anthropic's Mythos found 271 security vulnerabilities in Firefox 150
3. 3.Indian med student rakes in thousands with AI-generated MAGA hottie
4. 4.Investors lost billions on Trump’s memecoin. Another gala won’t fix that.
5. 5.Great white sharks are overheating

Customize