---
title: 'Programação Criativa: Vamos desenhar com código? - DEV Community'
url: https://dev.to/he4rt/programacao-criativa-vamos-desenhar-com-codigo-4a1
site_name: devto
content_file: devto-programação-criativa-vamos-desenhar-com-código-dev
fetched_at: '2026-08-07T11:44:04.645260'
original_url: https://dev.to/he4rt/programacao-criativa-vamos-desenhar-com-codigo-4a1
author: Sara Aniceto
date: '2026-08-02'
description: Quem acha que a discussão entre arte gerada por computadores começou com a popularização das... Tagged with creativecoding, p5js, braziliandevs.
tags: '#creativecoding, #p5js, #braziliandevs'
---

Reconnecting developers with fun visual hobbies

Quem acha que a discussão entre arte gerada por computadores começou com a popularização das ferramentas de IA provavelmente perdeu boa parte das discussões envolvidas em arte generativa, arte computacional e design paramétrico que surgiram ainda no século passado. A Programação Criativa, que vamos entender melhor nesse artigo, é uma das formas possíveis de gerar arte a partir de algoritmos que vai muito além de mandar um prompt pra IA e esperar sua arte ser gerada. É construção, linha a linha, onde o programador faz da tela do computador e das linhas de código seu papel e pincel. Vem comigo entender melhor como usar suas habilidades de desenvolvimento para se divertir, experimentar e deixar a criatividade rolar solta.

## O que é Programação Criativa?

Uma das coisas mais legais que ouvi me adentrando nos estudos decreative coding(termo em inglês para programação criativa) é que existem muitas pessoas que programam, mas que não são necessariamente "programadoras". A programação não precisa estar presa apenas à sua carreira, ela pode ser uma paixão, um hobby ou um playground lúdico.

A Programação Criativa é exatamente isso: usar o código para desenhar, criar animações e "brincar" com o computador. Em vez de focar apenas na criação de sistemas ou análise de dados o objetivo aqui é a exploração visual.

Você consegue acreditar que a imagem acima foi gerada com 0 linhas de um código Java? Em seguida vou te explicar melhor sobre o Processing e outras ferramentas de programação criativa.

## Processing e p5.js: Onde o desenho encontra o algoritmo

Processing e o p5.js são duas das ferramentas mais populares criadas para facilitar o contato de artistas, ilustradores, designers e pessoas não programadoras em geral que queiram criar arte usando código.

A lógica entre eles é a mesma, o que muda são especificidades da sintaxe de cada linguagem.

* Processing: Criado em 2001, é baseado em Java e é o "pai" de tudo isso. É um software gratuito, no formato de IDE, no qual você consegue escrever, executar e compilar os seus códigos, ou melhor suas obras (aqui chamadas desketches).
* p5.js: É uma versão do Processing baseada em JavaScript, mais popular atualmente e feita para rodar direto na web.

Hoje em dia também é possível usar o modelo do Processing baseado em Python e para a criação de aplicativos Android. O mais importante é entender que, enquanto no Photoshop você usa o mouse para desenhar, aqui você começa a desenhar escrevendo em uma página em branco.

## A Anatomia Básica do Código (Para quem já coda entender)

Diferente de um script tradicional, a estrutura básica nessas ferramentas é muito simples e visual:

1. setup(): É a função que roda uma única vez assim que o programa inicia. É aqui que você define configurações importantes da sua arte, como o tamanho do seu "papel" (canvas).
2. draw(): Aqui é onde a mágica acontece. Essa função é umloop infinito. Ela é lida ciclicamente enquanto o programa roda. Se você desenhar algo aqui, pode criar animações ou responder a eventos, como o movimento do mouse.

Com essa estrutura pronta, vale acessar a documentação e entender as inúmeras possibilidades de formas, elementos tipográficos, animações, etc que é possível criar com essas ferramentas. Esse pedaço de código abaixo é o que gerou a imagem que eu mostrei no início do artigo.

void
 
draw
(){

 
background
(
255
);

 
fill
(
0
);

 
noStroke
();

 
float
 
tiles
 
=
 
mouseX
/
10
;

 
float
 
tileSize
 
=
 
width
/
tiles
;

 
translate
(
tileSize
/
2
,
tileSize
/
2
);

 
for
(
int
 
x
 
=
 
0
;
 
x
 
<
 
tiles
;
 
x
++){

 
for
(
int
 
y
 
=
 
0
;
 
y
 
<
 
tiles
;
 
y
++){

 
//Picks the color based on the pixel, in which the pixel is the size of the tiles

 
color
 
c
 
=
 
img
.
get
(
int
(
x
*
tileSize
),
int
(
y
*
tileSize
));

 
float
 
size
 
=
 
map
(
brightness
(
c
),
255
,
0
,
0
,
20
);

 
ellipse
(
x
*
tileSize
,
y
*
tileSize
,
size
,
size
);

 
};

 
};

}

Enter fullscreen mode

Exit fullscreen mode

## Uma ferramenta visual de aprendizado de programação

É possível que você ainda não tenha sido convencido de explorar o Processing e a programação criativa para despertar o lado artista que mora em você? Se sim, eu te faço uma pergunta: quando é que você parou de desenhar e virou um adulto chato sem criatividade?

Brincadeiras à parte, talvez então você seja convencido de que a programação criativa pode também servir como um facilitador para o aprendizado técnico porque transforma conceitos abstratos (como laços de repetição e condicionais) em resultados visuais e imediatos na sua tela.

É como um "debug visual". Afinal, ver umfor loopgerando 100 bolinhas coloridas na sua tela em tempo real é a melhor forma de "debugar" sua lógica mental.

## Conclusão: Experimente!

Se você sente que a programação às vezes fica um pouco "rígida" ou mecânica demais, tente criar um sketch no Processing ou p5.js. É uma forma de usar sua lógica para algo puramente estético e divertido.

Abaixo deixo alguns links para encontrar referências de projetos, materiais gratuitos e comunidades pra quem quiser conhecer mais:

* OpenProcessing: Plataforma de hospedagem de projetos em Processing, é o GitHub da Programação Criativa
* Curso gratuito de Programação Criativa: Repositório no GitHub de curso por Monica Rizzolli e Alexandre Villares
* Código Transcendente : Uma introdução prática à programação e arte gerativa: Livro de Mateus Paresqui Berruezo
* Compoética- Encontro Brasileiro de Programação Criativa
* Comunidade de Programação Criativa no Brasil no Telegram

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse