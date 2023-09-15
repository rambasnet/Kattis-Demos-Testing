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


def solve1() -> None:
    n = input()
    temps = sys.stdin.readline().strip()
    print(f'{n=}; {temps=}', file=sys.stderr)
    print(answer1(temps))


def solve() -> None:
    n = int(sys.stdin.readline())
    # use list comprehension syntax
    temps = [int(n) for n in sys.stdin.readline().strip().split()]
    print(f'{n=}; {temps=}', file=sys.stderr)
    print(answer(temps))


if __name__ == "__main__":
    solve()
    # solve1()
