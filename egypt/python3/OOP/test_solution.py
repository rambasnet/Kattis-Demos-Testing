__author__ = "Ram Basnet"
__date__ = "2023/1/1"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Ram Basnet"

"""
Unittesting Solution class
"""

import unittest
from unittest.mock import patch
from io import StringIO
from main import Solution
import sys


class TestSolution(unittest.TestCase):
	"""
	Unittesting Solution class
	"""

	def setUp(self) -> None:
			"""
			Setup method - called before each test
			:return: None
			"""
			self.sol = Solution()

	@patch('sys.stdout', new_callable=StringIO)
	def test_solve1(self, mock_stdout: StringIO) -> None:
			"""
			Tests solve method
			:return: None
			"""
			# source = '6 8 10\n25 52 60\n5 12 13\n0 0 0\n'
			source = open('./data/1.in', 'r')
			self.sol.solve(source)
			expected: str = 'right\nwrong\nright\n'
			source.close()
			self.assertEqual(mock_stdout.getvalue(), expected)

	@patch('sys.stdout', new_callable=StringIO)
	def test_solve2(self, mock_stdout: StringIO) -> None:
			"""
			Tests solve method
			:return: None
			"""
			data2 = '6 8 10\n25 52 60\n5 12 13\n0 0 0\n'
			with patch('sys.stdin', StringIO(data2)):
					self.sol.solve(sys.stdin)
					expected: str = 'right\nwrong\nright\n'
					self.assertEqual(mock_stdout.getvalue(), expected)

	@patch('sys.stdout', new_callable=StringIO)
	def test_solve3(self, mock_stdout: StringIO) -> None:
			"""
			Tests solve method
			:return: None
			"""
			data3 = '2 3 4\n20 50 62\n3 4 7\n3 4 5\n0 0 0\n'
			with patch('sys.stdin', StringIO(data3)):
					self.sol.solve(sys.stdin)
					expected: str = 'wrong\nwrong\nwrong\nright\n'
					self.assertEqual(mock_stdout.getvalue(), expected)


if __name__ == '__main__':
	unittest.main(verbosity=2)
