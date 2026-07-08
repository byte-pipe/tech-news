---
title: 'Ownership: do "temos um rojão na mão" até "não precisa mais pensar nisso" - DEV Community'
url: https://dev.to/he4rt/ownership-do-temos-um-rojao-na-mao-ate-nao-precisa-mais-pensar-nisso-3ki7
site_name: devto
content_file: devto-ownership-do-temos-um-rojão-na-mão-até-não-precisa
fetched_at: '2026-07-08T19:33:35.013561'
original_url: https://dev.to/he4rt/ownership-do-temos-um-rojao-na-mao-ate-nao-precisa-mais-pensar-nisso-3ki7
author: Daniel Reis
date: '2026-07-08'
description: É aquele famoso "ou faz direito ou não faz" que todo dev deveria respeitar desde o inicio dos seus... Tagged with productivity, beginners, braziliandevs, career.
tags: '#productivity, #beginners, #braziliandevs, #career'
---

É aquele famoso "ou faz direito ou não faz" que todo dev deveria respeitar desde o inicio dos seus estudos.

## Tabela de Conteúdo

* 1. Prólogo
* 2. Entenda o problema real
* 3. Projete antes de codar
* 4. Execute
* 5. Verifique (em produção)
* 6. Comunique
* 7. Acompanhe
* É muita coisa. E olha que ainda tem mais.

## 1. Prólogo

Acho que toda vez que eu vejo um dev iniciante, meu primeiro pensamento é: a hora de "criar" responsabilidade é literalmente agora, no inicio da carreira. Por exemplo: quando eu era junior eu pegava task, escrevia o código, mandava o Pull Request, que era mergeado e ia dormir feliz. Três dias depois o problema voltava, do mesmo jeito, e adivinha quem teve que mexer de novo? Eu. Por anos eu continuei fazendo aquilo, esquecendo daquela frase clichê de que: "30% do trabalho é de fato código". Mas ai de fato, quais são os outros 70%?

Quando comecei a me perguntar isso, simplesmente entendi que: eu tinha entregado umcódigo, poranosnão tinha resolvido umproblema. E é sobre isso que a gente vai falar hoje.

Eu uso muito a palavraownership. Vivo falando "você pode assumir isso?", "consegue cuidar disso?", "tá com você?" e faz um tempão que eu não paro pra explicar o queownershipsignificapra mim. Então bora lá, que hoje o assunto é esse.

Quando eu te pergunto "você pode assumir isso?", presta atenção: eunãotô te pedindo pra escrever um código e mandar um PR. Eu tô te pedindo pra serdono da solução de um problema, de ponta a ponta. Do "temos um problema" até o "não precisa mais pensar nisso".

E cara, isso muda TUDO. Assumir uma tarefa é entregar um código. Assumir umproblemaé garantir que ele deixou de existir, e que ninguém, você inclusive, vai precisar voltar a pensar nele nunca mais. Quando você fala que táresolvendoalguma coisa, a expectativa é que você faça essa porra toda que vem abaixo. E ó, não é papo de gestão não: dominar isso é o que faz o time te dar problema cada vez maior sem medo. É basicamente o cheat code pra virar sênior de verdade, não sênior de tempo de casa.

## 2. Entenda o problema real

Antes de qualquer linha de código, tenha CERTEZA de que você sabe o que tá resolvendo.

O erro mais comum do mundo é começar pela solução. Você provavelmente já tem uma na cabeça sem ter parado 5 minutos pra pensar no que a gente tá de fato tentando resolver. Se você acha que "o problema é que precisamos migrar de X pra Y", pera aí mano, isso não é um problema, isso é umasolução. O problema de verdade é algo tipo "a performance tá uma merda", "não é estável", "quebra pro cliente X".

"Migrar do MySQL pro Postgres" é solução."A busca de membros da comunidade demora 8 segundos" é problema.

Sacou a diferença? Beleza. Uma vez que você tem o problema real na mão, a próxima pergunta é:será que existem outras soluções possíveis?Pensa nelas. Um índice resolve? Um cache resolve? Reescrever aquela query zoada resolve, antes de trocar o banco INTEIRO? Cada caminho tem seus tradeoffs. Qual é o melhor levando isso em conta?

Se você pular essa fase, você corre o risco de passar duas semanas construindo a solução perfeita pro problema errado. E aí não tem PLAU que salve.

Nosso caso (a busca de 8s):o problema não é "migrar pro Postgres". É "a busca de membros demora 8 segundos". Antes de trocar de banco, será que um índice não mata isso?

## 3. Projete antes de codar

É aqui que a maioria dos problemas de produção nasce: nas perguntas que ninguém fez antes de começar. Então vamo fazer elas agora.

Pensa nos edge cases.Quais são? Quais são importantes? Quais dá pra ignorar de propósito (e deixar registrado que você ignorou)? Membro sem avatar, nome com emoji, lista vazia, fuso horário diferente do servidor. Escolher o que ignorar é uma decisão consciente; ignorar sem perceber é um bug esperando a hora de estourar na sua cara.

Pensa nas falhas.Falha de rede, por exemplo, é GARANTIDA. Como a gente lida com ela? Retry? Tá, mas com que frequência? Por quanto tempo? O webhook caiu: retry com backoff? três tentativas? e depois, descarta ou joga numa fila de reprocesso?

Pensa no fluxo de dados.Quanto dado tá envolvido? Precisa migrar algo? Limpar algo? Como você consegue dado de verdade pra testar direito? Quais invariantes existem nos dados? E principalmente: quais premissas sobre o formato dos dados você tem e aindanão confirmou? "Todo membro tem e-mail"... você checou isso na base ou só assumiu e foi feliz?

