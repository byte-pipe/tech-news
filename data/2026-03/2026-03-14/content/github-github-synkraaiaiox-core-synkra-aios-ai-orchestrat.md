---
title: 'GitHub - SynkraAI/aiox-core: Synkra AIOS: AI-Orchestrated System for Full Stack Development - Core Framework v4.0 · GitHub'
url: https://github.com/SynkraAI/aiox-core
site_name: github
content_file: github-github-synkraaiaiox-core-synkra-aios-ai-orchestrat
fetched_at: '2026-03-14T11:08:59.321479'
original_url: https://github.com/SynkraAI/aiox-core
author: SynkraAI
description: 'Synkra AIOS: AI-Orchestrated System for Full Stack Development - Core Framework v4.0 - SynkraAI/aiox-core'
---

SynkraAI



/

aiox-core

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork753
* Star2.3k




 
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

836 Commits
836 Commits
.aiox-core
.aiox-core
 
 
.aiox
.aiox
 
 
.antigravity/
rules/
agents
.antigravity/
rules/
agents
 
 
.claude
.claude
 
 
.codex
.codex
 
 
.cursor/
rules/
agents
.cursor/
rules/
agents
 
 
.docker/
llm-routing
.docker/
llm-routing
 
 
.gemini
.gemini
 
 
.github
.github
 
 
.husky
.husky
 
 
.synapse
.synapse
 
 
bin
bin
 
 
docs
docs
 
 
packages
packages
 
 
pro @ 9639d70
pro @ 9639d70
 
 
scripts
scripts
 
 
squads
squads
 
 
tests
tests
 
 
.coderabbit.yaml
.coderabbit.yaml
 
 
.env.example
.env.example
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
.prettierrc
.prettierrc
 
 
.releaserc.json
.releaserc.json
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.en.md
README.en.md
 
 
README.md
README.md
 
 
eslint.config.js
eslint.config.js
 
 
jest.config.js
jest.config.js
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
tsconfig.json
tsconfig.json
 
 
View all files

## Repository files navigation

# AIOX Squad: Artificial Intelligence Orchestration eXperience

🌍English|Português

🌐 README por idioma:EN|PT|ES|ZH

Devolvendo às pessoas o poder de criar— Framework open source de orquestração de IA que devolve o controle a quem tem coragem de construir. Agentes especializados, workflows e experiência CLI First para qualquer domínio.

## Comece Aqui (10 Min)

Se é sua primeira vez no AIOX, siga este caminho linear:

1. Instale em um projeto novo ou existente:

#
 novo projeto

npx aiox-core init meu-projeto

#
 projeto existente

cd
 seu-projeto
npx aiox-core install

1. Escolha sua IDE/CLI e o caminho de ativação:

* Claude Code:/agent-name
* Gemini CLI:/aiox-menu→/aiox-<agent>
* Codex CLI:/skills→aiox-<agent-id>
* Cursor/Copilot/AntiGravity: siga os limites e workarounds emdocs/ide-integration.md

1. Ative 1 agente e confirme o greeting.
2. Rode 1 comando inicial (*helpou equivalente) para validar first-value.

Definição de first-value (binária): ativação de agente + greeting válido + comando inicial com output útil em <= 10 minutos.

## Compatibilidade de Hooks por IDE (Realidade AIOX 4.2)

Muitos recursos avançados do AIOX dependem de eventos de ciclo de vida (hooks). A tabela abaixo mostra a paridade real entre IDEs/plataformas:

IDE/CLI

Paridade de Hooks vs Claude

Impacto Prático

Claude Code

Completa (referência)

Automação máxima de contexto, guardrails e auditoria

Gemini CLI

Alta (eventos nativos)

Cobertura forte de automações pre/post tool e sessão

Codex CLI

Parcial/limitada

Parte das automações depende de
AGENTS.md
,
/skills
, MCP e fluxo operacional

Cursor

Sem lifecycle hooks equivalentes

Menor automação de pre/post tool; foco em regras, MCP e fluxo do agente

GitHub Copilot

Sem lifecycle hooks equivalentes

Menor automação de sessão/tooling; foco em instruções de repositório + MCP no VS Code

AntiGravity

Workflow-based (não hook-based)

Integração por workflows, não por eventos de hook equivalentes ao Claude

