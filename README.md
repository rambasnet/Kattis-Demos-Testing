# kattisdemos

Demo solutions using automated unit testing

## requirements

-   bash terminal along with language specific tools (compiler/interpreter, etc.) properly installed
-   terminal in (Linux/Mac) or command prompt in (Windows)

# solutions available in following programming languages:

# C++

-   open a terminal/cmd prompt
-   change working directory to a problem folder, e.g.
    ```
    $ cd cold
    ```
-   compile using g++
    ```
    $ g++ -std=c++14 cold.cpp
    ```
-   run unit testing; user provided test cases
    ```
    $ ./a.out test
    ```
-   run kattis provided sample test cases e.g. if 1.in and 1.ans are sample test files:
    in Mac/Linux Terminal:
    ```
    $ cat 1.in | ./a.out | diff - 1.ans
    ```
    in Windows cmd prompt:
    ```
    > type input1.txt | a.out > programOutput1.txt
    > FC.exe programOutput1.txt output1.txt
    ```

# Python3

1.  open a terminal

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
    in Windows cmd prompt
    ```
    > type input1.txt | python3 program.py > programOutput1.txt
    > FC.exe programOutput1.txt output1.txt
    ```

# NodeJS

1.  open a terminal

-   change working directory to a problem folder, e.g.
    ```
    $ cd cold
    ```
-   run unit testing; user provided test cases
    ```
    $ node cold.js test
    ```
-   run kattis provided sample test cases e.g. if 1.in and 1.ans are sample test files:
    ```
    $ cat 1.in | node cold.js | diff - 1.ans
    ```
    in Windows cmd prompt
    ```
    > type input1.txt | node cold.js > programOutput1.txt
    > FC.exe programOutput1.txt output1.txt
    ```

# C

1.  open a terminal

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
-   run kattis provided sample test cases e.g. if 1.in and 1.ans are sample test files:
    ```
    $ cat 1.in | ./a.out | diff - 1.ans
    ```
    in Windows cmd prompt
    ```
    > type input1.txt | a.out > programOutput1.txt
    > FC.exe programOutput1.txt output1.txt
    ```

# Java

-   See each problem folder - TBD
