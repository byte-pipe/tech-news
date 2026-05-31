---
title: 'Google Workspace Updates: Google Chat external interoperability with Microsoft Teams via NextPlane OpenHub is now available'
url: https://workspaceupdates.googleblog.com/2026/05/google-chat-external-interoperability-with-Microsoft-Teams-via-NextPlane-OpenHub-is-now-available.html
site_name: tldr
content_file: tldr-google-workspace-updates-google-chat-external-inte
fetched_at: '2026-06-01T04:17:40.833445'
original_url: https://workspaceupdates.googleblog.com/2026/05/google-chat-external-interoperability-with-Microsoft-Teams-via-NextPlane-OpenHub-is-now-available.html
date: '2026-06-01'
description: Google Chat and Microsoft Teams Interoperability Now Available (2 minute read)
tags:
- tldr
---

arrow_back

 Back
 

May 28, 2026

# Google Chat external interoperability with Microsoft Teams via NextPlane OpenHub is now available

* Google Chat
* Rapid Release
* Scheduled Release

Organizations often need to collaborate with customers, partners, and suppliers who use Microsoft Teams. 
NextPlane OpenHub
 was built to bridge this Google Chat and Microsoft Teams divide, and it is now launching external interoperability to allow communication across organizational boundaries. OpenHub directly connects Google Chat users to people on external Microsoft Teams tenants, making cross-platform collaboration more seamless.
This release supports external interoperability between Google Chat and Microsoft Teams, including presence, 1:1 chat, group chat, Channels and Spaces, file sharing, and meeting and call initiation. A single Google Workspace environment can connect to multiple external Microsoft Teams tenants via OpenHub, enabling cross-tenant collaboration through a single interoperability layer. OpenHub is designed to provide a familiar cross-platform collaboration experience without requiring all parties to use the same collaboration platform.
OpenHub is also designed to support enterprise governance and deployment requirements. It is deployed as a dedicated single-tenant service, can run in a customer-owned GCP project, and keeps customer data under customer control. It uses customer-managed identities and does not require fake user accounts, Nextplane-controlled user accounts, cross-tenant impersonation, or a proxy Teams tenant.
For Google Workspace admins and IT decision-makers, this can help reduce deployment friction through tightly scoped, auditable permissions aligned with customer best practices. Ongoing configuration and management are handled through the existing Google Admin console and Microsoft Teams admin center, without requiring a separate OpenHub administration console. This is especially important for Google Workspace customers working with external organizations, because it avoids imposing a separate portal or a new management process on customers, partners, and suppliers.
Examples of how this can be used include:
* Collaborate with customers, partners, and suppliers who use Microsoft Teams
* Support cross-Teams tenant collaboration from a single Google Workspace environment
* Maintain cross-platform communication during multi-company projects, joint ventures, or extended partner workflows
* Enable interoperability when domain validation requirements make internal interoperability difficult to deploy

### Getting started

* Admins:This feature requires administrator consent on both sides of the connection, and Workspace and Teams admins must register NextPlan OpenHub as an enterprise application with their respective platforms before use. Configuration is managed at the domain level through the Google Admin console and Microsoft Teams admin center. OpenHub does not require a separate administration console and is managed through existing platform controls. Visit the NextPlane site tolearn more about connecting Teams and Workspace.
* End users:There is no end user setting for this feature.

### Rollout pace

* Rapid Release and Scheduled Release domains:Available now

### Availability

* Business:Business Starter, Standard, and Plus
* Enterprise:Enterprise Starter, Standard, and Plus
Note that separate NextPlane licensing is required to enable interoperability.

### Resources

* NextPlane:Connect Teams & Google Workspace
* Workspace Updates Blog:Introducing enhanced interoperability between Google Chat and Microsoft Teams — powered by NextPlane
* NextPlane Blog:Google and NextPlane Partner to Enhance Cross-Platform Collaboration for Google Workspace Customers