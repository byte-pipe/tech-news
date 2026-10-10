---
title: Bun v1.4.3 | Bun Blog
url: https://bun.com/blog/bun-v1.4.3
date: 2026-10-10
site: tldr
model: llama3.2:1b
summarized_at: 2026-10-10T16:17:46.727633
---

# Bun v1.4.3 | Bun Blog

#### Install Bun

*   Curl: A command-line tool for retrieving and transferring data over the internet
*   npm: A package manager for Node.js
*   PowerShell: A shell command-line interface for Windows
*   Scoop: A package manager for Linux
*   Brew: A package manager for macOS
*   Docker: An application life cycle management tool that provides a consistent and standard model for containerization

#### Install Bun

To install Bun, follow these steps:

*   Use `curl` to download the `install` script from Bun's GitHub repository.
*   Execute the script using `bash`:
    ```bash
curl https://bun.sh/install | bash
```
*   Install Bun globally using `npm`:
    ```bash
npm install -g bun
```
*   Install Bun locally using `powershell`:
    ```powershell
powershell -c "irm bun.sh/install.ps1|iex"
```
    Follow the prompts to complete the installation.
*   You can install Bun using `scoop`:
    ```bash
scoop install bun
```
*   You can install Bun using `brew`:
    ```bash
brew tap oven-sh/bun
brew install bun
```
*   Docker pull the oven/bun image:
    ```docker
docker pull oven/bun
```
*   Run the oven/bun image as a container:
    ```docker
docker run --rm --init --ulimit memlock=-1:-1 oven/bun
```
### Upgrade Bun

To upgrade Bun, run the following command:

```bash
bun upgrade
```
#### bun check

Type check, then run: If there's a type error, your code doesn't run.

*   Download the `bash` script from Bun's GitHub repository.
*   Execute the script using `bash`:
    ```
curl https://bun.sh/install | bash
```
*   Make sure the script is executed as the root user.
```bash
sudo chmod +x ./user
```

**Error**

Bun does not emit JavaScript or .ts files, and it doesn't have a language server. Your editor will continue to use TypeScript.

**Type check**

Bun's type checker is significantly faster than TypeScript 7.0.2.
-   Check the `src/index.ts` file to see the error:

    ```
error: TS2322: Type 'string' is not assignable to type 'number'.
```

*   Run the `bash` script again:
    ```bash
./user
```