# Kattis Demos

demo solutions using automated testing for some problems from https://open.kattis.com

## Requirements

-   bash terminal (preferred) along with language specific tools (compiler/interpreter, etc.) properly installed
-   command prompt in Windows with g++
    - g++ compiler can be downloaded from https://nuwen.net/mingw.html; extract it into c:\ drive as shown in the instructions here: https://nuwen.net/mingw.html#install

# Programming Languages
- demos are provided in the following several languagues
- follow the instruction based on your language and operating system

# C++

-   open a terminal on Mac/Linux and cmd prompt on Windows
-   change working directory to a problem folder, e.g.
    ```
    $ cd cold
    ```
-   compile using g++
    ```
    $ g++ -std=c++14 cold.cpp
    ```
-   run unit testing; user provided test cases
    - on Mac/Linux:
    ```
    $ ./a.out test
    ```
    - on Windows:
    ```
    > a.exe test
    ```
-   run kattis provided sample test cases e.g. if 1.in and 1.ans are sample test files:
    - On Mac/Linux Terminal:
    ```
    $ cat 1.in | ./a.out | diff - 1.ans
    ```
    - On Windows cmd prompt:
    ```
    > type 1.in | a.exe > out1.txt
    > FC out1.txt 1.ans
    ```

# Python3

-   open a terminal on Mac/Linux and cmd prompt on Windows

-   change working directory to a problem folder, e.g.
    ```
    $ cd cold
    ```
-   run unit testing; user provided test cases
    ```
    $ python3 cold.py test
    ```
-   run kattis provided sample test cases e.g. if 1.in and 1.ans are sample test files:
    ```
    $ cat 1.in | python3 cold.py | diff - 1.ans
    ```
    - on Windows cmd prompt:
    ```
    > type 1.in | python3 program.py > out1.txt
    > FC out1.txt 1.ans
    ```

# NodeJS

-   open a terminal on Mac/Linux and cmd prompt on Windows

-   change working directory to a problem folder, e.g.
    ```
    $ cd cold
    ```
-   run unit testing; user provided test cases
    ```
    $ node cold.js test
    ```
-   run kattis provided sample test cases e.g. if 1.in and 1.ans are sample test files
    - on Mac/Linux Terminal:
    ```
    $ cat 1.in | node cold.js | diff - 1.ans
    ```
    - on Windows cmd prompt:
    ```
    > type 1.in | node cold.js > out1.txt
    > FC out1.txt 1.ans
    ```

# C

-   open a terminal on Mac/Linux and cmd prompt on Windows

-   change working directory to a problem folder, e.g.
    ```
    $ cd cold
    ```
-   compile using g++
    ```
    $ gcc cold.c
    ```
-   run unit testing; user provided test cases
    ```
    $ ./a.out test
    ```
-   run kattis provided sample test cases e.g. if 1.in and 1.ans are sample test files
    - on Mac/Linux Terminal:
    ```
    $ cat 1.in | ./a.out | diff - 1.ans
    ```
    - on Windows cmd prompt:
    ```
    > type 1.in | a.out > out1.txt
    > FC out1.txt 1.ans
    ```

# Java

-   See each problem folder - TBD
