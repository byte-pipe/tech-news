---
title: O que uma usina nuclear tem a ver com o seu processo de QA? - DEV Community
url: https://dev.to/he4rt/o-que-uma-usina-nuclear-tem-a-ver-com-o-seu-processo-de-qa-103j
site_name: devto
content_file: devto-o-que-uma-usina-nuclear-tem-a-ver-com-o-seu-proces
fetched_at: '2026-04-07T11:23:31.796196'
original_url: https://dev.to/he4rt/o-que-uma-usina-nuclear-tem-a-ver-com-o-seu-processo-de-qa-103j
author: Alicia Marianne 🇧🇷
date: '2026-04-05'
description: A gente sabe que testar e validar um software antes de ir para produção é importante. Mas você já... Tagged with braziliandevs, testing, qa, software.
tags: '#braziliandevs, #testing, #qa, #software'
---

A gente sabe que testar e validar um software antes de ir para produção é importante. Mas você já parou para pensar no peso real que isso carrega?

Recentemente, estava revendo a sérieChernobyl, e ela me fez refletir sobre muita coisa — especialmente sobre a forma como encaro minha área, sendo QA, e sobre a responsabilidade que ela traz. Resolvi compartilhar isso com vocês.

Para quem não conhece,Chernobylé uma minissérie dramática lançada em 2019 que retrata o desastre nuclear ocorrido na usina de mesmo nome, na então União Soviética, em 26 de abril de 1986. A história acompanha os eventos logo após a explosão do reator número 4 — o caos, as tentativas do governo soviético de esconder a gravidade do acidente e o enorme esforço de cientistas, bombeiros, militares e trabalhadores que arriscaram, e muitas vezes perderam, suas vidas para evitar uma catástrofe ainda maior. A série também segue o cientista Valery Legasov, que tenta descobrir a verdadeira causa do acidente e expor a verdade por trás da tragédia.

Mas o ponto aqui vai além da série.

O que mais me chamou atenção foi o quanto aquela tragédia conversa com algo que vivemos diariamente no desenvolvimento de software:a responsabilidade nas decisões.

## O que aconteceu em Chernobyl?

Mesmo sabendo que existem elementos dramatizados, dá para aprender muita coisa com esse desastre. Não sou física nuclear, mas vou tentar resumir o que aconteceu — porque foi justamente essa parte que mais me fez refletir sobre responsabilidade e tomada de decisão.

Na madrugada do dia26 de abril de 1986, os operadores da usina realizavam umteste de segurança no reator 4. O objetivo era validar se, em caso de queda de energia, as turbinas ainda conseguiriam gerar eletricidade por alguns segundos — tempo suficiente até que os geradores de emergência fossem acionados. No papel, o teste parecia simples.

O problema é que, para executá-lo, diversos sistemas de segurança foram desativados e a potência do reator foi reduzida para um nível muito abaixo do ideal. Foi aí que tudo começou a sair do controle.

O reator utilizado era do tipoRBMK, um modelo com uma falha crítica de projeto: em determinadas condições, quanto mais vapor era gerado dentro do sistema, maior ficava a potência do reator. Em vez de estabilizar, ele se tornava cada vez mais instável. Para piorar, o teste foi conduzido sob forte pressão da liderança, mesmo diante de sinais claros de que não era seguro continuar.

Ao longo da série, vemos os próprios operadores levantando preocupações — que foram ignoradas. Quando perceberam que a situação era crítica, acionaram o botão de desligamento de emergência. Em teoria, esse comando deveria encerrar a reação. Mas, por uma falha no design das barras de controle, o efeito inicial foi o oposto: a potência disparou. Em poucos segundos, temperatura e pressão subiram de forma descontrolada.

O resultado foram duas explosões que destruíram o topo do reator, expuseram o núcleo à atmosfera e liberaram uma enorme quantidade de material radioativo. O incêndio que se seguiu espalhou radiação por boa parte da Europa, transformando Chernobyl no maior desastre nuclear da história.

O que mais me impactou foi perceber que a tragédia não aconteceu por um único erro. Ela foi consequência de umacadeia de decisões ruins: falhas técnicas ignoradas, riscos mal avaliados e pessoas que não foram ouvidas.

## E o que isso tem a ver com software?

Depois de assistir à série, comecei a fazer um paralelo com a nossa área. Porque, no fim, quantas vezes um incidente em produção também não nasce da mesma forma?

Nem sempre o problema vem de um único bug. Muitas vezes, ele é o resultado de uma sequência de decisões tomadas sem o devido cuidado: um requisito mal definido, um risco não mapeado, uma validação superficial, uma entrega apressada — ou um alerta levantado pelo time que acabou sendo ignorado.

Foi aí que a série me fez enxergar algo que vai além do contexto dela:quando a pressa fala mais alto do que a análise, o custo quase sempre aparece depois.

## O maior problema: risco tratado de forma rasa

Um dos maiores desafios que vejo hoje no desenvolvimento de software é justamente o planejamento e o levantamento de riscos feitos de maneira superficial.

Tenho certeza de que você vai concordar: não tem coisa pior do que refazer algo ou ficar apagando incêndios que poderiam ter sido discutidos antes.

Vivemos num mundo onde tempo é dinheiro. E é exatamente por isso que qualidade precisa estar presente desde o início — não como uma etapa final, mas como parte do processo.

Como QA, vou compartilhar duas coisas que considero essenciais.

### Ouça sua equipe

Independentemente da sua posição no time, ouça as pessoas ao seu redor.

Ninguém conhece melhor o produto do que quem o construiu, testou e convive com ele diariamente. Antes de uma nova funcionalidade entrar ou de um teste ser executado, converse com o time.

Escute quem desenvolveu. Escute o produto. Escute suporte. Escute quem está mais próximo do usuário.

Muitas vezes, o risco já foi identificado por alguém. Ele só não foi ouvido.

### Analise antes de agir

Entender o impacto de uma mudança não é só uma questão técnica — é também uma questão de negócio.

Por exemplo: você vai melhorar a query de uma API. Em teoria, isso pode não alterar nenhuma regra de negócio. Mas como isso afeta o usuário final? A performance realmente melhorou? Existe algum impacto colateral? Como vamos medir se essa mudança foi positiva ou negativa?

Nem toda melhoria técnica gera melhoria de produto. E esse olhar crítico é parte fundamental do papel de QA.

## Conclusão

No fim,Chernobylme fez refletir sobre algo que vai muito além de uma série:a responsabilidade por trás de cada decisão que tomamos no dia a dia.

A gente não está lidando com um reator nuclear. Mas ainda assim lida com impacto real — no usuário, no negócio e no próprio time. Um risco ignorado, um teste mal planejado ou uma decisão tomada sem ouvir a equipe podem não gerar uma catástrofe, mas certamente geram problemas que poderiam ter sido evitados com mais atenção, diálogo e análise.

Para mim, ser QA vai muito além de encontrar bugs.

É questionar antes que o problema aconteça. É analisar cenários com olhar crítico. É antecipar riscos. É provocar conversas importantes dentro do time. É ajudar a construir decisões mais seguras e conscientes.

No final, qualidade não é apenas sobre software funcionando.

É sobre responsabilidade, colaboração e cuidado com tudo aquilo que criamos.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse