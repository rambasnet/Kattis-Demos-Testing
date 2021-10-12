#! /usr/bin/env python3

__author__ = "Ram Basnet"
__license__ = "MIT"
__copyright__ = "Copyright 2021"

from joingjogjam import distance, answer

max_error = 1e-6

def test_distance():
  ans = 1.41421356237
  assert(abs(distance(0, 0, 1, 1) - ans) <= max_error)
  ans = 2.82842712475
  assert(distance(0, 0, 2, 2) - ans <= max_error) 
  ans = 48.6004115209
  assert(distance(1, 30, 6, 45) - ans <= max_error)
  print('Congrtulations! All test cases passed for distance()')

def test_answer():
  startDist = distance(0, 0, 1, 1)
  endDist = distance(1, 1, 2, 2)
  actual = 1.4142135624
  assert(answer(startDist, endDist) - actual <= max_error)
  startDist = distance(0, 0, 0, 1)
  actual = 2.2360679775
  endDist = distance(0, 2, 2, 1)
  assert(answer(startDist, endDist) - actual <= max_error)
  startDist = distance(5, 0, 10, 0)
  endDist = distance(5, 0, 10, 0)
  actual = 5
  assert(answer(startDist, endDist) - actual <= max_error)
  print('Congratulations! All test cases passed for answer()')

if __name__ == '__main__':
  test_distance()
  test_answer()