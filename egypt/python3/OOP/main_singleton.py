import sys
from typing import Any, List
from triangle import Triangle

class Solution:
	_data: List[List[int]] = []
	_triangles: List[Triangle] = []
	_answer : List[str] = []

	@staticmethod
	def read_data(input_source: Any) -> None:
		"""
		Reads the data from the given source
		:return: None
		"""
		data = input_source.readlines()
		# ignore the last line: 0, 0, 0
		Solution._data = [list(map(int, data[i].split())) for i in range(len(data)-1)]
		for a, b, c in Solution._data:
			Solution._triangles.append(Triangle(a, b, c))
		#print(self._triangles)

	@staticmethod
	def data() -> List[List[int]]:
		"""
		Returns the data
		:return: data
		"""
		return Solution._data

	@staticmethod
	def answer() -> str:
		"""
		Returns the answer
		:return: answer
		"""
		return '\n'.join([str(t) for t in Solution._answer])

	@staticmethod
	def solve() -> None:
		"""
		Solves the problem
		:return: None
		"""
		for t in Solution._triangles:
			Solution._answer.append('right' if t.is_right_angled() else 'wrong')

		Solution._answer.append('')

	@staticmethod
	def print_answer() -> None:
		"""
		Prints the answer
		:return: None
		"""
		sys.stdout.write(Solution.answer())

if __name__ == '__main__':
	Solution.read_data(sys.stdin)
	Solution.solve()
	Solution.print_answer()
	#can't prevent to do the following
	#b = Solution()
	#b.read_data(sys.stdin)
	#b.solve()
	#b.print_answer()

