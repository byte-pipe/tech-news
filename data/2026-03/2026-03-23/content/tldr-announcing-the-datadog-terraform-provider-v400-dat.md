---
title: Announcing the Datadog Terraform provider v4.0.0 | Datadog
url: https://www.datadoghq.com/blog/datadog-terraform-provider-v4/
site_name: tldr
content_file: tldr-announcing-the-datadog-terraform-provider-v400-dat
fetched_at: '2026-03-23T19:49:13.061083'
original_url: https://www.datadoghq.com/blog/datadog-terraform-provider-v4/
author: David Iparraguirre, SeGe Jung, Justin Yan
date: '2026-03-23'
description: Learn how the new Datadog Terraform provider improves monitor governance, AWS integrations, and application key security.
tags:
- tldr
---

Further Reading

 
 

Datadog Platform Datasheet

 
 
 
 
 
 
 
 
 
 

Learn about the key components, capabilities, and features of the Datadog platform.

 
 
Download to learn more
 
 
 
 
 
 
 

David Iparraguirre

 
 
 
 
 
 

SeGe Jung

 
 
 
 
 
 

Justin Yan

 

Datadog supports managing Datadog configuration as code through theDatadog Terraform provider. As platform engineering practices evolve, we are focused on making this provider more reliable and trustworthy at enterprise scale.

We’re excited to announce the Datadog Terraform provider v4.0.0. This major release is designed to improve reliability and enforce stricter security standards so that teams can have even greater trust in their infrastructure-as-code (IaC) configurations. With v4.0.0, teams get predictable access controls for monitors and a unified AWS integration that replaces four different resources. The new provider also supports one-time read application keys for stronger credential security and provides a foundational upgrade to support future feature improvements.

This post introduces the key improvements in the Datadog Terraform provider v4.0.0 and shares guidance to help you upgrade when your team is ready. Specifically, it will cover how the Datadog Terraform provider v4.0.0 enables you to:

* Enforce predictable monitor governance in code
* Simplify AWS integration management through one unified resource
* Harden credential security
* Upgrade provider capabilities with Terraform protocol v6

## Enforce predictable monitor governance in code

Teams have asked for monitor editing permissions that behave predictably when managed as code so that Terraform can stay the source of truth for governance. In v4.0.0, monitor permissions are designed to persist exactly as defined in configuration so that access control intent stays stable across normal plan/apply workflows.

The Datadog Terraform provider v4 makes changes to monitor restriction behavior more explicit, so permission updates reflect deliberate intent. Specifically,restricted_rolesis now “sticky” by default, which means that you must explicitly set it to[]if you intend to remove all restrictions. This helps teams avoid accidental permission wipes during routine updates.

 
 
 
 
 
 
 
 
 
 
 
 
 
 
Close dialog

 
 
 
 
 
 

Datadog Terraform provider v4 also clarifies the forward path for managing monitor edit permissions by standardizing onrestriction_policy. The deprecatedlockedfield is removed, and we recommend migrating permission control torestriction_policygoing forward.

## Simplify AWS integration management through one unified resource

As AWS footprints grow, platform teams need one place in Terraform to link accounts and manage integration settings. The Datadog Terraform provider v4 introducesdatadog_integration_aws_accountas that unified resource and a single source of truth. In v4.0.0, it replaces four legacy AWS integration resources from v3. It also adds capabilities like log tag filtering,X-Raytracing collection,EC2 automute control, andAWS partitionsupport.

When teams upgrade to Datadog Terraform provider v4, they migrate from the legacy AWS resources todatadog_integration_aws_account, while the underlying v1 APIs remain live. Teams that stay on v3 can keep using the legacy resources, and teams that move to v4 adopt the unified resource.

## Harden credential security

The Datadog Terraform provider v4 tightens application key workflows to reduce exposure, while keeping core key management intact. In the Datadog Terraform provider v4, thedatadog_application_keydata source is removed to reduce pathways that could expose raw application keys through Terraform. The Datadog Terraform provider v4 also removes support for importing preexisting application keys into thedatadog_application_keyresource. These changes enable compatibility withone-time read application keys.

For most teams, upgrading does not change how they create and manage application keys through Terraform. Terraform can still create, edit, and delete application keys, and keys already managed in Terraform continue to work after you upgrade. Terraform still stores secrets in state as it always has, and this release does not change that behavior. Teams only need to update workflows that fetched preexisting keys via the removed data source or that imported preexisting keys into state.

## Upgrade provider capabilities with Terraform protocol v6

The Datadog Terraform provider v4 upgrades the provider’s foundation so that future improvements to schemas and validation are easier to ship. Specifically, the provider moves from Terraform Plugin SDK v2 to theTerraform plugin framework, which implementsTerraform protocol v6. Protocol v6 supports nested attributes and enables a more user-friendly evolution path for the provider.

## Strengthen governance, security, and IaC reliability

The Datadog Terraform provider v4.0.0 is a major step toward a more reliable observability-as-code experience. It delivers predictable monitor governance, a unified AWS integration resource, hardened application key workflows, and a modern protocol v6 foundation for future schema improvements.

When you’re ready to upgrade, start by confirming yourTerraform CLIis 1.1.5 or later. Then followthe migration guidance for the AWS integration changesand application key workflows. If you are staying on v3 for now, your existing configurations will continue to work until you choose to upgrade.

To learn more about the Datadog Terraform provider, you can consult theDatadog documentationor view theTerraform Registry documentationandhands-on tutorialon the Terraform site.

If you’re not yet a Datadog customer, you cansign up for a 14-day free trial.

 

## RelatedArticles

 
 
 
 
 
 
 
 
 
 
 
 
 

## Managing Datadog with Terraform

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

## Approaching your observability migration with the right mindset

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

## Manage your dashboards and monitors at scale

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

## Monitor Azure AI Search with Datadog

 
 
 
 
 
 
 
 
 

## Related jobs at Datadog

 
 

### We're always looking for talented people to collaborate with

 
 

Featured positions

 
 
 
 
 
 
 
 
 
 
 

We havepositions

 
 
 
 
View all
 
 
 
 
 
 
 

## Start monitoring your metrics in minutes

 
find out how