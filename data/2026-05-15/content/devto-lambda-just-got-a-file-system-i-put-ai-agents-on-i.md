---
title: Lambda Just Got a File System. I Put AI Agents on It. - DEV Community
url: https://dev.to/aws/lambda-just-got-a-file-system-i-put-ai-agents-on-it-1ej8
site_name: devto
content_file: devto-lambda-just-got-a-file-system-i-put-ai-agents-on-i
fetched_at: '2026-05-15T11:42:19.154540'
original_url: https://dev.to/aws/lambda-just-got-a-file-system-i-put-ai-agents-on-it-1ej8
author: Eric D Johnson
date: '2026-05-13'
description: You've written this code before. An S3 event fires, your Lambda function wakes up, and the first... Tagged with serverless, aws, lambda, ai.
tags: '#serverless, #aws, #lambda, #ai'
---

Eliminating the /tmp tax for shared workspaces

You've written this code before. An S3 event fires, your Lambda function wakes up, and the first thing it does is download a file to/tmp. Process it. Upload the result. Clean up/tmpso you don't run out of space. Repeat for every file, every invocation, every function in your pipeline.

S3 Files changes that. You mount your S3 bucket as a local file system, and your Lambda code just usesopen(). I built a set of AI code review agents that share a workspace through a mounted S3 bucket, orchestrated by a durable function, and the file access code is the most boring part of the whole project. That's the point.

## The /tmp Tax

If you've built anything on Lambda that touches S3 data, you know the pattern. You need a file. S3 doesn't give you files. It gives you objects. So you download the object to/tmp, do your work, and upload the result back.

# The old way: every Lambda developer has written this

import
 
boto3

s3
 
=
 
boto3
.
client
(
"
s3
"
)

def
 
lambda_handler
(
event
,
 
context
):

 
bucket
 
=
 
event
[
"
bucket
"
]

 
key
 
=
 
event
[
"
key
"
]

 
# Download to /tmp

 
local_path
 
=
 
f
"
/tmp/
{
key
.
split
(
'
/
'
)[
-
1
]
}
"

 
s3
.
download_file
(
bucket
,
 
key
,
 
local_path
)

 
# Do your actual work

 
with
 
open
(
local_path
)
 
as
 
f
:

 
content
 
=
 
f
.
read
()

 
result
 
=
 
process
(
content
)

 
# Upload the result

 
s3
.
put_object
(
Bucket
=
bucket
,
 
Key
=
f
"
output/
{
key
}
"
,
 
Body
=
result
)

 
# Clean up so you don't fill /tmp

 
os
.
remove
(
local_path
)

Enter fullscreen mode

Exit fullscreen mode

That's a lot of ceremony for "read a file and write a file." And it gets worse when you have multiple functions that need to work with the same data. Each one downloads its own copy. Each one manages its own/tmp. If you're processing a large repo or a dataset, you're burning through the 10GB/tmplimit fast.

I'd be doing you a disservice if I didn't mention the libraries that make this less painful. Tools likes3fsandsmart_openabstract some of this away. But they're still making API calls under the hood. Your code is still talking to S3 through an SDK, not through a file system.

## S3 Files for Lambda

S3 Files is a new feature that mounts your S3 bucket as a local file system on your Lambda function. Your code reads and writes files at a mount path like/mnt/workspace, and S3 Files handles the synchronization back to the bucket. Changes you write show up in S3 within minutes. Changes made to S3 objects appear on the file system within seconds.

# The new way: just file paths

from
 
pathlib
 
import
 
Path

WORKSPACE
 
=
 
Path
(
"
/mnt/workspace
"
)

def
 
lambda_handler
(
event
,
 
context
):

 
# Read directly from the mount

 
content
 
=
 
(
WORKSPACE
 
/
 
"
source
"
 
/
 
"
app.py
"
).
read_text
()

 
result
 
=
 
process
(
content
)

 
# Write directly to the mount

 
(
WORKSPACE
 
/
 
"
output
"
 
/
 
"
result.json
"
).
write_text
(
result
)

Enter fullscreen mode

Exit fullscreen mode

No boto3 for file access. No/tmpmanagement. No upload step. The file system IS the interface.

Under the hood, S3 Files is built on Amazon EFS. It delivers sub-millisecond latency for actively used data by caching your working set on high-performance storage. For large sequential reads, it streams directly from S3. You get file system semantics with S3 durability and economics.

Here's the thing, though. S3 Files requires a VPC. Your Lambda function needs to be in the same VPC as the mount targets, and you need a NAT gateway for outbound internet access.

I'll be honest: as a serverless guy, I generally avoid VPCs. But AWS has removed most of the hurdles over the years. VPC-attached Lambda functions no longer have the cold start penalty they used to. The networking setup is boilerplate you write once. And for what S3 Files gives you, the tradeoff is worth it. Get yourself a reusable network template and move on.

## What We're Building

I wanted to test S3 Files with something more interesting than "read a CSV." So I built a serverless code review system. You point it at a public GitHub repo, and three things happen:

1. A durable orchestrator function clones the repo to a shared S3 Files workspace
2. A security review agent and a style review agent analyze the code in parallel
3. The results land in the same workspace as JSON files, synced back to S3

All three Lambda functions mount the same S3 bucket. The orchestrator writes files. The agents read them. No S3 keys passed between functions. No downloading to/tmp. The file system is the coordination layer.