Impactos e mitigação detalhados:docs/ide-integration.md.

## Visão Geral

### Premissa Arquitetural: CLI First

O AIOX segue uma hierarquia clara de prioridades:

CLI First → Observability Second → UI Third

Camada

Prioridade

Foco

Exemplos

CLI

Máxima

Onde a inteligência vive. Toda execução, decisões e automação acontecem aqui.

Agentes (
@dev
,
@qa
), workflows, comandos

Observability

Secundária

Observar e monitorar o que acontece no CLI em tempo real.

Dashboard SSE, logs, métricas, timeline

UI

Terciária

Gestão pontual e visualizações quando necessário.

Kanban, settings, story management

Princípios derivados:

* A CLI é a fonte da verdade - dashboards apenas observam
* Funcionalidades novas devem funcionar 100% via CLI antes de ter UI
* A UI nunca deve ser requisito para operação do sistema
* Observabilidade serve para entender o que o CLI está fazendo, não para controlá-lo

As Duas Inovações Chave do AIOX:

1. Planejamento Agêntico:Agentes dedicados (analyst, pm, architect) colaboram com você para criar documentos de PRD e Arquitetura detalhados e consistentes. Através de engenharia avançada de prompts e refinamento com human-in-the-loop, estes agentes de planejamento produzem especificações abrangentes que vão muito além da geração genérica de tarefas de IA.

2. Desenvolvimento Contextualizado por Engenharia:O agente sm (Scrum Master) então transforma estes planos detalhados em histórias de desenvolvimento hiperdetalhadas que contêm tudo que o agente dev precisa - contexto completo, detalhes de implementação e orientação arquitetural incorporada diretamente nos arquivos de histórias.

Esta abordagem de duas fases elimina tanto ainconsistência de planejamentoquanto aperda de contexto- os maiores problemas no desenvolvimento assistido por IA. Seu agente dev abre um arquivo de história com compreensão completa do que construir, como construir e por quê.

📖Veja o fluxo de trabalho completo no Guia do Usuário- Fase de planejamento, ciclo de desenvolvimento e todos os papéis dos agentes

## Pré-requisitos

* Node.js >=18.0.0 (v20+ recomendado)
* npm >=9.0.0
* GitHub CLI (opcional, necessário para colaboração em equipe)

Problemas de instalação?Consulte oGuia de Troubleshooting

Guias específicos por plataforma:

* 📖Guia de Instalação para macOS
* 📖Guia de Instalação para Windows
* 📖Guia de Instalação para Linux

Documentação multilíngue disponível:English|Português|Español|中文

## Navegação Rápida

### Entendendo o Fluxo de Trabalho AIOX

Antes de mergulhar, revise estes diagramas críticos de fluxo de trabalho que explicam como o AIOX funciona:

1. Fluxo de Planejamento (Interface Web)- Como criar documentos de PRD e Arquitetura
2. Ciclo Principal de Desenvolvimento (IDE)- Como os agentes sm, dev e qa colaboram através de arquivos de histórias

⚠️Estes diagramas explicam 90% da confusão sobre o fluxo AIOX Agentic Agile- Entender a criação de PRD+Arquitetura e o fluxo de trabalho sm/dev/qa e como os agentes passam notas através de arquivos de histórias é essencial - e também explica por que isto NÃO é taskmaster ou apenas um simples executor de tarefas!

### O que você gostaria de fazer?

* Instalar e Construir software com Equipe Ágil Full Stack de IA→ Instruções de Início Rápido
* Aprender como usar o AIOX→ Guia completo do usuário e passo a passo
* Ver agentes IA disponíveis→ Papéis especializados para sua equipe
* Explorar usos não técnicos→ Escrita criativa, negócios, bem-estar, educação
* Criar meus próprios agentes IA→ Construir agentes para seu domínio
* Navegar Squads prontos→ Veja como criar e usar equipes de agentes IA
* Entender a arquitetura→ Mergulho técnico profundo
* Reportar problemas→ Bug reports e feature requests

## Importante: Mantenha Sua Instalação AIOX Atualizada

Mantenha-se atualizado sem esforço!Para atualizar sua instalação AIOX existente:

npx aiox-core@latest install

Isto vai:

