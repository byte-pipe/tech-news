---
title: Official Claude Code Extension Compromise: Security Advisory | Phorion
url: https://phorion.io/blog/offical-claude-code-vsx-compromise/
date: 2026-10-30
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-10-31T19:04:02.867969
---

# Official Claude Code Extension Compromise: Security Advisory | Phorion

# Official Claude Code Extension Compromise: Security Advisory | Phorion

## TL;DR
- Phorion identified a backdoored **Claude Code for VS Code** extension (versions 2.1.312 and 2.1.313) on the Cursor Marketplace.
- The extension drops a persistent SSH backdoor on macOS, Linux, and Windows; the advisory focuses on macOS.
- Immediate actions: audit for the affected versions, remove them, and trigger incident‑response procedures.
- Cursor has removed the compromised packages from its marketplace.

## Infection Chain Overview
### Compromised Extension
- An injected IIFE is prepended to the normal `extension.js` bundle.
- The malicious code runs as soon as Node loads the file, before the extension’s normal activation.

### Stage 1 – Preparing SSH Access
- Creates `~/.ssh` (if missing) and appends an attacker‑controlled Ed25519 public key (`svc-telemetry`) to `authorized_keys` (permissions 0700/0600).
- Checks for the comment string rather than the key fingerprint when deciding whether to add the key.
- Attempts to enable the SSH daemon:
  - **Linux:** `systemctl` / `service` / `/etc/init.d/` start attempts.
  - **macOS:** Runs `systemsetup -getremotelogin`; if output contains “Off”, executes `sudo -n systemsetup -setremotelogin on`.
  - **Windows:** Tries to install/start OpenSSH Server via PowerShell (contains a helper‑function bug).

### macOS SSH Logic Bug
- `systemsetup -getremotelogin` requires admin rights; when run as a standard user it prints an error and exits with status 0.
- The script interprets any non‑“Off” output as “SSH already enabled”, so it never attempts the `sudo -n` enable command.
- Result: on machines where Remote Login is disabled, the inbound SSH backdoor is ineffective, though the key and persistence files are still placed.

### Stage 2 – Establishing a Reverse SSH Tunnel
- Writes an embedded attacker private key (`svc-telemetry-tun`) to a temporary file named `.stk_<md5(hostname+HOME)>`.
- Initiates an outbound SSH connection to `134.209.82.225` (port 22) using the private key, creating a reverse tunnel.
- Two keys involved:
  1. Public key in `authorized_keys` → attacker can log into the victim.
  2. Private tunnel key → victim machine connects out to attacker’s server.

## Impact and Recommendations
- **Persistence:** SSH keys are stored permanently; the reverse tunnel runs continuously.
- **Privilege Escalation:** No exploit is used; the payload works with the privileges of the logged‑in user.
- **Detection:** Look for:
  - New files in `~/.ssh/authorized_keys` containing the comment `svc-telemetry`.
  - Temporary files matching `.stk_*.` pattern in the OS temp directory.
  - Outbound SSH connections to the IP `134.209.82.225`.
  - Unexpected `systemsetup` or `systemctl` commands in process logs.
- **Mitigation:**
  - Remove the compromised extension versions immediately.
  - Revoke any unauthorized SSH keys from user accounts.
  - Disable Remote Login if not required, and enforce proper sudo policies.
  - Conduct a full forensic review of affected hosts for additional artifacts.