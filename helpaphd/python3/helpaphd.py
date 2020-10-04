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


def test():
    assert answer('P=NP') == 'skipped'
    assert answer('99+1') == 100
    assert answer('0+1000') == 1000
    print('all test casses passed...')


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test()
    else:
        solve()
