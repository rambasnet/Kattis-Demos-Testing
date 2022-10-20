#! /usr/bin/env python3

"""
unittest for hello solution
"""

__author__ = "Ram Basnet"
__copyright__ = "Copyright 2020"
__license__ = "MIT"

import unittest
from hello import answer

class TestHello(unittest.TestCase):
    """
    test cases must start with test and must be a method
    """
    def test1_answer(self):
        self.assertEqual(answer(), 'Hello World!', "Test failed...")


if __name__ == "__main__":
    unittest.main(verbosity=2)

