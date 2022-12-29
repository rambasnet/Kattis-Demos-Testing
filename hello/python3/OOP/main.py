__author__ = "Ram Basnet"
__date__ = "2023/1/1"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Ram Basnet"

from hello import HelloWorld

class Solution(object):
	"""
	Solution class
	"""
	def __init__(self) -> None:
		"""
		Constructor
		"""
		self.hello = HelloWorld()

	def solve(self) -> None:
		"""
		Solves the problem
		:return: None
		"""
		self.hello.printMessage()

if __name__ == '__main__':
	solution = Solution()
	solution.solve()
