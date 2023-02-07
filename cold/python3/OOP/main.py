#! /usr/bin/env python3
__author__ = "Ram Basnet"
__date__ = "2022/1/1"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Ram Basnet"

"""
Kattis problem - cold
https://open.kattis.com/problems/cold
"""

import sys
import functools
from temperature import Temperature
from typing import Any, List

class Solution(object):
	def __init__(self) -> None:
		"""
		Represents a solution to the problem
		"""
		self._n: int = 0 # number of temperatures
		self._data: str = '' # data
		self._temps: List[Temperature]  = [] # list of temperatures

	def find_answer(self) -> int:
		"""
		Counts the number of temperatures below zero
		:return: number of temperatures below zero"""
		count = 0 
		for t in self._temps:
			if t.is_negative():
				count += 1
		return count

	def read_data(self, source: Any) -> None:
		"""
		Reads data from stdin
		return: None
		"""
		# ignore the first line
		data = source.readlines()
		self._n = int(data[0])
		self._data = data[1].strip()
		self._temps = [Temperature(int(i)) for i in self._data.split()]
	
	def getN(self) -> int:
		"""
		Returns the number of temperatures
		:return: number of temperatures
		"""
		return self._n

	def get_data(self) -> str:
		"""
		Returns the data
		:return: data
		"""
		return self._data

	def solve(self, source: Any) -> None:
		"""
		Solves the problem
		:return: None
		"""
		self.read_data(source)
		print(self.find_answer())
		#sys.stdout.write('1')

if __name__ == "__main__":
		sol = Solution()
		sol.solve(sys.stdin)
