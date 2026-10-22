---
title: "WorldTUI: I trained a 360M model to pretend to be a terminal - SimEdw's Blog"
url: https://simedw.com/2026/10/21/world-model-terminal/
date: 2026-10-22
site: hnrss
model: llama3.2:1b
summarized_at: 2026-10-22T16:05:42.156772
---

# WorldTUI: I trained a 360M model to pretend to be a terminal - SimEdw's Blog

**Fine-tuning a 360M-Parameter Language Model for a Terminal Emulator**

**Introduction**

This project aims to train a 360M-parameter language model to simulate a terminal emulator. The model's primary role is to predict the screen contents and changes as user input, and its predictions will be used to generate output. The terminal being simulated is a 32x96 grid of characters, where each cell represents a single character on the screen.

**Overview of the Model**

The model was trained on sessions recorded from real terminal applications, including bash, vim, and snake. Each session consists of a snapshot of the screen, its contents, and the cursor position. The model uses this information to predict the screen contents and changes as user input. The predictions are then used to generate output, which is based on the actual input sent to the terminal.

**Key Features**

* The model can predict screen changes based on a single keypress, unlike most standard LLMs that take a prompt and append tokens one at a time.
* The model can manipulate the screen contents and cursor position directly, without relying on a separate prompt or shell.
* The model can generate convincing output, including errors and recoveries, by accurately predicting changes to the screen.

**How the Model Works**

1. The initial session snapshot includes the screen size, contents, and cursor position.
2. For each subsequent session, a sequence of tokens is generated to describe the input (e.g. bash prompt, vim buffer, snake game).
3. The model predicts the screen contents and changes as input based on the sequence of tokens and the updated cursor position.
4. The predicted output is generated based on the actual input sent to the terminal.
5. The output is used to update the screen snapshot, and the model continues with the next session.

**Technical Challenges**

* Training on a small dataset, such as terminal applications, is necessary to achieve accurate predictions.
* Managing the complexity of the terminal emulator's behavior is challenging.
* Ensuring the model remains predictable and controllable is essential for reliable use.

**Use Case**

The terminal emulator can be used in various scenarios, including:

* Testing and debugging applications before they are released.
* Simulating user interactions with applications for educational or research purposes.
* Developing applications that require interactive testing or debugging.

**Example**

Here is an example of a terminal input session:

```l
INPUT_START
'l'
(INPUT_END
'CURSOR
0
17
```

The model predicts the screen contents and changes as the input, and generates output based on the actual input sent to the terminal.

**Demonstration**

A demo version of the terminal emulator can be accessed in a dedicated browser, and users can type in sample inputs to see the model in action. The demo is available in a 208 MB file, which can be downloaded. Running Chrome or Edge on a user's device can also be used to access the demo.