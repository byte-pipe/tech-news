---
title: Proofcraft News - 2026
url: https://proofcraft.systems/news-2026/#2026-08-21
site_name: hackernews_api
content_file: hackernews_api-proofcraft-news-2026
fetched_at: '2026-08-25T06:00:22.011964'
original_url: https://proofcraft.systems/news-2026/#2026-08-21
author: snvzz
date: '2026-08-24'
published_date: '2026-01-01T12:00:00+10:00'
tags:
- hackernews
- trending
---

# Proofcraft News - 2026

News from other years:

2025

2024

2023

2022

2021

21 Aug 2026

## seL4 security proofs now complete on AArch64

After completing the proofs offunctional correctnessandintegrity,
Proofcraft has now established the proof that seL4 enforcesconfidentialityon
AArch64, providing a formal mathematical proof that the kernel prevents an
application running on top of seL4 from learning information without
authorisation.

Thanks to continued support fromNCSC, this milestone completes the formal
proof that the seL4 implementation code on AArch64 enforces security isolation
of the applications running on top (under the assumptions listedhere). This
isolation prevents attacks on non-critical applications from propagating to
critical applications and compromising them.

24 Jul 2026

## Proof Engineering and Theory at LICS'26

The paperThe Algebra of Iterative Constructionsby Kevin Batz,
Benjamin Lucien Kaminski, Lucas Kehrer, Gerwin Klein, Henning Urbat, and Todd
Schmid was presented at the 41st Annual Symposium on Logic in Computer Science
(LICS) in Lisbon this week. This paper in theoretical computer science is
about an algebraic abstraction and reasoning principles for the iterative
construction of fixed points. Fixed points are a recurring theme in computer
science with many famous results such as the Kleene fixed point theorem. The
algebra shown in this paper allows expressing such theorems concisely and
enables reasoning about them in an abstract and streamlined way that can be
implemented efficiently in proof assistants such as Isabelle/HOL, which
Proofcraft is using for the verification of the seL4 microkernel.

The highly automated Isabelle/HOL implementation of iteration algebra in this
paper resulted from a spontaneous collaboration between Proofcraft’s Chief
Scientist Gerwin Klein and Benjamin Kaminski that started at the IFIP Working
Group 2.3 (Programming Methodology) meeting in Athens in 2025. It shows that
proof engineering ranges from practical application all the way to deep theory.

29 Jun 2026

## MCS seL4 now verified! (for RISC-V)

Proofcraft achieved a significant milestone in theseL4verification roadmap
that was years in the making: the MCS configuration of seL4, providing support
for mixed-criticality systems, is now proved to be correct on RISC-V.

This configuration is the largest new seL4 feature, indispensable for mixed
criticality real-time applications such as automotive use cases. It contains
wide-ranging changes to the kernel’s implementation and API. Its verification
therefore required considerable effort and has been a priority in the seL4
roadmap for a long time.

Proofcraft has now completed, for the very first time, the verification of
functional correctness for seL4 with MCS. Functional correctness is the largest and most central
proof in theseL4 verification stack. The proof targets the RISC-V architecture
and will now be ported to the Arm 64-bit architecture, as part ofDARPA’s PROVERS program.

1 Jun 2026

## Dynamic Domain Scheduler for seL4

Proofcraft delivered the implementation and formal proof of more flexible
domain scheduling inseL4.

Before the change, the seL4 security proofs, and in particular the proof of
information flow enforcement, required a fully static schedule that was
compiled into the kernel. This meant that, when using seL4 to enforce the
information flow boundaries between applications, developers were required
to provide a fixed predetermined amount of time for each domain, for the
entire lifetime of the running system. This strict policy made it hard to apply
information flow control in practice and to support in SDK-style development such
as theMicrokit.

Proofcraft proposed a new seL4 runtime API (Application Programming Interface)
allowing the loading of semi-static domain schedules. This means that a system
with information flow protection can go through different phases at runtime that
can satisfy different domain timing requirements. For instance, a boot phase of
the system can have longer time slices to allow virtual machines to start
without overrunning their domain time allocation, and an operational phase of
the system can provide shorter time slices so that each domain can be responsive
to outside interaction. Additionally, an SDK-based system such as the Microkit
can use the new API to set a domain schedule at boot time.

This new seL4 API is implemented, verified and available in seL4 15.0.0.

21 May 2026

## June Andronick Keynote at CDIS Spring Conference in Stockholm

On May 21st 2026,CDIS– Swedish research Center for Cyber Defense and
Information Security – held itsspring conferenceat KTH Royal Institute of
Technology in Stockholm.

Proofcraft CEO June Andronick was one of the two keynote speakers, alongside
August Martens from Mistral AI. June gave an overview of formal verification for
cybersecurity, and participated in a panel on Digital Sovereignty.

28 Apr 2026

## Proofcraft presenting at the Cyberagentur Milestone Research summit

In April 2026, Germany’s Cyberagentur held a Milestone Research summit to
present the progress and outcomes of its funded programs, including theEcosystem trustworthy IT research program (ÖvIT), which Proofcraft is arecipientof, partnering withKry10.

Proofcraft’s Chief Scientist Gerwin and Kry10’s Chief Scientist Martin
Dehnel-Wild presented the progress on the Dyvercon project, to deliver
dynamism, performance, and proof for complex cyber-physical systems. In
particular, Gerwin reported on Proofcraft’s work on extending theseL4proofs to support a static multikernel configuration, where applications can
benefit from the use of multiple CPU cores for performance, while at the kernel
level a separate instance of seL4 run on each core.

Gerwin additionally gave a general introduction to formal verification and
overview of its use in the real world.

17 Apr 2026

## Proofcraft is a proud sponsor of the seL4 summit 2026

Proofcraft is happy to be supporting the2026 seL4 summitas a Silver sponsor.

The seL4 summit is an annual international gathering of participants from
industry, government and universities with interests in the world’s most highly
assured OS kernel. Attendees and presenters include the creators and maintainers
of the seL4 technology such as the Proofcraft team.

This year’s seL4 summit will be held in Vancouver, Canada, on Sep 1-3, 2026.

14 Apr 2026

## 5 years of Proofcraft. 5 years closer to a verified future.

On the 14th of April 2021, we created Proofcraft. Five years later, we are so
busy working for a verified future that we have not posted news for a while.

Much has happened, and more is to come. For now, here are some posts from our
back log of news items with technical highlights that Proofcraft has been
delivering.

Firstly, the seL4 proofs are nowsupported on 100% of Arm platformsthat the
kernel can run on. With this significant progress towards reducing the reliance
on experts, users of seL4 can now choose freely between the supported Arm
platforms and always be sure they use a verified code base. This work is part of
DARPA’s PROVERS program.

Secondly, seL4 on AArch64 now provably enforcesintegrity: We have a formal
mathematical proof that the kernel prevents an application running on top of
seL4 from modifying data without authorisation. And the work on security
theorems goes on: thanks to continued support from NCSC, we are close to
completing the confidentiality property, and with that the entire security proof
stack for the 64-bit Arm architecture.

Much more is happening, with three large projects going on in parallel, funded
byDARPA,CyberagenturandNCSCrespectively. Stay tuned for more!