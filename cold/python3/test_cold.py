#!/ usr/bin/env python3

"""
separate test file for pytest
pytest recursively discovers all the files with test* and runs the
assert statements in them
"""

__author__ = "Ram Basnet"
__copyright__ = "Copyright 2021"
__license__ = "MIT"

from cold import answer, answer1

def test_answer():
  assert answer([12, -4, -56, -4544545, 64, 46464]) == 3
  assert answer([0, 453445, -1, -100, -45454, -44445]) == 4
  assert answer1('0 453445 -1 -100 -45454 -44445') == 4
  print('all test casses passed...')

if __name__ == "__main__":
  test_answer()