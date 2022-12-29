__author__ = "Ram Basnet"
__date__ = "2023/1/1"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Ram Basnet"

"""
Testing Solution class
"""

import unittest
from unittest.mock import patch
from io import StringIO
from main import Solution

class TestSolution(unittest.TestCase):
	"""
	Testing Solution class
	"""
	def setUp(self) -> None:
		"""
		Setup method
		:return: None
		"""
		self.sol: Solution = Solution()

	@patch('sys.stdout', new_callable=StringIO)
	def test_solve(self, mock_stdout: StringIO) -> None:
		"""
		Tests solve method
		:return: None
		"""
		self.sol.solve()
		self.assertEqual(mock_stdout.getvalue(), 'Hello World!\n')

if __name__ == '__main__':
	unittest.main(verbosity=2)

