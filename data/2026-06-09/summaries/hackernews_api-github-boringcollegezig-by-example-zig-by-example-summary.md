---
title: GitHub - boringcollege/zig-by-example: Zig by example · GitHub
url: https://github.com/boringcollege/zig-by-example
date: 2026-06-08
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-06-09T06:48:59.400174
---

# GitHub - boringcollege/zig-by-example: Zig by example · GitHub

# Zig by Example – Repository Summary

## Overview
- A hands‑on introduction to the Zig programming language using annotated, runnable examples.  
- Emphasizes Zig’s goals: robustness, optimality, and simplicity without hidden control flow, allocations, or a preprocessor.  
- Authored by Dariush Abbas for Boring College; inspired by *Go by Example*.  

## Repository Layout
- `content/NN-name.md` – Markdown chapters with explanations and annotated code.  
- `examples/NN-name.zig` – Corresponding source files that can be compiled and run.  
- Each code block in `content/` mirrors the matching file in `examples/` and is compiled against Zig 0.16.  

## Index of Topics
1. Hello, World  
2. Values  
3. Variables  
4. Integers  
5. Floats  
6. Strings  
7. Arrays  
8. Slices  
9. Vectors  
10. Structs  
11. Enums  
12. Unions  
13. Functions  
14. Blocks and Statements  
15. If / Else  
16. Switch  
17. While Loops  
18. For Loops  
19. Defer  
20. Errors  
21. Optionals  
22. Pointers  
23. Multi‑Pointers  
24. Slices (Pointers)  
25. Comptime  
26. Generics  
27. Memory Allocation  
28. ArrayList  
29. HashMap  
30. Linked List  
31. Testing  
32. Formatting and Print  
33. Io Interface (new in 0.16)  
34. Writer & Reader (new)  
35. File I/O  
36. Threading & Concurrency (new)  
37. Processes  
38. Networking & HTTP (new)  
39. JSON  
40. Random Numbers  
41. Sorting  
42. Math  
43. Build System  
44. C Interop  

## Running the Examples
1. Install Zig 0.16.0 (e.g., `brew install zig` on macOS or download from ziglang.org).  
2. Execute an example:  
   ```bash
   zig run examples/01-hello-world.zig
   ```  
3. Some examples require extra flags:  
   - Tests: `zig test examples/31-testing.zig`  
   - C interop: `zig run examples/44-c-interop.zig -lc`  

## Further Resources
- Official Zig documentation and standard library source.  
- Release notes for Zig 0.15.1 and 0.16.0.  
- *Ziglings* – a set of exercises for practice.  

## Contribution
- Contributions are welcome; guidelines are in `CONTRIBUTING.md`.  

## Repository Statistics
- Stars: 237  
- Forks: 4  
- Watchers: 3  

---  
*All examples target Zig 0.16.*