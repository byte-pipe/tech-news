---
title: 5 Terminal Commands That Saved Me Hours of Clicking - DEV Community
url: https://dev.to/maame-codes/5-terminal-commands-that-saved-me-hours-of-clicking-4mfn
date: 2025-12-19
site: devto
model: llama3.2:1b
summarized_at: 2025-12-24T11:19:41.325969
screenshot: devto-5-terminal-commands-that-saved-me-hours-of-clickin.png
---

# 5 Terminal Commands That Saved Me Hours of Clicking - DEV Community

**5 Terminal Commands That Saved Me Hours of Clicking**

I used to be terrified of the terminal. As a new programmer, I was stuck in a world of graphical user interfaces (GUIs) and mouse-driven workflows. But as I delved deeper into complex projects, I realized that the GUI was slowing me down.

Here are 5 basic commands that revolutionized how I approach coding:

### **1. The Teleporter: `cd` with Tab Completion**

In the old way of doing things, I'd open the file explorer, navigate to a folder, and then manually type out the name of the target directory using parentheses (e.g., `Documents(Cd)`). It was tedious enough; now, you can use the tab key and `cd` with completion:

*   `cd ~/Doc/Cd/Py/Cd/Proj/Web/Cd`: Instantly teleports to where I need to be
*   `Enter fullscreen mode` and then exit

### **2. The Instant Architect: `mkdir -p`**

To set up a new project structure, I'd spend too much time navigating folders. Now, with `mkdir -p`, I can create entire directories in one line:

```bash
mkdir my-app/ {src/components/ assets teste tests}
```

### **3. The "Safety Net": `cp -r`**

When making a critical refactor that might break things, I'd backup and then undo it. Now, with `cp -r`, I can copy a folder and instantly create a backup:

```bash
cp -r my-cool-project BBACKUP
```

### **4. The Navigator: `find` and `printf`**

To locate specific files or directories quickly, I used to rely on `find`. Now, I have the power of `printf` for more advanced filtering options:

```bash
find ~/Code -name "*.py" | printf "\$(cd Documents && ls -l)"
```

### **5. The Optimizer: `zip` and `grep`**

When compressing large datasets or searching for patterns in massive files, I used to rely on cumbersome methods. Now, with the integrated packages `zip` (for zipping) and `grep` (for searching), I can perform these tasks efficiently:

```bash
zip my-data.zip Documents | grep "test"
```

With these 5 commands under my belt, I've become more efficient in coding time and reduced my errors. The terminal no longer holds me hostage; it's my trusty partner in programming.
