# Kattis Demos with Unit Testing

Demo solutions with unit testing for some problems from [https://open.kattis.com](https://open.kattis.com)

## Requirements

- Linux/Mac/WSL (Windows Subsystem Layer) bash terminal is preferred along with language specific tools (compiler/interpreter, etc.) properly installed
- On Windows g++ compiler is required to compile and run C and C++ code from command prompt
  - g++ compiler for Windows can be downloaded from [https://nuwen.net/mingw.html](https://nuwen.net/mingw.html); extract it into C:\ drive as shown in the instructions here: [https://nuwen.net/mingw.html#install](https://nuwen.net/mingw.html#install)

- pytest Python3 package for testing Python3 solutions

```bash
pip3 install -U pytest
pip3 install -U mypy
```

## Programming Languages

- demos are provided in the following several languages
- follow the instruction based on your language and operating system

## C++

- open a terminal on Mac/Linux/WSL or cmd prompt on Windows
- change working directory to a problem folder, e.g.

```bash
  cd cold/C++
```

- compile using g++ or use provided Makefile

```bash
  g++ -std=c++14 cold.cpp
  make
```

- run unit testing; user provided test cases
- on Mac/Linux, either run the program with test argument or use the provided Makefile

```bash
  ./a.out test
  make unit_test
```

- on Windows:

```bash
  a.exe test
```

- run kattis provided sample test cases e.g. if 1.in and 1.ans are sample test files:
- on Mac/Linux/WSL Terminal

```bash
  cat 1.in | ./a.out | diff - 1.ans
  make kattis_test
```

- on Windows cmd prompt:

```bash
  > type 1.in | a.exe > out1.txt
  > FC out1.txt 1.ans
```

## Python3

- open a terminal on Mac/Linux/WSL or cmd prompt on Windows
- change working directory to a problem folder, e.g.,

```bash
  cd cold/python3
```

- run unit tests; user provided test cases
- several different ways...

```bash
  python3 cold.py test
  python3 test_cold.py
  python3 test_unit_cold.py
  pytest # make sure pytest is installed
  python3 -m unittest
```

### Testing Python OOP solutions

- open terminal 
- change current working directory to OOP folder inside problem/python3 folder
- run the following commands

```bash
  mypy --strict <module>.py
  mypy --strict test_<module>.py
  pytest
  python3 -m unittest
  python3 test_<module>.py
```

- run kattis provided sample test cases e.g. if 1.in and 1.ans are sample test files

```bash
  cat 1.in | python3 cold.py | diff - 1.ans
```

- on Windows cmd prompt

```bash
  type 1.in | python3 cold.py > out1.txt
  FC out1.txt 1.ans
```

## NodeJS

- open a terminal on Mac/Linux/WSL or cmd prompt on Windows
- change working directory to a problem folder
- run unit testing with your own test cases
- uses Jest Unit Testing Framework
- run the following commands on a Terminal

```bash
  cd cold
  npm install
  npm run jest
  npm run kattis_test
```

- run kattis provided sample test cases e.g. if 1.in and 1.ans are sample test files
- on Mac/Linux Terminal

```bash
  cat 1.in | node cold.js | diff - 1.ans
```

- on Windows cmd prompt:

```bash
  type 1.in | node cold.js > out1.txt
  FC out1.txt 1.ans
```

## C

- open a terminal on Mac/Linux/WSL or cmd prompt on Windows
- change working directory to a problem folder, e.g.

```bash
  cd cold
```

- compile using gcc

```bash
  gcc cold.c
```

- run unit testing; user provided test cases
- write and use a Makefile as demonstrated in C++ section

```bash
  ./a.out test
```

- run kattis provided sample test cases e.g. if 1.in and 1.ans are sample test files
- on Mac/Linux Terminal:

```bash
  cat 1.in | ./a.out | diff - 1.ans
```

- on Windows cmd prompt

```bash
  type 1.in | a.out > out1.txt
  FC out1.txt 1.ans
```

## Java

- See each problem folder
