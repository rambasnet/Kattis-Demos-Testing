#! /usr/bin/env python3

__author__ = "Ram Basnet"
__license__ = "MIT"
__copyright__ = "Copyright 2021"

from jointjogjam import distance, answer

MAX_ERROR = 1e-6

def test_distance():
  ans = 1.41421356237
  assert(abs(distance(0, 0, 1, 1) - ans) <= MAX_ERROR)
  ans = 2.82842712475
  assert(abs(distance(0, 0, 2, 2) - ans) <= MAX_ERROR) 
  ans = 15.8113883008
  assert(abs(distance(1, 30, 6, 45) - ans) <= MAX_ERROR)
  print('Congrtulations! All test cases passed for distance()')

def test_answer():
  startDist = distance(0, 0, 1, 1)
  endDist = distance(1, 1, 2, 2)
  actual = 1.4142135624
  assert(answer(startDist, endDist) - actual <= MAX_ERROR)
  startDist = distance(0, 0, 0, 1)
  actual = 2.2360679775
  endDist = distance(0, 2, 2, 1)
  assert(answer(startDist, endDist) - actual <= MAX_ERROR)
  startDist = distance(5, 0, 10, 0)
  endDist = distance(5, 0, 10, 0)
  actual = 5
  assert(answer(startDist, endDist) - actual <= MAX_ERROR)
  print('Congratulations! All test cases passed for answer()')

if __name__ == '__main__':
  test_distance()
  test_answer()