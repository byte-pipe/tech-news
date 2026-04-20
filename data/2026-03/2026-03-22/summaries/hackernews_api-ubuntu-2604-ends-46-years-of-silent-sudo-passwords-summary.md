---
title: Ubuntu 26.04 Ends 46 Years of Silent sudo Passwords
url: https://pbxscience.com/ubuntu-26-04-ends-46-years-of-silent-sudo-passwords/
date: 2026-03-21
site: hackernews_api
model: llama3.2:1b
summarized_at: 2026-03-22T11:37:30.573681
---

# Ubuntu 26.04 Ends 46 Years of Silent sudo Passwords

### Ubuntu 26.04 Ends 46 Years of Silent Sudo Passwords: A New Era Begins

***Why Enterprise RAID Rebuilding Succeeds Where Consumer Arrays Fail:***
    Main Idea: Linux distributions are changing their password protocol from silent to visible to provide enhanced security.
      Key Points:
        *   Existing systems were designed for shared terminals with physical screens open, where shoulder surfing could occur easily.
        *   With the introduction of Ubuntu 26.04 LTS, every keystroke at asudopassword prompt produces an echo asterisk that was initially unintended.

* **Linux Torvalds Rejects MMC Subsystem Updates and Explains Why:**
    Main Idea: Linus Torvalds is rejecting a proposed update to theMMC subsystem for Linux 7.0 due to its potential impact on the security of users.
      Key Points:
        *   The current implementation of MMC caused issues like user authentication being bypassed by malicious attacks from other terminals.
        *   Torvalds argues that security outweighs the benefits of this change and provides an explanation for why.

* **sudo-rs: A Rust-Based Alternative to the Classic C Implementation:**
    Main Idea: sudo-rs is a new rewrite of the existing sudo implementation in the Rust programming language, offering improved security features.
      Key Points:
        *   This shift from traditional C code to Rust provides better performance and reliability for password execution when visual feedback is not displayed.

* **Ubuntu 26.04 LTS Enters the Scene with Visible Sudo Passwords:**
    Main Idea: The upcoming release addresses the long-standing silent sudo password problem, providing a clear UX experience.
      Key Points:
        *   As of Ubuntu 26.04, every input at asudopassword prompts will be echoed, allowing users to verify their actions and enhancing security features.

* **Other Side Effects of this Change:*
    Main Idea: Depending on how changes are implemented in mainstream distributions, it may seem counterintuitive for user authentication methods like sudo passwords not be affected.
      Key Points:
        *   Changes affect some parts of the Linux platform such as apt package manager and security features associated with new sudo password functionality.
