---
title: oss-security - Dirty Frag: Universal Linux LPE
url: https://www.openwall.com/lists/oss-security/2026/05/07/8
date: 2026-05-08
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-05-08T08:14:31.705307
---

# oss-security - Dirty Frag: Universal Linux LPE

# Dirty Frag: Universal Linux LPE

## Overview
- Report submitted by Hyunwoo Kim (8 May 2026) to the oss‑security mailing list.  
- Describes “Dirty Frag”, a universal local privilege escalation (LPE) affecting all major Linux distributions.  
- The vulnerability chain is analogous to the earlier “Copy Fail” issue.

## Impact
- Allows immediate escalation to root privileges on any major Linux distribution.  
- No patches or CVE identifiers exist because the embargo was broken before a responsible disclosure could be completed.  

## Vulnerability Chain
- **First component:**  
  `https://git.kernel.org/pub/scm/linux/kernel/git/netdev/net.git/commit/?id=f4c50a4034e62ab75f1d5cdd191dd5f9c77fdff4`
- **Second component:**  
  `https://lore.kernel.org/all/afKV2zGR6rrelPC7@v4bel/`

## Disclosure Status
- Embargo broken; maintainers of various linux‑distros were consulted and requested public release.  
- No official patches are available for any distribution at this time.

## Mitigation (Temporary Work‑around)
```sh
sh -c "printf 'install esp4 /bin/false\ninstall esp6 /bin/false\ninstall rxrpc /bin/false\n' > /etc/modprobe.d/dirtyfrag.conf; rmmod esp4 esp6 rxrpc 2>/dev/null; true"
```
- Disables the affected kernel modules (`esp4`, `esp6`, `rxrpc`) to prevent exploitation.

## References
- Original email header:  
  - Message‑ID: `<afzgS2SCWNcZU3vU@v4bel>`  
  - Date: Fri, 8 May 2026 03:56:11 +0900  
- Comparison to prior “Copy Fail” vulnerability.