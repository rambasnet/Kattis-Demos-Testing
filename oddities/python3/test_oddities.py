#! /usr/bin/env python3

"""
unittesting oddities solution.
"""

__author__ = "Ram Basnet"
__copyright__ = "Copyright 2020"
__license__ = "MIT"

import unittest
from oddities import answer

class TestOddities(unittest.TestCase):
    """
    test cases must start with test and must be a method
    """
    def test1_answer(self):
        self.assertEqual(answer(101), 'is odd', 'broken')
    
    def test2_answer(self):
        self.assertEqual(answer(2323530), 'is even', 'failed')


if __name__ == "__main__":
    unittest.main(verbosity=2)