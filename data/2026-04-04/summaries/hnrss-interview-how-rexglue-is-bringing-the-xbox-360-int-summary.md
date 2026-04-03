---
title: Interview: How ReXGlue is bringing the Xbox 360 into the static recompilation era
url: https://readonlymemo.com/rexglue-xbox-360-recompilation-interview/
date: 2026-03-29
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-04-04T01:03:57.666995
---

# Interview: How ReXGlue is bringing the Xbox 360 into the static recompilation era

# Interview: How ReXGlue is bringing the Xbox 360 into the static recompilation era

## The Big Two

### 1. Getting into the sticky details with ReXGlue creator Tom
- Tom, a longtime Xbox 360 fan and systems engineer, was inspired by the **Sonic Unleashed Recompiled** project, which showed the potential of static recompilation for 360 games.  
- Contact with the Fable 2 Recomp community (led by Ryan “Loreaxe” Fisher) gave him a group of like‑minded developers.  
- ReXGlue was created to provide a **foundational SDK** that combines an emulated backend with the ability for developers to plug in native rendering, audio, and other subsystems.  
- Early ports built with ReXGlue include:
  - Blue Dragon  
  - Lost Odyssey  
  - Banjo‑Kazooie: Nuts & Bolts  
  - Ninja Gaiden 2  
  - Halo 3 beta  
  - Crackdown 2  
  - Viva Pinata  
- The project is still in early development; the GitHub page warns that polished, “pristine” PC ports are not yet available.  

### 2. Technical approach and distinction from pure emulation
- ReXGlue **borrows heavily** from the Xbox 360 emulator **Xenia**, but replaces Xenia’s JIT backend with an **ahead‑of‑time (AOT) static recompilation** pipeline.  
- The pipeline:
  1. Parses the original PowerPC machine code.  
  2. Generates equivalent C++ code.  
  3. Compiles the C++ with Clang to produce native host binaries.  
- No JIT or runtime instruction interpretation is used; the game runs as native code compiled offline.  
- GPU handling currently relies on Xenia’s Xenos backend, but all **CPU‑side logic** (physics, AI, scripting, kernel interactions) is statically recompiled.  
- Advantages of static recompilation over JIT emulation:
  - Enables deep modding and native subsystem replacements.  
  - Allows platform‑specific optimizations and modern compiler optimizations, often yielding **better performance** than the original console (e.g., higher framerates in the early Blue Dragon “ReBlue” prototype).  
- The methodology is **hardware‑agnostic**: the same static recompilation concept applies to N64, Xbox 360, or any other CPU, differing only in instruction‑set translation.  

## Additional notes
- Tom’s background includes Source Engine modding and professional systems/platform engineering, giving him the skill set to tackle a project of this scale.  
- Community interest is growing, with several unreleased or “never‑left‑the‑box” titles already being targeted for recompilation.  
- The interview emphasizes that ReXGlue is **not just an emulator**; it is a **platform and SDK** aimed at unlocking capabilities that traditional emulation cannot provide.