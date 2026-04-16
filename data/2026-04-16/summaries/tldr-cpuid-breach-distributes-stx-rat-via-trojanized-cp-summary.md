---
title: CPUID Breach Distributes STX RAT via Trojanized CPU-Z and HWMonitor Downloads
url: https://thehackernews.com/2026/04/cpuid-breach-distributes-stx-rat-via.html
date: 2026-04-16
site: tldr
model: llama3.2:1b
summarized_at: 2026-04-16T12:05:09.435547
---

# CPUID Breach Distributes STX RAT via Trojanized CPU-Z and HWMonitor Downloads

## CPUID Breach Distributes STX RAT via Trojanized CPU-Z and HWMonitor Downloads

**Summary**

The CPUID website, a popular platform for hardware monitoring tools, was breached over a 24-hour period. This breach allowed unknown threat actors to compromise the site, infecting software products such as CPU-Z and HWMonitor with a remote access trojan called STX RAT.

**Key Points:**

* CPUID was compromised by an attack that lasted from April 9-10.
* The breach involved replacing download URLs for CPU-Z and HWMonitor installers with malicious websites.
* STX RAT is a RAT (remote access trojan) with HVNC (host-based virtualization) and broad infostealer capabilities.
* The malware is designed to deploy itself after anti-sandbox checks are performed and execute payloads such as in-memory execution of EXE/DLL/PowerShell/shellcode, reverse proxy/tunneling, and desktop interaction.

**Organization Affected:**

* Kaspersky identified over 150 victims, including organizations in retail, manufacturing, consulting, telecommunications, and agriculture.
* The majority of infections were located in Brazil, Russia, and China.

**Impact:**

* Organizations across various sectors have been impacted.
* The attack highlights the potential for widespread exploitation by a single actor with malicious intentions.