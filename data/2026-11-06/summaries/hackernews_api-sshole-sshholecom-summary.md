---
title: *sshole · sshhole.com
url: https://sshhole.com
date: 2026-11-05
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-11-06T12:29:51.675426
---

# *sshole · sshhole.com

# sshhole – summary

## overview
- The page demonstrates a proof‑of‑concept where a Debian (glibc) box and an Alpine (musl) box run identical code in the browser; nothing is transmitted to a server.  
- It shows that the `crypt(pw, bob's salt)` function behaves the same on both systems, highlighting a discrepancy in how password verification is handled by OpenSSH when compiled against musl.

## are you affected?
- Conditions that make a system vulnerable:  
  - The SSH daemon (`sshd`) is built on **musl** (e.g., Alpine, OpenWrt, Buildroot, Yocto).  
  - PAM is **not** used (Alpine’s `openssh-server` disables PAM by default, or `UsePAM no` is set).  
  - Password authentication is **enabled** (the default).  
  - There exists an account whose password field is a single asterisk (`*`) – typically a key‑only, LDAP, or root account on Alpine.  
  - There is another account with a normal password.  
  - Under these circumstances the second account will accept any password whose length is between **257 and 1024 characters**.

- Example: Alpine’s official AWS and Azure images ship with the default `alpineuser`, which has password‑less `doas`; this effectively grants root access.

- Systems using glibc (Debian, Ubuntu, Fedora, etc.), or those that go through PAM, Dropbear, or OpenBSD’s SSH, are **not** vulnerable.

## mitigation
- **Update OpenSSH**: version 10.6p2 contains the fix.  
  ```sh
  apk upgrade openssh
  ```
- **If you cannot update yet**, disable password authentication:  
  ```sh
  echo "PasswordAuthentication no" > /etc/ssh/sshd_config.d/00-no-passwords.conf
  rc-service sshd restart
  ```

## what to do next
- Verify the SSH daemon’s libc (musl vs glibc) and PAM configuration.  
- Apply the update or disable password logins promptly to close the vulnerability.