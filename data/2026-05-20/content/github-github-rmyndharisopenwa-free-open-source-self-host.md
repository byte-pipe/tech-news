---
title: 'GitHub - rmyndharis/OpenWA: Free, Open Source, Self-Hosted WhatsApp API Gateway · GitHub'
url: https://github.com/rmyndharis/OpenWA
site_name: github
content_file: github-github-rmyndharisopenwa-free-open-source-self-host
fetched_at: '2026-05-20T12:02:50.507641'
original_url: https://github.com/rmyndharis/OpenWA
author: rmyndharis
description: Free, Open Source, Self-Hosted WhatsApp API Gateway - rmyndharis/OpenWA
---

rmyndharis

 

/

OpenWA

Public

* NotificationsYou must be signed in to change notification settings
* Fork899
* Star4.4k

 
 
 
 
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

104 Commits
104 Commits
.github
.github
 
 
dashboard
dashboard
 
 
docs
docs
 
 
scripts
scripts
 
 
sdk
sdk
 
 
src
src
 
 
test
test
 
 
traefik
traefik
 
 
.dockerignore
.dockerignore
 
 
.env.example
.env.example
 
 
.env.minimal
.env.minimal
 
 
.gitignore
.gitignore
 
 
.prettierrc
.prettierrc
 
 
CHANGELOG.md
CHANGELOG.md
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
docker-compose.dev.yml
docker-compose.dev.yml
 
 
docker-compose.yml
docker-compose.yml
 
 
eslint.config.mjs
eslint.config.mjs
 
 
nest-cli.json
nest-cli.json
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
tsconfig.build.json
tsconfig.build.json
 
 
tsconfig.json
tsconfig.json
 
 
View all files

## Repository files navigation

# OpenWA

Open Source WhatsApp API Gateway

Features•Quick Start•Docs•API•Contributing

## ✨ Why OpenWA?

OpenWAis a free, open-source WhatsApp API Gateway designed for developers who need full control over their messaging infrastructure—without vendor lock-in or hidden paywalls.

Built on apluggable architecture, OpenWA lets you swap database engines (SQLite/PostgreSQL), storage backends (Local/S3), and cache layers (Memory/Redis) without changing a single line of application code.

🔓 
100% Open Source

No licensing fees, no feature locks, full source code access

🏗️ 
Pluggable Architecture

Swap adapters for database, storage, and cache via config

🖥️ 
Full Dashboard

Modern React UI for session, webhook, and API key management

🔹 
Multi-Session Ready

Run multiple WhatsApp sessions concurrently on one instance

🐳 
Docker Native

Production-ready with zero configuration

🔗 
n8n Integration

Community nodes for workflow automation

## 🎯 Features

### Core Features

Feature

Status

Description

REST API

✅

Full WhatsApp API via HTTP endpoints

Multi-Session

✅

Manage multiple WhatsApp accounts

Webhooks

✅

Real-time events with HMAC signature

Web Dashboard

✅

Visual management interface

API Key Auth

✅

Secure API authentication

Swagger Docs

✅

Interactive API documentation

### Messaging

Feature

Status

Description

Text Messages

✅

Send/receive text messages

Media Messages

✅

Images, videos, documents, audio

Message Reactions

✅

React to messages with emoji

Bulk Messaging

✅

Send to multiple recipients

Message Status

✅

Track delivery and read receipts

### Advanced

Feature

Status

Description

Groups API

✅

Create, manage, and message groups

Channels/Newsletter

✅

WhatsApp Channels support

Labels Management

✅

Organize chats with labels

Proxy Support

✅

Per-session proxy configuration

Rate Limiting

✅

Configurable request limits

CIDR Whitelisting

✅

IP-based access control

Audit Logging

✅

Track all API operations

### Infrastructure

Feature

Status

Description

SQLite

✅

Zero-config embedded database

PostgreSQL

✅

Production-grade database

Redis Cache

✅

Optional performance caching

S3/MinIO Storage

✅

Scalable media storage

Docker

✅

One-command deployment

Health Checks

✅

Kubernetes-ready probes

Data Migration

✅

Export/import between backends

## 🚀 Quick Start

### Option A: Docker (Recommended)

#
 Clone and start

git clone https://github.com/rmyndharis/OpenWA.git

cd
 OpenWA
docker compose -f docker-compose.dev.yml up -d

#
 Access

#
 Dashboard: http://localhost:2886

#
 API: http://localhost:2785/api

#
 Swagger: http://localhost:2785/api/docs

### Option B: Local Development

#
 Clone repository

git clone https://github.com/rmyndharis/OpenWA.git

cd
 OpenWA

#
 Install dependencies (includes dashboard)

npm install

#
 Start API + Dashboard (config is auto-generated on first run)

npm run dev

#
 Access

#
 Dashboard: http://localhost:2886

#
 API: http://localhost:2785/api

#
 Swagger: http://localhost:2785/api/docs

## 🏭 Production Deployment

For production, use the maindocker-compose.ymlwith optional services:

