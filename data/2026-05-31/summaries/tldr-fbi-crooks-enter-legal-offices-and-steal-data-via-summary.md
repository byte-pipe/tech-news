---
title: FBI: Crooks enter legal offices and steal data via USB drive
url: https://www.theregister.com/security/2026/05/27/fbi-crooks-enter-legal-offices-and-steal-data-via-usb-drive/5247212/
date: 2026-05-31
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-05-31T06:01:28.847640
---

# FBI: Crooks enter legal offices and steal data via USB drive

# FBI warns law firms of Silent Ransom Group’s USB‑drive extortion tactics  

## Overview  
- The FBI alerts U.S. law firms that the “Silent Ransom Group” (SRG) continues to target them with both remote and in‑person attacks.  
- SRG, active since 2022, pretends to be corporate IT staff, walks into offices, and plugs malicious USB drives to steal data for extortion.  

## In‑person USB‑drive attacks  
- After a failed phishing call, SRG members physically visit the targeted office.  
- They claim to need to image the victim’s device or create a backup, then copy confidential files onto a thumb drive.  
- Stolen data is later used on the group’s data‑leak site (DLS) to pressure the firm into paying for its return.  

## Remote “callback phishing” attacks  
- SRG sends SMS or email messages urging employees to call a number posing as IT support.  
- During the call the impostor convinces the victim to grant remote‑desktop access.  
- Once inside, attackers elevate privileges, harvest files (often via WinSCP or disguised Rclone), and may upload them to cloud services such as Google Drive or OneDrive.  

## Extortion model  
- SRG does not deploy ransomware; instead it threatens public release of stolen documents unless a ransom is paid.  
- Recent alleged victims include the law firm Jones Day, which reported a phishing incident in April 2026.  

## FBI recommendations for law firms  
- Disable or physically lock USB ports on devices that handle sensitive information.  
- Verify credentials of anyone entering the building before allowing hardware connections.  
- Block inbound SSH (port 22) to prevent encrypted remote access.  
- Enforce phishing‑resistant multi‑factor authentication and limit data access from insecure networks.  
- Provide staff training to recognize social‑engineering attempts and to refuse external devices.  

## Call for public assistance  
- The FBI asks anyone with evidence (phone numbers, call transcripts, phishing emails, cryptocurrency wallet details, or identification of on‑site intruders) to submit it to aid investigations.