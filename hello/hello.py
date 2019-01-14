#!/usr/bin/env python3
# Kattis - hello problem

import sys

def answer():
    return "Hello World!"

def solve():
    print(answer())

def test():
    assert answer() == "Hello World!"
    print('all test cases passed...')

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        #print(sys.argv)
        test()
    else:
        solve()