* ✅ Detectar automaticamente sua instalação existente
* ✅ Atualizar apenas os arquivos que mudaram
* ✅ Criar arquivos de backup.bakpara quaisquer modificações customizadas
* ✅ Preservar suas configurações específicas do projeto

Isto facilita beneficiar-se das últimas melhorias, correções de bugs e novos agentes sem perder suas customizações!

## Início Rápido

### 🚀 Instalação via NPX (Recomendado)

Instale o AIOX com um único comando:

#
 Criar um novo projeto com assistente interativo moderno

npx aiox-core init meu-projeto

#
 Ou instalar em projeto existente

cd
 seu-projeto
npx aiox-core install

#
 Ou usar uma versão específica

npx aiox-core@latest init meu-projeto

### ✨ Assistente de Instalação Moderno

O AIOX agora inclui uma experiência de instalação interativa de última geração, inspirada em ferramentas modernas como Vite e Next.js:

Recursos do Instalador Interativo:

* 🎨Interface Moderna: Prompts coloridos e visuais com @clack/prompts
* ✅Validação em Tempo Real: Feedback instantâneo sobre entradas inválidas
* 🔄Indicadores de Progresso: Spinners para operações longas (cópia de arquivos, instalação de deps)
* 📦Seleção Multi-Componente: Escolha quais componentes instalar com interface intuitiva
* ⚙️Escolha de Gerenciador de Pacotes: Selecione entre npm, yarn ou pnpm
* ⌨️Suporte a Cancelamento: Ctrl+C ou ESC para sair graciosamente a qualquer momento
* 📊Resumo de Instalação: Visualize todas as configurações antes de prosseguir
* ⏱️Rastreamento de Duração: Veja quanto tempo levou a instalação

O instalador oferece:

* ✅ Download da versão mais recente do NPM
* ✅ Assistente de instalação interativo moderno
* ✅ Configuração automática do IDE (Codex CLI, Cursor ou Claude Code)
* ✅ Configuração de todos os agentes e fluxos de trabalho AIOX
* ✅ Criação dos arquivos de configuração necessários
* ✅ Inicialização do sistema de meta-agentes
* ✅ Verificações de saúde do sistema
* ✅Suporte Cross-Platform: Testado em Windows, macOS e Linux

É isso!Sem clonar, sem configuração manual - apenas um comando e você está pronto para começar com uma experiência de instalação moderna e profissional.

Pré-requisitos:Node.jsv18+ necessário (v20+ recomendado) |Troubleshooting

### Atualizando uma Instalação Existente

Se você já tem o AIOX instalado:

npx aiox-core@latest install

#
 O instalador detectará sua instalação existente e a atualizará

### Configure Seu IDE para Desenvolvimento AIOX

O AIOX inclui regras pré-configuradas para IDE para melhorar sua experiência de desenvolvimento:

#### Para Cursor:

1. Abra as configurações do Cursor
2. Navegue atéUser Rules
3. Copie o conteúdo de.cursor/global-rules.md
4. Cole na seção de regras e salve

#### Para Claude Code:

* ✅ Já configurado! O arquivo.claude/CLAUDE.mdé carregado automaticamente
* Sync dedicado de agentes:npm run sync:ide:claude
* Validacao dedicada:npm run validate:claude-sync && npm run validate:claude-integration

#### Para Codex CLI:

* ✅ Integração de primeira classe no AIOX 4.2 (pipeline de ativação e greeting compartilhado)
* ✅ Já configurado! O arquivoAGENTS.mdna raiz é carregado automaticamente
* Opcional: sincronize agentes auxiliares comnpm run sync:ide:codex
* Recomendado neste repositório: gerar e versionar skills locais comnpm run sync:skills:codex
* Usenpm run sync:skills:codex:globalapenas fora deste projeto (para evitar duplicidade no/skills)
* Validacao dedicada:npm run validate:codex-sync && npm run validate:codex-integration
* Guardrails de skills/paths:npm run validate:codex-skills && npm run validate:paths

#### Para Gemini CLI:

