---
title: Jailbreaking the Switch 2
url: https://pepsipu.com/blog/2026-10-switch2-jailbreak-ns2jb/
date: 2026-10-22
site: hackernews_api
model: llama3.2:1b
summarized_at: 2026-10-22T16:06:17.739207
---

# Jailbreaking the Switch 2

# Jailbreaking the Switch 2 with ns2jb

**Introduction**
-----------------------------

ns2jb is a software-only jailbreak of the Switch 2 firmware up to 23.0.1, allowing arbitrary native code execution as any ordinary sysmodule. This text summarize the article 'Jailbreaking the Switch 2: ns2jb'.

**Setup and Preparation**
---------------------------

* The author, Codex, set up a harness around the Switch 1 and 2 to jailbreak the Switch 2 without manual intervention.
* The goal was achieved in 1.2 weeks with a focus on userland code execution.

**Jailbreak Implementation**
------------------------------

* The author utilized the WebKit target for code execution, allowing for arbitrary IPC calls and execution of microkernel services (sysmodules).
* The exploit relies on a custom Wi-Fi captive portal to load a n-day loaded WebKit binary.

**Code Execution and Capabilities**
---------------------------------

* The jailbreak achieves code execution, but with limitations due to the WebKit n-day execution mechanism, which restricts arbitrary IPC calls and requires a new approach for generalization beyond existing functions.
- The WebKit n-day mechanism has "execute-only memory" (XOM), making it difficult to detect arbitrary IPC calls.
- The author suggests that the execution mechanism is based on a custom Wi-Fi captive portal.

**Game Play with Mario Kart World**
------------------------------------

* The author demonstrated the capabilities of the jailbreak by playing with Mario Kart World.
- The first gameplay video and second gameplay video highlight the exciting gameplay experience.

**Disclaimer**
--------------

* The author clarifies that the prompt to jailbreak the Switch 2 was not actually used as intended.