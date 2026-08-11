---
title: GitHub - 3b1b/manim: Animation engine for explanatory math videos · GitHub
url: https://github.com/3b1b/manim
date: 
site: github
model: llama3.2:1b
summarized_at: 2026-08-11T11:50:03.425873
---

# GitHub - 3b1b/manim: Animation engine for explanatory math videos · GitHub

**Manim Engine for Explanatory Math Videos**
=====================================================

The 3Blue1Brown project, known as Manim, is a Python animation engine designed to create precise programmatic animations for explanatory math videos.

### GitHub Repository

* **Purpose:** Provides source code and instructions for installing the ManimGL version.
* **History:** Originated as a personal project by 3Blue1Brown, which later became part of the community edition with improved stability, testing, and documentation.
* **Install Method:**

**For Local Installation:**
```python
pip install manimgl
```
Alternatively, clone the repository and execute:
```bash
pip install -e .
```

### Features

Manim supports:

* Programmatic animations for math videos
* Video-specific code available on the 3Blue1Brown website
* Community edition with improved stability and documentation

**System Requirements:**

* Python 3.10 or higher
* FFmpeg (for animation rendering)
* OpenGL (required, optional LaTeX support)
* Pango (Linux system requirement)

### Direct Installation Example:
```bash
# Try it out
manimgl example_scenes.py OpeningManimExample
```
Or:
```bash
# Install ManimGL from a clone repository and execution environment
git clone https://github.com/3b1b/manim.git
cd manim
pip install -e .
```
Note: The community edition is recommended for new installations, as it addresses stability and testing issues.