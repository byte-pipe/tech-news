---
title: Details That Make Interfaces Feel Better
url: https://jakub.kr/writing/details-that-make-interfaces-feel-better
date: 2026-03-23
site: tldr
model: llama3.2:1b
summarized_at: 2026-03-23T11:36:19.905674
---

# Details That Make Interfaces Feel Better

# Details that make interfaces feel better
===========================================================

Interfaces can have various components that contribute to making them feel better. This list provides some key points and examples of how designers can achieve great results with small details in their interfaces.

## Small Components for Better Interfaces

* **Text Wrapping**: Using `text-wrap: balance` distributes text evenly across lines, preventing orphaned words.
* **Concentric Border Radius**: Applying `padding: 8px`, `12px`, and `20px` creates a balanced visual look when nesting elements inside each other.
* **Animate Icons Contextually**: Animate the opacity, scale, and blur effect on icons to create a more responsive transition.
* **Make Text Crispy**: Use `html lang="en"` with `font-smoothing: antialiased` or `antialiased` instead of default settings.
* **Use Tabular Numbers**: Apply `font-variant-numeric: tabular-nums` from Tailwind CSS to render numbers more professionally.

## Additional Tips

* Ensure guides are hidden when they no longer need attention (e.g., `Hide guides`).
* Consider implementing concentric offset for balanced visual effects.
* Check browser limitations before attempting complex animation or border radius effects.

## Best Practices
-----------------

* Test your interface on different devices and platforms to ensure a polished experience.
* Use online tools like Tailwind CSS and Font Squirrel's Subpixel rendering hack if subpixel rendering is affecting the appearance of text elements.
* Always start with small changes and build upon them for a well-rounded interface experience.