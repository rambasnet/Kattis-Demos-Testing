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
    def test1_answer(self):
        self.assertEqual(answer(101), 'is odd', 'broken')
    
    def test2_answer(self):
        self.assertEqual(answer(2323530), 'is even')


if __name__ == "__main__":
    unittest.main(verbosity=2)