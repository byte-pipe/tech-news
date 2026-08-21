---
title: '1ª vez trabalhando com git em um time: tudo que você precisa saber - DEV Community'
url: https://dev.to/he4rt/1a-vez-trabalhando-com-git-com-time-tudo-que-voce-precisa-saber-19il
site_name: devto
content_file: devto-1ª-vez-trabalhando-com-git-em-um-time-tudo-que-voc
fetched_at: '2026-08-21T19:25:10.611780'
original_url: https://dev.to/he4rt/1a-vez-trabalhando-com-git-com-time-tudo-que-voce-precisa-saber-19il
author: vitoriazzp
date: '2026-08-20'
description: Faz mais de 5 anos que eu não abria um PR ou issue técnica no Github, mas essa semana tenho aprendido... Tagged with braziliandevs, opensource, github, beginners.
tags: '#braziliandevs, #opensource, #github, #beginners'
---

Faz mais de 5 anos que eu não abria um PR ou issue técnica no Github, mas essa semana tenho aprendido algumas boas práticas e termos que reuni neste artigo.

## Introdução

Essa semana eu fiz uma coisa simples: atualizei o README de um projeto open source, o4noobs, da comunidade He4rt. Troquei um badge, ajustei o contraste de um logo, organizei umas pastas e adicionei um índice pra facilitar a navegação. Nada muito complexo no fim das contas.

Só que antes de chegar no "nada muito complexo", eu passei um tempo enrolada com uma pergunta boba:

"E se eu mandar isso direto pra branch principal e bagunçar tudo?"

Se tu já sentiu esse friozinho na barriga antes de mexer num repositório que não é só teu, esse artigo é pra ti. Não importa se tu é dev há anos ou se nunca abriu um terminal na vida... A lógica por trás de "como contribuir sem quebrar nada" é a mesma e bem mais simples do que parece.

## Definição de Git Colaborativo

Quando eu aprendi git há uns anos, aprendi somente o versionamento e a enviar os arquivos pra dentro do Github, mas ele é bem mais que isso, né?

É através dele que times enormes interagem a respeito de um mesmo projeto de forma organizada, comentando, gerenciando tarefas, sugerindo melhorias e conhecendo o que os outros envolvidos estão fazendo. Isso é a parte doGit Colaborativo.

O Git resolve isso com um conceito central:branches(ou "ramificações"). Cada branch é tipo uma cópia paralela do projeto, onde tu pode mexer à vontade sem afetar a versão "oficial" (geralmente chamada demainoumaster). Quando tu termina sua parte, tu propõe que essas mudanças sejam incorporadas de volta peloPull Request (PR).

Ou seja, o fluxo básico é:

1. Tu cria uma branch nova a partir do projeto principal
2. Faz as alterações lá, no seu espaço isolado
3. Envia (push) essa branch pro repositório remoto
4. Abre um Pull Request pedindo pra essas mudanças serem revisadas e, se aprovadas, unidas (merge) à branch principal

Ninguém mexe direto na versão "de produção" do projeto. Isso é o que torna possível centenas de pessoas contribuírem pro mesmo repositório sem o caos se instalar.

## Principais Aprendizados

Bom, na prática, foi mexendo que aprendi (e relembrei) algumas coisas que acho que valem ser compartilhadas:

Branch nova não é sobre desconfiança, é sobre segurança.Criar uma branch pra cada contribuição não é burocracia sem sentido — é o que garante que, se algo der errado, o "errado" fica isolado ali, sem afetar o projeto principal. Isso vale tanto pra quem tá contribuindo quanto pra quem revisa.

git pushnão é a mesma coisa que abrir um Pull Request.Isso me pegou de surpresa: o push só envia sua branch pro GitHub. O PR é um passo separado, onde tu formaliza o pedido de revisão. O próprio terminal, inclusive, já te entrega o link pronto pra criar o PR depois do push.

Não precisa ter issue aberta pra contribuir.Eu fiquei presa nessa por um tempo. Pensei: "Ah, mas ninguém pediu essa melhoria, será que posso mandar mesmo assim?"Pode!Principalmente em documentação: se tu enxergou algo que pode melhorar, a contribuição em si já é a justificativa.

Descrição de PR boa não é uma lista de tudo o que mudou linha por linha.É um resumo categorizado, por exemplo:

* o que foi feito,
* por quê,
* e os principais pontos agrupados por tema. 
Isso poupa um tempo enorme para quem vai revisar.

A pasta.githubpode ser local ao repositório ou um "padrão" pra organização inteira, dependendo se existe um repositório especial chamado literalmente.githubna conta. Detalhe pequeno, mas que ajuda a entender por que às vezes umas configurações "aparecem" em vários repositórios sem alguém ter copiado e colado em cada um.

Nenhum desses pontos é complicado isoladamente. O que trava a gente, geralmente, não é a técnica —é o medo.

## Gerenciando o medo de fazer errado

Aqui vai a parte que eu acho mais importante desse artigo, sinceramente.

Toda vez que eu vou mexer num repositório que não é só meu, seja um projeto open source, seja no trabalho, bate aquele receio: "e se eu errar? E se eu quebrar algo? E se acharem que eu não sei o que tô fazendo?

E olha, isso não passa de uma hora pra outra. Mas duas coisas mudaram bastante minha relação com esse medo:

### Entender a ferramenta tira o poder do medo.

Muito do que a gente teme é o desconhecido. Quando eu entendi que uma branch é literalmente um espaço isolado, que nada do que eu fizesse lá afetaria amainaté alguém aprovar um merge, o medo diminuiu bastante. Não é sobre ser corajosa, é sobre saber que o sistema já foi desenhado pra proteger contra erro.

### Errar em público faz parte do processo; não é uma falha nele.

Acomunidade open sourceinteira éconstruída em cima de gente errando, corrigindo, revisando o trabalho umas das outras. Um PR rejeitado ou com pedido de ajuste não é um veredito sobre tua competência, é literalmente o sistema funcionando como devia.

Se tem uma coisa que eu queria ter escutado antes de começar a contribuir, é isso: ninguém espera que tu chegue sabendo tudo. As branches, os PRs, as revisões, tudo isso existe justamente porque errar faz parte.

Então, se tu tá enrolando para abrir aquele primeiro PR por medo de fazer besteira: cria a branch, faz a mudança e manda ver. O pior que pode acontecer é alguém te dar um feedback — e isso, no fim das contas, é como a gente aprende e melhora

## Materiais Complementares

Esses são todos os materiais que me foram indicados ou lidos durante as práticas descritas acima. Alguns ensinam sobre estrutura e outros sobre boas práticas. Também tive muita ajuda de amigos e fiz pesquisas com IA pra compreender exatamente termos ou partes de código que eu não estava entendendo.

* How to Write a Bug Report
* What Makes a Good Bug Report
* Revisando alterações propostas em um Pull Request — Documentação do GitHub
* Where to Publish: Article Types — Frontiers
* Conventional Branch
* Semantic Versioning (SemVer) em português

Se esse artigo te ajudou de alguma forma, deixa o coraçãozinho aí 💜 e conta nos comentários:

qual foi teu primeiro PR ou tua primeira contribuição pra um projeto que não era seu? Bora trocar ideia!

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse