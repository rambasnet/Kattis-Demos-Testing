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
from main import Solution
from unittest.mock import patch
from io import StringIO
import sys

class TestSolution(unittest.TestCase):
	"""
	Unit tests for Solution class
	"""

	def setUp(self) -> None:
		"""
		Setup method
		:return: None
		"""
		data = '4\n2+2\n1+2\nP=NP\n0+0\n'
		with patch('sys.stdin', StringIO(data)):
			self.sol = Solution(sys.stdin)

	def test_getData(self) -> None:
		"""
		Tests getData method
		:return: None
		"""
		self.assertEqual(self.sol.getData(), [[2, '+', 2], [1, '+', 2], ['P', '=', 'NP'], [0, '+', 0]])

	def test_n(self) -> None:
		"""
		Tests n property
		:return: None
		"""
		self.assertEqual(self.sol.n, 4)

	def test_solve(self) -> None:
		"""
		Tests solve method
		:return: None
		"""
		with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
			self.sol.solve()
			self.assertEqual(mock_stdout.getvalue(), '4\n3\nskipped\n0\n')

	def test_solve1(self) -> None:
		"""
		Tests solve method
		:return: None
		"""
		data = '5\n20+2\n10+200\nP=NP\n110+10\n11+11\n'
		with patch('sys.stdin', StringIO(data)):
			with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
				sol = Solution(sys.stdin)
				sol.solve()
				self.assertEqual(mock_stdout.getvalue(), '22\n210\nskipped\n120\n22\n')
		
if __name__ == '__main__':
	unittest.main(verbosity=2)
	
