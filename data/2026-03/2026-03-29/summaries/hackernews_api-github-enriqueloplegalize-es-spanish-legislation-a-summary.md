---
title: GitHub - EnriqueLop/legalize-es: Spanish legislation as a Git repo — every law is a Markdown file, every reform a commit. 8,600+ laws. · GitHub
url: https://github.com/EnriqueLop/legalize-es
date: 2026-03-28
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-03-29T01:02:27.296075
---

# GitHub - EnriqueLop/legalize-es: Spanish legislation as a Git repo — every law is a Markdown file, every reform a commit. 8,600+ laws. · GitHub

# Legalize — España

## Descripción
- Legislación española almacenada como repositorio Git.  
- Cada ley es un archivo Markdown y cada reforma se registra como un commit.  
- Más de 8 600 leyes obtenidas del API de datos abiertos del BOE, con historial completo desde 1960.  

## Inicio rápido
- Clonar el repositorio: `git clone https://github.com/EnriqueLop/legalize-es.git`  
- Consultar el texto de un artículo: `grep -A 10 "Artículo 135" spain/BOE-A-1978-31229.md`  
- Ver cambios históricos: `git log --oneline -- spain/BOE-A-1978-31229.md`  
- Obtener el diff de una reforma específica: `git diff 6660bcf^..6660bcf -- spain/BOE-A-1978-31229.md`  

## Estructura de ficheros
```
spain/
├── BOE-A-1978-31229.md   # Constitución Española
├── BOE-A-1995-25444.md   # Código Penal
├── BOE-A-2015-11430.md   # Estatuto de los Trabajadores
├── BOE-A-2000-323.md     # Ley de Enjuiciamiento Civil
└── ... (8 600+ leyes)
```
- Cada archivo inicia con front‑matter YAML que incluye título, identificador, país, rango, fechas de publicación y última actualización, estado y fuente.  

## Qué incluye
- Constitución Española.  
- Leyes Orgánicas y ordinarias.  
- Reales Decretos‑ley y Reales Decretos Legislativos.  
- Cada reforma aparece como un commit con la fecha oficial de publicación y un mensaje que contiene el identificador y enlace a la fuente.  

## Fuente de datos
- Contenido extraído del API de Legislación Consolidada del BOE (dominio público).  
- El repositorio aporta estructura, control de versiones y metadatos, sin crear contenido original.  

## API
- Próximamente disponible en **legalize.dev** para búsqueda, filtrado, comparación de versiones y notificaciones de cambios.  

## Contribuir
- Informar errores o ausencias mediante *issues* indicando nombre de la ley, artículo y fuente oficial con la versión correcta.  

## Autor y licencia
- Creado por Enrique López.  
- Texto legislativo: dominio público (fuentes oficiales).  
- Metadatos y herramientas del repositorio: licencia MIT.  

## Estadísticas del repositorio
- 27 867 commits.  
- 79 estrellas, 1 observador, 2 forks.  
- No hay releases ni paquetes publicados.