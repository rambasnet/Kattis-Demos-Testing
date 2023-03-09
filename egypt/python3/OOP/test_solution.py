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

	@patch('sys.stdout', new_callable=StringIO)
	def test_solve1(self, mock_stdout: StringIO) -> None:
		"""
		Tests solve method
		:return: None
		"""
		# source = '6 8 10\n25 52 60\n5 12 13\n0 0 0\n'
		with open('./data/1.in', 'r') as source:
			sol = Solution(source)
			sol.solve()
			sol.print_answer()
			expected: str = 'right\nwrong\nright\n'
			self.assertEqual(mock_stdout.getvalue(), expected)

	@patch('sys.stdout', new_callable=StringIO)
	def test_solve2(self, mock_stdout: StringIO) -> None:
		"""
		Tests solve method
		:return: None
		"""
		data2 = '6 8 10\n25 52 60\n5 12 13\n0 0 0\n'
		with patch('sys.stdin', StringIO(data2)):
			sol = Solution(sys.stdin)
			sol.solve()
			sol.print_answer()
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
			sol = Solution(sys.stdin)
			sol.solve()
			sol.print_answer()
			expected: str = 'wrong\nwrong\nwrong\nright\n'
			self.assertEqual(mock_stdout.getvalue(), expected)

	def test_solve4(self) -> None:
		"""
		Tests solve method
		:return: None
		"""
		data4 = '2 3 4\n20 50 62\n3 4 7\n3 4 5\n0 0 0\n'
		with patch('sys.stdin', StringIO(data4)):
			sol = Solution(sys.stdin)
			sol.solve()
			expected: str = 'wrong\nwrong\nwrong\nright\n'
			self.assertEqual(sol.answer, expected)

