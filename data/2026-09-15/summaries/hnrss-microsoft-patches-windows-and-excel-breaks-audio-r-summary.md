---
title: Microsoft patches Windows and Excel – breaks audio, remote access, and paste
url: https://www.theregister.com/os-platforms/2026/09/14/microsoft-patches-windows-and-excel-breaks-audio-remote-access-and-paste/5296085
date: 2026-09-14
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-09-15T07:39:25.084829
---

# Microsoft patches Windows and Excel – breaks audio, remote access, and paste

# Microsoft patches Windows and Excel – breaks audio, remote access, and paste

## Main issues introduced by the September 2026 updates
- **Remote Desktop Services (RDS) failures**  
  - Affects Windows 11 26H1, 25H2, 24H2 and Windows Server 2012.  
  - Connections may drop after a few minutes, servers can hang on “Please wait for the Remote Desktop Configuration,” and related tools (MMC, RDS Licensing Diagnoser, File Explorer) may become unresponsive.  
  - The Windows Update page can stop responding and show a perpetual loading indicator.  
- **USB Audio Class 1.0 device problems**  
  - Occur on the same Windows 11 builds.  
  - Users may lose audio, encounter broken sound settings, or experience multichannel audio failures.  
  - Switching to two‑channel mode can temporarily restore sound.  
- **Excel paste operation silently fails**  
  - Impacts Excel 2016, 2019, 2021, and 2024.  
  - When pasting, the source remains selected and the destination is unchanged, with no beep, error message, or other indication of failure.  

## Microsoft’s acknowledgement and current status
- All three problems are listed on the official **known‑issues list**.  
- Microsoft is developing fixes but has not provided a timeline.  
- Temporary mitigations:  
  - For RDS, deallocating and restarting the affected virtual machine may restore connectivity.  
  - For audio, use two‑channel mode.  
  - For Excel, uninstalling/reinstalling Office or removing the specific security update restores paste functionality, though this also removes the security fixes.  

## Impact on users and administrators
- Automatic updates may have already installed the problematic patches, exposing users without warning.  
- Windows Server 2012 will lose Extended Security Updates on 13 Oct 2026, adding urgency for administrators.  
- No official workaround has been published by Microsoft.  

## Outlook
- Microsoft continues to work on patches for the RDS, audio, and Excel issues, but exact release dates remain unspecified.