#
 Basic production (SQLite, local storage)

docker compose up -d

#
 With PostgreSQL database

docker compose --profile postgres up -d

#
 Full stack (PostgreSQL, Redis, Dashboard, Traefik)

docker compose --profile full up -d

Profile

Services

postgres

PostgreSQL database

redis

Redis cache

minio

S3-compatible storage

with-dashboard

Web dashboard

with-proxy

Traefik reverse proxy

full

All services above

Development vs Production

* Development (docker-compose.dev.yml): SQLite, local storage, both API & Dashboard included
* Production (docker-compose.yml): Configurable database, profiles for optional services

## 🔌 Ports

Service

Port

Description

API

2785

REST API endpoints

Dashboard

2886

Web management interface

Swagger

2785/api/docs

Interactive API docs

## 📡 API Examples

### Create a Session

curl -X POST http://localhost:2785/api/sessions \
 -H 
"
Content-Type: application/json
"
 \
 -H 
"
X-API-Key: YOUR_API_KEY
"
 \
 -d 
'
{"name": "my-bot"}
'

### Start Session & Get QR Code

#
 Start the session

curl -X POST http://localhost:2785/api/sessions/{sessionId}/start \
 -H 
"
X-API-Key: YOUR_API_KEY
"

#
 Get QR code (scan with WhatsApp)

curl http://localhost:2785/api/sessions/{sessionId}/qr \
 -H 
"
X-API-Key: YOUR_API_KEY
"

### Send a Message

curl -X POST http://localhost:2785/api/sessions/{sessionId}/messages/send-text \
 -H 
"
Content-Type: application/json
"
 \
 -H 
"
X-API-Key: YOUR_API_KEY
"
 \
 -d 
'
{

 "chatId": "628123456789@c.us",

 "text": "Hello from OpenWA!"

 }
'

### Setup Webhook

curl -X POST http://localhost:2785/api/sessions/{sessionId}/webhooks \
 -H 
"
Content-Type: application/json
"
 \
 -H 
"
X-API-Key: YOUR_API_KEY
"
 \
 -d 
'
{

 "url": "https://your-server.com/webhook",

 "events": ["message.received", "session.status"],

 "secret": "your-hmac-secret"

 }
'

## 🛠 Tech Stack

Layer

Technology

Runtime

Node.js 22 LTS

Framework

NestJS 11.x

Language

TypeScript 5.x

WA Engine

whatsapp-web.js

Database

SQLite / PostgreSQL

Cache

Redis (optional)

Storage

Local / S3 / MinIO

ORM

TypeORM

Container

Docker + Docker Compose

## 📁 Project Structure

openwa/
├── src/
│ ├── main.ts # Application entry point
│ ├── app.module.ts # Root module
│ ├── config/ # Configuration
│ ├── common/ # Shared utilities
│ │ ├── cache/ # Redis caching
│ │ └── storage/ # File storage (Local/S3)
│ ├── core/ # Core systems
│ │ ├── hooks/ # Plugin hooks
│ │ └── plugins/ # Plugin system
│ ├── engine/ # WhatsApp engine abstraction
│ └── modules/
│ ├── session/ # Session management
│ ├── message/ # Message handling
│ ├── webhook/ # Webhook management
│ ├── group/ # Groups API
│ ├── contact/ # Contacts API
│ ├── auth/ # API key authentication
│ ├── infra/ # Infrastructure management
│ └── health/ # Health checks
├── dashboard/ # React web dashboard
├── docs/ # Documentation
├── docker-compose.yml
├── Dockerfile
└── package.json

## 📚 Documentation

Comprehensive documentation is available in thedocs/folder:

Document

Description

Project Overview

Introduction and goals

Requirements

Feature specifications

Architecture

System design

Security

Security implementation

Database

Data models and migrations

API Spec

Complete API reference

Development

Coding standards

Migration Guide

Database & storage migration

## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. Forkthe repository
2. Createyour feature branch (git checkout -b feature/amazing-feature)
3. Commityour changes (git commit -m 'Add amazing feature')
4. Pushto the branch (git push origin feature/amazing-feature)
5. Opena Pull Request

Please read ourDevelopment Guidelinesfor coding standards and best practices.

## 📄 License

This project is licensed under theMIT License– free for personal and commercial use.

SeeLICENSEfor details.

OpenWA– Free, Open Source WhatsApp API Gateway

📖 Documentation·🔌 API Docs·🐛 Report Bug·💡 Request Feature

Made with ❤️ byYudhi Armyndharisand the OpenWA Community

## About

Free, Open Source, Self-Hosted WhatsApp API Gateway

www.open-wa.org

### Topics

 api

 gateway

 whatsapp

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

4.4k

 stars
 

### Watchers

21

 watching
 

### Forks

899

 forks
 

 Report repository

 

## Releases5

v0.1.6

 Latest

 

May 17, 2026

 

+ 4 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript86.4%
* CSS11.8%
* Shell0.8%
* Python0.5%
* Dockerfile0.3%
* JavaScript0.2%