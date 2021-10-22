#! /usr/bin/env python3

from egypt import answer

def test_answer():
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
  test_answer()