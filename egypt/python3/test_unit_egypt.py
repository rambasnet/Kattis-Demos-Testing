#! /usr/bin/env python3

"""
unittesting egypt solution
"""

__author__ = "Ram Basnet"
__copyright__ = "Copyright 2020"
__license__ = "MIT"

import unittest
from egypt import answer

class TestEgypt(unittest.TestCase):
    """
    test cases must start with test and must be a method
    """
    def test1_answer(self):
        input1 = [8, 6, 10]
        self.assertEqual(answer(input1), "right", "broken")
    
    def test2_answer(self):
        input2 = [5, 4, 3]
        self.assertEqual(answer(input2), "right", "broken")

    def test3_answer(self):
        input3 = [5, 12, 13]
        self.assertEqual(answer(input3), "right", "broken")

    def test4_answer(self):
        input4 = [1, 2, 3]
        self.assertEqual(answer(input4), "wrong", "broken")

    def test5_answer(self):
        input5 = [2000, 100, 30000]
        self.assertEqual(answer(input5), "wrong", "broken")


if __name__ == "__main__":
    unittest.main(verbosity=2)