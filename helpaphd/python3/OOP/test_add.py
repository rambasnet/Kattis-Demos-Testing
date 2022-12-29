__author__ = "Ram Basnet"
__date__ = "2023/1/1"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Ram Basnet"

"""
Unit tests for Add class
"""

import unittest
from add import Add

class TestAdd(unittest.TestCase):
	"""
	Unit tests for Add class
	"""
	def setUp(self) -> None:
		"""
		Setup method
		:return: None
		"""
		self.add = Add()

	def test_setA(self) -> None:
		"""
		Tests setA method
		:return: None
		"""
		self.add.setA(1)
		self.assertEqual(self.add.getA(), 1)

	def test_getA(self) -> None:
		"""
		Tests getA method
		:return: None
		"""
		self.assertEqual(self.add.getA(), 0)

	def test_setB(self) -> None:
		"""
		Tests setB method
		:return: None
		"""
		self.add.setB(10)
		self.assertEqual(self.add.getB(), 10)

	def test_getB(self) -> None:
		"""
		Tests getB method
		:return: None
		"""
		self.assertEqual(self.add.getB(), 0)

	def test_add(self) -> None:
		"""
		Tests add method
		:return: None
		"""
		self.assertEqual(self.add.add(), '0')

	def test_add2(self) -> None:
		"""
		Tests add method
		:return: None
		"""
		self.add.setA(1)
		self.add.setB(10)
		self.assertEqual(self.add.add(), '11')

	def test_add3(self) -> None:
		"""
		Tests add method
		:return: None
		"""
		self.add.setA('P')
		self.add.setB('NP')
		self.assertEqual(self.add.add(), 'skipped')

if __name__ == '__main__':
	unittest.main(verbosity=2)

