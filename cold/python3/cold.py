#! /usr/bin/env python3

import sys
from typing import List

def answer(data: List[int]) -> int:
    count = 0
    for t in data:
        if t < 0:
            count += 1
    return count


def answer1(line: str) -> int:
    return line.count('-')

def solve() -> None:
    #n = int(input())
    #temps = [int(n) for n in input().split()]
    data = sys.stdin.readlines()
    #n = int(data[0])
    #temps = [int(i) for i in data[1].split()]
    #print(n, temps)
    print(answer1(data[1]))


if __name__ == "__main__":
    solve()
