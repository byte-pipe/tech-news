---
title: "\"Do You Still Read the Code?\" • zanlib"
url: https://zanlib.dev/blog/do-you-still-read-the-code
date: 2026-09-15
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-09-15T07:39:02.619071
---

# "Do You Still Read the Code?" • zanlib

# Do You Still Read the Code?

## Introduction
- The phrase “do you still read the code?” implies that reading code may be becoming obsolete, similar to memorising phone numbers or using paper maps.  
- I rely heavily on AI and always read the code it generates because I am accountable for the code I commit and deploy.  
- Different teams make different choices about how much they inspect AI‑generated code, and these choices affect future maintenance, requirement changes, and tooling.  
- It is unclear which approach will dominate; confidence in either side’s victory is premature.

## Accelerators and Vibecoders
- **Accelerators**  
  - Use AI to translate their understanding into code while retaining enough knowledge to explain, anticipate changes, and maintain the implementation.  
  - Treat language models like advanced text editors: they speed up coding but still require reading and reviewing generated code.  
  - Accumulate “cognitive debt” when reading falls behind generation; disciplined review is essential.  

- **Vibecoders**  
  - Delegate both implementation and its revision to AI, focusing on specifying desired behaviour, providing context, and defining evaluation criteria.  
  - View language models as analogous to compilers or frameworks, believing detailed technical understanding is no longer necessary.  
  - Accumulate “intent debt” as requirements evolve, context drifts, and engineering effort shifts to curating prompts and managing model quality.  

- A third group rejects AI for programming altogether, usually for legal or ethical reasons; I have not encountered a commercial software organization that avoids AI because it is deemed less efficient.

## Naur Is Still undefeated
- I align with Peter Naur’s view that programming is “pure applied philosophy”: the true product is the underlying model or theory, not the source code itself.  
- Code is often mistaken for an asset, while the real asset is the knowledge that lets a programmer explain, predict, and adapt the solution.  
- A programmer who possesses the theory can:  
  - Explain how the solution relates to real‑world affairs.  
  - Justify why each part of the program is designed as it is.  
  - Respond constructively to modification requests.  
- Treating code as the primary output is like valuing steam from a power plant over the electricity it produces.  
- Software engineering should name and structure business concepts, turning implicit knowledge into explicit models that benefit both developers and domain experts.  
- Naming based on essential attributes, rather than superficial appearance, yields more flexible and robust models, though it requires greater effort.  
- Test suites verify that the program does what was specified, not that the specification matches reality; continuous engagement with the domain is necessary.  

## Takeaway
- The debate between reading AI‑generated code and delegating to AI reflects deeper questions about what we consider the core product of programming.  
- Maintaining a clear, explainable model of the problem domain remains crucial, regardless of how much code is produced automatically.  
- Teams must choose consciously between accelerator and vibecoder mindsets, aware of the cognitive or intent debt each can generate, and align that choice with their long‑term maintenance strategy.