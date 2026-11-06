---
title: Security advisory: openssh-server password authentication bypass | Alpine Linux
url: https://alpinelinux.org/posts/2026-11-05-openssh-password-authentication-bypass/
date: 2026-11-06
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-11-06T12:29:01.258161
---

# Security advisory: openssh-server password authentication bypass | Alpine Linux

# Security advisory: openssh‑server password authentication bypass

## Summary
- Alpine Linux systems running the `openssh-server` package without PAM are vulnerable to a password‑authentication bypass.  
- An attacker can log in without a password by sending a long password string (257‑1024 bytes) when the system has at least one account with a `*` password field and another account with a `$5$` or `$6$` hash.  
- The issue is fixed in specific OpenSSH package versions; until then, disable password authentication.

## Problem
- A crafted SSH connection succeeds without knowing any password.  
- Requirements for the attack:  
  - An account whose password field is `*` (key‑only or no password).  
  - At least one local account with a `$5$` or `$6$` password hash.  
  - `PasswordAuthentication` enabled (default).  
- The vulnerability is described in the OpenSSH 10.6p2 release notes; no CVE was assigned at the time of writing.

## Affected systems
- Alpine releases 3.16 through 3.24 and edge that use the `openssh-server` package built without PAM (or `openssh-server-pam` with `UsePAM no`).  
- `PasswordAuthentication` set to `yes`.  
- Presence of at least one account with password field `*` (e.g., `root`, key‑only users, users from directory services, the `alpine` user in tiny‑cloud images).  
- At least one local account with a `$5$` or `$6$` password hash.

## Not affected
- Containers that do not run `sshd`.  
- Systems with `PasswordAuthentication no`.  
- Systems using `openssh-server-pam` with `UsePAM yes`.  
- Accounts locked with `!` in `/etc/shadow`.  
- Systems lacking any `$5$`/`$6$` style password hashes.  
- Cloud images configured by cloud‑init that set `PasswordAuthentication no`.

## Mitigation

### 1. Update OpenSSH
```sh
apk upgrade -U -a
rc-service sshd restart
```
Fixed package versions:
| Alpine branch | Fixed openssh version |
|----------------|----------------------|
| edge           | 10.6_p2-r0           |
| 3.24           | 10.3_p1-r2           |
| 3.23           | 10.2_p1-r1           |
| 3.22           | 10.0_p1-r11          |
| 3.21           | 9.9_p2-r1            |
| 3.20           | 9.7_p1-r6            |
| 3.19           | 9.6_p1-r3            |
| 3.18           | 9.3_p2-r4            |
| 3.17           | 9.1_p1-r7            |
| 3.16           | 9.0_p1-r6            |

### 2. Disable password authentication (if update is not possible)
```sh
mkdir -p /etc/ssh/sshd_config.d
echo 'PasswordAuthentication no' > /etc/ssh/sshd_config.d/00-no-passwords.conf
sed -i.bak -e '1i PasswordAuthentication no' \
           -e 's/^\(\s*PasswordAuthentication[^y#]*\)yes/\1no/i' \
           /etc/ssh/sshd_config
sshd -t && rc-service sshd restart
sshd -T | grep -i passwordauthentication
```
- Verify the last command prints `passwordauthentication no`.  
- To revert, delete the drop‑in file and restore the original config backup.

## Cloud images (tiny‑cloud)
- Official tiny‑cloud images (3.18.11‑3.24.3) include an `alpine` user with `*` password and password‑less `doas`.  
- They are safe on first boot but become vulnerable once any `$6$` hash exists (e.g., after setting a console password).  
- Images built from 3.21.10 onward contain the fixed OpenSSH package; earlier images must be updated or have password authentication disabled.

## Legacy releases
- The same bug exists in releases no longer supported (3.16‑3.21).  
- Fixed packages have been published for these versions despite end‑of‑life status.

## Detecting compromise
- Check `/var/log/messages` for lines like `Accepted password for <user>` where the user’s password field is `*`.  
- Review recent `doas` usage, newly created users, files, and authorized keys.  
- If any doubt remains, treat the host as compromised.

## Root cause
- When built without PAM, `sshd` uses `crypt()` to verify passwords.  
- For accounts with a short password field (`*`), `sshd` incorrectly reuses the salt from another account.  
- `musl`’s `crypt()` returns `*` as an error indicator for passwords longer than 256 bytes; this matches the stored `*` field, causing authentication to succeed.  
- OpenSSH 10.6p2 and the patched stable‑branch packages correct this behavior.

## Credits
- Reported by Özgün Kültekin (Wakefield).  
- Fix contributed by Damien Miller, Darren Tucker, and the OpenSSH project (10.6p2 release).  
- Analysis assistance from Timo Teräs.  
- Package building and upload by Natanael Copa.