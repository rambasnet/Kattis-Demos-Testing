__author__ = "Ram Basnet"
__date__ = "2023/1/1"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Ram Basnet"

from typing import Any

class Temperature(object):
	"""
	Represents a temperature
	"""
	def __init__(self, temp: int, unit: str='F') -> None:
		"""
		initializes a temperature
		:param temp: temperature
		"""
		self.temp: int = temp
		self.unit: str = unit

	def setTemp(self, temp: int) -> None:
		"""
		sets the temperature
		:param temp: temperature
		"""
		self.temp = temp

	def getTemp(self) -> int:
		"""
		returns the temperature
		:return: temperature
		"""
		return self.temp

	def setUnit(self, unit: str) -> None:
		self.unit = unit

	def getUnit(self) -> str:
		return self.unit

	def isNegative(self) -> bool:
		return self.temp < 0

	def __str__(self) -> str:
		return f'{self.temp} {self.unit}'

	def __repr__(self) -> str:
		return f'{self.temp} {self.unit}'

	def __lt__(self, other: 'Temperature') -> bool:
		if not isinstance(other, Temperature):
			return False
		return self.temp < other.temp
	
	def __gt__(self, other: 'Temperature') -> bool:
		if not isinstance(other, Temperature):
			return False
		return self.temp > other.temp

	def __eq__(self, other: Any) -> bool:
		if not isinstance(other, Temperature):
			return NotImplemented
		return self.temp == other.temp

	def __le__(self, other: 'Temperature') -> bool:
		if not isinstance(other, Temperature):
			return False
		return self.temp <= other.temp

	def __ge__(self, other: 'Temperature') -> bool:
		if not isinstance(other, Temperature):
			return False
		return self.temp >= other.temp


