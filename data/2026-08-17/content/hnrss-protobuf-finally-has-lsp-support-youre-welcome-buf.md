---
title: Protobuf finally has LSP support. You’re welcome. · Buf
url: https://buf.build/blog/protobuf-lsp
site_name: hnrss
content_file: hnrss-protobuf-finally-has-lsp-support-youre-welcome-buf
fetched_at: '2026-08-17T11:22:24.990009'
original_url: https://buf.build/blog/protobuf-lsp
date: '2026-08-16'
published_date: '2026-01-14'
description: Buf is proud to announce the first fully-featured, production-grade LSP server for Protobuf. The Language Server Protocol is the standard API for integrating language support into your favorite IDE or text editor, such as VSCode, IntelliJ, or Neovim. An LSP server provides the smarts that power go to definition, code completion, finding references, and semantics-aware syntax highlighting.
tags:
- hackernews
- hnrss
---

Buf is proud to announce the first fully-featured, production-grade LSP server for Protobuf.

TheLanguage Server Protocolis the standard API for integrating language support into your favorite IDE or text editor, such as VSCode, IntelliJ, or Neovim. An LSP server provides the smarts that power go to definition, code completion, finding references, and semantics-aware syntax highlighting.

Before today, Protobuf lacked the same LSP support other major programming languages enjoy. We don’t want to overstate our own work, butthis is a game-changer for Protobuf development: Protobuf now has modern IDE support for the first time, all powered by theBuf CLI.

At Buf, we believe that Protobuf is the best schema language, thanks to its established ecosystem of libraries and tools. Protobuf shouldn’t just be the smart choice; it should be the easiest choice too. This is why we’re releasing the Buf LSP server, as part of our family of tools that complete the Protobuf ecosystem, includingProtobuf-ES(used in Chromium!),Protovalidate,ConnectRPC, and theBuf Schema Registry. No matter your project or use-case, developing with Protobuf should be the easy,obviouschoice.

Here’s how you can try it out!

## Installing the Buf LSP

VSCodeis one of the most popular graphical editors available, and it has stellar LSP support (LSP originated with VSCode). To use the Buf LSP, just install theBuf extension. This will automatically use your installed version of theBuf CLI(which bundles the LSP server), or install one if you need it.

Neovimis Buf engineers’ favorite editor, and the Buf LSP works great with it, too. All you need to do is install the Buf CLI, and configure Neovim to use it as an LSP server.

1. Make sure you’ve installed thenvim-lspconfigrepository, which provides default LSP config options. Follow the instructionshere.
2. Addlspconfig.buf_ls.setup {}to your.nvimrc.

Alternatively, you can add the following somewhere ininit.lua(or another config file, if you like):

vim.
lsp
.
config
(
'buf-lsp'
, {

 cmd 
=
 { 
'buf'
, 
'lsp'
, 
'serve' 
},

 filetypes 
=
 { 
'proto' 
},

 root_markers 
=
 { 
'buf.yaml'
, 
'.git' 
},

})

Then, you can enable it withvim.lsp.enable('buf-lsp')in your.nvimrc.

Learn more about LSP and Neovimhere.

If you’re using another editor, first find out how LSP integration works, and just make sure thebuf lsp servecommand gets run to spawn the server.

## Leveraging our toolchain

Buf already maintains a Protobuf compiler frontend (the part that parses files and calls plugins, likeprotoc), which we callprotocompile. Our implementation isn’t just fully-compliant, but it is much faster and more flexible thanprotoc. Our compiler is so good that even Google is using it alongsideprotocin some parts of its massive codebase.

To build the Buf LSP, we’ve takenprotocompileto the next level. We’ve developed a brand-new,query-drivenfrontend which enables incremental compilation and much better diagnostics. For example, unlikeprotoc, we correctly diagnose a duplicaterepeatedmodifier:

error: encountered more than one type modifier

 --> testdata/parser/type/repeated.proto:23:14

 |

23 | repeated repeated M x4 = 4;

 | -------- ^^^^^^^^ help: consider removing this

 | |

 | first one is here

We designed a new AST and intermediate representation for precisely diagnosing these errors, instead of usingFileDescriptorProto. Its flexibility makes it easy for us to implement new language features as they are added to Protobuf, such as upcoming features in Editions 2024. It is also memory-efficient, so it can handle workspaces that include very large Buf modules.

## Our commitment

Our work on the Buf LSP is not done. We are always improving our diagnostics, and we’re planning to add more features to the LSP server, too:

* Addingimports as an automatic fix.
* Tighter integration withbuf.yaml(such as automatically importing modules).
* Code completion and reference lookup for custom options.
* Automatic suggestion of field/enum numbers.
* Dedicated Protovalidate support, including syntax highlighting for CEL snippets.

At Buf, we will always push the boundary of whatyoucan accomplish with Protobuf, enabling schema-driven development for all!

If you want help enforcing standards on your organization’s data,contact usto see if Buf can help. If building excellent developer tooling excites you, reach out atinfo@buf.build!