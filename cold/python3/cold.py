#! /usr/bin/env python3
"""
Kattis cold problem
Ram Basnet
Sept. 14, 2023

Find the number of temperatures strictly less than zero.
"""
import sys
from typing import List


def answer(data: List[int]) -> int:
    """Count total number of -ve temeratures in data.

    Args:
        data (List[int]): List of integers as temperature

    Returns:
        int: count of -ve temps
    """
    count = 0
    for t in data:
        if t < 0:
            count += 1
    return count


def answer1(line: str) -> int:
    """Count total number of -ve temeratures in data.

    Args:
        line (str): integer temperatures as space separated string

    Returns:
        int: count of -ve temps
    """
    return line.count('-')


def solve1() -> None:
    """Reads input ans uses answer1 function.
    """
    n = input()
    temps = sys.stdin.readline().strip()
    print(f'{n=}; {temps=}', file=sys.stderr)
    print(answer1(temps))


def solve() -> None:
    """Reads input and parses the string as list of integer.
    """
    n = input()
    # use list comprehension syntax
    temps = [int(temp) for temp in sys.stdin.readline().strip().split()]
    print(f'{n=}; {temps=}', file=sys.stderr)
    print(answer(temps))


if __name__ == "__main__":
    solve()
    # solve1()
