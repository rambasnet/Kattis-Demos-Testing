__author__ = "Ram Basnet"
__date__ = "2023/1/1"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Ram Basnet"

"""
Testing Solution class
"""

import unittest
from unittest.mock import patch
from io import StringIO
from main import Main

class TestMain(unittest.TestCase):
	"""
	Testing Singleton Main class
	"""
	def setUp(self) -> None:
		"""
		Setup method
		:return: None
		"""
		# can't call Main() because it's a singleton class
		self.main: Main = Main.get_instance()

	@patch('sys.stdout', new_callable=StringIO)
	def test_solve(self, mock_stdout: StringIO) -> None:
		"""
		Tests solve method
		:return: None
		"""
		self.main.solve()
		self.assertEqual(mock_stdout.getvalue(), 'Hello World!\n')

	def test_get_instance(self) -> None:
		"""
		Tests get_instance method
		:return: None
		"""
		self.main: Main = Main.get_instance()
		self.assertEqual(self.main.get_instance(), self.main)

if __name__ == '__main__':
	unittest.main(verbosity=2)

