__author__ = "Ram Basnet"
__date__ = "2023/1/1"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Ram Basnet"

"""
Add class
"""

from typing import Union

class Add(object):
	"""
	Add class
	"""
	def __init__(self, a:Union[int, str]=0, b:Union[int, str]=0) -> None:
		"""
		Constructor
		"""
		self.a:Union[int, str] = a
		self.b:Union[int, str] = b

	def setA(self, a:Union[int, str]) -> None:
		"""
		Sets a
		:param a: a
		:return: None
		"""
		self.a = a

	def getA(self) -> Union[int, str]:
		"""
		Returns a
		:return: a
		"""
		return self.a

	def setB(self, b:Union[int, str]) -> None:
		"""
		Sets b
		:param b: b
		:return: None
		"""
		self.b = b

	def getB(self) -> Union[int, str]:
		"""
		Returns b
		:return: b
		"""
		return self.b

	def add(self) -> str:
		"""
		Adds a and b
		:return: sum
		"""
		if isinstance(self.a, str) or isinstance(self.b, str):
			return 'skipped'
		return str(self.a + self.b)

	def __str__(self) -> str:
		"""
		Returns the string representation of the object
		:return: string representation
		"""
		return f'{self.a} + {self.b}'

	def __repr__(self) -> str:
		"""
		Returns the string representation of the object
		:return: string representation
		"""
		return self.__str__()

