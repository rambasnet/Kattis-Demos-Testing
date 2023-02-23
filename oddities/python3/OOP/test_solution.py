from __future__ import annotations

__author__ = "Ram Basnet"
__date__ = "2023/1/1"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Ram Basnet"

"""
Unit tests for Solution class
"""

import unittest
import sys
from main import Solution
from unittest.mock import patch
from io import StringIO

class TestSolution(unittest.TestCase):
	"""
	Unit tests for Solution class
	"""
	def setUp(self) -> None:
		"""
		Setup method
		:return: None
		"""
		data = '3\n10\n9\n-5\n'
		with patch('sys.stdin', StringIO(data)):
			self.sol = Solution(sys.stdin)

	def test_getN(self) -> None:
		"""
		Tests getN method
		:return: None
		"""
		self.assertEqual(self.sol.getN(), 3)
	
	def test_getData(self) -> None:
		"""
		Tests getData method
		:return: None
		"""
		self.assertEqual(self.sol.getData(), [10, 9, -5])


	@patch('sys.stdout', new_callable=StringIO)
	def test_solve(self, mock_stdout: StringIO) -> None:
		"""
		Tests solve method
		:return: None
		"""
		self.sol.solve()
		expected = '10 is even\n9 is odd\n-5 is odd\n'
		self.assertEqual(mock_stdout.getvalue(), expected)

	@patch('sys.stdout', new_callable=StringIO)
	def test_solve1(self, mock_stdout: StringIO) -> None:
		"""
		Tests solve method
		:return: None
		"""
		data = '5\n20\n11\n-99\n-110\n-11\n'
		with patch('sys.stdin', StringIO(data)):
			sol = Solution(sys.stdin)
			sol.solve()
			expected = '20 is even\n11 is odd\n-99 is odd\n-110 is even\n-11 is odd\n'
			self.assertEqual(mock_stdout.getvalue(), expected)

if __name__ == '__main__':
	unittest.main(verbosity=2)
