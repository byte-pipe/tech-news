---
title: 'GitHub - EnriqueLop/legalize-es: Spanish legislation as a Git repo — every law is a Markdown file, every reform a commit. 8,600+ laws. · GitHub'
url: https://github.com/EnriqueLop/legalize-es
site_name: hackernews_api
content_file: hackernews_api-github-enriqueloplegalize-es-spanish-legislation-a
fetched_at: '2026-03-29T01:01:13.027516'
original_url: https://github.com/EnriqueLop/legalize-es
author: enriquelop
date: '2026-03-28'
description: Spanish legislation as a Git repo — every law is a Markdown file, every reform a commit. 8,600+ laws. - EnriqueLop/legalize-es
tags:
- hackernews
- trending
---

EnriqueLop

 

/

legalize-es

Public

* NotificationsYou must be signed in to change notification settings
* Fork2
* Star79

 
 
 
 
master
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

27,867 Commits
27,867 Commits
spain
spain
 
 
README.md
README.md
 
 
View all files

## Repository files navigation

# Legalize — España

Legislación española como repositorio Git. Cada ley es un fichero Markdown, cada reforma un commit.

Más de 8.600 leyes delAPI de datos abiertos del BOE, con historial completo de reformas desde 1960.

Parte del proyectoLegalize.

## Inicio rápido

git clone https://github.com/EnriqueLop/legalize-es.git

cd
 legalize-es

#
 ¿Qué dice el Artículo 135 de la Constitución hoy?

grep -A 10 
"
Artículo 135
"
 spain/BOE-A-1978-31229.md

#
 ¿Cuándo cambió?

git log --oneline -- spain/BOE-A-1978-31229.md

#
 Diff exacto de la reforma de estabilidad presupuestaria de 2011

git diff 6660bcf^..6660bcf -- spain/BOE-A-1978-31229.md

## Estructura de ficheros

spain/
├── BOE-A-1978-31229.md # Constitución Española
├── BOE-A-1995-25444.md # Código Penal
├── BOE-A-2015-11430.md # Estatuto de los Trabajadores
├── BOE-A-2000-323.md # Ley de Enjuiciamiento Civil
└── ... (8.600+ leyes)

Cada fichero empieza con frontmatter YAML:

---

titulo
: 
"
Constitución Española
"

identificador
: 
"
BOE-A-1978-31229
"

pais
: 
"
es
"

rango
: 
"
constitucion
"

fecha_publicacion
: 
"
1978-12-29
"

ultima_actualizacion
: 
"
2024-02-17
"

estado
: 
"
vigente
"

fuente
: 
"
https://www.boe.es/eli/es/c/1978/12/27/(1)
"

---

## Qué incluye

Toda la legislación consolidada clasificada como "estatal" del BOE:

* Constitución Española
* Leyes Orgánicas
* Leyes ordinarias
* Reales Decretos-ley
* Reales Decretos Legislativos

Cada reforma es un commit independiente con la fecha oficial de publicación como fecha de autoría. El mensaje del commit incluye el identificador de la reforma y un enlace a la fuente oficial.

## Fuente de datos

Todo el contenido proviene delAPI de Legislación Consolidada del BOE. El texto legislativo es de dominio público. Este repositorio añade estructura, control de versiones y metadatos — no contenido original.

## API

¿Buscas acceso programático? La API de Legalize estará disponible próximamente enlegalize.dev— busca, filtra, compara versiones y recibe notificaciones cuando una ley cambie.

## Contribuir

¿Has encontrado un error en un texto consolidado? ¿Falta alguna reforma? Abre un issue indicando el nombre de la ley, el artículo y la fuente oficial con la versión correcta.

## Autor

Creado porEnrique Lopez.

## Licencia

Contenido legislativo: dominio público (fuentes oficiales del gobierno).

Estructura del repositorio, metadatos y herramientas:MIT.

Un proyecto deEnrique Lopez· Con tecnología deBoletinClaro.es·legalize.dev

## About

Spanish legislation as a Git repo — every law is a Markdown file, every reform a commit. 8,600+ laws.

### Resources

 Readme

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

79

 stars
 

### Watchers

1

 watching
 

### Forks

2

 forks
 

 Report repository

 

## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors0

 No contributors