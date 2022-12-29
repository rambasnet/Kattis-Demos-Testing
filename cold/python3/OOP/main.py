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
from Temperature import Temperature
from typing import Any

class Solution(object):
	def __init__(self):
		"""
		Represents a solution to the problem
		"""
		self.n = 0 # number of temperatures
		self.data = None
		self.temps = [] # list of temperatures

	def findAnswer(self) -> int:
		"""
		Counts the number of temperatures below zero
		:return: number of temperatures below zero"""
		count = 0
		for t in self.temps:
			if t.isNegative():
				count += 1
		return count

	def readData(self, source) -> None:
		"""
		Reads data from stdin
		return: None
		"""
		# ignore the first line
		data = source.readlines()
		self.n = int(data[0])
		self.data = data[1].strip()
		self.temps = [Temperature(int(i)) for i in self.data.split()]
	
	def getData(self) -> str:
		"""
		Returns the data
		:return: data
		"""
		return self.data

	def solve(self, source: Any) -> None:
		"""
		Solves the problem
		:return: None
		"""
		self.readData(source)
		print(self.findAnswer())
		#sys.stdout.write('1')

if __name__ == "__main__":
		sol = Solution()
		sol.solve(sys.stdin)
