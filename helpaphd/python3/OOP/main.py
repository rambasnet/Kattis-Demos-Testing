from __future__ import annotations

__author__ = "Ram Basnet"
__date__ = "2023/1/1"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Ram Basnet"

"""
Solution class
"""

import sys
from typing import List, Any, Union
from add import Add


class Solution(object):
	"""
	Solution class
	"""
	def __init__(self, source:Any) -> None:
		"""
		Constructor
		"""
		self.n = 0
		self.data:List[List[Any]] = []
		self.readData(source)
		self.ans: List[str] = []
		self.findSolution()


	def readData(self, source:Any) -> None:
		"""
		Reads the data
		:return: None
		"""
		data = source.read().splitlines()
		self.n = int(data[0])
		for i in range(1, len(data)):
			try:
				a, b = data[i].split('+')
				eq = [int(a), '+', int(b)]
			except:
				a, b = data[i].split('=')
				eq = [a, '=', b]
			self.data.append(eq)


	def getData(self) -> List[List[str]]:
		"""
		Returns the data
		:return: data
		"""
		return self.data


	def findSolution(self) -> None:
		"""
		Solves the problem
		:param source: data source object: sys.stdin or file object
		:return: None
		"""
		#print(self.data)
		self.ans = []
		for d in self.data:
			eq = Add(d[0], d[2])
			self.ans.append(eq.add())
		self.ans.append('')


	def getAnswer(self) -> List[str]:
		"""
		Returns the answer
		:return: answer
		"""
		return self.ans


	def solve(self) -> None:
		"""
		Solves the problem
		:return: None
		"""
		sys.stdout.write('\n'.join(self.ans))


if __name__ == '__main__':
	import sys
	solution = Solution(sys.stdin)
	#print(solution.getData())
	solution.solve()
		
	