---
title: Building an Enterprise-Grade SQL Platform on Kubernetes using Crossplane and Azure PostgreSQL | Microsoft Community Hub
url: https://techcommunity.microsoft.com/blog/azureinfrastructureblog/building-an-enterprise-grade-sql-platform-on-kubernetes-using-crossplane-and-azu/4515635
site_name: tldr
content_file: tldr-building-an-enterprise-grade-sql-platform-on-kuber
fetched_at: '2026-06-04T12:02:27.703116'
original_url: https://techcommunity.microsoft.com/blog/azureinfrastructureblog/building-an-enterprise-grade-sql-platform-on-kubernetes-using-crossplane-and-azu/4515635
date: '2026-06-04'
description: Strategic Overview Build a Kubernetes-native SQL platform using Crossplane-based database operator to provision Azure PostgreSQL Flexible...
tags:
- tldr
---

## Blog Post

Azure Infrastructure Blog 
7 MIN READ

# Building an Enterprise-Grade SQL Platform on Kubernetes using Crossplane and Azure PostgreSQL

prabhattomar
Microsoft
Apr 29, 2026

## A Practical Engineering Deep Dive into HA, DR, DNS, and Real-World Operations

## Strategic Overview

* Build a Kubernetes-native SQL platform using Crossplane-based database operator to provision Azure PostgreSQL Flexible Server.
* Active–Passive, multi-region database architecture using read replicas and manual promotion for failover.
* Private networking, DNS abstraction, and virtual endpoints to ensure secure and stable connectivity.
* Azure Traffic Manager + DNS failover strategy to enable global routing and minimize manual intervention.
* Enterprise-grade HA/DR, with replication, backup, and failover testing workflows.
* Observability via Azure Monitor + Datadog for proactive detection (CPU, replication lag, etc.).
* Security-first architecture with private endpoints, Azure AD authentication, and no public access.

## Problem Statement

Modern platform teams struggle to offer database-as-a-service (DBaaS) with the same level of automation, governance, and consistency that exists for stateless workloads in Kubernetes.

Key gaps:

* Database provisioning is still manual, ticket-driven, or portal-based
* Lack of standardized HA/DR patterns across teams
* Inconsistent networking, DNS, and security configurations
* Failover and DR processes require manual intervention and risk downtime
* No unified declarative interface for database lifecycle management

## Goals

Design and implement a Kubernetes-native, enterprise-grade SQL platform that:

* Exposes databases as declarative Kubernetes resources
* Automates provisioning via Crossplane using Azure PostgreSQL Flexible Server
* Provides built-in HA/DR capabilities across regions
* Enables seamless failover through DNS abstraction
* Enforces secure, private, and compliant database access patterns
* Integrates observability, backup, and operational controls by default
* Delivers a self-service experience for developers without compromising governance

## Architecture Overview

* Crossplane acts as the control plane, translating Kubernetes intent into Azure-managed DB resources
* Azure PostgreSQL Flexible Server provides managed HA + replication primitives
* Private DNS + Private Endpoints ensure zero public exposure
* Traffic Manager enables global abstraction and failover routing
* Replica promotion + DNS switch = DR execution model

 

## Kubernetes-Native Provisioning (Crossplane)

### What I built

A custom database resource exposed to Kubernetes users:

kind: XPostgreSQLDatabase

Defines:

* Primary and secondary regions
* Storage and compute config
* Networking + DNS
* Security (credentials as secret references)

From config:

* Primary region: eastus2
* Secondary region: central us
* Private DNS zone used: testmulti.postgres.database.azure.com
* DB size and storage configured declaratively
* Credentials managed via Kubernetes Secret

### Crossplane Foundation

* Provider configuration uses Azure credentials via Kubernetes secret:

apiVersion: azure.m.upbound.io/v1beta1
kind: ClusterProviderConfig
metadata:
 name: default
spec:
 credentials:
 source: Secret
 secretRef:
 namespace: crossplane-system
 name: azure-creds
 key: credentials
---
apiVersion: azure.upbound.io/v1beta1
kind: ProviderConfig
metadata:
 name: default
spec:
 credentials:
 source: Secret
 secretRef:
 namespace: crossplane-system
 name: azure-creds
 key: credentials

* Functions extend composition logic:

apiVersion: pkg.crossplane.io/v1beta1
kind: Function
metadata:
 name: function-patch-and-transform
