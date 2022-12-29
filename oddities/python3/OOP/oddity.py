__author__ = "Ram Basnet"
__date__ = "2023/1/1"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Ram Basnet"

"""
Oddity class
"""

class Oddity(object):
	"""
	Odd class
	"""

	def __init__(self, n:int=0) -> None:
		"""
		Constructor
		"""
		self.n = n

	def setN(self, n:int) -> None:
		"""
		Sets n
		:param n: n
		:return: None
		"""
		self.n = n

	def getN(self) -> int:
		"""
		Returns n
		:return: n
		"""
		return self.n

	def isOdd(self) -> bool:
		"""
		Returns true if n is odd
		:return: True if n is odd
		"""
		return self.n % 2 == 1

	def isEven(self) -> bool:
		"""
		Returns true if n is even
		:return: True if n is even
		"""
		return self.n % 2 == 0

	def getOddity(self) -> str:
		"""
		Returns oddity of n
		:return: oddity of n
		"""
		return 'odd' if self.isOdd() else 'even'	

	def __str__(self) -> str:
		"""
		Returns the string representation of the object
		:return: string representation of the object
		"""
		return f'{self.n} is {self.getOddity()}'

	def __repr__(self) -> str:
		"""
		Returns the string representation of the object
		:return: string representation of the object
		"""
		return self.__str__()

