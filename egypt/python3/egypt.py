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



if __name__ == "__main__":
    solve()
