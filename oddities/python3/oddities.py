#!/usr/bin/env python3

import sys

def answer(num):
    if num % 2 == 0:
        return 'is even'
    else:
        return 'is odd'

def test():
    assert answer(101) == 'is odd'
    assert answer(2323530) == 'is even'
    print('all test cases passed...')

def solve():
    tests = int(sys.stdin.readline())
    for i in range(tests):
        num = int(sys.stdin.readline())
        print(num, answer(num))

if __name__ == "__main__":
    solve()