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
		self._temp: int = temp
		self._unit: str = unit

	@property
	def temp(self) -> int:
		"""
		returns the temperature
		:return: _temp
		"""
		return self._temp

	@temp.setter
	def temp(self, temp: int) -> None:
		"""
		sets the temperature
		:param temp: temperature
		"""
		self._temp = temp

	@property
	def unit(self) -> str:
		"""
		Property to get/set unit of temperature
		Returns:
				str: unit
		"""
		return self._unit

	@unit.setter
	def unit(self, unit: str) -> None:
		self._unit = unit

	def is_negative(self) -> bool:
		return self._temp < 0

	def __str__(self) -> str:
		return f'{self._temp} {self.unit}'

	def __repr__(self) -> str:
		return f'{self._temp} {self.unit}'

	def __lt__(self, other: 'Temperature') -> bool:
		if not isinstance(other, Temperature):
			return NotImplemented 
			# special value which should be returned by the binary special methods
			# to indicate the operation is not implemented wrt the other type
		return self._temp < other._temp
	
	def __gt__(self, other: 'Temperature') -> bool:
		if not isinstance(other, Temperature):
			return NotImplemented
		return self._temp > other._temp

	def __eq__(self, other: Any) -> bool:
		if not isinstance(other, Temperature):
			return NotImplemented
		return self._temp == other._temp

	def __le__(self, other: 'Temperature') -> bool:
		if not isinstance(other, Temperature):
			return NotImplemented
		return self._temp <= other._temp

	def __ge__(self, other: 'Temperature') -> bool:
		if not isinstance(other, Temperature):
			return NotImplemented
		return self._temp >= other._temp

