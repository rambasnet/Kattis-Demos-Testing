__author__ = "Ram Basnet"
__date__ = "2023/1/1"
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
	def setUp(self) -> None:
		"""
		Setup method - called before each test
		:return: None
		"""
		self.sol = Solution()
		self.input1 = open('./data/1.in', 'r')
		self.input2 = open('./data/2.in', 'r')

	def tearDown(self) -> None:
		"""
		Tear down method - called after each test
		:return: None
		"""
		self.input1.close()
		self.input2.close()
		return super().tearDown()

	def test_readData1(self) -> None:
		"""
		Tests readData method
		:return: None
		"""
		self.sol.readData(self.input1)
		self.assertEqual(self.sol.getN(), 3)
		self.assertEqual(self.sol.getData(), '5 -10 15')

	def test_readData2(self) -> None:
		"""
		Tests readData method
		:return: None
		"""
		self.sol.readData(self.input2)
		self.assertEqual(self.sol.getN(), 5)
		self.assertEqual(self.sol.getData(), '-14 -5 -39 -5 -7')

	def test_findAnswer1(self) -> None:
		"""
		Tests findAnswer method
		:return: None
		"""
		self.sol.readData(self.input1)
		expected = self.sol.findAnswer()
		self.assertEqual(expected, 1)

	def test_findAnswer2(self) -> None:
		"""
		Tests findAnswer method
		:return: None
		"""
		self.sol.readData(self.input2)
		expected = self.sol.findAnswer()
		self.assertEqual(expected, 5)

	#@patch('sys.stdout', new_callable=StringIO)
	#@patch('sys.stderr', new_callable=StringIO)
	def test_solve1(self) -> None:
		"""
		Tests solve method - using patch context manager
		- tests 1.in
		:return: None
		"""
		#self.sol.solve()
		with patch('sys.stdout', new=StringIO()) as mock_stdout:
			self.sol.solve(self.input1)
			self.assertEqual(mock_stdout.getvalue(), '1\n')

	@patch('sys.stdout', new_callable=StringIO)
	def test_solve2(self, mock_stdout: StringIO) -> None:
		"""
		Tests solve method - using patch decorator
		- tests 2.in
		:return: None
		"""
		self.sol.solve(self.input2)
		self.assertEqual(mock_stdout.getvalue(), '5\n')
		
if __name__ == "__main__":
	unittest.main(verbosity=2)
