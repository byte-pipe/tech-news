---
title: "Adventures in Guix Packaging - Nemin's Blog"
url: https://nemin.hu/guix-packaging.html
date: 2026-02-09
site: lobsters
model: gemma3n:latest
summarized_at: 2026-02-09T06:11:22.222497
---

# Adventures in Guix Packaging - Nemin's Blog

# Adventures in Guix Packaging - Nemin's Blog

This article details the author's experience packaging WezTerm, a GPU-accelerated terminal emulator, for the Guix distribution. The author recounts their initial unsuccessful attempt to package Gamescope, highlighting the complexities of Guix's recipe system compared to imperative distributions.  They then describe a more manageable project: packaging WezTerm, which took about a week and provided valuable insights into Guix packaging. The author emphasizes the learning process, including setting up the development environment, understanding project committing rules, and navigating the Guix code review process.

## Key Points:

* **Initial Difficulty with Gamescope:** The author's first attempt at packaging Gamescope was overly ambitious and quickly became overwhelming due to dependency issues and a lack of planning.
* **Focus on WezTerm:** The author chose WezTerm as a more approachable project to learn the intricacies of Guix packaging.  This choice was prompted by a user request on the r/Guix subreddit.
* **Iterative Learning Process:** The article emphasizes the iterative nature of packaging, with the author encountering and overcoming numerous challenges along the way.
* **Importance of Small Steps:**  The author advocates for starting with smaller, more manageable projects to gain a solid understanding of the packaging process.
* **Guix's Strengths:** The author praises Guix's system for enabling developers to do their jobs effectively, particularly highlighting the positive experience with the code review process.
* **Packaging Fundamentals:** The author details the steps involved in packaging WezTerm, including setting up the development environment, importing Cargo crates, patching the `Cargo.toml` file, and addressing GPU and font-related issues.
* **The Packaging Journey:** The article is framed not as a guide to a perfect package, but as a record of the author's learning journey, intended to provide insight into the process for newcomers.



## Detailed Breakdown:

* **Introduction:** The author introduces the project and explains the fundamental difference between imperative and declarative package management in distributions like Nix and Guix. They describe their initial failed attempt with Gamescope and the subsequent decision to package WezTerm.
* **Baby Steps:** The author decided to start with a simpler task: updating a dependency of Gamescope, specifically OpenVR. This involved modifying the package definition, a seemingly trivial task that required setting up the development environment, forking the repository, and understanding the project's contribution guidelines.
* **Enter WezTerm:** The author explains the motivation for packaging WezTerm, driven by a user request and the lack of an existing package. The article clarifies that the focus is on the learning process rather than creating a perfect package.
* **A Mediocre First Attempt:** The author details their initial, unsuccessful attempt to compile WezTerm within a Guix shell. This highlights the need to understand how Rust packages are structured in Guix, specifically the role of Cargo and the different outputs available (e.g., `out`, `rust-src`, `tools`, `cargo`).
* **And Yet, Some Stuff is Still Better Left to the Professionals:** This section acknowledges that some tasks, like complex projects, might be better suited for experienced developers.
* **Conclusion:** The author reiterates the value of the learning experience and encourages others to try packaging smaller projects to gain familiarity with the process. They also mention the positive experience with the code review process.
