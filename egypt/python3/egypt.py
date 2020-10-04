#! /usr/bin/env python3

import sys


def answer(sides):
    sides.sort()
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return 'right'
    else:
        return 'wrong'


def solve():
    data = sys.stdin.readlines()
    for line in data[0:-1]:
        sides = [int(i) for i in line.split()]
        print(answer(sides))


def test():
    input1 = [8, 6, 10]
    assert answer(input1) == "right"
    input2 = [5, 4, 3]
    assert answer(input2) == "right"
    input3 = [5, 12, 13]
    assert answer(input3) == "right"
    input4 = [1, 2, 3]
    assert(answer(input4) == "wrong")
    input5 = [2000, 100, 30000]
    assert answer(input4) == "wrong"
    print('all test cases passed...')


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test()
    else:
        solve()
