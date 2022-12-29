__author__ = "Ram Basnet"
__date__ = "2023/1/1"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Ram Basnet"

"""
Unittesting HelloWorld class
"""

import unittest
from hello import HelloWorld
from unittest.mock import patch
from io import StringIO

class TestHelloWorld(unittest.TestCase):
	"""
	Unittesting HelloWorld class
	"""
	def setUp(self) -> None:
		"""
		Setup method
		:return: None
		"""
		self.hello = HelloWorld()

	@patch('sys.stdout', new_callable=StringIO)
	def test_printMessage(self, mock_stdout: StringIO) -> None:
		"""
		Tests printMessage method
		:return: None
		"""
		self.hello.printMessage()
		self.assertEqual(mock_stdout.getvalue(), 'Hello World!\n')

	def test_getMessage(self) -> None:
		"""
		Tests getMessage method
		:return: None
		"""
		self.assertEqual(self.hello.getMessage(), 'Hello World!')

if __name__ == '__main__':
	unittest.main(verbosity=2)
