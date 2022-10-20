#! /usr/bin/env python3

"""
unittesting cold.py solution
"""

__author__ = "Ram Basnet"
__copyright__ = "Copyright 2020"
__license__ = "MIT"

import unittest
from cold import answer, answer1

class TestCold(unittest.TestCase):
    """
    test cases must start with test and must be a method
    """
    def test1_answer(self):
        data = [12, -4, -56, -4544545, 64, 46464]
        self.assertEqual(answer(data), 3, 'broken')
    
    def test2_answer(self):
        self.assertEqual(answer([0, 453445, -1, -100, -45454, -44445]), 4, 'borken')
    
    def test3_answer(self):
        self.assertEqual(answer1('0 453445 -1 -100 -45454 -44445'), 4, 'broken')


if __name__ =="__main__":
    unittest.main(verbosity=2)
