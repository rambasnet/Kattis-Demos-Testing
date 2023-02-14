__author__ = "Ram Basnet"
__date__ = "2023/1/1"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Ram Basnet"

"""
Triangle class
"""

from typing import Tuple

class Triangle(object):
	"""
	Triangle class
	"""
	def __init__(self, side1:float, side2:float, side3:float) -> None:
		"""
		Constructor
		"""
		self._side1:float = side1
		self._side2:float = side2
		self._side3:float = side3

	def set_sides(self, side1:float, side2:float, side3:float) -> None:
		"""
		Sets the sides of the triangle
		:param side1: side1
		:param side2: side2
		:param side3: side3
		:return: None
		"""
		self._side1 = side1
		self._side2 = side2
		self._side3 = side3

	@property
	def sides(self) -> Tuple[float, float, float]:
		"""
		Returns the sides of the triangle
		:return: sides
		"""
		return (self._side1, self._side2, self._side3)

	@property
	def perimeter(self) -> float:
		"""
		Returns the perimeter of the triangle
		:return: perimeter
		"""
		return self._side1 + self._side2 + self._side3

	@property
	def area(self) -> float:
		"""
		Returns the area of the triangle - Heron's formula
		:return: area
		"""
		s:float = self.perimeter / 2
		ans:float = (s * (s - self._side1) * (s - self._side2) * (s - self._side3)) ** 0.5
		return ans

	def __str__(self) -> str:
		"""
		Returns the string representation of the object
		:return: string representation
		"""
		return 'Triangle: side1 = ' + str(self._side1) + ' side2 = ' + str(self._side2) + ' side3 = ' + str(self._side3)

	def __repr__(self) -> str:
		"""
		Returns the string representation of the object
		:return: string representation
		"""
		return self.__str__()

	def is_right_angled(self) -> bool:
		"""
		Returns whether the triangle is right angled or not
		:return: True if right angled, False otherwise
		"""
		sides = [self._side1, self._side2, self._side3]
		sides.sort()
		return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2


