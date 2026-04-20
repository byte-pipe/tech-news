---
title: 'GitHub - hectorvent/floci: Light, fluffy, and always free - AWS Local Emulator · GitHub'
url: https://github.com/hectorvent/floci
site_name: hnrss
content_file: hnrss-github-hectorventfloci-light-fluffy-and-always-fre
fetched_at: '2026-03-22T11:09:52.410360'
original_url: https://github.com/hectorvent/floci
date: '2026-03-21'
description: 'Light, fluffy, and always free - AWS Local Emulator - GitHub - hectorvent/floci: Light, fluffy, and always free - AWS Local Emulator'
tags:
- hackernews
- hnrss
---

hectorvent



/

floci

Public

* NotificationsYou must be signed in to change notification settings
* Fork16
* Star566




 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

32 Commits
32 Commits
.github
.github
 
 
docs
docs
 
 
src
src
 
 
.dockerignore
.dockerignore
 
 
.gitignore
.gitignore
 
 
.releaserc.json
.releaserc.json
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Dockerfile
Dockerfile
 
 
Dockerfile.jvm-package
Dockerfile.jvm-package
 
 
Dockerfile.native
Dockerfile.native
 
 
Dockerfile.native-package
Dockerfile.native-package
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
docker-compose-test.yml
docker-compose-test.yml
 
 
docker-compose.yml
docker-compose.yml
 
 
logo.svg
logo.svg
 
 
mkdocs.yml
mkdocs.yml
 
 
pom.xml
pom.xml
 
 
View all files

## Repository files navigation

### 🍿☁️ Light, fluffy, and always free

Named afterfloccus— the cloud formation that looks exactly like popcorn.

A free, open-source local AWS emulator. No account. No feature gates. No CI restrictions. Justdocker compose up.

LocalStack's community editionsunset in March 2026— requiring auth tokens, dropping CI support, and freezing security updates. Floci is the no-strings-attached alternative.

## Why Floci?

Floci

LocalStack Community

Auth token required

No

Yes (since March 2026)

CI/CD support

Unlimited

Requires paid plan

Security updates

Yes

Frozen

Startup time

~24 ms

~3.3 s

Idle memory

~13 MiB

~143 MiB

Docker image size

~90 MB

~1.0 GB

License

MIT

Restricted

API Gateway v2 / HTTP API

✅

❌

Cognito

✅

❌

ElastiCache (Redis + IAM auth)

✅

❌

RDS (PostgreSQL + MySQL + IAM auth)

✅

❌

S3 Object Lock (COMPLIANCE / GOVERNANCE)

✅

⚠️
 Partial

DynamoDB Streams

✅

⚠️
 Partial

IAM (users, roles, policies, groups)

✅

⚠️
 Partial

STS (all 7 operations)

✅

⚠️
 Partial

Kinesis (streams, shards, fan-out)

✅

⚠️
 Partial

KMS (sign, verify, re-encrypt)

✅

⚠️
 Partial

Native binary

✅ ~40 MB

❌

20+ services. 408/408 SDK tests passing. Free forever.

## Quick Start

#
 docker-compose.yml

services
:

floci
:

image
:
hectorvent/floci:latest


ports
:
 -
"
4566:4566
"


volumes
:
 -
./data:/app/data

docker compose up

All services are available athttp://localhost:4566. Use any AWS region — credentials can be anything.

export
 AWS_ENDPOINT_URL=http://localhost:4566

export
 AWS_DEFAULT_REGION=us-east-1

export
 AWS_ACCESS_KEY_ID=test

export
 AWS_SECRET_ACCESS_KEY=test

#
 Try it

aws s3 mb s3://my-bucket
aws sqs create-queue --queue-name my-queue
aws dynamodb list-tables

## SDK Integration

Point your existing AWS SDK athttp://localhost:4566— no other changes needed.

// Java (AWS SDK v2)

DynamoDbClient

client
 =
DynamoDbClient
.
builder
()
 .
endpointOverride
(
URI
.
create
(
"http://localhost:4566"
))
 .
region
(
Region
.
US_EAST_1
)
 .
credentialsProvider
(
StaticCredentialsProvider
.
create
(

AwsBasicCredentials
.
create
(
"test"
,
"test"
)))
 .
build
();

# Python (boto3)

import

boto3

client

=

boto3
.
client
(
"s3"
,

endpoint_url
=
"http://localhost:4566"
,

region_name
=
"us-east-1"
,

aws_access_key_id
=
"test"
,

aws_secret_access_key
=
"test"
)

// Node.js (AWS SDK v3)

import

{

S3Client

}

from

"@aws-sdk/client-s3"
;

const

client

=

new

S3Client
(
{


endpoint
:
"http://localhost:4566"
,


region
:
"us-east-1"
,


credentials
:
{

accessKeyId
:
"test"
,

secretAccessKey
:
"test"

}
,


forcePathStyle
:
true
,

}
)
;

## Image Tags

Tag

Description

latest

Native image — sub-second startup
(recommended)

latest-jvm

JVM image — broadest platform compatibility

x.y.z
 /
x.y.z-jvm

Pinned releases

## Configuration

All settings are overridable via environment variables (FLOCI_prefix).

Variable

Default

Description

QUARKUS_HTTP_PORT

4566

HTTP port

FLOCI_DEFAULT_REGION

us-east-1

Default AWS region

FLOCI_DEFAULT_ACCOUNT_ID

000000000000

Default AWS account ID

FLOCI_STORAGE_MODE

hybrid

memory
 ·
persistent
 ·
hybrid
 ·
wal

FLOCI_STORAGE_PERSISTENT_PATH

./data

Data directory

→ Full reference:configuration docs→ Per-service storage overrides:storage docs

## License

MIT — use it however you want.

## About

Light, fluffy, and always free - AWS Local Emulator

hectorvent.dev/floci/

### Topics

 aws

 localstack

 aws-emulation

### Resources

 Readme



### License

 MIT license


### Code of conduct

 Code of conduct


### Contributing

 Contributing


### Uh oh!

There was an error while loading.Please reload this page.





Activity


### Stars

566

 stars


### Watchers

2

 watching


### Forks

16

 forks


 Report repository



## Releases9

1.0.4

 Latest



Mar 20, 2026



+ 8 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





## Contributors3

* hectorventHector Ventura
* semantic-release-botSemantic Release Bot
* juandiiiJuan Diego López

## Languages

* Java100.0%
