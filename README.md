# Kattis Demos

Demo solutions using automated testing

## requirements

-   bash terminal along with language specific tools (compiler/interpreter, etc.) properly installed
-   terminal in (Linux/Mac) or command prompt in (Windows)

# Demos in the following programming languages

# C++

-   open a terminal on Mac/Linus and cmd prompt on Windows
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

-   open a terminal on Mac/Linus and cmd prompt on Windows

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
    > type 1.tin | python3 program.py > out1.txt
    > FC out1.txt 1.ans
    ```

# NodeJS

-   open a terminal on Mac/Linus and cmd prompt on Windows

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

-   open a terminal on Mac/Linus and cmd prompt on Windows

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
