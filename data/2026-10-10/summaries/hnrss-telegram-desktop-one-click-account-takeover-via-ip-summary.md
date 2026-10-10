---
title: Telegram Desktop: one-click account takeover via IPC injection | beaksec
url: https://beaksec.github.io/posts/telegram-desktop-one-click-account-takeover/
date: 2026-10-10
site: hnrss
model: llama3.2:1b
summarized_at: 2026-10-10T16:11:30.373297
---

# Telegram Desktop: one-click account takeover via IPC injection | beaksec

# Telegram Desktop Exploited via One-Click Account Takeover via IPC Injection

## Introduction

Telegram Desktop allows users to click on links in chats and potentially grant unauthorized access to their account. This article outlines how Telegram Desktop is exploited to gain administrative control over a Telegram account via an IPC (Inter-Process Communication) injection vulnerability.

## Key Points

* A crafted link is injected into Telegram Desktop, which uses IPC to execute it without proper validation.
* The injected command reads a file from an instruction file without checking the requested file or providing a confirmation.
* The attack is able to steal the files belonging to the victim's login.

## One Link, Two Processes

Telegram Desktop uses a URI scheme, "tg://x", to authenticate itself to external applications. This scheme is defined by the Telegram Desktop source code, and it is used by the application to handle incoming links.
* The application registers the URI scheme with the operating system, which then knows which application to launch when it encounters the link type.
* When Telegram is not running, the application starts with the string as a parameter, converts it to a URL object, and attempts to handle it internally.

## Exploitation

The attack relies on two vulnerabilities:
* The first vulnerability is the injection of a malicious link into Telegram Desktop. The link is crafted to use the "tg://x" URI scheme, which is not properly validated by the application.
* The second vulnerability is the fact that the application only checks if the URL matches the expected signature (an "a" parameter) when handling incoming links. However, if the application is already running, a new process is created to communicate with the application. If the new process manages to connect, it is able to hand over the link and exit.
* To exploit the attack, a link is created with the "tg://x" signature, but does not include the expected "a=" parameter. The application will attempt to handle the link without adding the parameter, and since Telegram is not running, a new process is created to handle the link. Once the new process connects, it can hand over the link to the original process, allowing arbitrary file read and potentially causing the account to be taken over.

## Affected Versions

The attack is specifically targeted against Telegram Desktop versions 7.2.8 and earlier, with a confirmed impact on Windows versions 6.9.3.

## Impact

Remote arbitrary local file read, exfiltrated to an attacker-controlled chat; account takeover.