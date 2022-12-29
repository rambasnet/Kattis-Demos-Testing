__author__ = "Ram Basnet"
__date__ = "2023/1/1"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Ram Basnet"

from triangle import Triangle
from typing import Any, List
import sys

class Solution(object):
	"""
	Solution class
	"""
	def __init__(self) -> None:
		"""
		Constructor
		"""
		self.__data: List[List[int]] = []
		self.__triangles: List[Triangle] = []

	def readData(self, source:Any) -> None:
		"""
		Reads the data from the given source
		:return: None
		"""
		data = source.readlines()
		# ignore the last line: 0, 0, 0
		self.__data = [list(map(int, data[i].split())) for i in range(len(data)-1)]
		for a, b, c in self.__data:
			self.__triangles.append(Triangle(a, b, c))
		#print(self.__triangles)

	def getData(self) -> List[List[int]]:
		"""
		Returns the data
		:return: data
		"""
		return self.__data

	def answer(self, t:Triangle) -> str:
		"""
		Returns the answer
		:return: answer
		"""
		if t.isRightAngled():
			return 'right'
		else:
			return 'wrong'

	def solve(self, source:Any) -> None:
		"""
		Solves the problem
		:return: None
		"""
		#print('solve called', source)
		self.readData(source)
		answer = []
		for t in self.__triangles:
			answer.append(self.answer(t))

		answer.append('')
		sys.stdout.write('\n'.join(answer))
		
if __name__ == "__main__":
	solution = Solution()
	solution.solve(sys.stdin)