spec:
 package: xpkg.upbound.io/crossplane-contrib/function-patch-and-transform:v0.8.2

### Step-by-Step Implementation

1. Define Platform API

* Create XRD (Composite Resource Definition)
* Expose database as a Kubernetes primitive (XPostgreSQLDatabase)

2. Build Composition

* Map Kubernetes resource → Azure PostgreSQL Flexible Server
* Create:Primary serverReplica server (secondary region)Networking artifacts (Private Endpoint, DNS)
* Primary server
* Replica server (secondary region)
* Networking artifacts (Private Endpoint, DNS)

3. Provision Database

* Developer applies custom resource
* Crossplane:Calls Azure APIsCreates full database topology
* Calls Azure APIs
* Creates full database topology

### Control-plane prerequisites

#### 1. Install the Crossplane functions

Your attached functions.yaml installs two functions:

* function-patch-and-transform
* crossplane-contrib-function-python

apiVersion: pkg.crossplane.io/v1beta1
kind: Function
metadata:
 name: function-patch-and-transform
spec:
 package: xpkg.upbound.io/crossplane-contrib/function-patch-and-transform:v0.8.2
---
apiVersion: pkg.crossplane.io/v1beta1
kind: Function
metadata:
 name: crossplane-contrib-function-python
spec:
 package: ghcr.io/crossplane-contrib/function-python:v0.2.0

#### 2. Configure the Azure provider credentials

Your provider-config.yaml defines both a ClusterProviderConfig and a namespaced ProviderConfig, each reading credentials from the azure-creds secret in the crossplane-system namespace.

apiVersion: azure.m.upbound.io/v1beta1
kind: ClusterProviderConfig
metadata:
 name: default
spec:
 credentials:
 source: Secret
 secretRef:
 namespace: crossplane-system
 name: azure-creds
 key: credentials
---
apiVersion: azure.upbound.io/v1beta1
kind: ProviderConfig
metadata:
 name: default
 namespace: crossplane-system
spec:
 credentials:
 source: Secret
 secretRef:
 namespace: crossplane-system
 name: azure-creds
 key: credentials

## What Crossplane creates from that XR

#### 1. Resource Group

The composition first creates an Azure ResourceGroup, with its location patched from spec.regions.primary.name and its name patched from spec.resourceGroup.name. It also writes the resulting resource group name back into composite status.

- name: resource-group
 base:
 apiVersion: azure.upbound.io/v1beta1
 kind: ResourceGroup
 spec:
 forProvider:
 location: eastus2
 patches:
 - type: FromCompositeFieldPath
 fromFieldPath: spec.regions.primary.name
 toFieldPath: spec.forProvider.location
 - type: FromCompositeFieldPath
 fromFieldPath: spec.resourceGroup.name
 toFieldPath: metadata.name
 - type: ToCompositeFieldPath
 fromFieldPath: metadata.name
 toFieldPath: status.resourceGroupName

#### 2. Backup storage resources

The managed composition also creates:

* a storage account with accountReplicationType: GRS
* a backup container in that account

- name: backup-storage-account
 base:
 apiVersion: storage.azure.upbound.io/v1beta2
 kind: Account
 spec:
 forProvider:
 accountTier: Standard
 accountReplicationType: GRS
 sharedAccessKeyEnabled: true
 tags:
 purpose: postgresql-backups
 automation: enabled

- name: backup-container
 base:
 apiVersion: storage.azure.upbound.io/v1beta1
 kind: Container

#### 3. Private DNS zone

A PrivateDNSZone is created, and its external name is patched from spec.network.privateDnsZoneName. The zone name is also written back into composite status.

- name: private-dns-zone
 base:
 apiVersion: network.azure.upbound.io/v1beta1
 kind: PrivateDNSZone
 metadata:
 annotations:
 crossplane.io/external-name: postgres.database.azure.com
 patches:
 - type: FromCompositeFieldPath
 fromFieldPath: spec.network.privateDnsZoneName
 toFieldPath: metadata.annotations[crossplane.io/external-name]
 - type: ToCompositeFieldPath
 fromFieldPath: metadata.annotations[crossplane.io/external-name]
 toFieldPath: status.dnsZoneName

#### 4. Primary region network

The composition creates aprimary virtual network,primary subnet, and aPrivate DNS zone link. The VNet CIDR comes from spec.regions.primary.cidr. The subnet CIDR is derived from that primary CIDR using a regexp + format transform. The subnet is delegated to Microsoft.DBforPostgreSQL/flexibleServers.

- name: primary-vnet
 base:
 apiVersion: network.azure.upbound.io/v1beta1
 kind: VirtualNetwork
 metadata:
 labels:
 role: primary
 spec:
 forProvider:
 addressSpace:
 - 10.0.0.0/16
 patches:
 - type: FromCompositeFieldPath
 fromFieldPath: spec.regions.primary.cidr
 toFieldPath: spec.forProvider.addressSpace[0]

- name: primary-subnet
 base:
 apiVersion: network.azure.upbound.io/v1beta1
 kind: Subnet
 metadata:
 labels:
 role: primary
 spec:
 forProvider:
 delegation:
 - name: fs
 serviceDelegation:
 - name: Microsoft.DBforPostgreSQL/flexibleServers

#### 5. Primary database server

The primary Azure PostgreSQL Flexible Server is created with:

* private access only (publicNetworkAccessEnabled: false)
* subnet delegated from the primary subnet
* private DNS zone association
* admin credentials patched from the composite spec
* SKU, storage, version, retention, and backup settings patched from the composite spec
* FQDN and server ID written back into composite status

- name: primary-server
 base:
 apiVersion: dbforpostgresql.azure.upbound.io/v1beta1
 kind: FlexibleServer
 metadata:
 labels:
 role: primary
 autoscaling: enabled
 annotations:
 management.platform.io/autoscale-enabled: 'true'
 management.platform.io/backup-enabled: 'true'
 spec:
 forProvider:
 publicNetworkAccessEnabled: false
 administratorLogin: psqladmin
 administratorPasswordSecretRef:
 name: ''
 namespace: crossplane-system
 key: password
 patches:
 - type: FromCompositeFieldPath
 fromFieldPath: spec.database.size
 toFieldPath: spec.forProvider.skuName
 - type: FromCompositeFieldPath
 fromFieldPath: spec.database.storageGB
 toFieldPath: spec.forProvider.storageMb
 - type: FromCompositeFieldPath
 fromFieldPath: spec.database.version
 toFieldPath: spec.forProvider.version
 - type: FromCompositeFieldPath
 fromFieldPath: spec.database.backupRetentionDays
 toFieldPath: spec.forProvider.backupRetentionDays
 - type: FromCompositeFieldPath
 fromFieldPath: spec.database.geoRedundantBackup
 toFieldPath: spec.forProvider.geoRedundantBackupEnabled
 - type: FromCompositeFieldPath
 fromFieldPath: spec.security.adminUsername
 toFieldPath: spec.forProvider.administratorLogin

#### 6. Secondary region network and replica

The composition then creates:

* secondary VNet
* secondary subnet
* DNS link for the secondary VNet
* bidirectional VNet peering
* a secondary PostgreSQL Flexible Server with createMode: Replica

- name: secondary-server
 base:
 apiVersion: dbforpostgresql.azure.upbound.io/v1beta1
 kind: FlexibleServer
 metadata:
 labels:
 role: secondary
 replica: 'true'
 annotations:
 management.platform.io/failover-candidate: 'true'
 management.platform.io/promotion-priority: '1'
 spec:
 forProvider:
 location: centralus
 createMode: Replica
 sourceServerId: ''
 publicNetworkAccessEnabled: false
 patches:
 - type: CombineFromComposite
 combine:
 variables:
 - fromFieldPath: metadata.name
 strategy: string
 string:
 fmt: /subscriptions/96618111-38e8-48c0-b564-ee5acde49c15/resourceGroups/postgres-crossplane-rg/providers/Microsoft.DBforPostgreSQL/flexibleServers/%s-primary
 toFieldPath: spec.forProvider.sourceServerId

#### 7. Read/write DNS records

The composition creates multiple PrivateDNSCNAMERecord resources for read and write endpoint abstraction. These records are patched from spec.network.privateDnsZoneName, spec.network.writeEndpointName, and spec.network.readEndpointName, and some are annotated with management.platform.io/update-on-failover: 'true'.

- name: cname-write
 base:
 apiVersion: network.azure.upbound.io/v1beta1
 kind: PrivateDNSCNAMERecord
 metadata:
 annotations:
 management.platform.io/managed-by: failover-script
 management.platform.io/update-on-failover: 'true'
 spec:
 forProvider:
 ttl: 300

