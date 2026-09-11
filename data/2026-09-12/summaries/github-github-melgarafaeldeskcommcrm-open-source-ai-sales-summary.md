---
title: GitHub - melgarafael/DeskcommCRM: Open-source AI sales OS — self-hosted CRM with native AI agents + WhatsApp (WAHA). Open alternative to Kommo, Octade...
url: https://github.com/melgarafael/DeskcommCRM
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-09-12T01:22:33.568426
---

# GitHub - melgarafael/DeskcommCRM: Open-source AI sales OS — self-hosted CRM with native AI agents + WhatsApp (WAHA). Open alternative to Kommo, Octade...

# DeskcommCRM – Sistema Operacional de Vendas com IA (open source)

## Visão geral
- CRM open source que roda no seu servidor e integra IA e WhatsApp para atender, qualificar e vender.
- Sem mensalidade, sem recursos bloqueados; os dados permanecem sob seu controle.
- Alternativa aberta a Kommo, Octadesk e Intercom.
- Disponível em Português, Inglês e Espanhol.

## Instalação em produção com 1 comando
- Parceria com HostGator: o kit `hostgator-setup-kit` instala app, WhatsApp e banco em uma VPS com um único `curl … | bash`.
- O script indica o plano de VPS ideal e devolve o comando correto para o seu caso.
- Também pode ser executado localmente (macOS, Linux ou WSL) para testes.

## Instalação tradicional na VPS (caminho principal)
1. Conecte‑se à VPS via SSH (`ssh -p PORTA root@SEU_IP`).
2. Clone o repositório e execute o instalador:  
   ```bash
   git clone https://github.com/melgarafael/DeskcommCRM.git
   cd DeskcommCRM
   bash hostgator-setup-kit/install.sh
   ```
3. O instalador cuida de Docker, imagens prontas e cria tudo automaticamente.

## Requisitos
- VPS com Docker (recomendado 4 GB de RAM). HostGator é a opção padrão, mas qualquer VPS serve.
- Domínio apontando (registro A) para o IP da VPS.
- Conta gratuita no Supabase (para o banco) – o instalador pode criar o projeto e obter as credenciais.
- Chave de API de IA (OpenRouter, Anthropic ou OpenAI) – o instalador pergunta qual usar.
- Número de WhatsApp conectado via QR code no onboarding (ou canal oficial da Meta).

## O que o instalador faz
- Solicita apenas informações essenciais (domínio, chaves, senha do admin) e valida imediatamente.
- Gera segredos técnicos automaticamente.
- Cria extensões do PostgreSQL e aplica o schema completo.
- Cria o primeiro usuário admin com e‑mail e senha definidos por você.
- Levanta a stack completa com HTTPS automático e verifica a saúde ao final.
- Instala cron das automações (regras QUANDO/SE/ENTÃO) e o agente de atualização que habilita o botão “Atualizar agora”.
- É idempotente: reexecutar não duplica cron nem recria usuários, retomando de onde parou.
- Modo não‑interativo disponível via cópia de `.env.hostgator.example` para `.env` e execução com `--yes`.

## Outras hospedagens (Hostinger, Coolify, Dokploy, CapRover etc.)
- Funciona em VPS com proxy reverso próprio (porta 80/443). O instalador detecta o proxy e publica o CRM através dele, evitando conflitos com o Caddy.
- Em ambientes que usam `--network host`, o instalador pede confirmação para evitar publicação incorreta.

## Primeiro acesso
- Acesse `https://<seu‑domínio>` (o cadeado HTTPS pode levar ~1 minuto para aparecer).
- Entre com o admin criado; a verificação em duas etapas (Google Authenticator ou Authy) é opcional e pode ser ativada em **Configurações › Segurança**.
- No onboarding, escaneie o QR code para conectar o número de WhatsApp.