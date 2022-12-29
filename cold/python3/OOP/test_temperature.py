__author__ = "Ram Basnet"
__date__ = "2023/1/1"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Ram Basnet"

"""
Unittesting Temperature class
"""

import unittest
from temperature import Temperature

class TestTemperature(unittest.TestCase):
	"""
	Unittesting Temperature class
	"""
	def setUp(self) -> None:
		"""
		Setup method
		:return: None
		"""
		self.temp = Temperature(32)

	def test_setTemp(self) -> None:
		"""
		Tests setTemp method
		:return: None
		"""
		self.temp.setTemp(0)
		self.assertEqual(self.temp.getTemp(), 0)

	def test_getTemp(self) -> None:
		"""
		Tests getTemp method
		:return: None
		"""
		self.assertEqual(self.temp.getTemp(), 32)

	def test_setUnit(self) -> None:
		"""
		Tests setUnit method
		:return: None
		"""
		self.temp.setUnit('C')
		self.assertEqual(self.temp.getUnit(), 'C')

	def test_getUnit(self) -> None:
		"""
		Tests getUnit method
		:return: None
		"""
		self.assertEqual(self.temp.getUnit(), 'F')

	def test_isNegative(self) -> None:
		"""
		Tests isNegative method
		:return: None
		"""
		self.assertFalse(self.temp.isNegative())

	def test_str(self) -> None:
		"""
		Tests str method
		:return: None
		"""
		self.assertEqual(str(self.temp), '32 F')

	def test_repr(self) -> None:
		"""
		Tests repr method
		:return: None
		"""
		self.assertEqual(repr(self.temp), '32 F')

	def test_lt(self) -> None:
		"""
		Tests lt method
		:return: None
		"""
		self.assertFalse(self.temp < Temperature(0))

	def test_gt(self) -> None:
		"""
		Tests gt method
		:return: None
		"""
		self.assertTrue(self.temp > Temperature(0))

	def test_eq(self) -> None:
		"""
		Tests eq method
		:return: None
		"""
		self.assertFalse(self.temp == Temperature(0))

	def test_le(self) -> None:
		"""
		Tests le method
		:return: None
		"""
		self.assertFalse(self.temp <= Temperature(0))

	def test_ge(self) -> None:
		"""
		Tests ge method
		:return: None
		"""
		self.assertTrue(self.temp >= Temperature(0))

	def tearDown(self) -> None:
		"""
		Tear down method
		:return: None
		"""
		return super().tearDown()

if __name__ == '__main__':
	unittest.main(verbosity=2)