* ✅ Regras e agentes sincronizaveis comnpm run sync:ide:gemini
* Arquivos gerados em.gemini/rules.md,.gemini/rules/AIOX/agents/e.gemini/commands/*.toml
* ✅ Hooks e settings locais no fluxo de instalacao (.gemini/hooks/+.gemini/settings.json)
* ✅ Ativacao rapida por slash commands (/aiox-menu,/aiox-dev,/aiox-architect, etc.)
* Validacao dedicada:npm run validate:gemini-sync && npm run validate:gemini-integration
* Paridade multi-IDE em um comando:npm run validate:parity

Estas regras fornecem:

* 🤖 Reconhecimento e integração de comandos de agentes
* 📋 Fluxo de trabalho de desenvolvimento dirigido por histórias
* ✅ Rastreamento automático de checkboxes
* 🧪 Padrões de teste e validação
* 📝 Padrões de código específicos do AIOX

### Início Mais Rápido com Interface Web (2 minutos)

1. Instale o AIOX: Executenpx aiox-core init meu-projeto
2. Configure seu IDE: Siga as instruções de configuração para Codex CLI, Cursor ou Claude Code
3. Comece a Planejar: Ative um agente como@analystpara começar a criar seu briefing
4. Use comandos AIOX: Digite*helppara ver comandos disponíveis
5. Siga o fluxo: Veja oGuia do usuáriopara mais detalhes

### Referência de Comandos CLI

O AIOX oferece uma CLI moderna e cross-platform com comandos intuitivos:

#
 Gerenciamento de Projeto (com assistente interativo)

npx aiox-core init
<
nome-projeto
>
 [opções]
 --force Forçar criação em diretório não vazio
 --skip-install Pular instalação de dependências npm
 --template
<
nome
>
 Usar template específico (default, minimal, enterprise)

#
 Instalação e Configuração (com prompts modernos)

npx aiox-core install [opções]
 --force Sobrescrever configuração existente
 --quiet Saída mínima durante instalação
 --dry-run Simular instalação sem modificar arquivos

#
 Comandos do Sistema

npx aiox-core --version Exibir versão instalada
npx aiox-core --help Exibir ajuda detalhada
npx aiox-core info Exibir informações
do
 sistema
npx aiox-core doctor Executar diagnósticos
do
 sistema
npx aiox-core doctor --fix Corrigir problemas detectados automaticamente

#
 Manutenção

npx aiox-core update Atualizar para versão mais recente
npx aiox-core uninstall Remover AIOX

Recursos da CLI:

* ✅Help System Abrangente:--helpem qualquer comando mostra documentação detalhada
* ✅Validação de Entrada: Feedback imediato sobre parâmetros inválidos
* ✅Mensagens Coloridas: Erros em vermelho, sucessos em verde, avisos em amarelo
* ✅Cross-Platform: Funciona perfeitamente em Windows, macOS e Linux
* ✅Suporte a Dry-Run: Teste instalações sem modificar arquivos

### 💡 Exemplos de Uso

#### Instalação Interativa Completa

$ npx aiox-core install

🚀 AIOX Installation

◆ What is your project name
?

│ my-awesome-project
│
◇ Which directory should we use
?

│ ./my-awesome-project
│
◆ Choose components to install:
│ ● Core Framework (Required)
│ ● Agent System (Required)
│ ● Squads (optional)
│ ○ Example Projects (optional)
│
◇ Select package manager:
│ ● npm
│ ○ yarn
│ ○ pnpm
│
◆ Initialize Git repository
?

│ Yes
│
◆ Install dependencies
?

│ Yes
│
▸ Creating project directory...
▸ Copying framework files...
▸ Initializing Git repository...
▸ Installing dependencies (this may take a minute)...
▸ Configuring environment...
▸ Running post-installation setup...

✔ Installation completed successfully
!
 (34.2s)

Next steps:

cd
 my-awesome-project
 aiox-core doctor
#
 Verify installation

 aiox-core --help
#
 See available commands

#### Instalação Silenciosa (CI/CD)

#
 Instalação automatizada sem prompts

$ npx aiox-core install --quiet --force
✔ AIOX installed successfully

#### Simulação de Instalação (Dry-Run)

#
 Testar instalação sem modificar arquivos

$ npx aiox-core install --dry-run

[DRY RUN] Would create: ./my-project/
[DRY RUN] Would copy: .aiox-core/ (45 files)
[DRY RUN] Would initialize: Git repository
[DRY RUN] Would install: npm dependencies
✔ Dry run completed - no files were modified

#### Diagnóstico do Sistema

$ npx aiox-core doctor

🏥 AIOX System Diagnostics

✔ Node.js version: v20.10.0 (meets requirement:
>
=18.0.0)
✔ npm version: 10.2.3
✔ Git installed: version 2.43.0
✔ GitHub CLI: gh 2.40.1
✔ AIOX: v4.2.11

Configuration:
✔ .aiox-core/ directory exists
✔ Agent files: 11 found
✔ Workflow files: 8 found
✔ Templates: 15 found

Dependencies:
✔ @clack/prompts: ^0.7.0
✔ commander: ^12.0.0
✔ execa: ^9.0.0
✔ fs-extra: ^11.0.0
✔ picocolors: ^1.0.0

✅ All checks passed
!
 Your installation is healthy.

#### Obter Ajuda

$ npx aiox-core --help

Usage: aiox-core [options] [command]

AIOX: AI-Orchestrated System
for
 Full Stack Development

Options:
 -V, --version output the version number
 -h, --help display
help

for

command

Commands:
 init
<
project-name
>
 Create new AIOX project with interactive wizard
 install [options] Install AIOX
in
 current directory
 info Display system information
 doctor [options] Run system diagnostics and health checks

help
 [command] display
help

for

command

Run
'
aiox-core <command> --help
'

for
 detailed information about each command.

### Alternativa: Clonar e Construir

Para contribuidores ou usuários avançados que queiram modificar o código fonte:

#
 Clonar o repositório

git clone https://github.com/SynkraAI/aiox-core.git

cd
 aiox-core

#
 Instalar dependências

npm install

#
 Executar o instalador

npm run install:aiox

### Configuração Rápida para Equipe

Para membros da equipe ingressando no projeto:

#
 Instalar AIOX no projeto

npx aiox-core@latest install

#
 Isto vai:

#
 1. Detectar instalação existente (se houver)

#
 2. Instalar/atualizar framework AIOX

#
 3. Configurar agentes e workflows

## 🌟 Além do Desenvolvimento de Software - Squads

O framework de linguagem natural do AIOX funciona em QUALQUER domínio. Os Squads fornecem agentes IA especializados para escrita criativa, estratégia de negócios, saúde e bem-estar, educação e muito mais. Além disso, os Squads podem expandir o núcleo do AIOX com funcionalidade específica que não é genérica para todos os casos.Veja o Guia de Squadse aprenda a criar os seus próprios!

## Agentes Disponíveis

O AIOX vem com 12 agentes especializados:

### Agentes Meta

* aiox-master- Agente mestre de orquestração (inclui capacidades de desenvolvimento de framework)
* aiox-orchestrator- Orquestrador de fluxo de trabalho e coordenação de equipe

### Agentes de Planejamento (Interface Web)

* analyst- Especialista em análise de negócios e criação de PRD
* pm(Product Manager) - Gerente de produto e priorização
* architect- Arquiteto de sistema e design técnico
* ux-expert- Design de experiência do usuário e usabilidade

### Agentes de Desenvolvimento (IDE)

* sm(Scrum Master) - Gerenciamento de sprint e criação de histórias
* dev- Desenvolvedor e implementação
* qa- Garantia de qualidade e testes
* po(Product Owner) - Gerenciamento de backlog e histórias
* data-engineer- Design de banco de dados e modelagem de dados
* devops- CI/CD, infraestrutura e operações git (autoridade exclusiva de push)

## Documentação e Recursos

### Guias Essenciais

* 📖Guia do Usuário- Passo a passo completo desde a concepção até a conclusão do projeto
* 🏗️Arquitetura Principal- Mergulho técnico profundo e design do sistema
* 🚀Guia de Squads- Estenda o AIOX para qualquer domínio além do desenvolvimento de software

### Documentação Adicional

* 🤖Guia de Squads- Crie e publique equipes de agentes IA
* 📋Primeiros Passos- Tutorial passo a passo para iniciantes
* 🔧Solução de Problemas- Soluções para problemas comuns
* 🎯Princípios Orientadores- Filosofia e melhores práticas do AIOX
* 🏛️Visão Geral da Arquitetura- Visão detalhada da arquitetura do sistema
* ⚙️Guia de Ajuste de Performance- Otimize seu fluxo de trabalho AIOX
* 🔒Melhores Práticas de Segurança- Segurança e proteção de dados
* 🔄Guia de Migração- Migração de versões anteriores
* 📦Versionamento e Releases- Política de versões

## 🤖 AIOX Autonomous Development Engine (ADE)

O AIOX introduz oAutonomous Development Engine (ADE)- um sistema completo para desenvolvimento autônomo que transforma requisitos em código funcional.

### 🎯 O Que é o ADE?

O ADE é um conjunto de7 Epicsque habilitam execução autônoma de desenvolvimento:

Epic

Nome

Descrição

1

Worktree Manager

Isolamento de branches via Git worktrees

2

Migration V2→V3

Migração para formato autoClaude V3

3

Spec Pipeline

Transforma requisitos em specs executáveis

4

Execution Engine

Executa specs com 13 steps + self-critique

5

Recovery System

Recuperação automática de falhas

6

QA Evolution

Review estruturado em 10 fases

7

Memory Layer

Memória persistente de padrões e insights

### 🔄 Fluxo Principal

User Request → Spec Pipeline → Execution Engine → QA Review → Working Code
 ↓
 Recovery System
 ↓
 Memory Layer

### ⚡ Quick Start ADE

#
 1. Criar spec a partir de requisito

@pm
*
gather-requirements
@architect
*
assess-complexity
@analyst
*
research-deps
@pm
*
write-spec
@qa
*
critique-spec

#
 2. Executar spec aprovada

@architect
*
create-plan
@architect
*
create-context
@dev
*
execute-subtask 1.1

#
 3. QA Review

@qa
*
review-build STORY-42

### 📖 Documentação ADE

* Guia Completo do ADE- Tutorial passo a passo
* Alterações nos Agentes- Comandos e capabilities por agente
* Epic 1 - Worktree Manager
* Epic 2 - Migration V2→V3
* Epic 3 - Spec Pipeline
* Epic 4 - Execution Engine
* Epic 5 - Recovery System
* Epic 6 - QA Evolution
* Epic 7 - Memory Layer

### 🆕 Novos Comandos por Agente

@devops:

* *create-worktree,*list-worktrees,*merge-worktree,*cleanup-worktrees
* *inventory-assets,*analyze-paths,*migrate-agent,*migrate-batch

@pm:

* *gather-requirements,*write-spec

@architect:

* *assess-complexity,*create-plan,*create-context,*map-codebase

@analyst:

* *research-deps,*extract-patterns

@qa:

* *critique-spec,*review-build,*request-fix,*verify-fix

@dev:

* *execute-subtask,*track-attempt,*rollback,*capture-insights,*list-gotchas,*apply-qa-fix

## Criando Seu Próprio Squad

Squads permitem estender o AIOX para qualquer domínio. Estrutura básica:

squads/seu-squad/
├── config.yaml # Configuração do squad
├── agents/ # Agentes especializados
├── tasks/ # Fluxos de trabalho de tarefas
├── templates/ # Templates de documentos
├── checklists/ # Checklists de validação
├── data/ # Base de conhecimento
├── README.md # Documentação do squad
└── user-guide.md # Guia do usuário

Veja oGuia de Squadspara instruções detalhadas.

## Squads Disponíveis

Squads são equipes modulares de agentes IA. Veja aVisão Geral de Squadspara mais informações.

### Squads Externos

* hybrid-ops- Operações híbridas humano-agente (repositório separado)

## AIOX Pro

OAIOX Pro(@aiox-fullstack/pro) é o módulo premium do AIOX, oferecendo funcionalidades avançadas para equipes e projetos de maior escala.

Disponibilidade restrita:O AIOX Pro está disponível exclusivamente para membros doAIOX Cohort Advanced.Saiba mais sobre o programa.

### Instalação

npm install @aiox-fullstack/pro

### Features Premium

* Squads Avançados- Squads especializados com capacidades expandidas
* Memory Layer- Memória persistente de padrões e insights entre sessões
* Métricas & Analytics- Dashboard de produtividade e métricas de desenvolvimento
* Integrações Enterprise- Conectores para Jira, Linear, Notion e mais
* Configuração em Camadas- Sistema de configuração L1-L4 com herança
* Licenciamento- Gerenciamento de licença viaaiox pro activate --key <KEY>

Para mais informações, executenpx aiox-core pro --helpapós a instalação.

## Suporte

* 🐛Rastreador de Issues- Bug reports e feature requests
* 💡Processo de Features- Como propor novas funcionalidades
* 📋Como Contribuir
* 🗺️Roadmap- Veja o que estamos construindo
* 🤖Guia de Squads- Crie equipes de agentes IA

## Git Workflow e Validação

O AIOX implementa um sistema de validação de múltiplas camadas para garantir qualidade do código e consistência:

### 🛡️ Defense in Depth - 3 Camadas de Validação

Camada 1: Pre-commit (Local - Rápida)

* ✅ ESLint - Qualidade de código
* ✅ TypeScript - Verificação de tipos
* ⚡ Performance: <5s
* 💾 Cache habilitado

Camada 2: Pre-push (Local - Validação de Stories)

* ✅ Validação de checkboxes de histórias
* ✅ Consistência de status
* ✅ Seções obrigatórias

Camada 3: CI/CD (Cloud - Obrigatório para merge)

* ✅ Todos os testes
* ✅ Cobertura de testes (80% mínimo)
* ✅ Validações completas
* ✅ GitHub Actions

### 📖 Documentação Detalhada

* 📋Guia Completo de Git Workflow- Guia detalhado do fluxo de trabalho
* 📋CONTRIBUTING.md- Guia de contribuição

### Comandos Disponíveis

#
 Validações locais

npm run lint
#
 ESLint

npm run typecheck
#
 TypeScript

npm
test

#
 Testes

npm run test:coverage
#
 Testes com cobertura

#
 Validador AIOX

node .aiox-core/utils/aiox-validator.js pre-commit
#
 Validação pre-commit

node .aiox-core/utils/aiox-validator.js pre-push
#
 Validação pre-push

node .aiox-core/utils/aiox-validator.js stories
#
 Validar todas stories

### Branch Protection

Configure proteção da branch master com:

node scripts/setup-branch-protection.js

Requer:

* GitHub CLI (gh) instalado e autenticado
* Acesso de admin ao repositório

## Contribuindo

Estamos empolgados com contribuições e acolhemos suas ideias, melhorias e Squads!🎉

Para contribuir:

1. Fork o repositório
2. Crie uma branch para sua feature (git checkout -b feature/MinhaNovaFeature)
3. Commit suas mudanças (git commit -m 'feat: Adicionar nova feature')
4. Push para a branch (git push origin feature/MinhaNovaFeature)
5. Abra um Pull Request

Veja também:

* 📋Como Contribuir com Pull Requests
* 📋Guia de Git Workflow

## 📄 Legal

Documento

English

Português

Licença

MIT License

-

Modelo de Licença

Core vs Pro

-

Privacidade

Privacy Policy

-

Termos de Uso

Terms of Use

-

Código de Conduta

Code of Conduct

PT-BR

Contribuição

Contributing

PT-BR

Segurança

Security

PT-BR

Comunidade

Community

PT-BR

Roadmap

Roadmap

PT-BR

Changelog

Version History

-

## Contribuidores

### 🌟 Contribuidores da Comunidade

Nikolas de Hor
💻🐛
⚠️
👀

Construído com ❤️ para a comunidade de desenvolvimento assistido por IA

⬆ Voltar ao topo

## About

Synkra AIOS: AI-Orchestrated System for Full Stack Development - Core Framework v4.0

github.com/allfluence/aios-core

### Topics

 nodejs

 cli

 development

 automation

 framework

 typescript

 ai

 orchestration

 fullstack

 agents

 ai-agents

 claude

### Resources

 Readme



### License

 View license


### Code of conduct

 Code of conduct


### Contributing

 Contributing


### Security policy

 Security policy


### Uh oh!

There was an error while loading.Please reload this page.





Activity


Custom properties


### Stars

2.3k

 stars


### Watchers

56

 watching


### Forks

753

 forks


 Report repository



## Releases36

v5.0.0 — AIOX Rebrand

 Latest



Mar 5, 2026



+ 35 releases

## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.






* https://f5.ventures/aioxfullstack

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





### Uh oh!

There was an error while loading.Please reload this page.





## Contributors

### Uh oh!

There was an error while loading.Please reload this page.





## Languages

* JavaScript96.0%
* Python1.2%
* Shell1.1%
* Handlebars0.6%
* PLpgSQL0.4%
* CSS0.3%
* Other0.4%
