#! /usr/bin/env python3

import sys

def answer(equation):
    result = 'skipped'
    try:
        result = eval(equation)
    except:
        pass
    return result


def solve():
    data = sys.stdin.readlines()
    ans = []
    for line in data[1:]:
        ans.append(str(answer(line)))
    print('\n'.join(ans))


if __name__ == "__main__":
    solve()
