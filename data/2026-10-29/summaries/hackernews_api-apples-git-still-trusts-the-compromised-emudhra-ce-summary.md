---
title: "Apple's git still trusts the compromised eMudhra certificates"
url: https://emudhra.we-have-a-problem.com/apple.html
date: 2026-10-28
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-10-29T21:00:50.515133
---

# Apple's git still trusts the compromised eMudhra certificates

# Apple's git still trusts the compromised eMudhra certificates

## Incident timeline
- Apple was notified of the eMudhra certificate compromise on 17 Oct 2026.  
- As of 28 Oct 2026, macOS developer tools (git, curl, python3) still trust the compromised roots.  
- macOS 12.7.2, released on 26 Oct, did not fix the issue and even reverted a manual workaround applied by users.

## Why it matters
- All HTTPS connections made by the affected tools can be intercepted.  
- For git this enables:
  - Delivery of attacker‑chosen code via clones/pulls.  
  - Modification of pushes in transit.  
  - Theft of credentials such as GitHub tokens.  
- Similar interception is possible with curl and python3.

## How to test if your tools are vulnerable
- **git**:  
  ```bash
  git ls-remote https://git-emudhra.we-have-a-problem.com/check.git
  ```  
  - Certificate error → protected.  
  - Commit listed → vulnerable.  

- **Demonstration of a full attack** (run in a temporary directory):  
  ```bash
  git -c http.curloptResolve=github.com:443:15.235.19.186 \
      clone https://fake-user@github.com/galadran/emudhra-git-test
  ```  
  - Patched git: fails with certificate error.  
  - Vulnerable git: clone succeeds, README starts with “INTERCEPTED”.  

- **curl**:  
  ```bash
  curl https://dv-g3b-noct-emudhra.we-have-a-problem.com/
  curl https://dv-g3b-aaa-noct-emudhra.we-have-a-problem.com/
  ```  
  - Certificate error → protected.  

## What Apple should do
- Ship an immediate fix for macOS developer tools, e.g., remove the compromised roots from `/etc/ssl/cert.pem`.  
- Ensure the fix is not undone by future system updates.

## Interim mitigation for developers
- Manually remove the affected root certificates (see the macOS workaround on the article’s main page).  
- After each macOS update, repeat the verification steps and re‑apply the manual removal if needed.  
- Security teams should audit CI runners and other build infrastructure that rely on macOS for supply‑chain risk.

## Additional information
- The article is authored by Dennis Jackson with community contributions.  
- Source code and pull requests are available on GitHub under the Apache License 2.0.