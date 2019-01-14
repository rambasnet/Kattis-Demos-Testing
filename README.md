# kattisdemos

Demo solutions using automated testing

-   solutions available in: C++, Python3, NodeJS, C

# C++

-   open a terminal
-   Change working directory to a problem folder, e.g.
    \$ cd cold
-   compile using g++
    \$ g++ -std=c++14 cold.cpp
-   run unit testing; user provided test cases
    \$ ./a.out test
-   run kattis provided sample test cases. e.g. if 1.in and 1.ans are sample test files:
-   \$ cat 1.in | ./a.out | diff - 1.ans

# Python3

-   open a terminal
-   change working directory to a problem folder, e.g.
    \$ cd cold
-   run unit testing; user provided test cases
    \$ python3 cold.py test
-   run kattis provided sample test cases. e.g. if 1.in and 1.ans are sample test files:
-   \$ cat 1.in | python3 cold.py | diff - 1.ans

# NodeJS

-   open a terminal
-   change working directory to a problem folder, e.g.
    \$ cd cold
-   run unit testing; user provided test cases
    \$ node cold.js test
-   run kattis provided sample test cases. e.g. if 1.in and 1.ans are sample test files:
-   \$ cat 1.in | node cold.js | diff - 1.ans

# C

-   open a terminal
-   Change working directory to a problem folder, e.g.
    `$ cd cold`
-   compile using g++
    -   \$ gcc cold.c
-   run unit testing; user provided test cases
    -   \$ ./a.out test
-   run kattis provided sample test cases. e.g. if 1.in and 1.ans are sample test files:
    -   \$ cat 1.in | ./a.out | diff - 1.ans

# Java

-   TBD
