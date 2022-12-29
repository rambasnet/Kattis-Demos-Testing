__author__ = "Ram Basnet"
__date__ = "2023/1/1"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Ram Basnet"

"""
Solution class
"""

import sys
from oddity import Oddity
from typing import List, Any

class Solution(object):
	def __init__(self, source:Any):
		"""
		Constructor
		"""
		self.__n: int = 0
		self.__data: List[int] = []
		self.__answer: List[str] = []
		self.readData(source)
		self.findAnswer()

	def readData(self, source:Any) -> None:
		"""
		Reads the data
		:return: None
		"""
		data = sys.stdin.readlines()
		self.__n = int(data[0])
		self.__data = [int(data[i]) for i in range(1, len(data))]
		self.findAnswer()

	def findAnswer(self) -> None:
		"""
		Finds the answer and stores it in self.answer
		:return: None
		"""
		self.__answer = [str(Oddity(n)) for n in self.__data]
		self.__answer.append('') # for the last new line

	def getAnswer(self) -> List[str]:
		"""
		Returns the answer
		:return: answer
		"""
		return self.__answer

	def getN(self) -> int:
		"""
		Returns the number of test cases
		:return: number of test cases
		"""
		return self.__n

	def getData(self) -> List[int]:
		"""
		Returns the data
		:return: data
		"""
		return self.__data

	def solve(self) -> None:
		"""
		Prints the answer
		:return: None
		"""
		sys.stdout.write('\n'.join(self.__answer))

if __name__ == '__main__':
	solution = Solution(sys.stdin)
	solution.solve()

	