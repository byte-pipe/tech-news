---
title: Chess in Pure SQL - DB Pro Blog
url: https://www.dbpro.app/blog/chess-in-pure-sql
site_name: hnrss
content_file: hnrss-chess-in-pure-sql-db-pro-blog
fetched_at: '2026-04-01T19:28:18.591714'
original_url: https://www.dbpro.app/blog/chess-in-pure-sql
author: Jay
date: '2026-03-29'
published_date: '[object Object]'
description: What if I told you SQL could play chess? No JavaScript, no frameworks - just pure SQL rendering a full chess board in your browser.
tags:
- hackernews
- hnrss
---

What if I told you SQL could play chess?

Not "store chess moves in a database." Not "track game state in a table." Actually render a chess board. With pieces. That you can move around. In your browser. Using nothing but SELECT, UPDATE, and a bit of creative thinking.

Loading chess board...

No JavaScript. No frameworks. Just SQL.

Let's build it.

## The Board

First, we need to represent the chess board. A chess board is an 8x8 grid. Each square can either be empty or contain a piece. That's just a table:

⚡
Loading SQL environment...

We've got 32 rows - one for each piece on the starting board. But that's not very... chess-like. We want to see an actual board.

## The Magic: Pivoting Rows into a Grid

Here's where it gets interesting. SQL doesn't naturally output grids - it outputs rows. But we cantransformrows into columns using a technique calledconditional aggregation.

The idea: GROUP BY the rank (row), and for each file (column), use a CASE statement inside MAX() to pick out the piece:

⚡
Loading SQL environment...

There it is. A chess board. Rendered entirely in SQL.

Let's break down what's happening:

1. The CTE(WITH full_board AS ...) generates all 64 squares by cross-joining ranks 1-8 with files 1-8, then LEFT JOINs our pieces
2. The pivotusesMAX(CASE WHEN file = N THEN piece END)to extract each column's piece
3. COALESCEfills empty squares with·so we can see the grid structure
4. ORDER BY rank DESCputs rank 8 at the top (black's back rank), like a real board

## Making Moves

Now for the fun part. To move a piece, we just UPDATE the board:

⚡
Loading SQL environment...

Both pawns have advanced! The most common chess opening, executed in pure SQL.

## Your Turn: The Sandbox

Here's a fully set up board. Try making some moves yourself. Some ideas:

* Play the Italian Game: 1. e4 e5 2. Nf3 Nc6 3. Bc4
* Try the Queen's Gambit: 1. d4 d5 2. c4
* Set up a checkmate position
* Or just mess around!

Remember:

* Files: a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8
* DELETE the piece from its starting square, INSERT it at the destination
* For captures, DELETE both the moving piece AND the captured piece first

⚡
Loading SQL environment...

## The Opera Game: A Chess Masterpiece in SQL

Let's replay one of the most famous chess games ever played. In 1858, Paul Morphy played against the Duke of Brunswick and Count Isouard at the Paris Opera (during a performance of The Barber of Seville, no less).

It's a beautiful demonstration of rapid development and tactical brilliance. Let's watch it unfold in SQL.

Morphy has developed his pieces aggressively, targeting the weak f7 pawn:

⚡
Loading SQL environment...

Morphy sacrificed his bishop, but now his knight joins the attack with devastating effect:

⚡
Loading SQL environment...

The finale is stunning. Morphy plays Rd8+, and when the Queen takes the rook, the other rook delivers checkmate:

⚡
Loading SQL environment...

The white rook on d8 delivers checkmate. The bishop on f8 blocks the king's escape, and the knight on b5 covers d6. A masterpiece then, a masterpiece now - rendered in SQL.

## Wrapping Up

We just built a fully playable chess board in pure SQL. No JavaScript. No frameworks. Just:

* A simple table with rank, file, and piece
* A clever pivot query using conditional aggregation
* DELETE and INSERT to move pieces

The same pivot technique works for any grid-based visualization - calendars, seating charts, game boards, heatmaps. SQL is more expressive than most people give it credit for.

Now if you'll excuse me, I have a rematch against a database to prepare for.

Jay

## Keep Reading

### Getting Started with SQL: A Hands-On Tutorial

Learn SQL by doing. This interactive tutorial covers SELECT, INSERT, UPDATE, DELETE, JOINs, and aggregations - everything you need to start working with databases.

December 10, 2025