- name: cname-read
 base:
 apiVersion: network.azure.upbound.io/v1beta1
 kind: PrivateDNSCNAMERecord
 metadata:
 annotations:
 management.platform.io/managed-by: failover-script
 management.platform.io/update-on-failover: 'true'
 spec:
 forProvider:
 ttl: 300

#### 8. Management objects inside Kubernetes

The managed composition also creates Kubernetes-native control objects through the Kubernetes provider:

* a ConfigMap for management settings
* a ServiceAccount
* a ClusterRole
* a ClusterRoleBinding

- name: management-config
 base:
 apiVersion: kubernetes.crossplane.io/v1alpha1
 kind: Object
 spec:
 forProvider:
 manifest:
 apiVersion: v1
 kind: ConfigMap
 data:
 backup-enabled: "true"
 backup-retention-days: "35"
 autoscaling-enabled: "true"
 failover-enabled: "true"

- name: management-clusterrole
 base:
 apiVersion: kubernetes.crossplane.io/v1alpha1
 kind: Object
 spec:
 forProvider:
 manifest:
 apiVersion: rbac.authorization.k8s.io/v1
 kind: ClusterRole

## High Availability (HA) and Disaster Recovery (DR)

### High Availability (HA) Strategy

#### Design Principles

* Ensure minimal disruption for infrastructure-level failures
* Leveragemanaged Azure HA capabilities
* Maintain consistent connectivity through private networking

### Implementation

#### 1. Zone-Redundant High Availability (Primary Region)

* PostgreSQL Flexible Server supports zone-redundant HA deployment
* Primary database instance is replicated synchronously across Availability Zones
* Platform configuration enables:Same-region redundancyAutomatic failover within region (infrastructure-level issues)
* Same-region redundancy
* Automatic failover within region (infrastructure-level issues)

Failover within region is handled by Azure, but cross-region failover is not automatic

#### 2. Resource Connectivity (HA Path)

Within a region, connectivity follows:

Application → Private DNS → Private Endpoint → PostgreSQL Primary

* Private endpoints connect database to VNet
* Private DNS ensures internal resolution
* Traffic never leaves Azure backbone
* Public access is disabled

### Disaster Recovery (DR) Strategy

#### Design Principles

* Handle regional outages and large-scale failures
* Ensure data durability and failover capability
* Minimize RPO and RTO impact

#### 1. Cross-Region Replication Architecture

* Secondary PostgreSQL server deployed in paired region
* Configured as read replica (asynchronous replication)
* Example:Primary: East US 2Secondary: Central US
* Primary: East US 2
* Secondary: Central US

Primary (Write) ─────────► Replica (Read) Async Replication

* Replica is continuously receiving updates but not writable

#### 2. Resource Connectivity (DR Path)

Cross-region setup includes:

* Global VNet + Hub-Spoke connectivity
* Private endpoints in both regions
* Shared Private DNS zone

App → DNS → Traffic Manager → Region Endpoint → Private Endpoint → DB

* Cross-region communication uses Azure backbone

#### 3. Failover Process (DR Execution)

Azure PostgreSQL does not provide automatic global failover, hence DR is controlled and explicit

#### Step-by-step failover:

* Detect primary region failure
* Promote replica to standalone primary
* Update DNS / Traffic Manager routing
* Redirect application traffic
* Validate connectivity and resume operations

Replica → Promote → Becomes Primary → Traffic redirected

## Conclusion

We modeled the database platform as a Kubernetes-native composite API, XPostgreSQLDatabase, and delegated infrastructure realization to a Crossplane pipeline composition. The composition reads user intent from the composite spec—regions, CIDR ranges, DNS settings, database sizing, retention, and admin secret references—and translates that into Azure resources including a resource group, private DNS zone, regional VNets and subnets, bidirectional peering, a primary Azure PostgreSQL Flexible Server, a cross-region replica, and private DNS CNAME records for read/write abstraction. In the managed variant, the composition also creates Kubernetes-side management artifacts for backup, autoscaling, and failover-related configuration.

 
Updated 
Apr 29, 2026
Version 1.0
Comment
Comment
prabhattomar
Microsoft
Joined 
March 04, 2025
Send Message
View Profile
Azure Infrastructure Blog 
Follow this blog board to get notified when there's new activity