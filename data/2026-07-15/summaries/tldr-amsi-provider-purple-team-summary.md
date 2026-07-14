---
title: AMSI Provider – Purple Team
url: https://ipurple.team/2026/07/13/amsi-provider/
date: 2026-07-15
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-07-15T04:48:21.695417
---

# AMSI Provider – Purple Team

# AMSI Provider – Purple Team

## Overview
- The Antimalware Scan Interface (AMSI) is a Microsoft‑provided Windows security interface that forwards potentially unsafe content (e.g., PowerShell scripts) to the installed antimalware engine or EDR for scanning before execution.  
- Microsoft allows third‑party applications to register as AMSI providers so they can receive the content for analysis.  
- An attacker with elevated privileges can abuse this feature by registering a malicious (fake) AMSI provider, achieving persistence: when a defined trigger string is entered in a PowerShell console, the provider executes arbitrary code.

## Playbook Summary
- **Goal:** Use a custom AMSI provider to run code whenever a specific string appears in PowerShell input.  
- **Technique:**  
  1. Implement a COM in‑process server that registers itself as an AMSI provider.  
  2. In the `Scan` method, retrieve the script content from the `IAmsiStream`.  
  3. Compare the content against trigger strings (e.g., `pentestlab`, `"pentestlab"`, `'pentestlab'`).  
  4. If a match is found, launch a new thread that executes the attacker‑chosen payload (the sample launches `calc.exe`).  
  5. Register the provider in the registry under the CLSID and AMSI provider keys; unregister to clean up.

## Key Code Elements
- **COM Server Boilerplate**
  - `DllMain` initializes and terminates the COM module.  
  - `DllCanUnloadNow`, `DllGetClassObject` expose standard COM entry points.  

- **Provider Class (`PentestlabAmsiProvider`)**
  - Implements `IAntimalwareProvider` with `Scan`, `CloseSession`, and `DisplayName`.  
  - `Scan` obtains the content size and address via `IAmsiStream::GetAttribute`.  
  - Uses `RtlInitUnicodeString` and `RtlEqualUnicodeString` from `ntdll.dll` to compare content with trigger strings.  
  - On a match, creates a thread (`MyThreadFunction`) that runs `system("c:\\Windows\\System32\\calc.exe")`.  
  - Always returns `AMSI_RESULT_NOT_DETECTED` to avoid alerting the real antimalware engine.  

- **Registration Functions**
  - `SetKeyStringValue` writes string values to the registry.  
  - `DllRegisterServer` creates CLSID entries under `HKLM\Software\Classes\CLSID\{CLSID}` and registers the DLL path and threading model.  
  - Adds the CLSID to `HKLM\Software\Microsoft\AMSI\Providers\{CLSID}` to make the provider visible to AMSI.  
  - `DllUnregisterServer` removes the provider registration keys.  

## Persistence Mechanism
- Once the malicious provider is registered, every PowerShell command passes through AMSI.  
- When the attacker‑chosen trigger string is detected, the provider’s `Scan` method spawns the payload, giving the attacker code execution each time the string is entered.  

## Reference
- Microsoft has published sample code and an article describing the technique; the full proof‑of‑concept is available in the public `AMSI-Provider` repository.