Pensa em como você vai testar.Como você vai saber se o que construiu tá certo? Testes automatizados bastam? Precisa cutucar na mão? A diferença aparece num screenshot ou num vídeo? Um bug de dark mode não aparece em teste unitário, meu amigo. Aparece num print.

Pensa em como isso vai ser anunciado.Como a gente comunicaria? Você consegue visualizar o anúncio? Como isso se encaixa no quadro maior do roadmap? Dúvida ou preocupação nessa área?Questiona, pergunta, dá um push back.Se você não consegue escrever o anúncio em duas frases, o escopo provavelmente ainda tá bagunçado.

Nosso caso:e se o membro não tiver avatar? E se a busca vier vazia? E se caírem 50 mil membros de uma vez? Anota tudo isso ANTES de codar.

## 4. Execute

A fase mais curta de descrever e a mais longa de viver. O padrão é um só, e é simples.

Faça o trabalho com precisão, com cuidado, com senso de urgência e com calma. Não faça nada pela metade. E ó, urgência aqui não é pressa afobada não: é não deixar o problema esperando por você, sem sacrificar o cuidado no caminho.

E tem um teste antes de dar merge, o meu favorito:

Eu tenho orgulho disso?Eu mostraria isso pro John Carmack (o lendário programador do Doom e Quake) e falaria: "foi isso que eu construí, com essas restrições, com esses tradeoffs"?

Se a resposta for não, sinto muito, mas ainda não terminou.

Nosso caso:boto o índice, reescrevo a query zoada, testo local. Caiu de 8s pra 120ms. Tenho orgulho disso? Tenho.

## 5. Verifique (em produção)

Terminar de codar NÃO é terminar. Terminar é o problema resolvido, rodando, no ar. Anota isso.

Testa na mão.Sim, existem testes automatizados. Mas Daniel, se eu tenho teste automatizado, pra quê testar na mão? Porque teste passa e feature quebra, meu amigo. São coisas diferentes. Em 99% dos casos você consegue confirmar na unha que o que construiu funciona: rodando você mesmo, pedindo pra um agente percorrer os cenários, cutucando os dados antes e depois, tirando screenshots, gravando uma demo. Você temcertezaque resolveu o problema? Roda o fluxo inteiro como se fosse o usuário: cria a conta, dispara a ação, confere o resultado no banco.

Garanta que chegou em produção e funciona lá.Tá deployado? O deploy quebrou? Precisa ativar alguma feature flag? A flag funciona mesmo? Dá pra usar em produção? Você consegue confirmar que tá de fato no ar? "Mergeou" não é "shipou", tá ligado? Abre a produção e usa a feature você mesmo.

Nosso caso:subo pra produção, abro EU MESMO e busco "daniel". Os 8s viraram instantâneo de verdade, com dado real, não só no meu localhost feliz.

## 6. Comunique

Código que ninguém sabe que existe gera bug que ninguém sabe explicar. Comunicação é parte do trabalho, não é um extra que você faz se sobrar tempo.

Seus colegas precisam saber?É uma feature nova que todo mundo deveria testar? Uma convenção nova no código? Uma coisa traiçoeira que todos precisam conhecer? Avisa. Não subestima a visão periférica do time: saber que a pessoa X mudou ontem o comportamento de como Z funciona pode economizar TRÊS HORAS de debug da pessoa Y amanhã. Mudou como o cache de sessão funciona? Uma mensagenzinha no canal do time hoje vale três horas de debug de outra pessoa amanhã. É de graça, faz.

Os clientes precisam saber?Quem reportou o bug? Quem tá bloqueado esperando isso? Avisa essas pessoas. Responde a thread de quem abriu a issue: "saiu na versão de hoje, pode testar aí".

O mundo precisa saber?Anuncia que saiu. Changelog, post no canal de announcements, tweet, o formato que fizer sentido pro tamanho da mudança.

Nosso caso:mando no canal do time: "a busca de membros tava 8s, agora tá instantânea, quem reclamou pode testar". E respondo a thread de quem abriu a issue.

## 7. Acompanhe

Ownership não termina no deploy. Termina quando NINGUÉM mais precisa pensar naquilo, você incluso.

Tem follow-ups? Você precisa dar uma olhada nos logs pra ver como tá aquilo que shipou? Uma semana depois, quem sabe? Agenda um lembrete: "conferir a taxa de erro do endpoint novo na sexta". O ciclo só fecha de verdade quando você tem certeza que o problema ficou resolvido econtinuouresolvido.

Nosso caso:sexta que vem eu volto no log pra confirmar que a busca continuou rápida mesmo com a base crescendo. Aí sim o ciclo fechou.

## É muita coisa. E olha que ainda tem mais.

Sim, é muita coisa, eu sei. E na real ainda tem mais, porque com certeza a gente esqueceu algum item aqui no meio.

Mas mano, é assim que se constrói produto em time pequeno. A gente não tem PM, não tem departamento de QA pra passar a bola. Somos pequenos, mas somos bons, e a gente dá conta dessa porra toda.

E ó, é SEMPRE ok pedir ajuda. É ok fazer pergunta. É ok refazer e conferir três vezes.O que não é ok é assumir, lá no fundo sem falar pra ninguém, que outra pessoa vai fazer as coisas que você não pensou.

Da comunidade para a comunidade.

Bebe água, me segue nas redes sociais e a gente se vê no próximo artigo!

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse