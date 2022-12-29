__author__ = "Ram Basnet"
__date__ = "2022/1/1"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Ram Basnet"

"""
Unittesting Solution class
"""

import unittest
from main import Solution
from unittest.mock import patch
from io import StringIO

class TestSolution(unittest.TestCase):
	"""
	Unittesting Solution class
	"""
	def setUp(self):
		"""
		Setup method - called before each test
		:return: None
		"""
		self.sol = Solution()
		self.input1 = open('../../1.in', 'r')
		self.input2 = open('../../2.in', 'r')

	def tearDown(self) -> None:
		"""
		Tear down method - called after each test
		:return: None
		"""
		self.input1.close()
		self.input2.close()
		return super().tearDown()

	def test_readData1(self):
		"""
		Tests readData method
		:return: None
		"""
		self.sol.readData(self.input1)
		self.assertEqual(self.sol.n, 3)
		self.assertEqual(self.sol.getData(), '5 -10 15')

	def test_readData2(self):
		"""
		Tests readData method
		:return: None
		"""
		self.sol.readData(self.input2)
		self.assertEqual(self.sol.n, 5)
		self.assertEqual(self.sol.getData(), '-14 -5 -39 -5 -7')

	def test_findAnswer1(self):
		"""
		Tests findAnswer method
		:return: None
		"""
		self.sol.readData(self.input1)
		expected = self.sol.findAnswer()
		self.assertEqual(expected, 1)

	def test_findAnswer2(self):
		"""
		Tests findAnswer method
		:return: None
		"""
		self.sol.readData(self.input2)
		expected = self.sol.findAnswer()
		self.assertEqual(expected, 5)

	@patch('sys.stdout', new_callable=StringIO)
	@patch('sys.stderr', new_callable=StringIO)
	def test_solve(self, mock_stdout, mock_stderr):
		"""
		Tests solve method
		:return: None
		"""
		#self.sol.solve()
		self.sol.solve(self.input1)
		self.assertEqual(mock_stdout.getvalue(), '1')
		

if __name__ == "__main__":
	unittest.main(verbosity=2)
