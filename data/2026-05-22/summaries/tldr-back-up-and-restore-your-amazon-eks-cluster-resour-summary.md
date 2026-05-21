---
title: Back up and restore your Amazon EKS cluster resources using Velero | Containers
url: https://aws.amazon.com/blogs/containers/back-up-and-restore-your-amazon-eks-cluster-resources-using-velero/
date: 2026-05-22
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-05-22T06:01:24.362882
---

# Back up and restore your Amazon EKS cluster resources using Velero | Containers

# Back up and restore your Amazon EKS cluster resources using Velero

## Introduction
- Manual recreation of deployments, services, and persistent volumes is required after accidental namespace deletion or failed cluster upgrades.  
- Velero backs up Kubernetes resource definitions to Amazon S3 and persistent‑volume data to Amazon EBS snapshots.  
- Supports cross‑cluster restores, namespace‑level granularity, and portability across Kubernetes distributions.  
- For fully managed backup scheduling, AWS Backup for Amazon EKS can be used instead.

## What the tutorial covers
- Deploy a sample stateful application on Amazon EKS.  
- Back up the application’s resources and persistent‑volume data with Velero.  
- Restore the backup to a different namespace within the same cluster.  
- Configure least‑privilege IAM roles using Amazon EKS Pod Identity.  
- Scope Velero’s Kubernetes permissions with a custom ClusterRole.

## Prerequisites
- 45–60 minutes; expect charges for S3 storage, EBS snapshots, and EKS cluster runtime.  
- Active AWS account with permissions to create S3 buckets, IAM policies/roles, and EKS resources.  
- Amazon EKS cluster (Kubernetes 1.35+), Auto Mode enabled (optional for tutorial).  
- AWS CLI v2, Helm v3.x, and kubectl installed and configured.  
- Basic knowledge of Kubernetes objects (pods, deployments, PVs) and IAM roles.  
- Note: Default Velero install uses `cluster-admin`; tutorial replaces it with a least‑privilege ClusterRole for production use.

## Velero overview
- Open‑source, Kubernetes‑native backup and restore tool.  
- Operates via the Kubernetes API, eliminating direct storage‑system access.  
- Key advantages:  
  - Understands Kubernetes resources and relationships.  
  - Flexible filtering by namespace, resource type, or label.  
  - Cloud‑agnostic; restores possible on different Kubernetes distributions.  
  - Integrates with cloud provider snapshot APIs for persistent‑volume backups.  
- Backup targets in Amazon EKS:  
  - Control‑plane objects and configurations.  
  - Application data stored in persistent volumes.  

## Backup and restore workflow
- Velero controller runs as a Kubernetes Deployment.  
- Users submit `Backup` or `Restore` custom‑resource manifests.  
- Controller processes the manifests and performs the requested operation.  

## Tutorial steps (high‑level)

### 1. Set environment variables
```bash
export CLUSTER_NAME=<<Cluster Name>>
export AWS_REGION=<<AWS region>>
export AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text --no-cli-pager)
export BUCKET_NAME=velero-backups-$(date +%s)
export POLICY_NAME=VeleroBackupPolicy
export ROLE_NAME=VeleroBackupRole
export AWS_PAGER=""
```

### 2. Create S3 bucket and IAM policy
- Create bucket: `aws s3 mb s3://${BUCKET_NAME} --region ${AWS_REGION}`  
- Define policy (`velero-s3-policy.json`) granting S3 read/write and EBS snapshot permissions.  
- Create policy: `aws iam create-policy --policy-name ${POLICY_NAME} --policy-document file://velero-s3-policy.json`

### 3. Create IAM role with EKS Pod Identity trust
- Capture policy ARN.  
- Define trust policy (`velero-trust-policy.json`) allowing `pods.eks.amazonaws.com` to assume the role when tagged with `kubernetes-namespace: velero` and `kubernetes-service-account: velero`.  
- Create role and attach policy.  
- Associate role with Velero service account via `aws eks create-pod-identity-association`.

### 4. Install snapshot controller add‑on
```bash
aws eks update-kubeconfig --name ${CLUSTER_NAME}
aws eks create-addon --cluster-name ${CLUSTER_NAME} --addon-name snapshot-controller --region ${AWS_REGION}
```

### 5. Prepare Helm values for Velero
- Create `velero-values.yaml` configuring:
  - Backup storage location (S3 bucket, region).  
  - Volume snapshot location (EBS, region).  
  - CSI feature enabled.  
  - Service account using Pod Identity (no secret credentials).  
  - AWS plugin init container.

### 6. Install Velero with Helm
```bash
helm repo add vmware-tanzu https://vmware-tanzu.github.io/helm-charts
helm repo update
helm install velero vmware-tanzu/velero -n velero --create-namespace -f velero-values.yaml
```
- Verify Velero pod is running (`kubectl get pods -n velero`).

### 7. Deploy sample stateful application
- Deploy a namespace (e.g., `myprimary`) and a stateful workload with a PVC.  
- Ensure the application writes data to the persistent volume.

### 8. Create a Velero backup
```yaml
apiVersion: velero.io/v1
kind: Backup
metadata:
  name: myprimary-backup
  namespace: velero
spec:
  includedNamespaces:
  - myprimary
  storageLocation: default
  snapshotVolumes: true
```
- Apply manifest and monitor backup status (`kubectl get backup -n velero`).

### 9. Restore to a new namespace
```yaml
apiVersion: velero.io/v1
kind: Restore
metadata:
  name: myrestore
  namespace: velero
spec:
  backupName: myprimary-backup
  restoreNamespaceMapping:
    myprimary: myrestore
```
- Apply manifest and verify restored resources and PVC data in `myrestore`.

### 10. Clean up
- Delete Velero resources, S3 bucket, IAM policy/role, and EKS add‑on.  
- Terminate the EKS cluster if no longer needed to avoid ongoing charges.

## Key takeaways
- Velero provides a Kubernetes‑native, cloud‑agnostic way to back up both control‑plane objects and persistent‑volume data.  
- Using Amazon EKS Pod Identity enables least‑privilege IAM role assignment without managing static credentials.  
- Custom ClusterRoles can replace the default `cluster-admin` permissions for production‑grade security.  
- The workflow demonstrated (backup → restore to another namespace) can be extended to cross‑cluster migrations or disaster‑recovery scenarios.