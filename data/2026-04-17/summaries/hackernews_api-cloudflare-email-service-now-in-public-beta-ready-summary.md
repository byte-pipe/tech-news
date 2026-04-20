---
title: Cloudflare Email Service: now in public beta. Ready for your agents
url: https://blog.cloudflare.com/email-for-agents/
date: 2026-04-16
site: hackernews_api
model: llama3.2:1b
summarized_at: 2026-04-17T11:53:32.765531
---

# Cloudflare Email Service: now in public beta. Ready for your agents

# Cloudflare Email Service: Now in Public Beta
=====================================

**Introduction**
---------------

Cloudflare Email Service is now available in public beta, revolutionizing the way agents interact with email-based applications. This innovative solution enables developers to send emails as native functionality, without having to manage API keys or external services.

**Key Features**
----------------

* **Email Routing**: Receive and route emails to your application or agent using our `WithEmailRouting` API.
* **Email Sending**: Send transactional emails directly from Workers with a native `Workers` binding (no API keys or secrets management).
* **Infrastructure for Developers**: Complete toolkit for building email-native agents, including:
 + Email Sending binding
 + Email MCP server
 + Wrangler CLI email commands
 + Skills for coding agents

### Email Sending in Public Beta

#### Fetch API Example

```javascript
export default {
  async fetch(request, env, ctx) {
    await env.EMAIL.send({
      to: "mailto:user@example.com",
      from: "admin@example.com",
      subject: "Your order has shipped",
      text: "Your order #1234 has shipped and is on its way."
    });
    return new Response("Email sent");
  },
};
```

#### Rest API Example

```shell
curl "https://api.cloudflare.com/client/v4/accounts/{account_id}/email-service/send" \
--header "Authorization: Bearer <API_TOKEN>" \
--header "Content-Type: application/json" \
--data '[{
  \"to\": \"mailto:user@example.com\",
  \"from\": \"admin@example.com\",
  \"subject\": \"Your order has shipped\",
  \"text\": \"Your order #1234 has shipped and is on its way.\"
 }]'
```

### Benefits of Using Cloudflare Email Service

* **Global Authentication**: Configure SPF, DKIM, and DMARC records automatically for your domain in response to Email Sending.
* **No API Keys or Secrets Management**: Developers can route emails directly as native functionality.

### Next Steps
-------------

Use our public beta to experience the power of Cloudflare Email Service today. Complete the toolkit and build email-native agents on top of this core interface.

# Technical Details

* API: HTTP/2 with WebSockets for real-time messaging.
* Authentication: Simple Authentication and Security Layer (SACL) for SPF, DKIM, and DMARC records configuration.
* Infrastructure: Fully managed service hosting infrastructure to ensure seamless integration.
