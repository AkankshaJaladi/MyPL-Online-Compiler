# MyPL-Online-Compiler
An online compiler and interpreter for MyOPL – a custom programming language built in Python with Flask.
MyPL is a lightweight programming language interpreter built from scratch in Python.
It supports variables, math operations, control structures, functions, lists, and built-in functions.

# Features

Variables: VAR x = 10

Math: + - * / ^

Conditionals: IF ... ELIF ... ELSE ... END

Loops: FOR ... TO ... STEP ... END, WHILE ... END

Functions: FUN name(args) -> expr or multiline with END

Lists: [1, 2, 3] with APPEND, POP, EXTEND, LEN

Built-ins: PRINT, INPUT, CLEAR, type checks, RUN to execute scripts

## Syntax Reference
The language syntax is formally defined in 'grammar.txt' file.

## Project Structure
mypl/
│── app.py                  # Flask web runner (backend for the online compiler)
│── basic.py                # Core interpreter (lexer, parser, runtime, built-ins)
│── shell.py                # CLI REPL (interactive terminal for MyOPL)
│── strings_with_arrows.py  # Error formatting for syntax/runtime errors
│── grammar.txt             # Formal grammar definition of MyOPL language
│── __pycache__/            # Python cache files (auto-generated, can be ignored)
│   ├── basic.cpython-313.pyc          # Compiled bytecode of basic.py
│   └── strings_with_arrows.cpython-313.pyc  # Compiled bytecode of strings_with_arrows.py
│── templates/              # HTML templates for Flask web app
│   └── index.html          # Frontend webpage for running MyOPL code
