__author__ = "Ram Basnet"
__date__ = "2023/1/1"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Ram Basnet"

from hello import HelloWorld
from typing import Optional

class Main(object):
	"""
	Singleton class Main
	"""
	_instance = None

	def __init__(self) -> None:
		"""
		Constructor - uses single pattern
		"""
		if Main._instance:
			raise Exception("Cannot create multiple instances of a singleton class Main")
		self._solution: 'HelloWorld' = HelloWorld()
		Main._instance = self

	def solve(self) -> None:
		"""
		Solves the problem
		:return: None
		"""
		self._solution.print_message()

	@classmethod
	def get_instance(cls) -> 'Main':
		if not cls._instance:
				cls._instance = Main()
		return cls._instance

	@staticmethod
	def main() -> None:
		main = Main()
		main.solve()

def main() -> None:
	main = Main()
	main.solve()

if __name__ == '__main__':
	Main.main()
	#main = Main()
	#main = Main.get_instance()
	#main.solve()
