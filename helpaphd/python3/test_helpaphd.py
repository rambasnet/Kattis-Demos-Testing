#! /usr/bin/env python3

from helpaphd import answer

def test():
    assert answer('P=NP') == 'skipped'
    assert answer('99+1') == 100
    assert answer('0+1000') == 1000
    print('all test casses passed...')

if __name__ == "__main__":
    test()