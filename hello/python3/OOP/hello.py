__author__ = "Ram Basnet"
__date__ = "2023/1/1"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Ram Basnet"

"""
Hello World Program using OOP
"""

class HelloWorld(object):
	"""
	Hello World Class
	"""
	def __init__(self) -> None:
		"""
		Constructor
		"""
		self._message = 'Hello World!'

	def print_message(self) -> None:
		"""
		Prints the message
		"""
		print(self._message)

	def get_message(self) -> str:
		"""
		Returns the message - using getter method

		Returns:
			self._message (str): Message stored in the object
		"""
		return self._message

	@property
	def message(self) -> str:
		"""
		Returns the message - using getter property

		Returns:
			self._message (str): Message stored in the object
		"""
		return self._message

