#! /usr/bin/env pthon3

"""unittesting helpaphd solution"""

__author__ = "Ram Basnet"
__copyright__ = "Copyright 2020"
__license__ = "MIT"

import unittest
from helpaphd import answer

class TestHelpAPhD(unittest.TestCase):
    """
    test cases must start with test and must be a method
    """
    def test1_answer(self):
        self.assertEqual(answer('P=NP'), 'skipped', 'broken')
    
    def test2_answer(self):
        self.assertEqual(answer('99+1'), 100, 'broken')

    def test3_answer(self):
        self.assertEqual(answer('0+1000'), 1000, 'broken')

if __name__ == "__main__":
    unittest.main(verbosity=2)