The agents use the Strands Agents SDK with Amazon Bedrock. Each agent gets custom file tools that operate on the mount path, and Claude decides which files to read, what to analyze, and what to write. The orchestrator uses Lambda durable functions to coordinate the workflow with automatic checkpointing.

The full source is on GitHub:singledigit/lambda-s3-files-example

## The SAM Template

The IaC is the part that took the most iteration. S3 Files is brand new, and the CloudFormation resource types aren't in the linter yet. Here's what I learned.

### The Resource Chain

You need five resources to get S3 Files working with Lambda:

1. S3 Bucketwith versioning enabled (required)
2. IAM Rolefor S3 Files to access the bucket
3. S3 Files FileSystemthat bridges the bucket to NFS
4. Mount Targetsin each AZ (network endpoints)
5. Access Pointthat controls POSIX identity for Lambda

The resource types areAWS::S3Files::FileSystem,AWS::S3Files::MountTarget, andAWS::S3Files::AccessPoint. Your IDE's CloudFormation linter won't recognize them yet. Ignore the red squiggles.

### The IAM Role Gotcha

The S3 Files IAM role trustselasticfilesystem.amazonaws.com, nots3files.amazonaws.com. This tripped me up. S3 Files is built on EFS, so the trust relationship goes through the EFS service principal.

S3FilesRole
:

 
Type
:
 
AWS::IAM::Role

 
Properties
:

 
Path
:
 
/service-role/

 
AssumeRolePolicyDocument
:

 
Version
:
 
'
2012-10-17'

 
Statement
:

 
-
 
Sid
:
 
AllowS3FilesAssumeRole

 
Effect
:
 
Allow

 
Principal
:

 
Service
:
 
elasticfilesystem.amazonaws.com

 
Action
:
 
sts:AssumeRole

 
Condition
:

 
StringEquals
:

 
aws:SourceAccount
:
 
!Ref
 
AWS::AccountId

 
ArnLike
:

 
aws:SourceArn
:
 
!Sub
 
'
arn:aws:s3files:${AWS::Region}:${AWS::AccountId}:file-system/*'

Enter fullscreen mode

Exit fullscreen mode

The role needs S3 permissions to read and write the bucket. Scope it to your specific bucket ARN withaws:ResourceAccountconditions.

### The Access Point

This is the important part for Lambda. The access point controls the POSIX identity your function runs as and creates a writable root directory. Without it, Lambda can mount the file system but can't write to it.

S3FilesAccessPoint
:

 
Type
:
 
AWS::S3Files::AccessPoint

 
Properties
:

 
FileSystemId
:
 
!GetAtt
 
S3FileSystem.FileSystemId

 
PosixUser
:

 
Uid
:
 
'
1000'

 
Gid
:
 
'
1000'

 
RootDirectory
:

 
Path
:
 
/lambda

 
CreationPermissions
:

 
OwnerUid
:
 
'
1000'

 
OwnerGid
:
 
'
1000'

 
Permissions
:
 
'
755'

Enter fullscreen mode

Exit fullscreen mode

TheCreationPermissionsproperty is crucial. It auto-creates the/lambdadirectory with the right ownership when a client first connects. Without it, the root directory is owned by root (UID 0), and Lambda (running as UID 1000 through the access point) can't create subdirectories.

### Lambda Configuration

On the Lambda side,FileSystemConfigstakes the access point ARN (not the file system ARN) and a local mount path:

OrchestratorFunction
:

 
Type
:
 
AWS::Serverless::Function

 
DependsOn
:

 
-
 
MountTargetA

 
-
 
MountTargetB

 
Properties
:

 
FileSystemConfigs
:

 
-
 
Arn
:
 
!GetAtt
 
S3FilesAccessPoint.AccessPointArn

 
LocalMountPath
:
 
/mnt/workspace

 
VpcConfig
:

 
SecurityGroupIds
:

 
-
 
!GetAtt
 
NetworkingStack.Outputs.LambdaSGId

 
SubnetIds
:

 
-
 
!GetAtt
 
NetworkingStack.Outputs.PrivateSubnetAId

 
-
 
!GetAtt
 
NetworkingStack.Outputs.PrivateSubnetBId

Enter fullscreen mode

Exit fullscreen mode

TheDependsOnon the mount targets is important. Lambda can't mount the file system until the mount targets are available, and they take about five minutes to create.

## What I'd Do Differently

S3 Files is genuinely good for this use case. Shared file access between Lambda functions without the ceremony of S3 API calls. But a few things to know:

Consistency model matters.S3 Files provides close-to-open consistency. If Function A writes a file and Function B reads it immediately, B might not see the latest version. For my use case, the orchestrator writes first and the agents run after, so ordering is natural. If you need real-time coordination between concurrent writers, you'll want a different pattern.

VPC adds complexity.Not much, but some. You need subnets, security groups, NAT gateway for internet access. Template it once and reuse it.

Cold starts are fine.VPC-attached Lambda functions used to add 10+ seconds of cold start. That's been fixed for years. My functions cold-start in under 2 seconds with the file system mount.

The full code is atgithub.com/singledigit/lambda-s3-files-example. Clone it, deploy it, point it at a repo. The agents will tell you what they think.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (12 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse