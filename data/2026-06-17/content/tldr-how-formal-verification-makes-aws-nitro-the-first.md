---
title: How formal verification makes AWS Nitro the first formally verified cloud hypervisor - Amazon Science
url: https://www.amazon.science/blog/ec2s-formally-verified-isolation-engine-provides-mathematical-assurance-of-virtual-machine-isolation
site_name: tldr
content_file: tldr-how-formal-verification-makes-aws-nitro-the-first
fetched_at: '2026-06-17T12:27:25.013891'
original_url: https://www.amazon.science/blog/ec2s-formally-verified-isolation-engine-provides-mathematical-assurance-of-virtual-machine-isolation
date: '2026-06-17'
published_date: '2026-06-10T15:00:00'
description: 330,000 lines of machine-checked proofs in Isabelle/HOL verify that the Nitro Isolation Engine correctly enforces confidentiality, integrity, and memory safety between EC2 virtual machines on Graviton5.
tags:
- tldr
---

Automated reasoning

# EC2’s formally verified “isolation engine” provides mathematical assurance of virtual-machine isolation

## Splitting the “separation kernel” off from the rest of the Nitro security system and using only a subset of the Rust programming language to code it enabled its formal verification.

By 
Dominic Mulligan
, 
Nathan Chong

 June 10, 2026
 

7 min read

Share

* Copy link
* Email
* X
* LinkedIn
* Facebook
* Line
* Reddit
* QZone
* Sina Weibo
* WeChat
* WhatsApp

 分享到微信
 

x

 Overview by Amazon Nova
 

* The Nitro Isolation Engine is the core component of the Nitro Hypervisor, the first formally verified hypervisor deployed in a commercial cloud environment, ensuring correct behavior and enforcement of isolation between virtual machines.
* The formal verification of the Nitro Isolation Engine was achieved using the Isabelle/HOL proof assistant, resulting in 330,000 lines of machine-checked mathematics, comparable in scale to the seL4 project.
* The verification process involved creating a formalization of a core subset of the Rust language (μRust), using Separation Logic for specifications, and applying weakest-precondition calculus for proofs, all part of the open-sourced AutoCorrode library.
* The verification addressed four types of properties: confidentiality and integrity, functional correctness, absence of runtime errors, and memory safety, with confidentiality and integrity treated separately using noninterference and indistinguishability preservation.
* The Nitro Isolation Engine is designed for a commercial cloud environment and is an always-on feature for Graviton5 users, providing unprecedented visibility into how isolation is enforced.

Was this answer helpful?

Today we announced the general availability of the new M9g and M9gd instances of Amazon Web Services’ (AWS’s) Elastic Compute Cloud (EC2), the first instance types powered by Graviton5, the latest generation of our general-purpose CPU. Graviton5 doubles the number of cores from the previous generation, from 96 to 192.

They’re also the first instance types to use the new Nitro Isolation Engine, a component of the Nitro Hypervisor whose sole job is isolating virtual machines (VMs) from each other. In this post, we explain how we used theIsabelle/HOL (higher-order logic) proof assistant— software that mechanically checks reasoning steps for adherence to the laws of logic — to prove that the Nitro Isolation Engine behaves correctly and enforces isolation between virtual machines. The Nitro Isolation Engine is the critical component of the first formally verified hypervisor to be deployed in a commercial cloud environment.

Our Isabelle/HOL model and proof comprise 330,000 lines of machine-checked mathematics. It’s comparable in scale toseL4, the landmark project that first demonstrated that realistic operating-system verification was feasible and was an inspiration for our own work. However, unlike seL4, the Nitro Isolation Engine is designed for a commercial cloud environment and ships on production hardware as an always-on feature for Graviton5 users.

Our talkat Amazon’s 2025 re:Invent conference introduces our formal-verification methodology, and ourwhite paperis a more detailed discussion covering important aspects of the results, such as scope and assumptions. This blog post gives an informal overview of the main aspects of our formal-verification work and how they fit together.

## What is a separation kernel?

John Rushby coined the term “separation kernel” in 1981 to describe a minimal OS component that partitions a system into isolated compartments. The key idea: separatepolicyfrommechanism. A separation kernel does not decide what to isolate, how to allocate resources, or which VMs to schedule: those decisions are made elsewhere. Instead, it focuses solely on enforcing isolation, and this clarity of purpose makes separation kernels much simpler to implement than full OS kernels.

Since its introduction in 2017, the Nitro Hypervisor has been responsible for enforcing isolation in EC2, but it also handles business logic, device drivers, and AWS-specific features. That complexity makes proving correctness much more difficult. Moreover, the Nitro Hypervisor was not designed for verification from the start.

Distilling the hypervisor’s critical isolation logic into a minimal component, the Nitro Isolation Engine, makes it small enough to verify and audit, giving customers unprecedented visibility into how isolation is enforced. We also wrote the Nitro Isolation Engine in Rust, a language that lends itself more naturally to formal verification.

The Nitro Hypervisor still handles policy — VM creation, resource allocation, migration, scheduling — but it is now deprivileged and must ask the Nitro Isolation Engine to perform any operation touching guest state. The Nitro Isolation Engine checks every request before acting.

System architecture of a Nitro-Isolation-Engine-enabled server.

## Specifications and proofs

The two key parts of our work are specifications and proofs. Formal specifications precisely capture the expected behavior of the system, and proofs establish that the implementation meets those specifications.

Our theorems about the Nitro Isolation Engine address four types of properties:

1. Confidentiality and integrity.Only authorized information flows can occur. For example, guest memory allocations are always scrubbed before reuse.
2. Functional correctness.The implementation behaves exactly as specified.
3. Absence of runtime errors.There are no runtime errors such as unwraps of None option values in Rust — an erroneous command invocation that will stop program execution.
4. Memory safety.There are no issues such as buffer overflows and NULL pointer dereferences.

In practice, we handle the last three properties collectively, as a functional-verification result, with confidentiality and integrity treated separately, because we use different proof techniques for each.

## Functional verification

For functional verification, the key parts are a formalization of a core subset of the Rust language, called μRust (“micro Rust”); an expressive specification language using Separation Logic for precisely capturing specifications; and a verification technique, weakest-precondition calculus, with custom proof automation for proving a program correct with respect to its specification. Each of these is part of a general-purpose proof infrastructure that we open-sourced in 2025 as theAutoCorrode library.

In more detail, μRust is a restricted subset of the Rust programming language that is expressive enough to write the Nitro Isolation Engine but amenable to formal reasoning because we deliberately excluded advanced Rust features, such as traits and dynamic dispatch. The formal semantics of μRust is defined as ashallow embeddingin Isabelle/HOL, which means that the meaning of μRust is defined in terms of higher-order logic, the “host language” of Isabelle/HOL.

The specification for a μRust program is defined as a contract with pre- and postconditions, which are assertions about the system state before and after executing the program. Our contracts specify “total correctness”, which means that in all states that satisfy the precondition, the program always terminates, and the resulting state satisfies the postcondition. This total-correctness condition also means the program is memory safe and free of runtime errors. Our specifications are written usingSeparation Logic, a logic designed to reason about low-level pointer-manipulating programs.

Despite the relative simplicity of separation kernels, with the verification of the Nitro Isolation Engine we are still operating on the edge of what is possible with formal verification, and both our specifications and proofs grow very large. For example, the following specification captures what happens when an executing guest virtual CPU tries to turn itself on (an erroneous request):

Specification of PSCI_CPU_ON, a power state function for turning on a target CPU.

While the specification above is complex, what it captures is intuitively straightforward: in this circumstance, the Nitro Isolation Engine sees that, to act as the caller, the virtual CPU must be turned on already, and it therefore returns a defined error code,AlreadyOn. Everything else about the system state remains unchanged. The complexity in the specification is a reflection of the depth of our modeling and the fact that several other error checks must already have been performed for us to have reached this point in the implementation of the Nitro Isolation Engine.

To prove a μRust program correct with respect to its specification, we use a standardweakest-precondition calculus. A weakest-precondition calculus is a systematic way to identify the least restrictive constraint that can ensure that the state of a program after a particular operation is not outside some specified range of states. For example, the weakest precondition of the expression "x + y" is the state in which the values ofxandycannot overflow the addition. The proof obligation then is to show that the contract’s precondition entails the computed weakest precondition.

## Confidentiality and integrity

For confidentiality and integrity, the first key part is a high-level specification that captures the behavior of the Nitro Isolation Engine as a transition relation, where each “high-level” step of the system (e.g., hypercall) is an atomic transition. This specification is rigorously connected to the more concrete Separation Logic specification used in our functional-verification results, which uses another proof idea called Refinement. The second key part is the idea ofnoninterference.

Noninterference is the idea of indistinguishability preservation that we use to make confidentiality and integrity mathematically precise. The idea is that if two states are indistinguishable to an observer before a step, they must remain indistinguishable afterward. The intuitive reason why this captures confidentiality is that the observer has learned nothing new because of the step.

Understanding why indistinguishability preservation guarantees confidentiality is subtle. Consider two simple machines, A and B, each with one public and one private register. An observer considers them indistinguishable if their public registers match: the private register is hidden. In the following diagram, A and B are indistinguishable:

An example of a confidentiality violation.

Now consider what happens if we execute a program that branches on the private register to assign 1 to the public register. The resulting machines A' and B' now have different public registers — they'redistinguishable!A clever observer could use this to deduce the original private values, and this failure to preserve indistinguishability corresponds to illicit information flow to the observers.

## And more to come

We hope you’ve enjoyed this overview of the main pieces of our verification work. There are many other aspects to our work, such as conformance testing and how we handle reasoning about concurrent code, that we’re excited to share in future posts.

 Research areas
 

* Automated reasoning
* Cloud and systems
* Security, privacy, and abuse prevention

 Tags
 

* Formal verification
* Provable security

About the Author

Dominic Mulligan

 Dominic Mulligan is a principal applied scientist with Amazon's Automated Reasoning Group.
 

Nathan Chong

 Nathan Chong is a principal applied scientist with Amazon's Automated Reasoning Group. His work focuses on the correctness of concurrent systems code, particularly at the hardware-software boundary.