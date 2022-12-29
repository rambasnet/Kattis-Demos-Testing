__author__ = "Ram Basnet"
__date__ = "2023/1/1"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Ram Basnet"


"""
Unit tests for Odd class
"""
import unittest
from oddity import Oddity

class TestOdd(unittest.TestCase):
	"""
	Unit tests for Odd class
	"""
	def setUp(self) -> None:
		"""
		Setup method
		:return: None
		"""
		self.oddity = Oddity()

	def test_setN(self) -> None:
		"""
		Tests setN method
		:return: None
		"""
		self.oddity.setN(1)
		self.assertEqual(self.oddity.getN(), 1)

	def test_getN(self) -> None:
		"""
		Tests getN method
		:return: None
		"""
		self.assertEqual(self.oddity.getN(), 0)

	def test_isOdd(self) -> None:
		"""
		Tests isOdd method
		:return: None
		"""
		self.assertEqual(self.oddity.isOdd(), False)

	def test_isEven(self) -> None:
		"""
		Tests isEven method
		:return: None
		"""
		self.assertEqual(self.oddity.isEven(), True)

	def test_getOddity(self) -> None:
		"""
		Tests getOddity method
		:return: None
		"""
		self.assertEqual(self.oddity.getOddity(), 'even')

	def test_getOddity1(self) -> None:
		"""
		Tests getOddity method
		:return: None
		"""
		self.oddity.setN(-99)
		self.assertEqual(self.oddity.getOddity(), 'odd')

	def test_oddity(self) -> None:
		"""
		Tests oddity method
		:return: None
		"""
		self.assertEqual(str(self.oddity), '0 is even')

	def test_oddity1(self) -> None:
		"""
		Tests oddity method
		:return: None
		"""
		self.oddity.setN(-199)
		self.assertEqual(str(self.oddity), '-199 is odd')

if __name__ == '__main__':
	unittest.main(verbosity=2)
