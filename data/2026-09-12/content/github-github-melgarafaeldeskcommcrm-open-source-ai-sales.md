---
title: 'GitHub - melgarafael/DeskcommCRM: Open-source AI sales OS — self-hosted CRM with native AI agents + WhatsApp (WAHA). Open alternative to Kommo, Octadesk & Intercom for any business that sells by chat. MCP-ready, multi-tenant, LGPD. · GitHub'
url: https://github.com/melgarafael/DeskcommCRM
site_name: github
content_file: github-github-melgarafaeldeskcommcrm-open-source-ai-sales
fetched_at: '2026-09-12T01:21:56.904228'
original_url: https://github.com/melgarafael/DeskcommCRM
author: melgarafael
description: Open-source AI sales OS — self-hosted CRM with native AI agents + WhatsApp (WAHA). Open alternative to Kommo, Octadesk & Intercom for any business that sells by chat. MCP-ready, multi-tenant, LGPD. - melgarafael/DeskcommCRM
---

melgarafael

 

/

DeskcommCRM

Public

* NotificationsYou must be signed in to change notification settings
* Fork470
* Star1.2k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

3,954 Commits
3,954 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.agents
.agents
 
 
.changes
.changes
 
 
.claude
.claude
 
 
.codex
.codex
 
 
.cursor/
rules
.cursor/
rules
 
 
.github
.github
 
 
.specs
.specs
 
 
app
app
 
 
components
components
 
 
docker/
scheduler
docker/
scheduler
 
 
docs
docs
 
 
evidence
evidence
 
 
hooks
hooks
 
 
hostgator-setup-kit
hostgator-setup-kit
 
 
lib
lib
 
 
loop
loop
 
 
patches
patches
 
 
plan
plan
 
 
public
public
 
 
scripts
scripts
 
 
supabase
supabase
 
 
tasks
tasks
 
 
tests
tests
 
 
triagem
triagem
 
 
types
types
 
 
workers
workers
 
 
.dockerignore
.dockerignore
 
 
.env.example
.env.example
 
 
.env.hostgator.example
.env.hostgator.example
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.mailmap
.mailmap
 
 
.nvmrc
.nvmrc
 
 
.prettierrc
.prettierrc
 
 
AGENTS.md
AGENTS.md
 
 
ARCHITECTURE.md
ARCHITECTURE.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Caddyfile
Caddyfile
 
 
Dockerfile
Dockerfile
 
 
Dockerfile.scheduler
Dockerfile.scheduler
 
 
Dockerfile.worker
Dockerfile.worker
 
 
HANDOFF-conversa-vira-lead.md
HANDOFF-conversa-vira-lead.md
 
 
HANDOFF-followup-vivo.md
HANDOFF-followup-vivo.md
 
 
HANDOFF-fv-w1-fila.md
HANDOFF-fv-w1-fila.md
 
 
HANDOFF-handoff-avisa-o-lead.md
HANDOFF-handoff-avisa-o-lead.md
 
 
HANDOFF-harness-evolution.md
HANDOFF-harness-evolution.md
 
 
HANDOFF-ia-360.md
HANDOFF-ia-360.md
 
 
HANDOFF-marca-propria.md
HANDOFF-marca-propria.md
 
 
HANDOFF-operacao-visivel.md
HANDOFF-operacao-visivel.md
 
 
HANDOFF-silencio-retomada-humana-nao-gruda.md
HANDOFF-silencio-retomada-humana-nao-gruda.md
 
 
HANDOFF-sistema-vivo-consertos.md
HANDOFF-sistema-vivo-consertos.md
 
 
HANDOFF-tres-papeis.md
HANDOFF-tres-papeis.md
 
 
HANDOFF.md
HANDOFF.md
 
 
LICENSE
LICENSE
 
 
README.en.md
README.en.md
 
 
README.es.md
README.es.md
 
 
README.md
README.md
 
 
RELATORIO-W1-GATILHOS.md
RELATORIO-W1-GATILHOS.md
 
 
SECURITY.md
SECURITY.md
 
 
VISION.md
VISION.md
 
 
components.json
components.json
 
 
docker-compose.build.yml
docker-compose.build.yml
 
 
docker-compose.prod.yml
docker-compose.prod.yml
 
 
docker-compose.traefik.yml
docker-compose.traefik.yml
 
 
docker-compose.yml
docker-compose.yml
 
 
eslint.config.mjs
eslint.config.mjs
 
 
instrumentation-client.ts
instrumentation-client.ts
 
 
instrumentation.ts
instrumentation.ts
 
 
next.config.ts
next.config.ts
 
 
package.json
package.json
 
 
playwright.config.ts
playwright.config.ts
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
postcss.config.mjs
postcss.config.mjs
 
 
proxy.ts
proxy.ts
 
 
sentry.edge.config.ts
sentry.edge.config.ts
 
 
sentry.server.config.ts
sentry.server.config.ts
 
 
tsconfig.json
tsconfig.json
 
 
tsconfig.typecheck.json
tsconfig.typecheck.json
 
 
vercel.ts
vercel.ts
 
 
vitest.config.ts
vitest.config.ts
 
 
vitest.db.config.ts
vitest.db.config.ts
 
 
View all files

