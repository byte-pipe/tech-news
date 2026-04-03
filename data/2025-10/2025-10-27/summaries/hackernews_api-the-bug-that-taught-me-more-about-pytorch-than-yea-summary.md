---
title: the bug that taught me more about PyTorch than years of using it | Elana Simon
url: https://elanapearl.github.io/blog/2025/the-bug-that-taught-me-pytorch/
date: 2025-10-23
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-10-27T11:16:56.266578
screenshot: hackernews_api-the-bug-that-taught-me-more-about-pytorch-than-yea.png
---

# the bug that taught me more about PyTorch than years of using it | Elana Simon

# The PyTorch GPU Kernel Bug that Taught Me More than a Year of Using It

## A Loss Plateau That Wasn't My Mistake

### Tracking Down Every Layer of Abstraction

The trainer's expected solution, optimizing hyperparameters, turned out to be the cause of a loss plateau in our training process. This was just one of many potential fixes that I had tried.

### The Bug: Non-Contiguous Memory Layout

PyTorch's MPSbackend had a bug where addcmul_andaddcdiv kernel function silently fails when writing to non-contiguous output tensors. However, the actual culprit was an operation within Adam's state tensor calculation, which inherited the non-contiguous memory layout.

## The Technical Details

The error manifested due to our encoder weights being initialized as transpose of decoder, resulting in a non-contiguous memory layout. Additionally, the MPS kernels for addcmul_ and addcdiv didn't handle non-contiguous outputs correctly, leading to incorrect computations and temporary buffer storage. Furthermore, writing the results back to a temporary buffer instead of actual tensors caused the training plateau.

### Teaching Me More About PyTorch Internals

This bug hunt forced me through layers of abstraction that I normally don't consider, including optimizer internals, memory layouts, dispatch systems, kernel implementations, and more. This journey taught me more about the framework than I could have expected.

## Debugging Post-Mortem: No Need to Be Smarter Than Your Code

Debugging post-mortems can leave one worrying they wouldn't figure it out on their own. But when you structure your approach with clear reasoning and justification, writing bugs takes less intelligence and more time. This walkthrough demonstrates the importance of observation, persistence, knowledge (of PyTorch internals), and the willingness to dig deeper.

### Tips for Those Who Enjoy Debugging Mistakes or Learning Through Bugs

1.  **Structure Your Approach**: Break down the investigation into manageable steps.
2.  **Understand What Clues Suggested Each Move**: Ask yourself why certain tests suggested each path or hypothesized solutions.
3.  **Keep Digging and Experimentation Necessary**: Without expertise, this process can take time; keep iterating upon your findings.

### The Bug: PyTorch GPU Kernel

The error was triggered due to the MPSbackend not correctly handling non-contiguous output tensors in its addcmul_andaddcdiv kernel function. These non-contiguous operands were written back to a temporary buffer instead of actually storing them as non-contiguous memory segments, leading to freezing during training on Apple Silicon (MPS) devices.

This story serves as an instructive example that even with extensive experience, PyTorch's many quirks and nuances can be challenging to master. However, exploring these complexities through debugging, like learning more about a complex framework such as this one, helps us develop our problem-solving skills – essential for becoming proficient developers in various computing environments.
