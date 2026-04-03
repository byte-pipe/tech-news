---
title: 'Engenharia de Prompt: Por Que a Forma Como Você Pergunta Muda Tudo(Um guia introdutório) - DEV Community'
url: https://dev.to/he4rt/engenharia-de-prompt-por-que-a-forma-como-voce-pergunta-muda-tudoum-guia-introdutorio-3hb0
site_name: devto
content_file: devto-engenharia-de-prompt-por-que-a-forma-como-você-per
fetched_at: '2026-03-26T19:28:44.249641'
original_url: https://dev.to/he4rt/engenharia-de-prompt-por-que-a-forma-como-voce-pergunta-muda-tudoum-guia-introdutorio-3hb0
author: Fran Borges
date: '2026-03-23'
description: Neste artigo irei explicar alguns pontos importantes sobre Engenharia de prompt, e como saber esses... Tagged with ai, productivity, beginners, braziliandevs.
tags: '#ai, #productivity, #beginners, #braziliandevs'
---

Neste artigo irei explicar alguns pontos importantes sobre Engenharia de prompt, e como saber esses pontos pode te ajudar muito no dia a dia lidando com IAs, no seus estudos, pesquisas, trabalho, vibeconding, whatever.

* Prefácio
* Antes de tudo, para lembrar, o que é uma LLM mesmo?
* Fazendo Perguntas1 - Evite a Ambiguidade2 - Delimite o Escopo3 - Forneça Contexto Relevante
* 1 - Evite a Ambiguidade
* 2 - Delimite o Escopo
* 3 - Forneça Contexto Relevante
* Considerações Finais

# Prefácio

A base do conhecimento é necessária em tudo que se quer aprender, com LLMs não é diferente. Analisando padrões, conversando com amigos, observei que a grande parte das pessoas que usam LLMs no dia a dia de trabalho, estudo, pessoas que trabalham com tecnologia e principalmente quem está começando na área tech, não tem ideia de como a LLM funciona e de como fazer as perguntas e tirar dúvidas de forma certa para um ChatGPT da vida.

Tendo isso em vista, e como venho estudando bastante sobre esse assunto, como forma de compartilhar o conhecimento, já dizia a poetisa brasileira Cora Coralina:"Feliz aquele que transfere o que sabe, e aprende o que ensina", farei uma série de artigos explicando sobre o tema, e esse é só o primeiro deles...

# Antes de tudo, para lembrar, o que é uma LLM mesmo?

A LLM pode ser definida de algumas formas. Uma delas é:"São modelos de linguagem de máquina, que usam algoritmos de aprendizado profundo (Deep Learning) para processar e aprender a linguagem natural", essa é a sua definição estrutural. A definição que mais gosto é:"A LLM, na sua essência, é composta por dois arquivos: um contendo os pesos (parâmetros) com os conhecimentos aprendidos, e o outro com o código necessário para rodar os dados aprendidos.", como uma pessoa visual, consigo imaginar melhor como funciona.

Então, ChatGPT, Claude e muitos outros são exatamente isso, e atualmente têm a capacidade de executar várias atividades, como escrever código, traduzir texto, responder às mais variadas dúvidas e, dependendo da sua capacidade de escrever prompts mais robustos, pode até criar arquiteturas de produtos, te ajudar a resolver bugs complexos, te dar ideias, e até criar um SaaS revolucionário(risos).

O ponto é que a capacidade das LLMs de "compreender" e "criar" chegou a um ponto bem avançado, e você só chega na camada -17 de boas respostas fazendo as perguntas de forma certa!

Nota:Camada -17se refere à camada onde se acha o minério de ouro no jogo Minecraft ;).

# Fazendo Perguntas

Como fazer as perguntas certas? E por que saber isso importa? Vamos lá.

Saber fazer as perguntas certas para uma LLM é tão importante que existe uma área da tecnologia específica só para isso: aEngenharia de Prompts, definida como"a ciência empírica de planejar, criar e testar prompts para gerar melhores respostas em LLMs". Saber fazer as perguntas certas te coloca em outro nível, você consegue obter as melhores respostas, e isso te traz muitos ganhos, sendo o principal deles aprodutividade.

## Mas afinal, como perguntar de forma certa?

A LLM é poderosa, mas não adivinha sua intenção. Para obter os melhores resultados nas suas buscas, você precisa se concentrar na criação de prompts claros, na especificidade e ser rico em dar contexto. E tudo isso envolve:

### 1 - Evite a Ambiguidade

"Espaço de possibilidades"

Quando você escreve um prompt muito ambíguo, vago, o modelo enxerga vários caminhos estatisticamente válidos. É como se ele estivesse numa encruzilhada com 50 estradas e todas tivessem placas dizendo"Talvez por aqui", ele vai escolher uma, mas não necessariamente a que você precisa: a estrada com o percurso mais rápido e sem trânsito (a resposta correta de fato).

Exemplos:

Prompt ambíguo:

"Crie uma API."

Enter fullscreen mode

Exit fullscreen mode

O que a LLM "vê": Vários caminhos, API REST? GraphQL? Em qual linguagem? Para qual domínio? Com autenticação? Com banco? O modelo vai escolher o caminho mais estatisticamente comum nos dados de treino (provavelmente uma API REST genérica em Node.js com Express), que pode não ter nada a ver com o que você precisa.

Prompt sem ambiguidade:

"Crie um microsserviço em Node.js com Express e TypeScript para processar pagamentos via
Stripe. Endpoints: criar pagamento, confirmar webhook e consultar status. O payload tem:
orderId(UUID), amount(number), currency(enum: BRL, USD) e customerId(string).
Use zod para validação, Prisma com PostgreSQL para persistir as transações e winston
para logs. Retorne status codes apropriados como(201, 200, 400, 422, 500). Trate falhas de
rede com retry automático (máx. 3 tentativas)."

Enter fullscreen mode

Exit fullscreen mode

O que a LLM "vê": Um caminho quase único. Cada detalhe funciona como uma restrição que elimina ambiguidade: "Node.js com Express e TypeScript" define runtime, framework e linguagem de uma vez. "Pagamentos via Stripe" restringe o SDK e o domínio. "3 endpoints explícitos + payload com tipos" elimina adivinhações sobre rotas e schema. "Zod, Prisma, PostgreSQL, Winston" travam a stack, o modelo não vai sugerir alternativas. "Status codes específicos + retry com máximo de 3 tentativas" definem os status HTTP e a estratégia com limites claros. A distribuição de probabilidade fica concentrada e o modelo praticamente "só tem uma opção" a cada token gerado.

### 2 - Delimite o Escopo

"Janela de atenção"

LLMs têm umcontext window(Janela), uma quantidade de tokens (pedaço de palavra) que conseguem ser processados de uma vez. Isso inclui o seu prompt e a resposta gerada. Dentro dessa janela, existe um fenômeno importante: nem todos os tokens recebem a mesma "atenção" no processamento.

O mecanismo deself-attention(o coração da arquitetura Transformer, não é um cubo rsrsrs, e a arquitetura de rede neural, que seria o framework da LLM se a mesma fosse uma linguagem de programação), ela define a estrutura se tudo, calcula relações entre todos os tokens do prompt. Quanto mais tokens irrelevantes existem, mais o modelo precisa "dividir atenção" entre informações úteis e inúteis.

Exemplos:

Sem escopo:

"Me ensine Docker."

Enter fullscreen mode

Exit fullscreen mode

O que acontece internamente: O modelo precisa decidir entre centenas de subtópicos, instalação, conceitos básicos, Dockerfile, docker-compose, volumes, orquestração, a atenção se fragmenta e o resultado é um overview superficial de tudo.

Com escopo:

"Explique o conceito de multi-stage build no Docker para um dev backend pleno que já usa
Docker no dia a dia mas nunca otimizou o tamanho das imagens. Mostre um exemplo prático
com uma aplicação JavaScript, comparando o Dockerfile sem e com multi-stage build,
incluindo o tamanho final de cada imagem."

Enter fullscreen mode

Exit fullscreen mode

O que acontece internamente: O mecanismo de atenção se concentra em uma região muito específica, a interseção entre "Docker", "multi-stage build", "otimização de imagem" e "JavaScript". Os pesos de atenção ficam fortemente direcionados.

### 3 - Forneça Contexto Relevante

"Estado da aplicação"

Uma LLM éstatelesspor natureza, ela não tem memória entre requisições. Cada prompt é processado do zero, o único "estado" que ela tem é o que você coloca no prompt. Isso significa que todo contexto que você não fornece simplesmente não existe para o modelo.

Internamente, o contexto funciona como um sistema de pesos no mecanismo de atenção. Quando você adiciona informações, elas criam "âncoras" que influenciam a distribuição de probabilidades de todos os tokens subsequentes, é como se cada pedaço de contexto fosse um ímã que puxa a resposta para uma direção específica.

Exemplos:

Sem contexto:

"Revise meu código."

Enter fullscreen mode

Exit fullscreen mode

O que a LLM faz: Sem saber a linguagem, o framework, o nível do dev, o objetivo do código, o padrão do time ou o tipo de revisão esperada, ela vai fazer comentários genéricos: "adicione tratamento de erro", "use nomes mais descritivos", "considere adicionar testes".

Com contexto:

"Revise este endpoint Node.js com Express que lida com upload de arquivos para o S3.
O time usa ESLint + Prettier, então ignore estilo. O padrão do time é async/await com
try/catch e erros customizados. Endpoint em produção, recebe 200 uploads/min.
Foque em: memory leaks, tratamento de erros e uso correto do SDK do S3."

Enter fullscreen mode

Exit fullscreen mode

O que a LLM faz: Cada informação do prompt funciona como um filtro que elimina ruído e concentra a revisão: "Node.js com Express + upload para S3" ativa conhecimento específico sobre streams, buffers, multipart e AWS SDK. "ESLint + Prettier, ignore estilo" elimina os comentários possíveis que o linter já resolve. "async/await com erros customizados" faz o modelo pular sugestões que o time já aplica e focar em como estão sendo usadas. "Produção, 200 uploads/min" muda o peso de cada problema, um buffer não liberado que seria aceitável em dev vira um incidente crítico sob carga. "Foque em: memory leaks, erros, SDK S3" restringe a revisão a 3 eixos e ignora dezenas de outros tópicos.

Com base nisso, saber as limitações do modelo que você está usando, te ajuda também a entender até aonde você pode ir nas perguntas e inferências, então escolha a sua melhor IA, treine ela, faça as suas perguntas, teste, tente! ;)

É Lembre-se: a LLM não "pensa", ela calcula probabilidades!

# Considerações Finais

É isto, tentei resumir cada ponto que achei interessante abordar e explicar nessa primeira etapa, mas há muito mais sobre engenharia de prompt de LLM para falar, como técnicas mais clássicas de engenharia de prompts(Zero-shot prompting, Role prompting), técnicas mais avançadas(Chain-of-Thought (CoT), Prompt Chaining), são muitas camadas que tentarei destrinchar nos próximos artigos, esse é apenas o primeiro que traz a minha volta para a escrita de artigos após alguns bons anos. Espero que você caro leitor tenha entendido e aprendido algo. Obrigado por ler até aqui. ;)

Onde me encontrar:

Meu LinkedInMeu GitHub

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse