---
title: 'GitHub - imtomt/ymawky: MacOS Web Server written entirely in ARM64 assembly · GitHub'
url: https://github.com/imtomt/ymawky
site_name: hackernews_api
content_file: hackernews_api-github-imtomtymawky-macos-web-server-written-entir
fetched_at: '2026-05-10T11:50:24.403614'
original_url: https://github.com/imtomt/ymawky
author: imtomt
date: '2026-05-10'
description: MacOS Web Server written entirely in ARM64 assembly - imtomt/ymawky
tags:
- hackernews
- trending
---

imtomt

 

/

ymawky

Public

* NotificationsYou must be signed in to change notification settings
* Fork2
* Star142

 
 
 
 
main
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

95 Commits
95 Commits
docs
docs
 
 
err
err
 
 
src
src
 
 
www
www
 
 
.gitignore
.gitignore
 
 
COPYING
COPYING
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
build_err_pages.sh
build_err_pages.sh
 
 
View all files

## Repository files navigation

# ymawky-- web server in ARM assembly

This isymawky(yuh maw kee), a web server written entirely in ARM64 assembly. ymawky is a syscall-only, no libc, fork-per-connection web server written by hand. While it is developed for MacOS, I've tried to make it as portable as possible --however, it's likely you will still need to make some(hopefully minor)Significant tweaks to get this to run on Linux/other Unix systems. SeeImplementation Notesfor more details.

## Building

Requires Xcode Command Line Tools. Install withxcode-select --install.
ymawky only runs on apple silicon (arm64).

Runmaketo build.

Ensure there is awww/directory next to theymawkyexecutable. That's the document root whereymawkysearches for files.GETwith an empty filename (GET /) will search forwww/index.html, so you might want to make sure there's anindex.htmlas well.

ymawkywill try to serve static error pages when a client's request results in error, eg 404. The pages it searches for inerr/(code).html, so ensureerr/exists alongisdeymawkyandwww/.
SeeConfigurationto modify the default file and docroot.

## Running

* ./ymawkyto start running the web server on127.0.0.1:8080.
* ./ymawky [port]to start running the web server on127.0.0.1:[port]
* ./ymawky [literally-any-character-other-than-0-9]to start running the web server on 127.0.0.1:8080 in debug mode. Debug mode disables forking, and makes ymawky only handle one request. (I needed to do this becauselldbwasn't letting me debug the children, ugh.)

Unfortunately, while custom ports are supported, custom addresses are not. as of right now, ymawky can only run on127.0.0.1. This is solely because I haven't implemented it -- but if you'd like to consider this a safety feature, then I guess it could be intentional.

To see ymawky in action, start running ymawky with./ymawky [port]. Then open your web browser of choice (or use curl), and visit127.0.0.1:8080/or127.0.0.1:8080/pretty/index.html. Bask in the warmth of assembly.

## What can it do?

ymawky is a static-file web server. It doesn't support server-side code to generate content on-the-fly, or more advanced URL parsing, such as/search?query=term. That's not to say it's non-functional, though.

* Supported HTTP methods:GETPUTDELETEOPTIONSHEAD
* GET
* PUT
* DELETE
* OPTIONS
* HEAD
* Basic protection from slowloris-like Denial of Service attacks
* Decodes % hex encoding, eg,%20decodes to a space in filenames, and%61decodes toa
* Smart path traversal detection and prevention. Blocks..from traversing paths, while not disallowing multiple periods when they're part of a file:GET /../../../etc/passwd->403 ForbiddenGET /ohwell...txt->200 OKGET /../src/ymawky.S->403 ForbiddenGET /hehe..txt->200 OK
* GET /../../../etc/passwd->403 Forbidden
* GET /ohwell...txt->200 OK
* GET /../src/ymawky.S->403 Forbidden
* GET /hehe..txt->200 OK
* Automatically prependswww/to requested files.GET /index.htmlwill retrievewww/index.html
* EmptyGET /requests default toGET www/index.html
* PUTrequests support uploads of up to 1GiB, though this can be configured for larger files
* PUTis atomic due to writing to a temporary file then renaming, allowing concurrentPUTrequests without leaving partially-written files
* Content-Length:parsing and verification inPUTrequests
* MIME type detection, givingContent-Typein the response header with the corresponding MIME type
* AcceptsRange: bytes=ranges in GET requests, supporting full rangesbytes=X-N, suffix rangesbytes=-N, and open-ended rangesbytes=X-. Video scrubbing is well supported
* Basic HTTP version parsing. Requests need to specifyHTTP/1.1orHTTP/1.0, and if requestingHTTP/1.1, aHost:field needs to be present in the header. Currently, ymawky doesn't do anything with Host, but per RFC 9112 Section 3.2, the Header must be sent
* Serves custom HTML pages for error codes, such as 404, or 500. Look in theerr/directory for an example
* If the requested resource is a directory, list all files and subdirs in the directory. Note that this excludes www/ (or whatever your docroot is): GET / will always search for index.html if no file is given.

## "Safety"

This is a web server written entirely by-hand in ARM64 assembly as a fun project. It's probably got a lot of vulnerabilities I'm unaware of. However, I did do my best to make it safer. Here are some safety precautions ymawky takes.

* Rejects paths >= PATH_MAX (4096 bytes)
* Reject any paths that include path traversal --/../..
* Reject any requests that do not contain a path within 16 bytes
* Confined towww/. Any path requested getswww/prepended to it
* Rejects any path containing symlinks, with O_NOFOLLOW_ANY
* PUT writes to a temporary file,www/.ymawky_tmp_<pid>. Upon successfully receiving the whole file, this temporary file is then renamed to the requested filename. This prevents partial or corrupted PUT requests from overwriting existing files.
* Reject any requests whose path starts withwww/.ymawky_tmp_. This prevents someone fromGETing a temporary file, and prevents someone from sendingPUT /.ymawky_tmp_4533or something.
* Must receive data within 10 seconds. If it's slower, the connection will close. If the entire header is not received within 10 seconds total, the connection will be closed. This is to prevent slowloris-like attacks.

## HTTP Status Codes

ymawky currently supports and can reply with the following status codes:

* 200 OK
* 201 Created
* 204 No Content
* 206 Partial Content
* 400 Bad Request
* 403 Forbidden
* 404 Not Found
* 408 Request Timeout
* 409 Conflict
* 411 Length Required
* 413 Content Too Large
* 414 URI Too Long
* 416 Range Not Satisfiable
* 418 I'm a teapot
* 431 Request Header Fields Too Large
* 500 Internal Server Error
* 501 Not Implemented
* 503 Service Unavailable
* 505 HTTP Version Not Supported
* 507 Insufficient Storage

Custom HTML pages will be served alongside the error codes (400+). These HTML files are located inerr/(code).html. You can usebuild_err_pages.shto create a page for each code, with different text at your leisure. Edit the source code ofbuild_err_pages.shto modify the text per-page, and modifyerr/template.htmlto modify the base template. Inerr/template.html:

* {{CODE}}- HTTP Code: eg, 404
* {{TITLE}}- Title text: eg, "Not Found"
* {{MSG}}- Custom message: eg, "the rats ate this page"

## MIME Types

MIME types are detected by analyzing the file extension. The following MIME types are recognized.

Web-related files:

* .html->text/html; charset=utf-8
* .htm->text/html; charset=utf-8
* .css->text/css; charset=utf-8
* .csv->text/csv; charset=utf-8
* .xml->text/xml; charset=utf-8
* .js->text/javascript; charset=utf-8
* .json->application/json
* .wasm->application/wasm
* .mjs->text/javascript; charset=utf-8
* .map->application/json

Image files:

* .png->image/png
* .jpg->image/jpeg
* .jpeg->image/jpeg
* .gif->image/gif
* .svg->image/svg+xml
* .ico->image/x-icon
* .webp->image/webp
* .avif->image/avif
* .bmp->image/bmp
* .tiff->image/tiff
* .apng->image/apng

Font files:

* .woff->font/woff
* .woff2->font/woff2
* .ttf->font/ttf
* .otf->font/otf

Document files:

* .txt->text/plain; charset=utf-8
* .pdf->application/pdf
* .doc->application/msword
* .docx->application/vnd.openxmlformats-officedocument.wordprocessingml.document
* .epub->application/epub+zip
* .rtf->application/rtf

Video files:

* .mp4->video/mp4
* .webm->video/webm
* .mkv->video/x-matroska
* .avi->video/x-msvideo
* .mov->video/quicktime

Audio files:

* .mp3->audio/mpeg
* .ogg->audio/ogg
* .wav->audio/wav
* .flac->audio/flac
* .aac->audio/aac
* .m4a->audio/mp4
* .opus->audio/opus

Archive files:

* .zip->application/zip
* .gz->application/gzip
* .tar->application/x-tar
* .7z->application/x-7z-compressed
* .bz2->application/x-bzip2
* .rar->application/vnd.rar

## Configuration

You can configure ymawky with theconfig.Sfile. The options are documented here.

* #define DEFAULT_DIR "www/"-- This is the docroot. Change it to wherever your HTML files are, relative to ymawky, or use an absolute path:#define DEFAULT_DIR "www/"#define DEFAULT_DIR "/Library/WebServer/Documents#define DEFAULT_DIR "./"
* #define DEFAULT_DIR "www/"
* #define DEFAULT_DIR "/Library/WebServer/Documents
* #define DEFAULT_DIR "./"
* #default ERR_DIR "err/"-- This is the directory in which ymawky will search for custom error HTML pages, eg,err/404.htmlorerr/500.html
* #define DEFAULT_FILE "index.html"-- This is the default file ymawky will serve when it receives an emptyGET / HTTP/1.1request
* .equ RECV_TIMEOUT, 10-- Number of seconds ymawky will wait to receive datta before closing the connection. If it's more thanRECV_TIMEOUTseconds betweenread()s, ymawky will close the connection with408 Request Timed Out
* .equ HEADER_REQ_TIMEOUT_SECS, 10-- Maximum number of seconds ymawky will wait to receive the full header before timing out. If it takes, longer than this to receive the header, ymawky will close the connection with408 Request Timed Out
* .equ PUT_GRACE_SECS, 5-- ymawky dynamically calculates a max-time-per-PUT based onContent-Length. The max time is defined asPUT_GRACE_SECS + Content-Length / PUT_MIN_BPS. This is the minimum grace period allowed if it calculates a file should take <1 second to upload
* .equ PUT_MIN_BPS, 1024 * 16-- Minimum bytes-per-second. Higher if you want to be stricter, smaller if you want to be more lenient. Since this uses the.equdirective, arithmetic is supported, and1024 * 16gets calculated at assembly time becoming16384or 16KB
* .equ MAX_BODY_SIZE, 1024 * 1024 * 1024-- Maximum bytes PUT allows for Content-Length. By default, 1GB (102410241024 = 1073741824 bytes). Files with a larger Content-Length larger than this will be rejected with413 Content Too Large
* .equ MAX_PROCS, 256-- Maximum number of concurrent proccesses ymawky is allowed to run. Since ymawky is a fork-per-connection server, you want to ensure ymawky doesn't exhaust your PID space. ymawky will reply with503 Service Unavailable

## Implementation Notes

ymawky is written for MacOS (sorry...). There are a few (well, more than afew) things that are MacOS-specific in this code that won't be portable.

* Syscalls on MacOS usex16for the number andsvc #0x80to call it. Linux usesx8andsvc #0.
* Error reporting is different. MacOS sets the carry flag on error, and putserrnoinx0. Linux returns a negative value inx0, like-ENOENT. Everb.cswould need to be replaced withcmp x0, #0/b.lt ..., and you'd negatex0to get errno.
* fork()works differently, MacOS puts 1 inx1in the child process, whereas Linux puts0inx0.
* SO_NOSIGPIPEdoesn't exist on Linux.
* O_NOFOLLOW_ANYis also MacOS-specific.
* renameatx_np()is also MacOS-specific. Linux hasrenameat2(), with different flag values.
* Struct layouts and offsets will differ. Thestat64struct,itimervalstruct, andsockaddr_instruct, will all need to be reconsidered.
* adr xN, foo@PAGE/add xN, xN, foo@PAGEOFFare Mach-O relocation operators. Linux ELF uses different syntax, like:pg_hi21:and:lo12:. Theadr_l,ldr_landstr_lmacros would need to be rewritten or replaced.
* My personal favorite :3 Signal handling works differently on Linux and MacOS. MacOS'ssigactionstruct contains asa_trampfield that the kernel jumps to before your handler. ymawky utilizessa_trampdirectlyas the handler itself, skipping the libc trampoline andsigreturnentirely. Since the handler only sends a 408 and exits, without needing to return, that's fine and works wonderfully without libc. Thesigactioncall would need to be rewritten for POSIX systems.

### Special Thanks:

* Bob Johnson
* Bob Johnson's Therapist

## About

MacOS Web Server written entirely in ARM64 assembly

### Resources

 Readme

 

### License

 GPL-3.0 license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

142

 stars
 

### Watchers

0

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

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Assembly87.0%
* HTML10.7%
* Other2.3%