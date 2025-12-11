# Advent of Code

This repository contains solutions to [**Advent of Code**](https://adventofcode.com/),
an annual series of programming puzzles released each December. Each event
consists of 25 days of challenges, with two parts per day, increasing in
difficulty and covering a wide range of problem-solving skills.

The goal of this project is to explore different problem-solving approaches and
keep a record of progress over time. Code may be written in various languages
depending on the problem or experimentation.

For more information about Advent of Code and the yearly challenges, visit the
official site.

## Running solutions

Each solution folder contains a small `Makefile` that allows every problem to
be run with a single command, regardless of the programming language used.

This system keeps each solution runnable with a single, unified command, no
matter the language.

### How it Works

Solutions may be written in many languages (Python, JavaScript/Node.js, Rust,
Go, C/C++, Java, etc.). Every solution directory includes a unified `Makefile`
that automatically detects the language based on common files:

- `main.py` → Python
- `index.js` → JavaScript/Node.js
- `Cargo.toml` → Rust
- `main.go` → Go
- `main.c` → C
- `main.cpp` → C++
- `main.java` → Java

Once inside a solution folder, simply run:

```sh
make run
```

The Makefile will:

1. Detect which language is present
2. Build/compile if necessary
3. Run the solution using the appropriate command

### Cleaning Build Artifacts

If a language creates compiled files (e.g., C, C++, Java), clean them with:

```sh
make clean
```
