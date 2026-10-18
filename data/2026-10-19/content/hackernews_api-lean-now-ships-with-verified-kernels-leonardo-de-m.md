---
title: Lean Now Ships with Verified Kernels — Leonardo de Moura
url: https://leodemoura.github.io/blog/2026-10-15-lean-now-ships-with-verified-kernels/
site_name: hackernews_api
content_file: hackernews_api-lean-now-ships-with-verified-kernels-leonardo-de-m
fetched_at: '2026-10-19T09:16:24.509138'
original_url: https://leodemoura.github.io/blog/2026-10-15-lean-now-ships-with-verified-kernels/
author: Leonardo de Moura
date: '2026-10-16'
description: Leonardo de Moura — Creator of Lean and Z3
tags:
- hackernews
- trending
---

# Lean Now Ships with Verified Kernels

 2026-10-15

AI agents are very effective at finding vulnerabilities in our software. This includes the kernel (the proof checker) of the Lean proof assistant. See our two recent postmortems (August 1,August 24). We are strengthening the official kernel, adding new kernels, and building new tools that simplify rechecking your Lean developments with external kernels. Leanv4.35.0comes with thelake checkcommand. This command exports your development and rechecks it withleanchecker, the official Lean kernel without all the baggage around it. The whole process runs inside a sandbox. You can disable the sandbox usinglake check --inadvisably-no-sandbox. Lean now ships with four additional kernels:nanoda,lean4lean,con-leche, andcon-ron. You can recheck your development with all of them using the commandlake check --paranoid. In this mode, we also run a variant of the official kernel built with a hardened memory allocator, which turns memory corruption into a checked abort instead of a silently wrong answer.

Con-leche is the first kernel for Lean written in Lean and proven consistent. It was implemented and proven consistent by Claude (Fable and Opus), under heavy supervision byJoachim Breitnerat theLean FRO. "Consistent" here means that every environment con-leche accepts has a model in set theory, following Mario Carneiro's model of Lean's type theory. The proof idea is written uphere. The proof itself is checked by the official Lean kernel, and it assumes the consistency of the set theory used in the model. This approach eliminates a complete class of bugs: programming mistakes in the kernel implementation. It does so without a performance penalty. On the full Mathlib export, con-leche executes 0.69x the instructions of the official kernel and checks the whole library in about 100 seconds using eight threads (seePERF.md).

However, con-leche is not bulletproof, because there might be bugs in the compiler and runtime used to build it. To minimize this kind of risk, Joachim used AI to translate con-leche to Rust and then usedAeneasto prove that the Rust version refines con-leche's checking algorithm. Aeneas is a tool for verifying Rust code using Lean. This kernel is called con-ron. The key point is that, since con-leche has a formal consistency proof, any remaining unsoundness bugs are most likely in Lean's compiler or runtime (including the bignum library). It is very unlikely that the same bug also exists in the Rust compiler or runtime, so by checking a proof with both con-leche and con-ron, you gain a high level of protection against this class of bugs.

We also expect the verification of lean4lean to be completed in the next few months, and then we will have three verified kernels in our distribution. The lean4lean verification is also important because its implementation follows the official C++ kernel implementation very closely.

Arthur Adjedjis working on the kernel renovation plan (see issue#14977). Arthur has already submitted several PRs implementing the plan. Joachim is reviewing them, making sure con-leche implements the same changes, and patching its proof to ensure no new holes are introduced during the renovation. Arthur is also working on even simpler kernels for Lean. The goal is to reduce their complexity and simplify the process of validating their specification.

There is still a lot of work to be done. We want a more user-friendlylake checkcommand. We want to enable users to hook their favorite kernel intolake check. TheLean Kernel Arenahas several new and efficient kernels. It should be easy to use them. We want to verify parts of our compiler. Scalability is also a major concern now.Anthropic's FLTis over 13M LoC,Mathlibis 2.5M LoC, andTau Cetiis already over 3M LoC and growing fast.The General Courtade–Kumar theoremrepo is above 50M LoC. We are seeing the Lean community write proposals for math libraries in the 1B+ LoC range. The current approach for external kernels does not scale to developments of this size. We need binary export formats and incremental checking with external checkers. At the Lean FRO, we are working on these challenges. In the meantime, runlake check --paranoidon your own project. If the kernels disagree about one of your proofs, we want to hear about it at contact@lean-fro.org.