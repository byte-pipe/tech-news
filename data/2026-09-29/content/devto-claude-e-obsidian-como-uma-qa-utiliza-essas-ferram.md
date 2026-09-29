---
title: Claude e Obsidian - Como uma QA utiliza essas ferramentas no dia-a-dia - DEV Community
url: https://dev.to/he4rt/claude-e-obsidian-como-uma-qa-utiliza-essas-ferramentas-no-dia-a-dia-51jc
site_name: devto
content_file: devto-claude-e-obsidian-como-uma-qa-utiliza-essas-ferram
fetched_at: '2026-09-29T16:48:42.009558'
original_url: https://dev.to/he4rt/claude-e-obsidian-como-uma-qa-utiliza-essas-ferramentas-no-dia-a-dia-51jc
author: Alicia Marianne Gonçalves
date: '2026-09-28'
description: 🇺🇸 You can also read the English version of this article on AWS Community Builders. Ser QA nessa... Tagged with ai, productivity, braziliandevs, claude.
tags: '#ai, #productivity, #braziliandevs, #claude'
---

Local Markdown beats Notion bloat for QA focus

🇺🇸You can also read the English version of this article onAWS Community Builders.

Ser QA nessa era de IA tem sido bem desafiador, principalmente quando a velocidade de entrega é maior, fica o grande questionamento: Como eu vou conseguir garantir que não me esqueci de nada? Será que estou cobrindo os cenários que realmente precisam ser cobertos? Ter uma boa organização é essencial pra todas áreas da vida, e dentro da área de QA não seria diferente, por isso atualmente o Obsidian tem sido uma ferramenta bem presente no meu dia-a-dia, e vim falar pra vocês como eu tenho utilizado ela.

## Por que o Obsidian?

Basicamente, o Obsidian é um aplicativo de anotações e gestão de conhecimento que funciona com arquivos Markdown(.md) que são guardados localmente no seu computador, tendo a possibilidade de te-los na nuvem utilizando a versão paga ou algum plugin da comunidade.

E diversos fatores me fizeram migrar para essa ferramenta. Antes, eu utilizava o Notion que apesar de ser uma boa ferramenta, pra mim, ser tão personalizável visualmente me fazia perder mais tempo criando templates do que realmente adicionando conteúdo a eles.

O fato do Obsidian ser uma ferramenta bem mais "clean" e focada em notas, faz com que menos coisas me tirem do foco. Outro fator é que minhas notas ficam registradas localmente. No ambiente de trabalho a segurança de dados é essencial, então a certeza de que minhas anotações estão seguras me deixa mais tranquila em relação a outras ferramentas. Dentro do obsidian também é possível adicionar plugins externos que possam te auxiliar na produtividade e sem deixar a tela tão poluída, o que é um grande diferencial para mim.

E por ultimo, e mais importante: como tenho utilizado bastante IA em determinadas tarefas, a produção de conteúdos em Markdown já facilita a integração com elas, basicamente o meu Obsidian se tornou meu segundo cérebro.

## Uso e integração com IA

Antes de ir para como tudo se integra, primeiro preciso passar um breve contexto dos recursos que tenho utilizado, que são:

* Os Templates
* As Skills
* E os Plugins do Obsidian

### Templates

A primeira coisa que fiz quando comecei a utilizar o Obsidian, foi a criação de templates para os documentos que normalmente preciso.

Templates são notas que você pode criar, com um padrão específico e sempre que criar uma nota, você pode reutilizar esse template.

Como QA, por enquanto tenho os seguintes templates:

* Template tasks técnicas: é um arquivo de template que sempre que preciso gerar planos de teste para tarefas técnicas(migração de banco de dados, criação de consumers, APIs) esse template será usado de referência.
* Template de tasks de business: segue a mesma lógica do arquivo de template da tasks técnicas, mas o utilizo uma etapa anterior, quando estou dentro do product discovery juntamente com o Product Owner, para definir quais camadas de testes podem ser adicionados para aquela nova funcionalidade, riscos e mitigação dos mesmos, como medir o sucesso daquela nova funcionalidade.
* Template para notas de reuniões: Nesse template tenho os dados principais sobre uma reunião e eu uso ele para tomar notas ou criar roteiros de reuniões que irei estar a frente.

### Skills

A gente sabe que as skills é um recurso muito bom para reduzirmos o tempo em tarefas repetitivas, e manter um padrão enquanto utilizamos a IA, dentro do meu contexto criei algumas skills, sendo elas:

* Criação de plano de testes: Essa é uma skill que sempre que chamo ela passando o ID de uma tarefa do Jira, ela irá buscar o contexto daquela tarefa, em seguida, vai procurar conteúdos de referencia dentro do confluence(eu especifiquei dentro do meuCLAUDE.md), e após essa contextualização, ela irá criar um arquivo .md de plano de teste, utilizando os templates que eu criei anteriormente.
* Busca de tarefas que não possuem planos de teste: É uma skill simples integrada ao MCP da Atlassian, que irá buscar todas as tarefas que possuo com uma flag específica para criação de plano de testes, e irá adicionar a um arquivo .md que utilizo com o pluginKanban, para controle do que eu preciso fazer, já fiz.
* Publicar casos de teste do Zephyr: Essa é uma skill de integração para pegar os testes planejados e publica-los no Zephyr, que é a ferramenta que utilizo para gestão de testes.

### Plugins

Já comecei a citar um plugin que utilizo, que é oKanbanpara a gestão das tarefas, mas recentemente vi a necessidade de dois novos plugins:

* Um plugin que se integre diretamente ao Claude Code, sem a necessidade de sair do Obsidian
* Um plugin para ter fácil acesso as minhas skills.

Como não os encontrei na loja, decidi criar os dois.

O primeiro é um plugin que abre o terminal dentro do vault(pasta) que estou trabalhando, assim fica fácil utilizar o Claude Code dentro do próprio Obsidian:

O segundo, foi um plugin simples para exibir e executar minhas skills, onde consigo ver todas as skills disponíveis e executa-las diretamente do Obsidian.

### Como tudo se integra

Agora já sabemos tudo que eu uso de Templates, Skills e Plugins vou dar um exemplo de como isso funciona na vida real.

Suponha que tenha uma tarefa AB-123, que é um épico ou product discovery vindo de produto, o fluxo para o plano de teste para essa tarefa seria:

Em tasks técnicas, o processo seria similar:

## Notas finais

Confesso que tem sido divertido me aventurar em formas de organização para melhor desempenho utilizando ferramentas de IA. Ainda existe o desafio de revisar o conteúdo gerado por ela, para isso sempre tento coletar feedback do time em relação aos testes gerados, massa de dados fornecidas, validando se está claro ou algo não foi coberto.

Também utilizo a mesma lógica para os Templates. Sempre estou atualizando meus templates, baseado nas revisões que vou fazendo, sempre adiciono um contexto a mais, ou retiro um contexto que não faz sentido para o que preciso.

Sobre os plugins, tenho me aventurado em alguns da comunidade, e também me diverti bastante fazendo um novo. Ainda não estão em uma versão final e nem na loja da comunidade, mas caso você queira se aventurar, dentro do repositório tem o passo-a-passo de como utiliza-los localmente, o link está no final deste artigo.

Enfim, espero que esse artigo seja uma inspiração para você integrar mais coisas ao seu Obsidian ou até mesmo rever seus pensamentos sobre o mesmo.

* Claude Skills Plugin
* Open Terminal Plugin

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse