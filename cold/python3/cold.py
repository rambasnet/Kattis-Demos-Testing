#! /usr/bin/env python3

import sys


def answer(data):
    count = 0
    for t in data:
        if t < 0:
            count += 1
    return count


def answer1(line):
    return line.count('-')


def solve():
    #n = int(input())
    #temps = [int(n) for n in input().split()]
    data = sys.stdin.readlines()
    #n = int(data[0])
    #temps = [int(i) for i in data[1].split()]
    #print(n, temps)
    print(answer1(data[1]))


def test():
    assert answer([12, -4, -56, -4544545, 64, 46464]) == 3
    assert answer([0, 453445, -1, -100, -45454, -44445]) == 4
    assert answer1('0 453445 -1 -100 -45454 -44445') == 4
    print('all test casses passed...')


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test()
    else:
        solve()
