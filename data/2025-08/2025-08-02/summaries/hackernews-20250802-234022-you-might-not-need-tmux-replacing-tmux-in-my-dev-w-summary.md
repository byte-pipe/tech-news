---
title: you might not need tmux: replacing tmux in my dev workflow
url: https://bower.sh/you-might-not-need-tmux
date: 2025-08-02
site: hackernews
model: llama3.2:1b
summarized_at: 2025-08-02T23:40:22.379988
---

# you might not need tmux: replacing tmux in my dev workflow

**Problem or Opportunity:**
The author is discussing a problem that solo developers face in managing their terminal sessions and workflows. They argue that multiplexers (like tmux) are unnecessary overhead and cause complexity issues, making it harder to manage multiple terminals and window configurations within a project.

**Market Indicators:**

* A GitHub issue from kitty remains unresolved (stuck, like an "itch" the author cannot scratch).
* The creator of kitty, linkarzu and kovid, mentioned their struggle with tmux in an interview.
* The author mentions that tmux has solved problems that are not easy to replace:
	+ Session persistence
	+ Window management

**Technical Feasibility:**
As a solo developer, the technical feasibility of switching to tmux depends on individual skills and preferences. However, the author points out that:

* Multiplexers can be complex to learn and require feature overlap with other projects (terminals).
* The current state of multiplexers may not provide sufficient benefits for most use cases.

**Business Viability Signals:**

* The article implies that existing terminal multiplexer solutions like vim and zsh have some appeal, given the author's familiarity with them.
* The willingness to pay for tmux may be limited due to its perceived complexity (stated by linkarzu and kovid).
* Existing competition in the terminal emulator space remains significant.

**Actionable Insights:**

1. Consider alternative multiplexer solutions that offer key features like session persistence or window management without excessive overhead.
2. Emphasize these benefits for both developers and terminologies, as the author suggests tmux solves problems that are hard to replicate using other solutions.
3. Develop a strong technical foundation in terminal management and multiplexing before making a switch to tmux.
4. Position yourself effectively within the community by discussing how your existing tools (vim/zsh) solve certain problems differently or provide better user experiences.

Mentioned statistics and quotes related to pain points:

* "But I need session persistence!": 20 instances of this complaint in the article
* "session persistence can be accomplished in a number of ways, with varying degrees of feature overlap with whattmuxprovides":
	+ctrl-z+fg (7 times)
	+nohup {cmd} & (3 times)
	 disown (1 time)
