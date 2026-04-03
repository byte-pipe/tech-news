---
title: Engenharia de Prompt: Por Que a Forma Como Você Pergunta Muda Tudo(Um guia introdutório) - DEV Community
url: https://dev.to/fransborges/engenharia-de-prompt-por-que-a-forma-como-voce-pergunta-muda-tudoum-guia-introdutorio-3hb0
date: 2026-03-23
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-03-25T01:03:58.725010
---

# Engenharia de Prompt: Por Que a Forma Como Você Pergunta Muda Tudo(Um guia introdutório) - DEV Community

# Engenharia de Prompt: Por Que a Forma Como Você Pergunta Muda Tudo (Guia introdutório)

## Prefácio
- O conhecimento básico é essencial para usar LLMs de forma eficaz.  
- Muitos usuários, especialmente iniciantes em tecnologia, não sabem como as LLMs funcionam nem como formular perguntas adequadas.  
- O autor compartilha sua experiência em uma série de artigos; este é o primeiro.

## O que é uma LLM?
- Modelos de linguagem de máquina que utilizam deep learning para processar linguagem natural.  
- Estrutura simplificada: um arquivo com os pesos (conhecimento aprendido) e outro com o código de inferência.  
- Exemplos: ChatGPT, Claude e outros, capazes de escrever código, traduzir textos, gerar ideias, criar arquiteturas de produto, etc.  
- Respostas de alta qualidade dependem de perguntas bem formuladas (referência à “camada -17”).

## Fazendo Perguntas – Engenharia de Prompt
- Engenharia de Prompt: ciência empírica de planejar, criar e testar prompts para melhorar respostas de LLMs.  
- Perguntas corretas aumentam a produtividade e a utilidade das respostas.

### 1. Evite a Ambiguidade
- Prompts vagos deixam o modelo escolher entre múltiplas interpretações, resultando em respostas genéricas.  
- **Exemplo ambíguo:** “Crie uma API.” → pode gerar REST, GraphQL, diferentes linguagens, etc.  
- **Exemplo claro:** especificar linguagem, framework, endpoints, tipos de payload, validações, logs, códigos de status, tratamento de falhas, etc.  
- Detalhes funcionam como restrições que concentram a distribuição de probabilidade, reduzindo opções indesejadas.

### 2. Delimite o Escopo
- LLMs têm janela de contexto limitada; tokens irrelevantes competem por atenção.  
- **Prompt amplo:** “Me ensine Docker.” → resposta superficial cobrindo muitos subtópicos.  
- **Prompt focado:** definir objetivo específico, público-alvo, tecnologia de apoio e exemplos concretos (ex.: multi‑stage build para dev backend pleno com exemplo em JavaScript).  
- O escopo delimitado direciona a atenção para a interseção de termos relevantes.

### 3. Forneça Contexto Relevante
- LLMs são stateless; só consideram o que está incluído no prompt.  
- Contexto atua como âncoras que guiam a geração de tokens.  
- **Sem contexto:** “Revise meu código.” → comentários genéricos.  
- **Com contexto:** indicar linguagem, framework, padrões da equipe, objetivo da revisão, nível do desenvolvedor, etc., produz feedback preciso e alinhado às necessidades.

## Considerações Finais
- Dominar a formulação de prompts eleva a qualidade das interações com LLMs.  
- Aplicar consistentemente os três princípios (evitar ambiguidade, delimitar escopo, fornecer contexto) gera respostas mais precisas, úteis e produtivas.  
- A prática contínua e a atenção aos detalhes são fundamentais para aproveitar todo o potencial das LLMs.