## Repository files navigation

🇧🇷 Português ·🇺🇸 English·🇪🇸 Español

# 🛠️ DeskcommCRM — o Sistema Operacional de Vendas com IA, open source, pro WhatsApp

Agentes de IA que atendem, qualificam e vendem no WhatsApp — dentro de um CRM open source rodando no seu servidor.Sem mensalidade, sem feature travada, seus dados com você. A alternativa aberta a Kommo, Octadesk e Intercom.

⚡ Instalar·🔄 Atualizar·🧭 Visão·🏗️ Arquitetura·🤝 Contribuir·🗺️ Roadmap

### ☁️ Rode este CRM em produção com 1 comando

O DeskcommCRM foi desenvolvido emparceria com a HostGator: ohostgator-setup-kit/instala o CRM completo (app + WhatsApp + banco) numa VPS com um único comando, e orunbook de produçãojá assume esse ambiente.

👉 Assinar a VPS HostGator com desconto da parceria—
datacenter em São Paulo, ideal pro WhatsApp rodando 24/7.(link de parceiro — assinar por ele apoia o projeto e sai mais barato)

Ainda não tem servidor?Rode istono seu computador(macOS, Linux ou WSL). Ele diz
qual plano contratar — com os números do runbook, não um "depende" — e te devolve o
comando certo pro seu caso:

curl -fsSL https://raw.githubusercontent.com/melgarafael/DeskcommCRM/main/hostgator-setup-kit/comecar.sh 
|
 bash

(prefere ler antes de executar? clone o repo e rodebash hostgator-setup-kit/comecar.sh—
ele não instala nada sem você confirmar.)

## ⚡ Instalar na sua VPS (o caminho principal)

### 1. Entre na sua VPS

Abra oTerminalno seu computador (no Windows, oPowerShell; no Mac ou Linux, oTerminal) e conecte com o IP e a porta que a hospedagem te mandou por e-mail:

ssh -p PORTA root@SEU_IP

TroquePORTAeSEU_IPpelos seus. Se a hospedagem não mencionou porta nenhuma, é a padrão
(22) e você pode omitir:ssh root@SEU_IP.

Ele pede a senha.Ao digitar, não aparece nada na tela — nem asteriscos.Isso não é
travamento: é o terminal escondendo a senha. Digite (ou cole) e dê Enter.

Na primeira conexão ele perguntaAre you sure you want to continue connecting?— respondayes. É o servidor se apresentando pela primeira vez.

### 2. Rode o instalador

Já dentro da VPS:

git clone https://github.com/melgarafael/DeskcommCRM.git

cd
 DeskcommCRM
bash hostgator-setup-kit/install.sh

É isso.Você não instala Node, nem pnpm, nem compila nada— a imagem do app já vem pronta.
Se faltar Docker, o instalador pergunta e instala sozinho.

### O que você precisa ter em mãos

Item

Onde conseguir

VPS com Docker

HostGator
 (parceria) — ou qualquer VPS com Docker. 4 GB de RAM recomendados

Domínio

Um registro 
A
 apontando pro IP da VPS (ex.: 
crm.suaempresa.com.br
)

Banco

Conta grátis no 
supabase.com
 — 3 chaves + connection string do 
Session pooler

IA

Uma chave de 
OpenRouter
, 
Anthropic
 ou 
OpenAI
 — o instalador pergunta qual você quer

WhatsApp

Seu número, conectado por QR code no onboarding (ou o canal oficial da Meta)

💡O Supabase pode ser criado pelo próprio instalador.Exporte umSUPABASE_ACCESS_TOKENantes de rodar e ele cria o projeto, espera o banco ficar saudável,
busca as 4 credenciais e descobre o host do pooler testando conexão real — sem copiar e colar.

### O que o instalador faz por você

Elepergunta só o que é seu(domínio, chaves, senha do admin),valida cada resposta antes
de seguir— chave errada ele recusa na hora, não três passos depois — e cuida do resto:

1. Gera todos os segredos técnicos sozinho (você não inventa senha nenhuma).
2. Cria as extensões do Postgres e aplica o schema completo (supabase/baseline.sql).
3. Cria o primeiro admin com o e-mail e a senha que você escolheu.
4. Sobe a stack inteira comHTTPS automáticoe confere a saúde no fim.
5. Instala ocron das automações(sem ele, as regras QUANDO/SE/ENTÃO ficam paradas na fila)
e oagente de atualização, que é o que faz o botão "Atualizar agora" existir na tela.

Rodar de novo não quebra nada— oinstall.shé idempotente: não duplica cron, não recria
usuário, retoma de onde parou.

Modo não-interativo:copie.env.hostgator.examplepara.env, preencha e rodebash hostgator-setup-kit/install.sh --yes.

### Outra hospedagem? (Hostinger, Coolify, Dokploy, CapRover…)

Funciona. Se a sua VPS já vem com umproxy reverso próprioocupando as portas 80/443, o
instaladordetecta isso sozinhoe publica o CRM através dele, em vez de tentar subir um
Caddy que não caberia. Num caso específico — proxy em--network host, como faz a Hostinger —
elepergunta em vez de adivinhar, porque publicar atrás do proxy errado instala "com
sucesso" um site mudo. Detalhes emhostgator-setup-kit/README.md.

### Primeiro acesso

Abrahttps://<seu-domínio>(o cadeado leva ~1 min pra aparecer), entre com o admin, e tenha oGoogle AuthenticatorouAuthyà mãosevocê quiser ligar a verificação em duas etapas — ela éopcionale fica em Configurações › Segurança; o primeiro loginnãoa exige. No onboarding,
escaneie o QR code com o WhatsApp do seu número.

### 🤖 Prefere que uma IA instale pra você?

Jogue a pastahostgator-setup-kit/no chat doClaude Coderodando dentro da VPS e diga"instala o DeskcommCRM pra mim". Ele lê oCLAUDE.mddo kit
— que traz o passo a passo e as armadilhas já mapeadas — e conduz tudo em português.

## 🔄 Atualizar

Saiu versão nova? Há dois caminhos, e o primeironão exige terminal.

Com o repositório clonado, oguia de instalaçãojá vem dentro —.agents/skills/deskcomm-instalar/—
e carrega sozinho no Claude Code, Codex, Cursor, OpenCode ou Antigravity aberto na pasta. Diga só"quero instalar o CRM na minha VPS". Há guias também para montar um cliente por nicho, analisar
métricas, afinar o prompt do agente e contribuir (AGENTS.md, seção "Guias do assistente").

### Pela tela (recomendado)

Quando existe versão nova, o rodapé do menu lateral acende"Nova versão"— só pro dono do
servidor, porque avisar quem não pode atualizar é ruído. Clique e você cai emConfigurações → Atualização, que mostra o que muda, fazbackup do banco sozinhae
acompanha cada fase (backup → código → banco → no ar) até terminar. Nada de SSH.

Se a versão nova subir quebrada, o agentevolta pra imagem anterior sozinhoe grava essa
volta no.env— sem isso, o próximo restart traria o app quebrado de novo, em silêncio.

Por baixo: o app só registra o pedido; quem executa é o agente que oinstall.shdeixou na
sua VPS, num cron que conferea cada 5 minutos— então a atualização começa em até 5
minutos depois do clique. Se esse agente estiver fora do ar, a tela avisa"Atualização automática indisponível"e mostra o comando abaixo — ela não finge que deu certo.

### Pelo terminal

cd
 /caminho/do/DeskcommCRM
bash hostgator-setup-kit/update.sh

O comando faz, nesta ordem: (1) confere se há mesmo versão nova — se não houver, sai na hora;
(2)faz backup do banco antes de tocar em qualquer coisa; (3) baixa o código novo;
(4) atualiza o banco re-aplicando obaseline.sql, que é idempotente eauto-curativo(conserta sozinho dados bagunçados por versões antigas); (5) puxa a imagem nova do app;
(6) confere a saúde no fim.

O alvo é a última versão publicada(v1.2.3), não o topo damain— atualizar leva sempre
a uma versão marcada e descrita noCHANGELOG.md, nunca a um commit não testado.
Elerecusavoltar pra uma versão anterior à instalada (isso desligaria coisas que você já tem);
pra isso existe--force, de propósito.

Coisas normais que você vai ver:um monte dealready exists/multiple primary keysna
parte do banco —é esperado e inofensivo, são coisas que já existiam. O script filtra esse
ruído e mostra✓ banco atualizado. Se aparecer⚠ avisos que não são os esperados, aí sim
guarde a mensagem.

Deu ruim?bash hostgator-setup-kit/restore.shvolta pro backup.Quer só diagnosticar?bash hostgator-setup-kit/healthcheck.sh.

⚠️Numa instalação antiga que ainda não tem o agente da tela, rodeupdate.shduas
vezes: a primeira execução ainda é a do script velho (que baixa o novo); a segunda instala
o agente e liga o botão.

Passo a passo em linguagem simples:docs/ATUALIZANDO.md.

### Outros comandos do kit

Script

Função

install.sh

Instala tudo (idempotente — pode rodar de novo)

update.sh

Atualiza pra versão nova, com backup automático

backup.sh

Backup do banco + sessões de WhatsApp

restore.sh

Restaura um backup

reset-password.sh

Redefine a senha de um usuário

reset-mfa.sh

Remove o MFA de quem perdeu o celular

healthcheck.sh

Diagnóstico de todos os serviços de uma vez

Backup importa:o plano grátis do Supabasenão faz backup sozinho. Vale agendarbackup.shno cron diariamente. Oupdate.shjá roda um backup antes de cada atualização.

## ✨ O que é

Deskcommvem deDesk(mesa) +comm(comércio):o comercial de mesa— toda a operação de vendas do seu negócio numa mesa só, operada por pessoas e agentes de IA juntos.

O projeto nasceu como CRM de e-commerce e a comunidade o levou muito além: hoje roda emclínicas, imobiliárias, infoprodutos, agências, lojas e prestadores de serviço— qualquer negócio que vende pelo WhatsApp. O produto acompanhou essa virada e virou umsistema operacional de vendas: agentes de IA com RAG por tenant atendem, qualificam, movem leads no funil, disparam automações e sabem a hora de passar pra um humano — com o CRM inteiro exposto viaMCPpros agentes operarem de verdade. A história completa está emVISION.md.

### Diferenciais

* 🤖Agentes de IA que operam o CRM— RAG por tenant, skills que o agente executa sozinho durante o atendimento, memória da operação, análise de sentimento, handoff IA→humano auditado, IA como assignee de primeira classe e teto de gasto por organização. Não é chatbot decorativo: o agente atende, qualifica e move o funil.
* 🔁Nada morre no silêncio— follow-up que retoma a conversa esfriada (com tempo adaptativo e gatilhos por etapa do funil), radar do que está em risco de morrer sem resposta, e central de avisos pro que precisa de decisão humana.
* 🧠Agentes que se auto-aprimoram— conversas resolvidas viram conhecimento novo; a tela deEvolução da IAmostra se o agente está melhorando, onde erra e o que falta ensinar;Propostassão melhorias que a IA sugere pra si mesma, aplicáveis como versão nova — sempre com gate humano.
* 🧩Multi-nicho por design— vocabulário configurável por pipeline: lead viraCliente,PacienteouComprador; won viraPago,AgendadoouFechado. O mesmo core serve e-commerce (nosso berço, com integração Nuvemshop), clínica, imobiliária ou infoproduto.
* 💬WhatsApp de duas formas— porQR code(WAHA, multi-número, com anti-banimento: throttle + jitter + janela de horário) ou pelocanal oficial da Meta(Cloud API, com templates aprovados e sincronizados). Mídia via Storage, STOP detection.
* 🔀Escolha sua IA— OpenRouter, Anthropic ou OpenAI, decidido na instalação e trocável depois pela tela,por parte do sistema(o que conversa não precisa ser o que indexa).
* 👥Governança de atendimento— RBAC server-side de verdade, atribuição/transferência auditada, fila com rodízio, roteamento automático por intenção e escopo de visualização por papel.
* 🏢Multi-tenant + LGPD by-design— RLS em toda tabela tenant-aware com teste de isolamento como gate de CI; anonimização preferida sobre delete; audit append-only com retenção 5 anos.
* 🖥️Self-hosted de verdade— seus dados na sua VPS; instalação e atualização com 1 comando (ou 1 clique); sem versão paga, sem feature travada.

### 🔌 Webhooks & Automações

Todo tenant pode criarfontes de captação: um endereço público (/api/v1/webhooks/in/<token>) que recebe leads de landing pages, formulários próprios ou ferramentas como Zapier/n8n via POST (JSON ouapplication/x-www-form-urlencoded) e já entra direto no funil/estágio escolhido — sem código, sem integração customizada por tenant. Em cima dessas fontes (e dos outros eventos do CRM — lead mudou de etapa, ganhou tag, chegou mensagem no WhatsApp), o tenant montaautomações: regras no formato QUANDO/SE/ENTÃO que disparam ações como adicionar tag, mover o lead no funil, atribuir a um atendente, mandar uma mensagem de WhatsApp ou avisar outro sistema via webhook de saída.

Na UI, tudo mora emWebhooksna sidebar (visível só pra quem tem papelmanager/admin). A tela tem três abas:Receber dados(criar fonte, copiar o endereço/formulário pronto, disparar um lead de teste, ver os últimos recebimentos),Automações(montar a regra, que sempre nasce pausada até você revisar e ligar) eAtividade(timeline de cada execução, com o resultado de cada ação e reenvio manual quando uma chamada externa falha).

Por baixo, cada evento vira uma linha emevent_log— nenhum trigger de banco faz chamada HTTP diretamente. Quem drena essa fila é a rota/api/v1/cron/event-log-drain, chamada a cada minuto.Oinstall.sh/update.shjá configuram esse cron sozinhos— sem ele, as automações são criadas normalmente mas nunca rodam.

## 🖥️ O que você opera (as telas)

Grupo

Telas

Atendimento

Inbox
 (conversas de WhatsApp, você e a IA lado a lado) · 
Radar
 (quem esfriou e ainda está aberto) · 
Respostas rápidas

CRM

Kanban
 (onde cada negócio está no funil) · 
Contatos
 · 
Funis
 (etapas, vocabulário do negócio e motivos de perda)

Agente de IA

Agentes
 · 
Follow-ups
 · 
Roteadores
 · 
Provedores
 e 
Credenciais
 · 
Conhecimento
 (RAG) · 
Memória
 · 
Skills
 · 
Casos
 · 
Alertas
 · 
Propostas
 · 
Execuções
 · 
Uso e orçamento

Canais

Conexões
 (QR ou canal oficial da Meta, com saúde, reconexão e templates) · 
Nuvemshop
 · 
Webhooks

Análise

Desempenho
 (funil e performance por atendente) · 
Evolução da IA
 · 
Audit Log

Organização

Equipe
 · 
Distribuição de atendimento
 · 
Organização
 · 
LGPD
 · 
API Tokens
 · 
Segurança
 (MFA, códigos de recuperação, sessões) · Perfil, Notificações, Billing

Toda tela tem porta na navegação — o CI reprova tela que existe mas em que só se chega digitando a URL.

## 🧱 Stack

Camada

Escolha

Por quê

Frontend

Next.js 16 App Router (Turbopack) + React 19 + TypeScript 6 estrito

Server Components + Route Handlers no mesmo repo

Estilo

Tailwind + shadcn/ui (
new-york
, neutral)

Customizável sem lock-in

DB

Supabase (Postgres + RLS + 
vector
)

Multi-tenant nativo, embedding pra RAG

Auth

Supabase Auth via 
@supabase/ssr

Cookie SameSite=Strict, HttpOnly

Realtime

Supabase Realtime

postgres_changes + broadcast

Storage

Supabase Storage (URLs assinadas)

Bucket privado 
whatsapp-media

WhatsApp

WAHA Plus (engine NOWEB) + Meta Cloud API

QR pra começar rápido; canal oficial pra escala

Filas

event_log
 table + workers (cron)

Trigger de banco nunca faz HTTP

Rate limit

Upstash Redis (sliding window)

Serverless, free tier suficiente

AI

Vercel AI SDK v7 — OpenRouter, Anthropic, OpenAI e Google

Instalador pergunta qual; troca depois pela tela

Validação

Zod

Input externo, env, payloads

Observability

Sentry (scrub em erro, transação, span e breadcrumb)

Telemetria opt-in no install

Hospedagem

VPS com Docker (HostGator/SP na parceria)

App + WhatsApp + workers na sua máquina

Detalhes:ARCHITECTURE.md.

## 🧑‍💻 Desenvolvimento (só pra contribuir com o código)

⚠️Se você quer USAR o CRM, não é aqui— use oinstalador da VPS.
Esta seção é pra quem vai mexer no código.

git clone https://github.com/melgarafael/DeskcommCRM.git

cd
 DeskcommCRM

nvm use 
#
 Node 22

npm install -g pnpm 
&&
 pnpm install

cp .env.example .env.local 
#
 guia completo em docs/SETUP.md

docker compose up -d 
#
 WAHA local (opcional em dev sem WhatsApp)

#
 Schema: aplique o baseline, NÃO as migrations.

#
 As migrations 0001-0009 e 0013 são stubs `SELECT 1;` — a cadeia não sobe do zero.

#
 O schema real vive no baseline.sql, o mesmo que o install.sh aplica na VPS.

#
 `supabase db push` "passa" e deixa o banco vazio.

supabase link --project-ref 
<
seu-ref
>

#
 Num projeto Supabase NOVO, habilite antes as extensões que o schema usa —

#
 sem elas o baseline para em `type public.vector does not exist`.

psql 
"
$SUPABASE_DB_URL
"
 -v ON_ERROR_STOP=1 -c \
 
'
create extension if not exists vector with schema public;

 create extension if not exists citext with schema public;

 create extension if not exists pg_trgm with schema public;
'

psql 
"
$SUPABASE_DB_URL
"
 -v ON_ERROR_STOP=1 -f supabase/baseline.sql

pnpm dev

App:http://localhost:3000· Health check:http://localhost:3000/api/v1/health

docs/SETUP.mdé o tutorial completo detodas as integrações(Supabase, WAHA, provedores de IA, Upstash, Sentry, Resend, Nuvemshop) — ~60–90 min do zero ao app rodando.

## 📁 Estrutura

DeskcommCRM/
├── app/ # Next.js App Router
│ ├── (admin)/ # Rotas super-admin (impersonate, tenants)
│ ├── (public)/ # Login, recovery
│ ├── app/ # Rotas autenticadas: inbox, radar, kanban, contacts,
│ │ # connections, ai/*, integrations, metrics, lgpd,
│ │ # audit, team, settings
│ └── api/v1/ # API REST canônica (196 route handlers)
├── components/ # React (ui/, inbox/, kanban/, shell/, ...)
├── lib/ # supabase/, waha/, channels/, ai/, agent-engine/,
│ # api/, routing/, navigation/, env.ts
├── workers/ # consumers de event_log (IA, RAG, LGPD, mídia, rotinas)
├── supabase/migrations/ # SQL versionado (+ baseline.sql pro self-host)
├── tests/{e2e,unit,invariants,shell}/
├── scripts/ # seeds, qa-waves, manutenção
├── docs/ # PRDs, specs, runbooks, SETUP.md, ATUALIZANDO.md
└── hostgator-setup-kit/ # instalação e atualização self-host

## 🧪 Testes

pnpm typecheck 
#
 tsc --noEmit (estrito)

pnpm lint 
#
 eslint next/core-web-vitals

pnpm test:unit 
#
 Vitest (NÃO inclui tests/invariants/**)

pnpm test:db 
#
 Postgres efêmero + baseline install/update + invariantes

pnpm test:e2e 
#
 Playwright (requer dev server)

Estes checks são obrigatóriospra mergear namain. A lista abaixo já disse "quatro" e depois "cinco" —meça, não confie nela:

gh api repos/melgarafael/DeskcommCRM/branches/main/protection \
 --jq 
'
.required_status_checks.contexts|join(", ")
'

#
 em 2026-08-14: verify, build-and-size, invariants, e2e, imagens-ok

Check

O que faz

verify

typecheck + lint + 
lint:channels
 + 
test:unit
 + 
test:shell

invariants

sobe um Postgres limpo, aplica o 
baseline.sql
 em modo 
install
 e depois em modo 
update
 — as duas passadas com 
ON_ERROR_STOP=1
, que é o que torna a segunda uma prova de idempotência e não só um "terminou" —, e roda os invariantes de RBAC, atribuição, escopo, roteamento, follow-up, webhooks e automações

build-and-size

pnpm build
 em Node 22

e2e

sobe Supabase local, aplica o 
baseline.sql
 e roda 
48 das 49 specs
 Playwright pelo frontend

imagens-ok

reprova quando qualquer uma das três imagens Docker (
app
, 
worker
, 
scheduler
) não constrói — é o artefato que o self-hoster instala

A única spec fora doe2eévps-fresh-onboarding— ela precisa de WAHA + Redis + Resend + Nuvemshop de verdade. Ela é aP0da nossa doutrina de QA visual, entãoe2everdenãoprova a jornada de instalação fresca; essa se prova numa VPS.

Entre os invariantes está oteste de isolamento RLS: cria 2 organizações, simula os claims JWT pelo mesmo caminhoauth.uid()/fn_user_org_ids()que as policies de produção usam, e prova que um usuário da org A enxergazero linhasda org B emconversations,messages,contactsecrm_leads. Antes disso, um caso de controle prova que as linhas da org B realmente existem — sem ele, o teste passaria com a tabela vazia.

## 📚 Documentação

Doc

O que tem

hostgator-setup-kit/README.md

Instalação self-host
 — o kit, os scripts, as hospedagens com proxy próprio

docs/ATUALIZANDO.md

Como atualizar
 sua instalação, em linguagem simples

VISION.md

Visão e posicionamento
 — o que o projeto é, no que acredita e pra onde vai

CHANGELOG.md

O que mudou em cada versão — 
leia a seção da versão antes de atualizar

docs/SETUP.md

Setup de desenvolvimento, passo a passo de todas as integrações

docs/white-label.md

Instalar para clientes
 — trocar a marca, uma instalação por cliente vs compartilhada, revenda

docs/runbooks/waha-hostgator.md

Runbook de WAHA em produção (dimensionamento, recuperação)

docs/runbooks/deploy.md

Deploy em produção

CLAUDE.md

Convenções não-negociáveis (leitura obrigatória pra contribuir)

ARCHITECTURE.md

Visão de 1 página da arquitetura

docs/index.md

Índice dos 157 documentos, com regra de precedência

docs/prd/
 · 
docs/specs/

PRDs e specs técnicas (schema SQL, payloads, MCP, governança)

## 🤝 Contribuindo

Esse projeto é open source pra comunidade. Toda contribuição é bem-vinda — desde fix de typo em doc até feature nova.

Antes de abrir PR:

1. LeiaCLAUDE.md(~5 min) — convenções não-negociáveis (multi-tenancy, RLS, audit, LGPD).
2. LeiaCONTRIBUTING.md— fluxo de branches, commits, epic-executor.
3. Siga oCódigo de Conduta.

Fluxo curto:

git checkout -b feat/short-slug

#
 implementa + testes

pnpm typecheck 
&&
 pnpm lint 
&&
 pnpm lint:channels 
&&
 pnpm test:unit 
&&
 pnpm test:shell 
&&
 pnpm build
pnpm test:db 
#
 precisa de Docker — é o job `invariants`, obrigatório no merge

git commit -m 
"
feat(escopo): descrição
"

#
 abre PR — o template já traz o checklist de Definition of Done

Essas duas linhas sãotudo o que dá para rodar na sua máquina, de propósito: rodar só metade e
descobrir o resto como surpresa vermelha depois de horas de espera é a pior primeira experiência
que este repositório sabe entregar.

Dois gates obrigatóriosnãocabem aí e só rodam no CI: oe2e(precisa de Supabase local) e
oimagens-ok(constrói as três imagens Docker). Verde na sua máquina não é verde no merge.

Definition of Done:typecheck zero, lint zero, testes relevantes verdes, RLS testada se toca tabela tenant-aware, audit log emitido em mutações, migration versionada+ apêndice nobaseline.sqlse muda schema (senão a mudança não chega em quem se auto-hospeda). Detalhes emCLAUDE.md.

## 🐛 Reportando bugs

Abra umaissue— o template pede o que precisamos (ambiente,/api/v1/health, steps). Rodarbash hostgator-setup-kit/healthcheck.she colar a saída ajuda muito.

Pravulnerabilidades de segurança,NÃO abra issue pública— use orelato privado de vulnerabilidades. Detalhes emSECURITY.md.

## 🗺️ Roadmap

### ✅ Entregue

* Fundação & plataforma— auth (MFA pra admin), multi-tenancy com RLS + teste de isolamento, RBAC 4 papéis, audit log append-only, onboarding de tenant.
* Atendimento WhatsApp— inbox 3 painéis em tempo real, conexões multi-número porQR (WAHA)oucanal oficial da Meta(templates aprovados e sincronizados), mídia via Storage, anti-banimento (throttle + jitter + janela de horário), STOP detection.
* CRM & pedidos— kanban com vocabulário configurável por nicho (fractional indexing), gestão de funis pela tela, customer 360, contatos, tags, integração Nuvemshop.
* IA nativa— agentes com RAG por tenant (pgvector),skillsque o agente executa sozinho,memória da organização, roteador de intenção por número, análise de sentimento, handoff IA→humano, teto de gasto por org, MCP server interno.
* Escolha de provedor de IA— OpenRouter, Anthropic ou OpenAI, decidido na instalação e trocável por parte do sistema pela tela.
* Follow-up vivo— retomada de conversa esfriada com tempo adaptativo, gatilhos por etapa do funil e por caso, fila com rodízio, e o Radar do que corre risco de morrer sem resposta.
* LGPD— export e redact via workers, anonimização em cascata, consentimento auditado.
* Self-host—hostgator-setup-kit(app + WhatsApp + banco com 1 comando),baseline.sqlauto-curativo,atualização pela telacom backup automático, runbook de produção.
* Webhooks & automação— fontes de captação + regras QUANDO/SE/ENTÃO + gatilhos pra sistemas externos.
* Governança de atendimento— RBAC server-side em toda a API, atribuição e transferência auditadas (IA como assignee de 1ª classe), visualização por papel (RLS) + métricas por atendente, roteamento automático com fila e painel de gestão, e contrato de governança pra agentes de IA externos (docs/specs/14).
* Operação visível— motivo da retenção anti-ban traduzido na conversa, central de avisos com severidade, aviso de mensagem presa, controle de proteção de envio (janela/ritmo/teto), capacidades declaradas do agente e propostas do flywheel aplicáveis como versão nova (com gate humano).

### 🔮 Próximo

* MCP público— capabilities do CRM expostas pro ecossistema de agentes: plugue o agente que quiser e ele opera o Deskcomm.
* Templates por nicho— pipelines e vocabulários prontos pra clínica, imobiliária, infoproduto e serviços (e-commerce já entregue).
* Integrações— VTEX e Shopify via adapter pattern (Nuvemshop já entregue).
* Identity probabilística— unificação de contatos entre canais.

## 💬 Comunidade

* Discussões:GitHub Discussions— pra perguntas, ideias, showcase.
* Issues:GitHub Issues— bugs e tasks.
* Instagram:@melgarafael
* YouTube:youtube.com/@melgarafael

## 📜 Licença

Distribuído sob a licençaMIT— vejaLICENSE. Você pode usar, modificar
e distribuir livremente, inclusive comercialmente. O software é fornecido"como está",
sem garantias(ver cláusula de isenção noLICENSE).

## 🛟 Suporte & responsabilidades (self-host)

Este é um projetoself-host: cada pessoa roda o CRM naprópria infraestrutura(VPS, banco Supabase e chave de IA próprios). Isso implica:

* Suporte é comunitário e "as-is".Dúvidas e bugs entram comoIssuesouDiscussions. Não há SLA nem
suporte garantido — é open source mantido por boa vontade.
* Você é responsável pela sua instalação.Atualizações não são automáticas (você clica
ou rodaupdate.shquando quiser), e manter/backup do seu servidor é com você.
* LGPD — atenção:quemhospedaa instância é ocontroladordos dados pessoais
ali tratados (clientes, conversas, pedidos), com as obrigações legais decorrentes. Os
mantenedores do projetonão sãocontroladores nem operadores da sua instância, e não
têm acesso ao seu banco, ao seu WhatsApp nem ao seu storage. A única coisa que pode sair
da sua máquina para nós é o relatório de erro descrito abaixo — e só se você deixar.
* Telemetria (Sentry):oinstall.shperguntadurante a instalação e respeita a
sua resposta; em modo não-interativo, semSENTRY_DSNdefinido, a telemetria ficadesligada. Se você aceitar o Sentry da comunidade, o que é enviado sãorelatórios
de erro(stack trace) com CPF, telefone e e-mail substituídos, cabeçalhos sensíveis
removidos, e token de webhook/convite redigido da URL —semrastreamento de
performance esemreplay de sessão, que ficam em 0 nesse caminho. Para desligar a
qualquer momento:SENTRY_DSN=offno.env. Para mandar aoseuSentry (aí sim com
performance e replay):SENTRY_DSN=<seu-dsn>. O que é redigido, e por quê, está emlib/sentry/scrub.ts; a resolução do DSN emlib/sentry/dsn.ts.

## 🙏 Agradecimentos

* WAHA(devlikeapro) — engine WhatsApp.
* Supabase— Postgres + Auth + Storage + Realtime numa stack só.
* HostGator— parceria de infraestrutura que tornou o self-host de 1 comando possível.
* Anthropic,OpenAIeOpenRouter— os provedores de IA que o CRM sabe usar.
* shadcn/ui— base de componentes.
* A comunidade que nos levou do e-commerce pra clínicas, imobiliárias, infoprodutos e além — vocês definiram o que este projeto é.

Built with ☕ in Brasil·Made for the community

Siga o desenvolvimento:Instagram·YouTube