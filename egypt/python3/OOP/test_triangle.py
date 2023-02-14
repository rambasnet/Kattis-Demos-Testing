__author__ = "Ram Basnet"
__date__ = "2023/1/1"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Ram Basnet"

"""
Unittesting Triangle class
"""

import unittest
from triangle import Triangle
from unittest.mock import patch

class TestTriangle(unittest.TestCase):
	"""
	Unittesting Triangle class
	"""

	def setUp(self) -> None:
		"""
		Setup method - creates a triangle object every time a test is run
		:return: None
		"""
		self.triangle = Triangle(3, 4, 5)

	def test_getPerimeter(self) -> None:
		"""
		Tests getPerimeter method
		:return: None
		"""
		self.assertEqual(self.triangle.perimeter, 12)

	def test_getArea(self) -> None:
		"""
		Tests getArea method
		:return: None
		"""
		self.assertEqual(self.triangle.area, 6)

	def test_getSides(self) -> None:
		"""
		Tests getSides method
		:return: None
		"""
		self.assertEqual(self.triangle.sides, (3, 4, 5))

	def test_isRightAngled(self) -> None:
		"""
		Tests isRight method
		:return: None
		"""
		self.assertTrue(self.triangle.is_right_angled())

	def test_isRightAngled2(self) -> None:
		"""
		Tests isRight method
		:return: None
		"""
		self.triangle.set_sides(3, 4, 6)
		self.assertFalse(self.triangle.is_right_angled())

	def test_isRightAngled3(self) -> None:
		"""
		Tests isRight method
		:return: None
		"""
		self.triangle.set_sides(3, 4, 7)
		self.assertFalse(self.triangle.is_right_angled())


if __name__ == '__main__':
	unittest.main(verbosity=2)
