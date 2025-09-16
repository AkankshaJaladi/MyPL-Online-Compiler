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
myopl/
│── app.py                  # Flask web runner
│── basic.py                # Core interpreter
│── shell.py                # CLI REPL
│── strings_with_arrows.py  # Error formatting
│── grammar.txt             # Language grammar
│── __pychche__/
    |__basic.cpython-313
    |__strings_with_arrows.cpython-313
│── templates/
  |__index.html
