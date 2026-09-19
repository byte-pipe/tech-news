---
title: 'GitHub - docling-project/docling: Get your documents ready for gen AI · GitHub'
url: https://github.com/docling-project/docling
site_name: github
content_file: github-github-docling-projectdocling-get-your-documents-r
fetched_at: '2026-09-19T14:10:36.422015'
original_url: https://github.com/docling-project/docling
author: docling-project
description: Get your documents ready for gen AI. Contribute to docling-project/docling development by creating an account on GitHub.
---

docling-project

 

/

docling

Public

* NotificationsYou must be signed in to change notification settings
* Fork4.8k
* Star66.8k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

1,452 Commits
1,452 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.actor
.actor
 
 
.agents/
skills
.agents/
skills
 
 
.claude/
skills
.claude/
skills
 
 
.codex/
skills
.codex/
skills
 
 
.github
.github
 
 
.opencode/
skills
.opencode/
skills
 
 
.plans
.plans
 
 
docling
docling
 
 
docs
docs
 
 
packages
packages
 
 
perfs
perfs
 
 
scripts
scripts
 
 
tests
tests
 
 
.git-blame-ignore-revs
.git-blame-ignore-revs
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CITATION.cff
CITATION.cff
 
 
CLAUDE.md
CLAUDE.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
MAINTAINERS.md
MAINTAINERS.md
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
mkdocs.yml
mkdocs.yml
 
 
pyproject.toml
pyproject.toml
 
 
tach.toml
tach.toml
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

# Docling

## What is Docling ?

Docling simplifies document processing by parsing diverse formats — including advanced PDF understanding — and providing seamless integrations with the generative AI ecosystem.

## Features

* 🗂️ Parsing ofmultiple document formatsincluding PDF, DOCX, PPTX, XLSX, HTML, EPUB, Apple Pages, WAV, MP3, WebVTT, Box Notes, email formats (EML, MSG), images (PNG, TIFF, JPEG, ...), LaTeX, DocLang, plain text, and more
* 📑 Advanced PDF understanding incl. page layout, reading order, table structure, code, formulas, image classification, and more
* 🧬 A unified, expressiveDoclingDocumentrepresentation format
* ↪️ Variousexport formatsand options, including Markdown, HTML, WebVTT, DocLang,DocTagsand lossless JSON
* 📜 Support for several application-specific XML schemas includingDocLang,USPTOpatents,JATSarticles, andXBRLfinancial reports.
* 🔒 Local execution capabilities for sensitive data and air-gapped environments
* 🤖 Plug-and-playintegrationsincl. LangChain, LlamaIndex, Crew AI & Haystack for agentic AI
* 🔍 Extensive OCR support for scanned PDFs and images
* 👓 Support for several Visual Language Models, such as (GraniteDocling)
* 🎙️ Audio support with Automatic Speech Recognition (ASR) models
* 🔌 Connect to any agent using theMCP server
* 🌐 Run Docling as a service with theAPI server(docling-serve)
* 💻 Simple and convenient CLI

### What's new

* 🎬 Parsing of video files (MP4, AVI, MOV, MKV, and WebM) with an ASR transcript and representative keyframes
* 📄 Parsing of ODF (OpenDocument Format) files for text documents (.odt), spreadsheets (.ods), and presentations (.odp)
* 💼 Parsing of XBRL (eXtensible Business Reporting Language) documents for financial reports
* 📧 Parsing of email files (.eml,.msg)
* 📚 Parsing of EPUB (Electronic Publication) files for e-books
* 🍎 Parsing of Apple Pages (.pages) documents, both container generations (Pages 5+ and iWork '09)
* 📝 Parsing of plain-text files (.txt,.text) and Markdown supersets (.qmd,.Rmd)
* 📊 Chart understanding (Barchart, Piechart, LinePlot): convert them into tables or code and add detailed descriptions

### Coming soon

* 📝 Metadata extraction, including title, authors, references & language
* 📝 Complex chemistry understanding (Molecular structures)

## Quickstart

### 1. Install

pip install docling

Note:Python 3.9 support was dropped in docling version 2.70.0. Please use Python 3.10 or higher.

Works on macOS, Linux and Windows environments for both x86_64 and arm64 architectures.

Moredetailed installation instructionsare available in the docs.

## 2. Convert a document (CLI)

docling https://arxiv.org/pdf/2206.01062

This generates a .md file in the current directory containing structured document content.

You can also use 🥚GraniteDoclingand other VLMs via Docling CLI:

docling --pipeline vlm --vlm-model granite_docling https://arxiv.org/pdf/2206.01062

## 3. Python usage (recommended)

from
 
docling
.
document_converter
 
import
 
DocumentConverter

source
 
=
 
"https://arxiv.org/pdf/2408.09869"
 
# a document via a local path or URL

converter
 
=
 
DocumentConverter
()

result
 
=
 
converter
.
convert
(
source
)

print
(
result
.
document
.
export_to_markdown
()) 
# output: "## Docling Technical Report[...]"

More advancedusageandconfigurationoptions.

## Documentation

Check out Docling'sdocumentationfor details on
installation, usage, concepts, recipes, extensions, and more.

## Examples

Go hands-on with ourexamples,
demonstrating how to address different application use cases with Docling.

## Integrations

To further accelerate your AI application development, check out Docling's nativeintegrationswith popular frameworks
and tools.

## Get help and support

Please feel free to connect with us using thediscussion section.

## Technical report

For more details on Docling's inner workings, check out theDocling Technical Report.

## Contributing

Please readContributing to Doclingfor details.

## References

If you use Docling in your projects, please consider citing the following:

@techreport
{
Docling
,
 
author
 = 
{
Deep Search Team
}
,
 
month
 = 
{
8
}
,
 
title
 = 
{
Docling Technical Report
}
,
 
url
 = 
{
https://arxiv.org/abs/2408.09869
}
,
 
eprint
 = 
{
2408.09869
}
,
 
doi
 = 
{
10.48550/arXiv.2408.09869
}
,
 
version
 = 
{
1.0.0
}
,
 
year
 = 
{
2024
}

}

## License

The Docling codebase is under MIT license.
For individual model usage, please refer to the model licenses found in the original packages.

## LF AI & Data

Docling is hosted as a project in theLF AI & Data Foundation.

### IBM ❤️ Open Source AI

The project was started by the AI for knowledge team at IBM Research Zurich.