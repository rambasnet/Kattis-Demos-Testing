#! /usr/bin/env python3

"""
unittest for jointjogjam program
"""

__author__ = "Ram Basnet"
__copyright__ = "Copyright 2021"
__license__ = "MIT"

import unittest
from jointjogjam import answer, distance

PLACES = 6

class Test_jointjogjam(unittest.TestCase):
  """
  test cases must start with test and must be a method
  """
  def test1_distance(self):
    ans = distance(0, 0, 1, 1)
    actual = 1.41421356237
    self.assertAlmostEqual(ans, actual, PLACES)

  def test2_distance(self):
    actual = 2.82842712475
    self.assertAlmostEqual(distance(0, 0, 2, 2), actual, PLACES)

  def test3_distance(self): 
    actual = 15.8113883008
    self.assertAlmostEqual(distance(1, 30, 6, 45), actual, PLACES)

  def test1_answer(self):
    startDist = distance(0, 0, 1, 1)
    endDist = distance(1, 1, 2, 2)
    actual = 1.4142135624
    self.assertAlmostEqual(answer(startDist, endDist), actual, PLACES)

  def test2_answer(self):
    startDist = distance(0, 0, 0, 1)
    actual = 2.2360679775
    endDist = distance(0, 2, 2, 1)
    self.assertAlmostEqual(answer(startDist, endDist), actual, PLACES)

  def test3_answer(self):
    startDist = distance(5, 0, 10, 0)
    endDist = distance(5, 0, 10, 0)
    actual = 5
    self.assertAlmostEqual(answer(startDist, endDist), actual, PLACES)

if __name__ == "__main__":
  unittest.main(verbosity=2)